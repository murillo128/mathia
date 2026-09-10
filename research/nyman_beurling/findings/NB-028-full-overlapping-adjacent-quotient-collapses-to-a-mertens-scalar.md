# NB-028 — full overlapping adjacent quotient collapses to a Mertens scalar

**Status:** `EXACT-DERIVED + FULL-ADJACENT-QUOTIENT + RESIDUAL-TO-MERTENS-STABILITY + CLASSICAL-PNT-INPUT + NEGATIVE/METHOD-BOUNDARY`. `NB-027` proves that Möbius locking forces logarithmically growing coefficient mass transverse to at least one of the two disjoint checkerboard adjacent-difference matchings. That separation does not survive the most obvious enlargement of the nuisance class. Once **all overlapping adjacent differences** are admitted, their coefficient span has codimension one, and the entire source-sensitive quotient is exactly the unweighted partial sum of the canonical projection coefficients. The shell Möbius inversion from `NB-020` then shows that this scalar is a stable perturbation of `1-M(Y)`, where `M` is the Mertens function.

Let

\[
V_N=\operatorname{span}(g_2,\ldots,g_N),\qquad
r_N=e-P_{V_N}e,\qquad d_N=\|r_N\|,
\]

and write

\[
P_{V_N}e=\sum_{n=2}^N a_{N,n}g_n,
\qquad
s_n:=\|g_n\|,
\qquad
\alpha_{N,n}:=a_{N,n}s_n.
\tag{1}
\]

For `3<=Y<=N`, let `alpha_N^[Y]` denote the block `(alpha_(N,2),...,alpha_(N,Y))` and define the full adjacent coefficient nuisance space

\[
\mathcal U_Y
:=\operatorname{span}\left\{
\frac{s_ne_n-s_{n+1}e_{n+1}}
{\sqrt{s_n^2+s_{n+1}^2}}:
2\le n<Y
\right\}
\subset\mathbb R^{Y-1}.
\tag{2}
\]

Put

\[
S_Y:=\sum_{n=2}^Y\frac1{s_n^2},
\qquad
A_N(Y):=\sum_{n=2}^Y a_{N,n},
\qquad
M(Y):=\sum_{n\le Y}\mu(n).
\tag{3}
\]

Then the quotient is exact:

\[
\boxed{
\operatorname{dist}_{\ell^2}\!\left(\alpha_N^{[Y]},\mathcal U_Y\right)^2
=\frac{|A_N(Y)|^2}{S_Y}.
}
\tag{4}
\]

Moreover there is an exact residual representation

\[
\boxed{
A_N(Y)=1-M(Y)+E_N(Y),
}
\tag{5}
\]

with

\[
E_N(Y)
=r_{N,1}\bigl(M(Y)-1\bigr)
+\sum_{d=2}^Y
\bigl(r_{N,d}-r_{N,d-1}\bigr)
M\!\left(\left\lfloor\frac Yd\right\rfloor\right),
\tag{6}
\]

where `r_(N,d)` is the value of `r_N` on the harmonic shell `I_d=(1/(d+1),1/d]`. The perturbation is uniformly controlled by the actual Hilbert residual:

\[
\boxed{|E_N(Y)|\le4Yd_N.}
\tag{7}
\]

Using the canonical generator-size bound `s_n^2<=2/n` from `NB-027`, one has `S_Y>=Y^2/4`. Hence

\[
\boxed{
\operatorname{dist}_{\ell^2}\!\left(\alpha_N^{[Y]},\mathcal U_Y\right)
\le
2\frac{|1-M(Y)|}{Y}+8d_N.
}
\tag{8}
\]

In particular, at the full section `Y=N`, the classical prime number theorem in its equivalent Möbius form `M(N)=o(N)` gives

\[
\boxed{
\operatorname{dist}_{\ell^2}(\alpha_N,\mathcal U_N)
\le 8d_N+o(1).
}
\tag{9}
\]

Therefore along any closure subsequence `d_N->0`,

