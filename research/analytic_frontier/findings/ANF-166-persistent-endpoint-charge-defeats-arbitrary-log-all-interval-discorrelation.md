# ANF-166 — persistent endpoint charge defeats arbitrary-log all-interval discorrelation

**Status:** `EXACT-DERIVED + MATCHED-INFORMATION-CONTROL + ENDPOINT-CHARGE-PERSISTENCE + SHARP-ABSOLUTE-PREFIX-GATE`. `ANF-163`--`ANF-165` progressively strengthen control of the actual demodulated prime-minus-Cramer residual: local `L^1`, local `L^2`, and then arbitrary fixed logarithmic cancellation on every interval above the all-interval activation scale. Those facts force bow-scale endpoint completion beyond every fixed polylogarithmic enlargement of

\[
R_{\rm TV}=(XK\log X)^{1/3},
\]

but they do not by themselves force the endpoint square function to be small. There is a deterministic matched control satisfying **simultaneously** the aggregate diagonal scale, pointwise and local mass bounds, exact total-sum cancellation, and a stronger-than-any-log all-interval discrepancy bound above the Matomäki--Shao--Tao--Teräväinen activation length, while its endpoint completion remains a prescribed positive fraction of `XK log X`.

The mechanism is a persistent endpoint charge. A very small coefficient bias is accumulated only over the first controlled interval, after which the coefficients vanish near the boundary and the partial sum simply stays at height `asymp sqrt(X log X)` for almost all `K` endpoint lengths. All long interval increments are tiny, but the **absolute primitive** retains memory of the initial charge. Consequently a theorem of the form

\[
\left|\sum_{n\in I}b_n\right|\le \rho_X |I|
\qquad (|I|\ge H_0)
\]

cannot by itself imply `E_partial=o(XK log X)` unless

\[
\boxed{\rho_X H_0=o(\sqrt{X\log X}).}
\]

At the current all-interval threshold `H_0=X^{5/8+eta}`, this requires an actual power-scale gain

\[
\rho_X=o\!\left(X^{-1/8-\eta}\sqrt{\log X}\right),
\]

not merely `log^{-A} X` for every fixed `A`. Thus the next endpoint theorem is more specific than the generic “obtain a power saving” gate left by `ANF-165`: it must either anchor the absolute endpoint primitive below `sqrt(X log X)`, lower the all-interval activation essentially to the square-root scale, control the primitive square function directly, or use source-faithful prime/rough structure that rules out charge persistence.

## 1. Abstract endpoint charge-and-hold control

Use the exact finite bow geometry of `ANF-157`. Let

\[
N=X,\qquad M=N+K-1,
\]

with `K=o(X)` and `K to infinity`. Let `H_0=H_0(X)` satisfy

\[
\sqrt{X\log X}\ll H_0\ll K.
\tag{1}
\]

Fix `delta>0`, and put

\[
a_X:=\sqrt{\frac{\delta}{2}X\log X},
\qquad
q_X:=\frac{a_X}{H_0}.
\tag{2}
\]

Define the edge sequence `e=(e_n)_{1<=n<=M}` by

\[
e_n=
\begin{cases}
q_X,&1\le n\le H_0,\\
-q_X,&M-H_0<n\le M,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]

The two edge blocks have equal and opposite total charge, so

\[
\sum_{n=1}^M e_n=0.
\tag{4}
\]

For every contiguous integer interval `I subset [1,M]`, the intersection with each edge block has length between `0` and `H_0`. Therefore

\[
\boxed{
\left|\sum_{n\in I}e_n\right|\le q_XH_0=a_X.
}
\tag{5}
\]

This estimate is independent of the length of `I`. In particular, for every `|I|>=H_0`,

\[
\left|\sum_{n\in I}e_n\right|
\le q_X|I|.
\tag{6}
\]

Now inspect the endpoint primitives in the exact completion formula of `ANF-157`. Since `H_0<K` and the two edge blocks are farther apart than `K`,

\[
S_r^-:=\sum_{n=1}^r e_n
=q_X\min(r,H_0),
\]

and, up to the irrelevant sign,

