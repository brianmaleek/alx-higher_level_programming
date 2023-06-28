#!/usr/bin/python3
"""
Module 100-singly_linked_list
Define class Node (with private data and next_node)
Define class SinglyLinkedList(with private head and public sorted_insert)
"""


class Node:
    """
    class Node definition

    Args:
        data (int): private
        next_node (Node): private

    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """

    def __init__(self, data, next_node):
        """
        initiialize Node object

        Attributes:
            data (int): private
            next_node (Node): private
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter function for data

        Returns:
            data (int): private
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter function for data

        Args:
            value (int): private
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        getter function for next_node

        Returns:
            next_node (Node): private
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter function for next_node

        Args:
            value (Node): private
        """
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition

    Args:
        head (Node): private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):
        """
        initialize SinglyLinkedList object

        Attributes:
            head (Node): private
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        insert node into linked list in ascending order

        Args:
            value (int): private
        """

        new_node = Node(value, None)

        if self.__head is None:
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """
        string representation of SinglyLinkedList object

        Returns:
            string representation of SinglyLinkedList object
        """

        tmp = self.__head

        string = ""

        while tmp is not None:
            string += str(tmp.data)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return (string)
