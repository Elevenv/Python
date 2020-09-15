# t = (1,2,3,1,3)
# count = 0
# l = []
# for i in t:
#     if t.count(i)>1:
#         if len(l)==0:
#             l.append(i)
#         else:
#             for j in l:
#                 if l.count(i)==0:
#                     l.append(i)
# print(l)

# from num2words import num2words
# l = tuple(map(int,input("enter no:").split()))
# for i in l:
#     print(num2words(i),end=" ")

# t = (2,8,34,23,78)
# print("Minimum:",min(t))

# d = {'a':'c2','c':'qwe','d':'cdhs','b':'a'}
# for key1,values in sorted(d.items(),reverse= True,key=lambda i:i[1]):
#     print(key1,values)


# wordlist = open("wordlist.txt", "r").read().split()
# words = open("que.txt", "r").read().split() 

# s = list()

# # loop through scrambled words
# for word in words:
#     # break scrambled word into characters
#     chars = list(word)
#     # loop through comparison list
#     for compare in wordlist:
#         # break compare word into characters
#         compare_chars = list(compare)
#         # make copy of scrambled characters
#         char_list = chars[:]
#         # loop through scrambled word characters
#         for char in chars:
#             # if character not in compare word go to next compare word
#             if not char in compare_chars:
#                 break
#             # if character found remove it (in case character exists more than once)
#             compare_chars.remove(char)
#             char_list.remove(char)
#         # if all compare characters exhausted we *may* have found the word
#         if not compare_chars:
#             # if all scrambled characters are utilized then we have the right word
#             if not char_list:
#                 s.append(compare)
#             else:
#                 s.append('???')
#             break

# # create comma separated list of words
# print(",".join(s))

# answer_file = open("wordlist.txt",mode='r' ,encoding='utf-8')
# que_file = open("que.txt",mode='r')
# for i in que_file:
#     print(i)
#     word_len = len(i)
#     print(word_len)
#     for j in answer_file:
#         if len(i)==len(j):
            

#     break


# class Some:
#     def show(self,intn,charc):
#         if type(intn)== int :
#             self.a = intn
#             self.b = charc
#         else:
#             self.a = charc
#             self.b = intn
#         print("Integer is: ",self.a,"And Character is : ",self.b)

# obj = Some()
# print("First function is :")
# obj.show(2,"c")
# print("Second Function is :")
# obj.show("h",5)        

# class Area:
#     def cal(self,length,width):
#         self.length = length
#         self.width = width
#         area = self.length * self.width
#         print("Area of Reactangle is: ",area)

#     def cal(self,side):
#         self.side = side 
#         area = self.side * self.side
#         print("Area of square is : ",area)

# obj = Area()
# obj.cal(5)
# obj.cal(4,5)

# class Degree:
#     def getDegree(self):
#         print("I got degree.")
# class Undergraduate(Degree):
#     def getDegree(self):
#         print("I am Undergraduate.")
# class PostGraduate(Degree):
#     def getDegree(self):
#         print("I am PostGraduate.")

# d = Degree()
# d.getDegree()
# ug = Undergraduate()
# ug.getDegree()
# pg = PostGraduate()
# pg.getDegree()

# class Employee:

#     # name = "Eleven"
#     # department = "Computer"
#     # salary = 70000
#     def read(self):
#         self.name = str(input("Enter Name:"))
#         self.department = str(input("Enter department:"))
#         self.salary = int(input("Enter salary:"))
# class der(Employee):
#     def show(self):
#         print("Name is : ",self.name)
#         print("Department is : ",self.department)
#         print("salary is : ",self.salary)
# e = der()
# e.read()
# e.show()

# class base:
#     def show(self):
#         print("This is Base class.")
# class base2:
#     def show1(self):
#         print("This is another base class.")
# class derived(base,base2):
#     def show2(self):
#         print("This is Derived class.")
# obj = derived()
# obj.show()
# obj.show1()
# obj.show2()

# class Some(Exception):
#     pass
#     # def check(self,password):
#     #     self.password = password
#     #     pass1 = "Anonymous"
#     #     if pass1 == password:
#     #         print("Welcome Eleven")
# try:
#     password = str(input("Enter password : "))
#     pass1 = "Eleven"
#     if pass1 == password:
#         print("Welcome Eleven")
#     else:
#         raise Some
# except:
#     print("Please Enter Correct Password.")


# msg_number = []
# key_number = []
# key_msg_add = []

# msg_number1 = []
# key_number1 = []
# key_msg_add1 = []
# number_to_alphabet_dict = { 1:'a',2:'b',3:'c',4:'d',5:'e'
#                            ,6:'f',7:'g',8:'h',9:'i',10:'j'
#                            ,11:'k',12:'l',13:'m',14:'n',15:'o'
#                            ,16:'p',17:'q',18:'r',19:'s',20:'t'
#                            ,21:'u',22:'v',23:'w',24:'x',25:'y'
#                            ,26:'z'}

# alphabet_to_number_dict = {  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
#                            , 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10
#                            , 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15
#                            , 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20
#                            , 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25
#                            , 'z': 26}

# msg = str(input("Enter message : "))
# key = str(input("Enter key : "))

