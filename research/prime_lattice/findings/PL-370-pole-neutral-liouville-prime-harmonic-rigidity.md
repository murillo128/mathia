# PL-370 — Pole neutrality forces finite prime-harmonic distance from Liouville

**Evidence:** `VENTURINI-EULER-LOG + EXACT-DERIVED + PRIOR-ART-CALIBRATED-SOURCE-CLASS-NARROWING`.

**Parent finding:** `PL-369`.

**Related findings:** `PL-003`, `PL-021`, `PL-137`, `PL-369`.

**Status:** `A-BOUNDED-COMPLETELY-MULTIPLICATIVE-DIRICHLET-SERIES-THAT-EXTENDS-HOLOMORPHICALLY-ACROSS-s=1-AND-VANISHES-THERE-MUST-HAVE-A-SIMPLE-ZERO-AND-ITS-PRIME-AXIS-DATA-LIE-AT-FINITE-HARMONIC-DISTANCE-FROM-LIOUVILLE; THIS-NARROWS-THE-VENTURINI-WITNESS-CLASS-BUT-DOES-NOT-SUPPLY-THE-CRITICAL-CONTINUATION`.

## Precise claim

Let

\[
a:\mathbb N\to\mathbb C
\]

be bounded and completely multiplicative, and let

\[
L(a,s)=\sum_{n\ge1}\frac{a(n)}{n^s}.
\]

Assume only that `L(a,s)` has a holomorphic continuation to a neighbourhood of `s=1` and

\[
L(a,1)=0.
\tag{PL370-1}
\]

Then:

1. the zero at `s=1` is necessarily simple;
2. one has the exact boundary-energy identity

\[
\boxed{
\log |L'(a,1)|
=
\sum_p\sum_{k\ge1}
\frac{1+\Re(a(p)^k)}{k p^k}
<\infty;
}
\tag{PL370-2}
\]

3. consequently

\[
\boxed{
\sum_p\frac{1+\Re a(p)}p<\infty,
}
\tag{PL370-3}
\]

and hence

\[
\sum_p\frac{|1+a(p)|^2}{p}<\infty.
\tag{PL370-4}
\]

Because Liouville satisfies `lambda(p)=-1`, (PL370-3) is exactly finite prime-harmonic distance from the Liouville/parity character in the standard multiplicative-function metric:

\[
\mathbb D(a,\lambda;\infty)^2
=
\sum_p\frac{1-\Re(a(p)\overline{\lambda(p)})}{p}
=
\sum_p\frac{1+\Re a(p)}p
<\infty.
\tag{PL370-5}
\]

In exponent-lattice language, a pole-neutral Venturini witness cannot choose arbitrary prime-axis phases: it must approach the parity assignment

\[
e_p\longmapsto -1,
\qquad
v(n)\longmapsto (-1)^{\sum_p v_p(n)}
\]

in prime-harmonic square distance.

## 1. Positive Euler-log energy forces a simple boundary zero

Bounded complete multiplicativity implies `|a(p)|<=1` for every prime, because otherwise the sequence `a(p^k)` would be unbounded. For real `sigma>1`, absolute convergence gives the legitimate Euler logarithms

\[
\log L(a,\sigma)
=
\sum_p\sum_{k\ge1}\frac{a(p)^k}{k p^{k\sigma}},
\qquad
\log\zeta(\sigma)
=
\sum_p\sum_{k\ge1}\frac1{k p^{k\sigma}}.
\]

Therefore

\[
G(\sigma)
:=
\zeta(\sigma)^2|L(a,\sigma)|^2
=
\exp\!\left(
2\sum_p\sum_{k\ge1}
\frac{1+\Re(a(p)^k)}{k p^{k\sigma}}
\right).
\tag{PL370-6}
\]

Every coefficient in the exponent is nonnegative, since `|a(p)^k|<=1`. In particular,

\[
G(\sigma)\ge1
\qquad(\sigma>1).
\tag{PL370-7}
\]

Suppose the zero in (PL370-1) has order `m>=1`:

\[
L(a,s)=c(s-1)^m+O((s-1)^{m+1}),
\qquad c\ne0.
\]

Since zeta has a simple pole of residue one at `1`,

\[
G(\sigma)
\sim |c|^2(\sigma-1)^{2m-2}
\qquad(\sigma\downarrow1).
\tag{PL370-8}
\]

If `m>=2`, the right side tends to zero, contradicting (PL370-7). Thus

