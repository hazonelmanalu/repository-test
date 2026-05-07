# INITIALIZING SOME CLASSES
from Class.Pet import Pet
from Class.Owner import Owner
from Class.Doctor import Doctor
from Class.Room import Room
from Class.Treatment import Treatment
Pet1 = Pet("123", "Kitty", "Female", "Cat", "Anggora", 3, None)
Owner1 = Owner("O001", "Andre", "Male", "08989557173", Pet1)
Doctor1 = Doctor("123", "Dr. Tirta", "Male", "Dog", 1000000)
Room1 = Room("R001", "Kitty Room", 200000, 5, "Cat")
Treatment1 = Treatment("T001", 5, Owner1, Pet1, Doctor1, Room1)


def check_object_info(Object):
  Object.info()

def main():
  option = None
  while option not in ["1", "2", "3", "4", "5"]:
    print("=" * 5 + " Information Center " + "=" * 5)
    print("[1] Doctor(s)")
    print("[2] Patient(s)")
    print("[3] Room(s)")
    print("[4] Owner(s)")
    print("[5] Treatment(s)")
    print("=" * 30)
    option = input("Please Enter a chosen number: ")
  
  if option == "1":
    check_object_info(Doctor1)
  elif option == "2":
    check_object_info(Pet1)
  elif option == "3":
    check_object_info(Room1)
  elif option == "4":
    check_object_info(Owner1)
  elif option == "5":
    check_object_info(Treatment1)
  
  option1 = None
  while option1 not in ["1", "2"]:
    print("=" * 20)
    print("[1] Back to main menu")
    print("[2] Quit")
    print("=" * 20)
    option1 = input("Please Enter a chosen number: ")
  
  if option1 == "1":
    main()
  elif option1 == "2":
    pass

main()
    

  