# def encryption(msg,key):
#     if len(msg)==len(key):
#         vernam_text = ""
#         for i in msg:
#             msg_number.append(alphabet_to_number_dict[i])      
#         for j in key:
#             key_number.append(alphabet_to_number_dict[j])
#         for k in range(0,len(msg_number)):
#             key_msg_add.append((msg_number[k]+key_number[k])%26)
#         for i in key_msg_add:
#             vernam_text+=number_to_alphabet_dict[i]
#     else:
#         print("Key and Message should be of same length")
#     return vernam_text

# def decryption(msg,key):
#     plain_text = ""
#     for i in msg:
#             msg_number1.append(alphabet_to_number_dict[i])      
#     for j in key:
#         key_number1.append(alphabet_to_number_dict[j])
#     for k in range(0,len(msg_number1)):
#         key_msg_add1.append((msg_number1[k]-key_number1[k]))
#     for i in key_msg_add1:
#         plain_text+=number_to_alphabet_dict[i]
#     return plain_text

# res = encryption(msg,key)
# print("Vernam cipher is : ",res)
# print("Plain Text is : ",decryption(res,key))

# x = 1
# y = 1 
# z = 1
# n = 2
# l = [ [i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if ((i+j+k)!=n)]
# print(l)

# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()
# t = tuple(arr)
# print(t)
# print(t[n-2])
# def sort1(m):
#     m.sort(key=lambda x: x[1])
#     return m
# n = int(input())
# m = [[input(),float(input())] for i in range(n)]
# q = sort1(m)
# s = set(q)
# t = tuple(s)
# print(t[-2])

# inp ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# out = ""
# for i in inp:
#     if i ==" " or i == "  " or i == ".":
#         out += " "
#     else:
#         n = a.index(i)
#         if n == 24:
#             temp = "a"
#         elif n == 25:
#             temp ="b"
#         else:
#             temp = a[n+2]
#         out +=temp
# print(out)
# aeilqtuy

# f = open("some.txt", mode="r",encoding="utf-8")
# a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# out = ""
# for i in f:
#     for j in i.split():
#         print(j)
        

# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)
#     return string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     res = sum(student_marks[query_name])/3
#     print("%.2f" %res)

# import numpy
# r,c = map(int,input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# matrix1 = numpy.array(a).reshape(r,c)
# matrix2 = numpy.array(b).reshape(r,c)
# print(matrix1+matrix2)
# print(matrix1-matrix2)
# print(matrix1*matrix2)
# print(matrix1//matrix2)
# print(matrix1%matrix2)
# print(matrix1**matrix2)

# f = open("some.txt",mode='r')
# a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# l = []
# while True:
#     c = f.read(1)
#     if c in a:
#         l.append(c)
#     if not c:
#         break
# print(l)

# n = int(input())
# a,b = input().split()
# a1,b1 = input().split()
# a2,b2 = input().split()
# try:
#     print(a/b)
#     print(a1/b1)
#     print(a2/b2)
# except Exception as e:
#     print("Error Code",e)


# def count_substring(string, sub_string):
#     count = []
#     for i in range(len(string)+1):
#         if i==len(string)-(len(sub_string)-1):
#             break
#         else:
#             temp = string[i:i+len(sub_string)]
#             if temp == sub_string:
#                 count.append(temp)
#     return len(count)

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# string = "dfg jgfsd gf"
# temp = ""
# count = 0
# for i in range(len(string)):
#     if count == 0:
#         count = 1
#         temp = temp+string[0].upper()
#     else:
#         if string[i-1] == " ":
#             temp = temp + string[i].upper()
#         else:
#             temp = temp + string[i]
# print(temp)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = input()
# a = set(map(int,input().split()))
# n1 = input()
# b = set(map(int,input().split()))
# re = a^b
# for i in sorted(re):
#     print(i)

# def average(array):
#     # your code goes here
#     sum1 = 0
#     a = set(array)
#     for i in a:
#         sum1 = sum1 + i
#     avg = sum1/len(a)
#     return avg


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# import numpy
# a,b = input().split()
# a1,b1 = input().split()
# a2,b2 = input().split()
# print((int(a1)+int(a2))*(int(b1)+int(b2)))

# import re
# a = open("candle.txt",mode="r")
# c = a.read()
# pattern = re.compile(r'[A-Z]{3}[a-z]{1}[A-Z]{3}')
# result = pattern.finditer(c)
# for i in result:
#     print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# s = []
# for i in range(n):
#     s.append(input())
# print(len(set(s)))

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import re
# string = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
# pattern = re.compile(r'(a*|e*|i*|o*|u*)*')
# result = pattern.findall(string)
# print(result)

# for i in range(1,int(input())):
#     print((10 ** i - 1) // 9)

# l = list(map(int(input().split())))
# r = []
# for i in l:
#     pattern = re.compile(r'')

# import numpy

# array_1 = numpy.array([1,2,3])
# array_2 = numpy.array([4,5,6])
# array_3 = numpy.array([7,8,9])

# print (numpy.concatenate((array_1, array_2, array_3))) 

# Enter your code here. Read input from STDIN. Print output to STDOUT
# set1_size = int(input())
# set1 = set(map(int,input().split()))
# set2_size = int(input())
# set2 = set(map(int,input().split()))
# l = set1 - set2
# print(len(l))

# def squre(num):
#     print(num*num)


x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)    