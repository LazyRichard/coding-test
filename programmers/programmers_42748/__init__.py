def solution(array, commands):
    answer = []
    
    for cmd in commands:
        cmd = list(map(lambda x: x - 1, cmd))
        sliced_arr = array[cmd[0]:cmd[1] + 1]
        sliced_arr.sort()

        answer.append(sliced_arr[cmd[2]])
        
    return answer