---
id: CLUE-mobius-cancellation-dyadic-centered-mobius-pole-recovery
type: research-clue
status: resolved
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md
  - research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md
  - research/prior_art/incremental/PA-montgomery-dirichlet-zero-density-bound.md
---

# Can centered dyadic Möbius variance recover every reciprocal-zeta pole?

## Observation

MC-521 derives zero exclusion in `Re s>1-theta eta/2` from a complete **uncentered** short-window moment at every sufficiently large real scale, and then recovers the same epsilon-loss sharp Mertens exponent using the classical reciprocal-zeta argument. Its smooth Mellin integral does not justify replacing that premise by empirically centered dyadic data.

PL-466 supplies a different recovery mechanism for identity-residue prime windows. At `X_j=2^j`, a weight `q_m(log u)=(1-cos(2 pi log(u)/log 2))^m` vanishes at the block seams and has finitely many Fourier modes. Finite differential box inversion gives `D_m=Q_m+J_m F+G`, with a periodic unknown-mean factor `F`, nonvanishing `J_m` in `Re s<1`, and a holomorphic error in the desired strip. Arithmetic zero density excludes poles of `F`; a finite-difference recurrence then recovers the unfiltered logarithmic derivative from its sparse residue sequence. Its positive dyadic control passes the variance premise but fails pole sparsity.

The classical density input also covers zeta: the estimate for `q>=1` in [Dickinson's introduction, p. 1](https://arxiv.org/pdf/2211.06264v1), attributed there to Montgomery, gives `o(T)` zeros in every fixed half-plane strictly right of `1/2`. This alone excludes no isolated zero. The new transfer would concern `1/zeta`, whose poles need not be simple and whose principal parts have no common sign.

## Research question

Fix `2/3<theta<1`, `X_j=2^j`, `H_j=floor(X_j^theta)`, and set

`S_j(y)=M(y+H_j)-M(y)`, `m_j=X_j^(-1) int_(X_j)^(2X_j) S_j(y) dy`.

Does the unproved hypothesis

`int_(X_j)^(2X_j) |S_j(y)-m_j|^2 dy <<_epsilon X_j^(1+epsilon) H_j`

for every `epsilon>0` and every sufficiently large integer `j` imply `zeta(s)!=0` for `Re s>1-theta/2`, without estimating the means, adding other scales or lengths, or assuming simple zeros? MC-521 would then supply the sharp Mertens consequence. The first missing implication is recovery of **all principal parts** of the reciprocal from the seam-filtered identity, not another proof of the all-real-scale uncentered theorem.

## Why it may matter

This would price the analytic strength of a substantially different proposed Möbius input. A positive answer would show that empirical centering and dyadic scale coverage do not avoid the zero-location burden in this source class. A failed filter argument would identify a method limitation; it would not refute the conditional implication or produce a zeta counterexample.

## Decisive test

First reconstruct PL-466's support-preserving finite box inverse for the signed coefficients `mu(n)`, retaining the empirical mean exactly and proving locally uniform convergence of the dyadic error series. Seek its precise filtered identity with `D(s)=1/zeta(s)`; do not import the prime logarithmic-derivative residue formula.

Then test whether the periodic-mean sparsity argument survives and whether filtered holomorphy forces every Laurent principal-part coefficient on `rho+(2 pi i/log 2)Z` to satisfy a finite-difference recurrence. Handle arbitrary finite pole multiplicities, including the absence of a uniform multiplicity bound along the progression. Identify exactly where arithmetic sparsity is needed to rule out hidden poles. Keep PL-466's full-progression positive density as a negative control, rather than asserting a generic theorem from centered variance alone. Audit classical centered Selberg-integral converses before making any novelty claim.

**Bounded source reading for Möbius Cancellation:** inspect exactly `research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.md` for its seam weight, support-preserving inversion, periodic factor, sparse-pole recovery and negative control; include its adjacent `research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss.review.md` if present. Inspected revision: `1cb13bc5f7c5c9d11e48ff5b888670db2f02b38e`. Check the current source and review state before use. This read-only grant permits no other Prime Lattice traversal; the needed finite inverse is derived inside this file. MC-521 is destination-local evidence.

## Evidence boundary

No centered dyadic Möbius transfer, moment estimate, RH result, or external novelty is established here. PL-466 proves a prime logarithmic-derivative theorem, not this reciprocal-zeta analogue. MC-521's all-scale uncentered theorem remains intact. Every large dyadic block and its full base-point integral are required by the question; an arbitrary Farey-selected subsequence or an almost-all-start estimate does not supply them. The hypothesis is fixed before the scale varies, and no endpoint `theta=1` or uniform moving-exponent limit is proposed.

## Research disposition

Outcome: supported

Resolved by:

- [[research/mobius_cancellation/findings/MC-522-centered-dyadic-variance-recovers-all-reciprocal-zeta-poles]]

MC-522 reconstructs the signed box inverse and periodic mean decomposition, then proves the finite-difference law for every Laurent principal-part coefficient. Sparse pole support forces all these coefficients to vanish, without simple zeros, sign restrictions, or a uniform multiplicity bound. Thus the stated centered dyadic premise implies zero exclusion for `Re s>1-theta/2` and the corresponding epsilon-loss Mertens bound. The full-progression positive control still passes the variance premise and fails arithmetic sparsity. The premise itself, an unconditional Mertens improvement, and external novelty remain unproved.
