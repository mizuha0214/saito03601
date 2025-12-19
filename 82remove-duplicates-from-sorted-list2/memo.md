# step1
dummy nodeを使うことを考えたが上手く実装できず5分経ったので断念。  
とりあえず動きはする。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        checking_node = head
        single_val_end = dummy_node

        while checking_node:
            if checking_node.next is not None and checking_node.val == checking_node.next.val:
                duplicate_val = checking_node.val
                while checking_node and checking_node.val == duplicate_val:
                    checking_node = checking_node.next
                single_val_end.next = checking_node
            else:
                single_val_end = checking_node
                checking_node = checking_node.next

        return dummy_node.next
```

# step2
## 読んだプルリク
- https://discord.com/channels/1084280443945353267/1195700948786491403/1197102971977211966
- https://github.com/docto-rin/leetcode/pull/4
- https://github.com/hiroki-horiguchi-dev/leetcode/pull/4
## step2-1.py
step1.pyの名前だけ変更。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        checking = head
        single_val_end = dummy

        while checking:
            if checking.next is not None and checking.val == checking.next.val:
                duplicate_val = checking.val
                while checking and checking.val == duplicate_val:
                    checking = checking.next
                single_val_end.next = checking
            else:
                single_val_end = checking
                checking = checking.next

        return dummy.next
```
## stp2-2.py
if else文のelseの方が処理が簡単なので先に持ってくる。  
また、ifとelse内の処理があまりに異なる場合はif elseにしない方が読みやすいらしい。

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        checking = head
        single_val_end = dummy

        while checking:
            if checking.next is None or checking.val != checking.next.val:
                single_val_end = checking
                checking = checking.next
                continue
            duplicate_val = checking.val
            while checking is not None and checking.val == duplicate_val:
                checking = checking.next
            single_val_end.next = checking

        return dummy.next
```

## step2-3.py
まとめてskipした後に、さらに`checking = checking.next`ともう一度進める必要があるので、step2-2.pyの方がよさそう。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        checking = head
        single_val_end = dummy

        while checking:
            if checking.next is None or checking.val != checking.next.val:
                single_val_end = checking
                checking = checking.next
                continue
            while checking.next is not None and checking.val == checking.next.val:
                checking = checking.next
            checking = checking.next
            single_val_end.next = checking
            
        return dummy.next
```

## step2-4.py
関数化もあり。
```python

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def skip_duplicate(checking: ListNode) -> ListNode:
            duplicate_val = checking.val
            while checking is not None and checking.val == duplicate_val:
                checking = checking.next
            return checking
    
        dummy = ListNode()
        dummy.next = head
        checking = head
        single_val_end = dummy

        while checking:
            if checking.next is None or checking.val != checking.next.val:
                single_val_end = checking
                checking = checking.next
                continue
            checking = skip_duplicate(checking)
            single_val_end.next = checking

        return dummy.next
```

## step2-5.py
`single_val_end`関連を更新するタイミングは、単一値が見つかった時点の方が自然な気がする。
step2-4.pyまでは重複をまとめてskipした時に`single_val_end.next`を次にチェックするnodeにしている。
しかし、単一値を見つけた時に`single_val_end`を動かすから、これと一緒に`single_val_end.next`を動かした方が処理がつかみやすい。
（step2-4.pyまでは`single_val_end` と `checking` の責務が混ざって見える。）
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        checking = head
        single_val_end = dummy

        while checking:
            if checking.next is None or checking.val != checking.next.val:
                single_val_end.next = checking
                single_val_end = checking
                checking = checking.next
                single_val_end.next = None
                continue
            duplicate_val = checking.val
            while checking is not None and checking.val == duplicate_val:
                checking = checking.next

        return dummy.next
```

## step2-6.py
まとめて重複をskipせず、1個ずつ行う方法。本来はまとめて飛ばす手法よりこっちの方が自然な発想で出てきそう（83の問題はそうだった）。  
step2-5.pyと同様に単一値を見つけた時に`single_val_end.next`を動かす方法で書いてみる。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        single_val_end = dummy
        is_deleting = False
        deleting_number = 0
        checking = head

        while checking:
            if is_deleting and deleting_number == checking.val:
                checking = checking.next
                continue
            is_deleting = False
            if not checking.next or checking.val != checking.next.val:
                single_val_end.next = checking
                single_val_end = checking
                checking = checking.next
                single_val_end.next = None
                continue
            is_deleting = True
            deleting_number = checking.val
            checking = checking.next

        return dummy.next
```

# step3
`checking`はbool値を連想させると見たのを思い出して、`runner`にした。step2-1.pyとstep2-5.pyの融合code。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        single_val_end = dummy
        runner = head

        while runner is not None:
            if runner.next is not None and runner.val == runner.next.val:
                duplicate_val = runner.val
                while runner is not None and runner.val == duplicate_val:
                    runner = runner.next
            else:
                next_runner = runner.next
                single_val_end.next = runner
                single_val_end = runner
                single_val_end.next = None
                runner = next_runner

        return dummy.next
```

