#This is my day one in doing python for software engineering 
'''
#printing statements and variables 
print ("Iam a software engineer")
engineer = "software engineer"
print(f"Iam a {engineer}")

###variables can store all data types like integers , floats , booleans and strings
string = "Kawooma Elijah"
integer = 20
floating = 179.9
boleaning  = True
print(f"My name is {string} and iam {integer} years old . Iam {floating} cm tall and its {not(boleaning)} that iam still single")

'''
###asking for user input 
#String user input 
name = input("What is your name ?")
print(f"Nice to meet you {name }, iam Devin AI your personal AI assistant ")

#integer user input 
age = int(input(f"How old are you {name} ?"))
if age in range (1,18):
    print(f"Your quite young {name } you are {age} years old and you cannot access this site. Bye")
else:
    print(f"I see you are {age } years old .. Welcome to Devin Ai {name } we are excited to work with you ")


#Float input 
height = float(input(f"How tall are you { name} in cm ?"))
print(f"You are {height} cm tall ")

#Bool
print("Enter either : True or False ")
sick = bool(input("Do you have any impairments ?"))

if sick == "True":
    print(f"We would love to work with you when you are better {name} Chao")
elif sick == "False":
    print("We are glad to know you are good to go. Please contact us when you are ready to start the trail of the job thanks ")
else:
    print("You have an error")

























