class SNode:
    def __init__(self, data, node_next=None):
        self.data = data
        self.next = node_next


class SingleChainTable:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, data_or_node):
        if isinstance(data_or_node, SNode):
            item = data_or_node
        else:
            item = SNode(data_or_node)
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    def insert(self, index, data_or_node):
        if index >= self.length or index < 0:
            raise IndexError('index not right')
        if isinstance(data_or_node, SNode):
            item = data_or_node
        else:
            item = SNode(data_or_node)
        j = 0
        if index == 0:
            self.head = item
        else:
            node = self.head
            while j < index and node:
                j += 1
                node = node.next

            item.next = node.next
            node.next = item

    def printd(self):
        if not self.is_empty():
            node = self.head

            while node:
                print(node.data)
                node = node.next
        else:
            print('chain is empty')

    def __len__(self):
        return self.length


s = SingleChainTable()
for i in range(10):
    s.append(i)
s.insert(8, 'xys')
s.printd()
