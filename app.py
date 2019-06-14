## python_aviation_project
##This is some code that I am putting together while learning python. 

pilot = int(input("Enter Pilot weight: "))
co_pilot = int(input("Enter Copilot weight: "))
passengers = int(input("Enter Passengers weight: "))
fuel = int(input("Enter Gallons: ")) * 6

pay_load = pilot + co_pilot + passengers + fuel

print("Pay load: " + str(pay_load))

if pay_load == 750:
    print("You are at max weight.")
    print("Be careful with high density altitude at Max weight. Have a safe flight and squawk VFR!")
elif pay_load <= 750:
    print("You're under weight by " + str(750 - pay_load) + " pounds.")
    print("Have a safe flight and squawk VFR!")
else:
    print("You're OVER weight by " + str(pay_load - 750) + "pounds.")
    print("You will need to take " + str((pay_load - 750) / 6) + " less gallons of fuel.")


