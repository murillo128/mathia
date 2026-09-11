# PF-289 — fixed local Rayleigh floors suffice for a heavy-angle noncompactness witness

**Status:** `EXACT-DERIVED + FORM-NATIVE-NONCOMPACTNESS-CRITERION + ROUTE-SHARPENING + PF-227-SPECIALIZATION`.

[[research/prime_flute/findings/PF-288-diverging-local-form-witnesses-force-heavy-angle-noncompactness|PF-288]] proves a strong local falsifier for the physical heavy-angle problem: if separated physical-low/high local vectors have diagonal Rayleigh quotients tending to infinity and retain a nonzero energy-normalized mixed correlation, then the heavy angle is noncompact at **every** fixed positive threshold. That theorem deliberately uses divergence because it wants negligible spectral-projection error for an arbitrarily prescribed heavy threshold.

For the actual endpoint falsification, this is stronger than necessary. To prove that the PF-281/PF-282 mixed operator is noncompact, it suffices to exhibit **one** pair of positive heavy thresholds at which the angle is noncompact. If the separated local families have only uniform positive Rayleigh floors,

\[
\frac{k[u_j]}{\|u_j\|^2}\ge M_P>0,
\qquad
\frac{k[v_j]}{\|v_j\|^2}\ge M_H>0,
\]

then one may choose the heavy thresholds small enough compared with `M_P,M_H`. The low-energy spectral leakage of the whole energy-normalized synthesis operator is then small in **operator norm**, not merely columnwise. A nonvanishing diagonal cross-Gram therefore survives projection to those fixed heavy sectors and gives a noncompact heavy angle.

This removes one of the two geometric obligations left after PF-288. [[research/prime_flute/findings/PF-227-fixed-physical-high-pass-does-not-remove-thin-pant-channel-multiplicity|PF-227]] already supplies a separated physical-high local family with a uniform positive diagonal Rayleigh floor. Indeed its fixed-threshold high/high crossing, together with Cauchy--Schwarz for the positive precision form, forces at least one endpoint of each singular pair to have diagonal high energy bounded below by the same fixed constant. [[research/prime_flute/findings/PF-216-positive-shift-pant-compression-has-a-growing-mass-floor|PF-216]] supplies the low family with a much stronger diverging floor.

Thus a **diverging physical-high Rayleigh family no longer has to be constructed** for the cheapest negative test. The remaining local obstruction question is only whether one can choose the PF-227 high witnesses so that their energy-normalized mixed correlation with the corresponding PF-216 low-symmetric module vectors stays bounded away from zero. If that correlation persists along one sparse tail, the physical mixed operator is noncompact. If it vanishes for all such local choices, this particular PF-288/PF-289 falsifier fails and the line must return to the positive essential-orthogonality/counting problem of PF-287.

## Claim

Retain the PF-281/PF-282 closed nonnegative precision form `k` on

\[
\mathcal H=\mathcal H_P\oplus\mathcal H_H,
\]

with diagonal energy operators `|R_P|,|R_H|` and extension angle

\[
\Gamma=V_P^*V_H.
\]

Assume the PF-214 nearest-neighbor form locality. Let `I_j` be pairwise separated finite module windows, with distance greater than one, and choose nonzero

\[
u_j\in P\operatorname{Dom}k,
\qquad
v_j\in H\operatorname{Dom}k
\]

supported in `I_j`. Put

\[
a_j=k[u_j],\qquad b_j=k[v_j].
\tag{1}
\]

Suppose there are constants `M_P,M_H,c>0` such that after a finite head

\[
\boxed{
\frac{a_j}{\|u_j\|^2}\ge M_P,
\qquad
\frac{b_j}{\|v_j\|^2}\ge M_H,
}
\tag{2}
\]

and

\[
\boxed{
|k[u_j,v_j]|\ge c\sqrt{a_jb_j}.
}
\tag{3}
\]

Then there exist **fixed positive** thresholds `\mu_P,\mu_H>0` such that

\[
E_P^{\mu_P}\Gamma E_H^{\mu_H},
\qquad
E_P^{\mu_P}:=\mathbf1_{[\mu_P,\infty)}(|R_P|),
\qquad
E_H^{\mu_H}:=\mathbf1_{[\mu_H,\infty)}(|R_H|),
\tag{4}
\]

