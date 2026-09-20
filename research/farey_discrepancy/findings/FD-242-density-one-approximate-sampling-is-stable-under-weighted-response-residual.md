# FD-242 — Density-one approximate sampling is stable under weighted response residual

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / approximate data / quantitative stability / signed linear capacity / weighted residual
- **Depends on:** FD-225, FD-231, FD-238, FD-241
- **Classification:** `EXACT-DERIVED + APPROXIMATE-SAMPLING-STABILITY + DENSITY-ONE-COERCIVITY + LINEAR-RESPONSE-SCALE`

## Claim

FD-241 proves capacity coercivity when the divisor response is exactly zero on a density-one sampling set. The exact support localization used there disappears as soon as the sampled values are merely small. There is nevertheless a quantitative replacement: the escaped increment mass is controlled directly by the weighted variation of the sampled response.

For a real sequence `b=(b_n)` define

\[
Y(m):=(\mathscr A b)(m)
=
\sum_{d\le m}b_d
M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad Y(0)=0,
\tag{1}
\]

and assume the linear coefficient envelope

\[
|b_n|\le Cn
\qquad(n\ge1)
\tag{2}
\]

for some fixed `C`. Let `S subset N` be the set of sampled response locations, put

\[
E=\mathbb N\setminus S,
\qquad
R(N)=|E\cap[1,N]|,
\tag{3}
\]

and write `S_0=S union {0}`. Define the weighted sampled first variation

\[
V_S(N)
:=
\sum_{\substack{1\le m\le N\\m\in S,\ m-1\in S_0}}
\frac{|Y(m)-Y(m-1)|}{m}.
\tag{4}
\]

Then for every integer `N>=2`,

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\sqrt{\frac{R(N)+1}{N}}
+
\frac{V_S(N)}{N}.
}
\tag{5}
\]

The implied constant is absolute.

There is a simpler residual-amplitude version. Set

\[
Q_S(N)
:=
\sum_{\substack{m\le N\\m\in S}}
\frac{|Y(m)|}{m}.
\tag{6}
\]

Then

\[
V_S(N)\le2Q_S(N),
\tag{7}
\]

so

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\sqrt{\frac{R(N)+1}{N}}
+
\frac{Q_S(N)}{N}.
}
\tag{8}
\]

Consequently, density-one sampling remains capacity-coercive under approximate data whenever

\[
R(N)=o(N)
\qquad\text{and}\qquad
Q_S(N)=o(N).
\tag{9}
\]

In particular, if the omitted fraction tends to zero octave-by-octave and

\[
Y(m)=o(m)
\qquad(m\to\infty,\ m\in S),
\tag{10}
\]

then

\[
\boxed{
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
\longrightarrow0,
\qquad
B_k=(2^{k-1},2^k].
}
\tag{11}
\]

Thus the exact-zero theorem of FD-241 has a robust approximate form. Literal support localization is replaced by a sparse-defect term plus a weighted sampled-residual term.

## Möbius inversion separates defect locations from observed increments

Use the exact divisor inversion from FD-225. Define

\[
g=\mu*b.
\tag{12}
\]

Then `b=1*g`, and the divisor response has first difference

\[
\boxed{
g(m)=Y(m)-Y(m-1).}
\tag{13}
\]

For exact sampled zeros, FD-241 used (13) to force `g(m)=0` whenever both `m-1` and `m` are sampled. Under approximate data those increments no longer vanish, but they are now known exactly from adjacent sampled response values.

Define the defect set

\[
T_N
:=
\{1\le m\le N:
 m\notin S\ \text{or}\ m-1\notin S_0\}.
\tag{14}
\]

If an index lies outside `T_N`, both endpoints are sampled and its increment is the observed difference in (13). If it lies inside `T_N`, then either `m` is omitted or `m-1` is omitted. Hence

\[
T_N
\subseteq
(E\cap[1,N])
\cup
((E+1)\cap[1,N]),
\]

and therefore

\[
\boxed{|T_N|\le2R(N)+1.}
\tag{15}
\]

This is the stable replacement for the support statement in FD-241. The Möbius-inverted response has two pieces: arbitrary increments on a sparse defect set, and explicitly measured increments on the sampled runs.

## The coefficient envelope controls the sparse defect

From `g=mu*b` and (2),

