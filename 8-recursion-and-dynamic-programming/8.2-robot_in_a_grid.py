class Node:
  def __init__(self, value, right=None, bottom=None):
    self.value=value
    self.right=right
    self.left=bottom  
    
all_paths=list()
def path(grid, r, c):  
  for row in grid:
    print(row)
  start=Node((0,0))
  form_tree(grid, start,r, c)
  first_path=list()
  for path in all_paths:
    first_path.append(path)
    if path==(r-1,c-1):      
      break
  return first_path

def form_tree(grid, root, r ,c): #O(rc)
    i,j=root.value
    all_paths.append(root.value)
    if j+1>c-1 and i+1<=r-1:
      if grid[i+1][j]==0:
        print("Go bottom only")
        root.left=Node((i+1,j))
        form_tree(grid,root.left,r,c)
      if grid[i+1][j]==1:
        print("reverse")
        all_paths.pop()
        grid[i][j]=1

    elif j+1<=c-1 and i+1>r-1:
      if grid[i][j+1]==0:
        print("Go right only")
        root.right=Node((i,j+1))
        form_tree(grid,root.right,r,c)
      if grid[i][j+1]==1:
        print("reverse")
        all_paths.pop()
        grid[i][j]=1   

    elif j+1<=c-1 and i+1<=r-1:
      if grid[i+1][j]==0:
        print("Go bottom")
        root.left=Node((i+1,j))
        form_tree(grid,root.left,r,c)      
      if grid[i][j+1]==0:
        print("Go right")
        root.right=Node((i,j+1))
        form_tree(grid,root.right,r,c)      
      if grid[i+1][j]==grid[i][j+1]==1:
        print("reverse")
        all_paths.pop()
        grid[i][j]=1


grid = [[0, 0, 0, 0, 0, 0, 0],[0, 1, 1, 0, 1, 1, 0],[0, 0, 1, 0, 0, 0, 0],[1, 1, 0, 0, 0, 1, 0]]
print(path(grid, len(grid), len(grid[0])))    
