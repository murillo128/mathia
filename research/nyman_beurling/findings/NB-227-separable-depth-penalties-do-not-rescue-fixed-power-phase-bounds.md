# NB-227 — Separable depth penalties do not rescue fixed-power phase bounds

**Date:** 2026-09-19  
**Status:** `DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + DEPTH-PHASE-SEPARABILITY-NO-GO + FIXED-POWER-POPULATION + EXACT-FORD-SCALE + SUBLINEAR-LOG-SHELL + NB-226-SHARPENING + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-226` shows that a fixed power saving in the raw vertical phases does not control the exact-Ford endpoint for a genuinely sublinear source width. Its matched packet chooses the horizontal zero depth so that the Ford damping exactly compensates the permitted `M^vartheta` phase bias.

A natural repair is to make the phase theorem stronger as zeros move left. This finding shows that a very broad version of that repair still does not suffice: **an arbitrary predetermined depth-only penalty multiplying a fixed population power can always be tuned away by letting the matched packet move left sufficiently slowly**.

More precisely, fix

\[
0<\vartheta<1
\]

and any function

\[
\mathcal Q:\mathbb N\to[1,\infty)
\]

that is finite at every fixed integer depth. Suppose the additional phase information available at common normalized depth `D` has the separable form

\[
\left|
\sum_{j\in I} e^{iX(\gamma_j-t)}
\right|
\ll
1+\frac{|I|^{\vartheta}}{\mathcal Q(D)}
\tag{1}
\]

for every consecutive vertical subpacket `I`. The additive `1` is unavoidable for an unweighted raw phase estimate because a singleton phase has modulus one.

Then, within the same abstract zero-packet model audited in `NB-225`--`NB-226`, one can choose a depth `D=D(X)\to\infty` and a packet satisfying (1) at every vertical scale while its residue-weighted moving-shell contribution remains bounded away from zero. The conclusion holds no matter how rapidly the fixed function `\mathcal Q(D)` grows.

Thus **depth sensitivity is not enough if it factorizes from a fixed positive population power**. To defeat the matched control, the missing theorem must couple population and depth nonseparably, exclude the required population at the chosen depth, or control the actual residue-weighted sum directly.

This is a logical insufficiency statement about the audited information package, not a construction of actual zeta zeros.

## 1. Exact-Ford setup inherited from NB-226

Keep the notation and source geometry of `NB-226`. Let

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR,
\tag{2}
\]

along a sequence with

\[
Y\longrightarrow Y_*\in(0,\infty).
\tag{3}
\]

Let the logarithmic source width satisfy

\[
H=o(R),
\qquad
J=\frac RH\longrightarrow\infty,
\tag{4}
\]

and take the same slowly growing packet population

\[
M=\left\lfloor\min\{J^{1/2},L\}\right\rfloor.
\tag{5}
\]

Hence

\[
M\to\infty,
\qquad
\frac{M^2}{J}\le1,
\qquad
M\le L.
\tag{6}
\]

For the smooth shell profile used there,

\[
L_{X,H}(v)=e^{iXv}F(Hv),
\tag{7}
\]

and a zero at normalized horizontal depth

\[
D=R(1-\beta)
\tag{8}
\]

contributes the common damping factor `e^(-YD)` up to the fixed `e^(-r)` coming from the source line. Across a packet of `M` ordinates spaced at scale `1/X`, the profile remains flat whenever `M/J->0` and `D/J->0`.

`NB-225` and `NB-226` already audit the zero-free, density, local-disk and ordinary local-count budgets for packets in this regime. The only new question is whether an arbitrary depth-only strengthening of the phase bound blocks their matched control.

## 2. A diagonal depth can outrun every fixed depth-only penalty

Because `Y->Y_*>0`, choose constants

\[
0<Y_-<Y_*<Y_+<\infty
\tag{9}
\]

such that eventually

\[
Y_-\le Y\le Y_+.
\tag{10}
\]

For the prescribed function `\mathcal Q`, define `D=D_M` to be the largest positive integer `d` satisfying

\[
d\le\log\log M
\tag{11}
\]

