# PL-278 — Canonical noncompact completion collapses the active finite-source Morse defect to finite negative index

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-STRUCTURAL + MATCHED-CONTROL-NEGATIVE + MORSE-INDEX-SEPARATION + PRIOR-ART-SYNTHESIS`

## Claim

Fix a localization radius `a>0`. There are two distinct statements, with different hypotheses, that must not be conflated.

First, if the localized source contains a **nonzero finite positive atomic measure supported strictly inside the source window** (or its overall sign reversal), then the associated bounded source operator plus any fixed compact self-adjoint correction has infinite positive and infinite negative Morse index. For the rational-prime source in the normalization `log q<2a`, this source-side statement applies only once at least one prime-power atom is active; equivalently, only for

\[
a>\frac{\log 2}{2}.
\]

For `0<a<=log(2)/2` there is no active prime-power atom, so there is no finite-source two-sided Morse defect to repair.

Second, Suzuki's canonical completed localized Weil operator `A_a` is self-adjoint, lower bounded, and has compact resolvent for every `a>0`. Hence it has only finitely many negative eigenvalues. Removing its bounded finite prime-power source and finite-rank pole term preserves compact resolvent, and adding back **any** finite signed atomic source is again only a bounded self-adjoint perturbation. Therefore the completed operator retains finite negative index and an eventually positive spectral tail under arbitrary finite source replacement.

Thus, whenever the positive finite source is active, the canonical noncompact completion changes the operator category from an infinite two-sided source defect to a finite residual negative sector. But that high-frequency repair is generic rather than rational-prime-specific. The RH-sensitive information can only lie in the finite low/mesoscopic sector and in its coherent evolution as the aperture crosses prime-power thresholds, not in eventual spectral positivity alone.

## 1. Finite localized sources are bounded operators

Fix `a>0` and extend `v in L^2(-a,a)` by zero to the real line. A source atom at shift `h`, with `|h|<2a`, evaluates the autocorrelation

\[
C_h(v)=\int_{\mathbb R}v(x)\overline{v(x-h)}\,dx.
\]

If `R_h` denotes zero-extended translation followed by restriction to `(-a,a)`, then

\[
C_h(v)=\langle v,R_hv\rangle,
\qquad \|R_h\|\le1.
\]

The real-even Weil contribution uses the symmetric combination of `h` and `-h`. Hence a finite signed atomic source

\[
\mu=\sum_{j=1}^r b_j\delta_{h_j}
\]

produces a bounded self-adjoint operator `B_mu`; under the standard symmetric normalization one may take

\[
\|B_\mu\|\le 2\sum_{j=1}^r|b_j|.
\]

At fixed aperture the rational-prime source is finite because only prime powers `q=p^m` satisfying `log q<2a` contribute, with coefficient `Lambda(q)/sqrt(q)` up to the conventional overall sign. In particular, no prime-power term is active when `0<a<=log(2)/2`.

The pole term is also bounded and finite rank. As in `PL-059`, it factors through finitely many bounded Laplace functionals on the finite interval. Therefore all fixed-aperture source and pole changes are bounded perturbations of the noncompact completed operator.

## 2. An active positive interior source has infinite two-sided Morse index after compact correction

Let

\[
\mu=\sum_{j=1}^r a_j\delta_{\omega_j},
\qquad a_j>0,\quad 0<\omega_j<1,
\]

be nonzero, and let `K` be any fixed compact self-adjoint operator on the ambient even Fourier Hilbert space. `PL-276` proves that there are two infinite sets of orthonormal Fourier modes, in fact of positive lower density, and constants `eta_+,eta_->0` such that along one set

\[
\langle T_k,(B_\mu+K)T_k\rangle\ge\eta_+,
\]

while along the other

\[
\langle T_k,(B_\mu+K)T_k\rangle\le-\eta_-.
\]

The same statement holds after reversing the overall sign of the source.

Set `B=B_mu+K`. If the negative spectral subspace of the bounded self-adjoint operator `B` were finite dimensional, then

\[
B_-:=(-B)\mathbf1_{(-\infty,0)}(B)
\]

would be positive finite rank and therefore trace class. For each negative witness `e_j`,

\[
\eta_-\le -\langle e_j,Be_j\rangle\le \langle e_j,B_-e_j\rangle.
\]

Summing over `M` orthonormal witnesses gives

\[
M\eta_-\le \sum_{j=1}^M\langle e_j,B_-e_j\rangle\le \operatorname{Tr}(B_-),
\]

which is impossible for arbitrarily large `M`. Thus the negative spectral subspace is infinite dimensional. Applying the same argument to `-B` and the positive witnesses proves that the positive spectral subspace is also infinite dimensional:

\[
\boxed{
\operatorname{ind}_-(B_\mu+K)=
\operatorname{ind}_+(B_\mu+K)=\infty.
}
\]

This conclusion requires the nonzero positive interior-source hypothesis of `PL-276` (or its overall sign reversal). It is not a statement about an empty source and is not asserted for an arbitrary signed source, where cancellations may occur.

For the actual zeta source, the smallest possible active prime power is `q=2`. Therefore the source-side infinite-Morse conclusion begins only after the strict threshold `log 2<2a`. Before that threshold the source operator is zero, so for example `K=0` has neither an infinite positive nor an infinite negative source defect.

## 3. The completed localized operator has finite negative index for every aperture

Suzuki's 2026 screw-function formulation records the Connes--Consani--Moscovici theorem that, for every fixed `a>0`, the closed localized completed Weil form has a canonical self-adjoint representative `A_a` whose spectrum is bounded below and discrete, with `+infinity` as its only accumulation point. Equivalently, `A_a` has compact resolvent. Consequently

\[
\boxed{\operatorname{ind}_-(A_a)<\infty.}
\]

No RH assumption enters this operator-category statement. Compact resolvent does not imply positivity; it only says that possible negative spectrum is confined to finitely many eigenvalues at each fixed aperture.

Let `B_arith,a` denote the bounded finite prime-power source operator at aperture `a`, with the sign convention used in `A_a`, and let `K_pole,a` denote the finite-rank pole operator. Define

\[
A_{\rm ns,a}=A_a-B_{\rm arith,a}-K_{\rm pole,a}.
\]

Because bounded self-adjoint perturbations preserve self-adjointness, lower boundedness, and compact resolvent, `A_ns,a` has the same operator category. The notation is bookkeeping for the non-source completed sector; it does not assert that the archimedean term by itself is positive.

## 4. Arbitrary finite source replacement preserves the completed spectral tail

Now replace the rational-prime source at the same aperture by an arbitrary finite signed atomic source `nu`. Its operator `B_nu` is bounded by Section 1. For any fixed bounded finite-rank or compact correction `K_0`, set

\[
A_{\nu,a}=A_{\rm ns,a}+B_\nu+K_0.
\]

This is again a bounded self-adjoint perturbation of a lower-bounded compact-resolvent operator, so it has compact resolvent and only finitely many negative eigenvalues. If

\[
\alpha_1\le\alpha_2\le\cdots\to+\infty
\]

are the eigenvalues of `A_ns,a`, counted with multiplicity, the min--max principle gives

\[
\lambda_n(A_{\nu,a})
\ge
\alpha_n-\|B_\nu+K_0\|.
\]

Hence every fixed finite source has an eventually positive spectral tail after the same noncompact completion.

This is the matched control. Once a nonzero positive source is active, `PL-276` gives an infinite two-sided defect for source plus compact correction; the canonical noncompact completed category reduces any finite-source replacement to a finite negative sector. The reduction therefore cannot by itself encode the special rational-prime norm map, the von-Mangoldt weights, or the exponent-ray relation `q=p^m`.

## 5. Consequence for the prime-lattice frontier

The fixed-aperture hierarchy has three regimes that must be kept separate.

Before the first prime-power threshold, the arithmetic source is empty and there is no source-side Morse defect. Once at least one positive interior prime-power atom is active, the finite source plus every fixed compact correction has infinite positive and negative index. After canonical noncompact completion, every finite source replacement has only a finite negative sector.

Therefore the RH-facing question is not whether the archimedean/noncompact completion can suppress high-frequency source indefiniteness. Whenever such a source defect exists, the completed compact-resolvent category suppresses it generically. The remaining arithmetic question is whether the finite residual negative index of the **actual** zeta source vanishes at every aperture, and how that finite sector changes when the log-energy boundary crosses the thresholds

\[
2a=m\log p.
\]

In exponent-lattice language, compact localization sees finitely many axis points `m e_p` with `m log p<2a`. Replacing those points and weights arbitrarily does not destroy the eventual completed positive tail. Any mechanism that distinguishes the rational primes must therefore act in the residual low/mesoscopic sector or through its coherent cross-aperture threshold evolution.

## 6. Prior-art and novelty audit

All load-bearing literature is already registered in `research/prime_lattice/SOURCES.md`.

Akiva Groskin, *A finite Guinand--Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828v3, supplies the exact finite-source calculus used by `PL-270`--`PL-276`. Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v2, records the lower-bounded discrete-spectrum/compact-resolvent theorem for the canonical localized completed operator, referring to Connes--Consani--Moscovici. Enrico Bombieri's *Remarks on Weil's quadratic functional in the theory of prime numbers, I* is prior art for negative-eigenvalue analysis of finite Weil truncations.

The functional-analysis ingredients are standard: finite sums of truncated translations are bounded; bounded self-adjoint perturbations preserve compact resolvent; the min--max principle controls eigenvalue shifts; and uniform sign expectations on infinitely many orthonormal vectors rule out finite-dimensional spectral subspaces of the corresponding sign.

The durable project delta is the matched-control separation, with the source-activation hypothesis made explicit: **active positive finite source plus compact correction has an infinite two-sided Morse defect, whereas canonical noncompact completion plus any finite source has only finite negative index.** No publication-level novelty is claimed, and no new `SOURCES.md` entry is required.

## 7. Boundaries and falsification

The infinite-Morse statement requires a nonzero finite positive interior atomic source or its overall sign reversal. The arbitrary finite signed-source statement applies only to the compact-resolvent matched replacement, where boundedness is sufficient. The result is fixed-aperture; no uniform bound on the residual negative index as `a` grows is obtained.

Compact resolvent does not prove Weil positivity. One low negative eigenvalue is enough to fail positivity, and the present argument does not control that residual sector. No Euler product is continued into the critical strip: the decomposition is taken from the completed Weil explicit-formula form, and compact support makes the prime-power source finite.

The claim would be falsified if `PL-276`'s positive-density two-sided witnesses failed for an active positive interior source, if a finite localized source did not define a bounded self-adjoint operator, or if the canonical localized completed operator failed to have lower-bounded compact-resolvent spectrum. The first is the preceding canonical result, the second is the truncated-shift estimate above, and the third is the cited Suzuki/Connes--Consani--Moscovici theorem.
