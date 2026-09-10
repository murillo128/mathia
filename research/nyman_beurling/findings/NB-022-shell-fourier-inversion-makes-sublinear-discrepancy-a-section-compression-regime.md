# NB-022 — shell Fourier inversion turns sublinear discrepancy into section compression

**Status:** `EXACT-DERIVED + SHELL-FOURIER-MOBIUS-DUALITY + DISCREPANCY-COEFFICIENT-COERCIVITY + SUBLINEAR-SECTION-COMPRESSION + INTRINSIC-MIXING-FLOOR + NEGATIVE/METHOD-BOUNDARY`. `NB-019` identifies the intrinsic consecutive-shell discrepancy `Delta_N` as the quantity controlling deep dilation mixing, while `NB-020` shows that a small Nyman residual forces an early Möbius-shaped coefficient core. `NB-021` then proves that the alternative `Delta_N=o(N)` makes every sufficiently deep visible dilation channel asymptotically invisible. The missing structural question is what the same discrepancy hypothesis says about the finite section itself.

There is an exact answer. The periodic shell sequence has a sparse finite Fourier transform: its frequency `1/n` sees precisely the coefficients whose indices are multiples of `n`. Möbius inversion over those multiples recovers the weighted coefficient vector. Parseval therefore turns shell discrepancy directly into a coercive coefficient estimate.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},\qquad
r_N=e-P_Ne,\qquad d_N=\|r_N\|,
\tag{1}
\]

and write the canonical projection uniquely as

\[
P_Ne=\sum_{j=2}^{N}a_{N,j}g_j.
\tag{2}
\]

As in `NB-019`, let `r_{N,t}` be the harmonic-shell values, let `mu_N` be their periodic mean, and put

\[
\Delta_N
:=\sup_{A\le B}\left|
\sum_{t=A}^{B}(r_{N,t}-\mu_N)
\right|.
\tag{3}
\]

Then the weighted coefficient vector satisfies the unconditional finite inequality

\[
\boxed{
\left(\sum_{n=2}^{N}n^2|a_{N,n}|^2\right)^{1/2}
\le 60\,\Delta_N.
}
\tag{4}
\]

The constant `60` is explicit rather than optimized. It comes from the elementary root-of-unity bound `2 sin(pi/n)<=2pi/n` and the exact Dirichlet-series identity

\[
\sum_{q\ge1}\frac{|\mu(q)|}{q^2}
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2}.
\tag{5}
\]

Equation (4) has two source-specific consequences.

First, for every `2<=K<N`, if

\[
v_{N,\le K}:=\sum_{j=2}^{K}a_{N,j}g_j,
\qquad
w_{N,>K}:=\sum_{j=K+1}^{N}a_{N,j}g_j,
\tag{6}
\]

then

\[
\boxed{
\|w_{N,>K}\|\le\frac{60\Delta_N}{K},
}
\tag{7}
\]

and hence, writing `r_K=e-P_Ke`,

\[
\boxed{
0\le d_K^2-d_N^2
=\|r_K-r_N\|^2
\le\frac{3600\Delta_N^2}{K^2}.
}
\tag{8}
\]

Thus intrinsic shell discrepancy controls not only deep mixing but also how much of the actual target projection can be gained from high generator indices.

Second, the Möbius core of `NB-020` cannot coexist with arbitrarily small intrinsic discrepancy. There are absolute constants `c,C>0` such that, whenever

\[
\min\{N,d_N^{-1}\}\ge C,
\]

one has

\[
\boxed{
\Delta_N
\ge c\,\min\{N,d_N^{-1}\}^{3/2}.
}
\tag{9}
\]

In particular, along any subsequence on which `d_N->0`, Burnol's classical lower bound places `d_N^{-1}=O(sqrt(log N))=o(N)`, so

\[
\boxed{
\Delta_N\gg d_N^{-3/2}.
}
\tag{10}
\]

