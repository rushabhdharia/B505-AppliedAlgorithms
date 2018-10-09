#Reference - Thread/Discussion no @88 - on Piazza

def pavingRoad(n):
    if n<=0:
        return 0

    roadpaving = [0] * (n+1)
    roadpaving[0] = 1
    roadpaving[1] = 0
    for i in range(2, n+1):
        sum = 0
        if i >=2:
            sum += roadpaving[i-2]

        if i >=3:
            sum += roadpaving[i-3]
        if i >=5:
            sum += roadpaving[i-5]
        roadpaving[i] = sum
    print(roadpaving)
    return roadpaving[n]

print(pavingRoad(15))
