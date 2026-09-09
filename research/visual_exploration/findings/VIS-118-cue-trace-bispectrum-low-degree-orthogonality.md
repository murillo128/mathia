# VIS-118 — low-degree CUE trace bispectra have an exact centered orthogonal null corridor

## Claim

Let `U` be Haar distributed on `U(N)` and write

`p_m(U)=Tr(U^m)`

for `m>=1`. For positive integers `a,b`, define the third-order trace triad

`B_(a,b)=p_a p_b overline(p_(a+b))`.

Because multiplication is symmetric in `a,b`, regard `(a,b)` as an unordered pair and normally take `a<=b`.

Then the classical Diaconis–Shahshahani trace-moment formula, in the corrected finite-`N` form recorded by Diaconis–Evans, gives the following exact CUE calibration.

First, whenever

`a+b <= N`,

one has

`E_CUE[B_(a,b)] = 0`.

Second, whenever

`2(a+b) <= N`,

`E_CUE[|B_(a,b)|^2] = z_(a,b)`,

where

`z_(a,b) = a b (a+b)` if `a<b`,

and

`z_(a,a) = 4 a^3`.

Third, for two unordered positive pairs `(a,b)` and `(c,d)`, if

`a+b+c+d <= N`,

then

`E_CUE[B_(a,b) overline(B_(c,d))] = 0`

unless `{a,b}={c,d}`. Under the same degree condition,

`E_CUE[B_(a,b) B_(c,d)] = 0`

for every pair of triads.

Consequently, for any predeclared panel

`P_N = {(a,b): a<=b, a+b<=N/2}`,

the normalized coordinates

`W_(a,b) = B_(a,b) / sqrt(z_(a,b))`

satisfy the exact finite-size identities

`E[W_(a,b)] = 0`,

`E[W_(a,b) overline(W_(c,d))] = 1_{(a,b)=(c,d)}`,

`E[W_(a,b) W_(c,d)] = 0`.

Thus the low-degree CUE trace-bispectrum panel is already exactly whitened at second order after a deterministic normalization. No CUE Monte Carlo covariance estimate is needed in this corridor.

This remains true for genuinely growing frequencies `a=a_N`, `b=b_N`, including frequencies of order `N`, provided the predeclared triads stay inside `a_N+b_N<=N/2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + FINITE-SIZE-CUE NULL + GROWING-SCALE THIRD-ORDER CHANNEL + NO-NOVELTY-CLAIM`.

No independence or Gaussian law for the `W_(a,b)`, no corresponding zeta-zero statistic, no arithmetic excess over CUE, and no RH implication is established.

## 1. Classical Haar-unitary moment input

Diaconis and Shahshahani computed the joint moments of traces of powers of a Haar unitary matrix. Diaconis and Evans restate the result with the finite-size condition used here.

For nonnegative exponent arrays `r_j,s_j`, if

`N >= max(sum_j j r_j, sum_j j s_j)`,

then

`E[ product_j p_j^(r_j) overline(p_j)^(s_j) ]`

vanishes unless the two exponent arrays agree exactly. When they agree, the moment is

`product_j j^(r_j) r_j!`.

Equivalently, compound power sums indexed by two distinct partitions are orthogonal throughout the low-degree range. This is classical representation-theoretic CUE structure, not a new Mathia moment theorem.

The important point for the current visual line is that the theorem applies directly to a third-order spectral triad whose frequencies may grow with `N`; one only has to keep the total weighted degree below the exact finite-size boundary.

## 2. The trace bispectrum is exactly centered

For

`B_(a,b)=p_a p_b overline(p_(a+b))`,

the positive and negative weighted degrees are both `a+b`.

The positive exponent pattern corresponds to the partition `(a,b)` while the negative pattern corresponds to the one-part partition `(a+b)`. Since `a,b>0`, these exponent arrays are different, including when `a=b`.

Therefore the classical trace-moment identity gives

`E[B_(a,b)]=0`

whenever `a+b<=N`.

This centering is stronger than an appeal to global angular rotation. The triad itself is rotation invariant because the phases `a`, `b`, and `-(a+b)` sum to zero, so Haar rotational symmetry does not by itself force its mean to vanish. The zero comes from low-degree power-sum/partition orthogonality.

## 3. Exact variance and deterministic normalization

The squared modulus is

`|B_(a,b)|^2`
` = p_a p_b p_(a+b) overline(p_a p_b p_(a+b))`.

Its positive and negative exponent arrays agree. Their weighted degree is

`a+b+(a+b)=2(a+b)`.

Hence, when `2(a+b)<=N`, the trace-moment formula gives the standard partition factor

`z_lambda = product_j j^(m_j) m_j!`

for the partition

`lambda=(a,b,a+b)`.

If `a<b`, the three parts are distinct and

`z_lambda = a b (a+b)`.

If `a=b`, the part `a` occurs twice and the part `2a` once, so

`z_lambda = a^2 2! (2a) = 4a^3`.

Thus dividing by `sqrt(z_lambda)` stabilizes the CUE second moment exactly, not merely asymptotically. In particular, an `a_N,b_N=Theta(N)` triad does not acquire artificial growth after this normalization as long as `a_N+b_N<=N/2`.

## 4. Distinct frequency triangles are exactly orthogonal in the safe corridor

Consider

`E[B_(a,b) overline(B_(c,d))]`.

