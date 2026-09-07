# MC-118 — Balanced prime blocks preserve multiplicativity while defeating sub-L1 transfer

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `0<p<1` and choose a fixed exponent

\[
\frac34<a<a_p:=\frac{p+2}{2(p+1)}.
\tag{1}
\]

For every sufficiently large scale `Q`, put `H=\lfloor Q^a\rfloor` and

\[
T=\left\lfloor Q\exp\!\left(\sqrt{\log Q}\right)\right\rfloor.
\tag{2}
\]

Then there exists a multiplicative function

\[
f_Q:\mathbb N\to\{-1,0,1\},
\qquad |f_Q(n)|=\mu(n)^2,
\tag{3}
\]

with exact Möbius square-free support such that, for

\[
S_Q(N)=\sum_{n\le N}f_Q(n),
\qquad
P_{p,Q}(X)=\left(\frac1X\sum_{N<X}|S_Q(N)|^p\right)^{1/p},
\qquad
D_{1,Q}(X)=\frac1X\sum_{N<X}|S_Q(N)|,
\tag{4}
\]

one has

\[
P_{p,Q}(Q)\ll_p Q^{1/2},
\qquad
P_{p,Q}(T)\ll_p T^{1/2},
\tag{5}
\]

but simultaneously

\[
\boxed{
D_{1,Q}(Q)
\gg_p
\frac{Q^{2a-1}}{\log Q}.
}
\tag{6}
\]

Because `a>3/4`, the exponent in `(6)` is strictly larger than `1/2`. Meanwhile

\[
\frac{\log T}{\log Q}
=1+\frac1{\sqrt{\log Q}}+o(1)
\longrightarrow1.
\tag{7}
\]

Thus exact square-free support, multiplicativity, and square-root `p`-moment control at a scale and at a subpower-separated future scale do **not** generically transfer to square-root first-absolute-moment control when `p<1`.

The construction is driven by a balanced terminal prime block. Its important extra feature is that multiplicativity does not destroy the engineered excursion after the source cutoff. Instead, the balanced block propagates into explicit thin multiplier windows. If `P` is the selected prime set, `b_q=f_Q(q)` on `P`,

\[
B(y)=\sum_{\substack{q\in P\\q\le y}}b_q,
\tag{8}
\]

and `g` is obtained from `f_Q` by replacing the selected prime values by zero, then for every

\[
N<(Q-H)^2
\]

there is the exact decomposition

\[
\boxed{
S_Q(N)=G(N)+R(N),
\qquad
R(N)=\sum_{m\ge1}g(m)B(N/m),
}
\tag{9}
\]

where `G(N)=sum_{m<=N}g(m)`. Since the selected prime signs have total sum zero, `B` is supported inside the terminal interval of width `H`. Consequently, for `0<p<1`,

\[
\boxed{
\sum_{N\le T}|R(N)|^p
\ll
L^p\left(H\left(\frac{T}{Q}\right)^2+\frac{T}{Q}\right),
}
\tag{10}
\]

where `L=max_y |B(y)|`. For the block below, `L\asymp H/\log Q`, so `(10)` is

\[
Q^{a(p+1)+o(1)}.
\tag{11}
\]

The strict upper inequality in `(1)` is exactly

\[
a(p+1)<1+\frac p2,
\tag{12}
\]

so the multiplicative replicas stay below the square-root `p`-moment budget all the way to the subpower future scale `(2)`.

This sharpens the residual left by `MC-117`. That finding showed that exact support, qualitative Chowla, bounded increments, and subpower-dense checkpoint coverage do not make sub-`L^1` moments transfer to the RH-complete first absolute moment, but its matched control deliberately broke multiplicativity. The present result restores **exact multiplicativity** and shows that multiplicativity alone is still not the missing recovery principle. Any successful transfer must use more specific arithmetic information: for example the fixed Möbius prime law `mu(q)=-1`, one fixed function coherently across an unbounded scale sequence, a genuinely joint multiplicativity-plus-correlation input, or another source relation that forbids balanced prime-block excursions.

## 1. A balanced terminal prime block

Split the terminal interval `(Q-H,Q]` into thirds. By Guth and Maynard's uniform prime theorem (`MC-S32`), because `a>3/4>17/30`, both

\[
I_+=\left(Q-H,Q-\frac{2H}{3}\right],
\qquad
I_-=\left(Q-\frac H3,Q\right]
\tag{13}
\]

contain `\asymp H/\log Q` primes. Choose equal sets

\[
P_+\subset I_+,
\qquad
P_-\subset I_-,
\qquad
|P_+|=|P_-|=L\asymp\frac H{\log Q},
\tag{14}
\]

and let `P=P_+ union P_-`. Prescribe

\[
b_q=+1\quad(q\in P_+),
\qquad
b_q=-1\quad(q\in P_-).
\tag{15}
\]

Then