and

\[
\mathcal Q(d)e^{Y_+d}
\le
M^{\vartheta/2}.
\tag{12}
\]

For every fixed integer `d`, the left side of (12) is a fixed finite number while `M^(vartheta/2)->infinity`. Thus every fixed `d` is eventually admissible, and consequently

\[
\boxed{D_M\to\infty.}
\tag{13}
\]

At the same time,

\[
D_M\le\log\log M=o(\log M),
\tag{14}
\]

and, using `Y<=Y_+`,

\[
\boxed{
\mathcal Q(D_M)e^{YD_M}
\le
M^{\vartheta/2}.
}
\tag{15}
\]

This elementary diagonal step is the key point. No fixed function of depth alone, however fast it grows, can force a useful penalty uniformly over **all** depths tending to infinity: the packet can always let its depth diverge more slowly than the penalty scale becomes effective relative to the available population.

## 3. Build a phase code with exactly the required tiny bias

Put

\[
F_M=\left\lfloor\frac12 e^{YD}\right\rfloor,
\qquad
B_M=2F_M.
\tag{16}
\]

Since `D->infinity` and `Y>=Y_->0`,

\[
B_M\sim e^{YD}\to\infty.
\tag{17}
\]

Equation (15) and `\mathcal Q(D)>=1` also give

\[
B_M\ll M^{\vartheta/2}=o(M).
\tag{18}
\]

Start from the alternating signs `a_j=(-1)^j`. Divide the index interval `{1,...,M}` into `F_M` consecutive blocks of lengths differing by at most one. Because `M/F_M->infinity`, every block contains an index at which `a_j=-1` for all sufficiently large `M`. Flip exactly one such negative sign to `+1` in each block, and call the resulting sequence

\[
\epsilon_1,\ldots,\epsilon_M\in\{-1,+1\}.
\]

The alternating baseline has total sum `O(1)`, while each flip adds two. Therefore

\[
\boxed{
\sum_{j=1}^{M}\epsilon_j
=B_M+O(1)
\sim e^{YD}.
}
\tag{19}
\]

Now let `I` be any consecutive interval containing `m` indices. Its alternating contribution has modulus at most one. Because the flipped positions are distributed one per nearly equal block, `I` meets at most

\[
O\!\left(1+\frac{mF_M}{M}\right)
\]

flipped positions. Hence

\[
\left|\sum_{j\in I}\epsilon_j\right|
\ll
1+\frac{mB_M}{M}.
\tag{20}
\]

From (15)--(18), for sufficiently large `M`,

\[
B_M\mathcal Q(D)\le M^{\vartheta}.
\tag{21}
\]

Therefore, for every `1<=m<=M`,

\[
\frac{mB_M}{M}
\le
\frac{m^{\vartheta}}{\mathcal Q(D)},
\tag{22}
\]

because (21) implies

\[
\frac{mB_M\mathcal Q(D)}{M}
\le
m\,M^{\vartheta-1}
\le
m^{\vartheta}.
\]

Combining (20) and (22),

\[
\boxed{
\left|\sum_{j\in I}\epsilon_j\right|
\ll
1+\frac{m^{\vartheta}}{\mathcal Q(D)}
}
\tag{23}
\]

uniformly over **every** consecutive interval.

The full packet nevertheless retains the deliberately chosen bias `~e^(YD)` needed to cancel the horizontal damping.

## 4. Encode the signs by ordinates without changing the packet budgets

As in `NB-226`, choose a fixed odd positive integer `q`. Construct strictly increasing integers `k_j` with

\[
(-1)^{k_j}=\epsilon_j,
\qquad
k_{j+1}-k_j\in\{1,2\}.
\tag{24}
\]

Define

\[
\rho_j
=
1-\frac DR
+i\left(t+\frac{\pi q k_j}{X}\right),
\qquad
1\le j\le M.
\tag{25}
\]

Then

\[
e^{iX(\gamma_j-t)}
=e^{i\pi qk_j}
=\epsilon_j,
\tag{26}
\]

