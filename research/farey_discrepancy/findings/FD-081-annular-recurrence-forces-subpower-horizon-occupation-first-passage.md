# FD-081 — annular recurrence forces subpower horizon occupation first passage

**Status:** `EXACT-DERIVED + ANNULAR-TO-POINTWISE + HORIZON-FIRST-PASSAGE + POWER-SYNDETIC-OCCUPATION + SCHUR-TRANSVERSE-RECURRENCE`.

`FD-080` proves that fixed-strength **annular** nonsquarefree occupation cannot remain small through a fixed-power future interval: from every sufficiently large annular endpoint, one reaches an exact nonsquarefree-dilation descendant with occupation above a fixed threshold after only a subpower enlargement. The live gap is that the accepted occupation clue is formulated at individual horizons,

\[
\nu_{H,D}:=\frac{U_{H,D}}{E_{H,D}},
\]

whereas `FD-080` controls the energy-weighted annular ratio

\[
\Omega_{D,\alpha}(Y)
:=
\frac{\mathscr U_{D,\alpha}(Y)}{\mathscr E_{D,\alpha}(Y)}.
\]

There is nevertheless an exact transfer to the pointwise horizon currency. The annular ratio is a positive weighted average of the pointwise ratios, and the lower edge of its power annulus can be placed just beyond any prescribed starting horizon. Combining this elementary observation with the **subpower first passage** of `FD-080` gives a pointwise theorem that is stronger than logarithmic-density recurrence but still weaker than eventual pointwise occupation.

Fix a Schur head `D>=1` and a nonsquarefree integer `q>1`. Put

\[
w(q):=\frac{J_2(q)}{q^2},
\qquad
c_q:=w(q)q^{-2\Theta},
\]

where

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

For every fixed threshold

\[
0<\eta<c_q,
\tag{1}
\]

define the pointwise first-passage horizon

\[
\sigma_\eta(X)
:=
\min\{H\in\mathbb Z:H>X,\ \nu_{H,D}>\eta\}.
\tag{2}
\]

Then, for all sufficiently large `X`, the minimum exists and

\[
\boxed{
\frac{\log\sigma_\eta(X)}{\log X}\longrightarrow1,
\qquad
\frac{\sigma_\eta(X)}X=X^{o(1)}.
}
\tag{3}
\]

Equivalently, for every fixed `epsilon>0`, every sufficiently large `X` contains an integer horizon satisfying

\[
\boxed{
X<H\le X^{1+\epsilon},
\qquad
\nu_{H,D}>\eta.
}
\tag{4}
\]

Thus constant-strength **pointwise** nonsquarefree Jordan occupation is power-syndetic in the forward multiplicative scale. The remaining bad horizons may still be infinite, arbitrarily deep, and locally clustered, but no sufficiently large horizon can begin a pointwise bad desert extending through any fixed-power enlargement.

For `q=4`,

\[
w(4)=\frac34,
\qquad
c_4=\frac34\,4^{-2\Theta}\ge\frac3{64},
\tag{5}
\]

so every fixed `eta<3/64` is available unconditionally. Under RH, `Theta=1/2`, hence every fixed `eta<3/16` is available.

## 1. Annular occupation is exactly an energy-weighted average of horizon occupation

Retain the definitions of `FD-079`--`FD-080`:

