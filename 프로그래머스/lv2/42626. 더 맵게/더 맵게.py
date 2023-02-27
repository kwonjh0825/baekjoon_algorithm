import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        answer += 1
    if scoville[0] >= K:
        return answer 
    else:
        return -1