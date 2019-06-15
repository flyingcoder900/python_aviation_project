#  python_aviation_project
# This is some code that I am putting together while learning python.

# set up the show.

plane_models = ["C172", "PA28R", "C150"]
plane_payloads = [650, 900, 500]

print("Plane models: " + str(plane_models))
# plane = input("Enter plane Model: ")

pilot = int(input("Enter Pilot weight: "))
co_pilot = int(input("Enter Copilot weight: "))
passengers = int(input("Enter Passengers weight: "))
fuel = int(input("Enter Gallons: "))

fuel_weight = fuel * 6
max_payload = plane_payloads [1]
over_weight = False
pay_load = pilot + co_pilot + passengers + fuel_weight
excess_weight = pay_load - max_payload
fuel_removed = ((pay_load - max_payload) / 6)


print("Pay load: " + str(pay_load))

if pay_load >= max_payload:
    over_weight = True

if pay_load == max_payload:
    print("You are at max weight.")
    print("Be careful with high density altitude at Max weight. Have a safe flight and squawk VFR!")
elif pay_load <= max_payload:
    print("You're under weight by " + str(max_payload - pay_load) + " lbs.")
    print("Have a safe flight and squawk VFR!")
else:
    if over_weight is True:
        if pay_load - max_payload >= 200:
            print("You are seriously over weight. Do not go fly until removing " + str(excess_weight) + " lbs." )
        else:
            print("You're OVER weight by " + str(pay_load - max_payload) + " pounds.")
            print("You will need to carry " + str(round(fuel_removed)) + " less gallons of fuel.")
            print("This would put your fuel total at: " + str(round(fuel - fuel_removed)) + " gallons.")