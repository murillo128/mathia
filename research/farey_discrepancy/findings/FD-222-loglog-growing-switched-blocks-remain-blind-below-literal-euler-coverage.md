# FD-222 — Log-log growing switched blocks remain blind below literal Euler coverage

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing same-source horizon block / uniform divisor-reservoir countermodel / quantitative triangular repair / pre-coverage obstruction
- **Depends on:** FD-221, FD-005
- **Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GROWING-HORIZON + LOGLOG-BLOCK + UNIFORM-DIVISOR-RESERVOIRS + QUANTITATIVE-TRIANGULAR-REPAIR`

## Claim

FD-221 proves that every **fixed** number of switched dyadic horizons remains blind until the latest Euler window literally covers the original prefix, but its constants are allowed to deteriorate with the block length. The first genuinely growing regime can still be handled uniformly.

Let

\[
q_t=
\begin{cases}
0,&t\equiv0\pmod3,\\
3,&t\equiv1,2\pmod3,
\end{cases}
\qquad
q(n)=q_{\lfloor\log_2 n\rfloor},
\]

and

\[
\mathcal C_q^X(n)=(T-I)^{q+1}X(n),
\qquad (TF)(n)=F(2n).
\]

Fix constants

\[
C>0,
\qquad
0<\beta<1.
\tag{1}
\]

Then for all sufficiently large integers `N` and every integer

\[
1\le J\le C\log\log N,
\tag{2}
\]

there is one deterministic sequence

\[
\xi_n^{(N)}\in\{-1,0,1\},
\qquad
(\xi_n^{(N)})^2=\mu(n)^2,
\qquad
\xi_1^{(N)}=1,
\tag{3}
\]

which obeys the exact Euler relation

\[
\boxed{
\xi_{pn}^{(N)}=-\xi_n^{(N)}
\quad
(p\le \beta N,\ p\nmid n)
}
\tag{4}
\]

globally. Writing

\[
X_N(x)=\sum_{n\le x}\xi_n^{(N)},
\]

one can arrange simultaneously, for every `0<=j<J`,

\[
\boxed{
\left|
\mathcal C_{q(2^jN)}^{X_N}(2^jN)
\right|
\ll_{C,\beta} 2^J,
}
\tag{5}
\]

while

\[
\boxed{
X_N(N)\asymp_{C,\beta}
\frac{N}{2^J\log N}.
}
\tag{6}
\]

In particular, throughout (2), the entire observation block is only polylogarithmic,

\[
\max_{j<J}
|\mathcal C_{q(2^jN)}^{X_N}(2^jN)|
=(\log N)^{O_C(1)},
\tag{7}
\]

whereas the first prefix remains strongly super-square-root,

\[
|X_N(N)|
\gg_{C,\beta}
\frac{N}{(\log N)^{1+C\log2}}
\gg N^{1/2+\varepsilon_C}
\tag{8}
\]

for some fixed `epsilon_C>0` and all sufficiently large `N`.

To compare directly with FD-221, put

\[
\theta_{N,J}=\beta\,2^{-(J-1)}.
\tag{9}
\]

At horizon `2^jN`, the FD-221 fractional rule would request Euler coherence only through

\[
p\le \theta_{N,J}2^jN
=\beta\,2^{j-J+1}N
\le\beta N.
\]

Thus (4) is stronger than every requested Euler window in the growing block. The latest window reaches only the fixed fraction `beta N<N` of the original prefix, so literal prefix coverage has not occurred.

This is a true quantifier extension of FD-221: `J` may tend to infinity with `N`. It does **not** construct one permanent source valid for infinitely many horizons; the comparison source may still depend on `N` and `J`.

## 1. Growing sample depth and a uniform floor-cell width

Put

\[
s=\lfloor\log_2N\rfloor\pmod3,
\qquad
q_j=q_{s+j},
\qquad
e_j=j+q_j+1
\quad(0\le j<J),
\tag{10}
\]

and define

\[
E=\max_{0\le j<J}e_j,
\qquad
D=2^E.
\tag{11}
\]

Since `q_j in {0,3}`,

\[
J\le E\le J+3,
\qquad
2^J\le D\le 8\,2^J.
\tag{12}
\]

Under (2), therefore,

\[
D\le8(\log N)^{C\log2}.
\tag{13}
\]

Every scheduled observation is a linear combination of samples `X_N(2^kN)` with `0<=k<=E`.

The fixed-`J` proof of FD-221 chose a separate small left-neighborhood for every divisor cell. Here those neighborhoods need a common quantitative width. Set

\[
h=
\min\left\{
\frac{1-\beta}{2},
\frac{1}{2(D+1)}
\right\}.
\tag{14}
\]

For every integer `1<=d<=D`, define

\[
I_d=((d-h)N,dN).
\tag{15}
\]

These intervals are pairwise disjoint because `h<1/2`. Also every prime in every `I_d` exceeds `beta N`: for `d=1`,

\[
1-h\ge\frac{1+\beta}{2}>\beta,
\]

and for `d>=2` the interval lies above `N`.

The key point is that (14) is small enough to freeze **all** relevant floors. Fix `d<=D` and `k<=E`, and put

\[
m=\left\lfloor\frac{2^k}{d}\right\rfloor.
\]

The next discontinuity to the left of `d` occurs at `2^k/(m+1)`. Since

\[
(m+1)d-2^k
\]

is a positive integer,

\[
d-\frac{2^k}{m+1}
=
\frac{(m+1)d-2^k}{m+1}
\ge\frac1{m+1}
\ge\frac1{D+1}.
\tag{16}
\]

Hence every `c in (d-h,d)` satisfies

\[
\boxed{
\left\lfloor\frac{2^k}{c}\right\rfloor
=
\left\lfloor\frac{2^k}{d}\right\rfloor
\qquad(0\le k\le E).
}
\tag{17}
\]

Moreover

\[
h\asymp_\beta D^{-1}.
\tag{18}
\]

So the floor cells shrink only like `1/D`, not faster.

## 2. Every growing reservoir still contains enough primes

The quantitative prime-number-theorem estimate already anchored in `SOURCES.md` gives, uniformly for `d<=D`,

\[
\vartheta(dN)-\vartheta((d-h)N)
=
hN
+O\!\left(
DN\exp(-c\sqrt{\log N})
\right).
\tag{19}
\]

Because `D` is only polylogarithmic by (13),

\[
D^2\exp(-c\sqrt{\log N})=o(1).
\tag{20}
\]

Combining (18)--(20), every reservoir contains

\[
\boxed{
|I_d\cap\mathbb P|
\gg_\beta
\frac{N}{D\log N}
}
\tag{21}
\]

uniformly for `1<=d<=D`.

Choose a sufficiently small fixed `kappa_beta>0` and put

\[
A=
\left\lfloor
\kappa_\beta\frac{N}{D\log N}
\right\rfloor.
\tag{22}
\]

Then every reservoir has room for `A` selected primes with a fixed multiplicative margin.

## 3. Exact selected-Euler response survives the growing depth

Let

\[
Y=\beta N,
\qquad
P_N=\{p\text{ prime}:p\le Y\},
\qquad
Q_N=\prod_{p\in P_N}p.
\tag{23}
\]

Every squarefree integer has a unique factorization `n=am`, with `a|Q_N` and `(m,Q_N)=1`. Choose signs `eta_m in {-1,+1}` on squarefree cores coprime to `Q_N`, define

\[
\xi_{am}=\mu(a)\eta_m,
\tag{24}
\]

and put `xi_n=0` on nonsquarefree integers. Then (4) holds identically.

Start from the physical choice `eta_m=mu(m)` and alter only selected core primes `r>Y`, changing `eta_r` from `-1` to `+1`. One such flip changes the summatory function by

\[
\Delta X_N(x)
=
2\sum_{\substack{a\mid Q_N\\a\le x/r}}\mu(a).
\tag{25}
\]

By (13), `D=o(N)`, so `Y>D` for sufficiently large `N`. For `r in I_d` and `k<=E`, (17) gives

\[
\left\lfloor\frac{2^kN}{r}\right\rfloor
=
\left\lfloor\frac{2^k}{d}\right\rfloor
\le D.
\]

Every prime factor of every squarefree integer at most this quotient therefore lies in `Q_N`. Equation (25) becomes the exact response

\[
\boxed{
\Delta X_N(2^kN)
=
2M\!\left(
\left\lfloor\frac{2^k}{d}\right\rfloor
\right)
\qquad(r\in I_d,\ 0\le k\le E).
}
\tag{26}
\]

Thus the finite response table of FD-221 remains exact even though its dimension now grows with `N`.

## 4. The positive divisor-reservoir null cycle is dimension-free

Flip exactly `A` core primes in **every** reservoir `I_d`, `1<=d<=D`. At a sampled point `2^kN`, (26) gives total perturbation

\[
2A\sum_{d=1}^{D}
M\!\left(\left\lfloor\frac{2^k}{d}\right\rfloor\right).
\tag{27}
\]

For `d>2^k` the summand is `M(0)=0`. The exact divisor identity from FD-005,

\[
\sum_{d=1}^{n}
M\!\left(\left\lfloor\frac nd\right\rfloor\right)=1,
\tag{28}
\]

therefore yields

\[
\boxed{
\Delta X_N(2^kN)=2A
\qquad(0\le k\le E).
}
\tag{29}
\]

The perturbation is constant over every dyadic sample used by the growing block. Consequently every positive-order scheduled difference annihilates it exactly. The null-cycle mechanism itself has no conditioning loss as `J` grows.

The only remaining issue is whether the growing triangular repair needed to cancel the physical Möbius baselines fits inside the shrinking reservoir capacities.

## 5. Quantitative conditioning of the triangular repair

Let

\[
b_j=
\mathcal C_{q_j}^{M}(2^jN)
\qquad(0\le j<J)
\tag{30}
\]

be the physical baseline vector. As in FD-221, use the pivot reservoir

\[
d_j=2^{e_j}
\tag{31}
\]

for row `j`. The endpoint exponents `e_j` are pairwise distinct: if `i<j` and `e_i=e_j`, then

\[
j-i=q_i-q_j\in\{-3,0,3\},
\]

which would force `j-i=3` and `q_i-q_j=3`; periodicity of the schedule gives `q_i=q_j`, a contradiction.

Order rows and columns by increasing endpoint exponent. Let `V` be the response matrix of one extra prime flip in each pivot reservoir. As in FD-221,

\[
V_{ij}=0\quad(e_i<e_j),
\qquad
V_{ii}=2.
\tag{32}
\]

For a lower-triangular entry `e_i>=e_j`, every sample entering row `i` has exponent at most `e_i`. Trivially `|M(m)|<=m`, while a difference of order at most four has coefficient `l^1` norm at most `16`. Hence

\[
\boxed{
|V_{ij}|
\le32\,2^{e_i-e_j}.
}
\tag{33}
\]

Let

\[
R=\operatorname{diag}(2^{e_i}),
\qquad
B=R^{-1}VR.
\tag{34}
\]

Then `B` is lower triangular, its diagonal entries are `2`, and every strict-lower entry has absolute value at most `32`. Forward substitution gives the crude but sufficient bound

\[
\boxed{
\|B^{-1}\|_\infty\le17^J.
}
\tag{35}
\]

Indeed, if `Bz=y` and `S_i=sum_{r<=i}|z_r|`, then

\[
S_i\le\frac12\|y\|_\infty+17S_{i-1},
\]

which implies (35).

Now use the Davenport cancellation estimate already anchored in `SOURCES.md`. For every fixed exponent `L>0`, uniformly over all dyadic arguments appearing in the block,

\[
|M(x)|\ll_L\frac{x}{(\log x)^L}.
\]

Since `x` lies between `N` and `DN` and `D` is polylogarithmic,

\[
\boxed{
\|R^{-1}b\|_\infty
\ll_L
\frac{N}{(\log N)^L}.
}
\tag{36}
\]

The exact real correction vector `delta=-V^{-1}b` therefore satisfies

\[
\|\delta\|_\infty
\ll_L
D\,17^J\,
\frac{N}{(\log N)^L}.
\tag{37}
\]

Relative to the reservoir occupancy (22),

\[
\frac{\|\delta\|_\infty}{A}
\ll_{C,\beta,L}
\frac{D^2 17^J}{(\log N)^{L-1}}
\ll
\frac{68^J}{(\log N)^{L-1}}.
\tag{38}
\]

Because `J<=C log log N`, choose once and for all a fixed Davenport exponent

\[
L>1+C\log68.
\tag{39}
\]

Then (38) tends to zero. Thus every pivot count can be changed from `A` to `A+delta_j` at real level while remaining positive and inside the prime capacity with room to spare.

Take instead the integer count

\[
A+s_j,
\qquad
s_j=\operatorname{round}(\delta_j).
\tag{40}
\]

The rounding residual in row `i` is at most one half of the absolute row sum of `V`. Since the endpoint exponents are distinct positive integers,

\[
\sum_{e_j\le e_i}2^{-e_j}\le1.
\]

Using (33),

\[
\boxed{
\|b+Vs\|_\infty
\le16D
\ll 2^J.
}
\tag{41}
\]

This proves (5). The finite-index rounding loss of FD-221 grows only like the sampled dyadic depth and is still polylogarithmic throughout (2).

## 6. The macroscopic prefix defect survives the growing repair

Only the reservoir `I_1` lies below `N`. Every pivot has

\[
d_j=2^{e_j}\ge2,
\]

so none of the triangular repair counts changes the prefix at `N`.

For `r in I_1`, floor stability at `k=0` gives `floor(N/r)=1`, and each of the `A` low flips changes `X_N(N)` by exactly `2M(1)=2`. Hence

\[
X_N(N)=M(N)+2A.
\tag{42}
\]

Choosing the fixed Davenport exponent in (39) slightly larger if necessary also gives

\[
M(N)=o\!\left(\frac{N}{D\log N}\right).
\tag{43}
\]

Therefore

\[
X_N(N)
=(2\kappa_\beta+o(1))
\frac{N}{D\log N}.
\tag{44}
\]

Together with `2^J<=D<=8*2^J`, this is exactly (6). Because `2^J` is at most a fixed power of `log N`, the source retains an almost-linear prefix defect while every scheduled readout is only polylogarithmic.

## 7. Boundary, prior art, and consequence

The proof preserves the strongest representation-faithfulness conditions used in FD-221: exact squarefree support, unit amplitudes, one common source across the complete block, and every selected Euler relation through the largest requested cutoff. The new ingredient is quantitative rather than conceptual: floor-cell widths, prime capacities, triangular conditioning, Davenport decay, and integer rounding are controlled **uniformly while `J` grows**.

The logarithmic-logarithmic range is a certified regime, not a claimed sharp threshold. It arises because the crude triangular inverse costs exponentially in `J`, while the anchored Davenport theorem supplies arbitrarily large but fixed powers of `log N`. Stronger uniform conditioning or a stronger quantitative Mertens input could extend the allowed growth of `J`; failure of the present proof beyond (2) is not an obstruction there.

The result also remains nonuniform in the source itself. For each `N` and `J` a new comparison source may be chosen. It therefore does not contradict the elementary fact that one permanent squarefree source satisfying an eventually exhaustive nested family of exact Euler laws is forced to be Möbius. The still-open cofinal problem is whether a **single persistent source**, or a substantially faster growing family of coupled horizons with compatible source choices, becomes rigid before literal coverage.

A prior-art audit found neighboring work on Möbius-like multiplicative functions with prescribed prime signs and on partial sums of multiplicative functions, but not this partial-Euler, floor-response divisor-reservoir construction or its growing switched-horizon capacity law. No new external theorem is load-bearing: the proof uses only the quantitative PNT and Davenport cancellation already recorded in `SOURCES.md`, together with the exact FD-005 divisor identity.

Thus FD-221's `fixed J` restriction is not the first place where switched blindness breaks. **Any fixed multiple of `log log N` coupled horizons can still be repaired below literal Euler prefix coverage**, with a polylogarithmically small observation vector and an almost-linear earlier-prefix defect. Any coercive mechanism along this route must therefore use coherence beyond this growing finite regime, substantially better conditioning information, or a source-persistence constraint that cannot be retuned with `N`.