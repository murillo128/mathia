# AF-231 — power-decay targets shift the prime rate-distortion phase

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-FRAMEWORK-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `TARGET-RELATIVE`, `RATE-DISTORTION`, `EULER-ATOM`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-230 prices approximate localization of the prime source itself. A downstream task can be much cheaper when its observable contracts the prime tail. The precise first-order saving is determined by the decay of the target derivative.

Let

\[
\mathcal P_Q:=\{p\le Q:p\text{ prime}\},
\qquad
n_Q:=\pi(Q),
\tag{1}
\]

and let `P_Q` be uniform on `\mathcal P_Q`. Fix `a>0`, and let

\[
f:[2,\infty)\to\mathbb R
\tag{2}
\]

be strictly monotone and `C^1`, with constants `0<c_-\le c_+<\infty` such that

\[
c_-x^{-a-1}
\le
|f'(x)|
\le
c_+x^{-a-1}
\qquad(x\ge2).
\tag{3}
\]

For `\varepsilon>0` and `0\le\delta<1`, define the target-relative stochastic information price

\[
\mathcal R^{f}_Q(\varepsilon,\delta)
:=
\inf I(P_Q;M),
\tag{4}
\]

where the infimum is over arbitrary finite-valued stochastic marks `P_{M\mid P_Q}` and decoders `d` satisfying

\[
\Pr\{|f(P_Q)-d(M)|>\varepsilon\}\le\delta.
\tag{5}
\]

Because the distortion depends only on the deterministic target

\[
Y_Q:=f(P_Q),
\tag{6}
\]

this is exactly the ordinary single-letter rate-distortion problem for `Y_Q` with threshold distortion:

\[
\boxed{
\mathcal R^{f}_Q(\varepsilon,\delta)
=
\inf_{P_{\widehat Y\mid Y_Q}:\;
\Pr\{|Y_Q-\widehat Y|>\varepsilon\}\le\delta}
I(Y_Q;\widehat Y).
}
\tag{7}
\]

Now let `\varepsilon_Q>0` and `\delta_Q\to\delta\in[0,1)`, and put

\[
\gamma_Q
:=
\frac{\log^+(1/\varepsilon_Q)}{\log Q}.
\tag{8}
\]

If

\[
\gamma_Q\longrightarrow\gamma\in[0,\infty],
\tag{9}
\]

then

\[
\boxed{
\frac{\mathcal R^{f}_Q(\varepsilon_Q,\delta_Q)}
{\log\pi(Q)}
\longrightarrow
(1-\delta)\,
\min\!\left\{(\gamma-a)_+,1\right\}.
}
\tag{10}
\]

Thus a power-decaying target creates a **shifted information phase**. At polynomial absolute target accuracy `\varepsilon_Q=Q^{-\gamma+o(1)}`:

- if `\gamma\le a`, the target costs only `o(\log\pi(Q))` information;
- if `a<\gamma<a+1`, the normalized price is `(1-\delta)(\gamma-a)`;
- if `\gamma\ge a+1`, the target costs the full first-order source information `(1-\delta)\log\pi(Q)`.

The transition at `a+1` is the local-spacing scale induced by `|f'(Q)|\asymp Q^{-a-1}`. Exact target recovery still retains the whole prime identity because `f` is injective; the saving is purely an **approximate, target-metric** phenomenon.

A directly arithmetic specialization is the one-prime Euler-log atom

\[
e_a(x):=-\log(1-x^{-a}).
\tag{11}
\]

It satisfies

\[
|e_a'(x)|
=
\frac{a x^{-a-1}}{1-x^{-a}},
\tag{12}
\]

so `(3)` holds with

\[
c_-=a,
\qquad
c_+=\frac{a}{1-2^{-a}}.
\tag{13}
\]

Therefore `(10)` applies verbatim to reproducing `e_a(P_Q)` in absolute error. For `a>1`, `e_a(p)` is the prime summand in the absolutely convergent identity

