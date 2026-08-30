# PC-066 — transverse profinite symmetry fixes exact-order projectors, not an RH Hamiltonian

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for obtaining a new RH mechanism from a translation- and unit-invariant operator on the abstract transverse fiber of the prime-circle solenoid.

## Claim

PC-064 identifies the transverse fiber over the common anchor in the compatible-circle inverse limit with

\[
K=\widehat{\mathbb Z},
\qquad
\widehat K\cong\mathbb Q/\mathbb Z.
\]

A natural repair of the leafwise failure in PC-065 is to ask whether the transverse profinite direction itself canonically supplies a prime-selective compact-resolvent operator. In the natural **abstract-refinement symmetry class** this can be classified exactly.

Let `T` be a self-adjoint operator on `L^2(K)` whose spectral projections commute with

1. all translations of `K`; and
2. all additive automorphisms `x\mapsto ux`, `u\in\widehat{\mathbb Z}^{\times}`.

Then there is a real scalar function `h:\mathbb N\to\mathbb R` such that

\[
\boxed{
T=\sum_{n\ge1}h(n)P_n,
}
\]

where `P_n` is the orthogonal projector onto the characters of **exact order** `n` in `\mathbb Q/\mathbb Z`. Moreover,

\[
\boxed{
\operatorname{rank}P_n=\varphi(n),
}
\]

and the convolution kernel of `P_n` is the classical Ramanujan sum `c_n` pulled back from `\mathbb Z/n\mathbb Z`.

Thus the transverse/refinement symmetries canonically fix the same exact-order birth decomposition already present in the roots-of-unity tower, but they do **not** fix the spectral scale `h(n)`. The simplest order/conductor choice,

\[
C\chi_\gamma=\operatorname{ord}(\gamma)\chi_\gamma,
\]

is positive with compact resolvent, but its spectral zeta is exactly the classical totient Dirichlet series

\[
\boxed{
\operatorname{Tr}(C^{-s})
=\sum_{n\ge1}\frac{\varphi(n)}{n^s}
=\frac{\zeta(s-1)}{\zeta(s)},
\qquad \Re s>2.
}
\]

This is a genuine transverse prime discriminator only in the tautological sense that the multiplicity of level `n` is the number of primitive `n`-th roots. It does not create a new zeta-zero mechanism: nontrivial zeros of `\zeta` reappear as poles of a pre-existing classical quotient, and equally symmetry-compatible reparametrizations `C^\alpha` move those poles to `s=\rho/\alpha`.

Consequently, **abstract transverse profinite symmetry repairs the analytic defect of PC-065 only by returning to the classical exact-order/Bost–Connes/Ramanujan package already identified in PC-010 and PC-022.** Any surviving transverse route must use additional embedded prime-circle geometry that breaks this abstract unit symmetry, or a genuinely nonseparable leaf–fiber coupling before the exact-order Fourier decomposition.

## 1. Translation invariance makes the transverse operator a Fourier multiplier

The compact abelian group `K=\widehat{\mathbb Z}` has discrete Pontryagin dual

\[
\widehat K=\mathbb Q/\mathbb Z.
\]

For `\gamma\in\mathbb Q/\mathbb Z`, write `\chi_\gamma` for the corresponding character of `K`. These characters form an orthonormal basis of `L^2(K)`.

If the spectral projections of a self-adjoint `T` commute with the translation representation of `K`, each one-dimensional character space is invariant. Hence

\[
T\chi_\gamma=\lambda(\gamma)\chi_\gamma
\]

for a real multiplier `\lambda` (on the operator domain). This step uses only compact-abelian harmonic analysis; no prime arithmetic has yet entered.

## 2. Unit symmetry makes exact order the complete orbit invariant

The additive automorphisms of `\widehat{\mathbb Z}` are multiplication by units

\[
u\in\widehat{\mathbb Z}^{\times}.
\]

On the dual they act by

\[
\gamma\longmapsto u\gamma.
\]

Suppose `\gamma=a/n\pmod1` has exact order `n`, so `(a,n)=1`. Every other exact-order-`n` character has the form `b/n` with `(b,n)=1`. The reduction map

\[
\widehat{\mathbb Z}^{\times}\longrightarrow(\mathbb Z/n\mathbb Z)^{\times}
\]

is surjective, so one can choose `u` with

\[
u\equiv ba^{-1}\pmod n.
\]

Therefore `\widehat{\mathbb Z}^{\times}` acts transitively on the characters of each exact order `n`. Unit invariance of `T` forces

\[
\lambda(\gamma)=h(n)
\qquad
\text{whenever }\operatorname{ord}(\gamma)=n.
\]

