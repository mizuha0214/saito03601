# step1
最終的にacceptされるcodeが書けた。  
だだし、最初、node自体ではなく、nodeの値が一致するか、を見てしまっていてreject。  
（解法自体は以前に見たことがあったので、0から本当に自分で実装できたのか不明）

# step2
他の方々のcodeを見てrefactor。
- list_nodes →　visitedに変更。  
reachedも散見されたが感覚的にあまりしっくりこない。 
　「reach だと特定のゴールに到達と言うニュアンス」（他者のmemo.md）
- 可読性はwhile node:がベターかと思ったが、`head.__bool__()` や `head.__len__()`の実装を気にする必要があるので、`while node is not None`が良いと思った。

# step3
3回連続でstep2.pyと同じcodeが時間内に書けた。  
ただし、一度失敗。step2.pyを書いたときから1週間経過した上でぼーっとしながら書いたら、以下2行の順番を逆に書いた。
```python
visited.add(node)
node = node.next
```

# その他メモ（他者のmemo.mdからコピー）
- 平均計算量で見ると、list も set も要素の追加は O(1)になり、検索だと list が O(n)、set が O(1)になる。setはハッシュテーブルで実装されているから。
- LeetCode の実行時間はブレがあるため、あまり信用しないほうがよい。計測したい場合は、手元で何度か実行して中央値を取るのがいい。
- 以下のような書き方もあり得る。currentの書き換えは意図が伝わりづらい。
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        while current:
            if current.val is None:
                return True
            current.val = None
            current = current.next

        return False
```


