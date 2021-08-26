---
title: "First-Class Patterns を自作言語に導入したい話"
date: 2021-08-26T00:31:26+09:00
draft: false
---

Ramune という言語を作ろうとしているんですが、そこに First-Class Patterns を導入することを妄想しているので、それについて書きます

まだ妄想でしかないので、よく分からないようなことを口走っていると思います（すみません！）

First-Class Patterns については、[こういうの（slideshare）](https://www.slideshare.net/jdegoes/firstclass-patterns)とか[こういうの（hackage）](https://hackage.haskell.org/package/first-class-patterns)とか見るといいかもしれない

{{< tweet 1362810124155293698 >}}

こんな気の抜けたことも言っています（アホなので）

# Pattern as Function

要は、パターンというのは関数`a -> Maybe b`とみなせて、関数を適用して`Just`ならマッチ成功、`Nothing`なら失敗とすればパターンマッチが実現できますよね、ということ <!-- で、パターンを値として取り回すことが可能になる -->

先ほど挙げた hackage のやつでは、マッチした結果を右辺の関数に渡すことで束縛の代用とされているが、Ramune では First-Class Patterns をネイティブにサポートして、レコード型（Haskell のようにデータ型の一部ではなく、PureScript のように単体で存在するもの）を介して識別子を束縛したい（`{ x :: Int }`が返ってきたら`x`が`Int`型の値に束縛されるように）

パターンの型は Haskell 風に書くと`newtype Pattern a r = Pattern { runPattern :: a -> Maybe r }`（`r`はレコード型）と定義できる。例えば、座標平面上の点を受け取ってx座標を`x`に、y座標を`y`に束縛するパターン`point`は、疑似 Haskell で`point = Pattern $ \(x, y) -> Just { x = x, y = y }`と書ける。このとき`point`は`Pattern (a, b) { x :: a, y :: b }`というような型を持つ値になるだろう。

記述を平易にするため、いくつか特別な記法を導入しようと思う。

1つが、variable pattern と呼ばれる（予定の）構文である。`#x`と書くと、受け取った値をそのまま`x`に束縛するパターン（疑似 Haskell では`Pattern $ \x -> Just {x = x}`）を表す。当然これは式であるため、他の式が書けるところならどこにでも書ける。

```haskell
-- トップレベルの識別子に束縛しちゃったり
xPat :: Pattern a { x :: a }
xPat = #x

-- 単なる値なのでタプルに突っ込むことができる
a :: (Int, Pattern a { x :: a })
a = (42, #x)

-- 型を制限することもできる
intX :: Pattern Int { x :: Int }
intX = #x
```

もう1つは、constructor pattern と呼ばれる（かもしれない）構文である。`data Pair a b = Pair a b` のように型`Pair a b`を定義したとき、コンストラクタ`Pair :: a -> b -> Pair a b`に対して、いわば「パターン・コンストラクタ」とでも呼べるような、パターンを受け取ってパターンを返す関数`#Pair :: Pattern a r1 -> Pattern b r2 -> Pattern (Pair a b) (r1 +++ r2)`（ただし、`+++`はレコードの併合）が定義される。使い方はご想像の通り、`#Pair #a #b`のようにすれば良い。演算子になっているコンストラクタにも同様。

ちなみに、constructor pattern の派生として、`#(p1, p2, p3)`や`#[p1, p2, p3, p4]`といったものも考えている。これを使えば、先ほどの`point`は`#(#x, #y)`と簡単に書くことができる。

```haskell
-- 疑似Haskellで書くと、こう
pair :: Pattern (a, b) { x :: a, y :: b }
pair = Pattern $ \(x, y) -> { x = x, y = y }

-- しかし、単純なパターンの合成は簡潔に書ける（こともある）
pair :: Pattern (a, b) { x :: a, y :: b }
pair = #(#x, #y)
```

# Matching as MonadPlus

パターンについて書いたのだから、マッチングについても書かなくてはいけないだろう。

見出しの通り、マッチングは`MonadPlus`の演算を繰り返していくことと解釈することができる。

```haskell
-- 以下のように定義したとき、
f p1 p2 ... pn = body
f q1 q2 ... qn = body

-- 以下の式は、
f a1 a2 ... an

-- 以下のような式と等価（{..} はHaskellのRecordWildCardsをイメージ）
let
  pClause = do
    {..} <- runPattern p1 a1
    {..} <- runPattern p2 a2
    ...
    {..} <- runPattern pn an
    return body

  qClause = do
    {..} <- runPattern q1 a1
    {..} <- runPattern q2 a2
    ...
    {..} <- runPattern qn an
    return body
in
  fromJust $ pClause `mplus` qClause
```

ちなみに、`p1`で束縛した識別子は`p2`以降で利用可能だったりする予定。

ところで、パターンマッチは関数の引数以外でも使うことができる。

```haskell
f #p = let #(#x, #y) = p
        in x + y

g #x = case x of
         #Just #v -> show v
         #Nothing -> "Nothing"
```

まあ説明も必要ないだろうとは思う。

# 問題点・悩んでいるところなど

そもそも、パターンが値と言うことはパターンに束縛された識別子が存在しうるわけで、そうなったときに`f x = ...`などと書くと非常に紛らわしくて分かりづらい。`let x = ...`のようなケースは、0引数関数の宣言とみなすことで`let #x = ...`と等価になるのだが、`f x = ...`を`f #x = ...`とみなすのは無理がある。せいぜい warning を出して、推奨スタイルを`f (x) = ...`のように単一の識別子はカッコで囲むこととするくらいしかできないような気がする。

これは仕方がないのだが、パターンマッチの網羅性検査がめちゃくちゃ難しくなる。そもそも他の言語でもガード節がある時点で厳密な網羅性検査はできなくて、First-Class Patterns を採用するとより厳しくなるのは当然の道理ではある。まあ、がんばってコンパイラ内部で網羅性の情報を持ち回ってそれなりの検査はできるかもしれない。

あと、value pattern（値が等しければマッチするパターン）というのを考えていて、簡潔に書きたいのだけど、その構文が思いつかない

# ところで......

ところで、ユーザーが定義したパターンに対して、独自のエラーメッセージを持たせたいことがあるかもしれない。そこまでいかなくとも、マッチの結果を`Maybe`で表していては心もとないこともある。実際面では、`Either`にエラーの型を持たせるとか、独自のデータ型を定義するとか、そういう方針がいいかもしれない。そうなってくると、そういった型をまとめるために独自に`MonadMatch`とかを作るのもアリかもしれない。

あと、私は思いつかなかったが、もしかしたら`Lens`と連携して何かができるかもしれない。

# 使用例

ここのコードは、あくまでもイメージです

```haskell
is :: (a -> Bool) -> Pattern a {}
is p = Pattern $ \#x -> if p x then Just {} else Nothing

which :: Pattern a xs -> Pattern a ys -> Pattern a (xs +++ ys)
which p1 p2 = do
  r1 <- p1
  r2 <- p2
  return $ r1 +++ r2

collatz :: Int -> Int
collatz (#n `which` is even) = n `div` 2
collatz #n = 3 * n + 1
```

```haskell
reversed :: Pattern [a] r -> Pattern [a] r
reversed (Pattern p) = Pattern $ p . reverse

last :: [a] -> Maybe a
last (reversed $ #x #: _) = Just x
last _ = Nothing
```
