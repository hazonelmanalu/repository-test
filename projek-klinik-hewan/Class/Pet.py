class Pet:
    pet_database = []

    def __init__(self, pet_ID, name, gender, species, race, age, health_status):
        self.pet_ID = pet_ID
        self.name = name
        self.gender = gender
        self.species = species
        self.race = race
        self.age = age
        self.health_status = health_status

        self.Owner = None
        self.AssignedDoctor = None
        self.Room = None

    def info(self):
        print(f"--- Pet Info ---")
        print(f"Name            : {self.name}")
        print(f"ID              : {self.pet_ID}")
        print(f"Species/Race    : {self.species} / {self.race}")
        print(f"Gender          : {self.gender}")
        print(f"Age             : {self.age}")
        print(f"Health Status   : {self.health_status}")
        
        if self.Owner != None:
            owner_name = self.Owner.name
        else:
            owner_name = "None"
            
        if self.AssignedDoctor != None:
            doctor_name = self.AssignedDoctor.name
        else:
            doctor_name = "None"
            
        if self.Room != None:
            room_name = self.Room.name
        else:
            room_name = "None"
        
        print(f"Owner   : {owner_name}")
        print(f"Doctor  : {doctor_name}")
        print(f"Room    : {room_name}")
        print("---------------------------")

    def tambah_data(self):
        Pet.pet_database.append(self)
        print(f"Data hewan '{self.name}' berhasil ditambahkan ke database!")

    def replace_data(cls, target_ID, new_pet_object):
        for i, pet in enumerate(cls.pet_database):
            if pet.pet_ID == target_ID:
                cls.pet_database[i] = new_pet_object
                print(f"[Sukses] Data hewan dengan ID '{target_ID}' telah diganti dengan '{new_pet_object.name}'.")
                return
        print(f"[Gagal] Hewan dengan ID '{target_ID}' tidak ditemukan.")

    def hapus_data(cls, target_ID):
        for pet in cls.pet_database:
            if pet.pet_ID == target_ID:
                cls.pet_database.remove(pet)
                print(f"[Sukses] Data hewan dengan ID '{target_ID}' berhasil dihapus.")
                return
        print(f"[Gagal] Hewan dengan ID '{target_ID}' tidak ditemukan.")

    def set_doctor(self, doctor):
        self.AssignedDoctor = doctor

    def set_room(self, room):
        self.Room = room
        
    def set_owner(self, owner):
        self.Owner = owner

# CLASS TEST
if __name__ == "__main__":
    # INSTANCE OF CLASS
    print("=" * 20 + " (Pet Info) " + "=" * 20)
    Pet1 = Pet("123", "Kitty", "Female", "Cat", "Anggora", 3, None)
    Pet1.info()

    # SET OWNER
    from Owner import Owner
    Owner1 = Owner("O001", "Andre", "Male", "08989557173", Pet1)
    Pet1.set_owner(Owner1)

    # SET DOCTOR
    from Doctor import Doctor
    Doctor1 = Doctor("123", "Dr. Tirta", "Male", "Dog", 1000000)
    Pet1.set_doctor(Doctor1)

    # SET ROOM
    from Room import Room
    Room1 = Room("R001", "Kitty Room", 100000, 5, "Cat")
    Pet1.set_room(Room1)

    # CHECKING THE INFO AGAIN AFTER SETTING OWNER, DOCTOR, AND ROOM
    print("=" * 10 + " (Pet Info After Some Settings) " + "=" * 10)
    Pet1.info()