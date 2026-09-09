# MC-169 — The Bost–Connes θ-heat orbit has RH-critical exponential type `1/16`

**Status:** `LITERATURE+EXACT-DERIVED`, `RH-EQUIVALENT-BOUNDARY`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the square-free supersymmetric Riemann-gas/Bost–Connes spectral data used in `MC-167`–`MC-168`,

\[
\mathcal H_F=
\overline{\operatorname{span}}\{\varepsilon_n:n\text{ squarefree}\},
\qquad
F\varepsilon_n=\mu(n)\varepsilon_n,
\qquad
H\varepsilon_n=(\log n)\varepsilon_n.
\]

Greenfield–Marcolli–Teh prove that the corresponding Dirac operator is `θ`-summable; in this representation this is the elementary trace-class fact

\[
\operatorname{Tr}(e^{-\beta H^2})
=
\sum_{n\text{ squarefree}}e^{-\beta(\log n)^2}
<\infty
\qquad(\beta>0).
\]

The source-forced **signed time-orbit heat trace** is therefore an honest absolutely convergent spectral observable for every `β>0` and every real `t`:

\[
\Theta_\mu(\beta,t)
:=
\operatorname{Tr}_{\mathcal H_F}
\!\left(F e^{-\beta H^2}e^{-itH}\right)
=
\sum_{n\ge1}\mu(n)n^{-it}e^{-\beta(\log n)^2}.
\tag{1}
\]

No analytic continuation of `1/ζ` is needed to define `(1)`.

Nevertheless, the critical small-`β` growth threshold of the **full time orbit** is already equivalent to RH:

\[
\boxed{
\mathrm{RH}
\iff
\forall t\in\mathbb R:\quad
\limsup_{\beta\downarrow0}
\beta\log^+|\Theta_\mu(\beta,t)|
\le \frac1{16}.
}
\tag{2}
\]

Equivalently, RH holds if and only if for every fixed `t` and every `ε>0`,

\[
\boxed{
\Theta_\mu(\beta,t)
=
O_{t,\varepsilon}\!\left(
\exp\!\left(\frac{1/16+\varepsilon}{\beta}\right)
\right)
\qquad(\beta\downarrow0).
}
\tag{3}
\]

The constant `1/16` is not an arbitrary normalization. The map

\[
x^a
\quad\longleftrightarrow\quad
\exp\!\left(\frac{a^2}{4\beta}\right)
\tag{4}
\]

is the exact Gaussian saddle/Poisson-subordination conversion for the Hamiltonian `H=\log n`. Thus the Mertens critical exponent `a=1/2` becomes the heat exponential type `a^2/4=1/16`.

This gives a precise classification of a natural infinite analytic completion left open by the finite Bost–Connes obstruction ladder. The `θ`-heat trace is genuinely convergent and globally phase-sensitive, unlike the finite singular-value channels classified in `MC-167`. But controlling its source-forced time orbit at the critical type is **not cheaper than RH**: it is another exact RH-equivalent boundary.

## 1. RH gives the `1/16` heat type

For fixed `t`, write

\[
A_t(x)
:=
\sum_{n\le x}\mu(n)n^{-it}.
\tag{5}
\]

Assume RH. The classical Littlewood–Titchmarsh Mertens criterion gives, for every `δ>0`,

\[
M(x)=O_\delta(x^{1/2+\delta}).
\tag{6}
\]

Partial summation with the fixed phase `n^{-it}` yields

\[
A_t(x)
=
x^{-it}M(x)
+it\int_1^x M(u)u^{-it-1}\,du,
\]

and hence

\[
A_t(x)=O_{t,\delta}(x^{1/2+\delta}).
\tag{7}
\]

Now put

\[
w_\beta(x)=e^{-\beta(\log x)^2}.
\]

Since `(1)` converges absolutely and `w_\beta(x)` decays faster than every fixed power as `x\to\infty`, Abel summation gives

\[
\Theta_\mu(\beta,t)
=-\int_1^\infty A_t(x)w_\beta'(x)\,dx.
\]

With `x=e^u`,

