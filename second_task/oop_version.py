import statistics
import csv
from second_task.const import file_path

with open(file_path, "r", encoding="UTF-8") as f:
    data_values = [float(row[0]) for row in csv.reader(f)]


class DataSet:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return statistics.mode(self.data)

    def standard_deviation(self):
        return statistics.stdev(self.data)


statistics_calculator = DataSet(data_values)

print(f"Mean: {statistics_calculator.mean()}")
print(f"Median: {statistics_calculator.median()}")
print(f"Mode: {statistics_calculator.mode()}")
print(f"Standard Deviation: {statistics_calculator.standard_deviation()}")
