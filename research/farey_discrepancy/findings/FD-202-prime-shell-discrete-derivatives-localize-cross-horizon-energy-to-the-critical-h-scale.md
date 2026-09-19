# FD-202 — Prime-shell discrete derivatives localize cross-horizon energy to the critical H scale

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** cross-mode projection / fixed-mode cross-horizon differencing / prime-path Dirichlet energy / random-multiplicative benchmark
- **Depends on:** FD-117, FD-196, FD-197, FD-200, FD-201
- **Classification:** `EXACT-DERIVED + CROSS-MODE-PROJECTION + PRIME-PATH-DIRICHLET + RANDOM-MULTIPLICATIVE-CRITICAL-BASELINE + POSITIVE/PROJECTED-ROUTE-CANDIDATE`

## Claim

`FD-201` shows that fixed-mode cross-horizon rows are genuinely source-sensitive, but squaring those rows independently leaves a random-multiplicative prime-shell baseline of size `H^(3/2+o(1))`. The missing operation is visible already inside the same observed shell: **take a signed discrete derivative across adjacent prime modes before squaring**.

Let

\[
D_{r,H}(k):=\mathcal B_{rH}(k)-\mathcal B_H(k),
\qquad r\ge2
\tag{1}
\]

for the same signed Farey/divisor coordinates as `FD-201`, put

\[
K:=\lfloor\sqrt H\rfloor,
\tag{2}
\]

and list the primes in the square-root shell as

\[
K/2<p_1<p_2<\cdots<p_m\le K.
\tag{3}
\]

For the physical source `A=M`, normalize and center the prime row by

\[
S_{r,H}(p)
:=
\frac{D_{r,H}(p)-D_{r,H}(1)}p
=
M\!\left(\left\lfloor\frac{rH}{p}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H p\right\rfloor\right).
\tag{4}
\]

Define the adjacent-prime discrete derivative

\[
\delta_i
:=
S_{r,H}(p_i)-S_{r,H}(p_{i+1}),
\qquad 1\le i<m.
\tag{5}
\]

Writing

\[
L_i:=\left\lfloor\frac H{p_i}\right\rfloor,
\qquad
R_i:=\left\lfloor\frac{rH}{p_i}\right\rfloor,
\tag{6}
\]

there is the exact localization identity

\[
\boxed{
\delta_i
=
\sum_{R_{i+1}<n\le R_i}\mu(n)
-
\sum_{L_{i+1}<n\le L_i}\mu(n).
}
\tag{7}
\]

Thus a row of `FD-201`, which sums over a multiplicative interval of length `Theta(K)`, becomes after adjacent-prime differencing a difference of two **endpoint slabs** whose lengths are controlled by the prime gap `p_(i+1)-p_i`:

\[
\frac{H(p_{i+1}-p_i)}{p_i p_{i+1}}
\quad\text{and}\quad
\frac{rH(p_{i+1}-p_i)}{p_i p_{i+1}},
\tag{8}
\]

up to the harmless floor errors. Since `p_i,p_(i+1)=Theta(K)` and `H=Theta(K^2)`, these lengths are `Theta_r(p_(i+1)-p_i)` rather than `Theta(K)`.

The slabs telescope globally. The lower slabs are pairwise disjoint and partition

\[
(L_m,L_1],
\tag{9}
\]

while the upper slabs are pairwise disjoint and partition

\[
(R_m,R_1].
\tag{10}
\]

Moreover these two global supports are disjoint for every fixed integer `r>=2` and all sufficiently large `H` (indeed the elementary shell inequalities already give `R_m>=L_1`).

Now define the path Dirichlet energy

\[
Q_{r,H}
:=
\sum_{i=1}^{m-1}|\delta_i|^2
\tag{11}
\]

and its shell-normalized version

\[
\boxed{
\mathcal G_{r,H}:=K Q_{r,H}.
}
\tag{12}
\]

For the standard squarefree Rademacher random multiplicative source `f`, the same construction satisfies the exact second-moment identity

\[
\boxed{
\mathbb E Q_{r,H}^f
=
\sum_{L_m<n\le L_1}\mu(n)^2
+
\sum_{R_m<n\le R_1}\mu(n)^2.
}
\tag{13}
\]

Consequently, by PNT at the two ends of the prime shell and the standard squarefree count,

\[
\boxed{
\mathbb E Q_{r,H}^f
\sim
\frac6{\pi^2}(1+r)K,
}
\tag{14}
\]

and therefore

\[
\boxed{
\mathbb E\,\mathcal G_{r,H}^f
\sim
\frac6{\pi^2}(1+r)H.
}
\tag{15}
\]

