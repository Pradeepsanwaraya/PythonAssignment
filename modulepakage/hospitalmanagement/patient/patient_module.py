patients=[]

def add_patient():
    id=input("enter patient id: ")
    name=input("enter patient name: ")
    age=int(input("enter age: "))
    gender=input("enter gender: ")
    disease=input("enter disease: ")
    mobile=input("enter mobile number: ")

    patient={
        "id":id,
        "name":name,
        "age":age,
        "gender":gender,
        "disease":disease,
        "mobile":mobile
    }

    patients.append(patient)

    print("patient added successfully")


def display_patients():
    if len(patients)==0:
        print("no patients found")
    else:
        for patient in patients:
            print("--------------------")
            print("patient id:",patient["id"])
            print("patient name:",patient["name"])
            print("age:",patient["age"])
            print("gender:",patient["gender"])
            print("disease:",patient["disease"])
            print("mobile number:",patient["mobile"])


def search_patient():
    id=input("enter patient id: ")

    for patient in patients:
        if patient["id"]==id:
            print("--------------------")
            print("patient id:",patient["id"])
            print("patient name:",patient["name"])
            print("age:",patient["age"])
            print("gender:",patient["gender"])
            print("disease:",patient["disease"])
            print("mobile number:",patient["mobile"])
            return

    print("patient not found")