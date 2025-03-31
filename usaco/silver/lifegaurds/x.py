balls = [1, 3, 5, 7, 9, 11, 13, 15]

for ball1 in balls:
    for ball2 in balls:
        for ball3 in balls:
            if ball1+ball2+ball3 == 30:
                print(ball1, ball2, ball3)
                break

print("failed")