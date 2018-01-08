
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

if __name__ == '__main__':
    import time
    start_time = time.time()
    print(fibonacci(20))
    end_time = time.time()
    print("Exec time:" ,end_time - start_time)