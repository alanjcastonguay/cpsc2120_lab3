https://people.cs.clemson.edu/~goddard/handouts/cpsc2120/LABS/lab3.html seeks to teach recursion in C++, and recommends a flood-fill strategy to find contiguous groups of X characters in a field.

This repo contains a python solution (swapping in python naming conventions and dropping the Class requirement). Done as an exercise while watching someone work through the problem.

A stack-based flood implemementation consumes one stack frame for each step away from the starting position (unless tail-call recursion can help here).
This repo contains a deque-based flood implementation that trades one stack-frame per layer for one queue-item per flood-head.
