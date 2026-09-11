# PL-269 — The localized Weil ground energy tends to zero if and only if RH holds

**Evidence:** `LITERATURE+DERIVED`

**Status:** `EXACT-EQUIVALENCE + ASYMPTOTIC-ORDER-PARAMETER + PRIOR-ART-COMBINATION`

## Claim

Let `Q_W^a` be Suzuki's completed Weil form localized to `L^2(-a,a)`, let `A_a` be its associated lower-bounded self-adjoint operator, and set

\[
\lambda_a:=\min\sigma(A_a)
=\inf_{0\ne u\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(u)}{\|u\|_2^2}.
\]

Then

\[
\boxed{\mathrm{RH}\iff\lim_{a\to\infty}\lambda_a=0.}
\]

The alternatives are sharper than this bare equivalence. Under RH, `lambda_a` is strictly positive at every finite aperture and decreases to zero. If RH is false, it crosses zero at one finite aperture and stays strictly negative thereafter; its extended limit lies in `[-infinity,0)`. Thus the large-window lower spectral edge is a scalar RH order parameter.

This is not an RH proof. It combines Suzuki's localized Weil criterion, the monotonicity/strictness already isolated in `PL-266` and `PL-268`, and Xuefeng Zhu's 2026 conditional large-window upper bound. The useful delta is that the RH branch can no longer have a positive limiting spectral gap.

## 1. Zhu's profile is an admissible upper bound for the full localized problem

Zhu defines the compact-window profile over the smaller real-even test family

\[
\lambda^*(L):=
\inf_{\substack{0\ne f\in L^2(\mathbb R)\\
f\ \mathrm{real\ and\ even}\\
\operatorname{supp}f\subset[-L,L]}}
\frac{Q_W(f)}{\|f\|_2^2}.
\]

Suzuki's `lambda_L` takes the infimum of the same completed Weil quadratic form over the full localized form domain. Hence every Zhu trial vector is admissible for Suzuki's problem and

\[
\boxed{\lambda_L\le\lambda^*(L).}
\]

No equality of the two profiles is asserted. Zhu proves parity information and a simple even ground state at a certified finite scale, but that finite-scale statement is not extrapolated here to arbitrary `L`.

The support normalizations match for this comparison: `[-L,L]` and `(-L,L)` differ only at null endpoints in `L^2`. Moreover `supp(f*\widetilde f)\subset[-2L,2L]`, so the geometric explicit formula contains only prime powers with `log n<2L`. In exponent coordinates these are precisely the axis points `r e_p` with `r log p<2L`.

## 2. Under RH the ground energy collapses to zero

Zhu's Theorem 1.3 states that, assuming RH, there is `L_0` such that

\[
\lambda^*(L)\le\exp(-L e^L)
\qquad(L\ge L_0).
\]

This is a proved conditional variational bound. It must be kept separate from the stronger fitted Landau--Widom law in the same paper: the measured `e^(2L)` resolution scale and fitted constant near `2 pi^2` remain conjectural and are not used here.

On RH, Weil positivity gives `lambda_L>=0`. `PL-268` strengthens this to strict positivity at every finite radius: if `lambda_L=0` at one finite `L`, strict domain monotonicity would force negativity for every larger aperture, contradicting Weil positivity. Therefore, for all sufficiently large `L`,

\[
0<\lambda_L\le\lambda^*(L)\le\exp(-L e^L),
\]

and hence

\[
\boxed{\mathrm{RH}\Longrightarrow\lambda_L\downarrow0.}
\]

This closes the positive-limit possibility left open by monotonicity alone.

## 3. Off RH a finite negative witness prevents a zero limit

Suzuki's localized formulation gives

\[
\neg\mathrm{RH}
\quad\Longleftrightarrow\quad
\lambda_{a_0}<0
\quad\text{for some finite }a_0>0.
\]

`PL-266` gives domain monotonicity,

\[
0<a<b\quad\Longrightarrow\quad\lambda_b\le\lambda_a.
\]

Consequently, after any negative witness,

\[
\lambda_a\le\lambda_{a_0}<0
\qquad(a\ge a_0).
\]

The monotone extended limit therefore exists and satisfies

\[
\lim_{a\to\infty}\lambda_a
\in[-\infty,\lambda_{a_0}]
\subset[-\infty,0).
\]

No uniform lower semibound as `a` varies is required, and no claim is made that the off-RH limit is finite. `PL-268` adds that the decrease is strict, so continuity and small-window positivity give a unique finite crossing radius `a_c` with positive values to its left and negative values to its right.

Combining the two branches proves the claimed equivalence

