def solution(participant, completion):
    participant.sort()
    completion.sort()

    i = 0
    while True:
        try:
            if participant[i] == completion[i]:
                i = i + 1
            else:
                return participant[i]
        except IndexError:
            break

    return participant[i]
