
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{

            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky numbers": [10, 14, 3]
        },
        {
            
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky numbers": [7, 13, 22]
        },
        {
            
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        
        for item in self._members:
            
            if item["id"] == member["id"]:
                return {"msj":"this member its allready created"}
            else:
                self._members.append(member)
                return None

        
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for indice, miembro in enumerate(self._members):
            if int(id) == miembro["id"]:
                self._members.pop(indice)
            else:
                return None
        return self._members


    def get_member(self, id):
        # fill this method and update the return
        member = list(filter(lambda item: item["id"] == id  , self._members))

        if len(member) == 0:

            return None
        else:
            return member[0]
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
