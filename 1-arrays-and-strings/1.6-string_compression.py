def compression(S):

  original_length=len(S)
  if original_length==0:
  	return S
  count=1
  code=list()
  code_length=0
  for i in range(0, original_length-1): #O(N)
    if code_length>=original_length:
    	return S
    if S[i]==S[i+1]:
      count+=1
    else:
      code.append(S[i])
      code.append(str(count))
      code_length+=2
      count=1
  code.append(S[-1])
  code.append(str(count))
  return ''.join(code)
  
if __name__=="__main__":
	print(compression("abcddddddddddddddddddddddddacccooottt"))
