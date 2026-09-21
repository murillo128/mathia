# FD-243 — Sparse omission defect improves from square-root to entropy scale

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / sparse omissions / higher reciprocal-divisor moments / quantitative inverse
- **Depends on:** FD-225, FD-241, FD-242
- **Classification:** `EXACT-DERIVED + ENTROPY-SCALE-DEFECT + DENSITY-ONE-STABILITY + FINER-THAN-CAPACITY`

## Claim

FD-241 and FD-242 control the contribution of omitted response samples by applying Cauchy--Schwarz to the reciprocal-divisor weight `sigma_{-1}`. That gives a square-root loss in the omission density. The square root is not intrinsic: higher moments of the same arithmetic weight yield an entropy-scale defect.

For a real sequence `b=(b_n)` define

\[
Y(m):=(\mathscr A b)(m)
=
\sum_{d\le m}b_d
M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad Y(0)=0,
\tag{1}
\]

and assume

\[
|b_n|\le Cn
\qquad(n\ge1).
\tag{2}
\]

Let `S subset N` be the sampled response locations, put

\[
E=\mathbb N\setminus S,
\qquad
R(N)=|E\cap[1,N]|,
\qquad
S_0=S\cup\{0\},
\tag{3}
\]

and retain the FD-242 weighted sampled first variation

\[
V_S(N)
:=
\sum_{\substack{1\le m\le N\\m\in S,\ m-1\in S_0}}
\frac{|Y(m)-Y(m-1)|}{m}.
\tag{4}
\]

Define the adjacency-defect set

\[
T_N
:=
\{1\le m\le N:
 m\notin S\ \text{or}\ m-1\notin S_0\},
\qquad
\rho_N:=\frac{|T_N|}{N},
\tag{5}
\]

and

\[
h(\rho):=
\begin{cases}
\rho\log(e/\rho),&0<\rho\le1,\\
0,&\rho=0.
\end{cases}
\tag{6}
\]

Then for every integer `N>=2`,

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\,h(\rho_N)
+
\frac{V_S(N)}{N}.
}
\tag{7}
\]

The implied constant is absolute. Since `S_0` contains the known endpoint zero,

\[
|T_N|\le2R(N),
\tag{8}
\]

so with

\[
\eta_N:=\min\!\left(1,\frac{2R(N)}N\right),
\tag{9}
\]

and using that `h` is increasing on `[0,1]`,

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\,\eta_N\log\!\frac e{\eta_N}
+
\frac{V_S(N)}N,
}
\tag{10}
\]

with the first term interpreted as zero when `R(N)=0`.

As in FD-242, if

\[
Q_S(N)
:=
\sum_{\substack{m\le N\\m\in S}}
\frac{|Y(m)|}{m},
\tag{11}
\]

then `V_S(N)<=2Q_S(N)`, hence

\[
\boxed{
\frac{\sum_{N/2<n\le N}|b_n|}
     {\sum_{N/2<n\le N}n}
\ll
C\,\eta_N\log\!\frac e{\eta_N}
+
\frac{Q_S(N)}N.
}
\tag{12}
\]

Thus the `sqrt(R(N)/N)` defect in FD-241--FD-242 can be replaced by

\[
\frac{R(N)}N
\log\!\frac{eN}{R(N)}
\tag{13}
\]

up to absolute constants while leaving the sampled-residual term unchanged. The new bound is strictly smaller asymptotically whenever `R(N)=o(N)`.

## Exact inversion again isolates the only uncontrolled increments

Use the exact divisor inversion from FD-225:

\[
g=\mu*b,
\qquad
b=\mathbf1*g,
\qquad
\boxed{g(m)=Y(m)-Y(m-1).}
\tag{14}
\]

Outside `T_N`, both endpoints of the first difference are sampled, so `g(m)` is measured by (4). On `T_N`, the coefficient envelope gives exactly the same pointwise estimate as in FD-241--FD-242:

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
\tag{15}
\]

The improvement therefore reduces to a sparse-subset estimate for `sigma_{-1}`. FD-241 used its bounded second moment. The required stronger statement is elementary.

## Sparse reciprocal-divisor mass has an entropy bound