\[
|S_r^+|:=\left|\sum_{n=M-r+1}^{M}e_n\right|
=q_X\min(r,H_0)
\qquad (1\le r<K).
\tag{7}
\]

Hence

\[
\begin{aligned}
E_\partial(e)
&=2q_X^2\left(
\sum_{r=1}^{H_0}r^2
+(K-1-H_0)H_0^2
\right)\\
&=2a_X^2K\left(1+O(H_0/K)\right).
\end{aligned}
\tag{8}
\]

Using (2),

\[
\boxed{
E_\partial(e)
=\delta XK\log X\,(1+o(1)).
}
\tag{9}
\]

Thus an endpoint square function of bow size is compatible with every long interval sum being bounded by the single absolute number `a_X asymp sqrt(X log X)`. The large completion is not produced by a long coherent block of coefficients. It is produced by a short initial charging region followed by a long interval on which the coefficients are exactly zero but the primitive remains charged.

## 2. The control can also match the bow diagonal and all aggregate source budgets

The edge sequence alone has too little global `L^2` mass to imitate the diagonal normalization of the actual residual. That is easy to repair without changing either endpoint completion or long-interval discrepancy.

Let

\[
L:=\lfloor\log X\rfloor,
\]

and choose the largest even integer `J` for which

\[
n_j:=K+jL\le N,
\qquad 1\le j\le J.
\tag{10}
\]

Define a central alternating sparse calibrator

\[
c_{n_j}:=(-1)^jL,
\qquad
c_n:=0\quad\text{otherwise}.
\tag{11}
\]

Because `J` is even,

\[
\sum_n c_n=0.
\tag{12}
\]

Every interval contains a consecutive set of these spikes, and the alternating sum of any consecutive set has magnitude at most `L`. Thus

\[
\boxed{
\left|\sum_{n\in I}c_n\right|\le L
}
\tag{13}
\]

for every interval `I`. Moreover

\[
\sum_{n\in I}|c_n|
\le |I|+2L,
\qquad
\sum_{n\in I}|c_n|^2
\le L|I|+2L^2.
\tag{14}
\]

Since `K=o(X)`, the number of spikes is

\[
J=(1+o(1))\frac{X}{L},
\]

and therefore

\[
\boxed{
\sum_{n=1}^M|c_n|^2
=(1+o(1))X\log X.
}
\tag{15}
\]

All spikes lie in the full-incidence coefficient region `K<n<=N`, so their contribution to the exact moving-window diagonal of `ANF-157` is

\[
D_{N,K}(c)
=K\sum_n|c_n|^2
=(1+o(1))XK\log X.
\tag{16}
\]

They lie outside the first and last `K-1` coefficients, hence contribute **nothing** to either endpoint primitive in `E_partial`.

Set

\[
b:=c+e.
\tag{17}
\]

The supports are disjoint. Equations (4) and (12) give exact global centering,

\[
\sum_n b_n=0.
\tag{18}
\]

The edge contribution to the moving-window diagonal is only `O(X log X)`, because the edge incidence ramps are at most `H_0` there and `q_X^2H_0^2=asymp X log X`. Hence

\[
\boxed{
D_{N,K}(b)
=(1+o(1))XK\log X.
}
\tag{19}
\]

At the same time, (9) is unchanged:

\[
\boxed{
E_\partial(b)
=\delta XK\log X\,(1+o(1)).
}
\tag{20}
\]

The familiar aggregate source envelopes are also respected. Pointwise,

\[
|b_n|\ll\log X.
\tag{21}
\]

On every interval of fixed polynomial length, (14) together with `q_X=o(1)` gives

\[
\sum_{n\in I}|b_n|\ll |I|,
\qquad
\sum_{n\in I}|b_n|^2\ll |I|\log X,
\tag{22}
\]

matching the currencies used in `ANF-162`--`ANF-163`. Finally, (5) and (13) yield

\[
\boxed{
\left|\sum_{n\in I}b_n\right|
\le a_X+L
=(1+o(1))a_X.
}
\tag{23}
\]

The control therefore does not exploit a missing global diagonal normalization, a nonzero total mean, an oversized coefficient, or an `L^1/L^2` mass violation. Its only non-source-faithful feature is the exact placement/sign law of the synthetic coefficients.

