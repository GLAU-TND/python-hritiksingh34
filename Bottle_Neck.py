#bottle neck python program
n=int(input("enter number of bottle"))
r= list(map(int,input().split()))
print(max([r.count(i)for i in r]))