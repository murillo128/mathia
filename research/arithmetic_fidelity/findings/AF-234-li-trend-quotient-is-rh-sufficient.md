# AF-234 — the Li trend quotient is RH-sufficient under subleading distortion

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-CRITERION-SPECIALIZATION`, `RH-SUFFICIENT-QUOTIENT`, `TARGET-METRIC`, `ROBUSTNESS`, `NO-NOVELTY-CLAIM`

## Claim

Arithmetic Fidelity must distinguish two different requirements:

1. recovering the arithmetic source or its rational-prime provenance; and
2. retaining only a downstream discriminator already proved sufficient for the final theorem.

The Keiper--Li coefficients give a concrete RH-facing case where the second requirement is strictly weaker.

Let `lambda_n` be Li's coefficients for the Riemann xi function, in Li's normalization,

\[
\lambda_n
=\sum_\rho\left[1-\left(1-\frac1\rho\right)^n\right],
\qquad n\ge1,
\tag{1}
\]

with the standard symmetric interpretation of the zero sum. Li proved

\[
\mathrm{RH}
\iff
\lambda_n\ge0\quad\text{for every }n\ge1.
\tag{2}
\]

Voros later proved the stronger large-`n` dichotomy

\[
\mathrm{RH}
\iff
\lambda_n
=\frac12 n\bigl(\log n-1+\gamma-\log 2\pi\bigr)+o(n),
\tag{3}
\]

whereas failure of RH produces non-tempered oscillations governed by off-critical zeros.

Define an asymptotic equivalence relation on real sequences by

\[
a\sim_{\mathrm{tr}} b
\iff
\frac{a_n-b_n}{n\log n}\longrightarrow0.
\tag{4}
\]

Then the quotient class of the Li sequence is already sufficient for RH:

\[
\boxed{
\mathrm{RH}
\iff
\frac{a_n}{n\log n}\longrightarrow\frac12
\quad\text{for one, equivalently every, }a\sim_{\mathrm{tr}}\lambda.
}
\tag{5}
\]

Equivalently, **any approximation** `\widetilde\lambda_n` satisfying

\[
\widetilde\lambda_n-\lambda_n=o(n\log n)
\tag{6}
\]

preserves the RH decision through the coarse asymptotic test

\[
\boxed{
\mathrm{RH}
\iff
\frac{\widetilde\lambda_n}{n\log n}\longrightarrow\frac12.
}
\tag{7}
\]

Thus exact Li values, every finite prefix, and all additive detail of order `o(n log n)` may be discarded without losing this particular RH discriminator.

Voros' decomposition makes the surviving datum even more explicit. Write

\[
\lambda_n=S_n+\overline S_n,
\tag{8}
\]

where `S_n` is the contribution of `(s-1)\zeta(s)` and `\overline S_n` is the explicit archimedean/completion contribution. Voros obtains unconditionally

\[
\overline S_n
=\frac12 n\bigl(\log n-1+\gamma-\log2\pi\bigr)+O(1)
\tag{9}
\]

at the precision needed here, while under RH

\[
S_n=o(n).
\tag{10}
\]

Combining `(3)`, `(8)`, and `(9)` gives the exact quotient reformulation

\[
\boxed{
\mathrm{RH}
\iff
S_n=o(n\log n).
}
\tag{11}
\]

If

\[
\mathcal N_{\mathrm{tr}}
:=\{u=(u_n):u_n=o(n\log n)\},
\tag{12}
\]

then `(11)` says that RH is exactly the statement that the zeta-dependent Li remainder maps to the **zero class** in the additive quotient

\[
\mathbb R^{\mathbb N}/\mathcal N_{\mathrm{tr}}.
\tag{13}
\]

This is a genuine target-sufficiency compression: the quotient deliberately forgets enormous exact information, but the forgotten directions are contained in the kernel of the declared RH discriminator.

## Derivation

### The leading Li trend is itself an RH criterion

Under RH, `(3)` immediately yields

\[
\frac{\lambda_n}{n\log n}
=\frac12
+O\!\left(\frac1{\log n}\right)
+o\!\left(\frac1{\log n}\right)
\longrightarrow\frac12.
\tag{14}
\]

Conversely, Voros' asymptotic theorem gives a dichotomy: failure of RH produces a non-tempered oscillatory contribution from zeros off the critical line rather than the tempered trend `(3)`. Hence the finite limit in `(14)` cannot occur in the RH-false branch. Therefore

\[
\boxed{
\mathrm{RH}
\iff
\lambda_n/(n\log n)\to1/2.
}
\tag{15}
\]

No new criterion is claimed here; `(15)` is a direct coarse consequence of Voros' stronger theorem.

### The trend quotient is well defined

If `a\sim_{\mathrm{tr}}b`, then

\[
\frac{a_n}{n\log n}
-
\frac{b_n}{n\log n}
\longrightarrow0.
\tag{16}
\]

Therefore existence and value of the normalized limit in `(15)` are invariant under the quotient `(4)`. Taking `b=lambda` proves `(5)--(7)`.

Finite changes disappear automatically in this quotient. More generally, errors may diverge in absolute size -- for example `n`, `n\log\log n`, or `n\log n/\log\log n` -- and are still invisible provided they are `o(n\log n)`.

The scale is load bearing for this decoder. An unrestricted perturbation

\[
e_n=c\,n\log n,
\qquad c\ne0,
\tag{17}
\]

changes the normalized limit by `c`. Thus one cannot replace `(6)` by arbitrary `O(n\log n)` distortion while keeping the exact target test `(7)` unchanged. This is a metric/quotient boundary, not a claim that `o(n\log n)` is a universally minimal representation of RH.

### Subtracting the explicit completion isolates the surviving zeta-dependent class

Voros writes `lambda_n=S_n+\overline S_n`, with `\overline S_n` determined by the explicit completion factors. His unconditional asymptotic expansion implies `(9)`, so

\[
\frac{\lambda_n}{n\log n}
=\frac12+rac{S_n}{n\log n}+o(1).
\tag{18}
\]

If RH holds, `(10)` gives `S_n/(n\log n)\to0`.

Conversely, if `S_n=o(n\log n)`, then `(18)` gives `lambda_n/(n\log n)\to1/2`; by `(15)`, RH follows. This proves `(11)`.

The quotient `(13)` therefore removes the universal archimedean trend and then asks only whether the remaining zeta-dependent component is asymptotically negligible at the `n log n` scale. Exact reconstruction of `S_n`, of the zero divisor, or of the rational primes is strictly stronger than this declared endpoint.

## Exact controls and boundaries

### Exact Li positivity and asymptotic trend are different fidelity metrics

Li's original criterion `(2)` is pointwise and exact: changing even one coefficient across zero can alter the all-`n` positivity statement. The trend criterion `(15)` is tail-asymptotic and deliberately ignores finite prefixes and `o(n\log n)` additive perturbations.

Both are RH-sufficient, but their distortion geometries are different. Therefore saying that a representation "preserves the Li criterion" is ambiguous unless it specifies whether it preserves exact signs, the full coefficient sequence, the two-term asymptotic, or only the normalized trend class.

### A full RH-sufficient endpoint need not recover rational-prime provenance

AF-017 gives Grosswald--Schnitzer matched Euler-product controls with changed generator norms but the same nontrivial zero divisor in the relevant half-plane. The zero-derived expression `(1)` therefore cannot distinguish those norm systems at the divisor layer, even though for the actual Riemann divisor its Li sequence is RH-sufficient.

This does **not** say that a Grosswald--Schnitzer modified Euler product satisfies all hypotheses of Li's theorem under its own natural completion. The only control claim used here is narrower: once the retained endpoint is the Riemann zero divisor, or any deterministic transform of that divisor such as `(1)`, distinct upstream norm systems can map to the same retained data.

Hence

\[
\boxed{
\text{RH-target sufficiency}
\not\Rightarrow
\text{rational-prime source fidelity}.
}
\tag{19}
\]

This is the concrete RH specialization of AF-165's task-relative endpoint principle.

### Source fidelity can still be necessary at an earlier proof stage

Equation `(19)` must not be inverted into "prime information never matters." A proof route may need exact arithmetic structure to establish that its compressed endpoint really is the Riemann Li/divisor object or to prove the required asymptotic bound.

The correct gate is therefore stage-specific:

- before an RH-sufficient quotient has been proved, loss of the discriminator required by the next theorem can kill the route;
- after a destination has independently been proved sufficient for RH, distinctions lying wholly inside one destination fiber are no longer required merely because they existed upstream.

The proof obligation is **sufficiency of the retained target**, not universal preservation of source identity.

### This finding does not make RH easier by definition

The quotient `(13)` is useful because the equivalence `(11)` is a classical theorem-level consequence of the Li/Voros theory, not because the quotient was defined to carry an arbitrary one-bit answer. But proving that the actual zeta-dependent remainder belongs to `\mathcal N_{\mathrm{tr}}` is still equivalent to RH.

Thus `(13)` is a valid endpoint contract and a compression boundary, not a proof of membership in the zero class.

## Prior art and novelty assessment

The underlying RH criteria are classical.

- Xian-Jin Li, **“The positivity of a sequence of numbers and the Riemann hypothesis,”** *Journal of Number Theory* 65(2) (1997), 325--333, DOI `10.1006/jnth.1997.2137`, proves the positivity criterion `(2)`.
- Enrico Bombieri and Jeffrey C. Lagarias, **“Complements to Li's criterion for the Riemann hypothesis,”** *Journal of Number Theory* 77(2) (1999), 274--287, DOI `10.1006/jnth.1999.2392`, develops the general zero-set form of Li-type criteria and quantitative growth conditions.
- André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, proves the RH-true tempered asymptotic and RH-false non-tempered oscillatory alternative used in `(3)` and `(15)`, and gives the decomposition `(8)` with the unconditional completion trend `(9)`.

No novelty is claimed for Li's criterion, the Voros asymptotic criterion, or the decomposition of the coefficients. The derived quotient statements `(5)--(13)` are elementary consequences of that prior art.

The Arithmetic Fidelity contribution is their **placement as a target-sufficiency counterweight to source-fidelity demands**: an intrinsically defined, theorem-proved RH endpoint can tolerate an entire `o(n\log n)` additive ideal while failing to retain rational-prime provenance. This supplies an actual RH-facing example in which the mathematically relevant question is not "did the prime discriminator survive?" but "did the discriminator required by the proved endpoint theorem survive at the declared metric scale?"

## Consequences for the research frontier

1. A compression should no longer be rejected solely because it loses rational-prime identity. It is fatal only when the lost distinction is required by the next theorem or when no independently proved RH-sufficient destination has yet been reached.
2. The Li trend quotient provides a concrete benchmark for future information-price work: the target metric is explicit, its tolerated additive error is `o(n\log n)`, and the endpoint is rigorously RH-sufficient.
3. A useful next question is therefore upstream rather than definitional: identify natural arithmetic/analytic representations from which the class of `S_n` in `\mathbb R^{\mathbb N}/\mathcal N_{\mathrm{tr}}` can be controlled without reconstructing strictly more information than the RH endpoint consumes.
4. Any proposed reduced representation must still be tested against AF-017/AF-165-style same-endpoint controls. Such controls are harmless if they remain inside one RH-equivalence class, but decisive if they change the Li trend class while the proposed representation cannot distinguish them.

## Decisive audit test

For a proposed compressed route into the Li/Voros endpoint:

1. specify the retained data and a theorem mapping them to an approximation `\widetilde\lambda_n` or remainder `\widetilde S_n`;
2. prove an error bound at the **declared target scale**, with `o(n\log n)` sufficient for the coarse trend quotient;
3. verify that any matched controls collapsed by the retained representation also agree in the required Li trend class, rather than demanding full prime-source equality;
4. reject the route if its error is only uncontrolled `O(n\log n)` or larger, if the target-sufficiency theorem secretly uses discarded source data, or if the retained object is merely defined to encode the RH truth value.

Passing these gates would establish fidelity to an actual RH-sufficient quotient. It would still not prove that the required `o(n\log n)` estimate holds for zeta.