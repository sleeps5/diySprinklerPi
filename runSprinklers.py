import sys  #get variables from command line
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO libary
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

#Syntax for 9 zones pointing to the pins below
#python3 runSprinklers.py X X X X X X X X X
#select pins for sprinkler terminals
pins = [26,24,21,19,11,15,16,18,22]

# Set pins to be an output pin and set initial value to low (off)
for pin in pins:
 GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def runZone ( zone, time ):
 GPIO.output(zone, GPIO.HIGH) # Turn on
 sleep(time) # Sleep for arg passed in seconds
 GPIO.output(zone, GPIO.LOW) # Turn off
 sleep(1)

nodes = len(pins)
#argPassed = format(len(sys.argv))
#if int(argPassed) == int(nodes+1):
count = 0
while (count < nodes):
 current = pins[count]
 count += 1
 time = int(sys.argv[count])
 if time == 0:
  print ('Zone '+str(count)+' not run')
 else:
  print ('Zone '+str(count)+' run '+str(time)+' seconds')
  runZone ( current, time )
#else:
# print ('Number of nodes doesn''t match arguments. Passed: '+str(argPassed)+ ' need: '+str(nodes))
