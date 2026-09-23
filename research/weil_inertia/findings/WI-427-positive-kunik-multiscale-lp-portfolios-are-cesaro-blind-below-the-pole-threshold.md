# WI-427 — Positive Kunik multiscale `L^p` portfolios are Cesàro-blind below the pole threshold

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-CONSTRAINT + DECISIVE-NEGATIVE + FRONTIER-ADVANCE + NO-RH`.

**Parents:** [WI-412](./WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md), [WI-422](./WI-422-translated-blaschke-source-regularity-has-sharp-lp-threshold.md), [WI-424](./WI-424-kunik-boundary-flux-is-a-poisson-defect-counter.md), [WI-425](./WI-425-fixed-safe-lines-are-cubically-blind-to-shallow-boundary-flux.md), [WI-426](./WI-426-kunik-multiscale-l2-has-blind-or-singular-dichotomy.md).

## Claim

WI-424 identifies the boundary logarithmic derivative of the Kunik Blaschke factor as a canonical positive defect counter. WI-425 shows that a fixed interior line is badly conditioned for shallow defects, and WI-426 shows that positive multiscale `L^2` line energy has a blind-or-singular dichotomy. An explicit loophole left by WI-426 was to move below the planar pole threshold and use `L^p` line energies with `1\le p<2`, where crossing the unknown defect depth is locally integrable.

That loophole still does not produce a target-independent positive defect counter.

For one right-half zero

\[
\rho=\frac12+d+i\gamma,
\qquad d>0,
\]

and a vertical line displaced by `a>0` from the critical line, center the ordinate at `gamma` and write

\[
g_{a;d}(t)
:=
\frac1{a-d+it}
-
\frac1{a+d+it}.
\tag{1}
\]

At the boundary `a=0`, `|g_{0;d}(t)|=2d/(d^2+t^2)`, exactly the one-zero Poisson flux from WI-424.

Fix `1\le p<2` and define

\[
C_p
:=
2^p\int_{\mathbb R}(1+v^2)^{-p}\,dv
=
2^p\sqrt\pi\,
\frac{\Gamma(p-\tfrac12)}{\Gamma(p)}.
\tag{2}
\]

Then

\[
\boxed{
\|g_{0;d}\|_p^p=C_p d^{1-p}.
}
\tag{3}
\]

Let `mu` be any positive Borel measure on `(0,infty)`, chosen independently of the unknown depth `d`, and form the positive diagonal scale portfolio

\[
Q_{p,\mu}(d)
:=
\int_{(0,\infty)}
\|g_{a;d}\|_p^p\,d\mu(a).
\tag{4}
\]

Assume only that this portfolio has finite cost for one nonzero hypothetical defect depth:

\[
Q_{p,\mu}(d_*)<\infty
\qquad\text{for some }d_*>0.
\tag{5}
\]

Then the normalized shallow-depth response is Cesàro-null:

\[
\boxed{
\lim_{\varepsilon\downarrow0}
\frac1\varepsilon
\int_0^\varepsilon
\frac{Q_{p,\mu}(d)}{C_p d^{1-p}}\,dd
=0.
}
\tag{6}
\]

Consequently, for every `c>0`,

\[
\boxed{
\frac1\varepsilon
\left|
\left\{0<d<\varepsilon:
Q_{p,\mu}(d)\ge c\,\|g_{0;d}\|_p^p
\right\}
\right|
\longrightarrow0.
}
\tag{7}
\]

In particular there is no constant `c>0` for which a fixed positive scale measure with finite one-defect cost can satisfy

\[
Q_{p,\mu}(d)
\ge c\,\|g_{0;d}\|_p^p
\tag{8}
\]

for every sufficiently shallow depth. This allows arbitrary positive Borel scale portfolios: finite, infinite, continuous, discrete, singular, or mixtures. Atoms may make `Q_{p,mu}` infinite at their exactly matching depths, but (6)--(7) show that such spikes cannot fill a whole shallow-depth interval at finite target-independent cost.

Thus moving from `L^2` to any ordinary positive diagonal line functional `L^p`, `1\le p<2`, removes the pole singularity but does **not** remove the scale-budget obstruction. The natural scale-invariant weight `d\mu(a)=da/a` would make the response depth-homogeneous, but it has

\[
Q_{p,\mu}(d)=\infty
\tag{9}
\]

for every `d`, because the scale integral diverges logarithmically at `a=0`. This is the line-energy analogue of WI-412's infinite Haar-scale budget.

The conclusion is deliberately restricted to **positive diagonal scale combinations of ordinary line `L^p` energies**. It does not exclude signed or non-diagonal cross-scale forms, cancellation before taking a norm, Lorentz/tent/maximal functionals, renormalized pole subtraction, an independently generated depth selector, or zeta-specific arithmetic information that couples the accessible source to the unknown defect set.

## 1. Exact dilation reduction

Put

\[
a=dr,
\qquad
t=dv.
\]

Then

\[
g_{dr;d}(dv)
=
\frac1d
\left(
\frac1{r-1+iv}
-
\frac1{r+1+iv}
\right).
\tag{10}
\]

Define

\[
F_p(r)
:=
\int_{\mathbb R}
\left|
\frac1{r-1+iv}
-
\frac1{r+1+iv}
\right|^p\,dv.
\tag{11}
\]

Equivalently,

\[
\boxed{
F_p(r)
=
2^p
\int_{\mathbb R}
\frac{dv}{
\left(((r-1)^2+v^2)((r+1)^2+v^2)\right)^{p/2}}
.}
\tag{12}
\]

The scaling is exact:

\[
\boxed{
\|g_{a;d}\|_p^p
=d^{1-p}F_p(a/d).
}
\tag{13}
\]

At `r=0`, (12) gives

\[
F_p(0)=C_p,
\tag{14}
\]

which proves the boundary tariff (3). Hence the normalized portfolio can be written purely as a dilation average,

\[
R_{p,\mu}(d)
:=
\frac{Q_{p,\mu}(d)}{C_p d^{1-p}}
=
\frac1{C_p}
\int F_p(a/d)\,d\mu(a).
\tag{15}
\]

The problem is therefore a Mellin-scale allocation problem: can a fixed positive measure in `a` keep the dilation convolution in (15) uniformly bounded below as `d` approaches the boundary?

## 2. The scale kernel has an integrable crossing only below `p=2`

The exact formula (12) gives the three asymptotic regimes needed for the theorem.

As `r\downarrow0`, dominated convergence gives

\[
\boxed{F_p(r)\to C_p.}
\tag{16}
\]

As `r\to\infty`, put `v=rx`. Then

\[
\boxed{
F_p(r)
\sim C_p r^{1-2p}.
}
\tag{17}
\]

Indeed the two denominator factors become `r^2((1\mp1/r)^2+x^2)`, so the limiting integrand is exactly the one defining `C_p`.

Near the matching line `r=1`, write `delta=r-1`. For `1<p<2`, the singular first pole dominates after `v=|delta|x` and yields

\[
\boxed{
F_p(r)
\sim
A_p|r-1|^{1-p},
\qquad
A_p
=
\sqrt\pi\,
\frac{\Gamma((p-1)/2)}{\Gamma(p/2)}.
}
\tag{18}
\]

For the endpoint `p=1`, the same local comparison gives

\[
\boxed{
F_1(r)
=2\log\frac1{|r-1|}+O(1).
}
\tag{19}
\]

Thus the scale singularity is locally integrable exactly below `p=2`. This is the one-dimensional scale manifestation of WI-426's planar pole threshold: crossing the defect depth is not itself fatal for `1\le p<2`.

For later use define

\[
J_p(x)
:=
x\int_x^\infty F_p(r)\,\frac{dr}{r^2},
\qquad x>0.
\tag{20}
\]

Equations (16)--(19) imply that `J_p` is finite and bounded on `(0,infty)` for every `1\le p<2`, with

\[
\boxed{
J_p(x)\to C_p
\quad(x\downarrow0),
}
\tag{21}
\]

and

\[
\boxed{
J_p(x)
\sim
\frac{C_p}{2p}x^{1-2p}
\quad(x\to\infty).
}
\tag{22}
\]

The local singularity at `r=1` is exactly where `p<2` is used.

## 3. Finite cost at one depth forces enough scale integrability

Assume (5). By (13),

\[
\int F_p(a/d_*)\,d\mu(a)<\infty.
\tag{23}
\]

On every bounded interval in `a`, the function `F_p(a/d_*)` has a strictly positive lower bound; at the matching point it diverges rather than vanishes. Therefore

\[
\boxed{
\mu((0,A])<\infty
\qquad(A<\infty).
}
\tag{24}
\]

In particular `mu` is sigma-finite. At large scale, (17) supplies constants `A,c>0` such that

\[
F_p(a/d_*)
\ge c a^{1-2p}
\qquad(a\ge A),
\]

so (23) also forces

\[
\boxed{
\int_A^\infty a^{1-2p}\,d\mu(a)<\infty.
}
\tag{25}
\]

For `p=1`, this is the finite inverse-scale moment `int a^{-1}dmu`; for `1<p<2` it is the corresponding stronger negative moment. Conditions (24)--(25) are not extra hypotheses: they are consequences of asking the fixed portfolio to be finite at just one defect depth.

## 4. Depth averaging proves the no-go theorem

Because the integrands are nonnegative, Tonelli and the substitution `r=a/d` give

\[
\begin{aligned}
\frac1\varepsilon
\int_0^\varepsilon
R_{p,\mu}(d)\,dd
&=
\frac1{C_p}
\int
\left[
\frac1\varepsilon
\int_0^\varepsilon F_p(a/d)\,dd
\right]d\mu(a)\\
&=
\frac1{C_p}
\int J_p(a/\varepsilon)\,d\mu(a).
\end{aligned}
\tag{26}
\]

Fix `A>0` large enough for the tail estimate (22). On `(0,A]`, (24) gives finite measure, `J_p` is uniformly bounded, and for each fixed `a>0`,

\[
J_p(a/\varepsilon)\to0.
\]

Dominated convergence therefore gives

\[
\int_{(0,A]}J_p(a/\varepsilon)\,d\mu(a)	o0.
\tag{27}
\]

For the tail, (22) gives a constant `K` such that for all sufficiently small `epsilon`,

\[
\begin{aligned}
\int_A^\infty J_p(a/\varepsilon)\,d\mu(a)
&\le
K\int_A^\infty(a/\varepsilon)^{1-2p}\,d\mu(a)\\
&=
K\varepsilon^{2p-1}
\int_A^\infty a^{1-2p}\,d\mu(a)
\longrightarrow0,
\end{aligned}
\tag{28}
\]

using (25). Equations (26)--(28) prove (6).

Equation (7) is then just Markov's inequality on the depth variable. It is stronger than the existence of a blind sequence: for every fixed target fraction `c`, the depths on which the portfolio recovers that fraction of the boundary defect tariff have asymptotic density zero inside `(0,epsilon)`.

The argument is insensitive to atoms or singular scale measures. A point mass at `a=a_0` makes `Q_{p,mu}(a_0)=infty`, because `F_p(1)=infty`, but this one-depth spike has zero Lebesgue measure and cannot defeat the averaged statement. More generally, any singular behavior compatible with (5) is already absorbed by Tonelli in (26).

## 5. The scale-invariant escape is exactly the inadmissible endpoint

A useful control family is

\[
d\mu_\alpha(a)=a^{-\alpha}\,da.
\tag{29}
\]

Whenever the integral is finite, (13) gives

\[
Q_{p,\mu_\alpha}(d)
=
 d^{2-p-\alpha}
\int_0^\infty F_p(r)r^{-\alpha}\,dr,
\tag{30}
\]

so relative to the boundary tariff,

\[
R_{p,\mu_\alpha}(d)
\asymp d^{1-\alpha}.
\tag{31}
\]

Depth-independent normalized response would require `alpha=1`, namely Haar scale measure `da/a`. But (16) gives

\[
\int_0^1F_p(r)\,\frac{dr}{r}=\infty,
\tag{32}
\]

hence the matching scale-invariant portfolio has infinite cost for every defect. Every admissible power law has `alpha<1` at the boundary and therefore loses normalized response as `d\downarrow0`.

This is the same structural tradeoff exposed for the Blaschke potential itself in WI-412, now for the logarithmic-derivative line energies that WI-424--WI-426 brought to the front. The present theorem is stronger than a finite-total-variation statement: `mu` may have infinite total mass, provided only that its one-defect portfolio is finite somewhere.

## 6. Relation to the `p=2` barrier

The result fills the subcritical half of the line-energy phase diagram.

For `1\le p<2`, the line can cross the unknown defect depth without a nonintegrable scale singularity, but every positive target-independent portfolio with finite one-defect cost is Cesàro-blind to almost all sufficiently shallow depths by (6)--(7).

At `p=2`, WI-426 gives

\[
\|g_{a;d}\|_2^2
=
\frac{2\pi d^2}{a(a^2-d^2)}
\qquad(a>d),
\]

and the crossing singularity is proportional to `1/|a-d|`. Any ordinary positive continuum of scales that sweeps through a possible defect depth therefore has infinite energy, while support bounded away from the boundary remains cubically blind.

For `p>2`, the local model `|z-rho|^{-p}` is even less area-integrable across a line family. The present finding does **not** promote that observation into a universal theorem for every singular Borel portfolio above `p=2`; arbitrary thin or non-diagonal constructions remain a separate problem. The safe conclusion is narrower and sufficient for the current frontier: simply choosing an ordinary exponent below `2` does not repair WI-426.

## 7. Adversarial checks and evidence boundary

The derivation was stress-tested against the main ways a positive multiscale construction could evade a fixed-line no-go.

First, `mu` is not assumed finite. The proof derives only the local finiteness and negative tail moment actually needed from one finite value `Q_{p,mu}(d_*)`. Thus a portfolio cannot evade the theorem merely by assigning infinitely much total scale mass far from the boundary.

Second, exact scale atoms are allowed. They may create infinite matching-depth spikes but cannot create a positive-depth-density lower bound, because the depth average in (26) remains controlled.

Third, the theorem normalizes against the **actual boundary `L^p` defect tariff** `C_p d^{1-p}` rather than an arbitrary fixed constant. For `p=1` this tariff is exactly `2pi`, the count-like boundary mass from WI-424; the endpoint is therefore included rather than hidden inside a `p>1` argument.

Fourth, the scale-invariant candidate `da/a` was checked explicitly and sits exactly outside the admissible finite-cost class. The no-go is therefore not an artifact of choosing a noninvariant family of test measures.

What is not proved is equally important. `Q_{p,mu}` is a positive diagonal sum of line norms after taking absolute values. Signed cross-scale interference can use phase before absolute value; non-diagonal quadratic forms can correlate two scales; a source identity might renormalize the pole contribution; and arithmetic data might select scales by a rule independent of the hypothetical zero. None of those mechanisms is represented by (4).

No statement about the existence, density, or displacement of actual off-critical zeta zeros follows. The result is a universal one-zero conditioning barrier for this auxiliary Kunik observable.

## 8. Prior-art and novelty audit

The zeta-specific analytic source remains Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829`, whose symmetric Poisson--Schwarz factorization in `Re(s)>1/2` explicitly includes Blaschke factors for zeta zeros. That source supports the half-plane object, not the new scale-budget conclusion.

