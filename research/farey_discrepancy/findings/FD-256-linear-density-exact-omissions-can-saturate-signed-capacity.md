# FD-256 — Linear-density exact omissions can asymptotically saturate signed coefficient capacity

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / constructive lower bound / top-half antichain / signed coefficient capacity / density-threshold sharpness
- **Depends on:** FD-225, FD-245, FD-255
- **Classification:** `EXACT-DERIVED + CONSTRUCTIVE-LOWER-BOUND + LINEAR-DEFECT-SATURATION + DENSITY-THRESHOLD-SHARPNESS + SIGNED-RESPONSE-SPACE`

## Claim

FD-255 proves that if an exact response is omitted at only `K=o(H)` sample points, then every coefficient sequence satisfying the linear envelope

\[
|b_n|\le n\qquad(1\le n\le H)
\tag{1}
\]

has `o(H^2)` signed coefficient mass on the top dyadic band. The remaining macroscopic question is whether the condition `K=o(H)` is merely sufficient or whether a positive density of omitted response values can genuinely hide coefficient mass at the full `H^2` capacity scale.

It can. In fact the obstruction is elementary and does not require ill-conditioned divisor incidence geometry.

For every integer `H>=4` and every

\[
1\le K\le \left\lfloor\frac H4\right\rfloor,
\tag{2}
\]

there exist an omission set `E subseteq (H/2,H]` with `|E|=K`, an exact response `Y`, and coefficients `b_1,...,b_H` such that

\[
Y(m)=(\mathscr A b)(m),
\qquad
Y(m)=0\quad(m\notin E),
\tag{3}
\]

\[
|b_n|\le n\qquad(1\le n\le H),
\tag{4}
\]

and

\[
\boxed{
\sum_{H/2<n\le H}|b_n|>KH.
}
\tag{5}
\]

Thus every fixed positive omission density `K/H -> delta` with `0<delta<=1/4` admits exact-zero observed data while retaining a positive fraction of the available signed coefficient capacity.

More sharply, for `H=4M` and `K=M=H/4`, one can arrange

\[
\boxed{
\sum_{2M<n\le4M}|b_n|=6M^2,
}
\tag{6}
\]

whereas the maximum allowed by (1) on that band is

\[
\sum_{n=2M+1}^{4M}n=M(6M+1)=6M^2+M.
\tag{7}
\]

Hence

\[
\boxed{
\frac{\sum_{2M<n\le4M}|b_n|}
     {\sum_{2M<n\le4M}n}
=\frac{6M}{6M+1}\longrightarrow1.
}
\tag{8}
\]

So an omission density of exactly one quarter can asymptotically hide **all signed coefficient capacity** in the top half while the response is exactly zero at every observed integer.

Combined with FD-255, this pins the macroscopic exact-omission threshold at the density scale:

- `K=o(H)` is coercive at `H^2` scale;
- `K=Theta(H)` can fail maximally.

The construction is signed and finite-horizon. It is not a positive physical-source countermodel.

## Top-half response spikes become disjoint coefficient pairs

FD-225 gives the exact identities

\[
g=\mu*b=\Delta Y,
\qquad
b=\mathbf1*g,
\qquad
Y(m)=(\mathscr A b)(m),
\tag{9}
\]

with `Y(0)=0`. Equivalently,

\[
g(m)=Y(m)-Y(m-1),
\qquad
b_n=\sum_{d\mid n}g(d).
\tag{10}
\]

Choose `K` disjoint adjacent pairs

\[
\{e,e+1\}\subseteq(H/2,H],
\tag{11}
\]

and let `E` be the set of their left endpoints. Such a family exists whenever (2) holds; for example one may take

\[
e_j=\left\lfloor\frac H2\right\rfloor+1+2j,
\qquad
0\le j<K.
\tag{12}
\]

Define the response by

\[
Y(e)=e\quad(e\in E),
\qquad
Y(m)=0\quad(m\notin E).
\tag{13}
\]

Every isolated spike contributes two increments:

\[
g(e)=e,
\qquad
g(e+1)=-e.
\tag{14}
\]

Therefore

\[
\boxed{
b_n=
\sum_{e\in E}e
\bigl(\mathbf1_{e\mid n}-\mathbf1_{e+1\mid n}\bigr).
}
\tag{15}
\]