\[
\boxed{m=1.}
\tag{PL370-9}
\]

This is already a structural restriction absent from `PL-369`: local pole neutrality is not allowed to over-cancel the zeta pole.

## 2. Monotone passage to the boundary gives the exact energy identity

With the zero simple,

\[
\lim_{\sigma\downarrow1}G(\sigma)=|L'(a,1)|^2.
\tag{PL370-10}
\]

The exponent in (PL370-6) is a sum of nonnegative terms increasing monotonically as `sigma` decreases to `1`. Monotone convergence therefore gives

\[
2\log|L'(a,1)|
=
2\sum_p\sum_{k\ge1}
\frac{1+\Re(a(p)^k)}{k p^k},
\]

which is (PL370-2). In particular `|L'(a,1)|>=1`.

The contribution of the powers `k>=2` is always absolutely finite:

\[
0\le
\sum_p\sum_{k\ge2}
\frac{1+\Re(a(p)^k)}{k p^k}
\le
2\sum_p\sum_{k\ge2}\frac1{k p^k}<\infty.
\tag{PL370-11}
\]

Hence the entire boundary obstruction is concentrated at first order on the prime axes, and (PL370-3) follows.

Finally,

\[
|1+a(p)|^2
=1+|a(p)|^2+2\Re a(p)
\le 2(1+\Re a(p)),
\tag{PL370-12}
\]

so (PL370-4) follows as well. Thus for every fixed `epsilon>0`, the exceptional primes with `|a(p)+1|>=epsilon` have finite reciprocal-prime mass.

## 3. Independent check by normalizing against Liouville

The prime-harmonic conclusion can be recovered without the nonnegative prime-power sum, providing an independent check of the load-bearing step.

For Liouville,

\[
L(\lambda,s)=\frac{\zeta(2s)}{\zeta(s)}
\]

has a simple zero at `1` with derivative `zeta(2)`. By (PL370-9), the quotient

\[
R(s)=\frac{L(a,s)}{L(\lambda,s)}
\]

extends holomorphically and nonvanishingly near `s=1`, with

