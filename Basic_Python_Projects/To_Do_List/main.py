to_do_list = []
task_number = 1

while True:
    task = input(f'Enter task {task_number}: ')
    
    if task != '':
        to_do_list.append(task)
        task_number += 1
    else:
        print("\nYour To-Do List:")
        for i, t in enumerate(to_do_list, 1):
            print(f"{i}. {t}")
        break  # ✅ Exit the loop after printing
