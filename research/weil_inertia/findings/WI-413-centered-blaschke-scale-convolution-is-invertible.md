# WI-413 — centered Blaschke scale convolution is invertible, so an exact count quantum uniquely forces Haar mixing

**Status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-412](./WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md).

## Claim

WI-412 showed that the canonical Haar mixture of centered Burnol--Kunik horizontal scales produces a depth-independent zero-side quantum, but only at infinite logarithmic-scale budget and with a nonintegrable height tail. It deliberately left open a `distributional scale combination` loophole: perhaps a signed distribution on scale, rather than a finite measure or Haar itself, could produce the same exact all-depth quantum while avoiding that conclusion.

Within the natural tempered-distribution completion of the centered log-scale problem, that loophole is absent. Put

\[
K(t):=\log\coth\frac{|t|}{2},
\qquad t\in\mathbb R\setminus\{0\},
\tag{1}
\]

with the locally integrable logarithmic singularity at `t=0`, and use the Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-i\xi t}\,dt,
\qquad
f(t)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\xi)e^{i\xi t}\,d\xi.
\tag{2}
\]

Then

\[
\boxed{
\widehat K(\xi)=\frac{\pi}{\xi}\tanh\frac{\pi\xi}{2}
}
\tag{3}
\]

for `xi != 0`, with the removable value

\[
\boxed{\widehat K(0)=\frac{\pi^2}{2}.}
\tag{4}
\]

The multiplier in (3) is smooth and strictly positive on the real axis. Both `\widehat K` and `1/\widehat K` are Schwartz multipliers: all derivatives have at most polynomial growth. Consequently the operator

\[
T_K\mu:=\mathcal F^{-1}(\widehat K\,\widehat\mu)
\tag{5}
\]

is an automorphism of `S'(R)`. In particular it has no tempered-distribution nullspace.

Therefore, if a tempered log-scale distribution `mu` produces the exact constant centered response

\[
T_K\mu\equiv q
\tag{6}
\]

at every log-depth, then necessarily

\[
\boxed{
\mu(ds)=\frac{2q}{\pi^2}\,ds.
}
\tag{7}
\]

Equivalently, in the original positive scale variable `a=e^s`,

\[
\boxed{
\mu(da)=\frac{2q}{\pi^2}\frac{da}{a}.
}
\tag{8}
\]

Thus normalized Haar scale mixing is not merely one convenient way to create an exact all-depth count quantum: it is the **unique tempered linear scale distribution** that does so in the centered Blaschke architecture. Combined with WI-412, an exact count quantum therefore uniquely forces the same infinite scale budget and `1/|height|` tail already exhibited there.

This closes the specific distributional-scale escape left open by WI-412. It does **not** exclude approximate constant response, a merely coercive lower bound, a bounded interval of depths, ordinate-dependent or nontranslation-invariant scale architectures, nonlinear observables, genuinely nontempered/renormalized objects, or new arithmetic information that quantizes horizontal displacement independently.

## 1. Exact Fourier multiplier

For `t != 0`,

\[
\begin{aligned}
K(t)
&=\log\frac{1+e^{-|t|}}{1-e^{-|t|}}\\
&=2\sum_{n\ge0}\frac{e^{-(2n+1)|t|}}{2n+1}.
\end{aligned}
\tag{9}
\]

The series is nonnegative and its `L^1` norms are summable:

\[
\sum_{n\ge0}
\left\|2\frac{e^{-(2n+1)|t|}}{2n+1}\right\|_1
=4\sum_{n\ge0}\frac1{(2n+1)^2}
=\frac{\pi^2}{2}.
\tag{10}
\]

Hence termwise Fourier transformation is justified in `L^1`. Since for `a>0`

\[
\int_{\mathbb R}e^{-a|t|}e^{-i\xi t}\,dt
=\frac{2a}{a^2+\xi^2},
\tag{11}
\]

we obtain

\[
\widehat K(\xi)
=4\sum_{n\ge0}
\frac1{(2n+1)^2+\xi^2}.
\tag{12}
\]

Use the classical partial-fraction identity

\[
\sum_{n\in\mathbb Z}\frac1{n^2+\xi^2}
=\frac{\pi}{\xi}\coth(\pi\xi).
\tag{13}
\]

Subtracting the even integers and halving the remaining symmetric sum gives

\[
4\sum_{n\ge0}\frac1{(2n+1)^2+\xi^2}
=rac{2\pi}{\xi}\coth(\pi\xi)
-\frac{\pi}{\xi}\coth\frac{\pi\xi}{2}.
\tag{14}
\]

The elementary identity

\[
2\coth(2x)-\coth x=\tanh x
\tag{15}
\]

turns (14) into (3). Letting `xi -> 0` gives (4), consistently with `||K||_1=pi^2/2` from WI-412.

In particular,

\[
\widehat K(\xi)>0
\qquad(\xi\in\mathbb R).
\tag{16}
\]

Near zero the quotient in (3) is an even analytic function with nonzero value `pi^2/2`. At infinity,

