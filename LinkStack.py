# LinkStack.py by Thomas Nisterenko

class LinkStack:
    class LinkStackNode:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def delete_node(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.last = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return not len(self)

    def push(self, data):
        new_node = LinkStack.LinkStackNode(data)
        if not self.is_empty():
            self.last.next, new_node.prev = new_node, self.last

        self.last = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        popped_node = self.last
        ret_val = popped_node.data
        self.last = self.last.prev
        self.length -= 1
        popped_node.delete_node()
        return ret_val

    def top(self):
        if self.is_empty():
            raise Exception("There is nothing in the stack")
        return self.last.data

    def remove_all(self):
        while not self.is_empty():
            self.pop()
