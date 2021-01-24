from prettytable import PrettyTable

def sortFunc(lst_process, lst_names):
    copy_names = lst_names[:]
    copy_lst = lst_process[:]
    new_lst = [[0, 0]]   #Initializing CPU
    minVal = min(copy_lst, key = lambda x : x[0])   # To Find Out if the Processes Arrive at 0 or not
    remVal = minVal[0]
    currentTime = remVal
    
    tempFunc = lambda x : x[1]

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
        #print(temp)

        minVal = min(temp, key = tempFunc)
        minVal_index = copy_lst.index(minVal)
        if minVal[1] != 0:
            new_lst += [[minVal[0], minVal[1]-1]]
            ready_que.append(copy_names[minVal_index])
            copy_lst[minVal_index][1] -= 1
            currentTime += 1
        else:
            copy_lst.pop(minVal_index)
            copy_names.pop(minVal_index)
        #print(new_lst)

    new_lst.pop(0)
    return new_lst, ready_que

num = int(input("Please Enter Number of Processes: "))
num = 5
# process_lst = [[2, 6], [5, 2], [1, 8], [0, 3], [4, 4]]
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

sorted_process_lst, new_process_names = sortFunc(temp_process_lst, process_names)

print("Order of Execution:", new_process_names)

new_process_lst = []
average_WT = 0
average_TAT = 0

for process_name, process in zip(process_names, process_lst):
    for time, executed_process in enumerate(new_process_names):
        if process_name == executed_process:
            completion_time = time + 1       
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

