# ANF-151 — a growing Hardy--Littlewood local hierarchy still leaves the bow diagonal intact

**Status:** `EXACT-DERIVED + PROBABILISTIC-MATCHED-CONTROL + GROWING-K-TUPLE-LOCAL-PROFILE + SOURCE-SPECIFIC-GATE + NO-ACTUAL-PRIME-CORRELATION-CLAIM`. `ANF-150` showed that the sieved-Cramer control can reproduce the complete finite-Ramanujan **pair** profile while its centered residual has purely diagonal bow variance in expectation. The same control is substantially stronger than that pair calculation suggests. For every distinct shift set `H={h_1,...,h_k}`, all uncentered `k`-point moments reproduce the exact truncated Hardy--Littlewood singular series attached to the same MRSTT sieve. Moreover, uniformly for every `H` of diameter at most the bow length, that truncated product agrees relatively with the full Hardy--Littlewood singular series whenever `k^2 log X/(R log R)=o(1)`; in particular this holds simultaneously for every `k<=R^{1/3}`, where `R=exp((log X)^{1/10})`. Yet the centered two-point covariance of the model is still identically zero and its expected bow variance remains `(1+o(1))XK log X`. Hence neither the pair singular series nor any fixed-order Hardy--Littlewood hierarchy, nor even a slowly growing hierarchy of local Euler-product main terms, can by itself supply the anti-Bernoulli sign required at the distinguished twist. The missing source information must live in centered correlation/error structure that is invisible to those local main terms.

## 1. The ANF-150 control matches every truncated local k-tuple profile exactly

Retain the MRSTT scale and rough model

\[
R=\exp((\log X)^{1/10}),\qquad
P=\prod_{p<R}p,\qquad
c_R=\frac{P}{\varphi(P)},
\tag{1}
\]

and

\[
Q_R(n)=c_R\,1_{(n,P)=1}.
\tag{2}
\]

As in `ANF-150`, independently for every integer `n\asymp X` let

\[
B_n\sim \operatorname{Bernoulli}\!\left(
1_{(n,P)=1}\frac{c_R}{\log n}
\right),
\qquad
\vartheta_R^{\rm rnd}(n):=(\log n)B_n.
\tag{3}
\]

For large `X` the probability in (3) is valid because `c_R\asymp\log R=o(\log X)`. Pointwise,

\[
\boxed{\mathbb E\,\vartheta_R^{\rm rnd}(n)=Q_R(n).}
\tag{4}
\]

Now let

\[
\mathcal H=\{h_1,\ldots,h_k\}
\tag{5}
\]

be any set of `k` **distinct** integer shifts, and write

\[
\nu_p(\mathcal H):=|\mathcal H\bmod p|.
\tag{6}
\]

Whenever the sites `n+h_j` lie in the dyadic region on which (3) is defined, independence and (4) give the exact identity

\[
\boxed{
\mathbb E\prod_{j=1}^{k}\vartheta_R^{\rm rnd}(n+h_j)
=
\prod_{j=1}^{k}Q_R(n+h_j).
}
\tag{7}
\]

Average the right side over any complete residue period modulo `P`. For each prime `p<R`, exactly `\nu_p(\mathcal H)` residue classes of `n` are forbidden. The Chinese remainder theorem therefore gives

\[
\begin{aligned}
\frac1P\sum_{n\bmod P}
\prod_{j=1}^{k}Q_R(n+h_j)
&=
\prod_{p<R}
\left(1-\frac{\nu_p(\mathcal H)}p\right)
\left(1-\frac1p\right)^{-k}\\
&=:\mathfrak S_R(\mathcal H).
\end{aligned}
\tag{8}
\]

Thus

\[
\boxed{
\frac1P\sum_{n\bmod P}
\mathbb E\prod_{j=1}^{k}\vartheta_R^{\rm rnd}(n+h_j)
=\mathfrak S_R(\mathcal H)
}
\tag{9}
\]

for every finite distinct shift set. Equation (9) is the exact `k`-tuple extension of the pair identity in `ANF-150`. It includes all small-prime admissibility constraints simultaneously; if some `p<R` has `\nu_p(\mathcal H)=p`, both sides vanish.

This statement concerns the local Euler-product profile. It does **not** replace the complete-period average in (9) by an interval average on `[X,2X]`, and it does not assert a Hardy--Littlewood theorem for the actual primes.

## 2. The truncation remains relatively exact through a growing range of tuple orders

Let the full Hardy--Littlewood singular series of the finite set `\mathcal H` be

\[
\mathfrak S(\mathcal H)
:=
\prod_p
\left(1-\frac{\nu_p(\mathcal H)}p\right)
\left(1-\frac1p\right)^{-k}.
\tag{10}
\]

Assume that the shifts are distinct and lie in an interval of diameter at most `K`, with `K<=X`. If `\mathfrak S_R(\mathcal H)=0`, then the same small prime already forces `\mathfrak S(\mathcal H)=0`, so there is nothing to compare. Suppose henceforth that `\mathfrak S_R(\mathcal H)>0`.

