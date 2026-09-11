# NB-058 — collective late quotient tail is dual to compact-time defects

**Status:** `EXACT-DERIVED + SEMIGROUP-RANGE/ADJOINT-KERNEL + PALEY-WIENER-SUPPORT + TARGET-CERTIFICATE + FLAT-CONTROL + METHOD-REDUCTION`.

`NB-057` closes the possibility that the canonical finite residual can retain a positive signal by following one individual shifted block farther into the tail, but it deliberately leaves open the collective span of many late off-grid directions. The present finding identifies that collective object exactly. For every integer cutoff `R>=2`, the entire late quotient space is the closed range of one compressed integer-log shift, and its orthogonal complement inside the deflated defect space consists exactly of defect vectors whose Paley--Wiener representatives are supported before `log R`.

Use the deflated Hardy-space notation of `NB-053` and `NB-056`. Put

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)},\qquad
q_a(s)=\frac{e^{-a}-e^{-as}}{s-1},\qquad
F_a:=Oq_a,
\tag{1}
\]

and let

\[
\mathcal A=
\overline{\operatorname{span}}\{F_{\log n}:n\ge2\},
\qquad
Q=I-P_{\mathcal A},
\qquad
\mathcal D=\mathcal A^\perp.
\tag{2}
\]

For `a>=0` write `v_a=QF_a`, and for an integer `R>=2` define the collective late quotient

\[
\mathcal T_R=
\overline{\operatorname{span}}\{v_a:a\ge\log R\}
\subseteq\mathcal D.
\tag{3}
\]

Let

\[
(U_tF)(s)=e^{-t(s-1/2)}F(s)
\tag{4}
\]

be the Hardy shift semigroup. Since `NB-053` proves `U_(log R) A subseteq A`, the compression

\[
V_R:=Q U_{\log R}\big|_{\mathcal D}:\mathcal D\to\mathcal D
\tag{5}
\]

is a contraction. Then

\[
\boxed{\mathcal T_R=\overline{\operatorname{Ran}V_R}.}
\tag{6}
\]

Moreover `D` is invariant under `U_(log R)^*`, so

\[
\boxed{
\mathcal D\cap\mathcal T_R^\perp
=
\ker V_R^*
=
\mathcal D\cap\ker U_{\log R}^*.
}
\tag{7}
\]

Under the Paley--Wiener unitary used in `NB-056`, `U_t` is the right-shift isometry on `L^2(0,infinity)`. Hence `ker U_t^*` consists exactly of functions supported in `[0,t]`. If `mathcal P^{-1}` denotes this Paley--Wiener representative, (7) becomes

\[
\boxed{
\mathcal D\cap\mathcal T_R^\perp
=
\left\{
 h\in\mathcal A^\perp:
 \operatorname{supp}(\mathcal P^{-1}h)\subseteq[0,\log R]
\right\}.
}
\tag{8}
\]

Thus the surviving multichannel problem after `NB-057` is not an unspecified conditioning effect. Its exact dual is a **finite-time localization problem inside the actual arithmetic defect space**.

## 1. The tail is the range of one compressed natural shift

For `b>=0` and integer `R>=2`, the kernels satisfy the exact cocycle identity

\[
q_{\log R+b}
=
e^{-b}q_{\log R}+R^{-s}q_b.
\tag{9}
\]

Multiplication by `O` gives

\[
F_{\log R+b}
=
e^{-b}F_{\log R}+R^{-1/2}U_{\log R}F_b.
\tag{10}
\]

The first term belongs to `A`. Also integer-log invariance gives

\[
Q U_{\log R}P_{\mathcal A}=0,
\tag{11}
\]

so projection of (10) yields

\[
\boxed{
v_{\log R+b}
=
R^{-1/2}V_Rv_b.
}
\tag{12}
\]

