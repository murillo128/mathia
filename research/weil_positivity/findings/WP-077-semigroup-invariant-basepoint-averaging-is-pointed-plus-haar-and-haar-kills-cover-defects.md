# WP-077 — Semigroup-invariant basepoint averaging is only pointed-plus-Haar, and the Haar branch kills the cover scale defects

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-HARMONICALLY-WEIGHTED-DIRICHLET + MATHIA-SPECIALIZATION`.

`WP-072`--`WP-076` isolate a strong Prime-Circle survivor at the distinguished boundary point `1`: the local Dirichlet form makes the exact Mangoldt boundary anchor bounded, normalized root covers force the critical `n^{-1/2}` half-weight, and the fixed-point Hardy coordinates produce positive inverse-scale defects with trace `log n`. The main unresolved issue after `WP-076` is whether one can globalize that pointed geometry before positivity so that different boundary/degree sectors interact nontrivially.

The most canonical positive globalization by **averaging the same local Dirichlet energies over boundary basepoints** is completely classifiable. Let `mu` be a Borel probability measure on the unit circle and define the harmonically weighted/local-average form

\[
\mathcal D_\mu(f,g)
:=
\int_{\mathbb T}
\left\langle
\frac{f(z)-f(\zeta)}{z-\zeta},
\frac{g(z)-g(\zeta)}{z-\zeta}
\right\rangle_{H^2}
\,d\mu(\zeta)
\tag{1}
\]

initially on analytic polynomials with zero constant term. Let

\[
P_n(\zeta)=\zeta^n,\qquad C_nf=f\circ P_n,\qquad V_n=n^{-1/2}C_n.
\]

Then:

1. the exact covariance law is
   \[
   \boxed{
   \mathcal D_\mu(C_nf,C_ng)
   =
   n\,\mathcal D_{(P_n)_*\mu}(f,g);
   }
   \tag{2}
   \]
2. consequently `V_n` is an isometry of one fixed form `D_mu` for every degree `n>=2` **if and only if**
   \[
   (P_n)_*\mu=\mu
   \qquad(n\ge2);
   \tag{3}
   \]
3. every probability measure satisfying (3) is exactly
   \[
   \boxed{
   \mu=a\,\delta_1+(1-a)m_{\mathbb T},
   \qquad 0\le a\le1,
   }
   \tag{4}
   \]
   where `m_T` is normalized Haar measure;
4. hence every positive measure-averaged local Dirichlet geometry compatible with the full root-cover semigroup is merely
   \[
   \boxed{
   \mathcal D_\mu
   =
   a\,\mathcal D_1+(1-a)\mathcal D_{\rm Haar}.
   }
   \tag{5}
   \]

The two extremal branches are already structurally exhausted in opposite ways. `a=1` is precisely the pointed geometry of `WP-072`--`WP-076`. For `a=0`, Haar averaging gives the classical Dirichlet seminorm

\[
\mathcal D_{\rm Haar}(f)
=
\sum_{k\ge1}k|a_k|^2
\qquad
\left(f(z)=\sum_{k\ge1}a_kz^k\right),
\tag{6}
\]

and the normalized covers become pure multiplicative shifts. In that branch the entire Jensen/resolvent defect mechanism of `WP-074`--`WP-076` vanishes identically: with the orthonormal basis `b_k=z^k/sqrt(k)` and `A b_k=k b_k`,

\[
V_n b_k=b_{nk},
\qquad
V_n^*AV_n=nA,
\tag{7}
\]

and for every real `c>-1`,

\[
\boxed{
nV_n^*(A+cI)^{-1}V_n
-
(A+c/n\,I)^{-1}
=0.
}
\tag{8}
\]

In particular,

\[
nV_n^*A^{-1}V_n-A^{-1}=0,
\tag{9}
\]

so there is no positive `log n` trace defect at all. The Haar branch also loses the bounded boundary anchor at `1`. Thus semigroup-compatible positive basepoint averaging gives no third mechanism between the already-pointed branch and a rotation-invariant branch that removes precisely the finite structures that made the pointed construction interesting.

This is a no-go only for **positive measure averaging of the existing local Dirichlet fibers with one fixed semigroup-compatible form**. It does not exclude a genuinely nonseparable cross-basepoint kernel, a matrix-valued/internal coupling, a quotient or compression, a cohomological object, or a finite--archimedean boundary interaction introduced before positivity.

## 1. Exact local covariance under a root cover

For `zeta in T`, write

\[
T_\zeta f(z)
:=
\frac{f(z)-f(\zeta)}{z-\zeta},
\qquad
\mathcal D_\zeta(f,g)
=
\langle T_\zeta f,T_\zeta g\rangle_{H^2}.
\]

For the degree-`n` power map,

\[
f(z^n)-f(\zeta^n)
=
(z^n-\zeta^n)
\left(T_{\zeta^n}f\right)(z^n),
\]

and

\[
\frac{z^n-\zeta^n}{z-\zeta}
=
\sum_{r=0}^{n-1}z^{n-1-r}\zeta^r.
\tag{10}
\]

If

\[
T_{\zeta^n}f(z)=\sum_{k\ge0}a_kz^k,
\]

then the right side of (10) times `T_{zeta^n}f(z^n)` occupies `n` disjoint residue classes modulo `n`; every coefficient multiplier `zeta^r` has modulus one. Hardy orthogonality therefore gives the exact sesquilinear identity

\[
\boxed{
\mathcal D_\zeta(C_nf,C_ng)
=
n\,\mathcal D_{\zeta^n}(f,g).
}
\tag{11}
\]

Integrating (11) against `mu` proves (2):

\[
\mathcal D_\mu(C_nf,C_ng)
=
n\int_{\mathbb T}\mathcal D_\eta(f,g)\,
d((P_n)_*\mu)(\eta).
\]

Thus invariance of `mu` under `P_n` is sufficient for `V_n=n^{-1/2}C_n` to be an isometry.

It is also necessary. For `k,l>=1`,

\[
T_\zeta z^k
=
\sum_{j=0}^{k-1}z^j\zeta^{k-1-j},
\]

so

\[
\boxed{
\mathcal D_\mu(z^k,z^\ell)
=
\min(k,\ell)
\int_{\mathbb T}\zeta^{k-\ell}\,d\mu(\zeta).
}
\tag{12}
\]

Hence the sesquilinear form determines every Fourier coefficient of `mu`. If `V_n` preserves the norm for all polynomials, complex polarization preserves the whole form; combining (2) and (12) forces `mu` and `(P_n)_*mu` to have identical Fourier coefficients, hence to be the same finite Borel measure. This proves the equivalence in (3).

So the invariance condition is not an optional symmetry assumption added after the calculation. It is exactly what is required if one wants **one positive averaged local-Dirichlet Hilbert geometry** on which all intrinsic root covers retain the `n^{-1/2}` isometric normalization of `WP-073`.

## 2. Common invariance under all power maps has only two extremal measures

Assume now that `mu` is a probability measure satisfying (3). Put

\[
c_r:=\int_{\mathbb T}\zeta^r\,d\mu(\zeta).
\]

For every integer `r>=2`, invariance under `P_r` gives

\[
c_1
=
\int_{\mathbb T}\zeta\,d\mu
=
\int_{\mathbb T}\zeta^r\,d\mu
=
c_r.
\tag{13}
\]

Thus every positive Fourier moment is the same number; write it `a=c_1`. Negative moments are its complex conjugate.

Now average the positive moments:

\[
a
=
\frac1N\sum_{r=1}^N c_r
=
\int_{\mathbb T}
\left(
\frac1N\sum_{r=1}^N\zeta^r
\right)
d\mu(\zeta).
\tag{14}
\]

The parenthesized Cesaro average is bounded in modulus by one, equals one at `zeta=1`, and tends to zero for every `zeta != 1`. Dominated convergence therefore gives

\[
\boxed{a=\mu(\{1\})\in[0,1].}
\tag{15}
\]

Set

\[
\nu:=\mu-a\delta_1.
\]

Then `nu` has total mass `1-a` and every nonzero Fourier coefficient of `nu` vanishes. By uniqueness of finite Borel measures from their Fourier coefficients,

\[
\nu=(1-a)m_{\mathbb T}.
\]

This proves (4).

The same conclusion already follows if covariance is required only for every prime degree: the prime power maps generate all integer power maps by composition. Thus the classification is aligned with the primitive-generator decomposition used elsewhere in the research line.

This is an exact convex-geometry boundary. Within positive measure averages of local Dirichlet fibers, the common root-cover invariant measures have only the two extremal points

\[
\delta_1,
\qquad
m_{\mathbb T}.
\]

There is no third diffuse semigroup-invariant boundary distribution carrying arithmetic structure.

## 3. Haar averaging is exactly the classical Dirichlet form

Let

\[
f(z)=\sum_{k\ge1}a_kz^k.
\]

Using (12) and the Haar moments

\[
\int_{\mathbb T}\zeta^{k-\ell}\,dm_{\mathbb T}(\zeta)
=
\mathbf 1_{k=\ell},
\]

one obtains

\[
\boxed{
\mathcal D_{\rm Haar}(f,g)
=
\sum_{k\ge1}k\,a_k\overline{b_k},
}
\tag{16}
\]

and hence (6). This is the classical rotation-invariant Dirichlet seminorm.

Let

\[
b_k:=\frac{z^k}{\sqrt k},
\qquad k\ge1.
\]

Then `(b_k)` is an orthonormal basis for the zero-constant Dirichlet Hilbert space. The normalized cover acts by

\[
V_nb_k
=
\frac1{\sqrt n}\frac{z^{nk}}{\sqrt k}
=
\frac{z^{nk}}{\sqrt{nk}}
=
b_{nk}.
\tag{17}
\]

Thus the Haar globalization turns the pointed block-replication representation of `WP-073` into the bare multiplicative shift

\[
\boxed{b_k\longmapsto b_{nk}.}
\tag{18}
\]

Its range projection is simply

\[
P_n b_k
=
\mathbf 1_{n\mid k}b_k,
\]

so

\[
P_mP_n=P_{\operatorname{lcm}(m,n)}.
\tag{19}
\]

All of these projections commute. The globalized boundary representation is therefore flat divisibility geometry of the same broad multiplicative-shift type already classicalized in `WP-012`; averaging has not created a noncommuting or cross-prime interaction.

## 4. The mechanism that produced `log n` disappears identically

The important point is not merely that the Haar norm is classical. The exact **positive anomaly** discovered in `WP-074` vanishes.

On the basis `(b_k)`, define the canonical frequency operator

\[
A b_k=k b_k.
\tag{20}
\]

Equation (17) gives

\[
V_n^*AV_n=nA.
\tag{21}
\]

Among affine shifts `A+cI`, exact pure degree covariance

\[
V_n^*(A+cI)V_n=n(A+cI)
\]

for any `n>1` forces `c=0`. Thus the Haar geometry selects spectral origin zero, whereas the pointed block geometry of `WP-074` selected `L=N+1/2` from the nonzero mean of its residue block.

More decisively, for any real `c>-1`,

\[
V_n^*(A+cI)^{-1}V_n\,b_k
=
\frac1{nk+c}b_k,
\]

and hence

\[
nV_n^*(A+cI)^{-1}V_n\,b_k
=
\frac1{k+c/n}b_k
=
(A+c/n\,I)^{-1}b_k.
\]

This proves the zero-defect identity (8).

Therefore the whole shifted-resolvent family corresponding to `WP-075` collapses:

```text
pointed D_1 geometry:
    cover -> block average over n residue classes
    strict Jensen defect -> positive trace class
    trace at c=0 -> log n
    shifted trace -> log n + digamma coboundary

