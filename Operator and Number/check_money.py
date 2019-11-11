money = float(input("Amount to be paid >> "))

thousand = money // 1000
fivehundred = (money % 1000) // 500
hundred = ((money % 1000) % 500) // 100
fifty = (((money % 1000) % 500) % 100) // 50
twenty = ((((money % 1000) % 500) % 100)  % 50) // 20
ten = (((((money % 1000) % 500) % 100)  % 50) % 20) // 10
five = ((((((money % 1000) % 500) % 100)  % 50) % 20) % 10) // 5
two = (((((((money % 1000) % 500) % 100)  % 50) % 20) % 10) % 5) // 2
one = ((((((((money % 1000) % 500) % 100)  % 50) % 20) % 10) % 5) % 2) // 1
pointfive = (((((((((money % 1000) % 500) % 100)  % 50) % 20) % 10) % 5) % 2) % 1) // 0.5
pointtwofive = ((((((((((money % 1000) % 500) % 100)  % 50) % 20) % 10) % 5) % 2) % 1) % 0.5) // 0.25

print("B1000 =",int(thousand))
print("B500 =",int(fivehundred))
print("B100 =",int(hundred))
print("B50 =",int(fifty))
print("B20 =",int(twenty))
print("B10 =",int(ten))
print("B5 =",int(five))
print("B2 =",int(two))
print("B1 =",int(one))
print("B.50 =",int(pointfive))
print("B.25 =",int(pointtwofive))