# LEDを光らせる

## 回路の作成
### 必要なもの

* LED
* 抵抗(1KΩ)
* ブレッドボード
* ジャンパワイヤー(メスオス) 2本

### ブレッドボード配線図

配線図の通りに配線していきます。

![breadboard_led](img/RPi3_breadboard_led.png) 

1. 配線図と同じ向きにRaspberry Piとブレッドボードを並べます。
2. LEDをブレッドボードに差し込みます。足の長い方を左側、短い方を右側に差し込みます。
3. 抵抗をブレッドボードに差し込みます。向きはどちらでもよいです。
4. 黒のジャンパワイヤーをブレッドボードとRaspberry PiのGPIOコネクタ(上段左から7番目)のGNDに差し込みます。
5. 赤のジャンパワイヤーを同様に、ブレッドボードとRaspberry PiのGPIOコネクタ(上段左から6番目)のGPIO18番ピンに差し込みます。

#### 注意点
* 配線を行う際には、Raspberry Piの電源はOFFにすることを推奨します。
(今回は起動の手間を省くため電源ONのままやってしまいます。間違えないように注意してください。)
* LEDには極性(+/-)があります。一般的には足の長い方が＋側(アノード)、足の短い方が−側(カソード)です。
間違えると点灯しません。壊れてしまうこともあります。
* 配線をする際には、マイナス側から作成し、最後にプラス側のピンを接続するようにします。
(回路が完成する前に電流が流れてしまうのを防ぐため)
* 電子工作は水分に非常に弱いです。金属部分が濡れないよう気をつけてください。

### 回路図

![circuit_led](img/RPi3_circuit_led.png)

上のブレッドボード配線図を回路図にすると、このようになります。
GPIOポートの18番ピンに、抵抗、LEDが接続されています。

## 制御プログラムの作成

Pythonを使ってLEDを点灯させるプログラム led.py を作成します。

```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

if __name__ == ("__main__"):

  #start
  LED1 = 4 # LED1 --> GPIO7

  GPIO.setmode(GPIO.BCM) # use GPIO Number
  GPIO.setup(LED1, GPIO.OUT) # set GPIO led output

  GPIO.output(LED1, GPIO.HIGH)
  time.sleep(2)

  GPIO.output(LED1, GPIO.LOW)

  GPIO.cleanup()
```

* RPi.GPIOモジュールを使用して、GPIOポートを制御します。
* LED1にはGPIO番号(BCM)を指定します。
* GPIO.setmode(GPIO.BCM) で、BCMのポート番号を使う設定にします。
* GPIO.setup(LED1, GPIO.OUT) で、GPIO7番ポートを出力設定にします。
* GPIO.output(LED1, GPIO.HIGH) で、ポートにHighの信号を出力します。
(LEDが点灯します。)
* GPIO.output(LED1, GPIO.LOW) で、ポートにLowの信号を出力します。
(LEDが消灯します。)
* GPIO.cleanup() で、GPIOポートの撤収処理を行います。

led.pyを実行してみましょう。
```bash
$ python led.py
```

* LEDが2秒点灯して終了します。

## 抵抗値の求め方



## ブレッドボードの使い方
ブレッドボードには、ミニブレッドボードと通常のブレッドボードの2種類があります。
上に記載したブレッドボード配線図では、どちらも同じ配線になっていました。

2種類のブレッドボードの違いは、通常のブレッドボードには上下2列に＋と−の列があることです。
これらを使うと、よりわかりやすく配線をすることができます。


## 電子回路図作成ツール Fritzing
ブレッドボード配線図や回路図はFritzingというアプリを使って作成しています。
無料でダウンロードできます。

http://fritzing.org/home/

![Fritzing](img/Fritzing_screenshot.png)

