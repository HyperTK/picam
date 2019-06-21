# 1. Flask + WSGI + Apache2
本プロジェクトはRaspberry Pi上にApache+WSGIを稼働させ、PythonのWebフレームワークであるFlaskからラズパイのカメラ映像を配信するものである。
``` sh
.
|-app.py(Flaskのプログラム)
|-camera_pi.py(Picameraを制御するプログラム)
|-flask_app.wsgi(WSGI読み込み用)
|-templates
    |- index.html(Jinja2 テンプレート)
```
## 1.1. 実施環境
* Raspberry Pi 3 Model B
* Raspbian Stretch
* 16GB MicroSD
* For raspberry pi カメラモジュール 5MP
  * https://amzn.to/2IZr5zJ

## 1.2. 環境構築
今回はRaspberry Pi上でPythonのプログラムを走らせる。ラズパイ用のPythonパッケージの管理として"berryconda"をインストールし、仮想環境を構築した。
### 1.2.1. berrycondaインストール
1. berrycondaは下記を参考にインストール

   * https://urashita.com/archives/26622
   * https://qiita.com/rsm223_rip/items/c6105d22ba360623530a
        ``` sh
        wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
        chmod +x Berryconda3-2.0.0-Linux-armv7l.sh
        ./Berryconda3-2.0.0-Linux-armv7l.sh
        ```
        .bashrcへのパスはberrycondaをインストール中に通すか聞かれるのでyesにしとくと楽。

2. 仮想環境構築
    ``` sh
    conda create -n env python=3.5
    * codna create -n 仮想環境名 使用するpythonバージョン

    仮想環境を使う
    source activate env

    仮想環境をやめる
    source deactivate
    ```
    * パッケージインストール
        ``` sh
        仮想環境を使う
        source activate env

        flask
        conda install flask

        OpenCV
        conda install -c conda-forge opencv

        picamera
        pip install picamera
        ```

### 1.2.2. Apache2, wsgiインストール
1. インストール
    ``` sh
    sudo apt install apache2 libapache2-mod-wsgi-py3
    ```
2. 設定
    
    設定関係は下記の記事のとおりで概ねOK
    * https://qiita.com/t114/items/761eb4e81f0ba3db35b0
    
    * ルートディレクトリ
      * /home/pi/public_flask
      * 下層構造
      ``` sh
      .
      |-app.py
      |-camera_pi.py
      |-flask_app.wsgi
      |-templates
          |- index.html
      ```
    
    * wsgi有効化\
        上記記事の"VirtualHost設定反映"後にそのままApacheを再起動すると下記のようなエラーが発生するかもしれない。
        自分はwsgiを有効化することでエラーが解消された。
        * 参考 http://bit.ly/2x57uZv
        ``` sh
         エラー内容
        tarting httpd: Syntax error on line 10 of /etc/xxxxx/xxxxx/xxxxx.conf:Invalid command 'WSGIDaemonProcess', perhaps misspelled or defined by a module ot included in the server configuration
        
        下記で有効化
        sudo a2enmod wsgi

        Apacheリロード
        sudo systemctl reload apache2.service
        ```
