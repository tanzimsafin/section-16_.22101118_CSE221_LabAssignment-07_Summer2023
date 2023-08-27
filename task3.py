def union(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    if x_root!= y_root:
        if rank[x_root] < rank[y_root]:
            x_root, y_root = x_root, y_root
        parent[y_root] = x_root
        rank[x_root] += rank[y_root]
    return rank[x_root]
def find_root(a):
    if parent[a] == a:
        return a
    parent[a] = find_root(parent[a])  
    return parent[a]
with open('input3.txt','r') as f:
 b=f.readline().strip().split(' ')
 n=int(b[0])
 m=int(b[1])
 parent = {i: i for i in range(n+1)}
 rank = {i: 1 for i in range(n+1)}
 new=[]
 for i in range(m):
    p=f.readline().strip().split(' ')
    q=int(p[0])
    r=int(p[1])
    new.append(union(q,r))
with open('output3.txt','w') as w:
    for i in new:
        w.write(str(i)+'\n',)