Haar/global Dirichlet geometry:
    cover -> pure frequency dilation k -> nk
    no internal residue average
    Jensen defect -> exactly zero
    no log n trace
    no digamma remainder
```

The same holds for inverse powers. For every `alpha>0`,

\[
n^\alpha V_n^*A^{-\alpha}V_n-A^{-\alpha}=0.
\tag{22}
\]

So Haar averaging does not merely fail to improve the `WP-076` cocycle. It removes the block variance from which that cocycle and its positive trace defect arose.

This also gives a useful interpretation of `WP-074`. Its `log n` was not an invariant of the abstract cover degree alone. It measured a **pointed residue-class anomaly** in the fixed-basepoint Hardy coordinates. Once the boundary point is globalized by Haar averaging, the same cover becomes exact dilation and the anomaly vanishes.

## 5. Haar globalization also loses the bounded Mangoldt anchor

The second finite survivor of the pointed geometry disappears at the same endpoint.

Consider

\[
f_N(z)=\sum_{k=1}^N\frac{z^k}{k}.
\]

Then

\[
\mathcal D_{\rm Haar}(f_N)
=
\sum_{k=1}^N\frac1k
=
H_N,
\tag{23}
\]

while

\[
f_N(1)=H_N.
\tag{24}
\]

Consequently

\[
\frac{|f_N(1)|}
{\sqrt{\mathcal D_{\rm Haar}(f_N)}}
=
\sqrt{H_N}
\longrightarrow\infty.
\tag{25}
\]

Boundary evaluation at `1` is therefore unbounded in the Haar Dirichlet seminorm. Adding the standard `H^2` term does not repair this example, because

\[
\|f_N\|_{H^2}^2
=
\sum_{k=1}^N\frac1{k^2}
\]

remains bounded.

Thus the two endpoints of (4) make the tradeoff explicit:

- `delta_1`: keeps the bounded exact cyclotomic/Mangoldt anchor and the nonzero pointed scale defect of `WP-072`--`WP-076`;
- `m_T`: restores full boundary homogeneity, but loses bounded evaluation at `1` and collapses every canonical cover-resolvent defect to zero.

This is consistent with `WP-071`, which already proved abstractly that a rotation-invariant positive ambient Hilbert completion cannot both retain a cyclotomic shell and make the boundary Mangoldt anchor bounded. The Haar calculation is the canonical measure-averaged realization of that boundary.

## 6. Intermediate invariant measures are only convex mixtures, not new coupling

For `0<a<1`, equation (5) is literal:

\[
\mathcal D_\mu
=
a\mathcal D_1+(1-a)\mathcal D_{\rm Haar}.
\]

There is no cross term between the pointed and Haar components. One can realize the form by the direct-sum embedding

\[
f
\longmapsto
\left(
\sqrt a\,T_1f,\;
\sqrt{1-a}\,(\sqrt{k}\,a_k)_{k\ge1}
\right).
\tag{26}
\]

Under normalized root covers, the first component carries the block-replication isometry of `WP-073`, while the second carries the pure multiplicative shift (18). The averaging construction itself introduces no operator mixing between them.

If `a>0`, the exact boundary anchor remains bounded because

\[
|f(1)|^2
\le
\mathcal D_1(f)
\le
a^{-1}\mathcal D_\mu(f).
\tag{27}
\]

But this happens precisely because the invariant measure retains an atom at the already distinguished point `1`. The diffuse invariant component is only Haar and contributes no new arithmetic discriminator or cover-scale anomaly.

Accordingly, a claim that semigroup-invariant basepoint averaging has produced a new global finite--archimedean geometry must identify an additional operation beyond (1). Merely choosing `0<a<1` is a convex superposition of the existing pointed survivor with classical Haar Dirichlet geometry; it is not a nonseparable coupling generated by the cover system.

This does not rule out applying a later nontrivial quotient, compression, boundary condition, or operator to the mixed space. It says that **the averaging step itself** cannot be the missing mechanism.

## 7. Matched controls and prior-art audit

Every calculation above uses only:

- the classical local Dirichlet difference quotient;
- positivity of integration against a Borel measure;
- the disk power maps `z -> z^n`;
- Hardy/Fourier orthogonality;
- uniqueness of Fourier coefficients of finite measures.

No prime support, cyclotomic coefficient, zeta zero, functional equation, or RH assumption enters the classification. The same two-extreme-point result holds for any analytic family acted on by the full integer power semigroup. This is therefore a **universal cover-geometry obstruction**, which is the correct behavior for a negative control.

The function-space framework is classical. The local Dirichlet integral is already anchored in `SOURCES.md` by Richter--Sundberg, and harmonically weighted Dirichlet spaces are the standard positive-measure averages of these local forms. Composition/root maps on local Dirichlet spaces are likewise established function-space territory, as already recorded for `WP-073`. No novelty is claimed for those ingredients, Haar Fourier orthogonality, or the elementary invariant-measure argument.

The Haar endpoint also lands on familiar multiplicative-shift geometry: equation (18) has the same bare `e_k -> e_{nk}` semigroup skeleton that `WP-012` identifies with the classical Bost--Connes/endomotive neighborhood. No claim is made that the shift representation itself is new.

A directed literature audit around harmonically weighted Dirichlet spaces, power-map composition, and common power-map invariant measures did not identify an external theorem packaging the exact Mathia-specific conclusion here. That absence is not used as a historical novelty claim. The durable content is the **classification of this candidate route** relative to `WP-072`--`WP-076`: the only semigroup-compatible positive basepoint averages are pointed-plus-Haar, and the Haar component destroys rather than globalizes the positive scale defect that supplied `log n`.

## 8. What is actually closed

The result closes the direct route

```text
pointed local Dirichlet positivity
    -> average canonically over boundary basepoints
    -> retain one root-cover isometric geometry
    -> obtain new global/cross-prime positive interaction
    -> Weil positivity
