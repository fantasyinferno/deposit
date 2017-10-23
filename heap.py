def printBinaryTree(treeArray, idx=0):
  if idx >= len(treeArray):
    return
  printBinaryTree(treeArray, 2 * idx + 1)
  print('{0}'.format(treeArray[idx]))
  printBinaryTree(treeArray, 2 * idx + 2)
def breadFirstTraversal(treeArray):
  queue = []
  currentIdx = 0
  while (currentIdx != -1):
    print('{0}'.format(treeArray[currentIdx]))
    left = 2 * currentIdx + 1
    right = 2 * currentIdx + 2
    if (left < len(treeArray)):
      queue.append(left)
    if (right < len(treeArray)):
      queue.append(right)
    if (len(queue) != 0):
      currentIdx = queue[0]
      queue = queue[1:]
    else:
      currentIdx = -1
class MaxHeap:
  heap = []
  def __init__(self, heapArray):
    # sort if not already sorted
    self.heap = sorted(heapArray)
    self.buildHeap()
  def reheapUp(self, node):
    parent = (node - 1) // 2
    while (node > 0) and (self.heap[node] > self.heap[parent]):
      self.heap[parent], self.heap[node] = self.heap[node], self.heap[parent]
      node = parent
      parent = (node - 1) // 2
  def reheapDown(self, node):
    left = node * 2
    right = node * 2 + 1
    while left < len(self.heap) and (self.heap[node] < self.heap[left] or self.heap[node] < self.heap[right]):

      if self.heap[left] > self.heap[right]:
        self.heap[left], self.heap[node] = self.heap[node], self.heap[left]
        node = left
      else:
        self.heap[right], self.heap[node] = self.heap[node], self.heap[right]
        node = right
      left = node * 2
      right = node * 2 + 1
  def buildHeap(self):
    for idx, val in enumerate(self.heap):
      self.reheapUp(idx)


heap = MaxHeap([8, 19, 23, 32, 45, 56, 78])
print(heap.heap)
breadFirstTraversal(heap.heap)