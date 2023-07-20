import pandas as pd
from pathlib import Path

# reference to csv file to read
budget_csv = "Resources/budget_data.csv"

budget_df = pd.read_csv(budget_csv)

budget_df.head()
print(budget_df)

# Total number of months included in the set.
num_months = budget_df["Date"].count()
print(f"Total number of months: {num_months}")

#total amount of profit or losses over the period (sum)
net_total = budget_df["Profit/Losses"].sum()
print(f"Net total amount of profit/losses: ${net_total}")

difference = budget_df['Profit/Losses'].diff()
budget_df["Difference"] = difference

# Sum the difference in the Difference column.
sum_of_differences = budget_df["Difference"].sum()

# Figure out the number of difference values in the Difference column.
num_of_differences = budget_df["Difference"].count()

# Calculate average of changes.
average_of_changes = sum_of_differences / num_of_differences

#PRINTING BELOW
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {num_months}")
print(f"Total: {net_total}")
print(f"Average Change:  {average_of_changes}")
print(f"Greatest Increase in Profits: {date}  ({GreatestIncrease})")
print(f"Greatest Decrease in Profits: {date} ({GreatestDecrease})")

#Saving to a txt file
text_file = open("PyBank_Results.txt", "w")
with open("PyBank_Results.txt", "w") as text_file:
    print("Financial Analysis" + '\n' +
    ("-"*25) + '\n' +
    (f"Total Months: {Months}") + '\n' +
    (f"Total: {Total_Funds}") + '\n' +
    (f"Average Change:  {Average}") + '\n' +
    (f"Greatest Increase in Profits: {Gi_Date}  ({GreatestIncrease})") + '\n' +
    (f"Greatest Decrease in Profits: {Gd_Date} ({GreatestDecrease})"), file=text_file)
text_file.close()