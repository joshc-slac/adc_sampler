import argparse
import time
import subprocess
import json
import numpy as np
import pandas as pd
'''
Josh this is hacky, env that runs this py script needs the pcds_conda env 
'''

def main():
  argparser = argparse.ArgumentParser()
  argparser.add_argument("-t", "--sample_time", help="time in seconds to sample", type=float)
  argparser.add_argument("-f", "--file_name", help="file out name", type=str)

  args = argparser.parse_args()


  startTime = time.time()

  should_read = lambda : ((time.time() - startTime) < args.sample_time)
  i = 0

  f = open(args.file_name, "w")
  while (should_read()):
    data = []
    process = subprocess.Popen(['ads-async get --add-route plc-tst-proto4 MAIN.fbPowerMeter.fVoltage'], \
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    data.append(str(json.loads(out.decode('utf-8'))['MAIN.fbPowerMeter.fVoltage'][0]))
    process = subprocess.Popen(['ads-async get --add-route plc-tst-proto4 MAIN.fVoltageOther'], \
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    data.append(str(json.loads(out.decode('utf-8'))['MAIN.fVoltageOther'][0]))
    data.append(str(time.time() - startTime))
    line = ','.join(data)
    print(line)
    f.write(line + '\n')

  f.close()

if __name__ == "__main__":
  main( )