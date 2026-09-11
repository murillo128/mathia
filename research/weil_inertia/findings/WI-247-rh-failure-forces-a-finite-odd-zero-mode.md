# WI-247 — RH failure forces a finite odd zero mode

## Status

- **Evidence:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.
- **Scope:** this closes a logical gap between the odd-sector source tariffs of `WI-241`/`WI-244`--`WI-246` and the RH-facing first-crossing program of `WI-238`. It does **not** prove RH and does not supply the missing arithmetic upper bound for the signed von Mangoldt discrepancy.
- **Novelty boundary:** Yoshida's odd-test criterion is classical, and Bombieri stated continuity of the parity-restricted variational minima. Suzuki 2026 explicitly notes that the details of Bombieri's parity-continuity proof are not fully provided, then proves continuity of the unrestricted minimum by a fixed-interval compactness argument. The exact parity-restricted continuity proof below is obtained by running Suzuki's argument inside the closed odd subspace. No priority claim is made for the continuity statement; the durable new value here is the audited bridge from `not RH` to an attained finite **odd** zero mode and hence directly to the finite-radius source tariff already isolated in this line.

## Claim

For `a>0`, let

\[
\lambda_a^-:=\inf_{0\ne v\in H^1_{0,-}(-a,a)}
\frac{Q_W^a(v)}{\|v\|_2^2},
\]

where `H^1_{0,-}(-a,a)` is the odd subspace of `H_0^1(-a,a)`. Equivalently, after closing the form, `lambda_a^-` is the bottom of the odd reducing part of Suzuki's localized self-adjoint operator `A_a`.

Then:

1. `a -> lambda_a^-` is continuous on `(0,infinity)`;
2. it is nonincreasing in `a`;
3. `lambda_a^->0` for all sufficiently small `a`;
4. if RH is false, then `lambda_A^-<=0` for some finite `A`.

Consequently, under `not RH` the finite number

\[
\boxed{
 a_*^-:=\inf\{a>0:\lambda_a^-\le0\}
}
\]

satisfies

\[
\boxed{
0<a_*^-<\infty,\qquad
\lambda_a^->0\ (a<a_*^-),\qquad
\lambda_{a_*^-}^-=0.
}
\]

The odd restriction of `A_{a_*^-}` has discrete spectrum, so the zero is attained: there is a normalized nonzero odd form-domain vector `v_*` supported in `[-a_*^-,a_*^-]` with

\[
\boxed{Q_W^{a_*^-}(v_*)=0.}
\]

Moreover `v_*` cannot be supported in any strict interior interval `[-b,b]` with `b<a_*^-`.

Combining this with the exact odd source decomposition and the optimal joint finite-radius mean reserve of `WI-246` gives the RH-failure necessary condition

\[
\boxed{
\neg\mathrm{RH}
\Longrightarrow
\exists\ a_*^-<\infty,\ v_*\ \text{odd},\ \|v_*\|_2=1:\quad
\Delta_\Lambda^{a_*^-}(v_*)
\ge \frac{M(0)+\beta_*(a_*^-)}2.
}
\]

Since `WI-246` proves `beta_*(a)>B_Robin(a)` for every finite `a`, every RH failure therefore forces an odd finite-radius source witness paying **strictly more** than the termwise Robin tariff:

\[
\boxed{
\Delta_\Lambda^{a_*^-}(v_*)
>
\frac{M(0)+B_{\rm Robin}(a_*^-)}2.
}
\]

Thus the odd-sector tariff is not merely a condition on a hypothetical parity choice of Suzuki's unrestricted ground state. An RH failure itself forces some finite odd degeneracy to which the tariff applies.

## 1. Exact prior-art inputs

Suzuki's 2026 preprint records the two classical facts needed at the ends of the argument.

First, citing Yoshida, Proposition 1, Suzuki states that

\[
Q_W(v)>0\quad\text{for every nonzero odd }v\in C_c^\infty(\mathbb R)
\quad\Longrightarrow\quad \mathrm{RH}.
\]

