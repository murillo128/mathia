# FD-190 — Sub-square-root dyadic Fourier bands remain null on prime-faithful squarefree sources

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** arithmetic-admissibility boundary / Fourier-band noninjectivity / squarefree nullspace
- **Depends on:** FD-117, FD-187, FD-188, FD-189

## Claim

`FD-189` proves that, over unrestricted formal sources, the complete dyadic signed Farey Fourier band

\[
1\le k\le H^\alpha,\qquad H=2^m,
\]

is tail-injective for every `alpha>1/2` and is noninjective for `alpha<=1/2`. Its explicit endpoint null direction did not preserve squarefree support because it changed a coefficient at a power of two. The natural next question was whether elementary Möbius-side admissibility could lower the square-root exponent.

It cannot lower it below `1/2`.

Fix

\[
0<\alpha<\frac12.
\]

Let

\[
\mathcal Q_\alpha
:=
\left\{
\left\lfloor\frac{2^m}{k}\right\rfloor:
 m\ge0,
 1\le k\le 2^{\alpha m}
\right\}
\tag{1}
\]

be the complete set of cumulative-source coordinates exposed by all retained dyadic bands. Put

\[
\beta:=\frac{\alpha}{1-\alpha}<1,
\qquad
\gamma:=1-\beta
=
\frac{1-2\alpha}{1-\alpha}>0.
\tag{2}
\]

Then:

1. For every large `N`,

\[
|\mathcal Q_\alpha\cap[N,2N]|
=O_\alpha(N^\beta).
\tag{3}
\]

2. Consequently some contiguous interval

\[
J_N\subset[N,2N]\setminus\mathcal Q_\alpha
\tag{4}
\]

contains

\[
\gg_\alpha N^\gamma
\tag{5}
\]

**composite squarefree** integers.

3. If `R_N` is any set of such composite squarefree indices inside one interval `J_N`, then every perturbation `h` supported on `R_N` with

\[
\sum_{n\in R_N}h(n)=0
\tag{6}
\]

is invisible to the complete dyadic signed band history. Thus the band operator has a squarefree, prime-fixing nullspace of dimension

\[
\gg_\alpha N^\gamma.
\tag{7}
\]

4. In particular, after **any prescribed finite prefix** `X` and for **any** `0<epsilon<1`, there are composite squarefree

\[
X<u<v
\]

such that the source

\[
a_\varepsilon(n)
=
\begin{cases}
\mu(u)+\varepsilon,&n=u,\\
\mu(v)-\varepsilon,&n=v,\\
\mu(n),&n\ne u,v
\end{cases}
\tag{8}
\]

has exactly the same retained signed Fourier data as Möbius at every dyadic horizon:

\[
\boxed{
\mathcal F_{2^m}^{a_\varepsilon}(k)
=
\mathcal F_{2^m}^{\mu}(k)
\quad
\text{for all }m\ge0,
\ 1\le k\le2^{\alpha m}.
}
\tag{9}
\]

The perturbation preserves all of the following coordinatewise arithmetic facts:

- `a_epsilon(1)=1`;
- `a_epsilon(p)=-1` for every prime `p`;
- `a_epsilon(n)=0` whenever `n` is nonsquarefree;
- `sign(a_epsilon(n))=mu(n)` on every squarefree `n`;
- `|a_epsilon(n)|<2`;
- it differs from Möbius at exactly two composite squarefree coordinates, both beyond the prescribed prefix.

For every fixed `q>0`, its coefficient-amplitude discrepancy is therefore only

\[
D_{a_\varepsilon,q}(x)
=
\sum_{n\le x}|a_\varepsilon(n)-\mu(n)|^q
\le2\varepsilon^q
=O(1).
\tag{10}
\]

So squarefree support, exact prime fidelity, exact Möbius sign fidelity, bounded coefficients, finite-support perturbations and even `D_q(x)=o(x)` **do not move the power-law observation barrier below square root**. Any improvement below `alpha=1/2` must use a genuinely cross-coordinate restriction such as multiplicative compatibility, not only coordinatewise fidelity.

The endpoint `alpha=1/2` is not settled here. The counting exponent in (3) becomes linear exactly there, so this argument intentionally stops at the critical endpoint identified by `FD-189`.

## 1. Sub-square-root quotient coverage has zero density

Suppose

