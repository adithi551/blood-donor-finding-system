import math
blood_banks = [
    {"name": "Red Cross Bank", "location": (2, 3), "stock": {"A+": 10, "B+": 5, "O+": 8}},
    {"name": "City Blood Bank", "location": (5, 7), "stock": {"A+": 4, "B+": 6, "O+": 2}},
    {"name": "LifeCare Bank", "location": (1, 1), "stock": {"A+": 7, "B+": 3, "O+": 6}}
]
def calculate_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

hospital_location = int(input("Enter hospital X: ")), int(input("Enter hospital Y: "))
blood_group = input("Enter required blood group: ")
units_needed = int(input("Enter units needed: "))
nearest_bank = None
min_distance = float('inf')
for bank in blood_banks:
    if blood_group in bank["stock"] and bank["stock"][blood_group] >= units_needed:
        dist = calculate_distance(hospital_location, bank["location"])
        if dist < min_distance:
            min_distance = dist
            nearest_bank = bank
if nearest_bank:
    print("\nNearest Blood Bank Found:")
    print("Name:", nearest_bank["name"])
    print("Distance:", round(min_distance, 2))
    print("Available Units:", nearest_bank["stock"][blood_group])
    choice = input("Send request? (yes/no): ")
    if choice.lower() == "yes":
        print("Request Accepted ✔")
        nearest_bank["stock"][blood_group] -= units_needed
        print("Updated Units:", nearest_bank["stock"][blood_group])
    else:
        print("Request Cancelled ❌")
else:
    print("No blood bank found with required units ❌")
    print("send request to the donor")
    