# WI-028 — the independent one-sided fourth-moment route needs only a coarse remainder bound to improve the current theorem

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEEDS-AUDIT + PRIOR-ART-REDIRECTION`. Hongyi Yang and Shihua Yang's August 2026 higher-moment preprint contains a logically independent one-sided fourth-moment route based on the Matomäki--Radziwiłł--Tao averaged shifted-prime-correlation theorem. Its advertised `0.691615` simple-critical proportion is **not established evidence here**: the authors themselves grade the theorem `certified-candidate`, and the public deterministic core/tail implementation still uses non-rigorous numerical extrapolation/error budgets. The durable new deduction in this finding is narrower but strategically important: relative to Mathia's current exact unconditional bound from WI-024, that route does **not** need anything close to the advertised remainder `0.0066`. A rigorous asymptotic upper bound below `0.0380702829042...` for its single remainder variable would already give a strict unconditional improvement, and a bound below `0.0221687593561...` would cross the `0.68185` first-two-moment ceiling discussed by Alpöge--Furman/Yang--Yang.

## 1. The external one-sided route is distinct from the WI-003 truncation gap

The Yang--Yang manuscript separates two fourth-moment programs.

1. Its exact higher-moment ladder attempts to prove `m_4=13/4`, then moments five and six, by a cell truncation followed by arithmetic transport. WI-003 shows that this proof is not established as written because the manuscript's only defined `ell_1` is the global Riemann--von Mangoldt normalization, while the truncation later treats `ell_1` as a varying cell parameter.
2. Section 4 of the same manuscript gives a **logically independent one-sided fourth-moment route**. It does not require the exact `m_4=13/4` evaluation. Instead it writes the fourth moment as the baseline contribution plus a remainder `R(1)`, controls most shifted-prime correlations with the published Matomäki--Radziwiłł--Tao long-shift theorem, and reduces the remaining deterministic contribution to a core plus a singular-series tail.

The manuscript states this independence explicitly. Its Theorem `t:fm` is nevertheless graded `certified-candidate with the numerical-analysis step of Lemma CL`; therefore this branch is not a way to bypass the evidence gate merely by citing its final decimal.

The relevant published arithmetic input is Matomäki--Radziwiłł--Tao's averaged Hardy--Littlewood theorem in the range

\[
X^{8/33+\varepsilon}\le H\le X^{1-\varepsilon}.
\]

Yang--Yang quote it in the variance form needed for their shift aggregation and give an exact divisor-multiplicity argument that transfers the full-shift mean-square estimate to structured shifts `h=qk`. This audit found no conflict between the quoted exponent range and the published theorem. The live gap identified below is later, in the deterministic remainder certification.

## 2. Exact consumption formula for an arbitrary one-sided remainder

Let `r` denote any rigorous asymptotic upper bound supplied to the Yang--Yang one-sided consumer,

\[
\limsup_{T\to\infty}R(1)\le r.
\tag{1}
\]

Their counting step sets

\[
\Delta=r+\frac1{30}
\]

and

\[
\Lambda_2(0)
=\frac{5/108+\Delta/3}{1/3+4\Delta/3}.
\tag{2}
\]

The resulting simple-critical proportion simplifies exactly to

\[
\boxed{
P(r):=1-2\Lambda_2(0)
=\frac{180r+71}{360r+102}.
}
\tag{3}
\]

This scalar map is strictly decreasing throughout the relevant range, since

\[
\boxed{
P'(r)=-\frac{7200}{(360r+102)^2}<0.
}
\tag{4}
\]

Consequently a target proportion `t>1/2` is beaten exactly when

\[
\boxed{
r<r_*(t):=\frac{102t-71}{180-360t}.
}
\tag{5}
\]

Equation (5) is the useful proof-budget conversion: it says how weak the arithmetic/numerical remainder theorem may be while still producing a desired unconditional zeta-zero proportion.

## 3. The current Mathia theorem only requires `r < 0.0380703`

WI-024 proves, using the Lean-checked four-point Gram certificate and exact support-one assembly,

\[
t_{\rm current}
=
\frac{515H_{\rm MT}-1536/2500}
{515-1182717/1000000}
=0.6728529261926306156447555\ldots.
\tag{6}
\]

Substitution into (5) gives

\[
\boxed{
r_*(t_{\rm current})
=0.0380702829042267938771462\ldots.
}
\tag{7}
\]

Therefore the independent one-sided fourth-moment architecture would **strictly improve the current established theorem** as soon as its combined asymptotic remainder is rigorously shown to satisfy

\[
\boxed{
\limsup R(1)<0.0380702829042.
}
\tag{8}
\]

This is much weaker than Yang--Yang's candidate target

\[
r=0.0066,
\]

which yields their advertised

\[
P(0.0066)=0.691615\ldots.
\]

Likewise, taking the `0.68185` bandwidth-one first-two-moment ceiling used in the same literature as a comparison target gives

\[
\boxed{
r_*(0.68185)
=0.0221687593560015886\ldots.
}
\tag{9}
\]

Thus a proof of `limsup R(1)<0.02217` would already cross that ceiling, without proving the sharper `0.0066` claim.

For orientation, the exact consumer would need a *negative* remainder to reach the manuscript's unconsumed numerical projection around `0.7031`:

\[
r_*(0.7031)=-0.00979539362109\ldots.
\]

That last figure is not an objective for the first certification pass.

## 4. Why the published `0.0066` is not yet a certified asymptotic bound

The manuscript assembles

\[
R(1)
\le
\operatorname{core}(T)
+\varepsilon_{\rm tail}
+o(1)
\tag{10}
\]

and advertises the conservative ledger

\[
(-0.0055+0.0010)+0.0111=0.0066.
\tag{11}
\]

But the manuscript itself explicitly states that the continuum-core constants and its quadrature are **computed constants with stated bands, not certified enclosures**, and names certification of the quadrature as an open item. Its Lemma CL reports

\[
C_{\rm core}=-0.0209\pm0.0026
\]

from Richardson extrapolation, but does not present a rigorous enclosure theorem for that number. The theorem therefore cannot be promoted merely because the displayed finite-height values trend in the desired direction.

The public reproduction code confirms this trust boundary rather than closing it. `scripts/quadrature_cert.py` uses floating NumPy arrays and constructs its error budget from empirical or extrapolative ingredients: a last-block geometric-ratio estimate for the infinite gamma tail, numerical regression for a slope/constant, finite-grid interpolation, differences of two- and three-point Richardson extrapolants, a doubled grid-difference heuristic, and a finite slab-sensitivity scan. These are useful falsifiers and diagnostics, but without analytic derivative/tail/error estimates they are not rigorous interval enclosures.

The public tail code has the same issue at a second load-bearing place. `scripts/tail_bound.py` truncates its signed gamma array at a finite `DCAP`, estimates the omitted part from the mass in the last computed half-range, and propagates that quantity numerically. The code does not itself prove the infinite arithmetic tail bound needed to convert the finite computation into the asserted asymptotic `epsilon_tail<=0.0111`.

Thus the mathematically correct current status is

\[
\boxed{
0.691615\text{ is a high-value candidate, not an established unconditional improvement.}
}
\tag{12}
\]

This conclusion is independent of WI-003: even if the separate exact-moment cell truncation were abandoned completely, the one-sided route still needs its own rigorous deterministic remainder enclosure.

## 5. The certification target can be weakened drastically

The main strategic consequence is that the first rigorous replay should **not** try to reproduce `C_core=-0.0209+-0.0026` or the exact candidate `r=0.0066`.

The only quantity that enters (3) is the combined asymptotic remainder `r`. Therefore the lowest-cost meaningful certification gate is directly

\[
\boxed{
\limsup_{T\to\infty}R(1)<0.0380702829042.
}
\tag{13}
\]

A proof at this coarse scale would already beat WI-024. If the tail were independently certified at the manuscript's advertised `0.0111`, then even a very weak core estimate

\[
\limsup\operatorname{core}(T)<
0.0380702829042-0.0111
=0.0269702829042\ldots
\tag{14}
\]

would suffice for an improvement. To cross `0.68185`, the analogous core target would only be

\[
\limsup\operatorname{core}(T)
<0.0110687593560\ldots.
\tag{15}
\]

By contrast, reproducing the candidate `0.691615` at a tail charge `0.0111` requires roughly

\[
\limsup\operatorname{core}(T)< -0.0045001049558\ldots,
\tag{16}
\]

which is a materially stronger burden.

Equations (13)--(16) show why the route deserves renewed attention despite the failed exact-moment audit: **the current theorem can be improved by a coarse one-sided certification with roughly a factor `5.8` more remainder allowance than the manuscript's `0.0066` target.** The finite-height computations are suggestive evidence that such a coarse certificate may be attainable, but they are not themselves proof.

## 6. Prior art and novelty assessment

No novelty is claimed for the one-sided fourth-moment architecture, the candidate `0.691615`, the Matomäki--Radziwiłł--Tao shifted-correlation theorem, or the Yang--Yang decomposition into a core and tail. Those belong to the cited literature/research draft.

The new Mathia deduction is the exact threshold audit relative to the **current established Mathia bound**: equation (7) converts the unresolved external remainder problem into a much weaker falsifiable gate. A targeted search did not locate a public statement of this threshold comparison, but absence of a search hit is not a priority claim.

This result is therefore best viewed as **prior-art redirection plus proof-budget reduction**, not as a new zeta theorem. It changes which external candidate is worth attacking first and what must actually be proved to obtain a material result.

## 7. Falsification and verification gate

A successful upgrade must supply an asymptotic theorem, not a better finite-height fit. A minimal rigorous replay should:

1. reconstruct the exact definition and normalization of `R(1)` from the fourth trace ledger and verify the counting formula (3);
2. verify the Matomäki--Radziwiłł--Tao range and every weight/divisor transfer used by the structured-shift aggregation;
3. derive a genuine infinite-tail estimate for the gamma/singular-series contribution, rather than extrapolating from the last computed shell;
4. bound the deterministic core either analytically or with outward-rounded interval quadrature plus a proved discretization and truncation error;
5. combine the terms directly and target (13) first. Only after that gate closes is it useful to spend proof budget tightening toward `0.02217` or `0.0066`.

A counterexample to any of the bridge/aggregation steps would instead kill this route before numerical certification matters. Conversely, a proof of (13) with those analytic bridges intact would immediately constitute a new unconditional improvement over WI-024.

## 8. Consequence for `weil_inertia`

WI-003 correctly blocks importing the Yang--Yang exact fourth-through-sixth-moment tower as established arithmetic evidence. It does **not** imply that every higher-moment escape from the support-one/two-moment barrier is equally remote.

The independent one-sided fourth-moment branch has a significantly lower proof burden than its headline presentation suggests:

\[
\boxed{
R(1)<0.0380703
\Longrightarrow
\text{strict improvement over }0.67285292619\ldots,
}
\]

while

\[
\boxed{
R(1)<0.0221688
\Longrightarrow
\text{cross the }0.68185\text{ comparison ceiling.}
}
\]

This is now the highest-leverage arithmetic audit target among the currently identified single-rung routes: first prove a coarse one-sided remainder theorem, then tighten it only if the coarse gate succeeds. The established bound itself is unchanged until that certification exists.
