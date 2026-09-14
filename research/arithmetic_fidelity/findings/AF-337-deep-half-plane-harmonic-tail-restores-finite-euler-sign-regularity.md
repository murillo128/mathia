# AF-337 — deep-half-plane harmonic suppression restores every fixed Euler sign order on integer tails

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `SOURCE-COMPLEXITY-GATE`, `QUANTITATIVE-RECOVERY`, `ARITHMETIC-TAIL`, `NO-NOVELTY-CLAIM`

## Claim

AF-216 proves an all-order sign-complexity theorem for the first Dirichlet harmonic and explicitly leaves open the missing transfer to the full Euler logarithm. AF-217 shows that such a transfer cannot hold globally at every order, while AF-218--AF-220 recover only low order or separation-dependent regimes.

There is nevertheless an exact regime in which the full Euler logarithm inherits **any prescribed finite sign order** from its first harmonic: move sufficiently far into the positive real half-plane relative to the requested order, and restrict the source to a fixed multiplicative integer window escaping to infinity.

Write

\[
E_s(q):=-\log(1-q^{-s})
       =\sum_{m\ge1}\frac{q^{-ms}}m,
\qquad s>0,\ q>1.
\tag{1}
\]

For an integer `r>=1`, spacing `h>0`, and left sample `sigma>0`, consider the real sampling grid

\[
s_i=\sigma+(i-1)h,
\qquad i=1,\ldots,r.
\tag{2}
\]

Put

\[
C_r=\binom r2,
\qquad
\Gamma_{r,h}=(h+1)C_r.
\tag{3}
\]

Then the following hold.

### 1. Exact first-harmonic/tail decomposition for consecutive sample rows

For any `k>=1` and distinct

\[
1<q_1<\cdots<q_k,
\]

let

\[
D_k(\sigma,h;q)
:=\det\!\left[E_{\sigma+(i-1)h}(q_j)\right]_{i,j=1}^k.
\tag{4}
\]

Define

\[
\Phi(x):=\frac{-\log(1-x)}x
        =\sum_{m\ge1}\frac{x^{m-1}}m,
\qquad 0<x<1,
\tag{5}
\]

and the first-harmonic Vandermonde margin

\[
V_h(q_1,\ldots,q_k)
:=\prod_{1\le a<b\le k}
\left(q_a^{-h}-q_b^{-h}\right)>0.
\tag{6}
\]

Then

\[
\boxed{
\left|
(-1)^{C_k}
\frac{D_k(\sigma,h;q)}{\prod_{j=1}^k q_j^{-\sigma}}
-
V_h(q_1,\ldots,q_k)
\right|
\le
\prod_{j=1}^k\Phi(q_j^{-\sigma})-1.
}
\tag{7}
\]

Hence the explicit finite-order gate

\[
\boxed{
\prod_{j=1}^k\Phi(q_j^{-\sigma})-1
<
V_h(q_1,\ldots,q_k)
}
\tag{8}
\]

forces the checkerboard sign

\[
\boxed{
(-1)^{C_k}D_k(\sigma,h;q)>0.
}
\tag{9}
\]

Equation `(8)` has a direct interpretation: the higher-Euler-harmonic mass must be smaller than the determinant margin carried by the first Dirichlet harmonic.

### 2. Uniform strict sign regularity on escaping integer windows

Fix

\[
r\ge1,
\qquad h>0,
\qquad A>1,
\qquad
\boxed{\sigma>\Gamma_{r,h}}.
\tag{10}
\]

Then there exists `P_0=P_0(r,h,A,sigma)` such that for every `P>=P_0` and every finite increasing set of distinct integers

\[
P\le q_1<\cdots<q_N\le AP,
\tag{11}
\]

the `r x N` full-Euler sampling matrix

\[
M_{ij}=E_{\sigma+(i-1)h}(q_j)
\tag{12}
\]

is strictly sign-regular through order `r` with signature

\[
\boxed{\varepsilon_k=(-1)^{C_k}}.
\tag{13}
\]

Explicitly, for every `1<=k<=r`, every increasing row set `I` of size `k`, and every increasing column set `J` of size `k`,

