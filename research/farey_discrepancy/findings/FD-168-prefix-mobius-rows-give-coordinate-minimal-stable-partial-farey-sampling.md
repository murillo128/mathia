# FD-168 — Prefix Möbius rows give coordinate-minimal stable partial Farey sampling

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** partial Fourier observation / exact coordinate minimality / stable prefix recovery
- **Depends on:** FD-117, FD-118, FD-167
- **Classification:** `EXACT-DERIVED + PARTIAL-FOURIER-OBSERVATION + COORDINATE-MINIMALITY + PREFIX-STABILITY`

## Claim

The complete-field hypothesis in `FD-167` can be weakened sharply when the goal is only to recover a growing initial source prefix. The required positive Fourier frequencies are exactly the nonzero supports of the relevant divisor-Möbius inverse rows, and no smaller subset of the `FD-118` skeleton coordinates can recover the same formal prefix from raw Fourier-coordinate observations.

Fix `H>=2` and

\[
1\le R\le \lfloor\sqrt H\rfloor.
\tag{1}
\]

Let

\[
\mathcal Q_H
=\left\{\left\lfloor\frac Hm\right\rfloor:1\le m\le H\right\},
\qquad
\tau_H(k)=\left\lfloor\frac Hk\right\rfloor,
\tag{2}
\]

and for each target prefix coordinate `1<=r<=R` put

\[
k_r:=\tau_H(r).
\tag{3}
\]

Because `r\in\mathcal Q_H` throughout the square-root prefix and `\tau_H` is an involution on `\mathcal Q_H`, one has `k_r\in\mathcal Q_H` and `\tau_H(k_r)=r`.

Define the sampled frequency set

\[
\boxed{
\mathcal S_{H,R}
:=
\bigcup_{1\le r\le R}
\left\{
 d\mid k_r:
 \mu(k_r/d)\ne0
\right\}.
}
\tag{4}
\]

`FD-118` implies every divisor appearing in (4) is again in `\mathcal Q_H`. If

\[
Y_H(d):=1+2\pi i d\,\widehat{\mathcal D_H}(d),
\qquad d\in\mathcal Q_H,
\tag{5}
\]

then the physical cumulative source prefix is recovered from only these sampled modes:

\[
\boxed{
M(r)
=
\frac1{k_r}
\sum_{\substack{d\mid k_r\\\mu(k_r/d)\ne0}}
\mu(k_r/d)Y_H(d),
\qquad 1\le r\le R.
}
\tag{6}
\]

Moreover, `\mathcal S_{H,R}` is the **unique coordinate-minimal sampling set** inside the positive `FD-118` skeleton for exact recovery of all `M(1),...,M(R)` when the quotient-source vector is allowed to range over the full formal real source space. Every frequency in (4) is necessary; frequencies outside (4) are unnecessary.

The same support gives uniform stability. Let `a:\mathbb N\to\mathbb R`, `A(x)=\sum_{n\le x}a(n)`, let `\mathcal D_{H,A}` be the real source-controlled field from `FD-117`, and put

\[
E_H:=\mathcal D_{H,A}-\mathcal D_H.
\tag{7}
\]

Let `\Pi_{H,R}` denote Fourier projection onto the signed frequencies `\pm\mathcal S_{H,R}`. Then

\[
\|\Pi_{H,R}E_H\|_2^2
=
2\sum_{d\in\mathcal S_{H,R}}|\widehat E_H(d)|^2
\tag{8}
\]

and

\[
\boxed{
\max_{1\le r\le R}|A(r)-M(r)|
\le
\sqrt{30}\,\|\Pi_{H,R}E_H\|_2.
}
\tag{9}
\]

Thus modes outside `\mathcal S_{H,R}` are not merely algebraically redundant for this prefix: their error energy is irrelevant to its `FD-167` conditioning bound.

If `a` is integer-valued, then

\[
\boxed{
\|\Pi_{H,R}E_H\|_2<\frac1{\sqrt{30}}
\quad\Longrightarrow\quad
A(r)=M(r),\quad a(r)=\mu(r)
\quad(1\le r\le R).
}
\tag{10}
\]

Finally, the exact sampler is sparse for genuinely sub-square-root prefixes. Since the row for `k` has exactly `2^{\omega(k)}` nonzero Möbius coefficients,

\[
R
\le
|\mathcal S_{H,R}|
\le
\sum_{r\le R}2^{\omega(k_r)}
\le
R\exp\!\left(O\!\left(\frac{\log H}{\log\log H}\right)\right)
=
R H^{o(1)}.
\tag{11}
\]

Hence for every fixed `\delta>0`,

\[
R\le H^{1/2-\delta}
\quad\Longrightarrow\quad
|\mathcal S_{H,R}|\le H^{1/2-\delta+o(1)}=o(\sqrt H),
\tag{12}
\]

whereas the complete `FD-118` skeleton has `2\sqrt H+O(1)` coordinates. A vanishing fraction of that skeleton therefore stably recovers a polynomially growing source prefix.

## 1. Prefix targets select explicit inverse-row supports

