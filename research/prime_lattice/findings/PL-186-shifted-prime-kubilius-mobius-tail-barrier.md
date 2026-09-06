# PL-186 — Shifted-prime small-coordinate exponent data is Kubilius-generic; the Möbius obstruction lives in the large-prime tail

## Claim

`PL-185` closes polylogarithmic congruence labels on the affine target `q+h`, while `PL-178` shows that the full Liouville/Möbius parity of a fixed shifted prime remains a classical hard frontier. Kevin Ford's shifted-prime Kubilius theorem sharpens the gap between those two facts directly in prime-exponent coordinates.

Fix a nonzero integer `h`. For a prime `q` chosen uniformly from `(|h|+1,X]`, write

\[
q+h=\prod_{\ell}\ell^{u_\ell},
\qquad U_{X,y}:=(u_\ell:\ell\le y).
\]

Ford constructs mutually independent random variables `W_ell` such that, for `ell|h`, `W_ell=0` almost surely, and for `ell\nmid h`,

\[
\Pr(W_\ell=0)=1-\frac1{\ell-1},
\qquad
\Pr(W_\ell=v)=\frac1{\ell^v}\quad(v\ge1).
\]

Unconditionally, for every fixed `0<alpha<1/2` and `A>0`, his Theorem 1 gives

\[
d_{TV}(U_{X,y},W_y)
\ll_{h,A,\alpha}
\exp(-\alpha u\log u)+(\log X)^{-A},
\qquad
u:=\frac{\log X}{\log y},
\]

for `2<=y<=X`; the required distribution hypothesis follows from Bombieri--Vinogradov. In particular, whenever `y=X^{o(1)}`, every bounded observable of the entire truncated exponent vector `(v_ell(q+h))_{ell<=y}` is asymptotically determined by the independent model.

For the canonical truncated Möbius parity

\[
\mu_{\le y}(n)
:=\prod_{\ell\le y}\eta(v_\ell(n)),
\qquad
\eta(0)=1,\quad \eta(1)=-1,\quad \eta(k)=0\ (k\ge2),
\]

this yields the explicit asymptotic

\[
\boxed{
\frac1{\pi(X)}\sum_{q\le X\atop q\ \mathrm{prime}}
\mu_{\le y}(q+h)
=
\prod_{\ell\le y\atop \ell\nmid h}
\left(1-\frac1{\ell-1}-\frac1\ell\right)+o(1)
}
\]

for any `y=y(X)->infinity` with `y=X^{o(1)}`. The product is

\[
O_h((\log y)^{-2}),
\]

indeed a nonzero `h`-dependent constant times `(log y)^(-2)` up to `1+o(1)`, so the truncated parity average tends to zero.

By contrast, the corresponding **full** statistic

\[
\frac1{\pi(X)}\sum_{q\le X}\mu(q+h)
\]

is the fixed-shift Möbius-on-shifted-primes conjecture isolated in `PL-178` and in Lichtman's peer-reviewed work; the strongest cited theorem there averages over the shift rather than settling a prescribed `h`. Therefore the first simple factorization target that escapes `PL-184`/`PL-185` does not hide in any subpower set of prime coordinates. The unresolved information is necessarily in the nonlocal exponent tail above every `X^{o(1)}` cutoff, or in a coupling involving that tail.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. Ford's total-variation theorem is literature. The transfer to arbitrary bounded exponent-cylinder observables, the displayed truncated-Möbius product, and its `(log y)^(-2)` decay are immediate exact consequences. No novelty is claimed for Kubilius models, shifted-prime factorization statistics, the fixed-shift Möbius conjecture, or Mertens' product estimate. The durable line-specific result is the location of the current affine/factorization escape: all subpower prime-coordinate data is already probabilistically classicalized, while the full parity problem remains in the large-coordinate tail.

## 1. Ford's theorem is already an exponent-vector theorem

The object in Ford's Theorem 1 is exactly a finite coordinate projection of the prime-exponent lattice. For the shifted target `q+h`,

\[
U_{X,y}=\bigl(v_\ell(q+h)\bigr)_{\ell\le y}.
\]

The independent model has the local law expected from primes in progressions. When `ell\nmid h`, the condition `ell^v||(q+h)` is a residue-class condition on the moving prime `q`, and the probabilities above are the corresponding prime densities. When `ell|h`, a prime `q>|h|+1` cannot also contribute that fixed divisor, so the local coordinate is frozen at zero.

Ford proves, under his smooth-modulus distribution hypothesis `Z(gamma)`,

\[
d_{TV}(W_y,U_{X,y})
\ll
\exp(-\alpha u\log u)+(\log X)^{-A}
\]

