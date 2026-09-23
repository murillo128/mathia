# MC-487 — First-exit inverse shifts are affine gauge; the surviving q-dependence is support and cutoff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-484` rewrites the exact Buchstab first-exit branch by choosing a root of

\[
q\mid n(n+h)
\]

and writing

\[
n=a+qm,
\qquad a\equiv0\text{ or }-h\pmod q.
\]

In that `m`-coordinate, the character phase and the residual pair-sieve mask both acquire the same inverse-dilation shift `h q^{-1}`: modulo the character conductor `p`, one sees a translated-ratio phase with shift `h q^{-1}`, while modulo `P(q)` the two forbidden sieve classes differ by `h q^{-1}`. The accepted source clue therefore retained the common motion of those two shifts as part of the possible surviving `q`-coupling.

That visible inverse-shift motion is **not an independent arithmetic resource**. It is exactly the affine covariance created by the root parameterization. The same row-dependent change of variable that produced the shifts removes both of them simultaneously.

Assume first that `q\ne p` and consider the root `a=0`, so `n=qm`. Put

\[
\delta_{q,p}\equiv hq^{-1}\pmod p,
\qquad
\delta_q\equiv hq^{-1}\pmod{P(q)}.
\]

Then, with

\[
K_{\delta}(m)=\chi(m+\delta)\overline{\chi(m)},
\]

one has exactly

\[
\boxed{
K_{\delta_{q,p}}(m)
=
\chi(qm+h)\overline{\chi(qm)}
=
K_h(qm).
}
\tag{1}
\]

Likewise, because `(q,P(q))=1`, multiplication by `q^2` is a unit modulo every prime below `q`, and therefore

\[
\boxed{
(m(m+\delta_q),P(q))=1
\iff
((qm)(qm+h),P(q))=1.
}
\tag{2}
\]

Thus after returning to the intrinsic integer coordinate

\[
x=qm=n,
\]

the first root branch has **fixed character separation `h` and fixed pair-sieve root separation `h`**. The `q`-dependence has moved into the arithmetic-progression support `x\in qI_{q,0}` (equivalently `q\mid x` together with the exact interval endpoints), the changing roughness cutoff `P(q)`, and whatever outer source weights depend on `q`.

For the other root, write

\[
n=-h+qm,
\qquad x=qm=n+h.
\]

Then the same calculation gives

\[
\boxed{
\chi(qm)\overline{\chi(qm-h)}
=
\chi(x)\overline{\chi(x-h)},
}
\tag{3}
\]

and

\[
\boxed{
(m(m-hq^{-1}),P(q))=1
\iff
(x(x-h),P(q))=1.
}
\tag{4}
\]

up to the harmless choice of sign convention for the shifted `m`-coordinate. Again the inverse shift disappears, while the branch support is the progression `x\equiv0 (mod q)` for `x=n+h`. If `q\mid h`, the two roots modulo `q` merge; this removes a branch rather than creating a new inverse-shift degree of freedom.

Equations `(1)`--`(4)` give the representation-level obstruction:

\[
\boxed{
\text{the common motion }hq^{-1}\text{ in phase and sieve mask is affine gauge.}
}
\tag{5}
\]

A theorem cannot claim a gain merely from the fact that the same first-exit prime moves both shifts. After the natural branchwise affine normalization, that motion is gone. What remains genuinely source-sensitive is the family of **q-dependent arithmetic-progression supports, endpoints, sieve cutoffs, and outer coefficients**.

This does not collapse the live route. The affine normalizations are different for different `q`, so they cannot be applied as one common column permutation before a cross-`q` recombination. In a common intrinsic coordinate the cost is exactly that each row now lives on a different progression and carries a different `P(q)`-roughness condition. Hence cross-`q` information has not vanished; it has been localized to the support/cutoff geometry rather than to the bare inverse-shift labels.

