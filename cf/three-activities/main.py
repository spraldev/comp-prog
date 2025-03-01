for _ in range(int(input())):
    n = int(input())
    skis = [[int(v),i] for i,v in enumerate(input().split())]
    movies = [[int(v),i] for i,v in enumerate(input().split())]
    games = [[int(v),i] for i,v in enumerate(input().split())]
    
    skis.sort(reverse=True)
    movies.sort(reverse=True)
    games.sort(reverse=True)
    

 
    anws = 0

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if skis[i][1] != movies[j][1] and skis[i][1] != games[k][1] and movies[j][1] != games[k][1]:
                    anws = max(anws, skis[i][0] + movies[j][0] + games[k][0])
        
    print(anws)