class Doctor:
    def __init__(self, doctor_ID, name, gender, specialty, patient_log, patient_list, tariff):
        self.doctor_ID = doctor_ID
        self.name = name
        self.gender = gender
        self.specialty = specialty
        self.patient_log = patient_log
        self.patient_list = patient_list
        self.tariff = tariff

    def info(self):
        print("| - - - - - - - - - |\n")
        print("Name: ", self.name)
        print("ID: ", self.doctor_ID)
        print("Gender: ", self.gender)
        print("Field Specialty: ", self.specialty)
        print("Tariff: ", self.tariff)
        print("\n | - - - - - - - - - |")

    def update_data(self):

        if self.name != doctor_name_input:
            self.name = doctor_name_input
        elif self.name == doctor_name_input:
            print("Name input is the same with the old name")
        else:
            print("Error! Input is invalid!")

        if self.doctor_ID != doctor_ID_input:
            self.doctor_ID = doctor_ID_input
        elif self.doctor_ID == doctor_ID_input:
            print("ID input is the same with the old ID!")
        else:
            print("Error! Input is invalid!")

        if self.gender != doctor_gender_input:
            self.gender = doctor_gender_input
        elif self.gender == doctor_gender_input:
            print("Gender input is the same with the old gender!")
        else:
            print("Error! Input is invalid!")

        if self.specialty != doctor_specialty_input:
            self.specialty = doctor_specialty_input
        elif self.specialty == doctor_specialty_input:
            print("Field specialty input is the same with the old field specialty!")
        else:
            print("Error! Input is invalid!")

        if self.tariff != doctor_tariff_input:
            self.tariff = doctor_tariff_input
        elif self.tariff == doctor_tariff_input:
            print("Tariff input is the same with the old tariff!")
        else:
            print("Error! Input is invalid!")
    
    def pet_check(pet.health_status):
        pet.health_status = pet_status_input
        if pet.health_status == 1:
            pet.health_status == "Health"
            return
        elif pet.health_status == 2:
            pet.health_status == "Sick"
            return
        elif pet.health_status == 3:
            pet.health_status == "Dead"
            return
        else:
            print("Input is invalid!")


#INI UNTUK DATABASE PATIENT LIST
patient_data = {}
Patients = ["Patient1", "Patient2", "Patient3"]
#INI UNTUK INPUT DAN UPDATE KE PATIENT LIST
for Patient in Patients:
    pat_data: input(f"Input the data for {Patient}: ")
    patient_data[Patient] = pat_data

    def patient_info(pet.name, pet.pet_ID, pet.species, pet.race, pet.gender, pet.age, pet.health_status):
        print("| - - - - - - - - - |\n")
        print("Pet Name: ", pet.name)
        print("Pet ID: ", pet.pet_ID)
        print("Pet Gender: ", pet.gender)
        print("Pet Species: ", pet.species)
        print("Pet Race: ", pet.race)
        print("Pet Age: ", pet.age)
        print("Pet Health Status", pet.health_status)
        print("\n | - - - - - - - - - |")