This is stronger for the present purpose than the corresponding even statement, which permits possible real zeros. By contraposition,

\[
\neg\mathrm{RH}
\quad\Longrightarrow\quad
\exists\,0\ne v\in C_c^\infty(\mathbb R),\ v\text{ odd},\ Q_W(v)\le0.
\]

Because such a `v` has finite support, `lambda_A^-<=0` for some finite `A`.

Second, Suzuki proves that the unrestricted localized bottom eigenvalue is continuous by scaling every interval `[-a,a]` to `[-1,1]`. In Section 4.5 he also defines the parity-restricted minima `lambda_a^+` and `lambda_a^-`, proves

\[
\lambda_a=\min(\lambda_a^+,\lambda_a^-),
\]

and notes explicitly that continuity of `lambda_a^+/-` was asserted in Bombieri's Theorem 5, although the details are not fully provided there. The next section records why Suzuki's own rigorous continuity proof already supplies those missing details after restriction to either parity sector.

Primary sources:

- H. Yoshida, **On Hermitian Forms attached to Zeta Functions**, *Advanced Studies in Pure Mathematics* 21 (1992), 281--325, Proposition 1 and Lemma 2.
- E. Bombieri, **Remarks on Weil's quadratic functional in the theory of prime numbers, I**, *Rend. Lincei Mat. Appl.* 11 (2000), 183--233, especially Theorem 5.
- M. Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026), especially Theorem 1.3 and Sections 4.2--4.5. Suzuki's current HTML version explicitly states the Yoshida odd criterion, the parity decomposition, and the caveat on the earlier parity-continuity proof.

## 2. Suzuki's continuity argument is parity-stable

Use Suzuki's unitary scaling to the fixed interval. If `w(t)=v(at)`, the Rayleigh quotient becomes

\[
R(a,w)=\frac{\bar q_a(w)}{\|w\|_2^2}
\]

on `[-1,1]`, with

\[
\bar q_a=\bar q^0+\bar q_a^1.
\]

Here `bar q^0` is the `a`-independent lower-bounded closed logarithmic form, while on every compact `a`-interval the remainder `bar q_a^1` is a bounded quadratic form depending jointly continuously on `(a,w)` in the `L^2` topology. Suzuki's compact embedding

\[
H^{\log}(-1,1)\hookrightarrow L^2(-1,1)
\]

is the compactness input for the lower-semicontinuity half of the proof.

All ingredients preserve parity. Reflection `Jw(x)=w(-x)` commutes with the localized form, as Suzuki verifies in Section 4.5. Therefore the odd space

\[
L_-^2(-1,1):=\{w:Jw=-w\}
\]

is a closed reducing subspace for every `bar q_a`, and it is also closed in `H^{log}`. The compact embedding remains compact after restricting its domain and codomain to this closed odd subspace.

There is one core issue to check. Suzuki's upper-semicontinuity proof approximates a form-domain minimizer by `C_c^infty(-1,1)`. If `w_0` is odd, begin with any smooth-core approximants `u_n` and apply the odd projection

\[
P_-u_n:=\frac{u_n-Ju_n}{2}.
\]

Because the closed form is reflection invariant and its even/odd cross terms vanish, `P_-` is bounded in any shifted positive form norm. Hence `P_-u_n` converges to `w_0` in the same form norm; after harmless normalization these are odd smooth compactly supported approximants. Thus Suzuki's upper-semicontinuity proof stays entirely inside the odd sector and gives

\[
\limsup_{a\to a_0}\lambda_a^-\le\lambda_{a_0}^-.
\]

For lower semicontinuity, take normalized odd minimizers `w_n` for `lambda_{a_n}^-` with `a_n->a_0`. The same comparison with a fixed odd test vector bounds `lambda_{a_n}^-` above. Suzuki's decomposition then bounds `bar{\mathcal L}(w_n)` and hence the `H^{log}` norms. Compactness yields an `L^2`-convergent subsequence. Since `L_-^2` is closed, its limit `w_*` remains odd. Lower semicontinuity of `bar q^0` plus joint continuity of `bar q_a^1` gives

