# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:49:58 2019

@author: 432663
"""

# Trees

# A tree is a data structure composed of nodes
    # each node has a root
    # the root node has zero or more child nodes
    # each child node has zero or more child nodes, and so on
    
# A tree cannot:
    # contain cycles
    # The nodes may or may not be a particular order
    # nodes can have any data type as value
    # nodes may or may not be linked back to their parent node
    
# A binary tree:
    # a tree in which each node has up to two children
    # a node is a "leaf" if it has no children
    
# A binary search tree
    # a binary tree in which every node fits a specific ordering property:
        # ex: all left descendants <= n < all right descendants
        
# Balanced trees are not perfectly balanced for each subtree, but not terribly imbalanced
        
# Complete binary tree
    # every level of the tree is fully filled except the last level
        # the last level must be filled left to right if it is filled
        
# Fully binary tree:
    # each node has either 0 or 2 children. No nodes have 1 child.
    
# Perfect binary tree:
    # full and complete. All leaves are at the same level.
    # a perfect tree has 2^k - 1 nodes. k is the number of levels

# =======================

# Binary tree traversal: (in-order, post-order, and pre-order)

# In-Order traversal:
    # visit (and usually print) the left branch, then the current node, finally the right branch
    # on a binary search tree, it visits the nodes in ascending order

# Pre-Order traversal:
    # visits the current node before its child nodes
    # root is always the first node visited

# Post-Order traversal
    # visits the current node after its child nodes
    # root node is always the last node visited
    
# Binary Heaps (Min-Heaps and Max-Heaps):
    # Min-Heap is a complete binary tree (totally filled other than rightmost elements of last level)
        # where each node is smaller than its children
            # thus, the root is the minimum element of the tree
            
        # when we insert a node into a Min-Heap,
            # always insert at the bottom, and the rightmost spot to maintain completeness

# =======================
   
# Tries (Prefix Trees)
    # a n-ary tree in which characters are stored at each node
        # each path down the tree may represent a word
        # The "*" nodes often indicate complete words
    # pro of Trie: quick word prefix lookups, faster than dict

# =======================
    
# Graphs
    # a tree is a type of graph, but not all graphs are trees
    # a tree is a connected graph without cycles
    # A graph is simply a collection of nodes with edges between them
        # graphs can be directed or undirected (1-way or 2-way streets)
        # graphs can consist of multiple isolated subgraphs
        
# Storing a graph:
    # Adjacency List:
        # every node stores a list of adjacent vertices
            # in an undirected graph, each adjacent vertice is stored twice
        # note: you can just create a node class, with a dict of dicts for the nodes
        
# Graph Search:
    # Depth-first search (DFS):
        # start at the root (or any node)
        # and explore each branch completely, then move onto next branch
    # Breadth-first search (BFS):
        # start at the root (or any node)
        # and explore each neighbor before going onto any of their children
# Depth-first is preferred to visit every node. Breadth-first for shortest path
        # NOTE: In both seaches, you must mark each node if it has been visited
    
    