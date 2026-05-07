class Treatment:
  def __init__(self, 
               treatment_code, 
               stay_period, 
               Customer,
               Patient,
               Doctor,
               Room):

    self.treatment_code = treatment_code
    self.stay_period = stay_period
    self.Customer = Customer
    self.Patient = Patient
    self.Doctor = Doctor
    self.Room = Room
    
    # tariffing
    if Room:
      self.tariff = stay_period * Room.stay_cost + Doctor.tariff
    else:
      self.tariff = Doctor.tariff
  
  def info(self):
    print(f"""
Treatment Code: {self.treatment_code}
Stay Period   : {self.stay_period} day(s)
Owner's Name  : {self.Customer.name}
Pet's Name    : {self.Patient.name}
Doctor's Name : {self.Doctor.name}
Room          : {self.Room.room_code} | {self.Room.name}
Total Tariff  : Rp{f"{self.tariff:,}".replace(",", ".")},00     
""")

# CLASS TEST
if __name__ == "__main__":
  # INITIALIZING SOME CLASSES FOR TREATMENT CLASS
  from Pet import Pet
  from Owner import Owner
  from Doctor import Doctor
  from Room import Room
  Pet1 = Pet("123", "Kitty", "Female", "Cat", "Anggora", 3, None)
  Owner1 = Owner("O001", "Andre", "Male", "08989557173", Pet1)
  Doctor1 = Doctor("123", "Dr. Tirta", "Male", "Dog", 1000000)
  Room1 = Room("R001", "Kitty Room", 200000, 5, "Cat")

  # INSTANCE OF CLASS
  print("=" * 10 + " (Treatment Info) " + "=" * 10)
  Treatment1 = Treatment("T001", 5, Owner1, Pet1, Doctor1, Room1)
  Treatment1.info()
  