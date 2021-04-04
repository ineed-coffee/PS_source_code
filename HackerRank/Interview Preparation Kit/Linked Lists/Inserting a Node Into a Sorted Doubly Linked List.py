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

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    tmp = DoublyLinkedListNode(data)
    if not head:
        return tmp
    
    ptr=head
    while ptr:
        if ptr.data>data:
            prv=ptr.prev
            tmp.next=ptr
            ptr.prev=tmp
            if prv:
                prv.next=tmp
                tmp.prev=prv
            flag=True
            break
        else:
            if ptr.next:
                ptr=ptr.next
            else:
                ptr.next=tmp
                tmp.prev=ptr
                break
    while head.prev:
        head=head.prev
    return head

if __name__ == '__main__':