\[
\begin{aligned}
|g(m)|
&\le
\sum_{d\mid m}|\mu(d)|\,|b_{m/d}|\\
&\le
Cm\sum_{d\mid m}\frac1d
=
Cm\,\sigma_{-1}(m).
\end{aligned}
\tag{16}
\]

FD-241 derived the elementary mean-square estimate

\[
\sum_{m\le N}\sigma_{-1}(m)^2
\le
C_2N,
\qquad
C_2=\zeta(3)\zeta(2)^2.
\tag{17}
\]

Therefore Cauchy--Schwarz gives

\[
\boxed{
\sum_{m\in T_N}\sigma_{-1}(m)
\le
\sqrt{C_2N|T_N|}
\ll
\sqrt{N(R(N)+1)}.
}
\tag{18}
\]

So the unobserved increments retain exactly the same square-root density penalty as in the exact-zero theorem. Approximate sampling changes only the complementary, observed part.

## Divisor summation converts sampled residual variation into capacity control

Since `b=1*g`,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|.
\tag{19}
\]

Summing over `(N/2,N]` and counting multiples of `d`,

\[
\begin{aligned}
\sum_{N/2<n\le N}|b_n|
&\le
\sum_{d\le N}|g(d)|
\#\{n\in(N/2,N]:d\mid n\}\\
&\le
2N\sum_{d\le N}\frac{|g(d)|}{d}.
\end{aligned}
\tag{20}
\]

Split the last sum into `T_N` and its complement. On the defect set, (16) and (18) give

\[
2N
\sum_{d\in T_N}\frac{|g(d)|}{d}
\ll
C N^2
\sqrt{\frac{R(N)+1}{N}}.
\tag{21}
\]

Outside `T_N`, both adjacent locations are sampled, so (13) gives exactly

\[
2N
\sum_{d\notin T_N}\frac{|g(d)|}{d}
=
2N
\sum_{\substack{d\le N\\d\in S,\ d-1\in S_0}}
\frac{|Y(d)-Y(d-1)|}{d}
=
2N V_S(N).
\tag{22}
\]

Combining (20)--(22),

\[
\sum_{N/2<n\le N}|b_n|
\ll
C N^2
\sqrt{\frac{R(N)+1}{N}}
+
N V_S(N).
\tag{23}
\]

Since

\[
\sum_{N/2<n\le N}n
=
\frac38N^2+O(N),
\tag{24}
\]

this proves (5).

To obtain (7), use the triangle inequality on every sampled adjacent pair:

\[
\frac{|Y(m)-Y(m-1)|}{m}
\le
\frac{|Y(m)|}{m}
+
\frac{|Y(m-1)|}{m}.
\tag{25}
\]

The first terms sum to at most `Q_S(N)`. For `m>=2`, writing `s=m-1`,

\[
\frac{|Y(m-1)|}{m}
=
\frac{|Y(s)|}{s+1}
\le
\frac{|Y(s)|}{s},
\]

while the `m=1` predecessor is `Y(0)=0`. Thus the second terms also sum to at most `Q_S(N)`, proving (7) and hence (8).

## Density-one approximate coercivity

Suppose the omitted fraction tends to zero on dyadic octaves. As in FD-241, this is equivalent to

\[
\frac{R(2^k)}{2^k}\to0.
\tag{26}
\]

If also `Q_S(N)=o(N)`, equation (8) gives normalized octave mass tending to zero.

A useful pointwise sufficient condition is (10). Define

\[
a_m=
\begin{cases}
|Y(m)|/m,&m\in S,\\
0,&m\notin S.
\end{cases}
\tag{27}
\]

Then (10) says `a_m->0`. By Cesaro averaging,

\[
\frac{Q_S(N)}N
=
\frac1N\sum_{m\le N}a_m
\to0.
\tag{28}
\]

So any sampled residual that is genuinely sublinear in the response location is harmless at capacity scale once the omissions have density zero. More generally, no pointwise assumption is needed: the exact stability quantity is the weighted adjacent variation `V_S(N)`, and the amplitude sum `Q_S(N)` is merely a convenient sufficient upper bound.

Examples of admissible noise include a uniformly bounded sampled residual, for which `Q_S(N)=O(log N)`, and a polynomially sublinear bound `|Y(m)|=O(m^alpha)` with any fixed `alpha<1`, for which `Q_S(N)=O(N^alpha)`.

## The linear residual scale is order-sharp

The `o(N)` requirement on weighted residual mass cannot in general be relaxed to `O(N)` for unrestricted signed profiles.

