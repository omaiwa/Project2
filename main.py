class Driver:
    def __init__(self, name, laps):
        self.name = name
        self.laps = laps
        self.total = sum(laps)

    def __lt__(self, other):
        return self.total < other.total

n,k = [int(x) for x in input().split()]
arr =[]
for x in range(n):
    name = input()
    time = [int(x) for x in input().split()]
    arr.append(Driver(name, time))


print(min(arr).name)