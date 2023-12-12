def is_mirror_number(num):
    mirror_dict = {'0': '0', '1': '1', '2': '5', '5': '2', '8': '8'}
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] not in mirror_dict or mirror_dict[num_str[i]] != num_str[len(num_str) - 1 - i]:
            return False
    return True
number = 321
result = is_mirror_number(number)

if result:
    print(f"{number} can be reversed to form a mirror number.")
else:
    print(f"{number} cannot be reversed to form a mirror number.")
