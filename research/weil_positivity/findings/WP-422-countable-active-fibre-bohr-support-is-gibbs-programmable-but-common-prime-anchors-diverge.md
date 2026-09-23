---
id: WP-422
title: Countable active-fibre Bohr support is Gibbs-programmable, while common critical prime anchors diverge
branch: weil_positivity
status: supported
kind: infinite-active-fibre-gibbs-bohr-programmability-and-common-anchor-obstruction
claim_strength: exact RH-independent universality/control for infinite autonomous type-I active fibres at beta=1, plus an exact trace-class obstruction to realizing every prime logarithmic gap from one finite-energy anchor
created: 2026-09-24
related: [WP-209, WP-215, WP-227, WP-255, WP-421]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary, CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
  - WP-255, which gives a different critical KMS packing obstruction for globally orthogonal prime ranges
---

# WP-422 — Countable active-fibre Bohr support is Gibbs-programmable, while common critical prime anchors diverge

## Claim

`WP-421` leaves an infinite active auxiliary spectrum as one possible way to compensate infinitely many Bost--Connes time degrees. There are two sharply different versions of that escape.

First, **mere countable spectral capacity is completely programmable even inside an honest critical Gibbs fibre**. Let `(omega_j)_(j>=1)` be any countable sequence of real numbers, and let `(w_j)_(j>=1)` be any strictly positive probability vector. There is a separable unital type-I C*-algebra

\[
B=\left(\bigoplus_{j\ge1}^{c_0}M_2(\mathbf C)\right)^\sim,
\]

with a norm-continuous autonomous dynamics `tau`, represented on

\[
\mathcal H=\bigoplus_{j\ge1}\mathbf C^2,
\]

by a positive self-adjoint Hamiltonian `K` with compact resolvent, such that:

1. every prescribed `omega_j` occurs as a Bohr frequency of `tau` on the `j`-th block;
2. `e^{-K}` is trace class and `Tr(e^{-K})=1`;
3. the beta-one Gibbs state assigns total mass exactly `w_j` to the `j`-th two-level block.

In particular, taking `omega_j=log p_j` programs **all prime logarithmic frequencies** into a perfectly normalized beta-one Gibbs auxiliary system. Replacing the primes by any countable nonarithmetic frequency set changes nothing.

Second, the most direct common-vacuum implementation has the opposite behavior. Let `K` be self-adjoint on a Hilbert space, suppose

\[
Z_\beta=\operatorname{Tr}(e^{-\beta K})<\infty,
\]

and let `xi` be a finite-energy eigenvector, `Kxi=E xi`. If for every prime `p` there is a bounded homogeneous operator `V_p` satisfying

\[
e^{itK}V_pe^{-itK}=p^{it}V_p,
\qquad
V_p\xi\ne0,
\]

then necessarily

\[
Z_\beta\ge e^{-\beta E}\sum_p p^{-\beta}.
\]

Hence no such common finite-energy anchor can coexist with a trace-class Gibbs partition function at `beta<=1`; in particular it is impossible at the critical value `beta=1`.

So the infinite-fibre survivor of `WP-421` splits into a precise dichotomy. **Disjoint, prime-dependent anchor sectors make arbitrary all-prime Bohr support cheap and programmable; a single finite-energy anchor carrying every prime gap makes the critical Gibbs trace diverge.** The missing Mathia structure therefore cannot be certified merely by exhibiting infinitely many compensating frequencies. It has to force their incidence, sector geometry, or coupling from the arithmetic/global source.

**Classification:** `EXACT-DERIVED-TYPE-I-GIBBS-UNIVERSALITY + ARBITRARY-COUNTABLE-BOHR-SUPPORT + ARBITRARY-CRITICAL-BLOCK-MASSES + COMMON-ANCHOR-PRIME-HARMONIC-DIVERGENCE + MATCHED-NONARITHMETIC-CONTROL + SOURCE-FORCING-STILL-MISSING + TYPE-III/INTERACTING-ESCAPES-REMAIN + NOT-A-WEIL-POSITIVITY-PROOF`.

## Exact programmable construction

Put `Delta_j=|omega_j|` and

\[
q_j=1+e^{-\Delta_j},
\qquad
E_j=\log\frac{q_j}{w_j}.
\]

