# PC-325 — Green relative spectrum is phase-gauge and autocorrelation-only

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the phase-sensitive continuation of the PC-323 relative Green/Hilbert branch.

PC-323 leaves the trace-class defect of the cross-level Green operator, and in particular its relative determinant/scattering data against the universal Hilbert core, as a possible carrier of detailed Prime-Circle residue information. PC-324 shows that isolated residue controls already have classical generalized-Hilbert edge spectra, but it deliberately leaves multi-residue interference open.

There is an exact obstruction before any zero search: for the entire PC-323 Green operator, **all independent Fourier phases of the two periodic source sequences are removable by one block-diagonal unitary, and the same unitary removes them simultaneously from the comparison core**. Consequently the complete self-adjoint spectrum and every simultaneously-unitary invariant of the relative pair factor through the two source magnitude sequences. In the PC-316 Fourier-source realization, those magnitudes are exactly equivalent to the two cyclic autocorrelations by finite Wiener--Khinchin.

Thus the PC-323/324 branch cannot use oriented Fourier phase, higher-order phase interference, or source placement information beyond pair autocorrelation as the missing RH carrier. Any surviving multi-residue mechanism in this branch must already be visible in the magnitude/autocorrelation data.

## 1. Two-sided phase gauge for the full Green operator

Let `a,b` be the bounded periodic source sequences of PC-323 and write

\[
a(k)=u_a(k)|a(k)|,
\qquad
b(k)=u_b(k)|b(k)|,
\tag{1}
\]

where `|u_a(k)|=|u_b(k)|=1` whenever the corresponding source coefficient is nonzero, with the harmless convention `u=1` at zeros. Let `U_a,U_b` denote the associated diagonal unitaries on `\ell^2(\mathbb N)`.

The canonical Green operator is

\[
X_{a,b}=D_aK_1D_b,
\qquad
(K_1)_{kl}=\frac1{k+l}.
\tag{2}
\]

Since diagonal multipliers commute,

\[
D_a=U_aD_{|a|},
\qquad
D_b=D_{|b|}U_b,
\tag{3}
\]

and therefore

\[
\boxed{
X_{a,b}=U_aX_{|a|,|b|}U_b.
}
\tag{4}
\]

This is two-sided unitary equivalence, so all singular values and all spectral data of `X^*X` and `XX^*` already depend only on `|a|,|b|`.

More importantly, the canonical self-adjoint dilation from PC-323,

\[
G_{a,b}=
\begin{pmatrix}
0&X_{a,b}\\
X_{a,b}^*&0
\end{pmatrix},
\tag{5}
\]

is genuinely unitarily equivalent to its modulus version. Put

\[
W=\operatorname{diag}(U_a,U_b^*).
\tag{6}
\]

Then (4) gives exactly

\[
\boxed{
G_{a,b}=W G_{|a|,|b|}W^*.
}
\tag{7}
\]

Hence the full spectrum, point spectrum with multiplicities, spectral measures up to the natural unitary transport, essential spectrum, singular spectrum, and absolutely-continuous spectral type are all phase-blind. This is stronger than the RMS collapse of the leading Hilbert band in PC-323: the **entire** self-adjoint Green lift, including any off-band eigenvalues created by the trace-class defect, is unchanged by independent phase changes of `a` and `b`.

## 2. The relative Hilbert pair is simultaneously phase-gauge

The remaining possibility after PC-323 is not the absolute spectrum alone but the relative pair `(G_{a,b},G_0(a,b))`. Let `L` be a common period. In the residue decomposition of PC-323 the comparison core is

\[
X_0(a,b)=A_{a,b}\otimes H_1,
\qquad
A_{a,b}=\frac1L a_Lb_L^{\mathsf T}.
\tag{8}
\]

Writing the finite source vectors as

\[
a_L=U_{a,L}|a_L|,
\qquad
b_L=U_{b,L}|b_L|,
\tag{9}
\]

with diagonal unitary matrices, one has

\[
A_{a,b}=U_{a,L}A_{|a|,|b|}U_{b,L}.
\tag{10}
\]

Under residue grouping, the periodic infinite diagonal unitaries become `U_{a,L}\otimes I` and `U_{b,L}\otimes I`. Therefore the **same** block unitary `W` used in (7) simultaneously conjugates both members of the relative pair:

