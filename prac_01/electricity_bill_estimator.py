"""
print("Electricity bill estimator\n")

price_per_kWh_in_cents = int(input("Enter cents per kWh: "))
daily_kWh_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
print(" ")

estimated_bill = (price_per_kWh_in_cents * daily_kWh_use * number_of_days) / 100
print("Estimated bill: ${:.2f}".format(estimated_bill))
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0\n")

tariff_choice = str(input("Which tariff? 11 or 31: "))
daily_kWh_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
print(" ")

if tariff_choice.upper() == "11":
    estimated_bill = ((TARIFF_11 * daily_kWh_use) * number_of_days)
    print("Estimated bill: ${:.2f}".format(estimated_bill))
else:
    estimated_bill = ((TARIFF_31 * daily_kWh_use) * number_of_days)
    print("Estimated bill: ${:.2f}".format(estimated_bill))