and the ordinates are increasing. Every vertical interval therefore picks a consecutive index set, so (23) becomes

\[
\boxed{
\left|
\sum_{\substack{j:\gamma_j\in I}}
e^{iX(\gamma_j-t)}
\right|
\ll
1+\frac{N_I^{\vartheta}}{\mathcal Q(D)}
}
\tag{27}
\]

for every vertical interval `I` intersecting the packet.

The spacing remains

\[
\gamma_{j+1}-\gamma_j
\asymp_q\frac1X
\asymp_{Y_*}\frac1R,
\tag{28}
\]

and the complete vertical span is `O(M/X)`. Thus introducing the depth penalty has not consumed additional vertical room relative to `NB-226`.

## 5. The weighted residue still remains order one

For

\[
v_j=(\gamma_j-t)+i(\sigma_X-\beta_j),
\]

the same calculation as in `NB-226` gives

\[
H|\gamma_j-t|
\ll
\frac{M}{YJ},
\qquad
H(\sigma_X-\beta_j)
=
O\!\left(\frac1J+\frac DJ\right).
\tag{29}
\]

Since `M/J->0` and `D<=log log M`, the Fourier profile is uniformly flat:

\[
F(Hv_j)
=
F(0)+O\!\left(\frac MJ+\frac DJ+\frac1J\right).
\tag{30}
\]

The common exponential factor is

\[
e^{-X(\sigma_X-\beta_j)}
=e^{-r}e^{-YD}.
\tag{31}
\]

Therefore

\[
\begin{aligned}
\sum_{j=1}^{M}L_{X,H}(v_j)
&=
e^{-r}e^{-YD}
\sum_{j=1}^{M}\epsilon_jF(Hv_j)\\
&=
e^{-r}F(0)e^{-YD}(B_M+O(1))+E_X.
\end{aligned}
\tag{32}
\]

By (17),

\[
e^{-YD}B_M\longrightarrow1.
\tag{33}
\]

For the profile error,

\[
|E_X|
\ll
e^{-YD}M
\left(
\frac MJ+\frac DJ+\frac1J
\right).
\tag{34}
\]

Since `e^(-YD)~1/B_M` and `M^2/J<=1`,

\[
\frac{M^2}{B_MJ}\le\frac1{B_M}\to0.
\tag{35}
\]

Also `M/J<=1/M`, so

\[
\frac{MD}{B_MJ}
\le
\frac{D}{B_MM}	o0,
\qquad
\frac{M}{B_MJ}\to0.
\tag{36}
\]

Thus `E_X=o(1)` and

\[
\boxed{
\sum_{j=1}^{M}L_{X,H}(v_j)
=
e^{-r}F(0)+o(1).
}
\tag{37}
\]

The depth-sensitive raw phase envelope (27) is therefore fully compatible with an order-one weighted residue packet.

## 6. All population and zero-free checks remain inside the NB-225 budget

The new diagonal depth is deliberately much smaller than the depth used in the explicit `NB-226` power-matching construction:

\[
D\le\log\log M.
\tag{38}
\]

Nevertheless `D->infinity`, so the packet eventually lies to the left of every fixed normalized Vinogradov--Korobov zero-free depth. It also eventually disappears from every fixed-depth near-one count.

Because `M<=L`,

\[
D\le\log\log M=o(L^\alpha)
\tag{39}
\]

for every fixed `alpha>0`. The growing-depth density allowance used in `NB-225` and `NB-226` therefore remains vastly larger than this packet population. The spacing (28) satisfies the same local disk count after choosing the fixed odd `q` sufficiently large, and `M<=L=o(Q)` remains far below ordinary unit-interval zero counts.

Carrier flatness is actually easier than before: (35)--(36) show that the extra factor `e^(-YD)` makes the total profile error vanish even when the global raw bias grows only as slowly as the chosen depth permits.

Consequently the packet is admissible under **all the same population-only controls already audited in NB-225--NB-226**, plus the stronger separable depth-sensitive phase hypothesis (27).

## 7. What this rules out, and what it does not

The no-go concerns a specific but broad architecture. If a raw phase theorem has the form

