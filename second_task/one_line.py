import statistics
import csv
from const import file_path

with open(file_path, "r", encoding="UTF-8") as f:
    data_values = [float(row[0]) for row in csv.reader(f)]

print(f'Mean - {statistics.mean(data_values)}, Median - {statistics.median(data_values)}'
      f'\nMode -  {statistics.mode(data_values)}, Standard deviation {statistics.stdev(data_values)}')
