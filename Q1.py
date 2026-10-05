# IRCTC Senior Citizen / Female Passenger Eligibility

age = int(input("Enter passenger age: "))
gender = input("Enter gender (male/female): ").lower()
traveling_alone = input("Is the passenger traveling alone? (yes/no): ").lower()
tatkal = input("Is this a Tatkal ticket? (yes/no): ").lower()
blackout = input("Is the journey on a blackout festival holiday? (yes/no): ").lower()

senior_citizen = age >= 60
female_alone = gender == "female" and traveling_alone == "yes"
non_tatkal = tatkal == "no"
not_blackout = blackout == "no"

if (senior_citizen or female_alone) and non_tatkal and not_blackout:
    print("Passenger is eligible for special preference and ticket discount.")
else:
    print("Passenger is not eligible.")