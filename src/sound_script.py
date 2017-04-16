#! /usr/bin/env python
# coding:utf-8

import sys
import os.path
import time
import RPi.GPIO as GPIO

if __name__ == ("__main__"):
  argv = sys.argv
  argc = len(argv)

  # 引数の確認
  if (argc != 2):
    print 'usage: python %s filename' % argv[0]
    quit()

  # ファイルの存在チェック
  if not os.path.exists(argv[1]):
    print 'file "%s" is not found' % argv[1]
    quit()

  BZ1 = 4    # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定

  tonename = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#')
  toneall = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'Lah', 'La#h', 'Sih', 'Doh', 'Do#h', 'Reh', 'Re#h', 'Mih', 'Fah', 'Fa#h', 'Soh', 'So#h', 'Lahh')

  freq_dict = {}
  freq_base = 220.0    # 220Hz(低いラの音)

  # 2オクターブ分の周波数情報を作成
  for i in range(0, len(toneall)):
    freq_dict[toneall[i]] = freq_base * (2 ** (i/float(len(tonename))))
    #print '%3s : %.1f Hz' % (tonename[i%len(tonename)], freq_dict[toneall[i]])

  # ファイルを読み込む
  f = open(argv[1])
  soundsall = f.readlines()
  f.close()

  buzzer = GPIO.PWM(BZ1, freq_base)
  buzzer.start(50)    # デューティ比 50 でPWM出力開始

  # 音を鳴らす
  try:
    for line in soundsall:
        sounds = line.split(',')
        print sounds
        for tone in sounds:
          if tone in freq_dict:
            buzzer.ChangeFrequency(freq_dict[tone])
            time.sleep(0.2)

  except KeyboardInterrupt:
    print 'key interrupt'

  buzzer.stop()
  GPIO.cleanup()
