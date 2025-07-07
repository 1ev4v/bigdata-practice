# p68 1번
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a+5)


# p68 2번
import numpy as np

a = np.array([12, 21, 35, 48, 5])
print(a[::2])


# p68 3번
import numpy as np

a = np.array([1, 22, 93, 64, 54])
print(a.max())


# p68 4번
import numpy as np

a = np.array([1, 2, 3, 2, 4, 5, 4, 6])
a = np.unique(a)
print(a)


# p68 5번
import numpy as np

a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
c = []

min_len = min(len(a), len(b))

for i in range(min_len):
    c.append(a[i])
    c.append(b[i])

if len(a) > min_len:
    c.extend(a[min_len:])
elif len(b) > min_len:
    c.extend(b[min_len:])

print(c)


# import numpy as np

# a = np.array([21, 31, 58])
# b = np.array([24, 44, 67])
# c = np.empty(len(a) + len(b), a.dtype)
# c[0::2] = a
# c[1::2] = b
# print(c)


# p68 6번
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])

print(a[:-1] + b)