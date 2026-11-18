from dao.datadao import select,savestudent,getbyname,deletebyname,update
while True:

    print("1. insert")
    print("2. show all data")
    print("3. Get by name")
    print("4. delete by name")
    print("6. exit")
    choice=int(input("enter your choice"))
    match choice:
        case 1:
            print("insert data")
            name=input("enter your name")
            marks=int(input("enter your marks"))
            age=int(input("enter your age"))
            savestudent(name,marks,age)
            print("data iserted")
        case 2:
            print("show all data")
            print(select())
        case 3:
            print("Get by name")
            name=input("enter your name")
            print(getbyname(name))
        case 4:
            print("Delete by name")
            name=input("enter your name")
            print(deletebyname(name),"record affected")
        case 5:
            print("update")
            print(update(name,marks,age,sname))
        case 6:
            break
