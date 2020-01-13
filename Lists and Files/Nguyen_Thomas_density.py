#os.chdir(r'/Users/tobeysdw/Downloads')

f = open(r'/Users/tobeysdw/Downloads/density.txt')

content = f.read()

nums = f.readlines()
nums = [int(i) for i in nums]

print(nums[1])

#print(content)

