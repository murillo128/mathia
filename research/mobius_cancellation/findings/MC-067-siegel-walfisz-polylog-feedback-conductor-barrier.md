# MC-067 — Page–Siegel extends the positive quadratic-feedback barrier to stretched-exponential conductors

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the square-free quadratic comparator of `MC-066`. Let `q` be an odd prime,

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
f_\chi(n)=\mu(n)^2\chi(n),
\qquad
h_\chi=1*f_\chi,
\]

and recall the exact local coefficients

\[
h_\chi(p^a)=
\begin{cases}
0,&\chi(p)=-1,\\
2,&\chi(p)=+1,\\
1,&p=q,
\end{cases}
\qquad a\ge1.
\tag{1}
\]

For `0<theta<1`, define the positive feedback budget

\[
R_\theta(X;\chi)
:=
\sum_{2\le d\le X}\frac{h_\chi(d)}{d^\theta}.
\tag{2}
\]

There is an absolute constant `b>0` with the following property. For every fixed `eta>0`, uniformly for odd prime conductors

\[
q\le \exp\!\bigl(b\sqrt{\log X}\bigr)
\tag{3}
\]

and exponents

\[
0<\theta\le1-\eta,
\tag{4}
\]

one has, for all sufficiently large `X`,

\[
\boxed{R_\theta(X;\chi)>1.}
\tag{5}
\]

More quantitatively, if `L(s,chi)` has no exceptional zero in the classical Page region, then

\[
R_\theta(X;\chi)
\gg
\frac{X^{1-\theta}}{\log X}.
\tag{6}
\]

If it has an exceptional zero `beta`, then after choosing `b` sufficiently small relative to the effective constant in the classical Page prime-number theorem,

\[
R_\theta(X;\chi)
\gg
X^{1-\theta}\exp\!\left(-\frac b2\sqrt{\log X}\right).
\tag{7}
\]

Both lower bounds diverge for every fixed `theta<=1-eta`. Thus the positive-kernel triangle bootstrap from `MC-066`, which requires `R_theta(X;chi)<1`, cannot use **any** prime quadratic conductor up to stretched-exponential scale `(3)`, whether or not a Landau–Siegel zero is present.

This strictly strengthens the original Siegel–Walfisz conclusion of this finding. The previous argument excluded every fixed polylogarithmic conductor. The exceptional-zero audit shows that the same architecture actually fails throughout

\[
q\le \exp\!\bigl(b\sqrt{\log X}\bigr).
\tag{8}
\]

Combining `(8)` with the Munsch/Burgess squarefree-character certificate retained in `MC-064`--`MC-066`, a near-critical implementation satisfying

\[
|F_\chi(X)|=X^{1/2+o(1)}
\]

through the displayed classical bound still requires `q=X^{o(1)}`. Hence the method-specific surviving conductor window is narrowed to

\[
\boxed{
\exp\!\bigl(b\sqrt{\log X}\bigr)<q<X^{o(1)}.
}
\tag{9}
\]

Equation `(9)` is only a necessary search corridor for this exact certificate package. It does not assert that suitable characters exist there, and no improved bound for `M(X)` is claimed.

## 1. Terminal split primes are enough to break contraction

Let

\[
\mathcal P_+(X;\chi)
:=
\{p:X/2<p\le X,\ \chi(p)=+1\}.
\tag{10}
\]

Every prime in this set contributes `h_chi(p)=2`. Positivity therefore gives

\[
R_\theta(X;\chi)
\ge
2\sum_{p\in\mathcal P_+(X;\chi)}p^{-\theta}
\ge
2X^{-\theta}\#\mathcal P_+(X;\chi).
\tag{11}
\]

It is enough to prove that the terminal interval contains sufficiently many split primes. Put

\[
\vartheta(x)=\sum_{p\le x}\log p,
\qquad
\vartheta(x,\chi)=\sum_{p\le x}\chi(p)\log p.
\tag{12}
\]

Except for the conductor prime itself,

\[
2\mathbf 1_{\chi(p)=1}=1+\chi(p)
\]

on primes. Hence

\[
2\sum_{p\in\mathcal P_+(X;\chi)}\log p
=
\bigl(\vartheta(X)-\vartheta(X/2)\bigr)
+
\bigl(\vartheta(X,\chi)-\vartheta(X/2,\chi)\bigr)
+O(\log q).
\tag{13}
\]

The ordinary prime number theorem gives

\[
\vartheta(X)-\vartheta(X/2)
=
\frac X2+O\!\left(Xe^{-c\sqrt{\log X}}\right).
\tag{14}
\]