This proves the orthogonal decomposition

\[
\boxed{
L^2(\widehat{\mathbb Z})
=\bigoplus_{n\ge1}E_n,
\qquad
E_n=\operatorname{span}\{\chi_\gamma:\operatorname{ord}(\gamma)=n\},
}
\]

and every operator in the stated symmetry class is

\[
\boxed{T=\sum_{n\ge1}h(n)P_n.}
\]

There are exactly `\varphi(n)` exact-order-`n` elements of `\mathbb Q/\mathbb Z`, hence

\[
\dim E_n=\varphi(n).
\]

The important distinction is that the projectors `P_n` are forced, while the eigenvalue assignment `h(n)` is not.

## 3. The projectors are precisely Ramanujan birth projectors

For `x\in\widehat{\mathbb Z}`, let `x_n` be its residue class modulo `n`. The finite-rank projector kernel is

\[
\kappa_n(x)
=\sum_{\operatorname{ord}(\gamma)=n}\chi_\gamma(x)
=\sum_{\substack{a\bmod n\\(a,n)=1}}
 e^{2\pi i a x_n/n}
= c_n(x_n).
\]

Thus `P_n` is exactly the Ramanujan-sum projector onto primitive/exact-order modes. This is the transverse version of the exact-order character decomposition already obtained in PC-022; it is not a new arithmetic layer generated by the solenoid.

Equivalently, the abstract profinite fiber remembers the primitive-shell partition

\[
\mathbb Q/\mathbb Z
=\bigsqcup_{n\ge1}\{\gamma:\operatorname{ord}(\gamma)=n\},
\]

which PC-010 already identifies with the birth-labelled cyclotomic tower underlying Bost–Connes dynamics.

## 4. The natural conductor operator is compact but classical

The most direct positive operator using the intrinsic exact-order label is

\[
C\chi_\gamma
=\operatorname{ord}(\gamma)\chi_\gamma.
\]

Its eigenvalue `n` has multiplicity `\varphi(n)`. Since

\[
\sum_{n\le N}\varphi(n)<\infty
\]

for every finite `N` and the eigenvalues tend to infinity, `(C+1)^{-1}` is compact. So this transverse weighting does repair the noncompact low-energy behavior of the bare leafwise Laplacian in PC-065.

But its trace data contain no new spectral arithmetic:

\[
\operatorname{Tr}(C^{-s})
=\sum_{n\ge1}\varphi(n)n^{-s}
=\frac{\zeta(s-1)}{\zeta(s)},
\qquad \Re s>2.
\]

The identity is the standard totient Dirichlet series already recorded in `research/prime_circle/SOURCES.md` as a classical boundary for the line.

For a nontrivial Riemann zero `\rho`, the numerator `\zeta(\rho-1)` is nonzero because `-1<\Re(\rho-1)<0` contains no zeta zeros. Thus `\rho` becomes a pole of the meromorphic continuation of this quotient, with the same multiplicity as the zero of `\zeta`, rather than an eigenvalue produced by a self-adjoint spectral condition.

There is therefore a formal zeta-zero locator here, but it is exactly the forbidden kind of progress: the denominator `\zeta(s)` is already present in a classical Dirichlet transform of the totient multiplicities.

## 5. Symmetry does not select the critical-line normalization

The classification also exposes why the spectral scale is not forced. For every `\alpha>0`,

\[
C^\alpha=\sum_{n\ge1}n^\alpha P_n
\]

has the same canonical exact-order eigenspaces and all the same translation/unit symmetries. Its spectral zeta is

\[
\boxed{
\operatorname{Tr}((C^\alpha)^{-s})
=\frac{\zeta(\alpha s-1)}{\zeta(\alpha s)}.
}
\]

A Riemann zero `\rho` therefore appears at

\[
s=\rho/\alpha.
\]

Changing an equally symmetry-compatible scalar function of the order moves the apparent vertical line. No intrinsic `1/2`, gamma factor, or `s\leftrightarrow1-s` functional equation has been derived from the transverse group itself.

The logarithmic generator

\[
H=\log C
\]

makes the same point in statistical-mechanical language:

\[
\operatorname{Tr}(e^{-\beta H})
=\frac{\zeta(\beta-1)}{\zeta(\beta)}.
\]

This lies in the same cyclotomic/refinement neighborhood as Bost–Connes; it does not constitute a new Hamiltonian realization of Riemann zeros.

## 6. Prime discrimination is only primitive-shell cardinality

The conductor spectrum certainly detects prime levels in a literal finite-level sense:

