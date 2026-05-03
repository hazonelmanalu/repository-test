class Pet:
    def __init__(self, pet_ID, name, gender, species, race, age, health_status):
        pet_ID.self = pet_ID
        name.self = name
        gender.self = gender
        species.self = species
        race.self = race
        age.self = age
        health_status.self = health_status

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
        
        if self.Owner:
            owner_name = self.Owner.name
        else:
            owner_name = "None"
        
        print(f"Owner   : {self.Owner}")
        print(f"Doctor  : {self.AssignedDoctor}")
        print(f"Room    : {self.Room}")
        print("---------------------------")

    def update_data():
        

    def set_doctor(self):
        self.AssignedDoctor = Doctor

    def set_room(self):
        self.Room = Room
