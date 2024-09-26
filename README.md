# Locustって何？
Locust（ https://locust.io/ ）は，WebアプリケーションやAPIの性能テストを行うためのオープンソースの負荷テストツールです．  
Locustの特徴は何といってもPythonで書けることです。


[公式ドキュメント](https://docs.locust.io/en/stable/)



# 実行環境
- MacOS
- Python 3.7.9

> [!NOTE]  
> Pythonをインストールされていない方は，以下のページよりインストールしてください．  
> [Pythonダウンロードはコチラから](https://pythonlinks.python.jp/ja/index.html)

### サポートされているpythonのバージョン
- 3.6
- 3.7
- 3.8


# 使い方
ここではpythonの仮想環境を作成し，そこにlocustをインストールして実行する方法を説明します．  
pythonの仮想環境とは，pythonのライブラリをプロジェクトごとに管理するためのものです．  
（別の実行環境が作成できる）  
なぜ仮想環境を作成するのかというと，他のpythonのプロジェクトに影響を与えないようにするためです．  
仮想環境を作成することで，locustをインストールした環境と，他のpythonのプロジェクトを作成した環境を分けることができます．  
また，仮想環境を作成することで，他のpythonのプロジェクトと同じまたは違うバージョンのpythonを使用することができます．  

ライブラリによってサポートされているpythonのバージョンが異なる場合があるため，仮想環境を作成することで，ライブラリのバージョンを固定することができます．


仮想環境を作成するには以下の手段があります．
代表的なものを紹介します．

- venv
  - venvはpython3.3から標準でサポートされている仮想環境の作成ツールです．
- conda
  - condaは[Anaconda](https://www.anaconda.com/)をインストールすることで使用できる仮想環境の作成ツールです．
- virtualenv
  - [virtualenv](https://pypi.org/project/virtualenv/)はpythonの仮想環境を作成するためのツールです．pipでインストールすることができます．`pip install virtualenv`



ここでは，venvを使用して仮想環境を作成します．


## 仮想環境の作成と有効化

1. 仮想環境を作成します．

任意のディレクトリで以下のコマンドを実行します．

```
$ python3.7 -m venv test
```

> **Note**  
> `python3.7`は，pythonのバージョンによって変更してください．
> `test` は仮想環境の名前です．任意の名前をつけることができます．



2. 仮想環境を有効化します．

```
$ source test/bin/activate
```

## Locustのインストールと実行
1. Locustをインストールします．

```
$ pip install locust
```

2. インストールできたか確認します．

locustコマンドが使えればOKです．

```
$ pip list

$ locust -V
```

3. `locustfile.py`を編集しシナリオを書きます．  

(例1)`/helloworld`にGETリクエストを送るシナリオ

```python
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    #  1タスク = 1秒間に1回リクエストを送信する
    wait_time = constant_pacing(1)
    
    @task
    def hello_world(self):
        self.client.get("/helloworld")
```

(例2)Basic認証(ユーザ名とパスワード)が必要な場合は以下のように書きます．

```python
from locust import HttpUser, task, constant_pacing
from requests.auth import HTTPBasicAuth

class QuickstartUser(HttpUser):
    #  1タスク = 1秒間に1回リクエストを送信する
    wait_time = constant_pacing(1)

    @task
    def view_top(self):
        # Basic認証を通過するため、以下を記述する
        auth = HTTPBasicAuth(username="username", password="password")
        self.client.get("/hello-world", auth=auth)
```



4. ターミナルで以下のコマンドを実行します．

```
$ locust
```

5. ブラウザで以下のURLにアクセスします．

```
http://localhost:8089/
```

GUIで負荷テストを行うことができます．

6. GUIで負荷テストを行う

- Number of users to simulate: 最終的に到達するユーザ数(=クライアント数)
- Hatch rate: 1秒あたりに増加する秒間ユーザ数
「Number of total users to simulate」で100を指定し、「Spawn rate」で10を設定した場合、1秒に10ユーザーずつ増えていき10秒後に100ユーザとなります。それ以上ユーザーは増加しません。
- URL: 検証したいURLを入力します

上の設定をしたら「Start swarming」を押下すると，負荷テストが開始されます．

7. テスト結果の確認

8. locustを終了する
```
Ctrl + C
```




## 仮想環境の終了
最後に：作業が修了したら仮想環境を無効化します．

1. 作業が修了したら仮想環境を無効化します．

```
$ deactivate
```



## GUIについて説明  
Chats タブ： どのくらいの秒間リクエストでているのか等をグラフで見れます  
Failures: リクエスト失敗した場合は簡単な例外内容含めて出してくれます  
Exceptions: 例外のStackTrace  
Download Data: CSVとして結果のデータをダウンロードできます  
Slaves: LocustのSlaveの状態を見れます  




# 参考
- [pythonで始める負荷試験](https://speakerdeck.com/nissy0409240/pythondeshi-merufu-he-shi-yan)

# Appendix

- `locustfile` の自動生成
  [har2locust](https://github.com/SvenskaSpel/har2locust) を使用すると、ブラウザ記録 (HAR ファイル) に基づいて
  `locustfile` を生成できます。
  - これは、独自の `locustfile` の作成に慣れていない初心者にとって特に便利ですが、より高度な使用例に合わせて高度にカスタマイズすることもできます。
    - 以下のコマンドを実行することで、`locustfile.py` が生成されます。
    ```
    $ pip install har2locust
    $ har2locust myrecording.har > locustfile.py
    ```