`FD-118` writes the skeleton transform as a square invertible linear map. In its scalar form, for every `k\in\mathcal Q_H`,

\[
M(\tau_H(k))
=
\frac1k
\sum_{d\mid k}
\mu(k/d)Y_H(d).
\tag{13}
\]

For `r<=R<=sqrt(H)`, choose `k=k_r=\tau_H(r)`. The involution property gives `\tau_H(k_r)=r`, so (13) becomes (6). Terms with squareful quotient `k_r/d` vanish identically and need not be observed. This is why the correct partial sampler is the support in (4), not the whole divisor closure of the target frequencies.

The number of nonzero coordinates in one row is exact. Writing `e=k_r/d`, nonzero terms correspond bijectively to squarefree divisors `e` of `k_r`; there are `2^{\omega(k_r)}` of them.

## 2. Coordinate minimality is exact, even against nonlinear reconstruction

Let the formal quotient-source vector be

\[
m=(m_q)_{q\in\mathcal Q_H}\in\mathbb R^{\mathcal Q_H}.
\tag{14}
\]

As proved in `FD-118`, the map from `m` to the normalized skeleton coordinates

\[
Y=(Y_H(d))_{d\in\mathcal Q_H}
\tag{15}
\]

is a linear bijection. Consequently `Y` ranges over all of `\mathbb R^{\mathcal Q_H}` when the formal source ranges over all of its allowed values.

For a fixed target `r`, equation (13) is therefore not just one possible reconstruction formula. It is the unique linear functional of the full coordinate vector `Y` equal to `m_r` for every formal source. Its coefficient at frequency `d` is

\[
\frac1{k_r}\mu(k_r/d)
\tag{16}
\]

when `d\mid k_r`, and zero otherwise.

Suppose a coordinate subset `S\subseteq\mathcal Q_H` allowed exact recovery of `m_r` for every formal source, even by an arbitrary nonlinear rule using only `Y|_S`. If some `d_0` with nonzero coefficient (16) were omitted from `S`, two vectors `Y,Y'` could agree on every sampled coordinate and differ only at `d_0`. Because the skeleton map is onto, both are realized by formal sources, while (13) gives different values of `m_r`. This is impossible.

Thus every nonzero inverse-row coordinate is necessary. Taking the union over `1<=r<=R` proves that (4) is the exact coordinate-minimal set for the whole prefix. Conversely (6) proves sufficiency. The lower bound `|\mathcal S_{H,R}|>=R` also follows directly because every distinct target frequency `k_r` belongs to its own row support through the term `d=k_r`, where `\mu(1)=1`.

The minimality statement is deliberately scoped to **raw coordinate selection from the `FD-118` Fourier skeleton and arbitrary formal quotient sources**. It does not forbid fewer custom linear measurements, nonlinear measurements that mix frequencies before observation, or compression that exploits additional arithmetic restrictions on the one physical Mertens vector.

## 3. The full-field conditioning proof localizes to the same rows

Subtract the source-controlled and physical versions of (13). For `k=k_r`, exactly as in `FD-167`,

\[
A(r)-M(r)
=
\frac{2\pi i}{k_r}
\sum_{\substack{d\mid k_r\\\mu(k_r/d)\ne0}}
\mu(k_r/d)d\,\widehat E_H(d).
\tag{17}
\]

Cauchy--Schwarz gives

\[
|A(r)-M(r)|
\le
2\pi
\left(
\sum_{e\mid k_r}\frac{\mu(e)^2}{e^2}
\right)^{1/2}
\left(
\sum_{\substack{d\mid k_r\\\mu(k_r/d)\ne0}}
|\widehat E_H(d)|^2
\right)^{1/2}.
\tag{18}
\]

The first factor is bounded by

\[
\sum_{e\ge1}\frac{\mu(e)^2}{e^2}
=
\frac{\zeta(2)}{\zeta(4)}
=
\frac{15}{\pi^2},
\tag{19}
\]

while the second sum is contained in `\mathcal S_{H,R}`. Using (8) therefore gives

\[
|A(r)-M(r)|
\le
\sqrt{30}\,\|\Pi_{H,R}E_H\|_2,
\tag{20}
\]

uniformly in `H`, `R` and `r`. Taking the maximum proves (9).

If `a` is integer-valued, every cumulative difference `A(r)-M(r)` is integral. The strict inequality in (10) makes all of them have absolute value below one, so they vanish; consecutive differencing then yields `a(r)=\mu(r)` throughout the recovered prefix.

Notice the logical strengthening relative to `FD-167`: Parseval over the unobserved Fourier tail is no longer used. The inverse row itself certifies that the tail cannot affect the chosen source coordinates.

## 4. A growing prefix needs only a vanishing fraction of the full skeleton

For `n<=H` with `w=\omega(n)`, the product of its distinct prime factors is at least the product of the first `w` primes, and the `j`-th prime is at least `j+1`. Hence

\[
H\ge n\ge (w+1)!.
\tag{21}
\]

Stirling's elementary lower bound then gives

\[
w=O\!\left(\frac{\log H}{\log\log H}\right),
\tag{22}
\]

