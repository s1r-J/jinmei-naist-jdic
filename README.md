jinmei-naist-jdic
====

[NAIST-jdic](https://ja.osdn.net/projects/naist-jdic/wiki/FrontPage)の辞書データから人名だけを抜き出しました。  
読み仮名（カタカナ）をキーとして、候補となる書き文字をリストで保持するようなJSON形式に整形しています。

NAIST-jdicについては下記のとおりです。修正BSDライセンスなので商用利用も安心して出来ます。

> NAIST-jdic は、IPAdic の後継です。 IPAdic の固有名詞以外の全エントリをチェック（可能性に基づく品詞の整理）し、 表記ゆれ情報を付与し、複合語の構造を付与する作業を行っています。 固有名詞については不要な語、新規追加などの整理を随時行っていきます。 この作業により IPAdic のライセンスで問題となっていた ICOT 条項を削除し、 広告条項無しの BSD ライセンスに変更致しました

## Description

`sei.json`は姓のデータです。`mei.json`は名のデータです。  
`mecab-naist-jdic-0.6.3b-20111013.tar.gz`からデータを抜き出しました。

scriptsフォルダ以下には人名データを抜き出してJSONに整形するスクリプト（Python）があります。  
使い方は以下のとおりです。

1. [NAIST-jdic](https://ja.osdn.net/projects/naist-jdic/wiki/FrontPage)から辞書データをダウンロード、解凍します。
2. scripts/jinmei_naist-jdic.pyを実行します。（Python3）
```
python jinmei_naist-jdic.py '~/naist-jdic.csv'
```

## Usage

GitHub Pagesで[サイト](https://s1r-j.github.io/jinmei-naist-jdic/)を作成しているので、
姓または名のリンクを押せばそれぞれのJSONファイルが返却されます。

## Licence

[Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

## Author

[s1r-J](https://github.com/s1r-J)
