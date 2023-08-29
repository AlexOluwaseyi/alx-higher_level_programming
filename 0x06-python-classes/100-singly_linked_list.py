#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Get/set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the data of the next Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Get/set the data of the next Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
