# coding=utf-8

class Node:
    def __init__(self, root=None, left=None, right=None):
        self.root = root
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


def get_after_deep(pre, mid, a):
    if len(pre) == 1:
        a.append(pre[0])
        return
    if len(pre) == 0:
        return
    root = pre[0]
    root_index = mid.index(root)
    get_after_deep(pre[1:root_index + 1], mid[:root_index], a)
    get_after_deep(pre[root_index + 1:], mid[root_index + 1:], a)
    a.append(root)
    return a


def last_sort(pre, mid):
    if len(mid) <= 1:
        return mid
    else:
        return last_sort(pre[1:mid.index(pre[0]) + 1], mid[:mid.index(pre[0])]) \
               + last_sort(pre[mid.index(pre[0]) + 1:], mid[mid.index(pre[0]) + 1:]) + pre[:1]


pre = [1, 2, 3]
mid = [2, 1, 3]
print(last_sort(pre, mid))

# res = get_after_deep([1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10], [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7], [])
# res = get_after_deep([1,2,3], [2,1,3], [])
# print(res)
# res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]
# t=Tranversor()
# t.pre_r_tranverse(node)
# t.level_tranverse(node)
