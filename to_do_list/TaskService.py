import Task


def insert_task(task_list):
    newTask = Task.Task(input("Task name: "), input("task date: "), input("task description: "))
    task_list.append(newTask)


def delete_task_by_name(task_list):
    task = search_task_by_name(task_list, '2')
    task_list.remove(task)


def update_task_by_name(task_list):
    choice_menu = True
    task = search_task_by_name(task_list, '3')
    while choice_menu:
        task_update, choice_menu = choice_update_field(task)
        task_list.update(task, task_update)
    return task_list


def search_task_by_name(task_list, menu_option):
    name = input("Search task by name: ")
    if menu_option in ('2', '3', '6'):
        return task_list.search_by_name(name)
    else:
        return print_task(task_list.search_by_name(name))


def search_task_by_date(task_list):
    date = input("Search tasks by date: ")
    task_list_date_filtered = task_list.search_by_date(date)
    task_list_date_filtered.print_list()


def list_task(task_list):
    task_list.print_list()


def print_task(task):
    print("Task =========")
    print(task.name)
    print(task.date)
    print(task.description)
    if task.get_done():
        print("Task done! *************************")
    print("================")


def choice_update_field(task):
    print('----------Update Task Fields Choice Menu----------')
    print('(1) Update name')
    print('(2) Update date')
    print('(3) Update description')
    print('(4) Update all')
    print('(Any others) Exit')
    c = int(input("Option: "))

    if c == 1:
        name = input("Set a new name task: ")
        task.set_name(name)
        return task, Task
    elif c == 2:
        date = input("Set a new date task: ")
        task.set_date(date)
        return task, Task
    elif c == 3:
        description = input("Set a new description task: ")
        task.set_description(description)
        return task, Task
    elif c == 4:
        name = input("Set a new name task: ")
        date = input("Set a new date task: ")
        description = input("Set a new description task: ")
        task.set_name(name)
        task.set_date(date)
        task.set_description(description)
        return task, Task
    else:
        return task, False


def mark_task_done(task_list):
    task = search_task_by_name(task_list, '6')
    task.set_done()


def remove_tasks_done(task_list):
    task_list.remove_done()