The only question is therefore how much the quadratic twist can cancel this terminal prime mass.

## 2. The non-exceptional case gives positive-density split mass

`MC-S15`, Montgomery and Vaughan, Chapter 11, Theorem 11.16, gives an effective constant `c_1>0` such that for

\[
q\le\exp\!\bigl(2c_1\sqrt{\log x}\bigr)
\]

a nonprincipal character with no exceptional zero satisfies

\[
\psi(x,\chi)
\ll
x e^{-c_1\sqrt{\log x}}.
\tag{15}
\]

Removing prime powers changes this by only `O(sqrt(x) log^2 x)`, which is negligible here. Taking `b<c_1` ensures that `(15)` applies at both `x=X` and `x=X/2` once `X` is large. Thus

\[
\vartheta(X,\chi)-\vartheta(X/2,\chi)
=
o(X).
\tag{16}
\]

Equations `(13)`--`(16)` imply

\[
\sum_{p\in\mathcal P_+(X;\chi)}\log p
\ge cX
\tag{17}
\]

for an absolute `c>0`, and therefore

\[
\#\mathcal P_+(X;\chi)
\gg \frac X{\log X}.
\tag{18}
\]

Substitution into `(11)` proves `(6)`. This is the same mechanism as the former polylogarithmic Siegel–Walfisz argument, but the twisted Page estimate reaches the much larger range `(3)` without summing errors separately over residue classes.

## 3. An exceptional zero cannot save a sufficiently small stretched-exponential conductor

Suppose now that `L(s,chi)` has an exceptional real zero `beta`, and write

\[
\delta:=1-\beta>0.
\]

In the same range, Theorem 11.16 gives

\[
\psi(x,\chi)
=
-\frac{x^\beta}{\beta}
+O\!\left(xe^{-c_1\sqrt{\log x}}\right).
\tag{19}
\]

Thus the main part of `(13)` is no longer `X/2`: the exceptional term almost cancels it on residue classes with `chi=+1`. The exact remaining main mass is

\[
\frac X2-rac{X^\beta-(X/2)^\beta}{\beta}
=
\int_{X/2}^{X}\bigl(1-t^{-\delta}\bigr)\,dt.
\tag{20}
\]

This identity isolates the only possible loophole. For `t in [X/2,X]`,

\[
1-t^{-\delta}
=1-e^{-\delta\log t}
\gg
\min\{1,\delta\log X\},
\tag{21}
\]

so

\[
\int_{X/2}^{X}(1-t^{-\delta})dt
\gg
X\min\{1,\delta\log X\}.
\tag{22}
\]

The classical Siegel lower bound in `MC-S15`, Corollary 11.15, applied with `epsilon=1/2`, gives a positive constant `C` such that

\[
\delta\ge Cq^{-1/2}.
\tag{23}
\]

For conductors satisfying `(3)`,

\[
\delta\log X
\gg
(\log X)\exp\!\left(-\frac b2\sqrt{\log X}\right).
\tag{24}
\]

Choose `b>0` small enough that `b/2<c_1` and also small enough for Theorem 11.16 to apply at `X/2`. Then the lower bound in `(22)` dominates the error term in `(19)` and the prime-power error. Equations `(13)` and `(20)`--`(24)` yield

\[
\sum_{p\in\mathcal P_+(X;\chi)}\log p
\gg
X(\log X)\exp\!\left(-\frac b2\sqrt{\log X}\right).
\tag{25}
\]

Consequently,

\[
\#\mathcal P_+(X;\chi)
\gg
X\exp\!\left(-\frac b2\sqrt{\log X}\right),
\tag{26}
\]

and `(11)` gives `(7)`.

For every fixed `eta>0` and `theta<=1-eta`,

\[
X^{1-\theta}e^{-(b/2)\sqrt{\log X}}
\ge
X^\eta e^{-(b/2)\sqrt{\log X}}
\longrightarrow\infty,
\]

so even the strongest possible exceptional bias in this classical range cannot make the positive feedback contractive.

The threshold is mathematically meaningful. Page's formula allows the split-prime main term to be almost annihilated by an exceptional zero; the reason it still beats the error in `(3)` is precisely that Siegel's `q^{-1/2}` lower bound on `1-beta` decays more slowly than the `e^{-c_1 sqrt(log X)}` Page error when `log q` is a sufficiently small multiple of `sqrt(log X)`.

## 4. Coupling to the squarefree-character certificate

`MC-S38`, Munsch's squarefree-character estimate, gives for prime `q`

