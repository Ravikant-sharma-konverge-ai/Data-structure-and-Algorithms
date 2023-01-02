# binary tree exercises

## What is the purpose of defining the functions __str__ and __repr__ within a class? How are the two functions different? Illustrate with some examples using the empty cells below
# Ans: __str__ is genrally for end user to print the in  class statement but __repr__ is for mainly debuging and development purpose as it return the precise values 


## Create the following binary tree using the TreeNode class defined above.

class treenode:
    def __init__(self,key):

        self.key = key
        self.left = None
        self.right = None


tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def tuple_to_tree(tup):

    if isinstance(tup, tuple) and len(tup) == 3:
        node = treenode(tup[1])
        node.left = tuple_to_tree(tup[0])
        node.right = tuple_to_tree(tup[2])

    elif tup == None:
        node = None

    else:
        node = treenode(tup)
    return node   


#print(tuple_to_tree(tree_tuple).right.right.right.key)         


## Exercise: Define a function tree_to_tuple that converts a binary tree into a tuple representing the same tree. 
## E.g. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def tree_to_tuple(node):

    if node.left == None and node.right == None:
        return node.key
    if node.left ==  None and node.right != None:
        tup = (None,node.key,tree_to_tuple(node.right))
        return tup
    if node.left !=  None and node.right == None:
        tup = (tree_to_tuple(node.left),node.key,None) 
        return tup  

    tup = (tree_to_tuple(node.left),node.key,tree_to_tuple(node.right))

    return tup


print(tree_to_tuple(tuple_to_tree(tree_tuple)))

## Exercise: Implement functions for preorder and postorder traversal of a binary tree.

def preorder_traversal(node):

    if node is None:
        return []

    return [node.key]+preorder_traversal(node.left)+preorder_traversal(node.right)

def postorder_traversal(node):

    if node is None:
        return []

    return postorder_traversal(node.left)+postorder_traversal(node.right)+[node.key] 

print(preorder_traversal(tuple_to_tree(((3,2,4),1,(4,2,3)))),postorder_traversal(tuple_to_tree(((3,2,4),1,(4,2,3)))))

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))
print(traverse_in_order(tuple_to_tree(((3,2,4),1,(4,2,3)))))


## QUESTION: Write a function to calculate the height/depth of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

## QUESTION: Write a function to count the number of nodes in a binary tree
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)







def is_bst(node):
    
    if node == None:
        return True, None , None
   
   
    
    bst_l,  bst_r = is_bst(node.left), is_bst(node.right)
    

    if bst_l and bst_r:
        
        if (node.left == None or node.left.key <= node.key) and (node.right == None or node.right.key > node.key):
            
            return True
        else:
            return False
            
    else:
        return False

    



print(is_bst(tuple_to_tree(tree_tuple)))
