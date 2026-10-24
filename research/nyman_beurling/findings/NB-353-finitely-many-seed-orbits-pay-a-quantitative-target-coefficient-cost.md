# NB-353 — Finitely many seed orbits pay a quantitative target coefficient cost

- **Status:** proved (author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-351 and NB-352; classical Mellin identity and simultaneous approximation
- **Classification:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + NORMED-TARGET-CERTIFICATE + CLASSICAL-INGREDIENTS

## Claim and scope

Allowing every dilation of a second seed is an infinite-dimensional extension, so NB-352's finite-patch theorem does not cover it. Nevertheless, finitely many additional seed types cannot repair the geometric target obstruction with bounded coefficient mass, regardless of the number or size of their dilations. There is a quantitative tradeoff in the actual Hilbert norm.

In \(H=L^2(0,1;dx)\), put
\[
e(x)=1,\qquad g_j(x)=\{1/(jx)\}-j^{-1}\{1/x\},\qquad
A_af(x)=\sqrt a\,f(ax)\mathbf1_{x\le1/a}.
\]
Fix an integer \(q\ge2\) and let
\[
\mathcal C_q=\overline{\operatorname{span}}
\{A_ag_{q^k}:a\ge1,\ k\ge1\}.
\]
Fix an integer \(d\ge1\). Consider any finite sum
\[
f=u+\sum_{\nu=1}^{L}c_\nu A_{a_\nu}g_{j_\nu},
\qquad u\in\mathcal C_q,\quad a_\nu\ge1,\quad j_\nu\in\mathbb N_{\ge2},
\tag{1}
\]
with complex coefficients \(c_\nu\), where the list \((j_\nu)\) uses at most \(d\) distinct seed indices. There is no bound on \(L\), the real dilation factors, the coefficients of \(u\), or \(\|u\|\). Define the declared coefficient cost of this representation by
\[
R(f;u,c,a,j)=\sum_{\nu=1}^{L}\frac{|c_\nu|}{j_\nu\sqrt{a_\nu}}.
\tag{2}
\]
This is a weighted absolute coefficient sum, not a Hilbert norm or a basis-independent measure of complexity.

There is a constant \(c_{q,d}>0\), independent of the chosen seed indices, such that every representation (1) of cost at most \(R\ge0\) satisfies
\[
\boxed{\|e-f\|_2\ge
\frac{c_{q,d}}{\big[(1+R)\log(e+R)\big]^d}.}
\tag{3}
\]
Here the \(e\) inside the logarithm is Euler's number. The same bound holds on the norm closure of the union of all such budget-constrained representations, even if their seed indices vary. It therefore also holds for the infimum of target error over that closed set.

In particular, for a geometric family with \(q=2\) augmented by arbitrarily many real dilations of \(g_3\), any approximating sequence with error \(\varepsilon\to0\) must satisfy
\[
(1+R)\log(e+R)\ge c_{2,1}/\varepsilon.
\tag{4}
\]
The theorem does not decide whether such an approximating sequence exists when its cost is unbounded. It gives neither a positive floor without a budget nor an upper approximation rate.

## 1. A bounded physical dual on the geometric zero lattice

Set
\[
\tau=\frac{2\pi}{\log q},\qquad s_\ell=1+i\tau\ell,
\qquad E_\ell(h)=s_\ell\int_0^1h(x)x^{s_\ell-1}\,dx
\quad(\ell\ge1).
\]
The integral is absolutely convergent for every \(h\in H\), and
\[
E_\ell(e)=1,\qquad \|E_\ell\|=|s_\ell|.
\tag{5}
\]
The norm is exactly the \(L^2(dx)\) norm of the integral kernel \(s_\ell x^{i\tau\ell}\). Thus \(E_\ell/|s_\ell|\) is a unit dual functional; its target response decreases with the evaluation height and must not be discarded.

The classical Mellin and dilation identities give
\[
E_\ell(A_ag_j)=
\frac{a^{-1/2-i\tau\ell}}{j}\,
\zeta(s_\ell)\big(1-e^{-2\pi i\ell\log j/\log q}\big).
\tag{6}
\]
For every \(j=q^k\), this vanishes. Continuity then yields
\(E_\ell(u)=0\) for every \(u\in\mathcal C_q\), including arbitrary norm limits with uncontrolled geometric coefficients. The point \(s=1\) is excluded: the zeta pole there cancels the elementary zero.

The dilation factor in (6) has modulus \(a^{-1/2}\). Consequently, once the seed phases nearly vanish, using more dilations or arranging their phases cannot overcome the triangle-inequality bound at fixed cost (2).

## 2. Returns with a controlled dual norm

List the distinct additional seed indices as \(J_1,\ldots,J_d\), repeating an index if fewer than \(d\) occur; the empty case is immediate. Put \(\alpha_r=\log J_r/\log q\). For every integer \(Q\ge2\), simultaneous Dirichlet approximation gives
\[
1\le\ell\le Q^d,\qquad
\max_{1\le r\le d}\|\ell\alpha_r\|_{\mathbb R/\mathbb Z}\le Q^{-1}.
\tag{7}
\]
To prove this, place the \(Q^d+1\) vectors with indices \(0,\ldots,Q^d\) in the \(Q^d\) equal boxes of the unit \(d\)-cube and subtract two lying in the same box. No rational independence or Diophantine lower bound is used. In particular,
\[
|1-e^{-2\pi i\ell\alpha_r}|\le2\pi/Q.
\tag{8}
\]

One explicit coarse zeta bound sufficient here is
\[
|\zeta(1+i\tau\ell)|\le C_q+\log\ell,
\quad
C_q=1+\log2+\log_+\tau+\tau^{-1}+\sqrt2,
\tag{9}
\]
where \(\log_+t=\max(0,\log t)\). Indeed, Euler summation for integer \(K\ge1\) gives
\[
\zeta(s)=\sum_{n\le K}n^{-s}+\frac{K^{1-s}}{s-1}
-s\int_K^\infty\{v\}v^{-s-1}\,dv.
\tag{10}
\]
At \(s=1+it\), take \(K=\lceil\max(1,t)\rceil\). The three terms have absolute values at most \(1+\log K\), \(1/t\), and \(\sqrt{1+t^2}/K\). Since \(t=\tau\ell\ge\tau\), these imply (9). This proof needs no information about zeta zeros.

For the index (7), equations (2), (6), (8), and (9) yield
\[
|E_\ell(f)|\le \frac{2\pi R(C_q+d\log Q)}{Q}.
\tag{11}
\]
Combining this with (5) proves the finite-parameter bound
\[
\boxed{\|e-f\|_2\ge
\frac{\big[1-2\pi R(C_q+d\log Q)/Q\big]_+}
{\sqrt{1+\tau^2Q^{2d}}}\qquad(Q\ge2).}
\tag{12}
\]
The positive part is \([x]_+=\max(x,0)\). The denominator prices the norm of the chosen evaluation; merely exhibiting small source responses at unbounded height would not give (12).

## 3. The budget-error law and its closure boundary

Choose a constant \(A\ge2\), depending only on \(q,d\), large enough that
\[
A\ge4\pi\big(C_q+d\log(2A)+2d\big).
\tag{13}
\]
Such a constant exists because the right side grows logarithmically in \(A\). Put
\[
F(R)=(1+R)\log(e+R),\qquad Q=\lceil A F(R)\rceil.
\]
Then \(Q\le2AF(R)\) and
\[
\log Q\le\log(2A)+2\log(e+R).
\]
Using \(\log(e+R)\ge1\), the subtracted term in the numerator of (12) is at most
\[
\frac{2\pi}{A}\big(C_q+d\log(2A)+2d\big)\le\frac12.
\]
Also \(\sqrt{1+\tau^2Q^{2d}}\le(1+\tau)Q^d\). Thus (3) holds with, for example,
\[
c_{q,d}=\frac{1}{2(1+\tau)(2A)^d}.
\tag{14}
\]
These constants are deliberately coarse. The exponent \(d\) counts additional seed types in the pigeonhole argument, not their possibly smaller multiplicative rank; no optimal exponent or logarithm is claimed.

For each fixed budget \(R\), the numerical lower bound (3) is uniform over every representation in the asserted union. The map \(f\mapsto\|e-f\|_2\) is norm-continuous, so the same inequality passes to its norm closure. A single common evaluation need not work for all seed choices: (7) can select a different bounded dual for each choice, while its norm bound remains uniform. No compactness of the coefficient parameter set is assumed.

An infinite series of dilated columns is covered if its partial sums converge in \(H\), use at most \(d\) seed types, and have uniformly bounded cost (2). Finite weighted cost alone is not asserted to imply convergence in \(H\): the isometry \(A_a\) preserves column norm even while the weight \(a^{-1/2}\) decreases. Conversely, taking a closure after allowing \(R\to\infty\) discards the positive bound. That latter closure remains outside this result.

## Controls and consequence for source compression

- The geometric component is entirely uncharged. The lower bound therefore constrains the added seed orbits even after arbitrary use of the original closed geometric space.
- The seed indices may change with the approximant. The only uniform restriction is their number; no constant in (3) depends on the indices themselves.
- Complex coefficients, dependent columns, repeated dilations, real dilation factors, and arbitrarily large numbers of columns are allowed. Integer-only dilation families are smaller and inherit the bound.
- Ordinary absolute coefficient budget \(S=\sum|c_\nu|\) implies \(R\le S/2\), hence also gives a positive bound via (3). A coefficient \(\ell^2\) bound alone does not control \(R\) when the number of columns grows.
- If all added indices are powers of \(q\), the exact common zeros remain and NB-351 gives a stronger budget-independent floor. If an added seed is multiplicatively independent, the present proof uses near returns rather than a fictitious exact common zero.
- No assertion about the full arithmetic generator family follows when the seed count grows. No RH-scale estimate, exclusion of zeta zeros, or closure equivalence is used or proved.

NB-352 separates a fixed finite patch even with unrestricted coefficients, by finite-dimensional elimination. Here the patch has arbitrarily many columns and may occupy whole dilation orbits. Its finite-dimensional elimination is unavailable, but bounded coefficient mass controls the approximate annihilator uniformly. The new consequence is a source-native conditioning requirement: at fixed seed count, convergence to the actual target forces the weighted absolute coefficients to diverge at least according to (3). This is a necessary cost for this compression scheme, not a constructive approximation mechanism.

## Prior art and evidence boundary

The Mellin identity, bounded evaluation duality, and dilation model are classical. They were checked against Bagchi, *On Nyman, Beurling and Baez-Duarte's Hilbert space reformulation of the Riemann hypothesis*, [Theorem 7 and its proof](https://arxiv.org/pdf/math/0607733), and Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [Section 2](https://arxiv.org/pdf/math/9910055). Dirichlet's simultaneous approximation is proved in the needed finite form in (7). The classical logarithmic zeta bound is recorded in Patel, *An explicit upper bound for* \(|\zeta(1+it)|\), Indag. Math. 33 (2022), 1012–1032, [introduction, equation (1)](https://arxiv.org/pdf/2009.00769); (9) independently supplies the coarse version used here.

Alouges, Darses, and Hillion, *Polynomial approximations in a generalized Nyman–Beurling criterion*, J. Théor. Nombres Bordeaux 34 (2022), 767–785, DOI `10.5802/jtnb.1227`, [Theorem 1.2](https://www.numdam.org/item/10.5802/jtnb.1227.pdf), separate approximation by randomized fractional-part functions from a coefficient-tail control. That is relevant prior art for treating coefficient control as a separate analytic obligation. Their theorem is not the finite-seed geometric-orbit estimate (12), and no implication for its probabilistic hypotheses is claimed here.

Locally, NB-127 already establishes simultaneous phase recurrence as a stability obstruction for finite-base zero data; NB-352 combines recurrence with logarithmic zeta growth for finite patch elimination. The present result reuses those classical ingredients and retains both the actual target response and evaluation norm to obtain a quantitative budget law for an infinite-dimensional orbit extension. Searches around restricted generators, finite seed dilations, coefficient constraints, and simultaneous approximation did not supply a theorem to replace this derivation. This is not a priority or general-method novelty claim.

The evidence is the analytic proof (5)–(14). No numerical experiment, Lean proof, or independent adversarial validation is asserted. The conclusion is falsified by an admissible representation violating (12); proposed escapes must change the seed-count or coefficient-budget hypothesis, or challenge the Mellin identity, recurrence height, or dual normalization.
