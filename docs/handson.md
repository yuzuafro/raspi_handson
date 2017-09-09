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

### 貸し出ししているもの
* 電子工作部品一式(後ほど中身の確認をします。)

## 事前準備ができているかの確認
### WiFi接続と設定の確認
* 1人ずつディスプレイに接続して起動し、会場のWiFiに接続します。

### MACアドレスの確認
* ターミナルを起動し、ifconfig コマンドで、MACアドレスを確認します。wlan0 のハードウェアアドレスをメモします。
```bash
$ ifconfig
...
wlan0     Link encap:イーサネット  ハードウェアアドレス xx:xx:xx:xx:xx:xx 
          inetアドレス:192.168.xx.xx ブロードキャスト:192.168.0.255  マスク:255.255.255.0
...
```

### VNCServerの確認
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
* VNCServerがインストールされているかを確認します。
```bash
$ which vncserver
```
インストールされていない場合は、後ほどインストールします。

#### Raspbian jessie 以降のバージョンを使用している場合
* VNC Server の Options を起動します。
    * Security
        * Authentication: UNIX password → VNC password に変更
        * Applyボタンを押下します。パスワード設定画面が表示されるのでパスワードを設定します。

### その他の設定
* 設定 → Raspberry Piの設定メニューを起動します。
    * システム
        * パスワードを変更(raspberry以外を推奨)
        * ホスト名を設定(raspberrypi以外を推奨)
            * hostname には "-"(ハイフン)以外の記号を使用することはできません。("_"アンダースコアなどは使用できません)
    * インターフェイス
        * SSH、VNC、リモートGPIO を有効にします。
    * ローカライゼーション
        * 4項目全て、日本に設定します。
* 再起動します。再起動できたら、シャットダウンして、PCからの確認に移ります。

### PCからの接続の確認
#### sshの確認
* PCからsshでログインします。PCのターミナルを起動します。(Windowsの人はTera Termなど)
ユーザ名は特に変更していない場合は pi になります。
```bash
$ ssh (Raspberry Pi の ユーザ名)@(Raspberry Pi の ホスト名.local)
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

インストールができたら、vncserver を起動します。
```bash
$ vncserver
(略)
Log file is /home/pi/.vnc/yuzuafro:1.log
New desktop is yuzuafro:1 (192.168.0.10:1)
```

最後に、起動したVNCの番号が出力されます。

Macの人は、画面共有(Finder → 移動 → サーバへ接続) に以下のように入力し、接続を選択します。
```bash
vnc://yuzuafro.local:5901
または
vnc://192.168.0.10:5901
```

パスワードを入力すると、リモート画面が起動します。

Windowsの人は、VNC Viewer を起動して、同様に入力します。

Mac の画面共有がうまくできない場合は、設定が正しくない可能性があります。

この辺りのページを参考に確認してみてください。

https://pc-karuma.net/mac-screen-sharing/

https://support.apple.com/kb/PH21800?viewlocale=ja_JP&locale=ja_JP

vncserver を終了させる時は、クライアント(画面共有やVNC Viewer)を落として、
Raspberry Piのsshのターミナルで以下のように入力します。

(:1 の部分に起動したvncserverの番号が入ります。)
```bash
$ vncserver -kill :1
```

##### sshの認証方法について
* sshの認証方法には、パスワード認証方式と公開鍵認証方式があります。
* Raspberry Pi の VNC Server の設定では、パスワード認証が VNC password、公開鍵認証が UNIX password という名前になっています。
* 公開鍵認証方式の方が安全性が高いというメリットがありますが、設定が少し面倒だったり、Mac の画面共有メニューでは使えないデメリットがあります。
* 公開鍵認証方式を使用したい場合は、PCに VNC Viewer をインストールすれば使用できます。

## その他もろもろ
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
