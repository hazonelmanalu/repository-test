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