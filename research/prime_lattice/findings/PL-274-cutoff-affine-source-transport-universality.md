# PL-274 — Cutoff transport of the normalized Weil source is generic affine kinematics, not arithmetic rigidity

**Evidence/status:** `LITERATURE+EXACT-DERIVED`; `DECISIVE-NEGATIVE + GENERIC-SOURCE-CONTROL + NO-NOVELTY-CLAIM` for cutoff-coherence mechanisms using only positivity, projective band coherence, and the canonical affine normalization of one fixed log-source.

## Claim

The source-coherence route left open by `PL-270`--`PL-273` has a sharp generic control. The dependence of the normalized finite-Weil source on the prime cutoff is an exact affine transport law shared by **every** locally finite measure on the positive log axis; it is not a rational-prime-specific constraint.

Let `eta` be any locally finite finite-on-compacts signed Borel measure on `(0,infinity)`. For cutoff `L>0`, define

\[
T_L(x)=1-\frac{x}{L},
\qquad
\nu_L=(T_L)_*\bigl(\eta\vert_{(0,L]}\bigr).
\]

For the zeta source,

\[
\eta_\zeta
=\sum_{q=p^a}\frac{\Lambda(q)}{\sqrt q}\,\delta_{\log q},
\]

this gives exactly the positive source convention used in `PL-270` and `PL-271`:

\[
\nu_L
=\sum_{\log q\le L}\frac{\Lambda(q)}{\sqrt q}
\,\delta_{1-\log q/L}.
\]

For `0<L_1<L_2`, put

\[
A_{L_1,L_2}(\omega)
=1-\frac{L_1}{L_2}(1-\omega).
\]

Then the cutoff family satisfies the exact identity

\[
\boxed{
\nu_{L_2}
=(A_{L_1,L_2})_*\nu_{L_1}
+(T_{L_2})_*\bigl(\eta\vert_{(L_1,L_2]}\bigr).
}
\]

The old source is transported by one universal affine map and only the newly admitted log-source is added. Moreover

\[
A_{L_2,L_3}\circ A_{L_1,L_2}=A_{L_1,L_3},
\]

so this is a genuine projective transport law across cutoffs.

This law remains too weak even when combined with all-band coherence and exact source identifiability. The family of all matrices

\[
\{Q_N[\nu_L]:N\ge0,\ L>0\}
\]

identifies the underlying log-source `eta` exactly, but **positive `eta` plus exact cutoff transport plus full cross-band coherence does not imply positivity of the Galerkin source matrices**. The one-atom control

\[
\eta=a\,\delta_x,
\qquad a>0,
\]

already satisfies every one of those source-side conditions. At the cutoff `L=2x`, however,

\[
\nu_{2x}=a\,\delta_{1/2},
\]

and `PL-272` gives, on the constant/first-cosine two-mode compression,

\[
Q_N[a\delta_{1/2}]\big|_{\{0,1\}}
=a\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\qquad(N\ge1).
\]

Thus the simplest remaining hope after `PL-271` is false:

\[
\boxed{
\text{positive fixed log-source}
+\text{ exact cutoff coherence}
+\text{ full band coherence/identifiability}
\not\Longrightarrow
\text{Weil-source matrix positivity}.
}
\]

What survives must use a relation that distinguishes the actual von Mangoldt log-source from an arbitrary positive measure, or must use the pole/archimedean completion in an essential way. Merely insisting that one coherent source be seen at every band and every cutoff supplies reconstruction, not sign.

## 1. Exact cutoff transport

If `x<=L_1`, write `omega=T_{L_1}(x)`. Then

\[
x=L_1(1-\omega),
\]

and therefore

\[
T_{L_2}(x)
=1-\frac{L_1}{L_2}(1-\omega)
=A_{L_1,L_2}(\omega).
\]

Splitting `eta|_(0,L_2]` into the old interval `(0,L_1]` and the newly admitted interval `(L_1,L_2]` proves the boxed transport identity. No prime-number theorem, Euler product, analytic continuation, or zero information enters it.

Between source-entry locations, the same statement has a transport-equation form. A source atom at normalized coordinate

\[
\omega(L)=1-\frac{x}{L}
\]

moves with velocity

\[
\omega'(L)=\frac{1-\omega(L)}{L}.
\]

Hence, on an interval of `L` containing no atom of `eta`, the measure family satisfies weakly

\[
\partial_L\nu_L
=-\partial_\omega\!\left(\frac{1-\omega}{L}\nu_L\right).
\]

At a source location `L=x`, new mass enters at `omega=0`. Groskin's source matrix annihilates that endpoint, `Q_N[\delta_0]=0`, so the finite matrix path remains continuous while its subsequent inward motion creates the derivative shock analyzed in `PL-264`. This explains why the local prime-edge geometry is compatible with the generic transport law: the arithmetic input is the event stream and its weights, not the affine motion itself.

## 2. The all-band/all-cutoff family is lossless but still sign-neutral

