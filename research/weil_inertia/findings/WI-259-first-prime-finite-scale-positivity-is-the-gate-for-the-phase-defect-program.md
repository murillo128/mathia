# WI-259 — first-prime finite-scale positivity is the gate for the phase-defect program

**Status:** `EXACT-DERIVED + PRIOR-ART-REDIRECT + COMPUTATIONAL-CERTIFICATE-NEEDS-INDEPENDENT-REPLAY`.

The current first-crossing phase program has a previously implicit prerequisite. Let

\[
a_*:=\inf\{a>0:\lambda_a\le0\}
\]

be the first localized Weil ground-state crossing from WI-238 under `RH` failure. The phase-defect identity of WI-258 contains the first von-Mangoldt atom only once the aperture radius exceeds

\[
r_2:=\frac{\log 2}{2}=0.3465735902799726\ldots.
\]

Therefore prime-coupled phase analysis at a guaranteed radius requires an unconditional finite-scale positivity theorem beyond `r_2`; it cannot be obtained merely from the existence of a first crossing.

A public external project, `telleroutlook/weil-first-prime`, targets exactly this missing gate at

\[
L=\frac7{20}=0.35>\frac{\log2}{2}.
\]

If its `FP-0.35` positivity certificate is independently validated, WI-238's monotonicity gives

\[
\boxed{\lambda_{7/20}>0\Longrightarrow a_*>\frac7{20}>\frac{\log2}{2}.}
\]

Consequently the fixed radius `r=7/20` is admissible in every hypothetical first-crossing mode, and because

\[
\log2<\frac7{10}<\log3,
\]

its finite prime-power source contains **exactly the single atom `n=2`**. This turns the current medium-radius phase clue into a sharply defined one-prime problem rather than an unspecified “first few prime powers” problem.

The public `FP-0.35` repository is not imported here as established mathematics. Its current certificate is a serious computational candidate, but its public publication state is internally inconsistent and the currently relevant post-fix certificate has not been independently replayed by Mathia. The correct research redirect is therefore to audit/replay `FP-0.35` before treating prime activation at the first crossing as available evidence.

## 1. Exact first-prime gate from the localized Weil operator

WI-238 proves from the variational definition that `a -> lambda_a` is nonincreasing. Under `RH` failure there is a first crossing `a_*` with

\[
\lambda_a>0\quad(a<a_*),\qquad \lambda_{a_*}=0.
\]

For a first-crossing zero mode `v`, WI-258 defines the source-weighted autocorrelation measure

\[
d\mu_v(h)=C_v(h)\left[
\sum_{\log n<2a_*}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}(dh)+w(h)\,dh
\right]
\]

and, for every `0<r<a_*`, the localized phase correction

\[
J_v(r,t)=\int_0^{2r}(2r-h)(1-\cos(th))\,d\mu_v(h).
\]

At a given radius `r`, a prime-power atom `n` occurs in this localized integral precisely when `log n<2r`. Thus the first arithmetic threshold is `r_2=(log2)/2`.

Now suppose one has the finite-scale positivity statement

\[
\lambda_{7/20}>0.
\tag{1}
\]

Because `lambda_a` is nonincreasing, (1) and `lambda_{a_*}=0` force

\[
a_*>7/20.
\tag{2}
\]

The elementary inequalities

\[
\log2<7/10<\log3
\tag{3}
\]

then show that `r=7/20` lies strictly below `a_*` and the discrete part of `J_v(7/20,t)` consists only of `n=2`. Explicitly,

\[
\boxed{
\begin{aligned}
J_v(7/20,t)
={}&\frac{\log2}{\sqrt2}
\left(\frac7{10}-\log2\right)
(1-\cos(t\log2))C_v(\log2)\\
&+\int_0^{7/10}
\left(\frac7{10}-h\right)(1-\cos(th))w(h)C_v(h)\,dh.
\end{aligned}}
\tag{4}
\]