\[
\liminf_{n\to\infty}\lambda_{a_n}^-
\ge \bar q_{a_0}(w_*)
\ge\lambda_{a_0}^-.
\]

This proves the claimed continuity of `lambda_a^-`. No new estimate is inserted; this is Suzuki's proof with the parity projection made explicit.

## 3. Monotonicity, attainment, and the finite odd threshold

If `0<a<b`, zero extension embeds the odd form class on `[-a,a]` isometrically into the odd form class on `[-b,b]`. The global Weil quadratic functional and the `L^2` norm of the test do not change under this embedding. Therefore

\[
\boxed{\lambda_b^-\le\lambda_a^-.}
\]

Suzuki/Yoshida give positivity of the full localized form for sufficiently small support. Hence its odd restriction is also positive there, so `lambda_a^->0` for small `a`.

Under `not RH`, Yoshida's odd criterion supplies a finite-support odd smooth test with nonpositive Weil value, hence `lambda_A^-<=0` for some finite `A`. Continuity and monotonicity now imply

\[
0<a_*^-<\infty,\qquad
\lambda_a^->0\quad(a<a_*^-),\qquad
\lambda_{a_*^-}^-=0.
\]

Suzuki's localized operator commutes with parity and has lower-bounded discrete spectrum. Its odd reducing part therefore also has discrete spectrum, and its spectral bottom at `a_*^-` is an actual odd eigenvector `v_*` with eigenvalue zero.

The strict-support statement follows immediately. If the essential support of `v_*` were contained in `[-b,b]` for some `b<a_*^-`, zero extension would identify the same vector in the smaller localized form and give `Q_W^b(v_*)=0`, contradicting `lambda_b^->0`.

This `a_*^-` need not coincide with Suzuki's unrestricted first threshold from `WI-238`. The unrestricted first crossing can occur in the even sector. The point is instead that **a separate finite odd threshold is forced by RH failure**, which is exactly what the odd source program needs.

## 4. The source tariff now applies to every RH failure

`WI-241` proves on odd tests the exact decomposition

\[
Q_W^a(v)=Q_{\rm mean}(v)-2\Delta_\Lambda^a(v).
\]

At fixed finite `a`, the arithmetic part is a finite sum of translation quadratic forms and the continuum comparison term is bounded; consequently this identity extends from the smooth/H1 core to the closed form domain used above. Thus for the normalized odd zero mode at `a_*^-`,

\[
\Delta_\Lambda^{a_*^-}(v_*)
=\frac12Q_{\rm mean}(v_*).
\]

`WI-246` defines the exact joint odd finite-radius reserve `beta_*(a)` and proves

\[
Q_{\rm mean}(v)\ge M(0)+\beta_*(a)
\]

for every normalized odd vector supported in `[-a,a]`. Therefore

\[
\Delta_\Lambda^{a_*^-}(v_*)
\ge\frac{M(0)+\beta_*(a_*^-)}2.
\]

This bridge removes an important logical qualifier from `WI-244`--`WI-246`. Those findings correctly described their tariff as applying to a hypothetical **odd** finite-radius zero witness and explicitly did not claim that Suzuki's unrestricted first ground-state crossing had odd parity. The present result does not force that unrestricted crossing to be odd; instead it uses Yoshida's stronger odd-test criterion to force a finite odd degeneracy independently.

The remaining theorem is therefore genuinely arithmetic and directional:

\[
\boxed{
\text{exclude, for every finite }a,\text{ an odd zero-mode source charge meeting }
\Delta_\Lambda^a(v)\ge\frac{M(0)+\beta_*(a)}2.
}
\]

A zeta-specific upper bound below that threshold on the **first odd crossing class** would prove RH. `WI-243` still forbids replacing this finite-radius directional task by a generic global subexponential bound for the signed discrepancy, because that large-radius statement is already RH-equivalent.

## 5. Prior-art and novelty audit

The prior-art boundary is unusually important here.

