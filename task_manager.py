# Program is a task manager that can manage users and designate task to them

#=====importing libraries===========
from datetime import datetime

#====Login Section====
logged_in = False
list_username = []
list_user_password = []

# Gets all users from user.txt file and stores usernames and passwords in 
# separate arrays
with open("user.txt", 'r') as f:
    for line in f:
        temp_name, temp_pass = line.split(", ")
        temp_pass = temp_pass.replace("\n", '') 
        list_username.append(temp_name)
        list_user_password.append(temp_pass)

# Loops until valid login
while logged_in != True:
    print("Enter your details to login")
    username = input("Username: ")
    password = input("Password: ")

    user_exist = False
    password_exist = False
    for i in range(len(list_username)):   
        # If username and password is correct
        if (username == list_username[i]) and (password == list_user_password[i]):
            user_exist = True
            password_exist = True
        # If username only is correct
        elif (username == list_username[i]):
            user_exist = True
            password_exist = False
                
    if (user_exist == True) and (password_exist == True):
        print("\nLogged in succesfully! \n")
        logged_in = True
    elif (user_exist == True):
        print("\nIncorrect password, please try again. \n")
    else: 
        print("\nUser does not exist, please try again. \n")

# Show Menu until user types exit
while True:
    #presents a menu to the user and makes sure that the user input 
    # is converted to lower case.
    if username == "admin":
        menu = input("\nSelect one of the following Options below: \n"
                    + "r - register user \n"
                    + "a - add task \n"
                    + "va - view all tasks \n"
                    + "vm - view my task \n"
                    + "ds - display statistics \n"
                    + "e - exit \n"
                    + ": ").lower()
    else: 
        menu = input("\nSelect one of the following Options below: \n"
                    + "r - register user \n"
                    + "a - add task \n"
                    + "va - view all tasks \n"
                    + "vm - view my task \n"
                    + "e - exit \n"
                    + ": ").lower()

    # Allows user to add new user if they are the admin
    if menu == 'r':    
        if (username == "admin"):
            print("Enter new user details")
            new_username = input("Username: ")
            new_password = input("Password: ")

            # Confirms password if correct adds user else ask user 
            # to add new user again
            password_confirmed = input("Confirm Password: ")
            if password_confirmed == new_password:
                with open("user.txt", 'a') as f:
                    f.write(f"\n{new_username}, {new_password}")
            else:
                print("\nPassword confirmation incorrect, Please try again. \n")
        else:
            print("\nYou do not have admin privilege, "
                + "only admins can add new user \n")

    # Allows user to add a new task for users
    elif menu == 'a':
        print("Add a task for a user")
        user_assigned = input("Enter the user you wish to assign the task to: ")
        task_title = input("Enter title for the task: ")
        task_desc = input("Enter description for the task: ")
        task_due_date = input("Enter due date the for task: ")

        # Gets the current date and formats it into suitable format
        current_date = datetime.now()
        current_date = current_date.strftime("%d %B %Y")
        print(current_date)

        # Adds task to task.txt file
        with open("tasks.txt", 'a') as f:
            f.write(f"\n{user_assigned}, {task_title}, {task_desc}" 
                    + f", {task_due_date}, {current_date}, No")

    # Views all tasks in a easy to read format
    elif menu == 'va':
        with open("tasks.txt", 'r') as f:
            for line in f:
                task_details = line.split(", ")
                print("___________________________________________________\n\n"
                    + f"Task:\t\t\t{task_details[1]} \n"
                    + f"Assigned to:\t\t{task_details[0]} \n"
                    + f"Date Assigned:\t\t{task_details[3]} \n"
                    + f"Due Date:\t\t{task_details[4]} \n"
                    + f"Task Complete?\t\t{task_details[5]} \n"
                    + f"Task description:\n {task_details[2]} \n"
                    + "___________________________________________________\n")

    # Views all tasks designated to the current user in a easy to read format
    elif menu == 'vm':
        with open("tasks.txt", 'r') as f:
            for line in f:
                task_details = line.split(", ")
                if (task_details[0] == username):
                    print("___________________________________________________\n\n"
                        + f"Task:\t\t\t{task_details[1]} \n"
                        + f"Assigned to:\t\t{task_details[0]} \n"
                        + f"Date Assigned:\t\t{task_details[3]} \n"
                        + f"Due Date:\t\t{task_details[4]} \n"
                        + f"Task Complete?\t\t{task_details[5]} \n"
                        + f"Task description:\n {task_details[2]} \n"
                        + "___________________________________________________\n")  
    
    # If the user is admin they can display stats about 
    # the total amount of users and tasks
    elif menu == "ds" and username == "admin":
        user_count = 0
        task_count = 0

        with open("user.txt", 'r') as f:
                for line in f:
                    user_count += 1
        with open("tasks.txt", 'r') as f:
                for line in f:
                    task_count += 1

        print("___________________________________________________\n\n"
            + f"The total number of users: {user_count} \n"
            + f"The total number of tasks: {user_count} \n"
            + "___________________________________________________\n")  

    # Exits program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")