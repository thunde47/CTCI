def change(A,B):
  
  length_a=len(A)
  length_b=len(B)
  diff, large_length, large_str, small_str=(length_a-length_b,length_a,A,B) if length_a>length_b else (length_b-length_a, length_b,B,A)
  if diff>1:
    return False
  once_count=0
  j=0
  for i in range(0, large_length): #O(N)
    if once_count>1:
      return False
    try:
      if large_str[i]!=small_str[j]:
        once_count+=1
        if diff==1:
          j-=1
    except:
      pass
    j+=1    
  return True
  
if __name__=="__main__":
	print(change("pale","ple"))
