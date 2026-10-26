# WI-464 — full Euler correction has an integrable threshold primitive

**Status:** EXACT-DERIVED + CLASSICAL-TRANSPORT-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-462](WI-462-prime-power-coherence-lowers-the-zero-sampled-euler-response-mean.md), for the coherent response and first mean coefficient; [WI-463](WI-463-first-euler-threshold-correction-exceeds-logarithmic-bracket-bandwidth.md), for finite-panel signed threshold coefficients and their separate arithmetic transport obstruction.

## Claim and evidence boundary

Fix `epsilon,r>0`. The finite-prime-panel signed threshold coefficients
of the coherent Euler–Hankel response converge in `L^1([0,1])` as the
prime-power cutoff is removed. The limit is independent of the finite
exhaustion, and the proof gives an explicit error bound in the omitted
Euler coefficient mass. Its integral equals the positive mean-bias
coefficient `B_epsilon(r)` of WI-462.

This limit exists even though the prescribed finite-panel correction
densities cannot be the marginals of **any finite signed Borel measure on
the infinite prime torus**. The correct guaranteed scalar object is an
integrable cumulative coefficient, or equivalently its distributional
derivative acting on Lipschitz observables. We do not prove that this
derivative is a finite signed measure on the response interval.

These are statements about the candidate coefficient derived from the
prime-axis character corrections. They do not prove an actual first
zero-sampling asymptotic for a threshold, or even convergence of the
finite coefficients at every fixed threshold. WI-463's arithmetic
transport obstruction remains intact.

## Definitions and the summable coordinate budget

Set `sigma=1+epsilon` and use the original normalization

\[
 A=A_\varepsilon=-\zeta'(1+\varepsilon)/\zeta(1+\varepsilon),
 \qquad a_{p^k}=\frac{\log p}{A p^{k\sigma}},
 \qquad \sum_{p,k\ge1}a_{p^k}=1.
 \tag{1}
\]

On the product of angle circles, with product probability Haar measure
`m`, let `z_p=exp(i theta_p)` and

\[
 V(z)=\sum_{p,k\ge1}a_{p^k}z_p^k v_{p^k},\qquad
 Q(z)=\|V(z)\|^2,
 \quad
 \langle v_n,v_m\rangle
 =e^{-r|\log(n/m)|}-(nm)^{-r}.
 \tag{2}
\]

These are the negative-Hardy tone vectors of WI-462. In particular,
`||v_n||<=1`, the vector series converges uniformly, and `0<=Q<=1`.
For a finite set `F` of prime powers, retain only those terms in (2),
obtaining `V_F,Q_F`, without renormalizing. Put

\[
 \delta_F=\sum_{p^k\notin F}a_{p^k},\qquad
 w_p=\sum_{k\ge1}a_{p^k}
     =\frac{\log p}{A(p^\sigma-1)}.
 \tag{3}
\]

Then `||Q-Q_F||_infinity<=2 delta_F`. Deleting all powers of one prime
from `V` gives a response `Q^{(-p)}` independent of `z_p`, with
`||Q-Q^{(-p)}||_infinity<=2w_p`. The same deletion bound holds for
every `Q_F` with the smaller retained mass, hence also with `w_p`.

The one-coordinate signed density is

\[
 h_p(z_p)=-\log p\,[K_{p^{-1/2}}(\theta_p)-1],\qquad
 K_u(\theta)=\frac{1-u^2}{1-2u\cos\theta+u^2}.
 \tag{4}
\]

Its integral is zero. The absolutely convergent Fourier expansion gives

\[
 h_p=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta_p),
 \quad
 \|h_p\|_1\le b_p:=\frac{2\log p}{\sqrt p-1}.
 \tag{5}
\]

The central budget is

\[
 \boxed{S_\varepsilon:=\sum_p w_pb_p<\infty.}
 \tag{6}
\]

Indeed `w_p b_p <<_epsilon (log p)^2 p^{-3/2-epsilon}`;
even summing this majorant over all integers converges. No prime number
theorem or zero hypothesis is needed for this estimate.

For `P(F)={p: p^k in F for some k}`, define

\[
 h_F=\sum_{p\in P(F)}h_p,\qquad
 C_F(t)=\int\mathbf1_{\{Q_F\le t\}}h_F\,dm,
 \quad 0\le t\le1.
 \tag{7}
\]

This agrees with WI-463's coefficient at an initial cutoff. Including
additional unused prime coordinates in `h_F` has no effect, since their
densities have mean zero and `Q_F` is independent of them.

## Integrating the threshold removes the discontinuity cost

For any `x,y in [0,1]`,

