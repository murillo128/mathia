# PC-117 — arbitrary-conductor joint Hardy corrector has a zero-free Gaussian determinant

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-114 classified the one-new-prime Hardy corrector `G_{p,q}` for fixed old conductor `q`, PC-115 classified the subsequent growing-prime coarse-conductor model, and PC-116 closed arbitrary simultaneous paths only when the old conductor `q` was itself prime. The remaining natural escape is therefore to let the old conductor grow through completely general integers — including repeated prime powers and many distinct prime factors — while adjoining a genuinely new prime `p`.

That escape also closes at the exact finite-corrector level. Let `q>1` be arbitrary, let `p` be prime with `p\nmid q`, and let `G_{p,q}` be the canonical finite one-new-prime Hardy corrector of PC-113. Put

\[
X_{p,q}:=\frac{G_{p,q}}{\sqrt{\varphi(q)}}.
\]

Along every joint path

\[
p\to\infty,
\qquad
q\to\infty,
\qquad
p\ \text{prime},
\qquad
p\nmid q,
\]

one has

\[
\boxed{
\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow
c:=\gamma-4+5\log2,
}
\]

and simultaneously

\[
\boxed{\|X_{p,q}\|\longrightarrow0.}
\]

Consequently the Hilbert--Schmidt regularized determinants satisfy, locally uniformly for `z\in\mathbb C`,

\[
\boxed{
\det{}_2(I-zX_{p,q})
\longrightarrow
\exp\!\left[-\frac{\gamma-4+5\log2}{2}z^2\right].
}
\]

The limit is entire and zero-free. Thus allowing an unrestricted composite old conductor does not recover a hidden Riemann-zero divisor from the scalar-normalized finite Hardy corrector. No theorem-level historical novelty is claimed for Ramanujan-sum orthogonality, Möbius inversion, periodic averaging, trace ideals, or regularized Fredholm determinants. The durable Prime-Circle content is the exact **uniform-in-the-old-conductor** second-moment law for this geometry-forced corrector and the resulting closure of the arbitrary-conductor simultaneous-limit escape left open by PC-116.

## 1. Exact finite corrector and a periodic Hilbert--Schmidt law

Use the same off-origin Hilbert block as PC-113/116,

\[
D_\alpha^\circ,
\qquad
F(\alpha):=\|D_\alpha^\circ\|_{\mathcal S_2}^2
=
\sum_{m\ge1}(m+1)
\left(
\frac1{m+\alpha}-\frac1{m+1}
\right)^2.
\]

PC-113 proves that `F` is continuous on `[0,2]`; in particular `F(1)=0`. Put

\[
h(x):=\min(x,2-x)F(x),
\qquad 0\le x\le2.
\]

Let `N=pq`. The flattened finite-block formula of PC-113, with the new-prime Möbius difference already taken, gives a block coefficient `c_q(R+S+1)/N`. There are

\[
m_N(t):=\min(t,2N-t)
\]

pairs `(R,S)\in\{0,\ldots,N-1\}^2` with `R+S+1=t`. Therefore, for every `q>1` and every prime `p\nmid q`, not just for prime `q`,

\[
\begin{aligned}
\|G_{p,q}\|_{\mathcal S_2}^2
&=
\frac1{N^2}
\sum_{t=1}^{2N-1}
 m_N(t)c_q(t)^2F(t/N)\\
&=
\boxed{
\frac1N
\sum_{t=1}^{2N-1}
c_q(t)^2h(t/N).
}
\end{aligned}
\]

The arithmetic dependence is now isolated entirely in the periodic weight `c_q(t)^2`; the Hardy geometry is the single continuous profile `h`.

## 2. Ramanujan orthogonality makes the asymptotic uniform in `q`

Partition the sum into complete residue periods modulo `q`. Harmlessly add the endpoint `t=2N`, whose contribution is zero because `h(2)=0`, and write uniquely

