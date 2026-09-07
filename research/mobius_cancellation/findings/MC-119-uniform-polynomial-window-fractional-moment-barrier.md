# MC-119 — Balanced prime blocks defeat sub-L1 transfer across a polynomial scale window

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-CONTROL`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `0<p<1`. Choose an exponent

\[
\frac34<a<\min\!\left(\frac{p+2}{2(p+1)},0.99\right)
\tag{1}
\]

and then choose

\[
1<\theta<\theta_*(a,p)
:=
\frac{2-a(p+1)}{1-p/2}.
\tag{2}
\]

For every sufficiently large scale `Q`, there exists a multiplicative function

\[
f_Q:\mathbb N\to\{-1,0,1\},
\qquad |f_Q(n)|=\mu(n)^2,
\tag{3}
\]

such that, with

\[
S_Q(N)=\sum_{n\le N}f_Q(n),
\qquad
P_{p,Q}(X)=
\left(\frac1X\sum_{N<X}|S_Q(N)|^p\right)^{1/p},
\qquad
D_{1,Q}(X)=\frac1X\sum_{N<X}|S_Q(N)|,
\tag{4}
\]

one has the **uniform polynomial-window bound**

\[
\boxed{
P_{p,Q}(X)
\ll_{p,a,\theta}
(\log Q)^{2/p}X^{1/2}
\qquad
(Q\le X\le Q^\theta),
}
\tag{5}
\]

while simultaneously

\[
\boxed{
D_{1,Q}(Q)
\gg_{p,a}
\frac{Q^{2a-1}}{\log Q}.
}
\tag{6}
\]

Because `a>3/4`, the exponent in `(6)` is strictly larger than `1/2`. Thus even exact square-free support, exact multiplicativity, and RH-scale fractional `p`-moment control at **every intermediate cutoff in a fixed polynomial window** do not generically imply RH-scale first-absolute-moment control when `p<1`.

Equivalently, since the logarithmic factor in `(5)` is `X^{o(1)}`, for every `epsilon>0`,

\[
P_{p,Q}(X)
\ll_{\epsilon,p,a,\theta}
X^{1/2+\epsilon}
\qquad
(Q\le X\le Q^\theta)
\tag{7}
\]

uniformly throughout the window.

The admissible window is genuinely polynomial. Letting `a` decrease to `3/4` shows that for every

\[
1<\theta<\Theta_p
:=
\frac{5-3p}{4-2p}
=1+\frac{1-p}{4-2p},
\tag{8}
\]

one can choose `a>3/4` so that `(2)` holds. Hence `\theta` may be separated from `1` by a fixed positive amount depending only on `p`.

This strengthens `MC-118`. That finding controlled the weak statistic at the source scale and one subpower-separated future scale. The present result removes the immediate escape that the missing information might be recovered merely by requiring the same fractional moment bound at all intermediate scales over a substantial finite horizon. The surviving distinction is no longer sparse scale coverage over that horizon: it must use one-function coherence across unbounded scales, genuinely Möbius-specific prime/correlation information, or another source relation absent from the comparator.

## 1. Reuse the balanced terminal prime block

Take the balanced-block construction of `MC-118` with

\[
H=\lfloor Q^a\rfloor.
\tag{9}
\]

Inside `(Q-H,Q]`, choose equal-sized prime sets `P_+` and `P_-` in separated thirds, with signs `+1` and `-1`, respectively. The short-interval prime theorem recorded as `MC-S32` gives

\[
|P_+|=|P_-|=:L\asymp\frac H{\log Q}.
\tag{10}
\]

The explicit upper restriction `a<0.99` in `(1)` keeps this invocation inside the quoted range of `MC-S32`; it is immaterial to the barrier because the critical choice is `a` just above `3/4`.

Let

\[
B(y)=\sum_{\substack{q\in P_+\cup P_-\\q\le y}}b_q,
\qquad
b_q=
\begin{cases}
+1,&q\in P_+,\\
-1,&q\in P_-.
\end{cases}
\tag{11}
\]

Then `B` has a plateau of height `L` and width comparable with `H`, but

\[
\sum_q b_q=0,
\tag{12}
\]

so it returns exactly to zero after the terminal block.

As in `MC-118`, define `g` to vanish at the selected primes, to take independent Rademacher signs at every other prime, and to vanish on prime powers of exponent at least two. Restore the selected prime signs to obtain `f_Q`. For every `N<(Q-H)^2`, at most one selected prime can divide `N`, and the exact decomposition is

\[
\boxed{
S_Q(N)=G(N)+R(N),
\qquad
R(N)=\sum_{m\ge1}g(m)B(N/m),
}
\tag{13}
\]

with `G(N)=\sum_{m\le N}g(m)`.

The balance `(12)` localizes each multiplier copy: a term with multiplier `m` contributes only when

\[
Q-H<\frac Nm<Q.
\tag{14}
\]

For `0<p<1`, subadditivity therefore gives, uniformly for every `X<(Q-H)^2`,

\[
\boxed{
\sum_{N<X}|R(N)|^p
\ll
L^p\left(
H\left(\frac XQ\right)^2+rac XQ
\right).
}
\tag{15}
\]

This is the same exact transport bound as in `MC-118`; the new step is to keep its exponent budget uniformly over an interval of scales rather than evaluate it at one future cutoff.

## 2. The transport budget stays subcritical on the whole window

Write

\[
X=Q^u,
\qquad 1\le u\le\theta.
\tag{16}
\]

Ignoring only logarithmic factors from `L`, the first term on the right of `(15)` has `Q`-exponent

\[
a(p+1)+2u-2,
\tag{17}
\]

whereas the square-root `p`-moment budget

\[
X^{1+p/2}
\tag{18}
\]

has `Q`-exponent `u(1+p/2)`. Their exponent gap is

\[
\Delta_1(u)
=
2-a(p+1)-u(1-p/2).
\tag{19}
\]

It decreases with `u`, and `(2)` is exactly the condition

\[
\Delta_1(\theta)>0.
\tag{20}
\]

The second term in `(15)` has `Q`-exponent `ap+u-1`. Its gap below `(18)` is

\[
\Delta_2(u)
=
1+p\left(\frac u2-a\right)
\ge
1+p\left(\frac12-a\right)>0,
\tag{21}
\]

because `a<1`.

Hence there is an `eta=eta(p,a,theta)>0` such that

\[
\sum_{N<X}|R(N)|^p
\ll
Q^{-\eta}X^{1+p/2}
\qquad
(Q\le X\le Q^\theta).
\tag{22}
\]

The interval remains safely inside the one-selected-prime regime of `(13)`: the maximal value of `theta_*(a,p)` under `0<p<1` and `a>3/4` is approached at `p\downarrow0`, `a\downarrow3/4`, where it is `5/4`. Thus every admissible `theta` is strictly below `2`, and `Q^\theta<(Q-H)^2` for all sufficiently large `Q`.

Equation `(8)` is obtained by letting `a\downarrow3/4` in `(2)`:

\[
\theta_*(3/4,p)
=
\frac{5-3p}{4-2p}.
\tag{23}
\]

The surplus over `1` vanishes as `p\uparrow1`, coherently with the exact generic transfer threshold at `p=1` established in `MC-117`.

## 3. One random background realization works at every cutoff

For the Rademacher background `g`, distinct square-free `P`-free integers are orthogonal, so exactly as in `MC-118`,

\[
\mathbb E|G(N)|^2\le N.
\tag{24}
\]

Since `0<p<2`,

\[
\mathbb E|G(N)|^p
\le
N^{p/2},
\tag{25}
\]

and therefore

\[
\mathbb E
\sum_{N<X}|G(N)|^p
\ll_p
X^{1+p/2}.
\tag{26}
\]

To make this simultaneous in `X`, take a dyadic mesh from `Q` to `Q^\theta`, including the exact endpoint. It has

\[
K=O(\log Q)
\tag{27}
\]

points. At every mesh point `X_j`, Markov's inequality gives

\[
\Pr\!\left(
\sum_{N<X_j}|G(N)|^p
>
C K^2 X_j^{1+p/2}
\right)
\ll_p \frac1{C K^2}.
\tag{28}
\]

Summing over all mesh points makes the total failure probability `O_p(1/(CK))`.

The same realization must also leave the source excursion visible. On the plateau of `(11)`, `MC-118` gives

\[
\mathbb E\sum_{N\in\text{plateau}}|G(N)|
\ll H\sqrt Q,
\tag{29}
\]

while the deterministic signal mass is

\[
HL\asymp\frac{H^2}{\log Q}.
\tag{30}
\]

Their ratio is

\[
\frac{H\sqrt Q}{HL}
\ll Q^{1/2-a}\log Q=o(1).
\tag{31}
\]

A further Markov bound therefore shows that, with probability tending to one, the background absolute mass on the plateau is at most half of the signal mass. Intersecting this event with the simultaneous mesh event from `(28)` leaves positive probability for all sufficiently large `Q`. Fix one realization in that intersection.

For an arbitrary `X` between two consecutive mesh points, monotonicity of the cumulative `p`-mass and the factor-two spacing give

\[
\sum_{N<X}|G(N)|^p
\ll_{p,a,\theta}
K^2X^{1+p/2}.
\tag{32}
\]

Combining `(22)` and `(32)` with

\[
|G(N)+R(N)|^p\le |G(N)|^p+|R(N)|^p
\qquad(0<p<1)
\tag{33}
\]

proves `(5)`.

On the source plateau, `R(N)=B(N)=L`. The background event just selected yields

\[
\sum_{N\in\text{plateau}}|S_Q(N)|
\gg HL,
\tag{34}
\]

and division by `Q` gives `(6)`.

## Prior-art and novelty assessment

The arithmetic input and comparator class are not new objects. `MC-S32` supplies the prime counts in the terminal intervals; square-free-supported multiplicative sign models are established prior art (`MC-S16`), and random multiplicative functions have an extensive literature on partial sums and moments. No novelty claim is made for any of those ingredients.

A targeted literature check for fractional moments of multiplicative partial sums, prescribed prime-sign perturbations, and random multiplicative partial-sum control found adjacent random-model moment and oscillation results, but no external theorem is needed for `(24)`--`(32)`: only elementary character orthogonality, Markov's inequality, and a finite dyadic union bound are used. The durable delta is narrower and internal to the present obstruction chain: the exact balanced-block transport identity already proved in `MC-118` has enough quantitative slack to defeat **interval-uniform** sub-`L^1` control over a polynomial horizon.

Accordingly this finding is labeled `NO-NOVELTY-CLAIM`. Its value is the information audit: a proposed recovery theorem cannot now rely merely on the fact that the weak fractional statistic is known continuously across nearby scales for a bounded but polynomially long future window.

## Boundaries and failure modes

This remains a scale-dependent matched control. The function `f_Q` changes with the source scale `Q`; the construction does **not** produce one fixed multiplicative function with the bad behavior along an unbounded sequence of windows. Cross-generation products would interact and require a different argument.

The selected prime signs are also not Möbius's exact prime law: Möbius has `mu(q)=-1` at every prime. As already noted in `MC-005`, exact support plus multiplicativity plus exact agreement at every prime reconstructs Möbius tautologically, so the meaningful unresolved question is to find an intermediate quantitative Möbius-specific condition rather than to impose the answer as input.

The construction does not preserve the full qualitative Chowla property of the nonmultiplicative matched control in `MC-117`. Thus it does not rule out a theorem from a genuinely joint correlation-plus-multiplicativity hypothesis, provided that hypothesis is independently available for Möbius and has enough quantitative strength.

The polynomial horizon is finite and limited by the transport exponent budget. It does not rule out an argument that extracts information specifically from consistency over an unbounded scale sequence, nor does it show that the same obstruction survives once products involving several generations of engineered prime blocks are unavoidable.

Finally, the result is specific to `0<p<1`. It is consistent with `MC-117`: at `p=1`, `D_1=P_1` by definition and there is no sub-`L^1` information-loss gap to exploit.

## Consequence for the active mean-absolute transfer route

`MC-117` showed that a square-root fractional moment does not recover the RH-complete first absolute mean from bounded increments, even with exact support, qualitative Chowla, and a subpower-dense checkpoint mesh, but its matched control was nonmultiplicative. `MC-118` restored exact multiplicativity and transported a bad excursion through one future subpower scale.

The present finding closes the next obvious scale-coverage repair: **the same multiplicative matched control can satisfy the weak square-root statistic at every cutoff in a fixed polynomial window while retaining super-square-root first-absolute mass at the source scale.** The residual escape is therefore more specific. A successful source-to-`D_M` transfer must exploit either one fixed function coherently across unbounded scales, a quantitatively strong joint multiplicativity/correlation condition, or another genuinely Möbius-specific arithmetic relation that forbids the balanced-block mechanism without already encoding RH-scale cancellation.