\[
\Theta_\mu(\beta,t)
=
2\beta\int_0^\infty
A_t(e^u)\,u\,e^{-\beta u^2}\,du.
\tag{8}
\]

Take

\[
a=\frac12+\delta.
\]

Using `(7)` in `(8)`,

\[
|\Theta_\mu(\beta,t)|
\ll_{t,\delta}
2\beta\int_0^\infty
u e^{a u-\beta u^2}\,du.
\tag{9}
\]

Completing the square,

\[
a u-\beta u^2
=
\frac{a^2}{4\beta}
-\beta\left(u-\frac{a}{2\beta}\right)^2.
\]

The remaining Gaussian integral contributes only a polynomial factor in `β^{-1/2}`; for example

\[
2\beta\int_0^\infty
u e^{a u-\beta u^2}\,du
\ll_a
(1+\beta^{-1/2})
\exp\!\left(\frac{a^2}{4\beta}\right).
\tag{10}
\]

Given any requested `ε>0`, choose `δ>0` so small that

\[
\frac{(1/2+\delta)^2}{4}<\frac1{16}+\frac\varepsilon2.
\]

The polynomial factor in `(10)` is absorbed by

\[
\exp\!\left(\frac{\varepsilon}{2\beta}\right)
\]

for sufficiently small `β`. This proves `(3)` and therefore the forward implication in `(2)`.

The argument also records the more general exponent conversion: any bound

\[
A_t(x)=O(x^{a+o(1)})
\]

forces heat type at most `a^2/4`.

## 2. Poisson subordination turns the heat orbit back into `1/ζ`

For real `σ>0` and `u\ge0`, the classical Poisson/heat subordination identity is

\[
\boxed{
e^{-\sigma u}
=
\frac{\sigma}{2\sqrt\pi}
\int_0^\infty
\beta^{-3/2}
\exp\!\left(-\frac{\sigma^2}{4\beta}\right)
 e^{-\beta u^2}\,d\beta.
}
\tag{11}
\]

It is an elementary Gaussian integral and can be checked directly by the substitution `v=σ/(2\sqrt\beta)`.

For `σ>1`, absolute convergence permits insertion of `(11)` term by term into the ordinary Möbius Dirichlet series. Using `(1)` gives

\[
\boxed{
\frac1{\zeta(\sigma+it)}
=
\frac{\sigma}{2\sqrt\pi}
\int_0^\infty
\beta^{-3/2}
\exp\!\left(-\frac{\sigma^2}{4\beta}\right)
\Theta_\mu(\beta,t)\,d\beta.
}
\tag{12}
\]

Equation `(12)` is initially only an identity in the absolutely convergent half-plane. Its importance here is that the small-`β` growth of `Θ_\mu` determines how far the right side itself can be continued before any zero information is inserted.

Assume now `(3)` for every fixed `t`. Fix an arbitrary

\[
\sigma_0>\frac12
\]

and the chosen real `t`. Select `η>0` so that

\[
\frac1{16}+\eta
<
\frac{\sigma_0^2}{4}.
\tag{13}
\]

The assumed heat bound and `(13)` imply absolute convergence of the right side of `(12)` at every real `σ\ge\sigma_0`: near `β=0` the integrand has an exponential margin

\[
\exp\!\left(
-\frac{\sigma^2/4-1/16-\eta}{\beta}
\right),
\]

while near `β=\infty` the factor `β^{-3/2}` is integrable and `\Theta_\mu(\beta,t)` is bounded because `(1)` is absolutely convergent uniformly for `β` bounded away from zero.

More is true. For complex `z` in the right-hand component of

\[
\operatorname{Re}(z^2)>\frac14+4\eta,
\tag{14}
\]

the integral

\[
G_t(z)
:=
\frac{z}{2\sqrt\pi}
\int_0^\infty
\beta^{-3/2}
 e^{-z^2/(4\beta)}
\Theta_\mu(\beta,t)\,d\beta
\tag{15}
\]

converges locally uniformly and is holomorphic. The component in `(14)` contains the whole real interval `[\sigma_0,\infty)`.