- **Classical theorem:** Yoshida's Proposition 1 already establishes that strict positivity on all nonzero odd compactly supported smooth tests implies RH. No novelty is claimed for the odd-test criterion.
- **Earlier continuity claim:** Bombieri's Theorem 5 (and the 2003 variational paper's corresponding theorem) states continuity for parity-restricted variational lower bounds. Suzuki 2026 explicitly describes the proof details as incomplete/delicate; this finding therefore does not present parity continuity as a newly discovered statement.
- **Modern rigorous mechanism:** Suzuki's Theorem 1.3 gives a complete fixed-domain compactness proof for the unrestricted bottom eigenvalue, and Section 4.5 identifies the parity decomposition. The exact deduction here is that every step of Sections 4.3--4.4 is stable under the odd projection, which supplies a self-contained rigorous parity-restricted proof in the same modern closed-form framework.
- **Mathia bridge:** combining that restricted continuity with Yoshida's contrapositive and `WI-246` turns the odd finite-radius source tariff from a conditional parity candidate into a necessary finite obstruction under every RH failure.

A targeted search around Bombieri's parity-restricted minima, Yoshida's odd criterion, and Suzuki's 2026 continuity theorem located the classical statement and Suzuki's explicit caveat, but no later independent proof beyond these sources. Search absence is recorded only as audit context and is not a priority claim.

## 6. Stress tests and boundaries

1. **Strict versus non-strict positivity.** Yoshida's implication uses strict positivity on every nonzero odd smooth test. Its contrapositive gives a finite odd test with `Q_W<=0`; this is exactly enough for the threshold argument. No unjustified negative sign is needed.
2. **Parity-preserving core.** The only extra step relative to Suzuki's upper-semicontinuity proof is symmetrizing the smooth approximants. Reflection invariance and vanishing even/odd cross terms make this legitimate in the shifted form norm.
3. **Prime thresholds do not create discontinuities.** Suzuki's `bar q_a^1` is jointly continuous even when `e^{2a}` crosses a prime power, because the corresponding translated-overlap term enters with zero overlap at the threshold. The odd restriction does not change this argument.
4. **The zero mode is a closed-form eigenvector.** It need not lie literally in `H_0^1`; the odd smooth class is a form core and the restricted self-adjoint operator has discrete spectrum. The source identity and finite-radius variational reserve extend by form closure.
5. **No claim about the unrestricted ground-state parity.** The small-radius unrestricted ground state is even, and the first unrestricted threshold may also be even. The theorem constructs a separate odd threshold forced by Yoshida's criterion.
6. **No arithmetic upper bound has been proved.** The result makes `WI-246` RH-facing but does not show that the actual von Mangoldt discrepancy misses the tariff. That remains the live bottleneck.
7. **No percentage improvement.** This finding concerns elimination of zero-density/individual exceptional zeros, not the existing simple-critical proportion.

## Falsification test

The bridge fails if any of the following occurs: Yoshida's odd-test implication is being applied to a different test class not dense in Suzuki's localized form; Suzuki's fixed-domain decomposition fails to preserve parity or its compactness/joint-continuity argument cannot be restricted to the closed odd subspace; the parity-projected smooth core fails to be form-dense; or the odd source decomposition/`beta_*` reserve does not extend to the attained form-domain zero mode.

Each point is explicit. The first two are stated directly in Suzuki's 2026 paper; the parity-core step follows by symmetrization under the commuting reflection; and the last step uses only bounded finite-shift terms plus the closed `H^{log}` mean form at fixed radius.

## Consequence for the research line

The finite-radius odd source program is now logically connected to the global objective without needing to guess the parity of Suzuki's unrestricted first ground state:

\[
\neg\mathrm{RH}
\Longrightarrow
\text{finite first odd degeneracy}
\Longrightarrow
\text{finite odd source charge at least }\frac{M(0)+\beta_*(a)}2.
\]

The next useful result must attack the final arrow from the arithmetic side: use the first-odd-crossing structure, exact finite prime support, or another zeta-specific invariant to prove that the signed von Mangoldt source cannot attain the required charge. Reoptimizing the same positive archimedean resolvents remains blocked at leading order by `WI-246`.