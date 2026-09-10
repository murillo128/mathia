# ANF-155 — N-grid box characters force a thick low-spectrum ladder

**Status:** `EXACT-DERIVED + SPECTRAL-MULTIPLICITY + SHARP-SCALE-EXTENSION + SOURCE-GATE-REFINEMENT`. `ANF-153` freezes the bow geometry and `ANF-154` shows that its smallest positive normalized scale is `Theta(K/N^2)`, with one detuned box-null character attaining that order while remaining globally orthogonal to the exact periodic kernel. The near-kernel is substantially thicker than that single witness suggests. On the cofinal integer family `N=mK`, the `N` Fourier characters sampled on the full output horizon simultaneously diagonalize the moving diagonal form and the moving-energy form **inside their trial subspace**. This gives an exact min--max lower bound for the spectral counting function of the normalized Gram matrix. Around the central `K`th-root box zeros, detunings by `j` full-horizon Fourier quanta produce `Theta(KJ)` mutually form-orthogonal positive trial directions below scale `O(J^2 K/N^2)`. In particular, already at the bottom scale `K/N^2` there are `Omega(K)` positive eigenvalues, and by scale `1/K` there are `Omega(N)` of them. Thus the bow low spectrum is not a thin perturbation of the `(K-1)`-dimensional exact kernel. Dimension scarcity cannot supply the missing arithmetic obstruction; the source problem is genuinely directional inside a growing low-spectrum sector.

## 1. An exact N-grid trial family diagonalizes both quadratic forms

Keep the integer moving-window operator of `ANF-146`--`ANF-154`,

\[
A_{N,K}:\mathbb C^{N+K-1}\to\mathbb C^N,
\qquad
(A_{N,K}b)_j=\sum_{r=1}^{K}b_{j+r},
\quad 0\le j<N,
\tag{1}
\]

and assume in this finding that

\[
N=mK
\tag{2}
\]

with integers `m,K>=2`. Let `d_n` be the number of output windows containing coefficient site `n`, so

\[
D(b,c):=\sum_{n=1}^{N+K-1}d_n b_n\overline{c_n},
\qquad
V(b,c):=\langle A_{N,K}b,A_{N,K}c\rangle.
\tag{3}
\]

For `0<=p<N`, set

\[
\theta_p:=\frac{2\pi p}{N},
\qquad
b^{(p)}_n:=e^{in\theta_p}.
\tag{4}
\]

The moving weights have the exact convolution factorization

\[
d_n=\#\{(j,r):0\le j<N,\ 1\le r\le K,\ j+r=n\}.
\tag{5}
\]

Consequently, for `p!=q`,

\[
\begin{aligned}
D(b^{(p)},b^{(q)})
&=
\sum_{j=0}^{N-1}\sum_{r=1}^{K}
e^{i(j+r)(\theta_p-\theta_q)}\\
&=
\left(\sum_{j=0}^{N-1}e^{ij(\theta_p-\theta_q)}\right)
\left(\sum_{r=1}^{K}e^{ir(\theta_p-\theta_q)}\right)
=0,
\end{aligned}
\tag{6}
\]

because the first factor is a nontrivial `N`th-root geometric sum. Each vector has

\[
D(b^{(p)},b^{(p)})=NK.
\tag{7}
\]

The same `N`-point orthogonality occurs after applying `A_{N,K}`. Writing

\[
H_K(\theta):=\sum_{r=1}^{K}e^{ir\theta},
\tag{8}
\]

we have

\[
(A_{N,K}b^{(p)})_j
=e^{ij\theta_p}H_K(\theta_p),
\tag{9}
\]

and therefore

\[
V(b^{(p)},b^{(q)})=0
\qquad(p\ne q),
\tag{10}
\]

while

\[
V(b^{(p)},b^{(p)})
=N|H_K(\theta_p)|^2.
\tag{11}
\]

Hence the generalized Rayleigh quotient on each character is exactly

\[
\boxed{
q_p
:=
\frac{V(b^{(p)})}{D(b^{(p)})}
=
\frac{|H_K(2\pi p/N)|^2}{K}.
}
\tag{12}
\]

More strongly, if `S` is any set of `N`-grid frequencies and `b=sum_{p in S} c_p b^{(p)}`, then (6) and (10) give

\[
\boxed{
\frac{V(b)}{D(b)}
=
\frac{\sum_{p\in S}|c_p|^2 q_p}
{\sum_{p\in S}|c_p|^2}.
}
\tag{13}
\]

Thus the sampled box response is not merely a collection of separate test vectors: every selected family spans a trial subspace whose maximal Rayleigh quotient is the largest sampled response in that family.

This does **not** say that the characters are eigenvectors of the full diagonally normalized matrix. The edge weights in `D` prevent that conclusion. What is exact is the simultaneous orthogonality of the two quadratic forms on this `N`-dimensional trial space, which is exactly what the min--max principle needs.