\[
\boxed{
\operatorname{dist}_{\ell^2}(\alpha_N,\mathcal U_N)\longrightarrow0.
}
\tag{10}
\]

This is a decisive coefficient-space control on the continuation suggested after `NB-027`: **the span of all overlapping adjacent differences is too large to serve as a source-specific nuisance quotient.** Under the very closure regime one hopes to prove, the canonical coefficient vector is asymptotically absorbed by that span. The only coefficient direction left outside it is a weighted constant mode, and the canonical loading of that mode is the scalar `A_N(Y)`, asymptotically governed by ordinary Mertens cancellation plus the residual error.

The result is deliberately not spectral. It does not say that `mathcal U_N` is a low-Rayleigh subspace, that the low spectral projector from `NB-024` is absorbed by `mathcal U_N`, or that arbitrary overlapping adjacent combinations have small Hilbert norm. Those are different statements because Gram interactions between overlapping edges can be large. What is ruled out is the simpler plan of obtaining a durable source separation merely by quotienting the normalized coefficient vector by the full adjacent-difference span.

## 1. The full adjacent span has one exact quotient coordinate

Write

\[
u_n:=
\frac{s_ne_n-s_{n+1}e_{n+1}}
{\sqrt{s_n^2+s_{n+1}^2}},
\qquad 2\le n<Y.
\tag{11}
\]

The `Y-2` vectors `u_2,...,u_(Y-1)` are linearly independent: after multiplying coordinates by the nonzero diagonal matrix `diag(1/s_2,...,1/s_Y)`, they become nonzero scalar multiples of the ordinary path differences `e_n-e_(n+1)`. Thus `mathcal U_Y` has codimension one.

A vector `q=(q_2,...,q_Y)` is orthogonal to every `u_n` exactly when

\[
s_nq_n=s_{n+1}q_{n+1}
\qquad(2\le n<Y).
\tag{12}
\]

Consequently

\[
q_Y:=\frac1{\sqrt{S_Y}}
\left(\frac1{s_2},\ldots,\frac1{s_Y}\right)
\tag{13}
\]

is the Euclidean-unit generator of `mathcal U_Y^perp`. Pairing (13) with the normalized canonical coefficient block gives

\[
\langle\alpha_N^{[Y]},q_Y\rangle
=\frac1{\sqrt{S_Y}}
\sum_{n=2}^Y a_{N,n},
\tag{14}
\]

which proves (4).

Equivalently,

\[
\mathcal U_Y
=\left\{v:\sum_{n=2}^Y\frac{v_n}{s_n}=0\right\}.
\tag{15}
\]

Thus passing from one checkerboard matching in `NB-027` to **all** adjacent edges does not leave a complicated multichannel arithmetic quotient. It leaves exactly one scalar functional.

## 2. Möbius inversion identifies that scalar with a Mertens channel

`NB-020` proves the exact shell inversion

\[
a_{N,n}
=\sum_{d\mid n}
\mu\!\left(\frac nd\right)
\bigl(r_{N,d}-r_{N,d-1}\bigr),
\qquad 2\le n\le N,
\tag{16}
\]

with `r_(N,0)=1`. Its separated form is

\[
a_{N,n}+\mu(n)
=\mu(n)r_{N,1}
+\sum_{\substack{d\mid n\\d\ge2}}
\mu\!\left(\frac nd\right)
\bigl(r_{N,d}-r_{N,d-1}\bigr).
\tag{17}
\]

Sum (17) over `2<=n<=Y` and reverse the finite divisor sums. Since

\[
\sum_{2\le n\le Y}\mu(n)=M(Y)-1,
\]

one obtains

\[
A_N(Y)+M(Y)-1
=r_{N,1}(M(Y)-1)
+\sum_{d=2}^Y
(r_{N,d}-r_{N,d-1})
M\!\left(\left\lfloor\frac Yd\right\rfloor\right),
\tag{18}
\]

which is exactly (5)--(6).

