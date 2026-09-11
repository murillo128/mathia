# PL-277 — Canonical noncompact completion universally collapses the finite-source infinite Morse defect to finite negative index

**Evidence:** `LITERATURE+DERIVED`

**Status:** `PROVED-STRUCTURAL + MATCHED-CONTROL-NEGATIVE + MORSE-INDEX-SEPARATION + PRIOR-ART-SYNTHESIS`

## Claim

`PL-276` leaves one standard completion channel alive at fixed aperture: the finite positive von-Mangoldt source remains indefinite after every compact correction, so any eventual high-frequency repair must use the noncompact archimedean/scalar part of the completed Weil form. That surviving channel can now be classified more sharply.

At every fixed localization radius `a>0`, the uncompleted finite source block has **infinite positive and infinite negative Morse index** after any fixed compact self-adjoint correction. In contrast, Suzuki's canonical completed localized Weil operator `A_a` is self-adjoint, lower bounded, and has discrete spectrum with `+infinity` as its only accumulation point. Hence it has only **finitely many negative eigenvalues**.

More importantly, this collapse from an infinite high-frequency sign defect to finite negative index is **not specific to the rational-prime weights**. The finite prime-power source is a bounded self-adjoint perturbation on `L^2(-a,a)`. Removing it (and, if desired, the finite-rank pole term) from `A_a` leaves a lower-bounded self-adjoint operator with compact resolvent. Adding back **any other finite signed atomic source** is again a bounded self-adjoint perturbation, so the resulting operator still has compact resolvent and only finitely many negative eigenvalues.

Thus the canonical noncompact completion supplies the operator category that `PL-276` proved compact completion cannot supply, but it does so generically:

\[
\boxed{
\text{finite source + compact correction}
\;\Longrightarrow\;
\text{infinite two-sided Morse defect},
}
\]

whereas

\[
\boxed{
\text{canonical noncompact completion + any finite source}
\;\Longrightarrow\;
\text{finite negative index and eventual positive spectrum}.
}
\]

The RH-sensitive content therefore cannot be the mere disappearance of high-frequency negative directions. It is pushed into the **finite low/mesoscopic spectral sector**: whether the remaining negative index is actually zero for the rational-prime source at every aperture, and how that finite sector evolves as new prime powers enter. This is a matched-control negative result, not an RH theorem.

## 1. Every finite localized source defines a bounded operator

Fix `a>0` and extend `v in L^2(-a,a)` by zero to the real line. A prime-power term in the localized explicit formula evaluates the autocorrelation at a fixed shift `h` with `|h|<2a`:

\[
C_h(v)
=\int_{\mathbb R}v(x)\overline{v(x-h)}\,dx.
\]

If `R_h` denotes zero-extended translation followed by restriction to `(-a,a)`, then

\[
C_h(v)=\langle v,R_hv\rangle,
\qquad
\|R_h\|\le1.
\]

The real-even Weil contribution uses the symmetric combination of the shifts `h` and `-h`. Therefore a finite signed atomic source

\[
\mu=\sum_{j=1}^r b_j\delta_{h_j},
\qquad |h_j|<2a,
\]

produces a bounded self-adjoint operator `B_mu` satisfying, under the standard symmetric normalization,

\[
\|B_\mu\|\le 2\sum_{j=1}^r|b_j|.
\]

The precise factor of two depends only on whether the `+h` and `-h` contributions are stored separately; boundedness does not. In the actual zeta source the set is finite because compact support permits only prime powers `q=p^m` with `log q<2a`, and the coefficients are `Lambda(q)/sqrt(q)` up to the conventional overall sign.

This supplies an ambient-operator realization for the fixed-source forms used in `PL-273`--`PL-276`: Groskin's finite source matrices are the Galerkin compressions of a bounded finite sum of truncated translation/reflection operators. No convergence of an infinite prime sum is involved at fixed aperture.

