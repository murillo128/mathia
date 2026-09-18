# PL-349 — Beurling–Malliavin radius is the exact local form-core boundary for source-selected modulations

**Evidence:** `LITERATURE + EXACT-DERIVED + DECISIVE-BOUNDARY`

**Status:** `BM-COMPLETENESS-RADIUS-CONTROLS-WEIL-FORM-CORE + INFINITE-BM-DENSITY-COLLAPSES-RESTRICTED-MODULATION + FINITE-BM-DENSITY-REQUIRED-FOR-A-GENUINELY-INTERMEDIATE-FAMILY`

## Precise claim

`PL-348` proved a coarse but strong rejection rule for endpoint modulations: if a real frequency set `Lambda` has superlinear counting, then its exponentials are complete on every fixed interval and the corresponding endpoint states already form a core for the localized completed Weil form. Classical Beurling–Malliavin theory gives the sharp replacement for that counting test.

For a discrete real frequency set `Lambda`, define its ordinary `L^2` completeness radius by

\[
R_2(\Lambda)
:=\sup\{L>0:\{e^{i\lambda x}:\lambda\in\Lambda\}
\text{ is complete in }L^2(0,L)\}.
\tag{PL349-1}
\]

With the standard exterior/effective Beurling–Malliavin density `D_BM^*(Lambda)`, the Beurling–Malliavin theorem states

\[
\boxed{R_2(\Lambda)=2\pi D_{BM}^*(\Lambda).}
\tag{PL349-2}
\]

The interval normalization in (PL349-1) is important: some references define the radius using `(-a,a)` and therefore display a different factor of two.

Fix the endpoint envelope `u_A` of `PL-347`/`PL-348` on `I_A=(-A,A)` and the source-selected modulation family

\[
u_{A,\lambda}(x):=u_A(x)e^{i\lambda x},\qquad \lambda\in\Lambda.
\tag{PL349-3}
\]

Then, for every `A>0`, the following strict-threshold statements hold:

\[
2A<R_2(\Lambda)
\quad\Longrightarrow\quad
\overline{\operatorname{span}\{u_{A,\lambda}:\lambda\in\Lambda\}}^{\,\mathrm{form}}
=D(Q_W^A),
\tag{PL349-4}
\]

whereas

\[
2A>R_2(\Lambda)
\quad\Longrightarrow\quad
\overline{\operatorname{span}\{u_{A,\lambda}:\lambda\in\Lambda\}}^{\,\mathrm{form}}
\ne D(Q_W^A).
\tag{PL349-5}
\]

Consequently the supremal aperture at which this endpoint-modulation family is automatically a form core is exactly

\[
\boxed{
A_{\rm core}(\Lambda)
:=\sup\{A:\operatorname{span}\{u_{A,\lambda}\}\text{ is a form core}\}
=\frac12R_2(\Lambda)
=\pi D_{BM}^*(\Lambda).
}
\tag{PL349-6}
\]

No claim is made about the single boundary aperture `2A=R_2(Lambda)`; completeness at the critical endpoint is not determined by the radius alone and is irrelevant to the supremal identity (PL349-6).

Thus `PL-348`'s superlinear-counting gate was only an easy sufficient test for the infinite-radius side. The exact generic boundary is Beurling–Malliavin density:

\[
D_{BM}^*(\Lambda)=\infty
\quad\Longrightarrow\quad
\text{the restricted modulation family is a form core on every finite aperture.}
\tag{PL349-7}
\]

Conversely, a source-selected frequency family can avoid automatic form-core collapse on all sufficiently large apertures only if

\[
D_{BM}^*(\Lambda)<\infty.
\tag{PL349-8}
\]

For the canonical prime frequencies `Lambda_P={log p}`, `PL-348` already proved completeness on every finite interval by elementary exponential-type zero counting. Combining that result with (PL349-2) gives

\[
D_{BM}^*(\{\log p\})=\infty.
\tag{PL349-9}
\]

So the prime-log family lies at the maximally overcomplete end of the sharp Beurling–Malliavin classification, not merely beyond the coarse superlinear-counting gate.

## 1. Classical completeness radius and the Sobolev bridge

Beurling and Malliavin solved the interval completeness problem for exponential systems. In the normalization (PL349-1), a modern statement is Theorem 4 of N. Makarov and A. Poltoratski, “Two-spectra theorem with uncertainty,” *Journal of Spectral Theory* **9** (2019), 1249–1285, DOI `10.4171/JST/276`: for a discrete sequence `Lambda`,

