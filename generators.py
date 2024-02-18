# ex1
# def squares(n):
#     for i in range(1, n + 1):
#         yield i**2

# n = int(input())
# for square in squares(n):
#     print(square)


#ex2
# def evens(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# n = int(input())
# for even_num in evens(n):
#     print(even_num)


#ex3
# def nums(n):
#     for i in range(n + 1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i

# n = int(input())
# for num in nums(n):
#     print(num)


#ex4
# import math
# def squares(a, b):
#     for i in range(a, b + 1):
#         i = pow(i, 2)
#         yield i
    
# a = int(input())
# b = int(input())
# for i in squares(a, b):
#     print(i)


#ex5
# def down(n):
#     for i in range(n, -1, -1):
#         yield i

# a = int(input())
# for i in down(a):
#     print(i)
