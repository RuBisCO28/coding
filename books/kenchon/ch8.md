# 配列、連結リスト、ハッシュテーブル
## 計算量

|操作|配列|連結リスト|ハッシュテーブル|
|--|--|--|--|
|i番目の要素へのアクセス|O(1)|O(N)|-|
|要素xを挿入|O(1)|O(1)|O(1)|
|要素xを特定の要素の直後に挿入|O(N)|O(1)|O(1)|
|要素xを削除|O(N)|O(1)|O(1)|
|要素xを検索|O(N)|O(N)|O(1)|

## 配列
- 特定のデータにアクセスするのに適した構造
- 一方で、要素の挿入、削除は苦手(検索も伴う)

## 連結リスト
- 要素が何番目の要素かという情報を持たず、前の要素の情報だけもっている
- このため挿入、削除が容易
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next

  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.data)
      node = node.next
    nodes.append("None")
    return " -> ".join(nodes)
```

## ハッシュテーブル
- どのキーに対してもハッシュ値が異なるようなハッシュ関数が設計できた場合の各処理

|クエリ|計算量|実装|
|要素xの挿入|O(1)|T[h(x)]<-true|
|要素xの削除|O(1)|T[h(x)]<-false|
|要素xの検索|O(1)|T[h(x)]がtrueかどうか|

### ハッシュの衝突対策
- ハッシュ値が等しくなる可能性があるので、解決方法として各ハッシュ値ごとに連結リストを構築する方法が代表的

### 実装
```python
l = [1,2,2,3,1,4]
s_l = set(l)
s_l.add(5)
print(s_l)
s_l.remove(5)
print(s_l)
```