The continuous deflated Nyman family `{F_b:b>=0}` has dense span in `H^2(Re s>1/2)` by the continuous Nyman closure after removal of Burnol's common Blaschke factor; equivalently this is the continuous-hull statement used in `NB-053`. Applying the bounded projection `Q` therefore gives

\[
\overline{\operatorname{span}}\{v_b:b\ge0\}=\mathcal D.
\tag{13}
\]

Taking closed spans in (12) proves (6).

For `x,y in D`,

\[
\langle V_Rx,y\rangle
=
\langle U_{\log R}x,y\rangle
=
\langle x,U_{\log R}^*y\rangle.
\tag{14}
\]

Because `U_(log R) A subseteq A`, its adjoint preserves `D`. Consequently

\[
V_R^*=U_{\log R}^*\big|_{\mathcal D},
\tag{15}
\]

and the Hilbert-space identity `(closure Ran V_R)^perp=ker V_R^*` proves (7). Equation (8) is then just the standard Paley--Wiener support description of the kernel of the backward translation.

## 2. The canonical collective target gain is exactly a compact-support approximation error

Let

\[
e(s)=\frac1s,
\qquad
h_*=Qe,
\tag{16}
\]

so `||h_*||=delta_def`. Define

\[
\mathcal K_R:=
\mathcal D\cap\ker U_{\log R}^*
=
\mathcal D\cap\mathcal T_R^\perp.
\tag{17}
\]

Since `T_R` is closed, `D=K_R direct-sum T_R`. Therefore

\[
\boxed{
\|P_{\mathcal T_R}h_*\|^2
=
\operatorname{dist}(h_*,\mathcal K_R)^2.
}
\tag{18}
\]

The dual-certificate formulation is consequently exact:

\[
\boxed{
\inf_{u\in\mathcal A,\ h\in\mathcal K_R}
\|e-u-h\|^2
=
\|P_{\mathcal T_R}h_*\|^2.
}
\tag{19}
\]

Indeed `e=P_Ae+h_*`, and the two summands of

\[
e-u-h=(P_Ae-u)+(h_*-h)
\tag{20}
\]

lie in the orthogonal spaces `A` and `D`. Minimizing the first term gives zero and minimizing the second over `K_R` gives (18).

Equation (19) is an abstract identity, not a source algorithm: choosing `u=P_Ae` or `h=P_(K_R)h_*` simply invokes the unknown projections. Its value is that it identifies exactly what a source-controlled certificate must construct. Any proposed `h_R` orthogonal to both `A` and `T_R` is automatically not merely a formal annihilator: **its own Paley--Wiener representative must be supported in `[0,log R]`**.

The spaces `K_R` increase with integer `R`, while `T_R` decrease. Put

\[
\mathcal K_{\rm fin}:=
\overline{\bigcup_{R\ge2}\mathcal K_R},
\qquad
\mathcal T_\infty:=
\bigcap_{R\ge2}\mathcal T_R.
\tag{21}
\]

Then

\[
\boxed{
\mathcal T_\infty
=
\mathcal D\ominus\mathcal K_{\rm fin},
\qquad
\lim_{R\to\infty}
\|P_{\mathcal T_R}h_*\|^2
=
\operatorname{dist}(h_*,\mathcal K_{\rm fin})^2.
}
\tag{22}
\]

Hence collective late-tail target gain tends to zero **if and only if** the canonical defect `h_*` can be approximated in norm by actual defect vectors of finite Paley--Wiener support. This criterion is weaker than asking every defect vector to be finitely localizable and stronger than the individual-shift decay proved in `NB-053`--`NB-057`.

## 3. The unit-outer control becomes the exact calibration

For the `O=1` control of `NB-056`, the natural space is the orthogonal direct sum of one coarse vector on each logarithmic cell

\[
I_j=[\log j,\log(j+1)].
\tag{23}
\]

Its defect space is the direct sum of the corresponding cell-detail spaces. Equation (8) therefore gives

