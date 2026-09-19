# NB-228 — Nested depth phase sums are the Abel dual of Ford residue damping

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + CANDIDATE-MECHANISM + ZETA-SPECTRAL-MATCHED-CONTROL + NESTED-DEPTH-PHASE + ABEL-LAPLACE-DUALITY + EXACT-FORD-SCALE + SUBLINEAR-LOG-SHELL + NB-225/NB-227-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-225`--`NB-227` isolate the exact-Ford obstruction for a genuinely sublinear logarithmic shell. Population bounds alone permit an order-one phase-aligned zero packet, a fixed-power raw phase estimate does not remove it, and even multiplying that estimate by an arbitrarily strong predetermined depth-only penalty can be defeated by letting the packet depth diverge sufficiently slowly.

Those negative results leave one qualitatively different escape: constrain **all nested horizontal depth slabs simultaneously**, rather than assign an independent phase allowance at each chosen depth. This finding makes that escape exact.

For the actual moving-shell residue carrier, exponential Ford damping in the normalized zero depth is the Laplace dual of a cumulative depth-phase sum. If the cumulative carrier phase has exponential type strictly below the Ford damping rate, the deep residue tail is forced small; if it reaches the critical type, the matched packets of `NB-225`--`NB-227` survive with order-one mass. Thus the missing joint theorem has a sharp target: it must make the nested cumulative carrier subcritical relative to `e^(Y D)`, not merely improve population and depth by separable factors.

No such zeta theorem is proved here. The result is an exact reduction and a sharp matched-control threshold for the surviving source-side route.

## 1. Keep the full source-faithful residue coefficient

Use the notation of `NB-224`--`NB-227`. Let

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR,
\tag{1}
\]

and work on an exact-Ford sequence

\[
Y\longrightarrow Y_*\in(0,\infty).
\tag{2}
\]

Fix `r>0`, put

\[
\sigma_X=1+\frac rX,
\tag{3}
\]

and let the logarithmic source shell be

\[
h_{X,H}(u)
=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\qquad
1\le H\le C X,
\tag{4}
\]

with nonzero `phi in C_c^infinity((0,1))`. Its Fourier carrier is

\[
L_{X,H}(v)
=e^{iXv}F(Hv),
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{5}
\]

For a nontrivial zero

\[
\rho=\beta+i\gamma
\]

of multiplicity `m(rho)`, define its normalized horizontal depth

\[
d_\rho:=R(1-\beta)
\in(0,R),
\tag{6}
\]

and the carrier argument

\[
v_\rho
=(\gamma-t)+i(\sigma_X-\beta).
\tag{7}
\]

Then the moving-shell residue factor splits **exactly** as

\[
\begin{aligned}
L_{X,H}(v_\rho)
&=
 e^{iX(\gamma-t)}
 e^{-X(\sigma_X-\beta)}
 F(Hv_\rho)\\
&=
 e^{-r}
 e^{-Yd_\rho}
 e^{iX(\gamma-t)}
 F(Hv_\rho).
\end{aligned}
\tag{8}
\]

The point of keeping `F(Hv_rho)` inside the phase coefficient is that no absolute-value decoupling and no flat-carrier approximation is being made. Define

\[
b_\rho
:=
m(\rho)
 e^{iX(\gamma-t)}
 F(Hv_\rho).
\tag{9}
\]

The signed nontrivial-zero carrier is therefore

\[
\mathcal Z_{X,H}(t)
:=
\sum_\rho m(\rho)L_{X,H}(v_\rho)
=
 e^{-r}
\sum_\rho e^{-Yd_\rho}b_\rho.
\tag{10}
\]

For `Im z>=0`, repeated integration by parts in (5) gives

\[
|F(z)|\ll_{A,\phi}(1+|z|)^{-A}
\tag{11}
\]

for every fixed `A`. Together with the ordinary local zero count this makes the sums below absolutely convergent after vertical localization, and the full identity follows by taking the localization limit. One can alternatively read every formula first for a finite zero packet, where no convergence issue occurs.

## 2. Abel summation turns the residue sum into one nested-depth observable

Define the cumulative depth-phase carrier

\[
\boxed{
\mathcal C_{X,H,t}(D)
:=
\sum_{\rho:\ d_\rho\le D} b_\rho,
\qquad
0\le D\le R.
}
\tag{12}
\]

This quantity is deliberately **nested**: increasing `D` retains all shallower zeros and adds the next horizontal slab. It simultaneously remembers population, vertical phase and the actual shell profile.

Apply Stieltjes integration by parts to the discrete measure

\[
d\mathcal C
=\sum_\rho b_\rho\,\delta_{d_\rho}.
\]

Since `YR=X`, one obtains the exact identity

\[
\boxed{
\mathcal Z_{X,H}(t)
=
 e^{-r}
\left[
 e^{-X}\mathcal C_{X,H,t}(R)
+
Y\int_0^R
 e^{-YD}\mathcal C_{X,H,t}(D)\,dD
\right].
}
\tag{13}
\]

This is the missing coupling in its most economical form. Ford damping does not ask for an independent phase theorem at each depth; it tests the **Laplace transform of the cumulative phase process**.

The endpoint in (13) is harmless at the exact Ford scale. From (11) and the classical `O(log(2+|u|))` zero count in unit ordinate intervals,

\[
|\mathcal C_{X,H,t}(R)|
\ll_{A,\phi} 1+Q
\tag{14}
\]

for `H>=1`, after enlarging the constant to cover bounded ordinates. Hence

\[
e^{-X}\mathcal C_{X,H,t}(R)=o(1).
\tag{15}
\]

Consequently

\[
\boxed{
\mathcal Z_{X,H}(t)
=
 e^{-r}Y
\int_0^R
 e^{-YD}\mathcal C_{X,H,t}(D)\,dD
+o(1).
}
\tag{16}
\]

In particular, the source-faithful quantity

\[
\|\mathcal C\|_{Y,1}
:=
Y\int_0^R
 e^{-YD}|\mathcal C(D)|\,dD
\tag{17}
\]

is an exact sufficient currency for the signed residue carrier:

\[
|\mathcal Z_{X,H}(t)|
\le
 e^{-r}\|\mathcal C\|_{Y,1}+o(1).
\tag{18}
\]

Conversely, an order-one residue contribution forces

\[
\|\mathcal C\|_{Y,1}\gg 1.
\tag{19}
\]

Thus any surviving matched control must create order-one exponentially weighted `L^1` mass in the nested cumulative phase process. This is stronger information than a large phase sum at one arbitrarily selected depth.

## 3. A subcritical depth exponent kills the Ford tail

The identity gives a simple quantitative target. Let `D_0>=0`, and define the cumulative carrier of the tail beginning at `D_0`,

\[
\mathcal C_{D_0}(D)
:=
\sum_{\rho:\ D_0\le d_\rho\le D}b_\rho,
\qquad D\ge D_0.
\tag{20}
\]

Suppose that for some `0<delta<1` and some amplitude `A_X>=0`, uniformly for `D_0<=D<=R`,

\[
\boxed{
|\mathcal C_{D_0}(D)|
\le
A_X
\exp\!\left((1-\delta)YD\right).
}
\tag{21}
\]

Applying (13) to the restricted depth measure gives

\[
\begin{aligned}
\left|
\sum_{\rho:\ d_\rho\ge D_0}
 m(\rho)L_{X,H}(v_\rho)
\right|
&\le
 e^{-r}
\left[
 e^{-X}|\mathcal C_{D_0}(R)|
+
Y\int_{D_0}^R
 e^{-YD}|\mathcal C_{D_0}(D)|\,dD
\right]\\
&\le
 e^{-r}A_X
\left[
 e^{-\delta X}
+
\frac1\delta e^{-\delta YD_0}
\right].
\end{aligned}
\tag{22}
\]

Hence

\[
\boxed{
\text{nested exponential type }<(Y)
\quad\Longrightarrow\quad
\text{deep residue tail decays like }e^{-\delta YD_0}.
}
\tag{23}
\]

This is qualitatively different from the separable bound ruled out by `NB-227`. There the packet is allowed a population power `M^vartheta` and can choose `D=D(M)` so slowly that any fixed depth-only penalty has not yet consumed that power. Under (21), increasing `D` directly tightens the **same cumulative quantity that Ford damping integrates**. There is no independent population currency left to retune.

A useful special case starts at the local Vinogradov--Korobov zero-free depth. For zeros whose ordinates are comparable with `t`, write

\[
d_\rho\ge a_0>0
\tag{24}
\]

for the fixed normalized zero-free constant. The remote ordinate tail is already negligible by (11). If one could prove, for fixed `A` and `delta>0`,

\[
|\mathcal C(D)|
\le
A e^{(1-\delta)YD}
\qquad
(a_0\le D\le R),
\tag{25}
\]

then

\[
\boxed{
|\mathcal Z_{X,H}(t)|
\le
 e^{-r}\frac{A}{\delta}
 e^{-\delta Ya_0}
+o(1).
}
\tag{26}
\]

Within the exact-Ford family, taking the fixed ratio `Y=X/R` sufficiently large would therefore make the signed residue carrier smaller than any prescribed positive constant. Since the positive Euler shell has order-one mass, the explicit-formula route would then recover a constant positive return gap at the exact Ford denominator even when `H=o(R)`.

Equation (25) is not claimed as known. It is a precise sufficient joint population-depth-phase theorem whose strength can now be compared directly with candidate zero statistics.

## 4. The exponent `Y` is sharp for the matched-control obstruction

The threshold in (21) cannot be relaxed to the critical exponential type. The common-depth packet constructed in `NB-227` makes this exact.

That packet places `M` zeros at one normalized depth `D=D_M->infinity`, keeps the shell profile flat, and arranges a total raw phase bias

\[
B_M\sim e^{YD}.
\tag{27}
\]

For the full carrier coefficients (9), flatness gives

\[
\sum_{j=1}^M b_{\rho_j}
=
F(0)B_M+o(e^{YD}).
\tag{28}
\]

Its cumulative process is therefore

\[
\mathcal C(D')
=
\begin{cases}
0,&D'<D,\\
F(0)e^{YD}(1+o(1)),&D'\ge D,
\end{cases}
\tag{29}
\]

up to the end of the packet model. Substitution into (16) gives

\[
Y\int_D^R
 e^{-YD'}\mathcal C(D')\,dD'
=
F(0)+o(1),
\tag{30}
\]

which is exactly the order-one residue already obtained in `NB-227`.

Thus the matched packet sits on the boundary

\[
\boxed{
|\mathcal C(D)|\asymp e^{YD}.
}
\tag{31}
\]

Any nested-depth theorem that still permits critical-type excursions of this size cannot exclude the packet. A fixed relative saving in the exponent, as in `(1-delta)Y`, does exclude it. In this matched-control sense, **`Y` is the sharp cumulative-depth phase exponent**.

This also clarifies why a theorem about each common-depth slice separately is structurally weaker. The residue is not the sum of independently priced slices after absolute values; it is the Laplace transform of their cumulative signed interaction. The correct joint object is therefore `C(D)`, not a collection of unrelated per-depth discrepancy caps.

## 5. Relation to Landau--Gonek zero sums

There is classical neighboring prior art, but it does not supply (25). If one drops the shell profile `F(Hv_rho)`, then

\[
e^{-YD_\rho}e^{iX(\gamma-t)}
=
e^{-X}e^{-iXt}e^{X\rho}.
\tag{32}
\]

Thus the unprofiled Ford residue phase is a translated and normalized version of the classical Landau--Gonek zero sum `sum x^rho` with `x=e^X`. Landau's formula and Gonek's uniform refinements exploit exactly this zero/prime duality.

The live object here is different in two decisive ways. First, it is localized around a moving high ordinate by `F(Hv_rho)`. Second, the cumulative process (12) truncates zeros by **horizontal depth** `R(1-beta)` while retaining their vertical phases. The standard Landau--Gonek formulas sum by ordinate and, through the explicit formula, expose the corresponding prime-side arithmetic; they do not provide a source-independent estimate of the form (25) for this moving depth-truncated carrier.

The closest classical boundary is S. M. Gonek, *An explicit formula of Landau and its applications to the theory of the zeta-function*, Contemporary Mathematics 143 (1993), 395--413. A recent extension is B. Durkan, C. Hughes and A. Pearce-Crump, *Generalisations of the Landau--Gonek Theorem and applications to mean values of zeta*, arXiv:2601.18025 (2026). These works are prior-art context rather than load-bearing inputs to (13)--(31), which use only the already-established shell carrier and elementary Stieltjes summation. Accordingly `SOURCES.md` needs no new dependency anchor in this pass.

This comparison is also a circularity warning. Proving (25) by simply applying an explicit formula that reintroduces the same Euler shell would not create new information. A useful theorem must control the nested zero statistic independently enough to constrain the source-side return rather than merely restate it.

## 6. Representation and falsification audit

The Abel identity itself is generic. For any discrete complex measure

\[
\mu=\sum_j c_j\delta_{d_j}
\]

on a bounded positive depth interval, exponential weighting is the Laplace transform of its cumulative function. What is zeta-specific is the exact identification

\[
d_\rho=R(1-\beta),
\qquad
Y=X/R,
\tag{33}
\]

and the carrier coefficient (9) inherited from the smoothed logarithmic Euler shell.

Several boundaries are essential:

- `F(Hv_rho)` must remain inside `b_rho`. Replacing it by `F(0)` is legitimate only in a flat-packet model such as `NB-225`; it is not the exact zeta observable.
- Multiplicities are included in (9)--(12).
- The statement is source-side. Even a proof of (25) would still require the already-isolated destination bridge before it becomes a quantitative Nyman--Beurling distance theorem.
- `NB-224` already closes the population-only route for `H=Theta(X)`. The value of (21) is precisely the unresolved sublinear-shell regime `H=o(R)`.
- No assertion is made that actual zeta zeros satisfy a subcritical cumulative exponent. Current zero-free, density and local-count inputs do not imply it; `NB-225`--`NB-227` were designed to show that gap.

The decisive falsification test is explicit. Construct a zero packet that satisfies the proposed subcritical bound (21) with fixed `delta>0` and controlled `A_X`, yet contributes order one after Ford damping. Equation (22) forbids such a packet. Conversely, the existing `NB-227` matched packet attains the critical boundary (31) and therefore verifies that the exponent in the criterion cannot be improved by a purely formal argument.

## Research consequence

The live source-side target after `NB-227` can now be stated without the ambiguous phrase "joint depth-phase information". The exact quantity to control is

\[
Y\int e^{-YD}\mathcal C_{X,H,t}(D)\,dD,
\]

where `C` is the nested cumulative **full carrier coefficient**, not an unweighted zero count or an independently normalized phase sum.

A theorem forcing `C(D)` to have exponential type strictly below `Y` would cross the matched-control barrier and suppress the deep exact-Ford residue tail. The abstract controls of `NB-225`--`NB-227` show that critical type `e^(YD)` remains admissible, so the next substantive question is sharply falsifiable: **do the actual near-one zeta zeros satisfy any uniform subcritical nested-depth carrier estimate, or can known/possible zero statistics still support critical-type excursions?**
