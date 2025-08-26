class MagicalContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Wizard(MagicalContact):
    def __init__(self, name, phone, wand_type, house):
        self.wand_type = wand_type
        self.house = house
        super().__init__(name, phone)


class MagicalCreature(MagicalContact):
    def __init__(self, name, phone, creature_type):
        self.creature_type = creature_type
        super().__init__(name, phone)

class MagicalContactBook:
    def __init__(self):
        self.list=[]
    def add(self,target):
        self.list.append(target)

    def view(self):
        for i in self.list:
            print(i.name)
    
dareen=Wizard("dareen",123,"nagical","Ravenclaw")
creature1=MagicalCreature("LAURY",1234,"Dog")
contact1=MagicalContact("KHALED",1234)

x=MagicalContactBook()
x.add(dareen)
x.add(contact1)
x.add(creature1)

x.view()