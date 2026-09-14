# WI-294 — one-signed pole positivity kills large two-island complete screening

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.
- **Scope:** the **one-signed, completely screened, symmetric two-island** first-crossing branch of `WI-284`--`WI-293`. The result uses the actual nonnegative null vector, not the unrestricted spectral bottom over all functions supported on the same set.
- **Result:** the large-aperture two-island branch is impossible already from the classical prime number theorem. Complete screening makes the two island widths tend to zero because a prime occurs in every fixed relative interval `[x,e^eta x]` for all sufficiently large `x`. But `WI-284` forces the actual nonnegative null mode `v` to satisfy `q_arch(v)=0`; on such a vector Suzuki's pole term is **strictly positive**, while the support-measure uncertainty bound of `WI-287` makes the gamma term strictly positive once the support measure is small. Hence `q_arch(v)>0`, a contradiction.
- **General structural consequence:** every nonzero nonnegative completely screened first-crossing null mode has an **absolute positive lower bound on the measure of its positivity support**. Any support topology for which complete screening forces that measure to zero is therefore excluded, independently of a spectral-bottom analysis.
- **Correction/redirect boundary:** `WI-286`--`WI-287` remain correct as statements about the unrestricted prime-deleted spectral bottom. Their negative comparison vectors are odd/sign-changing and exploit the negative eigenvalue of the rank-two pole form. They therefore do not describe the actual one-signed null vector. The Lambert-`W` endpoint and the rare-host arithmetic of `WI-288`--`WI-293` remain valid necessary-condition analyses inside that relaxed support problem, but they are no longer needed to exclude the **large** one-signed symmetric two-island branch.
- **What it does not claim:** it does not exclude a bounded-aperture two-island configuration without an effective finite-range check, and it does not treat sign-changing first modes, incomplete screening, or many-component supports whose total support measure need not shrink.
- **Novelty boundary:** Suzuki supplies the exact gamma/von-Mangoldt/pole decomposition; Bombieri/Yoshida supply the classical support-restricted variational framework; the prime number theorem supplies primes in fixed relative intervals. The Fourier `L^infinity`/bathtub support-measure lower bound was already derived in `WI-287`, and the pole factorization was already recorded in `WI-240`. The new line-local deduction is to apply those two facts to the **actual nonnegative null vector** from `WI-284`, rather than to the unrestricted supported spectral bottom, which removes the negative-pole escape used by `WI-286`--`WI-287`. Targeted searches around Suzuki/Bombieri support-restricted Weil forms and nonnegative/support-sign arguments did not locate this combination; search absence is audit context only, not a priority claim.

## Claim

Let `a>0` be a Suzuki first crossing and let

\[
0\ne v\ge 0,
\qquad A_av=0,
\qquad q_a(v)=0,
\tag{1}
\]

be a real nonnegative null mode. Assume complete screening of every active prime-power autocorrelation, and let

\[
E:=\{t\in(-a,a):v(t)>0\}
\tag{2}
\]

modulo null sets. Then `WI-284` gives

\[
q_{\rm arch}^a(v)=0.
\tag{3}
\]

There is an absolute constant `mu_0>0` such that necessarily

\[
\boxed{|E|>\mu_0.}
\tag{4}
\]

Now specialize to a symmetric two-island positivity support

\[
E_{R,b}=(-R-b,-R+b)\cup(R-b,R+b),
\qquad R>b>0,
\tag{5}
\]

with

\[
\Delta=2R,
\qquad x=e^\Delta,
\qquad a=R+b.
\tag{6}
\]

If this support completely screens every active prime lag, then there is an absolute `X_0` such that no such first-crossing null mode exists for

\[
\boxed{x\ge X_0.}
\tag{7}
\]

Equivalently, the large-aperture one-signed completely screened symmetric two-island branch is empty.

## 1. The actual one-signed vector sees the opposite pole sign from the WI-287 extremizer

Write Suzuki's exact prime-deleted form as

\[
q_{\rm arch}^a(u)=G(u)+P_a(u),
\tag{8}
\]

where

\[
G(u)=\frac1{2\pi}\int_{\mathbb R}
\left(
\operatorname{Re}\psi\!\left(\frac14+\frac{iz}{2}\right)-\log\pi
\right)|\widehat u(z)|^2\,dz
\tag{9}
\]

and, for functions supported in `(-a,a)`, the pole term factors exactly as in `WI-240`:

\[
P_a(u)=2\operatorname{Re}\!\left(L_-(u)\overline{L_+(u)}\right),
\qquad
L_\pm(u)=\int_{-a}^a u(t)e^{\pm t/2}\,dt.
\tag{10}
\]

