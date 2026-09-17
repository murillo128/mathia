# PC-327 — band-normalized Green defect has universal Schatten divergence

**Status:** `EXACT-DERIVED` + `DECISIVE-BOUNDARY` + `PRIOR-ART-CLASSICALIZATION` for the growing-conductor escape left open by PC-326.

PC-326 proves that at every fixed pair of conductors the canonical cross-level Green operator is a trace-class perturbation of one universal Hilbert channel and that the relative-determinant zeros outside the band have an `ell^1` edge-gap budget. It deliberately leaves open a growing-conductor limit in which the trace-class control could cease to be uniform.

That loss of uniformity does occur, but it is forced by the generalized-Hilbert offsets for **every** nonzero pair of centered periodic sources. Let `q,r` be distinct primes, `L=qr`, and let `a,b` be the periodic Fourier masks used in PC-323, with periods `q,r`, respectively, and with `a(0)=b(0)=0`. Write

\[
X_{a,b}=A_{a,b}\otimes H_1+S_{a,b},
\qquad
G_{a,b}=G_0+V,
\qquad
V=\begin{pmatrix}0&S_{a,b}\\S_{a,b}^*&0\end{pmatrix}.
\]

If

\[
\mu_a=\frac1q\sum_{i=1}^{q-1}|a(i)|^2,
\qquad
\mu_b=\frac1r\sum_{j=1}^{r-1}|b(j)|^2,
\qquad
c=\sqrt{\mu_a\mu_b},
\]

then `[-pi c,pi c]` is the PC-323 essential Hilbert band. Put `m=min(q,r)`. For every `m>128`,

\[
\boxed{
\frac{\|S_{a,b}\|_2^2}{c^2}
\ge \frac14\log\frac{m}{128}
}
\tag{1}
\]

and therefore

\[
\boxed{
\left\|\frac{V}{c}\right\|_2^2
\ge \frac12\log\frac{m}{128},
\qquad
\left\|\frac{V}{c}\right\|_1
\ge \sqrt{\log\frac{m}{128}}.
}
\tag{2}
\]

Thus, when both conductors grow, normalizing by the only intrinsic scale that keeps the universal Hilbert band fixed makes the relative defect leave every uniformly bounded `S_2` and `S_1` family. The phenomenon is source-independent: it occurs for arbitrary centered masks, including non-arithmetic matched controls. Consequently the mere breakdown of the fixed-conductor PC-326 trace-class budget in a growing-conductor limit cannot itself be a Prime-Circle or RH discriminator.

## 1. Exact Hilbert-Schmidt cost of one generalized-Hilbert offset

For `alpha>0`, let

\[
(H_\alpha)_{uv}=\frac1{u+v+\alpha},
\qquad u,v\ge0,
\]

and put

\[
g(\alpha):=\|H_\alpha-H_1\|_2^2.
\]

Grouping the matrix entries by `s=u+v`, with multiplicity `s+1`, gives the exact identity

\[
\boxed{
 g(\alpha)
=(1-\alpha)^2
\sum_{s\ge0}\frac1{(s+\alpha)^2(s+1)}.
}
\tag{3}
\]

Equivalently, in terms of the digamma and trigamma functions,

\[
g(\alpha)=\psi(\alpha)-\psi(1)+(1-\alpha)\psi_1(\alpha).
\tag{4}
\]

Only the elementary positive series (3) is needed below. Its `s=0` term gives

\[
\boxed{
0<\alpha\le\frac12
\quad\Longrightarrow\quad
 g(\alpha)\ge\frac1{4\alpha^2}.
}
\tag{5}
\]

Hence the trace-class equivalence `H_alpha-H_1 in S_1` used in PC-323 is highly nonuniform as `alpha->0+`: already its Hilbert-Schmidt energy diverges quadratically.

## 2. The complete source dependence is a convex mixture of shifted universal grids

PC-323 gives, after grouping the common period `L=qr`,

\[
S_{\rho\sigma}
=\frac{a(\rho)b(\sigma)}{L}
\left(H_{(\rho+\sigma)/L}-H_1\right),
\qquad 1\le\rho,\sigma\le L.
\tag{6}
\]

Since the finite residue blocks are orthogonal in Hilbert-Schmidt norm,