\[
\log\zeta(a)=\sum_p e_a(p).
\tag{14}
\]

No use of `(14)` outside its convergence half-plane is made here.

## Derivation

### 1. The target problem is exactly functional rate-distortion

Given any admissible mark `M` and decoder `d`, set

\[
\widehat Y:=d(M).
\tag{15}
\]

Then

\[
P_Q\longrightarrow M\longrightarrow\widehat Y
\tag{16}
\]

and data processing gives

\[
I(Y_Q;\widehat Y)
\le
I(P_Q;M).
\tag{17}
\]

The distortion event in `(5)` depends only on `(Y_Q,\widehat Y)`, so the right-hand side of `(7)` is no larger than `(4)`.

Conversely, for any channel `P_{\widehat Y\mid Y_Q}` admissible in `(7)`, let the encoder compute `Y_Q=f(P_Q)` and use `M=\widehat Y`. Since `P_Q\to Y_Q\to\widehat Y` and `Y_Q` is a deterministic function of `P_Q`,

\[
I(P_Q;\widehat Y)=I(Y_Q;\widehat Y).
\tag{18}
\]

This proves `(7)`. The reduction is classical task-relative source coding; the new line-specific content is the prime-cutoff asymptotic induced by `(3)`.

### 2. Target occupancy gives the stochastic converse

Define the maximal target occupancy

\[
N^f_Q(t)
:=
\max_{y\in\mathbb R}
\#\{p\in\mathcal P_Q:f(p)\in[y,y+t]\}.
\tag{19}
\]

If two primes `p<q\le Q` lie in one target interval of length `t`, the mean-value theorem and the lower derivative bound in `(3)` give

\[
t
\ge
|f(p)-f(q)|
\ge
c_-Q^{-a-1}(q-p).
\tag{20}
\]

Hence every such fiber lies in an ordinary integer interval of length at most `tQ^{a+1}/c_-`, so

\[
\boxed{
N^f_Q(t)
\le
\min\!\left\{
 n_Q,
 1+\frac{tQ^{a+1}}{c_-}
\right\}.
}
\tag{21}
\]

The Fano/occupancy argument of AF-230 is target-agnostic. Applied to the finite source `Y_Q`, it gives

\[
\mathcal R^f_Q(\varepsilon,\delta)
\ge
\left[
(1-\delta)
\bigl(\log n_Q-\log N^f_Q(2\varepsilon)\bigr)
-\log2
\right]_+.
\tag{22}
\]

By the prime number theorem,

\[
\log n_Q
=
\log Q+o(\log Q).
\tag{23}
\]

Equations `(8)--(9)` and `(21)` imply

\[
\limsup_{Q\to\infty}
\frac{\log N^f_Q(2\varepsilon_Q)}{\log Q}
\le
\min\!\left\{
1,
(a+1-\gamma)_+
\right\}.
\tag{24}
\]

Substituting `(24)` into `(22)` yields

\[
\liminf_{Q\to\infty}
\frac{\mathcal R^f_Q(\varepsilon_Q,\delta_Q)}
{\log n_Q}
\ge
(1-\delta)
\min\!\left\{(\gamma-a)_+,1\right\}.
\tag{25}
\]

No local prime-counting theorem is needed: the occupancy upper bound uses only ordinary interval length, while PNT enters only through the total source entropy.

### 3. A tail-adapted quantizer gives the matching zero-error upper bound

First take `\delta=0`. For the nontrivial regime `\gamma<a+1`, choose

\[
\eta_Q:=\frac1{\log Q},
\qquad
A_Q:=\eta_QQ.
\tag{26}
\]

The prefix probability

\[
\alpha_Q
:=
\Pr\{P_Q<A_Q\}
=
\frac{\pi(A_Q)}{\pi(Q)}
\tag{27}
\]

satisfies

\[
\alpha_Q\to0
\tag{28}
\]

by PNT.

Encode every prefix prime `p<A_Q` exactly. On the tail `[A_Q,Q]`, partition the source coordinate into ordinary intervals of length at most

