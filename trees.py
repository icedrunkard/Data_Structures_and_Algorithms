# coding=utf-8

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({},)'.format(self.root)


node = Node(1, Node(2, Node(4, Node(6), Node(7)), Node(5)), Node(3))


class Tranversor():

    def pre_r_tranverse(self, node):
        if node:
            print(node.root, end='_')
            self.pre_r_tranverse(node.left)
            self.pre_r_tranverse(node.right)
        return

    def pre_l_tranverse(self, node):
        mystack = []
        while mystack or node:
            while node:
                print(node.root, end='~')
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            node = node.right

    def mid_l_tranverse(self, node):
        mystack = []
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left
            node = mystack.pop()  # 上一步的node.left==None
            print(node.root, end='~')
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

    def postorder_from_pre_mid(self,pre, mid):
        if len(mid) <= 1:
            return mid
        else:
            return self.postorder_from_pre_mid(pre[1:mid.index(pre[0]) + 1], mid[:mid.index(pre[0])]) \
                   + self.postorder_from_pre_mid(pre[mid.index(pre[0]) + 1:], mid[mid.index(pre[0]) + 1:]) + pre[:1]

# pre = [1, 2, 3]
# mid = [2, 1, 3]
# res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]
# t=Tranversor()
# t.pre_r_tranverse(node)
# t.level_tranverse(node)
class AVLNode(Node):
    def __init__(self,value):
        Node.__init__(self,value)
        self.bf=0

class AVLTree:
    def __init__(self):
        self.root=None

    def insert(self,data_or_node):
        if isinstance(data_or_node,AVLNode):
            node=data_or_node
        elif isinstance(data_or_node,int):
            node=AVLNode(data_or_node)
        else:
            raise TypeError('wrong data type, please input Type "integer" or "Node"...')

        # 此树为空时
        if not self.root:
            self.root=node
            return
        o=self.root
        while o:
            if node.value<o.value:
                if not o.left:
                    o.left=node
                    o.bf=1
                    return
                else:
                    o=o.left
            else:
                if not o.right:
                    o.right = node
                    o.bf = -1
                    return
                else:
                    o = o.right






