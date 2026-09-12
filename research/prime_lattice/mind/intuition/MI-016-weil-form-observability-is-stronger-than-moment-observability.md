# MI-016 — Completed Weil order is a one-sided index ledger; fixed-support positivity is finitely certifiable

**Evidence level:** proved observability/order/exhaustion boundary through PL-281, plus PL-282's literature-derived fixed-support Stieltjes hierarchy and PL-283's transfer of a non-peer-reviewed computer-assisted positivity claim at `a=0.8`; completed arithmetic positivity remains open.

The complete Galerkin/cutoff family can recover the source, but source recovery and cutoff coherence are generic information properties rather than sign principles. PL-272--PL-276 show that every nonzero finite positive interior source is eventually sign-indefinite and no fixed compact self-adjoint correction repairs that high-frequency Morse defect.

PL-278 identifies what the canonical noncompact completion buys: the localized completed Weil operator has compact resolvent and only finitely many negative eigenvalues, with eventual positivity of the high spectral tail. PL-279 shows that a newly active prime-power shift turns on quadratically softly in the natural Sobolev form topology, so the finite residual sector is not driven by an isolated threshold shock.

PL-280 gives the order law. Because localized form domains are nested under aperture growth,

\[
\lambda_k(b)\le\lambda_k(a)\qquad(a<b),
\]

and the negative Morse index `nu(a)` is nondecreasing. Once a variational level becomes negative, later source events cannot restore it. PL-281 shows that this ledger exhausts the global compact-support form exactly:

\[
\kappa_c=\sup_a\nu(a)=\lim_{a\to\infty}\nu(a).
\]

A finite negative sector cannot drift to infinity unseen.

PL-282 supplies the reusable fixed-support certification mechanism. At each fixed aperture `a`, finite Gauss--Stieltjes lower operators `L_(a,m)` increase spectrally to the exact localized operator and

\[
L_a>0\quad\Longleftrightarrow\quad\exists m<\infty:\ L_{a,m}>0.
\]

Thus **strict positivity at any prescribed finite support has a terminating finite certificate mechanism**. This does not give a uniform certificate depth, margin, or theorem as `a->infinity`, and it does not decide an exact zero ground state.

PL-283 sharpens the concrete finite-aperture boundary using a different 2026 computer-assisted preprint. That source reports, for every complex `f` supported in `[-0.8,0.8]`,

\[
Q_W(f)\ge8.9\times10^{-18}\|f\|_2^2.
\]

The common-form and test-space bridge already audited in PL-265/PL-269 puts Suzuki's `H_0^1(-0.8,0.8)` core inside that supported class. A uniform lower form bound survives Friedrichs closure, so the transfer itself is exact:

\[
A_{0.8}\ge8.9\times10^{-18}I>0.
\]

Mathia has not independently reproduced the external interval-arithmetic certificate, so the numerical margin remains a non-peer-reviewed literature claim. Conditional on its correctness, PL-280 gives strict positivity for every `0<a<=0.8`. The active prime-power channels at `0.8` are exactly `2,3,4`; the next activation occurs at `log(5)/2\approx0.804719`. Therefore the certificate rules out a first crossing through almost the entire source-static interval before the `5` channel enters, but it does **not** justify extending positivity to that threshold because the domain and archimedean part continue to vary between source events.

The source-specific RH problem is therefore narrower than “can finite windows be certified?” The answer is yes in principle for every fixed strictly positive window, and a reported certificate now reaches `a=0.8`. The live theorem is **uniform first-crossing prevention as the von-Mangoldt comb grows**: find an arithmetic inequality, source stratification, or Schur mechanism whose positive margin survives increasing aperture, rather than merely improve finite-window diagonalization.

**Boundary.** The `a=0.8` numerical margin is not independently reproduced and is too small for ordinary floating-point evidence. The Stieltjes hierarchy is fixed-support, not aperture-uniform. The transfer to Suzuki's operator uses only restriction to the audited core and form closure; it does not reproduce the external certificate. None of these results identifies `\kappa_c` with an off-critical zero count or proves Weil positivity globally.