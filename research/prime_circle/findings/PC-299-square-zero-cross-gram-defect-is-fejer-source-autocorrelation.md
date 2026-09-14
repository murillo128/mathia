# PC-299 — square-zero cross-Gram defect is Fejer source autocorrelation

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the below-`r_q` square-zero defect left open by PC-298.

PC-297/298 show that the normalized one-profile boundary-log finite section is asymptotically close to a square-zero operator, quantitatively down to every pseudospectral scale `epsilon_q` with `r_q/epsilon_q -> 0`. Their proof identifies the low-Fourier cross-Gram matrix `C=Z^*X` as the obstruction to exact square-zero geometry, but uses only a maximal-atom upper bound on that matrix.

The first unresolved defect has an exact arithmetic classification. Every individual cross-Gram mean square is a triangular/Fejer average of the additive Fourier transform of the source law. In the canonical opposite-mode channel `n=-m`, it is exactly a Fejer-smoothed source autocorrelation; for a symmetric low-frequency packet, the complete cross-Gram Frobenius energy is a positive Fejer power spectrum with an unavoidable universal baseline. For the prime source, the excess over the uniform baseline is therefore nothing other than a weighted mean square of classical exponential sums over primes.

This gives a genuine bridge from the first nonzero two-step loop of the Prime-Circle boundary-log operator to additive prime-pair statistics, but it is not a new RH mechanism. The bridge lands in the classical short-interval/exponential-sum interface where zero pair correlation is already known to enter. In particular, taking norms or mean squares of the cross-Gram defect loses Fourier phase and cannot by itself create a new spectral variable.

Let `q` be an odd prime,

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and retain the PC-296/298 normalized Dirichlet coefficient

\[
c_d:=\frac1N\sum_{h\in H_B}e^{2\pi i d h/q}.
\tag{1}
\]

For a source probability law `mu` on `Z/qZ`, choose `p,r` independently with law `mu`. For a symmetric low-frequency packet

\[
S_M=\{\pm1,\ldots,\pm M\},\qquad 2M<q,
\]

PC-296 writes the low boundary-log block as

\[
A_{q,M}=X D Z^*,
\qquad
D=\operatorname{diag}_{m\in S_M}a_q(m),
\tag{2}
\]

with cross-Gram matrix

\[
C:=Z^*X,
\qquad
\boxed{C_{n,m}=c_{mp+nr}.}
\tag{3}
\]

Use the finite additive Fourier transform

\[
\widehat\mu(s):=\sum_{x\bmod q}\mu(x)e^{2\pi i sx/q}.
\tag{4}
\]

Then for every `m,n in S_M`,

\[
\boxed{
\mathbb E_{p,r\sim\mu}|C_{n,m}|^2
=
\frac1{N^2}
\sum_{|t|<N}(N-|t|)
\widehat\mu(mt)\widehat\mu(nt).
}
\tag{5}
\]

In particular, for the opposite-mode channel,

\[
\boxed{
\mathbb E|C_{-m,m}|^2
=
\frac1N+
\frac{2}{N^2}\sum_{t=1}^{N-1}(N-t)
|\widehat\mu(mt)|^2.
}
\tag{6}
\]

Thus

\[
\boxed{
\mathbb E|C_{-m,m}|^2\ge\frac1N
}
\tag{7}
\]

for every source law. Equality holds for the uniform law on `Z/qZ`.

More strongly, if `d=|S_M|=2M`, symmetry of `S_M` gives

\[
\boxed{
\mathbb E\|C\|_F^2
=
\frac{d^2}{N}
+
\frac{2}{N^2}\sum_{t=1}^{N-1}(N-t)
\left|
\sum_{m\in S_M}\widehat\mu(mt)
\right|^2.
}
\tag{8}
\]

Hence the uniform source is an exact minimizer of the mean-square cross-Gram energy, and the complete excess above `d^2/N` is a positive additive-source power spectrum.

The same statement survives the actual boundary-log multiplier. Put

\[
b_m:=|a_q(m)|^2,
\qquad
B_t:=\sum_{m\in S_M}b_m\widehat\mu(mt).
\]

Since `a_q(-m)=a_q(m)` and `mu` is real, `B_t` is real. Therefore

\[
\boxed{
\mathbb E\|D C D\|_F^2
=
\frac1N\left(\sum_{m\in S_M}b_m\right)^2
+
\frac{2}{N^2}
\sum_{t=1}^{N-1}(N-t)|B_t|^2.
}
\tag{9}
\]

The first term is universal and the second contains all source dependence in this mean-square two-step core. For fixed `M` followed by `q->infinity`, PC-298 gives `a_q(\pm j)->-1/(2j)`, so the universal coefficient tends to

