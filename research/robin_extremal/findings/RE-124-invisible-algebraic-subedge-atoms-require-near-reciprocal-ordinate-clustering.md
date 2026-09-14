# RE-124 — invisible algebraic subedge atoms require near-reciprocal ordinate clustering

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + NONISOLATED-EDGE + SPECTRAL-LOCALIZATION + ZERO-CLUSTERING-NECESSITY + CA-PHASE-TRANSFER + REPRESENTATION-AUDITED + PRIOR-ART-AUDITED`.

Assume the attained finite-edge branch of `RE-121`--`RE-123`,

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad
\frac12<\sigma_0<\Theta,
\]

and fix an expansion order `K>=0`. For a positive-ordinate subedge zero

\[
\rho=\beta+i\gamma,
\qquad
\sigma_0\le\beta<\Theta,
\qquad
\gamma>0,
\]

write

\[
\delta_\rho:=\Theta-\beta
\]

and define its order-`K` coefficient in the signed packet of `RE-121` by

\[
a_{\rho,K}(u)
:=
 e^{-\delta_\rho u}
\left[
\frac1{\rho(1-\rho)}
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k(1-\rho)^{k+1}}
\right].
\tag{1}
\]

Zeros are listed with multiplicity. Conjugate pairing gives

\[
\mathcal S_K(u)
=
2\Re
\sum_{\substack{\zeta(\rho)=0\\
\sigma_0\le\Re\rho<\Theta\\
\Im\rho>0}}
 a_{\rho,K}(u)e^{i\gamma u}.
\tag{2}
\]

`RE-123` showed that regular CA phases sample this complete packet superalgebraically well, but left open whether the packet itself can remain small because many subedge modes cancel internally. The first part of that cancellation problem can now be localized sharply.

Fix real numbers

\[
A>0,
\qquad
0<\eta<1.
\]

For a target zero `rho_0=beta_0+i gamma_0`, define the near-reciprocal ordinate cluster at phase `U` by

\[
\mathcal C_{\eta}(\rho_0;U)
:=
\left\{
\rho\ne\rho_0:
\sigma_0\le\Re\rho<\Theta,
\ \Im\rho>0,
\ |\Im\rho-\gamma_0|
\le U^{-1+\eta}
\right\}.
\tag{3}
\]

Then there is a constant `C=C(A,K,eta,sigma_0,Theta)` such that, for every sufficiently large `U`, every target atom satisfying

\[
|a_{\rho_0,K}(U)|\ge cU^{-A}
\tag{4}
\]

with fixed `c>0` obeys the localization inequality

\[
\boxed{
|a_{\rho_0,K}(U)|
\le
C
\left(
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
+
\sum_{\rho\in\mathcal C_\eta(\rho_0;U)}
|a_{\rho,K}(U)|
\right)
+o(U^{-A}).
}
\tag{5}
\]

Consequently, if the target atom is locally dominant in the sense that

\[
\sum_{\rho\in\mathcal C_\eta(\rho_0;U)}
|a_{\rho,K}(U)|
=o(|a_{\rho_0,K}(U)|),
\tag{6}
\]

then

\[
\boxed{
\sup_{|u-U|\le U^{1-\eta/2}}
|\mathcal S_K(u)|
\gg
|a_{\rho_0,K}(U)|
\gg U^{-A}.
}
\tag{7}
\]

Thus an **individually algebraically visible subedge zero cannot be hidden by distant frequencies**. To suppress it at order `U^-A`, the packet must place comparable coefficient mass inside an ordinate neighborhood of width `U^(-1+eta)`. Since `eta>0` is arbitrary, an invisible strong atom along an unbounded sequence requires such competing mass on every fixed near-reciprocal scale

\[
|\gamma-\gamma_0|\le U^{-1+\eta}.
\tag{8}
\]

Equivalently, the surviving cancellation must be concentrated in ordinate clusters whose width is `U^(-1+o(1))` or smaller, unless the algebraic mass is genuinely diffuse so that no single atom reaches the target scale.

When `A<K+1`, `RE-123` transfers (7) to actual regular CA states. There is then a regular CA state `C` with

\[
\nu_C:=\log\log C
=U+O(U^{1-\eta/2})
\tag{9}
\]

for which the order-`K` residual

\[
R_K(\nu_C)
:=B_\Theta(C)-\mathcal E_K(\nu_C)
\]

satisfies

\[
\boxed{
|R_K(\nu_C)|\gg U^{-A}.
}
\tag{10}
\]

Hence near-reciprocal clustering is not merely a continuum spectral curiosity: absent such local competition, a strong subedge atom is visible on the actual CA staircase.

## 1. Algebraic strength already forces near-edge, polynomial-height location

The bracket in (1) is uniformly comparable to its leading term. Indeed,

\[
\frac{
(-1)^k k!/[u^k(1-\rho)^{k+1}]
}{
1/[\rho(1-\rho)]
}
=
(-1)^k k!\,
\frac{\rho}{u^k(1-\rho)^k}.
\tag{11}
\]

On the fixed strip `sigma_0<=beta<Theta`, every nontrivial zeta zero has ordinate bounded away from zero, so

\[
\frac{\rho}{(1-\rho)^k}=O_{k,\sigma_0,\Theta}(1)
\qquad(k\ge1).
\]

Therefore, uniformly over all packet zeros and `u>=1`,

\[
\boxed{
 a_{\rho,K}(u)
=
\frac{e^{-\delta_\rho u}}{\rho(1-\rho)}
\left(1+O_K(u^{-1})\right).
}
\tag{12}
\]

In particular,

\[
|a_{\rho,K}(u)|
\asymp_K
\frac{e^{-\delta_\rho u}}{1+\gamma^2}
\tag{13}
\]

for large `u`.

The strong-atom hypothesis (4) therefore implies two useful restrictions without any additional zero-density theorem:

\[
\boxed{
\delta_{\rho_0}
\ll_A
\frac{\log U}{U},
\qquad
|\gamma_0|
\ll_A
U^{A/2}.
}
\tag{14}
\]

The first says that an atom visible at algebraic scale must already lie in the shrinking horizontal boundary layer isolated by `RE-121`--`RE-122`. The second is stronger than the aggregate polynomial-height statement when one asks for a **single** zero to carry the full `U^-A` amplitude: reciprocal-square weighting forces its ordinate to be at most `U^(A/2)` up to constants.

Equation (14) is only a single-atom statement. An order-`U^-A` packet may still be assembled from many individually smaller coefficients at higher ordinates; that diffuse regime remains live.

## 2. A band-limited matched filter isolates one ordinate

Choose a real even Schwartz function `phi` whose Fourier transform satisfies

\[
\widehat\phi(\xi)=1
\quad(|\xi|\le1/2),
\qquad
\widehat\phi(\xi)=0
\quad(|\xi|\ge1),
\tag{15}
\]

with Fourier convention

\[
\widehat\phi(\xi)
=
\int_{\mathbb R}\phi(t)e^{-i\xi t}\,dt.
\]

Such a function is obtained by taking any smooth compactly supported frequency cutoff equal to one near the origin and Fourier-inverting it. In particular,

\[
\int_{\mathbb R}\phi(t)\,dt=1.
\]

Set

\[
L:=U^{1-\eta},
\qquad
H:=U^{1-\eta/2},
\qquad
\phi_L(t):=L^{-1}\phi(t/L).
\tag{16}
\]

Consider the demodulated packet average

\[
I_{\rho_0}(U)
:=
\int_{1-U}^{\infty}
\phi_L(t)
\mathcal S_K(U+t)
 e^{-i\gamma_0(U+t)}\,dt.
\tag{17}
\]

Because the packet is absolutely convergent, uniformly for `u>=1`, termwise integration is legitimate. The reciprocal-square coefficient in (12) and the ordinary zero count give

\[
\sum_{\rho}
\frac1{1+\gamma^2}<\infty,
\tag{18}
\]

and hence

\[
\sup_{u\ge1}|\mathcal S_K(u)|<\infty.
\tag{19}
\]

Schwartz decay then localizes (17) to `|t|<=H`. For every fixed `M`,

\[
\int_{|t|>H}|\phi_L(t)|\,dt
\ll_M
\left(\frac LH\right)^M
=
U^{-M\eta/2}.
\tag{20}
\]

Taking `M` large compared with `A/eta`, the contribution outside the interval in (5) is `o(U^-A)`.

The crucial gain over a pointwise phase comparison is that the filter has an **exact compact frequency window**. After Taylor-freezing the slowly varying amplitudes, every mode whose ordinate differs from `gamma_0` by more than `1/L=U^(-1+eta)` vanishes identically under the filter.

## 3. Horizontal damping drifts slowly enough to preserve algebraic localization

It remains to justify Taylor-freezing the amplitudes in (17) to algebraic accuracy. Fix a large constant `D`. Split packet zeros into

\[
\delta_\rho
\le
D\frac{\log U}{U}
\tag{21}
\]

and its complement.

For the complement, throughout `|t|<=H=o(U)`,

\[
e^{-\delta_\rho(U+t)}
\le
U^{-D+o(1)}.
\]

Using (18), its total contribution to (17) is `O(U^(-D+o(1)))`; choose `D>A+2`.

For zeros satisfying (21), differentiate only the slowly varying amplitude `a_{rho,K}(u)`, leaving `e^(i gamma u)` untouched. From (1) one obtains, for every fixed integer `m>=0` and `u=U+O(H)`,

\[
|a_{\rho,K}^{(m)}(u)|
\ll_{K,m,D}
\frac{e^{-\delta_\rho U}}{1+\gamma^2}
\left(\frac{\log U}{U}\right)^m.
\tag{22}
\]

Taylor-expand at `U` to order `M-1`. Summing the remainders over all zeros by (18) gives

\[
\ll_{K,M,D}
\left(
H\frac{\log U}{U}
\right)^M
=
\left(
U^{-\eta/2}\log U
\right)^M
=o(U^{-A})
\tag{23}
\]

once `M` is fixed sufficiently large.

For each Taylor monomial, replacing the truncated `|t|<=H` integral by the whole-line integral also costs `o(U^-A)` by Schwartz decay. The resulting Fourier integrals are

\[
\int_{\mathbb R}
\phi_L(t)t^m e^{i(\gamma-\gamma_0)t}\,dt,
\tag{24}
\]

which are derivatives of `\widehat\phi(L(\gamma-\gamma_0))`. Hence every term in (24) vanishes when

\[
|\gamma-\gamma_0|>L^{-1}=U^{-1+\eta}.
\tag{25}
\]

For the target itself, `gamma=gamma_0`; because `\widehat\phi` is identically one near zero, every derivative of positive order vanishes at zero. Thus the target contributes exactly

\[
a_{\rho_0,K}(U)+o(U^{-A}).
\tag{26}
\]

All surviving non-target Taylor terms come from the cluster (3). Equation (22), together with `L(log U)/U=U^{-eta}log U=o(1)` and the comparability (12), bounds their combined contribution by

\[
\ll_{A,K,\eta}
\sum_{\rho\in\mathcal C_\eta(\rho_0;U)}
|a_{\rho,K}(U)|.
\tag{27}
\]

Finally,

\[
|I_{\rho_0}(U)|
\le
\|\phi\|_1
\sup_{|u-U|\le H}|\mathcal S_K(u)|
+o(U^{-A}),
\tag{28}
\]

and (5) follows from (26)--(28).

The proof uses no lower bound for gaps between zeta zeros. It instead identifies exactly what the absence of such a gap would have to accomplish.

## 4. What cancellation is still allowed

### An isolated strong atom

If

\[
\mathcal C_\eta(\rho_0;U)=\varnothing,
\]

then (5) immediately gives (7). Thus a single strong near-edge mode separated from every other positive ordinate by more than `U^(-1+eta)` forces an algebraic packet excursion.

### A weak neighboring cloud

Isolation is not required. If neighboring modes exist but their total coefficient mass is `o(|a_{rho_0,K}(U)|)`, the same conclusion holds. To hide the target, the cluster must carry **comparable absolute coefficient mass**. Mere proximity of an arbitrarily tiny zero contribution is insufficient.

### Multiplicity

A multiple zero is automatically represented by repeated atoms at the same ordinate and therefore falls inside the cluster alternative. This does not mean multiplicity cancels the target; identical copies reinforce one another. Equation (5) supplies a necessary clustering condition, not a sufficient cancellation mechanism.

### Diffuse algebraic mass

The result does not show that every order-`U^-A` packet contains a single order-`U^-A` atom. Many smaller coefficients can combine coherently. That diffuse regime is now a separate, explicit escape route rather than being mixed with single-mode cancellation.

### Why the scale is near reciprocal rather than merely inverse-polylogarithmic

The admissible filter length is almost linear in the phase: `L=U^(1-eta)`. Horizontal damping of every algebraically relevant zero is only `O(log U/U)`, so over that filter length it changes by `O(U^-eta log U)`, and arbitrary fixed algebraic accuracy is recovered by finite Taylor expansion. This is what improves the localization from the inverse-polylogarithmic scale suggested by a short window to

\[
|\Delta\gamma|\lesssim U^{-1+\eta}.
\]

The proof does **not** reach an exact `O(1/U)` window. At filter length comparable with `U`, the damping variation of a boundary-layer zero is no longer algebraically small, and the fixed-order Taylor argument loses its separating power. Therefore `U^(-1+o(1))` is a genuine boundary of the present argument, not shorthand for a proved `1/U` gap theorem.

## 5. Transfer to the CA staircase

Suppose (6) holds along an unbounded sequence `U_j` and that `A<K+1`. Equation (7) gives phases `u_j` satisfying

\[
|u_j-U_j|\le U_j^{1-\eta/2},
\qquad
|\mathcal S_K(u_j)|\gg U_j^{-A}.
\tag{29}
\]

Since `u_j~U_j`, apply the local superalgebraic phase-covering statement of `RE-123` around each `u_j`. There are regular CA states `C_j` with

\[
|\nu_{C_j}-u_j|
\ll
 e^{-u_j/2}u_j^{3/2}
\tag{30}
\]

and

\[
\mathcal S_K(\nu_{C_j})
=
\mathcal S_K(u_j)+o(U_j^{-A}).
\tag{31}
\]

`RE-121` supplies

\[
R_K(\nu_{C_j})
=
\mathcal S_K(\nu_{C_j})
+O(U_j^{-K-1}),
\tag{32}
\]

so (10) follows when `A<K+1`.

This is the key splice with the arithmetic selector. `RE-123` removed sparse CA placement as an obstruction once a continuum excursion exists; `RE-124` now shows that a strong single spectral atom creates such an excursion unless the zero set supplies near-reciprocal competing mass.

## 6. Representation and adversarial audit

The source data are unchanged: the subedge zeros already present in `mathcal S_K`. The matched filter is only a linear readout of that same absolutely convergent packet. It does not manufacture an independent arithmetic coordinate, and (5) is invariant under rewriting the packet in any equivalent zero-sum notation.

The main adversarial checks are as follows.

First, the derivative of the **full untruncated packet** is not used. `RE-123` already noted that the absolute derivative majorant would contain `sum 1/|gamma|`, which diverges. Here the oscillation `e^(i gamma u)` is kept exact inside a band-limited Fourier filter; only the slowly varying damping/amplitude is differentiated. Its derivatives retain the reciprocal-square summability in (22).

Second, no zero-spacing hypothesis enters. Near-collisions are explicitly retained in the cluster term of (5), and exact multiplicities are retained as repeated atoms.

Third, the proof does not infer a signed lower bound from the positive boundary-mass envelope `W(t)`. The lower bound is conditional on one actual complex coefficient being algebraically large and locally dominant. This avoids reversing the one-sided envelope argument of `RE-121`.

Fourth, the CA consequence respects the fixed-`K` quantifier. One first fixes `A<K+1` and `K`, derives the continuum excursion, and only then invokes `RE-123`; there is no all-orders or `K=K(U)` claim.

A separate adversarial review of the frequency support, horizontal split, Taylor remainder, multiplicity case, and CA transfer found no material objection, so no `.review.md` sidecar is opened.

## 7. Prior-art boundary

The harmonic-analysis mechanism itself is classical. Smooth frequency localization, Turan/Ingham-style extraction of oscillation from zeta zeros, and zero-spacing/zero-detection arguments are established techniques. In particular, Schlage-Puchta's work on oscillations of the prime-number-theorem error shows how an individual zeta zero can force a localized arithmetic oscillation, while Maynard--Pratt's *Half-Isolated Zeros and Zero-Density Estimates* studies detectors sensitive to vertical isolation of zeta zeros.

Those results bound the novelty claim here. `RE-124` does **not** claim a new general zero-isolation theorem or a new oscillation principle for `psi(x)-x`. The line-specific content is the quantitative splice with the already-derived nonisolated Robin/CA packet:

1. the relevant coefficient has reciprocal-square zero weight;
2. algebraic visibility forces horizontal drift only `O(log U/U)`;
3. this permits a band-limited filter of length `U^(1-eta)` while retaining arbitrary fixed algebraic accuracy;
4. `RE-123` then transfers the resulting continuum excursion to actual regular CA phases.

A targeted search found no prior theorem asserting this near-reciprocal ordinate-clustering necessity for the finite-edge Robin/CA residual. No external theorem beyond standard Fourier localization and the already-anchored ordinary zero count is load-bearing, so `SOURCES.md` does not require an additional dependency.

## 8. Consequence for the finite-edge frontier

`RE-122` says an algebraic anomaly requires polynomial-height approach to the attained edge. `RE-123` says arithmetic CA placement cannot miss an algebraic continuum excursion. `RE-124` now separates the surviving internal-cancellation problem into two genuinely different geometries.

If the algebraic mass is carried by an individually strong zero, then hiding it requires comparable subedge coefficient mass in ordinate windows of width `U^(-1+eta)` for every fixed `eta>0`; ordinary distant-frequency cancellation is impossible. If no strong atom exists, then the anomaly source must instead be a diffuse packet of many individually smaller modes.

Thus the next source question is no longer simply whether the signed packet cancels. It is whether polynomial-height near-edge zeros can support either **near-reciprocal ordinate clusters with enough comparable weight to cancel strong atoms**, or a **diffuse many-mode configuration** whose collective signed sum remains small despite nontrivial positive boundary mass. Neither mechanism is controlled by the current finite-edge representation.