\[
\sum_{q\in P}b_q=0.
\tag{16}
\]

For every

\[
Q-\frac{2H}{3}\le y\le Q-\frac H3,
\]

all positive selected primes and no negative selected primes have entered, so

\[
B(y)=L.
\tag{17}
\]

The block therefore contains a deterministic plateau of calendar width `H/3` and height `L` while returning exactly to zero before the endpoint is passed.

The use of Guth--Maynard is only a prime-supply input. The terminal-prime multiplicative mechanism itself is elementary. It is adjacent to `MC-045`--`MC-046`, which used an unbalanced terminal prime slab to produce a persistent endpoint discrepancy. Here balancing is essential: it removes the permanent endpoint offset and makes the subsequent multiplicative propagation occur through localized multiplier windows.

## 2. Exact multiplicative transport after endpoint matching

Define an auxiliary square-free-supported multiplicative function `g` by

\[
g(q)=0\quad(q\in P),
\qquad
g(r)\in\{-1,+1\}\quad(r\notin P\text{ prime}),
\qquad
g(r^k)=0\quad(k\ge2),
\tag{18}
\]

and define `f_Q` by restoring the selected prime values `f_Q(q)=b_q` while keeping the same values as `g` at all other primes and still setting every prime power of exponent at least two to zero. Then `f_Q` is multiplicative and `(3)` holds.

Let

\[
q_0=\min P>Q-H.
\]

For `N<q_0^2`, every integer `n<=N` contains at most one selected prime factor. Therefore every term is either `P`-free or can be written uniquely as `n=qm` with `q\in P` and `m` `P`-free. It follows exactly that

\[
S_Q(N)
=G(N)+\sum_{q\in P}b_qG(N/q).
\tag{19}
\]

Expanding `G` and interchanging the finite sums gives

\[
\sum_{q\in P}b_qG(N/q)
=\sum_{m\ge1}g(m)
  \sum_{\substack{q\in P\\q\le N/m}}b_q
=\sum_{m\ge1}g(m)B(N/m),
\tag{20}
\]

which proves `(9)`.

Because of `(16)`, `B(y)=0` both before the first selected prime and after the last selected prime. Hence a term with multiplier `m` can contribute only when

\[
Q-H<\frac Nm<Q.
\tag{21}
\]

At the source scale `Q-H<=N<=Q`, every multiplier `m>=2` has `N/m<Q-H`, so

\[
\boxed{R(N)=B(N)}.
\tag{22}
\]

In particular `R(Q)=0`: the engineered excursion exactly rejoins the auxiliary path at the endpoint.

For future scales, the same excursion is not erased; it is copied into the multiplier windows `(21)`. This is the precise multiplicative cost of endpoint matching.

## 3. Fractional mass of the multiplier copies

For `0<p<1`, subadditivity of `x^p` gives from `(9)`

\[
|R(N)|^p
\le
\sum_{m\ge1}|g(m)|^p|B(N/m)|^p
\le
L^p\sum_{m\ge1}
\mathbf 1_{Q-H<N/m<Q}.
\tag{23}
\]

Sum `(23)` over `N<=T`. For a fixed `m`, condition `(21)` places `N` in an interval of length at most `mH+1`. Also `m<=T/(Q-H)`. Therefore

\[
\sum_{N\le T}|R(N)|^p
\le
L^p
\sum_{m\le T/(Q-H)}(mH+1),
\tag{24}
\]

which is `(10)` because

\[
\sum_{m\le M}(mH+1)\ll HM^2+M.
\tag{25}
\]

For `T` from `(2)`,

\[
\frac TQ=\exp(\sqrt{\log Q})=Q^{o(1)},
\]

and `L=Q^{a+o(1)}` up to the logarithmic factor. Thus `(24)` is `(11)`. Since `(12)` is strict, the balanced prime perturbation uses `o(Q^{1+p/2})` total `p`-mass throughout this future horizon.

This is the key difference from merely observing that selected primes do not create composites below `2Q`, as in `MC-046`. Formula `(20)` describes the first nontrivial multiplicative propagation regime and shows quantitatively that a zero-sum prime excursion can be replicated without paying a fixed power at a subpower multiplicative dilation.

## 4. Completing a full-support multiplicative matched control

It remains to choose the nonselected prime signs in `(18)`. Choose them independently as Rademacher variables. For distinct square-free integers not divisible by any prime of `P`, orthogonality gives

\[
\mathbb E\,g(n)g(m)=0\quad(n\ne m),
\]

so

\[
\mathbb E|G(N)|^2\le N.
\tag{26}
\]

Hence, because `0<p<1<2`,

\[
\mathbb E|G(N)|^p\le N^{p/2}.
\tag{27}
\]

Summing yields

\[
\mathbb E\sum_{N<X}|G(N)|^p
\ll_p X^{1+p/2}
\qquad(X=Q,T).
\tag{28}
\]

