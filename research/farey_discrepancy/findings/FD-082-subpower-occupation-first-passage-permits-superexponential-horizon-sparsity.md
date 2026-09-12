# FD-082 — subpower occupation first passage permits superexponential horizon sparsity

**Status:** `EXACT-DERIVED + POINTWISE-FIRST-PASSAGE + LOGLOG-GAP-CLASSIFICATION + COUNTING-BOUNDARY + SUPEREXPONENTIAL-SPARSITY-COMPATIBILITY + FIXED-FACTOR-ACCUMULATION-OBSTRUCTION + NEGATIVE/OBSTRUCTION`.

`FD-081` upgrades the annular recurrence mechanism to the physical horizon ratio

\[
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\]

and proves that, for every fixed admissible threshold `eta`, the first later horizon with `nu_(H,D)>eta` lies at `X^(1+o(1))`. The current downstream question is whether this **power-syndetic pointwise** set is already dense enough in scale for the accumulated GCD/Schur obstructions of `FD-022`--`FD-023` to force an RH-relevant power gain.

There is an exact counting obstruction. The first-passage statement controls only the additive gaps after taking **two logarithms**. If the good horizons are enumerated increasingly, their log-log gaps tend to zero, which forces more than `log log X` good horizons below `X`; however it is fully compatible with only `(log log X)^2` good horizons below `X`, and hence with horizons that are superexponential in their index. That is precisely the sparsity regime that `FD-023` leaves open.

Consequently, **`FD-081` cannot by itself be consumed by a proof that earns only a fixed scale-independent multiplicative gain once per good horizon.** Even granting such a favorable gain at every occupied horizon, the guaranteed accumulated improvement may remain `X^(-o(1))`, too small to change a power exponent. Closing the current frontier therefore requires a quantitative strengthening of pointwise recurrence, a gain that grows with the intervening scale geometry, or a mechanism that also uses the bad intervals rather than merely skipping them.

Fix `D>=1`, a fixed nonsquarefree dilation `q>1`, and

\[
0<\eta<c_q=w(q)q^{-2\Theta}
\]

as in `FD-081`. Let

\[
\mathcal G_\eta
:=\{H\in\mathbb N:\nu_{H,D}>\eta\},
\]

and enumerate its sufficiently large elements as

\[
g_1<g_2<\cdots.
\]

Write

\[
N_\eta(X):=\#\{g_n\le X\}.
\]

Then `FD-081` implies

\[
\boxed{
\frac{\log g_{n+1}}{\log g_n}\longrightarrow1.
}
\tag{1}
\]

Equivalently, with

\[
u_n:=\log\log g_n,
\]

one has

\[
\boxed{u_{n+1}-u_n\longrightarrow0.}
\tag{2}
\]

Hence

\[
\boxed{
\frac{N_\eta(X)}{\log\log X}\longrightarrow\infty.
}
\tag{3}
\]

This is the universal counting content of the first-passage theorem. It is much weaker than the `N_eta(X) \gg \log X` scale that would turn a fixed gain per occupied horizon into a fixed power of `X`.

## 1. First passage is exactly a vanishing log-log gap condition

`FD-081` defines

\[
\sigma_\eta(X)
:=
\min\{H>X:\nu_{H,D}>\eta\}
\]

and proves

\[
\frac{\log\sigma_\eta(X)}{\log X}\longrightarrow1.
\tag{4}
\]

At a good horizon `X=g_n`, the next first passage is exactly

\[
\sigma_\eta(g_n)=g_{n+1}.
\]

Substituting into (4) proves (1). Taking one more logarithm gives

\[
\log\log g_{n+1}-\log\log g_n
=
\log\!\left(\frac{\log g_{n+1}}{\log g_n}\right)
\longrightarrow0,
\]

which is (2).

Conversely, for any increasing unbounded integer sequence `g_n`, condition (1) already implies the full first-passage property (4) for the set `{g_n}`. Indeed, if

\[
g_n\le X<g_{n+1},
\]

then its next point is `sigma(X)=g_(n+1)` and

\[
1<\frac{\log\sigma(X)}{\log X}
\le
\frac{\log g_{n+1}}{\log g_n}
\longrightarrow1.
\tag{5}
\]

Thus, as a statement about the geometry of the good set, `FD-081` is exactly a **vanishing-gap condition in the coordinate `log log H`**. It gives no bounded-gap statement in `log H`.

## 2. Vanishing log-log gaps force only a super-log-log counting law

From (2), Cesàro averaging gives

\[
\frac{u_n}{n}
=
\frac{u_1}{n}
+
\frac1n\sum_{j=1}^{n-1}(u_{j+1}-u_j)
\longrightarrow0.
\tag{6}
\]

Now let `g_n<=X<g_(n+1)`. Apart from an irrelevant finite initial offset,

\[
N_\eta(X)=n,
\]

while

\[
\log\log X<u_{n+1}=o(n).
\]

Therefore

\[
\frac{N_\eta(X)}{\log\log X}
\ge
\frac{n+O(1)}{u_{n+1}}
\longrightarrow\infty,
\]

which proves (3).

This bound is genuinely weaker than any fixed positive power of `log X`. The first-passage theorem says that occupied horizons cannot have a fixed positive gap in the `log log` coordinate; it does not supply positive density in the `log` coordinate used by the horizon-entropy obstruction of `FD-023`.

## 3. An explicit admissible good set remains superexponential in its index

Consider the abstract increasing integer sequence

\[
\boxed{
g_n:=\left\lceil\exp\!\bigl(\exp(\sqrt n)\bigr)\right\rceil.}
\tag{7}
\]

The ceiling is asymptotically negligible. One has

