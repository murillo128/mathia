# WI-084 — subwindow Ramanujan blocks form an exact Toeplitz basis

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens the signed scalar route in WI-079--WI-083 by showing that WI-083's exact saturated cancellation is necessarily a **super-window modulus phenomenon**: if every aggregated scalar modulus is at most the sample-window length, the finite Ramanujan blocks are linearly independent, indeed they form a basis of the real symmetric Toeplitz space. The coefficient-to-operator map is also quantitatively injective up to a polylogarithmic loss.

For an integer `N>=1`, write

\[
B_m^{(N)}=(c_m(i-j))_{0\le i,j<N},
\qquad 1\le m\le N,
\]

where `c_m` is the Ramanujan sum. Then

\[
\boxed{
\{B_1^{(N)},B_2^{(N)},\ldots,B_N^{(N)}\}
\text{ is a basis of the real symmetric }N\times N\text{ Toeplitz matrices}.}
\tag{1}
\]

Equivalently, the `N x N` consecutive-lag evaluation matrix

\[
C_N=(c_m(h))_{0\le h<N,\ 1\le m\le N}
\]

has the exact determinant

\[
\boxed{\det C_N=(-1)^{N-1}N!.}
\tag{2}
\]

Hence for arbitrary real aggregated coefficients supported on `m<=N`,

\[
\boxed{
\sum_{m\le N}\omega_m B_m^{(N)}=0
\quad\Longrightarrow\quad
\omega_m=0\ \text{for every }m.}
\tag{3}
\]

For `N>=2` there is also the elementary quantitative bound

\[
\boxed{
\left\|\sum_{m\le N}\omega_m B_m^{(N)}\right\|_{\rm op}
\ge
\frac{\max_{m\le N}|\omega_m|}{2(1+\log N)^2}.}
\tag{4}
\]

Thus, before any source-specific normalization is inserted, subwindow scalar Ramanujan blocks cannot even approximately annihilate a coefficient of fixed size by more than a polylogarithmic factor. This is much stronger than the rank-only information in WI-081--WI-082, but it applies to **coefficient cancellation of the scalar operator**, not directly to the inertia of a nonzero operator.

## 1. Exact divisor-factorization of the consecutive-lag matrix

The classical Kluyver formula is

\[
c_m(h)=\sum_{d\mid(m,h)}d\,\mu(m/d).
\tag{5}
\]

It remains valid at `h=0`, where every `d|m` divides zero and the sum is `phi(m)`. Define

\[
P_N(h,d):=d\,1_{d\mid h},
\qquad 0\le h<N,\ 1\le d\le N,
\tag{6}
\]

with the usual convention `d|0`, and

\[
M_N(d,m):=\mu(m/d)1_{d\mid m},
\qquad 1\le d,m\le N.
\tag{7}
\]

Then (5) gives the exact matrix factorization

\[
\boxed{C_N=P_NM_N.}
\tag{8}
\]

The matrix `M_N` is upper triangular in the natural ordering because `d|m` implies `d<=m`, and its diagonal entries are `mu(1)=1`. Therefore

\[
\det M_N=1.
\tag{9}
\]

The last column of `P_N`, corresponding to `d=N`, has exactly one nonzero entry: `P_N(0,N)=N`. Expanding along that column leaves the `(N-1)x(N-1)` matrix

\[
(d\,1_{d\mid h})_{1\le h,d\le N-1},
\]

which is lower triangular with diagonal `1,2,...,N-1`. Hence

\[
\det P_N
=(-1)^{N-1}N(N-1)!
=(-1)^{N-1}N!,
\tag{10}
\]

and (2) follows from (8)--(10).

A real symmetric Toeplitz matrix is determined by the `N` real lags `R(0),...,R(N-1)`, so that space has dimension `N`. The first row of `B_m^(N)` is exactly the corresponding column of `C_N` (up to the harmless evenness `c_m(-h)=c_m(h)`). Invertibility of `C_N` therefore proves the basis statement (1), not merely linear independence.

## 2. Explicit coefficient recovery by Möbius inversion