No `n=3` or higher prime-power atom is present. Equation (4) is an exact reduction, conditional only on the finite-scale positivity input (1), not on any numerical model of the zero mode.

This is useful but not by itself a contradiction. The coefficient of the `n=2` atom contains the small threshold factor `7/10-log2`, and `C_v(log2)` is not known to have a fixed sign or nonzero lower bound. The continuous archimedean term remains coupled to the same autocorrelation. Thus “the first prime is active” is a prerequisite, not a defect-to-zero theorem.

## 2. What the public `FP-0.35` project actually supplies

The repository `telleroutlook/weil-first-prime` states the finite-scale problem in exactly the needed normalization: strict positivity of the local Weil quadratic form on

\[
L^2(-7/20,7/20).
\]

Its analytic layer includes several exact results relevant to the gate:

1. In the first-prime window `(log2)/2<L<(log3)/2`, the `n=2` overlap operator has spectrum `{-1,0,1}` and operator norm exactly `1`. Hence the prime layer is indefinite and its operator norm jumps from zero to one immediately after the threshold; it is not a small bounded perturbation as `L` crosses `(log2)/2`.
2. After scaling to `(-1,1)`, the endpoint archimedean potential can absorb the first-prime shift on a nontrivial range. At `L=7/20` the repository gives the exact rational estimate `c_2/kappa_edge<31/100`, hence `V+P_{2,L}>=(69/100)V>=0`.
3. Its split-residual Schur criterion reduces full positivity to finite Legendre blocks plus rigorously bounded residuals, rather than merely checking a Ritz truncation.

These analytic statements materially constrain how WI-258 should be used. The first-prime operator is simultaneously **abrupt and indefinite**, yet can be absorbed by the local archimedean potential at `L=7/20`. A successful phase argument cannot infer instability merely from the appearance of the `n=2` shift; it must exploit the coupled source identity (4), first-crossing slack, or another invariant not erased by that absorption.

Primary public source: `telleroutlook/weil-first-prime`, especially `README.md`, `docs/THEOREMS.md`, and `scripts/reproduce_fp035.py`, <https://github.com/telleroutlook/weil-first-prime>.

## 3. Evidence audit of the claimed `FP-0.35` certificate

The current repository state reports `FP-0.35 HOLDS` and provides a recomputation script/certificate with positive margins in both parity sectors. The latest source commit located is

`e66f467bc4447c5b2491577cbb6c3ae0e721fb43` (12 Aug 2026),

which fixes a load-bearing interval-construction bug: `python-flint`'s `arb(lo,hi)` had been used as though the arguments were interval endpoints, although they are midpoint/radius. The fix introduces proper endpoint-to-ball conversion and regenerates the certificate. The repository reports post-fix lower spectral margins approximately

\[
9.5\times10^{-4}\quad\text{(even)},\qquad
1.896\times10^{-2}\quad\text{(odd)},
\]

at 256-bit Arb precision.

That is encouraging evidence, but three public-state issues prevent Mathia from treating (1) as established:

- the checked-in `docs/THEOREMS.md` still says that `FP-0.35` itself remains a conjecture, while the README says `HOLDS`;
- the checked-in `thm-fp-035` proofctl attestation predates the 12 Aug interval-construction fix and records a `generator_cmds` field that merely copies an existing certificate rather than recomputing it;
- the ordinary CI workflow runs tests/lint but does not constitute an independent cold replay of the roughly 10--15 minute `python-flint` certificate.

The repository itself describes independent/cold replay as part of its trust boundary. Mathia therefore classifies the current headline as

\[
\boxed{
\texttt{COMPUTATIONAL-CERTIFICATE + NEEDS-INDEPENDENT-REPLAY},
}
\]

not as a theorem that can yet be inserted into the WI chain.

This evidence boundary is important because the post-fix certificate is exactly the piece needed here. The older proofctl attestation cannot certify code/data generated after its freshness date, even if the corrected certificate ultimately proves the same mathematical statement.

## 4. Nearby independent prior art does not yet cross the prime threshold

