import queue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class Node:
    """The is a basic node class, consisting of a value, parent, and children."""

    def __init__(self, val='', parent=None, children=None, childIndex=0):
        if children is None:
            self.children = []
        else:
            self.SetChildren(children)

        self.val = val
        self.parent = parent
        self.childIndex = childIndex

    def SetChildren(self, children):
        self.children = children
        for child in self.children:
            child.parent = self

    def __str__(self):
        if type(self.val) is str:
            return self.val
        else:
            return str(self.val)


'''
In the following uninformed search algorithms, the implementation of each algorithm is attempted to be mimicked
as closely as possible to the strict definition/behavior of the search algorithm. In other words, any modifications or
improvements to each algorithm was attempted to be avoided.
'''
def BreadthFirstSearch(startNode, goalNode):
    """
    A Breadth-First Search algorithm.
    Time:     O(b^d)
    Space:    O(b^d)
    Complete: Yes, if the branching factor b is finite.
    Optimal:  Yes, if all path costs are identical.
    """
    node = startNode
    if startNode.val == goalNode.val:
        return startNode

    frontier = queue.Queue()
    frontier.put(node)

    reached = {startNode}

    print(node.val)

    while not frontier.empty():
        node = frontier.get()
        if node.children is not None:
            for child in node.children:
                s = child.val
                print(s)

                if s == goalNode.val:
                    return child

                if not reached.__contains__(s):
                    reached.add(s)
                    frontier.put(child)

    return None


def DepthFirstSearchPQ(startNode, goalNode):
    """
    A Depth-First Search algorithm. Implementation Style 1: PriorityQueue using depth.
    Time:     O(b^m)
    Space:    O(b*m)
    Complete: No, make search infinitely and miss the goal node.
    Optimal:  No, may find a path to the goal that is less than the optimal cost.
    """
    depth = 0
    p = PrioritizedItem(priority=depth, item=startNode)

    frontier = queue.PriorityQueue()
    frontier.put(p)

    while not frontier.empty():
        p = frontier.get()
        print(p.item)

        if p.item.val == goalNode.val:
            return p.item

        if p.item.children is not None:
            for child in p.item.children:
                frontier.put(PrioritizedItem(priority=p.priority - 1, item=child))

    return None


def DepthFirstSearchStack(startNode, goalNode):
    """
    A Depth-First Search algorithm. Implementation Style 2: Stack.
    Time:     O(b^m)
    Space:    O(b*m)
    Complete: No, make search infinitely and miss the goal node.
    Optimal:  No, may find a path to the goal that is less than the optimal cost.
    """
    frontier = queue.LifoQueue()
    frontier.put(startNode)
    pathTaken = [startNode]

    while not frontier.empty():
        node = frontier.get()
        pathTaken.append(node)

        print(node)

        if node.val == goalNode.val:
            return node

        if node.children is not None:
            for child in node.children:
                frontier.put(child)

    return None


def BacktrackingSearch(startNode, goalNode):
    """
    A Backtracking Search algorithm.
    Time:     O(b^m)
    Space:    O(b*m)
    Complete: No, make search infinitely and miss the goal node.
    Optimal:  No, may find a path to the goal that is less than the optimal cost.
    """
    frontier = queue.LifoQueue()
    frontier.put(startNode)

    while not frontier.empty():
        node = frontier.get()
        frontier.put(node)

        if node.val == goalNode.val:
            return node

        if node.children is not None and node.childIndex < node.children.__len__():
            child = node.children[node.childIndex]
            node.childIndex += 1

            print(child)

            frontier.put(child)
        else:
            frontier.get()

    return None


def DepthLimitedSearch(startNode, goalNode, maxDepth):
    frontier = queue.LifoQueue()
    frontier.put(startNode)
    depth = 0

    while not frontier.empty():
        node = frontier.get()
        print(node)

        if node.val == goalNode.val:
            return node

        if node.children is not None and depth < maxDepth:
            for child in node.children:
                frontier.put(child)

            depth += 1

    return None


def IterativeDeepeningSearch(startNode, goalNode):
    depth = 0
    while True:
        result = DepthLimitedSearch(startNode, goalNode, depth)

        if result is not None and result.val == goalNode.val:
            return result

        depth += 1


def BestFirstSearch(startNode, goalNode, pathCost):
    # TODO
    print("Not Implemented")
    # node = startNode
    #
    # frontier = queue.PriorityQueue()
    # reached = {startNode: node}
    #
    # while not frontier.empty():
    #     node = frontier.get()
    #
    #     if (node.val == goalNode.val):
    #
    #
    #     if node.children is not None:
    #         for child in node.children:
    #             s = child.val
    #
    #             if not reached.__contains__(s) or 'path cost':
    #
    #
    # return None


def UniformCostSearch(startNode, goalNode):
    # TODO
    return BestFirstSearch(startNode, goalNode, 'Path Costs')


def BidirectionalSearch():
    # TODO
    print("Not implemented")


'''
Test tree 1
===========

node: children
==============
A: [B, C]
B: [D, E]
C: [F, G]

 picture
==========
    A
 B     C
D E   F G
'''
A = Node(val='A')
B = Node(val='B')
C = Node(val='C')
D = Node(val='D')
E = Node(val='E')
F = Node(val='F')
G = Node(val='G')
H = Node(val='H')
A.children = [B, C]
B.children = [D, E]
C.children = [F, G]

print("Breadth-First Search result (goal is F): ")
answer = BreadthFirstSearch(A, F)

'''
Test tree 2
===========

node: children
==============
A: [B, C, D]
B: [E, F, G]
C: [H, I]
D: [J, K]
E: [L, M]
F: [N]

       picture
=====================
             A
      B      C     D
 E    F G   H I   J K
L M   N
'''
A = Node(val='A')
B = Node(val='B')
C = Node(val='C')
D = Node(val='D')
E = Node(val='E')
F = Node(val='F')
G = Node(val='G')
H = Node(val='H')
I = Node(val='I')
J = Node(val='J')
K = Node(val='K')
L = Node(val='L')
M = Node(val='M')
N = Node(val='N')
O = Node(val='O')
P = Node(val='P')
Q = Node(val='Q')
R = Node(val='R')
A.SetChildren([D, C, B])
B.SetChildren([F, G, E])
C.SetChildren([H, I])
D.SetChildren([J, K])
E.SetChildren([L, M])
F.SetChildren([N])

print("Breadth-First Search result (goal is M): ")
answer = BreadthFirstSearch(A, M)

print('Depth-First with priority-queue on depth, search result (goal is M):')
answer = DepthFirstSearchPQ(A, M)

print('Depth-First with stack, search result (goal is M):')
answer = DepthFirstSearchStack(A, M)

print('Backtracking Search result (goal is M):')
answer = BacktrackingSearch(A, M)

print('Depth-Limited Search result with max depth of 2 (goal is M):')
answer = DepthLimitedSearch(A, M, 2)

print('Notice the previous node was not found within a max-depth of 2.' +
      '\nDepth-Limited Search result with max depth of 3 (goal is M):')
answer = DepthLimitedSearch(A, M, 3)

print('Solution path for the last one: ')
answerPath = queue.LifoQueue()
answerPath.put(answer)
node = answer
while node.parent is not None:
    node = node.parent
    answerPath.put(node)

while not answerPath.empty():
    print(answerPath.get())

print('Iterative-Deepening Search:')
answer = IterativeDeepeningSearch(A, M)

# print('Uniform-Cost Search:')
# answer = UniformCostSearch(A, M)
#
# print('Bi-directional Search:')
# answer = BidirectionalSearch(A, M)