## 3. It satisfies stronger-than-any-log all-interval cancellation at the current activation scale

Now specialize to the regime where `ANF-165` applies,

\[
K=X^{1-2\varepsilon+o(1)},
\qquad
0<\varepsilon<\frac1{16}.
\tag{24}
\]

Choose fixed `eta>0` small enough that

\[
H_0:=X^{5/8+\eta}\ll R_{\rm TV}=(XK\log X)^{1/3};
\tag{25}
\]

as in `ANF-164`--`ANF-165`, any

\[
0<\eta<\frac{1-16\varepsilon}{24}
\]

is sufficient after absorbing the `o(1)` in `K`. Then (2) becomes

\[
\boxed{
q_X
=\sqrt{\frac\delta2}\,
X^{-1/8-\eta}\sqrt{\log X}.
}
\tag{26}
\]

This tends to zero by a fixed power. In particular, for every fixed `A>0`,

\[
q_X=o((\log X)^{-A}).
\tag{27}
\]

For every interval `I` with `|I|>=H_0`, equations (23) and (26) therefore give

\[
\boxed{
\left|\sum_{n\in I}b_n\right|
\ll |I|X^{-1/8-\eta}\sqrt{\log X}
=o_A\!\left(|I|(\log X)^{-A}\right)
}
\tag{28}
\]

for every fixed `A`. This is strictly stronger, as an abstract interval estimate, than the arbitrary-fixed-log saving supplied by the all-interval nilsequence theorem and transferred to the exact logarithmic twist in `ANF-165`.

Nevertheless (20) remains a positive fraction of the bow target. There is no contradiction with `ANF-165`. For every truncation length `R` with `H_0<=R<K`, the edge contribution below `R` is only

\[
E_{\partial,\,r\le R}(e)
\le 2Ra_X^2+O(H_0a_X^2)
\ll \delta XK\log X\,\frac{R}{K}.
\tag{29}
\]

Hence, if

\[
R=R_{\rm TV}(\log X)^C
\]

with fixed `C`, then `R/K ->0` by the power gap already computed in `ANF-165`, and (29) is `o(XK log X)`. The matched control reproduces exactly the phenomenon established there: every fixed polylogarithmic neighborhood of `R_TV` is harmless, while the same small absolute endpoint charge can persist through a polynomially longer set of prefix lengths and accumulate target-scale square energy only near the full `K` horizon.

## 4. The sharp interval currency is absolute anchoring, not arbitrary relative log saving

The construction isolates the information missing from a pure all-interval estimate. Suppose an argument knows only that

\[
\left|\sum_{n\in I}b_n\right|
\le \rho_X|I|
\qquad (|I|\ge H_0),
\tag{30}
\]

plus the aggregate mass and diagonal conditions above. The charge-and-hold control uses an endpoint value

\[
A_X:=\rho_XH_0
\]

and can keep a primitive of that order essentially unchanged over `Theta(K)` prefix lengths. Such a plateau contributes order

\[
KA_X^2
\]

to `E_partial`. Since the bow target is `XK log X`, a necessary information-scale condition for (30), by itself, to exclude target-size endpoint completion is therefore

\[
\boxed{
\rho_XH_0=o(\sqrt{X\log X}).
}
\tag{31}
\]

The cancellation factor must be judged at the **first controlled interval**, not by how many logarithms it saves relative to longer intervals. At the current activation length

\[
H_0=X^{5/8+\eta},
\]

condition (31) is

\[
\boxed{
\rho_X=o\!\left(X^{-1/8-\eta}\sqrt{\log X}\right).
}
\tag{32}
\]

Thus a generic estimate `rho_X=X^{-sigma}` safely crosses the barrier once `sigma>1/8+eta`; the exact borderline depends on its logarithmic factor and is already recorded by (31). Arbitrary fixed powers of `1/log X` are polynomially too weak.

There is a dual way to satisfy (31): lower the activation length. If one had arbitrary-log all-interval cancellation already for

\[
H_0\le \sqrt X\,(\log X)^B,
\]

