nums = [3,3]
target = 6
n = len(nums)-1 

for i in range(0,n):
    for j in range(n,0,-1):
        if i != j:
            if nums[i]+nums[j] == target:
                print([i,j])
                break
print('Hello GitHub')