For real `z>1`, `(12)` says

\[
G_t(z)=\frac1{\zeta(z+it)}.
\tag{16}
\]

By uniqueness of meromorphic continuation, `(15)` is therefore the continuation of `1/\zeta(z+it)` throughout that connected component. But `G_t` is holomorphic there. Hence `1/\zeta(z+it)` has no pole at the real point `z=\sigma_0`, which means

\[
\zeta(\sigma_0+it)\ne0.
\tag{17}
\]

Because both `t\in\mathbb R` and `\sigma_0>1/2` were arbitrary,

\[
\zeta(s)\ne0
\qquad
\text{for all }\operatorname{Re}s>\frac12.
\tag{18}
\]

The functional equation and conjugation symmetry of the nontrivial zero set then force every nontrivial zero onto `Re(s)=1/2`. This proves RH and the reverse implication in `(2)`.

## 3. The time orbit is essential; the untwisted scalar heat trace is not enough

The role of `t` in `(1)` is structural, not decorative. For one fixed `t`, subordination controls the shifted vertical line

\[
s=\sigma+it.
\]

The untwisted trace `\Theta_\mu(\beta,0)` can therefore probe only `1/\zeta(\sigma)` on the positive real axis through `(12)`. Since the nontrivial zeros are off that axis, a critical heat bound at `t=0` alone is not the criterion `(2)`.

To exclude every off-critical zero, one needs the critical heat-type estimate for every fixed time-flow modulation `e^{-itH}`. No uniformity of the implied constants in `t` is required for the equivalence: for each hypothetical zero ordinate `t`, the corresponding fixed orbit element is enough.

This clarifies the information content of the source-forced infinite completion. The family

\[
\{F e^{-\beta H^2}e^{-itH}:\beta>0,\ t\in\mathbb R\}
\]

is rich enough to recover the reciprocal-zeta zero-free boundary through the standard subordination transform. Its critical estimate is therefore not an independently weaker statistic unless some additional theorem controls the whole family without already paying the Mertens/RH information budget.

## 4. Matched phase-free control has heat type `1/4`

The critical `1/16` is not a universal consequence of the Hamiltonian alone. Replace the Möbius phase on the same square-free Hilbert space by the all-plus control `F_+=I`. Its untwisted heat trace is

\[
\Theta_+(\beta,0)
=
\sum_{n\text{ squarefree}}
 e^{-\beta(\log n)^2}.
\tag{19}
\]

Using the classical square-free counting law

\[
Q(x)=\frac6{\pi^2}x+O(\sqrt x)
\]

and Abel summation, the main term is governed by

\[
\int_1^\infty e^{-\beta(\log x)^2}\,dx
=
\int_0^\infty e^{u-\beta u^2}\,du.
\]

Its saddle is at `u=1/(2β)`, so

\[
\boxed{
\lim_{\beta\downarrow0}
\beta\log \Theta_+(\beta,0)
=
\frac14.
}
\tag{20}
\]

The square-free counting error has exponent `1/16` and is exponentially smaller than the main `1/4` type. Thus the canonical Hamiltonian plus support does not itself force the RH-critical heat behavior. The reduction from `1/4` to at most `1/16` is precisely a global signed-cancellation demand.

This matched control is useful because it separates the result from `MC-167`'s singular-value collapse. The signed heat trace is genuinely phase-sensitive. The obstruction is subtler: the **amount** of phase cancellation needed at critical heat type is already RH-equivalent.

## 5. Relation to the current Bost–Connes frontier

`MC-166` proves that arbitrary finite coefficient-decorated commutator words remain in the same two Möbius phase sectors. `MC-167` shows that the canonical `σ`-twisted commutator is a unitary copy of the phase-free Hamiltonian derivation, while its obvious signed eta trace gives the classical reciprocal-zeta series. `MC-168` shows that twisted Lipschitz regularity recovers phase only as a local parity selector.

The present result treats a different, genuinely infinite and source-forced object: the `θ`-summable heat semigroup already built into the same spectral triple. Because `(1)` is absolutely convergent for every `β>0`, this route does not fail by asking a finite commutator to manufacture global information, nor does it begin by analytically continuing `1/ζ` into the critical strip.

