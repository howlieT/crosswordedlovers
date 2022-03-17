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

    def link_item_action(self, item_to_link, action):
        self.link_item_action = item_to_link

    def get_details(self):
        print(self.description)
        for action in self.link_item_action:
            item = self.link_item_action[action]
        print(" " + Item.get_description())

    def action(self, action):
        if action in self.link_item_action:
            return self.link_item_action[action]
        else:
            print("You can't do that")
            return self
