# 事前準備(NOOBSを使用したOSインストールと初期設定)

NOOBSを使用して、Raspberry Pi 3 に Raspbian OS をインストールする手順をまとめました。

Raspberry Pi に OS をインストールする方法には様々なものがあります。その中でも NOOBS は、初心者向けのインストール方法となっています。

## 必要なものの準備
Raspberry Pi 3 に、Raspbian OS をインストールするためには、以下のものを準備する必要があります。

- Raspberry Pi 3 本体
- microSDカード(class 10/8GB以上がおススメ)
- HDMIケーブル
- USB電源アダプタ、microUSBケーブル(2.5Aを推奨してますが、2A以上のスマートフォン用のものでもほぼ大丈夫です)
- ディスプレイ、USBマウス、USBキーボード

## OSインストール用イメージ(microSDカード)の作成
### microSDカードのフォーマット
microSDカードをFATでフォーマットします。
(exFATにしないように！！)

### NOOBSのダウンロード
Raspberry Piの公式サイトのダウンロードページから、NOOBSをDownload ZIPでダウンロードします。

- 公式サイトダウンロードページ https://www.raspberrypi.org/downloads/noobs/

公式サイトは時間がかかることが多いので、ダウンロードがうまくいかなそうな場合は、ミラーサイトからダウンロードしてもよいかもしれません。

- JAISTのミラーサイト http://ftp.jaist.ac.jp/pub/raspberrypi/NOOBS/images/

ZIPファイルを展開して、NOOBS_vx_x_x の中身を全て microSDカードのルートディレクトリにコピーします。
(以下は NOOBS_v2_3_0 の例です。)

```
.
├── BUILD-DATA
├── INSTRUCTIONS-README.txt
├── RECOVERY_FILES_DO_NOT_EDIT
├── bcm2708-rpi-0-w.dtb
├── bcm2708-rpi-b-plus.dtb
├── bcm2708-rpi-b.dtb
├── bcm2708-rpi-cm.dtb
├── bcm2709-rpi-2-b.dtb
├── bcm2710-rpi-3-b.dtb
├── bcm2710-rpi-cm3.dtb
├── bootcode.bin
├── defaults
├── os
├── overlays
├── recovery.cmdline
├── recovery.elf
├── recovery.img
├── recovery.rfs
├── recovery7.img
└── riscos-boot.bin
```

## Raspbian のインストール
作成したインストール用の microSDカードを Raspberry Pi にセットします。
ディスプレイ(HDMI)、マウス、キーボードを Raspberry Pi に接続します。

最後に、microUSBケーブルを Raspberry Pi に接続すると、電源がオンになります。(Raspberry Pi の LED が点灯します。)

OSのインストール画面が表示されるので、Raspbian を選択して、「Install」ボタンをクリックします。

(インストールには時間がかかります。)

インストールが終わると、「OS installed Successfully」のメッセージが表示されるので「OK」をクリックします。

再起動後に、Raspbian のデスクトップ画面が表示されます。

## Wi-Fiの設定
デスクトップ画面の右上のバーの中にある、ネットワーク設定のアイコンをクリックします。

見えているネットワークから、接続したいネットワークを選択して、パスワードを入力します。

ネットワークに接続できたら、左上の方にある Epiphany ウェブブラウザー(地球儀のアイコン)を使って、インターネット接続ができているかを確認しましょう。

## Raspbianファームウェア、パッケージのアップデート
ネットワークに繋がったら、ファームウェア、パッケージのアップデートを行います。

左上の方にある LXTerminal をクリックし、ターミナルを起動します。
ターミナルから以下のコマンドを実行します。

アップデートには時間がかかります。全て終わったら再起動しましょう。

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo rpi-update
$ sudo reboot
```

- 初期設定時のユーザ名は pi、パスワードは raspberry になっています。

## 日本語環境の設定
### 日本語フォントのインストール
ターミナルから以下のコマンドを実行し、日本語フォントをインストールします。
```
$ sudo apt-get install ttf-kochi-gothic xfonts-intl-japanese xfonts-intl-japanese-big xfonts-kaname
$ sudo reboot
```

### 日本語入力環境の設定
Anthy をインストールします。
```
$ sudo apt-get install ibus-anthy
```

### 自動起動の設定
.bashrc に以下の4行を追加します。
```bash
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
ibus-daemon -d -x
```

### Raspberry Pi の設定変更

GUIメニューから以下の設定を行います。

- menu → preferences → raspberry pi configuration → localisation
- set localeの設定
    - language ja
    - country JP
    - characterset UTF-8
- set timezoneの設定
    - area asia
    - location tokyo
- set keyboardの設定
    - country japan
    - variant japanese
- wifi countryの設定
    - country jp japan

設定が終了したら、Raspberry Pi を再起動します。
```
sudo reboot
```