Since `0<w_j<=1` and `1<=q_j<=2`, every `E_j` is nonnegative. On the `j`-th copy of `C^2`, choose basis vectors `e_(j,0),e_(j,1)` and define

\[
K e_{j,0}=E_j e_{j,0},
\qquad
K e_{j,1}=(E_j+\Delta_j)e_{j,1}.
\]

Because a positive summable sequence satisfies `w_j -> 0`, one has `E_j -> infinity`. Therefore `K` has compact resolvent. Moreover

\[
\operatorname{Tr}(e^{-K})
=\sum_j e^{-E_j}(1+e^{-\Delta_j})
=\sum_j w_j
=1.
\]

The restriction

\[
\tau_t=\operatorname{Ad}(e^{itK})|_B
\]

is norm continuous on the `c_0` direct sum: continuity is uniform on finitely many leading blocks and the tail has arbitrarily small norm. The scalar block offsets `E_j I_2` cancel from `Ad(e^{itK})`; only the gap `Delta_j` enters the dynamics.

If `omega_j>0`, the matrix unit `|e_(j,1)><e_(j,0)|` transforms by `e^{it omega_j}`. If `omega_j<0`, use its adjoint; if `omega_j=0`, any nonzero diagonal matrix unit supplies the zero-frequency block. Thus the prescribed sequence is contained in the Bohr point spectrum. The normalized Gibbs state

\[
\psi(b)=\operatorname{Tr}(e^{-K}b)
\]

has block mass `w_j` by construction.

This exposes an important gauge of programmability that is invisible if one looks only at the automorphism group. The offsets `E_j` do not change `tau` at all, yet they can assign an arbitrary positive probability vector to the disconnected frequency blocks at beta one. Both the requested frequency labels and their equilibrium sector weights can therefore be supplied by auxiliary design rather than arithmetic structure.

For the Bost--Connes survivor, enumerate the primes `p_j` and set `omega_j=log p_j`. Any convenient summable `w_j`, for example a geometric sequence, then gives an ordinary trace-class beta-one auxiliary Gibbs fibre containing every prime logarithmic gap. This directly shows that the infinite-dimensional escape in `WP-421` is not by itself a rigidity theorem.

## Common-anchor critical obstruction

Assume now that `xi` and the `V_p` satisfy the hypotheses in the claim. From

\[
e^{itK}V_p\xi
=p^{it}V_pe^{itK}\xi
=e^{it(E+\log p)}V_p\xi
\]

for every real `t`, the spectral theorem gives

\[
K(V_p\xi)=(E+\log p)V_p\xi.
\]

After normalizing, `eta_p=V_p xi/||V_p xi||` is a unit eigenvector of `K` at energy `E+log p`. Distinct primes give distinct eigenvalues, hence the family `(eta_p)_p` is orthonormal. Positivity of `e^{-beta K}` then yields

\[
Z_\beta
\ge\sum_p\langle\eta_p,e^{-\beta K}\eta_p\rangle
=e^{-\beta E}\sum_p p^{-\beta}.
\]

The prime sum diverges for `beta<=1`. No orthogonality hypothesis on the **ranges** of the `V_p` is required; orthogonality of the particular vectors `V_p xi` is forced automatically by their distinct energy eigenvalues.

More generally, the same proof applies to any set of positive ratios whose beta-powers have divergent sum. Conversely, the argument says nothing when each prime uses a different anchor `xi_p` of energy `E_p`; the lower bound then has the weighted shape `sum_p e^{-beta E_p}p^{-beta}`, which can converge if the anchors escape to high energy. That is exactly how the programmable two-level construction evades the common-anchor obstruction.

## Relation to the current Bost--Connes route

`WP-421` proves that a fixed finite-dimensional autonomous fibre has only finitely many Bohr gaps and therefore can mix only finitely many prime-valuation directions. The present result tests the first surviving categorical enlargement rather than merely repeating that finite-dimensional bound.

The outcome is deliberately two-sided. Infinite dimension removes the finite-capacity obstruction immediately: one can install all `log p` gaps while retaining a normalized trace-class Gibbs state at beta one. But the construction succeeds only by putting the different gaps in disconnected blocks and by choosing central block offsets whose sole job is to make the Gibbs masses summable. Those offsets are not forced by the Bost--Connes source and are invisible to the auxiliary dynamics itself. Consequently an all-prime Bohr spectrum is **expressivity**, not evidence of a canonical finite--archimedean incidence law.

