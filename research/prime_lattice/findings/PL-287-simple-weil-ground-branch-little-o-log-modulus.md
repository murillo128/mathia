# PL-287 — A simple localized Weil ground branch automatically beats the sharp ambient inverse-log modulus

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-TOPOLOGY-REFINEMENT + ROUTE-NARROWING`

**Status:** `SIMPLE-BRANCH-HLOG-COMPACTNESS + LITTLE-O-LOG-TRANSPORT + NONQUANTITATIVE`

## Claim

`PL-285`--`PL-286` show that on a source-static aperture interval the localized Weil prime comb has the sharp worst-case form modulus

\[
\Theta\!\left(\frac1{\log(1/|a-b|)}\right)
\]

on the full unit ball of the canonical logarithmic form space. That worst-case scale is **not attained uniformly by any compact family of actual states in the logarithmic form topology**. More precisely, let

\[
E_{\log}(w)=\int_{\mathbb R}\log(2+|\xi|)|\widehat w(\xi)|^2\,d\xi
\]

for the zero extension of `w` from `I=(-1,1)`, and let `K` be compact in `H^log(I)`. For every fixed interior lag `h` and

\[
q_h(w)=\langle T_h w,w\rangle,
\]

one has the uniform strict improvement

\[
\boxed{
\sup_{w\in K}
|q_{h+\delta}(w)-q_h(w)|
=
o\!\left(\frac1{\log(1/|\delta|)}\right)
\qquad(\delta\to0).
}
\]

The same conclusion holds for any finite source-static prime-power comb whose lags move smoothly with the aperture.

At `a0=0.8`, `PL-284` records a certified simple even ground state separated from the rest of the spectrum. Combining that isolation with the common fixed-domain form decomposition used by Suzuki and the form-continuity estimate of `PL-285`, the normalized ground state can be chosen, on some source-static neighborhood of `a0`, as an `H^log`-continuous branch. Its image on every sufficiently small closed neighborhood is therefore `H^log`-compact. The min--max principle then gives

\[
\boxed{
|\lambda_1(a)-\lambda_1(b)|
=
o\!\left(\frac1{\log(1/|a-b|)}\right)
}
\]

for `a,b -> a0` inside that neighborhood. Thus the `Theta(1/log)` obstruction of `PL-286` is genuinely an **ambient moving-wave-packet obstruction**, not the asymptotic modulus of the isolated low branch itself.

This is a qualitative improvement only. It supplies no computable transport radius from the tiny certified margin at `a=0.8` to the next prime-power activation at `log(5)/2`. The surviving problem is now sharper: one needs a **quantitative uniform logarithmic-tail estimate for the actual ground branch**, or a stronger source-specific identity, rather than merely proving that the branch is qualitatively more regular than the worst-case `H^log` ball.

## 1. Fixed-state little-o improvement

For zero-extended `w`, Plancherel gives exactly

\[
q_{h+\delta}(w)-q_h(w)
=
\int_{\mathbb R}e^{ih\xi}(e^{i\delta\xi}-1)|\widehat w(\xi)|^2\,d\xi.
\]

Write

\[
L_\delta=\log(1/|\delta|)
\]

and split at

\[
R_\delta=|\delta|^{-1/2}.
\]

On `|xi|<=R_delta`,

\[
|e^{i\delta\xi}-1|\le |\delta\xi|\le |\delta|^{1/2},
\]

so the low-frequency contribution is at most

\[
|\delta|^{1/2}\|w\|_2^2.
\]

On `|xi|>R_delta`, the multiplier is at most `2`, while

\[
\log(2+|\xi|)\ge \frac12L_\delta+O(1).
\]

Hence

\[
|q_{h+\delta}(w)-q_h(w)|
\le
|\delta|^{1/2}\|w\|_2^2
+
\frac{4+o(1)}{L_\delta}
\eta_w(R_\delta),
\]

where

\[
\eta_w(R)=
\int_{|\xi|>R}\log(2+|\xi|)|\widehat w(\xi)|^2\,d\xi.
\]

For every fixed `w in H^log`, `eta_w(R)->0`; therefore

\[
L_\delta |q_{h+\delta}(w)-q_h(w)|\to0.
\]

This does not contradict the sharp lower bound in `PL-285`: its saturating wave packets depend on `delta` and move their Fourier mass to frequency `~1/delta`. No single fixed `H^log` state can follow that escape indefinitely.

## 2. Compact `H^log` families exclude the escaping witnesses uniformly

If `K` is compact in `H^log(I)`, then its Fourier images are compact in the weighted space

\[
L^2\bigl(\log(2+|\xi|)d\xi\bigr).
\]

Compactness implies uniform tail tightness:

\[
\eta_K(R):=
\sup_{w\in K}
\int_{|\xi|>R}\log(2+|\xi|)|\widehat w(\xi)|^2\,d\xi
\longrightarrow0.
\]

The preceding split is therefore uniform on `K`:

\[
\sup_{w\in K}|q_{h+\delta}(w)-q_h(w)|
\le
|\delta|^{1/2}\sup_{w\in K}\|w\|_2^2
+
\frac{4+o(1)}{L_\delta}\eta_K(R_\delta).
\]

Multiplication by `L_delta` sends the first term to zero and the second to zero by uniform tail tightness. This proves the boxed compact-family little-o statement.

For a fixed finite active set `S` of prime powers, Suzuki's scaled formula has lags

\[
h_n(a)=\frac{\log n}{a},\qquad n\in S.
\]

On a compact source-static interval,

\[
h_n(b)-h_n(a)=O(|a-b|),
\]

and therefore

\[
\log\frac1{|h_n(b)-h_n(a)|}
=
\log\frac1{|a-b|}+O(1).
\]

Summing finitely many channels preserves the uniform `o(1/log(1/|a-b|))` modulus on every `H^log`-compact family. The remaining terms in Suzuki's fixed-domain formula are `-log a` and integral forms with kernels depending smoothly on `a` on a source-static compact interval, hence contribute an ordinary `O(|a-b|)` modulus and are asymptotically smaller than `1/log(1/|a-b|)`.

## 3. Why the simple ground branch is `H^log`-compact locally

Source 56, Masatoshi Suzuki's *Weil's quadratic form via the screw function*, scales the localized problem to `I=(-1,1)` and decomposes the closed form as

\[
\bar q_a=\bar q_0+\bar q^1_a,
\]

where `q_0` is `a`-independent and its shifted form norm is equivalent to the `H^log` norm, while `q^1_a` is a finite sum of compressed-translation forms and continuous-kernel forms. Suzuki proves that normalized ground minimizers in a compact aperture neighborhood are uniformly bounded in `H^log`, relatively compact in `L^2`, and that

\[
\bar q^1_{a_j}(w_j)\to \bar q^1_{a_0}(w_*)
\]

whenever `a_j->a0` and the relevant minimizing subsequence converges in `L^2`.

At `a0=0.8`, `PL-284` supplies the additional ingredient absent from Suzuki's general continuity argument: the ground state is certified simple and isolated. `PL-285` gives common-domain form convergence of the moving prime channels, so the isolated eigenvalue and its one-dimensional spectral projection persist on a sufficiently small source-static neighborhood. Choose the normalized ground vector continuously in `L^2` there (with a fixed phase/sign convention).

Now let `a_j->a0` and write `w_j=w_{a_j}`. Simplicity identifies every `L^2` cluster point with `w_0`. Since

\[
\lambda_1(a_j)=\bar q_0(w_j)+\bar q^1_{a_j}(w_j)
\]

and both `lambda_1(a_j)->lambda_1(a0)` and the bounded part converges, one obtains

\[
\bar q_0(w_j)\to\bar q_0(w_0).
\]

For a closed lower-bounded quadratic form, strong `L^2` convergence together with convergence of the shifted form energies implies convergence in the form norm. Hence

\[
w_{a_j}\to w_{a_0}
\quad\text{in }H^\log(I).
\]

The same argument applies at every point of the local simple branch, so the branch is `H^log`-continuous. A continuous image of a compact aperture interval is compact in `H^log`, exactly the hypothesis of Section 2.

## 4. Variational transfer to the lowest eigenvalue

For normalized ground states `w_a,w_b`, the min--max principle gives the two one-sided inequalities

\[
\lambda_1(b)-\lambda_1(a)
\le
(\bar q_b-\bar q_a)(w_a),
\]

and

\[
\lambda_1(a)-\lambda_1(b)
\le
(\bar q_a-\bar q_b)(w_b).
\]

On a sufficiently small closed neighborhood of `a0=0.8`, the family `{w_a}` is `H^log`-compact. Section 2 applies uniformly to the finite active comb `{2,3,4}`, while the non-atomic aperture terms are smoother. Therefore both right-hand sides are

\[
o\!\left(\frac1{\log(1/|a-b|)}\right),
\]

which proves the local little-o modulus for `lambda_1`.

The result is intentionally nonquantitative. Compactness supplies only

\[
\eta_K(R)\to0
\]

with no usable numerical decay law. A family may have an arbitrarily slow common weighted-tail decay while remaining compact. Consequently this argument cannot turn the `8.9e-18` certified margin into a practical aperture increment, much less reach the next source event at

\[
\frac{\log5}{2}-0.8\approx4.7189562\times10^{-3}.
\]

## Prior-art and novelty audit

The external load-bearing operator facts are already present in source 56 of `research/prime_lattice/SOURCES.md`: Suzuki's fixed-domain scaling, the `H^log` form, compact embedding, decomposition into an `a`-independent logarithmic part plus bounded translation/kernel terms, and continuity of the lowest eigenvalue. Source 58, already audited by `PL-283`--`PL-284`, supplies the certified simple-even ground state and spectral separation at `a=0.8`.

The abstract facts used here are standard: weighted `L^2` compact sets have uniformly tight weighted tails; common-domain form convergence preserves an isolated simple spectral projection; and convergence of a closed-form energy plus strong Hilbert-space convergence yields form-norm convergence. No novelty is claimed for those general principles.

The durable line-specific delta is their combination with the exact sharpness mechanism of `PL-285`--`PL-286`. Those findings establish that the full `H^log` ball really has a `Theta(1/log)` aperture modulus because the witness changes with the aperture increment. The present argument proves that such moving witnesses cannot lie in a compact actual low-state branch, so the isolated localized-Weil ground state automatically has a strictly smaller asymptotic modulus. A targeted audit did not identify this compact-branch refinement in Suzuki or in the source-58 window analysis; search absence is not treated as evidence of novelty.

## Adversarial boundary checks

1. **No Sobolev regularity is inferred.** The conclusion uses only `H^log` compactness. It does not assert that the ground state belongs to any positive-order Sobolev space, has a power-law Fourier tail, or satisfies a differentiable aperture law.
2. **Little-o is not a rate.** It may be arbitrarily slow. The finding does not claim an explicit positive transport radius or continuation to `log(5)/2`.
3. **Simplicity matters for the branch statement.** The compact-family Fourier lemma is unconditional, but identifying one continuous ground branch near `0.8` uses the certified simple isolated eigenvalue from `PL-284` and persistence under the common-form perturbation.
4. **The sharp ambient lower bound remains correct.** `PL-286` uses `delta`-dependent high-frequency wave packets. Compactness excludes precisely that moving escape; it does not improve the operator/form norm on the whole `H^log` ball.
5. **The mechanism is not zeta-specific.** Any simple isolated eigenbranch of a matched finite-comb model with the same logarithmic principal form enjoys the same qualitative improvement. Thus this is a topology/branch-selection refinement, not an RH-rigidity theorem.

## Consequence for the research line

The immediate target after `PL-286` can be narrowed. It is no longer necessary to ask first whether the true low branch beats the ambient inverse-log modulus qualitatively: **it must** near the certified simple base point. What remains is quantitative and source-specific.

A useful next theorem would have to bound the compact-branch tail function

\[
\eta_{\mathrm{gs}}(R)
=
\sup_{a\in J_0}
\int_{|\xi|>R}\log(2+|\xi|)|\widehat w_a(\xi)|^2\,d\xi
\]

on an explicit source-static interval `J0` around `0.8`, or replace that tail bound by an exact eigen-equation cancellation. Any such estimate immediately feeds the explicit split in Section 1 and converts state-specific information into a certified aperture modulus. Generic prime-frequency cancellation and generic `H^log` regularity have already been exhausted; the remaining question is the **quantitative high-frequency tightness of the actual ground branch**.
