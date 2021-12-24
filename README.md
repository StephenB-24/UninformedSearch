# Comprehensive Uninformed Search Analysis and Implementation
The main uninformed search algorithms are implemented and discussed in detail. 

This includes Breadth-First Search, Depth-First Search, Backtracking Search, Depth-Limited Search, Iterative-Deepening Search, Uniform-Cost Search, and Bi-directional Search.

<h2>What is Uninformed Search?</h2>

Given a start node in a graph, an uninformed search algorithm will search for a goal node. However, the algorithm is not allowed/capable of determining/predicting how close to the goal it is. The efforts made by the algorithm are not directed by a score, or any similar concept. 

An example of this would be placing a person in a country they know nothing about, and asking them to find a specific city without asking for directions or any other geological information.

# Analysis

<h3>Key</h3>

In the below descriptions:
- b = branching factor
- m = maximum depth of the search tree
- l = depth limit
- d = depth of the shallowest solution 
- m = arbitrarily large search depth of size m (used in cases where we know the solution may not be hit)

<h2>Breadth-First Search</h2>

In Breadth-First Search, the root node is expanded, then each of the successors, then each of those successors, and so on. If Breadth-First Search were performed on a tree, the tree would be traversed one entire level at a time. Because every successor is expanded before moving onto the next node level, the search is complete. As one can imagine, Breadth-First Search is quite the memory hog. Increasing the branching factor or the depth even slightly can result in large increases in the amount of memory used.

What is the time complexity? O(b^d)

What is the space complexity? O(b^d)

Does it always find the optimal-cost solution? Yes, so long as branching factor is finite, and the search space has a solution or is finite. If the search space has a solution, with infinite time and memory, it will be found eventually.

Is it complete - meaning it always finds a solution? Yes, so long as all action costs are identical.

<h2>Depth-First Search</h2>

In Depth-First Search, the deepest node is repeatedly expanded. After each expansion, the child nodes are stored on a stack. If there is an end to the search space, the algorithm repeatedly retracts and re-expands to the next unsearched node. Notice how if there is no end to the search space, Depth-First Search would expand infinitely if it were allowed to do so. Due to this expansion style, a basic Depth-First Search implementation will also get stuck when the search space has cycles. Despite it's drawbacks, Depth-First Search greatly accels over Breadth-First Search in space complexity. Depth-First Search can be pictured as a probe, that expands and retracts to different areas of the search space. Issues of Depth-First Search are addressed and modified in the search algorithms to come.

What is the time complexity? O(b^d)

What is the space complexity? O(b*m)

Does it always find the optimal-cost solution? No, the algorithm will return the first solution path that it finds. This is not necessarily the best one.

Is it complete - meaning it always finds a solution? No, if the graph infinitely expands or has cycles, Depth-First Search can be essentially useless.

<h2>Backtracking Search</h2>



<h2>Depth-Limited Search</h2>



<h2>Iterative-Deepening Search</h2>



<h2>Uniform-Cost Search</h2>



<h2>Bidirectional Search</h2>