is noncompact. Consequently

\[
T=f(|R_P|)\Gamma f(|R_H|),
\qquad
f(t)=\frac{t}{\sqrt{1+t^2}},
\tag{5}
\]

is noncompact and cannot belong to `\mathcal S_{1,\infty}`.

More quantitatively, choose `0<\varepsilon<1` so that

\[
2\varepsilon+\varepsilon^2<c/2
\tag{6}
\]

and set

\[
\mu_P=\varepsilon\sqrt{M_P},
\qquad
\mu_H=\varepsilon\sqrt{M_H}.
\tag{7}
\]

Then the heavy cross-Gram operator contains an infinite-dimensional compression bounded below by `c/2`.

The distinction from PF-288 is exact: divergence of both Rayleigh quotients is sufficient to reach **every prescribed positive threshold**; the uniform floors (2) are sufficient for noncompactness because the thresholds may be chosen after the floors are known.

## 1. Uniform local floors give operator-norm heavy concentration at small thresholds

Define the unit-energy families

\[
x_j:=\frac{|R_P|u_j}{\sqrt{a_j}},
\qquad
y_j:=\frac{|R_H|v_j}{\sqrt{b_j}}.
\tag{8}
\]

PF-214 locality and the support separation give

\[
k[u_i,u_j]=k[v_i,v_j]=k[u_i,v_j]=0
\qquad(i\ne j),
\tag{9}
\]

so `(x_j)` and `(y_j)` are orthonormal and

\[
\langle x_i,\Gamma y_j\rangle
=\frac{k[u_i,v_j]}{\sqrt{a_i b_j}}.
\tag{10}
\]

Hence the unprojected cross-Gram is diagonal,

\[
D=X^*\Gamma Y=\operatorname{diag}(\gamma_j),
\qquad
|\gamma_j|\ge c,
\tag{11}
\]

where `X,Y:\ell^2\to\mathcal H` have columns `x_j,y_j`. In particular

\[
\|Dz\|\ge c\|z\|.
\tag{12}
\]

The point not used in PF-288 is that (2) controls the **synthesis** of the underlying form-domain vectors. Let

\[
U_Pz:=\sum_j z_j\frac{u_j}{\sqrt{a_j}}.
\tag{13}
\]

The windows are disjoint in the Hilbert-space decomposition, so

\[
\|U_Pz\|^2
=\sum_j|z_j|^2\frac{\|u_j\|^2}{a_j}
\le M_P^{-1}\|z\|^2.
\tag{14}
\]

For `Q_P=E_P^{\mu_P}` and `E=(I-Q_P)X`, spectral calculus gives

\[
\begin{aligned}
\|Ez\|
&=\left\|
\mathbf1_{[0,\mu_P)}(|R_P|)|R_P|U_Pz
\right\|\\
&\le \mu_P\|U_Pz\|
\le \frac{\mu_P}{\sqrt{M_P}}\|z\|.
\end{aligned}
\tag{15}
\]

Thus

\[
\boxed{\|E\|\le\mu_P/\sqrt{M_P}.}
\tag{16}
\]

The identical argument on the high side, with `Q_H=E_H^{\mu_H}` and `F=(I-Q_H)Y`, gives

\[
\boxed{\|F\|\le\mu_H/\sqrt{M_H}.}
\tag{17}
\]

Unlike PF-288, no convergence or sparse Hilbert--Schmidt tail is needed. The fixed local Rayleigh floors already give uniform operator-norm control when the threshold is chosen sufficiently small.

## 2. The projected heavy cross-Gram remains bounded below

Put

\[
X_h=Q_PX,
\qquad
Y_h=Q_HY,
\qquad
M=X_h^*\Gamma Y_h.
\tag{18}
\]

Since `X=X_h+E`, `Y=Y_h+F`, and `\|\Gamma\|\le1`,

\[
D-M
=E^*\Gamma Y_h+X_h^*\Gamma F+E^*\Gamma F.
\tag{19}
\]

With the choice (7), equations (16)--(17) give `\|E\|,\|F\|\le\varepsilon`, hence

\[
\boxed{
\|D-M\|\le2\varepsilon+\varepsilon^2<c/2.
}
\tag{20}
\]