\[
 \int_0^1|\mathbf1_{x\le t}-\mathbf1_{y\le t}|\,dt=|x-y|.
 \tag{8}
\]

For each prime define

\[
 C_p(t)=\int\mathbf1_{\{Q\le t\}}h_p\,dm
 =\int(\mathbf1_{\{Q\le t\}}
       -\mathbf1_{\{Q^{(-p)}\le t\}})h_p\,dm.
 \tag{9}
\]

The subtracted term integrates to zero by coordinate independence, not
by any independence assumption about `Q` itself. Tonelli's theorem,
(8), and the deletion bound give

\[
 \|C_p\|_{L^1(0,1)}\le2w_pb_p.
 \tag{10}
\]

Consequently

\[
 \boxed{C:=\sum_p C_p\ \text{converges absolutely in }L^1(0,1),
 \qquad \|C\|_1\le2S_\varepsilon.}
 \tag{11}
\]

The prime series also converges absolutely for Lebesgue-almost every
threshold, by integrating its absolute sum. This defines an `L^1`
equivalence class; it does not select a value at every prescribed level.

Write `C_{F,p}(t)=integral 1_{Q_F<=t} h_p dm` for every prime, including
those not represented in `F`, for which this is zero. Direct comparison
of `Q_F` with `Q`, and separately deletion of the `p` coordinate, yield

\[
 \|C_{F,p}-C_p\|_1
 \le \min\{2\delta_F b_p,\ 4w_pb_p\}.
 \tag{12}
\]

Thus, for every `R>=2`,

\[
 \boxed{\|C_F-C\|_1
 \le 2\delta_F\sum_{p\le R}b_p
       +4\sum_{p>R}w_pb_p.}
 \tag{13}
\]

First choose `R` large using (6), then send `delta_F` to zero. This proves
convergence for every finite exhaustion whose omitted coefficient mass
tends to zero, without monotonicity or a particular ordering of primes.
The cancellation is essential: the cruder bound
`delta_F ||h_F||_1` need not be useful.

There is also a convenient nonsharp rate. Integer-sum comparison gives

\[
 \sum_{p\le R}b_p\ll\sqrt R\log(2R),\qquad
 \sum_{p>R}w_pb_p
 \ll_\varepsilon R^{-\varepsilon-1/2}(\log(2R))^2.
\]

For sufficiently small positive `delta_F`, take
`R=delta_F^{-1/(1+epsilon)}` in (13). With
`kappa=(epsilon+1/2)/(epsilon+1)`,

\[
 \|C_F-C\|_1
 \ll_\varepsilon
 \delta_F^{\kappa}\bigl(\log(2/\delta_F)\bigr)^2.
 \tag{14}
\]

For the initial cutoff `F={p^k<=M}`, one may use WI-462's elementary
`delta_F <<_epsilon M^{-epsilon} log(2M)`. These estimates are at fixed
positive `epsilon`; no uniform passage to the pole is claimed.

## What this coefficient acts on

For every real Lipschitz function `f` on `[0,1]`, integration of
`f(x)=f(1)-integral_x^1 f'(t)dt` against the zero-mass finite density gives

\[
 \int f(Q_F)h_F\,dm=-\int_0^1 f'(t)C_F(t)\,dt
 \longrightarrow
 \mathcal L(f):=-\int_0^1 f'(t)C(t)\,dt.
 \tag{15}
\]

The convergence is uniform over functions with Lipschitz constant at most
one. In fact its operator norm is exactly `||C_F-C||_1`: the upper bound
is immediate, and a primitive of `sign(C_F-C)` attains it, up to sign.
The limiting functional annihilates constants and is represented by the
distributional derivative of `C`, extended by zero outside `[0,1]`.

For `f(x)=x`, direct Haar orthogonality in (2), (4) leaves exactly pairs
of distinct powers of the same prime. Therefore

\[
 \mathcal L(x)=-B_\varepsilon(r),\qquad
 \boxed{\int_0^1C(t)\,dt=B_\varepsilon(r)>0,}
 \tag{16}
\]

where, writing `G_r(n,m)=<v_n,v_m>`,

\[
 B_\varepsilon(r)
 =2\sum_p\sum_{\ell,j\ge1}
 a_{p^{\ell+j}}a_{p^\ell}G_r(p^{\ell+j},p^\ell)
 (\log p)p^{-j/2}.
 \tag{17}
\]

This is precisely WI-462's convergent positive series. It is a sign and
normalization check, not a proof that `C(t)>=0` almost everywhere.
For the prime-only response, common rotation of every retained `z_p`
preserves `Q_F` and kills every `h_p`. Hence all `C_F`, and their limit,
vanish in that control. Prime-power coherence remains necessary for the
nonzero integrated coefficient.