This is the first explicit post-`FD-201` positive quadratic statistic in this line whose source-faithful random-multiplicative benchmark already lies on the **critical `H` scale**, rather than the diagonal `H^(3/2+o(1))` scale. The gain comes from a signed cross-mode projection performed *before* squaring, exactly as the current frontier suggested.

The result is not an RH criterion. The path gradient has a one-dimensional constant-mode kernel on the prime shell. `G_(r,H)` controls local variation of the normalized cross-horizon rows, not their absolute level. A useful recovery theorem would still need a low-dimensional anchor or another relation that controls this kernel without recreating the shellwide overcoercion of `FD-198`--`FD-201`.

## 1. Exact boundary localization

For every prime `p`, `FD-201` gives the exact observation identity

\[
\frac{D_{r,H}(p)-D_{r,H}(1)}p
=
M\!\left(\left\lfloor\frac{rH}{p}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac Hp\right\rfloor\right).
\tag{16}
\]

Because `p_i<p_(i+1)`, both endpoint sequences decrease:

\[
L_i\ge L_{i+1},
\qquad
R_i\ge R_{i+1}.
\tag{17}
\]

Subtracting (16) at consecutive prime modes gives

\[
\begin{aligned}
\delta_i
&=[M(R_i)-M(L_i)]-[M(R_{i+1})-M(L_{i+1})]\\
&=[M(R_i)-M(R_{i+1})]-[M(L_i)-M(L_{i+1})],
\end{aligned}
\tag{18}
\]

which is exactly (7).

Ignoring floors for one line, the lower slab length is

\[
\frac H{p_i}-\frac H{p_{i+1}}
=
\frac{H(p_{i+1}-p_i)}{p_i p_{i+1}},
\tag{19}
\]

and the upper length is `r` times the same quantity. Floors change each by at most a constant. This is the localization mechanism: the common bulk of the two neighboring fixed-ratio intervals cancels algebraically before any norm is applied.

The slabs of a given endpoint family are adjacent and therefore disjoint, giving (9)--(10). The two families are also separated. Since `p_1>K/2`, `p_m<=K` and `r>=2`,

\[
\frac{rH}{p_m}
\ge
\frac{2H}{K}
>
\frac H{p_1},
\tag{20}
\]

so

\[
R_m\ge L_1.
\tag{21}
\]

Under the half-open conventions in (7), even equality of the integer endpoints creates no overlap. Hence every source coefficient that enters one of the shell derivatives enters exactly one of the two telescoped support intervals.

This is materially different from the diagonal energy of `FD-201`. There the same source coefficients are repeatedly present in many highly overlapping multiplicative intervals. Here the path incidence operator removes that repeated interior mass before the square is taken.

## 2. Exact random-multiplicative second moment

Let

\[
f(n)=\mu(n)^2\prod_{p\mid n}X_p
\tag{22}
\]

with independent Rademacher signs `X_p`. As in `FD-197` and `FD-201`,

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\mathbf 1_{a=b}.
\tag{23}
\]

Define `S^f_(r,H)` and `delta_i^f` by replacing `M` in (4)--(7) with the cumulative sum of `f`. Equation (7) remains an exact deterministic identity for each realization. By (21), the two slabs in one `delta_i^f` are disjoint, so orthogonality gives

\[
\mathbb E|\delta_i^f|^2
=
\sum_{R_{i+1}<n\le R_i}\mu(n)^2
+
\sum_{L_{i+1}<n\le L_i}\mu(n)^2.
\tag{24}
\]

Summing over `i` telescopes the disjoint slabs and proves (13) exactly. No independence between neighboring Fourier coordinates is assumed; the covariance is propagated from the random multiplicative source through the same Farey observation map and then through the exact path projection.

Let `p_1` and `p_m` denote the first and last shell primes. PNT gives

\[
p_1=\frac K2+o(K),
\qquad
p_m=K+o(K).
\tag{25}
\]

Since `H=K^2+O(K)`, this yields

\[
L_1-L_m=K+o(K),
\qquad
R_1-R_m=rK+o(K).
\tag{26}
\]

Using

\[
\sum_{n\le x}\mu(n)^2
=
\frac6{\pi^2}x+O(\sqrt x),
\tag{27}
\]

at endpoints of size `Theta_r(K)`, (13) and (26) give (14). Multiplying by `K` and using `K^2~H` proves (15).

The shell normalization in (12) is deliberate rather than canonical. On `K/2<p<=K`, the native half-Sobolev prime-row weight `p` is comparable to `K` within a fixed factor. Thus `G_(r,H)` places the path-gradient coordinates on the same shell scale as the diagonal energy audited in `FD-201`, while preserving an exact simple second-moment formula. No claim is made that it is literally the original Franel or half-Sobolev energy.

## 3. Why the half power disappears

