# Upside Braille-Down 説明書


## 目次

1. Upside Braille-Down について
2. 公開場所について
3. 動作環境
4. 使い方
5. 著作権
6. ご寄付・ご協力のお願い
7. 更新履歴
8. 問い合わせ先


## 1. Upside Braille-Down について

### 概要

Upside Braille-Down (USB-D) は、NVDAで点字ディスプレイを上下反転状態で使用するためのアドオンです。

### 特徴

* 点字ディスプレイを上下サカサマで使用可能<br>
    点字ディスプレイを上下反転で使用することで、セルが手前にあるディスプレイを使用する際に、PCのキーボードと点字セルをより近づけることができます。
* 点字表示とキースイッチを反転<br>
    対応点字ディスプレイのセル表示、カーソルルーティングスイッチ（タッチカーソルキー）が反転します。
    また、対応点字ディスプレイでは、行スクロールキー、方向キー、その他一部の点字入力キーも反転します。
* 反転の有効と無効を切り替え可能<br>
    NVDAメニューから点字ディスプレイを反転するかどうか、そのときの状況によって切り替えることができます。

### 対応点字ディスプレイ

以下に、対応の点字ディスプレイを示します。
なお、点字ディスプレイの対応作業成果などを広く受け入れており、すべての動作を保証することはできません。
作者は、Next Touch 40　にて動作を確認しております。

* KGS: Next Touch 40
    * キー反転: 対応
    * 動作確認、または対応受け入れバージョン: NVDA 2023.1, 2024.1
* KGS: ブレイルメモ32
    * キー反転: 対応
    * 動作確認、または対応受け入れバージョン: NVDA 2023.1
* 日本テレソフト: 精華40 version5
    * キー反転: 対応
    * 動作確認、または対応受け入れバージョン: NVDA 2023.1


## 2. 公開場所について

本アドオンは、以下のページにて公開しております。
最新版のアドオンとともに、更新内容なども案内しておりますのでご確認ください。

* Upside Braille-Down のページ: <a href="https://actlab.org/software/USB-D">https://actlab.org/software/USB-D</a>


## 3. 動作環境

本アドオンを利用するには、以下の環境が必要です。

* NVDA2023.1以降
* その他、Windows、およびNVDAが快適に動作する環境

なお、本アドオンを使用するには、対応の点字ディスプレイとそのドライバーが正しくセットアップされている必要があります。

## 4. 使い方

### 点字ディスプレイの反転状態を切り替える

NVDAメニューから、「Upside Braille-Down」を選択する。

* 「点字ディスプレイの向きをサカサマにする」を選択すると、点字ディスプレイの向きが反転状態になります。
* 「点字ディスプレイの向きを元に戻す」を選択すると、点字ディスプレイが通常の向きになります。

なお、NVDA起動時には、前回終了時の設定になっています。


### アップデートの確認と実行

本アドオンは、機能の更新、および不具合の修正などのため、アップデートが提供されることがあります。
アドオンのアップデートは、NVDAメニューから「Upside Braille-Down」を選択し、「アップデートの確認」を実行することでいつでも確認することができます。
アップデートが見つかると、更新を促すメッセージが表示されます。案内に従ってアップデート作業を行ってください。

また、本アドオンには、NVDA起動時に自動でアップデートを確認する機能が搭載されています。
NVDAメニューから「Upside Braille-Down」を選択し、「起動時のアップデートの確認を無効化」あるいは「起動時のアップデートの確認を有効化」を実行することで設定を変更できます。

## 5. 著作権

(c) 2024 Hiroki Fujii - ACT Laboratory

GNU General Public License, version 2

* URL: <a href="https://actlab.org/">https://actlab.org/</a>


## 6. ご寄付・ご協力のお願い

ACT Laboratory(Accessible Tools Laboratory)は、プログラミングを学ぶ視覚障害者の集まりです。<br>
本アドオンは無償ですが、公開には多少の経費も掛かっています。

本アドオンを気に入っていただけた方などで、活動にご支援・ご協力を頂ける方がいらっしゃいましたら、ぜひお力をお貸しください。
なお、ご支援を頂きました方につきましては、TwitterやACT Laboratoryサイトにてご紹介させて頂く予定です。

詳しくはこちらへ<br>
<a href="https://actlab.org/donate/">https://actlab.org/donate/</a>


## 7. 更新履歴

* 1.0.2 (2025/02/27)
    * NVDA 2025.1に対応

* 1.0.0 (2024/02/24)
    * 初回リリース

* 1.0.1 (2024/02/24)
    * アップデータの不具合修正

## 8. 問い合わせ先

本アドオンを利用しての感想やご要望、不具合のご報告などは、以下のメールアドレスまたは掲示板へご連絡ください。

* ACT Laboratory サポート: support@actlab.org
* ACT Laboratory 掲示板: <a href="https://actlab.org/bbs/">https://actlab.org/bbs/</a>

GitHubリポジトリは、こちらです。

* <a href="https://github.com/actlaboratory/USB-D">https://github.com/actlaboratory/USB-D</a>
