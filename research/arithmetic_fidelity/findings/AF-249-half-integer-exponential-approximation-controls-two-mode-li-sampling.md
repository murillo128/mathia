# AF-249 — Half-integer exponential approximation exactly controls two-mode Li sampling

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `OUTPUT-SAMPLING`, `DIOPHANTINE-FIDELITY`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-248 shows that periodic completeness does not protect a Li-shaped conjugate two-mode signal from transcendental near-cancellation. In that two-mode setting the missing quantitative resource can be identified exactly.

Let `alpha` be irrational, let `m>=1`, and define

\[
F_{\alpha,m}(n)=-2m\cos(\pi n\alpha),
\qquad
 d_\alpha(n)=\operatorname{dist}\!\left(n\alpha,\mathbb Z+\frac12\right).
\tag{1}
\]

For an unbounded set `S subset N`, put

\[
\tau_\alpha(S)
:=\liminf_{\substack{n\to\infty\\ n\in S}}
\frac{-\log d_\alpha(n)}{n}.
\tag{2}
\]

Then

\[
\boxed{
\limsup_{\substack{n\to\infty\\ n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=e^{-\tau_\alpha(S)}.
}
\tag{3}
\]

Thus a retained set loses exponential root rate for this conjugate Li mode **if and only if** it is eventually trapped, along that retained subsequence, in exponentially shrinking neighborhoods of the half-integer phase-cancellation target.

There is also an exact criterion for immunity to *every* unbounded output sampling set. Define the half-integer exponential approximation exponent

\[
\kappa_{1/2}(\alpha)
:=\limsup_{n\to\infty}
\frac{-\log d_\alpha(n)}{n}.
\tag{4}
\]

Then

\[
\boxed{
\kappa_{1/2}(\alpha)=0
\iff
\text{every unbounded }S\subset\mathbb N
\text{ satisfies }
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}=1.
}
\tag{5}
\]

The standard irrationality base of Sondow gives a convenient source-side sufficient condition. If `beta(alpha)` denotes the irrationality base, then

\[
\boxed{
\kappa_{1/2}(\alpha)\le 2\log\beta(\alpha).
}
\tag{6}
\]

In particular,

\[
\beta(\alpha)=1
\quad\Longrightarrow\quad
\kappa_{1/2}(\alpha)=0,
\tag{7}
\]

so **every unbounded retained index set preserves the full root rate of the two-mode signal**. Finite irrationality exponent is sufficient because it implies irrationality base one, but it is not necessary: the irrationality-base condition also includes some Liouville numbers.

Conversely, if one unbounded `S` gives

\[
\theta_S
:=\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}<1,
\tag{8}
\]

then

\[
\beta(\alpha)\ge \theta_S^{-1/2}>1.
\tag{9}
\]

Therefore a root-rate failure for a single conjugate Li pair forces an exponentially well approximable phase in Sondow's sense. Mere transcendence, irrationality, or even Liouville status is not enough.

The specific AF-248 construction is much more exceptional still: its approximants satisfy a superexponential estimate of order `e^{-n_j^2}`, hence its `alpha` has irrationality base `+infinity` (a super-Liouville phase in Sondow's terminology). AF-248 therefore proves possibility, but not genericity, of the two-mode sampling obstruction.

## Why it matters

AF-248 left the output-side frontier at the statement that some genuinely quantitative Diophantine input is required. AF-249 identifies that input exactly for the simplest Li-compatible dominant mode and separates three very different regimes that were previously bundled together as “transcendental.”

At the root-rate scale, the relevant distinction is not algebraic versus transcendental. Algebraic phases are safe by AF-247, but the safe class is much larger: any irrational phase with irrationality base one is immune to adversarial sparse output sampling in the two-mode problem. A sampling failure requires exponential rational approximation, and the AF-248 counterexample uses the strongest possible version of that pathology.

This substantially narrows what a zeta-specific theorem would have to prove in the single-pair case. One would not need algebraicity of a zero-derived phase, nor ordinary lower bounds formulated as a finite irrationality exponent. It would be enough to rule out exponentially accurate rational approximation, i.e. to establish irrationality base one for the relevant normalized Keiper phase.

## Exact derivation

### 1. Cosine amplitude is globally equivalent to half-integer distance

For any real `x`, write

\[
d=\operatorname{dist}\!\left(x,\mathbb Z+\frac12\right)
\in[0,1/2].
\tag{10}
\]

By translating to the nearest half-integer,

\[
|\cos(\pi x)|=\sin(\pi d).
\tag{11}
\]

Concavity of `sin` on `[0,pi/2]` and the elementary upper bound `sin y<=y` give

\[
2d\le \sin(\pi d)\le \pi d.
\tag{12}
\]

Hence for every `n`, since irrationality of `alpha` makes `d_alpha(n)>0`,

\[
4m\,d_\alpha(n)
\le |F_{\alpha,m}(n)|
\le 2\pi m\,d_\alpha(n).
\tag{13}
\]

After taking logarithms and dividing by `n`, the fixed constants vanish. Therefore

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=
\exp\!\left(
-\liminf_{\substack{n\to\infty\\n\in S}}
\frac{-\log d_\alpha(n)}{n}
\right),
\tag{14}
\]

