# PF-148 — square-resolvent trace class recovers a first-order Krein scattering phase by invariance

**Status:** `LITERATURE+DERIVED + EXACT-CONDITIONAL + CORRECTION/BOUNDARY`. PF-146 isolates the still-open global gate

\[
(P_1+1)^{-2}-(P_0+1)^{-2}\in\mathcal S_1
\]

for the exact prime flute and its exact all-composite shift clone. PF-147 correctly shows that this hypothesis forces the **first** relative resolvent into `S_2\setminus S_1`, so the direct bounded-resolvent pair lies in the `det_2`/Koplienko regime. The present finding records an important qualification: this does **not** mean that the same square-resolvent hypothesis lacks an ordinary Krein spectral-shift or Birman--Krein scattering phase. The trace-class pair of **squared** resolvents itself supplies such a first-order object, and the classical invariance principle transports it back to the original Laplacians. Thus PF-147's second-order statement is exact for the pair `((P_1+1)^{-1},(P_0+1)^{-1})`, but it is not the only canonical spectral-shift structure available under the stronger PF-146 hypothesis.

## Claim

Let `P_0,P_1 >= 0` be the two self-adjoint Laplacians after one fixed admissible common-Hilbert-space identification, and put

\[
R_i=(P_i+1)^{-1},
\qquad
B_i=R_i^2=(P_i+1)^{-2},
\qquad i=0,1.
\tag{1}
\]

Assume the still-open global PF-146 gate

\[
\boxed{B_1-B_0\in\mathcal S_1.}
\tag{2}
\]

Then:

1. The bounded self-adjoint pair `(B_1,B_0)` is an ordinary trace-class perturbation pair. It therefore has a Krein spectral-shift function `xi_B` and the usual trace-class perturbation determinant

\[
\boxed{
D_B(z)=
\det\!\left((B_1-z)(B_0-z)^{-1}\right)
=
\det\!\left(I+(B_1-B_0)(B_0-z)^{-1}\right)
}
\tag{3}
\]

for `z in rho(B_0)` in the standard determinant domain.

2. Let

\[
\phi(\lambda)=(1+\lambda)^{-2},
\qquad \lambda\ge0.
\tag{4}
\]

This is smooth and strictly decreasing. The standard spectral-shift invariance principle therefore defines a first-order spectral-shift function for the original unbounded pair by

\[
\boxed{
\xi_P(\lambda)
=-\xi_B(\phi(\lambda))
}
\tag{5}
\]

up to the usual normalization convention. The minus sign is exactly the orientation reversal caused by the decreasing change of variable.

3. Kato--Rosenblum gives complete wave operators for `(B_1,B_0)`, and Birman--Kato invariance transfers them to `(P_1,P_0)`. Moreover, the same monotone change of spectral variable transports the trace-class Birman--Krein phase. With the usual convention `S=W_+^*W_-`, decreasing `phi` interchanges `+` and `-`, so under the corresponding fiber identifications

\[
S_B(\phi(\lambda))\simeq S_P(\lambda)^*.
\tag{6}
\]

Consequently the original prime/shift scattering matrix has, for almost every energy in the absolutely continuous spectral representation where the scattering matrix is defined, an ordinary Fredholm determinant satisfying

\[
\boxed{
\det S_P(\lambda)
=
\exp\!\bigl(-2\pi i\,\xi_P(\lambda)\bigr).
}
\tag{7}
\]

Thus a proof of (2) would yield not only complete wave operators and the PF-147 Hilbert--Schmidt first-resolvent comparison, but also a canonical **first-order relative scattering phase** for the original Laplacians.

## 1. The trace-class object is the squared bounded transform

Equation (2) is already exactly the hypothesis required by ordinary Krein theory for the bounded operators `B_i`. No trace-class property of either `B_i` separately is needed. For `z in rho(B_0)`,

\[
(B_1-z)(B_0-z)^{-1}
=
I+(B_1-B_0)(B_0-z)^{-1},
\tag{8}
\]

and the perturbation of the identity is in `S_1`. Hence the ordinary Fredholm determinant in (3) exists. Likewise the Lifshits--Krein trace formula and a first-order SSF `xi_B` are available for the trace-class bounded pair.

