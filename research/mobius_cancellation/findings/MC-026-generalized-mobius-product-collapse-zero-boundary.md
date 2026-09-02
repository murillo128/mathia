# MC-026 — Product-collapsed higher-degree Möbius blocks inherit the zeta zero boundary

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The signed higher-degree escape left open by `MC-025` cannot obtain a cheaper power exponent merely by collapsing a degree-`d` product of Möbius values to its product variable and then invoking cancellation of the resulting unrestricted convolution coefficient.

For an integer `d>=1`, let

\[
\mu_d:=\underbrace{\mu*\cdots*\mu}_{d\text{ Dirichlet convolutions}}
\tag{1}
\]

and define

\[
U_d(X)
:=\sum_{n_1\cdots n_d\le X}\mu(n_1)\cdots\mu(n_d)
=\sum_{q\le X}\mu_d(q).
\tag{2}
\]

In the half-plane of absolute convergence,

\[
\sum_{q\ge1}\frac{\mu_d(q)}{q^s}
=\frac1{\zeta(s)^d},
\qquad \Re(s)>1.
\tag{3}
\]

The critical cancellation exponent of `U_d` is **independent of the convolution degree**. More precisely, fix `0<=theta<1`. If

\[
U_d(X)=O_\varepsilon\!\left(X^{\theta+\varepsilon}\right)
\quad\text{for every }\varepsilon>0,
\tag{4}
\]

then

\[
\boxed{\zeta(s)\ne0\quad\text{for }\Re(s)>\theta.}
\tag{5}
\]

In particular,

\[
U_d(X)=O_\varepsilon(X^{1/2+\varepsilon})
\quad\Longrightarrow\quad \mathrm{RH}.
\tag{6}
\]

Thus increasing `d` changes the multiplicity with which a zeta zero appears in `1/zeta(s)^d`, but it does **not** move the zero-location boundary encoded by a power bound for the summatory coefficients. A purported higher-degree signed gain whose only retained datum after product grouping is `U_d` has therefore compressed the multilinear state to an observable whose critical estimate already carries the RH zero-free burden.

This does not kill the truncated Huxley–Watt multilinear identities. Their individual cutoff faces retain information that is destroyed by unrestricted product collapse. For equal cutoff `N`, define the truncated degree-`d` product coefficient

\[
c_{d,N}(q)
:=\sum_{\substack{n_1\cdots n_d=q\\ n_j\le N}}
\mu(n_1)\cdots\mu(n_d).
\tag{7}
\]

Then

\[
\boxed{c_{d,N}(q)=\mu_d(q)\qquad(q\le N),}
\tag{8}
\]

because every factor of a product `q<=N` is automatically at most `N`. Hence the defect

\[
e_{d,N}(q):=c_{d,N}(q)-\mu_d(q)
\tag{9}
\]

is supported entirely on the cutoff region `q>N`. For unequal Huxley–Watt ranges `N_1,...,N_d`, the same statement holds on the interior `q<=min_j N_j`.

Consequently, after `MC-025` rules out degree-only gain from generic product norms, the obvious alternative "keep the signs, group by the product, and exploit cancellation of the resulting generalized Möbius function" is also not a weaker bootstrap at the critical exponent. Any genuinely new signed gain must use information lost by that collapse: the individual factor cutoffs, their boundary geometry, auxiliary factor variables, cancellation between inclusion–exclusion degrees, or another coupling that cannot be expressed solely through the unrestricted coefficient `mu_d(q)`.

## 1. Product grouping gives the convolution power exactly

Dirichlet convolution is defined by

\[
(f*g)(q)=\sum_{ab=q}f(a)g(b).
\]

Iterating this identity gives

\[
\mu_d(q)
=\sum_{n_1\cdots n_d=q}
\mu(n_1)\cdots\mu(n_d),
\tag{10}
\]

where ordered factorizations are counted exactly as in the expansion of a product of Dirichlet series. Summing (10) over `q<=X` proves (2).

The Euler factor is equally explicit:

\[
\sum_{a\ge0}\frac{\mu_d(p^a)}{p^{as}}
=(1-p^{-s})^d,
\]

so

\[
\mu_d(p^a)=(-1)^a\binom da\quad(0\le a\le d),
\qquad
\mu_d(p^a)=0\quad(a>d).
\tag{11}
\]

Nothing in this product collapse creates a new arithmetic coefficient: it is the classical convolution power of Möbius, with Dirichlet series `zeta(s)^(-d)`.

For the Huxley–Watt higher-degree identities audited in `MC-025`, the Möbius variables are instead individually truncated. Equation (8) shows exactly where this differs from the unrestricted convolution. The low-product interior is already `mu_d`; all information arising solely from the separate upper faces `n_j<=N` lives in the boundary defect `e_{d,N}`. Replacing `c_{d,N}` globally by `mu_d` is therefore not an innocuous simplification: it deletes the only product-collapsed datum that distinguishes the finite Huxley–Watt block from the classical convolution power.

## 2. A power bound for the convolution sum forces the same zero-free half-plane

Assume (4). Let

\[
F_d(s)=\sum_{q\ge1}\frac{\mu_d(q)}{q^s}.
\tag{12}
\]

For any compact subset of `Re(s)>theta`, choose `epsilon>0` smaller than its distance from the boundary. Abel summation with (4) then gives locally uniform convergence of (12), so `F_d` is holomorphic throughout

\[
\Re(s)>\theta.
\tag{13}
\]

On `Re(s)>1`, absolute convergence and the convolution product give (3).

