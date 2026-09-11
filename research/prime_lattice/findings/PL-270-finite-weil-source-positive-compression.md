# PL-270 — Fixed-band Weil prime blocks admit exact positive compression to at most 2N+1 prime-power atoms

**Evidence:** `LITERATURE+DERIVED`

**Status:** `DECISIVE-NEGATIVE + FINITE-BAND-NONIDENTIFIABILITY + PRIOR-ART-COMBINATION`

## Claim

Fix a prime cutoff `c>1`, put `L=log c`, and fix a Connes–van Suijlekom/Connes–Consani–Moscovici Galerkin band `N`. Write the active zeta prime-power source as the positive discrete measure

\[
\nu_c:=\sum_{q=p^a\le c}\frac{\Lambda(q)}{\sqrt q}\,\delta_{\omega_q},
\qquad
\omega_q:=1-\frac{\log q}{L}\in[0,1].
\]

The actual prime source carries the overall minus sign used in the Weil form. Akiva Groskin's finite-source calculus proves that at level `N` the map from a finite signed source measure on `[0,1]` to its Galerkin matrix factors **exactly** through a real quotient of dimension `2N+1`. Combining that theorem with the discrete Carathéodory–Tchakaloff theorem gives the following exact compression.

There exist active prime powers `q_1,...,q_m<=c` and positive numbers `a_1,...,a_m`, with

\[
m\le 2N+1,
\]

such that the sparse positive measure

\[
\widetilde\nu_{c,N}:=\sum_{j=1}^m a_j\,\delta_{\omega_{q_j}}
\]

produces **the identical level-`N` prime Galerkin matrix** as `nu_c`. Equivalently, after leaving the pole and archimedean blocks unchanged, replacing the full von Mangoldt source by this sparse reweighted subset of its own prime-power locations leaves the entire completed finite Weil matrix unchanged entry by entry, and therefore leaves every eigenvalue and quadratic value at that band unchanged.

Consequently, whenever the number of active prime-power atoms exceeds `2N+1`, a single fixed-band Weil matrix cannot identify the detailed rational-prime-power event stream even inside the cone of positive source measures supported on the original active prime-power locations. It sees only the finite source quotient. Any zeta-specific source rigidity capable of forcing Weil positivity must therefore use information not contained in one fixed finite quotient: for example compatibility as `N` grows, the canonical von Mangoldt weights before quotienting, coupling across changing cutoffs, or additional completed/global structure.

This is a **finite-band identifiability obstruction**, not a claim that the full localized Weil form is arithmetically generic. It does not replace the zeta source by a Beurling prime system, does not preserve a zeta function or Euler product, and does not show that the `N->infinity` family can be compressed by one common sparse source.

## 1. Groskin's exact finite source quotient

For a finite signed Borel measure `mu` on `[0,1]`, Groskin attaches the sine source

\[
\psi_\mu(x)=\frac1\pi\int_{0}^{1}\sin(2\pi\omega x)\,d\mu(\omega)
\]

and its finite divided-difference/Galerkin matrix. His Corollary 2.4 proves that at band `N` the source-to-form map factors exactly through the `2N+1` coordinates

\[
\int\omega\,d\mu(\omega),
\]

and, for `1<=k<=N`,

\[
\int\sin(2\pi k\omega)\,d\mu(\omega),
\qquad
\int\omega\cos(2\pi k\omega)\,d\mu(\omega).
\]

Moreover the induced map from this coordinate vector to the finite matrix is injective: two finite signed sources give the same level-`N` matrix if and only if these `2N+1` coordinates agree. This statement is exact; it is not an asymptotic moment approximation and does not involve an archimedean numerical cutoff.

For the zeta prime block Groskin's source is

\[
\psi_p^{(c)}(x)
=-\frac1\pi\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}
\sin\!\left(2\pi x\left(1-\frac{\log q}{L}\right)\right),
\]

so it is precisely the source associated with `-nu_c` above. In exponent-lattice language the atoms are the prime-axis points `a e_p`, pushed through the scalar energy coordinate `log q=a log p` and then affinely normalized to `omega_q`.

Define the coordinate map

\[
F_N(\omega)
:=\bigl(
\omega,
\sin(2\pi\omega),\ldots,\sin(2\pi N\omega),
\omega\cos(2\pi\omega),\ldots,\omega\cos(2\pi N\omega)
\bigr)
\in\mathbb R^{2N+1}.
\]

The complete information about the positive prime measure visible to the level-`N` source block is therefore the single vector

\[
b_{c,N}
:=\int F_N(\omega)\,d\nu_c(\omega)
=\sum_{q=p^a\le c}
\frac{\Lambda(q)}{\sqrt q}F_N(\omega_q).
\]

## 2. Positive Carathéodory–Tchakaloff compression is exact

The vector `b_{c,N}` is a positive conic combination of the finitely many vectors `F_N(omega_q)`. The discrete Carathéodory–Tchakaloff theorem applies to an arbitrary finite-dimensional function space on a finite positive discrete measure: if `S` has restricted dimension `d` on the support, all `S`-moments can be reproduced by a positive quadrature using at most `d` nodes selected from that same support.

Apply the theorem to `nu_c` and the space spanned by the `2N+1` coordinate functions in `F_N`. If its restricted dimension on the active set is `d_{c,N}`, then

