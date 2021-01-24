from prettytable import PrettyTable

def sortFunc(lst_process, lst_names, time_quantum):
    copy_names = lst_names[:]
    copy_lst = lst_process[:]
    new_lst = [[0, 0]]   #Initializing CPU
    minVal = min(copy_lst, key = lambda x : x[0])   # To Find Out if the Processes Arrive at 0 or not
    remVal = minVal[0]
    currentTime = remVal

    ready_que = []

    #print(new_lst)
    while copy_lst:
        temp = []
        temp_names = []
        #print(currentTime)

        for val, name in zip(copy_lst, copy_names):
            at, bt = val
            if at <= currentTime:
                temp.append([at, bt])
                temp_names.append(name)

        minVal = temp[0]
        minVal_index = 0 
        if minVal[1] != 0:
            if minVal[1] < time_quantum:
                new_lst += [[minVal[0], 0, currentTime + minVal[1]]]
                copy_lst[minVal_index][1] = 0
                currentTime += minVal[1]
                data = copy_lst.pop(minVal_index)
                copy_lst.append([currentTime, data[1]])
            else:
                new_lst += [[minVal[0], minVal[1]-time_quantum, currentTime + time_quantum]]
                copy_lst[minVal_index][1] -= time_quantum
                currentTime += time_quantum
                data = copy_lst.pop(minVal_index)
                copy_lst.append([currentTime, data[1]])
            
            ready_que.append(copy_names[minVal_index])
            data = copy_names.pop(0)
            copy_names.append(data)
        else:
            copy_lst.pop(minVal_index)
            copy_names.pop(minVal_index)
        #print(new_lst)

    new_lst.pop(0)
    return new_lst, ready_que

time_quantum = int(input("Please Enter Time Quantum: "))
num = int(input("Please Enter Number of Processes: "))
arrival_time_lst = []
burst_time_lst = []
process_names = []

for i in range(num):
    arrival_time = int(input(f"Please Input Arrival time for P{i+1}: "))
    burst_time = int(input(f"Please Input Burst Time for P{i+1}: "))
    process_names.append(f"P{i+1}")
    arrival_time_lst.append(arrival_time)
    burst_time_lst.append(burst_time)

process_lst = list(zip(arrival_time_lst, burst_time_lst))
temp_process_lst = [list(i) for i in process_lst]

sorted_process_lst, new_process_names = sortFunc(temp_process_lst, process_names, time_quantum)

print("Order of Execution:", new_process_names)

new_process_lst = []
average_WT = 0
average_TAT = 0

for process_name, process in zip(process_names, process_lst):
    for time, executed_process in zip(sorted_process_lst, new_process_names):
        if process_name == executed_process:
            completion_time = time[2]

    TAT = completion_time - process[0]
    average_WT += TAT - process[1]
    average_TAT += TAT
    new_process_lst.append([process_name, process[0], process[1], completion_time, TAT, TAT - process[1]])
    

pt = PrettyTable()
pt.field_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "TAT", "WT"]
pt.add_rows(new_process_lst)
print(pt)
print(f"Average Waiting Time: {average_WT/num}")
print(f"Average Turn Around Time: {average_TAT/num}")