\[
\frac{\|S\|_2^2}{c^2}
=
\frac1{L^2\mu_a\mu_b}
\sum_{\rho,\sigma=1}^{L}
|a(\rho)|^2|b(\sigma)|^2
 g\!\left(\frac{\rho+\sigma}{L}\right).
\tag{7}
\]

Every nonzero `q`-residue occurs in the common period as

\[
\rho=i+qu,
\qquad 1\le i\le q-1,
\quad 0\le u\le r-1,
\]

and similarly

\[
\sigma=j+rv,
\qquad 1\le j\le r-1,
\quad 0\le v\le q-1.
\]

Define probability weights

\[
p_i=\frac{|a(i)|^2}{q\mu_a},
\qquad
p'_j=\frac{|b(j)|^2}{r\mu_b}.
\tag{8}
\]

Then (7) becomes the exact convex decomposition

\[
\boxed{
\frac{\|S\|_2^2}{c^2}
=
\sum_{i=1}^{q-1}\sum_{j=1}^{r-1}
p_i p'_j\,T_{q,r}(i+j),
}
\tag{9}
\]

where

\[
\boxed{
T_{q,r}(\delta)
=
\frac1{qr}
\sum_{u=0}^{r-1}\sum_{v=0}^{q-1}
 g\!\left(
 \frac ur+\frac vq+\frac{\delta}{qr}
 \right).
}
\tag{10}
\]

This is the key structural point. Once the Hilbert band is normalized by `c`, the detailed source magnitudes do not alter the local singular kernel: they merely choose a convex mixture among shifts `delta=i+j` of one universal two-dimensional lattice sum.

## 3. Every admissible shift has a logarithmic singular floor

Assume without loss of generality `q=m<=r`. For all shifts appearing in (9),

\[
2\le\delta\le q+r-2,
\qquad
\varepsilon:=\frac{\delta}{qr}
<\frac1q+\frac1r\le\frac2q.
\tag{11}
\]

Let

\[
M=\left\lfloor\frac r8\right\rfloor,
\qquad
N=\left\lfloor\frac q8\right\rfloor.
\]

For `q>=16`, the grid points with `0<=u<M`, `0<=v<N` satisfy

\[
\frac ur+\frac vq+\varepsilon<\frac12,
\]

so (5) applies. Therefore

\[
T_{q,r}(\delta)
\ge
\frac1{4qr}
\sum_{u=0}^{M-1}\sum_{v=0}^{N-1}
\frac1{(u/r+v/q+\varepsilon)^2}.
\tag{12}
\]

The summand decreases separately in both variables. The lower-left Riemann sum therefore dominates the corresponding integral. Since `M/r,N/q>=1/16` for `q,r>=16`,

\[
T_{q,r}(\delta)
\ge
\frac14
\int_0^{1/16}\int_0^{1/16}
\frac{dx\,dy}{(x+y+\varepsilon)^2}.
\tag{13}
\]

For `A,B,epsilon>0`,

\[
\int_0^A\int_0^B\frac{dx\,dy}{(x+y+\epsilon)^2}
=
\log\frac{(A+\epsilon)(B+\epsilon)}
{\epsilon(A+B+\epsilon)}.
\tag{14}
\]

The right side decreases with `epsilon`. Using `epsilon<=2/q`, `A=B=1/16`, and `q>=16`, its argument is at least `q/128`. Hence every admissible shift obeys

\[
\boxed{
T_{q,r}(\delta)
\ge\frac14\log\frac{q}{128}.
}
\tag{15}
\]

Because (9) is a convex combination, (15) proves (1). Finally,

\[
\|V\|_2^2=2\|S\|_2^2,
\qquad
\|V\|_1=2\|S\|_1\ge2\|S\|_2,
\tag{16}
\]

which gives (2).

The constant `128` is only a convenient explicit cutoff. The durable statement is the uniform lower growth

\[
\frac{\|S\|_2^2}{c^2}\gg\log\min(q,r),
\tag{17}
\]

independent of the arithmetic content of the two source masks.

## 4. Matched controls show that the singular limit is not arithmetic

Take the centered point-source control on `Z/qZ`,

\[
f_q=\delta_0-\frac1q\mathbf1.
\tag{18}
\]

Its unnormalized finite Fourier transform is

