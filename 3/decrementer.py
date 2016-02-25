import redis
import time

conn = redis.Redis()

while True:

    cities = conn.keys()

    for city in cities:

        d = conn.hgetall(city)

        for ref in d:
            if int(d[ref]) > 1:
                count = int(d[ref])
                count -= 1
                d[ref] = str(count)

        conn.hmset(city,d)

    time.sleep(2)


