#!/usr/bin/python3
""" A function that checks if all boxes ranging
from 0 to n-1 are open
"""


def canUnlockAll(boxes):
    """ This defines a function calld canUnlock
        @boxes: the list of boxe
    """
    """ Total number of boxes"""
    n = len(boxes)

    """Initialize a list to keep track of visited boxes"""
    visited = [False] * n

    """The first box is unlocked initially"""
    visited[0] = True

    """ Initialize a stack with the first box"""
    stack = [0]

    while stack:
        """Get the current box from the stack """
        current_box = stack.pop()

        """ Iterate through the key in the current box"""
        for key in boxes[current_box]:
            """ If the key leads to an unvisited box"""
            if not visited[key]:
                """ Mark the box as visited"""
                visited[key] = True
                """ Add the box to the stack"""
                stack.append(key)

    """ Check if all boxes have been visited """
    return all(visited)