for every fixed `alpha<gamma`. He records that `Z(1/2)` follows from Bombieri--Vinogradov, and also cites stronger available exponents. Hence any fixed `alpha<1/2` gives the conclusion unconditionally.

If `y=X^{o(1)}`, then `u=log X/log y -> infinity`, so the total variation tends to zero. Consequently, for every possibly `X`-dependent function

\[
F_X:\mathbb N_0^{\{\ell\le y\}}\to\mathbb C,
\qquad |F_X|\le1,
\]

one has

\[
\left|
\mathbb E_{q\le X}F_X(U_{X,y})
-
\mathbb E F_X(W_y)
\right|
\le 2d_{TV}(U_{X,y},W_y)=o(1).
\]

Thus increasing combinatorial complexity inside a subpower block of prime coordinates is not, by itself, an escape. Total variation controls **all** bounded cylinder observables simultaneously, not just additive functions, residue labels, or low-variation functions.

## 2. Truncated Möbius already cancels in the independent model

Apply the preceding statement to

\[
F_X((a_\ell))=\prod_{\ell\le y}\eta(a_\ell).
\]

Because the `W_ell` are independent,

\[
\mathbb E F_X(W_y)
=
\prod_{\ell\le y}\mathbb E\eta(W_\ell).
\]

For `ell|h`, the factor is `1`. For `ell\nmid h`,

\[
\mathbb E\eta(W_\ell)
=
\Pr(W_\ell=0)-\Pr(W_\ell=1)
=
1-\frac1{\ell-1}-\frac1\ell.
\]

This proves the displayed product formula. For large `ell`,

\[
1-\frac1{\ell-1}-\frac1\ell
=1-\frac2\ell+O(\ell^{-2}).
\]

Therefore its ratio to `(1-1/ell)^2` is `1+O(ell^(-2))`. Removing the finitely many primes dividing fixed `h` only changes the constant, so Mertens' product theorem gives

\[
\prod_{\ell\le y\atop \ell\nmid h}
\left(1-\frac1{\ell-1}-\frac1\ell\right)
=C_h(\log y)^{-2}(1+o(1))
\]

with a finite nonzero signed constant `C_h`. Hence the small-coordinate squarefree parity already has vanishing mean.

This is stronger than the congruence scalarization in `PL-185` in one important sense. The observable may depend jointly on every valuation coordinate below `y`, where `y` can tend to infinity through any subpower scale. It is not reducible to one fixed modulus or a bounded-variation function of `q/X`. The classicalization instead comes from a genuine high-dimensional probabilistic model of the shifted target's factorization.

## 3. The full Möbius sign is precisely what the truncation does not see

The full Möbius value is not determined by `U_{X,y}`:

\[
\mu(q+h)
=
\mu_{\le y}(q+h)\times
\text{the squarefree/parity contribution of prime factors }\ell>y,
\]

with the understanding that a square factor in the tail annihilates the value. Even when `y=X^{o(1)}` tends to infinity very rapidly on a logarithmic scale, the remaining coordinates can include the largest prime factors of `q+h` and determine the final parity.

Ford explicitly marks this boundary: his small-coordinate vector is uniformly modeled for `y=X^{o(1)}`, while the distribution of the large prime factors of shifted primes is not well understood and the general transference principle must exclude statistics that depend strongly on the largest factors.

That is exactly where `PL-178` places the unresolved scalar. Lichtman states that

\[
\sum_{q\le X\atop q\ \mathrm{prime}}\mu(q+h)=o(\pi(X))
\]

for each fixed `h>0` is a folklore conjecture, and proves it on average over `h` in a growing range. The current literature audit found no peer-reviewed theorem settling the prescribed fixed-shift statement. Therefore one cannot pass from the truncated cancellation above to the full Möbius cancellation by an uncontrolled `y->X` limit.

The gap is not a cosmetic technicality. For every admissible subpower cutoff the finite-coordinate distribution is already close in total variation to an independent product law, yet the parity of the omitted factorization tail can still flip the full sign. This is a concrete exponent-lattice form of the classical parity barrier.

## 4. Consequence for the affine/Kronecker branch

The current frontier after `PL-184` and `PL-185` asks whether an arithmetic target attached to the affine destination `q+h` can survive the one-point Kronecker flattening. A natural next attempt is to replace a congruence label by factorization data such as `mu(q+h)`.

`PL-186` shows that this does escape the previous quotient, but only in a sharply delimited way. If the target factors through

\[
(v_\ell(q+h))_{\ell\le y},\qquad y=X^{o(1)},
\]

then Ford's theorem already sends it to an explicit independent-coordinate model. In particular, the canonical Möbius cylinder has zero limiting mean. To retain genuinely uncontrolled arithmetic, the target must depend on coordinates beyond every such cutoff, on the relation between those large coordinates and the source prime, or on a nonlocal/completed structure not measurable from the truncated vector alone.

