import os
import time

while True:
    os.system('sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches"')
    time.sleep( 180 ) # 3 min
    print("running succesfully")
