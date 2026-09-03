# WP-127 — Bochner subordination cannot sharpen Gamma-Markov decay beyond polynomial

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + GAMMA-MARKOV-SUBORDINATION + ALL-BERNSTEIN-SUBORDINATORS + COMPLETELY-MONOTONE-DAMPING + CORRELATED-BLOCK-CLASS + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-117` identifies the Prime-Circle-selected Riemann Gamma variation

\[
H_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-
\psi\!\left(\frac14\right)
\]

as a genuine symmetric Lévy--Dirichlet/Markov symbol, with

\[
H_\infty(0)=0,
\qquad
H_\infty(t)>0\ (t>0),
\qquad
H_\infty(t)=\log t+O(1)
\quad(t\to\infty).
\tag{1}
\]

`WP-125` and `WP-126` then show that the simple Gamma heat-dissipation filter

\[
H_\infty(t)e^{-\tau H_\infty(t)}
\tag{2}
\]

cannot rescue either the independent critical completion or any finite-block correlated completion. `WP-126` deliberately leaves a sharper escape: an endpoint-degenerate positive spectral filter with **superpolynomial** or compact high-frequency decay.

There is a canonical way one might try to obtain such a sharper filter while retaining the Markov meaning of the Gamma geometry: **Bochner-subordinate the Gamma semigroup first**, and then take heat dissipation or a positive mixture of heat dissipations for the subordinate generator. That entire route fails.

Let `phi` be any nonzero Bernstein function with `phi(0)=0`, so that `phi(H_infty)` is a conservative Bochner-subordinate Markov generator. Let `g` be any nonzero completely monotone function and form the positive spectral multiplier

\[
\boxed{
w_{\phi,g}(t)
:=
\phi(H_\infty(t))\,
 g\!\left(\phi(H_\infty(t))\right).
}
\tag{3}
\]

The standard subordinate heat-dissipation family is the special case

\[
g(x)=e^{-\tau x},
\qquad
w_{\phi,\tau}(t)
=
\phi(H_\infty(t))e^{-\tau\phi(H_\infty(t))}.
\tag{4}
\]

Positive mixtures in the heat parameter are included by complete monotonicity. For **every** nontrivial choice in (3), there exist constants `c>0`, `rho>=0`, and `T>0` such that

\[
\boxed{
w_{\phi,g}(t)\ge c\,t^{-\rho}
\qquad(t\ge T).}
\tag{5}
\]

Thus Bochner subordination can never turn the logarithmically growing intrinsic Gamma generator into the superpolynomial cutoff that remains outside `WP-126`. Applying `WP-126`, every `WP-101`-type finite-block critical completion has infinite cylindrical energy for (3).

If one instead allows a Bernstein function with a killing term `phi(0)>0`, the multiplier is already nondegenerate at zero and the low-frequency obstructions of `WP-113`/`WP-114` apply. Hence the whole fixed **Markov-subordinate Gamma functional-calculus route** is closed for this correlated completion class.

The surviving boundary is precise. A superlinear warping such as `phi(s)=s^2` gives

\[
H_\infty(t)^2e^{-\tau H_\infty(t)^2}
\asymp
(\log t)^2e^{-\tau(\log t)^2},
\tag{6}
\]

which is superpolynomially decaying and therefore escapes the present theorem and `WP-126`. But `s^2` is not a Bernstein function. Such a filter has left the inherited Bochner/Markov geometry and would need a separate Mathia-native reason for its superlinear scale and sign mechanism rather than obtaining them from subordination of the canonical Gamma jump process.

This does not prove Weil positivity or RH. It closes a natural attempt to sharpen the already intrinsic archimedean Markov sector while keeping its probabilistic/Dirichlet provenance.

## 1. Bernstein subordination preserves the Markov meaning of the Gamma channel

By `WP-117`, `H_infty` is a continuous conditionally negative-definite function on `R`. Equivalently,

\[
e^{-uH_\infty(t)}
\tag{7}
\]

is positive definite for every `u>=0`, and `H_infty` is the Fourier symbol of a symmetric Markov jump generator.

A Bernstein function `phi:[0,infinity)->[0,infinity)` is characterized by `phi'` being completely monotone. If `phi(0)=0`, Bochner subordination gives a convolution semigroup of probability measures whose Laplace transform is

