import csv
import statistics

from second_task.const import file_path

with open(file_path, "r", encoding="UTF-8") as f:
    data_values = [float(row[0]) for row in csv.reader(f)]


def mean(data):
    return statistics.mean(data)


def median(data):
    return statistics.median(data)


def mode(data):
    return statistics.mode(data)


def standard_deviation(data):
    return statistics.stdev(data)


print(f"Mean: {mean(data_values)}")
print(f"Median: {median(data_values)}")
print(f"Mode: {mode(data_values)}")
print(f"Standard Deviation: {standard_deviation(data_values)}")