The practical consequence is a sharper gate for the accepted first-exit clue. Any continuation that freezes the progression/cutoff profile and argues only from the motion of `hq^{-1}` is coordinate-dependent and should be rejected. A viable conductor-sensitive estimate must exploit the q-dependent progression incidence, endpoint nesting, changing roughness cutoff, actual outer coefficients, or a proved interaction among those objects before absolute values.

No estimate for the first-exit family, `M(x)`, or any zeta zero-free region is proved here.

## 1. The character shift is exactly multiplicative covariance

For the root `a=0`, `q` is a unit modulo `p`. Since

\[
qm+h\equiv q(m+hq^{-1})\pmod p,
\]

multiplicativity gives

\[
\chi(qm+h)
=
\chi(q)\chi(m+hq^{-1}),
\]

while

\[
\overline{\chi(qm)}
=
\overline{\chi(q)}\,\overline{\chi(m)}.
\]

The unit factors cancel, proving `(1)`. The apparent moving translate in the `m` chart is therefore just the pullback of the fixed translated-ratio kernel in the original integer chart.

For the second root the same cancellation occurs after taking `x=n+h=qm`, proving `(3)`. The two branches differ only by whether the fixed translated-ratio kernel is written with separation `+h` or `-h` and by which original divisibility condition is being represented.

This is the same kind of gauge test already used in `MC-215`: a source-dependent character phase that can be removed by a unit-coordinate change is not by itself invariant arithmetic information. The new point is that in the `MC-484` first-exit representation the **sieve mask transforms covariantly at the same time**, so the entire visible inverse-shift pair is removable branchwise.

## 2. The residual pair sieve has the same affine covariance

The first-exit residual mask at cutoff `q` is

\[
A_q(n)=\mathbf1_{(n(n+h),P(q))=1}.
\]

On the root `n=qm`, multiplying the `m`-coordinate product by the unit `q^2` modulo `P(q)` gives

\[
q^2m(m+hq^{-1})
\equiv
(qm)(qm+h)
\pmod{P(q)}.
\]

Because every prime dividing `P(q)` is strictly below `q`, `q` is invertible modulo `P(q)`, so multiplication by `q^2` does not change coprimality with `P(q)`. This proves `(2)`.

The second root is identical after `x=qm=n+h`; then the fixed polynomial is `x(x-h)`, proving `(4)`. Root collisions at primes dividing `h` remain the usual local-density degeneracy of the pair sieve and are independent of the inverse-dilation coordinate.

Consequently the statement in `MC-484` that character and sieve shifts both close under first-exit parameterization is exact, but the common shift should not itself be counted as retained arithmetic structure. It records how the fixed two-point configuration `{0,-h}` looks after division by `q`.

## 3. What the q-coupling becomes after normalization

Write schematically the root-zero piece from `MC-484` as

\[
T_q^{(0)}
=
\sum_{m\in I_{q,0}}
 c_{q,m}\,
 K_{h q^{-1}}(m)
 \mathbf1_{(m(m+hq^{-1}),P(q))=1},
\tag{6}
\]

where `c_{q,m}` denotes the exact outer/staged coefficient that survives before this branch is isolated. With `x=qm`, `(6)` becomes exactly

\[
T_q^{(0)}
=
\sum_{x\in qI_{q,0}}
 c_{q,x/q}\,
 K_h(x)
 \mathbf1_{(x(x+h),P(q))=1}.
\tag{7}
\]

There is no moving inverse shift left. Instead, the same fixed kernel `K_h` is sampled on a q-dependent progression, through a q-dependent roughness cutoff, with q-dependent endpoints and coefficients.

This is not merely cosmetic. It identifies which operations are incapable of using the remaining source information:

- any **per-q** estimate invariant under affine relabeling cannot gain from `hq^{-1}` itself;
- replacing the progression indicators and `P(q)` masks by one common coefficient profile returns to the coefficient-blind setting closed by `MC-485`--`MC-486`;
- a genuine cross-q estimate may still use the relative placement of the different progression supports or the nested cutoffs, because the branchwise changes of variable are not one common transformation of the whole q-family.