\[
\boxed{
(-1)^{C_k}\det M[I,J]>0.
}
\tag{14}
\]

Equivalently, after reversing the source-column order, every minor of order at most `r` is strictly positive.

This applies in particular to **every collection of rational primes in `[P,AP]`**, but the positive theorem is stronger than primality: it holds for matched composite/integer controls at the same scale as well.

### 3. The determinant margin has an arithmetic gap factor

For any selected integer norms in `[P,AP]`, the first-harmonic margin obeys

\[
\boxed{
V_h(q_1,\ldots,q_k)
\ge
h^{C_k}(AP)^{-(h+1)C_k}
\prod_{a<b}(q_b-q_a).
}
\tag{15}
\]

Thus the finite-order transfer is governed by two competing resources:

\[
\boxed{
\text{first-harmonic source separation}
\quad\text{versus}\quad
\text{higher-harmonic Euler mass}.
}
\tag{16}
\]

The first decays polynomially with the escaping source scale because the transformed nodes `q^{-h}` coalesce; the second is suppressed like `P^{-sigma}`. Condition `(10)` is a simple sufficient exponent inequality ensuring that the higher-harmonic tail dies faster than the worst determinant margin required through order `r`.

### 4. Low-sign-variation sources are therefore detected by finitely many full-Euler samples in this regime

By the classical oscillation/nullspace theorem for strictly totally positive matrices, `(14)` implies that a nonzero coefficient vector in the kernel of `M` must have at least `r` sign changes when its entries are ordered by increasing source norm.

Consequently, for `P>=P_0`, a nonzero signed integer- or prime-supported source in `[P,AP]` with at most `r-1` ordered sign changes cannot annihilate all `r` full-Euler samples in `(2)`.

This is the full-Euler transfer that AF-216 could not supply globally: a bounded source sign budget becomes an exact finite-sample discriminator once harmonic-tail suppression beats the transformed-node collision scale.

## Derivation

### The Euler logarithm separates into harmonic columns

For the consecutive `k`-sample determinant `(4)`, absolute convergence gives

\[
E_{\sigma+(i-1)h}(q_j)
=
\sum_{m_j\ge1}
\frac{q_j^{-m_j\sigma}}{m_j}
\left(q_j^{-hm_j}\right)^{i-1}.
\tag{17}
\]

Because `k` is finite and every column series is absolutely convergent, determinant multilinearity may be applied term by term. Writing

\[
z_j=q_j^{-hm_j}\in(0,1),
\tag{18}
\]

gives the exact harmonic expansion

\[
D_k
=
\sum_{m_1,\ldots,m_k\ge1}
\left(\prod_{j=1}^k\frac{q_j^{-m_j\sigma}}{m_j}\right)
\det[z_j^{i-1}]_{i,j=1}^k.
\tag{19}
\]

The inner determinant is the ordinary Vandermonde determinant,

\[
\det[z_j^{i-1}]
=
\prod_{a<b}(z_b-z_a).
\tag{20}
\]

The tuple `m_1=\cdots=m_k=1` is exactly the first Dirichlet harmonic. Since `q_1<\cdots<q_k`, its transformed nodes satisfy

\[
q_1^{-h}>\cdots>q_k^{-h},
\tag{21}
\]

so its contribution is

\[
(-1)^{C_k}
\left(\prod_jq_j^{-\sigma}\right)
V_h(q_1,\ldots,q_k).
\tag{22}
\]

For every other harmonic tuple, all `z_j` lie in `(0,1)`, hence

\[
\left|\prod_{a<b}(z_b-z_a)\right|\le1.
\tag{23}
\]

Therefore the total absolute contribution of every non-first-harmonic tuple is bounded by

\[
\begin{aligned}
&\sum_{(m_1,\ldots,m_k)\ne(1,\ldots,1)}
\prod_j\frac{q_j^{-m_j\sigma}}{m_j}\\
&\qquad=
\prod_jE_\sigma(q_j)
-
\prod_jq_j^{-\sigma}\\
&\qquad=
\left(\prod_jq_j^{-\sigma}\right)
\left[
\prod_j\Phi(q_j^{-\sigma})-1
\right].
\end{aligned}
\tag{24}
\]

