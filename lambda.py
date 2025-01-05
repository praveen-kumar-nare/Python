a=[1,2,3,4,5]
res=map(lambda num: str(num)+'even' if num %2 == 0 else str(num)+'odd',a) 
print(list(res))