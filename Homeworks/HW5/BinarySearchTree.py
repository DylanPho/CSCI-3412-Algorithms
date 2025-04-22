# Author: OMKAR PATHAK

# This program illustrates an example of Binary Search Tree using Python
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def delete(self, data, root):
        if self is None:
            return None
        if data < self.data:
            self.leftChild = self.leftChild.delete(data, root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data, root)
        else:
            if self.leftChild is None:
                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data, root)
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data, root)
                temp = self.leftChild
                self = None
                return temp
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data, root)
        return self

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            return self.leftChild.find(data) if self.leftChild else False
        else:
            return self.rightChild.find(data) if self.rightChild else False

    def minValueNode(self, node):
        current = node
        while current.leftChild:
            current = current.leftChild
        return current

    def maxValueNode(self, node):
        current = node
        while current.rightChild:
            current = current.rightChild
        return current

    def preorder(self):
        if self:
            print(str(self.data), end=' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end=' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end=' ')

    def get_height(self):
        left_height = self.leftChild.get_height() if self.leftChild else 0
        right_height = self.rightChild.get_height() if self.rightChild else 0
        return 1 + max(left_height, right_height)

    def count_nodes(self):
        left_count = self.leftChild.count_nodes() if self.leftChild else 0
        right_count = self.rightChild.count_nodes() if self.rightChild else 0
        return 1 + left_count + right_count

    # ✅ Generator-based descending order traversal
    def descending_generator(self):
        if self.rightChild:
            yield from self.rightChild.descending_generator()
        yield self.data
        if self.leftChild:
            yield from self.leftChild.descending_generator()


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root:
            return self.root.delete(data, self.root)

    def find(self, data):
        return self.root.find(data) if self.root else False

    def preorder(self):
        print('\nPreorder:')
        if self.root:
            self.root.preorder()

    def inorder(self):
        print('\nInorder:')
        if self.root:
            self.root.inorder()

    def postorder(self):
        print('\nPostorder:')
        if self.root:
            self.root.postorder()

    def get_height(self):
        return self.root.get_height() if self.root else 0

    def count_nodes(self):
        return self.root.count_nodes() if self.root else 0

    def descending_generator(self):
        return self.root.descending_generator() if self.root else iter([])