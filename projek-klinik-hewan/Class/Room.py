class Room:
    def __init__(self, room_code, name, stay_cost, capacity, specialty):
        self.room_code = room_code
        self.name = name
        self.stay_cost = stay_cost
        self.capacity = capacity
        self.specialty = specialty
        self.patients = []

    def info(self):
        print(f"--- Room Info ---")
        print(f"Code: {self.room_code} | Name: {self.name} | Specialty: {self.specialty}")
        print(f"Stay Cost: Rp {self.stay_cost:,}/day | Capacity: {self.capacity}")

    def update_data(self, stay_cost=None):
        if stay_cost:
            self.stay_cost = stay_cost

    def room_status(self):
        print(f"Room Status {self.name}: Occupied {len(self.patients)}/{self.capacity}")
        for pet in self.patients:
            print(f"- {pet.name}")

# CLASS TEST
if __name__ == "__main__":
    # INSTANCE OF CLASS
    Room1 = Room("R001", "Kitty Room", 200000, 5, "Cat")
    Room1.info()

    # SETTING A PATIENTS
    from Pet import Pet
    Pet1 = Pet("123", "Kitty", "Female", "Cat", "Anggora", 3, None)
    Pet2 = Pet("124", "Dante", "Male", "Dog", "Kintamani", 4, None)
    Room1.patients.append(Pet1)
    Room1.patients.append(Pet2)

    # CHECK OCCUPANCIES
    print("=" * 10 + " (Patients Info) " + "=" * 10)
    number = 0
    for patient in Room1.patients:
        number += 1
        print(f"Patient {number}: {patient.name}")