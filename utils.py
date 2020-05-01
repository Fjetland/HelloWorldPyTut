def find_max(list):
    max_num = list[0]
    for num in list[1:]:
        if num > max_num:
            max_num = num
    return max_num
