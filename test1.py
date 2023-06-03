list= "100;200;300"
nums = [int(x) for x in list.split(';')] 
a= sum(nums)
print(a)