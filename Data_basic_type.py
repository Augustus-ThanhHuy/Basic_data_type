#Basic Data type:
'''
Các kiểu dữ liệu cơ bản trong python: bool, None, int, float, str
'''
'''
Topic #0: bool & None 
'''
# [x] bool: True & False
var_bool = True

# [x] type(): Dynamically typed
#print(type(var_bool) )
#Numerically, they're evaluated as integers with value 1 (True), 0 (False)
#a = 4 + True
#print(a)
#b = False
#if b==0:
#   print("B is 0")

# [] None: phần tử không
var_none= None
# print(type(var_none))
# None is often used as a placeholder for optional or missing value.
# It evaluates as False in conditionals.
#email_address = None
# email_address = "Chủ nghĩa tối giản"

# if email_address:
#     print(f"Email address is {email_address}")
# else:
#     print(f"Email address is empty of {email_address}")
'''
Topic #2: Number (int & float)
'''

#[] Number: int (Integer = Số nguyên) & float (Floating point number = số thực)
#print(type(4E2), 4E2)# 4x10(^2)
# print(10**3) #10^3
# print(10//3) # 3
# print(10%3) # 1 vì 10 chia 3 = 3 dư 1

# [] Basic Function (Hàm cơ bản)
print(pow(10, 3)) #10**3 =1000
print(abs(-6.9)) #6.9
print(round(6.69)) # 7
print(round(5.468, 2)) #5.47 --> round to nth digit
print(bin(512)) # '0b10'
print(hex(512))