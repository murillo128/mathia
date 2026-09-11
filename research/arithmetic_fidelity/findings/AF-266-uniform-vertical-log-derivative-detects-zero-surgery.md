# AF-266 — Uniform vertical logarithmic derivative detects compact-open invisible zero surgery

**Status:** `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `MATCHED-CONTROL`, `HEIGHT-UNIFORM-WITNESS`, `QUANTITATIVE-RECOVERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-265 shows that a Riemann-symmetric off-critical zero quartet can escape to arbitrarily large height while the normalized completed functions converge back to `xi` uniformly on every compact set. The obstruction is therefore invisible to every fixed compact-open-continuous observation. The same controls are **not** invisible once the retained representation contains a height-uniform logarithmic-derivative channel on any fixed line `Re(s)=sigma>1`.

Fix `sigma>1`. Write

\[
A(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi\!\left(\frac s2\right),
\tag{1}
\]

so that for Riemann's completed function

\[
\frac{\xi'}{\xi}(s)
=A(s)+\frac{\zeta'}{\zeta}(s)
=A(s)-\sum_{n\ge2}\frac{\Lambda(n)}{n^s},
\qquad \Re s>1.
\tag{2}
\]

For any meromorphic `f` compared in this fixed Riemann completion, define the renormalized logarithmic derivative

\[
\mathcal R_f(s)=\frac{f'}{f}(s)-A(s).
\tag{3}
\]

Let

\[
\rho=\beta+i\gamma,
\qquad \frac12<\beta<1,
\qquad \gamma>0,
\tag{4}
\]

and insert the symmetric quartet

\[
Q=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},
\qquad
M(s)=\prod_{z\in Q}\left(1-\frac{s}{z}\right),
\qquad
F(s)=M(s)\xi(s).
\tag{5}
\]

Then

\[
\mathcal R_F(s)-\mathcal R_\xi(s)
=\frac{M'}M(s)
=\sum_{z\in Q}\frac1{s-z}.
\tag{6}
\]

Define the vertical-line seminorm

\[
\|g\|_{\sigma,\infty}
=\sup_{t\in\mathbb R}|g(\sigma+it)|.
\tag{7}
\]

Every such off-critical quartet has the **height- and beta-uniform separation**

\[
\boxed{
\|\mathcal R_F-\mathcal R_\xi\|_{\sigma,\infty}
\ge m_\sigma,
\qquad
m_\sigma:=\frac{2}{\sigma-1/2}.
}
\tag{8}
\]

The witness is the moving observation height `t=gamma`. In contrast, for a bounded vertical band

\[
\|g\|_{\sigma,T}=\sup_{|t|\le T}|g(\sigma+it)|,
\tag{9}
\]

one has for `gamma>T`

\[
\boxed{
\|\mathcal R_F-\mathcal R_\xi\|_{\sigma,T}
\le \frac{4}{\gamma-T},
}
\tag{10}
\]

so every fixed bandwidth is again asymptotically blind as the inserted quartet escapes upward. More generally, if `T_gamma <= (1-delta)gamma` for some fixed `delta>0`, the discrepancy is `O_delta(gamma^{-1})`. Thus the missing resource in AF-265 can be localized sharply: **the observer must follow the escaping height; compact accuracy or sublinear vertical reach cannot provide a uniform modulus.**

The height-uniform channel also has a finite arithmetic approximation independent of the quartet height. Put

\[
R_X(s)=-\sum_{2\le n\le X}\frac{\Lambda(n)}{n^s}.
\tag{11}
\]

For every integer `X>=3`, absolute convergence gives uniformly for all `t in R`

\[
\boxed{
\sup_t
|\mathcal R_\xi(\sigma+it)-R_X(\sigma+it)|
\le E_\sigma(X),
}
\tag{12}
\]

where

\[
E_\sigma(X)
:=\sum_{n>X}\Lambda(n)n^{-\sigma}
\le
X^{1-\sigma}
\left(
\frac{\log X}{\sigma-1}
+\frac1{(\sigma-1)^2}
\right).
\tag{13}
\]

Consequently choose any `X=X(sigma)` for which

\[
E_\sigma(X)<\frac{m_\sigma}{2}
=\frac1{\sigma-1/2}.
\tag{14}
\]

Then the same finite prime-power prefix separates `xi` from **every** one-quartet control `(5)`, regardless of `beta` and `gamma`:

\[
\sup_t|\mathcal R_\xi(\sigma+it)-R_X(\sigma+it)|
<\frac{m_\sigma}{2},
\tag{15}
\]

while

\[
\boxed{
\sup_t|\mathcal R_F(\sigma+it)-R_X(\sigma+it)|
>\frac{m_\sigma}{2}.
}
\tag{16}
\]

Thus the AF-265 controls are not merely distinguished by the *exact* Euler product, as AF-019 would already imply. They are separated with a positive uniform margin by a representation using only a **fixed finite arithmetic prefix plus unbounded vertical access**. The required arithmetic truncation scale depends on `sigma` and desired margin, but not on the escaping zero height.

## Exact derivation

### 1. The quartet has a positive moving-height Poisson contribution

Differentiating `(5)` gives `(6)`. Evaluate at

\[
s_\gamma=\sigma+i\gamma.
\tag{17}
\]

The two zeros with imaginary part `+gamma` contribute exactly

\[
\frac1{s_\gamma-\rho}
+\frac1{s_\gamma-(1-\bar\rho)}
=
\frac1{\sigma-\beta}
+\frac1{\sigma-1+\beta}.
\tag{18}
\]

The two reflected zeros at height `-gamma` contribute

\[
\frac1{\sigma-\beta+2i\gamma}
+\frac1{\sigma-1+\beta+2i\gamma}.
\tag{19}
\]

Because `sigma>1`, both real parts in `(19)` are positive. Hence

\[
\Re\frac{M'}M(s_\gamma)
\ge
\frac1{\sigma-\beta}
+\frac1{\sigma-1+\beta}.
\tag{20}
\]

Set

\[
a=\sigma-\frac12,
\qquad
x=\beta-\frac12.
\tag{21}
\]

Then `0<x<1/2<a` and

\[
\frac1{a-x}+\frac1{a+x}
=\frac{2a}{a^2-x^2}
\ge \frac2a
=\frac{2}{\sigma-1/2}.
\tag{22}
\]

Since modulus dominates real part, `(8)` follows. Notice that the lower bound does not deteriorate as `gamma` grows and, after minimizing over the full off-critical range, does not depend on `beta` either.

### 2. Every vertical band that stays macroscopically below the zero height is blind

For `|t|<=T<gamma`, every `z in Q` has imaginary part `+gamma` or `-gamma`, so

\[
|\sigma+it-z|
\ge |t-\Im z|
\ge \gamma-T.
\tag{23}
\]

Therefore `(6)` gives

\[
\left|\frac{M'}M(\sigma+it)\right|
\le\sum_{z\in Q}\frac1{|\sigma+it-z|}
\le\frac4{\gamma-T},
\tag{24}
\]

which proves `(10)`. If `T_gamma <= (1-delta)gamma`, then `gamma-T_gamma>=delta gamma` and the discrepancy is at most `4/(delta gamma)`.

This is the logarithmic-derivative analogue of AF-265's compact-open collapse, but it identifies the lost resource quantitatively: fixed or proportionally sub-height bandwidth cannot track a divisor component escaping to infinity, whereas the full vertical line retains a fixed separation modulus.

### 3. The true Riemann channel is uniformly approximable from a finite prime-power prefix

Equation `(2)` is the classical von Mangoldt Dirichlet series in `Re(s)>1`. Therefore

\[
\mathcal R_\xi(s)
=-\sum_{n\ge2}\Lambda(n)n^{-s}.
\tag{25}
\]

For `s=sigma+it`, absolute values remove the phase:

\[
|\mathcal R_\xi(s)-R_X(s)|
\le
\sum_{n>X}\Lambda(n)n^{-\sigma}
=E_\sigma(X),
\tag{26}
\]

uniformly in `t`. Since `Lambda(n)<=log n` and `x^{-sigma}log x` is decreasing for `x>=3`,

\[
E_\sigma(X)
\le
\sum_{n>X}(\log n)n^{-\sigma}
\le
\int_X^\infty (\log x)x^{-\sigma}\,dx,
\tag{27}
\]

which evaluates to `(13)`. In particular `E_sigma(X)->0`, so a finite `X(sigma)` satisfying `(14)` always exists.

For `xi`, `(15)` is immediate. For the quartet control, evaluate at `s_gamma` and use the reverse triangle inequality together with `(8)` and `(12)`:

\[
\begin{aligned}
|\mathcal R_F(s_\gamma)-R_X(s_\gamma)|
&\ge
|\mathcal R_F(s_\gamma)-\mathcal R_\xi(s_\gamma)|
-|\mathcal R_\xi(s_\gamma)-R_X(s_\gamma)|\\
&\ge m_\sigma-E_\sigma(X)
>\frac{m_\sigma}{2}.
\end{aligned}
\tag{28}
\]

This proves `(16)`.

## What this changes in the Arithmetic Fidelity audit

AF-265 established a genuine stability obstruction for the compact-open topology, but its controls deliberately alter the zero divisor without supplying a corresponding Euler/Dirichlet source law. The present result shows exactly how that missing arithmetic coupling becomes observable.

There are now three distinct resource levels for the same escaping quartet:

- **fixed compact / fixed vertical band:** discrepancy tends to zero as the quartet height tends to infinity;
- **full vertical logarithmic-derivative channel:** discrepancy is bounded below by the universal positive margin `m_sigma`;
- **full vertical channel referenced to the Riemann source:** a fixed finite von-Mangoldt prefix already approximates the genuine `xi` residual closely enough to separate every one-quartet AF-265 control uniformly in height.

The new point is quantitative rather than set-theoretic. AF-019 already says that equality of exact normalized Euler logarithmic derivatives is faithful. Here the source data may be truncated once and for all: what must grow with an escaping zero is **vertical observation height**, not arithmetic prefix length.

This turns the broad instruction “use Euler-product/Dirichlet structure” into a more precise next obstruction. A high dangerous quartet can survive only if its positive moving-height contribution is compensated by simultaneous changes elsewhere in the zero-side representation while the exact prime-side logarithmic derivative remains fixed. AF-265's pure insertion controls have no such compensation and are therefore eliminated immediately by the height-uniform source channel.

## Prior art and novelty assessment

All analytic ingredients are classical. The identity `(2)` is the standard logarithmic derivative of the Euler product for `zeta` in `Re(s)>1`, already used in AF-019. Hadamard/logarithmic-derivative representations of `xi` and Poisson-kernel-type positive contributions `Re(1/(s-rho))` are standard in the analytic theory of the zeta function; the local source ledger already records Titchmarsh's *The Theory of the Riemann Zeta-function* for the completed function and zero-product framework.

A targeted literature search also finds a substantial existing literature on bounds and positivity for real parts of logarithmic derivatives of `zeta` and `xi`. Nothing here is claimed as a new theorem about those classical functions. The Arithmetic Fidelity contribution is the **specific stability comparison against the AF-265 matched-control fiber**: compact-open convergence coexists with a beta- and height-uniform full-vertical separation, and absolute convergence then shows that a fixed finite arithmetic prefix suffices once that unbounded-height observation resource is admitted.

No claim of broad novelty is made for the quartet estimate, the Dirichlet tail estimate, or the positivity mechanism individually.

## Boundaries and failure modes

- The result eliminates the **pure quartet-insertion controls** `F=M xi` from AF-265 once the full vertical logarithmic-derivative representation is retained. It does not eliminate AF-264-style signed zero replacements, where removed zeros can contribute with the opposite sign and compensate the inserted quartet.
- The unbounded vertical seminorm is a real additional resource. A finite source prefix does not by itself detect a zero at unknown arbitrarily large height if the observer is restricted to bounded `|t|`; `(10)` quantifies that failure.
- The comparison subtracts the fixed Riemann archimedean completion `A(s)`. It is therefore a matched comparison inside the same completion category, not a theorem about arbitrary entire functions with different gamma factors or conductors.
- The finite arithmetic approximation uses `Re(s)=sigma>1`. It does not transport the finite Dirichlet polynomial itself into the critical strip.
- The theorem does **not** prove that an actual off-critical zero of `zeta` is impossible. For the genuine `xi`, the prime-side identity `(25)` holds whether or not RH is true. If an actual off-critical quartet exists, its contribution can be compensated by the rest of the true zero divisor. The open RH-facing problem is therefore a nonlocal compensation problem, not the one-quartet insertion problem solved here.
- The separation is target-relative. It distinguishes the exact Riemann prime-side residual from the synthetic AF-265 control; it is not a generic metric on all L-functions or generalized prime systems.
- `Lambda(n)<=log n` gives a deliberately elementary tail bound. Sharper truncation bounds can reduce `X(sigma)` but do not change the qualitative conclusion.

## Decisive audit test

For any proposed compression that claims to retain enough arithmetic information to rule out a dangerous high zero configuration, ask:

1. what vertical height range is actually observed;
2. whether the retained representation contains the regular logarithmic-derivative information or only divisor/residue summaries;
3. whether the prime-side approximation error is uniform in the vertical parameter;
4. whether an inserted positive Poisson contribution can be cancelled by other allowed changes in the zero divisor;
5. whether the claimed margin survives when the responsible zero height tends to infinity.

A fixed-band representation fails item 5 by `(10)`. The full right-half-plane logarithmic-derivative channel passes it for one-quartet insertion by `(8)`, and the Riemann Euler source admits the height-uniform finite-prefix approximation `(12)`--`(16)`.

## Consequence for the line

AF-265's compact-open obstruction is now sharply localized rather than merely negative. **Escaping zeros defeat local observation, but they do not defeat a height-uniform prime-side logarithmic-derivative channel.** For pure quartet insertion, the arithmetic prefix cost can remain fixed while the vertical observation must track the escaping height.

The live frontier therefore moves one level deeper. It is no longer enough to construct Riemann-symmetric high-zero controls that are locally invisible; those controls must also reproduce the nonlocal prime/zero coupling. Any genuine counter-control relevant to RH must arrange compensation of the moving-height logarithmic-derivative signature while preserving the exact Euler/Dirichlet source. Proving that such compensation is impossible, or classifying the minimal global information that prevents it, is the next zeta-specific fidelity question.