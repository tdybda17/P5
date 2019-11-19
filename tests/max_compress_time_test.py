import csv


def average(l):
    return sum(l) // len(l)


filenames = ['battery_test_time_results.txt',
             'battery_traning_time_results.txt',
             'cans_test_time_results.txt',
             'cans_training_time_results.txt',
             'glas_test_time_results.txt',
             'glas_training_time_results.txt']

__base_dir__ = '/Users/toby/Desktop/'
dir = 'results/'
source = __base_dir__ + dir
data = []

for filename in filenames:
    with open(source + filename, newline='') as csv_file:
        data.append(list(csv.reader(csv_file)))

diff_times = []
for i in range(len(data)):
    cur_list = data[i]
    for j in range(len(cur_list)):
        if j is not 0:
            diff_times.append(int(cur_list[j][2]))

print(diff_times)
print('average: ' + str(average(diff_times)))
print('max: ' + str(max(diff_times)))
diff_times.sort()
for i in range(len(diff_times) - 1, len(diff_times) - 10, -1):
    print(diff_times[i])
