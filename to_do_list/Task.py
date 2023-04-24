class Task:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description
        self.done = False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_done(self):
        return self.done

    def set_done(self):
        self.done = True