Combining (12) and (20),

\[
\boxed{
\|Mz\|\ge(c/2)\|z\|.
}
\tag{21}
\]

The projected columns are not exactly orthonormal, but

\[
A:=X_h^*X_h=I-E^*E,
\qquad
B:=Y_h^*Y_h=I-F^*F,
\tag{22}
\]

so `A,B\ge(1-\varepsilon^2)I`. Define

\[
\widetilde X=X_hA^{-1/2},
\qquad
\widetilde Y=Y_hB^{-1/2}.
\tag{23}
\]

These are isometries into the fixed heavy spaces. Their heavy cross-Gram is

\[
\widetilde X^*\Gamma\widetilde Y
=A^{-1/2}MB^{-1/2}.
\tag{24}
\]

Because `A,B\le I`, the inverse square roots do not decrease norms. Equation (21) therefore gives

\[
\boxed{
\|\widetilde X^*\Gamma\widetilde Y z\|
\ge(c/2)\|z\|.
}
\tag{25}
\]

So `Q_P\Gamma Q_H` has an infinite-dimensional compression bounded below and is noncompact. PF-287 then identifies this with noncompactness of the corresponding heavy-range projection product. Since the strength factors in (5) are bounded below by the positive constants `f(\mu_P),f(\mu_H)` on these sectors, PF-282/PF-287 imply that `T` is noncompact.

## 3. PF-227 already supplies the required physical-high Rayleigh floor

PF-227 proves that for one fixed `b>0` and infinitely many separated adjacent high modules there are unit physical-high vectors

\[
x_n\in H\mathcal B_n,
\qquad
y_n\in H\mathcal B_{n+1}
\]

such that

\[
|k_H[y_n,x_n]|\ge b.
\tag{26}
\]

This is the same high/high crossing input already used in PF-286 to prove noncompactness of the high strength factor. Since `k_H` is a nonnegative sesquilinear form, its Cauchy--Schwarz inequality gives

\[
|k_H[y_n,x_n]|^2
\le k_H[x_n]k_H[y_n].
\tag{27}
\]

Therefore

\[
\max\{k_H[x_n],k_H[y_n]\}\ge b.
\tag{28}
\]

For each separated pair choose `h_n` to be an endpoint attaining (28). Then

\[
\boxed{
\|h_n\|=1,
\qquad
h_n\in H\operatorname{Dom}k,
\qquad
k[h_n]\ge b.
}
\tag{29}
\]

Passing to indices separated by more than the PF-214 interaction range gives a pairwise separated local physical-high family satisfying (2) with `M_H=b`.

This does **not** upgrade PF-227 to a diverging high Rayleigh sequence. It shows that such divergence is unnecessary for the fixed-threshold noncompactness test. PF-288 remains the stronger theorem if one wants noncompactness of the angle at every prescribed positive strength threshold.

## 4. Prime-Flute specialization: the cheapest negative test is now one mixed correlation

PF-216 supplies unit low-symmetric physical-low module vectors `\ell_m` with

\[
k[\ell_m]
\gtrsim\frac{P_m}{\log P_m}\to\infty.
\tag{30}
\]

Hence, after discarding a finite head, these vectors satisfy the low floor in (2) with any fixed `M_P>0`. From PF-227 choose a sparse family `h_j` as in (29), and let `m_j` be the module supporting `h_j`. Pair it with `\ell_{m_j}`. The support windows can be made pairwise separated.

Consequently, if along some subsequence

\[
\boxed{
\frac{|k[\ell_{m_j},h_j]|}
{\sqrt{k[\ell_{m_j}]k[h_j]}}
\ge c>0,
}
\tag{31}
\]

then the physical mixed operator `T` is noncompact by the theorem above.

The decisive local negative test therefore no longer has two unknown geometric ingredients. The high diagonal-energy condition is already supplied by PF-227. The only genuinely new quantity to compute is the energy-normalized **physical low/high mixed form** in (31), optimizing over the PF-227 high witness family if useful.

A convenient falsification statistic on module `m` is

