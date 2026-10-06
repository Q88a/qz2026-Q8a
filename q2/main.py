import json

class UserManager:
    def __init__(self):
        self.users = []
        self.id0 = 0
        self.data = {}


    def add_user(self,name:str,age:int) -> dict:
        self.id0 += 1
        self.data
        self.data['id'] =self.id0
        self.data['name'] = name
        self.data['age'] = age
        self.users.append(self.data)#怎么改呢
        print(self.data)
        return self.data

    def get_user(self,id:int ) -> dict|None:
        for data in self.users:
            if data['id'] == id:
                return data
        return

    def edit_age(self,id:int,age:int) -> bool:

        try:
            get_user = self.get_user(id)
            get_user['age'] = age
            return True

        except TypeError:
            return False

    def del_user(self,id:int) -> bool:
        try:
            get_user = self.get_user(id)
            self.users.remove(get_user)
            return True

        except TypeError:
            return False

    def list_users(self) -> list:
        return self.users

    def save_all_json(self,title:str):
        return

    def load_all_json(self,title:str):
        return

u1=UserManager()
u1.add_user('a',1)
print(u1.list_users())
u1.add_user('b',2)
print(u1.get_user(9))
print(u1.list_users())