import pandas as pd


class RowOfDigits:
    def __init__(self, digits_str):
        self.digits = list(map(int, digits_str.split()))

    def check_increasing_order(self):
        return all(self.digits[i] < self.digits[i + 1] for i in range(len(self.digits) - 1))

    def check_decreasing_order(self):
        return all(self.digits[i] > self.digits[i + 1] for i in range(len(self.digits) - 1))

    def check_differences(self):
        return all(1 <= abs(self.digits[i + 1] - self.digits[i]) <= 3 for i in range(len(self.digits) - 1))


# intake rows from the data file
with open('Day2_puzzleInput1.txt', 'r') as file:
    rows = file.readlines()

# Creating objects for each row
row_objects = [RowOfDigits(row) for row in rows]

# Prepare data for DataFrame
data = []
for row_obj in row_objects:
    increasing_order = row_obj.check_increasing_order()
    decreasing_order = row_obj.check_decreasing_order()
    valid_differences = row_obj.check_differences()

    if increasing_order and valid_differences:
        category = "Safe"
    elif decreasing_order and valid_differences:
        category = "Safe"
    else:
        category = "Unsafe"

    data.append([row_obj.digits, increasing_order, decreasing_order, valid_differences, category])

# Create DataFrame
df = pd.DataFrame(data, columns=['Report', 'Increasing Order', 'Decreasing Order', 'Valid Differences', 'Category'])
#print(df)
count_safe_reports = df['Category'].value_counts()
print(count_safe_reports)
#df.to_csv(r'C:\Users\kelly\Desktop\tempReports.csv', mode='w', header=True, index=True)