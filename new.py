import random
x = "welcome to password generator"
print(x.upper())

letters= ["A","B","C","D","E","F","G","H","I","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
"a","b","c","d","e","f","g","h","i'","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

numbers = ["1",",2","3","4","5","6","7","8","9","0"]
special_characters = ["@","#","$","_","&","-","+","(",")","/","*",":",";","!","?",".","%","[","]","{","}"]

n_letters = int(input("how many letters do you want in you password.\n: "))
n_numbers = int(input("how many numbers do yiu want in your password.\n: "))
sp_letters = int(input("how many specila characters do you want in your password.\n : "))

random.seed(0)
password_list = [ ] 
for i in range (1,n_letters + 1):
    char = random.choice(letters)
    password_list += char 

   
for i in range(1,n_numbers + 1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,sp_letters+ 1):
    char = random.choice(special_characters)
    password_list += char

random.shuffle(password_list)

passcord = " "
for new_password in password_list:
    passcord += new_password

if len(passcord) < 12 :
      raise Exception("your password should not have less than 12 characters.")
if len(passcord) > 18 :
      raise Exception("you password has too many entries.")
       
y = ("write your password down so do you not forget it.")
print(y.capitalize())
print(passcord)

x_copy = passcord.copy()
print(x_copy)
