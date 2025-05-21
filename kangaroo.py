import copy
class Kangaroo:
    def __init__(self, name):
        self.name=name
        self.pouch_contents = []
    def __str__(self):
        s= f'{self.name}, pouch contents: \n'
        for obj in self.pouch_contents:
            s+= ('    '+ object.__str__(obj))
        return s
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
kanga=Kangaroo('kanga')
roo=Kangaroo('roo')
kanga.put_in_pouch(roo)
kanga.put_in_pouch('keys')
print(kanga)