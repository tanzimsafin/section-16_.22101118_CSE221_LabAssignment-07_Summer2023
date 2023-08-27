with open('input2.txt', 'r') as input_file:
    n, m = input_file.readline().split()
    n, m = int(n), int(m)
    time = []
    for i in range(n):
        a, b = input_file.readline().split()
        a, b = int(a), int(b)
        time.append((a, b))
    time.sort(key=lambda x: x[1])

def intervals(interval_list, person):
    selected_list1 = []
    selected_list2 = []

    select1 = interval_list[0][1]
    select2 = -999
    selected_list1.append(interval_list[0])

    for i in range(1, len(interval_list)):
        start, end = interval_list[i]

        if start < select1 and start > select2:
            select2 = end
            selected_list2.append(interval_list[i])
        elif start < select2 and start >= select1:
            select1 = end
            selected_list1.append(interval_list[i])
        elif start >= select2:
            selected_list2.append(interval_list[i])
            select2 = end
        elif start < select1 and start < select2:
            continue

    selected_list1.extend(selected_list2)
    return selected_list1

with open('output2.txt', 'w') as output_file:
    result_intervals = intervals(time, m)
    output_file.write(f'{len(result_intervals)}\n')
