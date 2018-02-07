#!/usr/bin/env python

# https://people.cs.clemson.edu/~goddard/handouts/cpsc2120/LABS/lab3.html

from __future__ import print_function
import sys
import copy


def parse(iterable):
    """Given an interable (list, filelike-object) of strings, produce a node-dict with (x,y) tuples as keys."""
    nodes = {}
    for row, line in enumerate(iterable):
        for column, character in enumerate(line.strip()):
            nodes[(row, column)] = {".": False, "X": True}[character]
    return nodes

def flood_fill_deque(row, col, nodes):
    """The deque here is maximum of 5 elements"""
    from collections import deque

    if not nodes[(row, col)]:
        return []

    partial_group = []

    to_review_stack = deque([(row, col, 0)])


    while True:
        try:
            x, y, distance = to_review_stack.popleft()
        except IndexError:
            return partial_group

        try:
            if not isinstance(nodes[(x,y)], bool):
                continue  # already an integer
            if nodes[(x,y)] is False:
                continue  # a wall
        except KeyError as e:
            continue  # off the edge of the map

        partial_group.append((x, y))

        nodes[(x,y)] = distance

        for offset_x, offset_y in [
            (x - 1, y),  # Up
            (x + 1, y),  # Down
            (x, y - 1),  # Left
            (x, y + 1),  # Right
        ]:
            if (offset_x, offset_y) in nodes and nodes[(offset_x, offset_y)] is True:
                to_review_stack.append((offset_x, offset_y, distance + 1))

def flood_fill_recursive(row, col, nodes):
    """
    A recurse flood-fill of True=>None

    Starting at a given row,col in nodes
    if current node is True
      add current node to returned list
      set current node to None
      step UDLR
      recurse 4 times, appending results to a list
      return populated list
    else
      return empty list
    # Step UDLR
    """

    if not nodes[(row, col)]:
        return []

    partial_group = [(row, col)]
    nodes[(row, col)] = None

    for x, y in [
        (row - 1, col),  # Up
        (row + 1, col),  # Down
        (row, col - 1),  # Left
        (row, col + 1),  # Right
    ]:
        try:
            if nodes[(x, y)] is True:
                partial_group.extend(flood_fill_recursive(x, y, nodes))
        except KeyError as e:
            pass  # edge of field

    return partial_group

def groups_with_members(nodes):
    for row, col in nodes:
        group_members = flood_fill_deque(row, col, nodes)
        if group_members:
            yield group_members

def print_groups(nodes):
    n = copy.copy(nodes)
    return "\n".join([
        "Group %d:  %s" % (group_number, " ".join(map(lambda x: "(%d,%d)" % x, members)))
        for group_number, members in enumerate(groups_with_members(n), start=1)
    ]) + "\n\n" + "\n".join(node_field(n))

def node_field(nodes):
    for row in range(len(nodes)):
        output_row = ""
        for column in range(len(nodes)):
            try:
                c = nodes[(row, column)]
                if c is True:
                    c = "X"
                elif c is False:
                    c = "."
                output_row += str(c)[-1]

            except KeyError:
                break
        if output_row == "":
            break
        yield output_row


def main(filename):
    with open(filename) as f:
        nodes = parse(f)

    print("Starting:")
    print("\n".join(node_field(nodes)))

    print(print_groups(nodes))


if __name__ == '__main__':
    main(sys.argv[1])