The positive compound power-sum partition is

`lambda=(a,b,c+d)`,

while the negative partition is

`mu=(a+b,c,d)`.

Both have weighted degree

`a+b+c+d`.

Inside the classical finite-size range, the moment can be nonzero only if these partitions are equal as multisets.

That equality forces the original unordered pairs to be the same. Indeed, equality of the sums of squares gives

`ab=cd`.

Equality of the products of the three multiset entries then gives

`ab(c+d)=cd(a+b)`.

Since all entries are positive and `ab=cd`, this implies

`a+b=c+d`.

The pairs `{a,b}` and `{c,d}` therefore have the same sum and product, so they are the same unordered pair.

Hence distinct unordered triads have exact zero conjugate covariance whenever

`a+b+c+d<=N`.

For the nonconjugated moment

`E[B_(a,b) B_(c,d)]`,

the positive exponent pattern contains four trace factors `p_a,p_b,p_c,p_d`, whereas the negative pattern contains only the two factors `p_(a+b),p_(c+d)`. The exponent arrays cannot agree: their total multiplicities are four and two. Therefore this moment is also exactly zero under the same weighted-degree condition.

If every panel member satisfies `a+b<=N/2`, any two panel members automatically satisfy the required joint degree bound. The whole normalized panel is therefore exactly second-order orthonormal, with zero pseudo-covariance, at finite `N`.

For real and imaginary parts this implies, coordinatewise,

`Var(Re W_(a,b)) = Var(Im W_(a,b)) = 1/2`

and zero second-order cross-covariance between distinct normalized triads. This is a covariance statement only; higher joint moments need their own degree accounting and do not justify calling the `W_(a,b)` independent complex Gaussians.

## 5. Prior art and novelty assessment

The decisive input is classical. Persi Diaconis and Mehrdad Shahshahani, **On the eigenvalues of random matrices**, *Journal of Applied Probability* 31A (1994), 49–62, DOI `10.1017/S0021900200106989`, derive the joint trace moments for Haar classical groups. Persi Diaconis and Steven N. Evans, **Linear functionals of eigenvalues of random matrices**, *Transactions of the American Mathematical Society* 353:7 (2001), 2615–2633, DOI `10.1090/S0002-9947-01-02800-8`, restate the unitary formula with the finite-size condition used above; their Theorem 2.1 is the exact source of the weighted-degree gate.

Higher-order spectral statistics and bispectral triads are also standard objects. The present result is only an elementary specialization of the classical CUE power-sum orthogonality to the frequency-conserving product `p_a p_b overline(p_(a+b))`, plus the elementary observation that the cross partitions `(a,b,c+d)` and `(a+b,c,d)` can coincide only for the same unordered frequency pair.

A targeted literature check found no basis for a novelty claim and none is made. The value here is operational: the accepted visual multiscale clue asked for a source-faithful finite-size null and amplitude normalization before looking for a higher-order source residual. This trace-bispectrum family supplies one exact CUE candidate where both are available analytically.

## Boundary and falsification

The exact identities require Haar CUE and the stated weighted-degree conditions. Outside those conditions the classical low-degree moment collapse no longer applies, and finite-`N` corrections or additional partition effects must be computed rather than extrapolated from this finding.

The statistic is a global Fourier/trace functional of CUE eigenangles. It is **not** the cyclic gap statistic calibrated in `VIS-115`–`VIS-117`, and it is not legitimate to transfer its variance directly to zeta gap triples. The change of observable is deliberate: the accepted multiscale clue allowed a predeclared growing-lag law **or an equivalent global higher-order functional**, and the trace triad has a much cleaner source-faithful CUE null.

The formulas are falsified by any Haar-unitary example within the low-degree corridor whose exact ensemble moment disagrees with the Diaconis–Shahshahani/Diaconis–Evans formula. Numerical Haar sampling can provide a sanity check, but the result itself is an exact literature specialization and does not depend on simulation.

## Visual consequence

No canonical PNG is retained. A heatmap of raw `|B_(a,b)|` would mix a deterministic frequency-dependent null amplitude `sqrt(z_(a,b))` with any source structure. The mathematically faithful view, if this channel is later rendered, is the normalized complex panel `W_(a,b)` or a derived statistic whose CUE second-order baseline is already the identity.

Likewise, a visually coherent ridge among low-degree CUE trace triads is not evidence merely because neighboring frequencies look organized. After the normalization above, second-order whitening is exact; any retained structure must be tested at higher order or against the corresponding predeclared source statistic.

## Research consequence

`VIS-117` closed the fixed-multiset shuffle covariance thread and explicitly left the finite-size source-faithful null as the next distinct boundary. The present finding crosses that boundary for one mathematically natural **global third-order spectral channel**: within `a+b<=N/2`, CUE provides exact centering, exact variance stabilization, and exact panel covariance without Monte Carlo.

This does **not** yet establish source specificity. Before inspecting zeta data, a later invocation must define and freeze the zeta-side counterpart: the zero window/unfolding or phase map, the frequency law `(a_N,b_N)`, the panel or pooled decision statistic, the treatment of finite-height deterministic corrections, and untouched confirmation windows. Only then can a zeta-versus-CUE residual be tested without choosing the observable after seeing the source.

Deriving that source-side dictionary is a separate research question and is intentionally left for a later invocation.