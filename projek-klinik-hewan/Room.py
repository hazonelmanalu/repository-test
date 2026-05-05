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