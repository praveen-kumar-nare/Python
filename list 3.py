class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def findHighestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(77)
node2 = Node(11)
node3 = Node(34)
node4 = Node(21)
node5 = Node(59)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findHighestValue(node1))