\[
\operatorname{mult}_C(n)=\varphi(n),
\]

and

\[
\varphi(n)=n-1
\quad\Longleftrightarrow\quad
n\text{ is prime}
\]

for `n>1`.

But this discriminator is already visible before any operator is introduced: `\varphi(n)` is exactly the number of new vertices in the primitive shell `\mu_n^*`. The transverse spectralization has merely promoted the birth partition to eigenspaces.

Likewise, prime-power/valuation information can be read from exact orders and their divisor relations, but PC-010 shows that those data belong to the abstract cyclotomic refinement tower. They do not use the Euclidean chord geometry, logarithmic potentials, old/new interactions, or another prime-circle observable absent from `(\mathbb Q/\mathbb Z,\mathbb N)`.

## 7. Prior-art and novelty audit

No historical novelty is claimed for any of the abstract ingredients.

- PC-010 already records that roots of unity with birth labels and power/refinement maps are the classical Bost–Connes cyclotomic tower, citing Bost–Connes and Connes–Consani–Marcolli. Bost–Connes already has zeta as a thermodynamic partition function; recovering cyclotomic order dynamics on the profinite fiber is therefore a prior-art return, not a new bridge.
- PC-022 already identifies exact-order Fourier layers with Ramanujan projectors in the cyclic-cover setting. The kernel `c_n` above is the same classical exact-order harmonic decomposition on the transverse fiber.
- `research/prime_circle/SOURCES.md` already records `\sum\varphi(n)n^{-s}=\zeta(s-1)/\zeta(s)` specifically as a classical totient Dirichlet-series identity rather than new spectral data.
- Targeted external searches around profinite/hierarchical Laplacians, Bost–Connes dynamics, and arithmetic spectral triples did not reveal a theorem that would turn the symmetry classification above into a new RH mechanism. The neighboring literature instead reinforces the distinction between a canonical filtration/projector decomposition and an additionally chosen scale on that filtration.

The project-specific contribution of this finding is therefore a **classification/no-go**: once the transverse fiber is stripped to the abstract symmetries naturally retained by compatible refinement, all invariant linear spectral operators share the exact-order projectors, and their only remaining freedom is a scalar function of conductor.

## 8. Boundary of the obstruction

The unit symmetry used here is natural for the **abstract transverse/refinement fiber**. It is not a symmetry of all embedded prime-circle geometry: a general arithmetic unit permutes primitive residues but does not preserve their Euclidean chord positions relative to a distinguished geometric configuration.

PC-066 therefore does **not** rule out:

- a transverse operator whose matrix entries are derived from embedded chord or old/new geometry and hence break `\widehat{\mathbb Z}^{\times}` symmetry;
- a leaf–fiber operator that couples real frequency and transverse refinement before either side is Fourier-diagonalized;
- nonlinear cross-level forms that do not reduce to a multiplier `h(\operatorname{ord}\gamma)`;
- finite-level old/new couplings such as the extensive squarefree sector reopened by PC-047;
- or the global uniformization/accessory-parameter branch of PC-017.

The narrowed research gate is

\[
\boxed{
\text{transverse refinement alone}
\Rightarrow
\text{exact-order/Ramanujan projectors};
\quad
\text{new RH content requires embedded or nonseparable geometry beyond them.}
}
\]

## 9. Exact audit tests

The claim has direct falsifiers:

1. verify `\widehat{\widehat{\mathbb Z}}\cong\mathbb Q/\mathbb Z`;
2. verify translation invariance diagonalizes `T` in the character basis;
3. verify `\widehat{\mathbb Z}^{\times}\to(\mathbb Z/n\mathbb Z)^{\times}` is surjective and hence acts transitively on exact-order-`n` characters;
4. sum those characters and recover the Ramanujan kernel `c_n`;
5. count the eigenspace and recover `\dim E_n=\varphi(n)`;
6. for `C\chi_\gamma=\operatorname{ord}(\gamma)\chi_\gamma`, verify compact resolvent and the classical identity `\operatorname{Tr}(C^{-s})=\zeta(s-1)/\zeta(s)` in `\Re s>2`;
7. replace `C` by `C^\alpha` and verify that the same eigenspaces/symmetries move every denominator zero from `s=\rho` to `s=\rho/\alpha`.

Failure of items 1–6 would invalidate the exact classification or its conductor example. A future prime-circle transverse mechanism evades the no-go only by violating the abstract symmetry/multiplier hypotheses for a reason derived from the original embedded geometry, not by choosing another scalar function `h(n)` because its Dirichlet series has desirable zeros.