\[
\frac1N
\left(\frac12\sum_{j=1}^{M}\frac1{j^2}\right)^2,
\tag{10}
\]

and then to `pi^4/(144N)` as `M->infinity`. This is a natural `N^{-1/2}` root-mean-square scale for the raw weighted cross-Gram core. It is **not** claimed to be a lower bound for the operator-norm distance of the complete matrix to the square-zero class; tails, frame re-orthogonalization, and the distinction between mean-square and in-probability scales remain separate.

## 1. Exact Fejer identity

Because `H_B` is an interval of `N` integers,

\[
\begin{aligned}
|c_d|^2
&=\frac1{N^2}
\sum_{h,h'\in H_B}e^{2\pi i d(h-h')/q}\\
&=\frac1{N^2}
\sum_{|t|<N}(N-|t|)e^{2\pi i dt/q}.
\end{aligned}
\tag{11}
\]

Substitute `d=mp+nr` and average over the independent source coordinates. The two expectations factor:

\[
\mathbb E e^{2\pi i(mp+nr)t/q}
=\widehat\mu(mt)\widehat\mu(nt),
\tag{12}
\]

which proves (5).

For `n=-m`, reality of `mu` gives

\[
\widehat\mu(-mt)=\overline{\widehat\mu(mt)}.
\]

The `t=0` term of (5) is `N/N^2=1/N`; pairing `t` and `-t` proves (6)--(7).

For (8), sum (5) over `m,n in S_M`. Since the packet is symmetric,

\[
H_t:=\sum_{m\in S_M}\widehat\mu(mt)
=2\operatorname{Re}\sum_{m=1}^{M}\widehat\mu(mt)
\in\mathbb R.
\]

Thus the double sum at frequency `t` is `H_t^2=|H_t|^2`. At `t=0`, `H_0=d`, giving the baseline `d^2/N`. The same calculation with weights `b_mb_n` proves (9).

These formulas are exact finite identities. No PNT, independence approximation, asymptotic equidistribution, or random-matrix model is used.

## 2. It is literally the first two-step loop closure

The cross-Gram matrix is not an auxiliary statistic added after the fact. From (2)--(3),

\[
\boxed{
A_{q,M}^2=X D C D Z^*.
}
\tag{13}
\]

Therefore exact square-zero behavior of the low block is obtained when the left and right Fourier frames are orthogonal, `C=0`; every failure of that orthogonality enters the first nonzero two-step loop through `D C D`. In particular, the opposite-mode coefficient is

\[
a_q(-m)a_q(m)c_{m(p-r)},
\tag{14}
\]

and the dominant `m=1` multiplier has `|a_q(1)|=1/2+O(q^{-3})` by PC-298.

Equation (9) therefore identifies the mean-square arithmetic content of the exact algebraic object that PC-297/298 must suppress to obtain square-zero geometry. It does not merely observe that prime pair correlations can be attached to the same finite section.

This also reconciles the result with PC-296. For fixed `M`, the universal floor `d^2/N` tends to zero, so `C->0` in mean square is unchanged. PC-299 refines the vanishing statement by locating its first source-sensitive coefficient rather than reopening an order-one eigenvalue escape.

## 3. Prime source: the excess is a classical exponential-sum packet

Let

\[
P_q:=\{\ell:\ell\text{ prime},\ 2<\ell<q\},
\qquad M_q:=|P_q|,
\]

and let `nu_q` be the uniform law on `P_q`. Define the ordinary additive exponential sum over that prime set,

\[
S_q(a):=\sum_{\ell\in P_q}e^{2\pi i a\ell/q}.
\tag{15}
\]

Then

\[
\widehat\nu_q(a)=\frac{S_q(a)}{M_q},
\]

so (6) becomes

\[
\boxed{
\mathbb E_{p,r\sim\nu_q}|c_{m(p-r)}|^2
=
\frac1N+
\frac{2}{N^2M_q^2}
\sum_{t=1}^{N-1}(N-t)|S_q(mt)|^2.
}
\tag{16}
\]

Equivalently, in physical source coordinates,

\[
\mathbb E|c_{m(p-r)}|^2
=
\frac1{M_q^2}\sum_{p,r\in P_q}|c_{m(p-r)}|^2,
\tag{17}
\]

so the same quantity is a Fejer smoothing of the additive prime-pair difference measure at spatial width about `q/N`.

The canonical Prime-Circle prime-pair law conditions on `p!=r`. For the single opposite-mode channel this adjustment is exact:

\[
\boxed{
\mathbb E_{p\ne r}|c_{m(p-r)}|^2
=
\frac{M_q\,\mathbb E_{\rm iid}|c_{m(p-r)}|^2-1}{M_q-1}.
}
\tag{18}
\]

