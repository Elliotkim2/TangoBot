
res = []

def dfs(s,m,st):
  if s > 3 or m > 3:
    return
  if s+m >= 3:
    if st[-3:]=='MMM' or st[-3:]=='SSS':
      return
  if s+m == 6:
    res.append(st)
    return
  dfs(s+1,m,st+'S')
  dfs(s,m+1,st+'M')
dfs(0,0,'')
print(res)
print(len(res))