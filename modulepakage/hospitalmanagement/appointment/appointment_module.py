appointments=[]

def book_appointment():
    appointmentid=input("enter appointment id: ")
    patientid=input("enter patient id: ")
    doctorid=input("enter doctor id: ")
    date=input("enter appointment date: ")
    time=input("enter appointment time: ")

    appointment={
        "appointmentid":appointmentid,
        "patientid":patientid,
        "doctorid":doctorid,
        "date":date,
        "time":time
    }

    appointments.append(appointment)

    print("appointment booked successfully")


def show_appointments():
    if len(appointments)==0:
        print("no appointments found")
    else:
        for appointment in appointments:
            print("--------------------")
            print("appointment id:",appointment["appointmentid"])
            print("patient id:",appointment["patientid"])
            print("doctor id:",appointment["doctorid"])
            print("appointment date:",appointment["date"])
            print("appointment time:",appointment["time"])