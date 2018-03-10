#  Simple Password Generator
#
import random
# initialize variables
complex_a = ["simple" , "a-z"]
# ASCII Dec: 97 - 122
complex_b = ["better" , "a-z,A-Z"]
# ASCII Dec: 65 - 90
complex_c = ["strong" , "a-z,A-Z,0-9"]
# ASCII Dec: 48 - 57
complex_d = ["complex" , "a-z,A-Z,0-9,sym"]
# ASCII Dec: 33 - 47, 58 - 64, 91 - 96, 123 - 126
#
# defaults
pass_complex = complex_d[1]
pass_type = complex_d[0]
pass_length = 12
pass_number = 5
#
menu_1 = " 1. Password Length:"
menu_2 = " 2. Password Complexity:"
menu_3 = " 3. Number to generate:"
menu_4 = " 4. Generate Passord(s):"
menu_9 = " Press 'q' to Quit"
# -----------------------------------
def print_menu():
    print()
    print(" " * 25 + "*** Password Generator ***")
    print("-" * 80)
    print("{:<28}{:<16} - default is: 12".format(menu_1, pass_length))
    print("{:<28}{:<16} - default is: a-z,A-Z,0-9,sym".format(menu_2, pass_complex))
    print("{:<28}{:<16} - default is: 5".format(menu_3, pass_number))
    print(menu_4)
    print(menu_9)
    print()
# -----------------------------------
def get_number():
    try:
        get_number = int(input("Enter a number: "))
    except:
        ValueError
        print("You must enter a number")
        return False
    if get_number == "":
        return False
    else:
        return get_number
# -----------------------------------
def change_length():
    print("Update the length of the passwords to generate...")
    new_length = get_number()
    if new_length == False:
        return
    elif new_length < 10:
        print()
        print("Your password is too short...")
        test = input("Are you sure(y/n)?")
        if test == "n":
            return
        elif test == "y":
            print("ok...")
            update_length(new_length)
        else:
            print()
            print("Invalid choice...aborting")
            return
    elif new_length > 64:
        print()
        print("Get serious...that is way to long")
        print("aborting...")
        return
    else:
        print()
        print("updating password length...")
        update_length(new_length)
# -----------------------------------
def update_length(new_length):
    global pass_length
    pass_length = new_length
    print("The new password length is ", pass_length)
# -----------------------------------
def change_complexity():
    global pass_complex, pass_type
    print(" * Password Complexity Menu *")
    print("-" * 60)
    print(" 1. a-z\t\tsimple, only lower case letters, 26 letter keyspace")
    print(" 2. A-Z\t\tbetter, lower and upper case letters, 52 character keyspace")
    print(" 3. 0-9\t\tstrong, adds numbers, 62 character keyspace")
    print(" 4. symbols\tcomplex, adds all the symbols...95 character keyspace")
    print()
    pass_choice = get_number()
    if pass_choice == 1:
        print("Password Complexity will be set to 'simple'")
        print("\tlower case letters (a-z)")
        pass_complex = complex_a[1]
        pass_type = complex_a[0]
    elif pass_choice == 2:
        print("Password Complexity will be set to 'better'")
        print("\tlower and upper case letters (a-z,A-Z)")
        pass_complex = complex_b[1]
        pass_type = complex_b[0]
    elif pass_choice == 3:
        print("Password Complexity will be set to 'strong'")
        print("\tlower, upper case letters, and numbers (a-z,A-Z,0-9)")
        pass_complex = complex_c[1]
        pass_type = complex_c[0]
    elif pass_choice == 4:
        print("Password Complexity will be set to 'complex'")
        print("\tlower, upper case letters, numbers, and symbols (a-z,A-Z,0-9,sym)")
        pass_complex = complex_d[1]
        pass_type = complex_d[0]
    else:
        print("Invalid choice...")
        return
# -----------------------------------
def number_to_generate():
    print()
    print("Update the number of the passwords to generate...")
    new_number = get_number()
    if new_number == False:
        return
    elif new_number >= 33:
        print()
        print("That is too many...")
    else:
        print()
        print("Updating the number of passwords to generate...")
        update_num_to_gen(new_number)
# -----------------------------------
def update_num_to_gen(new_number):
    global pass_number
    pass_number = new_number
    print("Generate ", pass_number, " passwords...")
# -----------------------------------
def get_rand_num():
    number = int(random.randint(33, 126))
    return number
# -----------------------------------
def build_pass(number):
    global password
    password = password + repr(chr(number))
# -----------------------------------
def fix_pass(password):
    fixed_pass = ''
    for item in password:
        item = item.replace("'", "") 
        fixed_pass = fixed_pass + item
    return fixed_pass
# ----------------------------------- 
def generate_passwords(p_type, p_length):
    final_pass = ''
    count = 0
    while count < p_length:
        number = get_rand_num()
        if p_type == "simple" and (97 <= number <= 122):
            # ASCII 97 - 122
            build_pass(number)
            count += 1
        elif p_type == "better" and ((65 <= number <= 90) or (97 <= number <= 122)):
            # ASCII 65 - 90, 97 - 122
            build_pass(number)
            count += 1
        elif p_type == "strong" and ((48 <= number <= 57) or (65 <= number <= 90) or (97 <= number <= 122)):
            # ASCII 48 - 57, 65 - 90, 97 - 122
            build_pass(number)
            count += 1
        elif p_type == "complex" and (33 <= number <= 126):
            # ASCII 33 - 126
            build_pass(number)
            count += 1
        else:
            continue
    final_pass = fix_pass(password)
    return final_pass
#
#
# -------------- MAIN LOOP --------------
#
while True:
    global password
    print_menu()
    choice = input("Choose wisely: ")
    if choice == "":
        print()
    elif choice == '1':
        change_length()
    elif choice == '2':
        change_complexity()
    elif choice == '3':
        number_to_generate()
    elif choice == '4':
        count = 0
        while count < pass_number:
            password = ''
            Final_Pass = generate_passwords(pass_type, pass_length)
            count_times = count + 1
            print(f"Password # {count_times} is: {Final_Pass}")
            Final_Pass = ''
            count += 1
    elif choice == 'q':
        print(choice)
        print("Exiting...")
        break
    else:
        print("Invalid Option")
#
# EOF
