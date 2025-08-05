def remove_last_node(self):

    if self.head is None:
        return

    curr_node = self.head
    while (curr_node.next != None and curr_node.next.next != None):
        curr_node = curr_node.next

    curr_node.next = None