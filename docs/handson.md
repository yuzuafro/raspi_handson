# 本日のハンズオンについて
## 今日のゴール
「初めてのRaspberry Pi 電子工作」 LED＆ブザーを使って、IoTを体験しよう！
* Webブラウザから、Raspberry Pi に接続された LED やブザーを操作します。

## 今日やること
* sshやVNCを使用して、PCからリモートで Raspberry Pi を操作します。
* Raspberry Pi の GPIOポートを使用して、電子工作を体験します。
* Python を使って、部品を動作させるプログラムを作成します。
* Webブラウザから、Raspberry Pi にアクセスする環境を整えます。

## 持ち物が揃っているかの確認
### 本日お持ちいただいているもの
* PC
* Raspberry Pi 3 本体
* Raspbian OSインストール済みのmicroSDカード
* 電源アダプタ(またはmicroUSBケーブル+USB急速充電器)
* 電子工作部品一式(後ほど中身の確認をします。)

## 事前準備ができているかの確認
### WiFi接続と設定の確認
* 1人ずつRaspberry Piにディスプレイ、マウス、キーボードを接続して起動し、会場のWiFiに接続します。
* Raspberry Piのデスクトップ画面の右上の方にあるネットワーク設定のメニューから、会場のWiFiを選択してパスワードを入力します。

### MACアドレス、IPアドレスの確認
* ターミナルを起動し、ifconfig コマンドで、MACアドレス、IPアドレスを確認します。wlan0 のハードウェアアドレス(MACアドレス)、inetアドレス(IPアドレス)をメモします。
```bash
$ ifconfig
...
wlan0     Link encap:イーサネット  ハードウェアアドレス xx:xx:xx:xx:xx:xx 
          inetアドレス:192.168.xx.xx ブロードキャスト:192.168.0.255  マスク:255.255.255.0
...
```
* MACアドレスは常に同じ値ですが、IPアドレスは途中で変わってしまう可能性があります。  
その際はMACアドレスからIPアドレスを検索しますので、念のためMACアドレスもメモしています。

### Raspberry Piの設定
* 設定 → Raspberry Piの設定メニューを起動します。
    * システム
        * パスワードを変更(raspberry以外を推奨)
        * ホスト名を設定(raspberrypi以外を推奨)
            * hostname には "-"(ハイフン)以外の記号を使用することはできません。("_"アンダースコアなどは使用できません)
    * インターフェイス
        * SSH、VNC、リモートGPIO を有効にします。
        * (カメラ以外全て有効にしておいてよいと思います。)
    * ローカライゼーション
        * 4項目全て、日本に設定します。
* 再起動します。再起動できたら、シャットダウンして、PCからの確認に移ります。  
(問題なければ次の方に場所を譲りましょう。)

### PCからの接続の確認
#### sshの確認
* PCのターミナルアプリケーションを起動します。  
Windowsの人はTera TermやPuttyなどのアプリケーションを起動します。  
なければインストールしてください。  
Tera Term : https://ttssh2.osdn.jp/  
Putty : http://www.putty.org/  
Macの人はターミナルを起動します。  

* sshでログインします。  
ユーザ名は特に変更していない場合は pi になります。
```bash
$ ssh (Raspberry Pi の ユーザ名)@(Raspberry Pi の ホスト名).local
または
$ ssh (Raspberry Pi の ユーザ名)@(Raspberry Pi の IPアドレス)
```

(例)
```bash
$ ssh pi@yuzuafro.local
$ ssh pi@192.168.0.10
```

パスワードを聞かれるので、入力します。

```bash
$ ssh pi@192.168.0.10
pi@192.168.0.10's password: 

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Apr xx xx:xx:xx 2017 from 192.xxx.x.x
```

Raspberry PiにログインできればOKです。  

### VNC の環境設定
今回のハンズオンでは必須ではないのですが、Raspberry PiにPCからVNCで接続できるようにしておくと、
PCからRaspberry PiのGUIが使えて便利ですので設定しておくのがオススメです。  

### VNC Viewerのインストール(PC)
* PCにVNC Viewerをインストールします。  
https://www.realvnc.com/en/connect/download/viewer/
  * PCにインストールするのはVNC Viewer(VNCクライアントアプリケーション)です。  
  VNC Connect(VNCサーバアプリケーション)をインストールしないように注意しましょう。

