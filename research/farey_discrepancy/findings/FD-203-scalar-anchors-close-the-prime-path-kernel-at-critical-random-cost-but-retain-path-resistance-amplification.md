# FD-203 — Scalar anchors close the prime-path kernel at critical random cost but retain path-resistance amplification

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** prime-path anchoring / effective-resistance audit / fixed-mode cross-horizon differencing / random-multiplicative benchmark
- **Depends on:** FD-196, FD-197, FD-201, FD-202
- **Classification:** `EXACT-DERIVED + PRIME-PATH-ANCHOR + EFFECTIVE-RESISTANCE + RANDOM-MULTIPLICATIVE-CRITICAL-BASELINE + REPRESENTATION-SPACE-CONDITIONING`

## Claim

`FD-202` reduces the square-root prime-shell obstruction to the one-dimensional constant kernel of a path gradient and leaves open whether one low-rank anchor can finish the job without restoring the `H^(3/2)` diagonal tariff. The answer splits cleanly into two parts:

1. **yes, a scalar anchor can close the kernel at the same critical random-multiplicative `H` scale;** but
2. **no, one scalar anchor does not make the path energy uniformly well-conditioned across the whole shell.** The lost half power reappears as ordinary path resistance when one propagates the anchor to distant prime modes.

Retain the notation of `FD-202`. Let

\[
K:=\lfloor\sqrt H\rfloor,
\qquad
K/2<p_1<\cdots<p_m\le K,
\tag{1}
\]

and write

\[
S_i:=S_{r,H}(p_i)
=
M\!\left(\left\lfloor\frac{rH}{p_i}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H{p_i}\right\rfloor\right),
\qquad r\ge2.
\tag{2}
\]

The FD-202 path energy is

\[
Q(S):=\sum_{i=1}^{m-1}|S_i-S_{i+1}|^2.
\tag{3}
\]

For any complex linear scalar anchor `ell` satisfying

\[
\ell(\mathbf 1)=1,
\tag{4}
\]

define the anchored norm

\[
\|S\|_\ell^2:=Q(S)+|\ell(S)|^2.
\tag{5}
\]

Then the endpoint-difference functional has exact dual norm

\[
\boxed{
\|e_1-e_m\|_{\ell,*}^2=m-1,
}
\tag{6}
\]

independently of the choice of scalar anchor. Consequently

\[
\boxed{
\max_{1\le i\le m}\|e_i\|_{\ell,*}^2
\ge \frac{m-1}{4}.
}
\tag{7}
\]

Thus every one-dimensional anchoring of the constant mode leaves worst-case point-evaluation amplification at least of order `m` in squared norm.

This order is sharp. For the endpoint anchor

\[
\ell(S)=S_m,
\tag{8}
\]

one has exactly

\[
\boxed{
\|e_i\|_{\ell,*}^2=m-i+1,
\qquad 1\le i\le m,
}
\tag{9}
\]

and hence

\[
\max_i\|e_i\|_{\ell,*}^2=m.
\tag{10}
\]

Since PNT gives

\[
m=\pi(K)-\pi(K/2)\sim\frac{K}{2\log K},
\tag{11}
\]

the minimax point-evaluation condition number of `path gradient + one scalar anchor` is therefore `Theta(K/log K)` in squared norm.

The endpoint anchor is nevertheless **cheap in the same source-faithful random benchmark as FD-202**. For the squarefree Rademacher multiplicative source `f`, define

\[
\mathcal A_{r,H}^f
:=
K\left(Q(S^f)+|S_m^f|^2\right).
\tag{12}
\]

FD-202 gives

\[
\mathbb E Q(S^f)
\sim
\frac6{\pi^2}(1+r)K.
\tag{13}
\]

The endpoint row is the squarefree-random sum on

\[
\left(\left\lfloor\frac H{p_m}\right\rfloor,
      \left\lfloor\frac{rH}{p_m}\right\rfloor\right],
\tag{14}
\]

whose length is `(r-1)K+o(K)` because `p_m=K+o(K)`. Orthogonality and squarefree density therefore give

\[
\mathbb E|S_m^f|^2
\sim
\frac6{\pi^2}(r-1)K.
\tag{15}
\]

Hence

\[
\boxed{
\mathbb E\,\mathcal A_{r,H}^f
\sim
\frac{12r}{\pi^2}H.
}
\tag{16}
\]

So the one-dimensional kernel of FD-202 really can be removed **without restoring the diagonal `H^(3/2)` random tariff**.

What the anchor does *not* provide is uniform shell recovery at that same budget. For the endpoint choice, (9) is equivalent to the sharp inequalities