The pole term is also bounded and finite rank. `PL-059` writes it through the two bounded Laplace functionals on the finite interval,

\[
Q_{\rm pole}(v)
=2\Re\bigl(V_{1/2}(v)\overline{V_{-1/2}(v)}\bigr),
\qquad
V_s(v)=\int_{-a}^a v(x)e^{sx}\,dx.
\]

Hence all non-archimedean finite-source and pole changes at fixed aperture are bounded perturbations of the noncompact completed operator.

## 2. The PL-276 witnesses force infinite positive and negative index

Let `mu` be a nonzero finite positive atomic source supported strictly inside the normalized source window, and let `K` be any fixed compact self-adjoint correction. `PL-276` proves that there are orthonormal Fourier modes `T_k` in two infinite sets, in fact sets of positive lower density, and constants `eta_+,eta_->0` such that for all sufficiently large witness indices

\[
\langle T_k,(B_\mu+K)T_k\rangle\ge\eta_+
\]

on one set and

\[
\langle T_k,(B_\mu+K)T_k\rangle\le-\eta_-
\]

on the other. The same statement holds after reversing the source sign, so it applies to the conventional sign of the prime contribution as well.

These uniform diagonal witnesses imply more than eventual indefiniteness. Suppose the negative spectral subspace of the bounded self-adjoint operator

\[
B:=B_\mu+K
\]

were finite dimensional. Its negative part

\[
B_-:=(-B)\mathbf1_{(-\infty,0)}(B)
\]

would then be positive finite rank and hence trace class. For any orthonormal collection of negative witnesses `e_j`,

\[
\langle e_j,Be_j\rangle
\ge-\langle e_j,B_-e_j\rangle.
\]

Summing the first `M` witnesses gives

\[
-\eta_-M
\ge
\sum_{j=1}^M\langle e_j,Be_j\rangle
\ge
-\sum_{j=1}^M\langle e_j,B_-e_j\rangle
\ge-\operatorname{Tr}(B_-),
\]

which is impossible for large `M`. Thus the negative spectral subspace is infinite dimensional. Applying the same argument to `-B` and the positive witnesses proves that the positive spectral subspace is also infinite dimensional.

Consequently the fixed finite source plus every compact correction has

\[
\boxed{
\operatorname{ind}_-(B_\mu+K)=
\operatorname{ind}_+(B_\mu+K)=\infty.
}
\]

This is the spectral-strengthening of the compression statement in `PL-276`: the recurrent sign defect is not merely that arbitrarily large Galerkin matrices remain indefinite; it represents an infinite-dimensional two-sided spectral defect of the bounded source operator itself.

## 3. The completed localized Weil operator has finite negative index

Suzuki's 2026 screw-function formulation records the Connes--Consani--Moscovici theorem that, for every fixed `a>0`, the closed localized completed Weil form has a canonical self-adjoint representative `A_a` whose spectrum is bounded below and discrete, with `+infinity` as its only accumulation point. Equivalently, `A_a` has compact resolvent. Therefore

\[
\boxed{\operatorname{ind}_-(A_a)<\infty.}
\]

No RH assumption enters this statement. If RH fails, the finite negative index may be nonzero; `PL-266` and `PL-269` isolate the corresponding ground-state crossing. The present point is only that the completed operator cannot retain the infinite high-frequency negative sector proved above for the finite source plus compact corrections.

Define `B_arith,a` to be the bounded finite prime-power source operator at aperture `a`, with whichever sign convention is used in `A_a`, and let `K_pole,a` denote the finite-rank pole operator. Then

\[
A_{\rm ns,a}:=A_a-B_{\rm arith,a}-K_{\rm pole,a}
\]

is self-adjoint on `Dom(A_a)` and lower bounded. It also has compact resolvent. Indeed, compact resolvent is stable under bounded self-adjoint perturbations: for a nonreal `z` with sufficiently large imaginary part, the resolvent identity writes the perturbed resolvent as a compact resolvent times a bounded inverse.

