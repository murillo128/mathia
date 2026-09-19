# PL-369 — Completely multiplicative pole-neutral witnesses force zeta zero-free half-planes

**Evidence:** `VENTURINI-2020 + EXACT-DERIVED-HARDY-EXCLUSION + PRIOR-ART-REDIRECT`.

**Parent finding:** `PL-368`.

**Related findings:** `PL-021`, `PL-365`, `PL-366`, `PL-367`.

**Status:** `A-SOURCE-FORCED-COMPLETELY-MULTIPLICATIVE-FILTER-CLASS-DOES-COUPLE-ANALYTIC-CONTINUATION-TO-ZETA-ZERO-FREENESS-BUT-THIS-IS-CLASSICAL-PRIOR-ART-AND-THE-CRITICAL-WITNESS-CONSTRUCTION-IS-ITSELF-RH-EQUIVALENT`.

## Precise claim

`PL-368` leaves open a specific escape from the generic Hardy-space no-go: perhaps the relevant filter is not an arbitrary pole-neutral coefficient sequence but is forced by the arithmetic source to satisfy a nonlinear prime-lattice law.

There is classical prior art almost exactly of this form.

Let

\[
a:\mathbb N\to\mathbb C
\]

be bounded and completely multiplicative, and write

\[
L(a,s)=\sum_{n\ge1}\frac{a(n)}{n^s}.
\tag{PL369-1}
\]

Sergio Venturini proved in 2020 that, for every `sigma_0<1`,

\[
\boxed{
L(a,s)\text{ holomorphic on }\Re s>\sigma_0,
\qquad
L(a,1)=0
\Longrightarrow
\zeta(s)\neq0\text{ on }\Re s>\sigma_0.
}
\tag{PL369-2}
\]

For `1/2<=sigma_0<1` the converse also holds, using the Liouville function

\[
\lambda(n)=(-1)^{\Omega(n)},
\qquad
L(\lambda,s)=\frac{\zeta(2s)}{\zeta(s)}.
\tag{PL369-3}
\]

Hence

\[
\boxed{
\exists\,a\text{ bounded completely multiplicative satisfying (PL369-2)}
\iff
\zeta\text{ is zero-free on }\Re s>\sigma_0
}
\tag{PL369-4}
\]

for every `1/2<=sigma_0<1`. At `sigma_0=1/2`, existence of such a witness is therefore equivalent to RH.

In exponent-lattice coordinates complete multiplicativity is exactly the semigroup-character law

\[
\boxed{
a(n)=\prod_p a(p)^{v_p(n)},
\qquad
v(mn)=v(m)+v(n).
}
\tag{PL369-5}
\]

Thus Venturini's theorem supplies the kind of **source-forced filter class** that `PL-368` identified as missing from generic `H^p` geometry. But it simultaneously shows that constructing the critical witness is not a shortcut around RH: the witness problem is already equivalent to the desired zero-free half-plane.

## 1. The rigidity comes from complete multiplicativity, not from an ambient coefficient norm

Because `a` is bounded and completely multiplicative, necessarily

\[
|a(n)|\le1
\qquad(n\ge1).
\tag{PL369-6}
\]

All lattice coefficients are therefore determined by the prime-coordinate values `a(p)`. In contrast with the linear filters of `PL-365`--`PL-368`, one cannot freely choose the coefficient attached to a composite exponent vector once the axis values have been fixed.

For `Re(s)>1`, Venturini proves directly that

\[
L(a,s)
=
\exp\!\left(
\sum_{n\ge2}
\frac{a(n)\Lambda(n)}{n^s\log n}
\right).
\tag{PL369-7}
\]

This is equivalent to the familiar Euler-product logarithm but his proof only uses complete multiplicativity and the von Mangoldt identity. In exponent coordinates the support of the logarithm lies on the prime-power axes

\[
v(p^k)=k e_p,
\]

while the coefficient on the `k`-th point of the `p`-axis is `a(p)^k/k`.

The decisive step is not merely this factorization. It is the conjugate symmetrization

\[
F(s)
=
\zeta(s)^2L(a,s)\overline{L(a,\overline s)}.
\tag{PL369-8}
\]

Since `L(a,1)=0`, the two `L` factors cancel the double pole contributed by `zeta(s)^2` at `s=1`, so the assumed holomorphic continuation of `L` makes `F` holomorphic on `Re(s)>sigma_0`.