The determinant proof can be strengthened into a useful exact inverse. Let

\[
A_\omega^{(N)}:=\sum_{m\le N}\omega_mB_m^{(N)}
\]

and write its Toeplitz kernel as

\[
R(h):=\sum_{m\le N}\omega_mc_m(h),
\qquad 0\le h<N.
\tag{11}
\]

For `1<=d<=N`, define the divisor-marginal transform

\[
F(d):=\sum_{k\le N/d}\mu(k)\omega_{dk}.
\tag{12}
\]

Using (5) and changing the order of summation gives, for every `1<=h<N`,

\[
\boxed{R(h)=\sum_{d\mid h}dF(d).}
\tag{13}
\]

Ordinary Möbius inversion therefore recovers every `F(d)` below the window endpoint:

\[
\boxed{
dF(d)=\sum_{e\mid d}\mu(d/e)R(e),
\qquad 1\le d<N.}
\tag{14}
\]

The transform (12) itself has the finite inverse

\[
\boxed{
\omega_m=\sum_{k\le N/m}F(mk).}
\tag{15}
\]

Indeed, substituting (12) into the right side of (15) gives `omega_m` by the identity `sum_{d|n}mu(d)=1_{n=1}`.

The only quantity not fixed by the nonzero lags is `F(N)`. The diagonal fixes it exactly. From (15) and `sum_{d|n}phi(d)=n`,

\[
\begin{aligned}
R(0)
&=\sum_{m\le N}\omega_m\varphi(m)\\
&=\sum_{n\le N}F(n)\sum_{m\mid n}\varphi(m)\\
&=\sum_{n\le N}nF(n).
\end{aligned}
\tag{16}
\]

Thus

\[
\boxed{
F(N)=\frac1N\left(R(0)-\sum_{n<N}nF(n)\right).}
\tag{17}
\]

Equations (14), (17), and (15) are an explicit inverse from the finite Toeplitz kernel back to all scalar coefficients `omega_1,...,omega_N`.

They also identify the one-dimensional ambiguity if the diagonal is deliberately discarded. If `R(h)=0` for every `1<=h<N`, then `F(d)=0` for `d<N`, so (15) gives

\[
\omega_m=
\begin{cases}
F(N),&m\mid N,\\
0,&m\nmid N.
\end{cases}
\tag{18}
\]

This is exactly the classical relation

\[
\sum_{m\mid N}c_m(h)=N\,1_{N\mid h}.
\tag{19}
\]

The diagonal value is then `R(0)=NF(N)`, so the full finite matrix has no nontrivial kernel. This gives a second exact proof of (3).

## 3. Polylogarithmic stability against approximate signed cancellation

Put

\[
\Delta:=\|A_\omega^{(N)}\|_{\rm op}.
\]

Every matrix entry has magnitude at most `Delta`, so

\[
|R(h)|\le\Delta
\qquad(0\le h<N).
\tag{20}
\]

From (14), for `d<N`,

\[
|F(d)|
\le\frac{\tau(d)}d\Delta.
\tag{21}
\]

Equation (17) and the elementary divisor-count bound

\[
\sum_{d<N}\tau(d)\le N(1+\log N)
\tag{22}
\]

give

\[
|F(N)|\le(2+\log N)\Delta.
\tag{23}
\]

For the remaining terms in (15), use `tau(ab)<=tau(a)tau(b)`, `tau(m)<=m`, and

\[
\sum_{k\le K}\frac{\tau(k)}k
=\sum_{ab\le K}\frac1{ab}
\le H_K^2
\le(1+\log K)^2.
\tag{24}
\]

Therefore the contribution from all `mk<N` is at most

\[
(1+\log N)^2\Delta.
\tag{25}
\]

If `m|N`, one extra endpoint term `F(N)` occurs. For `N>=2`,

\[
2+\log N\le(1+\log N)^2,
\]

so (23)--(25) give uniformly

\[
|\omega_m|
\le2(1+\log N)^2\Delta.
\tag{26}
\]

Taking the largest coefficient proves (4).

