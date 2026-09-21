# AF-481 — Prime density alone forces logarithmic Gibbs boundary collapse

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INPUT`, `ARITHMETIC-FIDELITY`, `QUANTITATIVE-FIDELITY`, `MATCHED-CONTROL`, `BOUNDARY-CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-479 identified the local boundary collapse

\[
\rho_{\mathbb P}(1+\varepsilon)
\sim
\frac{\sqrt{P(2)/2}}{\log(1/\varepsilon)}
\]

for the canonical coordinate Hilbert embedding of the rational-prime Gibbs family. The logarithmic rate is **not rational-prime-selective**.

Let

\[
Q=\{q_1<q_2<\cdots\}\subset(1,\infty)
\]

be any discrete sequence whose counting function satisfies the prime-density asymptotic

\[
N_Q(x):=\#\{q\in Q:q\le x\}
\sim \frac{x}{\log x}.
\tag{1}
\]

Define

\[
P_Q(\sigma)=\sum_{q\in Q}q^{-\sigma},
\qquad
\mu^Q_\sigma(q)=\frac{q^{-\sigma}}{P_Q(\sigma)},
\qquad \sigma>1,
\tag{2}
\]

and use the same canonical coordinate Hilbert embedding

\[
H(\mu)=\sqrt2\,\mu\in\ell^2(Q).
\tag{3}
\]

For the local lower-margin ratio