\[
|F_\chi(X)|
\ll
X^{1/2}q^{3/16}(\log X)(\log q)^{1/2}.
\tag{27}
\]

At a fixed target `theta=1/2+epsilon`, this theorem can certify

\[
|F_\chi(X)|\le X^{\theta+o(1)}
\]

only while

\[
q\le X^{16\varepsilon/3+o(1)}.
\tag{28}
\]

If the target exponent tends to `1/2`, the same certificate requires `q=X^{o(1)}`. The feedback side now simultaneously requires

\[
q>\exp\!\bigl(b\sqrt{\log X}\bigr)
\tag{29}
\]

for all sufficiently large `X`, producing `(9)`.

This remains a method-specific squeeze. A larger conductor may have a much smaller true squarefree character sum than `(27)` certifies, and a better comparator theorem would change the upper pressure. Conversely, `(29)` is tied to the positive-kernel triangle closure `R_theta<1`; a genuinely signed treatment of the feedback terms in

\[
M(X)=F_\chi(X)-\sum_{2\le d\le X}h_\chi(d)M(X/d)
\]

lies outside this obstruction.

## 5. Prior art and novelty boundary

All analytic-number-theory ingredients are classical. `MC-S15` is the primary retained anchor: Chapter 11 contains Page's exceptional-zero prime-number theorem, the effective `q<=exp(c sqrt(log x))` twisted-prime range, the Siegel lower bound for real zeros, and the usual Siegel–Walfisz corollary. The displayed formulas `(15)` and `(19)` are direct specializations of Theorem 11.16. The passage from `psi` to `vartheta`, the terminal-interval identity `(13)`, and the elementary deficit identity `(20)` add no new theorem about Dirichlet `L`-functions.

`MC-S38` supplies the independent squarefree-character estimate used on the comparator side. A targeted audit against Page/Landau exceptional-character theory, Siegel–Walfisz, and squarefree character-sum literature gives no basis for a standalone novelty claim. The retained contribution is instead a line-specific obstruction: applying the classical exceptional-zero dichotomy to the exact positive feedback carrier from `MC-066` enlarges the excluded conductor region from every fixed polylogarithmic scale to a fixed stretched-exponential scale.

The original polylogarithmic result remains true as an immediate subrange of `(3)`. Its former use of Siegel–Walfisz is therefore preserved conceptually but is no longer the strongest canonical statement.

## 6. Boundaries and falsification tests

The conclusion is deliberately restricted to the positive-kernel triangle bootstrap of `MC-066`.

- The proof uses only the prime terms of `R_theta`, so positive composite coefficients cannot repair the failure of contraction. A future argument that preserves signs of `h_chi(d)M(X/d)` rather than replacing them by `R_theta` is not covered.
- The uniform conclusion assumes `theta<=1-eta` for fixed `eta>0`. It says nothing when `theta` approaches `1` so rapidly that the power gain no longer dominates the stretched-exponential loss. This boundary is irrelevant to the intended Mertens/RH exponents near `1/2` but is real.
- The constant `b` is not optimized. It is chosen below the constants in the classical Page theorem so that `(19)` applies at both endpoints and the exceptional main deficit dominates the error.
- The quadratic character is primitive because `q` is prime. Composite-conductor extensions would require tracking induction and conductor factors separately and are not asserted here.
- No existence or nonexistence claim is made for characters in the surviving corridor `(9)`.
- No Riemann-zeta zero-free region, RH-equivalent Mertens estimate, or continuation of `1/zeta(s)` is used in deriving `(5)`.

The strengthened claim would fail if one could find arbitrarily large `X`, a prime `q<=exp(b sqrt(log X))`, and a quadratic character for which the terminal split-prime mass is smaller than the Page/Siegel formulas permit, or if the local coefficient identity `h_chi(p)=2` on split primes failed. The classical estimates and the exact convolution coefficient rule exclude those possibilities.

## Consequence for the active frontier

The absolute one-character transfer of `MC-065` had an `11/19` floor. `MC-066` correctly showed that signed convolution removes that particular conductor-zero floor, but replaces it with the positive split-prime feedback budget. The earlier version of this finding proved that merely making the conductor polylogarithmic could not solve that budget.

The stronger audit now closes a much larger escape: **even an exceptional quadratic character cannot make the positive feedback contractive while its conductor stays below `exp(b sqrt(log X))`**. A near-critical quadratic-comparator strategy using Munsch's certificate must therefore move into the narrower intermediate range `(9)`, improve the comparator theorem enough to alter that range, or abandon the positive triangle closure and exploit signed cancellation inside the feedback itself.