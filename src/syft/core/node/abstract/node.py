from typing import Any, List, Optional

from ...common.uid import UID
from ...io.address import Address
from ...store import ObjectStore
from ...common.message import (
    ImmediateSyftMessageWithoutReply,
    EventualSyftMessageWithoutReply,
    ImmediateSyftMessageWithReply,
)


class AbstractNode(Address):
    name: Optional[str]
    store: ObjectStore
    lib_ast: Any  # Cant import Globals (circular reference)
    """"""

    @property
    def known_child_nodes(self) -> List[Any]:
        raise NotImplementedError

    def recv_eventual_msg_without_reply(
        self, msg: EventualSyftMessageWithoutReply
    ) -> None:
        raise NotImplementedError

    def recv_immediate_msg_without_reply(
        self, msg: ImmediateSyftMessageWithoutReply
    ) -> None:
        raise NotImplementedError

    def recv_immediate_msg_with_reply(
        self, msg: ImmediateSyftMessageWithReply
    ) -> ImmediateSyftMessageWithoutReply:
        raise NotImplementedError

    def get_object(self) -> None:
        raise NotImplementedError

    def has_object(self) -> None:
        raise NotImplementedError

    def store_object(self) -> None:
        raise NotImplementedError

    def delete_object(self) -> None:
        raise NotImplementedError


class AbstractNodeClient(Address):
    lib_ast: Any  # Cant import Globals (circular reference)
    address: Address
    """"""

    @property
    def id(self) -> UID:
        """This client points to an node, this returns the id of that node."""
        raise NotImplementedError

    def send_immediate_msg_without_reply(
        self, msg: ImmediateSyftMessageWithoutReply
    ) -> None:
        raise NotImplementedError