\[
\rho_Q(\sigma)
:=
\frac{\sqrt2\,\| (\mu^Q_\sigma)'\|_2}
     {\|(\mu^Q_\sigma)'\|_1},
\tag{4}
\]

one has, as `epsilon downarrow 0`,

\[
\boxed{
\rho_Q(1+\varepsilon)
\sim
\frac{\sqrt{P_Q(2)/2}}
     {\log(1/\varepsilon)}.
}
\tag{5}
\]

Thus every source sequence with the same first-order counting density as the rational primes has the same `1/log(1/epsilon)` canonical Hilbert-conditioning collapse. The constant retains the square-summable fixed-coordinate profile `P_Q(2)`, but the **rate** comes from the coarse counting law `(1)`.

Two matched controls make the failure of prime selectivity explicit.

1. For the shifted-composite sequence

\[
Q_+=\{p+1:p\ge3\text{ prime}\},
\tag{6}
\]

every generator is an ordinary even composite and

\[
N_{Q_+}(x)=\pi(x-1)-1\sim\frac{x}{\log x}.
\tag{7}
\]

Hence `(5)` holds with `P_Q(2)=\sum_{p\ge3}(p+1)^{-2}`.

2. For the smooth pseudo-prime sequence

\[
Q_{\mathrm{sm}}=\{n\log n:n\ge2\},
\tag{8}
\]

inversion of `n log n` gives `N_{Q_{\mathrm{sm}}}(x)\sim x/\log x`, so `(5)` holds again despite the absence of rational-prime membership in the generator rule.

The reusable Arithmetic Fidelity conclusion is therefore

\[
\boxed{
\text{the AF-479 logarithmic boundary rate detects prime-scale density, not rational primality.}
}
\tag{9}
\]

Any RH-facing use of this Gibbs conditioning law must find an additional invariant beyond first-order prime density and the resulting normalization singularity.

## Exact derivation

Write

\[
A(\sigma):=P_Q(\sigma),
\qquad
m_Q(\sigma):=-\frac{A'(\sigma)}{A(\sigma)}.
\tag{10}
\]

Termwise differentiation is valid for every fixed `sigma>1`, and gives the standard exponential-family score identity

\[
(\mu^Q_\sigma)'(q)
=
\mu^Q_\sigma(q)\bigl(m_Q(\sigma)-\log q\bigr).
\tag{11}
\]

### Prime-density counting fixes the partition singularity

Stieltjes partial summation gives

\[
A(1+\varepsilon)
=\int_{1^-}^{\infty}x^{-1-\varepsilon}\,dN_Q(x).
\tag{12}
\]

After integration by parts, the tail is asymptotic to

\[
(1+\varepsilon)
\int^\infty
\frac{x^{-1-\varepsilon}}{\log x}\,dx.
\tag{13}
\]

With `u=log x`, this becomes the classical logarithmic Laplace integral

\[
\int^\infty \frac{e^{-\varepsilon u}}u\,du,
\]

so `(1)` implies

\[
\boxed{
A(1+\varepsilon)
\sim
L:=\log\frac1\varepsilon.
}
\tag{14}
\]

Applying the same partial-summation argument to `log q\,q^{-1-\varepsilon}` gives

\[
\boxed{
-A'(1+\varepsilon)
=\sum_{q\in Q}\frac{\log q}{q^{1+\varepsilon}}
\sim \frac1\varepsilon.
}
\tag{15}
\]

Therefore

\[
m_Q(1+\varepsilon)
\sim\frac1{\varepsilon L},
\qquad
\varepsilon m_Q(1+\varepsilon)\to0.
\tag{16}
\]

The same counting hypothesis also gives the Mertens-scale consequences

\[
\sum_{q\le x}\frac1q
\sim\log\log x,
\qquad
\sum_{q\le x}\frac{\log q}{q}
\sim\log x.
\tag{17}
\]

These are direct partial-summation consequences of `(1)`; no multiplicative structure is used.

### The `ell^1` tangent speed is universally `2m_Q`

Let `X=\log q` under `\mu^Q_\sigma`, and abbreviate `m=m_Q(\sigma)`. Since `E(X-m)=0`,

\[
\mathbb E|X-m|
=2\,\mathbb E[(m-X)_+].
\tag{18}
\]

For `sigma=1+epsilon`, on the set `q<e^m` one has

\[
e^{-\varepsilon m}\le q^{-\varepsilon}\le1,
\]

and `(16)` makes the lower factor tend to `1`. Hence `(14)`, `(16)`, and `(17)` imply

\[
\mu^Q_\sigma(X<m)
=
\frac1{A(\sigma)}
\sum_{q<e^m}q^{-1-\varepsilon}
\longrightarrow1,
\tag{19}
\]

because

\[
\log m=L-\log L+o(L).
\tag{20}
\]

Likewise,

\[
\mathbb E[X;X<m]
\le
\frac1{A(\sigma)}
\sum_{q<e^m}\frac{\log q}{q}
\sim
\frac{m}{L}
=o(m).
\tag{21}
\]

Thus

\[
\mathbb E[(m-X)_+]
\sim m,
\]

and by `(11)` and `(18)`,

\[
\boxed{
\|(\mu^Q_\sigma)'\|_1
\sim2m_Q(\sigma).
}
\tag{22}
\]

This is the same tangent-scale mechanism used in AF-479, but it follows from the density law `(1)` alone.

### The `ell^2` tangent speed sees only the square-summable fixed profile

From `(11)`,

\[
\|(\mu^Q_\sigma)'\|_2^2
=
\frac{
P_Q''(2\sigma)
+2m_Q(\sigma)P_Q'(2\sigma)
+m_Q(\sigma)^2P_Q(2\sigma)
}{P_Q(\sigma)^2}.
\tag{23}
\]

Condition `(1)` implies convergence of

\[
\sum_{q\in Q}\frac{(\log q)^j}{q^2}
\qquad (j=0,1,2),
\]

so `P_Q(2sigma)`, `P_Q'(2sigma)`, and `P_Q''(2sigma)` converge to finite limits as `sigma downarrow1`. Since `m_Q(sigma)->infinity`, the quadratic term dominates:

\[
\boxed{
\|(\mu^Q_\sigma)'\|_2
\sim
\frac{m_Q(\sigma)\sqrt{P_Q(2)}}{P_Q(\sigma)}.
}
\tag{24}
\]

Combining `(14)`, `(22)`, and `(24)` gives `(5)`.

For every fixed `sigma>1`, differentiability in both `ell^1` and `ell^2` also gives

\[
\lim_{\tau\to\sigma}
\frac{\|H(\mu^Q_\tau)-H(\mu^Q_\sigma)\|_2}
     {\|\mu^Q_\tau-\mu^Q_\sigma\|_1}
=
\rho_Q(\sigma).
\tag{25}
\]

Therefore the best global lower Lipschitz constant on the full open family is zero for every such `Q`:

\[
\inf_{\sigma\ne\tau>1}
\frac{\|H(\mu^Q_\sigma)-H(\mu^Q_\tau)\|_2}
     {\|\mu^Q_\sigma-\mu^Q_\tau\|_1}
=0.
\tag{26}
\]

This is a global **obstruction** obtained from local pairs. It does not yet assert the stronger AF-480-type matching asymptotic for the optimal anchored half-line constant under only `(1)`.

## Matched-control audit

The shifted-composite family `(6)` is particularly diagnostic. It preserves the exact one-dimensional ordering inherited from the primes and has the same first-order counting law, while the ordinary arithmetic predicate "is prime" is destroyed at every generator: for odd `p`, `p+1` is even and greater than `2`, hence composite.

Its Gibbs likelihood ratios remain monotone, its normalization has the same logarithmic divergence, and `(5)` gives the same boundary-collapse rate. Therefore neither single crossing nor the `1/log` conditioning law can certify rational-prime provenance.

The smooth control `(8)` removes even the shifted-prime origin. Its counting law alone is enough to recreate the same rate. This separates two information layers:

\[
\text{first-order source density}
\quad\Longrightarrow\quad
\text{normalization singularity and `1/log` fidelity rate},
\]

while any specifically arithmetic discriminator must live in finer structure not fixed by `(1)`.

The constant `P_Q(2)` does depend on the detailed generator locations, so the theorem does **not** say the entire metric geometry is universal. It says the rate that looked prime-zeta-specific in AF-479 is already forced by a much coarser equivalence class.

## Prior art and novelty audit

The component mathematics is classical, and this finding makes **no novelty claim** for the asymptotic tools.

- Arne Beurling, **“Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I,”** *Acta Mathematica* 68 (1937), 255--291, introduced generalized-prime systems in which the generators need not be the rational primes. This is the natural prior-art boundary for treating `Q_+` or another real generator sequence as a matched generalized-prime control.
- N. H. Bingham, C. M. Goldie, and J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), especially the Karamata and Abelian/Tauberian chapters, is standard prior art for passing from counting asymptotics such as `(1)` to Stieltjes/Laplace-transform asymptotics such as `(14)`--`(17)`.
- C.-E. Fröberg, **“On the Prime Zeta Function,”** *BIT* 8 (1968), 187--202, is the classical rational-prime reference underlying the AF-479 comparison case.
- Adolf Hildebrand, **“Additive and Multiplicative Functions on Shifted Primes,”** *Proceedings of the London Mathematical Society* 59 (1989), 209--232, is prior art showing that shifted-prime sequences such as `p+1` are classical arithmetic objects in their own right. No result from that paper is needed for `(7)`, which follows directly from the ordinary prime number theorem.

A targeted search across Beurling generalized primes, regular variation, shifted primes, and prime/zeta Gibbs distributions found the counting-law and transform ingredients as standard, but did not identify a standard statement of the total-variation-to-coordinate-Hilbert ratio `(5)`. That absence is not evidence of novelty. The durable contribution here is the Arithmetic Fidelity falsification: AF-479's logarithmic rate survives broad prime-density controls and therefore cannot be used as a rational-prime discriminator.

## Boundaries and falsification audit

- **The theorem assumes the full counting asymptotic `(1)`.** Weaker upper/lower density information may give only one-sided bounds or different slowly varying corrections.
- **The result is local in its sharp asymptotic.** Equation `(5)` describes tangent conditioning. Equation `(26)` follows globally because local pairs exist arbitrarily near the boundary, but `(1)` alone is not claimed to imply AF-480's exact global half-line asymptotic.
- **The embedding remains fixed.** As in AF-479/AF-480, this concerns `H(mu)=sqrt(2)mu`. It does not rule out nonlinear representations with different boundary conditioning.
- **This is a matched-control obstruction, not an RH statement.** Reproducing the rate with composite or pseudo-prime generators weakens arithmetic interpretation; it neither proves nor disproves any zero statement.
- **The shifted-composite control still inherits prime ordering.** That is intentional: it is a strong matched control, not an independent random model. The smooth `n log n` control shows that even this inherited origin is unnecessary for the rate.
- **The detailed constant is not universal.** `P_Q(2)` changes with the generator sequence. A future discriminator could in principle use finer fixed-coordinate data, but it must then survive controls matched at that stronger layer.
- **No multiplicative semigroup information is used in the proof.** The theorem lives at the source-law/counting layer. If a later mechanism uses genuinely multiplicative relations among generalized integers, this finding does not pre-empt it.

## Research consequence

AF-479 and AF-480 established a sharp logarithmic conditioning law for the rational-prime Gibbs curve. AF-481 identifies exactly how much of that law is already explained before rational primality enters: the local rate follows from `N_Q(x)~x/log x` plus the canonical coordinate geometry.

The next arithmetic gate should therefore move below first-order density. A prime-specific source invariant must distinguish rational primes from `Q_+`, `Q_sm`, and stronger Beurling controls while surviving the intended compression. Promising quantities are not the normalization singularity or the one-crossing sign law themselves, but finer relational or multiplicative structure whose matched-control equivalence class is strictly smaller than `(1)`.