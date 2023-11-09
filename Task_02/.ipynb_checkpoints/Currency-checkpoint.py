with open("CurrencyData.txt","r") as f:
    lines = f.readlines()

CurrencyDict = {}
for line in lines:
    parsed = line.split("\t")
    CurrencyDict[parsed[0]] = parsed[1]
    
amount = int(input("Enter the Amount you Want to Convert: "))
print("Enter the Name of Current you Want to Convert? Available Options: ")
[print(CurrencyName) for CurrencyName in CurrencyDict.keys()]
Currency = input("Enter the Current Name from the availabe Options: ")
print(f"{amount} PKR is equal to {amount * float(CurrencyDict[Currency])} {Currency}")