For the actual null vector `v`, real nonnegativity gives

\[
L_-(v)>0,
\qquad
L_+(v)>0,
\tag{11}
\]

because `v` is nonzero and the exponential weights are strictly positive. Consequently

\[
\boxed{P_a(v)=2L_-(v)L_+(v)>0.}
\tag{12}
\]

Combining (3), (8), and (12) yields the strict requirement

\[
\boxed{G(v)<0.}
\tag{13}
\]

This is the sign information lost when `WI-286`--`WI-287` replaced the actual null vector by the full supported form domain. On a symmetric support the pole operator has a large negative eigenvalue, but its corresponding directions are odd/sign-changing. They cannot represent a nonzero `v>=0`.

## 2. Negative gamma energy imposes an absolute support-measure floor

Let

\[
\mu:=|E|<\infty.
\tag{14}
\]

The support-measure argument of `WI-287` applies to every `u` supported in a measurable set of measure `mu`. With

\[
p_u(z):=\frac{|\widehat u(z)|^2}{2\pi\|u\|_2^2},
\tag{15}
\]

Parseval and Cauchy--Schwarz give

\[
\int_{\mathbb R}p_u(z)\,dz=1,
\qquad
0\le p_u(z)\le\frac{\mu}{2\pi}.
\tag{16}
\]

The bathtub rearrangement, together with the global digamma lower bound used in `WI-287`, gives an absolute constant `C_0` such that

\[
\boxed{
\frac{G(u)}{\|u\|_2^2}
\ge \log\frac1\mu-C_0.
}
\tag{17}
\]

For completeness, the sharper intermediate form is

\[
\frac{G(u)}{\|u\|_2^2}
\ge B(\pi/\mu)-C_\Gamma,
\qquad
B(t)=\frac{(1+t)\log(1+t)-t}{t},
\tag{18}
\]

and `B(t)>=log t-1` yields (17) after absorbing constants.

Apply (17) to `v`. Equation (13) forces

\[
\log\frac1\mu-C_0<0.
\tag{19}
\]

Thus, with the absolute constant

\[
\mu_0:=e^{-C_0}>0,
\tag{20}
\]

we obtain the support floor

\[
\boxed{|E|=\mu>\mu_0.}
\tag{21}
\]

This conclusion uses no prime-gap estimate and no two-island geometry. It is a general necessary condition for a one-signed completely screened first-crossing null mode: complete screening deletes the prime operator on `v`, pole positivity demands negative gamma energy, and Fourier uncertainty prevents negative gamma energy on arbitrarily small supports.

## 3. The prime number theorem forces a completely screened two-island support below that floor

For the two-island set (5),

\[
|E_{R,b}|=4b.
\tag{22}
\]

The positive difference set between the left and right islands is

\[
(\Delta-2b,\Delta+2b).
\tag{23}
\]

Therefore, if a prime `p` satisfies

\[
|\log p-\Delta|<2b,
\tag{24}
\]

then translation by the active lag `log p` produces a positive-measure cross-island overlap. When `\log p<\Delta+2b=2a`, this contradicts complete screening.

Now fix any `eta>0`. The classical prime number theorem implies

\[
\pi(e^\eta x)-\pi(x)
\sim \frac{(e^\eta-1)x}{\log x}>0,
\tag{25}
\]

so for every fixed `eta` and all sufficiently large `x` there is a prime

\[
x\le p\le e^\eta x.
\tag{26}
\]

Hence

\[
0\le\log p-\Delta\le\eta.
\tag{27}
\]

If `2b>eta`, (24) holds and the prime is automatically active because

\[
\log p\le\Delta+\eta<\Delta+2b=2a.
\tag{28}
\]

Thus complete screening implies, for every fixed `eta>0` and all sufficiently large `x`,

\[
2b\le\eta.
\tag{29}
\]

In particular, along any large-`x` completely screened two-island family,

\[
\boxed{b\to0,
\qquad |E_{R,b}|=4b\to0.}
\tag{30}
\]

This already contradicts the absolute floor (21).

Equivalently, make the contradiction one-shot. Choose

\[
\eta:=\frac{\mu_0}{4}>0.
\tag{31}
\]

The support floor (21)--(22) gives

\[
2b>\frac{\mu_0}{2}>\eta.
\tag{32}
\]

For all sufficiently large `x`, the PNT supplies a prime satisfying (26), so (27)--(28) force a forbidden cross-island overlap. This proves (7).

