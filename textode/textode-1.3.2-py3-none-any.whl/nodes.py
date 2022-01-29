from typing import Callable, Dict, List, Optional


class Node:
    """Base class of all nodes.

    All subclasses must have this two attributes:
    - `title`: title that will appear at keyboard.
    - `text`: text that will be send after clicking at keyboard button.
    """

    title: str
    text: str


class KeyboardNode(Node):
    """Keyboard node.

    This node is created for sending keyboard with its own buttons nodes.
    """

    _parent: Optional["KeyboardNode"] = None

    def __init__(self, title: str, text: str, buttons: List[Node]):
        self.title = title
        self.text = text

        if not buttons:
            raise ValueError("KeyboardNode must contain at least one button")

        self.buttons = buttons
        self._set_as_parent_to_buttons()

        NodeDict._register_node(self)

    def _set_as_parent_to_buttons(self):
        """Set parent to childs buttons.

        This required by BackNode to be able to get any level height parent.
        """
        for child in self.buttons:
            child._parent = self

    def get_child(self, node_title: str) -> Optional[Node]:
        """Get child by its title.

        Not recommended for use, but will help if
        you have non-unique title nodes.
        """
        for child in self.buttons:
            if child.title == node_title:
                return child
        return None


class TextNode(Node):
    """Text node.

    Default node that contains text that will be sent to the user.
    """

    def __init__(self, title: str, text: str):
        self.title = title
        self.text = text

        NodeDict._register_node(self)


class FillerNode(TextNode):
    """Filler node.

    This node has the same text and title and behaves like a TextNode.
    The only purpose of FillerNode is prototyping.
    """

    def __init__(self, title: str):
        super().__init__(title=title, text=title)


class FuncNode(Node):
    """Function node.

    This node behaves like a TextNode
    but `text` property generated by given func.
    """

    def __init__(self, title: str, text_func: Callable[[], str]):
        self.title = title
        self.text_func = text_func

        NodeDict._register_node(self)

    @property
    def text(self):
        return self.text_func()


class BackNode(Node):
    """Back node.

    This node returns user back in node hierarchy.
    """

    _parent: KeyboardNode

    def __init__(self, title: str, text: str, level: int):
        self.title = title
        self.text = text
        self._level = level

        NodeDict._register_node(self)

    def get_node_to_back(self) -> KeyboardNode:
        """Get "user returns to" node."""
        node = self._parent
        level = self._level
        while level:
            level -= 1
            if node._parent is None:
                return node
            node = node._parent
        return node


class ImageNode(Node):
    """Image node.

    This node sends user an image.

    If `caption` doesn't provided, you still can pass `node.caption`
    in `message.answer_photo`."""

    def __init__(self, title: str, path: str, caption: Optional[str] = None):
        self.title = title
        self.path = path
        self.caption = caption

        NodeDict._register_node(self)


class MultiNode(Node):
    """Multi node.

    This node represents multiple nodes thats need to be send at one time.

    Note that all children nodes must have the same title as
    its multinode parent.
    """

    def __init__(self, title: str, nodes: List[Node]):
        self.title = title
        self.nodes = nodes

        NodeDict._register_node(self)

    @property
    def _parent(self) -> KeyboardNode:
        """Parent property to override its setting."""

    @_parent.setter
    def _parent(self, parent: KeyboardNode):
        """Set provided parent for children of KeyboardNode type."""
        for node in self.nodes:
            if isinstance(node, KeyboardNode):
                node._parent = parent


class NodeDict:
    """Dictionary with all nodes.

    NodeDict must be used by message handler to get current node
    based on user message text.

    Nodes are contained as dict pair, where key is title
    and value is node itself.

    !! Because of the way how nodes contained, all nodes must have unique title.
    Otherwise, you can use FSM and store current KeyboardNode as parent
    and search by its childs to get correct non-unique title node.
    """

    _instance: Dict[str, Node] = {}

    @classmethod
    def _register_node(cls, node: Node):
        """Add node to all nodes dictionary."""
        cls._instance[node.title] = node

    @classmethod
    def get_node(cls, node_title: str) -> Optional[Node]:
        """Get node by node's title."""
        return cls._instance.get(node_title)
