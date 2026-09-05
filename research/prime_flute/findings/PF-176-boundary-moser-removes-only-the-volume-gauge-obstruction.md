# PF-176 — boundary-relative Moser removes only the abstract volume-gauge obstruction

**Status:** `LITERATURE+DERIVED + EXACT-LOCAL + BOUNDARY`. PF-175 isolates an attractive way to remove its remaining identification gap: if the prime/shift marking can be chosen area preserving, then the dual-volume, trivial, and density-unitary identifications coincide and the conditional `S_r`, `r>1`, resolvent theorem applies directly. At the level of each compactly truncated one-cusp pant, **existence of an area-preserving marking with the same boundary values is not an obstruction**. Equal hyperbolic area plus Banyaga's boundary version of Moser's theorem gives such a correction. What remains open is the part PF-175 actually needs: a correction whose derivatives, boundary jets, smooth gluing, quasi-isometry constants, and inverse-unit-ball weighted metric defect stay uniformly controlled over the degenerating infinite tail. Thus the area-preserving route is narrowed from a qualitative existence question to a quantitative boundary-relative Moser problem. No global smooth area-preserving prime/shift marking, weighted Schatten hypothesis, wave/scattering equivalence, or RH consequence is claimed.

## Claim

Let

\[
P=P(2a,2b,0),
\qquad
P'=P(2a',2b',0)
\tag{1}
\]

be two oriented hyperbolic pairs of pants with two geodesic boundary components and one cusp. Normalize their cusps as in PF-125 so that, above a common horocycle `y=Y>1`, both contain the same standard cusp strip

\[
C_Y=\{0\le x\le1,\ y\ge Y\},
\qquad
 ds^2=\frac{dx^2+dy^2}{y^2}.
\tag{2}
\]

Write

\[
K=P\setminus C_Y,
\qquad
K'=P'\setminus C_Y.
\tag{3}
\]

Fix any smooth orientation-preserving marked diffeomorphism

\[
F:K\longrightarrow K'
\tag{4}
\]

with the desired label-preserving traces on the two finite cuffs and the chosen common trace on the truncating horocycle. Let `omega,omega'` be the hyperbolic area forms of `K,K'`.

Then there exists a smooth orientation-preserving diffeomorphism

