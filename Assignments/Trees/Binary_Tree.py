class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printTree(root):
        if root==None:
            return
        print(root.data,end=" ")
        if root.left!=None:
            print('L',root.left.data,end=" ")
        if root.right!=None:
            print('R',root.right.data,end=" ")
        print()
        printTree(root.left)
        printTree(root.right)

btn1=BinaryTreeNode(100)
btn2=BinaryTreeNode(54)
btn3=BinaryTreeNode(150)
btn4=BinaryTreeNode(27)

btn5=BinaryTreeNode(80)
btn6=BinaryTreeNode(125)
btn7=BinaryTreeNode(185)

btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5
btn3.left=btn6
btn3.right=btn7
printTree(btn1)

