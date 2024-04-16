# def maximum(arrar):
#     if arrar == []:
#         return 0
#     elif arrar[0] > maximum(arrar[1:]):
#         return arrar[0]
#     else:
#         return maximum(arrar[1:])
    

# array = [2,4,18,1]
# # print(maximum(array))

# class Ticket:
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def greeting(self):
#         print(self.name ,"Welcome to website")

#     @staticmethod
#     def results():
#         print('Results manipulated by outside')
    
#     def __str__(self):
#         return f'Name : {self.name} , Age : {self.age}, Gender : {self.gender}'


# person = Ticket('suraj',17,'male')
# # print(person)

 # lcm


# def getLcm(array):
#     count = 0
#     for arrar_value in array:
#         numbers = [2,3,4,5,6,7,8,9]
#         for num in numbers:
#             if(arrar_value % num == 0):
#                count += 1
#                print(arrar_value,num)
#     return count
          
            

# getLcmarray = [2,3,16,5]

# print(getLcm(getLcmarray))

voted = {}

def check_voter(name):
    if name in voted:
        print('kick them out')
        return
    else:
        voted[name] = True
        return print('Thank you for vote')

print(check_voter('shubham'))
print(check_voter('suraj'))
print(check_voter('shubham'))