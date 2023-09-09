import heapq


def solution(jobs):
    answer = 0
    t = 0
    n = len(jobs)
    jobs.sort()
    heap = []

    while len(jobs) != 0 or len(heap) != 0:
        while len(jobs) != 0 and jobs[0][0] <= t:
            heapq.heappush(heap, jobs.pop(0)[::-1])

        if len(heap) == 0:
            t = jobs[0][0]
            continue

        process = heapq.heappop(heap)
        t += process[0]
        answer += t - process[1]

    return answer // n