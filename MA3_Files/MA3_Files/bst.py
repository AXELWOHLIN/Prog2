""" bst.py

Student: Axel Wohlin
Mail: axelwohlin@gmail.com
Reviewed by: Gustav Fredrikson
Date reviewed: 11/5
"""


from math import log2
from linked_list import LinkedList
import random


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)
    
    def _height(self,r):
        if not r:
            return 0
        else:
            a = self._height(r.right)
            b = self._height(r.left)
            return 1 + max(a,b) 

    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    def get_smallest(self,p,r):
        parent = r
        child = r.left
        if not child:
            a = r.key
            p.right = r.right
            return a
        while child.left:
            parent = child
            child = child.left
        tmp = child.key
        parent.left = None
        return tmp

    def _remove(self, r, k):                      # Compulsory

        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right,k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case
                a = self.get_smallest(r,r.right)
                r.key = a
                # 1Find the smallest key in the right subtree
                # 2Put that key in this node
                # 3Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):   
        if not self.root:
            return '<>'                         # Compulsory
        ans = '<'
        for x in self:
            ans = ans + str(x) + ', '
        ans = ans[:-2] + '>'
        return ans

    def to_list(self):  # Compulsory
        """
        The complexity of this function is dependant on the complexity of the
        BST's iterator (the for loop) and python's append() for lists.
        Since append() has comp O(1) and the iterator is O(log(n) [assuming that the 
        tree is effectively structured] the total
        complexity will be O(n) since append is nested inside the iterator.
        """
        lst = []
        for n in self:
            lst.append(n)
        return lst

    def to_LinkedList(self):                    # Compulsory
        """
        Since the iterator is O(n) and the linkedlist method insert O(n) is nested inside
        the BST's iterator the total complexity will be O(n**2)
        """
        lst = LinkedList()
        for n in self:
            lst.insert(n)
        return lst

    def ipl(self):                                # Compulsory
        if not self.root:
            return 0
        else:
            return self._ipl(self.root,1)
    def _ipl(self,n,d):
        if not n:
            return 0 
        else:
            a = self._ipl(n.left,d+1)
            b = self._ipl(n.right,d+1)
            return d + a + b

def random_tree(n):                               # Useful
    t = BST()
    for k in range(n):
        t.insert(random.random())
    return t

def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    """
    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    print( t.height() )
    print(t)
    print( t.to_list() )
    print( t.to_LinkedList() )
    """
    t = []
    for j in range(1,10):
        t.append(random_tree((2**2)**j))
    
    k = 1
    for _ in t:
        a = _.ipl()/((2**2)**k)
        b = 1.39*log2((2**2)**k)
        print(str(a) + ' Real')
        print(str(b) + ' Expected')
        print('Constant is ' + str( a / b ))
        k += 1

    """
    print( r_v1 )
    print("Height of t1 = " + str(t1.height()))
    print( r_v2, exp_v2)
    print("Height of t2 = " + str(t2.height()))
    print( r_v3, exp_v3)
    print("Height of t3 = " + str(t3.height()))
    print(r_v2/exp_v2)
    print(r_v2/exp_v3)
    """
    """
    #remove leaf
    t.remove(8)
    print(t)

    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    #remove root
    t.remove(4)
    print(t)

    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)

    #remove right and left subtree
    t.remove(6)
    print(t)

    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)

    #remove with only right
    t.remove(1)
    print(t)

    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    
    for x in t:
        print(x)

    #remove only left
    t.insert(2)
    print(t)
    t.remove(3)
    print(t)        
    """

if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes, just iterate through the tree and keep index of how many nodes u went through
2. computing height? No, information is lost when the iterator flattens the tree.
3. contains? Yes, iterate through whole tree and break the for loop when node's data matches key.
4. insert? No
5. remove? No



Results for ipl of random trees
===============================
I made a lot of random trees with increasing size of nodes, then I calculated the avg node height
ipl/n and compared it to the expected node height function given. The results were that as the 
amount of nodes in the trees got bigger and bigger the real avg node height divided by the 
expected node height function approached 1. This is the expected outcome since the O(1) term will become
smaller and smaller part of the total avg node height.

"""