\[
\mathcal K_R^{(0)}
=
\bigoplus_{j<R}
\left(
L^2(I_j)\ominus
\operatorname{span}\{e^{t/2}\mathbf1_{I_j}\}
\right),
\tag{24}
\]

while

\[
\mathcal T_R^{(0)}
=
\bigoplus_{j\ge R}
\left(
L^2(I_j)\ominus
\operatorname{span}\{e^{t/2}\mathbf1_{I_j}\}
\right).
\tag{25}
\]

Thus (18) is exactly the target-detail tail calculated in `NB-056`:

\[
\|P_{\mathcal T_R^{(0)}}Q_0e\|^2
=
\sum_{j\ge R}
\left[
\frac1{j(j+1)}-
\log^2\!\left(1+\frac1j\right)
\right]
=
\boxed{
\frac1{36R^3}+O(R^{-4})
}.
\tag{26}
\]

So the cubic flat-model law is not fundamentally a consequence of shrinking late columns. It is the rate at which the flat canonical defect is exhausted by **finite-time cell-detail defects**. The actual zeta factor can change the answer only through the geometry of `A^perp` inside these finite-support Paley--Wiener sectors.

## 4. Consequence for the early-cell adjoint-dual route

The proposed `CLUE-early-cell-adjoint-duals-certify-target-tail` asks for `h_R` annihilating `A` and the complete late quotient. Equations (7)--(8) show that this route has an exact hidden requirement:

\[
h_R\perp\mathcal A,\mathcal T_R
\quad\Longleftrightarrow\quad
h_R\in\mathcal A^\perp
\text{ and }
\operatorname{supp}(\mathcal P^{-1}h_R)
\subseteq[0,\log R].
\tag{27}
\]

The clue's weak adjoint/cell-moment construction is therefore one possible way of producing such a compact-time arithmetic defect, but the unbounded multiplier `O` need not be inverted to state the real target. A positive theorem now has a sharper form: construct enough vectors in `A^perp` with finite Paley--Wiener support to approximate `h_*`, with a quantitative remainder. A negative theorem could instead prove that these localized defect sectors are too small, or even trivial, for the actual arithmetic space.

This also supplies a strong adversarial boundary. It is consistent with all results above that `D` is nonzero while `K_R={0}` for every finite `R`. In that case

\[
\mathcal T_R=\mathcal D
\qquad\text{for every integer }R\ge2,
\tag{28}
\]

so the collective tail would retain the entire limiting defect at arbitrarily large ratios even though `NB-057` makes the projection onto every individual sufficiently late shifted block small. Individual-angle decay and collective-range decay are therefore genuinely different phenomena.

## 5. Prior-art boundary

The identities `overline(Ran V)^perp=ker V^*`, the Paley--Wiener support description of the backward translation kernel, and the general invariant-subspace language are standard operator/Hardy-space facts. Nyman--Beurling orthogonal complements and shift invariance have also been studied explicitly; in particular Calderaro, Manzur, Noor and Santos, *Orthogonality questions in the Hardy space related to zeta-zeros* (arXiv:2203.05030), use adjoint/operator methods, unbounded Toeplitz operators and shift-invariance to constrain the Hardy-space orthogonal complement. No novelty is claimed for those general tools.

A targeted search did not locate the exact specialization (6)--(8) identifying the **late continuous off-grid quotient after Blaschke deflation** with the compressed natural-shift range, nor the resulting finite-Paley--Wiener-support criterion (22) for the canonical collective target tail. This finding makes no priority claim. No specialized external theorem is load-bearing beyond the already anchored Nyman/Burnol/Hardy framework, so `SOURCES.md` is unchanged.

The durable line-local delta is the reduction itself: after `NB-057`, the multichannel large-ratio loophole is exactly the possible failure of finite-time defect vectors to exhaust the canonical deflated residual. That is now the source-specific object to attack, rather than raw column decay or individual late-shift angles.