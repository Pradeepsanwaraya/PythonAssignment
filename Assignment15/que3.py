start=int(input("Enter first year: "))
end=int(input("Enter last year: "))

i=start
while i<=end:
    j=1
    while j<=1:
        if (i%4==0 and i%100!=0) or (i%400==0):
            print(i)
        j=j+1
    i=i+1