which is `(3)`. This is the two-mode specialization of AF-246 with an exact first-order zero geometry: the general Łojasiewicz exponent is exactly one here.

### 2. The all-sampling criterion is a limsup condition

The quantities

\[
a_n:=\frac{-\log d_\alpha(n)}{n}
\tag{15}
\]

are nonnegative. If `kappa_{1/2}(alpha)=limsup a_n=0`, then `a_n->0`; hence every unbounded subsequence has `liminf a_n=0`, and `(3)` gives root rate one.

Conversely, if `kappa_{1/2}(alpha)>0`, choose any

\[
0<c<\kappa_{1/2}(\alpha).
\tag{16}
\]

There are infinitely many indices with `a_n>c`. Taking those indices as `S` gives

\[
\tau_\alpha(S)\ge c,
\qquad
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
\le e^{-c}<1.
\tag{17}
\]

This proves `(5)`. Notice the quantifier distinction from AF-246: for one fixed `S` the relevant quantity is a `liminf`; immunity against **all** unbounded `S` is governed by the ambient `limsup` in `(4)`.

### 3. Sondow irrationality base dominates the dangerous exponent

Use Sondow's definition: `beta(alpha)` is the least `beta>=1` such that, for every `epsilon>0`, all sufficiently large denominators `q` satisfy

\[
\left|\alpha-\frac pq\right|
>(\beta+\varepsilon)^{-q}
\quad\text{for every integer }p.
\tag{18}
\]

For each `n`, let `p_n` be an odd integer nearest to `2n alpha`. Then

\[
\left|\alpha-\frac{p_n}{2n}\right|
=\frac{d_\alpha(n)}{n}.
\tag{19}
\]

Applying `(18)` to `q=2n` yields eventually

\[
d_\alpha(n)
>n(\beta+\varepsilon)^{-2n}.
\tag{20}
\]

Consequently

\[
\limsup_{n\to\infty}
\frac{-\log d_\alpha(n)}{n}
\le 2\log(\beta+\varepsilon).
\tag{21}
\]

Letting `epsilon downarrow 0` proves `(6)`. In particular, `beta(alpha)=1` forces `(7)`.

If `(8)` holds, `(3)` gives

\[
\tau_\alpha(S)=-\log\theta_S>0.
\tag{22}
\]

The global limsup in `(4)` is at least this subsequential liminf, so `(6)` implies

\[
2\log\beta(\alpha)
\ge \kappa_{1/2}(\alpha)
\ge -\log\theta_S,
\tag{23}
\]

which is `(9)`.

Equation `(6)` is intentionally one-sided. The irrationality base permits arbitrary rational denominators and numerators, whereas cosine cancellation sees only the parity-restricted approximants `p/(2n)` with `p` odd. Thus `beta(alpha)>1` need not by itself produce a bad cosine-sampling subsequence. The exact invariant for this mode is `kappa_{1/2}` rather than the unrestricted irrationality base.

### 4. Consequence for one dominant conjugate Keiper--Li pair

Suppose an off-RH Li asymptotic has one conjugate innermost pole pair, of common multiplicity `m`, so that AF-244's decomposition reduces to

\[
\lambda_n=q^nF_{\alpha,m}(n)+r_n,
\qquad q>1,
\qquad
\limsup_{n\to\infty}|r_n|^{1/n}<q.
\tag{24}
\]

If `beta(alpha)=1`, then `(7)` and `(5)` imply for **every** unbounded `S subset N`

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}=1.
\tag{25}
\]

The separated remainder in `(24)` then gives, exactly as in AF-246,

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}
|\lambda_n|^{1/n}=q>1.
}
\tag{26}
\]

