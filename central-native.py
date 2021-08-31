import collections

values = [47, 95, 88, 73, 88, 84]

print(len(values))
print(sum(values))

print(sum(values)/len(values))

values.sort()
if len(values) % 2 == 0:
    first_median = values[len(values) // 2]
    second_median = values[len(values) // 2 - 1]
    median = (first_median + second_median) / 2
else:
    median = values[len(values) // 2]
print(median)

data = collections.Counter(values)
data_list = dict(data)
max_value = max(list(data.values()))
mode_val = [num for num, freq in data_list.items() if freq == max_value]
if len(mode_val) == len(values):
    print ("no mode")
else:
    print(mode_val)