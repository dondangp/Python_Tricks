# Using a filter 
nums = [1,2,3,4,5,6,7,8,9,10]

# Run and append values based on filter's conditions
my_list = filter(lambda x: x%2==0, nums)

print(my_list)
