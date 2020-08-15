import pydoc
from typing import List, Optional, Type
from typing import Set
from ...decorators import syft_decorator
from ...proto.core.store.store_object_pb2 import StorableObject as StorableObject_PB
from syft.core.common.serde.deserialize import _deserialize
from ..common.uid import UID
from google.protobuf.message import Message
from google.protobuf.reflection import GeneratedProtocolMessageType
from ...util import get_fully_qualified_name
from ..common.storeable_object import AbstractStorableObject
from nacl.signing import VerifyKey


class StorableObject(AbstractStorableObject):
    """
    StorableObject is a wrapper over some Serializable objects, which we want to keep in an
    ObjectStore. The Serializable objects that we want to store have to be backed up in syft-proto
    in the StorableObject protobuffer, where you can find more details on how to add new types to be
    serialized.

    This object is frozen, you cannot change one in place.

    Arguments:
        id (UID): the id at which to store the data.
        data (Serializable): A serializable object.
        description (Optional[str]): An optional string that describes what you are storing. Useful
        when searching.
        tags (Optional[List[str]]): An optional list of strings that are tags used at search.

    Attributes:
        id (UID): the id at which to store the data.
        data (Serializable): A serializable object.
        description (Optional[str]): An optional string that describes what you are storing. Useful
        when searching.
        tags (Optional[List[str]]): An optional list of strings that are tags used at search.

    """

    __slots__ = ["id", "data", "description", "tags"]

    @syft_decorator(typechecking=True)
    def __init__(
        self,
        id: UID,
        data: object,
        description: Optional[str] = "",
        tags: Optional[List[str]] = [],
        read_permissions: Optional[Set[VerifyKey]] = set(),
    ):
        self.id = id
        self.data = data
        self.description = description
        self.tags = tags

        # the set of "verify key" objects corresponding to people
        # who are allowed to call .get() and download this object.
        self.read_permissions = read_permissions

    @syft_decorator(typechecking=True)
    def _object2proto(self) -> StorableObject_PB:

        proto = StorableObject_PB()

        # Step 1: Serialize the id to protobuf and copy into protobuf
        id = self.id.serialize()
        proto.id.CopyFrom(id)

        # # Step 2: save the type of object we're about to serialize
        # proto.schematic_qualname = get_fully_qualified_name(obj=self.data)
        # print("Underlying Object Type:" + str(proto.schematic_qualname))

        # Step 3: Save the type of wrapper to use to deserialize
        proto.obj_type = get_fully_qualified_name(obj=self)

        # Step 4: Serialize data to protobuf and pack into proto
        data = self._data_object2proto()
        proto.data.Pack(data)

        # Step 5: save the description into proto
        proto.description = self.description

        # Step 6: save tags into proto if they exist
        if self.tags is not None:
            for tag in self.tags:
                proto.tags.append(tag)

        return proto

    @staticmethod
    @syft_decorator(typechecking=True)
    def _proto2object(proto: StorableObject_PB) -> object:
        # Step 1: deserialize the ID
        id = _deserialize(blob=proto.id)

        # Step 2: get the type of object we're about to serialize
        # data_type = pydoc.locate(proto.schematic_qualname)
        # # from syft.proto.lib.numpy.tensor_pb2 import TensorProto
        #
        # schematic_type = data_type

        # Step 3: get the type of wrapper to use to deserialize
        obj_type: StorableObject = pydoc.locate(proto.obj_type)  # type: ignore
        target_type = obj_type

        # Step 4: get the protobuf type we deserialize for .data
        schematic_type = obj_type.get_data_protobuf_schema()

        # Step 4: Deserialize data from protobuf
        if schematic_type is not None and callable(schematic_type):
            data = schematic_type()
            descriptor = getattr(schematic_type, "DESCRIPTOR", None)
            if descriptor is not None and proto.data.Is(descriptor):
                proto.data.Unpack(data)
            # if issubclass(type(target_type), Serializable):
            data = target_type._data_proto2object(proto=data)
        else:
            data = None
        # Step 5: get the description from proto
        description = proto.description

        # Step 6: get the tags from proto of they exist
        tags = None
        if proto.tags:
            tags = list(proto.tags)

        return target_type.construct_new_object(
            id=id, data=data, tags=tags, description=description
        )

    def _data_object2proto(self) -> Message:
        return self.data.serialize()  # type: ignore

    @staticmethod
    def _data_proto2object(proto: Message) -> int:
        return _deserialize(blob=proto)

    @staticmethod
    def get_data_protobuf_schema() -> Optional[Type]:
        return None

    @staticmethod
    def construct_new_object(id, data, tags, description):
        return StorableObject(id=id, data=data, description=description, tags=tags)

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        """ Return the type of protobuf object which stores a class of this type

        As a part of serializatoin and deserialization, we need the ability to
        lookup the protobuf object type directly from the object type. This
        static method allows us to do this.

        Importantly, this method is also used to create the reverse lookup ability within
        the metaclass of Serializable. In the metaclass, it calls this method and then
        it takes whatever type is returned from this method and adds an attribute to it
        with the type of this class attached to it. See the MetaSerializable class for details.

        :return: the type of protobuf object which corresponds to this class.
        :rtype: GeneratedProtocolMessageType

        """
        return StorableObject_PB

    def __repr__(self):
        return (
            "<Storable:"
            + self.data.__repr__().replace("\n", "").replace("  ", " ")
            + ">"
        )