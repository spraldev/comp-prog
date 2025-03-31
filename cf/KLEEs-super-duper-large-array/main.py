def ternary_search():
    l, r = 0, N #Adapt to your needs
    epsilon = 1e-9  # Define a small value for precision

    while r - l < epsilon:
        mid1 = l + (r - l) / 3
        mid2 = r - (r - l) / 3
        if f(mid1) < f(mid2): #This is for finding the maximum of f(x), change to > for minimum
            l = mid1
        else:
            r = mid2
    best = 0 #Change to float("inf") for minimum
    for i in range(int(l), int(r) + 1):
        best = max(best, f(i)) #Change to min(best, f(i)) for minimum
    return best

def f(x, a):
    