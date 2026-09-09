# PC-234 — prime-base packet normalization is binary-cyclotomic chord data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY` for the coupled amplitude/normalization escape left open by PC-227/PC-232 in the prime-coarse-base case. For distinct primes `p<q`, the coefficient energy used to normalize the fresh-prime cyclotomic mask is not a new cross-prime statistic: because `Phi_{pq}` is flat, that energy is exactly the classical number of nonzero coefficients of the binary cyclotomic polynomial, hence an explicit modular-inverse statistic. When `p` is fixed and `q` grows in one residue class, its affine slope is exactly four times a parent regular-`p`-gon inverse-square chord eigenvalue. The prime-base PC-227 singular square then has an exact closed form and tends to the universal value `1/2`, while the limiting packet-sector masses are a discrete Fejér/interval power spectrum.

Thus the prime-base packet normalization, its total singular mass, and its limiting distribution among Cauchy sectors are all classical finite cyclic/binary-cyclotomic data. This does **not** classify composite coarse bases or simultaneous mode-resolved growth with both primes tending to infinity, but it removes the possibility that the previously implicit prime-base normalization scalar or packet-energy profile is itself a new RH carrier.

## 1. Binary coefficient energy is exactly a modular-inverse statistic

Let `p<q` be distinct primes and write

\[
h_{pq}:=\sum_k a_{pq}(k)^2,
\qquad
\Phi_{pq}(z)=\sum_k a_{pq}(k)z^k.
\tag{1}
\]

Binary cyclotomic polynomials are flat: their coefficients belong to `{−1,0,1}`. Therefore

\[
\boxed{h_{pq}=\vartheta(pq),}
\tag{2}
\]

where `vartheta(pq)` is the number of nonzero coefficients. Define the two modular inverses

\[
x:=\overline p_q\in\{1,\ldots,q-1\},
\qquad
\delta:=\overline q_p\in\{1,\ldots,p-1\}.
\tag{3}
\]

The classical Carlitz formula for binary cyclotomic support, in the equivalent form used by Shparlinski--Wijaya, gives

\[
\boxed{h_{pq}=\vartheta(pq)=2x\delta-1.}
\tag{4}
\]

The inverses satisfy the exact Bézout relation

\[
\boxed{px+q\delta=pq+1.}
\tag{5}
\]

Indeed the left side is congruent to `1` modulo both `p` and `q`, and its allowed range forces the displayed representative. Hence either inverse determines the other. In particular, the scalar normalization `h_{pq}` that enters the PC-226/PC-227 source mask is already the standard binary-cyclotomic sparsity statistic whose distribution is studied through modular inverses and Kloosterman-type methods.

For `p=2`, the same formulas follow directly from

\[
\Phi_{2q}(z)=1-z+z^2-\cdots+z^{q-1},
\]

so `h_{2q}=q`, `\delta=1`, and `x=(q+1)/2`.

## 2. The PC-226 affine slope is exactly a parent chord eigenvalue

Now fix `p` and write

\[
q=pm+r,
\qquad 1\le r<p,
\qquad (r,p)=1.
\tag{6}
\]

Then

\[
\delta=\overline r_p
\tag{7}
\]

is constant along the residue class. Equation (5) gives

\[
x=m(p-\delta)+c_r,
\qquad
c_r:=\frac{r(p-\delta)+1}{p}\in\mathbb Z.
\tag{8}
\]

Substituting into (4),

\[
\boxed{
h_{pq}
=m\,2\delta(p-\delta)+(2\delta c_r-1).}
\tag{9}
\]

PC-226 writes the same coefficient energy as

\[
h_{pq}=mH_r+K_r.
\tag{10}
\]

Therefore the previously implicit finite-state constants are explicit at a prime coarse base:

\[
\boxed{H_r=2\delta(p-\delta),
\qquad
K_r=2\delta c_r-1.}
\tag{11}
\]

Let

\[
\Lambda_k^{(p)}=\frac{k(p-k)}2
\tag{12}
\]

be the classical unnormalized inverse-square chord-Laplacian eigenvalue of the regular `p`-gon from PC-032. Then

\[
\boxed{H_r=4\Lambda_\delta^{(p)}.}
\tag{13}
\]

Equivalently, for the normalized chord symbol of PC-233,

