def solution(genres, plays):
    answer = []
    h = {}
    for i in range(len(genres)):
        if genres[i] in h : 
            h[genres[i]] += plays[i]
        else : 
            h[genres[i]] = plays[i]
    numbers = [ _ for _ in range(len(genres))]
    s = list(zip(genres, plays, numbers))
    b = sorted(s, key = lambda x: (-h[x[0]], -x[1]))        
    answer = [a[2] for a in b]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))