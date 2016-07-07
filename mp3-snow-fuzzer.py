app = "snow/Player.exe"
file_list = ["hymn.mp3", "vodka.mp3", "eagleheart.mp3"]
output = "fuzz.mp3"

number_tests = 1000
number_crashes = 0

import math
import random
import subprocess
import time

for i in xrange(number_tests):
    file_test = random.choice(file_list)
    buf = bytearray(open(file_test, 'rb').read())
    fuzz_factor = random.randrange(100, 1000)

    # start Charlie Miller code
    numwrites = random.randrange(math.ceil((float(len(buf)) / fuzz_factor))) + 1

    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)
    # end Charlie Miller code

    open(output, 'wb').write(buf)

    process = subprocess.Popen([app, output])

    time.sleep(1)
    crashed = process.poll()
    
    if crashed:
        number_crashes += 1
        print "crashes: " + str(number_crashes)
    else:
        process.terminate()
