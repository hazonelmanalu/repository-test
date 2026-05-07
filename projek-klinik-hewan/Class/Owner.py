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

# CLASS TEST
if __name__ == "__main__":
    # INSTANCE OF CLASS
    O001 = Owner("O001", "Andre Puji", "laki laki", "085727626952", "Harimau")
    O002 = Owner("O002", "Haikal Wilhan", "laki laki", "089463992837", "kodok")
    O003 = Owner("O003", "Danu Rifai", "laki laki", "08637929028", "semut")
    O004 = Owner("O004", "Hazon el Manalu", "laki laki", "0876639302736", "nyamuk")
    O005 = Owner("O005", "Daffa Radix", "laki laki", "08157483990", "kutu")
    O006 = Owner("O006", "Justin", "laki laki", "08155748390", "mikroba berbahaya")

    # CHECKING INFO FOR EACH INSTANCES
    print("=" * 20 + " (O001) " + "=" * 20)
    O001.info()
    print("=" * 20 + " (O002) " + "=" * 20)
    O002.info()
    print("=" * 20 + " (O003) " + "=" * 20)
    O003.info()
    print("=" * 20 + " (O004) " + "=" * 20)
    O004.info()
    print("=" * 20 + " (O005) " + "=" * 20)
    O005.info()
    print("=" * 20 + " (O006) " + "=" * 20)
    O006.info()

