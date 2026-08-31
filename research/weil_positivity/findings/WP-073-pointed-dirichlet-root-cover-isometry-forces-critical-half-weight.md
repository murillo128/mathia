# WP-073 — Pointed Dirichlet root-cover isometry forces the critical half-weight

## Claim

Let

\[
\mathcal D_1^0
:=
\left\{f\in\operatorname{Hol}(\mathbb D):f(0)=0,\;
D_1(f):=\left\|\frac{f(z)-f(1)}{z-1}\right\|_{H^2}^2<\infty\right\}
\]

be the zero-at-origin pointed local Dirichlet space used in `WP-072`, with inner product induced by

\[
T_1f(z):=\frac{f(z)-f(1)}{z-1}.
\]

For the intrinsic Prime-Circle power map

\[
P_n(z)=z^n,
\qquad
C_nf:=f\circ P_n,
\]

one has the exact covariance law

\[
\boxed{D_1(C_nf)=nD_1(f)}
\]

for every `n>=1` and every `f in mathcal D_1^0`. Hence

\[
\boxed{V_n:=n^{-1/2}C_n}
\]

is an isometry of `mathcal D_1^0`, and the positive scalar `n^{-1/2}` is the unique normalization making the degree-`n` pullback isometric. Moreover

\[
V_mV_n=V_{mn},
\]

so the normalized root covers form a multiplicative semigroup of isometries.

The boundary representer `z` from `WP-072`, characterized by

\[
\langle z,f\rangle_{D_1}=f(1),
\]

is an exact joint adjoint eigenvector:

\[
\boxed{V_n^*z=n^{-1/2}z.}
\]

For the canonical Prime-Circle shell

\[
F_n(z)=\Log\Phi_n(z),
\qquad n>1,
\]

`WP-072` gives `F_n(1)=Lambda(n)`. Therefore the same positive pointed geometry and the same intrinsic degree-`n` root map give

\[
\boxed{
\langle V_n^*z,F_n\rangle_{D_1}
=
\frac{\Lambda(n)}{\sqrt n}.
}
\]

Thus the critical finite-place attenuation that `WP-072` had to leave unexplained is **not arbitrary in this branch**: it is forced by isometric normalization of the intrinsic root-cover pullback. No zero data, zeta continuation, fitted kernel, or RH assumption enters this derivation.

This is still **not a global Weil-positivity mechanism**. The half-weight is a universal degree effect, the Prime-Circle shell identity supplies the arithmetic selector, and the construction does not yet produce the Weil autocorrelation form, the Gamma contribution, or the polar/global counterterms.

**Evidence status:** `EXACT-DERIVED + POSITIVE-BRIDGE + CLASSICAL-LOCAL-DIRICHLET/COMPOSITION + MATHIA-SPECIALIZATION`.

## 1. Exact covariance of the pointed local Dirichlet form

Write

\[
g=T_1f
=\frac{f(z)-f(1)}{z-1}\in H^2.
\]

Since

\[
f(z^n)-f(1)
=(z^n-1)g(z^n)
=(z-1)(1+z+\cdots+z^{n-1})g(z^n),
\]

we have the exact intertwining identity

\[
\boxed{
T_1C_nf
=S_n(z)g(z^n),
\qquad
S_n(z):=1+z+\cdots+z^{n-1}.
}
\]

If

\[
g(z)=\sum_{k\ge0}a_kz^k,
\]

then

\[
S_n(z)g(z^n)
=
\sum_{k\ge0}\sum_{r=0}^{n-1}a_k z^{nk+r}.
\]

The exponent sets `nk+r`, `0<=r<n`, are disjoint. Hardy orthogonality therefore gives

\[
\begin{aligned}
D_1(C_nf)
&=\|S_ng(z^n)\|_{H^2}^2\\
&=\sum_{k\ge0}\sum_{r=0}^{n-1}|a_k|^2\\
&=n\|g\|_{H^2}^2\\
&=nD_1(f).
\end{aligned}
\]

This is an exact Hilbert-space identity, not an asymptotic or a boundary heuristic. In particular `C_n` is bounded with norm exactly `sqrt(n)` on this pointed geometry.

If `a_n C_n` is required to be an isometry, then

\[
|a_n|^2n=1.
\]

Thus `|a_n|=n^{-1/2}`. Requiring the canonical positive real normalization removes the irrelevant phase and gives precisely `V_n=n^{-1/2}C_n`.

## 2. Multiplicative compatibility makes the half-weight canonical

The Prime-Circle power maps satisfy

\[
P_m\circ P_n=P_{mn}.
\]

Consequently

\[
C_mC_n=C_{mn}.
\]

The degree normalization is multiplicative as well:

\[
\frac1{\sqrt m}\frac1{\sqrt n}
=\frac1{\sqrt{mn}},
\]

so

\[
\boxed{V_mV_n=V_{mn}.}
\]

This matters for the interpretation of the exponent `1/2`. It is not obtained by noticing the desired Weil coefficient and rescaling each shell afterward. It is the unique positive normalization that simultaneously makes every intrinsic degree pullback an isometry and respects multiplication of the power maps.

