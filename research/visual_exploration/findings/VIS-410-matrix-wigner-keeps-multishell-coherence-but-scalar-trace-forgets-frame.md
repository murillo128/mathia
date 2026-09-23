# VIS-410 — matrix-valued Wigner retains multi-shell coherence while scalar aggregation forgets the frame

## Claim

Let

`F=(f_1,...,f_K)`

be a finite labelled family of nonzero profiles in `L^2(R)`, for example logarithmic-coordinate shell profiles as in `VIS-409`. Define the matrix-valued cross-Wigner field

`W_F(u,xi) = [ W(f_j,f_k)(u,xi) ]_(j,k=1)^K`,

where

`W(f,g)(u,xi)=int_R f(u+tau/2) conjugate(g(u-tau/2)) exp(-2 pi i xi tau) d tau`.

Then the full matrix field is exactly the Weyl symbol of the rank-one operator

`|F><F|`

on `L^2(R) tensor C^K`. Fourier inversion in `xi` recovers every block kernel

`f_j(x) conjugate(f_k(y))`.

Consequently `W_F` determines the entire labelled vector `F` up to one common global unimodular phase. In particular it retains the relative phases and cross-shell coherences that are absent from the separate auto-Wigner portraits.

There are two exact information-loss boundaries.

1. Keeping only the diagonal portraits `{W(f_j,f_j)}` determines each shell ray separately but is invariant under the independent phase gauge

   `(f_1,...,f_K) -> (e^{i alpha_1}f_1,...,e^{i alpha_K}f_K)`.

   Relative phases between shells are lost.

2. Collapsing further to the scalar trace portrait

   `W_tr = sum_j W(f_j,f_j)`

   gives the Weyl symbol of the positive frame/density operator

   `rho_F = sum_j |f_j><f_j|`.

   For every `U in U(K)`, if

   `g_a = sum_j U_(a j) f_j`,

   then

   `sum_a |g_a><g_a| = rho_F`.

   Hence `W_tr` is invariant under arbitrary unitary mixing of the shell labels. It remembers the frame operator but not a particular labelled decomposition into shells.

Thus the visual hierarchy is exact:

`full cross-Wigner matrix  -> common U(1) gauge only`,

`diagonal auto-Wigners     -> independent U(1)^K phase gauge`,

