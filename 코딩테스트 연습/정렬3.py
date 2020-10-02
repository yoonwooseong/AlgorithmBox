def solution(citations):
    citations.sort(reverse=True)
    if citations[-1] >= len(citations):
        return len(citations)
    for idx, val in enumerate(citations):
        if idx >= val:
            return idx
        
            
        

solution([3, 0, 6, 1, 5])