At the other extreme, deriving every prime gap from one common finite-energy vacuum or source vector is too rigid for a type-I critical Gibbs realization: the prime harmonic series appears directly in the partition trace. A viable active-fibre continuation must therefore explain, from the source, why the prime sectors are distributed through energy in a summable but non-programmable way, or must leave this trace-class type-I category through a genuinely coupled/type-III/weight-valued construction.

This complements rather than duplicates `WP-227` and `WP-255`. `WP-227` concerns a frequency-matched **positive completion carrying the critical Weil amplitudes** and finds an infinite critical auxiliary trace. Here the first statement shows that frequency support alone has no such obstruction; it can be Gibbs-trace-class when the anchors are allowed to vary. `WP-255` assumes globally orthogonal prime isometry ranges and obtains a KMS packing contradiction. The common-anchor theorem above assumes no such global range orthogonality: one shared finite-energy vector plus distinct prime energy shifts already forces the required orthogonal test family.

## Adversarial controls and falsification

The strongest control is nonarithmetic. The programmable construction accepts an arbitrary countable real sequence `(omega_j)`, so prime logarithms play no privileged role. Any claim that the construction itself detects arithmetic structure is therefore false. Likewise, the positive weights `(w_j)` are arbitrary; the beta-one Gibbs normalization does not select Mangoldt coefficients, prime powers, archimedean Gamma terms, or the polar contribution.

The construction uses an honest positive Hamiltonian with compact resolvent and an ordinary trace-class Gibbs density at beta one. No regularized trace, signed state, zero data, RH input, or hidden limiting prescription is used. This makes the programmability diagnosis stronger: even the conventional analytic niceness of a type-I Gibbs fibre does not make its all-prime Bohr support canonical.

The common-anchor obstruction is falsifiable by a single counterexample: produce a self-adjoint `K` with `Tr(e^{-K})<infinity`, a finite-energy eigenvector `xi`, and nonzero homogeneous `V_p xi` of frequency `log p` for every prime. The spectral calculation would then produce an orthonormal eigenvector at every energy `E+log p`, contradicting the trace lower bound. The exact boundary is equally explicit: prime-dependent anchors with sufficiently increasing energies evade the theorem, as do frameworks in which there is no trace-class Gibbs Hamiltonian implementing the relevant KMS state.

The result does **not** rule out the critical Bost--Connes KMS state itself, whose beta-one regime is not a normal Gibbs trace in the canonical logarithmic representation; this boundary was already isolated in `WP-209`. It also does not rule out type-III fibres, semifinite/KMS-weight formulations, interacting joint dynamics not reducible to an autonomous tensor factor, source-dependent representations, or non-invariant scalarizations. None of those escapes supplies Weil positivity automatically.

## Prior-art and novelty audit

The Bost--Connes logarithmic Hamiltonian and its zeta partition function are classical, as are Bohr/energy-difference decompositions, compact-resolvent Gibbs Hamiltonians, and divergence of the prime harmonic series. General KMS and quasi-free-dynamics literature treats these ingredients at much greater breadth. Targeted searches across Bost--Connes/KMS, Bohr-spectrum, and prescribed-energy-gap terminology found no reason to attribute the elementary two-level direct-sum construction or the one-anchor trace estimate as new standalone operator-algebra theorems, and no such novelty is claimed.

The durable contribution is instead the **line-specific classification of the exact infinite-fibre escape left by `WP-421`**. It proves both that unrestricted countable compensating spectrum is too programmable to count as arithmetic structure and that the canonical common-anchor implementation is incompatible with a critical trace-class Gibbs fibre. This narrows the research mandate to the missing object it actually needs: source-forced incidence or coupling that survives between those two extremes and eventually incorporates the archimedean/global terms with an independent sign theorem.

## Consequence

**Supported exact boundary with a sharper survivor.** Moving from finite to infinite active fibres removes the finite Bohr-capacity obstruction, but in the unrestricted category it removes it trivially: arbitrary countable frequencies and arbitrary beta-one sector masses can be programmed. Requiring one common finite-energy anchor restores rigidity, but then all-prime critical Gibbs trace class is impossible. The live Bost--Connes route must therefore derive a non-programmable, source-forced distribution of prime-frequency incidence across the auxiliary geometry, or make a justified category change. Mere all-prime spectral matching is not enough.