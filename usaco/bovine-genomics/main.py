N, M = [0, 0]

spotty = []
plain = []

with open("cownomics.in", "r") as f:
    N, M = map(int, f.readline().strip().split())

    for i in range(N):
        spotty.append(list(f.readline().strip()))
    
    for i in range(N):
        plain.append(list(f.readline().strip()))


final_num = 0

for i in range(M):
    for j in range(i +1, M):
        for k in range(j+ 1, M):

            spotty_tuples = {}
            success = True

            for l in range(N):
                spotty_tuples[(spotty[l][i], spotty[l][j], spotty[l][k])] = True

            for l in range(N):
                plain_tuple = (plain[l][i], plain[l][j], plain[l][k])

                try:
                    if spotty_tuples[plain_tuple]:
                        success = False
                        break
                except:
                    continue
            
            if success:
                final_num += 1
                

with open("cownomics.out", "w") as f:
    f.write(str(final_num) + "\n")
