from patient.patient_module import add_patient,display_patients,search_patient
from doctor.doctor_module import add_doctor,display_doctors
from appointment.appointment_module import book_appointment,show_appointments
from billing.billing_module import generate_bill


while True:

    print("\n========== hospital management system ==========")
    print("1. add patient")
    print("2. display patients")
    print("3. search patient")
    print("4. add doctor")
    print("5. display doctors")
    print("6. book appointment")
    print("7. show appointments")
    print("8. generate bill")
    print("9. exit")

    choice=input("enter your choice: ")

    match choice:

        case "1":
            add_patient()

        case "2":
            display_patients()

        case "3":
            search_patient()

        case "4":
            add_doctor()

        case "5":
            display_doctors()

        case "6":
            book_appointment()

        case "7":
            show_appointments()

        case "8":
            generate_bill()

        case "9":
            print("thank you")
            break

        case _:
            print("invalid choice")