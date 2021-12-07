import heapq

def read_data():
    with open("test.txt") as f:
        timers = list(map(int, f.read().split(",")))
    return timers

def main():
    pq = read_data()
    heapq.heapify(pq)

    for i in range(256):
        while pq[0] == i:
            heapq.heappushpop(pq, i + 7)
            heapq.heappush(pq, i + 9)
    print(len(pq))

main()