Consequently an intrinsic mixing scheme based on the sharp `NB-019` error `Delta_N/m` cannot become effective at scales `m=m_N` with

\[
m_Nd_N^{3/2}=O(1).
\tag{11}
\]

This is weaker than the `m_Nd_N^2->infinity` obstruction for the absolute coefficient majorant `mathfrak A_N`, but unlike that majorant it survives arbitrary cancellation between generator discrepancies: it is a lower floor on the intrinsic discrepancy itself.

Most importantly, combine (8) with the same sublinear-discrepancy hypothesis used in `NB-021`. If

\[
\Delta_N=o(N),
\tag{12}
\]

set

\[
K_N:=1+\left\lceil\sqrt{N(1+\Delta_N)}\right\rceil.
\tag{13}
\]

Then `K_N=o(N)`, `Delta_N/K_N->0`, and therefore

\[
\boxed{
\|r_{K_N}-r_N\|\longrightarrow0,
\qquad
d_{K_N}^2-d_N^2\longrightarrow0.
}
\tag{14}
\]

At exactly this scale, `NB-021` gives

\[
\sup_{m\ge K_N}\|Q_mr_N\|_\infty\longrightarrow0,
\qquad Q_m=\sqrt m\,A_m^*.
\tag{15}
\]

So the `Delta_N=o(N)` branch has a two-sided compression interpretation: **above one sublinear scale, the extra finite-section approximation gain is negligible and every deeper semigroup transport channel is simultaneously mixed to zero.** A successful visibility argument in this branch cannot be rescued merely by moving to high generator indices or by pushing the dilation horizon farther out. Its non-negligible source information must already be present below the common transition scale, or the branch itself must be ruled out by proving linear-scale shell discrepancy.

This does not prove that `Delta_N=o(N)` holds, does not show that the pre-transition block has enough visible energy, and does not improve the Nyman distance. It sharpens the method boundary by making the same intrinsic quantity control both halves of the scale-coupled problem.

## 1. Root-of-unity samples isolate coefficient multiples

Let

\[
\Lambda_N=\operatorname{lcm}(2,3,\ldots,N).
\tag{16}
\]

The shell sequence of every `g_j` has period `j`, so the centered residual

\[
u_t:=r_{N,t}-\mu_N
\tag{17}
\]

is `Lambda_N`-periodic with mean zero. For a Fourier frequency `xi` in `(1/Lambda_N) Z/Z`, use the normalized finite transform

\[
\widehat u(\xi)
:=\frac1{\Lambda_N}
\sum_{t=1}^{\Lambda_N}u_t e^{-2\pi i t\xi}.
\tag{18}
\]

Fix `2<=n<=N` and put

\[
z_n:=e^{-2\pi i/n}.
\tag{19}
\]

Bagchi's shell formula is

\[
g_j|_{I_t}=\left\{\frac tj\right\}.
\tag{20}
\]

After subtracting the mean `(j-1)/(2j)`, its Fourier coefficient at `xi=1/n` vanishes unless `n|j`. Indeed a `j`-periodic sequence has no `1/n` Fourier mode over the common period unless `z_n^j=1`. If `n|j`, the constant mean contributes zero and

\[
\frac1j\sum_{t=1}^{j}
\left\{\frac tj\right\}z_n^t
=
\frac1{j^2}\sum_{t=1}^{j-1}t z_n^t
=-\frac1{j(1-z_n)}.
\tag{21}
\]

Since the centered residual is minus the corresponding linear combination of centered generators, define

\[
T_n:=\sum_{q\le N/n}\frac{a_{N,qn}}q.
\tag{22}
\]

Then (21) gives the exact sparse transform identity

\[
\boxed{
\widehat u(1/n)
=\frac{T_n}{n(1-z_n)}.
}
\tag{23}
\]

This is a finite shell identity. No Gram inversion, asymptotic approximation, zero estimate, or RH hypothesis enters it.