\[
L_Q
:=
\frac{\varepsilon_QA_Q^{a+1}}{c_+}.
\tag{29}
\]

When `\gamma<a+1`, `(8)--(9)` imply `L_Q\to\infty`. For two tail points in the same cell, the upper derivative bound in `(3)` gives

\[
|f(p)-f(q)|
\le
c_+A_Q^{-a-1}|p-q|
\le
\varepsilon_Q,
\tag{30}
\]

so one representative target value per cell gives zero-error reconstruction at tolerance `\varepsilon_Q`.

The number of tail cells obeys

\[
J_Q
\le
1+\frac{Q}{L_Q}
=
1+
\frac{c_+}{\varepsilon_QQ^a\eta_Q^{a+1}}.
\tag{31}
\]

Let `Z_Q` denote this deterministic zero-error mark, including a prefix/tail flag. Its entropy is bounded by

\[
H(Z_Q)
\le
h(\alpha_Q)
+
\alpha_Q\log\pi(A_Q)
+
(1-\alpha_Q)\log J_Q.
\tag{32}
\]

The first two terms are `o(\log n_Q)`, and `(31)` gives

\[
\limsup_{Q\to\infty}
\frac{H(Z_Q)}{\log n_Q}
\le
(\gamma-a)_+
\qquad(\gamma<a+1).
\tag{33}
\]

For `\gamma\ge a+1`, use the identity mark `Z_Q=P_Q`, which has entropy `\log n_Q`. Combining the two regimes,

\[
\limsup_{Q\to\infty}
\frac{H(Z_Q)}{\log n_Q}
\le
\min\!\left\{(\gamma-a)_+,1\right\}.
\tag{34}
\]

The construction makes the mechanism explicit: the quantizer is coarse on the contracted prime tail and spends exact labels only on a vanishing prefix where the target changes too quickly.

### 4. Independent erasure spends the allowed error budget exactly at first order

For general `\delta_Q`, let `B_Q` be independent of `P_Q` with

\[
\Pr(B_Q=0)=\delta_Q.
\tag{35}
\]

On `B_Q=1`, transmit the zero-error mark `Z_Q`; on `B_Q=0`, transmit a single erasure symbol. Decode the successful branch using the zero-error decoder and the erasure branch arbitrarily. The excess-error probability is at most `\delta_Q`, while

\[
I(P_Q;M_Q)
=
(1-\delta_Q)H(Z_Q).
\tag{36}
\]

Therefore `(34)` gives the matching upper bound

\[
\limsup_{Q\to\infty}
\frac{\mathcal R^f_Q(\varepsilon_Q,\delta_Q)}
{\log n_Q}
\le
(1-\delta)
\min\!\left\{(\gamma-a)_+,1\right\}.
\tag{37}
\]

Together with `(25)`, this proves `(10)`.

## Exact controls and boundaries

### The phase is target-relative, not a contradiction with full prime information

Because `f` is strictly monotone, the exact value `f(p)` determines `p`. Thus

\[
H(f(P_Q))=H(P_Q)=\log\pi(Q).
\tag{38}
\]

Equation `(10)` does not say the observable intrinsically contains less exact information. It says that the declared **absolute target metric** makes increasingly many large primes indistinguishable at finite tolerance because the map contracts them by `|f'(p)|\asymp p^{-a-1}`.

This is precisely the distinction suggested after AF-230: source identity and downstream task fidelity can have different information prices even when the target map is injective.

### Absolute target error is load bearing

The shift by `a` depends on measuring distortion in the ordinary absolute metric of `f(P_Q)`. A relative error, logarithmic target metric, inverse-coordinate error, or another target loss changes the induced fibers and can remove the contraction advantage.

For example, for `f(p)=p^{-a}`, infinitesimal relative target error satisfies

\[
\frac{|df|}{|f|}
\asymp
\frac{a\,dp}{p},
\tag{39}
\]