\[
n=\left\lfloor\frac Hk\right\rfloor\in[N,2N],
\qquad H=2^m,
\qquad k\le H^\alpha.
\tag{11}
\]

Since `k>=1` and `n>=N`, necessarily

\[
H\ge N.
\tag{12}
\]

On the other hand `n<=2N` gives

\[
\frac Hk<2N+1.
\tag{13}
\]

Using `k<=H^alpha`,

\[
H^{1-\alpha}<2N+1,
\]

hence every dyadic horizon capable of hitting `[N,2N]` satisfies

\[
N\le H<(2N+1)^{1/(1-\alpha)}.
\tag{14}
\]

For a fixed such `H`, condition `floor(H/k)>=N` implies

\[
k\le\frac HN.
\tag{15}
\]

Therefore the number of admissible `(H,k)` pairs which can produce any quotient in `[N,2N]` is at most

\[
\sum_{\substack{H=2^m\\N\le H<(2N+1)^{1/(1-\alpha)}}}
\frac HN.
\tag{16}
\]

Because the horizons are dyadic, the geometric sum is dominated by its final term:

\[
(16)
=O_\alpha\!\left(
\frac{N^{1/(1-\alpha)}}N
\right)
=O_\alpha(N^{\alpha/(1-\alpha)})
=O_\alpha(N^\beta).
\tag{17}
\]

Different pairs can of course produce the same quotient, so (17) is an upper bound for the number of distinct sampled coordinates and proves (3).

The strict inequality `alpha<1/2` is used only through

\[
\beta=\frac\alpha{1-\alpha}<1.
\tag{18}
\]

Thus the complete multihorizon quotient set itself has zero relative density on every large dyadic-scale interval. The obstruction is substantially larger than the isolated Mersenne holes used at the critical endpoint in `FD-189`.

## 2. One null corridor contains polynomially many composite squarefrees

Inside `[N,2N]`, the sampled coordinates partition the complement into at most

\[
O_\alpha(N^\beta)+1
\tag{19}
\]

maximal contiguous unsampled intervals.

The classical squarefree counting law gives

\[
\#\{N<n\le2N:\mu^2(n)=1\}
=
\frac N{\zeta(2)}+o(N).
\tag{20}
\]

Primes contribute only `o(N)` of these indices. Hence the number of **composite squarefree** integers in `[N,2N]` is

\[
\frac N{\zeta(2)}+o(N).
\tag{21}
\]

Removing the `O_\alpha(N^beta)=o(N)` sampled coordinates still leaves `gg N` composite squarefree integers in the unsampled complement. By pigeonhole over the `O_\alpha(N^beta)` unsampled intervals, at least one interval `J_N` contains

\[
\gg_\alpha N^{1-\beta}
=
\gg_\alpha N^\gamma
\tag{22}
\]

composite squarefree indices. This proves (4)--(5).

Only the positive density of squarefree integers and zero density of primes are used. The stronger quantitative squarefree estimate already anchored in `SOURCES.md` is more than sufficient; no short-interval squarefree theorem is needed because the pigeonhole argument chooses the corridor after the global count.

## 3. Every zero-sum perturbation inside one corridor is invisible

Let

\[
R_N=\{u_1<\cdots<u_r\}\subset J_N
\tag{23}
\]

consist of composite squarefree indices, and let `h` be supported on `R_N` with total sum zero. Write its cumulative perturbation as

\[
H_h(t):=\sum_{n\le t}h(n).
\tag{24}
\]

Before `u_1`, this is zero. After `u_r`, it is again zero because of (6). Any possibly nonzero value occurs only for

\[
u_1\le t<u_r,
\tag{25}
\]

which lies entirely inside the unsampled interval `J_N`. Therefore

\[
H_h(t)=0
\qquad(t\in\mathcal Q_\alpha).
\tag{26}
\]

For a retained mode `k<=H^alpha`, every divisor `d|k` also satisfies `d<=H^alpha`. By the exact source-side formula from `FD-117/189`,

\[
\mathcal F_H^a(k)
=
\sum_{d\mid k}d\,A(\lfloor H/d\rfloor).
\tag{27}
\]

Each quotient `floor(H/d)` belongs to `Q_alpha`; hence (26) makes every term of the perturbation in (27) vanish. This proves exact invisibility at every horizon and mode.

The space of vectors on `R_N` satisfying one linear equation (6) has dimension `r-1`. Combining this with (22) proves the polynomial nullity bound (7).

