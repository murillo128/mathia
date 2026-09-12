# NB-072 — branch-filter stable tails are exactly inner-factor model spaces

**Status:** `CLASSICAL+EXACT-DERIVED + MATCHED-CONTROL-CLASSIFICATION + INNER-OUTER-FACTOR + STABLE-TAIL + BRANCHING + METHOD-ADVANCE`.

`NB-071` constructs a well-conditioned exact-branching control with a nonzero stable tail by taking

\[
D_j^{(\rho)}=(I-\rho V_m)e_j,
\qquad \rho>1,
\]

where `V_m` is the consecutive-block branching isometry. That result shows that branching, the full local causal flag, and good global Gram conditioning do not by themselves rule out a stable tail. The present finding identifies the precise analytic source of that counterexample and classifies the whole stationary scalar branch-filter family containing it.

Fix `m>=2` and let

\[
V_me_j=m^{-1/2}\sum_{k=mj}^{m(j+1)-1}e_k
\]

on `S=ell^2(N)`. For a nonzero `psi in H^infty(D)` with `psi(0) != 0`, define

\[
D_j^{(\psi)}:=\psi(V_m)e_j,
\qquad
\mathcal A_\psi:=\overline{\operatorname{span}}\{D_j^{(\psi)}:j\ge1\}.
\]

Write the scalar inner--outer factorization

\[
\psi=\theta g,
\]

with `theta` inner and `g` outer. Then

\[
\boxed{
\mathcal A_\psi=\theta(V_m)\mathcal S,
\qquad
\mathcal S\ominus\mathcal A_\psi
\simeq
K_\theta\otimes\ker V_m^*,
}
\tag{1}
\]

where `K_theta=H^2(D) \ominus theta H^2(D)` is the classical model space. After adding the same infinite local defect sectors `Z_j` used in `NB-068/071`, the stable-tail space is exactly this scalar defect:

\[
\boxed{
\mathcal T_\infty(\mathcal A_\psi)
\simeq K_\theta\otimes\ker V_m^*.
}
\tag{2}
\]

Consequently

\[
\boxed{
\mathcal T_\infty(\mathcal A_\psi)=\{0\}
\iff
\psi\text{ is outer}.
}
\tag{3}
\]

Thus, within the entire stationary branch-filter class, a stable tail is **not** caused by long-range branching or poor conditioning as such. It is exactly an inner-factor defect. The outer part controls quantitative synthesis; the inner part alone controls the surviving orthogonal tail.

## 1. The branching isometry is a pure shift of infinite multiplicity

The descendant blocks defining `V_m e_j` are disjoint, so `V_m^*V_m=I`. Moreover `Ran(V_m^r)` is supported on indices at least `m^r`; hence

\[
\bigcap_{r\ge0}\operatorname{Ran}(V_m^r)=\{0\}.
\tag{4}
\]

Therefore `V_m` is a pure isometry. With

\[
\mathcal W:=\ker V_m^*,
\]

its Wold decomposition is

\[
\mathcal S
=\bigoplus_{r\ge0}V_m^r\mathcal W.
\tag{5}
\]

The unitary map

\[
\mathcal U:H^2(\mathbb D;\mathcal W)\to\mathcal S,
\qquad
\mathcal U\!\left(\sum_{r\ge0}z^rw_r\right)
=\sum_{r\ge0}V_m^rw_r,
\tag{6}
\]

intertwines multiplication by `z` with `V_m`. Hence

\[
\mathcal U M_\psi\mathcal U^*=\psi(V_m).
\tag{7}
\]

Classical inner--outer factorization now gives

\[
\overline{gH^2(\mathbb D;\mathcal W)}
=H^2(\mathbb D;\mathcal W)
\]

because `g` is outer, while multiplication by `theta` is an isometry with closed range. Thus

\[
\overline{\operatorname{Ran}\psi(V_m)}
=\theta(V_m)\mathcal S,
\tag{8}
\]

and (1) follows. No finite-dimensional or invertibility hypothesis on the outer factor is needed for this closure statement.

## 2. Inner--outer factorization is invisible to the whole finite-window flag

Let

\[
\psi(z)=c_0+c_1z+c_2z^2+\cdots,
\qquad c_0=\psi(0)\ne0.
\]

For every `r>=1`, the support of `V_m^r e_j` lies strictly after index `j`. Therefore

\[
D_j^{(\psi)}
=c_0e_j+\text{terms supported at indices }>j.
\tag{9}
\]

At every finite cutoff `R`, the truncated synthesis matrix of
`{D_j^(psi):j<R}` is triangular with nonzero diagonal `c_0`. Hence

\[
\boxed{
J_R\mathcal A_\psi
=\operatorname{span}\{e_1,\ldots,e_{R-1}\}.
}
\tag{10}
\]

After adjoining the same orthogonal infinite-dimensional cell sectors `Z_j` as in `NB-068/071`, this gives exactly

\[
\mathcal K_R=\bigoplus_{j<R}\mathcal Z_j,
\qquad
C_R=c_0e_R,
\qquad
\Gamma_R=0,
\qquad
\mathcal N_R=\mathcal Z_R.
\tag{11}
\]

So every filter in this class has the **same finite-window natural trace spaces and the same zero one-cell memory**, independent of whether `psi` has an inner factor. The union of the `K_R` exhausts the `Z` part, while the scalar orthogonal complement survives. This proves (2).

The exact branching law is also preserved. The block isometries commute,

\[
V_nV_m=V_mV_n=V_{mn},
\tag{12}
\]

so functional calculus gives `V_n psi(V_m)=psi(V_m)V_n`. Therefore for every integer `n>=2`,

