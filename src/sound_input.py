#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def input():
  BZ1 = 4    # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定

  tonename = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#')
  toneall = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'Lah', 'La#h', 'Sih', 'Doh', 'Do#h', 'Reh', 'Re#h', 'Mih', 'Fah', 'Fa#h', 'Soh', 'So#h', 'Lahh')

  freq_dict = {}
  freq_base = 220.0    # 220Hz(低いラの音)

  for i in range(0, len(toneall)):
    freq_dict[toneall[i]] = freq_base * (2 ** (i/float(len(tonename))))
    #print '%3s : %.1f Hz' % (tonename[i%len(tonename)], freq_dict[toneall[i]])

  try:
    while 1:
      tone = raw_input()
      if tone in freq_dict:
        buzzer = GPIO.PWM(BZ1, freq_dict[tone])
        buzzer.start(50)    # デューティ比 50 でPWM出力開始
        time.sleep(0.5)
        buzzer.stop()
      else:
        print 'not found'

  except KeyboardInterrupt:
    print 'key interrupt'

  GPIO.cleanup()

if __name__ == "__main__":
  input()
