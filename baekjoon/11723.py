import sys

m = int(sys.stdin.readline())
s = set()
for i in range(m):
    nowString = sys.stdin.readline().strip()
    if nowString == "all":
        s = set([str(i) for i in range(1, 21)])
    elif nowString == "empty":
        s = set()
    else:
        now = nowString.split()
        cal = now[0]
        if cal == "add":
            nowNum = now[1]
            s.add(nowNum)

        elif cal == "remove":
            nowNum = now[1]
            s.discard(nowNum)

        elif cal == "check":
            nowNum = now[1]
            if nowNum in s:
                print(1)
            else:
                print(0)

        elif cal == "toggle":
            nowNum = now[1]
            if nowNum in s:
                s.discard(nowNum)
            else:
                s.add(nowNum)
