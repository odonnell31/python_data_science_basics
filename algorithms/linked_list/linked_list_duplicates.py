# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:36:04 2019

@author: 432663
"""

# Question
# Write code to remove duplicates from an unsorted linked list.

def remove_Llist_duplicates(Llist):
    # first, create a blank list to store Linked list values
    LL_elements = []
    
    # now, loop through the Linked list and store value as tuple
    curr_node = LL.head
    while curr_node is not None:
        LL_elements.append(curr_node.data)
        curr_node = curr_node.next
    
    # create blank list for non-duplicates
    final_list = []
    
    # put not duplicate values in final list
    for i in LL_elements:
        if i not in final_list:
            final_list.append(i)
            
    # lastly, create new linked list without duplicates
    nodes = []
    
    node_names = []
    for j in range(len(final_list)):
        node_names.append("Node" + str(j))
    
    for n in range(len(final_list)):
        node_names[n] = Node(final_list[n])
        nodes.append(node_name[n])
        
    new_linked_list = LinkedList()
    new_linked_list.link_nodes(nodes)