The appearance of `M(Y)` here is not a new Möbius phenomenon. Mertens sums and Möbius-weighted Nyman approximants are classical. The useful point is the finite geometric dictionary: **the unique coefficient quotient left after all adjacent differences is precisely the partial coefficient sum, and the target residual controls its deviation from `1-M(Y)`.**

## 3. The residual perturbation has operator norm `O(Y)`

The naive way to use the pointwise locking estimate of `NB-020` would sum `|a_(N,n)+mu(n)|` and lose divisor factors. The exact formula (6) does better because the Mertens weights are differences of a monotone floor partition.

Set

\[
B_j:=M\!\left(\left\lfloor\frac Yj\right\rfloor\right)
\quad(1\le j\le Y),
\qquad B_{Y+1}:=0.
\tag{19}
\]

Summation by parts in (6) gives

\[
E_N(Y)=\sum_{j=1}^Y c_j r_{N,j},
\tag{20}
\]

where

\[
c_1=B_1-B_2-1,
\qquad
c_j=B_j-B_{j+1}\quad(2\le j\le Y).
\tag{21}
\]

Let

\[
q_j:=\left\lfloor\frac Yj\right\rfloor,
\qquad
D_j:=q_j-q_{j+1},
\qquad q_{Y+1}:=0.
\tag{22}
\]

Since `|mu|<=1`,

\[
|c_j|\le D_j\quad(j\ge2),
\qquad
|c_1|\le D_1+1\le2D_1.
\tag{23}
\]

The shell norm is

\[
d_N^2
=\sum_{j\ge1}\frac{|r_{N,j}|^2}{j(j+1)}.
\tag{24}
\]

Cauchy--Schwarz therefore yields

\[
|E_N(Y)|^2
\le d_N^2
\sum_{j=1}^Y j(j+1)c_j^2
\le4d_N^2
\sum_{j=1}^Y j(j+1)D_j^2.
\tag{25}
\]

Now

\[
D_j
\le\frac{Y}{j(j+1)}+1,
\]

so, because `D_j` is a nonnegative integer,

\[
j(j+1)D_j^2
\le YD_j+j(j+1)D_j.
\tag{26}
\]

The first terms sum to `Y^2` because `sum_j D_j=Y`. For the second terms, `D_j` counts the integers `m<=Y` for which `floor(Y/m)=j`, hence

\[
\sum_{j=1}^Y j(j+1)D_j
=
\sum_{m=1}^Y
\left\lfloor\frac Ym\right\rfloor
\left(\left\lfloor\frac Ym\right\rfloor+1\right)
\le
Y^2\sum_{m=1}^Y\frac1{m^2}
+YH_Y.
\tag{27}
\]

For `Y>=3`, `H_Y<=Y`, so (25)--(27) give

\[
\sum_{j=1}^Yj(j+1)c_j^2
\le4(2+\zeta(2))Y^2<16Y^2.
\tag{28}
\]

This proves (7).

The bound is source-faithful: it uses the **actual residual shells**, not an arbitrary coefficient perturbation. In particular, it controls the full partial sum through `Y` without requiring uniform pointwise Möbius locking at every index in that range.

## 4. Canonical normalization converts the scalar bound into coefficient absorption

`NB-027` derives directly from the harmonic-shell formula the two-sided generator estimate

\[
\frac1{4n}\le s_n^2\le\frac2n.
\tag{29}
\]

The upper half gives

\[
S_Y
=\sum_{n=2}^Y\frac1{s_n^2}
\ge\frac12\sum_{n=2}^Y n
=\frac{Y(Y+1)-2}{4}
\ge\frac{Y^2}{4}.
\tag{30}
\]

Combining (4), (5), (7), and (30) proves (8).

The prime number theorem is equivalent to

\[
M(Y)=o(Y).
\tag{31}
\]

It follows from (8) that for any sequence with `Y_N->infinity`, `Y_N<=N`, and `d_N->0`,

\[
\operatorname{dist}_{\ell^2}
(\alpha_N^{[Y_N]},\mathcal U_{Y_N})\to0.
\tag{32}
\]