This is stronger than merely constructing a pair of colliding sources. Below square root the arithmetic-admissible kernel remains macroscopically large on a power scale, even though all primes and every nonsquarefree coordinate are frozen.

## 4. A two-coordinate Möbius collision after any finite prefix

Choose `N` so large that the interval from Section 2 lies beyond the prescribed prefix `X`, and choose two distinct composite squarefree points

\[
u<v
\]

inside the same `J_N`. Set

\[
h(u)=\varepsilon,
\qquad
h(v)=-\varepsilon,
\tag{28}
\]

and zero elsewhere. Then

\[
H_h(t)
=
\begin{cases}
\varepsilon,&u\le t<v,\\
0,&\text{otherwise}.
\end{cases}
\tag{29}
\]

Since `[u,v-1]` lies inside `J_N`, equations (26)--(27) prove (9).

Taking the base source to be Möbius gives exactly (8). Because `u` and `v` are composite squarefree, prime values and nonsquarefree support are untouched. If `0<epsilon<1`, then adding `epsilon` to a value `+1` or `-1`, or subtracting it, never crosses zero, so the Möbius sign is preserved. The coefficient magnitude is at most `1+epsilon<2`.

The two sources are therefore arbitrarily close in `l^infinity`, differ in only two source coordinates, and have finite `l^q` coefficient discrepancy for every finite `q`, while their complete retained Farey Fourier histories are identical. This rules out an explanation of the sub-square-root kernel based merely on the highly nonphysical formal perturbation used in `FD-189`.

## Representation audit

No new measurement coordinate has been introduced. `FD-117` identifies the signed Farey Fourier coefficient with (27), and `FD-189` proves that retaining the initial band is exactly equivalent, by divisor Möbius inversion, to retaining the quotient samples `A(floor(H/k))`. The set `Q_alpha` in (1) is therefore the actual source-coordinate coverage of the stated Farey observation family.

The new restrictions are all imposed in the original increment source: squarefree support, exact prime values, Möbius signs, bounded amplitudes and finite perturbation support. None is a property of the transformed quotient coordinates. The only physical law deliberately *not* imposed is multiplicativity across different source coordinates. That distinction is the point of the result: coordinatewise arithmetic fidelity cannot repair the information deficit, while `FD-172--FD-174` show that genuine multiplicative coupling can.

## Prior-art and novelty boundary

The fixed-horizon floor-quotient set `{floor(X/n)}` and its cardinality are classical; Randell Heyman's 2019 work is already the nearest prior-art boundary recorded by `FD-189`. Targeted searches for dyadic multihorizon quotient coverage, Farey low-band recovery under squarefree support, and arithmetic sparse-recovery analogues did not surface a theorem matching (3)--(9).

The proof uses only elementary dyadic counting plus the classical positive density of squarefree integers and zero density of primes, both already covered by durable anchors in `SOURCES.md`. No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

No global novelty claim is made. The result is scoped to the dyadic schedule, the initial signed mode segment `k<=H^alpha`, and the broad coordinatewise Möbius-faithful class above. It does not settle the endpoint `alpha=1/2`, scalar band energies, arbitrary nonuniform frequency schedules, or the fully multiplicative cone.

## Research consequence

`FD-189` left open whether natural source restrictions could push exact recovery below the square-root power. `FD-190` rules out a large family of such explanations. The obstruction survives after fixing **all primes**, killing **all nonsquarefree coefficients**, preserving the **Möbius sign at every surviving coordinate**, bounding amplitudes, fixing an arbitrary prefix and allowing only a **two-coordinate** deviation from Möbius.

Thus the remaining possibilities are sharply separated. The critical endpoint `alpha=1/2` may still behave differently inside this source class, because the zero-density coverage argument becomes exactly linear there. Below the endpoint, however, no purely coordinatewise strengthening of this type can help. To beat square root one must exploit a relation between coordinates—multiplicativity, divisor compatibility, prime-extension consistency—or change the observation family itself.

This also aligns the observation-side and source-side currencies. The perturbation has `D_(a,q)=O(1)`, so even vanishing coefficient-amplitude density is invisible below square root. By `FD-187`, the same fixed composite defect necessarily creates prime-extension energy of critical order `x/log x`. The missing information is therefore precisely relational: the signed low band sees too few cumulative coordinates to expose the prime-fan/divisor-cube inconsistency, even when the coefficient error itself is finite.