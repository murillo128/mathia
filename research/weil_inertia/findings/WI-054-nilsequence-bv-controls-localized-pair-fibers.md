# WI-054 — nilsequence Bombieri--Vinogradov controls the localized pair-frequency fiber on its power-modulus range

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + CORRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It corrects one boundary statement in WI-053: Shao--Teräväinen's modulus-averaged nilsequence Bombieri--Vinogradov theorem is stronger at the Yang interface than “one coherent mode at a time.” Because Theorem 1.3 takes a **supremum over all bounded-complexity nilsequences for each modulus**, it gives a modulus-wise uniform bound for every linear Fourier frequency simultaneously. Once that bound is inserted into the exact localized fiber formula of WI-051, Parseval converts it into an `ell^2` bound for the whole pair-frequency fiber.

Consequently the many-frequency objection in WI-053 §6 is not valid for a Yang pair containing one Shao--Teräväinen-controlled prime residual: the pair spectrum has product structure, and

\[
\|A_r^{\mathrm{res}}\|_{\ell^2}
\le \delta_r\,\|h_r\|_2,
\]

where `delta_r` is the progression-normalized maximal twisted prime discrepancy. A second Cauchy--Schwarz step then controls the **entire locked sum over frequencies**, not merely one selected mode. After Mertens weighting, Theorem 1.3 makes this `o(1)` with arbitrary logarithmic room for every modulus range `r <= M^(1/4-epsilon)`.

Applied on both coefficient sides, this removes the analytic nonzero-fiber obstruction on a genuine positive-power Yang subregion. If

\[
r=X^\alpha,
\qquad q=X^\beta,
\]

then the physical prime lengths from WI-051 are `M_m asymp X/q` and `M_n asymp X/r`; with fixed margins, the Shao--Teräväinen range on both sides is

\[
\boxed{
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1.
}
\]

This extends the rigorously controlled analytic region beyond every fixed polylogarithmic coefficient range. It does **not** by itself finish the Yang welding theorem: the deterministic `W`-local all-main term still has to be matched source-faithfully to WI-049's genuine four-form local model, and source boundary/collision bookings remain separate. The durable redirection is narrower: any surviving post-local-main analytic obstruction must lie outside the doubly-small power-modulus region, or in that deterministic/main-term splice or the already separated boundary/collision interface.

## 1. Primary theorem and exact normalization

The load-bearing source is

Xuancheng Shao and Joni Teräväinen,
**The Bombieri--Vinogradov theorem for nilsequences**, *Discrete Analysis* 2021:21, 55 pp., DOI `10.19086/da.29048`, arXiv:2006.05954v2.

Their Theorem 1.3 states that for every fixed nilsequence degree/complexity and every fixed `A`, `Delta` and `epsilon in (0,1/4)`,

\[
\sum_{d\le x^{1/4-\varepsilon}}
\max_{(c,d)=1}
\sup_{\psi\in\Psi_s(\Delta,\log x)}
\left|
\sum_{\substack{n\le x\\n\equiv c\pmod d}}
\Lambda(n)\psi(n)
-
\frac{dW}{\varphi(dW)}
\sum_{\substack{n\le x\\(n,W)=1\\n\equiv c\pmod d}}
\psi(n)
\right|
\ll_{s,A,\Delta,\varepsilon}
\frac{x}{(\log x)^A},
\tag{1}
\]

with `W=P((log x)^C)` for a source constant `C`. Crucially, the supremum over `psi` sits **inside** the modulus sum. Linear phases are degree-one nilsequences, so after an irrelevant fixed normalization of the Lipschitz test function (1) controls

\[
\sup_{\theta\in\mathbb R/\mathbb Z}
\left|
\sum_{\substack{n\le x\\n\equiv c\pmod d}}
 e_d(n;\theta)
\right|
\tag{2}
\]

for the von-Mangoldt residual from the explicit `W`-local main, uniformly in the phase `theta` and residue class `c`. The phase may depend on `d`; this is why the `1/4-epsilon` theorem, rather than the fixed-nilsequence `1/3-epsilon` Theorem 1.4, is the source-faithful input here.