Subtracting `(22)`, dividing by the positive first-harmonic amplitude, and applying the triangle inequality proves `(7)`. The strict gate `(8)` immediately gives `(9)`.

This is more informative than saying merely that `E_s(q)=q^{-s}+O(q^{-2s})`: the determinant calculation identifies the exact quantity against which the higher harmonics must be small.

### Arbitrary row minors have the same first-harmonic sign

Now take the full matrix `(12)` and a `k x k` minor with row indices

\[
1\le i_1<\cdots<i_k\le r.
\]

Set

\[
\sigma_I=\sigma+(i_1-1)h,
\qquad
n_a=i_a-i_1,
\tag{25}
\]

so

\[
0=n_1<n_2<\cdots<n_k\le r-1.
\tag{26}
\]

For selected source norms `q_1<\cdots<q_k`, put `y_j=q_j^{-h}`. The all-first-harmonic contribution, after factoring `\prod_jq_j^{-\sigma_I}`, is the generalized Vandermonde determinant

\[
\det[y_j^{n_a}]_{a,j=1}^k.
\tag{27}
\]

The monomials `1,x^{n_2},\ldots,x^{n_k}` form a strict Chebyshev system on `(0,\infty)`. Since the `y_j` occur in decreasing order, `(27)` has sign `(-1)^{C_k}`.

For the quantitative lower bound, Jacobi's bialternant factorization writes its corrected absolute value as

\[
(-1)^{C_k}\det[y_j^{n_a}]
=
\prod_{a<b}(y_a-y_b)\,s_\lambda(y_1,\ldots,y_k),
\tag{28}
\]

where `s_lambda` is a Schur polynomial with nonnegative integer coefficients and

\[
|\lambda|
=
\sum_{a=1}^kn_a-C_k.
\tag{29}
\]

Because `0=n_1<n_2<\cdots<n_k<=r-1`,

\[
|\lambda|
\le
(k-1)(r-k).
\tag{30}
\]

### Integer spacing gives a uniform first-harmonic margin

For `P<=q_a<q_b<=AP`, the mean value theorem applied to `x^{-h}` gives

\[
q_a^{-h}-q_b^{-h}
\ge
h(AP)^{-(h+1)}(q_b-q_a).
\tag{31}
\]

Hence

\[
\prod_{a<b}(y_a-y_b)
\ge
h^{C_k}(AP)^{-(h+1)C_k}
\prod_{a<b}(q_b-q_a).
\tag{32}
\]

This proves `(15)` for consecutive rows. For an arbitrary row minor, every monomial in `s_lambda` has degree `|lambda|`, every `y_j>=(AP)^{-h}`, and the Schur polynomial is nonzero with positive coefficients. Thus

\[
s_\lambda(y)
\ge
(AP)^{-h|\lambda|}.
\tag{33}
\]

Since the `q_j` are distinct integers,

\[
\prod_{a<b}(q_b-q_a)\ge1.
\tag{34}
\]

Combining `(28)`--`(34)` gives

\[
(-1)^{C_k}\det[y_j^{n_a}]
\ge
h^{C_k}A^{-\gamma_{k,I}}P^{-\gamma_{k,I}},
\tag{35}
\]

where

\[
\gamma_{k,I}
=(h+1)C_k+h|\lambda|.
\tag{36}
\]

Using `(30)`,

\[
\gamma_{k,I}
\le
(h+1)C_k+h(k-1)(r-k)
\le
(h+1)C_r
=\Gamma_{r,h}.
\tag{37}
\]

The last inequality is strict unless the worst-size configuration is reached; explicitly, twice the difference between the right side and the middle expression equals

\[
(r-k)
\left[(h+1)r-(h-1)(k-1)\right]\ge0.
\tag{38}
\]

Therefore every first-harmonic minor has the uniform lower margin

\[
\boxed{
(-1)^{C_k}\det[y_j^{n_a}]
\ge
c_{r,h,A}P^{-\Gamma_{r,h}},
}
\tag{39}
\]

for

\[
c_{r,h,A}
:=\min\{1,h^{C_r}\}A^{-\Gamma_{r,h}}>0.
\tag{40}
\]

