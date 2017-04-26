# 圧電サウンダ(ブザー)で音を出す
## 制御プログラムの作成
### ラの音を出力するプログラム

圧電サウンダを使って音を出すプログラム sound_buzzer.py を作成します。
```bash
$ vi sound_buzzer.py
```

```python
#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def buzzer():
  BZ1 = 4                       # BZ1 --> GPIO7(BCM:4,Physical:7)

  GPIO.setmode(GPIO.BCM)        # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)     # BZ1をOUTPUTモード(出力モード)に設定
  buzzer = GPIO.PWM(BZ1, 440)   # BZ1の周波数設定(440Hz)

  buzzer.start(50)              # デューティ比 50 でPWM出力開始

  time.sleep(1)

  buzzer.stop()                 # PWM出力を停止

  GPIO.cleanup()                # GPIOポートの撤収処理

if __name__ == "__main__":
  buzzer()
```

sound_buzzer.pyを実行してみましょう。ターミナルから以下のように実行します。
```bash
$ python sound_buzzer.py
```

* ブザー音が1秒鳴り、終了します。
* ここでは、440Hzの音を1秒間出力しています。440Hzはラの音です。
  * 一般的に、20Hz〜20000Hz程度が人間の聴くことのできる音とされています。

### 音階を出力するプログラム

次に、音階を出力するプログラム sound_octave.py を作成します。
```bash
$ vi sound_octave.py
```

```python
#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def octave():
  BZ1 = 4                           # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)            # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)         # BZ1を出力に設定

  tonename = ['La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#']

  freq = 220.0                      # 220Hz(低いラの音)
  buzzer = GPIO.PWM(BZ1, freq)
  buzzer.start(50)                  # デューティ比 50 でPWM出力開始

  for i in range(0, 13):
    freq = 220.0 * (2 ** (i/12.0))  # 220 * (2 の i/12乗)
    print '%3s : %.1f Hz' % (tonename[i%12], freq)
    buzzer.ChangeFrequency(freq)    # 周波数を変更
    time.sleep(0.2)

  buzzer.stop()
  GPIO.cleanup()

if __name__ == "__main__":
  octave()
```

sound_octave.pyを実行してみましょう。ターミナルから以下のように実行します。
```bash
$ python sound_octave.py
```
* ブザー音が1オクターブ分鳴り、終了します。
  * 音を半音上げるためには、元の音に 2 の 1/12乗をかけた周波数を設定します。

### ターミナルに入力した音を鳴らすプログラム

ターミナルに入力したキーに応じて音を鳴らすプログラム sound_input.py を作成します。
```bash
$ vi sound_input.py
```

```python
#!/usr/bin/env python
# coding:utf-8

import time
import RPi.GPIO as GPIO

def input():
  BZ1 = 4                      # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)       # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定

  tonename = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#')
  toneall = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'Lah', 'La#h', 'Sih', 'Doh', 'Do#h', 'Reh', 'Re#h', 'Mih', 'Fah', 'Fa#h', 'Soh', 'So#h', 'Lahh')

  freq_dict = {}
  freq_base = 220.0            # 220Hz(低いラの音)

  for i in range(0, len(toneall)):
    freq_dict[toneall[i]] = freq_base * (2 ** (i/float(len(tonename))))
    #print '%3s : %.1f Hz' % (tonename[i%len(tonename)], freq_dict[toneall[i]])

  try:
    while 1:
      tone = raw_input()
      if tone in freq_dict:
        buzzer = GPIO.PWM(BZ1, freq_dict[tone])
        buzzer.start(50)       # デューティ比 50 でPWM出力開始
        time.sleep(0.5)
        buzzer.stop()
      else: 
        print 'not found'

  except KeyboardInterrupt:
    print 'key interrupt'

  GPIO.cleanup()

if __name__ == "__main__":
  input()
```

sound_input.pyを実行してみましょう。ターミナルから以下のように実行します。
```bash
$ python sound_input.py
Do  # Do と入力して Returnキー
Re
Lahh
```
* キー入力待ち状態になります。Do、Re、Sih、So#h など好きな音をキー入力してみましょう。
  * 低いLa(La) から 高いLa(Lahh) までの2オクターブ分を準備しています。
* 入力したキーの音が鳴ります。Ctrl + c でプログラムを終了します。

### 音階のテキストファイルを入力して、音を鳴らすプログラム

最後に、音階の書かれたテキストファイルを読み込んで、音を鳴らすプログラム sound_script.py を作成します。
```bash
$ vi sound_script.py
```

```python
#!/usr/bin/env python
# coding:utf-8

import sys 
import os.path
import time
import RPi.GPIO as GPIO

def script():
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

  BZ1 = 4                      # BZ1 --> GPIO7(BCM:4,Physical:7)
  GPIO.setmode(GPIO.BCM)       # BCMのポート番号を使用
  GPIO.setup(BZ1, GPIO.OUT)    # BZ1を出力に設定

  tonename = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#')
  toneall = ('La', 'La#', 'Si', 'Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'So', 'So#', 'Lah', 'La#h', 'Sih', 'Doh', 'Do#h', 'Reh', 'Re#h', 'Mih', 'Fah', 'Fa#h', 'Soh', 'So#h', 'Lahh')

  freq_dict = {}
  freq_base = 220.0            # 220Hz(低いラの音)

  # 2オクターブ分の周波数情報を作成
  for i in range(0, len(toneall)):
    freq_dict[toneall[i]] = freq_base * (2 ** (i/float(len(tonename))))
    #print '%3s : %.1f Hz' % (tonename[i%len(tonename)], freq_dict[toneall[i]])

  # ファイルを読み込む
  f = open(argv[1])
  soundsall = f.readlines()
  f.close()

  buzzer = GPIO.PWM(BZ1, freq_base)
  buzzer.start(50)             # デューティ比 50 でPWM出力開始

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

if __name__ == "__main__":
  script()
```

sound_script.pyを実行してみましょう。src下にあるDoremi.txt を実行してみます。ターミナルから以下のように実行します。
```bash
$ python sound_script.py Doremi.txt
```
* ドレミの歌のメロディが流れます。
  * Doremi.txt は以下のようなファイルになっています。
音階の名前をカンマで区切って並べています。

```
Do,Do,Do,Re,Mi,Mi,Mi,Do,Mi,Mi,Do,Do,Mi,Mi,Mi,Mi,
Re,Re,Re,Mi,Fa,Fa,Mi,Re,Fa,Fa,Fa,Fa,Fa,Fa,Fa,Fa,
```

* 途中で終了する場合は、Ctrl + c を入力してください。
* テキストファイルは自由に作成してメロディを鳴らすことができますので、挑戦してみてください。