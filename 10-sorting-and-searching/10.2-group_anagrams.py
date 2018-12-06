import collections
def groupAnagrams(strs): #O(M*N)
  anagrams=collections.defaultdict(list)
  for s in strs: #O(N)
    d=dict()
    for c in s: #O(M)
      if c in d:
        d[c]+=1
      else:
        d[c]=1
    encoded=frozenset(d.items()) #O(M)
    #print(encoded)
    if encoded in anagrams: #O(1)
      anagrams[encoded].append(s)
    else:
      anagrams[encoded]=[s]
  return [val for sublist in anagrams.values() for val in sublist] #O(M*N)

if __name__=="__main__":
  strs=["eat", "tea", "tan", "ate", "nat", "bat", "beat", "bate", "tab"]
  print(groupAnagrams(strs))
