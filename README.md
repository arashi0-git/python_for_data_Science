# python_for_data_Science
practice python for data science

## What difference "List", "Tuple", "Set", "Dict"
| 特徴 | List (リスト) | Tuple (タプル) | Set (集合) | Dict (辞書) |
| --- | --- | --- | --- | --- |
| 定義 | `[ ]` | `( )` | `{ }` (要素なしは `set()`) | `{キー: 値}` |
| 順序 | あり | あり | なし | あり (3.7+) |
| 重複 | 許可 | 許可 | 不可 | キーは不可 |
| 変更可否 | 変更可能 (ミュータブル) | 変更不可 (イミュータブル) | 変更可能 (ミュータブル) | 変更可能 (ミュータブル) |
| 主な用途 | 頻繁に変更する順序付きデータ | 変更しないデータの保持、高速アクセス | 重複排除、高速なメンバーシップテスト | キーと値の関連付け管理 |

```
my_list = [1, 2, 2, 3]
my_tuple = (1, 2)
my_set = {1, 2, 2, 3} # => {1, 2, 3}  重複はなし
my_dict = {1: 'a', 2: 'b'}
my_list_from_dict = list(my_dict.keys()) # [1, 2]
```

* https://qiita.com/ishida330/items/9692836aa860b2d0c36c
