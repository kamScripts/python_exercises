import copy
class Kangaroo:
    def __init__(self, name, contents=None):
        self.name=name
        self.pouch_contents = [] if contents is None else contents
    def __str__(self):
        s= f'{self.name}, pouch contents: \n'
        for obj in self.pouch_contents:
            s+= ('    '+ obj.__str__()+',')
        return s
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
kanga=Kangaroo('kanga')
roo=Kangaroo('roo')
roo.put_in_pouch('car')
kanga.put_in_pouch('keys')
kanga.put_in_pouch(roo)

print(kanga)