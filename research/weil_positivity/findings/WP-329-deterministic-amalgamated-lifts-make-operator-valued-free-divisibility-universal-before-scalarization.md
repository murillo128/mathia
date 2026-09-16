---
id: WP-329
title: Deterministic amalgamated lifts make operator-valued free divisibility universal before scalarization
branch: weil_positivity
status: supported
kind: operator-valued-amalgamation-universality-obstruction
claim_strength: exact matched-control construction at every finite C*-cutoff and exact algebraic full-source lift showing that operator-valued free infinite divisibility can coexist with the freely indecomposable Mangoldt scalar law by storing all source specificity in the scalarization state
created: 2026-09-16
related: [WP-304, WP-325, WP-326, WP-327, WP-328]
prior_art:
  - Mihai Popa and Victor Vinnikov, Non-commutative functions and the non-commutative free Levy-Hincin formula, Advances in Mathematics 236 (2013), 131-157, DOI 10.1016/j.aim.2012.12.013, arXiv:1007.1932
---

# WP-329 — Deterministic amalgamated lifts make operator-valued free divisibility universal before scalarization

## Claim

`WP-328` leaves operator-valued free convolution genuinely open because composing an amalgamated conditional expectation with a scalar state does **not** in general send operator-valued free convolution to scalar free convolution. The scalar free-indecomposability obstruction from `WP-326` therefore cannot simply be pushed through an arbitrary scalarization map.

There is now an exact matched-control reason why that loophole must be treated very carefully. The exact pole-normalized Mangoldt law

\[
\nu_s
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-s}\,\delta_{\log n},
\qquad s>0,
\tag{1}
\]

admits operator-valued free infinitely divisible lifts for a completely universal reason, even though `WP-326` proves that `nu_s` itself has no nontrivial scalar free square root.

At every finite energy cutoff one can realize the exact truncated source as the scalarization of a **deterministic element of the amalgamation algebra**. Deterministic `B`-valued point masses are freely infinitely divisible over `B` because they divide by ordinary scalar multiplication inside the base algebra. The same construction works for arbitrary probability weights on the same support and, more generally, for every compactly supported scalar law.

Globally, the same mechanism is exact in algebraic operator-valued probability. Take the universal polynomial `*-`algebra

\[
B=\mathbb C[t],\qquad t=t^*,
\tag{2}
\]

put `A=B`, `E=id_B`, and scalarize by the positive state

\[
\tau_s(P)=\int_{\mathbb R}P(x)\,d\nu_s(x).
\tag{3}
\]

The `B`-valued law of `X=t` is the deterministic point law `delta_t`, and for every integer `m>=2`,

\[
\boxed{
\delta_t
=
\underbrace{\delta_{t/m}\boxplus_B\cdots\boxplus_B\delta_{t/m}}_{m\text{ times}}.
}
\tag{4}
\]

Meanwhile `tau_s` recovers the exact scalar moments of `nu_s`. The source has a positive exponential moment in a neighborhood of zero, so those moments determine `nu_s` uniquely. Thus the full arithmetic law is recovered exactly after scalarization.

The crucial point is that (4) contains **no arithmetic at all**. The `B`-valued distribution `delta_t` and all its higher operator-valued free cumulants are the same for every scalar law encoded by a state on `C[t]`: only the scalarization state changes. Consequently,

\[
\boxed{
\text{existence of an operator-valued freely infinitely divisible lift of }\nu_s
\text{ is not an arithmetic-selective positivity mechanism.}
}
\tag{5}
\]

This does not close genuinely operator-valued free geometry. It closes the weaker escape in which one merely observes that an enriched freely divisible object can scalarize to the exact source. A surviving operator-valued route must force essential arithmetic into **non-deterministic amalgamated coupling data** — for example higher `B`-valued cumulants, a completely positive covariance, a boundary response, or another mixed operator invariant — and its positive theorem must remain nonautomatic under matched scalarization controls. It must still generate the archimedean and global Weil terms in the same construction.

**Classification:** `DERIVED + EXACT-MATCHED-CONTROL + OPERATOR-VALUED-FREE + AMALGAMATION + DETERMINISTIC-LIFT + SCALARIZATION + UNIVERSALITY-OBSTRUCTION + SOURCE-SEMIGROUP + NOT-WEIL-POSITIVITY`.

## 1. The full Mangoldt source is moment-determinate

The algebraic construction below would be ambiguous if only a moment sequence were retained and that sequence admitted several representing measures. The present source has no such defect.

For any `epsilon` with

\[
0<\epsilon<s,
\tag{6}
\]

its positive exponential moment is

\[
\int e^{\epsilon x}\,d\nu_s(x)
=
\frac1{L(s)}
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-(s-\epsilon)}.
\tag{7}
\]

Since `Lambda(n)<=log n` and the prime powers form a subset of the positive integers,

\[
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}n^{-(s-\epsilon)}
\le
\sum_{n\ge2}
\frac{\log n}{n+1}n^{-(s-\epsilon)}
<\infty,
\tag{8}
\]

