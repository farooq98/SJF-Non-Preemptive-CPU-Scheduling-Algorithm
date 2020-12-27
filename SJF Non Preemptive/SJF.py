from prettytable import PrettyTable

def sortFunc(lst):
    copy_lst = lst[:]
    new_lst = [[0, 0]]   #Initializing CPU
    minVal = min(copy_lst, key = lambda x : x[0])   # To Find Out if the Processes Arrive at 0 or not
    remVal = minVal[0]

    tempFunc = lambda x : x[1]

    #print(new_lst)
    while copy_lst:
        temp = []
        currentTime = sum(map(tempFunc, new_lst)) + remVal
        #print(currentTime)

        for index, val in enumerate(copy_lst):
            at, bt = val
            if at <= currentTime:
                temp.append([at, bt])
        #print(temp)

        minVal = min(temp, key = tempFunc)
        new_lst += [minVal]
        copy_lst.pop(copy_lst.index(minVal))
        #print(new_lst)

    new_lst.pop(0)
    return new_lst

num = int(input("Please Enter Number of Processes: "))
# num = 5
process_lst = [] # [[2, 6], [5, 2], [1, 8], [0, 3], [4, 4]]
process_names = [] # ["P1", "P2", "P3", "P4", "P5"]

for i in range(num):
    arrival_time = int(input(f"Please Input Arrival time for P{i+1}: "))
    burst_time = int(input(f"Please Input Burst Time for P{i+1}: "))
    process_names.append(f"P{i+1}")
    process_lst.append([arrival_time, burst_time])

sorted_process_lst = sortFunc(process_lst)
for i, val in enumerate(sorted_process_lst):
    idx = process_lst.index(val)
    sorted_process_lst[i].insert(0, process_names[idx])

new_process_lst = []
average_WT = 0
average_TAT = 0

for i, val in enumerate(sorted_process_lst):
    pno, arrival, burst = val
    completion_time = burst + arrival if len(new_process_lst) == 0 else burst + new_process_lst[i-1][3] if arrival < new_process_lst[i-1][3] else burst + new_process_lst[i-1][3] + (arrival - new_process_lst[i-1][3])
    TAT = completion_time - arrival
    WT = TAT - burst
    average_WT += WT
    average_TAT += TAT
    new_process_lst.append([pno, arrival, burst, completion_time, TAT, WT])

pt = PrettyTable()
pt.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "TAT", "WT"]
pt.add_rows(new_process_lst)
print(pt)
print(f"Average Waiting Time: {average_WT/num}")
print(f"Average Turn Around Time: {average_TAT/num}")

