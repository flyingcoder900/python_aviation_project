#  python_aviation_project

# Que the music.

plane_models = ["C172M", "PA28R", "C150"]
plane_payloads = [650, 900, 500]

print("Plane models in Database:")

# for loop to retrieve and display plane models

for plane_list in plane_models:
    print(plane_list)

# Request user for aircraft type and convert to uppercase.
plane = input("Enter plane ICAO + Model Number: ")
plane = plane.upper()


# This will set the payload based off of the correlating payload if the plane is already in the system.

if plane in plane_models:
    max_payload = plane_payloads.pop(plane_models.index(plane))
    print("Your plane is set as a " + plane + ". With a max payload of " + str(max_payload) + "lbs.")

# Now define new plane if not listed.

if plane not in plane_models:
    print("The plane was not listed!")
    new_plane = plane
    plane_payloads.append(input("What is the payload of this plane: "))
    max_payload = int(plane_payloads[-1])
    plane_models.append(new_plane)
    print("Your plane is set as a " + plane_models[-1] + ". With a payload of " + str(plane_payloads[-1]) + "lbs.")

# Request User to enter weights for flight.

pilot = int(input("Enter Pilot weight: "))
co_pilot = int(input("Enter Copilot weight: "))
passengers = int(input("Enter Passengers weight: "))
fuel = int(input("Enter Gallons: "))

# Add up the weights and define variables. 

fuel_weight = fuel * 6
over_weight = True
pay_load = pilot + co_pilot + passengers + fuel_weight
excess_weight = pay_load - max_payload
fuel_removed = ((pay_load - max_payload) / 6)

# Final checks to make sure pilot is at appropriate weight.

print("Pay load: " + str(pay_load))

if pay_load >= max_payload:
    over_weight = True

if pay_load <= max_payload:
    over_weight = False
    print("You're under weight by " + str(max_payload - pay_load) + " lbs.")
    print("Have a safe flight and squawk VFR!")

if pay_load == max_payload:
    over_weight = False
    print("You are at max weight.")
    print("Be careful with high density altitude at Max weight. Have a safe flight and squawk VFR!")

else:
    if over_weight is True:
        if pay_load - max_payload >= 150:
            print("You are seriously over weight. Do not go fly until removing " + str(excess_weight) + " lbs.")
        else:
            print("You're OVER weight by " + str(pay_load - max_payload) + " pounds.")
            print("You will need to carry " + str(round(fuel_removed)) + " less gallons of fuel.")
            print("This would put your fuel total at: " + str(round(fuel - fuel_removed)) + " gallons.")
