nums = [1,2,3,4,5,6,7,8,9,10]
res = []
for i in nums:
    res.append(i)

# first x is what you are returning, second is for loop for x in nums
result = [x for x in nums]

# multiply x by itself 
dex = [x*x for x in nums]

print(res)
print(result)
print(dex)
