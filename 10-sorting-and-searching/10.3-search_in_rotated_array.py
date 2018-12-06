def search_rotated(A, start, end,n): #O(logN)
  
  if end<start:
    return False
  mid=(start+end)//2
  #print(A[start],A[mid], A[end])
  if A[mid]==n or A[start]==n:
    return True
  if A[start]>A[mid]:
    if A[mid]<n and n<A[start]:
      return search_rotated(A, mid+1, end, n)
    else:
      return search_rotated(A, start+1, mid-1, n)
  elif A[start]<n and n<A[mid]:
    return search_rotated(A, start+1, mid-1, n)
  else:
    return search_rotated(A, mid+1, end, n)

if __name__=="__main__":
  A=[55, 60, 65, 70, 75, 80, 85, 90, 91, 100, 0, 20, 25, 30, 35, 40, 45]
  print(search_rotated(A,0,len(A)-1,70))