## 2. Discrepancy bounds the multiple-sum transform in weighted `ell^2`

Let

\[
U_t:=\sum_{s=1}^{t}u_s.
\tag{24}
\]

Because `u` has mean zero, `U_(Lambda_N)=0`; by the definition (3),

\[
|U_t|\le\Delta_N
\qquad(1\le t\le\Lambda_N).
\tag{25}
\]

Finite summation by parts gives

\[
\widehat u(1/n)
=(1-z_n)\widehat U(1/n),
\tag{26}
\]

so from (23)

\[
\widehat U(1/n)
=\frac{T_n}{n(1-z_n)^2}.
\tag{27}
\]

Now

\[
|1-z_n|
=2\sin\frac\pi n
\le\frac{2\pi}{n},
\tag{28}
\]

and hence

\[
|\widehat U(1/n)|
\ge\frac{n|T_n|}{4\pi^2}.
\tag{29}
\]

The frequencies `1/2,1/3,...,1/N` are distinct Fourier modes of the common period. Parseval and (25) therefore imply

\[
\sum_{n=2}^{N}
\frac{n^2|T_n|^2}{16\pi^4}
\le
\sum_{\xi}|\widehat U(\xi)|^2
=
\frac1{\Lambda_N}\sum_{t=1}^{\Lambda_N}|U_t|^2
\le\Delta_N^2.
\tag{30}
\]

Equivalently, if

\[
x_n:=nT_n,
\tag{31}
\]

then

\[
\boxed{
\|x\|_{\ell^2(2,\ldots,N)}
\le4\pi^2\Delta_N.
}
\tag{32}
\]

Unlike the absolute coefficient estimate in `NB-019`, no triangle inequality over the generator discrepancies has yet been used. Cross-generator cancellation is already present inside the Fourier data `T_n`.

## 3. Möbius inversion recovers the weighted coefficient vector

Put

\[
b_n:=n a_{N,n}.
\tag{33}
\]

Equation (22) is equivalent to the multiples transform

\[
\boxed{
x_n
=\sum_{q\le N/n}\frac{b_{qn}}{q^2}.}
\tag{34}
\]

Finite Möbius inversion gives

\[
\boxed{
b_n
=\sum_{q\le N/n}\frac{\mu(q)}{q^2}x_{qn}.}
\tag{35}
\]

Indeed substituting (34) into the right side groups each `b_(kn)/k^2` with `sum_(q|k)mu(q)`, leaving only `k=1`.

For each fixed `q`, the restriction `x_n -> x_(qn)` is an `ell^2` contraction. Minkowski's inequality applied to (35) therefore yields

\[
\begin{aligned}
\|b\|_2
&\le
\sum_{q\ge1}\frac{|\mu(q)|}{q^2}\|x\|_2\\
&=\frac{15}{\pi^2}\|x\|_2.
\end{aligned}
\tag{36}
\]

Combining (32) and (36) proves (4).

The proof exposes the exact information carrier. `Delta_N` controls the antiderivative of the shell residual; the root-of-unity modes read divisor-multiple sums of the projection coefficients; Möbius inversion then reconstructs those coefficients. Thus the coefficient coercivity is not an arbitrary norm comparison imposed on the Gram system.

## 4. High-index projection gain is bounded by the same discrepancy

The canonical generators obey the elementary norm estimate

\[
\boxed{
\|g_j\|^2\le\frac2j.
}
\tag{37}
\]

To see this from (20), split the shell norm at `j`. For `t<j`, `{t/j}=t/j`, so

\[
\sum_{t<j}\frac{\{t/j\}^2}{t(t+1)}
<\frac1j,
\]

while for `t>=j` use `{t/j}^2<=1` and telescope

\[
\sum_{t\ge j}\frac1{t(t+1)}=\frac1j.
\]

Now (4), Cauchy--Schwarz and (37) give