This bound is intentionally crude; no claim is made that the logarithmic exponent or constant is optimal. Its role is structural: the finite coefficient map is not merely algebraically injective in the subwindow regime. Any near-zero operator must also have every aggregated scalar coefficient small relative to the operator scale, with only a polylogarithmic inversion loss.

## 4. This separates two different kinds of overcompleteness

WI-082 factors the signed scalar operator as

\[
A_\omega^{(N)}=WJW^*,
\]

where `W` concatenates primitive Fourier atoms. Once the total primitive-mode count `K` exceeds `N`, `W` is overcomplete and dimension alone no longer fixes the inertia. WI-083 then exhibited a doubly saturated family of primes `p,q,r>N` whose weighted blocks cancel exactly.

The present result shows that these statements must not be conflated with **block-coefficient** dependence. Even when the primitive-frequency dictionary is heavily overcomplete, the `N` block matrices

\[
B_1^{(N)},...,B_N^{(N)}
\]

remain a basis. Thus

\[
\boxed{
K>N
\quad\text{does not by itself imply}\quad
\text{a nontrivial linear relation among the scalar Ramanujan blocks}.}
\tag{27}
\]

WI-083 is not contradicted. Its exact relation deliberately uses moduli larger than the observation window, where distinct long-period blocks can collapse to the same short finite-section features. The super-window hypothesis is therefore not a cosmetic choice in that witness: **some active modulus must exceed `N` in every exact zero relation**.

The phase boundary is now sharper:

\[
\boxed{
\begin{array}{ll}
\max m\le N:&\text{coefficient map is injective and polylogarithmically stable};\\
\max m>N:&\text{exact block collapse can occur, as WI-083 shows}.
\end{array}}
\tag{28}
\]

This boundary concerns the universal scalar Ramanujan interface. It says nothing by itself about whether the exact Yang covariance actually reduces to that interface.

## 5. Consequence for the Baker--Munsch--Shparlinski scalar escape

WI-077 records the printed Baker--Munsch--Shparlinski critical range for a regular scalar modulus sequence `m_j=j^(alpha+o(1))`:

\[
Q^\alpha\le N\le Q^{2\alpha}.
\tag{29}
\]

For the Yang unlabelled scalar family, WI-076--WI-077 give the natural exponent `alpha=1`: a source-scale block has `Q=X^(1+o(1))` effective scalar moduli, all lying in a range `m\ll X=Q^(1+o(1))`.

Consequently, at every fixed strict interior exponent

\[
N=Q^\theta,
\qquad 1<\theta\le2,
\tag{30}
\]

all source-scale scalar moduli satisfy `m<N` for sufficiently large `Q`. In that regime, any source-faithful signed scalar reduction of the WI-079 form lies under the basis theorem (1)--(4). In particular, the exact large-prime cancellation mechanism of WI-083 cannot be the explanation for a saving in the strict interior of the BMS range.

This does **not** restore the positive BMS theorem as a proof of the Yang covariance: WI-077--WI-079 already show that the unweighted support/energy route loses the signs, and the exact source-to-signed-scalar reduction remains unproved. It only changes the surviving signed possibility. In the strict interior, a scalar proof would have to exploit the actual smallness/structure of the aggregated coefficients, a nontrivial metric effect of a **nonzero** operator, or retained source labels; it cannot invoke universal exact block dependence.

The endpoint `theta=1` is different. There the scalar modulus scale and sample-window scale agree only up to subpolynomial factors, so (30) no longer forces `m<=N` without an exact source normalization. WI-083's super-window phenomenon therefore remains a legitimate endpoint warning, as do alternative scalar transforms whose observation window is shorter than their active modulus range.

## 6. Prior art and novelty boundary

All load-bearing arithmetic identities are classical.

