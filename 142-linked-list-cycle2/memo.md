# step1
- 問題141のsetを使う解法だと戻り値を変えるのみなので、フロイトで解くことにした。
- 解法が思いつかないので、動画の解説を見た（codeは見てない）。
- acceptはされたが、自分で書いたcodeながら何をしているか良く分からない。なぜその手法でこの問題が解けるのかが、分かる、分からない、はこっちがコントロールできないのは仕方ないが、今のcodeだと手法自体が伝わらなそう。

# step2（他者のcode見てrefactor）
- 関数に切りだす。どこを関数かするか悩んだが、meeting点を見つける、循環start点を見つける、をどちらも関数にした。  
理由：初見でcodeを見た場合、はじめの流れが、meeting点を探していることがすぐには分からないのではないかと思ったから。  
とはいえ、突然meeting関数でcodeが始まったら、循環検出の関数なのに何をしているのかと思われそうなので、最初にコメント「meetingが存在する＝循環が存在する」を入れた。
- meeting点を見つけた後は、fast, slowの概念は持ち込まないことに納得。  
名前もfrom_head, from_meetingはしっくりきたので使わせてもらった。

# step3 
- step2からの変更点： 自作関数名  
step3で何回か書いているうちに、自作関数名が気になった。step2では自作関数名にどちらもfindを使っている。
しかし、`find_meeting`はそもそもmeeting点が存在するか不明、一方で`find_cycle_start`は必ずstart点が存在する確証がある。
gptに聞いて、不確定な探索 → find / detect / search、確定条件下での探索 → get / locate / computeと言われたので、searchとgetを採用。  
ただし、この意図が初見の人に伝わるか不明。具体的な単語を使うことは推奨されるが、その単語と他の単語の違いを他者が感じ取れないなら逆に混乱を招くから良くないとは聞く。

  

# その他メモ
- set()解法の話だが、ListNodeクラスが`__hash__()` と `__eq__()`を実装していないので、以下はオブジェクト自体（メモリアドレス）の同一性を判定する。
```python
visited = set()
if node in visited:
```
例えばintは`__hash__()` と `__eq__()`を実装しているので、以下は値の等価性を判定する。
```python
a_list = [1, 2, 4] 
a_set = set(a_list) 
b= 2 
if b in a_set:
```
ドキュメントはこれ。
https://docs.python.org/3/reference/datamodel.html#object.__hash__