\[
\widehat K(\xi)\sim\frac{\pi}{|\xi|},
\qquad
\frac1{\widehat K(\xi)}\sim\frac{|\xi|}{\pi}.
\tag{17}
\]

Differentiating the exact hyperbolic expression shows that every derivative of either function has at most polynomial growth. Hence both are multipliers of the Schwartz space, and multiplication by `\widehat K` is invertible on tempered distributions with inverse multiplication by `1/\widehat K`. This proves the automorphism statement in (5) without invoking a pointwise convolution for arbitrary distributions.

## 2. Constant response has a unique tempered preimage

Suppose (6) holds in `S'(R)`. With convention (2),

\[
\widehat q=2\pi q\,\delta_0.
\tag{18}
\]

Applying the inverse multiplier gives

\[
\widehat\mu
=\frac{2\pi q}{\widehat K(0)}\delta_0
=\frac{4q}{\pi}\delta_0.
\tag{19}
\]

But the Fourier transform of the constant density `c` is `2pi c delta_0`; therefore

\[
c=\frac{2q}{\pi^2},
\tag{20}
\]

which proves (7). Since `ds=da/a`, equation (8) follows immediately.

For the unit quantum `q=1`, the unique tempered solution is therefore

\[
\boxed{
\mu(da)=\frac{2}{\pi^2}\frac{da}{a}.
}
\tag{21}
\]

There is no possibility of adding a hidden tempered distribution `nu` with `K*nu=0`: in the multiplier formulation this would require `\widehat K\widehat\nu=0`, and strict nonvanishing plus the slowly increasing reciprocal force `nu=0`.

## 3. What this adds to WI-412

WI-412 proved two facts about Haar mixing itself. First, a finite signed or complex scale measure whose centered response stays uniformly positive over a logarithmic depth interval must pay total variation at least linearly in the interval length. Second, the Haar limit that makes the centered response exactly constant has infinite scale mass and produces a nonintegrable `1/|gamma-b|` height tail.

Those statements alone did not exclude a more singular distributional scale combination. Equations (3)--(21) now show that the complete centered response profile determines every tempered log-scale distribution uniquely. Exact constancy has only one preimage, namely Haar. Thus singular signed derivatives, oscillatory tempered distributions, and other tempered generalized functions cannot cancel their way around the WI-412 budget while preserving an **exact** constant response at every depth.

The obstruction is sharp but deliberately narrow. It is an injectivity theorem for the one-dimensional centered, translation-in-log-scale linear response operator. It gives no quantitative stability estimate for approximate constancy and no lower bound for a response that is merely positive rather than exactly flat. Those remain genuinely different questions.

## 4. Prior-art and novelty audit

The ingredients are classical. The expansion of `log coth`, the Fourier transform of `exp(-a|t|)`, and the Mittag--Leffler/partial-fraction expansion of `coth` are standard Fourier/complex-analysis identities. The general principle that a nonvanishing Fourier multiplier with a slowly increasing reciprocal is invertible on tempered distributions is standard distribution theory. A targeted search around `log coth` Fourier transforms, half-integer reciprocal-square sums, Wiener--Tauberian convolution criteria, and Mellin/log-scale convolution found standard versions of these tools but no inspected source stating the present Blaschke-scale closure in this research-line language. No priority claim is made for the transform identity (3), its nonvanishing, or the resulting uniqueness statement.

The zeta-specific provenance remains exactly that of WI-412: Kunik's half-plane Poisson--Schwarz/Blaschke factorization and Burnol's quantitative half-plane Blaschke/Nyman connection supply the Blaschke geometry; WI-412 derives the centered scale kernel (1) and the source-budget consequences of Haar mixing. The present finding adds only the exact spectral analysis of that already-established kernel and the resulting closure of the distributional loophole.

The durable new evidence for this line is therefore not a new special-function formula. It is the exact implication

\[
\boxed{
T_K\mu\equiv q,\ \mu\in\mathcal S'(\mathbb R)
\quad\Longrightarrow\quad
\mu=\frac{2q}{\pi^2}\,ds,
}
\tag{22}
\]

and its combination with WI-412: within the tempered centered linear scale architecture, **exact all-depth count coercivity has no alternative distributional realization with a different budget profile**.

## 5. Boundaries and consequence

This result should not be promoted to a no-go theorem for every Blaschke-based defect detector. It leaves open, among other things, approximate or one-sided depth coercivity, finite depth windows, scale weights that depend on ordinate or other zero data, coupled scale-height operators rather than the centered one-dimensional kernel, nonlinear functionals, and source-side renormalizations outside `S'`. It also says nothing by itself about whether such alternatives can be represented by an unconditional zeta explicit/source formula with controlled arithmetic cost.

What it does remove is a concrete ambiguity at the WI-412 frontier. Once the target is an **exact constant response for all positive depths** and the admissible scale object is tempered, there is no distributional design freedom left: Fourier inversion forces normalized Haar measure. Since WI-412 already prices that Haar solution, further work on this route must relax exact constancy or change the architecture, rather than search for a more exotic tempered scale distribution implementing the same profile.