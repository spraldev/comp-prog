for _ in range(int(input())):
    N, M = map(int, input().split())
    matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

    final_p = True

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                continue

            col_sim = [[0] * M for _ in range(N)]
            row_sim = [[0] * M for _ in range(N)]


            for _ in range(j + 1):
                carry = 1
                for idx in range(M):
                    if row_sim[i][idx] == 0:
                        row_sim[i][idx] = carry
                        carry = 0
                        break
                    else:
                        row_sim[i][idx], carry = carry, 1



            for _ in range(i + 1):
                carry = 1
                for idx in range(N):
                    if col_sim[idx][j] == 0:
                        col_sim[idx][j] = carry
                        carry = 0
                        break
                    else:
                        col_sim[idx][j], carry = carry, 1


            P = True
            for k in range(N):
                for l in range(M):
                    if matrix[k][l] == 0 and col_sim[k][l] == 1:
                        P = False
                        break
                if not P:
                    break


            newP = True
            for k in range(N):
                for l in range(M):
                    if matrix[k][l] == 0 and row_sim[k][l] == 1:
                        newP = False
                        break
                if not newP:
                    break


            if not P and not newP:
                final_p = False
                break

        if not final_p:
            break

    print("yes" if final_p else "no")
