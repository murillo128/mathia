# PC-294 — boundary-log Hilbert-Schmidt mass is source-universal

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` for the first positive spectral moment at the square-root finite-section frontier left by PC-290/PC-293.

PC-293 removes every local residue band of width `T=O(N)` from the source-averaged boundary-log singular spectrum at `N~sqrt(q)`, but deliberately leaves the nonlocal complement unresolved. There is nevertheless one complete spectral statistic for which the whole matrix, including that complement, can be controlled exactly: the total squared singular-value mass.

Let `q` be an odd prime,

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and use the exact PC-283 boundary-renormalized logarithmic profile

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0).
\tag{1}
\]

For source residues `p,r` define the PC-280 finite section

\[
K_{q,B}^{p,r}(h,k)=k_q(ph+rk),
\qquad h,k\in H_B.
\tag{2}
\]

If `mu` is any probability measure on `Z/qZ`, write

\[
\beta(\mu)=\|\mu\|_\infty
\]

and let `p,r` be independent with law `mu`. Define the source-averaged normalized Hilbert-Schmidt spectral mass

\[
\mathcal E_{q,B}(\mu)
:=
\mathbb E_{p,r\sim\mu}
\left\|\frac{K_{q,B}^{p,r}}N\right\|_F^2
=
\mathbb E_{p,r\sim\mu}
\sum_{j=1}^{N}
\sigma_j\!\left(\frac{K_{q,B}^{p,r}}N\right)^2.
\tag{3}
\]

Let `u_q` be the uniform law on `Z/qZ`. Then

\[
\boxed{
\left|
\mathcal E_{q,B}(\mu)-\mathcal E_{q,B}(u_q)
\right|
\le
2(\log q)^2
\sqrt{\frac{q\,\beta(\mu)}{N}}.
}
\tag{4}
\]

The benchmark itself is explicit:

\[
\boxed{
\mathcal E_{q,B}(u_q)
=
\left(1-\frac1{N^2}\right)
\frac1q\sum_{t\bmod q}k_q(t)^2
+
\frac{(\log q)^2}{N^2}.
}
\tag{5}
\]

As `q,N -> infinity`,

\[
\frac1q\sum_{t\bmod q}k_q(t)^2
\longrightarrow
\int_0^1\log^2(2\sin\pi x)\,dx
=rac{\pi^2}{12}.
\tag{6}
\]

Consequently every source family satisfying

\[
\beta(\mu_q)=O\!\left(\frac{\log q}{q}\right),
\qquad
\frac{N}{(\log q)^5}\longrightarrow\infty,
\tag{7}
\]

has

\[
\boxed{
\mathcal E_{q,B}(\mu_q)\longrightarrow\frac{\pi^2}{12}.
}
\tag{8}
\]

In particular, both the normalized prime source and the count-matched Li-grid control of PC-290 satisfy the diffuseness hypothesis. At square-root coefficient resolution `N~sqrt(q)`, each therefore obeys

\[
\boxed{
\mathcal E_{q,B}
=rac{\pi^2}{12}
+O\!\left(\frac{(\log q)^{5/2}}{q^{1/4}}\right)
+o(1),
}
\tag{9}
\]

and their difference is `o(1)` unconditionally. Thus the unresolved nonlocal residue complement cannot carry a prime-specific signal in the **total squared singular-value mass**. Any order-one source-specific signal surviving in the one-profile boundary-log spectrum at `B~sqrt(q)` must redistribute spectral mass among singular values rather than change its total Hilbert-Schmidt mass.

## 1. Source dependence has an exact finite Fourier expansion

Put

\[
g_q(t):=k_q(t)^2
\]

and use the unnormalized finite Fourier transform

\[
\widehat g_q(m)
:=
\sum_{t\bmod q}g_q(t)e^{-2\pi i mt/q}.
\tag{10}
\]

For the source measure use the opposite harmless phase convention

\[
\widehat\mu(a)
:=
\sum_{x\bmod q}\mu(x)e^{2\pi i ax/q}.
\tag{11}
\]

Define the window-averaged source coefficient

\[
A_\mu(m)
:=
\frac1N\sum_{h\in H_B}\widehat\mu(mh).
\tag{12}
\]

Because `H_B=-H_B` and `mu` is real, `A_mu(m)` is real. Fourier inversion of `g_q`, followed by independence of `p,r`, gives the exact identity

\[
\boxed{
\mathcal E_{q,B}(\mu)
=
\frac1q\sum_{m\bmod q}
\widehat g_q(m)A_\mu(m)^2.
}
\tag{13}
\]

No asymptotic or distribution theorem is used here. Equation (13) is simply the squared-entry average of the finite section before spectral compression.

For the uniform source,

\[
A_{u_q}(0)=1,
\qquad
A_{u_q}(m)=\frac1N\quad(m\ne0),
\tag{14}
\]

because among the distinct residues `h in H_B`, only `h=0` makes `mh=0 mod q` when `m!=0`.

## 2. Diffuse sources have small window-averaged Fourier deviation

Write

\[
\delta=\mu-u_q.
\]

Then `widehat delta(0)=0`. For every `m!=0`, Cauchy-Schwarz gives

\[
\begin{aligned}
|A_\delta(m)|^2
&=
\frac1{N^2}
\left|
\sum_{\substack{h\in H_B\\h\ne0}}
\widehat\delta(mh)
\right|^2\\
&\le
\frac{N-1}{N^2}
\sum_{\substack{h\in H_B\\h\ne0}}
|\widehat\delta(mh)|^2.
\end{aligned}
\tag{15}
\]

Since multiplication by nonzero `m` permutes `Z/qZ` and the elements of `H_B` are distinct modulo `q`, finite Parseval yields

\[
\sum_{\xi\bmod q}|\widehat\delta(\xi)|^2
=
q\sum_{x\bmod q}\left|\mu(x)-\frac1q\right|^2
=q\left(\|\mu\|_2^2-\frac1q\right).
\tag{16}
\]

Because `||mu||_2^2<=beta(mu)`, equations (15)--(16) imply

\[
\boxed{
|A_\mu(m)-A_{u_q}(m)|
=|A_\delta(m)|
\le
\sqrt{\frac{q\,\beta(\mu)}N}
\qquad(m\ne0).
}
\tag{17}
\]

Both `A_mu(m)` and `A_u(m)` are averages of quantities of modulus at most one, hence

\[
\boxed{
|A_\mu(m)^2-A_{u_q}(m)^2|
\le
2\sqrt{\frac{q\,\beta(\mu)}N}.
}
\tag{18}
\]

This is the source side of the argument. It sees no source locations, no equidistribution in residue classes, no RH input, and no prime cancellation: only the maximal atom survives.

## 3. The boundary-log kernel has exact Wiener norm `log q`

The remaining issue is whether the Fourier coefficients of the singular profile are summable strongly enough for (18) to control the whole matrix. PC-283 supplies exactly the needed sign information. With the same unnormalized DFT convention,

\[
\widehat k_q(0)=0,
\qquad
\widehat k_q(j)<0
\quad(1\le j\le q-1).
\tag{19}
\]

Fourier inversion at the anchor gives

\[
-\log q
=k_q(0)
=\frac1q\sum_{j\bmod q}\widehat k_q(j).
\tag{20}
\]

Because every nonzero coefficient has the same sign, there is no cancellation in the Fourier `l^1` norm:

\[
\boxed{
\frac1q\sum_{j\bmod q}|\widehat k_q(j)|
=\log q.
}
\tag{21}
\]

This exact identity is stronger than a generic smoothness estimate. The logarithmic singularity has growing Fourier mass, but only at the controlled rate `log q`.

Since `g_q=k_q^2`, the finite-group product/convolution identity is

\[
\widehat g_q(m)
=
\frac1q
\sum_{j\bmod q}
\widehat k_q(j)\widehat k_q(m-j).
\tag{22}
\]

Young's elementary `l^1` convolution inequality and (21) therefore give

\[
\boxed{
\frac1q\sum_{m\bmod q}|\widehat g_q(m)|
\le
(\log q)^2.
}
\tag{23}
\]

Combining (13), (18), and (23), with the `m=0` term canceling exactly because every probability measure has `A_mu(0)=1`, proves (4).

This is the key distinction from the clipping route PC-284--PC-293. No residue band is removed, no derivative of the log profile is estimated, and no local/nonlocal split is needed. The complete profile is controlled through its exact finite Fourier `l^1` mass.

## 4. The universal benchmark is the log-sine `L2` energy

Under `u_q`, every noncentral linear form

\[
hp+kr
\]

with `(h,k)!=(0,0)` is uniform modulo `q`, because at least one nonzero coefficient is invertible. The central coefficient pair is identically zero. Averaging those `N^2` entries proves (5) directly.

The special anchor value contributes only

\[
\frac{(\log q)^2}{q}
\]

to the residue average in (5). Away from the anchor, `k_q(t)` samples the integrable square-log singularity `log^2(2 sin pi x)`. Hence the discrete averages converge to the improper integral in (6). Equivalently, the classical Fourier series

\[
\log(2\sin\pi x)
=-\sum_{n\ge1}\frac{\cos(2\pi nx)}n
\]

and Parseval give

\[
\int_0^1\log^2(2\sin\pi x)\,dx
=
\frac12\sum_{n\ge1}\frac1{n^2}
=rac{\pi^2}{12}.
\tag{24}
\]

If `beta(mu_q)=O(log q/q)`, equation (4) becomes

\[
\left|
\mathcal E_{q,B}(\mu_q)-\mathcal E_{q,B}(u_q)
\right|
\ll
\frac{(\log q)^{5/2}}{\sqrt N}.
\tag{25}
\]

This proves (7)--(9). Notice that square-root resolution is far from the threshold of this argument: the Hilbert-Schmidt mass is already source-universal whenever `N/(log q)^5 -> infinity` for sources of prime-scale diffuseness.

## 5. Prime and matched-control consequences

For the normalized prime source, `beta=1/M_q`, with `M_q asy q/log q` by the prime number theorem. The PC-290 count-matched Li-grid control likewise has maximal grid atom `O(log q/q)`. Thus (25) applies to each source separately and, by the triangle inequality through `u_q`,

\[
\boxed{
\left|
\mathcal E_{q,B}(\nu_q)-
\mathcal E_{q,B}(\widetilde\lambda_q^\#)
\right|
\ll
\frac{(\log q)^{5/2}}{\sqrt N}.
}
\tag{26}
\]

This comparison does not use RH and does not even use where the source points are located. It uses only the maximal-atom scale already shared by the prime and matched control.

The actual prime spectral laws in PC-284--PC-290 use distinct ordered source pairs. Conditioning the independent prime product law on `p!=r` changes (3) by at most

\[
O\!\left(\frac1{M_q}(\log q)^2\right)
=O\!\left(\frac{(\log q)^3}{q}\right),
\tag{27}
\]

because `||K/N||_F^2=O((log q)^2)` uniformly. This is negligible in every regime above, so the same conclusion holds for the distinct-pair prime law.

PC-293 showed that local singular residue bands cannot carry the missing critical-scale signal after diffuse source averaging. Equation (26) now says that even after restoring **all** residues, the total squared spectral mass remains blind to source position. The nonlocal complement may still alter the shape of the singular spectrum, but it cannot create or remove order-one Hilbert-Schmidt mass.

## 6. Prior-art and novelty audit

No new theorem of harmonic analysis or analytic number theory is claimed. Finite Fourier inversion and Parseval, Cauchy-Schwarz, the product-to-convolution identity, and the `l^1` convolution inequality are standard finite-group harmonic analysis. The sign and exact Fourier transform of the boundary log-sine kernel were already classicalized in PC-283 through the digamma/logarithmic Green-kernel formula. The limiting value `pi^2/12` is the classical `L^2` norm of the log-sine kernel.

Targeted checks against finite cyclic Wiener algebras, large-sieve/Plancherel estimates, finite Fourier transforms of the log-sine kernel, and source-averaged cyclic-convolution sections found the expected classical ingredients and stronger general-purpose harmonic-analysis frameworks. No independent prior-art mechanism was found that turns this particular Prime-Circle source-averaged finite-section Hilbert-Schmidt statistic into a new RH criterion. Absence of such a theorem is not used as evidence of novelty.

The durable project-local delta is the composition of those classical ingredients with the exact PC-280/PC-283 boundary-log finite section: the same-sign digamma multiplier makes its discrete Wiener norm exactly `log q`, and source diffuseness then forces the **complete** Hilbert-Schmidt spectral mass to forget source positions well before the square-root scale. No new `SOURCES.md` dependency is required.

## 7. Boundaries and falsification tests

The result is intentionally a first-positive-moment obstruction, not a collapse theorem for the complete ordered singular-spectrum law. Two sources can have the same total squared singular-value mass while distributing it very differently among singular directions. Higher trace moments, the top edge, small singular values, determinant-type statistics, joint singular vectors, non-averaged extremal pairs, cross-level couplings, or representation-richer observables remain outside (4).

The diffuseness hypothesis is essential for the quantitative conclusion. A source with large atoms need not satisfy (25), and a window with `N` too small compared with the source concentration can retain source dependence in its Frobenius mass. The exact inequality (4), however, holds for every probability measure on `Z/qZ`.

The claim has direct finite falsification points:

1. verify (13) by direct Fourier inversion for arbitrary finite source weights;
2. exhibit `m!=0` violating the Parseval bound (17);
3. exhibit a nonconstant Fourier coefficient of `k_q` with nonnegative sign, or violate the exact norm identity (21);
4. find a source for which the measured difference from the uniform benchmark exceeds (4);
5. for diffuse prime-scale sources with `N/(log q)^5 -> infinity`, keep an order-one discrepancy in the normalized Hilbert-Schmidt mass.

Any such example would invalidate a load-bearing step. Conversely, agreement with (4) says nothing about the unresolved higher-order shape of the critical-scale spectrum.

The live one-profile frontier is therefore narrower than after PC-293: at square-root resolution, neither the local singular sector nor the complete total squared singular-value mass can carry prime-specific information against a count/diffuseness-matched control. A surviving one-profile mechanism must live in **how** the universal spectral mass is organized, not in how much of it exists.