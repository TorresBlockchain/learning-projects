# Exercise on exponent function

# print(2**3)  # the operation to do an exponent is **

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result


print(raise_to_power(17, 5))
