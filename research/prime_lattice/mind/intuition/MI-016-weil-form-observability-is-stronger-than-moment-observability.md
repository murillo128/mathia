# MI-016 — Completed Weil order is a one-sided index ledger with exact support exhaustion

**Evidence level:** proved observability/order/exhaustion boundary through PL-281; completed arithmetic positivity and any zero-count identification remain open.

The complete Galerkin/cutoff family can recover the source, but source recovery and cutoff coherence are generic information properties rather than sign principles. PL-272--PL-276 show that every nonzero finite positive interior source is eventually sign-indefinite and no fixed compact self-adjoint correction repairs that high-frequency Morse defect.

PL-278 identifies what the canonical noncompact completion buys: the localized completed Weil operator has compact resolvent and only finitely many negative eigenvalues, with eventual positivity of the high spectral tail. PL-279 shows that a newly active prime-power shift turns on quadratically softly in the natural Sobolev form topology, so the finite residual sector is not driven by an isolated threshold shock.

PL-280 gives the order law. Because the localized form domains are nested under aperture growth,

\[
\lambda_k(b)\le\lambda_k(a)\qquad(a<b),
\]

and the negative Morse index `nu(a)` is nondecreasing. Once a variational level becomes negative, later source events cannot restore it.

PL-281 shows that this one-sided ledger exhausts the global compact-support form exactly. If

\[
\kappa_c:=\operatorname{ind}_-(q|_{\cup_aD_a}),
\]

then

\[
\kappa_c=\sup_a\nu(a)=\lim_{a\to\infty}\nu(a).
\]

The proof needs no eigenvector convergence: every finite-dimensional negative subspace has a finite basis and therefore fits inside one common support window. Consequently a finite global negative sector cannot drift to infinity unseen. If `\kappa_c=r<\infty`, then `nu(a)=r` for every sufficiently large `a`; if `\kappa_c=\infty`, the finite-aperture indices are unbounded.

The source-specific problem is therefore **whether the first crossing occurs at all**. Proving `nu(a)=0` for every finite aperture already excludes every compact-support negative direction; there is no separate localization-completeness theorem to prove afterward. Conversely any compact-support violation appears at finite aperture and remains in the index ledger thereafter.

**Boundary.** The exhaustion identity is generic functional analysis for nested support domains. It does not identify `\kappa_c` with Bombieri's Fourier-side index, count off-critical zeros, or prove Weil positivity. Those are separate arithmetic bridges; the result only removes “finite negative defect escaping all finite windows” as a possible loophole in the canonical support exhaustion.