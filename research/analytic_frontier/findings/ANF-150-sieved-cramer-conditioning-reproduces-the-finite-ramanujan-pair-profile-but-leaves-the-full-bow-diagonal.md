# ANF-150 — sieved-Cramér conditioning reproduces the finite Ramanujan pair profile but leaves the full bow diagonal

**Status:** `EXACT-DERIVED + PROBABILISTIC-MATCHED-CONTROL + CLASSICAL-SIEVE + SOURCE-SPECIFIC-GATE + NO-ACTUAL-PRIME-CLAIM`. `ANF-149` reduces the live bow source to the fixed-sign residual `r_X=\vartheta-Q_R`, where `Q_R=\Lambda^\sharp` is the deterministic `R`-rough/Ramanujan counterterm. There is an exact conditional-primality normal form for this residual, and it exposes a stronger matched control. If one first sieves by the same primorial `P(R)` and then places independent pseudo-primes on the surviving integers with the correct conditional intensity `c_R/\log n`, the model reproduces `Q_R` as its exact first moment and reproduces the entire truncated Hardy--Littlewood/Ramanujan pair profile from `ANF-149` as its exact off-diagonal second moment. Nevertheless its expected bow variance is `(1+o(1))XK\log X`, uniformly in the twist `U`: every off-diagonal residual covariance vanishes and the full bow diagonal survives. Thus small-prime local factors plus the correct conditional prime density do not force the cancellation sought after `ANF-149`. A successful source theorem has to detect a genuinely **anti-Bernoulli correlation of actual primes inside the `R`-rough set at the distinguished logarithmic twist**.

## 1. The actual residual is exactly a conditional-primality innovation on the rough set

Retain the notation of `ANF-149`,

\[
P=P(R)=\prod_{p<R}p,
\qquad
c_R=\frac{P}{\varphi(P)},
\qquad
Q_R(n)=c_R\,1_{(n,P)=1},
\tag{1}
\]

with

\[
R=\exp((\log X)^{1/10}),
\qquad
r_X(n)=\vartheta(n)-Q_R(n).
\tag{2}
\]

On the bow support `n\asymp X` one has `n>R`. Every prime in that support is therefore automatically coprime to `P`. Put

\[
A_R(n):=1_{(n,P)=1}
\tag{3}
\]

and define the deterministic conditional-primality score

\[
\eta_R(n)
:=
A_R(n)\left(\frac{\vartheta(n)}{c_R}-1\right).
\tag{4}
\]

Then, pointwise on the whole bow support,

\[
\boxed{
r_X(n)=Q_R(n)\eta_R(n).
}
\tag{5}
\]

Indeed `A_R(n)\vartheta(n)=\vartheta(n)` there. On an `R`-rough prime,

\[
\eta_R(p)=\frac{\log p}{c_R}-1>0,
\tag{6}
\]

whereas on an `R`-rough composite

\[
\eta_R(n)=-1.
\tag{7}
\]

Outside the rough set both `Q_R` and `r_X` vanish after the prime-power reduction of `ANF-149` has replaced `\Lambda` by `\vartheta`.

Thus the four-term inclusion--exclusion ledger in `ANF-149` has an exact one-field form:

\[
\boxed{
r_X(n)r_X(m)
=Q_R(n)Q_R(m)\eta_R(n)\eta_R(m).
}
\tag{8}
\]

The deterministic factor `Q_R(n)Q_R(m)` carries the complete small-prime admissibility mask. The only remaining source information is how the two-valued prime/composite score `\eta_R` is actually arranged on that mask.

There is also a useful diagonal identity. Since `Q_R^2=c_RQ_R` and `\vartheta Q_R=c_R\vartheta` on the bow support,

\[
\boxed{
r_X(n)^2
=\vartheta(n)^2-2c_R\vartheta(n)+c_RQ_R(n).
}
\tag{9}
\]

This makes explicit why the diagonal remains prime-sized: `c_R=O(\log R)=o(\log X)`, while the `\vartheta^2` term has second moment `X\log X`.

## 2. The matching sieved-Cramér control reproduces the finite Ramanujan pair profile exactly

Now keep the same deterministic rough set and construct a probabilistic control. For every integer `n\asymp X`, independently let `B_n` be Bernoulli with

\[
\mathbb P(B_n=1)
=
\begin{cases}
\dfrac{c_R}{\log n},&(n,P)=1,\\[4pt]
0,&(n,P)>1.
\end{cases}
\tag{10}
\]

