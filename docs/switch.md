# スイッチの押下を検出する
## 制御プログラムの作成
### スイッチ押下検出プログラム

Pythonを使ってスイッチの押下を検出するプログラム switch.py を作成します。

```python
#! /usr/bin/env python
# coding:utf-8

import RPi.GPIO as GPIO
import time

if __name__ == ("__main__"):
  SW1 = 21    # SW1 --> GPIO29(BCM:21,Physical:40)

  GPIO.setmode(GPIO.BCM)    # BCMのポート番号を使用
  GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # SW1を入力に設定、内部プルアップ抵抗を使用

  try:
    while True:
      state = GPIO.input(SW1)    # SW1の状態を読み込む(0:Low、1:High)
      print 'SW: %d' % state

      time.sleep(1)

  except KeyboardInterrupt:
    GPIO.cleanup()
```

switch.pyを実行してみましょう。ターミナルから以下のように実行します。
```bash
$ python switch.py
SW: 1
SW: 1
SW: 0
SW: 1
```

* スイッチの押下状態に応じて 0 または 1 が出力されます。Ctrl + c で終了します。
  * 0(Low) がスイッチオン、1(High) がスイッチオフの状態になっています。

INPUTモードでは、ハードウェアの状態(HIGH/LOW)を、プログラムで読み込むことができます。