For a modulus `r` and physical prime-variable length `M`, let `E_r(M)` be the maximum discrepancy in (1), and normalize by the natural number `M/r` of progression points:

\[
\boxed{
\delta_r(M):=\frac rM E_r(M).
}
\tag{3}
\]

Then, for prime moduli `r<=R<=M^(1/4-epsilon)`, the Mertens weight used in the Yang coefficient ledger gives exactly

\[
\begin{aligned}
\sum_{r\le R\atop r\ {\rm prime}}
\frac{\log r}{r}\,\delta_r(M)
&=
\frac1M
\sum_{r\le R\atop r\ {\rm prime}}
(\log r)E_r(M)\\
&\le
\frac{\log R}{M}
\sum_{d\le R}E_d(M)\\
&\ll_A (\log M)^{1-A}.
\end{aligned}
\tag{4}
\]

Because `A` is arbitrary, (4) absorbs any fixed polylogarithmic loss from the remaining prime legs, endpoint decomposition, or the companion coefficient ledger. The same argument works with lighter `1/r` weights. For source intervals whose endpoints are comparable to `M`, two prefix applications of (1) have the same strength; the resulting difference of the two explicit `W`-local mains is deterministic and belongs to the main-term splice rather than the analytic residual.

## 2. The exact WI-051 fiber is an average of AP pair spectra

WI-051 works on the source-faithful local groups

\[
G_m=\mathbb Z/(rL)\mathbb Z,
\qquad
G_n=\mathbb Z/(qL)\mathbb Z,
\qquad
G_k=\mathbb Z/L\mathbb Z,
\tag{5}
\]

and derives

\[
\Lambda_{r,q,L}^{\rm loc}
=
\sum_{t\bmod L}A_r(t)A_q(-t),
\tag{6}
\]

with

\[
A_r(t)
=
\sum_{\substack{a\bmod rL\\a\equiv t\pmod L}}
\widehat f_1(-a)\widehat f_2(a).
\tag{7}
\]

There is an equivalent residue-class formula which makes the Shao--Teräväinen interface explicit. For `c mod r`, put

\[
f_{i,c}(u):=f_i(c+ru),
\qquad u\in\mathbb Z/L\mathbb Z,
\tag{8}
\]

and use normalized Fourier transform on `Z/LZ`. Fourier inversion on `Z/(rL)Z` gives

\[
\widehat{f_{i,c}}(t)
=
\sum_{\substack{a\bmod rL\\a\equiv t\pmod L}}
\widehat f_i(a)e_{rL}(ac).
\tag{9}
\]

Averaging the product over the `r` residue classes kills every cross-term except opposite ambient frequencies, and therefore

\[
\boxed{
A_r(t)
=
\mathbb E_{c\bmod r}
\widehat{f_{1,c}}(-t)
\widehat{f_{2,c}}(t).
}
\tag{10}
\]

Equation (10) is exact. It shows that the fiber cardinality `r` in WI-051 is not an arbitrary collection of unrelated coefficients: it is the residue-average of ordinary pair spectra on the natural AP coordinate.

## 3. Uniform phase control plus Parseval bounds the whole pair fiber

Split one AP leg into the Shao--Teräväinen local model plus residual,

\[
f_{1,c}=m_{r,c}+e_{r,c},
\tag{11}
\]

and consider the part of (10) containing `e_{r,c}`. After normalization to the AP length, Theorem 1.3 gives, modulus by modulus,

\[
\max_c\sup_t
|\widehat e_{r,c}(t)|
\le \delta_r
\tag{12}
\]

for the corresponding interval residual, up to fixed endpoint/main bookkeeping already described in §1. Define

\[
A_r^{e,h}(t)
:=
\mathbb E_c
\widehat e_{r,c}(-t)
\widehat h_{r,c}(t).
\tag{13}
\]

By Cauchy--Schwarz in the residue variable,

\[
|A_r^{e,h}(t)|^2
\le
\delta_r^2
\mathbb E_c|\widehat h_{r,c}(t)|^2.
\tag{14}
\]

Summing over **all** frequencies and using Parseval on every AP coordinate gives

\[
\boxed{
\sum_t|A_r^{e,h}(t)|^2
\le
\delta_r^2
\mathbb E_c\mathbb E_u|h_{r,c}(u)|^2.
}
\tag{15}
\]

