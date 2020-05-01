def find_max(list):
    max = list[0]
    for num in list[1:]:
        if num > max:
            max = num
    return max