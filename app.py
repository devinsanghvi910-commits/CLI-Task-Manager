tasks = []
program_start = "start"
menu = ("""Here are the menu options: 
add tasks
remove task
show tasks
quit""")    
while program_start != "quit":
    print(menu)
    program_start = input("What would you like to do: ")
    if program_start == 'add tasks':
        task = input("What is your task: ")
        tasks.append(task)
        print(tasks)
    if program_start == "show tasks":
        print(tasks)
    if program_start == "remove task": 
        task_remove = input("Please enter the task that you want to remove: ")
        if task_remove in tasks:
            tasks.remove(task_remove)
            print(tasks)
else:
    print("please enter a valid input")

    