\[
E_{H,D}
=
\sum_{D<r\le H}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

\[
U_{H,D}
=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
\frac{J_2(r)}{r^2}
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2,
\]

and

\[
\lambda_H:=\log\frac{H+1}{H}>0.
\]

For a fixed `0<alpha<1`,

\[
\mathscr E_{D,\alpha}(Y)
=
\sum_{Y^{1-\alpha}<H\le Y}
\lambda_HE_{H,D},
\]

\[
\mathscr U_{D,\alpha}(Y)
=
\sum_{Y^{1-\alpha}<H\le Y}
\lambda_HU_{H,D}.
\]

Since `U_(H,D)=E_(H,D) nu_(H,D)`, one has the exact identity

\[
\boxed{
\Omega_{D,\alpha}(Y)
=
\frac{
\sum_{Y^{1-\alpha}<H\le Y}
\lambda_HE_{H,D}\nu_{H,D}
}{
\sum_{Y^{1-\alpha}<H\le Y}
\lambda_HE_{H,D}
}.
}
\tag{6}
\]

All weights in (6) are nonnegative, and `FD-079`--`FD-080` work beyond a fixed scale where the denominator is positive. Therefore

\[
\boxed{
\Omega_{D,\alpha}(Y)>\eta
\quad\Longrightarrow\quad
\exists H\in(Y^{1-\alpha},Y]\cap\mathbb Z
\text{ with }\nu_{H,D}>\eta.
}
\tag{7}
\]

No density theorem, regularity of `nu`, or source interpolation is needed for this implication. It is simply positivity of the physical energy weights.

## 2. Rescaling the annulus places its lower edge beyond an arbitrary horizon

Fix an arbitrary target enlargement exponent `epsilon>0`. Choose fixed constants

\[
0<\alpha<1,
\qquad
\delta>0
\]

so small that

\[
\boxed{
\frac{1+\delta}{1-\alpha}<1+\epsilon.
}
\tag{8}
\]

This choice is always possible. For a large starting horizon `X`, define the integer annular base

\[
Z:=\left\lceil X^{1/(1-\alpha)}\right\rceil.
\tag{9}
\]

Apply `FD-080` at `Z`, with this fixed `alpha`, the same fixed nonsquarefree dilation `q`, threshold `eta<c_q`, and the fixed multiplicative tolerance `delta`. For all sufficiently large `X`, there is an exact successor descendant `Y` such that

\[
Z<Y\le Z^{1+\delta},
\qquad
\Omega_{D,\alpha}(Y)>\eta.
\tag{10}
\]

By (7), choose an integer `H` with

\[
Y^{1-\alpha}<H\le Y,
\qquad
\nu_{H,D}>\eta.
\tag{11}
\]

The lower edge has been engineered so that

\[
H>Y^{1-\alpha}
>Z^{1-\alpha}
\ge X.
\tag{12}
\]

At the upper edge, (9)--(10) give

\[
H\le Y\le Z^{1+\delta}.
\tag{13}
\]

Because

\[
\frac{\log Z}{\log X}
\longrightarrow
\frac1{1-\alpha},
\tag{14}
\]

one obtains

\[
\limsup_{X\to\infty}
\frac{\log H}{\log X}
\le
\frac{1+\delta}{1-\alpha}
<1+\epsilon.
\tag{15}
\]

The strict margin in (8) absorbs the harmless ceiling in (9). Hence, for all sufficiently large `X`,

\[
X<H\le X^{1+\epsilon},
\qquad
\nu_{H,D}>\eta,
\]

which proves (4).

The important quantifier point is that `alpha` and `delta` are fixed **after epsilon is fixed and before X tends to infinity**. Nothing here uses a shrinking annulus parameter inside one application of `FD-080`, so the fixed-parameter boundary of that theorem is respected.

## 3. Pointwise first passage is subpower

By definition,

\[
\sigma_\eta(X)>X.
\]

Equation (4) gives, for every fixed `epsilon>0`,

\[
\sigma_\eta(X)\le X^{1+\epsilon}
\]

for all sufficiently large `X`. Therefore

\[
1
\le
\liminf_{X\to\infty}
\frac{\log\sigma_\eta(X)}{\log X}
\le
\limsup_{X\to\infty}
\frac{\log\sigma_\eta(X)}{\log X}
\le1+\epsilon.
\]

Since `epsilon` is arbitrary,

\[
\boxed{
\frac{\log\sigma_\eta(X)}{\log X}\to1.
}
\tag{16}
\]

Equivalently,

\[
\log\frac{\sigma_\eta(X)}X=o(\log X),
\]

which is the second assertion in (3).

This is the horizon-level analogue of the annular first-passage theorem in `FD-080`, but the proof does **not** identify the good horizon with the annular endpoint or with the exact `q`-successor orbit. The successor structure is used only to produce a good annulus; positivity then extracts at least one good physical horizon from inside it.

## 4. What this resolves and what it does not

The accepted clue `CLUE-joint-nonsquarefree-jordan-energy-occupation` asks for the much stronger eventual pointwise statement

\[
U_{H,D}\ge c_D E_{H,D}
\]

at every sufficiently large horizon. `FD-081` does not prove that statement and therefore does not resolve the clue. It establishes a different intermediate rigidity:

\[
\boxed{
\text{every sufficiently large scale reaches a fixed-strength pointwise occupied horizon after }X^{o(1)}\text{ enlargement}.}
}
\tag{17}
\]

