inf = float('inf')
switches = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]
unique_clock_switch = [1, 4, 9]
unique_clock = [11, 12, 13]

def is_aligned_clock(clock) :
    for time in clock : 
        if time != 12 :
            return False
    return True

def push_switch(clock, switch_num):
    for i in range(len(switches[switch_num])) :
        clock[switches[switch_num][i]] += 3
        if clock[switches[switch_num][i]] == 15 : 
           clock[switches[switch_num][i]] = 3

def match_clock (clock, switch_num) :
    if switch_num == 10 :
        if is_aligned_clock(clock):
            return 0
        else : 
            return inf
    if switch_num in [1, 4, 9] :
        return match_clock(clock, switch_num+1)
    result = inf
    
    if len(switches[switch_num]) ==1 : 
        cnt =  4 - ((clock[switches[switch_num]]//3)% 4)
        return min(result, cnt + match_clock(clock, switch_num + 1))

    for i in range(4) :
        result = min(result, i + match_clock(clock, switch_num+1))
        push_switch(clock, switch_num)
    return result


c = int(input())
for _ in range(c):
    clock = list(map(int, input().split()))
    if clock[8] != clock[12]:
        print(-1)
        continue
    prior_cnt = 0
    for i in range(len(unique_clock)):
        cnt = (4-clock[unique_clock[i]]//3)% 4
        prior_cnt+=cnt
        for j in range(cnt):
            push_switch(clock, unique_clock_switch[i])
    
    answer = match_clock(clock, 0)+ prior_cnt
    if answer == inf:
        print(-1)
    else :
        print(answer)