- Kluyver's formula (5), Möbius inversion, `sum_{d|n}phi(d)=n`, and the elementary divisor-sum bounds used in (22)--(24) are standard number theory. The Ramanujan-sum identities and finite-period language are already anchored for this line through Ushiroya and Vaidyanathan in `SOURCES.md`.
- Noboru Ushiroya, **Eigenvalues of Matrices whose Elements are Ramanujan Sums or Kloosterman Sums**, *Journal of Integer Sequences* 21 (2018), Article 18.2.6; arXiv:1803.02970, studies complete-period Ramanujan matrices and their spectra. WI-080 already uses this as the complete-period counterpart of the present finite-section problem.
- P. P. Vaidyanathan, **Ramanujan Sums in the Context of Signal Processing--Part I/II**, *IEEE Transactions on Signal Processing* 62 (2014), develops finite-duration Ramanujan subspaces and exact-period decompositions.
- Jan-Christoph Schlage-Puchta, **A determinant involving Ramanujan sums and So's conjecture**, *Archiv der Mathematik* 117 (2021), 379--384, DOI `10.1007/s00013-021-01643-8`, proves invertibility and an exact determinant for a different Ramanujan matrix indexed by the divisors of one integer. It is nearby determinant prior art, not the matrix in (2).

A bounded search of Ramanujan determinant/basis literature found these complete-period, divisor-indexed, and finite-signal frameworks but did not locate the exact consecutive-modulus/consecutive-lag determinant (2) or the WI-079 scalar-interface consequence (28). **No priority claim is made.** The durable Mathia contribution here is the exact application of classical divisor factorization to the finite signed scalar operator isolated by WI-079, together with the explicit inverse/stability bound and the resulting correction to how WI-082--WI-083 should be used.

No `SOURCES.md` change is required for the load-bearing argument: Ushiroya, Vaidyanathan, and Baker--Munsch--Shparlinski are already durable anchors there; Schlage-Puchta is recorded here only to delimit nearby determinant prior art.

## 7. Boundary conditions and falsification

1. **All active scalar moduli must satisfy `m<=N`.** A single super-window modulus lies outside the basis theorem for the active family and can participate in relations such as WI-083.
2. **Aggregate equal moduli first.** As in WI-079--WI-083, repeated copies of the same scalar modulus must be combined into one coefficient before applying (3)--(4).
3. **Consecutive sample window.** Translation of `N` consecutive coordinates is harmless because the scalar kernel depends only on differences. Sparse/nonconsecutive sampling is a different matrix and need not satisfy (2).
4. **Scalar Ramanujan interface only.** Mathia has still not proved that the full post-local-main Yang locked covariance equals `sum omega_m B_m^(N)`. The result is a theorem about that proposed interface, not a theorem about the original covariance.
5. **Injectivity is not an inertia lower bound.** A nonzero Hermitian matrix may have small rank or an unbalanced signature. Equations (3)--(4) block exact/strong coefficient cancellation; they do not by themselves force many positive or negative eigenvalues.
6. **Approximate source cancellation can still be useful.** Bound (4) is relative to the largest aggregated coefficient. If the source normalization makes every individual `omega_m` tiny while the relevant comparison scale is much larger, the theorem alone need not obstruct the desired estimate.
7. **The BMS endpoint remains open.** The exponent statement `m=Q^(1+o(1))`, `N=Q` does not decide the exact inequality `m<=N`; constants and subpolynomial factors matter there.
8. **No zeta proportion changes.** This is a structural barrier/redirection for one proposed route to the one-sided fourth moment, not a new simple-critical-zero bound.

## 8. Consequence for the research program

The cheapest next test for a signed scalar Yang proposal is now more precise than after WI-083:

\[
\boxed{
\text{derive the exact scalar interface}
\;\longrightarrow\;
\text{compare every active modulus with its sample length }N
\;\longrightarrow\;
\begin{cases}
\max m\le N:&\text{use the exact inverse (14)--(17) before any cancellation heuristic},\\
\max m>N:&\text{audit the super-window collapse/moment relations of WI-083}.
\end{cases}}
\tag{31}
\]

In particular, **primitive-frequency overcompleteness is no longer the decisive scalar gate by itself**. The modulus/window ratio is a separate exact invariant. In the subwindow regime, the signed Ramanujan operator retains every aggregated scalar coefficient and cannot vanish nontrivially; only after the modulus range protrudes beyond the observation window can universal finite-section aliasing create the complete cancellation exhibited in WI-083.