`PL-271` proves that at one fixed cutoff the full band tower has kernel exactly `R delta_0` on finite signed source measures. Apply that statement to two log-sources `eta` and `xi`. If

\[
Q_N[\nu_L^{\eta}]=Q_N[\nu_L^{\xi}]
\qquad\text{for every }N\ge0\text{ and every }L>0,
\]

then for each fixed `L`,

\[
\nu_L^{\eta}-\nu_L^{\xi}=b_L\delta_0.
\]

Because `T_L` is a bijection from `(0,L)` onto `(0,1)`, this implies

\[
\eta\vert_{(0,L)}=\xi\vert_{(0,L)}.
\]

Given any bounded interval `(0,R]`, choose `L>R`; then the two measures agree on `(0,R]`. Since `R` is arbitrary,

\[
\boxed{\eta=\xi.}
\]

Thus adding the cutoff parameter removes even the endpoint ambiguity of the one-cutoff projective tower: an atom invisible exactly when it enters at `omega=0` becomes visible at every later cutoff. The complete `(L,N)` family is an exact encoding of the underlying log-source.

That result is useful only as an information statement. It does not create order. The one-atom positive source above is already reconstructed perfectly and transported perfectly, yet it produces an indefinite source form. `PL-273` gives the stronger pointwise version: for every interior normalized coordinate `0<omega<1`, a positive atom `delta_omega` is indefinite on sufficiently large bands. Hence increasing `N` does not repair the one-atom counterexample after the atom has moved into the interior.

There is therefore a clean separation:

\[
\text{source identity and coherent transport}
\quad\neq\quad
\text{order/positivity of the induced Weil form}.
\]

The failure is not caused by finite-band aliasing. It persists after that information loss has been removed completely.

## 3. Adversarial control against a false arithmetic interpretation

For the rational-prime system, the underlying measure `eta_zeta` is highly special: its support consists of prime-power logarithms and its masses are `Lambda(q)/sqrt(q)`. The present result does **not** replace that source by a Beurling system while preserving zeta, nor does it claim that every nonlocal relation among those masses is generic.

The negative statement is narrower and exact. Any proposed mechanism whose only cross-cutoff input is

1. positivity of one fixed log-source `eta`,
2. restriction to `x<=L`,
3. affine normalization `x -> 1-x/L`, and
4. compatibility of the resulting matrices as `N` grows,

is shared by the one-atom control and therefore cannot force positive semidefiniteness. Recovering the entire source from those data does not help: it merely inverts the encoding.

Accordingly, a surviving source-side theorem must use an additional relation that the one-atom and arbitrary-positive-measure controls fail. Examples include a proved inequality coupling **different** von Mangoldt masses, a completed identity in which the pole and archimedean blocks participate essentially, or another rational-prime-specific constraint that is not equivalent to reconstructing `eta_zeta` from its normalized images. Such a relation would still need its own sign argument; inserting the classical explicit formula or zero divisor by definition would not satisfy the line's mechanism gate.

## 4. Prior-art and novelty audit

The normalized coordinate

\[
\omega_q=1-\frac{\log q}{\log c}
\]

and the linear finite source calculus are due to the Connes--van Suijlekom/Connes--Consani--Moscovici truncation as made explicit in Akiva Groskin's finite Guinand--Weil dictionary. `PL-264` records Groskin's separate result that differentiating the cutoff path at a prime-power entry recovers the von Mangoldt weight through a universal singular matrix jet. `PL-270`--`PL-273` already establish the finite quotient, projective identifiability, and failure of source-cone positivity used in the control above.

The affine push-forward identity is an elementary consequence of this existing cutoff parametrization, and the all-cutoff injectivity statement is an elementary combination with `PL-271`. A targeted literature search found the current Groskin finite-source and matrix-valued-von-Mangoldt papers but did not reveal this exact transport/no-go packaged as a theorem. That search cannot establish novelty, and none is claimed. The durable contribution is the matched control at the current line frontier: **cross-cutoff coherence generated solely by the canonical rescaling is generic kinematics and therefore cannot be the missing source-side positivity law.**

## Boundaries and falsification

This finding does not rule out a genuine arithmetic cross-cutoff law. It rules out only laws that follow for arbitrary `eta` from restriction plus the affine normalization `T_L`. A future mechanism evades the obstruction if it proves a relation involving the actual prime-power support or von Mangoldt masses that fails for a general positive log-source and then uses that relation to control the completed Weil form.

Nor does the one-atom control contradict the exact Guinand--Weil identity. It is a control for the source-to-matrix map, not an alternative zeta source with the same zero side. Its role is to falsify any implication claimed to follow from generic source positivity/coherence alone.

## Sources

- Akiva Groskin, **“A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form,”** arXiv:2607.02828v3 [math.NT] (revised 14 August 2026). Lemma 2.3 and Corollary 2.4 give the exact finite source calculus and the normalized prime-power source used here.
- Local dependencies: `PL-264`, `PL-270`, `PL-271`, `PL-272`, and `PL-273`.