The random benchmark can be read directly from the geometry. A fixed-mode row `S_(r,H)(p)` sums `Theta(K)` source coefficients. There are `Theta(K/log K)` prime rows, so the diagonal half-Sobolev shell of `FD-201` has random size

\[
H^{3/2+o(1)}.
\tag{28}
\]

For neighboring primes, however, the two long intervals overlap almost completely. Their signed difference retains only endpoint slabs with total length comparable to the prime gap. Across the ordered shell, those slabs partition intervals of total length `(1+r)K+o(K)`. Hence the unweighted path energy has expectation `Theta(K)`, and the shell weight raises it only to `Theta(K^2)=Theta(H)`.

So the improvement is not obtained by changing the random model, weakening multiplicativity or postulating cancellation inside each long interval. It comes from retaining a covariance that diagonal squaring discarded. In matrix language, if `S` is the vector of normalized centered prime rows and `Inc` is the incidence matrix of the prime path, then

\[
Q_{r,H}=\|\operatorname{Inc}S\|_2^2
=S^*L_{\rm path}S.
\tag{29}
\]

The non-diagonal path Laplacian subtracts neighboring rows before measuring magnitude. This is the first concrete mechanism in the line that realizes the post-`FD-201` prescription "preserve correlations before squaring" and pays the critical random scale rather than the diagonal one.

There is also an important conceptual change relative to `FD-201`. Its source intervals have length comparable to their location and are not additive short intervals. After the path projection, the surviving slabs *are* short additive intervals on average: their lengths are on the scale of prime gaps while their locations are `Theta(K)`. This makes modern work on random multiplicative functions in short intervals relevant as neighboring prior art, although none of it is needed for the second-moment identity (13).

## 4. Kernel, destination gap and next test

The path Laplacian is positive semidefinite but not coercive on the full shell. Its kernel consists of constant vectors:

\[
S_{r,H}(p_1)=\cdots=S_{r,H}(p_m).
\tag{30}
\]

Therefore a small `G_(r,H)` alone cannot recover any one `S_(r,H)(p)` or any absolute Mertens value. This prevents the critical random scale in (15) from being misread as an RH-level theorem.

What `FD-202` changes is the route audit. `FD-201` left open whether **any** positive quadratic statistic would inherit the `H^(3/2)` shell penalty. The answer is no: a non-diagonal quadratic form obtained from an exact signed projection can remove the common bulk and land naturally at `H`. The remaining cost is low-dimensional rather than shellwide.

The next decisive question is therefore narrower. Find a representation-native anchor `A_(r,H)` such that:

1. `G_(r,H)` plus `A_(r,H)` controls the destination needed for a geometric Mertens witness or the prime-extension relation currency;
2. the anchor has random-multiplicative cost at most `H^(1+o(1))` rather than restoring the diagonal `H^(3/2)` tariff; and
3. the pair is controlled by an analytically natural Farey quantity, not by inserting the source inverse by hand.

A single mean/endpoint/low-frequency coordinate is the obvious place to test first, but no such anchor theorem is claimed here. The point is that the unresolved obstruction has dropped from `Theta(K/log K)` independently squared long-interval rows to the kernel of a one-dimensional path gradient.

## 5. Representation, prior-art and formalization audits

The representation audit is clean. `D_(r,H)(p)`, `D_(r,H)(1)` and the prime ordering are all available from the same physical fixed-mode cross-horizon observation family. Subtraction, division by the known prime label and application of the path incidence matrix are exact linear transformations of observed coordinates. No cumulative-source inverse, hidden coefficient query or synthetic Fourier noise is introduced.

The random benchmark is likewise source-faithful. Randomness is placed on prime signs before the Farey transform. Equation (13) follows from the exact covariance of the squarefree Rademacher multiplicative function and disjointness of the localized source slabs; it is not a model in which Fourier modes or prime-shell rows are assumed independent.

A targeted prior-art search found the established literature on random multiplicative functions in short intervals, including Chatterjee--Soundararajan and the 2026 Harper--Soundararajan--Xu work on limiting distributions with proper normalization. That literature is genuinely adjacent now because (7) produces additive short endpoint slabs. It does not supply the Farey prime-shell path projection, the telescoping identity (13), or the critical-scale comparison (15), and no short-interval theorem is used in the proof. Standard PNT and squarefree counting are the only external analytic inputs and are already anchored for this research line, so `SOURCES.md` is unchanged.

No clue status changes. The accepted Farey-order clue concerns stronger controls on the order of Farey gaps and a spectral-allocation bridge; the prime-mode path here is a different order structure and does not resolve that question. No formalization issue is opened: the finite telescoping/disjointness core is elementary, while the substantive conclusion depends on probabilistic second moments and asymptotic prime/squarefree counts. The expected formalization return is currently too small.