What fails is the hoped-for quantitative discount. The full time-modulated heat orbit crosses the critical boundary exactly when its small-time exponential type reaches `1/16`, and that statement is equivalent to RH. Therefore simply replacing the eta/Dirichlet observable by the convergent `θ`-heat observable does not create a cheaper cancellation theorem.

A surviving heat-semigroup route would need an **independent source theorem** that forces the `1/16` type, or a weaker relational heat statistic from which the same bound follows with a genuine information gain. Merely observing `θ`-summability is far too weak: the all-plus control is `θ`-summable too and has type `1/4`.

## 6. Prior art and novelty audit

The source construction is established prior art. Mark Greenfield, Matilde Marcolli and Kevin Teh, *Type III σ-spectral triples and quantum statistical mechanical systems*, **p-Adic Numbers, Ultrametric Analysis and Applications** 6 (2014), 81–104, DOI `10.1134/S2070046614020010`, arXiv `1305.5492`, construct the Riemann-gas/Bost–Connes `σ`-spectral triples, prove `θ`-summability, and discuss the associated zeta/eta functions. Their Möbius construction is the source of `F`, `H`, and the heat semigroup used here.

The implication

\[
\mathrm{RH}
\iff
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\]

is the classical Littlewood–Titchmarsh Mertens criterion already used elsewhere in this line. Formula `(11)` is the standard Poisson-semigroup subordination formula for a heat semigroup and is proved directly above in the scalar case.

A targeted literature search for the specific Gaussian Möbius trace

\[
\sum_n\mu(n)n^{-it}e^{-\beta(\log n)^2}
\]

and for an RH criterion stated as its critical small-time exponential type did not locate a primary source stating `(2)` in this form. That search absence is **not** used as evidence of novelty. The derivation is a direct synthesis of established θ-summability, the classical Mertens criterion, Abel summation, and standard heat-to-Poisson subordination. Accordingly **no novelty claim is made**.

## Boundaries and falsification tests

- Equation `(2)` is an RH-equivalent criterion, not progress toward proving its critical estimate.
- `θ`-summability alone says only that `(1)` is finite for each fixed `β>0`; it gives no useful small-`β` exponent. The all-plus control `(20)` proves this distinction quantitatively.
- A bound only at `t=0`, at finitely many `t`, or on average over `t` does not imply `(18)` without an additional theorem controlling the missing ordinates.
- The constants in `(3)` may depend arbitrarily on the fixed `t`. Uniformity in `t` is not being smuggled into the criterion.
- The converse uses the known meromorphic continuation of `ζ` only to identify the holomorphic integral `(15)` with the unique continuation of the already-equal Dirichlet series from `Re(s)>1`. It does not assume that `1/ζ` is holomorphic in the region being proved zero-free.
- The threshold `1/16` is tied to the source Hamiltonian `H=\log n` and Gaussian heat kernel `e^{-\beta H^2}`. Replacing the Hamiltonian or kernel changes the Legendre/subordination conversion and requires a new audit.
- The result concerns the full signed trace. Absolute values taken **inside** the trace remove cancellation and return the phase-free `1/4` control scale.
- Nothing here rules out a relational, operator-valued, non-scalar, or cross-time heat observable whose estimate is genuinely cheaper. Such a proposal must identify the extra structure and prove that its transfer to `(3)` avoids target reconstruction.

## Consequence for the line

The most canonical nonfinite analytic exit from the recent Bost–Connes finite-algebra obstruction ladder can now be classified sharply. The source's `θ`-summable heat semigroup does retain Möbius cancellation in a convergent object, but its natural time-orbit critical growth condition is **exactly RH-equivalent**.

This narrows the live Bost–Connes search again: future work should not treat convergence or heat regularization itself as the missing mechanism. It must find a source-forced relation that controls the signed heat orbit at the `1/16` threshold from information strictly weaker than a Mertens/RH bound, or leave this scalar heat-trace channel.