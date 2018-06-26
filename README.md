 # リポジトリのクローン
1. 画面右上の<font color="green"> Clone or Download</font> → https...をコピー(右側のボタンで一発)
2. cygwinで作業ディレクトリに移動(/home/zemi/zemiAにしたいなら/home/zemiに移動)
3. $ git clone https...(さっきコピーしたもの)

# ブランチの作成
$ git checkout -b ブランチ名

# コミット
作業ディレクトリにファイルを追加して

$ git commit -m "コミットメッセージ" (""がないとシェルのワイルドカードとして展開されることがある)

ユーザ情報が要求されるかもしれない．メッセージにしたがってユーザ名とメールアドレスを適当に入力

# プッシュ
$ git push origin ブランチ名

アカウントとパスワードが要求されるのでGitHubのアカウントのものを入力
