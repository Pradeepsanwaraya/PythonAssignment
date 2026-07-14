pnr = input("Enter PNR: ")

if len(pnr) == 12 and pnr.startswith("PNR") and pnr[3:].isdigit():
    print("Valid PNR Number")
else:
    print("Invalid PNR Number")