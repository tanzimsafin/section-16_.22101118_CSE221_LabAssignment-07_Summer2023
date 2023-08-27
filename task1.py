#Task_1
with open('input1.txt','r') as f:
  n=int(f.readline())
  time=[]
  for i in range(n):
    a,b=f.readline().split()
    a,b=int(a),int(b)
    time.append((a,b))
  time.sort(key =lambda x:x[1])
def intervals(llist):
  my_selected=[]
  select=llist[0]
  my_selected.append(llist[0])
  for i in range(len(llist)):
    start,end=llist[i]
    if start<select[1]:
      continue
    else:
      my_selected.append(llist[i])
      select=llist[i]
  return my_selected

with open('output1.txt','w') as w:
  y=intervals(time)
  w.write(f'{len(y)}\n')
  for i in y:
    a,b=i
    w.write(f'{a} {b}\n')