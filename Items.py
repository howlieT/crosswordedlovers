class Item():
    def __init__(self, item_name, item_dict):
        self.name = item_name
        self.description = item_dict
        self.linked_item = {}

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def get_details(self):
        print(self.description)

    def link_item(self, item_to_link, room):
        self.linked_item[room] = item_to_link

    def use(self, use):
        if use in self.linked_item:
            return self.linked_item[use]
        else:
            print("You can't do that")
            return self