\[
\text{fixed population power}
\times
\text{predetermined depth-only improvement},
\]

then the two factors remain independently tunable. The packet can choose `D->infinity` so slowly that the depth penalty has not yet overwhelmed the available `M^vartheta` population allowance, and then choose a raw bias of size `e^(YD)` that survives the residue damping.

Equivalently, a separable estimate of the schematic form

\[
\left|\sum e^{i\phi_j}\right|
\lesssim
1+\frac{M^{\vartheta}}{\mathcal Q(D)}
\tag{40}
\]

can only force the weighted contribution small at depth `D` if

\[
\frac{M^{\vartheta}}{\mathcal Q(D)}
=o(e^{YD})
\tag{41}
\]

uniformly throughout the admissible coupled population-depth regime. No fixed function `\mathcal Q(D)` can guarantee (41) for every slowly diverging `D=D(M)`.

This does **not** say that every depth-sensitive theorem is insufficient. The construction does not defeat, for example:

- a genuinely nonseparable estimate whose effective population exponent or admissible population changes with depth;
- a joint depth-window density theorem that removes the `M` points before the phase estimate is applied;
- a theorem constraining nested depth slabs simultaneously rather than only the common-depth packet at its own depth;
- cancellation for the actual residue weights, where horizontal damping and vertical phase are controlled in one quantity;
- additional arithmetic correlations of genuine zeta zeros not encoded by the population bounds.

Those are precisely the types of inputs that evade the diagonal freedom used here.

## 8. Representation and generality audit

The obstruction is not specifically a theorem about zeta-zero statistics. Abstractly, it uses only four ingredients:

1. a packet population `M->infinity` that may grow arbitrarily slowly;
2. a depth variable `D->infinity` whose admissibility still permits such slow growth;
3. multiplicative attenuation `e^(-YD)` with `Y` bounded above and below away from zero;
4. a raw phase envelope with a fixed positive population power and a separable depth-only penalty.

Any residue-packet model with those features admits the same diagonal matched control. The zeta-specific content enters through `NB-225`--`NB-226`, which verify that the exact-Ford sublinear-shell model leaves precisely this population/depth freedom under the currently stored zero-free, density and local-count inputs.

This generality is useful as a control. The finding should **not** be interpreted as evidence that actual zeta zeros realize the constructed signs or common depth. It proves only that the listed information cannot logically exclude such a configuration. Any successful endpoint theorem must use information absent from this ambient model.

## 9. Prior-art and novelty audit

A literature search around exponential sums over ordinates of zeta zeros, phase distribution and weighted zero sums finds substantial classical and modern work on zero-ordinate distribution and exponential-sum estimates. None of that literature is used as a new load-bearing input here. The mathematical statement proved above is an elementary matched-control consequence of the packet freedom already established and source-audited in `NB-225`--`NB-226`.

Accordingly, no theorem-priority claim is made and `SOURCES.md` needs no new anchor. The substantive delta is internal and methodological: `NB-226` ruled out depth-independent fixed-power cancellation, while the present result shows that **even an arbitrarily strong fixed depth-only multiplier does not repair a fixed population power**. The missing information has to couple the two currencies rather than improve them separately.

## 10. Consequence for the live source-side frontier

The phrase "depth-sensitive phase estimate" after `NB-226` was still too broad. A theorem of the form

\[
M^{\vartheta}/\mathcal Q(D)
\]

with fixed `vartheta>0` does not cross the sublinear Ford boundary, irrespective of the growth rate of the predetermined `\mathcal Q`.

The live target can therefore be sharpened to a **uniform joint population-depth estimate** for the actual near-one zeros, or directly for their residue-weighted carrier sum. A useful theorem must remove the diagonal escape `D=D(M)->infinity` exhibited above. In particular, it must force the available phase bias to be `o(e^(YD))` uniformly over every depth/population pair still allowed by the zero-density and local-count information.

This remains source-side. It neither proves a new Nyman--Beurling distance estimate nor supplies the still-missing bridge showing that every good destination approximant must realize this positive Euler/zero-carrier observable.