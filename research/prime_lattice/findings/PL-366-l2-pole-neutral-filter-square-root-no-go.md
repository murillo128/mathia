# PL-366 — Pole-neutral `ell^2` divisor filters automatically force square-root summatory cancellation, so Hilbert/multiplier regularity alone is not RH rigidity

**Evidence:** `EXACT-DERIVED + CLASSICAL-HLS-HARDY-CONTROL + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-365`.

**Status:** `THE-NEXT-HILBERT-CLASS-BEYOND-ELL1-DOES-REACH-THE-SQUARE-ROOT-SCALE-BUT-FOR-A-GENERIC-CAUCHY-SCHWARZ-REASON-THAT-DOES-NOT-LOCALIZE-ZETA-ZEROS`.

## Precise claim

`PL-365` closes the absolutely summable shift-filter class: `ell^1` coefficients eliminate arbitrary programmability but leave only limit-periodic outputs and an `O(1)` summatory remainder after cancelling the zeta pole. The next natural enlargement is the coefficient Hilbert class itself.

Let

\[
c=(c_d)_{d\ge1}\in\ell^2(\mathbb N),
\qquad
b=c*\mathbf 1,
\qquad
b_n=\sum_{d\mid n}c_d,
\tag{PL366-1}
\]

and put

\[
C(s)=\sum_{d\ge1}c_dd^{-s}.
\tag{PL366-2}
\]

Because `(1/d) in ell^2`, the pole-neutrality functional

\[
C(1)=\sum_{d\ge1}\frac{c_d}{d}
\tag{PL366-3}
\]

is absolutely defined for every `c in ell^2`. If

\[
\boxed{C(1)=0,}
\tag{PL366-4}
\]

then the filtered coefficient sum satisfies the unconditional Hilbert estimate

\[
\boxed{
S_b(x):=\sum_{n\le x}b_n
=O\!\left(\sqrt{x}\,\|c\|_2\right).
}
\tag{PL366-5}
\]

A convenient explicit bound is

\[
|S_b(x)|\le \sqrt{2x+1}\,\|c\|_2.
\tag{PL366-6}
\]

Consequently the ordinary Dirichlet series

\[
B(s)=\sum_{n\ge1}b_nn^{-s}
\tag{PL366-7}
\]

converges locally uniformly throughout

\[
\operatorname{Re}s>\frac12.
\tag{PL366-8}
\]

For `Re(s)>1`, where the Dirichlet product is absolutely justified,

\[
B(s)=\zeta(s)C(s).
\tag{PL366-9}
\]

Since `C in mathcal H^2` is holomorphic on `Re(s)>1/2` and (PL366-4) removes zeta's simple pole at `1`, the identity theorem extends (PL366-9) to the whole half-plane `Re(s)>1/2`, with zeta interpreted by its known meromorphic continuation.

Thus an apparently RH-shaped phenomenon — square-root summatory cancellation and ordinary convergence exactly to the right of `1/2` — is **automatic for every pole-neutral `ell^2` filter**, independently of the zeta zero divisor. The `1/2` enters from Cauchy-Schwarz / Hilbert-space regularity, not from a mechanism forcing `Re(rho)=1/2`.

This is a negative route classification, not a new theorem claim: `ell^2` or bounded-multiplier membership plus cancellation of the pole at `1` is too weak, by itself, to serve as RH evidence.

## 1. The square-root bound is a Hilbert norm identity

Finite rearrangement gives

\[
\begin{aligned}
S_b(x)
&=\sum_{n\le x}\sum_{d\mid n}c_d\\
&=\sum_{d\le x}c_d\left\lfloor\frac{x}{d}\right\rfloor.
\end{aligned}
\tag{PL366-10}
\]

Use (PL366-4) to subtract the cancelled main term over the **full** coefficient sequence:

\[
S_b(x)
=
\sum_{d\le x}c_d
\left(\left\lfloor\frac{x}{d}\right\rfloor-\frac{x}{d}\right)
-x\sum_{d>x}\frac{c_d}{d}.
\tag{PL366-11}
\]

Define the residual vector

\[
r_x(d)=
\begin{cases}
\left\lfloor x/d\right\rfloor-x/d,&d\le x,\\
-x/d,&d>x.
\end{cases}
\tag{PL366-12}
\]

Then simply

\[
S_b(x)=\langle c,\overline{r_x}\rangle_{\ell^2}.
\tag{PL366-13}
\]

Its norm is generically of square-root size:

\[
\begin{aligned}
\|r_x\|_2^2
&\le \sum_{d\le x}1
+x^2\sum_{d>x}\frac1{d^2}\\
&\le x+x^2\left(\frac1{x}+\frac1{x^2}\right)\\
&\le 2x+1.
\end{aligned}
\tag{PL366-14}
\]