\[
\begin{aligned}
\|w_{N,>K}\|
&\le
\sum_{j>K}|a_{N,j}|\|g_j\|\\
&\le
\left(\sum_{j>K}j^2|a_{N,j}|^2\right)^{1/2}
\left(\sum_{j>K}\frac{\|g_j\|^2}{j^2}\right)^{1/2}\\
&\le
60\Delta_N
\left(2\sum_{j>K}\frac1{j^3}\right)^{1/2}\\
&\le\frac{60\Delta_N}{K},
\end{aligned}
\tag{38}
\]

which is (7).

Because `v_(N,<=K)` lies in `V_K`, it is an admissible competitor for the `K`-section distance. Moreover `r_N` is orthogonal to `w_(N,>K)`, since the latter lies in `V_N`. Hence

\[
\begin{aligned}
d_K^2
&\le\|e-v_{N,\le K}\|^2\\
&=\|r_N+w_{N,>K}\|^2\\
&=d_N^2+\|w_{N,>K}\|^2.
\end{aligned}
\tag{39}
\]

Nested orthogonal projections also give the exact identity

\[
\|r_K-r_N\|^2=d_K^2-d_N^2.
\tag{40}
\]

Equations (38)--(40) prove (8).

This is not a statement that the optimal coefficient vector is sparse. It says something basis-stable at the Hilbert level: if the shell discrepancy is small relative to `K`, allowing all generators with indices in `(K,N]` changes the best residual by at most `60 Delta_N/K`.

## 5. The Möbius coefficient core forces an intrinsic discrepancy floor

`NB-020` proves that there are absolute constants `C_0,c_0,x_0>0` such that, for every sufficiently large `x`, the squarefree indices satisfying `sigma(n)<=C_0n` carry weighted mass

\[
\sum_{\substack{n\le x\\\mu(n)^2=1\\\sigma(n)\le C_0n}}n
\ge c_0x^2.
\tag{41}
\]

It also proves the coefficient locking estimate

\[
|a_{N,n}+\mu(n)|\le2d_N\sigma(n).
\tag{42}
\]

Choose the same sufficiently small absolute `c_*>0` as in `NB-020` and put

\[
x_N=\left\lfloor
\min\left\{N,\frac{c_*}{d_N}\right\}
\right\rfloor.
\tag{43}
\]

On the subset counted by (41) with `n<=x_N`, equation (42) gives `|a_(N,n)|>=1/2`. If this set is `S_N`, then Cauchy--Schwarz and `|S_N|<=x_N` give

\[
\sum_{n\in S_N}n^2
\ge
\frac{(\sum_{n\in S_N}n)^2}{|S_N|}
\ge c_0^2x_N^3.
\tag{44}
\]

Therefore

\[
\left(\sum_{n=2}^{N}n^2|a_{N,n}|^2\right)^{1/2}
\ge\frac{c_0}{2}x_N^{3/2}.
\tag{45}
\]

Combining (45) with (4), and absorbing the harmless floor and fixed small-scale regime into absolute constants, proves (9).

The distinction from `NB-020` is important. That finding forces the absolute weighted budget

\[
\mathfrak A_N=\sum j|a_{N,j}|
\gg d_N^{-2}
\]

in the small-distance regime. Such a large `ell^1` budget could in principle have much smaller shell discrepancy because generator discrepancies cancel. Equation (9) shows that this cancellation has a quantitative limit: the intrinsic discrepancy itself must still be at least of order `d_N^{-3/2}`.

## 6. The sublinear branch compresses both section and transport

Assume (12) and use (13). Then

\[
\frac{K_N}{N}
\le
\frac2N+
\sqrt{\frac{1+\Delta_N}{N}}
\longrightarrow0,
\tag{46}
\]

while

