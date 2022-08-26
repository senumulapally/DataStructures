import collections

# Initialize deque:
dq = collections.deque([4, 5, 6])
print(dq)
# Appending to right:
dq.append(9)
print(dq)
# Appending to left:
dq.appendleft(12)
print(dq)
# Pop from right:
dq.pop()
print(dq)
# Pop from left:
dq.popleft()
print(dq)


