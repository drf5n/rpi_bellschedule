#!/usr/bin/python
import gpiozero
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--pulses",help="pulses to send", default=1, type=int)
parser.add_argument("--gpio",help="gpio pin", default=14, type=int)
parser.add_argument("--on",help="on time (ms)", default=250, type=int)
parser.add_argument("--delay",help="delay time (ms)", default=250, type=int)
parser.add_argument("--repeat",help="repetition groups", default=1, type=int)
parser.add_argument("--interval",help="delay time (ms)", default=500, type=int)
args = parser.parse_args()

bell = gpiozero.Buzzer(args.gpio)

for rep in range(args.repeat):
    if rep > 0:
        time.sleep(args.interval/1000.0)
    for pulse in range(args.pulses):
        if pulse > 0: 
            time.sleep(args.delay/1000.0)
        bell.on()
        time.sleep(args.on/1000.0)
        bell.off()
