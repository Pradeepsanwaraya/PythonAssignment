pnr=input("Enter PNR: ")
if pnr[0] == 'P' and pnr[1] == 'N' and pnr[2] == 'R':

    i = 3

    while i < 12:
        if pnr[i] >= '0' and pnr[i] <= '9':
            i = i + 1
        else:
            print("Invalid PNR")
            break
    else:
        print("Valid PNR")

else:
    print("Invalid PNR")