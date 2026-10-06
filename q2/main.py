import json

class UserManager:
    def __init__(self):
        self.users = []
        self.id0 = 0

    def add_user(self,name:str,age:int) -> dict:
        self.id0 += 1
        data = {
            'id':self.id0,
            'name':name,
            'age':age
        }
        self.users.append(data)
        return data

    def get_user(self,uid:int ) -> dict|None:
        for data in self.users:
            if data['id'] == uid:
                return data
        return None

    def edit_age(self,uid:int,age:int) -> bool:

        get_user = self.get_user(uid)
        if get_user is None:
            return False

        get_user['age'] = age
        return True



    def del_user(self,uid:int) -> bool:

        get_user = self.get_user(uid)
        if get_user is None:
            return False

        self.users.remove(get_user)
        return True

    def list_users(self) -> list:
        return self.users

    def save_all_json(self,title:str):
        with open(title, 'w',encoding="utf-8") as outfile:
            json.dump(self.users, outfile,ensure_ascii=False)

    def load_all_json(self,title:str):
        with open(title,encoding="utf-8") as json_file:
            self.users = json.load(json_file)

        if self.users:#这段判断是deepseek提醒我加上的()
            self.id0 = max(user['id'] for user in self.users)
        else:
            self.id0 = 0