uniformly for `n<=H`. Therefore

\[
2^{\omega(n)}
\le
\exp\!\left(O\!\left(\frac{\log H}{\log\log H}\right)\right)
=H^{o(1)},
\tag{23}
\]

which proves the upper bounds in (11)--(12).

This gives a robust permanent-source corollary. Fix `0<\delta<1/2` and take

\[
R_H=\lfloor H^{1/2-\delta}\rfloor.
\tag{24}
\]

Then `|\mathcal S_{H,R_H}|=o(\sqrt H)`. Nevertheless, if a fixed integer-valued source has first defect `n_0`, then for all sufficiently large `H` one has `n_0<=R_H`, and (10) forces

\[
\|\Pi_{H,R_H}E_H\|_2\ge\frac1{\sqrt{30}}.
\tag{25}
\]

Thus every fixed defect is eventually detected by a vanishing fraction of the complete minimal Fourier skeleton. The freedom exhibited by the finite-cutoff controls in `FD-164`--`FD-165` must again move outward with the horizon; it cannot remain hidden merely in Fourier coordinates outside a fixed polynomially growing prefix sampler.

## 5. Representation transplant, hostile audit, and boundary

The inverse-row support statement is generic incidence algebra. For any finite invertible zeta transform, a target coordinate is determined by the support of the corresponding Möbius-inverse row, and that support is coordinate-minimal when the transformed coordinates are allowed to vary freely. The `L^2` estimate is likewise a Cauchy--Schwarz bound on those row coefficients. No novelty is claimed for these generic facts.

The Farey-specific content is the dictionary established by `FD-117`--`FD-118`: the positive discrepancy Fourier coordinates on `\mathcal Q_H` are exactly a divisor-zeta transform of the quotient-Mertens source, `\tau_H` maps the consecutive square-root prefix to explicit skeleton rows, and the arithmetic Möbius function makes the row support equal to squarefree quotient divisors. That splice yields the exact sampler (4), its formal coordinate minimality, and the sparse stable detection statement (25).

The result does **not** solve sampled spatial observation. A set of point values `\mathcal D_H(x_j)` is not the same as direct access to selected Fourier modes, and recovering those modes from few spatial samples may be ill-conditioned or impossible without additional structure. It also gives no new Franel--Landau estimate: stable recovery of a source prefix remains a coefficient-identification statement, not destination coercivity at the RH-critical scale.

The `R<=sqrt(H)` restriction is structural to the consecutive-prefix formulation. For larger quotient coordinates the same inverse-row formula remains valid whenever the target lies in `\mathcal Q_H`, but there is no longer a consecutive interval of all integer source indices. When `R` approaches `sqrt(H)`, the bound (11) need not beat the full `2\sqrt H+O(1)` skeleton; the theorem claims sparsity only in regimes where the stated cardinality estimate is genuinely sub-root.

The formal coordinate-minimality claim must also not be promoted to an information-theoretic lower bound for the physical Mertens trajectory. It excludes dropping a nonzero inverse-row coordinate while demanding exact recovery for every formal source; it does not exclude a source-specific theorem that compresses the unique arithmetic trajectory more strongly.

## Prior-art check

A fresh search across floor-quotient orders, general poset zeta/Möbius inversion, and sparse Möbius-transform query models found the expected generic inversion and sparse-query machinery but no load-bearing theorem for the Farey-specific statement above. `FD-118` already records the relevant floor-quotient and Mertens-matrix prior-art boundary. Equations (4), (9) and the minimality argument are direct finite consequences of the internal `FD-117`--`FD-118` transform plus the `FD-167` conditioning calculation, so no new external source anchor is required in `SOURCES.md`.

## Research consequence

The partial-observation frontier is now split more sharply. **Sparse Fourier observation itself is not the bottleneck for recovering a genuinely sub-square-root source prefix:** there is an explicit coordinate-minimal sampler of size `R H^{o(1)}` with the same universal conditioning constant as the complete field. The remaining observation questions are spatial sampling/coarsening, recovery near the full square-root frontier, and source-specific compression beyond formal-coordinate minimality.

More importantly, this does not merge coefficient coercivity with destination coercivity. Even exact recovery of a growing Möbius prefix from a vanishing fraction of Fourier modes does not imply the RH-critical Franel norm bound. Any continuation that aims at RH must either connect these recovered coefficients to the nonlocal discrepancy destination with a genuinely stronger inequality, or exploit Farey-order structure before it collapses to source identification.

Clue transition check: no accepted clue changes status. This finding follows the explicit partial-observation frontier in the current research map and does not resolve the surviving clue-specific programs.

## Related findings

- `FD-117` — complete Farey discrepancy is explicitly invertible to the quotient-Mertens staircase.
- `FD-118` — `\mathcal Q_H` is a minimal full Fourier skeleton and is closed under divisors.
- `FD-164`--`FD-165` — finite-cutoff exact fields admit dense orientation ambiguity when the source may move with the cutoff.
- `FD-166` — unbounded exact complete fields rigidify one permanent source.
- `FD-167` — complete-field `L^2` inversion has uniform square-root-prefix conditioning.