The maps themselves are already part of Prime Circle rather than imported for this calculation. `PC-016` uses `z->z^n` as the canonical cyclic-cover/refinement map and shows that old-prime exponent growth is literally realized by regular cyclic covers. `PC-079` further organizes the Hardy refinement maps into a commuting multiplicative dilation calculus. The present result concerns a different positive topology: the base-point local Dirichlet geometry selected in `WP-072`.

## 3. The Mangoldt anchor becomes a half-density eigenvector relation

On `mathcal D_1^0`, `WP-072` identifies `z` as the Riesz representer of boundary evaluation:

\[
\langle z,f\rangle_{D_1}=f(1),
\qquad
D_1(z)=1.
\]

Since `V_n` is bounded, its adjoint exists. For every `f in mathcal D_1^0`,

\[
\begin{aligned}
\langle V_n^*z,f\rangle_{D_1}
&=\langle z,V_nf\rangle_{D_1}\\
&=(V_nf)(1)\\
&=n^{-1/2}f(1)\\
&=\langle n^{-1/2}z,f\rangle_{D_1}.
\end{aligned}
\]

Hence

\[
\boxed{V_n^*z=n^{-1/2}z.}
\]

Now take the conductor-`n` cyclotomic shell

\[
F_n=\Log\Phi_n.
\]

Its distinguished boundary value is the exact classical identity

\[
F_n(1)=\log\Phi_n(1)=\Lambda(n),
\qquad n>1.
\]

Pairing the normalized cover action with that intrinsic shell gives

\[
\begin{aligned}
\langle V_n^*z,F_n\rangle_{D_1}
&=n^{-1/2}\langle z,F_n\rangle_{D_1}\\
&=\frac{\Lambda(n)}{\sqrt n}.
\end{aligned}
\]

This is exactly the finite coefficient singled out independently by the Prime-Lattice compression in `WP-004`.

The division of labor is now precise:

\[
\boxed{
\text{cyclotomic boundary anchor}
\longrightarrow \Lambda(n),
\qquad
\text{positive root-cover isometry}
\longrightarrow n^{-1/2}.
}
\]

Neither ingredient is fitted to the other after the fact: the first was already forced by `Phi_n(1)`, while the second is forced by degree covariance of `D_1`.

## 4. A canonical positive orbit kernel is also forced

The same calculation exposes what additional scalar geometry the normalized covers produce. Since

\[
T_1(V_nz)
=\frac1{\sqrt n}(1+z+\cdots+z^{n-1}),
\]

we obtain for `m,n>=1`

\[
\boxed{
\langle V_mz,V_nz\rangle_{D_1}
=
\frac{\min(m,n)}{\sqrt{mn}}
=
\exp\left(-\frac12|\log m-\log n|\right).
}
\]

This kernel is automatically positive because it is a Gram kernel. On logarithmic scale it is the standard exponential Green kernel: up to the conventional normalization it is the integral kernel of

\[
\left(-\frac{d^2}{dt^2}+\frac14\right)^{-1}.
\]

This is useful mainly as a boundary marker. The half-scale appears twice from the same Hilbert geometry — in the adjoint eigenvalue and in the logarithmic orbit kernel — but the kernel is universal degree geometry. It is not, by itself, the finite Weil autocorrelation kernel or an archimedean Gamma term.

## 5. Adversarial controls

### Universal analytic-family control

The covariance proof never uses cyclotomic arithmetic. For any family `G_n in mathcal D_1^0` with boundary values

\[
a_n:=G_n(1),
\]

one has

\[
\langle V_n^*z,G_n\rangle_{D_1}
=\frac{a_n}{\sqrt n}.
\]

Therefore the positive geometry forces the **half-density law**, not the von Mangoldt support. Prime powers enter only through the independent Prime-Circle identity `F_n(1)=Lambda(n)`. A non-arithmetic control family inherits the same `n^{-1/2}` scaling.

This is a decisive limitation rather than a defect in the derivation: the result explains the critical normalization intrinsically but does not distinguish the Riemann arithmetic from arbitrary pointed analytic data.

### Full-root control

`WP-072` proved that the normalized full-root controls

\[
Y_N=\frac1{\log N}\log\frac{1-z^N}{1-z}
\]

satisfy `D_1(Y_N)->infinity` rather than becoming approximate null vectors. Since `V_n` is an isometry,

\[
D_1(V_nY_N)=D_1(Y_N).
\]

Thus the new degree normalization does not reopen the topology failure that killed the rotation-invariant Hardy candidates in `WP-068`--`WP-071`.

### Prime-power support is not produced by the cover semigroup

Every positive integer degree has a root map and an isometry `V_n`, including integers with several distinct prime factors. The vanishing of `Lambda(n)` away from prime powers comes entirely from the cyclotomic boundary anchor. Accordingly the route must not be reinterpreted as a geometric prime-power selector supplied by the cover action itself.

### The actual finite Weil form remains indefinite

