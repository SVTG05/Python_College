print("Let's Register!!")
username = input("Enter the username: ")
password = input("Enter the password: ")
register = input("Register? Y or N: ").strip().upper()

if register != 'Y':
    print("Registration Failed. Please re-run the program.")
    exit()

print("Registration successful! Let's Login.")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    re_username = input("Enter the Username: ")
    
    if re_username != username:
        print("Wrong Username.")
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
        continue  
    
    re_password = input("Enter the Password: ")
    if re_password != password:
        print("Wrong Password.")
        attempts += 1
        print(f"Attempt {attempts} of {max_attempts}")
    else:
        print("Login Successfully!")
        break

if attempts == max_attempts:
    print("Number of retries reached. Access Denied.")
