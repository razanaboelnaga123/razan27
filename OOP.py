class MagicalContact:
    def _init_(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

  
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

   
    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

   
    def describe(self):
        return f"Name: {self._name}, Email: {self.email}, Phone: {self._phone_number}"


# WizardOrWitch class
class WizardOrWitch(MagicalContact):
    def _init_(self, name, email, phone_number, wand, house):
        super()._init_(name, email, phone_number)

        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house not in valid_houses:
            raise ValueError("Invalid house! Must be Gryffindor, Hufflepuff, Ravenclaw, or Slytherin.")

        self.__wand = wand  
        self.__house = house

    def get_wand(self):
        return f"{self._wand['length']}, {self.wand['wood']}, {self._wand['core']}"

    def get_house(self):
        return self.__house

    def describe(self):
        base_description = super().describe()
        wand_details = self.get_wand()
        return f"{base_description}, Wand: {wand_details}, House: {self.__house}"


# MagicalCreature 
class MagicalCreature(MagicalContact):
    def _init_(self, name, email, phone_number, species, is_tame):
        super()._init_(name, email, phone_number)
        self.__species = species
        self.__is_tame = is_tame

    def get_species(self):
        return self.__species

    def is_tame(self):
        return self.__is_tame

    def describe(self):
        base_description = super().describe()
        tame_status = "Tame" if self.__is_tame else "Not Tame"
        return f"{base_description}, Species: {self.__species}, Tame: {tame_status}"


# MagicalContactBook Class
class MagicalContactBook:
    def _init_(self):
        self.__contacts = []

    def add_contact(self, contact):
        if isinstance(contact, MagicalContact):
            self.__contacts.append(contact)
        else:
            raise TypeError("Only MagicalContact or its subclasses can be added.")

    def list_contacts(self):
        for contact in self.__contacts:
            print(contact.describe())

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name() == name:
                return contact.describe()
        return "Contact Not Found"

if __name__ == "__main__":
    wand = {"core": "Phoenix feather", "wood": "Holly", "length": "11 inches"}
harry = WizardOrWitch("Harry Potter", "harry@hogwarts.com", "+44 987654321", wand, "Gryffindor")
razan = MagicalCreature("Razan AboElNaga", "razan@magicalcreatures.com", "+44 123456789", "Hippogriff", True)

    
book = MagicalContactBook()
book.add_contact(harry)
book.add_contact(razan)

print("All Contacts:")
book.list_contacts()

print("\nSearch for Razan:")
print(book.find_contact("Razan AboElNaga"))