\[
m_{\rm ch}(u)=\frac{u(1-u)}2,
\]

one has

\[
\boxed{H_r=4p^2m_{\rm ch}(\delta/p).}
\tag{14}
\]

Thus the large-`q` coefficient-energy normalization is not independent of the regular-polygon geometry. Its residue-class dependence is exactly the parent chord dispersion evaluated at the multiplicative inverse of the fresh residue.

## 3. The complete prime-base singular square has an exact closed form

PC-227 proves at finite `q` that the prime-base source singular spectrum is flat and gives its common squared singular value as

\[
\lambda_{p,q}
=\frac{p}{q h_{pq}}
\sum_{j=1}^{q-1}
\frac{\sin^2(\pi j/q)}{\sin^2(\pi p j/q)}.
\tag{15}
\]

Multiplication by `p` permutes the nonzero residues modulo `q`. Reindexing by `k=pj mod q` sends the numerator to `sin^2(pi xk/q)`, where `x=\overline p_q`. The elementary finite Fourier/Parseval identity

\[
\boxed{
\sum_{k=1}^{q-1}
\frac{\sin^2(\pi xk/q)}{\sin^2(\pi k/q)}
=x(q-x)
}
\tag{16}
\]

therefore evaluates the trigonometric sum exactly. Hence

\[
\boxed{
\lambda_{p,q}
=\frac{p\,x(q-x)}{q(2x\delta-1)}.
}
\tag{17}
\]

Using (5) once more gives the exact correction to the limiting value:

\[
\boxed{
\lambda_{p,q}
=\frac12+
\frac{q(2\delta-p)-2}
{2pq(2x\delta-1)}.
}
\tag{18}
\]

Consequently, for every fixed prime `p`, through **all** fresh primes `q` rather than only one residue class,

\[
\boxed{
\lambda_{p,q}=\frac12+O_p(q^{-1}),
\qquad q\to\infty.
}
\tag{19}
\]

The finitely many residue classes can approach `1/2` from different sides, but the residue dependence disappears from the leading singular mass. For example,

\[
(p,q)=(5,11):
\quad(x,\delta,h)=(9,1,17),
\quad
\lambda_{5,11}=\frac{90}{187}<\frac12,
\tag{20}
\]

whereas

\[
(p,q)=(5,29):
\quad(x,\delta,h)=(6,4,47),
\quad
\lambda_{5,29}=\frac{690}{1363}>\frac12.
\tag{21}
\]

Both are exactly governed by the same modular-inverse formula and converge to `1/2` as the fresh prime grows.

## 4. The limiting packet-energy profile is a discrete Fejér spectrum

The collapse is stronger than the total singular value. At prime coarse base, PC-227's selection rule leaves only `a=0`. Let `r=q mod p`, `\delta=\overline r_p`, and reindex a packet sector by

\[
s\equiv-rt\pmod p,
\qquad 1\le s\le p-1.
\tag{22}
\]

Then `t\equiv-\delta s mod p`. Since

\[
\Phi_p(1)=p,
\qquad
\alpha\Phi_p'(\alpha)=\frac{p}{\alpha-1}
\quad(\alpha^p=1,\ \alpha\ne1),
\tag{23}
\]

PC-227's Cauchy residue becomes

\[
\boxed{
C_{p,r}(s)
=\frac{\zeta_p^{-\delta s}-1}
{2\pi i\sqrt{2\delta(p-\delta)}}.
}
\tag{24}
\]

The corresponding shifted packet is `C_{p,r}(s)/(j+s/p)`. Summing its squared mass over `j in Z` with the classical cosecant partial fraction gives

\[
\boxed{
M_\delta(s)
:=\sum_{j\in\mathbb Z}
\left|\frac{C_{p,r}(s)}{j+s/p}\right|^2
=
\frac1{2\delta(p-\delta)}
\frac{\sin^2(\pi\delta s/p)}
{\sin^2(\pi s/p)}.
}
\tag{25}
\]

But

\[
\frac{\sin^2(\pi\delta s/p)}
{\sin^2(\pi s/p)}
=
\left|
\frac{1-\zeta_p^{\delta s}}
{1-\zeta_p^s}
\right|^2
=
\left|1+\zeta_p^s+\cdots+\zeta_p^{(\delta-1)s}\right|^2.
\tag{26}
\]