\[
\boxed{
(G_{a,b},G_0(a,b))
\simeq
(G_{|a|,|b|},G_0(|a|,|b|)).
}
\tag{11}
\]

This removes the possible loophole that the absolute operator might be phase-blind while its trace-class displacement from the comparison core retained a relative phase invariant. It does not.

For example, wherever the PC-323 relative perturbation determinant is defined,

\[
\Delta_{a,b}(z)
=
\det\!\left(
I+(G_{a,b}-G_0(a,b))(G_0(a,b)-z)^{-1}
\right),
\tag{12}
\]

simultaneous unitary conjugation and Fredholm-determinant invariance give

\[
\boxed{
\Delta_{a,b}(z)=\Delta_{|a|,|b|}(z).
}
\tag{13}
\]

The same conclusion applies to the spectral-shift function and to unitary-conjugacy invariants of any scattering operator defined for this trace-class pair. The statement is deliberately about the relative pair up to simultaneous unitary equivalence; it does not assert equality of basis-dependent scattering matrices before the corresponding unitary transport.

## 3. For Prime-Circle Fourier sources, the quotient is exactly autocorrelation

In the PC-316 realization, the periodic Green masks are finite Fourier transforms of centered source functions. Let `f:Z/qZ -> C` and use the project convention

\[
\widehat f(h)
=\sum_{x\in\mathbb Z/q\mathbb Z}
 f(x)e^{-2\pi i hx/q},
\qquad
a(h)=\widehat f(h),
\tag{14}
\]

periodically extended. Define the cyclic autocorrelation

\[
C_f(t)
=\sum_{x\in\mathbb Z/q\mathbb Z}
 f(x+t)\overline{f(x)}.
\tag{15}
\]

A direct finite Fourier calculation gives the Wiener--Khinchin identity

\[
\boxed{
\widehat{C_f}(h)=|\widehat f(h)|^2=|a(h)|^2.
}
\tag{16}
\]

Thus `C_f` determines `|a|` by finite Fourier transform and positive square root, while `|a|` determines `C_f` by inverse transform. The analogous statement holds independently for the second source `g` and its mask `b`.

Combining (7), (11), and (16), every spectral invariant of the full Green dilation considered here, and every simultaneously-unitary invariant of its relative Hilbert pair, factors as

\[
(f,g)
\longmapsto
(C_f,C_g)
\longmapsto
(|a|,|b|)
\longmapsto
\text{Green/relative spectral data}.
\tag{17}
\]

The operator can therefore retain arithmetic information encoded in pairwise difference counts or other autocorrelation structure, but **nothing that distinguishes sources having the same cyclic autocorrelations**.

## 4. Exact matched controls with identical complete Green spectral data

This quotient supplies a much stronger matched-control test than merely matching the Hilbert-band RMS scale. Suppose, for concreteness, that `f` is real and centered, so

\[
a(q-h)=\overline{a(h)},
\qquad a(0)=0.
\tag{18}
\]

Choose phases satisfying

\[
\widetilde a(h)=e^{i\theta_h}a(h),
\qquad
\theta_{q-h}=-\theta_h,
\qquad
\widetilde a(0)=0.
\tag{19}
\]

The inverse DFT `\widetilde f` is again real and centered, while

\[
|\widetilde a(h)|=|a(h)|
\tag{20}
\]

for every frequency. Hence `\widetilde f` has **exactly the same cyclic autocorrelation** as `f`. The same construction can be made independently for `g`.

Whenever there is a nontrivial conjugate frequency pair, continuous phase choices give a continuum of such real centered controls, while the translation/reflection orbit of a fixed finite cyclic source is finite. Generic choices are therefore not translations or reflections of the original source. Equations (7) and (11) then show that these distinct, generally non-arithmetic controls have exactly the same complete Green-dilation spectrum and the same relative determinant/spectral-shift/scattering conjugacy invariants.

For the canonical odd Prime-Circle source periods used in the PC-316 branch, the relevant nonzero conjugate frequency pairs are present, so this is not merely a formal possibility. It is an exact source-level matched-control obstruction.

## 5. Relation to earlier phase and autocorrelation obstructions