To continue the identity without treating `1/zeta^d` as already meromorphic through a hypothetical zero, set

\[
Z_0(s)=(s-1)\zeta(s).
\tag{14}
\]

This is holomorphic across `s=1`. On `Re(s)>1`, equation (3) gives

\[
Z_0(s)^d F_d(s)=(s-1)^d.
\tag{15}
\]

Both sides of (15) are holomorphic on the connected half-plane `Re(s)>theta`, so the identity theorem extends (15) throughout that half-plane. If `rho` were a nontrivial zeta zero with `Re(rho)>theta`, then `Z_0(rho)=0` while `(rho-1)^d` is nonzero, contradicting (15). This proves (5).

At `theta=1/2`, (5) excludes every nontrivial zero strictly to the right of the critical line. The functional equation and conjugation symmetry then exclude zeros strictly to the left, giving (6).

The key point for the active route is that `d` never enters the half-plane boundary. It appears only as a power in (15). Convolution degree can increase the order of the analytic singularity associated with a zero, but a summatory power estimate detects the **location** of that zero at exactly the same exponent for every fixed `d`.

## 3. Why this closes one signed higher-degree escape

`MC-025` proves that the raw degree-`d` Huxley–Watt error factorization is exponent-neutral under generic submultiplicative control: after accounting for the product of input scales, multiplying `d` small errors cannot outperform the best input exponent.

A natural response is to retain the signs rather than take product norms. The simplest such response is to group the Möbius variables by their product and seek cancellation in the grouped coefficient. Equations (2)–(6) show the exact limit of that move. For the unrestricted block, obtaining the critical exponent for the grouped signed coefficient already excludes zeta zeros beyond the critical line. The hoped-for new information has therefore not been made cheaper; the RH burden has been compressed into the summatory convolution power.

This is stronger than saying that `mu_d` is "related to zeta". The exact implication (4) -> (5) says that no fixed convolution degree changes the power-law zero boundary. Even if a higher-degree product empirically appears more oscillatory, a deterministic estimate at exponent `theta` carries the same zero-free half-plane `Re(s)>theta`.

The finite Huxley–Watt construction remains materially different precisely where (8) stops being true. A viable signed estimate may exploit, for example,

- cancellation in the boundary defect `e_{d,N}` produced by the individual cutoff faces;
- coupling between that defect and the auxiliary variables in the finite identity;
- cancellation between terms of different inclusion–exclusion degrees before product collapse;
- an anisotropic range structure whose signed estimate depends on the factorization coordinates, not only on `q=n_1...n_d`;
- or another arithmetic relation that gains a fixed power before the multilinear state is compressed to `mu_d`.

Any continuation that ultimately reduces its decisive bound to `sum_{q<=X} mu_d(q)` at the desired exponent has failed this test.

## 4. Prior art and novelty boundary

The convolution powers of Möbius and their Dirichlet-series identity with inverse powers of zeta are classical arithmetic-function machinery. Hung M. Bui and Alexandra Florea, *Negative moments of the Riemann zeta-function*, J. reine angew. Math. 806 (2024), 247–288, DOI `10.1515/crelle-2023-0091`, use generalized Möbius coefficients in their study of negative zeta moments and obtain conditional bounds for their averages. Debmalya Basak, Nicolas Robles and Alexandru Zaharescu, *Exponential sums over Möbius convolutions with applications to partitions*, Canad. J. Math. 78 (2026), 508–543, DOI `10.4153/S0008414X24000701`, study exponential sums twisted by generalized Möbius functions/convolutions and connect major-arc terms to zeta zeros. These works make clear that Möbius convolution powers are an established analytic-number-theory object rather than a new Mathia construction.

The parent finite identities are prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their general theorem contains products of up to `d` Möbius values with separate finite ranges; `MC-025` already audits the corresponding degree/scale product factorization.

Abel summation, holomorphy from a summatory-function bound, and the identity-theorem argument relating reciprocal-zeta Dirichlet series to zero-free half-planes are classical. No novelty is claimed for (1)–(6) individually. A targeted literature search located active work on generalized Möbius averages, exponential sums, and their zeta-zero explicit formulas, but no authoritative source was found presenting the specific finite-Huxley–Watt **pre-compression boundary audit** (8)–(9). Absence from that search is not evidence of novelty.

The durable line-specific result is therefore negative and structural: the unrestricted product-collapsed signed carrier has a degree-independent zero boundary, while the truncated finite block differs from it only beyond the interior cutoff. This identifies exactly where a higher-degree signed Huxley–Watt route must retain additional information if it is to be genuinely weaker than RH.

## 5. Consequence for the active frontier

The higher-degree branch is now narrowed by two complementary exact obstructions.

`MC-025` rules out gaining a power exponent merely from multiplying more separately controlled errors. The present finding rules out the simplest signed repair in which the factor variables are collapsed to the unrestricted convolution coefficient and its partial sum is then estimated at the target exponent.

The remaining opportunity is therefore **pre-compression signed coupling**. A future candidate must exhibit a fixed-power gain while the individual factor coordinates, truncation faces, or cross-degree cancellations are still visible. If the proof first forgets those coordinates and reduces to `mu_d(q)`, the critical bound already carries the same zeta zero-location problem for every `d`.

A decisive continuation would isolate one concrete boundary/cross-degree term from the Huxley–Watt finite formula and prove either a source-natural fixed-power saving for that term from independently weaker Möbius information, or a matched multiplicative control showing that even the retained boundary geometry does not force such a saving.