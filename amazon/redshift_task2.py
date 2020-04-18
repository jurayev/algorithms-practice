def solution(ranks):
    result = 0
    soldiers = 0
    sorted_ranks = sorted(ranks)
    for i in range(len(sorted_ranks) - 1):
        if sorted_ranks[i] == sorted_ranks[i+1] - 1:
            result += 1 + soldiers
            soldiers = 0
        elif sorted_ranks[i] == sorted_ranks[i+1]:
            soldiers += 1
        else:
            soldiers = 0
    return result

test = [5,4,4,3,3,3,1,1,0,0]

print(solution(test))