because `s-epsilon>0`. Hence the moment generating function exists on a nontrivial interval around zero on its positive side, and the standard exponential-moment criterion makes `nu_s` Hamburger moment-determinate. In particular the scalar moment functional in (3) identifies one exact probability law, not merely an indeterminate moment class.

The same estimate also shows that every polynomial moment of (1) is finite. No continuation of zeta, zero data, RH assumption, or asymptotic prime theorem enters.

## 2. Finite cutoffs already make C*-operator-valued divisibility nonselective

The strongest analytic version of the construction requires no unbounded operator if the source is cut off at finite log-energy.

Fix `R>log 2` and let

\[
\Sigma_R
=
\{\log n:n=p^k,\ \log n\le R\}.
\tag{9}
\]

This is finite. Let `nu_{s,R}` be the restriction of `nu_s` to `Sigma_R`, renormalized to total mass one. Set

\[
B_R=C(\Sigma_R),
\qquad
b_R(x)=x,
\tag{10}
\]

and define the state

\[
\tau_{s,R}(f)=\int_{\Sigma_R}f(x)\,d\nu_{s,R}(x).
\tag{11}
\]

Now take the `B_R`-valued probability space

\[
(A_R,E_R,B_R)=(B_R,\operatorname{id}_{B_R},B_R).
\tag{12}
\]

The self-adjoint element `b_R` is deterministic over the amalgamation algebra. Its `B_R`-valued distribution is the point law `delta_{b_R}`. For every integer `m>=2`, the element `b_R/m` is again in `B_R`, and the subalgebra generated by a deterministic base element has no nonzero centered part because `E_R|_{B_R}=id`. Thus amalgamated freeness of repeated deterministic copies is vacuous, and ordinary addition inside the common base gives

\[
\underbrace{\frac{b_R}{m}+\cdots+\frac{b_R}{m}}_{m\text{ times}}
=b_R.
\tag{13}
\]

Equivalently,

\[
\delta_{b_R}
=
\delta_{b_R/m}^{\boxplus_{B_R}m}.
\tag{14}
\]

So `delta_{b_R}` is freely infinitely divisible over `B_R` in the most elementary possible way.

Scalarization by `tau_{s,R}` recovers the exact finite source:

\[
\tau_{s,R}(f(b_R))
=
\int f(x)\,d\nu_{s,R}(x).
\tag{15}
\]

Nothing in (12)--(14) uses the Mangoldt masses. Keep the same finite set `Sigma_R`, the same algebra `B_R`, the same coordinate `b_R`, and the same `B_R`-valued law `delta_{b_R}`; replacing `tau_{s,R}` by **any** probability state on `C(Sigma_R)` changes the scalar weights arbitrarily while leaving operator-valued infinite divisibility untouched. The positive/divisible object upstairs therefore cannot distinguish Mangoldt weights from random positive weights on the exact same prime-power support.

The construction is even more general: for any compact set `K subset R` and any probability measure `mu` on `K`, the same choice `(C(K),id,C(K))` with the coordinate function gives a deterministic `C(K)`-valued freely infinitely divisible element whose scalar law under the integration state is exactly `mu`.

Thus every finite-cutoff certificate of the form “the source embeds into an operator-valued free infinitely divisible law” fails the README's matched-control requirement before any number theory is used.

## 3. The entire unbounded source has the same exact algebraic lift

The finite-cutoff argument could in principle leave open the possibility that passing to the unbounded full source forces a new arithmetic constraint. It does not at the purely algebraic level.

Use (2)--(3) and the algebraic `B`-valued probability space

\[
(A,E,B)=(B,\operatorname{id}_B,B).
\tag{16}
\]

For `X=t`, every mixed `B`-valued moment is just ordinary multiplication in `B`. In operator-valued free-cumulant language,

\[
\kappa_1^B(X)=t,
\qquad
\kappa_n^B(X,\ldots,X)=0
\quad(n\ge2),
\tag{17}
\]

because `X` is deterministic over the base algebra. Replacing `t` by `t/m` divides only the first cumulant by `m`, so addition of `m` amalgamated-free copies reproduces (4).

After composing with the scalar state,

\[
\varphi_s=\tau_s\circ E=\tau_s,
\tag{18}
\]

we obtain

\[
\varphi_s(X^j)
=\tau_s(t^j)
=\int x^j\,d\nu_s(x)
\qquad(j\ge0).
\tag{19}
\]

Section 1 makes this scalar moment sequence determinate, so (19) recovers exactly (1).

This is the precise mechanism by which operator-valued amalgamation evades the shadow obstruction in `WP-328`: **the arithmetic source sits in the scalar state on the base algebra, not in the `B`-valued free cumulants**. The enriched distribution can therefore be perfectly divisible even when its chosen scalarization is freely indecomposable.

The construction is deliberately stated algebraically at the unbounded stage. It does not claim that the coordinate `t` is a bounded element of a fixed `C*`-algebra. Section 2 already supplies genuine finite-dimensional `C*` realizations at every finite cutoff; the full algebraic lift isolates what additional analytic/domain input a global operator-valued candidate would actually have to contribute.

## 4. Why there is no contradiction with scalar free indecomposability

