import sys
i = 1
sum = 0
if len(sys.argv) == 1:
    print(f"{len(sys.argv) - 1}")
else:
    while i < len(sys.argv):
        sum += int(sys.argv[i])
    i += 1