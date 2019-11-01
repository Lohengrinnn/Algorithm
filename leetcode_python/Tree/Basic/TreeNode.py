from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def width(tn: TreeNode):
    w = 1
    if tn.left:
        w += width(tn.left) - 1
    if tn.right:
        w += width(tn.right)
    return w


def treeToString(tn: TreeNode):
    res = ''
    if not tn:
        return res
    tn.pos = 0
    l: List[TreeNode] = [tn]
    while l:
        next_l: List[TreeNode] = list()
        p = 0
        while l:
            n = l.pop(0)
            res += ' ' * 5 * (n.pos - p)
            p = n.pos
            lw, rw = 1, 0
            if n.left:
                lw = width(n.left)
                next_l.append(n.left)
                n.left.pos = p
            p += lw
            if n.right:
                rw = width(n.right)
                next_l.append(n.right)
                n.right.pos = p
            p += rw
            res += '%5d' % n.val + ' ' * 5 * (rw + lw - 1)
        res += '\n'
        l = next_l
    return res


#print(treeToString(stringToTreeNode('[1,2,3,null,4,5,null]')))
#print(treeToString(stringToTreeNode('[3, 0, 5, -1, 1, 4, 6]')))