One might try to apply scalarization to (4) and conclude that `nu_s` must have a scalar free `m`-th root, contradicting `WP-326`. That inference is exactly what fails in operator-valued probability.

The roots in (4) live in the common amalgamation algebra. Under the scalar state `varphi_s`, the repeated elements `t/m` are not scalar-free independent random variables. They are the same base coordinate viewed through the same state. Their scalar sum is simply `t`, so its law is `nu_s`, but there is no identity

\[
\operatorname{law}_{\varphi_s}(t)
=
\operatorname{law}_{\varphi_s}(t/m)^{\boxplus m}.
\tag{20}
\]

In fact `WP-326` proves that (20) cannot hold for the source (1).

This explicit example sharpens the warning at the end of `WP-328`. A scalar state composed with an amalgamated conditional expectation is not a semigroup homomorphism from `B`-valued free convolution to scalar free convolution unless additional hypotheses force scalar freeness. The absence of that homomorphism is not a technical edge case: it is large enough to make an arbitrarily chosen scalar law appear below a trivially freely divisible deterministic `B`-valued object.

So operator-valued free convolution genuinely escapes the scalar-shadow no-go, but the first escape is **too large**, not selectively arithmetic.

## 5. Adversarial controls and exact boundary

The strongest control keeps the operator-valued object itself fixed. On `B=C[t]`, the distribution `delta_t`, the root `delta_{t/m}`, and the cumulants (17) do not depend on `s`, on primes, on `Lambda`, or even on the choice of scalar law. Only the state `tau` changes.

For example, replace `tau_s` by integration against any compactly supported probability measure, a Gaussian moment state, or another discrete exponentially decaying law. The same deterministic `B`-valued divisibility proof survives unchanged. At finite cutoff one can even preserve the exact support `Sigma_R` and vary only the masses. Hence neither prime-power support nor Mangoldt weighting is responsible for the positive/divisible theorem upstairs.

This kills several tempting but insufficient claims:

- the existence of a `B`-valued free convolution semigroup scalarizing to the source;
- complete positivity or positivity statements that hold merely because the random variable lies in the amalgamation algebra;
- a proof that scalar free indecomposability disappears after enlarging the base algebra;
- a source-dependent choice of scalar state followed by a universal operator-valued positivity theorem.

None of those mechanisms can explain the Weil sign. They simply relocate the source from the random-variable law into the base-state readout.

The finding does **not** rule out a genuinely non-deterministic operator-valued construction. A candidate can evade it if arithmetic is forced into higher `B`-valued cumulants, a nontrivial completely positive covariance map, noncentral boundary data, or another mixed coupling that cannot be changed arbitrarily while keeping the positive theorem intact. Nor does this result rule out a source-defined `C*`/von Neumann completion whose domain or affiliated-operator geometry has a nontrivial global theorem; the algebraic lift shows only that such analytic input, rather than operator-valued divisibility by itself, must carry the content.

Finally, the construction contains no Gamma factor, pole counterterm, Weil autocorrelation, or finite--archimedean local-to-global identity. It is therefore a matched-control obstruction on a precursor architecture, not a candidate proof of Weil positivity.

## 6. Prior-art and novelty audit

Operator-valued free probability, amalgamated free convolution, and operator-valued infinite divisibility are classical. Popa--Vinnikov's noncommutative free Levy--HinCin theory is already registered in `SOURCES.md` as a modern analytic/classification boundary for the operator-valued category. A literature audit also finds the standard operator-valued convolution-power theory and the foundational amalgamated-cumulant framework; nothing in the deterministic identity (13)--(17) is claimed as a new theorem of free probability.

The Mathia-specific content is the **matched-control application to the exact source left open by `WP-328`**. `WP-326` says `nu_s` is scalar-freely indecomposable. The present construction shows exactly how an operator-valued lift can nevertheless be infinitely divisible without contradicting that theorem: all arithmetic can be shifted into scalarization while the `B`-valued law remains the universal deterministic `delta_t`. This separates a vacuous operator-valued escape from a potentially meaningful one.

That distinction is important for future novelty audits. A proposed operator-valued realization should not receive credit merely for bypassing scalar free indecomposability. It must identify which nontrivial amalgamated datum carries the finite-prime source, prove that the datum is canonically forced, and show that its positivity is not invariant under the matched controls above.

## Consequence for the research line

The current frontier can be narrowed further than `WP-328` stated.

A generic operator-valued free lift is not promising merely because scalar free divisibility fails downstairs: deterministic amalgamation can make the enriched object freely infinitely divisible while reproducing the exact Mangoldt scalar law after a source-dependent state. At finite cutoff this is a genuine `C*` construction; for the full source it is exact algebraically and moment-determinate.

Therefore the next operator-valued candidate must make arithmetic live **before scalarization** in nontrivial mixed/operator data and derive its sign there. A credible construction must then show, in the same architecture, how the finite-prime term couples to the archimedean Gamma and polar/global contributions and why the resulting nonnegativity fails on matched non-arithmetic controls.

That requirement returns the search to the README's central question: a global sign-producing geometry, not a larger category in which any scalar source can be embedded into a positive or divisible object.
