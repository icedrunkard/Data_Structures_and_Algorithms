# coding=utf-8

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({},)'.format(self.value)


node_0 = Node(1, Node(2, Node(4, Node(6), Node(7)), Node(5)), Node(3))


class Tranversor():

    def pre_r_tranverse(self, node):
        if node:
            print(node.value)
            self.pre_r_tranverse(node.left)
            self.pre_r_tranverse(node.right)
        return

    def pre_l_tranverse(self, node):
        mystack = list()
        while mystack or node:
            while node:
                print(node.root)
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            node = node.right

    def mid_l_tranverse(self, node):
        mystack = list()
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left
            node = mystack.pop()  # 上一步的node.left==None
            print(node.root)
            node = node.right

    def level_tranverse(self, node):
        mystack = [[node]]
        total = [[node]]
        while mystack:
            new = []
            level = mystack.pop()

            for node in level:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)

            if new:
                mystack.append(new)
                total.append(new)
            else:
                break
        print(total)

    def postorder_from_pre_mid(self, pre, mid):
        if len(mid) <= 1:
            return mid
        else:
            return self.postorder_from_pre_mid(pre[1:mid.index(pre[0]) + 1], mid[:mid.index(pre[0])]) \
                   + self.postorder_from_pre_mid(pre[mid.index(pre[0]) + 1:], mid[mid.index(pre[0]) + 1:]) + pre[:1]


# pre = [1, 2, 3]
# mid = [2, 1, 3]
# res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]
# t = Tranversor()
# t.pre_r_tranverse(node_0)
# t.level_tranverse(node_0)
class AVLNode(Node):
    def __init__(self, value):
        Node.__init__(self, value)
        self.bf = 0

    def __str__(self):
        return 'AVLNode(root=[{},bf={}],{},{})'.format(self.value, self.bf, self.left, self.right)


class AVLTree:
    """平衡二叉树"""

    def __init__(self, node=None):
        self.root = node

    def insert(self, data_or_node):
        if isinstance(data_or_node, AVLNode):
            node = data_or_node
        elif isinstance(data_or_node, int):
            node = AVLNode(data_or_node)
        else:
            raise TypeError('wrong data type, please input Type "integer" or "Node"...')

        # 此树为空时
        if not self.root:
            self.root = node
            return
        # 树不为空时
        a = o = self.root
        afather=ofather=None
        # 通过while找到插入的节点
        while o:
            if o.bf != 0:
                afather,a = ofather,o  # a是最小非平衡子树
            ofather = o
            if node.value < o.value:
                o = o.left
            else:
                o = o.right
        # 插入新节点
        if node.value < ofather.value:
            ofather.left = node
        else:
            ofather.right = node

        # 插入新节点之后，需要更改bf值
        if node.value < a.value:
            p = b = a.left
            d = 1
        else:
            p = b = a.right
            d = -1

        while p != node:  # 从a的子节点到新插入的节点的父节点需要调整bf值
            if node.value < p.value:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return
        if d == 1:
            # 需要调整,LL,LR,RR,RL
            if b.bf==1:
                b=AVLTree.LL(a,b)
            else:
                b=AVLTree.LR(a,b)
        else:
            if b.bf==1:
                b=AVLTree.RL(a,b)
            else:
                b=AVLTree.RR(a,b)
        if afather is None:
            self.root=b
        else:
            if afather.left==a:
                afather.left=b
            else:
                afather.right=b

    @staticmethod
    def LL(a,b):
        a.left=b.right
        b.right=a
        a.bf=b.bf=0
        return b

    @staticmethod
    def RR(a,b):
        a.right=b.left
        b.left=a
        a.bf=b.bf=0
        return b
    @staticmethod
    def LR(a,b):
        c=b.right
        a.left=c.right
        b.right=c.left
        c.left=b
        c.right=a
        if c.bf==0:
            a.bf=b.bf=0
        elif c.bf==1:
            b.bf=0
            a.bf=-1
        else:
            b.bf=1
            a.bf=0
        c.bf=0
        return c
    @staticmethod
    def RL(a,b):
        c=b.left
        a.right,b.left=c.left,c.right
        c.left,c.right=a,b
        if c.bf==0:
            a.bf=b.bf=0
        elif c.bf==1:
            a.bf=0
            b.bf=-1
        else:
            a.bf=1
            b.bf=0
        c.bf=0
        return c

    def __str__(self):
        if self.root:
            return 'AVLTree(root=[{},bf={}],{},{})'.format(self.root.value, self.root.bf, self.root.left,
                                                           self.root.right)
        else:
            return 'AVLTree(None,)'


avltree = AVLTree()
for i in [5, 1, 3, 4, 0, -1,2]:
    avltree.insert(i)
print(avltree)
