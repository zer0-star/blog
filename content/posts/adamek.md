---
title: "Adámekの不動点定理を比較的わかりやすく解説してみる"
date: 2023-11-12 06:11:33+09:00
draft: false
math: true
---

nLabの記事（[terminal coalgebra for an endofunctor in nLab](https://ncatlab.org/nlab/show/terminal+coalgebra+for+an+endofunctor)）を読んでいたら、図式は読みづらいし行間は広いしで、読解にだいぶ時間を使った。せっかくなので、[quiver](q.uiver.app)（図式を簡単に描けるアプリケーション）の練習と埋め込み機能のテストを兼ねて[^amscd]、大部分を参考にしながら自分なりにまとめ直すことにした。

[^amscd]: Katexで可換図式を描く唯一の手段であるAMScdは、斜めの射が描けないなど、不便なのである。

nLabの方ではterminal coalgebraについての定理だが、こっちではinitial algebraのバージョンについて書く。

## Adámekの不動点定理

initial object \\( 0 \\) を持つ圏 \\( C \\)と、その上の自己関手 \\( F \\) を考える。\\( F \\) はcolimitを保つとし、以下のchainがcolimit \\( T \\) を持つとする。

<!-- https://q.uiver.app/#q=WzAsNSxbMCwwLCIwIl0sWzEsMCwiRjAiXSxbMiwwLCJGXjIwIl0sWzMsMCwiRl4zMCJdLFs0LDAsIlxcY2RvdHMiXSxbMCwxLCIhIl0sWzEsMiwiRiEiXSxbMiwzLCJGXjIhIl0sWzMsNCwiRl4zISJdXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNSxbMCwwLCIwIl0sWzEsMCwiRjAiXSxbMiwwLCJGXjIwIl0sWzMsMCwiRl4zMCJdLFs0LDAsIlxcY2RvdHMiXSxbMCwxLCIhIl0sWzEsMiwiRiEiXSxbMiwzLCJGXjIhIl0sWzMsNCwiRl4zISJdXQ==&embed" width="688" height="176" style="border-radius: 8px; border: none;"></iframe>

このとき、射 \\( \theta \colon FT \to T \\) が存在して、\\( (T, \theta) \\) はinitial algebraとなる。

### 証明

まず、\\( T \\) がcolimitであったから、次のようなcoconeがとれる。

<!-- https://q.uiver.app/#q=WzAsNSxbMCwyLCIwIl0sWzIsMiwiRjAiXSxbNCwyLCJGXjIwIl0sWzYsMiwiXFxjZG90cyJdLFszLDAsIlQiXSxbMCwxXSxbMiwzXSxbMSwyXSxbMCw0XSxbMSw0XSxbMiw0XSxbMyw0XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNSxbMCwyLCIwIl0sWzIsMiwiRjAiXSxbNCwyLCJGXjIwIl0sWzYsMiwiXFxjZG90cyJdLFszLDAsIlQiXSxbMCwxXSxbMiwzXSxbMSwyXSxbMCw0XSxbMSw0XSxbMiw0XSxbMyw0XV0=&embed" width="944" height="432" style="border-radius: 8px; border: none;"></iframe>

このcocone全体を \\( F \\) で送って \\( 0 \\) からの射を左下にくっつけると、次のようになる。

<!-- https://q.uiver.app/#q=WzAsNSxbMCwyLCIwIl0sWzIsMiwiRjAiXSxbNCwyLCJGXjIwIl0sWzYsMiwiXFxjZG90cyJdLFszLDAsIkZUIl0sWzAsMV0sWzIsM10sWzEsMl0sWzAsNF0sWzEsNF0sWzIsNF0sWzMsNF1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNSxbMCwyLCIwIl0sWzIsMiwiRjAiXSxbNCwyLCJGXjIwIl0sWzYsMiwiXFxjZG90cyJdLFszLDAsIkZUIl0sWzAsMV0sWzIsM10sWzEsMl0sWzAsNF0sWzEsNF0sWzIsNF0sWzMsNF1d&embed" width="944" height="432" style="border-radius: 8px; border: none;"></iframe>


すると、\\( F \\) がcolimitを保つという条件から、このcoconeもchainのcolimitを与える。colimitの一意性より \\( FT \cong T \\) となるから、この同型射を \\( \theta \colon FT \to T \\) とする。

algebra \\( (T, \theta) \\) が得られたので、これのinitialityを証明するために、任意にalgebra \\( (A, \alpha) \\) をとる。

射の族 \\( f_n \colon F^n 0 \to A \\) を、以下のように帰納的に定義する。

$$
\begin{align*}
f_0 & \text{は、一意射} \\\\
f_{n+1} &= \alpha \circ Ff_n
\end{align*}
$$

すると、これはchainについてcoconeになる。すなわち、\\( f_n = f_{n+1} \circ F^n! \\) となる。

これは、以下のように帰納法により確かめられる（nLabの記事では"It is easily checked by induction"とされていたが、全然easyではないと思う！）。

まず、\\( f_0 \\) についてはいいだろう。（一意であるため）

次に、\\( f_n = f_{n+1} \circ F^n! \\) を仮定して、\\( f_{n+1} \\) について示す。

以下の図式を考えると、これは可換になる（左下の三角形は定義から、右上の三角形は仮定から）。

<!-- https://q.uiver.app/#q=WzAsNCxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMCwwLCJGXntuKzF9MCJdLFsyLDAsIkZebjAiXSxbMCwxLCJcXGFscGhhIiwyXSxbMiwwLCJGZl9uIl0sWzIsMSwiZl97bisxfSJdLFszLDIsIkZebiEiLDJdLFszLDEsImZfbiJdXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMCwwLCJGXntuKzF9MCJdLFsyLDAsIkZebjAiXSxbMCwxLCJcXGFscGhhIiwyXSxbMiwwLCJGZl9uIl0sWzIsMSwiZl97bisxfSJdLFszLDIsIkZebiEiLDJdLFszLDEsImZfbiJdXQ==&embed" width="451" height="432" style="border-radius: 8px; border: none;"></iframe>

この図式全体を \\( F \\) で送り、もとの図式と合わせて以下の可換図式を得る。

<!-- https://q.uiver.app/#q=WzAsNixbMiwyLCJGQSJdLFs0LDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFs0LDAsIkZebjAiXSxbMCwyLCJGXjJBIl0sWzAsMCwiRl57bisyfTAiXSxbMCwxLCJcXGFscGhhIiwyXSxbMiwwLCJGZl9uIl0sWzIsMSwiZl97bisxfSJdLFszLDIsIkZebiEiLDJdLFszLDEsImZfbiJdLFs0LDAsIkZcXGFscGhhIiwyXSxbMiw1LCJGXntuKzF9ISIsMl0sWzUsNCwiRl4yZl9uIl0sWzUsMCwiRmZfe24rMX0iXV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNixbMiwyLCJGQSJdLFs0LDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFs0LDAsIkZebjAiXSxbMCwyLCJGXjJBIl0sWzAsMCwiRl57bisyfTAiXSxbMCwxLCJcXGFscGhhIiwyXSxbMiwwLCJGZl9uIl0sWzIsMSwiZl97bisxfSJdLFszLDIsIkZebiEiLDJdLFszLDEsImZfbiJdLFs0LDAsIkZcXGFscGhhIiwyXSxbMiw1LCJGXntuKzF9ISIsMl0sWzUsNCwiRl4yZl9uIl0sWzUsMCwiRmZfe24rMX0iXV0=&embed" width="726" height="432" style="border-radius: 8px; border: none;"></iframe>

これの真ん中部分だけを取り出すと、次のようになる。

<!-- https://q.uiver.app/#q=WzAsNCxbMiwyLCJGQSJdLFs0LDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFswLDAsIkZee24rMn0wIl0sWzAsMSwiXFxhbHBoYSIsMl0sWzIsMSwiZl97bisxfSJdLFsyLDMsIkZee24rMX0hIiwyXSxbMywwLCJGZl97bisxfSJdXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMiwyLCJGQSJdLFs0LDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFswLDAsIkZee24rMn0wIl0sWzAsMSwiXFxhbHBoYSIsMl0sWzIsMSwiZl97bisxfSJdLFsyLDMsIkZee24rMX0hIiwyXSxbMywwLCJGZl97bisxfSJdXQ==&embed" width="726" height="432" style="border-radius: 8px; border: none;"></iframe>

見やすいように形を整えて、定義から可換となるような射を追加すると、以下の通り。

<!-- https://q.uiver.app/#q=WzAsNCxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFswLDAsIkZee24rMn0wIl0sWzAsMSwiXFxhbHBoYSIsMl0sWzIsMSwiZl97bisxfSJdLFsyLDMsIkZee24rMX0hIiwyXSxbMywwLCJGZl97bisxfSJdLFszLDEsImZfe24rMn0iXV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMiwwLCJGXntuKzF9MCJdLFswLDAsIkZee24rMn0wIl0sWzAsMSwiXFxhbHBoYSIsMl0sWzIsMSwiZl97bisxfSJdLFsyLDMsIkZee24rMX0hIiwyXSxbMywwLCJGZl97bisxfSJdLFszLDEsImZfe24rMn0iXV0=&embed" width="470" height="432" style="border-radius: 8px; border: none;"></iframe>

よって、示された。

さて、これによって \\( (A, f) \\) がchainのcoconeであることがわかった。colimitの普遍性から、一意に射 \\( h \colon T \to A \\) が存在して、以下の図式が可換になる。

<!-- https://q.uiver.app/#q=WzAsNixbMywxLCJUIl0sWzAsMywiMCJdLFsyLDMsIkYwIl0sWzQsMywiRl4yMCJdLFs2LDMsIlxcY2RvdHMiXSxbMywwLCJBIl0sWzEsMiwiISJdLFsyLDMsIkYhIl0sWzMsNCwiRl4yISJdLFsxLDBdLFsyLDBdLFszLDBdLFs0LDBdLFswLDUsImgiLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMSw1LCJmXzAiXSxbNCw1XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNixbMywxLCJUIl0sWzAsMywiMCJdLFsyLDMsIkYwIl0sWzQsMywiRl4yMCJdLFs2LDMsIlxcY2RvdHMiXSxbMywwLCJBIl0sWzEsMiwiISJdLFsyLDMsIkYhIl0sWzMsNCwiRl4yISJdLFsxLDBdLFsyLDBdLFszLDBdLFs0LDBdLFswLDUsImgiLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMSw1LCJmXzAiXSxbNCw1XV0=&embed" width="944" height="560" style="border-radius: 8px; border: none;"></iframe>

ここからゴチャゴチャしてくるので、図式の一部分だけを切り取って載せることにするが、常に考えているのはcocone全体である。

<!-- https://q.uiver.app/#q=WzAsMyxbMCwxLCJUIl0sWzEsMiwiRl5uMCJdLFswLDAsIkEiXSxbMSwwXSxbMCwyLCJoIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsMiwiZl9uIiwyXV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsMyxbMCwxLCJUIl0sWzEsMiwiRl5uMCJdLFswLDAsIkEiXSxbMSwwXSxbMCwyLCJoIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsMiwiZl9uIiwyXV0=&embed" width="304" height="432" style="border-radius: 8px; border: none;"></iframe>

これをさらに \\( F \\) で送ったものを考えると、\\( T \\) の普遍性から、以下の図式が可換になる。

<!-- https://q.uiver.app/#q=WzAsNCxbMCwxLCJGVCJdLFsyLDMsIkZee24rMX0wIl0sWzAsMCwiRkEiXSxbMCwyLCJUIl0sWzEsMF0sWzAsMiwiRmgiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMSwyLCJGZl9uIiwyXSxbMSwzXSxbMywwLCJcXHRoZXRhXnstMX0iLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0= -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwxLCJGVCJdLFsyLDMsIkZee24rMX0wIl0sWzAsMCwiRkEiXSxbMCwyLCJUIl0sWzEsMF0sWzAsMiwiRmgiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMSwyLCJGZl9uIiwyXSxbMSwzXSxbMywwLCJcXHRoZXRhXnstMX0iLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0=&embed" width="451" height="560" style="border-radius: 8px; border: none;"></iframe>


さらに、\\( f_n \\) の定義から、以下が可換になる。

<!-- https://q.uiver.app/#q=WzAsNSxbMCwyLCJGVCJdLFsyLDQsIkZee24rMX0wIl0sWzAsMSwiRkEiXSxbMCwzLCJUIl0sWzAsMCwiQSJdLFsxLDBdLFswLDIsIkZoIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsMiwiRmZfbiIsMV0sWzEsM10sWzMsMCwiXFx0aGV0YV57LTF9IiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsNCwiZl97bisxfSIsMl0sWzIsNCwiXFxhbHBoYSJdXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNSxbMCwyLCJGVCJdLFsyLDQsIkZee24rMX0wIl0sWzAsMSwiRkEiXSxbMCwzLCJUIl0sWzAsMCwiQSJdLFsxLDBdLFswLDIsIkZoIiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsMiwiRmZfbiIsMV0sWzEsM10sWzMsMCwiXFx0aGV0YV57LTF9IiwwLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzEsNCwiZl97bisxfSIsMl0sWzIsNCwiXFxhbHBoYSJdXQ==&embed" width="451" height="688" style="border-radius: 8px; border: none;"></iframe>

よって、\\( \alpha \circ Fh \circ \theta^{-1} \\) はcoconeの間の射なので、一意性より以下の図式が可換になる。

<!-- https://q.uiver.app/#q=WzAsNCxbMCwwLCJGVCJdLFsyLDAsIlQiXSxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMSwwLCJcXHRoZXRhXnstMX0iLDJdLFswLDIsIkZoIiwyXSxbMiwzLCJcXGFscGhhIl0sWzEsMywiaCIsMl1d -->
<iframe class="quiver-embed" src="https://q.uiver.app/#q=WzAsNCxbMCwwLCJGVCJdLFsyLDAsIlQiXSxbMCwyLCJGQSJdLFsyLDIsIkEiXSxbMSwwLCJcXHRoZXRhXnstMX0iLDJdLFswLDIsIkZoIiwyXSxbMiwzLCJcXGFscGhhIl0sWzEsMywiaCIsMl1d&embed" width="432" height="432" style="border-radius: 8px; border: none;"></iframe>

すなわち、\\( h \\) は \\( (T, \theta) \\) から \\( (A, \alpha) \\) への一意なalgebra mapである。 \\( \blacksquare \\)

## おわりに

証明が間違っていたりしたら教えてください。