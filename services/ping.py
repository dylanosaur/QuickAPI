from pythonping import ping
import time
from numpy import round


def run_ping(url, n):
    start = time.time()
    for i in range(n):
        ping(url)
    stop = time.time()
    print(f'{n} pings / {stop-start} s = {round(n/(stop-start), 2)} pings/second')
    return round(n / (stop - start), 2)


# 5000 pings / 4.582515716552734 s = 1091.1 pings/second localhost
# 500 pings / 10.62502908706665 s = 47.06 pings/second raspberrypi
# pings('localhost', 500)
