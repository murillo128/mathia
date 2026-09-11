# MI-016 — Finite-radius source localization can replace zero-side tightness

**Evidence level:** supported

## Core intuition

Bombieri's finite negative matrices are not the only exact way a hypothetical off-line zero can become finitely visible. Localized Weil theory moves the obstruction to the source side: RH failure forces a first finite support radius where a self-adjoint localized Weil operator acquires a zero mode, and the kernel at that radius depends on only finitely many von Mangoldt coefficients plus explicit archimedean data.

The passage from finite zero-side inertia to an infinite limiting eigenvector is therefore one route, not a logically necessary route. A second target is finite-radius source nondegeneracy.

## Strongest justified claim

WI-236 shows that Bombieri finite truncations detect every finite off-line packet with exact negative inertia, but a cofinal negative eigensequence may collapse toward zero and lose height tightness. WI-237 shows that generic interval-exponential separation cannot fix this: simple critical-line exponentials are complete on every bounded positive-measure window and are not Bessel, so an off-line packet can be approximated arbitrarily well in `L^2` without any useful unweighted frame geometry. What remains there is an eigenvector-specific coefficient-budget theorem.

WI-238 records Suzuki's independent localized criterion. For every support radius `a`, the localized Weil form is represented by a lower-bounded self-adjoint operator with discrete spectrum. The ground-state value `lambda_a` is continuous; nested support gives the exact monotonicity `lambda_b<=lambda_a` for `b>a`. If RH is false, `lambda_a` is positive for small radius and negative at some finite radius, so there is a first `a_*` with `lambda_{a_*}=0` and a nonzero ground-state zero mode.

The explicit screw-function kernel at radius `a` uses the von Mangoldt sum only for `n<=exp(2a)`. Hence

`not RH => finite a_* => finite-prime localized Weil operator has a nonzero zero mode`.

This conclusion does not require a limiting zero-ordinate relation or a uniform negative margin in Bombieri's cofinal matrices.

## Synthesis of evidence

The two routes expose different quantitative currencies. Bombieri starts from the zero divisor and needs coefficient cost/tightness to prevent a finite negative sector from dissolving. Suzuki starts from a compact source window and turns failure into a first ground-state crossing. The latter is finite in arithmetic input but still infinite-dimensional analytically.

This creates a cleaner source-side research question: can the first crossing be excluded by a structural property of the finite-prime kernel that is not merely a restatement of the full Weil criterion? Any proposed answer must use the nested-radius or source-locality structure; otherwise the RH-equivalent nondegeneracy theorem has only been renamed.

## Counterevidence / boundary cases

Suzuki's all-radius nondegeneracy is already equivalent to RH. Finite-prime locality does not imply a finite-dimensional problem, and no unconditional lower bound for `lambda_a` at arbitrary radius is supplied. The first-crossing viewpoint is a localization of the burden, not a solution.

WI-237's coefficient-budget route remains valid and may still be more tractable in some formulations. The two approaches should not be claimed equivalent without an explicit bridge.

## Epistemic status

**Supported structural redirect:** RH failure has an exact finite-radius source-side zero-mode consequence, so zero-side coefficient tightness is not a logically mandatory bridge; the alternative burden is to exploit finite-prime localized nondegeneracy or first-crossing structure.

## Novelty/prior-art status

The localized nondegeneracy theorem and operator formulation are Suzuki/Yoshida prior art as recorded in WI-238. The Mathia synthesis is the comparison with the WI-236/WI-237 passage-to-limit obstruction and the explicit finite-prime interpretation.

## Falsification criterion

Show that WI-238's finite-prime locality fails for the localized operator because the construction requires source values outside `n<=exp(2a)`, or that the claimed monotone first crossing does not follow from support nesting and continuity. More strategically, prove that excluding the finite-radius zero mode necessarily reconstructs the same Bombieri coefficient-tightness statement; that would collapse the two routes back into one.
