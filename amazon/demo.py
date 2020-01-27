states, days, ans = [1,0,0,0,0,1,0,0], 1, [0, 1, 0, 0, 1, 0, 1, 0]

states2, days2, ans2 = [1, 1, 1, 0, 1, 1, 1, 1], 2, [0, 0, 0, 0, 0, 1, 1, 0]

states3, days3, ans3 = [1, 1, 1, 0, 1, 1, 1, 1], 3, [0, 0, 0, 0, 1, 1, 1, 1]

states4, days4, ans4 = [1, 1, 1, 0, 1, 1, 1, 1], 4, [0, 0, 0, 1, 1, 0, 0, 1]

# Here we use simple mechanical algorithm, that is just matches predefined states for cell compete
# Time complexity O(n*2) and Space complexity O(n)
def cellCompete(states, days):
    # prepare array of zeros and consider that edge values are 0, so we add them in advance
    final_state = [0 for _ in range(len(states)+2)]
    # iterate over each day of competition
    for day in range(days):
        # insert current states into prepared arr of zeroes, as we want to make it easier to estimate what cell wins in current competition
        final_state[1:-1] = states
        # loop over each state
        for i in range(0, len(states)):
            # if one of predefined states in competitions is matched, update cell with the winner value
            if [final_state[i], final_state[i+1], final_state[i + 2]] in [[1, 1, 0], [0, 1, 1], [1, 0, 0], [0, 0, 1]]:
                states[i] = 1
            else:
                states[i] = 0
    return states

print(cellCompete(states4, days4))