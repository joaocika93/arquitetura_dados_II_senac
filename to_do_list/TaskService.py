import Constant
import LinkedList
import Task
import re


def insert_task(task_list):
    name = input("Task name: ")
    date_entry, valid = create_and_validate_date(input('Enter a date in YYYY-MM-DD format: '))
    description = input("task description: ")
    if valid:
        newTask = Task.Task(name, date_entry, description)
        task_list.append(newTask)
    else:
        print('Invalid parameters!')


def delete_task_by_name(task_list):
    name = input("Search task by name: ")
    task = iterator_filter_parameter(task_list, name, Constant.PARAMETER_TYPE_NAME, Constant.RETURN_TYPE_OBJECT) \
        if task_list.is_not_empty() else print('Task list is empty!')
    if task is not None:
        task_list.remove(task)


def update_task_by_name(task_list):
    choice_menu = True
    name = input("Search task by name: ")
    task = iterator_filter_parameter(task_list, name, Constant.PARAMETER_TYPE_NAME, Constant.RETURN_TYPE_OBJECT) \
        if task_list.is_not_empty() else print('Task list is empty!')
    if task is not None:
        while choice_menu:
            task_update, choice_menu = choice_update_field(task)
            task_list.update(task, task_update)
        return task_list
    else:
        print('Task not found!')


def search_task_by_name(task_list):
    name = input("Search task by name: ")
    iterator_filter_parameter(task_list, name, Constant.PARAMETER_TYPE_NAME, Constant.RETURN_TYPE_PRINT) \
        if task_list.is_not_empty() else print('Task list is empty!')


def search_task_by_date(task_list):
    date = input("Search tasks by date: ")
    task_list_date_filtered = iterator_filter_parameter_list(task_list, date, Constant.PARAMETER_TYPE_DATE) \
        if task_list.is_not_empty() else print('Task list is empty!')
    print('Any tasks found!') if task_list_date_filtered.is_empty() else list_task(task_list_date_filtered)


def list_task(task_list):
    current = task_list.get_head()

    while current is not None:
        print_task(current.get_data())
        current = current.get_next_node()


def print_task(task):
    print("Task =========")
    print(task.name)
    print(task.date.string)
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
    c = input("Option: ")

    if c == '1':
        name = input("Set a new name task: ")
        task.set_name(name)
        return task, Task
    elif c == '2':
        date_entry, valid = create_and_validate_date(input('Enter a new date in YYYY-MM-DD format: '))
        task.set_date(date_entry) if valid else print('Invalid new date!')
        return task, Task
    elif c == '3':
        description = input("Set a new description task: ")
        task.set_description(description)
        return task, Task
    elif c == '4':
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
    name = input("Search task by name: ")
    task = iterator_filter_parameter(task_list, name, Constant.PARAMETER_TYPE_NAME, Constant.RETURN_TYPE_OBJECT) \
        if task_list.is_not_empty() else print('Task list is empty!')
    task.set_done() if task is not None else print('Task not found!')


def remove_tasks_done(task_list):
    if task_list.is_not_empty():
        current = task_list.get_head()
        while current is not None:
            if current.get_data().done:
                task_list.remove(current.get_data())
            current = current.get_next_node()
    else:
        print('Task list is empty!')


def iterator_filter_parameter(task_list, parameter, parameter_type, return_option):
    current = task_list.get_head()
    while current is not None:
        if return_option == Constant.RETURN_TYPE_OBJECT \
                and (is_valid_parameter(current.get_data(), parameter, parameter_type)):
            return current.get_data()
        elif return_option == Constant.RETURN_TYPE_PRINT \
                and (is_valid_parameter(current.get_data(), parameter, parameter_type)):
            return print_task(current.get_data())
        else:
            current = current.get_next_node()

    return print('Any tasks found!')


def iterator_filter_parameter_list(task_list, parameter, parameter_type):
    current = task_list.get_head()
    new_linked_data_filtered = LinkedList.LinkedList()
    while current is not None:
        if is_valid_parameter(current.get_data(), parameter, parameter_type):
            new_linked_data_filtered.append(current.get_data())
        current = current.get_next_node()

    return new_linked_data_filtered


def is_valid_parameter(data, parameter, parameter_type):
    return True if (data.get_done() and parameter_type == Constant.PARAMETER_TYPE_DONE) \
                   or (data.get_name() == parameter and parameter_type == Constant.PARAMETER_TYPE_NAME) \
                   or (data.get_date() == parameter and parameter_type == Constant.PARAMETER_TYPE_DATE) else False


def create_and_validate_date(date_entry):
    pattern = re.compile(Constant.PATTERN_DATE)
    search = pattern.search(date_entry)
    if search is not None:
        return search, True
    else:
        return '', False
