#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    
    fptr=head
    bptr=None
    if not head:
        return bptr
    
    while fptr:
        if not bptr:
            bptr=DoublyLinkedListNode(fptr.data)
        else:
            bptr.prev=DoublyLinkedListNode(fptr.data)
            bptr.prev.next=bptr
            bptr=bptr.prev
        tmp=fptr.next
        del fptr
        fptr=tmp
    return bptr
        

if __name__ == '__main__':
