# 1) Repeat a tuple three times using * operator
t = (1, 2, 3)
print("1)", t * 3)


# 2) Join three tuples into one using + operator
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

new_tuple = t1 + t2 + t3
print("2)", new_tuple)


# 3) Check whether an element exists in tuple
t = (10, 20, 30, 40)
element = 30

if element in t:
    print("3) Element exists")
else:
    print("3) Element does not exist")


# 4) Find total, highest and lowest without sum(), max(), min()
nums = (12, 45, 8, 67, 23)

total = 0
highest = nums[0]
lowest = nums[0]

for i in nums:
    total += i

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

print("4) Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)


# 5) Filter tuple and keep values greater than 10
n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = tuple(i for i in n if i > 10)

print("5)", filtered)


# 6) Count elements in set without len()
s = {"cat", "dog", "bird", "fish"}

count = 0
for i in s:
    count += 1

print("6) Number of elements =", count)


# 7) Combine two sets into one
set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1 | set2

print("7)", combined)


# 8) Find common elements in two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1 & s2

print("8)", common)


# 9) Find elements in either set but not both
unique = s1 ^ s2

print("9)", unique)