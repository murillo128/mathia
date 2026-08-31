# WP-060 — Prym untwisted analytic-torsion completion erases the determinant-line prime scale

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT` for the most canonical analytic-torsion completion of the positive Prym determinant-line carrier isolated in `WP-058`. For the old-prime Prym

\[
P=P_{n,p},\qquad g_n>0,
\]

`WP-058` shows that the polarization metric on

\[
\Lambda=H_1(P,\mathbf Z)
\]

has

\[
\operatorname{covol}_{g_E}\Lambda=p^{g_n},
\qquad
\frac1{g_n}\log\operatorname{covol}_{g_E}\Lambda=\log p.
\]

A natural attempt to obtain the missing archimedean/global correction from the *same polarized manifold* is to pass from this degree-one determinant line to the determinant of its full de Rham or Dolbeault complex and equip that determinant with Ray--Singer/Quillen analytic torsion. For these Pryms the canonical untwisted route collapses exactly.

Let

\[
d=\dim_{\mathbf C}P=(p-1)(g_n+1),
\qquad N=\dim_{\mathbf R}P=2d.
\]

Since `g_n>0`, one has `d>=2`. Then:

1. the de Rham Ray--Singer analytic torsion of the closed even-dimensional flat torus `(P,g_E)` is exactly `1`;
2. more strongly, the natural integral generator of the full de Rham determinant line
   \[
   \det H^\bullet(P,\mathbf R)
   :=\bigotimes_{q=0}^{N}(\det H^q(P,\mathbf R))^{(-1)^q}
   \]
   has `L^2` norm exactly `1`, so the `p^{g_n}` volume stored in `det H^1` cancels algebraically across exterior degrees before analytic torsion can add anything;
3. the untwisted holomorphic analytic torsion of the flat complex torus is also exactly `1`, because the `(0,q)` Laplacians have the same nonzero scalar spectrum with multiplicity `binom(d,q)` and
   \[
   \sum_{q=0}^{d}(-1)^q q\binom dq=0
   \qquad(d>1).
   \]

Thus the strongest standard *untwisted* determinant-of-cohomology completion of `WP-058` does not turn its positive determinant-line norm into a global finite--archimedean object. It actually removes the prime-scale determinant in the de Rham determinant line and contributes no holomorphic torsion correction in the Quillen direction. A nontrivial analytic-torsion escape must introduce additional twisting/bundle/family/boundary data before the determinant is formed. That is a genuine change of object, and positivity of the resulting Hermitian/Quillen norm does not by itself supply the linear Weil quadratic sign.

## 1. The `WP-058` polarized Prym is a flat even-dimensional torus

Keep the old-prime cover from `WP-055`--`WP-059`,

\[
f:C_{pn}\longrightarrow C_n,
\qquad p\mid n,
\]

and assume

\[
g:=g_n=\frac{\varphi(n)-2}{2}>0.
\]

Its Prym variety

\[
P=P_{n,p}
\]

has complex dimension

\[
\boxed{d=(p-1)(g+1).}
\tag{1}
\]

The induced polarization gives a Riemann form `E` on

\[
\Lambda=H_1(P,\mathbf Z),
\qquad V=\Lambda\otimes\mathbf R,
\]

and the compatible positive metric

\[
g_E(v,w)=E(v,Jw).
\tag{2}
\]

Because `g_E` is constant on `V` and `P=V/\Lambda`, it descends to a translation-invariant Kähler metric on the abelian variety. In particular `(P,g_E)` is a closed flat Riemannian torus of real dimension

\[
\boxed{N=2d.}
\tag{3}
\]

`WP-058` proves from the polarization type that

\[
\boxed{
\operatorname{Vol}(P,g_E)
=\operatorname{covol}_{g_E}\Lambda
=p^g.
}
\tag{4}
\]

Thus `log p` is genuinely present in a positive metric determinant:

\[
\log p=\frac1g\log\operatorname{Vol}(P,g_E).
\tag{5}
\]

The question tested here is whether the canonical determinant-of-cohomology/analytic-torsion package of this *same metric manifold* upgrades (5) into a nontrivial archimedean completion.

There is an important dimension constraint already built into the old-prime carrier. Since `g>=1` and `p>=2`,

\[
\boxed{d=(p-1)(g+1)\ge2.}
\tag{6}
\]

The elliptic-curve case `d=1`, where holomorphic torsion is famously nontrivial, never occurs in the positive-genus Prym regime that carries the `WP-056`/`WP-058` discriminant.

## 2. The full de Rham determinant line cancels the `p^g` lattice volume exactly

The cancellation can be proved before invoking any zeta regularization.

Let `G` be the Gram matrix of `g_E` in an integral basis

\[
e_1,\ldots,e_N
\]

of `Lambda`. Then

\[
\sqrt{\det G}=\operatorname{Vol}(P,g_E)=:V_P.
\tag{7}
\]

Let

\[
e^1,\ldots,e^N
\]

be the dual integral basis of `H^1(P,Z)`. Since harmonic forms on a flat torus are constant, the pointwise Gram matrix of this basis is `G^{-1}`. On `q`-forms the pointwise Gram operator is the exterior power `\bigwedge^qG^{-1}`. Integrating over `P` multiplies the Gram matrix by the scalar `V_P`, hence

\[
\det G_{L^2,q}
=V_P^{\binom Nq}
\det\!\left(\bigwedge^qG^{-1}\right).
\tag{8}
\]

For an `N x N` positive matrix `A`,

\[
\det(\bigwedge^qA)
=(\det A)^{\binom{N-1}{q-1}},
\tag{9}
\]

with the exponent interpreted as `0` at `q=0`. Since

\[
\det G^{-1}=V_P^{-2},
\]

(8)--(9) give

\[
\boxed{
\left\|
\det(e^{i_1}\wedge\cdots\wedge e^{i_q})
\right\|_{L^2}
=V_P^{\frac12\binom Nq-\binom{N-1}{q-1}}.
}
\tag{10}
\]

Now take the alternating determinant line

\[
\lambda_{dR}(P)
:=\bigotimes_{q=0}^{N}
(\det H^q(P,\mathbf R))^{(-1)^q}
\tag{11}
\]

and its natural integral generator `omega_Z` obtained from the exterior-power integral bases. Its `L^2` norm is a power of `V_P` with exponent

\[
\begin{aligned}
A_N
&=\sum_{q=0}^{N}(-1)^q
\left[
\frac12\binom Nq-\binom{N-1}{q-1}
\right]\\
&=\frac12(1-1)^N
+\sum_{r=0}^{N-1}(-1)^r\binom{N-1}{r}.
\end{aligned}
\tag{12}
\]

For every `N>1`, both binomial sums vanish. Therefore

\[
\boxed{
A_N=0,
\qquad
\|\omega_{\mathbf Z}\|_{L^2}=1.
}
\tag{13}
\]

In particular, inserting the exact Prym volume (4),

\[
\boxed{
\|\omega_{\mathbf Z}\|_{L^2}
=(p^g)^0=1.
}
\tag{14}
\]

This is the key same-object obstruction. The positive degree-one determinant line of `WP-058` has norm `p^g`, but the canonical full cohomological determinant does **not** inherit that scale. The exterior algebra required by de Rham cohomology cancels it exactly.

No choice of basis is responsible for (13): the integral determinant generator changes only by sign under unimodular changes, while the calculation depends only on the covolume. The same cancellation holds for every metric flat torus of dimension `N>1`, not just for the cyclotomic Prym.

## 3. Ray--Singer analytic torsion contributes no missing spectral factor

The natural spectral correction to the `L^2` determinant line is Ray--Singer analytic torsion. Let `Delta_q` be the Hodge Laplacian on `q`-forms and let

\[
\zeta_q(s)
=\operatorname{Tr}'(\Delta_q^{-s})
\tag{15}
\]

be its spectral zeta function with zero modes omitted. In the standard convention,

\[
\log T_{RS}(P,g_E)
=\frac12\sum_{q=0}^{N}(-1)^q q\,\zeta_q'(0).
\tag{16}
\]

Because `N=2d` is even, Hodge star identifies the positive spectra in degrees `q` and `N-q`:

\[
\zeta_q(s)=\zeta_{N-q}(s).
\tag{17}
\]

On the other hand, on every positive eigenspace of the de Rham Laplacian the de Rham complex is exact, so the alternating multiplicity vanishes. Equivalently,

\[
\sum_{q=0}^{N}(-1)^q\zeta_q(s)=0.
\tag{18}
\]

Replacing `q` by `N-q` in the sum in (16) and using evenness of `N` gives

\[
2\sum_q(-1)^q q\zeta'_q(0)
=N\sum_q(-1)^q\zeta'_q(0)=0.
\tag{19}
\]

Hence

\[
\boxed{T_{RS}(P,g_E)=1.}
\tag{20}
\]

This is the classical even-dimensional Ray--Singer cancellation, here specialized to the actual Prym geometry. Combining (13) and (20), the Ray--Singer metric on the full de Rham determinant line has

\[
\boxed{
\|\omega_{\mathbf Z}\|_{RS}=1.
}
\tag{21}
\]

Thus the canonical real analytic-torsion completion does not merely fail to add the Riemann archimedean factor. It has **zero logarithmic response altogether** on the natural integral determinant generator:

\[
\log\|\omega_{\mathbf Z}\|_{RS}=0.
\tag{22}
\]

The exact prime scale (5) has been erased by the cohomological determinant, and the spectral correction is identically trivial.

The conclusion is unchanged for the usual even-dimensional unitary-flat Ray--Singer torsion factor: Hodge duality and positive-spectrum supersymmetric cancellation are structural, not arithmetic.

## 4. The untwisted holomorphic/Quillen spectral correction is also trivial because `d>=2`

The most obvious complex-geometric escape is to use the Dolbeault determinant and its Quillen metric rather than the real de Rham determinant. For the *untwisted* Prym this also collapses exactly.

On the flat complex torus `(P,g_E,J)`, the Dolbeault Laplacian on `(0,q)`-forms with coefficients in the trivial holomorphic line acts componentwise on constant exterior directions. Thus its nonzero spectral zeta function has the form

\[
\boxed{
\zeta_{0,q}(s)=\binom dq\,\zeta_{0,0}(s).
}
\tag{23}
\]

The holomorphic analytic torsion is the corresponding weighted determinant,

\[
\log T_{hol}
=\frac12\sum_{q=0}^{d}(-1)^q q\,\zeta_{0,q}'(0)
\tag{24}
\]

(up to the harmless global convention on sign/factor). Substituting (23),

\[
\log T_{hol}
=\frac12\zeta_{0,0}'(0)
\sum_{q=0}^{d}(-1)^q q\binom dq.
\tag{25}
\]

But

\[
\sum_{q=0}^{d}(-1)^q q\binom dq
=-d(1-1)^{d-1}.
\tag{26}
\]

By (6), `d>=2`, so

\[
\boxed{T_{hol}(P,\mathcal O_P)=1.}
\tag{27}
\]

Thus the analytic-torsion factor entering the Quillen metric of the trivial holomorphic determinant supplies no nontrivial archimedean spectral term either.

The dimension hypothesis is essential and provides an internal control. For a complex elliptic curve `d=1`, (26) is nonzero and the Quillen/holomorphic torsion is genuinely sensitive to the lattice. But `d=1` cannot occur in the `g>0` old-prime Prym regime: the smallest possible dimension is `2`. At the genus-zero base levels where a one-dimensional covering Jacobian can occur, `WP-056` already proves that the Prym polarization discriminant carrying `log p` is absent. Therefore the only dimension in which untwisted torus holomorphic torsion could escape the binomial cancellation is precisely a regime where the finite `WP-058` carrier is unavailable.

## 5. Why this does not rule out every Quillen/torsion construction

The result is deliberately about the **canonical untwisted completion** of the actual positive Hodge/determinant carrier. Holomorphic analytic torsion can be nontrivial after adding extra data, for example a non-flat positive holomorphic line bundle, a family parameter, a boundary condition, or a nonunitary/refined complex. Bismut--Gillet--Soulé's theory of Quillen metrics and its anomaly formulas is precisely the broad classical framework for such determinant-line spectral corrections.

Those escapes are genuine but no longer automatic consequences of `WP-058`.

The Prym polarization does supply a distinguished ample line bundle up to the usual polarization data, so twisting by the polarization is a particularly natural next candidate. But once the Dolbeault complex is twisted, one has changed the operator whose determinant is being measured. A nontrivial Quillen norm then says that a one-dimensional determinant line has a positive Hermitian metric; it does **not** imply that its logarithm, curvature, arithmetic degree, or a relative log-determinant has a fixed sign. Both a Hermitian line and its dual carry positive norms while their logarithmic degrees are opposite.

Moreover, a fixed twisted determinant on `P_{n,p}` has no Riemann test-variable `s` and no intrinsic reason to produce the independently identified `Gamma_R(s)`/digamma channel of `WP-036` and `WP-048`. Producing that channel would require an additional canonical family or scaling action. If such a family is found, it must be audited as a new coupled mechanism rather than treated as something guaranteed by the word "Quillen" or by positivity of a Hermitian metric.

So the surviving torsion route has a sharper proof obligation:

\[
\boxed{
\text{new intrinsic twist/family/coupling}
\ \Longrightarrow\ 
\text{nontrivial determinant response}
\ \Longrightarrow\ 
\text{Weil finite+archimedean form},
}
\]

with the final sign proved independently. The first arrow is not available from the untwisted Prym geometry, and the second is not a consequence of determinant-line positivity.

## 6. Matched controls

Three controls prevent overinterpretation.

### Arbitrary polarized flat tori

Equations (7)--(22) use only that `P` is a closed flat torus of real dimension `N>1`. Replace the cyclotomic Prym by any lattice `Lambda` in a Euclidean vector space, with any covolume `V`. The full de Rham determinant still has integral `L^2` norm `1`, and the even-dimensional Ray--Singer torsion is still `1`.

Hence this completion is maximally insensitive to the arithmetic origin of the volume. It cannot distinguish `V=p^g` from an arbitrary positive real covolume.

### Arbitrary flat complex tori of dimension greater than one

Equation (27) uses only the componentwise flat Dolbeault spectrum and `d>1`. The same untwisted holomorphic torsion cancellation occurs on every flat complex torus of complex dimension at least two. Cyclotomic structure, prime degree, and Prym polarization type play no role.

### Genus-zero old-prime boundary

At `g=0`, the polarization-kernel/covolume mechanism of `WP-056`--`WP-058` stores no `p`. This blocks the only tempting low-dimensional exception: even if an elliptic covering Jacobian has nontrivial holomorphic torsion, there is no `p^g` discriminant carrier there to combine with it. The two ingredients never coexist in the canonical old-prime construction.

## 7. Prior art and novelty boundary

No historical novelty is claimed for analytic torsion, Quillen metrics, or the even-dimensional cancellations.

- D. B. Ray and I. M. Singer, *R-torsion and the Laplacian on Riemannian manifolds*, Advances in Mathematics **7** (1971), 145--210, DOI `10.1016/0001-8708(71)90045-4`, introduced analytic torsion from zeta-regularized de Rham Laplacians and established its classical metric/topological framework. The even-dimensional triviality is a standard Hodge-duality consequence of the definition.
- D. B. Ray and I. M. Singer, *Analytic torsion for complex manifolds*, Annals of Mathematics **98** (1973), 154--177, DOI `10.2307/1970909`, develops the complex/holomorphic analytic-torsion setting used in the Dolbeault comparison.
- Jean-Michel Bismut, Henri Gillet, and Christophe Soulé, *Analytic torsion and holomorphic determinant bundles. III. Quillen metrics on holomorphic determinants*, Communications in Mathematical Physics **115** (1988), 301--351, DOI `10.1007/BF01466774`, is the standard determinant-bundle/Quillen-metric and anomaly-formula framework relevant to any twisted escape.

The Mathia-specific content is the collision of those classical constructions with the strongest current Prym finite-prime carrier. `WP-058` moved `log p` from finite torsion into an honest positive metric determinant line. The present calculation shows that the most canonical move from that line to the full cohomological determinant **annihilates its volume scale exactly**, while both real Ray--Singer and untwisted holomorphic torsion add no compensating spectral factor in the dimensions that actually occur.

This is distinct from `WP-019`. There the obstruction is a *decoupled* supersymmetric archimedean factor tensored with the Prime-Lattice Boolean supertrace. Here the supersymmetric cancellation occurs inside the actual polarized Prym manifold that carries `log p`, and the additional exterior-algebra calculation (12)--(14) shows that full cohomological determinant formation itself erases the stored prime scale before torsion is applied.

It is also distinct from `WP-043`/`WP-059`: those findings produce `log p` from a nontrivial positive cycle spectrum via a logarithmic determinant. Here the canonical untwisted analytic-torsion spectrum has the opposite behavior: its graded determinant is exactly trivial.

## 8. Falsification surface

The claim has short exact audit tests.

1. Verify the Prym dimension formula `d=(p-1)(g+1)` and hence `d>=2` for `g>0`.
2. Verify that the polarization metric of `WP-058` descends to a flat translation-invariant metric with volume `p^g`.
3. For an arbitrary flat `N`-torus, verify (8)--(10) and the exterior-power determinant identity (9).
4. Verify the two binomial cancellations in (12), giving unit `L^2` norm for the natural integral generator of `det H^bullet` whenever `N>1`.
5. Verify Hodge duality (17) and the positive-spectrum de Rham supertrace cancellation (18), giving `T_RS=1` in even dimension.
6. For the trivial holomorphic line on a flat complex `d`-torus, verify the multiplicity identity (23) and the binomial identity (26), giving `T_hol=1` for `d>1`.
7. Check the internal boundary: `d=1` is incompatible with `g>0`, while `g=0` removes the `WP-058` prime discriminant.

Items 1--7 are independent of RH, zeta zeros, analytic continuation of the Riemann zeta function, and any chosen Weil kernel.

## 9. Consequence for the Weil-positivity search

The Prym branch now has a sharper hierarchy:

\[
\begin{array}{rcl}
\text{polarization lattice defect}
&\xrightarrow{\text{WP-056}}&
\log p,\\[2mm]
\text{positive }\det H_1\text{ norm}
&\xrightarrow{\text{WP-058}}&
p^g,\\[2mm]
\text{theta action before positivity}
&\xrightarrow{\text{WP-059}}&
\text{cycle logdet},\\[2mm]
\text{full untwisted de Rham/Dolbeault determinant}
&\xrightarrow{\text{WP-060}}&
\boxed{1}.
\end{array}
\]

So ordinary determinant-line completion does not bridge the finite and archimedean jobs. The degree-one integral geometry is rich enough to remember the prime, but the most canonical full cohomological determinant is too symmetric and cancels it; the standard untwisted analytic-torsion corrections are correspondingly trivial.

A surviving Prym route must therefore introduce **nontrivial coupling before determinant formation**: a canonical polarization-twisted complex, relative family, boundary condition, correspondence, or other operator that simultaneously (i) retains the one-step `log p` and `p^{-k/2}` normalization, (ii) produces the `q=2` Riemann archimedean/polar response, and (iii) comes with a sign theorem stronger than positivity of a determinant-line norm. Merely placing a Quillen metric on a determinant line is not that theorem.

## Internal dependencies

- `research/weil_positivity/findings/WP-055-minimal-cyclotomic-double-cover-hodge-transfer-is-degree-flat.md`
- `research/weil_positivity/findings/WP-056-prym-polarization-stores-log-p-in-integral-discriminant.md`
- `research/weil_positivity/findings/WP-057-prym-discriminant-is-torsion-invisible-to-real-quadratic-positivity.md`
- `research/weil_positivity/findings/WP-058-prym-hodge-determinant-norm-exports-log-p-but-polarization-spectrum-is-flat.md`
- `research/weil_positivity/findings/WP-059-prym-heisenberg-adjoint-defect-is-cycle-laplacian-logdet.md`
- `research/weil_positivity/findings/WP-019-decoupled-supersymmetric-archimedean-completion-collapses-to-an-index.md`
- `research/weil_positivity/findings/WP-043-cycle-laplacian-shell-logdet-recovers-mangoldt-but-spectral-positivity-is-the-wrong-pairing.md`
- `research/weil_positivity/findings/WP-048-anchored-reflection-and-cycle-extremum-select-q2-riemann-gamma-channel.md`
