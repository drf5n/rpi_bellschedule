#!/usr/bin/python
import gpiozero
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--pulses",help="pulses to send", default=1, type=int)
parser.add_argument("--gpio",help="gpio pin", default=14, type=int)
parser.add_argument("--on",help="on time (ms)", default=250, type=int)
parser.add_argument("--delay",help="delay time (ms)", default=250, type=int)
args = parser.parse_args()


bell = gpiozero.Buzzer(args.gpio)

for pulse in range(args.pulses):
    bell.on()
    time.sleep(args.on/1000.0)
    bell.off()
    time.sleep(args.delay/1000.0)