Cauchy-Schwarz now gives (PL366-6). Equivalently, separating the two terms in (PL366-11) yields the same scale from

\[
\sum_{d\le x}|c_d|
\le \sqrt{x}\,\|c\|_2,
\qquad
x\left|\sum_{d>x}\frac{c_d}{d}\right|
\ll \sqrt{x}\,\|c\|_2.
\tag{PL366-15}
\]

Nothing about primes, Möbius signs, zeta zeros, the functional equation, or an Euler product enters this estimate. The square-root exponent is exactly the norm growth of the elementary floor-function residual in the dual of `ell^2`.

## 2. Why the critical half-plane appears without RH

For `sigma>1/2`, Cauchy-Schwarz gives

\[
\sum_{d\ge1}|c_d|d^{-\sigma}
\le
\|c\|_2
\left(\sum_{d\ge1}d^{-2\sigma}\right)^{1/2}
<\infty.
\tag{PL366-16}
\]

Hence `C(s)` is absolutely convergent and holomorphic on `Re(s)>1/2`. On the other side, (PL366-5) and Abel summation imply local uniform convergence of `B(s)` on the same open half-plane. One may write, for `Re(s)>1/2`,

\[
B(s)=s\int_1^\infty S_b(x)x^{-s-1}\,dx,
\tag{PL366-17}
\]

with the standard step-function interpretation.

The product identity requires a separate domain check. For `sigma>1`,

\[
\sum_{n\ge1}\frac{|b_n|}{n^\sigma}
\le
\zeta(\sigma)
\sum_{d\ge1}\frac{|c_d|}{d^\sigma}
<\infty,
\tag{PL366-18}
\]

so ordinary Dirichlet multiplication rigorously proves `B=\zeta C` only there. The left side then has the independently established holomorphic continuation supplied by its own convergent series on `Re(s)>1/2`. The right side is holomorphic there after removing the pole at `1` with `C(1)=0`. Identity theorem, not formal Euler-product continuation, yields

\[
\boxed{
B(s)=\zeta(s)C(s)
\quad (\operatorname{Re}s>1/2).
}
\tag{PL366-19}
\]

This distinction matters. Equation (PL366-19) does not imply that zeta is zero-free or that its zeros lie on the critical line. Any zeta zero in this half-plane would simply also be a zero of the filtered function `B`, unless cancelled by a singularity — and `C` has none there. The construction supplies no positivity or spectral principle that constrains such zeros.

## 3. The class is genuinely larger than the `ell^1` regime of `PL-365`

The estimate is not merely a restatement of the previous limit-periodic case. For example, let

\[
c_d=d^{-3/4}\quad(d\ge2),
\qquad
c_1=-\sum_{d\ge2}d^{-7/4}.
\tag{PL366-20}
\]

Then

\[
c\in\ell^2\setminus\ell^1,
\qquad
C(1)=0.
\tag{PL366-21}
\]

Thus (PL366-5) applies beyond the absolute-summability class. The `ell^1` proof of `PL-365` gave uniform approximation by periodic divisor filters and an `O(1)` remainder. Neither conclusion follows from `ell^2`; what survives is only the Hilbert-scale `O(sqrt(x))` estimate.

No sharpness claim is made. Particular coefficient sequences can have much stronger cancellation. The point is the opposite: **the square-root upper bound is already guaranteed by the ambient Hilbert class after one scalar pole-cancellation condition.** Therefore observing that scale in this filtered family cannot, without additional arithmetic structure, distinguish an RH mechanism from generic functional analysis.

## 4. Consequence for bounded multipliers

The standard Hardy Hilbert space of Dirichlet series is

\[
\mathcal H^2
=
\left\{
C(s)=\sum c_nn^{-s}:\sum|c_n|^2<\infty
\right\},
\tag{PL366-22}
\]

classically modeled by Hedenmalm-Lindqvist-Seip as Hardy `H^2` on the infinite polydisk / character space. In particular, if `M_C` is a bounded multiplication operator on `mathcal H^2`, then

\[
C=M_C1\in\mathcal H^2,
\tag{PL366-23}
\]

so its coefficient sequence automatically belongs to `ell^2`.

Therefore every bounded multiplier satisfying the single scalar condition `C(1)=0` falls under (PL366-5). This closes the most immediate suggestion left by `PL-365`: replacing `ell^1` operator-norm summability by the much larger bounded-multiplier/Hilbert setting can manufacture the square-root exponent, but that exponent is **generic Hilbert geometry**, not arithmetic rigidity.