\[
R(1)=\frac{L'(a,1)}{\zeta(2)}\ne0.
\tag{PL370-13}
\]

For real `sigma>1`, Euler products give

\[
\log|R(\sigma)|
=
\sum_p
\left(
\log|1+p^{-\sigma}|-
\log|1-a(p)p^{-\sigma}|
\right).
\tag{PL370-14}
\]

Uniformly for `|a(p)|<=1`, the local term equals

\[
(1+\Re a(p))p^{-\sigma}+O(p^{-2\sigma}).
\tag{PL370-15}
\]

The total `O(p^{-2 sigma})` contribution remains bounded as `sigma` decreases to `1`, while `log|R(sigma)|` has a finite limit by (PL370-13). Because the first-order coefficients are nonnegative, monotone convergence again forces (PL370-3). This independently confirms that the Liouville distance is not an artifact of the particular symmetrization in (PL370-6).

## 4. Finite phase alphabets become almost rigid

Let the prime values `a(p)` belong to a fixed finite subset `S` of the closed unit disk. If `-1` is not in `S`, then

\[
\delta:=\min_{z\in S}(1+\Re z)>0.
\]

Equation (PL370-3) would imply

\[
\delta\sum_p\frac1p<\infty,
\]

contradicting Euler's divergence of the reciprocal-prime sum. Therefore no such finite alphabet can support a holomorphic zero at `s=1`.

If `-1` belongs to `S`, set

\[
\delta:=\min_{z\in S\setminus\{-1\}}(1+\Re z)>0.
\]

Then

\[
\boxed{
\sum_{\{p:a(p)\ne-1\}}\frac1p<\infty.
}
\tag{PL370-16}
\]

Thus an odd-order root-of-unity alphabet, including the cubic alphabet often used in Helson-zeta constructions, is excluded completely from the pole-neutral class. A `{+1,-1}`-valued witness must equal Liouville on all primes except a set of finite reciprocal-prime mass.

This does not imply uniqueness. For example, fix a finite set `P_0` of primes and define

\[
a(p)=0\quad(p\in P_0),
\qquad
a(p)=-1\quad(p\notin P_0).
\]

Then

\[
L(a,s)
=
\frac{\zeta(2s)}{\zeta(s)}
\prod_{p\in P_0}(1+p^{-s}),
\tag{PL370-17}
\]

so `s=1` is indeed a simple zero. This matched control shows that the correct conclusion is a harmonic neighbourhood of Liouville, not exact equality with it.

For the pure Liouville case, (PL370-2) gives

\[
\sum_p\sum_{k\ge1}
\frac{1+(-1)^k}{k p^k}
=
\log\zeta(2),
\]

and hence `|L'(lambda,1)|=zeta(2)`, exactly matching the derivative of `zeta(2s)/zeta(s)` at `1`.

## 5. Prior-art and novelty audit

The zero-sensitive half-plane implication remains Venturini's theorem, not a Mathia discovery: Sergio Venturini, “Non vanishing of Dirichlet series of completely multiplicative functions,” *Rivista di Matematica della Università di Parma* **11**(1) (2020), 153–180. Venturini's proof already contains the positive logarithmic symmetrization underlying (PL370-6), but the targeted audit did not locate the simple-zero conclusion, the exact derivative identity (PL370-2), or the finite Liouville-distance consequence (PL370-3) stated there. Those are recorded here only as elementary derived corollaries of that established mechanism, not as claimed theorem-level novelty in the literature.

Jean-Pierre Kahane and Éric Saïas, “Fonctions complètement multiplicatives de somme nulle,” *Expositiones Mathematicae* **35**(4) (2017), 364–389, arXiv:1507.04858, is close prior art for the boundary problem. Their `CMO` theory studies when `f(n)/n` has convergent sum zero and gives prime-value necessary/sufficient conditions in several regimes. In particular, under `|f(p)|<=1` and `Re f(p)<=0`, the CMO condition is equivalent to `sum_p Re f(p)/p=-infinity`. That is substantially weaker than (PL370-3): ordinary boundary convergence permits a broad class, whereas **holomorphic continuation through the boundary point with a zero there forces finite harmonic distance from Liouville**.

The Helson-zeta flexibility stored in `PL-003` is also an essential control. Andersson's 2024 Mittag-Leffler theorem permits prescribed divisors throughout `Re(s)<1` and extreme continuation flexibility for completely multiplicative unimodular coefficients. That flexibility does not contradict (PL370-3), because the new constraint is tied specifically to a holomorphic zero at the Euler-product boundary point `s=1`. The boundary condition is therefore genuine extra arithmetic information, not ambient prime-torus geometry.

Targeted searches through 19 September 2026 for the exact simple-zero/derivative identity and for the condition `sum_p(1+Re a(p))/p<infinity` under a holomorphic zero at `1` did not locate a direct published statement. This is a novelty audit, not an exhaustiveness claim.

## Boundaries and falsification controls

This finding does **not** prove any new zero-free region for zeta. It assumes only local continuation of `L(a,s)` through `s=1`; Venturini's RH-facing theorem still requires continuation of the witness throughout the target half-plane. Finite prime-harmonic distance from Liouville is necessary for pole neutrality, not sufficient for continuation to `Re(s)>1/2` or even for continuation across `1`.

For general complex-valued `a`, (PL370-3) controls only the real/chordal prime distance. It does not imply absolute convergence of `sum_p(1+a(p))/p`, nor does it justify analytic continuation of the Euler-product ratio by termwise boundary substitution. All Euler logarithms used above remain strictly inside `Re(s)>1`; passage to `s=1` uses the assumed holomorphic continuation and one-sided limits.

The result would be falsified by a bounded completely multiplicative `a` whose Dirichlet series is holomorphic near `1`, vanishes there, and for which either the zero has order greater than one or `sum_p(1+Re a(p))/p` diverges. Equations (PL370-6)–(PL370-11) rule out both possibilities directly.

## Consequence for the research line

`PL-369` left the live question as an independent continuation mechanism for an arbitrary bounded completely multiplicative pole-neutral witness. The admissible source class is now much narrower:

\[
\boxed{
L(a,1)=0\text{ holomorphically}
\Longrightarrow
\mathbb D(a,\lambda;\infty)<\infty.
}
\]

Future continuation mechanisms should therefore be tested first on **Liouville-like prime-axis perturbations**, not on generic Helson phases. In finite phase alphabets, every admissible candidate is Liouville outside a reciprocal-prime-summable exceptional set. This identifies pole neutrality at the Euler-product boundary as the first genuinely rigid selection step; the unsolved RH-facing step remains whether any independent arithmetic input can push such a Liouville-like witness holomorphically into the critical half-plane without already importing zeta zero-freeness.