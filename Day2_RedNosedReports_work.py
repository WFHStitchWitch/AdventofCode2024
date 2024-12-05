import pandas as pd
import datetime

class RowOfDigits:
    def __init__(self, digits_str):
        self.digits = list(map(int, digits_str.split()))

    def check_increasing_order(self):
        return all(self.digits[i] < self.digits[i + 1] for i in range(len(self.digits) - 1))

    def check_decreasing_order(self):
        return all(self.digits[i] > self.digits[i + 1] for i in range(len(self.digits) - 1))

    def check_differences(self):
        return all(1 <= abs(self.digits[i + 1] - self.digits[i]) <= 3 for i in range(len(self.digits) - 1))

    # def problem_dampener_a(self):
    #     return all(self.digits[i] <= self.digits[i + 1] for i in range(len(self.digits) - 1))
    #
    # def problem_dampener_b(self):
    #     return all(self.digits[i] >= self.digits[i + 1] for i in range(len(self.digits) - 1))

    def count_unsafe_variance(self):
        return sum(not (1 <= abs(self.digits[i + 1] - self.digits[i]) <= 3) for i in range(len(self.digits) - 1))





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
    #fixed_by_dampener_a = row_obj.problem_dampener_a()
    #fixed_by_dampener_b = row_obj.problem_dampener_b()
    failed_variances = row_obj.count_unsafe_variance()

    if increasing_order and valid_differences:
        category = "Safe"
    elif decreasing_order and valid_differences:
        category = "Safe"
    else:
        category = "Unsafe"

    data.append([row_obj.digits, increasing_order, decreasing_order, valid_differences, failed_variances, category])

# Create DataFrame for visual inspection of errors to find where the logical conditions were failing
df = pd.DataFrame(data, columns=['Report', 'Increasing Order', 'Decreasing Order', 'Valid Differences', 'Failed Variances', 'Category'])
#print(df.head(5))
count_safe_reports = df['Category'].value_counts()
print(count_safe_reports)

# Export to CSV for visual inspection and create versions of exports
current_time = datetime.datetime.now()
filetimestamp = current_time.strftime("%H%M")
#df.to_csv(f'rednosereports_{filetimestamp}.csv', index=False)