\[
R_2(\Lambda)=2\pi D_{BM}^*(\Lambda).
\]

The original completeness theorem is A. Beurling and P. Malliavin, “On the closure of characters and the zeros of entire functions,” *Acta Mathematica* **118** (1967), 79–93, DOI `10.1007/BF02392477`.

The form-domain bridge in `PL-348` uses `H^s(I_A)` with any fixed `0<s<1/2`, so one must check that changing from `L^2` to this stronger topology does not change the **radius**. Define

\[
R_s(\Lambda)
:=\sup\{L>0:\{e^{i\lambda x}\}_{\lambda\in\Lambda}
\text{ is dense in }H^s(0,L)\}.
\tag{PL349-10}
\]

Then

\[
\boxed{R_s(\Lambda)=R_2(\Lambda)}
\qquad(0<s<1/2).
\tag{PL349-11}
\]

One inequality is immediate: `H^s`-density implies `L^2`-density because `H^s(0,L)` is dense in `L^2(0,L)` and the embedding `H^s -> L^2` is continuous.

For the reverse radius inequality, fix `L<R_2(Lambda)` and suppose the exponentials are not dense in `H^s(0,L)`. Standard Sobolev duality gives a nonzero compactly supported distribution `T in H^{-s}` supported in `[0,L]` such that

\[
\langle T,e^{i\lambda x}\rangle=0
\qquad(\lambda\in\Lambda).
\tag{PL349-12}
\]

Convolve `T` with a compactly supported smooth approximate identity `phi_epsilon`. For all sufficiently small `epsilon>0`,

\[
g_\epsilon:=T*\phi_\epsilon\ne0,
\]

`g_epsilon` is smooth and supported in an interval of length at most `L+2 epsilon`, and

\[
\widehat g_\epsilon(\lambda)
=\widehat T(\lambda)\widehat\phi_\epsilon(\lambda)=0
\qquad(\lambda\in\Lambda).
\tag{PL349-13}
\]

Choose `epsilon` with `L+2 epsilon<R_2(Lambda)`. Then `g_epsilon` is a nonzero `L^2` annihilator on an interval strictly inside the Beurling–Malliavin completeness radius, a contradiction. Hence every `L<R_2` lies in the `H^s` completeness regime. Together with the first inequality this proves (PL349-11) at the level of the supremal radius; it deliberately says nothing about completeness exactly at `L=R_2`.

This smoothing argument is generic functional analysis, not a new Beurling–Malliavin theorem. Its role is only to transfer the classical `L^2` threshold into the Sobolev topology already used by the localized Weil form.

## 2. The same radius is the endpoint-modulation form-core radius

For `2A<R_2(Lambda)`, (PL349-11) makes the exponentials dense in `H^s(-A,A)`. The proof of `PL-348` then applies unchanged: divide a compactly supported smooth test function by the positive endpoint envelope `u_A`, approximate the quotient in `H^s` by finite `Lambda`-exponential sums, multiply back by `u_A`, and use

\[
\log(2+|\xi|)\ll_s 1+|\xi|^{2s}
\]

to obtain convergence in the completed Weil form norm. This proves (PL349-4).

The converse is even simpler and does not require a sharp comparison between the form norm and `H^s`. If `2A>R_2(Lambda)`, the exponential system is incomplete in `L^2(I_A)`. Therefore there is a nonzero `g in L^2(I_A)` with

\[
\int_{I_A}e^{i\lambda x}\overline{g(x)}\,dx=0
\qquad(\lambda\in\Lambda).
\tag{PL349-14}
\]

On a fixed finite interval the endpoint envelope `u_A` is bounded above and bounded away from zero. Hence `h=g/u_A` also lies in `L^2(I_A)`, and

\[
\langle u_Ae^{i\lambda x},h\rangle_{L^2}=0
\qquad(\lambda\in\Lambda).
\tag{PL349-15}
\]

The completed local form norm controls the `L^2` norm, so pairing with `h` is a continuous nonzero functional on the form domain. It annihilates the whole algebraic span of the states (PL349-3). The span therefore cannot be a form core. This proves (PL349-5) and hence the exact supremal threshold (PL349-6).

The point of the converse is important for the research frontier: finite Beurling–Malliavin radius is not merely failure of one convenient Sobolev proof. Beyond its radius there is an actual continuous form-domain annihilator, so pure local density really is unavailable.