This determinant is different from PF-147's

\[
\det{}_2\!\left(I+(R_1-R_0)(R_0-z)^{-1}\right).
\tag{9}
\]

PF-112 still forbids replacing `det_2` by `det_1` in (9), because `R_1-R_0 notin S_1`. What changes is that the stronger hypothesis (2) already provides the separate trace-class transform (3).

## 2. Spectral shift returns to the Laplacian by a monotone change of variable

Pushnitski's invariance-principle formulation makes the relevant point explicit: in applications one may have

\[
f(H)-f(H_0)\in\mathcal S_1
\tag{10}
\]

for a smooth monotone `f` even when `H-H_0` or the first resolvent difference is not trace class. The spectral-shift function for `(H,H_0)` is then defined from the trace-class pair `(f(H),f(H_0))` by the monotone change of variables. Resolvent powers are one of the standard examples.

Here `f=phi` from (4), and `phi` is decreasing. To fix the sign directly, let `g` be a suitable test function on the spectral interval of the `B_i` and write `h(lambda)=g(phi(lambda))`. The bounded-pair trace formula gives

\[
\operatorname{Tr}(g(B_1)-g(B_0))
=
\int g'(\mu)\xi_B(\mu)\,d\mu.
\tag{11}
\]

Changing variables `mu=phi(lambda)` reverses the orientation and produces

\[
\operatorname{Tr}(h(P_1)-h(P_0))
=
\int h'(\lambda)
\bigl[-\xi_B(\phi(\lambda))\bigr]\,d\lambda,
\tag{12}
\]

which is (5) in the invariant normalization.

Therefore the phrase in PF-147 that the bounded **first-resolvent pair** lies in a second-order rather than first-order regime must be read literally at that level. Under (2), the original Laplacian pair also has a classical first-order SSF **through the squared-resolvent transform**.

## 3. The same invariance gives an ordinary Birman--Krein phase

Because `B_1-B_0 in S_1`, the trace-class scattering theory of `(B_1,B_0)` gives complete wave operators and an on-shell scattering matrix with trace-class deviation from the identity almost everywhere. Its determinant obeys the classical Birman--Krein identity

\[
\det S_B(\mu)
=
\exp\!\bigl(-2\pi i\xi_B(\mu)\bigr).
\tag{13}
\]

The wave-operator invariance principle used already in PF-146 applies to the same strictly monotone `phi`. Since `phi` is decreasing,

\[
W_\pm(B_1,B_0)
=
W_\mp(P_1,P_0)
\tag{14}
\]

under the standard spectral identification. Consequently

\[
S_B(\phi(\lambda))
\simeq S_P(\lambda)^*,
\tag{15}
\]

and taking determinants in (13), together with (5), gives (7).

This is stronger than saying merely that `det_2` exists off spectrum. Gesztesy--Pushnitski--Simon show that an arbitrary Hilbert--Schmidt perturbation determinant can fail to have nontangential boundary values, as PF-147 records. That warning remains valid for the direct `det_2` object (9), but it is **not** an obstruction to the trace-class scattering determinant obtained from `(B_1,B_0)` under the additional global hypothesis (2).

## 4. What this changes, and what it does not

The corrected implication chain is

```text
global squared-resolvent S1
    -> trace-class bounded pair B_i=(P_i+1)^-2
    -> ordinary Krein SSF / det1 for the B-pair
    -> complete wave operators
    -> invariance-principle SSF and Birman-Krein phase for P_i

and independently

    -> first relative resolvent in S2 \ S1          [PF-147]
    -> direct first-resolvent det2 / Koplienko regime
```

The two determinant statements concern different bounded transforms and are not contradictory.

This does **not** prove the global hypothesis (2). PF-146 remains only a fixed-central-collar result; the thick body, collar/body transmission terms, localization commutators, and infinite assembly are still the unresolved operator gate.

It also does not prove meromorphic continuation of the scattering determinant, resonance correspondence, a Selberg/Ruelle product, a relative zeta determinant, or any relation to Riemann zeros. Equation (7) is an almost-everywhere scattering identity supplied by classical trace-class theory once (2) is known, not an analytic continuation theorem.