\[
\frac{\Delta_N}{K_N}
\le
\frac{\Delta_N}{\sqrt{N(1+\Delta_N)}}
\le
\sqrt{\frac{\Delta_N}{N}}
\longrightarrow0.
\tag{47}
\]

Equation (8) gives (14). Independently, `NB-021` uses the same scale and the rooted normal equation to obtain (15). These statements concern different objects: (14) says the finite target approximation from `K_N` through `N` carries vanishing Hilbert gain, whereas (15) says the semigroup images of the `N`-residual vanish uniformly after `K_N`. Their conjunction is the new structural boundary.

It does **not** make the interval below `K_N` harmless. A source-specific theorem could still extract the divergent `NB-015` budget entirely from pre-transition channels, and the scale can move irregularly with `N`. Nor does (14) imply coefficientwise equality between the `N`- and `K_N`-optimal projections; it is a Hilbert-space approximation statement obtained by truncating the `N` coefficients and then comparing with the true `K_N` optimum.

The alternative branch is equally explicit. If `Delta_N` is not sublinear, then there is linear-scale consecutive variation available in the canonical shell residual. Turning that variation into `NB-015` visible graph energy remains a separate arithmetic problem; equation (4) alone does not supply the required lower bound for `rho_(N,M)/beta_(N,M)`.

## 7. Prior-art boundary and falsification controls

The ingredients are individually classical: finite Fourier analysis and Parseval, the root-of-unity transform of a sawtooth sequence, Möbius inversion, and the Nyman--Beurling/Báez--Duarte finite approximation framework. The Möbius role in Nyman approximants is already classical and is explicitly separated from the finite coefficient-locking delta in `NB-020`. `SOURCES.md` already anchors Báez--Duarte, Bagchi, Burnol, and Bettin--Conrey--Farmer.

A targeted prior-art check covered Báez--Duarte's arithmetical and discrete formulations, Bagchi's semigroup survey, numerical finite-section work, generalized coefficient-controlled Nyman approximation, Ehm's 2024 Gram-matrix analysis, and recent Mellin/Gram approaches. Those sources contain Möbius identities, coefficient questions, Fourier/Mellin descriptions, or Gram decompositions, but no located source stated the finite implication (23)--(36) from **consecutive shell discrepancy of the actual projection residual** to the weighted optimal-coefficient norm, nor the section-compression consequence (8). Search absence is not a claim of priority, and no newly located external theorem is load-bearing, so `SOURCES.md` is unchanged.

Several boundaries are load-bearing:

- Equation (4) is one-sided. A large weighted coefficient norm forces discrepancy, but large discrepancy need not imply useful visible semigroup energy.
- The exact Fourier sparsity uses the canonical harmonic-shell realization and the common finite period. It is not a generic statement about arbitrary bases with the same Gram matrix.
- Equation (8) bounds the **additional approximation gain** above `K`; it does not identify the optimal `K` coefficients with the first `K` optimal `N` coefficients.
- The lower bound (9) uses the source-specific Möbius locking from `NB-020`. Without accurate approximation to the target, arbitrary finite coefficient vectors need not have such an intrinsic discrepancy floor.
- The hypothesis `Delta_N=o(N)` remains unproved. Under that hypothesis, compression and invisibility narrow the route but do not establish `d_infinity=0` or any improved rate.
- Burnol is used only to simplify the branch in (9) to (10); no zero-sensitive lower bound is used in the exact Fourier/section-compression theorem.

The finding is falsified by a counterexample to the root-of-unity identity (23), the multiples Möbius inversion (35), the Parseval estimate (30), the section bound (8), or a canonical residual satisfying the hypotheses of `NB-020` while violating (9).

The research consequence is sharper than the previous mixing-only obstruction. The live route must now operate below a discrepancy-selected sublinear section, or prove that the canonical residual has linear-scale discrepancy and convert that variation into the source-visible multiplicative energy required by `NB-015`. Increasing either generator depth or dilation depth after the common transition cannot by itself restore the missing transport.