Thus in this single-pair regime the output set needs no density, thickness, periodic completeness, or recurrence hypothesis at all once the source phase has irrationality base one. Arbitrarily sparse unbounded output sampling remains root-rate faithful.

This is a conditional statement about the geometry of a possible off-RH dominant pair, not a theorem that the actual Riemann zeros satisfy the required Diophantine property.

## AF-248 reclassification

The construction in AF-248 has, along its selected indices,

\[
d_\alpha(n_j)\le \frac1{16}e^{-n_j^2}.
\tag{27}
\]

Hence

\[
\left|\alpha-\frac{p_j}{2n_j}\right|
\le \frac{e^{-n_j^2}}{16n_j}.
\tag{28}
\]

For every fixed `B>1`, the right-hand side is eventually smaller than `B^{-2n_j}`. Therefore no finite irrationality base can satisfy Sondow's eventual lower bound, and

\[
\boxed{\beta(\alpha)=+\infty.}
\tag{29}
\]

So the explicit periodically complete failure from AF-248 lives in the super-Liouville regime. This does not remove the obstruction: AF-248 remains a valid matched control against arguments that use only elementary Li symmetries. It does show that the control is Diophantinely extreme and identifies a much weaker sufficient source theorem that would exclude it.

## Prior-art audit

Jonathan Sondow, **“Irrationality Measures, Irrationality Bases, and a Theorem of Jarnik,”** arXiv:`math/0406300` (2004), develops the irrationality base as the exponential-scale analogue of the usual irrationality exponent and gives continued-fraction formulas, bounds, and examples with prescribed irrationality base. The irrationality-base notion and its distinction among Liouville numbers are classical prior art; no novelty is claimed for them.

The Keiper--Li conformal map and off-RH exponentially oscillatory asymptotics are classical and were already audited in AF-244/AF-248, in particular against André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`.

A targeted search for combinations of Keiper--Li coefficients, normalized zero phases, irrationality base, exponential rational approximation, and shrinking-target sampling did not locate a standard statement matching `(3)`--`(9)` or the all-unbounded-sampling consequence `(26)`. This is not an exhaustive novelty proof. The derived contribution is the narrow synthesis: in the single conjugate Li-mode case, the root-rate sampling obstruction is exactly a parity-restricted exponential Diophantine approximation problem, and Sondow irrationality base one is a sufficient source property eliminating the obstruction for every unbounded output set.

## Boundaries

**Single conjugate mode only.** Equations `(1)`--`(9)` classify a two-mode cosine arising from one conjugate dominant pair. If several distinct conjugate pairs share the innermost Keiper modulus, cancellation occurs in a higher-dimensional trigonometric polynomial. Coordinatewise irrationality-base-one statements need not control simultaneous approach to that polynomial's zero set. AF-246's finite-torus shrinking-target formulation remains the correct general object there.

**Irrational phase assumed.** Rational `alpha` can produce exact periodic zeros, returning to the aliasing phenomena isolated by AF-245--AF-247. The present theorem isolates near-cancellation rather than exact periodic cancellation.

**Irrationality base one is sufficient, not exact.** The exact all-sampling invariant is `kappa_{1/2}`. Because the dangerous approximants have forced denominator parity and odd numerator, an irrational number may have `beta(alpha)>1` while still having `kappa_{1/2}(alpha)=0`.

**No theorem about Riemann-zero irrationality.** Nothing here proves that an actual normalized Keiper phase is irrational, non-Liouville, of finite irrationality exponent, or of irrationality base one. Those are precisely source-side inputs still missing.

**Output sampling remains separate from source access.** Even if every unbounded set preserves the already-formed Li root rate, computing a selected large `lambda_n` can still require the cancellation-coherent source depth isolated by AF-238--AF-243.

## Research consequence

For a hypothetical off-RH configuration with a single dominant conjugate pair, the output-sampling question is now reduced to a precise Diophantine target. The strongest useful source statement is not “the phase is algebraic.” A substantially weaker theorem, `beta(alpha)=1`, would already make **all unbounded output samplings root-rate faithful**.

The remaining genuinely harder direction is the multi-pair case. There the analogue of `(4)` should be formulated for the actual finite trigonometric polynomial generated by all co-dominant Keiper phases, and the source-side goal becomes a simultaneous/linear-form lower bound excluding exponential approach to its zero locus. Any such theorem must be proved from properties genuinely forced by zeta zeros rather than assumed from generic phase behavior.