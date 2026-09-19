# NB-226 — Fixed-power phase cancellation does not rescue sublinear Ford shells

**Date:** 2026-09-19  
**Status:** `DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + FIXED-POWER-PHASE-CANCELLATION + EXACT-FORD-SCALE + SUBLINEAR-LOG-SHELL + NB-225-SHARPENING + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-225` shows that, at exact Ford scale, the zero-population information used in `NB-223`--`NB-224` permits a completely phase-aligned near-one zero packet whenever the logarithmic source width satisfies `H=o(R)`. That result identifies phase information as one possible missing input, but leaves open how strong such information would actually have to be.

A generic square-root-cancellation heuristic is not enough. More generally, **no fixed positive power saving in the raw carrier phases is enough by itself**. For every fixed

\[
0<\vartheta<1,
\]

one can modify the `NB-225` matched packet so that every consecutive vertical subpacket of `m` zeros satisfies the deterministic cancellation law

\[
\left|
\sum_{j\in I} e^{iX(\gamma_j-t)}
\right|
\ll m^{\vartheta},
\tag{1}
\]

while the same packet remains compatible with the Vinogradov--Korobov zero-free depth, Bellotti's fixed and growing near-one density bounds, Bellotti's local disk count, and ordinary local zero counting, and its **weighted signed residue contribution remains bounded away from zero**.

For `\vartheta=1/2`, the packet therefore has square-root cancellation on every consecutive vertical interval and still produces an order-one moving-shell residue. The horizontal depth can be tuned so that its damping `e^{-X(1-\beta)}` exactly pays for the allowed phase discrepancy.

This is again a logical insufficiency statement, not a claim about the actual zeta zeros. It narrows the missing endpoint input: a phase theorem that is only of the form "raw phase sum is at most a fixed power of the local population" cannot close the sublinear-width Ford endpoint. What is needed is a genuinely **joint depth-phase estimate**, or a stronger cancellation law whose saving improves with the horizontal depth.

## 1. Exact-Ford setup and the packet budget

Keep the source geometry of `NB-225`. Fix `r>0` and a nonzero `phi>=0` in `C_c^infinity((0,1))`. For

\[
1\le H=H(X)\le C X
\]

put

\[
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\tag{2}
\]

with Fourier carrier

\[
L_{X,H}(v)
=e^{iXv}F(Hv),
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{3}
\]

As in `NB-223`--`NB-225`, write

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR.
\tag{4}
\]

Work along an exact-Ford sequence

\[
Y\longrightarrow Y_*\in(0,\infty)
\tag{5}
\]

and assume the shell is genuinely sublinear,

\[
\frac HR\longrightarrow0.
\tag{6}
\]

Set

\[
J=\frac RH\longrightarrow\infty,
\qquad
M=\left\lfloor\min\{J^{1/2},L\}\right\rfloor.
\tag{7}
\]

Then

\[
M\to\infty,
\qquad
\frac{M^2}{J}\le1,
\qquad
M\le L.
\tag{8}
\]

The first two conditions keep the entire packet inside an asymptotically flat part of the Fourier carrier. The third keeps its population far below Bellotti's growing near-one density allowance.

Fix once and for all

\[
0<\vartheta<1.
\tag{9}
\]

We will spend only `M^vartheta` of raw phase coherence instead of the full `M` coherence used by `NB-225`.

## 2. An elementary phase code with power cancellation on every interval

We first construct signs

\[
\epsilon_1,\ldots,\epsilon_M\in\{-1,+1\}
\]

such that the full sum has size `M^vartheta`, while every consecutive partial block obeys the same power law.

Let

\[
B=\left\lceil M^{1-\vartheta}\right\rceil
\tag{10}
\]

and start from the alternating sequence

\[
a_j=(-1)^j.
\]

Partition the first `floor(M/B)B` indices into consecutive blocks of length `B`. In every complete block choose one index at which `a_j=-1` and flip that sign to `+1`; leave every other sign unchanged. For sufficiently large `M`, `B>=2`, so every complete block contains such an index.

The alternating baseline has total sum `O(1)`. If

\[
F_M=\left\lfloor\frac MB\right\rfloor,
\]

