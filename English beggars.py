def beggars(values, n):
    output = []
    for i in range(n):
        indeces = list(range(i,len(values), n))
        total = 0
        for index in indeces:
            total += values[index]
        output.append(total)
    return output