### Higher harmonics are uniformly smaller when `sigma>Gamma_{r,h}`

For an arbitrary row minor, harmonic expansion again applies. The generalized Vandermonde factor in a non-first-harmonic term has entries in `[0,1]`, so the elementary Leibniz bound gives absolute determinant at most `k!`. After factoring `\prod_jq_j^{-\sigma_I}`, the total higher-harmonic remainder is therefore at most

\[
k!\left[
\prod_j\Phi(q_j^{-\sigma_I})-1
\right].
\tag{41}
\]

For `0<x<=1/2`,

\[
\Phi(x)-1
=
\sum_{m\ge2}\frac{x^{m-1}}m
\le
\frac{x}{2(1-x)}
\le x,
\tag{42}
\]

so

\[
\Phi(x)\le1+x\le e^x.
\tag{43}
\]

For sufficiently large `P`, every `q_j^{-\sigma_I}<=P^{-\sigma}<=1/2` and `kP^{-\sigma}<=1`. Hence

\[
\prod_j\Phi(q_j^{-\sigma_I})-1
\le
e^{kP^{-\sigma}}-1
\le
2kP^{-\sigma}.
\tag{44}
\]

Uniformly over every minor of order at most `r`, the normalized higher-harmonic error is therefore at most

\[
2r\,r!\,P^{-\sigma}.
\tag{45}
\]

Comparing `(39)` with `(45)`,

\[
\frac{\text{higher-harmonic error}}
{\text{first-harmonic margin}}
\le
\frac{2r\,r!}{c_{r,h,A}}
P^{-(\sigma-\Gamma_{r,h})}.
\tag{46}
\]

Under `(10)`, the exponent is strictly negative and the ratio tends to zero. For all sufficiently large `P`, every minor therefore has the first-harmonic checkerboard sign. This proves `(14)`.

## Relation to the existing Euler obstruction chain

### AF-216's missing full-Euler transfer exists in a scale-dependent finite-order regime

AF-216 proves that `r` equally spaced first-harmonic Dirichlet samples detect every nonzero signed source with fewer than `r` sign changes, but explicitly warns that the higher Euler harmonics could cancel the first surviving Dirichlet component.

AF-337 gives one exact regime where that warning can be discharged. The higher harmonics are not ignored; `(7)` and `(41)` price their entire aggregate contribution. Once their mass falls below the first-harmonic determinant margin, the full Euler matrix has the same finite-order oscillation geometry as the Dirichlet matrix.

### AF-217 is not contradicted

AF-217 rules out all-order total positivity of the full Euler-log translation kernel. Here the requested order `r` is fixed first and the sufficient half-plane depth grows quadratically:

\[
\Gamma_{r,h}
=(h+1)\frac{r(r-1)}2.
\tag{47}
\]

No fixed `sigma` satisfies `(10)` for all `r`. The theorem therefore supplies a hierarchy of finite-order windows, not `PF_infinity` or global total positivity.

### AF-218 and AF-219 remain stronger at low order

AF-218 and AF-219 establish the correct full-Euler signs globally at orders two and three without a far-tail assumption and without requiring large `sigma`. AF-337 is weaker there. Its new content is that **arbitrary fixed order** becomes available on escaping integer/prime windows once the real sampling depth beats the explicit order-dependent exponent.

### AF-220's collapsing curvature certificate is not the end of the finite-order route

AF-220 supplies a curvature/separation certificate whose usable margin degenerates when transformed source columns coalesce on prime tails. AF-337 exposes a different resource balance. Even though `q^{-h}` nodes coalesce as `P->infinity`, their Vandermonde margin decays only like a finite power `P^{-Gamma}` at fixed order, while every extra Euler harmonic pays an additional `P^{-sigma}` factor. If `sigma>Gamma`, harmonic suppression wins.

Thus a failed **local-separation certificate** does not imply failure of the underlying sign property. The correct tail audit must compare the rate of source-column collision with the rate at which unwanted harmonics are attenuated.

## Exact controls and boundaries

### The theorem is not prime-specific

