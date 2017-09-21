TARIFFS = {11 : 0.244618, 31 : 0.136928, 21: 0.213828, 1: 0.592384, 41: 0.293710}

print("Electricity bill estimator 3.0\n")
tariff_choice = int(input("Which tariff? {}, {}, {}, {} or {}: ".format(*TARIFFS.keys())))

while tariff_choice not in TARIFFS:
    print("Invalid choice")
    tariff_choice = int(input("Which tariff? {}, {}, {}, {} or {}: ".format(*TARIFFS.keys())))

daily_kWh_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
estimated_bill = ((tariff_choice * daily_kWh_use) * number_of_days)
print("Estimated bill: ${:.2f}".format(estimated_bill))