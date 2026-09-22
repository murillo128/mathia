# MC-465 — Fejér-weighted favorable gcd classes remain sparse

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-464` counts the normalized shifts for which the fixed-anchor source-frame support gate can even be favorable, but leaves open whether the **actual outer shift weights** might concentrate enough mass on those sparse gcd classes to make the counting obstruction irrelevant. For the standard positive van-der-Corput/Fejér shift average, they do not.

Keep the `MC-463`--`MC-464` normalization

\[
r=g r_1,\qquad r'=g r_2,\qquad (r_1,r_2)=1,\qquad h=g h_0\ne0,
\tag{1}
\]

and define

\[
T(h_0):=\frac{r_2}{(h_0,r_2)}.
\tag{2}
\]

For a fixed-anchor residual support gate, `MC-464` shows that favorable shifts are exactly those with

\[
T(h_0)\le M,
\tag{3}
\]

where in that application

\[
M=\left\lceil\frac{SL}{p-L}\right\rceil-1
\tag{4}
\]

for source conductor `p`, residual support `S`, and translated-character interval length `0<L<p`.

Now use the ordinary Fejér bandwidth `Q>=1`. Its positive nonzero shift weights are

\[
W_Q(h)=(Q-h)_+,
\qquad 1\le h<Q.
\tag{5}
\]

Only shifts divisible by `g` are compatible with the outer pair. Put

\[
X:=\left\lfloor\frac{Q-1}{g}\right\rfloor.
\tag{6}
\]

The total Fejér mass on compatible positive nonzero shifts is

\[
D_Q(g)
:=\sum_{h_0=1}^{X}(Q-gh_0)
=XQ-\frac{gX(X+1)}2.
\tag{7}
\]

The favorable mass is

\[
F_Q(M;g,r_2)
:=\sum_{\substack{1\le h_0\le X\\T(h_0)\le M}}
(Q-gh_0).
\tag{8}
\]

For each divisor `T|r_2`, the class `T(h_0)=T` is parameterized exactly by

\[
h_0=\frac{r_2}{T}a,
\qquad (a,T)=1.
\tag{9}
\]

Therefore, with

\[
A_T:=\left\lfloor\frac{XT}{r_2}\right\rfloor,
\tag{10}
\]

we have the exact weighted class decomposition

\[
\boxed{
F_Q(M;g,r_2)
=
\sum_{\substack{T\mid r_2\\T\le M}}
\ \sum_{\substack{1\le a\le A_T\\(a,T)=1}}
\left(Q-\frac{g r_2}{T}a\right).
}
\tag{11}
\]

More importantly, if `X>=2`, then

\[
\boxed{
\frac{F_Q(M;g,r_2)}{D_Q(g)}
\le
\min\!\left(1,
2\frac{M(M+1)}{r_2}
\right).
}
\tag{12}
\]

The same ratio holds after including both positive and negative nonzero Fejér shifts, because the gate depends only on `(h_0,r_2)` and the standard kernel is symmetric.

Thus the totient/gcd sparsity from `MC-464` survives the **actual triangular Fejér weighting**. Uniformly over the common factor `g` and bandwidth `Q` once at least two compatible positive shifts are present,

\[
M=o(\sqrt{r_2})
\quad\Longrightarrow\quad
\frac{F_Q}{D_Q}=o(1).
\tag{13}
\]

In particular, the standard Fejér bias toward smaller shifts does not turn a sub-square-root family of favorable normalized gcd classes into a positive fraction of the off-diagonal shift mass. To obtain positive Fejér mass density one still needs, at exponent level,

\[
M\gtrsim \sqrt{r_2},
\tag{14}
\]

which in the `MC-464` support gate is the same square-root normalized-quotient threshold already visible from unweighted counting. Away from the source endpoint, for example `L<=(1-eta)p`, this keeps the necessary scale

\[
SL\gtrsim_\eta p\sqrt{r_2}
\tag{15}
\]

up to constants and integer-rounding effects.

This resolves the first weighted-support question left after `MC-464` for the **standard positive q-vdC/Fejér outer average**. It does not estimate coefficient participation inside the favorable classes, the residual amplitude, or the oscillatory staged kernel itself. It also does not rule out a deliberately redesigned non-Fejér shift architecture.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Exact propagation of the Fejér weight into gcd classes

The compatibility condition for the outer pair is `g|h`. Writing `h=gh_0`, the positive Fejér range `1<=h<Q` becomes exactly `1<=h_0<=X` with `X` from `(6)`. This gives `(7)` and `(8)`.

For any positive `h_0`, set `d=(h_0,r_2)`. Then `T=r_2/d` divides `r_2`, and writing `h_0=da=(r_2/T)a` forces `(a,T)=1`. Conversely every such coprime `a` produces `(h_0,r_2)=r_2/T`, so `(9)` is a bijective parameterization of the normalized-gcd class.

The range `h_0<=X` is equivalent to

\[
a\le \frac{XT}{r_2},
\tag{16}
\]

which gives `(10)`. Substituting `h=gh_0=g(r_2/T)a` into the Fejér weight proves `(11)`.

This is the weighted analogue of the exact totient-class decomposition in `MC-464`. No equidistribution or average-order theorem is used: the class formula is finite gcd arithmetic.

## 2. A uniform mass bound

Let

\[
N_X(M)
:=\#\{1\le h_0\le X:T(h_0)\le M\}.
\tag{17}
\]

From `(9)`--`(10)`, simply forgetting coprimality gives

\[
\begin{aligned}
N_X(M)
&\le
\sum_{\substack{T\mid r_2\\T\le M}}
\left\lfloor\frac{XT}{r_2}\right\rfloor\\
&\le
\frac{X}{r_2}
\sum_{T\le M}T\\
&=
\frac{X M(M+1)}{2r_2}.
\end{aligned}
\tag{18}
\]

Since every positive Fejér weight is at most `Q`, `(18)` gives

\[
F_Q(M;g,r_2)
\le
\frac{QX M(M+1)}{2r_2}.
\tag{19}
\]

For the denominator, `(7)` gives

\[
\frac{D_Q(g)}{XQ}
=1-\frac{g(X+1)}{2Q}.
\tag{20}
\]

Because `X=floor((Q-1)/g)`, we have `Q>gX`; hence for `X>=2`,

\[
\frac{D_Q(g)}{XQ}
>
1-\frac{X+1}{2X}
=
\frac{X-1}{2X}.
\tag{21}
\]

Combining `(19)` and `(21)`,

\[
\frac{F_Q}{D_Q}
<
\frac{X}{X-1}\frac{M(M+1)}{r_2}
\le
2\frac{M(M+1)}{r_2},
\tag{22}
\]

which proves `(12)` after adjoining the trivial upper bound `F_Q/D_Q<=1`.

The estimate is deliberately uniform in `g` and `Q`. The triangular kernel can overweight the earliest compatible shifts only by a bounded factor relative to its average compatible positive-shift mass once `X>=2`; the gcd-class count supplies the decisive `M^2/r_2` scale.

If `X=0`, there are no compatible positive shifts. If `X=1`, a single favorable shift can of course carry all the positive off-diagonal mass, so no density statement is possible. That tiny-band regime is a finite-support edge case rather than a contradiction to `(13)`.

## 3. Relation to the support gate

For the staged fixed-anchor family, `MC-464` gives `(4)`. If `L<=(1-eta)p`, then

\[
\frac{SL}{p-L}
\le \frac{SL}{\eta p},
\tag{23}
\]

so `M` is of the same exponent scale as `SL/p`. Hence the vanishing-mass regime `M=o(sqrt(r_2))` contains

\[
SL=o_\eta(p\sqrt{r_2}).
\tag{24}
\]

Conversely, obtaining a fixed positive fraction of the standard Fejér off-diagonal mass from favorable classes requires `M` at least on square-root scale by `(12)`, producing `(15)` at exponent level.

This should be read as a **necessary support/mass condition**, not an oscillatory estimate. A favorable shift merely has enough residual-divisor support to avoid the bare fixed-anchor impossibility; it may still contribute little after coefficient signs, residual amplitudes, character cancellation, or outer-factor summation are restored.

The zero shift is intentionally excluded throughout. At `h=0` there is no translated source-character phase, and `MC-415` identifies its exact positive cost as the re-squared lcm diagonal. Mixing that diagonal into the present favorable off-diagonal count would obscure rather than improve the staged support question.

## 4. What reweighting would have to change

The result closes the most immediate loophole in `MC-464`: **the standard q-vdC triangular weights do not preferentially rescue the favorable gcd classes at a new exponent scale**.

One can still try to choose a different filter or correlation architecture that deliberately concentrates on favorable shifts. That is a genuinely different obligation. `MC-416` shows that among finite filters whose squared sliding energy reconstructs the global sum, the ordinary constant window minimizes the normalized zero-shift burden. `MC-417` extends this through Fejér--Riesz to every scalar positive finite-band translation-invariant quadratic kernel: no such positive kernel has a smaller diagonal/DC ratio than the Fejér extremizer.

Those results do **not** by themselves prove a sharp concentration-versus-diagonal inequality for the particular arithmetic set `T(h_0)<=M`; therefore the present finding does not claim to close all positive reweightings. It says only that abandoning Fejér in order to target the favorable classes cannot be treated as a free modification: the new kernel must be analyzed together with its worsened or redistributed positive-energy cost, or must genuinely leave the scalar positive finite-band framework.

## 5. Prior art and novelty boundary

The triangular correlation weights and the van-der-Corput inequality are classical. A modern reference is N. Edeko, H. Kreidler and R. Nagel, *A dynamical proof of the van der Corput inequality*, Dynamical Systems **37** (2022), 1805--1825, DOI `10.1080/14689367.2022.2100244`, arXiv:`2106.11835`. The concrete finite Fejér identity used by this line was already derived in `MC-415`.

The factorization of a smooth modulus and repeated `A`-process/van-der-Corput steps belong to the classical `q`-analogue framework. A relevant modern source is A. J. Irving, *Estimates for character sums and Dirichlet L-functions to smooth moduli*, International Mathematics Research Notices 2016, arXiv:`1503.07156`, which uses q-analogue van der Corput differencing for character sums to smooth moduli.

The gcd/totient parameterization in `(9)` and the estimate `(18)` are elementary divisor arithmetic. A targeted literature search on 22 September 2026 found the standard Fejér/vdC and q-vdC ingredients, but no basis for claiming a separate named theorem for the exact normalized class `r_2/(h_0,r_2)<=M` with the staged source-frame interpretation here.

Accordingly, no novelty is claimed for the abstract ingredients or inequality in isolation. The durable Mathia contribution is the frontier specialization: the unweighted normalized-gcd sparsity from `MC-464` survives the exact standard outer weight used by the live positive q-vdC route, so the branch cannot evade its square-root quotient threshold merely through Fejér's preference for short shifts.

## Boundaries and falsification tests

- **Only the standard Fejér outer weights are classified here.** Arbitrary signed, nonstationary, modulus-dependent, or indefinite shift schemes require separate analysis.
- **The result concerns off-diagonal mass, not the full positive energy.** The zero-shift diagonal is separately classified by `MC-415`--`MC-417` and can dominate other budgets.
- **Favorable support is not favorable amplitude.** Equations `(11)`--`(12)` do not estimate the coefficient-weighted staged kernel on those classes.
- **No coprime-density heuristic is used.** Bound `(18)` is obtained by discarding the coprimality condition, so irregular divisor structure of `r_2` cannot invalidate it.
- **The `X>=2` condition is real.** A bandwidth containing only one compatible positive shift can place all of its off-diagonal mass on that shift. Any asymptotic use must ensure more than one compatible shift or handle this edge case separately.
- **The square-root threshold is necessary, not sufficient.** Even `M` on or above `sqrt(r_2)` does not prove a useful source estimate.
- **No RH-scale information is imported.** The proof is finite Fejér weighting plus exact gcd-class arithmetic.

## Consequence for the research line

The current staged route now has its first outer-weight question answered for the canonical positive differencing kernel. After fixing `(r,r')`, the standard Fejér average cannot hide the `MC-464` support sparsity: below the square-root normalized-quotient scale, favorable classes carry vanishing relative nonzero shift mass.

The next unresolved layer is therefore **inside** those favorable classes. The live calculation should restore the actual outer sieve coefficients and measure their participation in the classes `T(h_0)<=M`, then estimate the coupled residual amplitude/translated-character family before any absolute majorization destroys the staged structure. A genuinely arithmetic weighting that concentrates coefficient mass on the sparse favorable gcd classes would be new information; ordinary Fejér weighting is not such a mechanism.