then every flip increases the full sum by `2`, and therefore

\[
\sum_{j=1}^M\epsilon_j
=2F_M+O(1)
=2M^{\vartheta}(1+o(1)).
\tag{11}
\]

Now let `I` be any consecutive interval of `m` indices. The alternating part contributes at most `1` in absolute value. The interval intersects at most

\[
\frac mB+2
\]

of the distinguished flipped positions, so

\[
\left|\sum_{j\in I}\epsilon_j\right|
\le
1+2\left(\frac mB+2\right).
\tag{12}
\]

Because `m<=M` and `B>=M^(1-vartheta)`,

\[
\frac mB
\le
\frac{m}{M^{1-\vartheta}}
\le
m^{\vartheta}.
\tag{13}
\]

Hence, uniformly for every consecutive interval,

\[
\boxed{
\left|\sum_{j\in I}\epsilon_j\right|
\le 7m^{\vartheta}
}
\tag{14}
\]

for all sufficiently large `M` (the numerical constant is inessential).

Thus the same sign sequence has a deliberately nonzero global bias of order `M^vartheta` while satisfying fixed-power cancellation at **every vertical scale**.

## 3. Encode the phase code by a near-one zero packet

Choose an odd positive integer `q`, fixed independently of `X`. Construct a strictly increasing integer sequence `k_j` with

\[
(-1)^{k_j}=\epsilon_j
\tag{15}
\]

and increments in `{1,2}`. For example, choose `k_1` with the required parity and recursively put

\[
k_{j+1}-k_j
=
\begin{cases}
1,&\epsilon_{j+1}=-\epsilon_j,\\
2,&\epsilon_{j+1}=\epsilon_j.
\end{cases}
\tag{16}
\]

Then

\[
j\ll k_j\le 2j+O(1).
\tag{17}
\]

Define the common horizontal depth

\[
D=\frac{\vartheta\log M}{Y}
\tag{18}
\]

and the simple zero packet

\[
\rho_j
=
1-\frac DR
+i\left(t+\frac{\pi q k_j}{X}\right),
\qquad
1\le j\le M.
\tag{19}
\]

The moving-shell phase is exactly the prescribed sign:

\[
e^{iX(\gamma_j-t)}
=e^{i\pi q k_j}
=(-1)^{k_j}
=\epsilon_j,
\tag{20}
\]

because `q` is odd. Since the ordinates are strictly increasing, every vertical interval selects a consecutive set of indices. Equation (14) therefore becomes the genuine geometric cancellation law

\[
\boxed{
\left|
\sum_{\substack{j:\ \gamma_j\in I}}
e^{iX(\gamma_j-t)}
\right|
\ll
N_I^{\vartheta}
}
\tag{21}
\]

for every vertical interval `I`, where `N_I` is the number of packet points in that interval.

In particular `vartheta=1/2` gives square-root cancellation uniformly over all consecutive vertical subpackets.

## 4. Horizontal damping exactly compensates the allowed phase discrepancy

At every packet point,

\[
X(\sigma_X-\beta_j)
=r+\frac{XD}{R}
=r+YD
=r+\vartheta\log M.
\tag{22}
\]

Hence

\[
e^{-X(\sigma_X-\beta_j)}
=e^{-r}M^{-\vartheta}.
\tag{23}
\]

The profile `F(Hv)` is still asymptotically flat across the packet. Indeed, with

\[
v_j=(\gamma_j-t)+i(\sigma_X-\beta_j),
\]

we have from `k_j=O(M)`

\[
H|\gamma_j-t|
\ll
\frac{HM}{X}
=
\frac{M}{YJ},
\tag{24}
\]

and

\[
H(\sigma_X-\beta_j)
=
\frac{r}{YJ}+\frac DJ.
\tag{25}
\]

Both tend to zero uniformly. Since `F` is analytic near the origin,

\[
F(Hv_j)
=F(0)+O\!\left(\frac MJ+\frac DJ+\frac1J\right).
\tag{26}
\]

Using (20), (23), and (26),

