# NB-209 — Existing large-value bounds miss the prime harmonic plateau by one logarithmic dimension

**Date:** 2026-09-18  
**Status:** `LITERATURE+DERIVED + SOURCE-ACQUISITION + POSITIVE-EULER + PRIME-HARMONIC + LARGE-VALUES + ADDITIVE-ENERGY + METHOD-BOUNDARY`.

`NB-208` reduces an `o(1/X)` positive Euler return to a phase-pinned plateau of prime Dirichlet-polynomial values at the arithmetic progression of heights `t,2t,...,Theta(X)t`. That exposes two apparently natural next tools: generic large-value estimates, and the stronger Heath-Brown difference-set estimate designed for large-value sets with additive structure.

At the scales forced by the actual prime shell, both published mechanisms remain quantitatively too coarse. The reason is simple but structural. A fixed multiplicative prime shell inside `[x,2x]` contains only

\[
M\asymp \frac{x}{X},\qquad X=\log x,
\]

active coefficients. Thus a phase-pinned value is near the prime maximum `M`, but from the viewpoint of a generic length-`x` Dirichlet polynomial it has size only `x/X`. The standard large-value baseline therefore permits about `(x/M)^2\asymp X^2` exceptional points, while `NB-208` guarantees only `Theta(X)` harmonics. Even after one uses the arithmetic-progression structure through Heath-Brown's difference-set theorem, its coefficient-blind `|W|N^2` term forces the same threshold: the progression must have length larger than `X^2` before that estimate can contradict a near-maximal prime plateau.

So the remaining gap after `NB-208` is not merely that current large-value exponents are imperfect. **The existing generic large-value currency pays for the ambient integer length rather than the prime support density, and that alone costs one full factor `X`.** A successful next theorem must recover prime sparsity, phase pinning, or equivalent source-specific information.

## 1. Prime sub-shell and plateau transfer

Keep the notation of `NB-208`:

\[
x=e^{r_0/a},\qquad X=\log x=\frac{r_0}{a},\qquad y=e^\Delta x,
\]

and let `\mathcal A_a(t)` be the normalized positive Euler return from that finding. Choose once and for all

\[
1<\kappa<\min\{e^\Delta,2\}.
\]

Define the fixed prime sub-shell

\[
\mathcal P_x:=\{p:x\le p<\kappa x\},
\qquad
M_x:=|\mathcal P_x|.
\tag{1}
\]

By the prime number theorem,

\[
\boxed{
M_x\asymp_\kappa \frac{x}{X}.
}
\tag{2}
\]

Put

\[
D_x(u):=\sum_{p\in\mathcal P_x}p^{-iu},
\qquad
U_x(u):=\frac{D_x(u)}{M_x}.
\tag{3}
\]

The proof of `NB-208` gives more than the full-shell statement. The prime real-part deficit is nonnegative term by term, and the sub-shell `[x,\kappa x)` carries a fixed positive proportion of the prime Euler mass. On this sub-shell the Euler weights `(\log p)p^{-1-a}` are uniformly comparable with `X/x`, while `M_x\asymp x/X`. Hence equations (5), (11), and (12) of `NB-208` imply

\[
\boxed{
1-\Re U_x(ht)
\ll_{r_0,\Delta,\kappa}
 h\,\mathcal A_a(t)
}
\tag{4}
\]

for every integer `h>=1` and all sufficiently small `a`.

Consequently, for any integer scale `H=H_a` satisfying

\[
H\,\mathcal A_a(t)\longrightarrow0,
\tag{5}
\]

we have

\[
\boxed{
\min_{1\le h\le H}|D_x(ht)|
=(1-o(1))M_x.
}
\tag{6}
\]

In particular, the `NB-208` hypothesis

\[
X\mathcal A_a(t)\to0
\tag{7}
\]

forces (6) for every fixed `H=cX`. More generally it allows `H/X\to\infty` if the extra factor is chosen sufficiently slowly, but (7) alone does **not** force `H\gg X^2`. For example, the admissible scale

\[
\mathcal A_a(t)=\frac1{X\log X}
\tag{8}
\]

still satisfies (7), whereas (5) then requires `H=o(X\log X)`.

This distinction is exactly where the large-value estimates below lose the target scale.

## 2. Guth--Maynard large-value counting already loses a factor `X`

Regard `D_x` as a Dirichlet polynomial of ambient length `N\asymp x`, by taking coefficients

\[
b_n=\mathbf 1_{\{n\in\mathcal P_x\}}
\]

inside `[N,2N]` and zero elsewhere. Its near-maximal plateau level is