For large `X` this is a valid probability because `c_R=O((\log X)^{1/10})=o(\log X)`. Define the random prime field and its residual by

\[
\vartheta_R^{\rm rnd}(n):=(\log n)B_n,
\qquad
r_R^{\rm rnd}(n):=\vartheta_R^{\rm rnd}(n)-Q_R(n).
\tag{11}
\]

The normalization is exact, not asymptotic:

\[
\boxed{
\mathbb E\,\vartheta_R^{\rm rnd}(n)=Q_R(n),
\qquad
\mathbb E\,r_R^{\rm rnd}(n)=0.
}
\tag{12}
\]

For distinct `m,n`, independence therefore gives

\[
\boxed{
\mathbb E\!\left[r_R^{\rm rnd}(m)r_R^{\rm rnd}(n)\right]=0,
}
\tag{13}
\]

and equivalently

\[
\boxed{
\mathbb E\!\left[\vartheta_R^{\rm rnd}(m)\vartheta_R^{\rm rnd}(n)\right]
=Q_R(m)Q_R(n).
}
\tag{14}
\]

This is exactly the local profile isolated in `ANF-149`. Averaging (14) over one complete residue period in the first variable gives, for every nonzero shift `h`,

\[
\frac1P\sum_{n\bmod P}
\mathbb E\!\left[
\vartheta_R^{\rm rnd}(n)\vartheta_R^{\rm rnd}(n+h)
\right]
=
\frac1P\sum_{n\bmod P}Q_R(n)Q_R(n+h)
=
\boxed{\mathfrak S_R(h)}.
\tag{15}
\]

Hence the probabilistic control does not merely retain prime density or rough support. It reproduces **every small-prime pair factor `<R` simultaneously**, including the parity zero on odd lags and the exact truncated singular series on even lags. By `ANF-149`, `\mathfrak S_R(h)` already agrees with the full Hardy--Littlewood local product to relative `o(1)` on every even bow lag `h<K`.

The only place where the model deliberately differs from an actual prime process is the correlation of the conditional prime marks after small-prime sieving.

## 3. Its bow variance is exactly diagonal in expectation

For the same moving-window seminorm as `ANF-102` and `ANF-149`, put

\[
V_R^{\rm rnd}(U;K)
:=
\int_X^{2X}
\left|
\sum_{x<n\le x+K}
 r_R^{\rm rnd}(n)n^{-iU}
\right|^2dx.
\tag{16}
\]

Open the square using the exact overlap kernel `\omega_K(m,n)` of `ANF-102`. Equations (12)--(13) kill every off-diagonal term after expectation, for **every real `U`**. On the diagonal,

\[
\begin{aligned}
\mathbb E\!\left[(r_R^{\rm rnd}(n))^2\right]
&=
\operatorname{Var}(\vartheta_R^{\rm rnd}(n))\\
&=
A_R(n)\left(c_R\log n-c_R^2\right).
\end{aligned}
\tag{17}
\]

Therefore one has the finite-`X` identity

\[
\boxed{
\mathbb E\,V_R^{\rm rnd}(U;K)
=
\sum_n
\omega_K(n,n)
A_R(n)\left(c_R\log n-c_R^2\right),
}
\tag{18}
\]

which is independent of `U`.

At the bow scale

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{19}
\]

one has `K=o(X)`. The classical fundamental-lemma/Buchstab estimate for the sifted set, in the regime

\[
\frac{\log X}{\log R}=(\log X)^{9/10}\to\infty,
\tag{20}
\]

gives on any fixed dyadic bulk interval

\[
\#\{X<n\le2X:(n,P)=1\}
=(1+o(1))\frac{X}{c_R}.
\tag{21}
\]

The same asymptotic holds after deleting the `o(X)` bow edge strips. Since `\log n=\log X+O(1)` on the bulk and `c_R=o(\log X)`, the full-weight interior terms `\omega_K(n,n)=K` give the lower bound

\[
\mathbb E\,V_R^{\rm rnd}(U;K)
\ge
(1-o(1))XK\log X.
\tag{22}
\]

The support bound `\omega_K(n,n)\le K` and the same rough-number asymptotic on `(X,2X+K]` give the matching upper bound. Thus

\[
\boxed{
\mathbb E\,V_R^{\rm rnd}(U;K)
=(1+o(1))XK\log X
}
\tag{23}
\]

uniformly in every real twist `U`.

Since the random variable in (16) is nonnegative, (23) also implies that for every fixed `U` and large `X` there exists a deterministic realization of this sieved-prime model with