\[
\int_0^\infty e^{-s r}\,\mu_u(dr)
=
e^{-u\phi(s)}.
\tag{8}
\]

Consequently

\[
e^{-u\phi(H_\infty(t))}
=
\int_0^\infty
 e^{-rH_\infty(t)}\,\mu_u(dr)
\tag{9}
\]

is again positive definite, and

\[
L_\phi:=\phi(H_\infty(|X|))
\tag{10}
\]

is the generator obtained by subordinating the intrinsic Gamma Markov semigroup. This is the standard sign-preserving functional calculus, not an arbitrary positive spectral kernel.

The first heat-dissipation observable of this subordinate semigroup is

\[
L_\phi e^{-\tau L_\phi},
\tag{11}
\]

whose scalar symbol is exactly (4). More generally, if `g` is completely monotone then Bernstein's theorem gives a positive measure `nu` on `[0,infinity)` with

\[
\boxed{
g(x)=\int_{[0,\infty)}e^{-\tau x}\,\nu(d\tau).}
\tag{12}
\]

Thus (3) is a positive mixture of the subordinate heat-dissipation symbols:

\[
w_{\phi,g}(t)
=
\int_{[0,\infty)}
\phi(H_\infty(t))
 e^{-\tau\phi(H_\infty(t))}
\,\nu(d\tau).
\tag{13}
\]

This is a broad canonical class: arbitrary positive randomization of the heat scale is allowed, while the sign remains inherited from the same subordinate Markov generator.

## 2. A Bernstein function cannot grow superlinearly

The decisive elementary fact is that every Bernstein function is increasing and concave because

\[
\phi'\ge0,
\qquad
\phi''\le0.
\tag{14}
\]

Assume first that `phi(0)=0` and `phi` is nonzero. Concavity implies that `phi(s)/s` is nonincreasing on `(0,infinity)`. Therefore, for every `s>=1`,

\[
\boxed{
0<\phi(1)
\le
\phi(s)
\le
\phi(1)s.
}
\tag{15}
\]

The lower bound uses monotonicity; `phi(1)>0` because a nonnegative increasing concave Bernstein function vanishing at both `0` and `1` would be identically zero.

Now use the exact Gamma asymptotic (1). There is `T_0` such that for `t>=T_0`,

\[
1\le H_\infty(t)\le 2\log t.
\tag{16}
\]

Combining (15) and (16),

\[
\boxed{
\phi(1)
\le
\phi(H_\infty(t))
\le
2\phi(1)\log t
\qquad(t\ge T_0).
}
\tag{17}
\]

So subordination can slow the Gamma generator — fractional powers and logarithmic Bernstein transforms do exactly that — but it cannot accelerate the intrinsic `log t` growth to `(log t)^{1+epsilon}`, `(log t)^2`, or any other superlinear scale.

This is the structural reason the hoped-for superpolynomial cutoff cannot emerge from Bochner subordination.

## 3. Completely monotone damping cannot decay faster than some exponential

Let `g` be nonzero and completely monotone, with representing positive measure `nu` from (12). Since `nu` is nonzero, there is some finite `R>=0` for which

\[
m_R:=\nu([0,R])>0.
\tag{18}
\]

For every `x>=0`, retaining only that bounded part of the measure gives

\[
\boxed{
g(x)
\ge
m_R e^{-Rx}.}
\tag{19}
\]

Thus a nonzero completely monotone function may decay exponentially, subexponentially, or not at all, but it cannot be smaller than **every** exponential on the positive half-line. In particular it cannot have compact support.

Apply (19) at

\[
x=\phi(H_\infty(t)).
\]

Using both sides of (17), for sufficiently large `t`,

\[
\begin{aligned}
w_{\phi,g}(t)
&=
\phi(H_\infty(t))
 g(\phi(H_\infty(t)))\\
&\ge
\phi(1)m_R
\exp\!\left[-R\phi(H_\infty(t))\right]\\
&\ge
\phi(1)m_R
\exp\!\left[-2R\phi(1)\log t\right].
\end{aligned}
\tag{20}
\]