Thus the normalized source frame suggests a more intrinsic formulation of the live object: a fixed translated-ratio character kernel restricted simultaneously by first-exit progression incidence and by a nested dimension-two roughness condition.

## 4. Relation to the current obstruction atlas

`MC-484` proves that exact Buchstab first exit removes the selector that blocked positive sieve bracketing while preserving a dimension-two residual pair sieve. `MC-485` and `MC-486` then show that the complete or incomplete bare inverse-shift character family has no generic coefficient-blind `L^2` gain below the `sqrt(p)` scale.

The present finding explains why those phase-only routes were structurally fragile: the inverse-shift labels are not intrinsic once the full first-exit branch is retained. They arise from dividing the fixed source pair by the current first-exit prime. The only possible invariant value of the q-index must therefore survive the normalization `(6)` to `(7)`.

This is compatible with, but distinct from, `MC-215`. There a **single prescribed residue** was gauged to the identity and the surviving object was a principal/transverse covariance. Here the same first-exit dilation simultaneously fixes a character translate and a dimension-two sieve translate, and the surviving object is cross-row support/cutoff dependence. It is also distinct from `MC-238`: that finding studies a smooth-dilation orbit inside a fixed shell-square residue group and proves exact blind character modes for the whole orbit. Here the modulus `P(q)` and the support itself vary with `q`; the result is a coordinate audit, not a subgroup-generation statement.

A useful falsification test follows. If a proposed continuation still works unchanged after replacing every first-exit row by an arbitrary relabeling that preserves only the multiset of inverse shifts, then it is not using the intrinsic first-exit source. Conversely, an estimate stated directly in terms of the progression family `(7)`, the nested cutoffs, and the actual coefficients passes this particular gauge test and remains live.

## 5. Prior art and novelty boundary

The ingredients are classical. Buchstab first-exit decomposition and switching/reparameterization of sieve branches are standard sieve-theoretic operations; `MC-484` already audits that background against the classical Buchstab/DHR/Rosser-Iwaniec literature. Multiplicative-character covariance under multiplication by a unit and invariance of coprimality under multiplication by a unit are elementary. `MC-215` is the existing Mathia precedent for treating removable character phases as gauge rather than arithmetic information.

A targeted literature search for Buchstab/switching identities combined with affine changes of variables and multiplicative-character sums found standard sieve-switching and character-sum frameworks, including Friedlander--Iwaniec's classical sieve literature and later work on weighted sieves with switching, but no reason to claim the elementary identities `(1)`--`(4)` as new mathematics. No novelty is claimed.

The durable delta is repository-internal and frontier-specific: the accepted `MC-484` continuation had retained the **common moving inverse shift** in the character and pair-sieve factors as one candidate source of q-coupling. Equations `(1)`--`(7)` show exactly that this coupling is a branchwise affine coordinate effect. The live first-exit question must therefore be asked after normalization, where the q-variable survives only through progression support, endpoint/cutoff structure, and actual source coefficients.

## Evidence boundary

- Exact: equations `(1)`--`(7)` under the stated unit hypotheses.
- Exact: the inverse-shift labels in the phase and pair-sieve mask can be removed simultaneously on each first-exit root branch.
- Exact: doing so transfers q-dependence to the branch progression/support, nested cutoff `P(q)`, endpoints, and coefficients.
- Not proved: any cancellation between different q-branches after this normalization.
- Not proved: any conductor-power saving from the progression/cutoff family.
- Not proved: any special alignment of the actual source coefficients.
- Not proved: any improvement for `M(x)`, a zero-free region, or RH.

The next analytic question is therefore narrower than the current clue formulation: after fixing the translated-ratio separation in the intrinsic integer coordinate, can the **family of first-exit progression restrictions together with the changing pair-sieve cutoff and exact source weights** yield a conductor-sensitive dispersion/bilinear estimate before absolute values, or is that normalized family subject to another exact tariff?