This is exactly the paired-column representation isolated in FD-245. Here, however, all active divisors lie above `H/2`. Consequently for `n<=H`,

\[
e\mid n\iff n=e,
\qquad
(e+1)\mid n\iff n=e+1.
\tag{16}
\]

The top half is an antichain for divisibility below the horizon: no active divisor has a second multiple at or below `H`. Since the pairs are disjoint, (15) collapses to the coordinate-local formula

\[
\boxed{
b_e=e,
\qquad
b_{e+1}=-e
\quad(e\in E),
}
\tag{17}
\]

with `b_n=0` at every other `n<=H`.

Equation (17) immediately gives the envelope (4), since

\[
|b_e|=e,
\qquad
|b_{e+1}|=e<e+1.
\tag{18}
\]

Because `b=1*g` was constructed from `g=Delta Y`, the response identity in (9) recovers (13) exactly. There is no approximation and no unverified inversion step: every observed sample outside `E` is exactly zero.

## Quantitative lower bound for every `K<=H/4`

Each pair contributes coefficient mass

\[
|b_e|+|b_{e+1}|=2e>H.
\tag{19}
\]

Summing (19) over the `K` disjoint pairs gives (5).

It is useful to compare this directly with the FD-255 upper bound. Define the finite-horizon extremal top-band mass

\[
\mathcal M(H,K)
:=
\sup
\sum_{H/2<n\le H}|b_n|,
\tag{20}
\]

where the supremum ranges over all sequences satisfying `|b_n|<=n` and all exact responses that vanish outside at most `K` omitted integers. Then the present construction gives

\[
\boxed{
\mathcal M(H,K)>KH
\qquad
\left(K\le\left\lfloor\frac H4\right\rfloor\right).
}
\tag{21}
\]

On the other hand, FD-255 gives for `K<=H/4`

\[
\mathcal M(H,K)
\ll
KH\log\!\left(e+\log\frac HK\right).
\tag{22}
\]

Thus throughout the sparse-to-linear range currently controlled by the two findings,

\[
\boxed{
KH
\lesssim
\mathcal M(H,K)
\lesssim
KH\log\!\left(e+\log\frac HK\right),
}
\tag{23}
\]

up to absolute constants. The only remaining gap in this signed exact-omission extremal norm is the slowly varying double logarithm from FD-255. At fixed `K`, FD-245 already gives an `O_K(H)` upper bound, matching the `H` scale of (21).

For `K=delta H+o(H)` with fixed `0<delta<=1/4`, (21) alone gives

\[
\mathcal M(H,K)\gg_\delta H^2.
\tag{24}
\]

Therefore no theorem based only on the coefficient envelope and exact response values can extend the FD-255 conclusion from `K=o(H)` to arbitrary positive-density omission sets.

## Quarter-density construction asymptotically fills the whole top band

Take

\[
H=4M,
\qquad
K=M,
\tag{25}
\]

and choose

\[
E=\{2M+1,2M+3,\ldots,4M-1\}.
\tag{26}
\]

The paired supports

\[
\{e,e+1\},\qquad e\in E,
\tag{27}
\]

partition the entire top band

\[
\{2M+1,2M+2,\ldots,4M\}.
\tag{28}
\]

Using (17),

\[
\begin{aligned}
\sum_{2M<n\le4M}|b_n|
&=2\sum_{j=0}^{M-1}(2M+1+2j)\\
&=2\left(M(2M+1)+M(M-1)\right)\\
&=6M^2,
\end{aligned}
\tag{29}
\]

which proves (6). The total coefficient capacity is (7), so the only unused capacity is

\[
M(6M+1)-6M^2=M.
\tag{30}
\]

That loss is exactly one unit at each right endpoint, because `|b_{e+1}|=e` while the local envelope permits `e+1`. Relative to the `Theta(M^2)` capacity, this defect vanishes. Equation (8) follows.

This also shows why the example does not rely on delicate arithmetic resonance. Above `H/2`, the divisor transform has no cross-talk below the horizon. The omission spikes are converted into almost envelope-saturating adjacent signed coefficient pairs one by one.

## Reconciliation with FD-255

FD-255 proves, with

\[
\eta=\min\left(1,\frac{2K}{H}\right),
\tag{31}
\]

that every exact-omission sequence under the same coefficient envelope satisfies

