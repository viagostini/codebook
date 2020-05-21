![tests](https://github.com/viagostini/codebook/workflows/tests/badge.svg)

# codebook

## Motivation
This is meant to be my personal repository containing reference implementations
for all the different data structures and algorithms that I feel like implementing. Also, I'll be uploading my solutions to coding problems from sources like 
competitive programming websites or the book Elements of Programming Interviews,
for example. Many of these will be classic problems and solutions that are
worthy keeping a reference implementation. 

This is a big work in progress and many algorithms have yet to be added in the
future. The focus is not on making an actual library to be installed and used by
other people or anything overly professional, but rather on having clear and
concise implementations that can serve as reference for anyone interested in
learning these or if someone needs to implement some of these in a project of
their own.

The language of choice is mostly Python because I feel like C++ code can be
a little obfuscated sometimes for people who don't have much familiarity with
it and could prove to be a source of difficulty to some extent. Also, I kinda
want to get more experience with it, so it's a good thing for me too.

## Available Implementations

Disclaimer: All these implementations are subject to change at any time.

**Data Structures**
- [x] [Linked List](python/linked_list.py)
- [x] [Binary Heap (Min-Heap)](python/min_heap.py)

**Searching**
- [x] [Binary Search](python/binary_search.py)

**Strings**
- [x] [Longest Common Substring](python/lcs.py)
- [x] [Exact Pattern Matching (Z-Algorithm)](python/z_algorithm.py) 

**Math**
- [x] [Bit Manipulation Tricks](python/bit_manipulation.py) 
- [x] [Euclides Algorithm for GCD (Normal, Extended) and LCM](python/euclides.py)
- [x] [Modular Inverse](python/mod_inverse.py)
- [x] [Discrete Logarithm](python/discrete_logarithm.py)
- [x] [Fast Exponentiation (Normal, Modular)](python/fast_power.py)
- [x] [Big Integer (not a particularly good implementation, will probably be re-written)](python/big_integer.py)

**Machine Learning (with numpy)**
- [x] [Linear Regression](python/linear_regression.py)

**Graphs** (this section will probably be re-written soon)
- [x] [DFS](python/dfs.py)
- [x] [BFS](python/bfs.py)
- [x] [Connected Components](python/connected_component.py)
- [x] [Dijkstra Shortest Path](python/dijkstra.py)
- [x] [Floyd Warshall All-Pairs Shortest Paths](python/floyd_warshall.py)

**Geometry**
- [x] [Test Convexity](python/polygon.py) 
- [x] [Polygon Area](python/polygon.py)

## Testing
Unit testing for the code in `python/` is made by myself with `pytest` and the
code in `problems/` is tested by each source's respective judges.

The tests should be enough to make sure that everything works as expected but
there may be some missing edge cases, which could potentially make a faulty
implementation pass the tests. I plan to make even better tests somewhere in the
future.