For every `A subset [1,N]`, write

\[
t=|A|,
\qquad
\delta=t/N.
\]

Then

\[
\boxed{
\sum_{m\in A}\sigma_{-1}(m)
\ll
N\,\delta\log\!\frac e\delta,
}
\tag{16}
\]

with the right side interpreted as zero for `t=0`.

To prove this, majorize

\[
\sigma_{-1}(n)
=
\prod_{p^a\parallel n}
\left(1+\frac1p+\cdots+\frac1{p^a}\right)
\le
\prod_{p\mid n}\left(1-\frac1p\right)^{-1}
=
\frac n{\varphi(n)}
=:F(n).
\tag{17}
\]

Fix an integer `q>=1` and put

\[
a_p:=\left(1-\frac1p\right)^{-q}.
\tag{18}
\]

Because `F(n)^q=prod_(p|n) a_p`, expansion over squarefree divisors gives

\[
F(n)^q
=
\sum_{d\mid n}
\mu(d)^2
\prod_{p\mid d}(a_p-1).
\tag{19}
\]

Summing over `n<=N` and replacing each multiple count by `N/d`,

\[
\sum_{n\le N}F(n)^q
\le
N
\prod_p
\left(1+\frac{a_p-1}{p}\right)
=:N C_q.
\tag{20}
\]

The Euler product has a uniform elementary bound

\[
\boxed{C_q^{1/q}\le 2e q.}
\tag{21}
\]

For `p<=2q`,

\[
1+\frac{a_p-1}{p}\le a_p,
\]

so the `q`-th root of the small-prime part is at most

\[
\prod_{p\le2q}
\left(1-\frac1p\right)^{-1}
\le
\prod_{m=2}^{2q}
\left(1-\frac1m\right)^{-1}
=2q.
\tag{22}
\]

For `p>2q`, set `u=q/(p-1)<=1/2`. Since

\[
-q\log\!\left(1-\frac1p\right)
\le
\frac q{p-1}=u,
\]

we have

\[
a_p-1\le e^u-1\le2u=\frac{2q}{p-1}.
\tag{23}
\]

Therefore

\[
\begin{aligned}
\log
\prod_{p>2q}
\left(1+\frac{a_p-1}{p}\right)
&\le
2q\sum_{p>2q}\frac1{p(p-1)}\\
&\le
2q\sum_{m>2q}\frac1{m(m-1)}
=1.
\end{aligned}
\tag{24}
\]

The large-prime part contributes at most `e^(1/q)` after taking a `q`-th root, proving (21). Hence

\[
\left(\sum_{n\le N}F(n)^q\right)^{1/q}
\le
2e q\,N^{1/q}.
\tag{25}
\]

Hölder now gives

\[
\sum_{m\in A}\sigma_{-1}(m)
\le
\sum_{m\in A}F(m)
\le
2e q\,N^{1/q}t^{1-1/q}
=
2e q\,N\delta^{1-1/q}.
\tag{26}
\]

For `0<delta<=1`, choose

\[
q=\left\lceil\log\frac e\delta\right\rceil.
\tag{27}
\]

Then

\[
q\le2\log\frac e\delta,
\qquad
\delta^{-1/q}\le e,
\tag{28}
\]

and (26) becomes (16). In other words, the square-root loss in FD-241 was exactly the cost of stopping this moment argument at `q=2`; adapting the moment order to the sparsity produces the entropy factor.

## Capacity estimate

Since `b=1*g`,

\[
|b_n|
\le
\sum_{d\mid n}|g(d)|.
\tag{29}
\]

Summing over `(N/2,N]` and using

\[
\#\{n\in(N/2,N]:d\mid n\}
\le
\frac{2N}{d},
\tag{30}
\]

we get

\[
\sum_{N/2<n\le N}|b_n|
\le
2N\sum_{d\le N}\frac{|g(d)|}{d}.
\tag{31}
\]

On `T_N`, equations (15) and (16) give

\[
2N\sum_{d\in T_N}\frac{|g(d)|}{d}
\ll
C N^2 h(\rho_N).
\tag{32}
\]

Outside `T_N`, equation (14) is an observed adjacent difference, so