\[
|S_i|^2
\le
(m-i+1)\left(Q(S)+|S_m|^2\right),
\tag{17}
\]

with equality achievable in unrestricted shell-coordinate space. Therefore a bound at the random-critical scale

\[
\mathcal A_{r,H}=H^{1+o(1)}
\tag{18}
\]

permits, by the quadratic norm alone, worst-case distant coordinates as large as

\[
|S_i|
\lesssim
\frac{K^{1+o(1)}}{\sqrt{\log K}},
\tag{19}
\]

rather than the RH-sized `K^(1/2+o(1))` interval increment. More generally, (7) shows that no scalar anchor can improve this *uniform* representation-space conditioning by more than a constant factor.

Equivalently, if one insists that `path energy + one scalar anchor` alone force

\[
\max_i |S_i|\le K^{1/2+o(1)}
\tag{20}
\]

for every shell vector, the anchored shell budget must be of order at most

\[
\boxed{
K\frac{K}{m}
\asymp
K\log K
=
H^{1/2+o(1)},
}
\tag{21}
\]

up to constants and subpower factors. The endpoint anchor attains this order, while (7) makes it necessary for any scalar anchor in the unrestricted shell-coordinate problem.

There is an important boundary: **the anchored coordinate itself does not pay path resistance.** From (12),

\[
|S_m|^2\le\frac{\mathcal A_{r,H}}K,
\tag{22}
\]

so an `H^(1+o(1))` bound already gives

\[
|S_m|\le K^{1/2+o(1)}.
\tag{23}
\]

Thus FD-203 does not rule out a successful route in which the scalar anchor is itself a strategically chosen geometric witness and coherence across horizons propagates that witness without traversing the prime path. It rules out the simpler inference that, once the one-dimensional kernel is anchored, the critical FD-202 path energy automatically becomes uniformly coercive on the whole shell.

## 1. Exact scalar-anchor resistance theorem

Let `d_j:=S_j-S_(j+1)`. Then

\[
S_1-S_m=\sum_{j=1}^{m-1}d_j.
\tag{24}
\]

Cauchy--Schwarz gives

\[
|S_1-S_m|^2
\le
(m-1)Q(S)
\le
(m-1)\|S\|_\ell^2.
\tag{25}
\]

This constant is exact for every anchor satisfying (4). Take all increments equal to a common value `c`, so that `S_1-S_m=(m-1)c` and `Q=(m-1)|c|^2`. Adding a constant to every coordinate leaves the increments unchanged, and because `ell(1)=1` there is a unique constant shift that makes `ell(S)=0`. For that shifted vector the anchored norm equals `Q`, so equality holds in (25). This proves (6).

The triangle inequality in the dual norm now gives

\[
\sqrt{m-1}
=
\|e_1-e_m\|_{\ell,*}
\le
\|e_1\|_{\ell,*}+\|e_m\|_{\ell,*},
\tag{26}
\]

and therefore at least one endpoint has squared dual norm at least `(m-1)/4`, proving (7).

For the endpoint anchor `ell=e_m`, use the orthogonal coordinate system

\[
(S_m,d_1,\ldots,d_{m-1}).
\tag{27}
\]

The norm (5) becomes the ordinary Euclidean norm in these coordinates, while

\[
S_i=S_m+\sum_{j=i}^{m-1}d_j.
\tag{28}
\]

The representing coefficient vector has exactly `m-i+1` unit entries. Its squared Euclidean norm is therefore `m-i+1`, proving (9) and the sharpness of (17).

This is the path-graph effective-resistance mechanism in its simplest finite form: after grounding one scalar direction, point evaluation at graph distance `d` carries a dual cost of order `d`. No spectral approximation or asymptotic graph theorem is needed.

## 2. Random-multiplicative price of the endpoint anchor

For the Rademacher multiplicative source

\[
f(n)=\mu(n)^2\prod_{p\mid n}X_p,
\tag{29}
\]

one has

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\mathbf 1_{a=b}.
\tag{30}
\]

FD-202 already propagates this covariance through the prime-path derivative and proves (13). At the last shell prime,

\[
S_m^f
=
\sum_{\lfloor H/p_m\rfloor<n\le\lfloor rH/p_m\rfloor}f(n).
\tag{31}
\]

Therefore

\[
\mathbb E|S_m^f|^2
=
\sum_{\lfloor H/p_m\rfloor<n\le\lfloor rH/p_m\rfloor}\mu(n)^2.
\tag{32}
\]