On `Re(s)>1`, however,

\[
F(s)=\exp f(s),
\tag{PL369-9}
\]

where

\[
f(s)
=
\sum_{n\ge2}
\frac{2\bigl(1+\Re a(n)\bigr)\Lambda(n)}{n^s\log n}.
\tag{PL369-10}
\]

The coefficients are nonnegative because `|a(n)|<=1`:

\[
2(1+\Re a(n))\frac{\Lambda(n)}{\log n}\ge0.
\tag{PL369-11}
\]

Venturini's nonvanishing principle says that if an exponential of such a completely monotone Dirichlet series extends holomorphically to a larger half-plane, then its logarithm extends there as well and the exponential cannot vanish. Applied to (PL369-8)--(PL369-11), it gives

\[
F(s)\neq0
\qquad(\Re s>\sigma_0).
\tag{PL369-12}
\]

A zeta zero in that half-plane would force `F` to vanish because both `L` factors are holomorphic there. This proves (PL369-2).

The mechanism is therefore precise:

\[
\boxed{
\text{prime-lattice semicharacter}
+\text{pole neutrality at }1
+\text{continuation}
+\text{positive logarithmic symmetrization}
\Longrightarrow
\text{zeta zero-freeness}.
}
\tag{PL369-13}
\]

This is genuinely stronger than the generic pole-neutral multiplication mechanism ruled out in `PL-368`.

## 2. The Liouville converse makes the witness problem equivalent to zero-freeness

Venturini already records the converse relevant to the critical strip. The Liouville function is bounded and completely multiplicative, and for `Re(s)>1`,

\[
L(\lambda,s)
=
\sum_{n\ge1}\frac{\lambda(n)}{n^s}
=
\frac{\zeta(2s)}{\zeta(s)}.
\tag{PL369-14}
\]

If `1/2<=sigma_0<1` and zeta is zero-free in `Re(s)>sigma_0`, the quotient on the right gives a holomorphic continuation of `L(lambda,s)` throughout that half-plane. The possible pole of `zeta(2s)` occurs only at `s=1/2`, which is on or to the left of the boundary. At `s=1`,

\[
L(\lambda,1)=0
\tag{PL369-15}
\]

because `zeta(s)` has a simple pole while `zeta(2)` is finite.

Thus the Liouville witness gives the reverse implication in (PL369-4). This is an important adversarial control: replacing a generic filter by complete multiplicativity does create real zero-sensitive rigidity, but the critical construction problem has not become easier. For the canonical available candidate, the required continuation is exactly what zero-freeness of zeta supplies.

In particular, (PL369-4) must not be presented as a proof strategy unless some **independent arithmetic mechanism** produces the continuation of a witness without already assuming or encoding the same zeta zero-free region.

## 3. A Venturini witness cannot live in the coefficient `H^2` geometry of the earlier no-go

There is a useful derived separation from `PL-368`.

Assume, for contradiction, that a completely multiplicative witness also satisfies

\[
(a(n))_{n\ge1}\in\ell^2.
\tag{PL369-16}
\]

Then Cauchy--Schwarz gives

\[
\sum_{n\ge1}\frac{|a(n)|}{n}
\le
\left(\sum_{n\ge1}|a(n)|^2\right)^{1/2}
\left(\sum_{n\ge1}\frac1{n^2}\right)^{1/2}
<\infty.
\tag{PL369-17}
\]

Hence `L(a,1)` is absolutely convergent. Complete multiplicativity then gives an absolutely convergent Euler product

\[
L(a,1)
=
\prod_p\left(1-\frac{a(p)}p\right)^{-1}.
\tag{PL369-18}
\]

Indeed `sum_p |a(p)|/p<infinity`, and every local factor is finite and nonzero because `|a(p)|<=1<p`. Therefore the product converges to a finite **nonzero** number:

\[
L(a,1)\neq0,
\tag{PL369-19}
\]

contradicting the witness condition.

Thus

\[
\boxed{
L(a,1)=0\text{ and complete multiplicativity}
\Longrightarrow
(a(n))\notin\ell^2.
}
\tag{PL369-20}
\]

Equivalently, the critical witness cannot be an element of the standard coefficient Hilbert space `mathcal H^2` used by the native Bohr transform. The same Hölder argument actually excludes every finite coefficient space `ell^p`, `1<=p<infinity`.

