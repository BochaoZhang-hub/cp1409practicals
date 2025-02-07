print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = input("Which tariff? 11 or 31:")
daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
if tariff == "11":
    estimate_bill = TARIFF_11 * daily_use_in_kWh * number_of_days
else :
    estimate_bill = TARIFF_31 * daily_use_in_kWh * number_of_days
print(f"Estimated bill : {estimate_bill:.2f}")