Hence exactly

\[
\boxed{
w_{\phi,g}(t)
\ge
c\,t^{-\rho},
\qquad
c=\phi(1)m_R>0,
\quad
\rho=2R\phi(1).
}
\tag{21}
\]

This proves (5). No asymptotic regular-variation theorem is needed; positivity of the subordination and damping measures is enough.

For the single heat scale `g(x)=e^{-tau x}`, (21) simply says

\[
\phi(H_\infty(t))e^{-\tau\phi(H_\infty(t))}
\gtrsim t^{-\rho_\tau}
\tag{22}
\]

for some finite exponent `rho_tau`. Allowing fractional, relativistic, logarithmic, or any other Bernstein subordinator cannot improve this to a superpolynomial tail.

## 4. WP-126 therefore closes every Markov-subordinate Gamma filter on finite-block critical completions

`WP-126` treats every critical finite-block completion of the `WP-101` form and proves the following exact implication. If a fixed nonnegative spectral multiplier `w` obeys

\[
w(t)\ge c t^{-\rho}
\qquad(t\ge T)
\tag{23}
\]

for some finite `rho`, then its cylindrical Kronecker energy is infinite:

\[
\sup_{P\Subset\mathcal P}
\sum_{\alpha\in\mathbb Z^P}
 w(|E(\alpha)|)
 |\widehat\eta_P(\alpha)|^2
=+\infty.
\tag{24}
\]

Equation (21) puts every nonzero multiplier (3) exactly inside that theorem. Therefore

\[
\boxed{
\sup_{P\Subset\mathcal P}
\mathcal Q_{w_{\phi,g},P}(\eta_P)
=+\infty
}
\tag{25}
\]

for every admissible finite-block critical completion, every nonzero Bernstein `phi` with `phi(0)=0`, and every nonzero completely monotone `g` for which the fixed spectral form is defined.

This strictly strengthens the specific Gamma-heat stress test in `WP-126`. The obstruction is not tied to choosing `phi(s)=s` or one heat time `tau`. It survives **all Bochner subordinators and all positive mixtures of subordinate heat-dissipation scales**.

The independent product completion was already closed more strongly by `WP-125`, which rejects every nonzero continuous nonnegative multiplier. The new content is the correlated finite-block class, where superpolynomial decay had remained a real logical escape.

## 5. A killing term fails at the opposite endpoint

Suppose instead that the Bernstein function has

\[
\phi(0)=a>0.
\tag{26}
\]

For any nonzero completely monotone `g`, its Laplace representation makes `g(a)>0`. Therefore

\[
\boxed{
w_{\phi,g}(0)=a g(a)>0.}
\tag{27}
\]

Such a multiplier does not even enter the zero-degenerate escape. `WP-113` rejects it for the finite-block class, and the correlation-robust covariance theorem `WP-114` rejects fixed multipliers that remain positive at zero much more generally.

Hence the only subordination case worth considering after the low-frequency tests is the conservative case `phi(0)=0`, and that case is closed by the polynomial-tail argument above.

## 6. Matched control: superlinear warping really does cross the boundary

The theorem is not saying that every fixed positive function of the Gamma symbol has polynomial tail. The Bernstein/Markov hypothesis is doing real work.

Take the superlinear transform

\[
\Phi(s)=s^2.
\tag{28}
\]

Then

\[
\widetilde w_\tau(t)
=
H_\infty(t)^2e^{-\tau H_\infty(t)^2}
\tag{29}
\]

is nonnegative and endpoint-degenerate. By (1),

\[
\boxed{
\widetilde w_\tau(t)
=
(\log t+O(1))^2
\exp\!\left[-\tau(\log t+O(1))^2\right],
}
\tag{30}
\]

so for every `N>0`,

\[
t^N\widetilde w_\tau(t)\to0.
\tag{31}
\]

This is exactly the kind of superpolynomial cutoff not covered by `WP-126`.

