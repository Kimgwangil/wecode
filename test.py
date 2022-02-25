def even(start, end):
    result = []
    for i in range(start, end+1):
        if i % 2 == 0 and i > 0:
            result.append(i)
    return result


print(even(1,50))