No Baker--Harman--Pintz exponent, Runbo Li preprint, Cramer-scale estimate, Heath-Brown exceptional-gap bound, prime-square incidence estimate, or Lambert-`W` optimization is required.

## 4. Why WI-286--WI-293 did not see this contradiction

The distinction is between two optimization problems.

`WI-286`--`WI-287` asked whether the **entire prime-deleted form restricted to the support** must be positive. That problem legitimately minimizes over arbitrary signed vectors. On `E_{R,b}`, the rank-two pole form has a negative eigenvector essentially given by opposite signs on the two islands. At the currently known prime-gap exponents, this odd direction can drive the unrestricted supported Rayleigh quotient very negative. The Lambert-`W` threshold is the correct boundary for that relaxed spectral-bottom question.

But `WI-284` gives more information than a zero spectral bottom: the vector that actually attains zero is the same first-crossing mode `v`, and the branch assumption is `v>=0`. For that vector the pole sign reverses from the dangerous odd direction:

\[
P_a(v)>0
\quad\text{instead of}\quad
P_a(u_{\rm odd})<0.
\tag{33}
\]

Once this sign is retained, it is unnecessary to prove positivity on every vector supported in `E`. It suffices to show positivity on the one vector that would have to be null. Shrinking support already makes its gamma contribution positive, while its pole contribution is positive for free.

Thus the large-gap host program of `WI-288`--`WI-293` was solving a harder relaxed problem than the actual one-signed null-vector contradiction requires. Those findings remain valid descriptions of what support geometry alone permits and of how the unrestricted prime-deleted bottom behaves; the present finding changes their role from a live asymptotic closure route to a diagnostic of the relaxation gap.

## 5. Prior-art audit and provenance

The exact decomposition (8)--(10) is from Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (2026), already source-audited in `WI-240` and `SOURCES.md`. Suzuki's framework unifies the support-restricted Weil variational theory of Yoshida and Bombieri; Bombieri's **A variational approach to the explicit formula**, *Comm. Pure Appl. Math.* 56 (2003), 1151--1164, is the classical variational antecedent.

The support-measure Fourier cap and bathtub lower bound are elementary harmonic-analysis deductions already proved in `WI-287`; no external uncertainty theorem is imported here. The only arithmetic input in the asymptotic two-island closure is the classical prime number theorem in the fixed-ratio form (25).

Targeted searches around support-restricted Weil minimization, Suzuki's screw-function form, nonnegative test functions, and sign restrictions on the pole/gamma decomposition located the Suzuki/Bombieri framework but not the deduction (12)--(21) or its combination with fixed-ratio prime occurrence. This absence is not used as mathematical evidence and is not a priority claim.

## 6. Stress tests and limits

- **Strict pole sign:** `P_a(v)>0`, not merely `>=0`, because `v` is nonzero, nonnegative, and both exponential weights are strictly positive on the finite aperture.
- **No hidden use of the unrestricted spectral bottom:** the contradiction uses only `q_arch(v)=0` for the actual null vector. Negative odd directions in the same support subspace are irrelevant.
- **No quantitative prime-gap theorem is needed:** PNT in any fixed multiplicative interval is enough because the gamma argument supplies a fixed positive support-measure floor. The old need to compare a shrinking width against a growing negative pole edge arose only after allowing sign-changing vectors.
- **Large aperture only:** the PNT step yields an `X_0` depending on the absolute support-floor constant. This finding does not certify the finite range `x<X_0`.
- **One-signedness is essential:** for sign-changing `v`, `L_-` and `L_+` can have opposite signs or cancellations, so (12) fails. This is exactly the branch where the odd negative pole direction can become relevant again.
- **Complete screening is essential:** without it, `q_arch(v)=q_a(v)` need not hold, and surviving prime terms can offset the gamma/pole balance.
- **Many components are not automatically excluded:** (21) is a total support-measure floor. A multi-island topology can in principle retain positive total measure even if some individual components become thin.

## Research consequence

For the one-signed completely screened branch, the reusable invariant is now

\[
\boxed{
q_a(v)=0,\ v\ge0,\ \text{complete screening}
\Longrightarrow
|\{v>0\}|\ge\mu_0>0.
}
\tag{34}
\]

The symmetric two-island topology violates this invariant at large aperture by the PNT alone. Future work on complete one-signed screening should therefore move to support topologies capable of retaining a fixed positive total measure under all active prime-power translations, or exploit (34) directly to prove that no such topology is compatible with the first-crossing/null-equation constraints. Further refinement of rare `sqrt(x)\log x` host incidence is not load-bearing for the large two-island branch.