\[
V=(1-o(1))M_x\asymp\frac{N}{X}.
\tag{9}
\]

Let

\[
W_H:=\{t,2t,\ldots,Ht\}.
\tag{10}
\]

For `|t|>=1`, this is a 1-separated set of `R=H` points contained in an interval of length `T_0\ll H|t|`. Under (5), every point of `W_H` satisfies `|D_x(u)|>=V`.

Guth--Maynard Theorem 1.1 gives, for a bounded-coefficient length-`N` Dirichlet polynomial,

\[
R
\le
T_0^{o(1)}
\left(
N^2V^{-2}
+N^{18/5}V^{-4}
+T_0N^{12/5}V^{-4}
\right).
\tag{11}
\]

At the prime-shell level (9), the first term alone is

\[
\boxed{
N^2V^{-2}\asymp X^2.
}
\tag{12}
\]

Therefore (11) is fully compatible with the `NB-208` plateau

\[
R\asymp X.
\tag{13}
\]

This conclusion is independent of the height `t`: the obstruction is already present in the `T_0`-independent first term. The classical Montgomery--Halász--Huxley large-value estimate quoted as equation (1.1) by Guth--Maynard has the same `N^2V^{-2}` baseline, so improving only the `T_0`-dependent exponent cannot repair the mismatch.

This also explains why the fact that our values are much closer to the absolute prime maximum than the `N^{3/4}` regime central to Guth--Maynard does not by itself help. In ambient-length units the ratio is

\[
\frac NV\asymp X,
\tag{14}
\]

and generic large-value counting naturally pays its square.

## 3. Additive energy sees the progression but still pays the ambient support

The set `W_H` is not a generic separated set: it is an exact arithmetic progression. Heath-Brown's difference-set theorem is therefore the natural stronger test. In the form restated as Theorem 1.6 by Guth--Maynard, for a 1-separated set `\mathcal T` of `R` points in an interval of length `T_0`,

\[
\sum_{u,v\in\mathcal T}
\left|
\sum_{N<n\le2N}a_n n^{i(u-v)}
\right|^2
\le
T_0^{o(1)}
\left(
R^2N+RN^2+R^{5/4}T_0^{1/2}N
\right)
\tag{15}
\]

for bounded coefficients at the scale relevant here.

Apply this with `a_n=1` on `\mathcal P_x` and zero otherwise. Because every difference of two points of `W_H` is `jt` with `|j|<=H`, equation (4) and complex conjugation imply that under (5)

\[
|D_x(u-v)|=(1-o(1))M_x
\]

uniformly for `u,v\in W_H`. Hence the left side of (15) has the lower bound

\[
\boxed{
(1-o(1))R^2M_x^2
\asymp
\frac{R^2N^2}{X^2}.
}
\tag{16}
\]

But the second term on the right side of (15) is

\[
RN^2.
\tag{17}
\]

Comparing (16) with (17), the generic theorem can only hope to contradict the plateau after

\[
\boxed{
R\gg X^2.
}
\tag{18}
\]

At the `NB-208` guaranteed length `R\asymp X`, the coefficient-blind term (17) exceeds the plateau lower bound by a factor `\asymp X`. Thus **even the classical difference-set theorem explicitly designed to exploit arithmetic progressions misses the required harmonic length by one factor `X`.** The other terms in (15) can only make the upper bound larger.

The additive-energy reformulation tells the same story in the range where Guth--Maynard Lemma 1.7 applies. Since `W_H` is an exact progression and `|t|>1`,

\[
E(W_H)
=
\#\{h_1+h_2=h_3+h_4:1\le h_j\le H\}
=
\frac{2H^3+H}{3}.
\tag{19}
\]

Writing `V=N^\sigma` formally, that lemma gives

\[
E(W_H)
\le
T_0^{o(1)}
\left(
H^3N^{1-2\sigma}
+H^2N^{2-2\sigma}
\right).
\tag{20}
\]

Since `V\asymp N/X`,

\[
N^{1-2\sigma}\asymp\frac{X^2}{N},
\qquad
N^{2-2\sigma}\asymp X^2,
\tag{21}
\]

so (20) becomes

\[
E(W_H)
\lesssim
T_0^{o(1)}
\left(
\frac{H^3X^2}{N}
+H^2X^2
\right).
\tag{22}
\]

Again the second term does not fall below the true energy `\asymp H^3` until `H` passes `X^2`, up to subpower losses. The energy language therefore does not remove the support-density tariff; it merely exposes it differently.

## 4. Why `o(1/X)` does not provide the missing `X^2` harmonics

