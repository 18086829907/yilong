#生成器是一种特殊的迭代器

nums1 = [i *2 for i in range(10)]
print(nums1)

#生成器的创建方式，就是将列表推导式的中括号变成小括号
nums2 = (i *2 for i in range(10))
print(nums2)

for i in nums2:
    print(i)