Integrality supplies a uniform lower bound on source spacing. Primality is not used in the proof. Rational-prime blocks satisfy the theorem, but so do matched composite or mixed integer blocks in the same multiplicative window.

Therefore AF-337 is a transport theorem for a source-complexity discriminator, not evidence that rational primes themselves have acquired a unique Euler signature.

### The multiplicative window is a real hypothesis

The bound `q_j<=AP` keeps the transformed-node collision rate polynomially comparable across the selected source set. If the largest norm grows arbitrarily faster than the smallest, the uniform lower bound `(39)` must be replaced by the actual generalized Vandermonde margin.

The exact finite-instance gate `(7)`--`(8)` remains valid without any multiplicative-window assumption.

### Integer spacing is used only for the uniform tail theorem

Equation `(7)` is valid for arbitrary distinct real `q_j>1`. The integer hypothesis enters only through `(34)`. More generally, any source class with a quantitative lower bound on the gap product in `(32)` inherits the same argument with the corresponding margin.

### The exponent threshold is sufficient, not claimed sharp

The proof bounds every non-first-harmonic contribution in absolute value and therefore discards cancellations among higher harmonics. The threshold

\[
\sigma>(h+1)\binom r2
\tag{48}
\]

is a clean uniform sufficient condition, not a characterization of the true first failing order or the optimal half-plane depth.

In particular, AF-218 and AF-219 already show that this bound is far from necessary at orders two and three.

### Exact detection is still not a scale-free inverse norm bound

Strict sign regularity forbids exact annihilation by a source below the declared sign budget. The determinant estimate provides a quantitative minor margin, but AF-337 does not derive a source-norm lower bound uniform in coefficient dynamic range, support size, or arbitrary perturbations outside `[P,AP]`.

Zero-error fidelity and stable recovery therefore remain distinct.

### The theorem stays inside the absolute-convergence region

For every nontrivial order `r>=2`, `(48)` implies `sigma>1`. No analytic continuation, functional equation, zero divisor, or critical-strip argument is used. The finding is a rigorous source-to-Euler transfer theorem in the region where the harmonic expansion is absolutely convergent.

## Prior art and novelty assessment

No novelty is claimed for the individual mathematical ingredients.

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), is the classical source for strict sign regularity, total positivity, variation-diminishing/nullspace oscillation, and composition principles. AF-216 already uses this literature for the source sign-complexity viewpoint.
- I. J. Schoenberg's classical Pólya-frequency theory supplies the global translation-kernel framework used in AF-217 and explains why an all-order conclusion would be much stronger than the finite-order theorem proved here.
- The factorization of generalized Vandermonde determinants into an ordinary Vandermonde times a Schur polynomial is Jacobi's classical bialternant formula; its use in `(28)` is standard symmetric-function algebra.
- The Euler logarithm expansion in `(1)` and the separation of the first prime-power harmonic from the higher harmonics are classical Dirichlet/Euler-product manipulations already used throughout AF-180--AF-220.

The derived contribution is the **quantitative coupling of these standard pieces** in the Arithmetic Fidelity setting: `(7)` gives an exact harmonic-tail versus determinant-margin gate, and `(10)`--`(14)` turn it into a uniform arbitrary-finite-order theorem on escaping integer/prime windows. No claim is made that determinant perturbation by a small analytic tail is new in itself.

## Consequence for the Arithmetic Fidelity frontier

The source-complexity route no longer stops at the qualitative statement in AF-216. There is now a concrete three-way budget:

\[
\boxed{
\text{requested sign order}
\;\longleftrightarrow\;
\text{source-column collision rate}
\;\longleftrightarrow\;
\text{Euler harmonic-suppression depth}.
}
\tag{49}
\]

At fixed order, collapsing prime-tail geometry can be overcome by moving sufficiently deep into the half-plane. What remains unresolved for an RH-facing use is much sharper: whether a **natural prime-derived signed discrepancy** has a source-forced finite sign budget, and whether one can transport that budget toward analytically relevant observations without paying a half-plane depth that itself destroys the desired zero-sensitive information.

That is now the correct next bottleneck; higher Euler harmonics are no longer an unconditional obstruction to finite-order sign transfer.