Thus the sector weights are exactly the discrete Fourier power spectrum of the length-`\delta` interval indicator on `Z/pZ`, with the zero mode removed. Parseval gives

\[
\sum_{s=0}^{p-1}
\left|1+\zeta_p^s+\cdots+\zeta_p^{(\delta-1)s}\right|^2
=p\delta,
\tag{27}
\]

while the omitted zero-frequency value is `\delta^2`. Therefore

\[
\boxed{
\sum_{s=1}^{p-1}
\frac{\sin^2(\pi\delta s/p)}
{\sin^2(\pi s/p)}
=\delta(p-\delta),
}
\tag{28}
\]

and hence

\[
\boxed{
\sum_{s=1}^{p-1}M_\delta(s)=\frac12.
}
\tag{29}
\]

Equation (29) is the packet-limit counterpart of the finite exact formula (18). Conditional on the surviving packet mass, the sector distribution is simply the discrete Fejér/interval spectrum

\[
\boxed{
2M_\delta(s)
=\frac1{\delta(p-\delta)}
\left|1+\zeta_p^s+\cdots+\zeta_p^{(\delta-1)s}\right|^2.
}
\tag{30}
\]

So even the residue-dependent distribution of mass among the prime-base Cauchy sectors has no hidden coefficient statistic: it is ordinary finite cyclic harmonic analysis.

## 5. Prior-art and falsification audit

The key arithmetic input is classical rather than a new Prime-Circle identity. Carlitz's 1966 formula for the number of terms of `Phi_{pq}` is explicitly recalled in Shparlinski--Wijaya, **On nonzero coefficients of binary cyclotomic polynomials**, *Journal of Number Theory* 271 (2025), 246--258, DOI `10.1016/j.jnt.2024.11.008`; their equation (1.7) rewrites `vartheta(pq)` directly through the modular inverse `\overline q_p/p`, and their paper studies the distribution of that statistic using Kloosterman-sum methods. This source and Sanna's 2022 cyclotomic-coefficient survey are already recorded in `research/prime_circle/SOURCES.md` as the coefficient-sparsity boundary.

The finite sine identity (16)/(28) is elementary Parseval for a cyclic interval and is also the same regular-polygon trigonometric structure behind the Calogero--Perelomov inverse-square spectrum already anchored in `SOURCES.md`. No novelty is claimed for binary flatness, modular-inverse support formulas, Fejér kernels, or the sine quotient identity.

A matched non-arithmetic control is exact: take the cyclic group `Z/pZ`, choose an interval of length `delta`, and form its nonzero-frequency power spectrum. It reproduces (25)--(30) with no primality or cyclotomic birth interpretation. The project-specific content is only the identification that the PC-226/PC-227 **source-forced normalization and packet mass** land exactly on this classical package.

The formulas were stress-checked against direct cyclotomic coefficient energies for all prime pairs `2<=p<q<100`; (4), (11), and (18) agree exactly in every case. These checks are controls only; the derivations above are exact.

## 6. Prime-Circle consequence and surviving boundary

For a prime coarse base, the route

\[
\boxed{
\text{fresh-prime cyclotomic mask}
\longrightarrow
\text{coefficient-energy normalization / Cauchy packet mass}
\longrightarrow
\text{new cross-prime spectral carrier}
}
\]

is closed. The normalization scalar is classical binary-cyclotomic sparsity, its residue-class slope is a parent inverse-square chord eigenvalue, the complete finite source singular square has the modular-inverse formula (17), and the limiting sector masses are a cyclic Fejér spectrum. None supplies a free complex spectral parameter, gamma factor, functional-equation involution, zeta-zero divisor, or critical-line condition.

This boundary must not be overextended. It does **not** classify a composite coarse conductor with at least two old prime factors, where cyclotomic coefficients are no longer binary-flat; the full mode-resolved regime with `p,q -> infinity` simultaneously, for which the fixed-base PC-227 packet limit is unavailable; phase-sensitive couplings between packet sectors under non-translation-invariant operators; renormalized fresh-scale corrections; or the broader squarefree multi-prime amplitude/normalization state left open by PC-232/PC-233. Those remain the correct places to look after removing the prime-base scalar and packet-energy normalization as independent candidates.