## 3. Consequence for the intermediate-sufficiency route

The live question after `PL-347` and `PL-348` is whether a source-forced restricted family can retain enough completed Weil information to force the desired zero restriction without merely reconstructing the entire localized Weil form. Beurling–Malliavin theory divides frequency-only proposals into two exact regimes.

If `D_BM^*(Lambda)=infinity`, then the endpoint-modulation Gram family is automatically a form core on every finite aperture. Positivity on all of its finite Gram matrices is therefore exactly the full localized Weil positivity problem in redundant coordinates. No source selectivity survives at the level of unconstrained linear span.

If `D_BM^*(Lambda)<infinity`, the family ceases to be a form core once `A>pi D_BM^*(Lambda)`. That avoids the automatic-collapse objection, but it also removes density as a possible explanation of global sufficiency. Any RH-relevant criterion based on such a family must then supply an additional mechanism: a relation coupling different apertures, constrained coefficients, a target-relative operator relation, or another arithmetic theorem showing that positivity on a genuinely incomplete family controls the missing directions.

This is sharper than the `N_Lambda(R)=O(R)` escape condition recorded in `PL-348`. Linear global counting is not the exact invariant; the exterior Beurling–Malliavin density measures the long-interval concentration that actually governs completeness. A globally thin-looking set can therefore still fail the intended sparsity test if its effective BM density is infinite.

## 4. Prior-art and novelty audit

The decisive harmonic-analysis theorem is entirely classical: Beurling–Malliavin completeness theory already gives (PL349-2). The 1967 Acta paper is the primary source, and Makarov–Poltoratski give an audit-friendly modern statement with the normalization used here. The equality of the supremal `L^2` and `H^s` radii follows by the elementary compact-support smoothing argument above; the passage from `H^s` completeness to Weil-form core density is inherited from `PL-348`, while the `L^2` annihilator gives the converse.

A targeted literature audit on 18 September 2026 did not locate this exact endpoint-envelope/localized-Weil formulation. That absence is not treated as evidence of mathematical novelty. The durable contribution is a **route classification** inside `prime_lattice`: it replaces the coarse superlinear zero-count gate of `PL-348` by the exact classical completeness invariant and identifies the precise aperture beyond which an incomplete source-selected family is genuinely smaller than the full Weil form.

This is not a new RH criterion. It does not use the rational-prime arithmetic of `Lambda` except when specializing to `{log p}`; any generic real frequency set with the same BM completeness radius has the same local form-core threshold. That lack of prime selectivity is itself the matched-control reason to treat the result as a boundary/negative rather than as progress toward RH.

## 5. Adversarial boundaries

1. **No statement is made at the critical aperture.** The radius determines strict inside/outside behavior and the supremal threshold; endpoint completeness can require extra information about `Lambda`.

2. **Finite BM radius is only an escape from automatic density.** It does not imply that restricted positivity is arithmetically sufficient, stable, or useful. It creates missing directions that a separate theorem would have to control.

3. **The result assumes unconstrained finite linear combinations.** Positive coefficients, nonlinear source laws, cross-aperture constraints, noncommutative state families, or other restrictions can fall outside ordinary exponential completeness.

4. **The result is local in physical/logarithmic aperture.** It does not give uniform frame bounds as `A` grows and does not classify conditioning inside the completeness regime.

5. **No rational-prime selectivity is created.** Beurling–Malliavin density is an ambient harmonic-analysis invariant. The specialization `{log p}` only says that the canonical prime-log proposal is even more decisively overcomplete than the elementary test in `PL-348` already showed.

6. **No continuation shortcut occurs.** All zeta-zero sensitivity remains inside the pre-existing completed Weil form. The present theorem only classifies when a chosen modulation family reconstructs that form by density.

## Research consequence

The source-selected modulation problem now has an exact first gate. Before analyzing any proposed frequency family `Lambda`, compute or bound its exterior Beurling–Malliavin density. Infinite BM density closes the proposal immediately as another complete coordinate system for local Weil positivity. Finite BM density is necessary for a genuinely intermediate family on arbitrarily large apertures, but then the burden moves to a new arithmetic sufficiency mechanism because local completeness provably fails beyond `A=pi D_BM^*(Lambda)`.

For the bare Prime-Lattice choice `{log p}`, that gate is already terminal: its BM density is infinite. The next viable candidate must therefore thin or constrain the source family in a way that changes the BM completeness class, or leave the frequency-only linear-span setting altogether.