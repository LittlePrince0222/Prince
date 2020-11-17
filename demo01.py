print("Hello World!!")

import copy

# 原二维列表["a",["bb","cc"],["dd",["eee","fff"]]]
list = ["a", ["bb", "cc"], ["dd", ["eee", "fff"]]]

# 直接赋值会改变第一层
list01 = list
list01[0] = 1

print("原列表")
print(list)
# 第二层
list01 = list
list01[1][0] = 1

print("原列表")
print(list)
# 第三层
list01 = list
list01[2][1][0] = 1

print("原列表")
print(list)

"""
    浅拷贝
"""

list = ["a", ["bb", "cc"], ["dd", ["eee", "fff"]]]

list01 = list.copy()

list[0] = "asdf"
print(list01)

list01[0] = 1

print("浅原列表")
print(list)
print(list01)
# 第二层
list01[1][0] = 1

print("原列表")
print(list)
# 第三层
list01[2][1][0] = 1

print("原列表")
print(list)

