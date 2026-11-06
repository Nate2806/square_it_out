startvalue=int(input("Enter the starting value: "))

endvalue=int(input("Enter the ending value: "))
#function name
def squaring(start,end):
    evensquares=[]
    oddsquares=[]
    for num in range(start,end+1):
        square=num**2
        if square%2==0:
            evensquares.append(square) #function body
        else:
            oddsquares.append(square)

    print("Even square list:",evensquares)
    print("Odd square list:",oddsquares) 

#fucntion call
squaring(startvalue,endvalue)