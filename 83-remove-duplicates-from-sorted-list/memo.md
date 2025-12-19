# step1
- step1_reject.py  
リンクドリストであることを考慮していなかった。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        visited_val = set()
        result = []

        while current_node is not None:
            if current_node.val not in visited_val:
                visited_val.add(current_node.val)
                result.append(current_node)
            current_node = current_node.next

        return result
```
- step1_accept.py
  - 間の要素を削除したうえで連結させる方法が分からず、新井さんの解説を見た。
  - prev_nodeをいつ動かすかで何度もrejectされて、最終的にaccept。
  - 初期は、corrent=prevともにheadで一致しておりその時だけprevは次に進めないというのをcountで制御した。ただし、ネストが深くなってしまう。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = head
        seen_val = set()
        count = 0

        while curr_node is not None:
            if curr_node.val in seen_val:
                prev_node.next = curr_node.next
            else:
                seen_val.add(curr_node.val)
                if count != 0:
                    prev_node = prev_node.next

            curr_node = curr_node.next
            count += 1

        return head
```
  
# step2
南京錠の例えはしばらく考えて納得がいった。  
step1の手法も「処理済みの末尾node」を使っているが、私は頭の中で`prev`を何となく前のnodeと思っているだけで、
たまに、`prev`をたんに寄与リスト上で`curr`の直前nodeと思っている瞬間があった気がする。  
- 見たプルリク
  - https://github.com/shintaro1993/arai60/blob/527432880faf353f08a61b1d7fccca5c2fe6c43c/remobe-duplicates-from-sorted-list/remove-duplicates-from-sorted-list.md
  - https://github.com/myzn0806/leetcode-2/pull/3/files
  - https://github.com/t0hsumi/leetcode/blob/c1e77d9158472abb961403f974fefe45d51ae0c1/83.%20Remove%20Duplicates%20from%20Sorted%20List.md
  - https://github.com/katataku/leetcode/blob/048855948f7e9e50e12eb9d7e51c1b4657ea6298/83.%20Remove%20Duplicates%20from%20Sorted%20List.md?plain=1
- step2_1.py（step1_accept.pyを改修）
  - sortedなので、そもそも`set()`を使う必要はなかった
  - `prev_node = prev_node.next`を`prev_node = curr_node`に変更。  
  `prev_node = prev_node.next`だと一番初めだけ分岐が必要になってしまう。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = head
        seen_val = set()

        while curr_node is not None:
            next_node = curr_node.next
            if curr_node.val in seen_val:
                prev_node.next = next_node
            else:
                seen_val.add(curr_node.val)
                prev_node = curr_node

            curr_node = next_node

        return head
```
- step2_2.py
```python
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      checking = head
      non_duplicate_end = head

      while checking is not None:
          next_node = checking.next
          if checking.val == non_duplicate_end.val:
              non_duplicate_end.next = next_node
          else:
              non_duplicate_end = checking

          checking = next_node

      return head
```
- step2_3.py
  - step2_2.pyと異なる点は鎖の繋ぎ変えのタイミング。
  step2_2はcheckで毎回繋ぎ変える。step2_3は新しい値の時だけ繋ぎ変える。
  step2_3の方が効率的に思える。しかし、寄与リストの末尾に重複がある場合（[1, 2, 4, 3, 3]とか）、
  全てのチェックが終了した後に`non_duplicate_end.next=None`が必要になる。また、それにより`if head is None`が必要。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checking = head
        non_duplicate_end = head

        if head is None:
            return None

        while checking is not None:
            if checking.val != non_duplicate_end.val:
                non_duplicate_end.next = checking
                non_duplicate_end = checking
            checking = checking.next

        non_duplicate_end.next = None

        return head
```
- step2-4.py
  - `non_duplicate_end`を使わない方法。 重複をまとめて飛ばすことで、node自身だけで完結する。
  - `next_node`を定義すると分かりやすい。しないと`node.next.next`が登場し混乱する。
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node is not None:
            next_node = node.next
            while next_node is not None and node.val == next_node.val:
                next_node = next_node.next
            node.next = next_node
            node = node.next

        return head
```
