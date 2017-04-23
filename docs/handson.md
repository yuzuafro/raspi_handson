# 本日のハンズオンについて
## 今日のゴール
* Webブラウザから、Raspberry Pi に接続された LED やブザーを操作する。

## 今日やること
* sshやVNCを使用して、PCからリモートで Raspberry Pi を操作する。
* Raspberry Pi の GPIOポートを使用して、電子工作を体験する。
* Python を使って、部品を動作させるプログラムを作成する。
* Webブラウザから、Raspberry Pi にアクセスする環境を整える。

## 事前準備ができているかの確認
### WiFi接続と設定の確認
* 1人ずつディスプレイに接続して起動し、会場のWiFiに接続する。
* ターミナルを起動し、ifconfig コマンドで、MACアドレスを確認する。wlan0 のハードウェアアドレスをメモする。
```bash
$ ifconfig
```
* (PIXELじゃない人向け)VNCServerがインストールされているかを確認する。
```bash
$ which vncserver
```
インストールされていない場合は、後ほどインストールしてもらう。
* (PIXELの人向け)
* VNC Server の Options を起動する。
    * Security
        * Authentication: UNIX password → VNC password に変更
        * Applyボタンを押下する。パスワード設定画面が表示されるのでパスワードを設定する。
* 設定 → Raspberry Piの設定メニューを起動する。
    * システム
        * パスワードを変更(raspberry以外を推奨)
        * ホスト名を設定(raspberrypi以外を推奨)
    * インターフェイス
        * SSH、VNC、リモートGPIO を有効にする。
    * ローカライゼーション
        * 4項目全て、日本に設定する。
* 再起動する。再起動できたら、シャットダウンして席に戻ってもらう。

### PCからの接続の確認
#### sshの確認
* PCからsshでログインする。PCのターミナルを起動します。
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

Windowsの人は、RealVNC Viewer を起動して、同様に入力します。

Mac の画面共有がうまくできない場合は、設定が正しくない可能性があります。

この辺りのページを参考に確認してみてください。

https://pc-karuma.net/mac-screen-sharing/

https://support.apple.com/kb/PH21800?viewlocale=ja_JP&locale=ja_JP

vncserver を終了させる時は、クライアント(画面共有やRealVNC Viewer)を落として、
Raspberry Piのsshのターミナルで以下のように入力します。

(:1 の部分に起動したvncserverの番号が入ります。)
```bash
$ vncserver -kill :1
```

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