\[
\log g_n=\exp(\sqrt n)+o(1),
\]

and hence

\[
\frac{\log g_{n+1}}{\log g_n}
=
\exp(\sqrt{n+1}-\sqrt n)+o(1)
\longrightarrow1.
\tag{8}
\]

By (5), this set satisfies exactly the same subpower first-passage geometry as `FD-081`. Its counting function, however, obeys

\[
\boxed{
N(X)=(1+o(1))(\log\log X)^2.
}
\tag{9}
\]

In particular, for every fixed `a>0`,

\[
N(X)=o\!\bigl((\log X)^a\bigr).
\tag{10}
\]

At the same time its logarithmic horizon entropy in the sense of `FD-023` diverges:

\[
\boxed{
\frac1n\log\frac{g_n}{g_1}
\sim
\frac{e^{\sqrt n}}n
\longrightarrow\infty.
}
\tag{11}
\]

Thus `g_n` is superexponential in its index: for every fixed `L`, eventually `g_n>e^{Ln}`. This is exactly the qualitative escape regime that `FD-023` proves is necessary for Cesàro saturation by a polynomial-growth source. Therefore the new pointwise recurrence of `FD-081` does **not** contradict the old superexponential-sparsity escape; the two conditions are simultaneously realizable.

The sequence (7) is a control for the information content of the recurrence theorem. It is not asserted to be the actual Farey/Mertens occupied set. Its purpose is to falsify the implication

\[
\text{subpower first passage}
\Longrightarrow
\text{finite logarithmic horizon entropy}.
\]

## 4. Fixed-factor accumulation cannot change a power exponent from this input alone

Suppose, optimistically, that a downstream argument could extract a uniform favorable factor

\[
0<\kappa<1
\]

at every occupied horizon and multiply those gains across the retained sequence. After `N(X)` usable hits the accumulated factor would be

\[
\kappa^{N(X)}.
\tag{12}
\]

For the admissible recurrence geometry (7)--(9),

\[
\kappa^{N(X)}
=
\exp\!\left(-|\log\kappa|\,(1+o(1))(\log\log X)^2\right)
=
\boxed{X^{-o(1)}}.
\tag{13}
\]

For every fixed `delta>0`, this is eventually much larger than `X^(-delta)`. Hence even a favorable constant contraction at **every** power-syndetic hit is not enough, from the recurrence statement alone, to guarantee a fixed power saving.

This is the scale mismatch with the RH-facing zero-frontier problem. Moving a polynomial growth exponent requires a gain comparable to `delta log X` in logarithmic size. A bounded gain per good horizon requires

\[
N_\eta(X)\gg\log X
\tag{14}
\]

for that purpose, whereas `FD-081` guarantees only (3) and is compatible with (9).

The same observation explains why simply feeding the good horizons into `FD-023` does not close the loop. `FD-023` obtains a Cesàro obstruction when the sampled horizon entropy has a bounded subsequence; the model (7) satisfies the `FD-081` recurrence while its entropy tends to infinity, so the theorem's escape condition remains available.

## 5. Relation to the annular results

`FD-079` gives positive logarithmic recurrence of the **annular energy-weighted ratio**, and `FD-080` rules out fixed-power deserts for that annular ratio. Neither result automatically supplies a stronger count of distinct pointwise good horizons. The extraction in `FD-081` uses only positivity of the annular weights: one physical horizon can witness many overlapping power annuli, and no anti-concentration theorem for the horizon energies is presently available.

Thus the control above does not contradict `FD-079`. A sparse set satisfying (1) intersects every sufficiently late fixed-power window, so the same small collection of pointwise witnesses can in principle service a large family of overlapping annuli. Promoting annular logarithmic abundance to pointwise logarithmic abundance would require new information controlling how much annular energy a single horizon or a sparse cluster of horizons can carry.

This identifies three mathematically distinct ways past the obstruction. One may prove a genuinely stronger pointwise recurrence rate, strong enough to give at least logarithmically many usable scales; prove an anti-concentration theorem that converts annular energy recurrence into many distinct pointwise witnesses; or derive a gap-sensitive/nonlocal estimate whose gain grows with the scale interval and therefore does not pay only one bounded factor per occupied horizon.

## 6. Boundary and prior-art audit

The finding is an **information-sufficiency obstruction**, not a negative theorem about the actual physical set `G_eta`. It does not say that `N_eta(X)` is as small as `(log log X)^2`, that the physical good horizons have zero logarithmic density, or that a nonlocal Farey argument cannot use them. It proves only that none of those stronger conclusions follows from the subpower first-passage theorem presently available.

Likewise, the fixed-factor conclusion concerns proof architectures whose guaranteed logarithmic gain is bounded per occupied hit. A mechanism whose gain depends on the intervening gap, on the size of `E_(H,D)`, on correlations between several horizons, or on the bad intervals themselves is outside the obstruction.

No external theorem is load-bearing. Equations (1)--(6) are elementary sequence consequences of `FD-081`, while the comparison with superexponential index sparsity uses the exact horizon-entropy boundary already proved in `FD-023`. A targeted literature search around multiplicative/power syndeticity, sparse sequences, Farey discrepancy, and first-passage recurrence found standard notions of multiplicatively syndetic sets that impose a different bounded finite-multiplier condition, but no result needed by the argument here. No novelty claim is attached to the elementary sequence lemma, and `SOURCES.md` needs no new anchor.

The decisive falsification test is explicit: derive from the current `FD-081` hypotheses alone either `N_eta(X) \gg log X` or a bounded subsequence of `(1/n) log g_n`. The control (7) satisfies the exact first-passage condition while violating both conclusions, so any such strengthening must use additional physical arithmetic or energy-distribution information not present in `FD-081`.