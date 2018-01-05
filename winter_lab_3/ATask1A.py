x = 1

def square_root(a):
    global x
    epsilon = 0.0000001
    while True:
        #print (x)
        y = ((x+(a/x))/2)
        if abs(y-x) < epsilon:
            break
        x = y
    return(x)

if __name__ == '__main__':
    print(square_root(256))