def generate_bill():
    patientid=input("enter patient id: ")
    consultation=float(input("enter consultation charges: "))
    medicine=float(input("enter medicine cost: "))
    test=float(input("enter test charges: "))

    total=consultation+medicine+test

    print("--------------------")
    print("patient id:",patientid)
    print("consultation charges:",consultation)
    print("medicine cost:",medicine)
    print("test charges:",test)
    print("total bill:",total)