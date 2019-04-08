class Tree:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def get_tree(arr):
  if len(arr) is None:
    return None

  if len(arr) == 1:
    return Tree(arr[0])

  mid = int(len(arr)/2)
  
  root = Tree(arr[mid])
  root.left = get_tree(arr[:mid])
  print (arr[:mid], arr[mid], arr[mid+1:])
  if len(arr) == 2:
    return root
  root.right = get_tree(arr[mid+1:])

  return root

def find_smallest_value(tree):
  while tree.left:
      tree = tree.left
  return (tree.val)

def find_largest_value(tree):
  while tree.right:
      tree = tree.right
  return (tree.val)


##################################################################
# This method can solve similar different problems
##################################################################
def _getSmallest(root, holder):
    if not root:
        return
    else:
        _getSmallest(root.left, holder)
        holder.append(root.val)
        _getSmallest(root.right, holder)

def getSmallest(tree):
    holder = []
    _getSmallest(tree, holder)
    print ('Holder: ', holder)
    return holder[0]

sorted_array = [5,6,7,12,23,31,44,56,65,99, 100]
print('Get Smallest:' , getSmallest(get_tree(sorted_array)))
sorted_array = [5,6,7,12,23,31,44,56,65,99, 100]
print('Smallest Value:', find_smallest_value(get_tree(sorted_array)))
print('Largest Value: ' , find_largest_value(get_tree(sorted_array)))

