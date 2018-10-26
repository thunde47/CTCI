def insertion(n,m,i,j):

  print(n,bin(n))
  print(m,bin(m))
  p1=n&((1<<(j+1))-1) #clear bits from j+1 to most significant bits
  p2=p1&(-1<<i) #clear bits from 0 to i-1 th position
  p3=n&~p2 #Set bits from j to i to 0
  result=p3|(m<<i) #Insert m into cleared n
  print(p1,bin(p1))
  print(p2, bin(p2))
  print(p3, bin(p3))
  print(result, bin(result))
  return result

result=insertion(2003,19,2,6)
