amount = float(input("The initial investment amount >> "))
period = float(input("Number of years invested >> "))
rate = float(input("Interest rate per year (%) >> "))

print()

fv = amount * pow((1 + rate), period)

print("The future value of the investment money is: ",format(fv, ".2f"))