This is the missing square-function inequality that WI-053 treated as an additional theorem-level input. No new prime theorem is required: (15) is an elementary consequence of the source's modulus-wise `sup_psi` together with the exact fiber structure and Parseval.

The distinction from the generic warning in WI-053 is important. It is true that a vector can have many individually small coordinates and still have large `ell^2` energy. Here, however, the pair fiber is a **product** of the uniformly small residual Fourier coefficient with a second spectrum. Parseval budgets the latter spectrum, so the number of frequencies never appears.

## 4. One controlled residual leg bounds the complete locked frequency sum

Let the opposite pair fiber be

\[
B_q(t)
=
\mathbb E_d
\widehat g_{q,d}(-t)
\widehat j_{q,d}(t).
\tag{16}
\]

The same elementary inequalities give a crude but sufficient bound

\[
\|B_q\|_{\ell^2}
\le
\left(\max_d\mathbb E|g_{q,d}|\right)
\left(\mathbb E_d\mathbb E|j_{q,d}|^2\right)^{1/2}.
\tag{17}
\]

For von Mangoldt functions and the explicit `W`-local approximants, the completely trivial pointwise estimate already makes the right-hand side `log^{O(1)} X`; no delicate second-moment theorem is needed. Combining (15), (17), and Cauchy--Schwarz in `t` yields

\[
\boxed{
\left|
\sum_t A_r^{e,h}(t)B_q(-t)
\right|
\ll
\delta_r\,\log^{O(1)}X.
}
\tag{18}
\]

Thus **one** Shao--Teräväinen-controlled residual leg kills the entire nonzero-frequency sum attached to that mixed term. There is no factor `L`, `r`, `q`, or number-of-frequencies penalty.

After the Yang Mertens weighting in `r`, equation (4) and arbitrary choice of the logarithmic exponent `A` make the aggregate of (18) `o(1)`, even after a fixed polylogarithmic loss from summing the companion coefficient and source partitions.

## 5. A doubly-small power region has no remaining analytic fiber obstruction

On the dominant coprime coefficient family, WI-051 identifies

\[
M_m\asymp \frac Xq,
\qquad
M_n\asymp \frac Xr,
\qquad
K\asymp \frac X{rq}.
\tag{19}
\]

Suppose, with fixed margins,

\[
r\le M_m^{1/4-\varepsilon},
\qquad
q\le M_n^{1/4-\varepsilon}.
\tag{20}
\]

Expand each of the four prime legs into its Shao--Teräväinen `W`-local model plus residual. There are sixteen terms. Every term except the all-main term contains at least one residual leg; if that residual is on the `m` pair use (18) with modulus `r`, and if it is on the `n` pair use the symmetric estimate with modulus `q`. Since both inequalities in (20) hold, all fifteen mixed/residual terms are `o(1)` after the source Mertens aggregation.

Writing

\[
r=X^\alpha,
\qquad q=X^\beta,
\tag{21}
\]

and inserting (19), the endpoint of (20) is

\[
\alpha<\frac{1-\beta}{4},
\qquad
\beta<\frac{1-\alpha}{4}.
\tag{22}
\]

Equivalently, away from the endpoints by a fixed margin,

\[
\boxed{
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1.
}
\tag{23}
\]

This is a genuine positive-power region; in particular it strictly extends the fixed-polylogarithmic domain closed by WI-050. It also lies well inside the long-shift bulk, so it is disjoint from the short-shift boundary that the clue already books separately.

What remains in this region after the analytic residuals are removed is the **all-main deterministic term**. The Shao--Teräväinen model is a `W`-local coprimality model, whereas WI-049 centers the genuine four-form Hardy--Littlewood local factor and controls its full Euler passage. Their local factors are designed to represent the same small-prime obstruction, and WI-049 supplies the relevant CRT centering machinery, but an end-to-end Yang proof must still check the exact source normalization when these two decompositions are spliced. This finding deliberately does not promote that finite local-factor bookkeeping to a theorem without writing it out.

Therefore the rigorous conclusion is

\[
\boxed{
\text{the nonzero Fourier/pair-fiber analytic residual is controlled on (23);}
}
\tag{24}
\]

