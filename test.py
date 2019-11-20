import numpy as np

f = open('input.txt')
data = f.read().split()
f.close()
arr = np.zeros(1)
n = 0
for line in data:
    data1 = line.split(':')
    arr1 = np.array(data1)
    arr = np.hstack([arr,arr1])
    n +=1
m = int(arr[-1])
arr = np.delete(arr, 0)
arr = np.delete(arr, -1)
arr = arr.reshape(n-1,2)
arr2 = np.argsort(arr[:,0],axis=0)

s = ''
count = 0
for i in arr2:
    if m % int(arr[i,0]) == 0:
        s = s + arr[i,1]
        count+=1

if count==0:
    print(m)
else:
    print(s)
