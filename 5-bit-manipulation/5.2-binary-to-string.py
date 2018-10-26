def bin_to_str(n):
  binary="."

  while n>0:
    if len(binary)-1>=32: #32 bits and a "."
      return "Error"
    double=2*n
    binary+=str(int(double))
    n=double-int(double)
    print(len(binary)-1,double, int(double))
  return binary

print(bin_to_str(.72))
