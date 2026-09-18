# MC-376 — Quadratic conductor saturation carries a macroscopic inverse-root-rank bias population

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `BOUNDARY-POPULATION` · `STRUCTURAL-RIGIDITY` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint partition of `MC-296`, the full-cube energy calculation of `MC-301`, and the quartic-source conductor saturation of `MC-375`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\to\infty,
\]

with endpoint-cell weights

\[
d_i>0,
\qquad
\sum_{i=1}^R d_i=1.
\tag{1}
\]

For `I\subseteq[R]`, write

\[
\lambda_I=\sum_{i\in I}\lambda_i,
\qquad
d(I)=\sum_{i\in I}d_i.
\]

The exact endpoint law is

\[
x_{\lambda_I}
=(-1)^{|I|}\bigl(1-2d(I)\bigr).
\tag{2}
\]

Put

\[
S_2:=\sum_{i=1}^R d_i^2,
\qquad
S_4:=\sum_{i=1}^R d_i^4.
\tag{3}
\]

Then a uniformly random full-cube mode has the exact moments

\[
\boxed{
2^{-R}\sum_I |x_{\lambda_I}|^2=S_2
}
\tag{4}
\]

and

\[
\boxed{
2^{-R}\sum_I |x_{\lambda_I}|^4
=3S_2^2-2S_4
\le3S_2^2.
}
\tag{5}
\]

Consequently the endpoint energy cannot be hidden in a thin set of unusually large modes. One has the finite counting bound

\[
\boxed{
\#\left\{I:\ |x_{\lambda_I}|
\ge\sqrt{\frac{S_2}{2}}\right\}
\ge\frac{2^R}{12}.
}
\tag{6}
\]

Since `S_2\ge1/R`, this implies

\[
\boxed{
\#\left\{I:\ |x_{\lambda_I}|
\ge\frac1{\sqrt{2R}}\right\}
\ge\frac{2^R}{12}.
}
\tag{7}
\]

Now impose the quartic-saturated common-source regime of `MC-375`,

\[
\frac{\log P}{\log y}=4+o(1),
\qquad
R=y^{o(1)},
\tag{8}
\]

and let `\mathcal Q(\lambda_I)` be the minimum primitive lower-prime source conductor of the nonzero mode. `MC-375` proves that for every fixed `\delta>0`,

\[
\frac1{2^R}
\#\left\{I\ne0:
\left|\frac{\log\mathcal Q(\lambda_I)}{\log y}-2\right|>\delta
\right\}
\longrightarrow0.
\tag{9}
\]

Intersecting `(7)` with `(9)` therefore gives the new boundary-population statement

\[
\boxed{
\#\left\{I\ne0:
 y^{2-\delta}<\mathcal Q(\lambda_I)<y^{2+\delta},
\quad
 |x_{\lambda_I}|\ge\frac1{\sqrt{2R}}
\right\}
\ge
\left(\frac1{12}-o(1)\right)2^R.
}
\tag{10}
\]

Thus the quadratic conductor boundary exposed by `MC-323`--`MC-375` is not populated merely by many almost-unbiased modes. A **positive fraction of the entire endpoint Fourier cube** must simultaneously carry near-quadratic primitive conductor and shell bias at least of inverse-square-root-rank size.

The common source budget turns this into an explicit logarithmic bias floor. If `U` is the set of distinct source primes in the fixed package, then the `R` independent source representatives are linearly independent vectors in `\mathbf F_2^U`, hence

\[
R\le |U|.
\tag{11}
\]

Also `P=\prod_{p\in U}p\ge2^{|U|}`, so `(8)` gives

\[
R\le |U|
\le \frac{\log P}{\log2}
=O(\log y).
\tag{12}
\]

Therefore `(10)` implies, for every fixed `\delta>0`,

\[
\boxed{
\#\left\{I\ne0:
 y^{2-\delta}<\mathcal Q(\lambda_I)<y^{2+\delta},
\quad
 |x_{\lambda_I}|\gg(\log y)^{-1/2}
\right\}
\ge
\left(\frac1{12}-o(1)\right)2^R.
}
\tag{13}
\]

The implied constant in the displayed `\gg` is absolute. Using the actual odd-prime source floor improves it harmlessly; no such optimization matters here.

This sharpens the live analytic target. A theorem capable of killing the quartic-saturated endpoint does not merely need to find one exceptional quadratic-boundary character. It must be incompatible with a macroscopic family of distinct primitive real characters at conductor `y^{2+o(1)}` whose prime-shell biases are only logarithmically small. No estimate for `M(x)` follows.

