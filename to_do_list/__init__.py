import Task
import TaskService
import LinkedList


def main_menu():
    print('----------Main Menu----------')
    print('(1) Insert Task')
    print('(2) Delete Task')
    print('(3) Update Task')
    print('(4) Search task by name')
    print('(5) Search task by date')
    print('(6) Mark task done')
    print('(7) Remove task done')
    print('(8) View Tasks')
    print('(Any others) Exit')
    m = input("Option: ")
    return switch_main_menu(m)


def switch_main_menu(m):
    if m == '1':
        task_service.insert_task(task_list)
        return True
    elif m == '2':
        task_service.delete_task_by_name(task_list)
        return True
    elif m == '3':
        task_service.update_task_by_name(task_list)
        return True
    elif m == '4':
        task_service.search_task_by_name(task_list)
        return True
    elif m == '5':
        task_service.search_task_by_date(task_list)
        return True
    elif m == '6':
        task_service.mark_task_done(task_list)
        return True
    elif m == '7':
        task_service.remove_tasks_done(task_list)
        return True
    elif m == '8':
        task_service.list_task(task_list)
        return True
    else:
        return False


if __name__ == '__main__':
    menu = True
    task_list = LinkedList.LinkedList()
    task_service = TaskService

    while menu:
        menu = main_menu()