Hence iid and distinct-pair averages differ by at most `1/(M_q-1)`. In the square-root regime `N\asymp\sqrt q`, the PNT gives `N/M_q->0`, so this conditioning correction is negligible relative to the universal `1/N` scale.

The exact formula also makes the information quotient explicit. The opposite-mode mean square sees `nu_q` only through the additive power spectrum `|widehat nu_q(a)|^2`; common additive phase information is lost. Two source laws with the same relevant Fourier magnitudes are indistinguishable by this channel. The symmetric packet (8)--(9) retains only the corresponding symmetrized low-frequency combinations.

## 4. Prior-art and novelty audit

The harmonic mechanism is classical. Equation (11) is the Fejer/triangular-kernel identity for the squared Dirichlet kernel, and the passage between source autocorrelation and Fourier power is finite-group Wiener--Khinchin theory. No novelty is claimed for either ingredient.

For primes, mean squares of additive exponential sums and prime-pair/short-interval variances are a classical interface with the zeros of zeta. Goldston and Montgomery, **Pair correlation of zeros and primes in short intervals**, in *Analytic Number Theory and Diophantine Problems*, Progress in Mathematics 70 (1987), 183--203, prove under RH the well-known equivalence between strong zero-pair-correlation asymptotics and second moments of primes in short intervals. Alessandro Languasco and Alberto Perelli, **Pair correlation of zeros, primes in short intervals and exponential sums over primes**, *Journal of Number Theory* 84:2 (2000), 292--304, DOI `10.1006/jnth.2000.2511`, give an explicit exponential-sum formulation in that same circle of ideas.

Those results do **not** identify (16) verbatim: PC-299 uses an unweighted finite cyclic prime measure, a denominator-`q` Fejer window, and the specific Prime-Circle Fourier modes. No equivalence between (16) and Montgomery pair correlation is claimed. Their role is the prior-art boundary: once the first square-zero defect has reduced exactly to a Fejer mean square of exponential sums over primes, any critical-line sensitivity obtained merely by analyzing that mean square belongs to an established additive-prime/explicit-formula package rather than constituting a new spectral mechanism.

Targeted searches against Fejer-smoothed prime correlations, exponential sums over primes, primes in short intervals, and zeta zero pair correlation found this established interface and no independent source in which the exact PC-296 cross-Gram matrix is interpreted as a roots-of-unity square-zero defect. The latter is the project-local synthesis; absence of a matching paper is not used as evidence of novelty. The proof of (5)--(9) is finite and self-contained, so no new load-bearing `SOURCES.md` dependency is required.

## 5. Falsification controls

The result has direct finite checks.

For arbitrary `q,N,m,n` and an arbitrary source probability vector, direct enumeration of `p,r` in (3) must agree with (5). For `n=-m`, subtracting `1/N` from the left side must be nonnegative and equal the weighted Fourier power in (6). For the uniform source every nonzero additive Fourier coefficient vanishes and equality in (7)--(9) must hold exactly.

For a finite uniform source set of size `M_q`, deleting the diagonal pairs must obey (18) exactly because every deleted pair has `p-r=0` and therefore `c_0=1`. The formulas were also stress-tested by direct enumeration on small prime moduli; the numerical values agree to floating-point precision, but the stored result depends only on the exact derivation above.

A failure of the factorization (12), the triangular multiplicity `N-|t|`, or the symmetric-packet identity in (8) would falsify the finding immediately.

## 6. Consequence for the research frontier

PC-298 leaves open pseudospectral and operator information at scales comparable to or below its quantitative approximation error `r_q`. PC-299 identifies the simplest intrinsic quantity encountered there: **the first low-mode two-step closure is not a new hidden zeta operator; after source averaging, its positive mean-square content is exactly a Fejer-smoothed additive source autocorrelation.**

This is still mathematically useful because the defect is no longer an unspecified error term. For primes it points directly at a classical zero-sensitive arithmetic object, exponential-sum/pair-correlation energy, and therefore gives a precise interface at which stronger analytic-number-theory information could sharpen the square-zero approximation.

But the same identification is also a falsification gate. A future claim based only on `||C||_F`, `||DCD||_F`, opposite-mode squared overlaps, or another quadratic positive average of this cross-Gram packet must first show content beyond the corresponding additive Fourier power spectrum and beyond matched source laws with the same autocorrelation. To escape the classical quotient one needs information discarded by that positive compression: cross-Gram phase, genuinely higher joint correlations, noncommuting multiple profiles, source-coupled left/right structure not reducible to one autocorrelation, or a cross-level operation whose critical behavior is not inherited from standard prime exponential sums.