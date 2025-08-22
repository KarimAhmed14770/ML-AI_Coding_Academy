#class for raising an error if an invalid choice is entered
class InvalidChoice(Exception):
    pass

data=[] #this will hold the data
names = []
numbers=[]

def choice_check(num):
    if num<1 or num>5:
        raise InvalidChoice("choice must be between 1 to 5! try again!")
    else:
        return 1


def get_data():# this function will only work once to link the lists in the program to the data file
    global data,names,numbers
    with open('Contacts.txt','r') as Contacts:
        data=Contacts.readlines() #this will get each line as an element of the list data
    counter=0
    while counter<len(data):
        curr_data=data[counter] #this will store the current line in curr_data
        zero_index=curr_data.find('0') #this searches for the index of zero to seperate beween names and numbers
        names.append(curr_data[:zero_index].rstrip(" "))#to remove whitespace from right side
        numbers.append(curr_data[zero_index:].strip()) #.strip to remove \n
        counter+=1


def file_handle():
    global names,numbers
    max_len = 0

    for name in names:
        if len(name)>max_len:
            max_len=len(name)
    with open('Contacts.txt','w') as Contacts:
        counter=0
        name_adjust = 0
        for name in names:
            name_adjust = name.ljust(max_len)  # because string is imutable
            Contacts.write(name_adjust+" "*10+numbers[counter]+'\n')
            counter+=1

def add_contact(name,number):
    global names,numbers
    names.append(name)
    numbers.append(number)
    file_handle()

def get_contact(name):
    global names,numbers
    counter=0
    found=0
    for contact_name in names:
        if(contact_name==name):
            print(f"Contact name: {contact_name}")
            print(f"Contact number: {numbers[counter]}")
            found=1
            break
        counter+=1
    if(found==0):
        print("Contact not found")

def delete_contact(name):
    global names,numbers
    counter=0
    found = 0
    for contact_name in names:
        if(contact_name==name):
            del names[counter] #deletes the element with the given index
            del numbers[counter]
            file_handle()
            found=1
            print("Contact Deleted")
            break
        counter+=1
    if (found==0):
        print("Contact not found")


def get_contacts():
    global names,numbers
    max_len=0
    counter=0
    for name in names:
        if len(name)>max_len:
            max_len=len(name)
    for name in names:
        print(name.ljust(max_len)+(" "*10)+numbers[counter])
        counter+=1




def contact_book():
    get_data()
    print("Hello to My Contacts App:")
    while(True):
        choice=int(input("1. to add a contact press (1)"
        "\n2. to delete a contact press (2)"
        "\n3. to view a contact press (3)\n4. to view all contacts press(4):\n5. to exit press (5) "))
        choice_check(choice)
        if(choice==1):
            name=input('Enter the contact\'s name: ')
            number=input('Enter the contact\'s number: ')
            add_contact(name,number)
        elif (choice==2):
            name = input("Enter the contact name: ")
            delete_contact(name)
        elif(choice==3):
            name=input("Enter the contact name: ")
            get_contact(name)
        elif (choice == 4):
            get_contacts()
        else:
            print("Thanks for using the program")
            break


try:
    contact_book()
except InvalidChoice as e:
    print(e)