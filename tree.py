class binaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.nodeData)

tree = binaryTree("Корень")
BranchA = binaryTree("Ветвь А")
BranchB = binaryTree("Ветвь Б")

tree.left = BranchA
tree.right = BranchB

LeafC = binaryTree("Лист C")
LeafD = binaryTree("Лист D")
LeafE = binaryTree("Лист E")
LeafF = binaryTree("Лист F")

BranchA.left = LeafC
BranchA.right = LeafD
BranchB.left = LeafE
BranchB.right = LeafF

def traverse(tree):
    if tree.left != None:
        traverse(tree.left)
    if tree.right != None:
        traverse(tree.right)
    print(tree.nodeData)

traverse(tree)