## 2. Fourier-quantized detunings give an exact two-parameter near-null family

The exact kernel from `ANF-153` consists of the nonconstant `K`th-root characters. Under `N=mK` these are precisely the `N`-grid frequencies

\[
p=m\ell,
\qquad
1\le\ell\le K-1,
\tag{14}
\]

for which `q_p=0`.

Now detune the `ell`th box zero by an integer number `j` of full-horizon Fourier quanta:

\[
p=m\ell+j,
\qquad
j\ne0.
\tag{15}
\]

Using

\[
H_K(\theta)
=
e^{i(K+1)\theta/2}
\frac{\sin(K\theta/2)}{\sin(\theta/2)},
\tag{16}
\]

equation (12) becomes the exact identity

\[
\boxed{
q_{\ell,j}
=
\frac{\sin^2(\pi j/m)}
{K\sin^2(\pi\ell/K+\pi j/N)}.
}
\tag{17}
\]

For fixed or slowly growing `j` with `K|j|/N=|j|/m=o(1)`, this yields uniformly away from the endpoint roots

\[
q_{\ell,j}
=
\frac{\pi^2j^2K}
{N^2\sin^2(\pi\ell/K)}
\left(1+o(1)\right).
\tag{18}
\]

The root location therefore controls a genuine stiffness factor. Central roots with `ell/K` bounded away from `0,1` live at the `j^2 K/N^2` scale, whereas for `ell=o(K)` equation (18) gives the larger scale

\[
q_{\ell,j}
\asymp
\frac{j^2K^3}{\ell^2N^2}.
\tag{19}
\]

The witness of `ANF-154` is the special case `j=1`, `ell` near `K/2`, where the denominator in (17) is asymptotically one.

There is also an exact orthogonality fact needed below. If `j` is not divisible by `m`, then `p=m\ell+j` is not a `K`th-root frequency. Equation (6) shows that `b^{(p)}` is `D`-orthogonal to every exact kernel character `b^{(ma)}`. Thus all detuned characters used here lie in the weighted orthogonal complement of `ker A_{N,K}`, not merely outside the kernel.

## 3. Min--max turns the detuned family into a spectral multiplicity bound

Let

\[
W:=\operatorname{diag}(\sqrt{d_n}),
\qquad
C_0:=W^{-1}A_{N,K}^*A_{N,K}W^{-1}
\tag{20}
\]

be the normalized untwisted Gram matrix, and let

\[
\nu_+(\tau)
:=
\#\{\lambda\in\operatorname{spec}(C_0):0<\lambda\le\tau\}
\tag{21}
\]

count positive eigenvalues with multiplicity.

Fix the central root set

\[
\mathcal L_K
:=
\{\ell\in\mathbb Z:1\le\ell\le K-1,\ K/4\le\ell\le3K/4\}.
\tag{22}
\]

For `K>=8`, its cardinality is at least `K/2-1`. Let

\[
1\le J\le \frac m8.
\tag{23}
\]

For every `ell in L_K` and `1<=|j|<=J`, the frequency `p=m ell+j` lies in `1,...,N-1`, distinct pairs give distinct frequencies, and

\[
\left|\sin\left(\frac{\pi\ell}{K}+\frac{\pi j}{N}\right)\right|
\ge\frac12.
\tag{24}
\]

Using `|sin x|<=|x|` in (17),

\[
\boxed{
q_{\ell,j}
\le
4\pi^2j^2\frac{K}{N^2}
\le
4\pi^2J^2\frac{K}{N^2}
=: \tau_J.
}
\tag{25}
\]

Let `E_J` be the span of all these detuned characters. By (6), (10), and (13),

\[
\dim E_J
=
2J|\mathcal L_K|
\ge
J(K-2),
\tag{26}
\]

every nonzero vector in `E_J` has Rayleigh quotient at most `tau_J`, and `E_J` is `D`-orthogonal to the exact kernel. After the isometry `b mapsto Wb`, the same statements hold in the Euclidean geometry of `C_0`. The min--max principle therefore gives the exact counting consequence

\[
\boxed{
\nu_+\left(
4\pi^2J^2\frac{K}{N^2}
\right)
\ge
2J|\mathcal L_K|
\ge
J(K-2).
}
\tag{27}
\]

This is the main new quantitative statement. `ANF-154` located the first positive scale; (27) shows how quickly positive spectral multiplicity accumulates immediately above it.

Taking `J=1` gives

\[
\boxed{
\nu_+\left(4\pi^2\frac{K}{N^2}\right)
\ge K-2.
}
\tag{28}
\]

Together with the lower bound of `ANF-154`,

\[
\lambda_+(N,K)\ge \frac{K}{48N^2},
\tag{29}
\]

