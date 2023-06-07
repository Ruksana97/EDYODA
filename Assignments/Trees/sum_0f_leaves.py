
class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Leaf(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False


# This function return sum of all left leaves in a
# given binary tree
def leftLeavesSum(root):
    # Initialize result
    res = 0

    # Update result if root is not None
    if root is not None:

        # If left of root is None, then add data of
        # left child
        if Leaf(root.left):
            res += root.left.data
        else:
            # Else recur for left child of root
            res += leftLeavesSum(root.left)

        # Recur for right child of root and update res
        res += leftLeavesSum(root.right)
    return res



node1=Node(100)
node2=Node(54)
node3=Node(150)
node4=Node(27)
node5=Node(80)
node6=Node(125)
node7=Node(185)

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6
node3.right=node7

print("Sum of left leaves is", leftLeavesSum(node1))