For `p>=R`, put

\[
\delta_p:=k-\nu_p(\mathcal H)\ge0.
\tag{11}
\]

If `R>2k`, Taylor expansion is uniform because `\nu_p(\mathcal H)/p<=1/2`, and the missing local factor satisfies

\[
\begin{aligned}
\log\left[
\left(1-\frac{\nu_p(\mathcal H)}p\right)
\left(1-\frac1p\right)^{-k}
\right]
&=
\frac{\delta_p}{p}
+O\!\left(\frac{k^2}{p^2}\right).
\end{aligned}
\tag{12}
\]

The collision multiplicity `\delta_p` is controlled by pair differences. Partition the shifts into residue classes modulo `p`. If those class sizes are `s_1,\ldots,s_\nu`, then

\[
\delta_p
=\sum_a(s_a-1)
\le
\sum_a\binom{s_a}{2}
=\#\{i<j:p\mid h_i-h_j\}.
\tag{13}
\]

For any nonzero difference `d` with `|d|<=K`,

\[
\sum_{\substack{p>=R\\p\mid d}}\frac1p
\le
\frac1R\,\#\{p>=R:p\mid d\}
\le
\frac{\log(2K)}{R\log R}.
\tag{14}
\]

Summing (13)--(14) over all pairs gives

\[
\sum_{p>=R}\frac{\delta_p}{p}
\ll
\frac{k^2\log(2K)}{R\log R}.
\tag{15}
\]

The quadratic Taylor remainder is even simpler:

\[
\sum_{p>=R}\frac{k^2}{p^2}
\le
k^2\sum_{n>=R}\frac1{n^2}
\ll \frac{k^2}{R}.
\tag{16}
\]

Combining (12), (15), and (16) yields the uniform pointwise tail bound

\[
\boxed{
\left|
\log\frac{\mathfrak S(\mathcal H)}{\mathfrak S_R(\mathcal H)}
\right|
\ll
\frac{k^2}{R}
+
\frac{k^2\log(2K)}{R\log R}.
}
\tag{17}
\]

Consequently, throughout the bow range `K<=X`, if

\[
\boxed{
\frac{k^2\log X}{R\log R}=o(1),
}
\tag{18}
\]

then uniformly over every distinct `\mathcal H` of diameter at most `K`,

\[
\boxed{
\mathfrak S(\mathcal H)
=\mathfrak S_R(\mathcal H)(1+o(1))
}
\tag{19}
\]

whenever the series is nonzero, while inadmissible tuples vanish identically on both sides. Condition (18) automatically implies `k=o(R)`, so the expansion used above is self-consistent.

There is a convenient concrete corollary. Since `R=exp((log X)^{1/10})`,

\[
\frac{R^{2/3}\log X}{R\log R}
=
\frac{\log X}{R^{1/3}\log R}
\longrightarrow0.
\tag{20}
\]

Hence (19) holds simultaneously for

\[
\boxed{k\le R^{1/3}=\exp\!\left(\frac13(\log X)^{1/10}\right),}
\tag{21}
\]

a tuple order that tends to infinity faster than every fixed power of `\log X` only at the eventual asymptotic scale dictated by (21). More generally the sharp information from this argument is the condition (18), not the illustrative exponent `1/3`.

## 3. Matching that entire local hierarchy does not change the bow variance

Center the same model exactly as in `ANF-150`,

\[
r_R^{\rm rnd}(n)
:=\vartheta_R^{\rm rnd}(n)-Q_R(n).
\tag{22}
\]

The random variables `r_R^{rnd}(n)` are independent and have mean zero. Therefore for **every** collection of distinct sites and every `k>=1`,

\[
\boxed{
\mathbb E\prod_{j=1}^{k}r_R^{\rm rnd}(n+h_j)=0.
}
\tag{23}
\]

In particular the off-diagonal covariance is identically zero. For the bow moving-window norm

\[
V_R^{\rm rnd}(U;K)
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+K}
r_R^{\rm rnd}(n)n^{-iU}
\right|^2dx,
\tag{24}
\]

opening the square and taking expectation leaves only the diagonal, exactly as in `ANF-150`:

\[
\mathbb E V_R^{\rm rnd}(U;K)
=
\sum_n\omega_K(n,n)
1_{(n,P)=1}\bigl(c_R\log n-c_R^2\bigr).
\tag{25}
\]

The rough-number density estimate already used there gives, for

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{26}
\]

\[
\boxed{
\mathbb E V_R^{\rm rnd}(U;K)
=(1+o(1))XK\log X
}
\tag{27}
\]

uniformly for every real `U`.

Equations (9), (19), and (27) can therefore hold simultaneously: the same source can reproduce the full small-prime `k`-tuple local profile through an order tending to infinity, with that truncated profile already relatively indistinguishable from the full Hardy--Littlewood Euler product on every bow-scale tuple, while the residual bow variance remains completely diagonal in expectation.