\[
\boxed{\mathrm{RH}\iff\lim_{a\to\infty}\lambda_a=0.}
\]

In particular, an unconditional theorem proving only `lambda_a -> 0`, without separately proving finite-window positivity, would already prove RH: one negative window would force the entire later tail to remain bounded away from zero on the negative side.

## 4. Prime-lattice meaning and limitation

Through the `PL-265` dictionary, increasing `a` accumulates the completed arithmetic source through prime-power energy `r log p<=2a`, equivalently through exponent-axis points `r e_p` in the growing log-energy ball. The scalar `lambda_a` is the least Rayleigh quotient of the full accumulated completed Weil form, not the response to one prime edge.

That distinction is essential after `PL-264`: every individual prime-power threshold has universal local singular geometry whose arithmetic dependence has already collapsed to its von Mangoldt weight and location. The present dichotomy is genuinely global in aperture. On the RH branch, the completed accumulated form remains positive but its least margin tends to zero; off RH, it acquires a negative direction at finite aperture and nesting prevents that defect from healing.

This does not explain why the rational-prime source selects the RH branch. It is an exact spectral compression of the localized Weil criterion, not an independent sign mechanism. It should therefore be used as a target and falsification boundary rather than advertised as evidence that the prime lattice itself proves positivity.

## 5. Prior-art and novelty audit

The load-bearing sources are already registered in `research/prime_lattice/SOURCES.md`.

- Source 56: **Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2 (2026)**. Suzuki constructs the localized closed Weil form/operator, identifies its lowest eigenvalue variationally, proves continuity in aperture, and records that failure of RH is equivalent to strict negativity at some finite radius.
- Source 58: **Xuefeng Zhu, “Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law,” arXiv:2608.24827v2 (2026)**. Theorem 1.3 proves under RH that `lambda^*(L)<=exp(-L e^L)` for all sufficiently large `L`. Zhu explicitly distinguishes this theorem from the stronger empirical Landau--Widom asymptotic.

The order inputs are the stored derived results `PL-266` and `PL-268`. A repository audit found no earlier `PL-*` finding stating the large-aperture limit equivalence; the nearest findings concern finite negative-threshold detectability, possible plateaus, and their later exclusion. A targeted literature search around localized Weil spectral floors and compact-window asymptotics found Zhu's paper as the closest source but did not locate this exact full-profile limit formulation.

No general originality is claimed: once the cited ingredients are juxtaposed, the proof is short. The durable line-specific value is that Zhu's conditional upper bound removes a real logical branch and identifies the asymptotic bottom edge as an exact RH order parameter.

## 6. Adversarial audit and falsification boundary

The main failure modes were checked explicitly.

1. **Test-space mismatch.** Zhu's `lambda^*` is over a smaller real-even family. Only the safe inequality `lambda_a<=lambda^*(a)` is used; equality is never assumed.
2. **Theorem versus fit.** Only Zhu's conditional Theorem 1.3 enters. None of the fitted Landau--Widom constants or numerical decay laws are promoted to theorem status.
3. **Analytic continuation.** No Euler product is continued into the strip. Both constructions use the completed Weil explicit formula; compact support makes the geometric prime-power sum finite.
4. **Off-RH asymptotics.** The conclusion is only that the extended limit is strictly negative or `-infinity`; no finite limiting value or rate is asserted.
5. **No arithmetic sign theorem.** Monotonicity and translation geometry are not rational-prime selectors. The unresolved burden remains the global unshifted Weil sign isolated by `MI-016` and `PL-264`.
6. **Strictness is auxiliary to the iff.** Non-strict monotonicity plus one finite negative witness already excludes a zero limit off RH. `PL-268` sharpens the geometry to strict positive finite margins under RH and a unique crossing off RH.

The finding would fail if Zhu's conditional variational profile were not an admissible subclass of Suzuki's localized Weil form under the same support normalization, or if Suzuki's finite negative-window criterion/domain nesting failed. The inspected formulations supply exactly those hypotheses.

## Consequence for the research line

The large-aperture scalar objective is no longer a weaker surrogate:

\[
\text{prove }\lambda_a\to0\text{ unconditionally}
\quad\Longleftrightarrow\quad
\text{prove RH}.
\]

Future work should therefore concentrate on the missing source-side theorem: why the completed rational-prime Weil form stays on the positive branch for every finite aperture. Conditional study of the positive branch—decay rates, eigenvector structure, finite-core approximation, or interaction with the expanding-window transform gate of `PL-262`—can still sharpen the geometry, but an unconditional zero-limit theorem is already the target theorem itself.