\[
t=kq+r,
\qquad
0\le k\le2p-1,
\qquad
1\le r\le q.
\]

Since `c_q(kq+r)=c_q(r)`, the classical finite Ramanujan mean-square identity

\[
\boxed{
\sum_{r=1}^q c_q(r)^2=q\varphi(q)
}
\]

is exactly the averaging statement needed here. If

\[
\omega_h(\delta)
:=
\sup_{|x-y|\le\delta}|h(x)-h(y)|
\]

is the modulus of continuity of `h`, then

\[
\left|
 h\!\left(\frac{k}{p}+\frac{r}{pq}\right)
-h\!\left(\frac{k}{p}\right)
\right|
\le
\omega_h(1/p).
\]

After summing the Ramanujan weights over each complete period,

\[
\boxed{
\left|
\frac{\|G_{p,q}\|_{\mathcal S_2}^2}{\varphi(q)}
-
\frac1p\sum_{k=0}^{2p-1}h(k/p)
\right|
\le
2\omega_h(1/p).
}
\]

Crucially, the right-hand side contains **no `q`**. Since `h` is continuous,

\[
\frac1p\sum_{k=0}^{2p-1}h(k/p)
\longrightarrow
\int_0^2h(x)\,dx.
\]

PC-115/116 evaluated this same universal triangular integral as

\[
\boxed{
\int_0^2h(x)\,dx
=
\gamma-4+5\log2
=:c.
}
\]

Hence

\[
\boxed{
\sup_{\substack{q>1\\p\nmid q}}
\left|
\frac{\|G_{p,q}\|_{\mathcal S_2}^2}{\varphi(q)}-c
\right|
\longrightarrow0
\qquad(p\to\infty\ \text{through primes}).
}
\]

This simultaneously recovers the fixed-`q` law of PC-114 and the prime-`q` second-moment law used in PC-116, while also covering non-squarefree and highly composite old conductors.

## 3. Equivalent exact divisor-lattice formula

The same finite norm has an exact Möbius/divisor form that makes the old-conductor arithmetic explicit. Insert the classical identity

\[
c_q(t)
=
\sum_{d\mid(q,t)}d\,\mu(q/d)
\]

and square it. For `d,e\mid q`, set `L=\operatorname{lcm}(d,e)` and `M=N/L`. Restricting `t` to multiples of `L` gives

\[
m_N(Lu)=L\,m_M(u),
\qquad
F(Lu/N)=F(u/M).
\]

If

\[
B_M:=
\frac1{M^2}
\sum_{u=1}^{2M-1}m_M(u)F(u/M)
\]

is the universal triangular sum of PC-115/116, then `de/L=\gcd(d,e)` yields

\[
\boxed{
\|G_{p,q}\|_{\mathcal S_2}^2
=
\sum_{d,e\mid q}
\gcd(d,e)\,
\mu(q/d)\mu(q/e)\,
B_{pq/\operatorname{lcm}(d,e)}.
}
\]

For prime `q`, this reduces to the PC-116 identity

\[
\|G_{p,q}\|_{\mathcal S_2}^2
=B_{pq}+(q-2)B_p.
\]

Thus the prime formula was not a special spectral phenomenon; it was the two-divisor instance of a general finite divisor-lattice identity.

## 4. The operator norm vanishes after the canonical scalar normalization

The second moment alone does not imply a Gaussian determinant; the individual singular values must also become infinitesimal. For arbitrary `q`, this follows from the exact Hardy refinement bounds already established earlier in the line.

PC-079 gives

\[
\Gamma_n
=
\mathfrak D_{n/\operatorname{rad}(n)}
\prod_{r\mid\operatorname{rad}(n)}
(\mathfrak D_r-I)\Gamma_1,
\qquad
\Gamma_1=-H,
\qquad
\|H\|=\pi,
\]

where every coefficient dilation `\mathfrak D_r` is norm preserving. Hence

