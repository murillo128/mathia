# PC-296 — diffuse boundary-log eigenvalues collapse to zero

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` + `PRIOR-ART-CLASSICALIZATION` for the direct nonnormal-eigenvalue escape left open by PC-278 and PC-295.

PC-295 closes the complete **absolute singular-value** spectrum of the one-profile boundary-log finite section under diffuse source averaging: after normalization by the coefficient-window size, the ordered singular values converge to the nonzero classical Green sequence

\[
\left(\frac12,\frac12,\frac14,\frac14,\frac16,\frac16,\ldots\right).
\]

That result deliberately does not control the raw eigenvalues of the generally nonnormal square matrix. PC-278 had already identified this as a logically different escape: left/right diagonal or sampling phases can disappear from positive spectral data while still affecting nonnormal eigenvalues.

For the boundary-log finite section, that escape also collapses at order-one eigenvalue scale for every sufficiently diffuse product source. In fact the contrast is stronger than source universality: **all normalized eigenvalues collapse to zero even though the top singular values stay bounded away from zero.**

Let `q` run through odd primes, let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and use the PC-283 boundary-renormalized profile

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0).
\tag{1}
\]

For source residues `p,r` define

\[
K_{q,B}^{p,r}(h,k)=k_q(ph+rk),
\qquad h,k\in H_B,
\tag{2}
\]

and

\[
T_{q,B}^{p,r}:=\frac1N K_{q,B}^{p,r}.
\tag{3}
\]

Let `mu_q` be any probability measure on `Z/qZ`, choose `p,r` independently with law `mu_q`, and put

\[
\beta_q=\|\mu_q\|_\infty.
\tag{4}
\]

Assume exactly the same diffuseness regime as PC-295,

\[
\boxed{
N\to\infty,
\qquad
(\log q)^2\sqrt{\frac{q\beta_q}{N}}\longrightarrow0.
}
\tag{5}
\]

Then, with `rho(A)` denoting spectral radius,

\[
\boxed{
\mathbb E_{p,r\sim\mu_q}\,\rho\!\left(T_{q,B}^{p,r}\right)
\longrightarrow0.
}
\tag{6}
\]

Equivalently,

\[
\boxed{
\mathbb E\max_{1\le j\le N}
|\lambda_j(T_{q,B}^{p,r})|
\longrightarrow0.
}
\tag{7}
\]

Thus the normalized one-profile boundary-log matrices are asymptotically quasinilpotent in eigenvalue scale under diffuse source averaging, while PC-295 simultaneously gives

\[
\boxed{
\mathbb E\left|\|T_{q,B}^{p,r}\|_{\rm op}-\frac12\right|
\longrightarrow0.
}
\tag{8}
\]

The gap between (6) and (8) is a genuinely nonnormal effect, but it is not an RH carrier: it occurs for every diffuse source satisfying (5), including the matched non-prime controls already used in this line.

## 1. The low Fourier block sees only a cross-Gram matrix

Use the PC-295 Fourier normalization

\[
a_q(m):=\frac{\widehat k_q(m)}q.
\tag{9}
\]

Then

\[
a_q(0)=0,
\qquad
a_q(m)<0\quad(m\ne0),
\tag{10}
\]

and for every fixed positive integer `m`,

\[
a_q(m)=a_q(q-m)\longrightarrow-\frac1{2m}.
\tag{11}
\]

Define the unit vectors

\[
x_{m,p}(h)=N^{-1/2}e^{2\pi i mph/q},
\qquad
z_{m,r}(h)=N^{-1/2}e^{-2\pi i mrh/q}.
\tag{12}
\]

PC-295 gives the exact rank-one expansion

\[
\boxed{
T_{q,B}^{p,r}
=
\sum_{m\bmod q}a_q(m)x_{m,p}z_{m,r}^{*}.
}
\tag{13}
\]

Fix `M` and, for `q>2M`, put

\[
S_M=\{\pm1,\ldots,\pm M\}\subset\mathbb Z/q\mathbb Z.
\]

Let `X=X_{p,M}` and `Z=Z_{r,M}` be the `N x 2M` matrices with columns `x_{m,p}` and `z_{m,r}`, and let

\[
D=D_{q,M}:=\operatorname{diag}_{m\in S_M}a_q(m).
\]

The low-frequency truncation is

\[
A_{q,M}^{p,r}=X D Z^*.
\tag{14}
\]

Because `A=XDZ^*` is rank at most `2M`, its nonzero eigenvalues are exactly the nonzero eigenvalues of the small matrix

\[
\boxed{
D Z^*X.
}
\tag{15}
\]

This is the elementary `AB/BA` identity. The important object is therefore not either same-side Gram matrix from PC-295, but the **cross-Gram matrix** `Z^*X`.

## 2. Diffuse independent source dilations make the cross-Gram vanish

For `d mod q` define the normalized Dirichlet coefficient

\[
c_d:=\frac1N\sum_{h\in H_B}e^{2\pi i dh/q}.
\tag{16}
\]

Finite Parseval gives the exact identity

\[
\boxed{
\sum_{d\bmod q}|c_d|^2=\frac qN.
}
\tag{17}
\]

For `m,n in S_M`, direct substitution into (12) gives

\[
\boxed{
(Z^*X)_{n,m}=c_{mp+nr}.
}
\tag{18}
\]

Both `m` and `n` are nonzero modulo the prime `q`. Multiplication by either one permutes `Z/qZ`, so the laws of `mp` and `nr` have the same maximal atom `beta_q` as `mu_q`. Their convolution therefore also has maximal atom at most `beta_q`. Combining this with (17),

\[
\boxed{
\mathbb E|c_{mp+nr}|^2
\le
\beta_q\sum_{d\bmod q}|c_d|^2
=
\frac{q\beta_q}{N}.
}
\tag{19}
\]

Summing over the fixed `2M x 2M` block yields

\[
\boxed{
\mathbb E\|Z^*X\|_F^2
\le
(2M)^2\frac{q\beta_q}{N}
\longrightarrow0.
}
\tag{20}
\]

Hence, for every fixed `M`,

\[
\boxed{
\|Z^*X\|_{\rm op}\longrightarrow0
\quad\text{in probability}.
}
\tag{21}
\]

Since `||D||` stays bounded and converges on every fixed block by (11), equations (15) and (21) already prove

\[
\rho(A_{q,M}^{p,r})\longrightarrow0
\quad\text{in probability}
\tag{22}
\]

for each fixed `M`.

This mechanism is different from PC-295's singular-value limit. There the same-side Gram matrices `X^*X` and `Z^*Z` approach the identity, so the fixed Fourier channels preserve their singular magnitudes `|a_q(m)|`. Here the cross-Gram `Z^*X` approaches zero, so those same channels fail to close into eigenvalue loops. The singular values survive while the eigenvalues disappear.

## 3. The full Fourier tail cannot resurrect order-one eigenvalues

For a normal matrix, (22) plus an operator-small tail would immediately control the full spectrum. For a nonnormal matrix that inference is false in general: arbitrarily small perturbations can move eigenvalues macroscopically. The tail therefore has to be removed through a resolvent argument rather than by a spectral-radius Lipschitz claim.

Write

\[
T_{q,B}^{p,r}=A_{q,M}^{p,r}+R_{q,M}^{p,r}.
\tag{23}
\]

PC-295 proves that

\[
\boxed{
\limsup_{q\to\infty}
\mathbb E\|R_{q,M}^{p,r}\|_{\rm op}
\le
\sqrt{R_M},
\qquad
R_M=\frac12\sum_{j>M}\frac1{j^2},
}
\tag{24}
\]

and `R_M -> 0`.

Fix `eta>0`. Suppose `lambda` is an eigenvalue of `T` with `|lambda|>=eta` and `||R||<eta`. Then `lambda I-R` is invertible. From

\[
(\lambda I-R-XDZ^*)v=0
\]

we obtain, for the nonzero vector `y=Z^*v`,

\[
\boxed{
y=Z^*(\lambda I-R)^{-1}XDy.}
\tag{25}
\]

Thus the `2M x 2M` matrix on the right must have eigenvalue `1`.

The resolvent identity gives

\[
(\lambda I-R)^{-1}
=\lambda^{-1}I+
\left[(\lambda I-R)^{-1}-\lambda^{-1}I\right]
\]

with

\[
\left\|(\lambda I-R)^{-1}-\lambda^{-1}I\right\|
\le
\frac{\|R\|}{|\lambda|(|\lambda|-\|R\|)}.
\tag{26}
\]

Therefore

\[
\boxed{
\left\|Z^*(\lambda I-R)^{-1}XD\right\|
\le
\|D\|\left[
\frac{\|Z^*X\|}{\eta}
+
\frac{\|Z\|\,\|X\|\,\|R\|}
{\eta(\eta-\|R\|)}
\right].
}
\tag{27}
\]

For fixed `M`, PC-295's same-side Gram estimates imply

\[
\|X\|\to1,
\qquad
\|Z\|\to1
\quad\text{in probability}.
\tag{28}
\]

Now choose a small deterministic `epsilon<eta/2` and a cross-Gram threshold `gamma>0` such that the right side of (27) is strictly below `1` whenever

\[
\|R\|\le\epsilon,
\qquad
\|Z^*X\|\le\gamma,
\qquad
\|X\|,\|Z\|\le2,
\tag{29}
\]

for all sufficiently large `q` at the fixed `M`. This is always possible because `||D||` is bounded. On that event equation (25) is impossible, so no eigenvalue can satisfy `|lambda|>=eta`.

Finally choose `M` so large that `sqrt(R_M)` is arbitrarily small compared with `epsilon`. Markov's inequality and (24) make the bad-tail probability arbitrarily small; then let `q -> infinity`, using (20) and (28) to remove the cross-Gram and same-side bad events. Hence

\[
\boxed{
\rho(T_{q,B}^{p,r})\longrightarrow0
\quad\text{in probability}.
}
\tag{30}
\]

This step is what rules out a pseudospectral loophole at **order-one eigenvalue radius**. It does not assert that the pseudospectrum itself is small.

## 4. Convergence in mean follows from the surviving singular norm

PC-295 gives more than tightness of the operator norm. Its ordered singular-value convergence implies exactly

\[
\boxed{
\mathbb E\left|\|T_{q,B}^{p,r}\|_{\rm op}-\frac12\right|
\longrightarrow0.
}
\tag{31}
\]

Thus the family `||T||op` is uniformly integrable. Since

\[
0\le\rho(T)\le\|T\|_{\rm op}
\tag{32}
\]

and (30) gives convergence of `rho(T)` to zero in probability, uniform integrability upgrades (30) to (6).

The result is therefore not merely that a typical finite block has small eigenvalues. The **entire normalized spectral radius vanishes in mean** under the same diffuseness assumption that produces the deterministic nonzero Green singular spectrum.

## 5. Prime and matched-control consequence

For the normalized prime source below `q`, the maximal atom satisfies

\[
\beta_q\asymp\frac{\log q}{q}
\]

by the prime number theorem. The count-matched Li-grid control used in PC-290 has the same maximal-atom order. Consequently both obey (5) whenever

\[
\boxed{
\frac{N}{(\log q)^5}\longrightarrow\infty,
}
\tag{33}
\]

including the square-root regime `N~sqrt(q)`. For both source families,

\[
\boxed{
\mathbb E\rho(K/N)\longrightarrow0.
}
\tag{34}
\]

The canonical prime-pair law often conditions on distinct primes. Under the iid prime law the diagonal event has probability `1/M_q`, where `M_q` is the number of sampled primes. Since every entry of `T` has modulus at most `log q/N`,

\[
\rho(T)\le\|T\|_{\rm op}\le\log q.
\tag{35}
\]

Conditioning away the diagonal therefore changes the mean spectral radius by at most

\[
O\!\left(\frac{\log q}{M_q}\right)
=
O\!\left(\frac{(\log q)^2}{q}\right)
=o(1).
\tag{36}
\]

Thus (34) also holds for distinct prime pairs.

This is compatible with PC-292 rather than contradicting it. Same-source configurations such as `p=r=1` can retain order-one nonnormal spectral structure and saturate the mesoscopic operator-norm threshold. Their probability under a diffuse independent product source tends to zero fast enough that they do not survive the averaged spectral-radius limit.

## 6. Prior-art and novelty audit

The abstract ingredients are classical. The identity that nonzero eigenvalues of `AB` and `BA` coincide is standard linear algebra; Yuji Nakatsukasa, **The low-rank eigenvalue problem**, arXiv:1905.11490 (2019), discusses precisely this reduction for low-rank eigenproblems. General finite-section and compact-operator spectral approximation is classical as well; Philip M. Anselone and Michael L. Treuden, **Spectral analysis of asymptotically compact operator sequences**, *Numerical Functional Analysis and Optimization* 17 (1996), 679–690, DOI `10.1080/01630569608816718`, is representative neighboring theory.

The phenomenon "nonzero singular spectrum with zero eigenvalue spectrum" is also classical in non-self-adjoint operator theory. The Volterra operator is the standard quasinilpotent compact example. That analogy is only conceptual: no Volterra limit is claimed here, and the proof above does not import Volterra theory.

Targeted prior-art checks against low-rank nonnormal eigenproblems, finite-section spectral approximation, quasinilpotent/Volterra operators, Fourier submatrices, and log-sine/Hankel finite sections found the expected general operator-theoretic framework but no theorem that supplies the line-specific cross-Gram estimate (19) for these source-dilated Prime-Circle boundary-log sections. Absence of such a theorem is not used as evidence of novelty.

No novelty is claimed for `AB/BA`, resolvent perturbation, quasinilpotence as a concept, finite Parseval, or the classical log-sine Green multiplier. The durable project-local delta is the exact combination of those ingredients forced by the Prime-Circle representation: **diffuse independent multiplicative source dilations make the left and right low Fourier frames asymptotically orthogonal, so the same matrices whose singular spectrum converges to the nonzero Green sequence have spectral radius converging to zero.**

The proof is self-contained and the external references are neighboring prior art rather than load-bearing dependencies, so `SOURCES.md` is unchanged.

## 7. Boundaries and remaining nonnormal channels

Equation (6) closes only the direct order-one **eigenvalue** spectralization of a single boundary-log profile under diffuse product averaging. It does not say that the matrices become small as operators; equation (8) proves the opposite. It also does not control pseudospectral level sets at shrinking perturbation scales, eigenvector conditioning, resolvent norms near zero, or transient amplification. Those quantities can remain large precisely because the matrices are highly nonnormal.

Nor does (6) control a microscopic rescaling of the collapsing eigenvalues, determinants or log-determinants that amplify eigenvalues near zero, source-conditioned exceptional pairs, same-source/extremal configurations, singular vectors or phases, several profiles retained jointly before spectral compression, non-product source correlations, or genuine cross-level operators. Any such continuation must still pass the mandate's matched-control and prior-art gates.

The immediate negative conclusion is narrower and decisive:

\[
\boxed{
\text{one boundary-log profile}
\to
\text{diffuse source pair}
\to
\text{raw nonnormal eigenvalues at order-one scale}
\to
\text{new RH discriminator}
}
\]

fails. The normalized eigenvalue cloud contracts to the origin for prime sources and for the same diffuse non-prime controls, while the nonzero singular data classicalize to the universal Green sequence of PC-295.

## 8. Falsification and audit tests

The claim has direct finite checks.

1. Reconstruct (13) from the finite Fourier transform of `k_q`; any entrywise mismatch falsifies the starting decomposition.
2. For fixed `M`, compute `Z^*X` directly and verify (18). Summing `|c_d|^2` over all residues must give exactly `q/N`.
3. For a source law with maximal atom `beta_q`, estimate `E|c_{mp+nr}|^2`; exceeding `q beta_q/N` for nonzero fixed `m,n` would contradict the convolution bound.
4. Compare the nonzero eigenvalues of `XDZ^*` with those of `DZ^*X`; they must agree exactly, including algebraic multiplicity away from zero.
5. At fixed `M`, the low-block spectral radius must tend to zero whenever `q beta_q/N -> 0`, even though its leading singular values approach `1/2,1/2,1/4,1/4,...`.
6. The tail estimate from PC-295 and the deterministic resolvent bound (27) together forbid an order-one eigenvalue on the good event (29). An explicit counterexample satisfying all three good-event inequalities would falsify the argument.
7. Under prime-scale diffuse sources with `N/(log q)^5 -> infinity`, a persistent order-one mean spectral radius would contradict (6).
8. Same-source or deliberately concentrated source laws are outside hypothesis (5); order-one eigenvalues there are not counterexamples and are expected from PC-292.

Finite numerical stress tests can probe the convergence rate, but no numerical observation is used as durable evidence for (6).