PC-278 proved that a **single-source fixed dual-window** phase field becomes pure gauge under positive/Hermitian spectralization, and explicitly left cross-source or cross-level operators as a possible escape. The present result addresses one of those escapes: the genuinely cross-level, two-source Green operator of PC-323 still admits independent left/right phase gauges, and its self-adjoint dilation turns those gauges into one block unitary conjugacy.

PC-299 found source autocorrelation in a different square-zero cross-Gram/Fejer defect scalar. That result does not classify the PC-323 Green operator. Here the conclusion is stronger and operator-level: not one selected scalar, but the full Green spectrum and the canonical trace-class relative pair factor through source autocorrelations.

Accordingly PC-325 is not a restatement of either earlier obstruction. It closes the **phase-sensitive part** of the explicit multi-residue/relative-spectral frontier left by PC-323 and PC-324.

## 6. Prior-art and novelty audit

The abstract ingredients are classical. Equations (4) and (7) are elementary two-sided unitary equivalence and self-adjoint dilation. Equation (16) is finite Wiener--Khinchin, and the nonuniqueness of reconstructing a one-dimensional finite signal from Fourier magnitudes/autocorrelation is the standard Fourier phase-retrieval ambiguity.

A targeted novelty search against Fourier phase retrieval, homometric/autocorrelation-equivalent finite signals, weighted Hilbert/Hankel operators, and trace-class relative scattering found the expected classical phase-retrieval and operator-theoretic frameworks. No claim is made that unitary invariance, Wiener--Khinchin, or phase-retrieval ambiguity is new. No external theorem is load-bearing for the exact obstruction: the project-local claim follows directly from the explicit PC-323 factorization (2), its comparison core (8), and the finite Fourier identity (16). Therefore no new durable literature dependency is required and `SOURCES.md` is unchanged.

The line-local content is the simultaneous application of these elementary identities to the **full PC-323 relative Green/Hilbert pair**. In particular, the relative determinant proposed there cannot recover the independently variable Fourier phases that disappear from the absolute spectrum; the comparison operator loses exactly the same phases under the same unitary.

This is a negative classification, not a new spectral route to zeta. It survives the mandate's matched-control test by producing exact non-arithmetic phase controls rather than only asymptotically similar statistics.

## 7. Sharp boundary: what remains open

The theorem does **not** say that Prime-Circle autocorrelations are arithmetically trivial. For canonical indicator or signed-support sources they may contain nontrivial pair-difference information, and a magnitude-only multi-residue invariant could still distinguish arithmetic sources from suitable restricted controls. PC-325 only proves that such a mechanism cannot require the discarded Fourier phases.

The phase-twisted controls above also need not remain in a restrictive binary or support-indicator subclass. They are exact controls in the arbitrary centered real/complex source class already used to formulate the PC-316/PC-323 operator. A future claim restricted to a finite alphabet or to literal primitive-residue indicator sources would need its own phase-retrieval/homometry analysis rather than inheriting this continuum-control statement automatically.

Nor does the theorem cover an operator whose kernel couples source phases nonseparably, for example through products involving `a(k)` and `a(l)` in the same channel, higher-order polyspectra, nonlinear source-dependent index selection, or a genuinely different Prime-Circle operator not of the PC-323 form `D_aK_1D_b`. Such constructions change the hypothesis rather than evade (4).

The surviving question inside the Green branch is therefore narrower and testable: **does the source-forced magnitude/autocorrelation pair `(C_f,C_g)` produce any relative spectral invariant with a nonclassical, zeta-zero-sensitive mechanism?** Oriented phase/multi-residue interference by itself is no longer available as that carrier.

## Audit tests

The exact claim fails if any of the following fails: direct multiplication must give (4); the block unitary (6) must give (7); residue grouping must turn the same periodic phase multipliers into the finite diagonal factors in (10); both members of the relative pair must therefore obey (11); finite DFT of (15) must equal (16); and arbitrary conjugate-symmetric phase twists (19) must preserve realness, centering, and autocorrelation while reproducing the same Green spectral data. A counterexample to any of these finite identities would refute the corresponding part of the finding.

Passing these checks establishes only the phase/autocorrelation obstruction above. It does not establish a zeta functional equation, a critical-line theorem, or a no-go for magnitude-sensitive nonseparable Prime-Circle operators.