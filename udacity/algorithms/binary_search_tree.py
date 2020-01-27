class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Time complexity O(log(n)). Space complexity O(n log(n))
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        node = self.root
        self.insert_new_node(node, new_val)

    def insert_new_node(self, start, val):
        if start.value > val:
            if start.left:
                self.insert_new_node(start.left, val)
            else:
                start.left = Node(val)
        else:
            if start.right:
                self.insert_new_node(start.right, val)
            else:
                start.right = Node(val)

    def search(self, find_val):
        return self.search_node(self.root, find_val)

    def search_node(self, start, val):
        if start:
            if start.value == val:
                return True
            elif start.value < val:
                return self.search_node(start.right, val)
            else:
                return self.search_node(start.left, val)
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(3)


# Check search
# Should be True

#print(tree.search(4))
# Should be False
print(tree.search(0))