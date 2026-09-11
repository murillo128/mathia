# PL-269 — The localized Weil ground energy tends to zero if and only if RH holds

**Evidence:** `LITERATURE+DERIVED`

**Status:** `EXACT-EQUIVALENCE + ASYMPTOTIC-ORDER-PARAMETER + PRIOR-ART-COMBINATION`

## Claim

Let `Q_W^a` be Suzuki's closed completed Weil form localized to `L^2(-a,a)`, let `A_a` be its associated lower-bounded self-adjoint operator, and write

\[
\lambda_a:=\min\sigma(A_a)
=\inf_{0\ne u\in\mathfrak D(Q_W^a)}
\frac{Q_W^a(u)}{\|u\|_2^2}.
\]

Then

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\lim_{a\to\infty}\lambda_a=0.
}
\]

More precisely, the two alternatives are separated sharply:

- under RH, `PL-268` gives `lambda_a>0` for every finite `a`; `PL-266` gives monotonicity and `PL-268` sharpens it to strict decrease; Xuefeng Zhu's 2026 conditional compact-window upper bound implies

\[
0<\lambda_a\le \lambda^*(a)
\le \exp(-a e^a)
\]

for all sufficiently large `a`, where `lambda^*(a)` is Zhu's infimum over the smaller real-even test class. Hence

\[
\lambda_a\downarrow0;
\]

- if RH is false, Suzuki's localized Weil criterion gives some finite `a_0` with `lambda_(a_0)<0`. Domain monotonicity then gives

\[
\lambda_a\le\lambda_{a_0}<0
\qquad(a\ge a_0),
\]

so the monotone extended limit belongs to `[-infinity,0)` and in particular cannot equal zero. By `PL-268`, the sign change occurs at a unique finite aperture.

Thus the large-window bottom spectral edge is a scalar RH order parameter: **the RH branch approaches the positivity boundary from above, while every non-RH branch crosses it at finite radius and stays uniformly below zero thereafter.**

This is not a proof of RH and no originality is claimed for the ingredients. The line-specific delta is the exact asymptotic dichotomy obtained by combining Suzuki's localized operator/Weil criterion, the domain-order structure already isolated in `PL-266`--`PL-268`, and Zhu's conditional large-window variational upper bound. It closes the possibility that, even under RH, the localized spectral floor might converge to a positive constant.

## 1. The full localized bottom is bounded by Zhu's even-real profile

Zhu defines, for support in `[-L,L]`, the compact-window profile

\[
\lambda^*(L)
:=
\inf_{\substack{0\ne f\in L^2(\mathbb R)\\
                  f\ \mathrm{real\ and\ even}\\
                  \operatorname{supp}f\subset[-L,L]}}
\frac{Q_W(f)}{\|f\|_2^2}.
\]

Suzuki's `lambda_L` is the infimum of the same completed Weil quadratic form over the full localized form domain. Every admissible real-even test vector is therefore admissible for the full problem. Consequently

\[
\boxed{\lambda_L\le\lambda^*(L).}
\]

This one-sided comparison is all that is needed. **No equality of the two profiles is asserted.** Zhu proves parity-sector information and a simple even ground state at a certified finite scale, but the present argument does not extrapolate that finite-scale identification to arbitrary `L`.

The endpoint convention `[-L,L]` versus `(-L,L)` is immaterial in `L^2`; both constructions localize the same autocorrelation form to the same support radius. The prime-power horizon also agrees: since `supp(f*tilde f) subset [-2L,2L]`, the geometric side contains only von Mangoldt atoms with

\[
\log n<2L,
\]

which are exactly the prime-axis exponent vectors `r e_p` with `r log p<2L` in the prime-lattice coordinates.

## 2. RH forces the spectral floor to collapse to zero

Zhu's Theorem 1.3 states that, assuming RH, there is an `L_0` such that

\[
\lambda^*(L)\le\exp(-L e^L)
\qquad(L\ge L_0).
\]

The theorem is proved by an explicit variational construction using zeros up to height `2 pi e^L` and a band-limited window. It is distinct from Zhu's fitted Landau--Widom law: the stronger empirical scale involving `e^(2L)` and the fitted constant near `2 pi^2` is conjectural and is **not** used here.

