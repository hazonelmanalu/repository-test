class Owner:
    def __init__(self, owner_ID, name, gender, contact, OwnedPet):
        self.owner_ID = owner_ID
        self.name = name
        self.gender = gender
        self.contact = contact
        self.OwnedPet = OwnedPet
    def info(self):
        print("Owner ID: ", self.owner_ID)
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Contact: ", self.contact)
        print("Owned Pet: ", self.OwnedPet)
    def update_data(self):
        self.owner_ID = input("Enter new owner ID: ")
        self.name = input("Enter new name: ")
        self.gender = input("Enter new gender: ")
        self.contact = input("Enter new contact: ")
    def set_pet(self, OwnedPet):
        self.daftarHewan.append(OwnedPet)
    def delete_pet(self, OwnedPet):
        self.daftarHewan.remove(OwnedPet)
