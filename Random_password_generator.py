#random password generator
#importing the required libraries

import string
import random

#assigning the variables
alphabets=list(string.ascii_letters)
numbers=list(string.digits)
special_char=list("!@#$%^&*()?{}[]")

characters=list(alphabets + numbers + special_char)


#definening a function
def generate_random_password():
    #password length from user
    length=int(input("Enter the length of password:"))

    #number of character types from the user
    alphabet_count=int(input("Enter the count of alphabets in password:"))
    number_count=int(input("Enter the count of numbers in password:"))
    special_char_count=int(input("Enter the count of special characters in password:"))

    characters_count=alphabet_count + number_count + special_char_count


    #checking total length of password with characters_count
    #if sum is greater than length print not valid
    if characters_count>length:
        print("Characters total count is greater than the entered password length")
        return


    #initializing password
    password=[]

    #choosing alphabets randomly
    for i in range(alphabet_count):
        password.append(random.choice(alphabets))

    #choosing numbers randomly
    for i in range(number_count):
        password.append(random.choice(numbers))

    #choosing special characters randomly
    for i in range(special_char_count):
        password.append(random.choice(special_char))
        

    #if the total characters count less than the password length
    #to make it equal add random characters
    if characters_count<length:
        random.shuffle(characters)
        for i in range(length-characters_count):
            password.append(random.choice(characters))



    #shuffling the resultant password
    random.shuffle(password)

    #converting the list to a string
    # and printing it
    print("Your password is:","".join(password))

    
#calling the function
generate_random_password()
































        