then choosing the logarithmic saving exponent larger than `B+1/2` would make the right side of (30) at the first controlled scale `o(sqrt(X log X))`. This identifies the square-root physical length as the natural activation frontier for a log-saving-only strategy.

Equation (31) also reconnects to `ANF-158`. That finding showed that target-scale endpoint completion forces some prefix or suffix to reach absolute size `Omega(sqrt(X log X))`. The present matched control shows why that same absolute scale is not merely a consequence of a crude maximum argument: it is the **sharp anchor size that an interval-discrepancy architecture must beat** if it is to control the entire primitive square function.

## 5. What this does and does not rule out

The control `b` is deliberately synthetic. It is not asserted to equal

\[
r_X(n)n^{-iU}
=(\vartheta(n)-Q_X(n))n^{-iU}
\]

for any `X` or distinguished height. In particular, its sparse alternating bulk calibrator and constant edge ramps do not respect the exact prime locus, rough-number support, or Cramer--Granville amplitude law. Therefore (20) is **not a counterexample to the bow target** and does not show that the actual arithmetic endpoint completion is large.

What it proves is an information boundary. No proof whose source input is exhausted by the aggregate statements already extracted in `ANF-162`--`ANF-165`—pointwise size, local `L^1/L^2`, global diagonal normalization, exact total centering, and arbitrary fixed logarithmic bounds for all sufficiently long interval sums—can deduce `E_partial=o(XK log X)` without importing an additional property that excludes this control.

The useful surviving source-side options are consequently narrower:

1. prove an **absolute endpoint anchor** `|S_{H_0}^{\pm}|=o(sqrt(X log X))` and a return/mixing estimate preventing later recharging;
2. prove a direct cumulative-energy estimate for `sum_r|S_r^\pm|^2`, rather than bounding each interval increment separately;
3. push all-interval arbitrary-log control essentially to `sqrt X` scale;
4. exploit the exact prime-minus-rough placement/sign structure to show that a charge of size `sqrt(X log X)` cannot persist for a positive fraction of the `K` horizon.

A pointwise power saving is only one possible route, and (31) gives the exact amount it must buy at its activation scale.

## 6. Prior-art audit and novelty boundary

The load-bearing external theorem remains Kaisa Matomäki, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals I. All intervals*, Forum of Mathematics, Pi 11 (2023), e29, arXiv:2204.03754, already registered in `research/analytic_frontier/SOURCES.md`. `ANF-165` records exactly how its arbitrary-log nilsequence discorrelation is transferred to the globally fixed Cramer--Granville gauge and the distinguished logarithmic twist.

A fresh literature audit checked discrete Hardy/Copson inequalities and general discrepancy/partial-sum operator bounds. Those are the classical neighboring framework for controlling primitives from coefficient norms, but they do not supply the missing source-specific implication here: the unnormalized endpoint square function can retain a constant primitive plateau after the coefficient increment has vanished. The matched control above is proved directly and uses no external theorem beyond the already-cited arithmetic context. No new source anchor is therefore needed.

The finding should not be read as a novelty claim about Hardy operators. Its durable content is the **bow-normalized tariff** (31), together with a control that simultaneously matches the current arithmetic aggregate budgets and `ANF-165`'s stronger-than-any-fixed-log interval conclusion while retaining target-scale endpoint completion.

## Consequence for the research line

`ANF-165` correctly shows that current arithmetic discorrelation expels dangerous endpoint energy beyond every fixed polylogarithmic enlargement of the cubic total-variation scale. `ANF-166` identifies why that migration alone cannot converge to a proof: a small charge accumulated once can survive through the remaining polynomial horizon without violating any later interval bound.

The first unsupported endpoint implication is therefore no longer best phrased as “obtain some fixed-power improvement over `R_TV`.” The sharper gate is to control **absolute primitive memory**. At the existing `X^{5/8+eta}` activation scale, one must beat `sqrt(X log X)` absolutely—equivalently, gain about `X^{-1/8-eta}` relatively up to logarithmic factors—or establish a genuinely source-specific return/square-function law that makes persistent charge impossible. That is the smallest next theorem that would invalidate the matched control rather than merely move its energy farther toward `K`.