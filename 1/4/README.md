# Heap based improvement to Agglomerative Clustering to achieve better performance

The default implementation of Hierarchical(Agglomerative) clustering in `sklearn` already implements such a heap based improvement.

What this does is makes use of the existing codebase from `sklearn`

Monkey-patches the heappop, heappush, and heappushpop functions from `heapq` package in Python to print the status of the heap at each step.
