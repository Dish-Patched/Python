def time(curr, explo):
    currHr, currMin, currSec = map(int, curr.split(":"))
    exploHr, exploMin, exploSec = map(int, explo.split(":"))

    currTotal = currSec + currMin * 60 + currHr * 3600
    exploTotal = exploSec + exploMin * 60 + exploHr * 3600

    diff = (exploTotal - currTotal + 86400) % 86400

    if diff < 0: diff += 3600 * 24

    diffHr = diff // 3600
    diffMin = (diff % 3600) // 60
    diffSec = diff % 60

    return f'{diffHr:02d}:{diffMin:02d}:{diffSec:02d}'


curr  = input().strip()
explo = input().strip()

a = time(curr, explo)
print(a)