`scalar trace aggregation  -> U(K) frame-mixing gauge`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-WEYL/WIGNER-OPERATOR-CORRESPONDENCE + DECISIVE-REPRESENTATION-CONTROL + NO-NOVELTY-CLAIM`.

The result does not assert that a matrix-valued Wigner portrait contains a new arithmetic mechanism. It identifies precisely when multi-shell phase-space visualization preserves already-existing relational information and when scalarization destroys it.

## 1. The matrix-valued portrait is one rank-one state on an enlarged Hilbert space

Put

`H = L^2(R)`

and regard the labelled family as the single vector

`F = sum_j f_j tensor e_j in H tensor C^K`,

where `{e_j}` is the standard shell-label basis.

For each pair `(j,k)`, Fourier inversion of the cross-Wigner distribution in `xi` gives

`int_R W(f_j,f_k)(u,xi) exp(2 pi i xi tau) d xi`
` = f_j(u+tau/2) conjugate(f_k(u-tau/2))`.

With

`x=u+tau/2`, `y=u-tau/2`,

this becomes

`K_(j,k)(x,y)=f_j(x) conjugate(f_k(y))`.

The block matrix `K_(j,k)` is exactly the integral kernel of the rank-one operator

`P_F = |F><F|`

on `H tensor C^K`. Therefore the complete matrix-valued Wigner field and the complete rank-one state are equivalent representations:

`W_F <-> P_F`.

If two nonzero labelled vectors `F,G` have the same matrix-valued Wigner field, then `P_F=P_G`. Equality of nonzero rank-one operators implies

`G=e^{i alpha}F`

for one constant phase `alpha`. The full cross-Wigner matrix therefore loses only the common global phase of the whole labelled family.

This is the finite multi-shell analogue of `VIS-409`, but the distinction is important. `VIS-409` treated cross-Wigner portraits of descendants generated deterministically from one shell; there the off-diagonal blocks contain no source information beyond that one shell and the fixed descendant operators. Here the inputs may be genuinely independent source objects. The matrix portrait then preserves their existing relative coherence, but it still does not manufacture any information that was not already present in the labelled vector `F`.

## 2. Separate auto-Wigner portraits forget exactly the relative shell phases

For each nonzero shell, `VIS-409` gives

`W(f_j,f_j) <-> |f_j><f_j|`,

so the auto-Wigner portrait determines the ray of `f_j` but not its global phase. Hence the collection of diagonal portraits is unchanged under independent shell phases

`f_j -> e^{i alpha_j} f_j`.

The full matrix reacts differently:

`W(e^{i alpha_j}f_j,e^{i alpha_k}f_k)`
` = e^{i(alpha_j-alpha_k)} W(f_j,f_k)`.

Thus each off-diagonal block carries a relative phase. Once the complete matrix is retained, all phase differences are tied together and only a single common phase remains invisible.

This gives a precise test for claims that a visually striking off-diagonal interference pattern reveals additional structure. The pattern may reveal **relational information that separate shell portraits discarded**, but that information is exactly the pre-existing cross-shell coherence of the labelled state. A claim of new arithmetic content requires an independent reason why the source construction forces a special off-diagonal block, phase relation, or invariant that fails on a matched class of labelled controls.

## 3. Scalar trace Wigner is the frame operator and forgets the shell decomposition

Now discard the matrix labels and keep only

`W_tr(u,xi)=tr_(C^K) W_F(u,xi)=sum_j W(f_j,f_j)(u,xi)`.

By linearity of the Weyl correspondence, `W_tr` is the Weyl symbol of

`rho_F = sum_j |f_j><f_j|`.

Let `U` be any `K x K` unitary matrix and define

`g_a = sum_j U_(a j) f_j`.

Then finite expansion and unitarity give

`sum_a |g_a><g_a|`
` = sum_(a,j,k) U_(a j) conjugate(U_(a k)) |f_j><f_k|`
` = sum_(j,k) delta_(j k) |f_j><f_k|`
` = sum_j |f_j><f_j|`
` = rho_F`.

Therefore

`W_tr(G)=W_tr(F)`

for every shell-space unitary mixing. The scalar portrait cannot distinguish a canonical shell family from a different orthonormal mixing of the same frame factorization.

When the `f_j` are linearly independent and the number of components is fixed to their rank, equality of the positive operator `rho` gives the usual unitary freedom of minimal factorizations. With redundant families the freedom is described by the corresponding partial-isometry enlargement. The precise classification is classical density-operator/frame theory; the elementary unitary invariance above is already enough for the present representation audit.

This is a stronger loss than the independent phase gauge of the diagonal portraits. The trace does not merely forget relative phases: it forgets which orthonormal coordinate system in coefficient space was called the shell decomposition.

## 4. Fixed scalar projections are single coherent superpositions, not a substitute for the full matrix

A common visualization strategy is to choose one coefficient vector `c` and plot the scalar quadratic contraction of the matrix field. With the coefficient convention

`h_c = sum_j c_j f_j`,

one has

`W(h_c,h_c)=sum_(j,k) c_j conjugate(c_k) W(f_j,f_k)`.

So every fixed scalar contraction is just the auto-Wigner portrait of one coherent superposition. By `VIS-409` it determines only the rank-one state of that one combined profile.

A finite family of such contractions can reconstruct the full matrix field only when the associated coefficient projectors span the real vector space of Hermitian `K x K` matrices. That space has dimension `K^2`. If the chosen coefficient projectors span a proper subspace, then there are nonzero Hermitian shell-space directions invisible to every plotted contraction, pointwise in phase space.

This gives a simple design rule for future visual experiments. A small number of hand-picked coherent sums may be useful probes, but they must not be described as retaining the complete multi-shell interaction unless their coefficient measurements are informationally complete for the shell-space matrix. Conversely, retaining the complete matrix is information-complete for the labelled vector but should still be interpreted as a representation of existing source data, not as evidence that a new coupling has been created.

## 5. Prior art and novelty boundary

The load-bearing mathematics is classical. Dias, de Gosson and Prata, *A Refinement of the Robertson-Schrodinger Uncertainty Principle and a Hirschman-Shannon Inequality for Wigner Distributions*, Journal of Fourier Analysis and Applications 25 (2019), 210-241, DOI `10.1007/s00041-018-9602-x`, explicitly identifies the cross-Wigner function with the Weyl symbol of the rank-one operator having kernel `f(x) conjugate(g(y))`. That is the operator correspondence used entry by entry above.

The nonuniqueness of pure-state ensemble decompositions of a fixed density operator is also classical. Hughston, Jozsa and Wootters, *A Complete Classification of Quantum Ensembles Having a Given Density Matrix*, Physics Letters A 183 (1993), 14-18, DOI `10.1016/0375-9601(93)90880-9`, gives the standard constructive classification. The finite unitary-mixing identity used here is the elementary frame version of that general freedom.

No novelty is claimed for matrix-valued Wigner transforms, density matrices, frame operators, or ensemble-unitary freedom. The Mathia-specific value is the **representation boundary after VIS-409**: a genuinely multi-shell phase-space visualization can preserve relational information only by retaining off-diagonal shell coherence; diagonal or scalarized portraits have exact gauge groups that quantify what has already been discarded.

## 6. Research consequence

Future visual work should distinguish three very different claims.

A full cross-Wigner matrix of genuinely separate source objects may be worthwhile because it preserves their relative coherence. Any interesting feature must then be translated into a statement about the underlying labelled multi-shell state and tested against matched labelled controls.

A collection of only auto-Wigner shell portraits cannot support a claim that depends on relative phase unless that phase is supplied independently. A scalar trace or frame-density portrait is weaker still: any feature invariant under the trace representation is compatible with arbitrary unitary remixing of the shell labels.

Accordingly, **matrix-valued phase space is a faithful microscope for already-present multi-shell coherence, not an additional arithmetic carrier**. The next admissible positive direction is not merely to draw a richer phase-space object. It is to identify a source-derived cross-shell relation, incidence law, or response mechanism whose off-diagonal structure is mathematically forced and discriminates the arithmetic source from matched multi-shell controls. Establishing such a source theorem is a separate research question and is intentionally left for a later invocation.