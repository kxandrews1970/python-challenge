import pandas as pd

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