\[
\widehat f_q(0)=0,
\qquad
\widehat f_q(h)=1\quad(h\ne0).
\tag{19}
\]

Thus it has exactly the same formal centered-source admissibility as the PC-316/323 masks but no prime-support arithmetic. The analogous control exists at conductor `r`. Rescaling the two controls by constants can match any prescribed pair `(mu_a,mu_b)`, hence can match the **same** Hilbert-band scale `c` as the canonical Prime-Circle sources. Equations (1)--(2) still apply.

Therefore

\[
\boxed{
\text{fixed-band normalization}
\Longrightarrow
\text{nonuniform Schatten defect}
}
\tag{20}
\]

is a universal generalized-Hilbert boundary effect, not a discriminator between the prime source and a non-arithmetic centered control.

This also prevents a misleading absolute interpretation. For the canonical prime-support source at conductor `q`, Parseval gives

\[
\mu_q=\frac1{|P_q|}-\frac1q,
\tag{21}
\]

so the prime number theorem makes `c_{q,r}` shrink roughly like

\[
\sqrt{\frac{\log q\,\log r}{qr}}.
\tag{22}
\]

The theorem does **not** say that the unnormalized defect norm must diverge. It says that the defect becomes large relative to the simultaneously shrinking universal Hilbert band. That is precisely the normalization relevant to the growing-conductor escape from PC-326.

## 5. Prior art and consequence for the PC-326 frontier

The operator-theoretic ingredients are classical. Generalized Hilbert matrices and their spectral behavior are part of the Magnus--Rosenblum theory already anchored in `SOURCES.md`; PC-323 already uses the trace-class identity `H_alpha-H_1 in S_1`. Recent generalized-Hilbert work, including edge-eigenvalue and determinant asymptotics, reinforces that singular behavior as the offset approaches the endpoint belongs to the classical Hilbert/Hankel framework. The Hilbert-Schmidt series (3), convex decomposition (9), and logarithmic lower bound (15) are elementary consequences of the exact PC-323 residue representation, so no new external theorem is load-bearing and `SOURCES.md` needs no update.

A targeted search around generalized Hilbert matrices, weighted/periodic Hilbert operators, trace ideals, and shifted-Hilbert Schatten behavior found the expected classical operator frameworks, not an independent Prime-Circle-specific mechanism. No historical novelty is claimed for the endpoint singularity or for logarithmic divergence of the associated singular Riemann sum. The line-local mathematical delta is the **source-uniform** consequence for the exact cross-level Green decomposition: the band-normalized defect necessarily loses uniform `S_2` and `S_1` control as both conductors grow.

This sharpens, but does not contradict, PC-326. At each fixed `(q,r)`, `V` remains trace class and the `ell^1` edge-gap estimate is valid. After scaling the band to `[-pi,pi]`, however, its right-hand budget is

\[
\frac{\|V\|_1}{c},
\]

which cannot remain bounded by (2). Thus the fixed-conductor estimate supplies **no uniform growing-conductor edge-gap budget**. Importantly, the failure of uniformity is already present in matched non-arithmetic controls, so it cannot itself count as the missing zeta-sensitive ingredient.

The theorem does not prove that the actual normalized discrete edge-gap sum diverges: PC-326 gives an upper bound by the trace norm, and a diverging upper budget alone does not force bound states. Nor does it exclude source-specific information in a renormalized spectral-shift measure, in the coefficient or excess growth beyond the universal floor, or in a different nonseparable operator. A viable growing-conductor continuation must therefore subtract or otherwise control this universal generalized-Hilbert singularity and exhibit a residual invariant that separates the canonical Prime-Circle source from matched centered controls before attaching it to zeta zeros.

## Audit tests

The result is falsified if any of the following finite/exact steps fails: grouping the squared entries of `H_alpha-H_1` must give (3); the PC-323 block decomposition must give the Hilbert-Schmidt sum (7); periodic repetition over the product conductor must give the convex identity (9)--(10); the `s=0` term of (3) must imply (5); the lower-left Riemann sum must dominate (13); and the elementary integral (14) with `epsilon<=2/min(q,r)` must yield (15). These checks establish only the universal band-normalized Schatten divergence and its matched-control obstruction, not a zeta functional equation, zero-selection theorem, or classification of every possible singular conductor limit.