## Why a global finite signed torus measure is impossible

For a finite prime set `P`, the proposed density on its torus is
`H_P=sum_{p in P} h_p`. These densities are consistent under coordinate
projection. Nevertheless their total variation is unbounded.

Under product Haar measure the variables `h_p` are independent and
centered. Fourier orthogonality gives

\[
 V_P:=\mathbb E H_P^2
 =\sum_{p\in P}\frac{2(\log p)^2}{p-1}.
 \tag{18}
\]

For an exhaustion of all primes, `V_P` tends to infinity, already by
Euler's divergence of `sum_p 1/p`. On the other hand,
`sup_p ||h_p||_infinity<=sup_p b_p=:K<infinity`. Independence yields

\[
 \mathbb E H_P^4
 =\sum_p\mathbb E h_p^4
   +6\sum_{p<q}(\mathbb E h_p^2)(\mathbb E h_q^2)
 \le K^2V_P+3V_P^2.
 \tag{19}
\]

Hölder interpolation between `L^1,L^2,L^4` now implies

\[
 \|H_P\|_1\ge
 \frac{(\mathbb E H_P^2)^{3/2}}{(\mathbb E H_P^4)^{1/2}}
 \ge\frac{V_P}{\sqrt{K^2+3V_P}}\longrightarrow\infty.
 \tag{20}
\]

If a finite signed Borel measure on the full prime torus had all these
marginals, each marginal's total variation would be bounded by the total
variation of that measure, contradicting (20). In particular, there is
no integrable infinite-torus density with the prescribed marginals.
This argument does **not** rule out a finite signed measure after the
many-to-one projection to `Q`; proving or disproving that stronger scalar
regularity requires another argument.

## Prior art, stress tests, and consequence

The one-coordinate densities are the classical Landau/Ford–Zaharescu
prime-axis corrections. [Ford–Zaharescu, equations (1.9)–(1.10) and
Corollary 2](https://ford126.web.illinois.edu/wwwpapers/fz.pdf) use
normalization by `T`; multiplying their density by `2 pi` gives (4) for
the `log T / D_T` normalization, where `D_T=N(2T)-N(T)` counts all
nontrivial zeros in that ordinate interval with multiplicity. Their fixed smooth-test theorem
does not itself justify the infinite-panel or indicator passage.

The integrated-distribution-function identity behind (8), (15) is
classical one-dimensional transport: S. S. Vallender, *Calculation of the
Wasserstein Distance Between Probability Distributions on the Line*,
**Theory Probab. Appl. 18** (1974), 784–786,
[DOI 10.1137/1118101](https://doi.org/10.1137/1118101).
Completion of zero-mass signed measures in the Kantorovich norm can
produce derivatives of `L^1` functions rather than finite measures;
see G. Bouchitté, T. Champion and C. Jimenez, *Completion of the space of
measures in the Kantorovich norm*, **Riv. Mat. Univ. Parma (7) 4\*** (2005),
127–139, [Theorem 2.4](https://cvgmt.sns.it/media/doc/paper/3623/Parma-last.pdf).
We prove the needed one-dimensional identities directly. The general
functional-analytic mechanism and fourth-moment interpolation are not
new. The local delta is the verified summable prime-coordinate budget,
the exhaustion-independent full Euler coefficient with (13), and the
simultaneous exclusion of a global finite signed torus measure.

The proof does not rely on regular values or an anti-concentration bound
for `Q`. Equation (8) charges a displaced threshold by the length of its
displacement, so even atoms would not invalidate the `L^1` conclusion.
Conversely, integrated convergence cannot be evaluated at a preselected
threshold: a continuous triangular spike of height one and width tending
to zero already shows this logical gap. Nor is convergence in the
Lipschitz-dual norm convergence in total variation.

The bounds hold uniformly in `r` at fixed `epsilon` because only
`||v_n||<=1` was used; they provide no uniform arithmetic height estimate.
All cutoff limits above concern explicit Haar coefficients. No limit in
zero-sampling height has been exchanged with them. The established mean
case (16) remains the separately proved arithmetic statement of WI-462.

Thus the infinite candidate coefficient need not be abandoned merely
because its torus density cannot exist. It has a precise weaker
representation with a controlled cutoff error. Identifying actual
zero-sampled first corrections with this object, obtaining its value or
sign at every threshold, and isolating individual off-line zeros all
remain unproved. No improved critical-line proportion or RH conclusion
follows.