FD-231, strengthened by FD-238, constructs a signed integer profile satisfying

\[
|b_n|\le n,
\qquad
\liminf_{k\to\infty}
\frac{\sum_{n\in B_k}|b_n|}
     {\sum_{n\in B_k}n}
>0,
\tag{29}
\]

while its full all-integer divisor response obeys

\[
|Y(m)|=O(m).
\tag{30}
\]

Take `S=N`, so there are no omissions. Equation (30) gives

\[
Q_S(N)=O(N).
\tag{31}
\]

On the other hand, applying (8) to the macroscopic lower bound (29) forces

\[
Q_S(2^k)\gg2^k
\tag{32}
\]

for all sufficiently large dyadic scales along which the lower bound holds. Thus these signed blind profiles live precisely at linear weighted-residual order:

\[
Q_S(2^k)\asymp2^k.
\tag{33}
\]

Accordingly, the distinction between `o(m)` and merely `O(m)` sampled response is not an artefact of the proof. Capacity-scale signed mass can coexist with an everywhere linear response, but not with density-one sampled response whose normalized amplitude vanishes in Cesaro mean.

This is an order statement, not a claim of a sharp universal constant or a pointwise threshold for every profile.

## Consequence for the response-sampling frontier

FD-241 left approximate/noisy response as the immediate unresolved response-side question because exact zeros supplied a literal support theorem for `g=mu*b`. The present estimate supplies the missing stability mechanism:

\[
\boxed{
\text{capacity mass}
\lesssim
\sqrt{\text{omission density}}
+
\text{weighted sampled residual variation}.
}
\tag{34}
\]

At density one, exact zeros are therefore not singular. They sit inside an open asymptotic regime: any residual with `V_S(N)=o(N)` gives the same capacity-negligibility conclusion. The simpler condition `Q_S(N)=o(N)` is sufficient and includes pointwise `Y(m)=o(m)` on sampled locations.

This also identifies where a stronger response-side theorem would have to go. To permit sampled residuals of genuinely linear order while still forcing capacity decay, one needs structure not present in unrestricted signed profiles, because FD-231/FD-238 already occupy that scale. The remaining possible leverage is source-side: positivity, finite reservoir capacities, or arithmetic coherence. Alternatively, one can ask for finer-than-capacity estimates when `R(N)=o(N)` but the exact kernel is nontrivial.

None of these statements supplies an estimate for the physical Mertens function or RH. They classify stability of the relaxed divisor-response inverse problem under the stated coefficient envelope.

## Stress tests and boundaries

The coefficient envelope (2) remains load-bearing. It controls arbitrary increments on omitted locations through (16); without it, a sparse defect set can carry unbounded response increments and the square-root omission term need not hold.

The residual term must measure first variation, not only a sparse collection of absolute values with no adjacency information. Formula (13) reconstructs `g(m)` from two consecutive response values. The amplitude functional `Q_S` works because it dominates that adjacent variation by the triangle inequality; it is not claimed to be optimal.

Density one remains necessary for universal capacity coercivity when exact sampled zeros are allowed. If the omitted fraction stays positive on infinitely many octaves, FD-240 already supplies exact-zero macroscopic countermodels, so no approximate theorem can repair that defect without additional hypotheses.

The theorem is signed. It neither assumes nor proves nonnegative occupancies, prime-reservoir realizability, or exact Euler coherence. Those source-side restrictions may produce stronger stability than (5), but they require a separate transversality argument.

Finally, (5) is one-sided as an inverse estimate. Small omission density and small residual variation force small coefficient capacity; large residual variation need not imply large coefficient capacity because cancellation can occur before taking absolute values.

## Prior-art and novelty boundary

A targeted literature search covered classical Möbius/Dirichlet inversion, support and sparsity questions for arithmetic convolutions, stability of sparse convolutions, and Farey/Mertens discrepancy transforms. General convolution-stability results exist in other settings—for example sparse additive convolution on torsion-free groups—but the search did not locate the present divisor-response estimate combining arbitrary density-one point omissions, a linear arithmetic coefficient envelope, and weighted approximate response residuals.

No external theorem is load-bearing here. The only ingredients are the exact inversion already established in FD-225, the elementary coefficient estimate and reciprocal-divisor mean-square bound derived in FD-241, divisor counting, and the triangle inequality. No new `SOURCES.md` entry is therefore required, and no general novelty claim is made beyond this exact Farey/Mertens divisor-response formulation.