This explains why the Venturini mechanism escapes the `PL-366`--`PL-368` controls rather than contradicting them. In those findings pole neutrality is imposed inside an ambient coefficient/Hardy class where it is an ordinary linear constraint. Here complete multiplicativity makes an absolutely convergent zero at `s=1` impossible. The zero must arise only after conditional/global analytic continuation, exactly where the arithmetic difficulty lives.

## 4. What this changes after `PL-368`

`PL-368` concluded that a viable continuation mechanism must use extra structure not shared by generic pole-neutral Hardy data. Venturini supplies an established example of exactly that phenomenon:

- the filter coefficients obey the nonlinear lattice law (PL369-5);
- the logarithm is supported on the prime-power axis skeleton;
- conjugate symmetrization turns the local phases into the nonnegative weights `1+Re a(n)`;
- a zero at the pole location `s=1` converts this positivity into a zero-free theorem for zeta.

Accordingly, the route “look for a **source-forced multiplicative filter** whose continuation implies zero-freeness” is not killed by `PL-368`; it is classical and mathematically valid. What is killed is the idea that merely identifying such a class is progress toward RH. Venturini already reduces the problem to the hard step: constructing a member of that class with continuation to the desired half-plane and `L(a,1)=0`.

The most useful surviving question is narrower:

\[
\boxed{
\text{Can some arithmetic structure independent of zeta zero-freeness force the required continuation of a bounded completely multiplicative pole-neutral witness?}
}
\tag{PL369-21}
\]

A candidate answer must be audited against the Liouville converse: if its continuation proof merely rewrites `zeta(2s)/zeta(s)` or another quotient whose holomorphy already requires the target zero-free region, it is circular.

## 5. Literature / novelty audit

- **Sergio Venturini**, “Non vanishing of Dirichlet series of completely multiplicative functions,” *Rivista di Matematica della Università di Parma* **11**(1) (2020), 153--180. arXiv: https://arxiv.org/abs/2002.08903. Theorem 1.2 is exactly implication (PL369-2); the introduction explicitly states the Liouville converse (PL369-3)--(PL369-4); Lemma 4.1 gives (PL369-7), and the proof of Theorem 1.2 uses the positive symmetrization (PL369-8)--(PL369-12).
- Venturini explicitly states that he knew no example satisfying the theorem with `1/2<=sigma_0<1`, and observes that the `sigma_0=1/2` case would imply RH. His later sections extend the nonvanishing mechanism to generalized arithmetic semigroups and number-field ideal norms.
- Targeted searches through 19 September 2026 for the exact Venturini criterion, bounded completely multiplicative witnesses with `L(a,1)=0`, and later constructions in `1/2<=sigma_0<1` did not locate a subsequent accepted construction resolving this witness problem. The literature claim made here is therefore only that Venturini is direct prior art for the mechanism and that no resolution surfaced in the targeted audit, not that the bibliography is exhaustive.
- The `ell^2`/finite-`ell^p` exclusion in Section 3 is an elementary Mathia derivation used to connect Venturini's theorem to `PL-366`--`PL-368`; it is not attributed to Venturini and is not claimed as independent theorem-level novelty.

## Boundaries

This finding does **not** derive the critical line from prime-exponent geometry. Venturini's implication works for every half-plane `Re(s)>sigma_0` with `sigma_0<1`; the value `1/2` enters only when one asks for the zero-free half-plane equivalent to RH.

Complete multiplicativity is also not uniquely specific to the rational primes. Venturini develops analogous nonvanishing principles for generalized arithmetic semigroups and Dedekind-zeta settings. Therefore the positivity mechanism itself passes a strong algebraic source-consistency test but not a uniqueness test selecting the Riemann source or the exponent `1/2`.

Finally, (PL369-7)--(PL369-10) are used only in `Re(s)>1`, where their Dirichlet series converge absolutely. Passage into `Re(s)>sigma_0` comes from the assumed holomorphic continuation of `L` together with Venturini's analytic nonvanishing principle. No Euler product is formally continued into the critical strip.

The research redirect is therefore precise: generic coefficient-space filters remain closed by `PL-366`--`PL-368`, while the **nonlinear completely multiplicative + positive-logarithm** route is genuine prior art. Future passes should attack only an independent continuation mechanism for such a source-forced witness, or a stronger arithmetic constraint that narrows the class further; rediscovering the Venturini criterion or using Liouville's quotient as if it supplied the needed continuation is no progress.