def c(k):
  a = [[] for _ in range(36)]
  for i,j in k:
    a[i].append(j)
    a[j].append(i)
  print(a)

c([[1, 2], [1, 7], [2, 8], [7, 8], [15, 21], [20, 21]])
c([[14, 15], [14, 20], [27, 28], [27, 33], [28, 34], [33, 34]])