On RH, Weil positivity gives `lambda_L>=0`. The strict-domain result `PL-268` improves this to

\[
\lambda_L>0
\]

for every finite `L`: a finite zero would force strict negativity at every larger aperture and contradict global Weil positivity. Combining this with the test-class comparison gives, for `L>=L_0`,

\[
0<\lambda_L
\le\lambda^*(L)
\le\exp(-L e^L).
\]

Therefore

\[
\boxed{\mathrm{RH}\Longrightarrow\lambda_L\downarrow0.}
\]

The conclusion uses only Zhu's proved conditional upper bound, not the numerical values or the conjectured asymptotic formula for `lambda^*`.

## 3. Failure of RH forces a finite crossing and excludes a zero limit

Suzuki's localized formulation gives the exact finite-window detection statement

\[
\neg\mathrm{RH}
\quad\Longleftrightarrow\quad
\lambda_{a_0}<0
\quad\text{for some finite }a_0>0.
\]

`PL-266` proves the variational domain monotonicity

\[
0<a<b\quad\Longrightarrow\quad\lambda_b\le\lambda_a.
\]

Hence once one negative window exists,

\[
\lambda_a\le\lambda_{a_0}<0
\qquad(a\ge a_0).
\]

Since a monotone real-valued function has an extended limit, one obtains

\[
\lim_{a\to\infty}\lambda_a
\in[-\infty,\lambda_{a_0}]
\subset[-\infty,0).
\]

No lower uniform semibound in `a` is needed, and no claim is made that the non-RH limit is finite. The only fact required for the equivalence is that it is separated from zero on the negative side by any one finite negative witness.

`PL-268` adds a stronger geometric description: `a mapsto lambda_a` is strictly decreasing. Together with Suzuki's continuity and small-window positivity, this means that under failure of RH there is a unique finite `a_c` such that

\[
\lambda_{a_c}=0,
\qquad
\lambda_a>0\ (a<a_c),
\qquad
\lambda_a<0\ (a>a_c).
\]

Thus the asymptotic order parameter is not hiding repeated crossings or a zero plateau.

## 4. The equivalence and its logical strength

The two directions now give

\[
\boxed{
\mathrm{RH}
\iff
\lim_{a\to\infty}\lambda_a=0.
}
\]

Equivalently, because strict decrease is already known,

\[
\mathrm{RH}
\iff
\lambda_a>0\ \text{for every finite }a
\ \text{and}\
\inf_{a>0}\lambda_a=0.
\]

The second condition is no longer an independent possibility under RH: Zhu's theorem forces it. Conversely, proving merely that the full localized spectral floor tends to zero—without first proving positivity window by window—would already imply RH, because a single negative window would make the future tail stay strictly negative.

This observation changes how large-aperture numerical or asymptotic evidence should be interpreted. Very small positive finite-window upper bounds are compatible with RH, but their decay cannot be promoted to an unconditional statement `lambda_a to 0` without crossing an RH-equivalent gate. In particular, any future source-side argument that claims unconditional collapse of the unshifted localized ground energy to zero has, whether or not phrased that way, proved RH.

## 5. Prime-lattice interpretation

Through the `PL-265` dictionary, the aperture `a` accumulates the completed arithmetic source up to prime-power energy

\[
r\log p\le2a,
\]

or equivalently exponent-axis points

\[
r e_p
\]

inside the log-energy ball. The bottom eigenvalue `lambda_a` measures the smallest Rayleigh quotient of the **completed accumulated Weil form**, not the response to one prime edge. `PL-264` shows why that distinction matters: each individual prime-power threshold has universal local spectral geometry whose arithmetic dependence has already collapsed to its von Mangoldt scalar and location.

The new asymptotic dichotomy is therefore global. On the RH branch, adding larger and larger prime-power/completion windows drives the least positive margin arbitrarily close to zero; on a non-RH branch, the same accumulated form eventually acquires a negative direction and domain nesting prevents that defect from healing. The result does not explain why the rational-prime source should choose the first branch. It only identifies the exact scalar asymptotic that distinguishes the branches.