\[
\boxed{
\|\Gamma_n\|
\le2^{\omega(n)}\pi.
}
\]

From the PC-075 channel decomposition,

\[
W_n\Gamma_nW_n^*
=-\frac1n C_n\otimes H+T_n,
\qquad
\|C_n/n\|=1,
\]

so

\[
\|T_n\|\le\|\Gamma_n\|+\pi.
\]

The off-origin residual of PC-113 is `R_n=T_n-Q_nT_nQ_n`, therefore

\[
\|R_n\|
\le2(\|\Gamma_n\|+\pi).
\]

Finally PC-113 gives the exact finite split

\[
R_{pq}\cong J_p\otimes R_q+G_{p,q}.
\]

Because `p\nmid q`, `\omega(pq)=\omega(q)+1`; consequently

\[
\boxed{
\|G_{p,q}\|
\le
\pi\bigl(6\cdot2^{\omega(q)}+4\bigr).
}
\]

The remaining arithmetic estimate is elementary but decisive:

\[
\frac{4^{\omega(q)}}{\varphi(q)}
=
\prod_{r^a\parallel q}
\frac4{r^{a-1}(r-1)}
\longrightarrow0
\qquad(q\to\infty).
\]

Indeed, if `\omega(q)\to\infty`, all prime factors beyond the possible exceptional set `{2,3,5}` contribute at most `2/3`, while the exceptional product is uniformly bounded. If `\omega(q)` stays bounded and `q\to\infty`, some prime divisor or some prime exponent must diverge, forcing one local factor to zero. Thus

\[
\boxed{
\frac{2^{\omega(q)}}{\sqrt{\varphi(q)}}\longrightarrow0.
}
\]

Combining this with the norm bound gives

\[
\boxed{
\|X_{p,q}\|
=
\frac{\|G_{p,q}\|}{\sqrt{\varphi(q)}}
\longrightarrow0
}
\]

for every `q\to\infty`, uniformly in the coprime new prime `p`.

## 5. Every joint arbitrary-conductor path has the same zero-free Gaussian `det_2` limit

Now let `p,q\to\infty` jointly with `p` prime and `p\nmid q`. The uniform second-moment law gives

\[
\operatorname{Tr}(X_{p,q}^2)
=
\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow c,
\]

while the operator norm tends to zero. For every fixed `k\ge3`,

\[
\left|\operatorname{Tr}(X_{p,q}^k)\right|
\le
\|X_{p,q}\|^{k-2}
\|X_{p,q}\|_{\mathcal S_2}^2
\longrightarrow0.
\]

The standard trace expansion for the Hilbert--Schmidt regularized determinant therefore yields, initially on compact `z`-sets where the expansion is uniform and then by the usual analytic continuation/local-uniform argument,

\[
\begin{aligned}
\log\det{}_2(I-zX_{p,q})
&=-\sum_{k\ge2}\frac{z^k}{k}
\operatorname{Tr}(X_{p,q}^k)\\
&\longrightarrow
-\frac c2z^2.
\end{aligned}
\]

Hence

\[
\boxed{
\det{}_2(I-zX_{p,q})
\longrightarrow
\exp(-cz^2/2)
}
\]

locally uniformly on `\mathbb C`. The regularizing exponential in `det_2` never changes the finite-stage zero set, so this is already the relevant scalar Fredholm-divisor obstruction; no separate ordinary-determinant limit is needed here.

## 6. Scalar normalization boundary

The exact second-moment asymptotic also identifies the only scalar scale that can keep a nonzero finite Hilbert--Schmidt mass. If `a_{p,q}>0` and

\[
0<
\liminf
\left\|\frac{G_{p,q}}{a_{p,q}}\right\|_{\mathcal S_2}^2
\le
\limsup
\left\|\frac{G_{p,q}}{a_{p,q}}\right\|_{\mathcal S_2}^2
<\infty
\]

along a joint path with `p,q\to\infty`, then necessarily

