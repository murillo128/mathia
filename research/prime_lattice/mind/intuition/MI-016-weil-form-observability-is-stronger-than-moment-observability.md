# MI-016 — Completed Weil order is a one-sided index ledger; fixed windows can be finitely certified and spectrally isolated

**Evidence level:** proved observability/order/exhaustion boundary through PL-282, plus PL-283--PL-284's transfer of a non-peer-reviewed computer-assisted spectral certificate at `a=0.8`; completed arithmetic positivity remains open.

The complete Galerkin/cutoff family can recover the source, but source recovery and cutoff coherence are generic information properties rather than sign principles. PL-272--PL-276 show that every nonzero finite positive interior source is eventually sign-indefinite and no fixed compact self-adjoint correction repairs that high-frequency Morse defect.

PL-278 identifies what canonical noncompact completion buys: the localized completed Weil operator has compact resolvent and only finitely many negative eigenvalues, with eventual positivity of the high spectral tail. PL-279 shows newly active prime-power shifts turn on quadratically softly, so a first crossing cannot be attributed to a discontinuous threshold shock.

PL-280 gives the order law. Because localized form domains are nested under aperture growth,

\[
\lambda_k(b)\le\lambda_k(a)\qquad(a<b),
\]

and the negative Morse index is nondecreasing. PL-281 shows that this ledger exhausts the global compact-support negative index exactly. A finite negative sector cannot drift to infinity unseen.

PL-282 supplies the fixed-support certification mechanism: strict positivity at any prescribed finite aperture is equivalent to positivity of some finite Gauss--Stieltjes lower certificate. This gives termination at fixed support, but no uniform certificate depth or margin as the aperture grows.

PL-283--PL-284 sharpen one concrete window. Conditional on the correctness of the external computer-assisted proof, Suzuki's canonical operator at `a=0.8` satisfies

\[
8.9\times10^{-18}
\le\lambda_1(A_{0.8})
\le2.523\times10^{-16},
\]

has a simple even ground state, and obeys

\[
\lambda_2(A_{0.8})\ge8.206\times10^{-15},
\qquad
\lambda_2-\lambda_1\ge7.9537\times10^{-15}.
\]

So the certified endpoint is locally nondegenerate as well as positive. This matters because a perturbative continuation argument can start from an isolated eigenbranch rather than a potentially multiple threshold state. The numerical isolation, however, remains literature-level until its interval-arithmetic certificate is independently reproduced.

The central distinction is now **fixed-window spectral isolation versus aperture-uniform coercivity**. A positive gap at one aperture does not persist automatically under nested-domain enlargement; monotonicity moves ordered eigenvalues downward but supplies no lower bound on their separation or on the ground-state derivative. The next source event at `log(5)/2` is close to `0.8`, yet even on the source-static interval the archimedean/domain contribution continues to vary.

The live target is therefore not another proof that a finite window can be checked. It is a source-specific transport inequality—differential, variational, Schur, or otherwise—that propagates positivity or controls the first eigenbranch as the von-Mangoldt comb and support aperture grow.

**Boundary.** The `a=0.8` bounds depend on a recent non-peer-reviewed computer-assisted certificate not independently reproduced by Mathia. The fixed-support hierarchy and endpoint gap are not aperture-uniform. None identifies the global negative index with off-critical zero count or proves Weil positivity globally.