```

within the natural class (1).

The obstruction has two independent layers:

1. **measure classification:** full root-cover covariance forces `mu=a delta_1+(1-a) Haar`, so no new diffuse arithmetic boundary measure exists;
2. **Haar degeneration:** the only diffuse extremal measure converts block refinement into exact multiplicative dilation, making the positive inverse-scale/resolvent defects identically zero and losing the bounded point anchor.

The result does **not** close:

- nonlocal kernels coupling two or more boundary points before integration;
- matrix/operator-valued measures with internal degrees of freedom;
- a quotient or compression whose sign is proved independently;
- a boundary response linking the disk to an archimedean sector;
- cohomological/intersection constructions;
- a non-measure finite--archimedean coupling that breaks the direct-integral architecture.

Those are precisely the types of genuinely nonseparable mechanisms left by `WP-076`.

## 9. Exact falsification surface

The finding can be falsified by any of the following.

1. Failure of the local covariance
   \[
   \mathcal D_\zeta(C_nf,C_ng)=n\mathcal D_{\zeta^n}(f,g).
   \]
2. Failure of the monomial identity
   \[
   \mathcal D_\mu(z^k,z^\ell)
   =
   \min(k,\ell)\int\zeta^{k-\ell}\,d\mu.
   \]
3. A probability measure other than `a delta_1+(1-a)m_T` invariant under every power map `z -> z^n`, `n>=2`.
4. Failure of the Haar identity
   \[
   \mathcal D_{\rm Haar}(f)=\sum k|a_k|^2.
   \]
5. A nonzero operator in (8) for the multiplicative-shift realization (17).
6. Bounded boundary evaluation at `1` in the Haar Dirichlet geometry despite the explicit sequence (23)--(25).
7. A construction claimed to contradict the no-go while still being only a positive measure average of the local fibers with one fixed semigroup-covariant form. A genuinely nonseparable kernel, quotient, compression, or internal coupling is outside the hypotheses and is not a counterexample.

## Research consequence

`WP-073`--`WP-076` showed that fixing the Prime-Circle basepoint creates unexpectedly rich positive structure: the cover normalization forces `1/2`, the boundary anchor gives exact finite arithmetic data, and block refinement yields a positive `log n` scale defect whose shifted family contains a digamma profile but only as a coboundary.

`WP-077` shows that the most obvious way to make this geometry global is self-defeating. Requiring one positive local-energy average to be compatible with the full root-cover semigroup gives only

\[
\boxed{
\text{pointed endpoint}
\;\oplus_{\rm convex}\;
\text{Haar Dirichlet endpoint}.
}
\]

The diffuse endpoint removes the residue-class variance responsible for the `log n` anomaly and cannot represent the Mangoldt boundary anchor. Intermediate invariant averages merely retain some amount of the original pointed component.

Therefore the next viable continuation cannot be a scalar average over boundary basepoints. It must introduce a **genuine interaction before positivity is read out**: cross-basepoint, cross-prime, finite--archimedean, quotient/compression, boundary-response, or cohomological structure whose sign theorem is not inherited from a direct convex average and whose arithmetic/global terms survive the matched controls.