\[
\begin{aligned}
\sum_{j=1}^M L_{X,H}(v_j)
&=
e^{-r}M^{-\vartheta}
\sum_{j=1}^M
\epsilon_j F(Hv_j)\\
&=
e^{-r}F(0)M^{-\vartheta}
\sum_{j=1}^M\epsilon_j
+E_X.
\end{aligned}
\tag{27}
\]

The error is genuinely negligible even though we no longer have full phase alignment. From (26),

\[
|E_X|
\ll
M^{-\vartheta}M
\left(\frac MJ+\frac DJ+\frac1J\right).
\tag{28}
\]

Because `M^2/J<=1`, the first term is at most `M^{-vartheta}`. Also

\[
\frac{M^{1-\vartheta}D}{J}
\le
\frac{D}{M^{1+\vartheta}}
=o(1),
\tag{29}
\]

since `D=O(log M)`, and the final term is smaller. Thus

\[
E_X=o(1).
\tag{30}
\]

Combining (11) and (27),

\[
\boxed{
\sum_{j=1}^{M} L_{X,H}(v_j)
=
2e^{-r}F(0)+o(1).
}
\tag{31}
\]

The coefficient `2` is an artifact of the simple sign construction and has no significance. The important point is that the signed residue contribution stays order one despite the uniform power cancellation (21).

The mechanism is exact: the allowed global phase bias is `M^vartheta`, while the chosen horizontal depth contributes precisely the reciprocal factor `M^(-vartheta)`.

## 5. The packet still satisfies the population constraints of NB-225

The phase modification does not consume any of the population budget used in `NB-225`.

First,

\[
D=\frac{\vartheta\log M}{Y}\to\infty,
\tag{32}
\]

so the packet lies safely to the left of every fixed Vinogradov--Korobov zero-free depth `A_0/R` for sufficiently large `X`. It also eventually contributes no zeros to any fixed-depth near-one count.

Second, because `M<=L`,

\[
D=O(\log L)=o(L^\alpha)
\tag{33}
\]

for every fixed `alpha>0`. Bellotti's growing near-one density theorem permits exponentially more than `M` points at such depths, exactly as in `NB-225`.

Third, (16) gives vertical spacings

\[
\gamma_{j+1}-\gamma_j
\in
\left\{
\frac{\pi q}{X},
\frac{2\pi q}{X}
\right\}
\asymp_{Y_*,q}\frac1R.
\tag{34}
\]

A disk of radius `K/R` centered on the `1`-line therefore meets at most `O_{Y_*,q}(K)` packet points once its horizontal radius reaches the common depth `D/R`; smaller disks miss the packet. Taking `q` sufficiently large, if needed, makes this compatible with the fixed implied constant in Bellotti's local `O(K)` law.

Finally,

\[
M\le L=o(Q),
\tag{35}
\]

so ordinary unit-interval zero counting also leaves ample room. As in `NB-225`, one may complete the packet by conjugate and functional-equation-reflected partners. The conjugate packet is remote from `+t`, while the reflected near-zero-real-part packet receives exponentially small moving-shell weight. These symmetries therefore do not change (31).

Thus the new packet satisfies the same population-only admissibility checks as `NB-225` while carrying a much stronger internal phase-cancellation property.

## 6. What kind of phase theorem is actually ruled out

The conclusion is deliberately narrower than "phase information cannot help". Phase information can help, but a fixed population-power estimate does not suffice by itself.

Suppose an endpoint argument knows only that every relevant vertical subpacket `I` obeys, for some fixed `vartheta>0`,

\[
\left|
\sum_{\rho\in I}
e^{iX(\gamma-t)}
\right|
\ll
N_I^{\vartheta},
\tag{36}
\]

in addition to the population hypotheses already audited in `NB-225`. The packet above satisfies (36), yet its smoothed signed residue remains order one. Therefore those hypotheses cannot force the desired `o(1)` carrier bound for every sublinear `H=o(R)`.

The square-root case

\[
\vartheta=\frac12
\tag{37}
\]

is especially instructive. A random-phase heuristic would naturally suggest `sqrt(N)` cancellation, but at horizontal depth

\[
R(1-\beta)
=\frac{\log M}{2Y},
\tag{38}
\]

