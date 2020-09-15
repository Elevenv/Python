# l = [1,25,43,2,2,5,22]
# print(l.count(2))
# l.reverse()
# print(l)
# new_l = l.copy()
# new_l.append("Fu")
# print(new_l)
# print("Index of 25 ",l.index(25))
# new_l.pop()
# print(new_l)
# l.sort()
# print(l)

# a = 0
# b = 1
# i = int(input())
# print(a,b,end=" ")
# while i>0:
#     c = a+b
#     a = b
#     b = c
#     i-=1
#     print(c,end=" ")

# i = 5
# for j in range(0,i):
#     print(j)
# print("--------------------")
# while i>0:
#     print(i)
#     i-=2

# t = (1,2,5,3)
# print(t.index(3))
# print(min(t))
# print(max(t))

# f = open("first.txt","r+")
# print(f.read())
# f.write("Yeah Its grate")
# f.read()
# f.close()

# with open("first.txt","r+") as f:
#     with open("second.txt","r+") as f1:
#         for i in f:
#             f1.write(i)
# q = open("second.txt","r+")
# print(q.read())

# friut = "banana1"
# print(friut[:3])
# print(friut[3:])
# print(friut[3:3])
# print(friut[:])

# def fact(num):
#     re = 1
#     while num>0:
#         re = re * num
#         num-=1
#     return re
# num = int(input())
# print(fact(num))

# t = ['a','b','c','d','e','f']
# t[1:3] = ['x','y']
# print(t)

# try:
#     a = int(input())
#     b = int(input())
#     c = a/b
#     print(c)
# except Exception as e:
#     print("Exception Raised ",e)
# finally:
#     print("End of execution.")

# class Error(Exception):
#     pass
# class small(Error):
#     pass
# class big(Error):
#     pass
# while True:

#     try:
#         n1 = int(input())
#         n2 = 10 
#         if n1<n2:
#             raise small
#         elif n1>n2:
#             raise big
#         else:
#             print("Correct")
#     except small:
#         print("Small")
#     except big:
#         print("Big")
    
# import try1
# try1.squre(5)

# class Emp:    
#     def read(self):
#         self.name = input("Enter name:")
#         self.sal = int(input("Enter salary:"))
#         self.dep = input("Enter Department:")

#     def show(self):
#         print("Name :",self.name)
#         print("Department: ",self.dep)
#         print("Salary :",self.sal)
# obj = Emp()
# obj.read()
# obj.show()