which measures a different source-scale geometry from absolute error. Therefore `(10)` is not a generic theorem that “Euler observables are cheap”; it is a theorem about one declared fidelity notion.

### A single-prime target is not the global Euler product

For `a>1`, `(14)` identifies `e_a(p)` as one term in the convergent Euler logarithm, but `(10)` prices reproduction of the random **individual prime contribution**. It does not control the accumulated error in

\[
\sum_{p\le Q}e_a(p),
\tag{40}
\]

let alone analytic continuation, the zero divisor, the explicit formula, or RH. Many individually small errors can add coherently. Any global application must declare and prove the corresponding aggregate distortion or sufficient statistic separately.

### The phase is not rational-prime-specific

The proof of `(10)` uses primality only through the global facts

\[
\log\pi(Q)\sim\log Q,
\qquad
\frac{\pi(Q/\log Q)}{\pi(Q)}\to0.
\tag{41}
\]

The same phase holds for the uniform integer control on `{2,\ldots,Q}`, and more generally for comparably large discrete sources with the same vanishing-prefix property. The derivative envelope, not unique prime arithmetic, determines the shift.

Thus `(10)` is a quantitative **fidelity control**, not a prime discriminator. A proposed RH mechanism cannot claim arithmetic specificity merely because a decaying target can be encoded cheaply at absolute tolerance.

### The converse is deliberately first order

The occupancy bound `(21)` ignores actual prime gaps, and the tail quantizer `(26)--(32)` is not asserted to be finite-`Q` optimal. They match only after normalization by `\log\pi(Q)`. Lower-order terms may depend on prime distribution, the exact target shape, and a more efficient stochastic test channel.

## Prior art and novelty assessment

Claude E. Shannon, **“Coding Theorems for a Discrete Source With a Fidelity Criterion,”** *IRE National Convention Record*, vol. 7 (1959), pp. 142--163, introduced rate-distortion theory as mutual-information minimization under a fidelity constraint. Equation `(7)` is an elementary deterministic-target specialization of that classical framework.

Sourya Basu, Daewon Seo, and Lav R. Varshney, **“Hypergraph-Based Source Codes for Function Computation Under Maximal Distortion,”** *IEEE Journal on Selected Areas in Information Theory* 3(4) (2022), 824--838, DOI `10.1109/JSAIT.2022.3232222`, study functional source coding with threshold/maximal distortion and place task-relative approximate function computation directly inside established rate-distortion theory.

Robert M. Gray and David L. Neuhoff, **“Quantization,”** *IEEE Transactions on Information Theory* 44(6) (1998), 2325--2383, DOI `10.1109/18.720541`, survey classical scalar/nonuniform/high-resolution quantization. The idea that a nonlinear target induces nonuniform useful resolution is therefore not a novelty claim here.

The Arithmetic Fidelity result is the exact prime-cutoff specialization `(10)`: for a target whose derivative decays like `x^{-a-1}`, the polynomial accuracy exponent is shifted by `a`, with a one-unit transition from sublogarithmic target information to full first-order source information. This derivation uses only elementary occupancy, a tail-adapted quantizer, PNT at global scale, and classical rate-distortion logic. No claim is made that the general phenomenon or quantization mechanism is new.

## Consequences for the research line

AF-230 closed randomization as a first-order escape when the task was source localization. AF-231 shows the correct next distinction: **changing the target can genuinely change the information exponent**. A downstream sufficient statistic whose sensitivity decays along the prime tail may be far cheaper to preserve than prime identity even when it is injective exactly.

This does not yet solve the line's arithmetic-discriminator problem. The power-decay phase is reproduced by matched non-prime controls and depends on the chosen target metric. The useful next question is therefore not whether a compressed representation preserves every prime label, but whether an RH-facing target admits a rigorously justified lower-information statistic whose fidelity metric is strong enough for the eventual analytic conclusion. Such a target-specific sufficiency theorem must be established before the reduced information price can count as progress toward RH.