the Ford carrier damps each zero by exactly `M^(-1/2)`. A `sqrt(M)` residual phase bias therefore survives at constant size.

More generally, at depth `D` the natural quantity that must be small is not the raw phase sum alone but

\[
e^{-YD}
\left|
\sum_{\rho\ \text{at depth }D}
e^{iX(\gamma-t)}
\right|.
\tag{39}
\]

To beat the matched construction, a theorem must make (39) `o(1)` uniformly in the coupled depth/window regime, or exclude the required population there. Equivalently, phase cancellation has to improve with horizontal depth strongly enough that the permitted phase bias is `o(e^{YD})` on the packets allowed by the population estimates.

This leaves several genuine escape routes: a joint depth-window density theorem, a depth-sensitive exponential-sum estimate over actual near-one zeros, cancellation for the **weighted** residue coefficients rather than their raw phases, or an arithmetic correlation theorem that couples horizontal and vertical zero locations. The finding does not obstruct any of those stronger inputs.

It also does not address a theorem with bounded or subpower discrepancy in a regime where the corresponding horizontal depth no longer tends to infinity; the construction here requires a fixed `vartheta>0` so that `D->infinity` and the packet evades fixed-depth near-one bounds.

## 7. Prior-art and novelty boundary

The sign sequence in Section 2 is elementary discrepancy bookkeeping; no novelty is claimed for constructing deterministic signs with controlled interval sums. Likewise, Bellotti's zero-free/density/local-count inputs and the smoothed explicit-formula carrier are inherited from `NB-223`--`NB-225` and are already anchored in `SOURCES.md`.

A targeted literature audit also checked neighboring work on zero-ordinate exponential sums, pair correlation, and recent inverse theorems connecting large Dirichlet/zeta sums to local zero populations. In particular, Dong, Wang, Wang and Zhang, *Large zeta sums and zeros of the Riemann zeta function* (arXiv:2608.31060, 2026), proves a recent inverse relation from unusually large sums `sum_(n<=x) n^(it)` to many zeros near height `t`. Work on exponential sums over zero ordinates and pair correlation instead concerns broad/statistical zero sets, frequently near the critical line. None of these results supplies the pointwise, near-one, depth-sensitive cancellation estimate required to invalidate the packet above.

The line-local contribution is the matched-control deduction (31)--(39): **horizontal damping can be tuned to neutralize any prescribed fixed positive power of raw vertical phase cancellation while all current population constraints remain satisfied**. This strengthens the information boundary of `NB-225`; it is not a new theorem about the actual zeta zero set.

No new external theorem is load-bearing in the derivation, so `SOURCES.md` requires no new anchor for this finding.

## 8. Boundary conditions and route consequence

The construction relies on four explicit conditions: exact-Ford coupling `Y->Y_* in (0,infinity)`, genuinely sublinear source width `H/R->0`, a fixed exponent `0<vartheta<1`, and a positive one-sided smooth shell with `F(0)>0`. The choice `M<=sqrt(J)` is conservative and exists only to make the carrier-profile error in (28) vanish without optimizing constants.

The conclusion remains source-side. Even a future theorem that eliminates every such zero packet for actual `zeta` would still need a separate destination bridge showing that the relevant positive Euler-return observable constrains the finite Nyman--Beurling approximation distance.

Within the source-side endpoint route, however, the next target is sharper than after `NB-225`. It is not enough to ask for "some phase cancellation" or even for square-root cancellation of raw zero phases. A useful theorem must couple cancellation to the **horizontal zero depth and the moving `1/H` window**, or directly estimate the weighted residue sum before the horizontal damping and vertical phases are separated.

Thus `NB-224`--`NB-226` give the following hierarchy at exact Ford scale:

\[
\boxed{
\begin{array}{c}
H=\Theta(X):\ \text{current local population bounds force a positive gap},\\[2mm]
H=o(X):\ \text{population bounds alone admit an order-one packet},\\[2mm]
H=o(X):\ \text{even fixed-power raw phase cancellation still admits one}.
\end{array}
}
\tag{40}
\]

The remaining endpoint problem is therefore genuinely joint: **depth, vertical window, phase, and residue weight have to be controlled in one estimate.**