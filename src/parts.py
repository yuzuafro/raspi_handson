#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

# GPIOクラス
class GPIOSetting:
  def __init__(self):
    pass

  def start(self):
    GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用

  def stop(self):
    GPIO.cleanup()

# LEDクラス
class LED:
  def __init__(self):
    self.LED1 = 18    # LED1 --> GPIO1(BCM:18,Physical:12)
    GPIO.setup(self.LED1, GPIO.OUT)    # LED1を出力に設定

  def on(self):
    GPIO.output(self.LED1, GPIO.HIGH)    # ポートにHighの信号を出力(LEDが点灯します)

  def off(self):
    GPIO.output(self.LED1, GPIO.LOW)    # ポートにLowの信号を出力(LEDが消灯します)

# Buzzerクラス
class Buzzer:
  def __init__(self):
    self.BZ1 = 4    # BZ1 --> GPIO7(BCM:4,Physical:7)
    GPIO.setup(self.BZ1, GPIO.OUT)    # BZ1を出力に設定
    self.buzzer = GPIO.PWM(self.BZ1, 440)    # BZ1の周波数設定(440Hz)

  def on(self):
    self.buzzer = GPIO.PWM(self.BZ1, 440)    # BZ1の周波数設定(440Hz)
    self.buzzer.start(50)    # デューティ比 50 でPWM出力開始

  def off(self):
    self.buzzer.stop()    # PWM出力を停止

if __name__ == "__main__":
  gpioset = GPIOSetting()
  gpioset.start()

  led = LED()
  led.on()
  time.sleep(2)
  led.off()

  bz = Buzzer()
  bz.on()
  time.sleep(2)
  bz.off()

  gpioset.stop()
