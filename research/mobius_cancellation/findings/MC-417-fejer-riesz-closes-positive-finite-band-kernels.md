# MC-417 — Fejér–Riesz closes the positive finite-band kernel escape

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-416` proves that changing the signs or phases of one finite linear filter before squaring cannot reduce the normalized zero-shift burden below the ordinary constant window. The same obstruction in fact covers **every scalar translation-invariant positive quadratic correlation kernel of finite bandwidth**, whether or not it is initially presented as one filter, many filters, a Toeplitz form, or a positive trigonometric polynomial.

Let

\[
a_n=0\qquad(n\notin[1,N]),
\qquad
S=\sum_n a_n,
\qquad
C_h=\sum_n a_{n+h}\overline{a_n}.
\tag{1}
\]

Fix a Hermitian kernel `K` supported on `|h|<H`, and write its symbol

\[
P_K(\theta)
:=
\sum_{|h|<H}K(h)e(h\theta).
\tag{2}
\]

Assume

\[
P_K(\theta)\ge 0
\qquad\text{for every }\theta\in\mathbb R/\mathbb Z.
\tag{3}
\]

Then the correlation form

\[
E_K
:=
\sum_{|h|<H}K(h)C_h
=
\int_0^1 |A(\theta)|^2P_K(\theta)\,d\theta,
\qquad
A(\theta)=\sum_n a_ne(n\theta),
\tag{4}
\]

is nonnegative for every finitely supported sequence `a`.

If the kernel has nonzero DC response

\[
P_K(0)>0,
\tag{5}
\]

then

\[
\boxed{
\frac{K(0)}{P_K(0)}\ge \frac1H.
}
\tag{6}
\]

Equivalently, after normalizing `P_K(0)=1`, every positive bandwidth-`H` shift kernel must retain zero-shift coefficient at least `1/H`.

Moreover, equality in `(6)` is attained only by a scalar multiple of the ordinary Fejér kernel,

\[
P_K(\theta)
=
\alpha\left|\sum_{j=0}^{H-1}e(j\theta)\right|^2,
\qquad \alpha>0,
\tag{7}
\]

up to the irrelevant common phase of its spectral factor. Thus the standard constant sliding window is not merely optimal among single filters as in `MC-416`; it is extremal in the full cone of scalar positive finite-band translation-invariant quadratic shift energies with the same bandwidth.

By Fejér–Riesz factorization, `(3)` gives coefficients `c_0,...,c_(H-1)` such that

\[
P_K(\theta)
=
\left|\sum_{j=0}^{H-1}c_je(j\theta)\right|^2.
\tag{8}
\]

Consequently

\[
K(0)=\sum_{j=0}^{H-1}|c_j|^2,
\qquad
P_K(0)=\left|\sum_{j=0}^{H-1}c_j\right|^2,
\tag{9}
\]

and `(6)` is exactly Cauchy–Schwarz.

The factorization also imports the reconstruction inequality from `MC-416` without choosing a preferred realization of the kernel. Since at most `N+H-1` translated windows are nonzero,

\[
\boxed{
|S|^2
\le
\frac{N+H-1}{P_K(0)}E_K.
}
\tag{10}
\]

The zero-shift contribution on the right side of `(10)` is therefore

\[
(N+H-1)\frac{K(0)}{P_K(0)}C_0
\ge
\frac{N+H-1}{H}C_0.
\tag{11}
\]

For the well-factorable upper-sieve sequence of `MC-409`–`MC-416`, `C_0` is precisely the re-squared lcm diagonal identified in `MC-415`. Hence **no positive scalar finite-band translation-invariant quadratic kernel can reduce the normalized lcm diagonal below the ordinary Fejér/constant-window value while retaining a nonzero response to the global sum**.

This closes a larger escape than `MC-416`: replacing one filter by a filter bank, a positive Toeplitz kernel, a sum of positive quadratic shift energies, or another scalar nonnegative trigonometric multiplier cannot improve the diagonal/DC ratio. Any surviving route must leave this cone—for example through an indefinite signed correlation identity with independently controlled negative part, a nonstationary/modulus-factorized differencing scheme, or a genuinely higher-dimensional arithmetic object whose positivity is not scalar finite-band Toeplitz positivity.

No improved character-sum estimate, source-depth exponent, Mertens bound, or RH consequence follows.

## 1. Positive finite-band kernels are single-filter energies

The classical Fejér–Riesz theorem states that a scalar nonnegative trigonometric polynomial of degree at most `H-1` factors as the modulus square of an analytic polynomial of degree at most `H-1`. Applying it to `(2)`–`(3)` gives `(8)`.

Expanding `(8)`,

\[
K(h)
=
\sum_{\substack{0\le j,k<H\\j-k=h}}
c_j\overline{c_k}.
\tag{12}
\]

Thus every positive scalar finite-band kernel is exactly an autocorrelation kernel of the type denoted `K_c` in `MC-416`. In particular, introducing several positive filters does not enlarge the scalar cone: if

\[
P(\theta)=\sum_{r=1}^R
\left|\sum_{j=0}^{H-1}c_{r,j}e(j\theta)\right|^2,
\tag{13}
\]

then `P` is one nonnegative trigonometric polynomial and therefore has a single Fejér–Riesz spectral factor of the same degree bound.

This is the precise sense in which a positive filter bank, positive Toeplitz form, or sum-of-squares presentation is only a different realization of the same scalar shift kernel.

## 2. The DC/diagonal extremal inequality

Evaluating `(8)` at zero and reading the constant Fourier coefficient gives `(9)`. Cauchy–Schwarz yields

\[
\left|\sum_{j=0}^{H-1}c_j\right|^2
\le
H\sum_{j=0}^{H-1}|c_j|^2,
\tag{14}
\]

which is `(6)`.

Equality in `(14)` holds exactly when

\[
c_0=c_1=\cdots=c_{H-1}
\tag{15}
\]

up to one common complex scalar. Substituting `(15)` into `(8)` gives `(7)`. Therefore the Fejér kernel is the unique extremizer at the level of the scalar symbol.

If the actual support has degree `m<H-1`, the sharper bound is

\[
\frac{K(0)}{P_K(0)}\ge\frac1{m+1},
\tag{16}
\]

so padding a shorter kernel with zero coefficients cannot fake an improvement.

The inequality `(6)` can also be read as a finite-band uncertainty statement: a nonnegative shift multiplier that couples strongly to frequency zero must pay at least reciprocal-bandwidth mass in its average Fourier coefficient `K(0)`. Here that average coefficient is exactly the correlation diagonal.

## 3. Reconstruction and the unavoidable diagonal

Let the Fejér–Riesz factor from `(8)` be `c`, and define

\[
B_t=\sum_{j=0}^{H-1}c_j a_{t+j}.
\tag{17}
\]

As in `MC-416`, zero extension gives

\[
\sum_t B_t
=
\left(\sum_j c_j\right)S.
\tag{18}
\]

At most `N+H-1` values of `t` contribute. Hence

\[
P_K(0)|S|^2
=
\left|\sum_tB_t\right|^2
\le
(N+H-1)\sum_t|B_t|^2.
\tag{19}
\]

The final energy is

\[
\sum_t|B_t|^2
=
\sum_hK(h)C_h
=E_K,
\tag{20}
\]

which proves `(10)`.

The `h=0` term of `E_K` is `K(0)C_0`. Inserting `(6)` gives `(11)`. This lower bound is independent of which spectral factor or sum-of-squares presentation was used to discover the kernel.

For the upper-sieve weight `a_n=w(n)\chi(n)` from `MC-415`,

\[
C_0
=
\sum_{n\le N}|w(n)\chi(n)|^2
\tag{21}
\]

and the exact divisor expansion of `MC-415` gives

\[
|w(n)|^2
=
\sum_{\ell\mid n}C_\lambda(\ell).
\tag{22}
\]

Therefore every positive scalar finite-band shift kernel carries at least the Fejér-normalized amount of the same lcm-fiber diagonal. Repackaging the positive quadratic step cannot make that arithmetic cost disappear.

## 4. What this does and does not rule out

The obstruction applies simultaneously to several apparently different variants:

- one signed or oscillatory finite filter followed by a norm square;
- a finite bank of such filters with positive summed energies;
- any scalar positive semidefinite Toeplitz/translation-invariant band kernel;
- any nonnegative trigonometric multiplier of degree at most `H-1` used as the positive correlation weight.

They are all the same cone after Fejér–Riesz factorization, and `(6)` is the cone-wide diagonal/DC lower bound.

The obstruction does **not** cover:

- an indefinite signed correlation form whose negative contribution is controlled by separate arithmetic information;
- a nonstationary kernel depending on the position `n` as well as the shift `h`;
- a modulus-factorized `A`-process whose state changes between differencing stages;
- operator- or matrix-valued positivity in which additional arithmetic coordinates survive and are used before scalarization;
- an off-diagonal theorem strong enough to compensate for the unavoidable diagonal rather than attempting to remove it.

Those are mathematically different obligations. Calling one of them “weighted van der Corput” is not enough: to evade `(6)` it must genuinely leave scalar finite-band translation-invariant positivity.

## 5. Prior art and novelty boundary

The factorization step is classical Fejér–Riesz theory, not a new theorem. A standard authoritative statement is the *Encyclopedia of Mathematics* entry “Fejér–Riesz theorem,” which states that every scalar nonnegative trigonometric polynomial factors as `|p(e^{it})|^2`. Modern operator-valued treatments likewise take this one-variable factorization as the classical base case; see, for example, the discussion preceding Theorem 1.1 in *Factoring non-negative operator valued trigonometric polynomials in two variables*, Mathematische Annalen (2024), DOI `10.1007/s00208-024-02895-9`.

The extremal estimate `(14)` is elementary Cauchy–Schwarz after factorization. It is also consistent with the classical extremal theory of nonnegative trigonometric polynomials and Fejér kernels; no novelty is claimed for that inequality or for the equality case in isolation.

A targeted literature audit on 20 September 2026 found the factorization and positive-trigonometric-polynomial extremal setting as standard prior art. The durable Mathia contribution is the research-frontier classification relative to `MC-409`–`MC-416`: once the source-frame route enters **any** scalar positive finite-band translation-invariant quadratic shift energy, the ordinary Fejér diagonal budget is already optimal and cannot be reduced by changing the positive kernel realization.

## Boundaries and falsification tests

- **Positivity is load-bearing.** If `P_K` changes sign, Fejér–Riesz does not apply in the form used here and cancellation between diagonal/off-diagonal contributions may become possible. Such a route must independently control the resulting indefinite form.
- **Scalarity is load-bearing.** Matrix/operator-valued kernels can retain additional coordinates. They do not automatically evade the obstruction, but they require a separate compression/positivity analysis rather than the scalar argument above.
- **Translation invariance is load-bearing.** A kernel `K_n(h)` depending on the base point may not have one scalar trigonometric symbol. Any claimed escape should exhibit the exact nonstationary structure rather than merely relabel a stationary kernel.
- **Finite bandwidth fixes the constant.** The ratio `1/H` is tied to at most `H` filter taps. An infinite-support kernel needs its own normalization/convergence analysis and cannot inherit an improved finite-band ratio by truncation without accounting for tails.
- **The theorem does not bound the off-diagonal.** It proves only a lower bound on the unavoidable normalized diagonal/DC cost. The incomplete translated correlations isolated in `MC-413`–`MC-414` remain live.
- **No first-moment substitution is allowed.** For the sieve route, the diagonal is still the second-moment/lcm object of `MC-415`; the first-moment majorant estimate from `MC-409` does not replace it.
- **No RH-scale information is imported.** The derivation uses only finite Fourier algebra, Fejér–Riesz factorization, Cauchy–Schwarz, and the already finite lcm identity from `MC-415`.

## Consequence for the research line

`MC-416` closes signed phases inside one positive filter. The present result closes the remaining scalar positive-kernel enlargement: filter banks, positive Toeplitz kernels, and nonnegative finite-band correlation multipliers cannot improve the diagonal/DC tradeoff either.

The `MC-409` route therefore has a sharper fork. Either obtain enough off-diagonal arithmetic cancellation to pay the Fejér-optimal diagonal, or change the architecture before scalar positive quadratic closure. The most concrete live escapes are now an **indefinite but arithmetically controlled correlation identity**, a **nonstationary/modulus-factorized differencing scheme**, or a **higher-dimensional retained arithmetic state** that is used before scalarization. A future candidate that remains a scalar positive finite-band translation-invariant kernel is already classified by `(6)` and should not be counted as a new escape.