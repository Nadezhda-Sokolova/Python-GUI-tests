import random

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def get_group_list(self):
        self.open_group_editior()
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list



    def get_group_list_id(self):
        self.open_group_editior()
        tree = self.group_editor.window(auto_id='uxAddressTreeView')
        root = tree.tree_root()
        group_list = [node.ChildId() for node in root.children()]
        self.close_group_editor()
        return group_list



    def add_new_group(self, name):
        self.open_group_editior()
        self.group_editor.window(auto_id='uxNewAddressButton').click()
        input = self.group_editor.window(class_name='Edit')
        input.set_text(name)
        input.type_keys('\n')
        self.close_group_editor()

    def delete_any_group(self):
        self.open_group_editior()
        groups_list = self.get_group_list()
        group_for_deleting = random.choice(groups_list)
        self.delete_group.window(groups_list).click()
        self.group_editor.window(class_name='Delete')
        self.open_group_deleter()
        
        self.delete_group.window(name='Delete the selected group, subgroups and contacts').click(groups_list)
        self.delete_group.window(name='Ok').click()

        self.group_editor.window(name=group_for_deleting).click()
        self.group_editor.window(auto_id='ChildId').click()
        self.group_editor.window(class_name='Delete')




        self.group_editor.window(auto_id='ChildId').click()

        self.close_group_deleter()
        self.close_group_editor()

    #(auto_id='ChildId')

    def open_group_deleter(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.delete_group = self.app.application.window(title='Delete group')
        self.delete_group.wait('visible')


    def close_group_deleter(self):
        self.delete_group.close()




    def open_group_editior(self):
        self.app.main_window.window(auto_id='groupButton').click()
        self.group_editor = self.app.application.window(title='Group editor')
        self.group_editor.wait('visible')


    def close_group_editor(self):
        self.group_editor.close()




