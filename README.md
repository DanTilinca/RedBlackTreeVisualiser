# RedBlackTreeVisualiser

### Student: Tilincă Dan-Cristian

## Introduction
This project is a visualizer for Red-Black Trees (RBTree), implemented in Python. Red-Black Trees are a kind of self-balancing binary search tree, a data structure used in computer science, typically used to implement associative arrays. Each node of the tree has an extra bit for denoting the color of the node, either red or black. A red-black tree satisfies the following red-black properties:
1. Each node is either red or black.
2. The root is black.
3. All leaves (NIL nodes) are black.
4. If a red node has children then, both its children are black.
5. Every path from a given node to any of its descendant NIL nodes goes through the same number of black nodes.

These properties ensure the tree remains balanced during insertions and deletions.

## Description
This project is an implementation of the Red-Black Tree data structure in Python, with a visualization component using Tkinter. The Red-Black Tree is a self-balancing binary search tree that ensures the height of the tree remains proportional to the logarithm of the number of elements, thus guaranteeing efficient search, insertion, and deletion operations.

## Objectives
The purpose of this project is to provide a clear and interactive visual representation of the structure and operations of the Red-Black Tree, thus facilitating understanding and analysis of the tree's behavior in various scenarios. Specific objectives include:

* Correct implementation of the Red-Black Tree data structure.
* Providing a graphical interface for visualizing the tree and the operations performed on it.
* Ensuring a well-documented and easy-to-understand source code.

## Data Structures Used
The project utilizes the following data structures and concepts:

* The Node class, representing the tree nodes, with properties for value, color, and references to parent and children (left and right).
* The RBTree class, which implements the Red-Black Tree structure, with methods for insertion, deletion, and balancing.
* Using Tkinter for the graphical visualization of the tree.

## Features/Usage Examples/Tests/Benchmark
The project includes the following features:

* Insertion and deletion of elements in/from the Red-Black Tree.
* Graphical visualization of the tree after each operation, highlighting the structure and balancing of the tree.
* Tests to verify the correctness of the tree operations.

### Resources
* Python Documentation for Tkinter: https://docs.python.org/3/library/tk.html
* GeeksforGeeks: https://www.geeksforgeeks.org/introduction-to-red-black-tree/
* Python Documentation: https://docs.python.org/3/
* Stack Overflow: https://stackoverflow.com/