This also passes the no-repackaging audit only in a limited sense. The equivalence is a useful spectral compression of the localized Weil criterion, but it is not an independent positivity mechanism: its hard direction still rests on the RH-conditional variational construction of Zhu. It should therefore be used as a **target and falsification boundary**, not advertised as progress toward proving the sign from prime geometry.

## 6. Prior-art and novelty audit

The load-bearing literature sources are already registered in `research/prime_lattice/SOURCES.md`.

- Source 56: **Masatoshi Suzuki, “Weil's quadratic form via the screw function,” arXiv:2606.09096v2 (2026)**. Suzuki constructs the localized closed Weil form and self-adjoint operator, identifies its lowest eigenvalue variationally, proves continuity in the support radius, and records the equivalence between RH failure and strict negativity at some finite radius.
- Source 58: **Xuefeng Zhu, “Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law,” arXiv:2608.24827v2 (2026)**. Theorem 1.3 proves, under RH, `lambda^*(L)<=exp(-L e^L)` for sufficiently large `L`. The paper explicitly distinguishes this theorem from the stronger fitted Landau--Widom asymptotic, which remains conjectural.

The domain monotonicity and strictness inputs are the stored derived results `PL-266` and `PL-268`. A repository audit found no prior `PL-*` finding stating the large-aperture equivalence `RH iff lambda_a to 0`; the nearest records concern finite negative-threshold detectability, possible plateaus, and their later exclusion.

A targeted literature search around localized Weil operators, compact-window positivity, spectral lower edges, and large-window asymptotics found Zhu's paper as the closest source but did not locate the exact full-profile limit equivalence stated above. Nevertheless the derivation is short once the ingredients are juxtaposed, so **no claim of general mathematical originality is made**. The durable value is organizational: Zhu's conditional upper bound closes a logical branch left open by the monotonicity results and turns the full localized bottom edge into an exact asymptotic RH order parameter.

## 7. Adversarial audit and falsification boundary

The derivation was checked against the main possible overstatements.

1. **Even-real versus full test space.** Zhu's `lambda^*` is an infimum over a smaller test family. The proof uses only `lambda_a<=lambda^*(a)`. It does not identify the two ground energies for arbitrary aperture.

2. **Conditional theorem versus numerical law.** Only Zhu's Theorem 1.3 is used. The empirical Landau--Widom profile, its `e^(2L)` resolution scale, and the fitted constant near `2 pi^2` are not theorem-level inputs.

3. **Analytic continuation.** No Euler product is continued into the critical strip. Suzuki's and Zhu's forms use the completed Weil explicit formula; the finite prime-power geometric sum is valid because compact support truncates it, while the zero side and completed archimedean terms belong to the analytically continued object.

4. **Non-RH limit.** The argument proves only that the extended limit is strictly negative or `-infinity`; it does not prove a finite negative limit or an asymptotic rate.

5. **No source-side positivity theorem.** The equivalence does not derive the sign from the exponent lattice. A matched translation-invariant form could share monotonicity, and Zhu's decay theorem is assumed under RH. The rational-prime selector remains the unshifted Weil positivity problem isolated by `MI-016` and `PL-264`.

6. **Strict monotonicity is not needed for the iff.** Non-strict domain monotonicity plus one negative witness already excludes a zero limit off RH. `PL-268` is used only to sharpen the branch geometry to positive finite margins under RH and a unique crossing off RH.

The finding would be falsified if Zhu's conditional upper bound did not apply to an admissible subclass of Suzuki's localized Weil form under the same support normalization, or if Suzuki's negative-window criterion/domain nesting failed for the full form. The inspected formulations supply exactly these hypotheses.

## Consequence for the research line

The large-aperture scalar target is now exact:

\[
\text{prove }\lambda_a\to0\text{ unconditionally}
\quad\Longleftrightarrow\quad
\text{prove RH}.
\]

Accordingly, future work should not treat asymptotic collapse of the unshifted localized bottom eigenvalue as a weaker surrogate objective. A genuine advance must explain **why the completed rational-prime source stays on the positive branch for every finite aperture**, or provide an independent arithmetic mechanism forcing the same conclusion. Quantitative study of the conditional positive branch—decay rate, eigenvector shape, finite-core approximation, or relation to the expanding-window transform gate of `PL-262`—can still be useful, but any unconditional zero-limit theorem is already the target theorem itself.