Finally, neither the **existence** of this phase nor the trace-class ideal membership can be a primality selector: the whole comparison is deliberately between the exact prime flute and the exact all-composite shift clone. The actual function `xi_P(lambda)` or `det S_P(lambda)` could still carry fine information about their relative geometry, but any RH-relevant claim would have to derive and audit that content rather than infer it from the existence of a canonical phase.

## 5. Prior art and novelty audit

No novelty is claimed for Krein spectral shift, Birman--Krein, Kato--Rosenblum, or the invariance principle.

- **A. Pushnitski**, *The spectral shift function and the invariance principle*, Journal of Functional Analysis 183 (2001), 269--320; arXiv:`math/9911182`, DOI `10.1006/jfan.2001.3751`. In the introduction, equations (1.8)--(1.9) explicitly treat the case where `f(H)-f(H_0) in S_1` for a monotone smooth `f`, define the SSF for the original pair by change of variables, and note resolvent powers as standard choices of `f`.
- **T. Kato**, *Wave operators and unitary equivalence*, Pacific Journal of Mathematics 15 (1965), 171--180, DOI `10.2140/pjm.1965.15.171`, is the classical wave-operator/invariance source already used in PF-146.
- The ordinary Birman--Krein formula for trace-class scattering pairs is classical; Pushnitski's paper recalls `det S(lambda)=exp(-2 pi i xi(lambda))` and develops the SSF/scattering invariance framework needed here.

Directed searches around resolvent-power-comparable pairs, higher-order spectral shift, relative trace formulas, and metric/Laplacian scattering found this mechanism as standard operator theory rather than a new hyperbolic theorem. The durable Mathia content is the **correction of the project-specific boundary**:

\[
\boxed{
(P_1+1)^{-2}-(P_0+1)^{-2}\in S_1
\quad\Longrightarrow\quad
\text{ordinary invariant Krein/Birman--Krein phase for }(P_1,P_0),
}
\tag{16}
\]

even though

\[
(P_1+1)^{-1}-(P_0+1)^{-1}\in S_2\setminus S_1.
\tag{17}
\]

That implication is classical after the correct bounded transform is chosen; it is not a novel spectral theorem for infinite-type hyperbolic surfaces.

## 6. Audit / falsification core

A later adversary can verify the finding without using prime-specific heuristics:

1. check that the hypothesis is the **global** trace-class difference `B_1-B_0 in S_1`, not PF-146's local Dirichlet-collar estimate;
2. apply ordinary trace-class perturbation theory to the bounded pair `(B_1,B_0)` and verify (3);
3. use Pushnitski's spectral-shift invariance principle with the strictly decreasing `phi(lambda)=(1+lambda)^-2`; the only convention-sensitive point is the minus sign in (5);
4. use Kato/Birman invariance for the wave operators and track the `+/-` interchange for decreasing `phi` to obtain (6);
5. apply Birman--Krein to the trace-class `B` pair and transport the determinant identity to obtain (7);
6. retain PF-112 and PF-147 unchanged at the level of the **first-resolvent bounded pair**: no ordinary `det_1` exists for (9), while `det_2` remains canonical there;
7. do not infer any continuation, resonance, zeta, or RH statement from the almost-everywhere phase.

A refutation would have to show that the standard invariance principle does not apply to the monotone squared-resolvent transform under (2), or that the claimed sign/fiber transport is inconsistent with the chosen scattering convention. Failure to prove the global gate (2) would leave PF-148 conditional rather than refute the operator-theoretic implication.

## Consequence for the research line

PF-146's global operator gate is more consequential than PF-147 alone suggested. If the exact prime/shift squared-resolvent difference can be assembled in `S_1`, the result would not merely show absolutely continuous equivalence and place the first relative resolvent in `S_2`; it would automatically create a classical relative spectral-shift/scattering phase for the original Laplacians through the monotone squared-resolvent transform.

This sharpens the next question without promoting a zeta analogue: **can the global `S_1` gate actually be proved, and if so does the resulting invariant phase reduce to summable geometric bookkeeping or retain any nontrivial nonlocal prime-gap dependence?**