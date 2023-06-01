#!/usr/bin/python3
""" Task100 """


class Node:
    """ Class documentation """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class documentation """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            crnt = self.__head
            while crnt.next_node is not None and crnt.next_node.data < value:
                crnt = crnt.next_node
            new_node = Node(value, crnt.next_node)
            crnt.next_node = new_node

    def __str__(self):
        values = ""
        current = self.__head
        while current is not None:
            if current != self.__head:
                values += "\n"
            values += str(current.data)
            current = current.next_node
        return values
