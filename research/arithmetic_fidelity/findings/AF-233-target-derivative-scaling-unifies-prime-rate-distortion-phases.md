# AF-233 — target-derivative scaling unifies the prime rate-distortion phases

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-FRAMEWORK-SPECIALIZATION`, `QUANTITATIVE-FIDELITY`, `TARGET-METRIC`, `RATE-DISTORTION`, `PHASE-LAW`, `NO-NOVELTY-CLAIM`

## Claim

AF-230, AF-231, and AF-232 exhibit three apparently different first-order information phases: direct prime-tail localization, absolute reproduction of a power-decaying target, and scale-normalized reproduction of the same target. They are instances of one target-geometry law.

Let

\[
\mathcal P_Q:=\{p\le Q:p\text{ prime}\},
\qquad n_Q:=\pi(Q),
\]

and let `P_Q` be uniform on `\mathcal P_Q`. Let

\[
f:[2,\infty)\to\mathbb R
\]

be strictly monotone and `C^1`. Assume that `f'` is nonzero for all sufficiently large `x` and that the logarithmic derivative-growth exponent

\[
\boxed{
\rho
:=
1+\lim_{x\to\infty}
\frac{\log|f'(x)|}{\log x}
\in\mathbb R
}
\tag{1}
\]

exists. Equivalently, for every `\eta>0` and all sufficiently large `x`,

\[
x^{\rho-1-\eta}
\le |f'(x)|
\le x^{\rho-1+\eta}.
\tag{2}
\]

For `r>0` and `0\le\delta<1`, define

\[
\mathcal R_Q^f(r,\delta)
:=
\inf I(P_Q;M),
\tag{3}
\]

where the infimum is over finite-valued stochastic marks and decoders `d` satisfying

\[
\Pr\{|f(P_Q)-d(M)|>r\}\le\delta.
\tag{4}
\]

Let `\delta_Q\to\delta\in[0,1)` and let `r_Q>0` obey

\[
\frac{\log(1/r_Q)}{\log Q}
\longrightarrow
\beta\in[0,\infty].
\tag{5}
\]

Thus `\beta=0` includes constant and subpolynomially varying target resolution, while `\beta>0` means polynomially shrinking resolution. Define

\[
[x]_0^1:=\min\{1,\max\{0,x\}\}.
\tag{6}
\]

Then

\[
\boxed{
\frac{\mathcal R_Q^f(r_Q,\delta_Q)}{\log\pi(Q)}
\longrightarrow
(1-\delta)[\rho+\beta]_0^1.
}
\tag{7}
\]

The single exponent `\rho` therefore measures the first-order cost induced by the **absolute target metric**:

- `\rho<0`: the target contracts the prime tail strongly enough to create a free-resolution region `\beta\le-\rho`;
- `\rho=0`: target resolution and multiplicative source resolution have the same polynomial information phase;
- `0<\rho<1`: even constant target accuracy costs a positive fraction `\rho` of prime identity, and shrinking accuracy adds linearly until saturation;
- `\rho\ge1`: every non-polynomially-growing absolute tolerance in `(5)` already costs the full first-order prime information.

This gives an exact phase calculus for the recent examples. In particular:

1. `f(x)=-\log\log x` has `|f'(x)|=1/(x\log x)`, hence `\rho=0`; `(7)` recovers AF-230's unshifted phase.
2. The Euler-log atom
   \[
   e_a(x):=-\log(1-x^{-a})
   \]
   has `|e_a'(x)|=x^{-a-1+o(1)}`, hence `\rho=-a`; `(7)` recovers AF-231's shifted phase `(1-\delta)\min\{(\beta-a)_+,1\}`.
3. `g_a(x):=\log e_a(x)` has `|g_a'(x)|=x^{-1+o(1)}`, hence `\rho=0`; `(7)` recovers the logarithmic/relative-metric phase behind AF-232.

Thus AF-231's damping advantage and AF-232's reset are not separate Euler phenomena. They are consequences of changing the polynomial scaling of target distance.

## Derivation

### 1. The mark problem is ordinary target rate-distortion

Because `f` is strictly monotone, the finite target source

\[
Y_Q:=f(P_Q)
\tag{8}
\]

is in bijection with `P_Q`. As in AF-231, every admissible mark/decoder gives a reproduction `\widehat Y=d(M)` and data processing gives

\[
I(Y_Q;\widehat Y)\le I(P_Q;M).
\tag{9}
\]

Conversely, a reproduction channel for `Y_Q` can be used directly as the mark because the encoder can compute `Y_Q` from `P_Q`; bijectivity gives

\[
I(P_Q;\widehat Y)=I(Y_Q;\widehat Y).
\tag{10}
\]

Hence `(3)` is exactly the single-letter Shannon rate-distortion problem for the finite source `Y_Q` with threshold distortion `\mathbf 1_{|Y_Q-\widehat Y|>r}`. The remaining work is to compute its first-order geometry as `Q` moves.

### 2. The derivative exponent controls target-ball occupancy

Let

\[
N_Q^f(t)
:=
\max_{y\in\mathbb R}
\#\{p\in\mathcal P_Q:f(p)\in[y,y+t]\}.
\tag{11}
\]

AF-230's Fano/occupancy argument is target-agnostic and gives

\[
\mathcal R_Q^f(r,\delta)
\ge
\left[
(1-\delta)
\bigl(\log n_Q-\log N_Q^f(2r)\bigr)
-\log2
\right]_+.
\tag{12}
\]

Fix `\eta>0`. The asymptotic definition `(1)` gives a threshold `X_\eta` beyond which `(2)` holds. The finitely many primes below `X_\eta` affect `N_Q^f` by only an additive constant.

If `\rho<1`, choose `\eta<1-\rho`. For primes `X_\eta\le p<q\le Q`, the mean-value theorem and the lower bound in `(2)` give

\[
|f(q)-f(p)|
\ge
Q^{\rho-1-\eta}(q-p).
\tag{13}
\]

Therefore a target interval of length `t` contains, apart from the fixed prefix, primes lying in an ordinary source interval of length at most

\[
tQ^{1-\rho+\eta}.
\tag{14}
\]

If `\rho=1`, the same argument with the lower estimate `|f'(x)|\ge x^{-\eta}` gives an interval length at most `tQ^\eta`. If `\rho>1`, choose `\eta<\rho-1`; then `|f'|` is eventually bounded below by a positive constant, so the source interval has length `O_\eta(t)`.

Combining the three cases, using the cap `N_Q^f(t)\le n_Q`, and then letting `\eta\downarrow0`, `(5)` yields

\[
\limsup_{Q\to\infty}
\frac{\log N_Q^f(2r_Q)}{\log Q}
\le
\min\{1,(1-\rho-\beta)_+\}.
\tag{15}
\]

The prime number theorem gives

\[
\log n_Q=\log Q+o(\log Q).
\tag{16}
\]

Substituting `(15)` into `(12)` gives

\[
\liminf_{Q\to\infty}
\frac{\mathcal R_Q^f(r_Q,\delta_Q)}{\log n_Q}
\ge
(1-\delta)[\rho+\beta]_0^1.
\tag{17}
\]

No local prime-counting estimate is needed. The converse uses only target-ball diameter, ordinary integer spacing, and the global source entropy scale.

### 3. A vanishing-prefix quantizer attains the same exponent

Write

\[
s:=[\rho+\beta]_0^1.
\tag{18}
\]

If `s=1`, use the exact identity mark `P_Q`; it has entropy `\log n_Q`, so after the erasure step below it already gives the required upper bound.

Assume `s<1`. Then necessarily `\rho<1`. Put

\[
A_Q:=\frac{Q}{\log Q},
\qquad
\alpha_Q:=\Pr\{P_Q<A_Q\}
=
\frac{\pi(A_Q)}{\pi(Q)}.
\tag{19}
\]

By PNT,

\[
\alpha_Q\to0,
\qquad
\alpha_Q\log\pi(A_Q)=o(\log n_Q).
\tag{20}
\]

Fix `\eta>0` small enough that `\rho-1+\eta<0`. For large `Q`, `(2)` implies on `[A_Q,Q]`

\[
|f'(x)|
\le
A_Q^{\rho-1+\eta}.
\tag{21}
\]

Encode every prefix prime below `A_Q` exactly. Partition the tail source coordinate into intervals of length at most

\[
L_Q
:=
r_Q A_Q^{1-\rho-\eta}.
\tag{22}
\]

Two tail primes in one cell then satisfy

\[
|f(p)-f(q)|
\le
A_Q^{\rho-1+\eta}|p-q|
\le r_Q,
\tag{23}
\]

so one representative target value per cell gives zero-error reproduction at radius `r_Q`.

The number of tail cells satisfies

\[
J_Q
\le
1+\frac{Q}{L_Q}
=
1+
\frac{Q A_Q^{\rho-1+\eta}}{r_Q}.
\tag{24}
\]

Using `A_Q=Q/\log Q` and `(5)`,

\[
\limsup_{Q\to\infty}
\frac{\log J_Q}{\log Q}
\le
(\rho+\beta+\eta)_+.
\tag{25}
\]

If `Z_Q` is the resulting deterministic zero-error mark, its entropy is bounded by

\[
H(Z_Q)
\le
h(\alpha_Q)
+
\alpha_Q\log\pi(A_Q)
+
(1-\alpha_Q)\log J_Q.
\tag{26}
\]

Equations `(20)` and `(25)`, followed by `\eta\downarrow0`, give

\[
\limsup_{Q\to\infty}
\frac{H(Z_Q)}{\log n_Q}
\le
(\rho+\beta)_+
=s
\qquad(s<1).
\tag{27}
\]

Together with the identity construction when `s=1`, this proves a zero-error upper coefficient `s` for every regime in `(5)`.

### 4. Independent erasure spends the allowed failure budget

Let `B_Q` be independent of `P_Q` with

\[
\Pr(B_Q=0)=\delta_Q.
\tag{28}
\]

On `B_Q=1`, transmit `Z_Q`; on `B_Q=0`, transmit one erasure symbol. The distortion failure probability is at most `\delta_Q`, while

\[
I(P_Q;M_Q)
=(1-\delta_Q)H(Z_Q).
\tag{29}
\]

Therefore

\[
\limsup_{Q\to\infty}
\frac{\mathcal R_Q^f(r_Q,\delta_Q)}{\log n_Q}
\le
(1-\delta)s.
\tag{30}
\]

Together with `(17)`, this proves `(7)`.

## Structural interpretation

### `rho` is a target-metric exponent, not intrinsic information content

Exact `f(P_Q)` always determines `P_Q`, so

\[
H(f(P_Q))=H(P_Q)=\log\pi(Q).
\tag{31}
\]

The exponent `\rho` measures how an **absolute target tolerance** pulls back to source-scale uncertainty. Near the prime tail, a target ball of radius `Q^{-\beta}` corresponds at polynomial scale to a source interval of size

\[
Q^{1-\rho-\beta+o(1)}.
\tag{32}
\]

The normalized information price is exactly the complementary exponent left after this ambiguity, clipped between zero and the full source entropy. This is why three injective coordinates can have different approximate-compression costs without differing at all in exact recoverability.

### Bounded-distortion reparameterizations preserve the phase; singular companders can shift it

Suppose `\phi` is a monotone `C^1` postcomposition whose derivative along the relevant target tail is bounded above and below by positive constants. Then

\[
|(\phi\circ f)'(x)|\asymp|f'(x)|,
\]

so `\phi\circ f` has the same exponent `\rho` and therefore the same first-order phase `(7)`.

By contrast, a postcomposition whose derivative itself grows or decays polynomially along `f(x)` changes the exponent by the chain rule and can shift the phase. AF-232's logarithm is exactly such a non-bi-Lipschitz metric change on a target tending to zero: it converts the Euler atom's exponent `\rho=-a` into `\rho=0`.

Thus the first-order rate phase is stable under uniformly comparable target metrics, but not under arbitrary coordinate changes. The metric category must be declared before an information saving can be interpreted.

## Exact controls and boundaries

### The theorem is not rational-prime-specific

Primality enters through

\[
\log\pi(Q)=\log Q+o(\log Q)
\]

and the vanishing mass of the prefix `p<Q/\log Q`. The occupancy converse itself uses only ordinary integer spacing. Uniform integers, and broader discrete sources with comparable cardinality and a negligible prefix, obey the same exponent law.

Therefore `\rho` is a fidelity resource, not a rational-prime discriminator. Matching this phase with a non-prime control is expected, not a failure of the derivation.

### The derivative exponent is an asymptotic gate, not a universal local model

If `\log|f'(x)|/\log x` has no limit, if `f'` has arbitrarily deep tail zeros, or if different subsequences have genuinely different polynomial scalings, `(7)` need not hold with one number `\rho`. In that case upper and lower derivative exponents should be retained separately; replacing them by a convenient average can manufacture a false phase.

### The theorem is first-order only

Equation `(7)` identifies the coefficient of `\log\pi(Q)`. It does not optimize finite-`Q` channels, additive constants, or lower-order terms. Prime gaps, slowly varying factors such as powers of `\log Q`, and target curvature are deliberately invisible at this normalization.

This invisibility is useful as a control: a proposed arithmetic effect living only in a slowly varying correction cannot be inferred from the polynomial phase coefficient.

### Polynomially growing tolerances are outside the stated scale

Condition `(5)` requires a nonnegative resolution exponent. It permits constant or subpolynomially varying tolerances at `\beta=0`, but not `r_Q=Q^c` with fixed `c>0`. For growing targets (`\rho>0`), polynomially growing distortion can introduce additional global-range geometry not captured by simply allowing negative `\beta` in `(7)`. No such extension is claimed.

### A one-prime target is still not a global arithmetic sufficient statistic

As in AF-231 and AF-232, the theorem prices reproduction of one random prime target value. It does not price a whole Euler product, a coherent signed prime sum, an explicit-formula functional, analytic continuation, or the zero divisor. Aggregation can couple many individually cheap coordinates and change the information geometry completely.

A future RH-facing use therefore needs an independently justified target or sufficient statistic first. Equation `(7)` can then price that target only after its own distortion geometry has been derived.

## Prior art and novelty assessment

The underlying information-theory mechanism is classical. No novelty is claimed for rate-distortion theory, high-resolution quantization, companding, or the general principle that a smooth target's local sensitivity changes quantization cost.

- Robert M. Gray and David L. Neuhoff, **“Quantization,”** *IEEE Transactions on Information Theory* 44(6), 2325–2383 (1998), DOI `10.1109/18.720541`, survey the classical high-resolution and companding theory in which local coordinate scaling controls quantizer geometry.
- Tamás Linder and Ram Zamir, **“High-Resolution Source Coding for Non-Difference Distortion Measures: The Rate-Distortion Function,”** *IEEE Transactions on Information Theory* 45(2), 533–547 (1999), DOI `10.1109/18.749001`, give asymptotically tight rate-distortion formulas for source-dependent local distortion geometries. This is direct prior art for treating the declared target metric, rather than target values alone, as load bearing.
- Vinith Misra, Vivek K. Goyal, and Lav R. Varshney, **“Distributed Scalar Quantization for Computing: High-Resolution Analysis and Extensions,”** *IEEE Transactions on Information Theory* 57(8), 5298–5325 (2011), DOI `10.1109/TIT.2011.2158882`, develop functional scalar quantization in which the sensitivity of the downstream function determines optimal high-resolution allocation.
- Tsutomu Kawabata and Amir Dembo, **“The Rate-Distortion Dimension of Sets and Measures,”** *IEEE Transactions on Information Theory* 40(5), 1564–1572 (1994), DOI `10.1109/18.333868`, provides the classical bridge between fine-scale geometric dimension and rate-distortion asymptotics.

The present theorem is a discrete moving-source specialization with an elementary occupancy converse and tail quantizer. Its Arithmetic Fidelity value is organizational rather than a claim of a new information-theory principle: **AF-230 through AF-232 collapse to one polynomial target-metric exponent, and apparent compression gains are meaningful only modulo the metric class that preserves that exponent.**

## Research consequence

The recent prime-tail rate-distortion branch no longer needs separate heuristics for source localization, decaying observables, and relative target error. At first order they are governed by the same rule `(7)`. This sharpens the current frontier in two ways.

First, merely finding a downstream prime observable with small amplitude or slowly varying values is not evidence of cheap arithmetic fidelity. Its declared target metric fixes `\rho`, and a singular reparameterization can create or erase the apparent saving without changing exact information at all.

Second, the next genuinely new object should not be another one-dimensional injective prime coordinate with a different derivative scale. Such examples are now covered by `(7)` whenever they have a stable polynomial derivative exponent. Progress requires a **target-specific sufficient statistic or relational/global target** whose compression fibers are justified by the arithmetic task itself. Only then can its information price test whether a nontrivial fraction of prime identity is genuinely unnecessary rather than merely hidden by target-coordinate contraction.