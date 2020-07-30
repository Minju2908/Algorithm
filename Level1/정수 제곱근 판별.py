
import math

n = 3
a = math.sqrt(n)

if math.pow(math.trunc(a),2) == n:
    print(math.trunc(math.pow((a+1),2)))
else:
    print(-1)