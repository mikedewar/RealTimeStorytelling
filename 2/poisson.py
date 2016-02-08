import numpy as np
import time
import sys
import json

rate = 2

while True:
    print json.dumps({"t": time.time()})
    sys.stdout.flush()
    time.sleep(np.random.exponential(rate))
