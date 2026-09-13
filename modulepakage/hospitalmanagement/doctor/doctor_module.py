doctors=[]

def add_doctor():
    id=input("enter doctor id: ")
    name=input("enter doctor name: ")
    specialization=input("enter specialization: ")
    experience=int(input("enter experience: "))
    fees=float(input("enter consultation fees: "))

    doctor={
        "id":id,
        "name":name,
        "specialization":specialization,
        "experience":experience,
        "fees":fees
    }

    doctors.append(doctor)

    print("doctor added successfully")


def display_doctors():
    if len(doctors)==0:
        print("no doctors found")
    else:
        for doctor in doctors:
            print("--------------------")
            print("doctor id:",doctor["id"])
            print("doctor name:",doctor["name"])
            print("specialization:",doctor["specialization"])
            print("experience:",doctor["experience"])
            print("consultation fees:",doctor["fees"])