\[
\eta_m
:=
\sup_{\substack{h\in H\operatorname{Dom}k\;\text{local on }m\\
\|h\|=1,\ k[h]\ge b}}
\frac{|k[\ell_m,h]|}{\sqrt{k[\ell_m]k[h]}}.
\tag{32}
\]

One should restrict the supremum to the local physical-high witness spaces furnished by the PF-227 construction, rather than all high vectors, when making this a finite geometric calculation. If `\limsup\eta_m>0` along a sparse tail, noncompactness follows. If the corresponding optimized correlations tend to zero, the PF-227/PF-289 local obstruction is absent; that negative result would not prove compactness, but it would force the project back to PF-287's global essential-orthogonality or small-threshold counting route.

## 5. Why this does not contradict PF-288

PF-288 states that a fixed Rayleigh lower bound is insufficient to push unit-energy vectors asymptotically into **an arbitrarily prescribed** heavy sector. That statement remains correct. If the threshold `\mu` is fixed independently of the floor, the bound

\[
\|(I-E^\mu)x_j\|
\le \mu\frac{\|u_j\|}{\sqrt{k[u_j]}}
\tag{33}
\]

need not tend to zero under a mere uniform floor.

The present theorem changes the quantifier that matters for compactness. Noncompactness of `T` requires only **existence** of one positive pair of heavy thresholds carrying a noncompact angle. Equations (16)--(17) allow those thresholds to be chosen small enough that the projection errors are uniformly below the already-present cross-correlation gap `c`. The stronger PF-288 divergence hypothesis is needed only for its stronger conclusion covering every fixed threshold.

This distinction matters operationally because PF-227 naturally gives a fixed high-energy floor but not a divergent high Rayleigh law. The endpoint falsification should use exactly the amount of spectral concentration it needs rather than promote high-energy divergence into an artificial geometric gate.

## Prior-art and novelty audit

The functional-analysis ingredients are classical. PF-287 already records the standard principal-angle/product-of-projections literature, including Galántai, *Subspaces, angles and pairs of orthogonal projections*, **Linear and Multilinear Algebra** 56 (2008), 227--260, and Andruchow--Corach, *Essentially orthogonal subspaces*, **Journal of Operator Theory** 79 (2018), 79--100. The spectral-projection estimate in (15), Cauchy--Schwarz for a nonnegative form, and the compactness obstruction supplied by an infinite-dimensional compression bounded below are elementary Hilbert-space facts. A targeted check of projection-product/essential-orthogonality and positive-form literature found no reason to claim a new general operator theorem.

Accordingly, **no general novelty is claimed** for the abstract lemma. The project-specific contribution is the quantifier sharpening of PF-288 together with the exact PF-227 specialization: the canonical Prime-Flute physical-high geometry already supplies the uniform local Rayleigh floor needed for a fixed-threshold noncompactness witness. This removes the previously stated need to construct a diverging physical-high Rayleigh family before testing the mixed correlation. No new external dependency is required in `SOURCES.md`.

## Boundary checks and consequences

1. Uniform floors are enough only because the heavy thresholds may be chosen after `M_P,M_H,c` are known. They do not imply PF-288's every-threshold conclusion.
2. The mixed correlation (3) remains essential. PF-227 high/high multiplicity and the diagonal floors alone do not imply any physical low/high overlap.
3. The chosen PF-227 endpoint `h_n` may lie on either side of the adjacent-module high/high singular pair. The paired PF-216 vector in (31) must be taken on the same local module, and the sparse selection must preserve PF-214 support separation.
4. Equation (29) is only a fixed positive Rayleigh floor. No claim is made that `k[h_n]\to\infty`.
5. Failure of the local correlation test proves only that this local obstruction is absent. It does not establish compactness, the PF-283 weak-trace counting law, or any positive endpoint theorem.
6. Success of (31) proves noncompactness of the PF-281/PF-282 mixed physical coupling and therefore rules out the current weak-trace endpoint route before any finer threshold count. It does not by itself produce a wave-operator theorem, determinant/resonance statement, prime/clone separation, zeta-zero correspondence, critical-line statement, or RH consequence.

The immediate research priority is therefore sharply reduced: **compute or bound the normalized low/high form correlation (31) for the actual PF-205/PF-212 physical split on the PF-227 local witness spaces**. No separate construction of a divergent physical-high Rayleigh family is needed first.