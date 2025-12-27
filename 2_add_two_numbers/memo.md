# step1
繰り上げをどう処理するか悩んだので、chat gptに素直な書き方を聞いた。

# step2 
- 読んだプルリク
  - https://github.com/komdoroid/arai60/pull/7
  - https://github.com/resumit30minutes/leetcode-arai60-practice/pull/6
  - https://github.com/resumit30minutes/leetcode-arai60-practice/pull/6

- step2_1.py  
同じ作業の繰り返しなので再帰を使ってみる。
- step2_2.py  
dummyを使わない実装
- step2-3.py  
`if l1:`関連を一個にまとめる方法
- step2_4.py  
三項演算子なし

# step3
  - step2_4.pyのように`if l1`の処理を一個にまとめるのは簡潔だが、個人的には、現在の位の足し算中に、次の位のことに考えが及ばない。
  足し算が終れば自然に次の位に視野が向く。
  - step2_3.pyのように途中で初回だけ特別な処理が入るのは、忘れてしまう
  - `is not None`を使う。