The symbol `A_ns,a` is only a bookkeeping name for the **non-source/noncompact completed sector** under the standard explicit-formula decomposition. Depending on normalization, bounded scalar terms may be grouped with it or moved across the decomposition; that choice cannot affect the compact-resolvent conclusion. No claim is made here that the gamma/archimedean term alone is positive.

## 4. Matched-source replacement shows that high-frequency repair is universal

Now replace the rational-prime source at the same aperture by an arbitrary finite signed atomic source `mu`. Its operator `B_mu` is bounded by Section 1. For any fixed bounded finite-rank or compact correction `K_0`, consider

\[
A_{\mu,a}=A_{\rm ns,a}+B_\mu+K_0.
\]

This is again a bounded self-adjoint perturbation of an operator with compact resolvent. Therefore `A_{mu,a}` is lower bounded with compact resolvent and has only finitely many negative eigenvalues. If

\[
\alpha_1\le\alpha_2\le\cdots\to+\infty
\]

are the eigenvalues of `A_ns,a`, counted with multiplicity, then the min--max principle gives the simple tail estimate

\[
\lambda_n(A_{\mu,a})
\ge
\alpha_n-\|B_\mu+K_0\|.
\]

Hence every fixed finite source, however its locations and signed weights are chosen, has an eventually positive spectral tail after the same noncompact completion.

This is the decisive matched control. `PL-276` correctly identified the noncompact completion channel as the only standard operator category capable of repairing the recurrent high-frequency sign ledger. The present result shows that **the repair itself is generic**. It uses the coercive/discrete spectral category of the completed finite-interval operator, not the special rational-prime geometry, the von-Mangoldt weights, or the exponent-ray relations `q=p^m`.

What can still be arithmetic is the finite residual index

\[
\operatorname{ind}_-(A_{\mu,a})
\]

and, in particular, whether it vanishes for the actual zeta source at every aperture. For the rational-prime source, global vanishing of that residual index is just the localized Weil positivity problem. The matched control therefore moves the target rather than solving it.

## 5. Relation to the current prime-lattice frontier

The fixed-aperture sign hierarchy is now sharper.

`PL-273` shows that every individual active prime-power atom is eventually indefinite. `PL-275` shows that every finite positive aggregate is eventually indefinite. `PL-276` shows that both signs recur with positive density and survive every compact correction. The present finding upgrades that last statement to an infinite-Morse-index obstruction, then compares it with the canonical completed operator:

\[
\text{finite rational-prime source + compact completion}
\quad\Rightarrow\quad
\text{infinite positive and negative index},
\]

while

\[
\text{full noncompact completed form}
\quad\Rightarrow\quad
\text{finite negative index}.
\]

But because the second implication survives arbitrary finite source replacement, it cannot by itself select the rational primes. The RH-facing information is therefore necessarily **low/mesoscopic or cross-aperture**, not the eventual spectral tail. This dovetails with `PL-269`: the ground energy `lambda_a`, and whether it stays nonnegative while tending to zero as `a` grows, is an exact RH order parameter. The noncompact sector guarantees that only finitely many modes can threaten positivity at each fixed `a`; it does not tell us why none of those modes should be negative for the zeta source.

In exponent-lattice language, compact localization sees only finitely many axis points

\[
me_p,\qquad m\log p<2a.
\]

Replacing those points and their weights arbitrarily changes the bounded source operator but does not change the eventual completed spectral tail. Thus any mechanism that distinguishes the rational-prime norm map must act through the finite residual spectral sector or through its coherent evolution as the log-energy cutoff crosses the thresholds `m log p/2`.

## 6. Prior-art and novelty audit

All load-bearing literature is already anchored in `research/prime_lattice/SOURCES.md`.