It is tempting to answer (18) by using more harmonics. Equation (4) indeed says that a smaller return buys a longer plateau. But the exact currency is

\[
H\mathcal A_a(t)=o(1).
\tag{23}
\]

The target left by `NB-207` and `NB-208` is only

\[
\mathcal A_a(t)=o(1/X).
\tag{24}
\]

From (24) one can choose

\[
H=X L_a,
\qquad
L_a\to\infty,
\qquad
L_a X\mathcal A_a(t)\to0,
\tag{25}
\]

so the plateau is genuinely superlinear in `X`. But `L_a` may grow arbitrarily slowly. Nothing in (24) guarantees the quadratic scale `H\gg X^2` demanded by (18).

Equivalently, the Heath-Brown threshold would become naturally matched only after strengthening the hypothetical return to roughly

\[
\mathcal A_a(t)=o(1/X^2),
\tag{26}
\]

and even there the remaining terms and the `T_0^{o(1)}` factor still have to be checked. That is a different target from the `Omega(1/X)` obstruction sought after `NB-207`; using it would simply assume an extra logarithmic gain that the present program is trying to prove cannot occur.

So additive structure is real but insufficient at the current precision. The missing ingredient is not another slowly growing number of harmonics.

## 5. Representation audit: the gap is a sparse-support phenomenon

The mismatch can be expressed without primes. Suppose a length-`N` polynomial has `M=\delta N` active coefficients of comparable size and is observed near its support maximum `V\asymp M`. Then the generic large-value baseline is

\[
N^2V^{-2}
\asymp
\delta^{-2}.
\tag{27}
\]

A difference-set plateau of `R` such values has lower square-correlation mass `\asymp R^2M^2`, while the coefficient-blind `RN^2` term in (15) forces the same threshold

\[
R\gg \delta^{-2}.
\tag{28}
\]

For the prime shell,

\[
\delta\asymp\frac1X,
\tag{29}
\]

so (27)--(28) become `X^2`. The large-value mismatch is therefore **not itself prime-specific**; it is the generic cost of embedding a sparse support in the ambient integer interval.

What is prime-specific in this line is the conjunction of three facts: the source reduction of `NB-208` produces exactly the prime support, PNT fixes its density at `1/X`, and the positive Euler return supplies only the `o(1/X)` harmonic budget. Those facts place the Nyman source on the wrong side of the generic sparse-support threshold by precisely one logarithmic factor.

This audit also identifies what a useful refinement must change. Merely improving the exponent of a generic `T_0`-dependent large-value term leaves (12) untouched. Merely noticing that the sample set is an arithmetic progression leaves (17) untouched. A theorem capable of closing the `NB-208` route must instead exploit information that reduces the ambient-support tariff: for example the actual prime support / von-Mangoldt mass, the phase pinning at `+1`, or a source-specific estimate for correlations on the progression of differences.

## 6. Prior-art boundary and limitations

No new large-value theorem is claimed here. Guth--Maynard's 2026 paper, already anchored in `SOURCES.md`, is the load-bearing literature source for Theorem 1.1, its comparison with the classical Montgomery--Halász--Huxley bound, and its restatement of Heath-Brown's difference-set theorem and additive-energy consequence. Heath-Brown's underlying result is *A Large Values Estimate for Dirichlet Polynomials*, J. London Math. Soc. (2) 20 (1979), 8--18, DOI `10.1112/jlms/s2-20.1.8`.

The project-local delta is the scale audit obtained by inserting the exact `NB-208` prime plateau parameters

\[
V\asymp\frac NX,
\qquad
R\asymp X
\tag{30}
\]

into those results. It shows that both generic large-value counting and the standard additive-structure refinement retain an `X^2` support-density threshold and therefore cannot, as stated, prove the fixed-deficit harmonic criterion required by `NB-208`.

This is a method boundary, not an existence theorem. It does **not** show that the prime harmonic plateau exists, that no stronger large-value argument can rule it out, or that an appropriate sparse-coefficient refinement of Heath-Brown is impossible. On the contrary, the calculation isolates exactly why such a refinement could matter. It also does not change the positivity limitation or the destination bridge: signed/complex synthesis remains outside the argument, and a successful Nyman approximant has not yet been proved to force this positive Euler acquisition problem.

Within the positive source program, the next concrete target is therefore narrower than `NB-208`'s generic suggestion: **obtain a prime-density-aware difference-set or phase-pinned large-value inequality whose leading terms scale with the actual `M\asymp N/X` support rather than the ambient length `N`.** Any such gain must be strong enough to distinguish `R\asymp X` phase-pinned values from the generic `X^2` sparse-support allowance.
