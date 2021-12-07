from collections import deque

def read_data():
    with open("input.txt") as f:
        timers = list(map(int, f.read().split(",")))
    return timers

def main():
    data = read_data()
    timers = [0] * 9 # key is timer, value is number of fish
    for x in data:
        timers[x] += 1

    timers = deque(timers)

    for _ in range(256):
        n_fish = timers.popleft()
        timers.append(n_fish)
        timers[6] += n_fish

    print(sum(timers))

main()
