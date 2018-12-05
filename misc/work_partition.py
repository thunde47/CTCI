def partition(boards, k): #O(N)
  if k>len(boards) or k==0:
    return None
  
  total_work=0
  for length in boards:
    total_work+=length
  ideal_work=total_work/k
  actual_work=0
  i=0
  max_work=-1
  while i<len(boards): 

    if actual_work<ideal_work:
      actual_work+=boards[i]
    if i==len(boards)-1:
      max_work=max(max_work, actual_work)
    if (i+1)<len(boards) and actual_work+boards[i+1]>ideal_work:
      if (actual_work+boards[i+1]-ideal_work)<(ideal_work-actual_work):
        actual_work+=boards[i+1]
        i+=1
      max_work=max(max_work, actual_work)
      actual_work=0    
    i+=1
  
  #print(work)
  return max_work
          

A=[1,2,3,4,5,6,7,8,9]
for worker in range(1,len(A)):
  print("worker={}, time={}".format(worker, partition(A, worker)))
			