On the plateau from `(17)`, whose length is `\asymp H`, Cauchy--Schwarz at each time gives

\[
\mathbb E\sum_{Q-2H/3\le N\le Q-H/3}|G(N)|
\ll H\sqrt Q.
\tag{29}
\]

But

\[
HL\asymp\frac{H^2}{\log Q},
\qquad
\frac{H\sqrt Q}{HL}
\ll Q^{1/2-a}\log Q
=o(1).
\tag{30}
\]

Markov's inequality applied simultaneously to the two `p`-mass quantities in `(28)` and the plateau quantity in `(29)` therefore leaves a positive-probability set of choices for which

\[
\sum_{N<Q}|G(N)|^p\ll_p Q^{1+p/2},
\qquad
\sum_{N<T}|G(N)|^p\ll_p T^{1+p/2},
\tag{31}
\]

and

\[
\sum_{Q-2H/3\le N\le Q-H/3}|G(N)|
\le\frac12 HL
\tag{32}
\]

for all sufficiently large `Q` after adjusting harmless constants.

Fix one such realization. By `|x+y|^p<=|x|^p+|y|^p`, `(11)`, `(12)`, and `(31)`, the full partial sums `S_Q=G+R` satisfy `(5)`.

On the plateau, `(17)`, `(22)`, and `(32)` give

\[
\sum_{Q-2H/3\le N\le Q-H/3}|S_Q(N)|
\ge
\sum (L-|G(N)|)
\gg HL.
\tag{33}
\]

Dividing by `Q` proves `(6)`.

Thus the obstruction is realized by the **same exact-support multiplicative function** at both tested scales, not merely by comparing two nearby functions through a metric.

## Prior art and novelty assessment

The exact-support multiplicative comparator class is established prior art: `MC-S16` records square-free-supported multiplicative discrepancy results. Rademacher multiplicative functions are also a classical model for Möbius; the probabilistic step above uses only the elementary orthogonality calculation `(26)` and Markov's inequality, not a deep random-multiplicative-function theorem.

The prime-slab construction is directly adjacent to `MC-045`--`MC-046`, and `MC-S32` supplies the only non-elementary arithmetic input needed here. A targeted external search also found the established literature on partial sums of random multiplicative functions, including sign-change and extreme-value work, but no novelty claim is made from the absence of this exact balanced-block formulation in that search.

The durable mathematical delta is the combination of three already natural ingredients for the present line: exact support and multiplicativity, **zero-sum endpoint matching**, and the explicit multiplier-window identity `(20)` with the fractional-mass bound `(24)`. That combination answers the specific multiplicativity escape left open by `MC-117` at one source scale plus a subpower future scale.

## Boundary conditions and failure modes

This result does **not** construct one fixed multiplicative function satisfying the bad behavior on an infinite subpower-dense checkpoint sequence. The comparator `f_Q` depends on the source scale `Q`. Products involving prime blocks from several generations would interact, and controlling those interactions is a separate problem.

The construction also does not retain the qualitative Chowla property used by the nonmultiplicative control in `MC-117`. It therefore does not show that the conjunction of exact support, multiplicativity, and all fixed-shift Chowla limits is insufficient.

Most importantly, the engineered prime signs are not the Möbius prime signs: Möbius has `mu(q)=-1` at every prime. The finding rules out **generic multiplicativity** as a recovery theorem for sub-`L^1` compression; it does not rule out a theorem that exploits this fixed prime orientation or another exact Möbius identity.

The future transport bound is proved only while `T<(Q-H)^2`, so that no integer in the observation range contains two selected primes. The chosen subpower horizon `(2)` satisfies this comfortably. Beyond the quadratic scale, higher products of selected primes create additional interaction terms and `(20)` is no longer the complete expansion.

Finally, the lower bound is a first-absolute-moment statement at the source scale `Q`, while the second fractional-moment checkpoint lies at `T`. It shows that repeating the weak statistic once at a logarithmically adjacent future scale does not repair the missing amplitude information. It does not by itself defeat a hypothesis controlling that statistic uniformly at every intermediate scale or along an infinite fixed sequence for one function.

## Consequence for the active transfer route

`MC-117` identified multiplicativity as the most important major structure omitted by its exact-support Chowla control. The present result narrows that escape: **multiplicativity by itself does not suppress the rare coherent excursion; it transports a balanced prime excursion into thin multiplier windows whose sub-`L^1` mass remains power-cheap across a subpower dilation.**

Therefore a viable route from a sub-`L^1` statistic to the RH-complete mean-absolute endpoint must name a stronger source-specific mechanism. The clean remaining possibilities are fixed-function consistency across unbounded scales, a quantitative joint correlation-plus-multiplicativity constraint, or an exact Möbius-specific use of the uniform prime value `-1`. Merely adding the word "multiplicative" to the hypotheses of the generic transfer closed by `MC-117` is no longer an admissible escape.