\[
\boxed{
V_nD_j^{(\psi)}
=n^{-1/2}
\sum_{k=nj}^{n(j+1)-1}D_k^{(\psi)}.
}
\tag{13}
\]

Thus even imposing the full commuting family of integer branchings does not reveal the inner factor from finite-window flag data. The distinction is genuinely global and analytic.

## 3. Gram conditioning belongs to the outer factor, stable tail to the inner factor

Suppose in addition that the outer factor is boundedly invertible,

\[
g,\;g^{-1}\in H^\infty(\mathbb D).
\]

Since `theta(V_m)` is an isometry,

\[
\|\psi(V_m)x\|=\|g(V_m)x\|.
\]

Hence

\[
\boxed{
\|g^{-1}\|_\infty^{-2}I
\preceq
H_\psi:=\psi(V_m)^*\psi(V_m)
\preceq
\|g\|_\infty^2 I.
}
\tag{14}
\]

The Riesz conditioning is therefore controlled entirely by the invertible outer factor, whereas (2) depends entirely on `theta`. A nonconstant inner factor may coexist with arbitrarily good Gram conditioning, and an outer filter may have zero stable tail even when its range is nonclosed and its lower Gram bound vanishes.

This cleanly separates two phenomena that `NB-066/067/071` had shown could not be conflated: global source conditioning and causal stable-tail persistence.

## 4. `NB-071` is exactly a one-Blaschke-factor defect

Take

\[
\psi_\rho(z)=1-\rho z.
\]

For `rho>1`, put `a=rho^{-1}` and

\[
b_a(z)=\frac{z-a}{1-az}.
\]

Then

\[
\boxed{
1-\rho z
=-\rho\,b_a(z)(1-az).
}
\tag{15}
\]

The factor `b_a` is a one-zero Blaschke inner factor, while

\[
g_\rho(z)=-\rho(1-az)
\]

is outer and boundedly invertible. Equation (14) becomes exactly the `NB-071` Gram estimate

\[
(\rho-1)^2I
\preceq H_\rho\preceq
(\rho+1)^2I.
\tag{16}
\]

The model space of a one-point Blaschke factor is one-dimensional. Its normalized kernel is

\[
k_a(z)=\frac{\sqrt{1-a^2}}{1-az}.
\tag{17}
\]

Under the Wold unitary (6),

\[
k_a(z)w
\longmapsto
\sqrt{1-a^2}\sum_{r\ge0}a^rV_m^rw,
\tag{18}
\]

which is exactly the backward-eigenvector defect `t_w` constructed in `NB-071`. Thus the apparently nonlocal tree obstruction there is the coefficient-space image of a completely classical model-space defect:

\[
\boxed{
\mathcal T_\infty(\mathcal A_\rho)
\simeq K_{b_{1/\rho}}\otimes\ker V_m^*.
}
\tag{19}
\]

This also exposes a sharp phase transition. For `0<=rho<1`, `1-rho z` is invertible outer and the stable tail is zero. At `rho=1`, `1-z` is outer but not invertible; the range ceases to be closed, yet the stable tail is still zero. Only when `rho>1` and the zero enters the open unit disk does a nontrivial stable tail appear. Conditioning can deteriorate at the boundary, recover for `rho>1`, and still leave the tail behind. The location of the inner zero, not the condition number, is the decisive invariant.

## 5. Consequence for the Nyman route and strict boundary

The operator theory used above is classical: Wold decomposition, Beurling inner--outer factorization, and outer cyclicity. No novelty is claimed for those results or for model spaces. The line-local contribution is the exact classification of the `NB-068/071` matched-control architecture: once the source is a stationary scalar analytic filter of the branching shift with nonzero constant term, **its stable tail is precisely its inner factor**, while all finite causal trace data and exact integer branching remain unchanged.

This sharpens the interpretation of the current obstruction. `NB-071` does not show that an outer/cyclic branch source can hide a stable tail; its example obtains the tail by inserting a Blaschke factor. Conversely, every genuinely outer branch filter in this stationary class has zero stable tail even though it can preserve the same local tuple.

There is a suggestive but deliberately limited connection to the actual arithmetic source. `NB-062` uses Burnol's fact that the Blaschke-deflated Hardy multiplier

\[
O(s)=\frac{s-1}{s}\frac{\zeta(s)}{B(s)}
\]

is outer. **This finding does not identify that half-plane Hardy variable with the Wold branch variable `z`, and therefore does not infer `T_infinity=0` for the Nyman source.** The canonical innovations are nonstationary through their shrinking cells `Delta_j`, so an additional source-specific dictionary is required.

The useful target is now precise: prove that the actual causal innovation system is cyclic/outer in the relevant branching coordinate, or derive from its exact Mellin/Paley--Wiener Gram entries a no-inner-factor statement strong enough to replace that representation. Either would exclude the entire `NB-071` mechanism. If the actual source instead admits a nontrivial branch-inner factor, that factor would provide a concrete candidate carrier for the stable mode and should be detectable as a model-space defect.

The falsification boundary is strict. Equation (3) applies only to stationary scalar filters `psi(V_m)` with `psi(0) != 0`. It does not cover index-dependent filters, genuinely multivariable/noncommuting constructions, or arbitrary causal families satisfying branching without a stationary functional-calculus representation. Nor does outerness of `O(s)` in the Mellin/Hardy variable automatically imply outerness in this coefficient-side Wold variable. Finally, vanishing of the stable tail in a matched control is not itself a proof of RH or of a quantitative Nyman distance. The result classifies one important obstruction mechanism and converts the next source-specific question from generic conditioning to **inner-factor exclusion**.