\[
d_{c,N}\le2N+1
\]

and there exist distinct active coordinates `omega_{q_j}` and positive weights `a_j` with `m<=d_{c,N}` such that

\[
\int\phi(\omega)\,d\nu_c(\omega)
=\sum_{j=1}^m a_j\phi(\omega_{q_j})
\qquad
\text{for every }\phi\in\operatorname{span}F_N.
\]

Hence

\[
\int F_N\,d\nu_c
=\int F_N\,d\widetilde\nu_{c,N}.
\]

Groskin's injective quotient now gives the matrix identity

\[
\boxed{
Q_N[-\nu_c]=Q_N[-\widetilde\nu_{c,N}]
}
\]

entry by entry. Adding the same pole and cutoff-free archimedean blocks to both sides preserves the equality for the completed finite Weil matrix.

This proof uses positivity rather than discarding it: the alias source can be chosen with **positive** effective masses and with nodes among the actual active rational-prime-power locations. If the original source has `M(c)>2N+1` atoms, at least `M(c)-(2N+1)` of those events can be deleted in such an exact alias. For every fixed `N`, this nontrivial compression occurs for all sufficiently large `c`, since the number of prime powers up to `c` tends to infinity.

## 3. What the obstruction removes from the live source-positivity search

`PL-264` showed that one prime-power threshold has universal local singular geometry: apart from its location and von Mangoldt scalar, the event jet contains no extra arithmetic freedom. The present result is a distinct joint-event obstruction. Even after many prime powers have accumulated, **one fixed finite Galerkin band does not retain them individually**. Their whole positive source contribution can be replaced by at most `2N+1` positively reweighted survivors without changing the finite matrix at all.

Therefore a proof that reasons only from the spectral geometry of one fixed `N` matrix cannot claim that its sign follows from the detailed presence of all rational-prime-power events: that matrix has an exact positive-source alias in which most events are absent. In particular, eigenvalue interlacing, finite-band determinants, condition numbers, inertia, or any other invariant of that one matrix inherit the same alias automatically.

The surviving arithmetic target is correspondingly sharper. The canonical zeta source supplies a **coherent family** of these quotients as the band and cutoff vary, with fixed masses `Lambda(q)/sqrt(q)` rather than freely reweighted effective masses. A genuinely source-forced RH mechanism may exploit that coherence. This finding only rules out extracting more source identity from a single fixed quotient than the quotient contains.

The distinction matters for the current localized-Weil frontier. `PL-269` turns RH into the large-aperture behavior of the continuum localized ground energy, while `PL-261`–`PL-268` make clear that finite cores are observability devices rather than independent positivity theorems. The compression above explains one reason: at any fixed Galerkin rank, the non-archimedean block has only finitely many source coordinates, no matter how many prime powers have entered the aperture. The missing sign theorem must survive the expansion of that coordinate system; it cannot be certified merely by counting or individually tracking the finite set of source events visible before projection.

## 4. Novelty and adversarial audit

Neither ingredient is new. Groskin proves the exact `2N+1` source quotient and its injectivity onto the finite matrix. Positive support-preserving compression of a discrete measure to at most the restricted dimension of a finite-dimensional function space is the classical discrete Carathéodory–Tchakaloff theorem. The literature audit found no source presenting their combination specifically as a zeta/Weil finite-band nonidentifiability theorem, but absence from a search is not evidence of novelty. The durable content recorded here is therefore a **prior-art combination used as a line-specific obstruction**, not a novelty claim.

Several stronger statements are deliberately excluded. The compressed weights `a_j` need not equal the canonical `Lambda(q_j)/sqrt(q_j)` weights, so this does not construct a second arithmetic source satisfying the zeta Euler product. The compression is allowed to depend on `(c,N)`; no common sparse source for all bands is asserted. As `N` grows, the quotient grows and can recover source information that one fixed band discards. The result also says nothing by itself about positivity or negativity of the common matrix: it proves exact source nonidentifiability at finite rank, not a sign theorem.

A proposed fixed-band source mechanism would evade this obstruction only if it uses data not determined by the Galerkin matrix/source quotient itself—for example the canonical pre-projection weight labels, a compatibility law relating multiple `N` or `c`, or a completed relation that is demonstrably destroyed by the Tchakaloff alias. Without such extra data, replacing `nu_c` by `widetilde nu_{c,N}` is an exact matched control.

## Sources

- Akiva Groskin, **“A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3 [math.NT] (submitted 2 July 2026; revised 14 August 2026). In particular Lemma 2.3 and Corollary 2.4 give the finite source calculus and exact `2N+1` source quotient, while Theorem 2.5 identifies the corresponding finite quadratic values with exact Guinand–Weil zero sums.
- Federico Piazzon, Alvise Sommariva, Marco Vianello, **“Caratheodory-Tchakaloff Subsampling,”** *Dolomites Research Notes on Approximation* **10**(1) (2017), 5–14. DOI: https://doi.org/10.14658/PUPJ-DRNA-2017-1-2. arXiv: https://arxiv.org/abs/1611.02065. Theorem 1 gives the positive support-preserving compression of a finite discrete measure for an arbitrary finite-dimensional function space.