No special locking scale is needed. Taking `Y_N=N` gives (9)--(10) for the entire finite-section coefficient vector.

There is an even sharper comparison with `NB-024`. Along closure, `NB-024` proves that `||alpha_N||_2^2` diverges at least logarithmically on an inverse-distance scale. Here the **absolute** distance from `alpha_N` to the full overlapping adjacent span tends to zero. Hence its relative Euclidean angle to that span tends to zero a fortiori. This shows why `NB-027` had to keep the checkerboard matchings separate: the source-specific transverse mass visible against either fixed matching disappears after the two overlapping families are allowed to cooperate through the full path span.

## 5. Adversarial controls

Several distinctions are load-bearing.

First, `mathcal U_Y` is a coefficient-space span, not a certified low-Rayleigh subspace. `NB-025` gives small Rayleigh quotient for each individual adjacent cancellation, and `NB-026` extracts a large low-Rayleigh subspace from a **disjoint** packing. Neither result says that every linear combination of all overlapping edges has small Gram energy. Therefore (10) does not transport the target-selected low-spectral mass of `NB-024` into a universal low-spectral sector.

Second, (4) is coordinate-sensitive. It concerns the individually normalized canonical arithmetic dictionary and the exact adjacent vectors used in `NB-025`--`NB-027`. An arbitrary invertible basis change can alter both the meaning of adjacency and the Euclidean quotient.

Third, the PNT input in (31) is unconditional and strictly weaker than the closure statement being investigated. The argument does not use an RH-strength Mertens estimate. Conversely, (9) cannot prove closure because its right side still contains `d_N` itself.

Fourth, the small quotient is not a statement that the coefficient vector is small. Under closure `NB-024` gives growing coefficient norm while (10) gives vanishing distance to a codimension-one hyperplane. The phenomenon is cancellation in one scalar channel, not disappearance of the Möbius-sized coefficient core.

Finally, this does not contradict `NB-027`. A vector can be far from each of two different disjoint-edge checkerboard spaces while being arbitrarily close to the span generated when both overlapping edge families are combined. The present finding identifies exactly how that happens here.

## 6. Prior-art boundary and research consequence

Möbius and Mertens functions are classical in the Nyman--Beurling literature; Báez-Duarte's arithmetical formulations and natural Möbius approximants are an explicit prior-art boundary, and the implication `M(x)=o(x)` is the classical PNT. The fact that a path-difference matrix has a one-dimensional constant-mode quotient is elementary finite-dimensional linear algebra. No novelty is claimed for either ingredient separately.

A targeted literature audit covered Báez-Duarte's arithmetical and discrete Nyman criteria, Bagchi's semigroup formulation, finite/numerical Nyman work, Ehm's Gram-matrix analysis, the fractional-part autocorrelation literature, and recent Mellin-smoothed Gram work. The search did not locate the exact combination (4)--(9): the normalized canonical adjacent quotient together with the residual-stability estimate `|E_N(Y)|<=4Yd_N`. Search absence is not a priority proof. The durable content is the source-faithful obstruction obtained by composing the exact shell inversion of `NB-020` with the adjacent geometry of `NB-025`--`NB-027`.

This closes one natural continuation of the live spectral question. **Quotienting by all overlapping adjacent differences cannot isolate the target-selected arithmetic weakness:** at coefficient level it leaves only a Mertens scalar, and ordinary PNT cancellation makes even that scalar asymptotically invisible once the Nyman residual closes. A useful next spectral theorem must therefore keep more structure than the full coefficient path quotient. It could restrict the nuisance class to a genuinely low-Rayleigh closure, control the Gram energy of overlapping combinations before quotienting, or formulate a target/source-weighted projector that distinguishes Möbius-loaded weak modes without allowing the entire codimension-one path span as nuisance.

`NB-028` does not improve the Nyman distance, prove closure, or establish RH. It is a negative structural theorem: **the richest naive adjacent-difference nuisance space absorbs the canonical coefficient vector precisely because its sole transverse channel is already killed by classical Mertens cancellation plus the residual itself.**