But `Phi(s)=s^2` is not Bernstein: it is convex, with `Phi''=2>0`, whereas every Bernstein function is concave. Therefore (29) is **not obtained by Bochner subordination of the Gamma Markov process**. Its pointwise nonnegativity still gives an operator-positive spectral form, but the distinguished superlinear warping is an additional choice. A successful Mathia route could in principle force such a transform by some other geometry; the present finding only says that the already canonical Gamma Markov structure does not force it through its natural sign-preserving subordination calculus.

The same distinction applies to compactly supported filters or Gaussian cutoffs in the raw Kronecker frequency. They may be positive spectral multipliers, but they are not generated by positive heat-time mixing of a Bernstein-subordinate logarithmic Gamma generator.

## 7. Matched arithmetic controls and scope

**Off-critical attenuation.** As in `WP-126`, at `sigma>1/2` the wide-shell critical mass driving the finite-block obstruction disappears. The present theorem does not assert that subordinate Gamma forms are intrinsically divergent; it identifies their incompatibility with the exact critical prime amplitude density.

**General correlated completions.** Equation (25) inherits the finite-block hypothesis of `WP-126`. An arbitrary non-block positive completion may suppress the high-support subset coefficients used there. `WP-114` still controls its low-frequency mass, but a zero-degenerate superpolynomial filter on a sufficiently nonlocal correlated completion remains logically open.

**Non-Markov positive calculus.** Any superlinear/non-Bernstein function of `H_infty`, any matrix-valued coupling, or any nonseparable finite--archimedean operation formed before scalarization lies outside the theorem. Such a route must derive its own canonical scale and sign theorem rather than claiming them from Bochner subordination.

**No zero data or RH input.** The argument uses only the unconditional Gamma Markov symbol from `WP-117`, the classical shape theory of Bernstein/completely monotone functions, and the exact finite-block Fourier mass theorem `WP-126`. It does not insert zeta zeros or an RH-equivalent positivity kernel.

## 8. Prior-art and novelty audit

The abstract functional-analysis ingredients are classical and no theorem-level historical novelty is claimed for them.

Bernstein functions, their Lévy--Khintchine representation, complete monotonicity, and Bochner subordination are standard; a canonical reference is René L. Schilling, Renming Song, and Zoran Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), especially the chapters on Bernstein functions and `Subordination and Bochner's functional calculus`, DOI `10.1515/9783110269338`. Schilling's earlier paper *Subordination in the sense of Bochner and a related functional calculus*, J. Austral. Math. Soc. Ser. A 64 (1998), 368--396, is another direct semigroup reference.

A bounded literature audit of Bernstein subordination and subordinate Markov semigroups found the standard theorem that `phi(L)` is the generator of the subordinate semigroup, but no source addressing the Mathia-specific combination used here: the Prime-Circle-selected Riemann Gamma symbol with logarithmic high-frequency growth, exact critical prime-torus first moments, and the `WP-126` finite-block high-support mass explosion. The absence of such a source is not used as a claim of novelty.

The durable branch-local statement is therefore the synthesis

\[
\boxed{
\text{Gamma Markov generator }H_\infty\sim\log t
+\text{ Bernstein subordination}
+\text{ positive heat-scale mixing}
\Longrightarrow
\text{at-best polynomial cutoff}
\xRightarrow{\mathrm{WP\text{-}126}}
\text{critical finite-block divergence}.
}
\tag{32}
\]

## Research consequence

`WP-126` left open the possibility that the intrinsic Gamma sector might itself select a much sharper endpoint-degenerate spectral cutoff after a more sophisticated Markov functional calculus. It cannot do so by subordination. Bernstein concavity prevents the subordinate generator from growing faster than the original logarithmic Gamma scale, while complete-monotone heat mixing cannot decay faster than every exponential in that generator. Their composition is therefore bounded below by a power of the raw Kronecker frequency and is exactly in the class already killed by the finite-block Fourier-mass theorem.

So the surviving positive route must make a more structural move than **"subordinate and smooth the Gamma jump process."** It must either use correlations beyond the finite-block class, introduce a genuinely non-Markov superlinear spectral scale that Mathia forces independently, or couple the finite and archimedean sectors nonseparably before the final positive form is taken.