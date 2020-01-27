values = ['{({[})[]}', '{({[]})[]}{}', ']{({[})[]}', '{({[()]})}']

def braces(values):
    result = ['YES' for _ in range(len(values))]
    for i in range(len(values)):
        trace = []
        for val in values[i]:
            if val == '{':
                trace.append('}')
            elif val == '(':
                trace.append(')')
            elif val == '[':
                trace.append(']')
            else:
                if len(trace) != 0 and val == trace[-1]:
                    trace.pop()
                else:
                    result[i] = 'NO'
                    break
        if len(trace) != 0:
            result[i] = 'NO'
    return result

print(braces(values))
