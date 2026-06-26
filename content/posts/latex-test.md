---
title: "ブログ中に書く数式に本物のLaTeXを使いたくて頑張った話（可換図式もあるよ）"
date: 2026-06-27T00:46:20+09:00
preamble: |
  \newcommand{\U}{\mathcal{U}}
  \newcommand{\isProp}{\mathrm{isProp}}
  \newcommand{\rec}{\mathrm{rec}}
draft: false
math: true
---

具体的にどのように実現してるかは後で書きます

$$
\gdef\U{\mathcal{U}}
\gdef\isProp{\mathrm{isProp}}
\gdef\rec{\mathrm{rec}}
$$

おいっす

こういうのを書くと、

````md
```math
\begin{tikzcd}
  {F^{n+2}0} && {F^{n+1}0} && {F^n0} \\ \\
  {F^2A} && FA && A
  \arrow["{F^2f_n}", from=1-1, to=3-1]
  \arrow["{Ff_{n+1}}", from=1-1, to=3-3]
  \arrow["{F^{n+1}!}"', from=1-3, to=1-1]
  \arrow["{Ff_n}", from=1-3, to=3-3]
  \arrow["{f_{n+1}}", from=1-3, to=3-5]
  \arrow["{F^n!}"', from=1-5, to=1-3]
  \arrow["{f_n}", from=1-5, to=3-5]
  \arrow["{F\alpha}"', from=3-1, to=3-3]
  \arrow["\alpha"', from=3-3, to=3-5]
\end{tikzcd}
```
````

↓ こういうSVGになります

```math
\begin{tikzcd}
  {F^{n+2}0} && {F^{n+1}0} && {F^n0} \\ \\
  {F^2A} && FA && A
  \arrow["{F^2f_n}", from=1-1, to=3-1]
  \arrow["{Ff_{n+1}}", from=1-1, to=3-3]
  \arrow["{F^{n+1}!}"', from=1-3, to=1-1]
  \arrow["{Ff_n}", from=1-3, to=3-3]
  \arrow["{f_{n+1}}", from=1-3, to=3-5]
  \arrow["{F^n!}"', from=1-5, to=1-3]
  \arrow["{f_n}", from=1-5, to=3-5]
  \arrow["{F\alpha}"', from=3-1, to=3-3]
  \arrow["\alpha"', from=3-3, to=3-5]
\end{tikzcd}
```

プリアンブルもあるよ〜

```tex
\newcommand{\U}{\mathcal{U}}
\newcommand{\isProp}{\mathrm{isProp}}
\newcommand{\rec}{\mathrm{rec}}
```

````md
```math
$\displaystyle \rec_{\|A\|} : \prod_{X : \U} \isProp(X) \to (A \to X) \to \|A\| \to X$
```
````

```math
$\displaystyle \rec_{\|A\|} : \prod_{X : \U} \isProp(X) \to (A \to X) \to \|A\| \to X$
```

でもこういう普通の数式を使いたいときには色々不便なので普通にKaTeXを使った方がよいですね　サイズもデカすぎるし

$$
\rec_{\|A\|} : \prod_{X : \U} \isProp(X) \to (A \to X) \to \|A\| \to X
$$

````md
```math
\begin{tikzcd}
  \|A\| & |[font=\footnotesize]| (\text{when } h : \isProp(X)) \\
  A & X
  \arrow["|-|", from=2-1, to=1-1]
  \arrow["f", from=2-1, to=2-2]
  \arrow["{\rec_{\|A\|}(h, f)}" near end, from=1-1, to=2-2, dashed]
\end{tikzcd}
```
````

```math
\begin{tikzcd}
  \|A\| & |[font=\footnotesize]| (\text{when } h : \isProp(X)) \\
  A & X
  \arrow["|-|", from=2-1, to=1-1]
  \arrow["f", from=2-1, to=2-2]
  \arrow["{\rec_{\|A\|}(h, f)}" near end, from=1-1, to=2-2, dashed]
\end{tikzcd}
```
