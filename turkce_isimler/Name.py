class Name:

    def __init__(self, name, count):
        self.name = name
        self.count = count
    
    def __str__(self):
        return self.name + ": " + str(self.count)
    
    def get_name(self):
        return self.name.title()

    def get_count(self):
        return self.count