import argparse
import time
import subprocess
import json
import numpy as np
'''
Josh this is hacky, env that runs this py script needs the pcds_conda env 
'''


def main():
  argparser = argparse.ArgumentParser()
  argparser.add_argument("-t", "--sample_time", help="time in seconds to sample", type=float)
  argparser.add_argument("-f", "--file_name", help="file out name", type=str)

  args = argparser.parse_args()

  data = np.zeros((1000, 2))

  startTime = time.time()

  should_read = lambda : ((time.time() - startTime) < args.sample_time)
  i = 0
  while (should_read()):
    process = subprocess.Popen(['ads-async get --add-route plc-tst-proto4 MAIN.fbPowerMeter.fVoltage'], \
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    data[i, 0] = json.loads(out.decode('utf-8'))['MAIN.fbPowerMeter.fVoltage'][0]
    data[i,1] = time.time() - startTime
    print(data[i, 0])
    i = i + 1
  data = data[:i]
  print(data)
  data.tofile(args.file_name, sep=",")


if __name__ == "__main__":
  main( )