The broader function-theory neighborhood is classical. P. Ahern's work on mean moduli of derivatives of inner functions, Ahern--Clark on inner functions with `H^p`/Bergman-type derivative control, D. Girela--J. A. Peláez on Bergman membership of Blaschke derivatives, E. Fricain--J. Mashreghi on integral means of Blaschke derivatives, and later work on logarithmic derivatives of Blaschke products all show that derivative-integrability thresholds are established territory. General Mellin-convolution asymptotics likewise provide a classical language for dilation kernels.

A targeted search by the equivalent structures `Blaschke logarithmic derivative`, `B'/B`, `Bergman/line Lp`, `Mellin convolution`, `positive scale measure`, and `half-plane` did not locate a source giving the specific theorem (6)--(7) for the one-zero Kunik family. That negative search result is **not** used as a priority claim. The durable contribution recorded here is the independently derived exact obstruction at Mathia's current frontier: subcritical pole integrability does not imply target-independent shallow-depth coercivity, even for arbitrary positive Borel scale portfolios with potentially infinite total mass.

## Consequence

WI-426 left `other Lp/Lorentz/maximal/nonlinear functionals` open after closing the positive `L^2` route. The ordinary positive diagonal `L^p` branch is now closed for every `1\le p<2` as well. Together, WI-425--WI-427 show a sharp design split:

- fixed safe lines are conditioned away from shallow defects;
- positive scale averaging below `p=2` is finite but Cesàro-blind unless it spends inadmissible boundary-scale mass;
- positive continuum averaging at `p=2` hits the pole singularity.

The next useful attempt should therefore **change the information structure rather than the exponent**: retain complex phase across scales, introduce a genuinely non-diagonal/canceling form, prove a renormalized source identity, or obtain a zeta/arithmetic mechanism that fixes the relevant scale without oracle knowledge of the defect. Merely replacing `L^2` by another ordinary positive line `L^p` norm cannot supply the monotone defect-to-zero mechanism sought by the research mandate.