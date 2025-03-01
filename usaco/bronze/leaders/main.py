N = int(input())
A = list(input())
E = list(map(int, input().split()))


firstG = A.index('G')
lastG = N - A[::-1].index('G') - 1

firstH = A.index('H')
lastH = N - A[::-1].index('H') - 1

gLeads = []

if E[firstG] >= lastG + 1:
    gLeads.append(firstG)

hLeads = []

if E[firstH] >= lastH + 1:
    hLeads.append(firstH)


g_value = gLeads[0] if gLeads else -1
h_value = hLeads[0] if hLeads else -1

A = A[:max(g_value, h_value)]
E = E[:max(g_value, h_value)]

for i in range(len(A)):
    if A[i] == 'G':
        for j in range(len(hLeads)):
            if E[i] >= hLeads[j] + 1:
                gLeads.append(i)
                break

    else:
        for j in range(len(gLeads)):
            if E[i] >= gLeads[j] + 1:
                hLeads.append(i)
                break



print(len(gLeads) * len(hLeads))