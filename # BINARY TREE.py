# BINARY TREE
## Implement a binary tree using Python, and show its usage with some examples.

class TreeNode:
    def __init__(self,key):

        self.key = key
        self.left = None
        self.right = None


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

print(node0.left.key,node0.right.key)


## Create the following binary tree using the TreeNode class defined above.

tree_tuple = ((1,2,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(((1,2,None), 2, ((None, 3, 4), 5, (6, 7, 8))))    

## Exercise: Define a function tree_to_tuple that converts a binary tree into a tuple representing the same tree. 
## E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))). Hint: Use recursion.

def tree_to_tuple(node):
    pass


## Let's create another helper function to display all the keys in a tree-like structure for easier visualization.

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    


# TREAVERSAL
## Here's an implementation of inorder traversal of a binary tree.

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))    

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

traverse_in_order(tree)


# Height and Size of a Binary Tree

## Write a function to calculate the height/depth of a binary tree

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

tree_height(tree)

## Write a function to count the number of nodes in a binary tree

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

tree_size(tree)

#### As a final step, let's compile all the functions we've written so far as methods withing the TreeNode class itself. 
#### Encapsulation of data and functionality within the same class is a good programming practice.

class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node





tree = TreeNode.parse_tuple(tree_tuple)     

tree.display_keys('  ')

tree.height()

tree.size()

tree.traverse_in_order()

tree.to_tuple()













# Binary Search Tree (BST)

## Write a function to check if a binary tree is a binary search tree (BST).
## Write a function to find the maximum key in a binary tree.
## Write a function to find the minimum key in a binary tree
## Here's a function that covers all of the above:

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key


tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))                                       #(False, 1, 8)

tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))      # (True, 'aakash', 'vishal')



## Storing Key-Value Pairs using BSTs

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

tree = BSTNode(jadhesh.username, jadhesh)

tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)


# Insertion into BST

## Here's a recursive implementation of insert.

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node


tree = insert(None, jadhesh.username, jadhesh)

insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)


# Finding a Node in BST

## We can follow a recursive strategy similar to insertion to find the node with a given key within a BST.

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


node = find(tree, 'hemanth')
print(node.key, node.value)     


# Updating a value in a BST

## We can use find to locate the node to be updated, and simply update it's value.

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))

node = find(tree, 'hemanth')
print(node.value)

# List the nodes
## The nodes can be listed in sorted order by performing an inorder traversal of the BST.

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

list_all(tree)    



