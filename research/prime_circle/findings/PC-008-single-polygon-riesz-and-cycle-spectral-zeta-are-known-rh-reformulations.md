# PC-008 — single-polygon Riesz energy and cycle spectral zeta are already known RH reformulations

**Status:** `DECISIVE-PRIOR-ART` + `BRANCH-CLOSED-AS-NOVELTY`

## Exact identification

For the regular `N`-gon, let

\[
\zeta_N=e^{2\pi i/N}.
\]

The chord lengths from the common vertex satisfy

\[
|1-\zeta_N^k|^2
=4\sin^2\frac{\pi k}{N}.
\]

But the combinatorial cycle graph `C_N` has Laplace eigenvalues

\[
\lambda_k
=4\sin^2\frac{\pi k}{N},
\qquad 1\le k\le N-1.
\]

Hence the per-vertex Riesz `s`-energy of the polygon is exactly a graph spectral zeta:

\[
\boxed{
\sum_{k=1}^{N-1}|1-\zeta_N^k|^{-s}
=
\sum_{k=1}^{N-1}\lambda_k^{-s/2}
=
\zeta_{C_N}(s/2)
}
\]

(up to the harmless normalization convention for the graph Laplacian).

The full ordered-pair Riesz energy is therefore

\[
L_s(N)=N\,\zeta_{C_N}(s/2).
\]

So one of the most natural out-of-the-box ideas suggested by the original construction — treating each polygon itself as a spectral object via its chord geometry — is not merely analogous to a known graph model: it **is exactly the cycle-graph spectral zeta model**.

## Existing Riesz-energy theory

Brauchart, Hardin and Saff derived the complete large-`N` asymptotic expansion of the Riesz energy of the `N`th roots of unity. In their notation,

\[
L_s(N)
=
V_sN^2
+
\frac{2}{(2\pi)^s}
\sum_{j=0}^{p}
\alpha_j(s)\zeta(s-2j)N^{1+s-2j}
+
O_{s,p}(N^{-1+\Re s-2p}),
\]

away from the exceptional positive odd integers, with the corresponding modified formulas there.

In particular the leading finite-size discrepancy is

\[
L_s(N)-V_sN^2
\sim
\frac{2\zeta(s)}{(2\pi)^s}N^{1+s}.
\]

Thus a nontrivial zero `rho` can indeed be described geometrically as an interaction exponent at which this leading polygon-energy correction disappears. That is an attractive geometric sentence, but it follows immediately from established Riesz-energy asymptotics and is only a reformulation of `zeta(rho)=0`.

## Existing graph-spectral RH theory

Friedli and Karlsson subsequently studied the spectral zeta functions of the finite cycles `Z/NZ` precisely in the critical strip. They proved detailed asymptotics and showed that RH is equivalent to an approximate functional equation for these finite graph spectral zeta functions.

Therefore the chain

\[
\text{regular polygon}
\to
\text{chord spectrum}
\to
\text{cycle Laplacian}
\to
\text{spectral zeta}
\to
\text{RH-equivalent functional relation}
\]

is already established prior art.

## Research consequence

Close as a source of novelty any branch based only on a **single polygon at level `N`** and one of the following equivalent objects:

- its list of chord lengths from a vertex;
- its ordinary Riesz energy;
- the Laplacian of the cycle graph `C_N`;
- the spectral zeta of that cycle;
- the disappearance of the leading Riesz finite-size term at a zero of `zeta`;
- the known approximate-functional-equation RH reformulation for cycle graph zetas.

This does not make the original prime-circle uninteresting. It says that new information must come from structure **between polygon levels** — birth/refinement labels, primitive-shell interactions, scale dynamics, or a genuinely coupled inside/outside construction — rather than from the spectrum/energy of each regular polygon separately.

## Prior art

- J. S. Brauchart, D. P. Hardin, E. B. Saff, *The Riesz energy of the N-th roots of unity: an asymptotic expansion for large N*, Bull. Lond. Math. Soc. 41 (2009), 621–633, DOI 10.1112/blms/bdp034.
- F. Friedli, A. Karlsson, *Spectral zeta functions of graphs and the Riemann zeta function in the critical strip*, Tohoku Math. J. 69 (2017), 585–610, arXiv:1410.8010. Their main result includes an RH-equivalent approximate functional equation for finite cycle-graph spectral zeta functions.
- Later work on cycle-graph spectral zeta/L-functions explicitly notes that these graph functions naturally approximate Riemann/Dirichlet zeta and `L`-functions and develops their special values.

This finding is a prior-art closure, not a claim of novelty.
