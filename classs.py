class Employee:
    

    raise_amount=1.04
    def __init__(self,first,last,pay):

        self.first=first
        self.last=last
        self.pay=pay
        self.email= self.first +'.' + self.last +'@gmail.com'

    
    def fullname(self):
        
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):

        self.pay=int(self.pay*Employee.raise_amount)
        
class Developer(Employee):

    raise_amount=1.10
    def __init__(self,first,last,pay,prog_lang):
        Employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang    

    

class Manager(Employee):

    def __init__(self,first,last,pay,employee=None):
        Employee.__init__(self,first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee

    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)

    def print_emp(self):
        for emp in self.employee:
            print("---->",  emp.fullname())

dev_1=Developer('steve','waugh',10000,'python')
dev_2=Developer('steven','smith',20000,'java')
dev_3=Developer('mark','waugh',100000,'python3')
mgr_1=Manager('ricky','ponting',2000,[dev_1,dev_2])

mgr_1.add_emp(dev_3)

#mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
# print(dev_1.prog_lang)

# dev_1.apply_raise()
# print(dev_1.pay)











#     @classmethod



#     def self_raise_amount(cls,amount):
#         cls.raise_amount=amount

#     @classmethod
#     def from_string(cls,emp_str):
#         first,last,pay=emp_str_1.split('-')
#         return cls(first,last,pay)

#     @staticmethod
#     def is_workday(day):
#         if day.weekday()==5 or day.weekday()==6:
#             return False
        
#         return True        
# import datetime
# my_date=datetime.date(2016,7,7)        
# print(Employee.is_workday(my_date))                
# #emp_1=Employee('shubham','mahawar',36000)

# emp_str_1='brian-lara-30000'


# emp_1=Employee.from_string(emp_str_1)
# first,last,pay=emp_str_1.split('-')

# emp_1=Employee(first,last,pay)

# print(emp_1.fullname())
# print(emp_1.email)




# Employee.self_raise_amount(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)










# # def square(x):
# #     return x*x



# # def firstclass(func,list):
# #     result=[]
# #     for i in list:
# #         result.append(func(i))
# #     return result


# # p=firstclass(square,[1,2,3,4])

# # print(p)



# # def logger(msg):

# #     def log():
# #         print('hello '+ msg)

# #     return log

# # p=logger('shubham')
# # p()

# from functools import wraps
# ##### Decorators
# def decorator_function(original_function):
    
#     def wrapper_function(*args,**kwargs):
#         print("fello")
#         return original_function(*args,**kwargs)
#     return wrapper_function

# def my_logger(original_func):
#     import logging
#     logging.basicConfig(filename='{}.log'.format(original_func.__name__),level=logging.INFO)
#     @wraps(original_func)
#     def wrapper(*args,**kwargs):
#         logging.info('Ran with {} and {}'.format(*args,**kwargs))
#         return original_func(*args,**kwargs)
#     return wrapper

# def my_timer(original_func):
#     import time
#     @wraps(original_func)
#     def wrapper(*args,**kwargs):
#         t1=time.time()
#         result=original_func(*args,**kwargs)
#         t2=time.time()-t1
#         print('{} ran for {} seconds'.format(original_func.__name__,t2))
#         return result
#     return wrapper      

# import time
# @my_logger
# @my_timer


# def display_info(name,age):
#     time.sleep(1)
#     print("your name and age is {} and {}".format(name,age))
# # display_info= my_logger(my_timer(display_info))

# display_info('shubham',25)



