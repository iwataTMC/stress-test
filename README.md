# Locustって何？
Locust（ https://locust.io/ ）は，WebアプリケーションやAPIの性能テストを行うためのオープンソースの負荷テストツールです．  
Locustの特徴は何といってもPythonで書けることです。


[公式ドキュメント](https://docs.locust.io/en/stable/)



# 実行環境
- MacOS
- Python 3.7.9

> **Note**  
> Pythonをインストールされていない方は，以下のページよりインストールしてください．  
> [Pythonダウンロードはコチラから](https://pythonlinks.python.jp/ja/index.html)



# 使い方

## 仮想環境の作成

1. 仮想環境を作成します．

```
$ python3.7 -m venv test
```

2. 仮想環境を有効化します．

```
$ source test/bin/activate
```

3. Locustをインストールします．

```
$ pip install locust
```

4. インストールできたか確認します．

locustコマンドが使えればOKです．

```
$ pip list

$ locust -V
```

1. ターミナルで以下のコマンドを実行します．

```
$ locust
```

6. ブラウザで以下のURLにアクセスします．

```
http://localhost:8089/
```

GUIで負荷テストを行うことができます．

7. GUIで負荷テストを行う

- Number of users to simulate: 最終的に到達するユーザ数(=クライアント数)
- Hatch rate: 1秒あたりに増加する秒間ユーザ数
「Number of total users to simulate」で100を指定し、「Spawn rate」で10を設定した場合、1秒に10ユーザーずつ増えていき10秒後に100ユーザとなります。それ以上ユーザーは増加しません。
- URL: 検証したいURLを入力します

上の設定をしたら「Start swarming」を押下すると，負荷テストが開始されます．


さいごに：作業が修了したら仮想環境を無効化します．

1. 作業が修了したら仮想環境を無効化します．

```
$ deactivate
```



## GUIについて説明  
Chats タブ：　どのくらいの秒間リクエストでているのか等をグラフで見れます  
Failures: リクエスト失敗した場合は簡単な例外内容含めて出してくれます  
Exceptions: 例外のStackTrace  
Download Data: CSVとして結果のデータをダウンロードできます  
Slaves: LocustのSlaveの状態を見れます  