The scalar identity

\[
\Lambda(n)n^{-1/2}
\]

is only the coefficient-level target. `WP-005` proves that lifting these coefficients to the translation/autocorrelation operator required by the finite part of Weil's quadratic form gives an indefinite operator. The present construction does not change that result. It explains the coefficient normalization before the lift; it does not supply the missing global positive assembly.

### No archimedean completion

Neither `D_1`, the semigroup `V_n`, nor its orbit Gram intrinsically produces the digamma/Gamma contribution or the pole terms in the explicit formula. Interpreting the exponential orbit kernel as those terms merely because its logarithmic Green operator contains `1/4` would be an analogy, not a derivation. A surviving global mechanism still has to produce the finite and archimedean pieces from one coupled object before invoking its sign theorem.

## 6. Prior-art and novelty audit

The function-space ingredients are classical and no theorem-level novelty is claimed for them.

- Richter and Sundberg's local Dirichlet formula is the classical source for the pointed difference-quotient realization used already in `WP-072`: Stefan Richter and Carl Sundberg, *A formula for the local Dirichlet integral*, Michigan Math. J. **38** (1991), 355--379, DOI `10.1307/mmj/1029004388`.
- Composition operators on local Dirichlet spaces are a classical subject. A direct anchor is Donald Sarason and J.-N. Silva, *Composition operators on a local Dirichlet space*, J. Analyse Math. **87** (2002), 433--450, DOI `10.1007/BF02868484`. Georgios Stylogiannis, *Semigroups of composition operators on local Dirichlet spaces*, Bull. Aust. Math. Soc. **94** (2016), 144--154, DOI `10.1017/S0004972716000113`, treats the semigroup setting and cites the Sarason--Silva boundary-fixed-point theory.
- The root maps `z->z^n`, their multiplicative composition, and their cover/refinement role are already intrinsic to Prime Circle (`PC-016`, `PC-079`). `PC-079` also warns that the bare multiplicative refinement semigroup is commuting/flat and belongs near classical cyclotomic/Bost--Connes structure rather than constituting a new RH mechanism.

The exact identity

\[
D_1(f\circ z^n)=nD_1(f)
\]

is elementary once the local Dirichlet quotient is written in Hardy coordinates, so historical novelty is deliberately not asserted even though the directed literature check did not locate this exact formula stated as a number-theoretic mechanism.

The Mathia-specific contribution is the synthesis with a previously independent arithmetic fact: `WP-072` supplies the bounded exact cyclotomic Mangoldt anchor, while the intrinsic Prime-Circle root-cover action forces the previously missing `n^{-1/2}` normalization. This yields the exact `WP-004` finite coefficient from positive geometry without inserting the critical exponent by hand.

This remains well short of the mature prior-art mechanisms excluded by the research mandate. It neither recasts a known Weil-positive functional nor introduces zero data, but it also does not yet supply the global cohomology/intersection/compression/scattering structure that would make positivity imply the full Weil criterion.

## 7. Exact audit and falsification surface

The result has direct exact failure tests:

1. verify the intertwiner
   \[
   T_1C_nf=S_n(T_1f)\circ P_n;
   \]
2. verify that the `n` residue classes in `S_ng(z^n)` are disjoint in the Hardy basis and hence multiply the squared norm by exactly `n`;
3. verify `V_mV_n=V_{mn}` and that no positive scalar normalization other than `n^{-1/2}` makes every `C_n` isometric;
4. verify the adjoint identity `V_n^*z=n^{-1/2}z` against arbitrary finite-energy test functions;
5. verify independently the shell anchor `F_n(1)=Lambda(n)` and hence the paired coefficient `Lambda(n)/sqrt(n)`;
6. falsify any claimed global interpretation unless the same construction also derives the Weil autocorrelation channel and the archimedean/polar terms with an independent sign theorem.

A failure of items 1--5 invalidates the positive bridge. Item 6 is deliberately a non-promotion gate: passing the finite coefficient identity is not evidence for global Weil positivity.

## Research consequence

`WP-072` left two finite-place gaps: the local positive metric bounded `Lambda(n)` but did not derive either the critical `n^{-1/2}` attenuation or the Weil autocorrelation form. The first gap is now closed inside Prime Circle:

\[
\boxed{
\text{base-point local Dirichlet positivity}
+\text{ intrinsic degree-}n\text{ root pullback}
\Longrightarrow
n^{-1/2}\text{ half-density}
}
\]

and therefore

\[
\boxed{
\text{cyclotomic boundary anchor}
+\text{ normalized root-cover adjoint}
\Longrightarrow
\Lambda(n)n^{-1/2}.
}
\]

The remaining problem is correspondingly sharper. A viable continuation must use this or another intrinsic finite geometry to generate a **nontrivial global assembly** in which the same positive theorem also produces the autocorrelation structure and the archimedean/polar counterterms. Merely reading the half-weight as an RH signal is ruled out by the universal analytic-family control, and merely inserting the resulting coefficients into the classical finite Weil translation comb runs directly into `WP-005`.