not that the whole Yang welding theorem is already proved there.

## 6. Correction to WI-053 and new live boundary

WI-053 remains correct in its main negative conclusion about the 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen AP-maximal short-interval theorem: its black-box error is ambient-normalized and leaves a factor `r` on a progression of step `r`. Its fixed-coefficient generalized-von-Neumann boundary also remains unchanged.

The part superseded by the present finding is WI-053 §6's assertion that Shao--Teräväinen Theorem 1.3 only controls individual coherent modes and therefore cannot imply a pair-fiber square-function estimate. The theorem's **modulus-wise supremum over all phases**, together with the multiplicative form (10), gives exactly such a square-function estimate through (15). No contradiction with WI-051's generic quotient witness is involved: WI-051 is an information-theoretic obstruction for arbitrary bounded functions, while Theorem 1.3 supplies prime-specific, modulus-averaged Fourier uniformity strong enough to rule out that behavior on (20).

The live arithmetic region is therefore narrower than the current clue text states. For fixed power exponents, a leading post-local-main analytic covariance must now come from at least one side violating the Shao--Teräväinen density-normalized range,

\[
4\alpha+\beta\ge1
\qquad\text{or}\qquad
\alpha+4\beta\ge1,
\tag{25}
\]

apart from the deterministic `W`-main/full-local-main splice and separately booked collision/boundary terms. A one-sided extension may be possible by combining (18) on the small-modulus side with MRT control of the all-main pair against the large-modulus side, but that mixed theorem is **not** established here.

## 7. Prior-art and novelty audit

The analytic ingredients are established or classical:

- Shao--Teräväinen 2021, Theorem 1.3, is the sole prime-distribution theorem used in the new power-modulus estimate. The exact `1/4-epsilon` range, `max_c`, and modulus-wise `sup_psi` are source hypotheses, not Mathia claims.
- The same paper's Theorem 2.7 already derives finite-complexity linear-equation asymptotics for almost all **single common** arithmetic-progression moduli up to its corresponding power range, and Theorem 2.9 derives Gowers uniformity in almost all large progressions. These results confirm that using nilsequence Bombieri--Vinogradov as a transference input is established prior art; they do not directly treat the Yang two-modulus anisotropic system.
- Pierre-Yves Bienvenu, Xuancheng Shao and Joni Teräväinen, **A transference principle for systems of linear equations, and applications to almost twin primes**, *Algebra & Number Theory* 17 (2023), 497--539, DOI `10.2140/ant.2023.17.497`, is broader prior art for converting nilsequence pseudorandomness into finite-complexity configuration control. No claim is made that its printed hypotheses directly imply the Yang two-modulus statement.
- Fourier inversion, Cauchy--Schwarz and Parseval in (9)--(18) are classical identities.

No novelty or priority is claimed for any of these theorems or inequalities in isolation. The durable Mathia contribution is the **interface correction**: identify the exact residue-class representation of WI-051's aliasing fiber, notice that Shao--Teräväinen controls the maximum over all linear phases for each modulus before averaging the moduli, and use Parseval to eliminate the frequency-count loss. A bounded search did not locate the Yang-specific two-modulus deduction (23)--(24) in prior art; absence from that search is not a priority claim.

## 8. Evidence boundary and falsifiers

This finding establishes a source-backed analytic mechanism, not a new simple-zero percentage.

It would be falsified or require narrowing if any of the following source-interface checks fails:

1. the Yang normalized coefficient ledger does not permit the Mertens-weighted use of (4) after the exact source weights are restored;
2. source interval/lock masks introduce a non-polylogarithmic Fourier or endpoint loss not represented in WI-051's localized fiber formulation;
3. the `W`-local residual required in (12) cannot be aligned with the source cell decomposition without reintroducing a power loss;
4. the deterministic all-main term fails to match WI-049's genuine four-form local model at leading order.

Checks 1--3 concern the analytic conclusion (24). Check 4 concerns only upgrading (24) to a complete four-prime asymptotic on the doubly-small region. Until that splice is audited, the accepted conclusion is exactly the fiber suppression stated above, with the full Yang candidate and its larger simple-zero percentage remaining unproved.
