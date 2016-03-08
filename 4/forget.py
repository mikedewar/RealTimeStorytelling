import redis
import time
import numpy as np

conn = redis.Redis(db=1)

forgetting_rate = 0.1

while True:

    stations = conn.keys("*")

    for station in stations:

        pipe = conn.pipeline()
        with conn.pipeline() as pipe:
            while True:
                try:
                    pipe.watch(station)
                    d = pipe.hgetall(station)
                    pipe.multi()
                    for s,v in d.items():
                        count = int(v)
                        if count > 1:
                            to_remove = np.random.poisson(count * forgetting_rate)
                            print station,s,count-to_remove
                            pipe.hset(station,s,count-to_remove)
                    pipe.execute()
                    break
                except redis.WatchError:
                    print "interrupted!"
                    continue
    time.sleep(10)