\[
a_{p,q}\asymp\sqrt{\varphi(q)}.
\]

At every such scale the same operator-norm argument forces the normalized corrector to become infinitesimal; after passing to a subsequence on which the second moment converges, `det_2` again has a zero-free Gaussian limit with only the variance changed. Thus changing only the scalar normalization cannot recover a nontrivial discrete divisor from this finite arbitrary-conductor corrector.

This statement is deliberately about scalar normalization. A conductor-dependent **non-scalar** conjugation or unfolding can change the operator-norm geometry and remains outside the argument.

## 7. Falsification checks

The result has independent exact and numerical checks.

1. The periodic formula can be checked directly from the flattened PC-113 blocks for any composite `q`; no asymptotic input is required.
2. The divisor-lattice expression must agree identically with the periodic formula after expanding `c_q(t)^2` and rescaling multiples of `lcm(d,e)`.
3. Truncating the Hardy anti-diagonals gives, for `(p,q)=(5,4)`, the common value `0.0846598421938858` from the direct, periodic, and divisor formulas; dividing by `phi(4)=2` gives `0.0423299210969429`.
4. For `(p,q)=(5,6)`, the common value is `0.0852120852734812`, and for `(5,12)` it is `0.170424170546962`; after division by `phi(q)` both give approximately `0.0426060426367406`. This repeated-prime comparison directly tests that square factors do not spoil the normalized law.
5. At `p=7`, the corresponding normalized values are approximately `0.0426335663986114` for `q=4` and `0.0427748566510707` for both `q=6` and `q=12`, moving toward

\[
c=\gamma-4+5\log2\approx0.0429515677012593.
\]

6. The operator-norm bound can be independently reconstructed from the PC-079 Möbius--dilation formula, the PC-075 universal Hilbert channel norm, and the PC-113 exact finite split.

## 8. Prior-art and novelty audit

The general ingredients are classical and already lie in the Prime-Circle audit surface.

- Ramanujan sums are periodic Fourier sums on primitive roots of unity; their finite orthogonality gives `q^{-1}\sum_{r=1}^q c_q(r)^2=\varphi(q)`. Hardy's classical treatment and the Ramanujan-sum references already anchored in `SOURCES.md` cover this arithmetic input. Modern work such as Zhedanov's interpretation of Ramanujan sums as moments of measures on primitive roots of unity is structurally adjacent but does not supply this Hardy-corrector limit.
- The Möbius formula for `c_q`, finite divisor expansions, and the resulting gcd/lcm rearrangements are standard Ramanujan/divisor theory already audited throughout PC-027, PC-037, PC-056, and PC-079.
- Hilbert--Schmidt ideals, `det_2`, and the trace-log expansion are standard trace-ideal theory; Simon's *Trace Ideals and Their Applications*, already anchored for PC-107/115/116, is the relevant analytic prior art.
- No source located in the line's audit surface identifies this specific finite Prime-Circle Hardy corrector, proves the uniform-in-`q` averaging estimate above, or turns the unrestricted old-conductor joint limit into a distinct RH spectral mechanism. The result is therefore recorded as a line-specific exact obstruction, not as a historically novel theorem about Ramanujan sums or regularized determinants.

## 9. Research consequence and boundary

PC-116 left open the possibility that its Gaussian collapse was an artifact of taking the old conductor through primes. PC-117 removes that dependence: repeated prime powers, arbitrary composite structure, and unbounded numbers of old prime factors all disappear after the exact Ramanujan-period average at the canonical Hilbert--Schmidt scale.

Therefore the finite one-new-prime Hardy branch can no longer escape through a **scalar-normalized simultaneous conductor limit** merely by making the old conductor arithmetically more complicated. A surviving Hardy mechanism must instead use structure not preserved by this reduction — for example a conductor-dependent non-scalar unfolding, a nonlinear organization before the PC-113 split, or a genuinely different intrinsic operator family. This finding does not rule out those possibilities.