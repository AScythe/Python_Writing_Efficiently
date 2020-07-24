# acc = 0.0

# for k in range(10000):
#     acc = acc + pow(-1, k)/(2*k+1)

# acc = 4 * acc

# print("pi:", acc)

# use generator expression
x = 4*sum(pow(-1, k)/(2*k+1) for k in range(10000))
# sum built in function to add sequence of numbers
print("pi:", x)
# this has only 2 lines of codes
# it reads like it runs


# tip - ctrl + [ (or ]) - add or remove indentation
