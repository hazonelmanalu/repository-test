class Doctor:
    def __init__(self, doctor_ID, name, gender, specialty, tariff):
        self.doctor_ID = doctor_ID
        self.name = name
        self.gender = gender
        self.specialty = specialty
        self.patient_log = {}
        self.tariff = tariff
        self.patient_list = {}

    def info(self):
        print("| - - - - - - - - - |\n")
        print("Name: ", self.name)
        print("ID: ", self.doctor_ID)
        print("Gender: ", self.gender)
        print("Field Specialty: ", self.specialty)
        print("Tariff: ", self.tariff)
        print("\n | - - - - - - - - - |")

    def update_data(self, 
                    name, 
                    doctor_ID, 
                    gender, 
                    specialty, 
                    tariff):
        
        if not name.isalpha():
            print("Input name is invalid! \n" \
            "The name couldn't contains any numbers!")
        else:
            self.name = name

        if not doctor_ID.isdigit():
            print("Input ID is invalid! \n"
                  "Please input the ID in numbers!")
        else:
            self.doctor_ID = doctor_ID

        if gender.lower() not in ["female", "male"]:
            print("Input gender is invalid! \n" \
            "Please input 'Female' or 'Male'!")
        else:
            self.gender = gender

        if not specialty.lower() not in ["dog", 
                                         "cat", 
                                         "bird", 
                                         "rabbit", 
                                         "hamster"]:
            print("Input specialty is invalid! \n" \
            "Please input 'dog', 'cat', 'bird', 'rabbit', and 'hamster'!")
        else:
            self.specialty = specialty

        if not tariff.isdigit() or len(tariff) > 7 :
            print("Input tariff is invalid! \n" \
            "Please input in numbers and cannot be higher than 9.999.999!")
        else:
            self.tariff = tariff
        
    
    def pet_check(self, pet, pet_status_number):
        
        pet_status = {"1" : "Healthy",
                      "2" : "Sick",
                      "3" : "Dead"}

        if pet_status_number.digit() and pet_status_number in ["1", "2", "3"]:
            pet.health_status = pet_status[pet_status_number]

        else:
            print("Input is invalid!")

    def patient_info(self, pet):
        print("| - - - - - - - - - |\n")
        print("Pet Name: ", pet.name)
        print("Pet ID: ", pet.pet_ID)
        print("Pet Gender: ", pet.gender)
        print("Pet Species: ", pet.species)
        print("Pet Race: ", pet.race)
        print("Pet Age: ", pet.age)
        print("Pet Health Status", pet.health_status)
        print("\n | - - - - - - - - - |")

    def add_to_patient_list(self, pet):
        self.patient_list[pet.pet_ID] = pet
        print(f"Pasien {pet.name} telah terdaftar di bawah Dokter {self.name}.")

# CLASS TEST
if __name__ == "__main__":
    # INSTANCE OF CLASS
    print("=" * 20 + " (Doctor Info) " + "=" * 20)
    Doctor1 = Doctor("123", "Dr. Tirta", "Male", "Dog", 1000000)
    Doctor1.info()

    # SET PATIENT TO DOCTOR
    print("=" * 20 + " (Patient Info) " + "=" * 20)
    from Pet import Pet
    Pet1 = Pet("123", "Kitty", "Female", "Cat", "Anggora", 3, None)
    Doctor1.add_to_patient_list(Pet1)
    Doctor1.patient_info(Pet1)