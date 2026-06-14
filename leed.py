# nums=[1,1,3]
# ly=nums
# ls=[]
# a=None
# for i in ly:
#     if a==i:
#         pass
#     else:
#         ls.append(i)
#         a=i
# print(ls)
# print(len(ls))
nums=[1,1,3]
ls=[]
a=None
for i in nums:
    if a!=i:
        ls.append(i)
        a=i
for i in range(len(ls)):
    nums[i]=ls[i]
print(nums)
print(len(ls))