def palindrome(s):
  s=s.lower().replace(' ','')
  d=dict()
  for a in s: #O(N)
    if a in d:
      d[a]+=1
    else:
      d[a]=1
  
  odds=0
  for key in d: #worst O(N)
    if d[key]%2==1:
      odds+=1
    if odds>1:
      return False 
  return True

s="taCttt ca o ooooooioo"
print(palindrome(s))