PNT implies `p_m=K+o(K)`, while `H=K^2+O(K)`. Hence the interval in (32) has length `(r-1)K+o(K)` and lies at scale `Theta_r(K)`. The standard squarefree counting asymptotic gives (15). Adding (13) and (15), then multiplying by `K`, proves (16).

This calculation is important because it separates two costs. **Kernel removal is cheap in the random benchmark; propagation is expensive in the deterministic inverse.** The first costs only another `Theta(K)` unscaled variance, preserving the `Theta(H)` shell scale. The second costs `Theta(m)` in squared dual norm because the path has diameter `Theta(m)`.

## 3. What the resistance barrier does and does not say

Equations (6)--(10) are exact finite-dimensional statements about the observed prime-shell coordinate vector after the FD-202 projection. They show that a one-dimensional kernel is not synonymous with uniformly cheap inversion. The graph carrying the projected statistic matters: a path has large effective-resistance diameter.

For an endpoint anchor, an `H^(1+o(1))` shell bound gives the correct `K^(1/2+o(1))` scale at the anchored endpoint itself, but Cauchy propagation through `Theta(K/log K)` prime steps can lose almost another square-root factor at the opposite side. The `H^(1/2+o(1))` requirement in (21) is therefore **not proposed as a new RH-equivalent Farey target**. It is the minimax budget required if one insists on obtaining uniform shell control from this particular abstract quadratic norm without using any additional arithmetic compatibility.

There are two clear escapes not ruled out here. First, the anchor may itself track the particular quotient coordinate needed by a geometric Mertens witness across horizons, avoiding propagation through the path. Second, one may replace the path by a richer exact signed projection with nonlocal or multiscale edges, seeking smaller effective-resistance diameter while keeping the source-faithful random cost on the `H` scale.

The latter is now quantitatively testable: adding edges is useful only if the decrease in effective resistance is not paid back by an `H^(3/2)`-type increase in the random-multiplicative quadratic cost. FD-203 therefore converts the vague post-FD-202 phrase "add a cheap anchor" into a two-axis design problem: **random cost versus inverse resistance**.

## 4. Representation, prior-art and formalization audits

The representation audit has two layers. For the physical Möbius source, each `S_i` is exactly the representation-native fixed-mode cross-horizon coordinate of FD-201--FD-202. The endpoint anchor uses one of those already observed coordinates; no coefficient oracle, cumulative-source inverse or synthetic source data are inserted. The random benchmark likewise randomizes prime signs before the Farey transform and uses the exact same observation map.

The lower bound (7) and the sharp endpoint conditioning (9) are deliberately classified as **representation-space conditioning statements**. Their extremizers are arbitrary shell-coordinate vectors. FD-203 does not claim that those extremizers are realizable by Möbius, by a squarefree multiplicative source, or by another Farey point set. Consequently the result does not prove that Möbius must pay the path-resistance loss; it proves that the quadratic statistic by itself cannot certify better uniform recovery unless additional arithmetic/source compatibility is explicitly used.

A targeted prior-art search found the classical effective-resistance/Dirichlet-energy viewpoint for graph Laplacians and the standard fact that path graphs are maximally resistive among connected graph topologies; for example Ghosh--Boyd--Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1) (2008), 37--66. A 2026 preprint by Pandey studies exact grounded-resistance sums on path graphs. These are neighboring graph-theoretic formulations, not inputs to the proof above, which is the elementary one-line path calculation (24)--(28). The Farey-specific coupling of that resistance to the FD-202 cross-horizon prime-shell sensor and to the random-multiplicative `H` benchmark was not found in the targeted search. No new load-bearing literature dependency is introduced, so `SOURCES.md` is unchanged.

No clue status changes. The accepted local clues concern different source-side or Farey-order mechanisms and are neither proved nor falsified by the prime-mode resistance calculation. No formalization issue is opened: the reusable finite core is elementary path Hilbert-space algebra, while the substantive Farey conclusion depends on the asymptotic shell dictionary and the source-faithful random benchmark.

## Conclusion

FD-202's gain is real but incomplete. A single endpoint observation closes its constant-mode kernel while preserving the critical random-multiplicative `H` scale, so the kernel itself does **not** force the old `H^(3/2)` tariff back in. The remaining obstruction is geometric: a path transmits that anchor with `Theta(K/log K)` squared conditioning across the shell.

The useful next discriminator is therefore sharper than "find a cheap anchor". Either the anchor must itself be the moving arithmetic witness one needs, so no path propagation is required, or the projected observation graph must acquire nonlocal/multiscale edges that reduce effective resistance without destroying the `H` random benchmark. A one-dimensional kernel can be cheap to remove and still expensive to invert.