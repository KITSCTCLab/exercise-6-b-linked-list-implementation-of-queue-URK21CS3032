class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
   new_node=Node(data)
   new_node.next=self.head
   self.head=new_node

  def pop(self) -> None:
    if self.head != None:
      self.head=self.head.next
  
  def status(self):
    """
    It prints all the elements of stack.
    """
    elements = ''
    current = self.head
    while current != None:
      elements += str(current.data)+"=>"
      current = current.next
    print(elements+"None")

    
# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
