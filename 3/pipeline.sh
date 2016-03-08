#!/bin/bash


# I would actually run these in separate terminals rather than backgrounding the processes, so that I can easily see what's going on
./consume-1.usa.gov.sh | python insert_referrer_by_city.py &
python decrementer.py &
python city-bot-api.py &
