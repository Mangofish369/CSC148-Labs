"""CSC148 Prep 6: Linked Lists

=== CSC148 Winter 2025 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

All of the code from lecture is here, as well as some exercises to work on.
"""
from __future__ import annotations
from typing import Any


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Attributes:
    - item:
        The data stored in this node.
    - next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: _Node | None

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.

    Private Attributes:
    - _first:
        The first node in the linked list, or None if the list is empty.
    """

    ###########################################################################
    # [Part 1] Augmenting our LinkedList and adding to the __init__
    #
    # In this task, we will do 2 things:
    # 1. Add a new *private* attribute to LinkedList which will keep track
    #    of the length. Update this wherever needed (i.e. whenever we
    #    add or remove items from the LinkedList.)
    # 2. Initialize our LinkedList with the items provided, if any.
    #    e.g. LinkedList() should create an empty LinkedList as usual
    #    but LinkedList([1, 2, 3]) should create a LinkedList with
    #    the items 1 -> 2 -> 3
    ###########################################################################
    _first: _Node | None
    _length: int

    def __init__(self, items: list | None = None) -> None:
        """Initialize a new empty linked list containing the given items.
        """
        if items is None or len(items) == 0:
            self._first = None
            self._length = 0
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next
            self._length = len(items)

    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        >>> LinkedList([]).is_empty()
        True
        >>> LinkedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    ###########################################################################
    # [Part 2] Augmenting our LinkedList
    #
    # Following from Part 1: all of these methods change or use our
    # length. Modify them to update the private attribute you created.
    ###########################################################################
    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        >>> lst.insert(100, 2)
        Traceback (most recent call last):
        IndexError

        >>> lst.insert(0, 10)
        >>> str(lst)
        '[10 -> 1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        """

        # Create new node containing the item
        new_node = _Node(item)

        if index == 0:
            new_node.next, self._first = self._first, new_node
            #self._first, new_node.next = new_node, self._first
        else:
            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while not (curr is None or curr_index == index - 1):
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                # Update links to insert new node
                curr.next, new_node.next = new_node, curr.next
            self._length += 1

    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self) or index < 0.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(148)
        Traceback (most recent call last):
        IndexError
        >>> lst.pop(0)
        1
        """
        if index == 0:
            if self._first is not None:
                item, self._first = self._first.item, self._first.next
                self._length -= 1
                return item
        else:            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            if curr is None or curr.next is None:
                raise IndexError
            else:
                # Update link to skip over i-th node
                item, curr.next = curr.next.item, curr.next.next
                self._length -= 1
                return item

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        # Additionally: consider the runtime difference. If we *didn't*
        # have this attribute, how would you implement this method?
        # How would your runtime compare?
        return self._length

    ###########################################################################
    # [Part 3] More LinkedList methods
    #
    # Implement the LinkedList methods below.
    ###########################################################################
    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        >>> lst = LinkedList([1, 2, 1, 3, 2, 1])
        >>> lst.index(1)
        0
        >>> lst.index(3)
        3
        >>> lst.index(148)
        Traceback (most recent call last):
        ValueError
        """
        #create an index tracker
        curr = self._first
        curr_index = 0

        #Parse through the linked list for the item
        while curr is not None:
            if curr.item == item:
                return curr_index
            curr = curr.next
            curr_index += 1

        #If no item found return the error
        raise ValueError

    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this list.

        Raise IndexError if index >= len(self).

        >>> lst = LinkedList([1, 2, 3])
        >>> lst[0] = 100  # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> str(lst)
        '[100 -> 200 -> 300]'
        """
        #Handle edge case of index > linked list
        if index >= self._length:
            raise IndexError
        new_node = _Node(item)
        if index == 0:
            #Handle edge case of changing the first element
            next_node = self._first.next
            new_node.next = next_node
            self._first = new_node
        else:
            #Parse the linked list and keep track of both current and previous element
            curr = self._first.next
            curr_index = 1
            previous_curr = self._first
            while curr is not None:
                if curr_index == index:
                    #Link the node to the linked list
                    previous_curr.next = new_node
                    new_node.next = curr.next
                curr = curr.next
                previous_curr = previous_curr.next
                curr_index += 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # Uncomment to check your work with PythonTA!
    import python_ta
    python_ta.check_all()