### VNCServerの確認(Raspberry Pi)
####  Raspbian OSのバージョンの確認
* VNCServerの確認をする前に、Raspbian OSのバージョン確認をします。  
ターミナルに以下のコマンドを入力して、OSのバージョンを確認します。
```bash
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Raspbian
Description:	Raspbian GNU/Linux 8.0 (jessie)
Release:	8.0
Codename:	jessie
```
この場合は、Raspbian jessie がインストールされています。

#### Raspbian wheezy 以前のバージョンを使用している場合
* VNC Server はデフォルトではインストールされていません。  
次のステップでインストールします。

#### Raspbian jessie 以降のバージョンを使用している場合
* VNC Server がインストールされています。

#### VNCの確認
ssh で接続しているターミナルから vncserver コマンドがインストールされているか確認します。

```bash
$ which vncserver
/usr/bin/vncserver
```

インストールされていれば上のように、コマンドのパスが出力されます。

何も出力されない場合は、vncserver をインストールします。
```bash
$ sudo apt-get install vncserver
```

### VNC Server の起動
インストールができたら、vncserver を起動します。
```bash
$ vncserver
(略)
Log file is /home/pi/.vnc/yuzuafro:1.log
New desktop is yuzuafro:1 (192.168.0.10:1)
```

最後に、起動したVNCの番号が出力されます。  
この場合は1番となっています。(ポートの番号は5901番になります。)

### VNC Client からアクセスする
最後にPCからアクセスします。  
VNC Viewer を起動します。

File → New Connection で出てくる Properties メニューの General タブを選択します。  
VNC Server に以下のように入力します。(1番の場合)
```bash
VNC Server: (Raspberry Pi の ホスト名).local:5901
または
VNC Server: (Raspberry Pi の IPアドレス):5901
```

ユーザ名とパスワードを入力すると、リモート画面が起動します。
(ここのユーザ名は変更していなければ、piです。)

vncserver を終了させる時は、クライアント(VNC Viewer)を落として、
Raspberry Piのsshのターミナルで以下のように入力します。

(:1 の部分に起動したvncserverの番号が入ります。)
```bash
$ vncserver -kill :1
```

##### sshの認証方法について
* sshの認証方法には、パスワード認証方式と公開鍵認証方式があります。
* Raspberry Pi の VNC Server の設定では、パスワード認証が VNC password、公開鍵認証が UNIX password という名前になっています。
* デフォルトは UNIX password になっていますが、Raspberry Pi側の VNC Server の Option 設定で変更できます。
* 公開鍵認証の方がオススメです。

## その他もろもろ
### CUIからのインターフェイス設定変更方法
sshのみでPCからRaspberry Piに接続されている方は、raspi-configメニューでインターフェイス設定を変更することができます。
```bash
$ sudo raspi-config
```
灰色のconfig画面が起動します。

矢印キーで、「5 Interfacing Options」を選択し、Enterを押下します。  
「P2 SSH」を選択し、「Would you like the SSH server to be enabled?」に「＜はい＞」を選択します。  
同様に「P8 Remote GPIO」も Enable に変更します。  
すべての設定を終えたら「＜Finish＞」を選択し、再起動します。  

### rootユーザのパスワード設定
インストール後、特に設定をしないと、root のパスワードは設定されていません。

念のため、root のパスワードを設定しておきましょう。
```bash
$ sudo passwd root
```

### viが・・・
初期状態では、vim.tiny という vim しか入っていなくてイマイチなので、通常の vim をインストールします。
```bash
sudo apt-get install vim
```

### vimの設定が・・・
初期状態だとどうにも使いづらいので、src/vim/.vimrc に、vimの設定を置きました。

必要に応じて使ってください。(自分の好きな設定にしていただいて大丈夫です。)
```
cd
vi .vimrc
(src/vim/.vimrcの内容を貼り付ける)
```

### IPアドレスを調べるのに便利なスマートフォンアプリ Fing
スマートフォンアプリ Fing を使って、ネットワークに接続されている機器のIPアドレス、MACアドレスを簡単に調べることができます。

iOS向け 
https://itunes.apple.com/jp/app/fing-network-scanner/id430921107?mt=8

Android向け 
https://play.google.com/store/apps/details?id=com.overlook.android.fing&hl=ja

## 昔の Raspbian(wheezy以前) のインストール方法
- [NOOBSを使用したOSインストールと初期設定](./prepare.md)
- [VNCを使用したリモートアクセスの設定](./prepare_vnc.md)
