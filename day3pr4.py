def add_binary(a, b):
    a_int = int(a, 2)
    b_int = int(b, 2)
    result_int = a_int + b_int
    result_binary = bin(result_int)[2:]
    return result_binary
a = "101"
b = "1101"
result = add_binary(a, b)
print(result)