\[
\boxed{
V_R^{\rm rnd}(U;K)
\ge(1-o(1))XK\log X.
}
\tag{24}
\]

No generic geometric property of the moving window or logarithmic carrier can turn the local sieve model itself into the desired `o(XK\log X)` source.

## 4. The remaining theorem is anti-Bernoulli coherence after conditioning on the small-prime sieve

`ANF-148` showed that actual prime locations, prime density, real coefficients and logarithmic-size amplitudes do not determine the bow variance if the coefficient law is allowed to vary. `ANF-149` then recovered the genuine arithmetic law and showed that `Q_R` already packages essentially all finite local pair obstructions. The present control tests the next natural hypothesis: perhaps **small-prime sieving plus the correct conditional prime intensity and pair singular series** already force the required cancellation. Equations (13) and (23) show that they do not.

For the actual residual, equation (8) rewrites the off-diagonal ledger as

\[
2\operatorname{Re}
\sum_{m<n}
Q_R(m)Q_R(n)
\eta_R(m)\eta_R(n)
\left(\frac{n}{m}\right)^{-iU}
\omega_K(m,n).
\tag{25}
\]

The bow target can hold at a distinguished `U=U(X)` only if (25) is

\[
\boxed{
-(1+o(1))XK\log X,
}
\tag{26}
\]

because the diagonal remains `(1+o(1))XK\log X`. In the matched sieved-Cramér control, the expectation of (25) is identically zero term by term.

This isolates the source-specific information still missing after `ANF-149`: actual primes must exhibit a macroscopic **negative twisted covariance of the conditional innovation field `\eta_R` inside the `R`-rough pair mask**. It is not enough to know the one-point conditional probability `c_R/\log n`, the exact small-prime admissibility pattern, or the truncated Hardy--Littlewood singular series. Any proof that replaces the post-sieve prime marks by independent or merely locally calibrated marks has discarded precisely the sign needed to cancel the diagonal.

Equivalently, the useful analytic object is no longer four componentwise prime/rough correlations. It is the single centered covariance of the actual conditional-primality score against the deterministic positive base measure `Q_R(m)Q_R(n)`. This normal form should make it harder for type-I/type-II decompositions to erase the decisive sign by triangle inequality.

## 5. Prior-art boundary and falsification controls

The probabilistic architecture itself is classical in spirit. Jaeyoon Kim, **Prime Running Functions**, *Experimental Mathematics* 31:4 (2022), 1291--1313, DOI `10.1080/10586458.2020.1786863`, Section 4 studies a modified Cramér model obtained by first sieving with a modulus `Q` and then declaring each surviving integer prime independently with probability

\[
\frac{c_Q}{\log n},
\qquad c_Q=\frac{Q}{\varphi(Q)}.
\tag{27}
\]

That is exactly the conditional probability used in (10), although Kim's application and fixed-modulus asymptotics are different. Earlier sieved modifications of Cramér's model are also classical. No novelty is claimed for the random-prime construction, for the fundamental lemma of the sieve used in (21), or for the appearance of singular-series factors under small-prime conditioning.

The line-specific result is the exact specialization to the growing MRSTT primorial `P(R)`, the `ANF-149` residual, and the bow moving-window seminorm: equations (12)--(18) show that **all finite Ramanujan pair factors can be correct while the residual bow variance remains purely diagonal in expectation**. The proof of that covariance statement is elementary and does not depend on Kim's theorems; the literature audit only prevents misidentifying the sieved-Cramér model itself as new. No new durable literature dependency is therefore added to `SOURCES.md`.

The boundaries are essential. This finding does not assert that actual primes are independent after sieving, does not prove a lower bound for the actual bow variance, and does not rule out the distinguished bow cancellation. The difference `\mathfrak S(h)-\mathfrak S_R(h)` from `ANF-149`, higher correlations, long-range correlations, and the special Archimedean twist may encode exactly the anti-Bernoulli effect absent from the control. Also, (15) is an expectation/local-factor statement; it is not an asymptotic theorem for actual prime pairs in a short interval.

The falsification criterion is correspondingly sharp. Any source theorem that derives (26) from information also satisfied by the independent conditioned model contradicts (13)--(24) and must be using an unstated stronger hypothesis. A viable next step must identify an arithmetic correlation of the actual post-sieve innovation `\eta_R` that the conditioned Bernoulli model provably does not possess, and retain that correlation with its sign through the distinguished twist.