import collections
N, K = map(int, input().split())
container = collections.deque(map(int,input().split()))
count = 0
robot = collections.deque([0 for _ in range(2*N)])
print(robot)
while count >= K:
    count += 1
    container.append(container.popleft())
    robot.append(robot.popleft())
    