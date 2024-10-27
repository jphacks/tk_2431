## 感情分析LINEアシスタント

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2024/07/JPHACKS2024_ogp.jpg)](https://www.youtube.com/watch?v=DZXUkEj-CSI)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
  近年、SNSでのコミュニケーションが一般的となり、特に若者の間では「彼氏/彼女を怒らせてしまった...」といった悩みが増えています。気づかずにすれ違いが起こり、関係が悪化してしまうことも。そんな問題を解決するため、LINE上でのメッセージから感情を分析し、何気なく送信した文章のポジティブ/ネガティブ度合いをチェックするツールを開発しました。このツールは、以下の特長を持っています。
### 製品説明（具体的な製品の説明）
  LINE上のチャットメッセージをリアルタイムで解析し、感情の度合いを判定します。判定されたデータは蓄積され、後で確認できるようレポートとして提供します。
### 特長
#### 1. 特長1：　シンプルな感情分析
「嬉しい」と入力されると「ポジティブ」といったシンプルな分析結果を返し、ユーザーにわかりやすく感情の傾向を伝えます。
#### 2. 特長2：　感情の蓄積と分析
   ファインチューニングによって学習済みのユーザーの感情は、ポジティブ・ネガティブに分類された分析結果が蓄積され、どのくらいの頻度でその感情が現れているかを把握できます。
#### 3. 特長3：レポート機能
  一定量のメッセージ分析が完了すると、感情の傾向をまとめたレポートを自動生成し、ユーザーにフィードバックを提供します。



### 解決出来ること
  このツールを使うことで、無意識に発生するコミュニケーションのすれ違いを減らし、円滑なやり取りができるようサポートします。
### 今後の展望：
  今後は、データの蓄積と学習モデルを強化し、分析精度を向上させていきます。また、ネガポジ以外の感情（例えば、驚きや悲しみなど）も識別できるよう、さらなるモデル開発を行いたいと考えています。
### 注力したこと（こだわり等）：
* リアルタイムでのメッセージ分析と結果表示
* レポート機能による振り返りサポート

## 開発技術
### 活用した技術
#### API・データ
* LINE message API
* OpenAI API

#### フレームワーク・ライブラリ・モジュール
* Python
* Flask

#### デバイス
* Google Apps Script (GAS)

### 独自技術
#### ハッカソンで開発した独自機能・技術
* LINE上のメッセージを使った感情分析エンジン
* チャット履歴からの自動レポート生成機能
