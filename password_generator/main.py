import random
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


drawing = """
 ______                                     _     ______                                              
(_____ \                                   | |   / _____)                             _               
 _____) )___  ___  ___ _ _ _  ___   ____ _ | |  | /  ___  ____ ____   ____  ____ ____| |_  ___   ____ 
|  ____/ _  |/___)/___) | | |/ _ \ / ___) || |  | | (___)/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
| |   ( ( | |___ |___ | | | | |_| | |  ( (_| |  | \____/( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
|_|    \_||_(___/(___/ \____|\___/|_|   \____|   \_____/ \____)_| |_|\____)_|   \_||_|\___)___/|_|    
"""

print(drawing)



options =int(input("0 for New Password Generator and 1 to Retrive password: "))

if options==0:
    associatedKey = input("Enter Associated Key: ")
    password_list = []
    letters_needed = int(input("Enter no letters needed: "))
    numbers_needed = int(input("Enter no of numbers needed: "))
    symbols_needed = int(input("Enter no of symbols needed: "))
    i=0
    while(i<letters_needed):
        password_list.append(random.choice(letters))
        i+=1
    i=0
    while(i<numbers_needed):
        password_list += random.choice(numbers)
        i+=1
    i=0
    while(i<symbols_needed):
        password_list += random.choice(symbols)
        i+=1

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    print(password)


    with open('file.json','r') as json_file:
        json_decoded = json.load(json_file)

    if associatedKey not in json_decoded:
        json_decoded[associatedKey] = password

    with open('file.json', 'w') as json_file:
        json.dump(json_decoded, json_file)
elif options==1:
    enterKey = input("Enter Associated Key: ")

    with open('file.json','r') as json_file:
        json_decoded = json.load(json_file)

    if enterKey in json_decoded:
        print((enterKey, json_decoded[enterKey]))
    else:
        print(" No Key found")

else:
    print("Select 0 or 1")