\[
2N\sum_{d\notin T_N}\frac{|g(d)|}{d}
=
2N V_S(N).
\tag{33}
\]

Finally,

\[
\sum_{N/2<n\le N}n
=
\frac38N^2+O(N),
\tag{34}
\]

which proves (7). Since every defect index either is omitted or immediately follows an omitted positive index, (8) follows directly from the definition of `S_0`. Equations (10) and (12) then follow from monotonicity of `h` and the FD-242 inequality `V_S<=2Q_S`.

## Finer-than-capacity consequences

The density-one qualitative threshold of FD-241 is unchanged, but the size of the surviving exact or approximate kernel below capacity is much smaller than the previous square-root estimate showed.

For example, suppose

\[
R(N)=O(N^\alpha)
\qquad(0\le\alpha<1).
\tag{35}
\]

For exact sampled zeros, `V_S(N)=0`, and (10) gives

\[
\boxed{
\sum_{N/2<n\le N}|b_n|
\ll_C
N^{1+\alpha}\log N.
}
\tag{36}
\]

By comparison, the FD-241 square-root ledger only gave order

\[
N^{(3+\alpha)/2}.
\tag{37}
\]

Thus a bounded number of omissions per scale forces octave mass `O_C(N log N)` rather than `O_C(N^(3/2))`; `N^alpha` omissions cost essentially one matching power `N^alpha`, with only a logarithmic sparsity penalty.

For approximate data the same defect improvement holds and one simply adds the unchanged term

\[
O(NV_S(N))
\]

before normalization. Hence the residual side and the omission side of the FD-242 ledger are genuinely separable: the former is already first-variation exact, while the latter benefits from higher arithmetic moments.

## What this does and does not settle

The entropy factor in (16) is **not claimed optimal**. The proof deliberately uses the crude but self-contained estimate (22), replacing the prime product by a product over all integers. Finer distribution information for `sigma_{-1}` or `n/phi(n)` could reduce the slowly varying loss further. The present result only shows that the square-root omission penalty is not a structural threshold.

The linear sampled-response barrier from FD-242 is unchanged. Profiles from FD-231/FD-238 still show that an everywhere `O(m)` response may coexist with macroscopic signed capacity, so no sharpening of the omission term alone can replace the residual requirement `V_S(N)=o(N)` or the sufficient amplitude requirement `Q_S(N)=o(N)`.

The coefficient envelope `|b_n|<=Cn` remains load-bearing because it is what converts uncontrolled response increments into the reciprocal-divisor weight in (15). No positivity, finite prime-reservoir capacity, squarefree support, or Euler coherence is used. Consequently this remains a theorem about the relaxed signed divisor-response inverse problem; it does not by itself produce a physical Möbius source or an estimate for `M(N)`.

## Prior-art and novelty boundary

A targeted literature check covered reciprocal divisor sums, moments of `n/phi(n)`, multiplicative Euler-product moment arguments, sparse-subset estimates, and stability of arithmetic convolutions. Those ingredients are classical in isolation. The search did not locate the specific estimate (7) for this Farey/Mertens divisor-response inverse problem or its combination of arbitrary omitted samples, a linear coefficient envelope, and weighted approximate response data.

No external theorem is load-bearing in the proof. The only imported line-local fact is the exact divisor inversion from FD-225; the reciprocal-divisor moment estimate (16)--(28) is derived here from the Euler product, Hölder, and elementary inequalities. No new `SOURCES.md` entry is required, and no general novelty claim is made for high-moment bounds of multiplicative functions themselves.

## Next exact question

FD-243 moves the current density-one frontier genuinely below capacity: a defect set of size `R(N)` contributes only about `N R(N) log(N/R(N))` to octave `l1` mass rather than the earlier square-root interpolation.

The next response-side question is therefore the actual sharp sparse-set norm of `sigma_{-1}` in this inversion. Improving

\[
\delta\log(e/\delta)
\]

to the correct slowly varying factor would immediately sharpen every proper density-one exact-kernel bound without changing the divisor-response algebra. Separately, crossing the linear weighted-residual barrier still requires extra source-side structure such as positivity, finite reservoir capacities, or arithmetic coherence.
