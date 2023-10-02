from itertools import product

def debruijn(x):
  L = len(x[0])

  #all possible kmers
  kmers = set()
  for y in x:
    for i in range(L-1)
      kmers = x[i:i+2]
      kmers.add(newkmer)

  allkmers = ''.join(x) for x in product(kmers, repeat=L)

  
    