- Source 93, Akiva Groskin, **“A finite Guinand--Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3, supplies the exact finite source calculus behind `PL-270`--`PL-276` and independently shows that the omitted archimedean tail has a positive Cauchy--Stieltjes structure beyond a finite Galerkin band.
- Source 56, Masatoshi Suzuki, **“Weil's quadratic form via the screw function,”** arXiv:2606.09096v2, records that the canonical localized self-adjoint operator `A_a` is lower bounded with discrete spectrum and `+infinity` as the only accumulation point, referring to the Connes--Consani--Moscovici theorem.
- Source 26, Enrico Bombieri, **“Remarks on Weil's quadratic functional in the theory of prime numbers, I,”** already studies negative eigenvalues of finite Weil truncations and, under the hypothesis that only finitely many nontrivial zeros lie off the critical line, relates the eventual negative-eigenvalue count to those off-line zeros. Negative-index analysis of the completed Weil form is therefore strong prior art, not a new Mathia paradigm.

The functional-analysis ingredients used here are standard: finite sums of truncated translations are bounded; bounded self-adjoint perturbations preserve compact resolvent; the min--max principle controls eigenvalue shifts; and a bounded self-adjoint operator with uniform negative expectations on infinitely many orthonormal vectors cannot have a finite-dimensional negative spectral subspace.

A targeted literature audit around localized Weil operators, negative index, compact-resolvent completion, and finite Guinand--Weil source truncations found the ingredients above but not the exact **matched-control comparison** distilled here: `PL-276`'s recurrent infinite source defect versus the universal finite-index repair after canonical noncompact completion under arbitrary finite source replacement. No publication-level novelty is claimed. The durable project delta is the route restriction: high-frequency sign repair is now proved to be too universal to carry RH-specific arithmetic rigidity.

No new `SOURCES.md` entry is required because every cited theorem source was already registered by the findings on which this result depends.

## 7. Boundaries and adversarial checks

Several restrictions are essential.

First, the infinite-Morse-index statement uses the positive finite interior-source hypothesis of `PL-276` (or its overall sign reversal). It is not asserted for an arbitrary signed source, which can exhibit cancellations. The matched-control compact-resolvent statement, however, does allow arbitrary finite signed sources because only boundedness is needed.

Second, compact-resolvent completion does **not** imply positivity. It proves only that the negative index is finite. One negative low mode is enough to violate localized Weil positivity, and failure of RH supplies such a mode at some finite aperture.

Third, the result is fixed-aperture. As `a` grows, the number and norm of the active prime-power source terms grow, and no uniform bound on the residual negative index is obtained. The theorem therefore does not replace the cross-aperture problem isolated in `PL-266`--`PL-269`.

Fourth, no Euler product is continued into the critical strip. The decomposition is taken from the already-completed Weil explicit-formula form. Compact support makes the prime-power sum finite, and Suzuki's operator is constructed from the completed localized form.

Finally, the finding would be materially falsified if the fixed-aperture source contribution failed to extend to a bounded self-adjoint operator, if `PL-276`'s uniform two-sided orthonormal witnesses were invalid, or if the canonical localized operator did not have discrete lower-bounded spectrum with `+infinity` as its only accumulation point. The first is the elementary Cauchy--Schwarz estimate above; the second is proved in the preceding canonical finding; the third is the cited Suzuki/Connes--Consani--Moscovici theorem.

## Consequence for the research line

The live question after `PL-276` should no longer be phrased as whether the archimedean/noncompact completion can suppress the finite-source high-frequency indefiniteness. **It necessarily does so at the level of Morse index, and it does so for arbitrary finite sources.**

The surviving RH target is narrower: identify a rational-prime-specific law that forces the finite residual negative index to be zero, or controls its cross-aperture evolution strongly enough to force `lambda_a>=0` for every `a`. Candidate mechanisms must therefore act in the low/mesoscopic completed sector or couple different prime-power activation thresholds; generic coercive high-frequency completion is already accounted for and is not arithmetic evidence.
