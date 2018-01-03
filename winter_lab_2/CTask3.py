def is_power(a,b):
    result = True
    if a>b:
        if a%b == 0:
            # Since a>b, we check for is_power(a/b,b)
            is_power(a/b, b)
        else:
            result = False
    return result


print(is_power(16,2))
print(is_power(16,3))