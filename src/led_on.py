#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

if __name__ == "__main__":

  LED1 = 18    # LED1 --> GPIO1(BCM:18,Physical:12)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LED1, GPIO.OUT)

  GPIO.output(LED1, GPIO.HIGH)
  time.sleep(2)

  GPIO.output(LED1, GPIO.LOW)

  GPIO.cleanup()