The zero-frequency fiber of the full Möbius target also provides a hard audit test for any proposed phase theorem. If one defines

\[
M_{X,h}(t)
=
\frac1{\pi(X)}\sum_{q\le X\atop q\ \mathrm{prime}}
\mu(q+h)\exp\!\left(it\log\left(1+\frac hq\right)\right),
\]

then

\[
M_{X,h}(0)=\frac1{\pi(X)}\sum_{q\le X}\mu(q+h).
\]

Thus a uniform scalarization/cancellation theorem on any phase window containing `t=0` would in particular settle the fixed-shift shifted-prime Möbius conjecture. A high-frequency theorem on a window bounded away from zero is not ruled out by this observation, but it would require an independent exponential-sum mechanism and cannot be inferred from the small-coordinate Kubilius model.

## 5. Prior art and novelty audit

The primary new literature anchor is:

- **Kevin Ford**, “Poisson Approximation of Prime Divisors of Shifted Primes,” *International Mathematics Research Notices* **2025**(7) (2025), rnaf079, DOI `10.1093/imrn/rnaf079`; current arXiv version `2408.03803v4`. Theorem 1 gives the total-variation approximation of `(v_ell(p+a))_{ell<=y}` by independent variables with an explicit `exp(-alpha u log u)+(log x)^(-A)` error under `Z(gamma)`, and records the unconditional Bombieri--Vinogradov input. The paper explicitly distinguishes the controlled small-prime coordinates from the poorly understood large prime factors.

The fixed-shift boundary is already anchored by `PL-178`:

- **Jared Duker Lichtman**, “Averages of the Möbius Function on Shifted Primes,” *The Quarterly Journal of Mathematics* **73**(2) (2022), 729–757, DOI `10.1093/qmath/haab054`. The paper states the prescribed-shift Möbius cancellation as a folklore conjecture and proves cancellation after averaging over the shift.

A targeted novelty audit searched for later fixed-shift results and found recent work on the anatomy of shifted primes and Chowla-type statements on average, but no authoritative theorem upgrading the prescribed `sum_{p<=X} mu(p+h)` conjecture to a solved statement. Ford's 2025 theorem is especially important as a control because it shows how much of the exponent vector can be modeled without crossing that parity boundary.

No claim is made that the `(log y)^(-2)` product or the total-variation-to-bounded-observable implication is novel. They are elementary consequences of Ford's theorem. The research contribution here is a negative localization statement for this line: the live factorization-target escape cannot reside in any subpower cylinder of exponent coordinates.

## 6. Adversarial checks and failure modes

- **The cutoff must remain subpower.** Ford's error tends to zero in the stated use because `u=log X/log y -> infinity`. Nothing here controls a cutoff `y=X^theta` with fixed `theta>0`, much less the full vector.
- **Fixed shift is essential to the quoted theorem.** The result is stated for fixed nonzero `h`. A source prime `r=r(X)` giving `h=r-1` needs a uniform-in-shift theorem before the same conclusion can be asserted.
- **The phase is not included in Ford's total variation theorem.** The cylinder result is an unweighted target statement. The final `M_{X,h}(t)` observation only uses the exact `t=0` fiber; it does not claim weighted factorization cancellation for nonzero `t`.
- **Truncated cancellation does not approximate full Möbius in `L^1`.** The omitted large-prime coordinates can change the sign, and square factors in the tail can change a nonzero truncated value to zero. No dominated-convergence passage is available from the stated theorem.
- **No RH implication is supplied.** The fixed-shift Möbius conjecture is a hard parity statement but is not known here to be equivalent to RH or to a critical-line zero-free criterion. This finding redirects the affine branch; it does not promote shifted-prime parity into an RH mechanism.
- **Genericity is local-coordinate genericity only.** The independent model is a matched control for the truncated exponent vector. It does not show that rational primes and a generic multiplicative system have the same global factorization tail or completed zeta structure.

## Consequence

The next useful affine target should not merely be "more arithmetically complicated" inside a growing but subpower block of prime coordinates. That whole sigma-algebra is already controlled in total variation by Ford's shifted-prime Kubilius model. The genuinely live factorization branch begins at the **nonlocal tail**: large prime factors, full Möbius/Liouville parity, joint relations between several shifted targets, or a completed/source-relative coupling that cannot be read from `(v_ell(q+h))_{ell<=X^{o(1)}}`.

This sharpens the line's current falsification control: a candidate that is measurable from only subpower exponent coordinates should first be pushed through the independent `W_ell` model. If it survives there, its survival is not yet rational-prime-specific; if it dies there, only a tail or relational mechanism can rescue it.