## 1. The endpoint bias is a Rademacher sum in magnitude

Choose `I\subseteq[R]` uniformly and define independent signs

\[
\varepsilon_i=
\begin{cases}
+1,&i\notin I,\\
-1,&i\in I.
\end{cases}
\tag{14}
\]

Then

\[
1-2d(I)=\sum_{i=1}^R d_i\varepsilon_i.
\tag{15}
\]

The prefactor `(-1)^{|I|}` in `(2)` changes only the sign, so

\[
|x_{\lambda_I}|
=\left|\sum_i d_i\varepsilon_i\right|.
\tag{16}
\]

Let

\[
Y:=\sum_i d_i\varepsilon_i.
\]

Independence and `\mathbf E\varepsilon_i=0` give

\[
\mathbf E Y^2=\sum_i d_i^2=S_2,
\tag{17}
\]

which is `(4)`. Expanding the fourth power, only index patterns in which every sign occurs an even number of times survive:

\[
\mathbf E Y^4
=\sum_i d_i^4
+6\sum_{i<j}d_i^2d_j^2.
\tag{18}
\]

Since

\[
S_2^2
=\sum_i d_i^4
+2\sum_{i<j}d_i^2d_j^2,
\]

we obtain

\[
\mathbf E Y^4=3S_2^2-2S_4,
\tag{19}
\]

proving `(5)`.

This is the elementary Rademacher fourth-moment identity. No probability model for Möbius is being introduced: the independent signs are only the uniform coordinates of the exact finite Fourier cube of endpoint modes.

## 2. A direct second/fourth-moment argument forces a positive fraction of biased modes

Let

\[
\mathcal G
:=\left\{I:Y_I^2\ge\frac{S_2}{2}\right\},
\qquad
p:=2^{-R}|\mathcal G|.
\tag{20}
\]

Split the exact second moment over `\mathcal G` and its complement. On `\mathcal G^c`, `Y_I^2<S_2/2`, so

\[
S_2
=\mathbf E Y^2
\le\frac{S_2}{2}
+\mathbf E\bigl[Y^2 1_{\mathcal G}\bigr].
\tag{21}
\]

Cauchy--Schwarz and `(5)` give

\[
\mathbf E\bigl[Y^2 1_{\mathcal G}\bigr]
\le
(\mathbf E Y^4)^{1/2}p^{1/2}
\le
\sqrt3\,S_2\sqrt p.
\tag{22}
\]

Hence

\[
\frac12\le\sqrt{3p},
\qquad
p\ge\frac1{12},
\tag{23}
\]

which proves `(6)` without importing a named concentration theorem.

Finally Cauchy--Schwarz applied to `(1)` gives

\[
1=\left(\sum_i d_i\right)^2
\le R\sum_i d_i^2
=RS_2,
\tag{24}
\]

so `S_2\ge1/R` and `(7)` follows.

The estimate is intentionally robust rather than constant-optimal. For equal defects `d_i=1/R`, the full distribution is the ordinary normalized Rademacher sum and a much larger fraction lies at the `R^{-1/2}` scale. The point of `(6)` is that **no balance hypothesis at all is required**.

## 3. Conductor concentration and bias anti-concentration intersect at positive density

For fixed `\delta>0`, let

\[
\mathcal C_\delta
:=\left\{I\ne0:
 y^{2-\delta}<\mathcal Q(\lambda_I)<y^{2+\delta}
\right\}.
\tag{25}
\]

Equation `(9)` says

\[
|\mathcal C_\delta|
=(1-o(1))2^R.
\tag{26}
\]

Equation `(6)` supplies a set `\mathcal G` of at least `2^R/12` modes. Therefore

\[
|\mathcal G\cap\mathcal C_\delta|
\ge
|\mathcal G|-|\mathcal C_\delta^c|
\ge
\left(\frac1{12}-o(1)\right)2^R.
\tag{27}
\]

The zero mode contributes at most one element and is absorbed by the `o(2^R)` term because `R\to\infty`. This proves `(10)`.

The conclusion is stronger than the total-energy identity in `MC-301`. That identity gives

\[
\sum_I|x_{\lambda_I}|^2=2^R S_2,
\tag{28}
\]

but by itself allows the logical possibility that most of the energy is concentrated in a small set of modes. Equations `(5)`--`(7)` remove that escape: a fixed positive fraction of the cube carries the natural square-root energy scale.