This sharply separates **uncentered local main terms** from **centered dependence**. The singular series tells us how often a collection of sites survives local congruence obstructions. It does not determine whether the centered post-sieve innovations at those sites have the negative phase-sensitive covariance needed to cancel the bow diagonal.

## 4. Fixed-order Hardy--Littlewood information cannot be the missing anti-Bernoulli input

For the actual source, `ANF-150` writes

\[
r_X(n)=Q_R(n)\eta_R(n),
\tag{28}
\]

where `\eta_R` is the deterministic centered prime-versus-composite innovation on the `R`-rough set. The bow target at a distinguished `U=U(X)` requires

\[
2\operatorname{Re}
\sum_{m<n}
Q_R(m)Q_R(n)\eta_R(m)\eta_R(n)
\left(\frac nm\right)^{-iU}
\omega_K(m,n)
=
-(1+o(1))XK\log X.
\tag{29}
\]

The matched control now passes a much stronger local test than the pair profile of `ANF-150`: all of its uncentered local `k`-tuple Euler products agree with the Hardy--Littlewood hierarchy through the growing range (18), yet the centered analogue of (29) has expectation zero.

Therefore a positive bow theorem cannot be obtained merely by stacking finitely many Hardy--Littlewood main-term formulas, nor by replacing the pair singular series with a bounded or slowly growing collection of higher local singular series. Any theorem whose source information reduces to the local admissibility products `\mathfrak S(\mathcal H)` in the range above is still satisfied by a control with no off-diagonal bow cancellation.

What remains available to the actual primes is more specific. It can lie in the **error terms around** those local main terms, in centered cumulants/correlations that survive after `Q_R` is subtracted, in dependencies on tuple order beyond the regime (18), or in long-range/bilinear structure aligned with the special logarithmic carrier. The present finding does not distinguish among those possibilities; it removes the local singular-series hierarchy itself as the missing sign mechanism.

## 5. Prior-art boundary and adversarial checks

The probabilistic mechanism is classical. Granville's refinement of Cramer's model first sieves by small primes and then chooses surviving integers independently with a renormalized probability. Banks, Ford and Tao, **Large prime gaps and probabilistic models**, *Inventiones Mathematicae* 233 (2023), 1471--1518, DOI `10.1007/s00222-023-01199-0`, explicitly recall that Granville's model captures the appropriate Hardy--Littlewood `k`-tuple analog for every fixed finite shift set. Jaeyoon Kim's **Prime Running Functions** gives essentially the same fixed-modulus conditional Bernoulli architecture used in `ANF-150`. Vivian Kuperberg's **Sums of singular series with large sets and the tail of the distribution of primes**, *Quarterly Journal of Mathematics* 74 (2023), 1457--1479, studies singular-series averages when the tuple order itself grows. Thus no novelty is claimed for sieved Cramer models, for Hardy--Littlewood singular series, or for the general fact that local sieving restores prime-tuple correction factors.

The Mathia-specific content is narrower: the exact MRSTT choice of `R`, the pointwise uniform tail estimate (17) on **every** bow-scale shift set in the growing range (18), and the simultaneous comparison with the exact moving-window bow residual (27). No external theorem is needed for (7)--(19) or for the covariance identity; the literature audit only places those elementary derivations inside their classical probabilistic-number-theory context. Accordingly no new theorem from that literature is used as a load-bearing dependency.

The main stress tests are:

- The shifts in `\mathcal H` must be distinct. Repeated sites introduce higher moments of one Bernoulli variable and are not covered by the factorization (7) or (23).
- Equation (9) is a complete-period/local-factor identity, not an actual short-interval prime `k`-tuple asymptotic. The comparison (19) is a comparison of Euler products only.
- The growth condition (18) matters. Nothing here says that local factors remain relatively matched for tuple orders comparable to `R`, `K`, or any polynomial power of `X`.
- The expected diagonal variance (27) is a matched-control obstruction, not a lower bound for the actual primes and not evidence that the distinguished bow cancellation fails.
- The control is deliberately independent after conditioning on the small-prime sieve. Actual primes may differ precisely through the centered error/cumulant structure that independence deletes.

These boundaries prevent the result from turning a local Euler-product calculation into a conjectural prime-correlation theorem.

## 6. Consequence for the analytic bow frontier

`ANF-149` identified `vartheta-Q_R` as the exact source-normal form, and `ANF-150` showed that the correct conditional prime density plus the complete pair singular series still leave the bow diagonal. The present result removes the next obvious escape: **higher local Hardy--Littlewood main terms do not repair that defect, even when their order is allowed to grow slowly with `X`.**

The useful next object is therefore not another singular-series main term. It is a signed estimate for the centered post-sieve innovation itself, retaining the distinguished phase before absolute values: a twisted covariance/error theorem, a bilinear representation that preserves its sign, or a genuinely nonlocal dependency of the actual primes that the conditioned independent model cannot reproduce. Any proposed route should be stress-tested against the control above; if its hypotheses are already encoded by the local hierarchy (9)--(19), it cannot force the required cancellation (29).