\[
\sum_{n\le H}|b_n|
\ll
H^2\eta
\log\!\left(e+\log\frac1\eta\right).
\tag{32}
\]

When `K=o(H)`, the right side is `o(H^2)`. The present family shows that this qualitative hypothesis cannot be weakened to `K=O(H)` or even to `K<=delta H` for an arbitrary fixed `delta>0`: for every fixed `delta<=1/4`, choose `K=floor(delta H)` disjoint top-half pairs and obtain (24).

Hence the macroscopic transition is now sharp in order:

\[
\boxed{
K/H\to0
\quad\Longrightarrow\quad
\text{top-band signed mass}=o(H^2),
}
\tag{33}
\]

whereas

\[
\boxed{
K/H\to\delta>0
\quad\not\Longrightarrow\quad
\text{top-band signed mass}=o(H^2).
}
\tag{34}
\]

At `delta=1/4`, failure is asymptotically maximal by (8).

This clarifies the role of the incidence-conditioning branch FD-248--FD-254. Large conditioning is relevant for finer sparse-defect norms, but it is not needed to witness the first noncoercive density regime. Once enough response locations are omitted to place disjoint paired columns entirely in `(H/2,H]`, the divisor geometry becomes diagonal below the horizon and the envelope itself can be saturated.

## Adversarial checks

The construction was checked against the main failure modes exposed by FD-245--FD-255.

First, the omission set is the response-spike set `E`, not the increment support. The increment support is

\[
D=E\cup(E+1),
\tag{35}
\]

so `|D|=2K`. This is exactly the pairing constraint required by `g=Delta Y`; no independent sparse increments are being prescribed.

Second, divisor cross-talk cannot create extra coefficients below the horizon. Every `d in D` satisfies `d>H/2`, hence its only positive multiple at most `H` is itself. Equation (17) is therefore exact even when many pairs are present.

Third, the envelope is checked coefficient by coefficient, not only in aggregate. Each left endpoint saturates it and each right endpoint misses saturation by exactly one.

Fourth, the response is reconstructed through the exact FD-225 inverse identities, so the zeros outside `E` are genuine all-integer response zeros rather than switched or dyadic zeros.

Finally, the example is deliberately signed: half of each pair is negative. Any attempt to turn it directly into a nonnegative physical occupancy must pay macroscopic one-sided slack, precisely the obstruction studied in FD-230--FD-233. Nothing here bypasses that source-side constraint.

## Prior-art / novelty audit

The algebraic ingredient `b=1*Delta Y` is ordinary Dirichlet/Möbius inversion and is already internal and source-anchored through FD-225. A targeted prior-art search around sparse exact sampling, divisor transforms and Möbius-pair uncertainty surfaced the classical inversion framework and qualitative support-uncertainty results, but no external theorem is needed for this construction.

The substantive line-level contribution is therefore not a novelty claim about Möbius inversion. It is the explicit extremal use of the top-half divisibility antichain to settle the density-scale boundary left open by FD-255: positive-density exact omissions can retain `Theta(H^2)` signed coefficient mass, and quarter-density omissions can asymptotically attain the entire top-band envelope.

No new external result is load-bearing, so this pass adds no dependency to `SOURCES.md`.

## Boundary and research consequence

The signed exact-zero response picture is now qualitatively complete at macroscopic coefficient scale. FD-255 excludes `K=o(H)`; FD-256 constructs `K=Theta(H)` families with macroscopic hidden mass. Further work on exact omissions should therefore be **finer than the `H^2` capacity scale**, for example determining whether the double-log factor in (23) is real when `K/H->0` and `K->infinity`.

The physical Farey problem remains stricter. The present coefficients have a negative part of the same order as their positive part, so the construction is not a nonnegative source, does not respect finite prime-reservoir occupancy by itself, and does not establish a Farey countermodel. The next macroscopic route must therefore use source-side information rather than another refinement of exact-response sampling density.

## Status

**Proved.** The construction follows exactly from the FD-225 identities, disjoint adjacent response spikes above `H/2`, and the fact that an integer larger than `H/2` has no second multiple below `H`. It yields the lower bound (21), the asymptotic quarter-density saturation (8), and, together with FD-255, proves that `K=o(H)` is sharp in order as the macroscopic exact-omission coercivity threshold. The result is signed and finite-horizon and does not imply RH.