This statement is deliberately one-way. Not every `ell^2` Dirichlet series is a bounded multiplier, and the finding does not classify the multiplier algebra. Nor does it rule out a specially source-forced multiplier carrying extra arithmetic identities. It only rules out using bounded-multiplier membership, `ell^2` energy, and pole cancellation themselves as the missing RH mechanism.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for the ambient Hardy-space facts. The basic square-summable Dirichlet-series Hilbert space, its infinite-polydisk/character-space model, and its multiplier theory are classical in **H. Hedenmalm, P. Lindqvist, K. Seip, “A Hilbert space of Dirichlet series and systems of dilated functions in `L^2(0,1)`,” Duke Math. J. 86 (1997), 1–37**, DOI https://doi.org/10.1215/S0012-7094-97-08601-4, already recorded as source 1 in `research/prime_lattice/SOURCES.md.

The surrounding multiplier literature continues to treat `mathcal H^2` and its Hardy relatives in exactly this classical Bohr/infinite-variable framework; a modern audit point is **T. Fernández Vidal, D. Galicer, P. Sevilla-Peris, “Multipliers for Hardy spaces of Dirichlet series,” Ann. Inst. Fourier 75 (2025), 541–577**, DOI https://doi.org/10.5802/aif.3658. The present finding does not depend on a new multiplier classification: (PL366-23) follows immediately by applying any multiplier to the constant vector.

A literature search over Hardy spaces of Dirichlet series, multiplier algebras, Dirichlet convolution, Wintner-type mean-value theorems, and square-summable arithmetic coefficients did not identify a source presenting (PL366-5) as an RH mechanism. The estimate itself is an elementary Cauchy-Schwarz consequence of (PL366-11) and should be regarded as standard-level analysis, not advertised as a new analytic-number-theory theorem.

The durable delta is instead the **route audit**. `PL-365` explicitly left a bounded-multiplier / weighted-`ell^2` class as the next plausible intermediate regime between `ell^1` and unrestricted programmable filters. The calculation above shows that its most tempting critical-looking signal — square-root cancellation at the `1/2` threshold — arises for a completely generic reason and therefore cannot by itself be the source of RH rigidity.

## 6. Adversarial boundaries

1. **Pole neutrality is an imposed linear condition.** `C(1)=0` is not derived from the prime lattice. Any future mechanism must explain why its source forces this condition rather than choosing it by hand.

2. **The bound does not prove convergence on the critical line.** `S_b(x)=O(sqrt(x))` yields ordinary convergence only for `Re(s)>1/2`. No boundary convergence at `Re(s)=1/2` is asserted.

3. **The abscissa need not equal `1/2`.** Some filters have stronger cancellation and a smaller convergence abscissa. The finding proves a universal upper bound on the abscissa for the pole-neutral class, not sharpness for each member.

4. **This is not a statement about Möbius itself.** The reciprocal-zeta coefficient sequence `mu(n)` is not in `ell^2`, since `sum mu(n)^2` diverges. Therefore the automatic Hilbert estimate does not prove the Mertens bound or RH.

5. **Zeros are inherited, not localized.** The continuation identity `B=\zeta C` on `Re(s)>1/2` carries hypothetical off-line zeta zeros into `B`; it gives no self-adjointness, positivity, determinant sign, or other mechanism forcing them onto `Re(s)=1/2`.

6. **Bounded-multiplier structure may still matter if additional identities are source-forced.** The no-go concerns the ambient class plus pole cancellation. It does not exclude a canonical multiplier satisfying extra multiplicative, functional-equation, positivity, or target-relative constraints that are independently forced by arithmetic.

7. **The coefficient-one zeta source remains outside `mathcal H^2`.** As in `PL-365`, `b=c*1` is a coefficientwise divisor-filter readout; it is not literally the action of a bounded Hilbert-space multiplier on the non-square-summable vector `Omega=sum e_n`.

## 7. Prime-lattice consequence

The `ell^1` / `ell^2` comparison now separates two very different kinds of regularity:

\[
\begin{array}{c|c|c}
\text{filter condition}&\text{automatic summatory control after }C(1)=0&\text{reason}\\
\hline
c\in\ell^1&O(1)&\text{absolute tail / limit-periodic control}\\
c\in\ell^2&O(\sqrt{x})&\text{Hilbert duality / Cauchy-Schwarz}
\end{array}
\tag{PL366-24}
\]

The second row is superficially much closer to the RH scale, but precisely for that reason it is a useful warning: **a critical exponent can be generated by the geometry of the chosen function space rather than by the arithmetic zero problem.**

Accordingly, the next viable filter route cannot merely ask for an intermediate Banach/Hilbert norm whose dual estimate happens to produce exponent `1/2`. It must add a source-forced constraint that couples the filter to genuinely global zeta data — for example the functional equation, a Weil-positive form, a target-relative Nyman/model-space condition, or another invariant that off-line zeros would violate. Otherwise the critical exponent is only a norm artifact.