\[
\boxed{\widetilde F:K\longrightarrow K'}
\tag{5}
\]

such that

\[
\boxed{
\widetilde F|_{\partial K}=F|_{\partial K},
\qquad
\widetilde F^*\omega'=\omega.
}
\tag{6}
\]

Therefore the boundary marking itself does not obstruct an area-preserving comparison of any one matched prime/shift pant core.

Applied pant by pant to the PF-125 prime/shift comparison, these corrections preserve the already-chosen **boundary values**, so the corrected pieces still glue as a marked continuous/piecewise-smooth comparison and are area preserving on the interiors. However, the theorem does **not** control the normal derivative of the correction at the cuffs or truncating horocycle. Consequently it does not by itself produce the smooth globally coherent marking or the weighted metric-deviation estimate required by PF-175.

## 1. The truncated pant cores have exactly equal area

Every complete hyperbolic pair of pants with geodesic boundary and one cusp has Euler characteristic `-1`. Gauss--Bonnet gives

\[
\operatorname{Area}(P)
=
-2\pi\chi(P)
=
2\pi,
\tag{7}
\]

independently of the two cuff lengths.

The common normalized cusp strip (2) has area

\[
\operatorname{Area}(C_Y)
=
\int_Y^\infty\int_0^1\frac{dx\,dy}{y^2}
=
\frac1Y.
\tag{8}
\]

PF-125's deep-cusp normalization is exactly what makes the removed source and target pieces identical rather than merely asymptotic. Hence

\[
\boxed{
\int_K\omega
=
2\pi-\frac1Y
=
\int_{K'}\omega'.
}
\tag{9}
\]

No estimate involving `a,a',b,b'` is needed for this equality.

## 2. Banyaga's boundary Moser theorem fixes the prescribed boundary values

Pull the target area form back by the initial marking:

\[
\omega_1:=F^*\omega'.
\tag{10}
\]

Both `omega` and `omega_1` are smooth positive volume forms on the same compact oriented surface `K`, and (9) gives

\[
\int_K\omega_1
=
\int_{K'}\omega'
=
\int_K\omega.
\tag{11}
\]

Banyaga's extension of Moser's theorem to compact oriented manifolds with boundary says that two positive volume forms with equal total volume are related by a diffeomorphism which may be chosen to restrict to the identity on the boundary. Thus there is

\[
\phi:K\longrightarrow K,
\qquad
\phi|_{\partial K}=\operatorname{id},
\qquad
\phi^*\omega_1=\omega.
\tag{12}
\]

Set

\[
\widetilde F:=F\circ\phi.
\tag{13}
\]

Then

\[
\widetilde F|_{\partial K}=F|_{\partial K}
\tag{14}
\]

and

\[
\widetilde F^*\omega'
=
\phi^*F^*\omega'
=
\phi^*\omega_1
=
\omega,
\tag{15}
\]

which proves (6).

The same conclusion can be viewed as a prescribed-Jacobian problem. Dacorogna--Moser prove on bounded Euclidean domains that a positive density of the correct total mass can be realized by a diffeomorphism equal to the identity on the boundary. This reinforces the point that **boundary-fixed volume correction is classical existence theory**, not a new prime-flute mechanism.

## 3. Boundary values are enough for topological gluing, but not for PF-175

For neighboring pants in the zero-twist chain, PF-125 arranges compatible full-cuff traces. Replacing each interior map `F_n` by `F_n\circ\phi_n` with

\[
\phi_n|_{\partial K_n}=\operatorname{id}
\tag{16}
\]

leaves those traces unchanged. The same is true at the common cusp truncation horocycle. Hence the corrected maps can be glued with the same pointwise marking data.

The subtlety is differential, not topological. Equation (16) gives identity **values** on the boundary; it does not imply

\[
D\phi_n|_{\partial K_n}=I
\tag{17}
\]

nor identity on a whole boundary collar. Two independently corrected adjacent pants may therefore have mismatched normal derivatives across a shared cuff. Likewise, extending the truncated correction by PF-125's exact deep-cusp isometry can leave a derivative kink at the chosen horocycle.

This matters because PF-175 assumes a smooth complete quasi-isometric metric comparison and measures the full multiplicative metric deviation, not only the Jacobian determinant. Area preservation imposes only

\[
\det D\widetilde F_n
\quad\text{at the volume-form level},
\tag{18}
\]

while the anisotropic singular values of `D\widetilde F_n` may still be large. In particular

\[
\widetilde F_n^*\omega'_n=\omega_n
\quad\not\Longrightarrow\quad
\delta_{g_n,\widetilde F_n^*g'_n}\ \text{is small}.
\tag{19}
\]

Thus `rho=1` removes the **density-identification** correction only if the same marking also retains the weighted metric budget.

## 4. The missing statement is quantitative and tail-uniform

The ordinary boundary Moser theorem is qualitative. It supplies no estimate in this application of the form

\[
\|D\phi_n-I\|\le C\varepsilon_n
\tag{20}
\]

with a constant `C` uniform over the escaping prime/shift pants, and it does not supply the stronger weighted conclusion

\[
\sum_n
\int_{K_n}
W_{g_n}\,
\delta_{g_n,(F_n\circ\phi_n)^*g'_n}^{\,r}
\,d\mu_{g_n}
<\infty.
\tag{21}
\]

Dacorogna--Moser provide regularity for the Jacobian equation on a fixed bounded domain, but the constants relevant to a quantitative estimate depend on the analytic geometry of the domain and the density data. Nothing in that classical existence theorem supplies the uniform degeneration-independent bound needed for the prime-flute tail.

The exact PF-125 Lambert/Fermi coordinates make (20)--(21) a plausible **new bounded problem** rather than an abstract existence problem: their metric is parameter-independent on the Lambert pieces and the uncorrected map is already `1+O(\varepsilon_n)` bi-Lipschitz. What is still required is an explicit or quantitatively audited volume correction compatible with the shared cuff/cusp interfaces.

A sufficient result would construct corrections `phi_n` for the actual PF-125 tail with all three properties:

1. boundary jets or fixed collar models compatible across every zero-twist cuff and the exact cusp handoff, so the global marking is smooth;
2. degeneration-uniform quasi-isometry control preserving the `1+O(\varepsilon_n)` scale of the original comparison;
3. an inverse-unit-ball weighted `delta^r` cost summable over the complete body/interface tail for the desired `r>1`.

If these hold, the corrected marking has `rho=1`, so

\[
J^\vee=I=U,
\tag{22}
\]

and PF-175 would transfer its `S_r` first-resolvent conclusion to the canonical density-unitary comparison for every `r>1` without a separate one-sided density-multiplier theorem.

## 5. Prior art and novelty audit

The existence theorem is classical. Augustin Banyaga, *Formes-volume sur les variétés à bord*, Enseignement Mathématique (2) 20 (1974), 127--131, extends Moser's volume-form theorem to compact oriented manifolds with boundary. Bruveris--Michor--Parusiński--Rainer, *Moser's theorem on manifolds with corners*, Proc. Amer. Math. Soc. 146 (2018), 4889--4897, DOI `10.1090/proc/14130`, explicitly summarize the boundary result in the form used here: the matching diffeomorphism can be chosen to restrict to the identity on the boundary.

Bernard Dacorogna and Jürgen Moser, *On a partial differential equation involving the Jacobian determinant*, Ann. Inst. H. Poincaré Anal. Non Linéaire 7 (1990), 1--26, DOI `10.1016/S0294-1449(16)30307-9`, give the Euclidean prescribed-Jacobian analogue with identity boundary condition.

No novelty is claimed for Moser/Banyaga volume correction, for Gauss--Bonnet area `2pi`, or for the fact that a boundary-fixed correction preserves boundary values. The durable project-specific content is the exact gate separation

\[
\boxed{
\text{equal-area pant cores}
+\text{ boundary Moser}
\Longrightarrow
\text{qualitative }\rho=1\text{ gauge},
}
\tag{23}
\]

but

\[
\boxed{
\text{PF-175 still requires}
\quad
\text{smooth coherent gluing}
+\text{uniform metric control}
+\text{weighted tail summability}.
}
\tag{24}
\]

The first line is classicalized; the second is the remaining prime-flute research problem.

## 6. Audit / falsification core

A later adversary can check PF-176 through a short chain:

1. verify by Gauss--Bonnet that every one-cusp two-geodesic-boundary hyperbolic pant has area `2pi`;
2. use PF-125's exact deep-cusp normalization and compute `Area(C_Y)=1/Y`, giving equal total area for the matched compact cores;
3. apply Banyaga's boundary Moser theorem to `omega` and `F^*omega'` and check equations (12)--(15);
4. verify that fixing the boundary pointwise preserves the existing cuff/horocycle trace but does **not** imply matching normal derivatives or identity on a boundary collar;
5. verify that determinant one does not bound the full metric distortion: for example, linear maps with singular values `lambda` and `lambda^{-1}` preserve area while their anisotropy diverges;
6. therefore do not invoke PF-175 until one globally smooth area-preserving marking also satisfies its quasi-isometry and inverse-unit-ball weighted `delta^r` hypothesis.

A refutation of the local claim would require either failure of the equal-area calculation or a failure of the cited boundary Moser theorem under these compact smooth hypotheses. Failure to obtain uniform estimates for the corrections would **not** refute PF-176; it is precisely the boundary that this finding records.