It is also complementary to the fixed-Hamming-layer identity in `MC-372`. There the middle layer measures the endpoint `L^2` defect imbalance exactly. Here no Hamming conditioning is imposed; the full cube is used to show that the endpoint spectrum itself has unavoidable anti-concentration.

## 4. Why this changes the quadratic-boundary target

`MC-323` shows that for every fixed conductor gap `\delta>0`, prime Halász--Montgomery controls the total bias energy of distinct cubefree characters with conductor at most `y^{2-\delta}`. `MC-373` makes the approach to that boundary effective, and `MC-374`--`MC-375` show that a quartic-efficient endpoint is forced to place almost all modes at the quadratic boundary instead.

The present result adds the missing amplitude statement. Among those boundary modes, at least a positive fraction retain bias

\[
|x_{\lambda_I}|\ge R^{-1/2}/\sqrt2.
\tag{29}
\]

Thus a future boundary theorem must distinguish a family with three simultaneous features:

1. distinct primitive real characters;
2. conductor exponent `2+o(1)` at the prime-shell scale `y`;
3. a macroscopic population with bias of order at least `R^{-1/2}`.

The third feature matters because a theorem that only excludes a fixed positive bias does not address this surviving population when `R\to\infty`. Conversely, an average theorem that reaches the quadratic boundary with normalized energy `o(2^R/R)` would contradict `(28)` immediately; a theorem that controls the number of biases above `cR^{-1/2}` by `o(2^R)` would contradict `(10)` directly.

This isolates a sharper theorem surface than “improve the conductor bound”: **quadratic-boundary prime-family cancellation must reach the inverse-root-rank amplitude scale on a positive fraction of a coherent multiquadratic Fourier cube.**

## Prior art and novelty boundary

No external analytic theorem is added here. Equations `(17)`--`(19)` are the elementary second and fourth moments of a finite Rademacher sum, and `(21)`--`(23)` are a direct Cauchy--Schwarz argument equivalent in spirit to the classical second/fourth-moment anti-concentration method. No novelty is claimed for those facts.

The line-specific durable content is their composition with two already-audited exact structures: the reciprocal endpoint bias formula of `MC-296`/`MC-372` and the full-cube quadratic conductor concentration of `MC-375`. A targeted repository audit found the earlier total-energy statement `MC-301` and fixed-layer energy statement `MC-372`, but not the positive-density amplitude consequence `(6)` nor its intersection with the conductor-saturated population `(10)`.

The coding/Fourier moment literature already noted in `MC-375` is also adjacent: low moments of binary linear-code weights are classical. The present finding therefore makes no coding-theory novelty claim and does not require an additional source theorem.

## Boundaries and falsification tests

- **The reciprocal endpoint law is load-bearing.** The Rademacher representation `(15)` comes from the exact partition formula `(2)`. A generic family of shell characters need not have these moments.
- **The positive fraction is a full-cube statement.** It does not say that every fixed Hamming layer contains the same fraction of `R^{-1/2}`-biased modes.
- **Quartic source saturation is needed only for the conductor intersection.** Equations `(4)`--`(7)` hold for every positive defect partition with total mass one, independently of source conductors.
- **The conductor window in `(10)` is fixed-power.** `MC-375` gives convergence of the exponent for every fixed `\delta`; no shrinking `\delta(y)` is claimed without an additional rate hypothesis.
- **The `O(\log y)` rank cap is deliberately crude.** It uses only distinctness of source primes and `P\ge2^{|U|}`. Sharper primorial estimates can improve the logarithmic factor but are irrelevant to the qualitative analytic target.
- **Bias anti-concentration is not prime cancellation.** The `x_{\lambda_I}` are the hypothetical endpoint shell biases whose arithmetic realizability is under investigation. The result says what any realization must carry; it does not prove such characters exist independently of that realization problem.
- **No classical boundary theorem is claimed to rule out `(10)`.** Existing findings control fixed-subquadratic conductors or expose black-box large-sieve capacity limits. Whether prime-sensitive estimates can exclude the population in `(10)` at conductor `y^{2+o(1)}` is the remaining analytic question.
- **No Möbius or RH consequence follows.** The result sharpens the obstruction profile of the conditional endpoint construction only.

The decisive internal audit is finite. Recomputing the second and fourth moments from `(15)` must give `(17)` and `(19)`; if the fourth moment exceeds `3S_2^2`, `(6)` fails. Rechecking `MC-375` must give density-one conductor concentration before `(10)` is used. Finally, the source representatives must remain linearly independent in `\mathbf F_2^U` for `(11)`; otherwise the claimed endpoint rank `R` was not actually independent.