This is strictly stronger than the positive logarithmic-density information available before `FD-080`: a positive-density good set can still have sparse fixed-power deserts, whereas (4) forbids those deserts. It is also strictly weaker than eventual pointwise occupation: isolated bad horizons and even long `X^(o(1))` bad stretches remain compatible with the theorem.

Because nonsquarefree Jordan rows are exactly transverse to the Schur equality direction in the established `FD-034` normalization, every horizon supplied by (4) is also a horizon with a fixed positive transverse-energy fraction. This gives a **power-syndetic pointwise Schur-separation currency**, but it is not by itself a new Mertens exponent, a uniform scalar dual gap at every horizon, or an RH proof.

The live downstream question is therefore narrower. One no longer needs to promote annular recurrence to *some* physical horizon: that transfer is exact. What remains is to determine whether the Farey/RH criterion can consume a power-syndetic sequence of pointwise transverse horizons, or whether the still-allowed subpower gaps can carry all of the dangerous near-saturation behavior.

## 5. Stress tests and boundary of the claim

The weighted-average step cannot produce more than existence. Even if `Omega(Y)` is bounded below, the annular energy could in principle be concentrated on a very small subset of horizons, so (7) gives neither natural density nor a count of good horizons. Any stronger conclusion needs additional control on the distribution of `E_(H,D)` inside the annulus.

The theorem gives no uniform multiplicative constant `C` with `sigma_eta(X)<=CX`. The parameters `alpha` and `delta` used to realize a prescribed `epsilon` may need to become arbitrarily small as `epsilon` decreases, while `FD-080` supplies no uniform first-passage estimate as those parameters vary. Hence the honest conclusion is `X^(1+o(1))`, not bounded-ratio recurrence.

The threshold remains exactly the `FD-080` threshold `eta<c_q`. At `eta=c_q`, the positive drift used there vanishes, so this transfer cannot restore a threshold that the annular theorem does not provide.

The head `D` and dilation `q` remain fixed. A growing Schur head requires the head-covariant machinery of `FD-067`--`FD-068` and is not covered by the present statement.

Finally, this result does not contradict the pointwise escape constructions earlier in the line. Those constructions show that generic Lipschitz or abstract energy information does not force eventual positive occupation. Here the load-bearing input is the later physical annular theorem `FD-080`, itself dependent on the full physical `2 Theta` energy exponent from `FD-078`.

## 6. Prior-art and novelty boundary

No new external theorem is used. The proof is an exact consequence of the physical annular recurrence in `FD-080` and the positive energy-weighted identity already built into `FD-079`. Their external dependencies, including the zeta-zero frontier and Pintz inputs underlying `FD-078`, are already anchored in `SOURCES.md`.

A targeted literature search over Farey discrepancy, Mertens formulations, nonsquarefree/Jordan energy occupation, multiplicative recurrence, and power-syndetic exceptional sets did not locate a theorem matching this specific annular-to-horizon first-passage consequence. The averaging implication itself is elementary, so no broad novelty claim is made. The mathematical contribution recorded here is the observation that the lower edge of the fixed-power annulus can be rescaled to an arbitrary horizon **without losing the subpower recurrence supplied by `FD-080`**, thereby changing the available downstream currency from annular to pointwise.

The decisive falsification points are correspondingly narrow: (6) would fail only if the stored annular normalization differed from the positive weighted physical energy average; (10) would fail if `FD-080` did not apply for each fixed `alpha,delta`; and the scale transfer would fail if the fixed-parameter choice (8) could not be made. Under the current canonical statements, all three steps are exact.