The public `manxis-contact/Eureka` report (arXiv:2608.19047) contains an independent finite-scale positivity candidate through

\[
a\le\frac{69}{200}=0.345.
\]

That radius is very close to, but still strictly below,

\[
\frac{\log2}{2}=0.34657359\ldots.
\]

Accordingly its prime-free certificate candidate cannot by itself guarantee that the `n=2` atom is active at a hypothetical first crossing. The same report separately analyzes the first-prime layer and derives an endpoint-potential absorption range extending beyond the threshold, but explicitly does not promote that local absorption calculation to full finite-scale positivity there.

This nearby work corroborates that `(log2)/2` is a genuine structural boundary rather than an arbitrary numerical target. It does not close the gate required by WI-258.

Source: `manxis-contact/Eureka`, report body and finite-scale spectral section, <https://github.com/manxis-contact/Eureka>; arXiv:2608.19047.

## 5. Consequence for the live phase-defect clue

The next source-specific phase test should not begin by optimizing many prime thresholds. It has a sharper dependency chain:

\[
\boxed{
\lambda_{7/20}>0
\Longrightarrow
a_*>7/20
\Longrightarrow
\text{the radius }r=7/20\text{ is valid at first crossing}
\Longrightarrow
\text{exactly one prime atom enters }J_v.
}
\tag{5}
\]

Thus an independent replay or independent analytic proof of `FP-0.35` would immediately put the current clue in the clean one-prime regime (4). Conversely, until such a theorem is available, arguments that presume a prime contribution at every hypothetical first crossing have a gap: `a_*` could still lie in the prime-free interval allowed by currently established Mathia evidence.

Even after (1) is certified, the target remains nontrivial. The exact first-prime operator theorem shows that crossing the threshold does not provide perturbative smallness, while endpoint absorption shows that the prime shift alone need not create negativity. The live mathematical question is therefore whether **first-crossing zero-mode structure plus the full archimedean/prime source coupling in (4)** forces some `J_v(7/20,t)<0`, or whether an admissible compact-support autocorrelation can satisfy the whole phase cone.

## Prior-art and novelty assessment

Finite-scale Weil positivity, the first-prime overlap operator, endpoint absorption, and the candidate `FP-0.35` certificate are prior art from the cited public repositories. WI-238 already supplies the Mathia first-crossing monotonicity, and WI-258 supplies the phase-defect identity.

The exact implication (5), the isolation of `r=7/20` as a **single-prime phase-defect radius** for any first crossing once `FP-0.35` is validated, and the resulting dependency audit of the live clue are Mathia deductions. No priority claim is made. The substantive contribution is the research redirect: finite-scale positivity just beyond `(log2)/2` is the gate that must be settled before prime-coupled first-crossing phase arguments can be used unconditionally.

## Falsification and audit test

This finding has two layers that must remain separate.

The exact Mathia layer is falsified by any normalization mismatch between the `FP-0.35` local quadratic form and Suzuki/WI-238's `Q_W^a`, or by an error in the monotonicity/threshold implication. The direct audit is to identify the forms term by term and verify that `L=7/20` is the same support radius `a`.

The external-certificate layer is upgraded only by an independent cold replay of the corrected post-`e66f467` generator/checker stack, or an independent analytic/formal proof of the same strict lower bound. A README status, a stale attestation, a finite Ritz eigenvalue, or an unreplayed certificate is insufficient. If the corrected full-form certificate fails, equation (5) remains a valid conditional implication but supplies no new unconditional information about `a_*`.

## Research consequence

The accepted sliding-autocorrelation/phase clue should be narrowed accordingly. First settle or independently reproduce finite-scale positivity at `L=7/20`; if it survives, freeze `r=7/20` and attack the exact one-prime identity (4) before introducing larger radii or multi-prime numerical searches. If the certificate fails, the line should return to establishing any rigorous positivity margin past `(log2)/2` rather than assuming prime activation at the first crossing.
