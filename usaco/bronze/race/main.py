# Race -- USACO 2020 January Bronze

K, N = [0,0]
Xs = []

with open("race.in", "r") as f:
    K, N = map(int, f.readline().strip().split())
    for _ in range(N):
        Xs.append(int(f.readline().strip()))



def simulate(K, X):
    time = 0
    speed = 0
    distance = 0

    reverse = False

    while distance < K or speed != X:
        time+=1

        sum_ = distance + ((speed - X) * (speed + X - 1)) / 2

        if sum_ >= K:
            reverse = True

        if reverse:
            speed-=1
        else:
            speed+=1

        distance+=speed

    return (time, speed)


print(simulate(K, Xs[1]))