equation (28) shows that at least `K-2` positive eigenvalues already lie inside one absolute-constant band above the sharp bottom scale `K/N^2`. The near-kernel is therefore `K`-fold thick at its first positive scale, not a single detuned direction.

At the other end of the proved ladder, if `m>=16` choose `J=floor(m/8)`. Then `J>=m/16`, so (27) and (25) imply

\[
\boxed{
\nu_+\left(\frac{\pi^2}{16K}\right)
\ge
\frac{N}{16}\left(1-\frac2K\right).
}
\tag{30}
\]

Thus a fixed positive fraction of the `N` nonzero spectral directions already occurs by normalized scale `O(1/K)`.

Equivalently, throughout the discrete range `1<=J<=m/8`, the geometry contains a staircase with

\[
\text{positive multiplicity}\ \gg KJ
\quad\text{below scale}\quad
\asymp \frac{J^2K}{N^2}.
\tag{31}
\]

In continuous threshold language this supplies the lower-envelope heuristic `nu_+(tau) >> N sqrt(K tau)` between the bottom scale and `1/K`, with (27) as the precise statement used here.

## 4. The bow low spectrum is dimensionally abundant before arithmetic enters

In the bow regime,

\[
N\asymp X,
\qquad
K=X^{1-2\epsilon+o(1)},
\qquad
0<\epsilon<\frac14,
\tag{32}
\]

the two explicit scales in (28) and (30) become

\[
\frac{K}{N^2}
=
X^{-1-2\epsilon+o(1)},
\qquad
\frac1K
=
X^{-1+2\epsilon+o(1)}.
\tag{33}
\]

Already at the smaller, sharp rigidity scale, there are at least

\[
X^{1-2\epsilon+o(1)}
\tag{34}
\]

positive low-spectrum directions. By the still-vanishing scale `1/K`, there are `Omega(X)` positive eigenvalues. Hence the fixed geometry does not present the arithmetic source with one exceptional almost-null vector, or even with a bounded-dimensional family that could plausibly be excluded by a finite collection of generic nonalignment constraints.

This sharpens the source gate in `ANF-152`--`ANF-154`. The bow still requires the actual demodulated innovation

\[
y_U=D_UWr_X
\tag{35}
\]

to have vanishing Rayleigh quotient against `C_0`; nothing above shows that it does. The new result instead removes a possible **negative shortcut**: one cannot rule out bow cancellation by arguing that the low spectrum itself is too sparse near the first positive scale. It is already highly multiple before any prime information is imposed.

Nor does (27) identify the actual low-eigenvalue projector with the span of these Fourier characters. The trial space is not invariant under `C_0`; min--max only certifies how many genuine eigenvalues must lie below each threshold. A source theorem must therefore remain directional: it must estimate the actual projection of `D_UWr_X` onto the true low spectral subspaces, or derive an equivalent arithmetic cancellation law. Counting dimensions alone does not provide that information.

## 5. Prior-art boundary and next source test

The harmonic-analysis ingredients are classical. The moving average/boxcar filter has the geometric-sum or Dirichlet-kernel response (16) and regularly spaced unit-circle zeros; the prior-art audit again recovered that standard FIR picture. General Fourier and Toeplitz/convolution spectral theory also makes it unsurprising that sampled Fourier modes are useful trial vectors. No novelty is claimed for those ingredients or for the min--max principle.

The line-specific content is the exact finite weighted combination relevant to the bow normal form: the edge-correct moving diagonal factorizes as in (6), the same `N`-grid family orthogonalizes the output form as in (10), and those two facts turn the root-detuning law (17) into the explicit positive-eigenvalue counting bound (27). No external theorem is load-bearing for that derivation, and `ANF-146`--`ANF-154` already record the classical box-filter boundary, so `SOURCES.md` need not change.

Stress tests are important. The divisibility assumption `N=mK` is used essentially for the exact alignment of `K`th-root nulls with the `N`-grid; the result is a cofinal sharp model, not yet a uniform theorem for arbitrary `N/K`. The characters are relaxed coefficient vectors and are not models of the post-sieve prime innovation. The result supplies geometric availability and multiplicity, not source alignment. Finally, the upper thresholds in (27)--(30) are one-sided min--max bounds; they do not claim a complete asymptotic eigenvalue distribution.

For `analytic_frontier`, the next useful source test is consequently more specific than “exclude periodicity” or “exclude one detuned character.” Any arithmetic obstruction to the bow must control the demodulated post-sieve innovation against an increasingly large low-spectrum sector of the fixed moving-window geometry. A positive bow theorem must show the complementary phenomenon: source energy must actually enter that sector at the distinguished twist with the quantitative strength required by `ANF-152`. The geometry now shows that there is ample low-spectrum room; whether the primes select it remains the unresolved theorem.
