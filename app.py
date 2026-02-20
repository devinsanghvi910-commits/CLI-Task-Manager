tasks = []
tasks_finished = []
program_start = "start"
menu = ("""Menu: 
add tasks
remove task
show tasks
show completed tasks
mark task as done
quit""")    
while program_start != "quit":
    print(menu)
    program_start = input("What would you like to do: ")
    if program_start == 'add tasks':
        task = input("What is your task: ")
        tasks.append(task)
        print(f'Current Tasks: {tasks}')
    elif program_start == "show tasks":
        print(f'Current Tasks: {tasks}')
    elif program_start == "remove task": 
        task_remove = input("Please enter the task that you want to remove: ")
        if task_remove in tasks:
            tasks.remove(task_remove)
            print(f'Current Tasks: {tasks}')
    elif program_start == "mark task as done":
        task_done = input("Which task would you like to mark as done: ")
        if task_done in tasks:
            tasks.remove(task_done)
            tasks_finished.append(task_done)
            print(f'Current tasks: {tasks}')
            print(f'Completed Tasks: {tasks_finished}')
    elif program_start == 'show completed tasks':
        print(f'Completed Tasks: {tasks_finished}')
    else:
        print("Please enter a valid input")