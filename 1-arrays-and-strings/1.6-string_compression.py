def compression(S):
  count=1
  code=list()
  original_length=len(S)
  if original_length==0:
  	return S
  for i in range(0, original_length-1): #O(N)
    
    if S[i]==S[i+1]:
      count+=1
    else:
      code.append(S[i])
      code.append(str(count))
      count=1
  code.append(S[-1])
  code.append(str(count))
  return S if original_length<=len(code) else ''.join(code)
  
if __name__=="__main__":
	print(compression("aaaabbbbbaaaatttttttooopooopooojj"))
