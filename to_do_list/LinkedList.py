import ListNode


class LinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get_len(self):
        return self.len

    def set_len(self, new_len):
        self.len = new_len

    def is_empty(self):
        return self.head is None

    def append(self, new_data):
        new_node = ListNode.ListNode(new_data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.set_len(self.get_len() + 1)

    def remove(self, data):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()

        if previous is None:
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())

        self.set_len(self.get_len() - 1)

    def update(self, data, data_update):
        current = self.head

        while current is not None:
            if current.get_data() == data:
                return current.set_data(data_update)
            else:
                current = current.get_next_node()

    def search_by_name(self, parameter):
        current = self.head

        while current is not None:
            if current.get_data().name == parameter:
                return current.get_data()
            else:
                current = current.get_next_node()

    def search_by_date(self, parameter):
        current = self.head
        new_linked_data_filtered = LinkedList()
        while current is not None:
            if current.get_data().date == parameter:
                new_linked_data_filtered.append(current.get_data())
            current = current.get_next_node()

        return new_linked_data_filtered

    def search_by_done(self):
        current = self.head

        while current is not None:
            if current.get_data().done:
                return current.get_data()
            else:
                current = current.get_next_node()

    def print_list(self):
        current = self.head

        while current is not None:
            item = current.get_data()
            print("Task =========")
            print(item.name)
            print(item.date)
            print(item.description)
            if item.get_done():
                print("Task done! *************************")
            print("================")
            current = current.get_next_node()

    def remove_done(self):
        current = self.head
        while current is not None:
            self.remove(self.search_by_done())
            current = current.get_next_node()
