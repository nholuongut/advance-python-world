import json
from typing import Any 

class User :
    def __init__(self, name,age) -> None:
        self.name = name 
        self.age = age

user= User('Max',25)

#### option 1

# # to serialize a object into json we have to define encoder function
# def encode_user(object):
#     #check object instance
#     if isinstance(object , User):
#         return {
#             'name': object.name ,
#             'age': object.age ,
#             object.__class__.__name__ : True
#         }
#     else:
#         raise TypeError("Object of type User is not json serializable")
    
# userJson = json.dumps(user , default=encode_user)
# print(userJson)

######## option 2

from json import JSONEncoder

# create a sub class using json encoder
class UserEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o , User):
            return {
            'name': o.name ,
            'age': o.age ,
            o.__class__.__name__ : True
        }

        return super().default(o)
    

userJson = json.dumps(user , cls=UserEncoder)
print(userJson)

######## json decoeder

def user_decoder(json_obj):
    if User.__name__ in json_obj:
        return User(
            name=json_obj['name'] ,
            age=json_obj['age']
        )
    return json_obj


user = json.loads(userJson , object_hook=  user_decoder)
print( type(user) , user.__dict__)










