# VIS-056 — Wasserstein class-law drift controls Fisher balance under support motion

## Claim

Assume the nondegenerate exact two-ratio Fisher geometry of `VIS-050`, with fixed baseline cosine `kappa` satisfying `0<|kappa|<1`. Along one declared real log-gauge coordinate, the two normalized ratio classes induce probability laws `alpha` and `beta` for the gauge value `h`. Assume both laws are supported in a common interval `[-H,H]`, and write

`M_alpha(s)=integral exp(s x) d alpha(x)`,
`M_beta(s)=integral exp(s x) d beta(x)`,

`D(s)=M_alpha(s)-M_beta(s)`,
`q(s)=log M_alpha(s)-log M_beta(s)`.

As in `VIS-050` and `VIS-052`, the exact Fisher cosine is

`A(s)=F(q(s))`,

where

`F(q)=kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)`,

and exact balance returns are precisely the real zeros of `D`.

Now replace only the two normalized classwise `h`-value laws by arbitrary probability laws `alpha_tilde,beta_tilde` on the same interval `[-H,H]`, while retaining the same outer two-ratio Fisher geometry and the same `kappa`. This perturbation may move, split, merge, or reweight atoms inside either class; it does not require the two laws to have the same finite support. Put

`epsilon = W_1(alpha,alpha_tilde) + W_1(beta,beta_tilde)`

for Wasserstein-1 distance with the ordinary metric on the `h` axis, and define `D_tilde,q_tilde,A_tilde` analogously. Then for every real `s`,

`|D_tilde(s)-D(s)| <= |s| exp(|s| H) epsilon`,

`|D_tilde'(s)-D'(s)| <= exp(|s| H)(1+|s|H) epsilon`,

and

`|q_tilde(s)-q(s)| <= |s| exp(2|s|H) epsilon`.

The outer Fisher map is globally Lipschitz in the hidden contrast coordinate, with the exact uniform bound

`sup_q |F'(q)| = (1-kappa^2)/(3 sqrt(3))`.

Consequently,

`|A_tilde(s)-A(s)|
 <= [(1-kappa^2)/(3 sqrt(3))]
    |s| exp(2|s|H) epsilon`.

On a fixed window `|s|<=S`, these become uniform deterministic certificates. In particular, if an exact balance return `s_0` is simple and on

`I=[s_0-rho,s_0+rho] subset [-S,S]`

one has `|D'(s)|>=gamma>0`, then the perturbed balance equation has exactly one zero `s_tilde` in `I` whenever

`S exp(SH) epsilon < gamma rho`,

`exp(SH)(1+SH) epsilon < gamma`.

Moreover,

`|s_tilde-s_0| <= S exp(SH) epsilon / gamma`.

Thus the fixed-atom coefficient perturbation bound in `VIS-054` extends to a support-moving metric control: **Wasserstein-small class-law drift gives explicit `C^1` control of the signed Fisher balance equation and therefore linear stability of simple remote returns.**

**Evidence/status:** `EXACT-DERIVED + KANTOROVICH-RUBINSTEIN + REPRESENTATION CONTROL + SUPPORT-DRIFT STABILITY + NO-NOVELTY-CLAIM`.

No novelty is claimed for Kantorovich-Rubinstein duality, Wasserstein stability of expectations of Lipschitz functions, moment-generating functions, or simple-root perturbation theory. No claim is made that empirical zeta/CUE residuals obey the exact two-ratio model, that their sampling error is Wasserstein-small at a stated rate, or that changes of the ratio partition, residual tensors, baseline `kappa`, or closure construction are covered by `epsilon`.

## 1. Wasserstein distance controls the two class moment sums

For fixed real `s`, consider the test function

`f_s(x)=exp(sx)`

on `[-H,H]`. Its Lipschitz constant satisfies

`Lip(f_s) <= |s| exp(|s|H)`.

Kantorovich-Rubinstein duality therefore gives

`|M_alpha_tilde(s)-M_alpha(s)|
 <= |s| exp(|s|H) W_1(alpha,alpha_tilde)`,

and the analogous inequality for `beta`. Subtracting the two class moment sums yields

`|D_tilde(s)-D(s)| <= |s| exp(|s|H) epsilon`.

This is the key distinction from the coefficientwise bound in `VIS-054`. There the atom locations `a_j` were fixed and only their signed masses changed. Here the class laws may have different supports: a small displacement of mass is charged by how far it moves along the declared gauge axis rather than being treated as a complete coefficient replacement.

Because all four laws are probabilities, `M_alpha(0)=M_beta(0)=M_alpha_tilde(0)=M_beta_tilde(0)=1`. The compulsory baseline balance at `s=0` therefore survives exactly under this class-law perturbation.

## 2. The signed balance equation has uniform `C^1` control

Differentiate the class moment sums. The relevant test function becomes

`g_s(x)=x exp(sx)`.

Its derivative with respect to `x` is

`g_s'(x)=exp(sx)(1+s x)`,

hence on `[-H,H]`

`Lip(g_s) <= exp(|s|H)(1+|s|H)`.

A second application of Kantorovich-Rubinstein duality gives

`|D_tilde'(s)-D'(s)|
 <= exp(|s|H)(1+|s|H) epsilon`.

Therefore on `|s|<=S`,

`||D_tilde-D||_infinity <= S exp(SH) epsilon`,

`||D_tilde'-D'||_infinity <= exp(SH)(1+SH) epsilon`.

These are deterministic bounds. They require no coupling between the two classes and no matching of individual atoms; the optimal transport inside each class supplies the comparison.

## 3. The hidden contrast and rendered Fisher angle are also stable

Every moment sum for a probability law supported in `[-H,H]` obeys

`M(s) >= exp(-|s|H)`.

For positive `a,b`, the mean-value theorem for the logarithm gives

`|log a-log b| <= |a-b|/min(a,b)`.

Combining this with the moment-sum estimate gives, class by class,

`|log M_tilde(s)-log M(s)|
 <= |s| exp(2|s|H) W_1`,

and hence

`|q_tilde(s)-q(s)| <= |s| exp(2|s|H) epsilon`.

It remains to propagate this through the exact outer Fisher representation. With `k=|kappa|`, direct differentiation of `F` gives

`|F'(q)|
 = [k(1-k^2)/2]
   |sinh(q/2)|
   / [1+k^2 sinh(q/2)^2]^(3/2)`.

Writing `x=|sinh(q/2)|`, the elementary function

`x/(1+k^2 x^2)^(3/2)`

has its maximum at `x=1/(sqrt(2)k)`, where its value is `2/(3 sqrt(3) k)`. Therefore

`sup_q |F'(q)|=(1-kappa^2)/(3 sqrt(3))`.

The displayed Fisher-angle bound follows immediately. This does not remove the balance and saturation conditioning identified in `VIS-054` and `VIS-055`; it only gives a forward error certificate from class-law motion to the rendered scalar.

## 4. Simple balance returns survive small support drift

Let `s_0` be a simple zero of `D` and suppose `|D'|>=gamma>0` throughout `I=[s_0-rho,s_0+rho]`. `VIS-054` proves the elementary `C^1` stability lemma: if a perturbation `E=D_tilde-D` satisfies

`||E||_infinity < gamma rho`,
`||E'||_infinity < gamma`,

then `D_tilde` is strictly monotone on `I`, keeps opposite signs at the endpoints, has exactly one zero there, and that zero moves by at most `||E||_infinity/gamma`.

Substituting the Wasserstein bounds above gives the stated sufficient conditions and displacement estimate. For the compulsory baseline root `s_0=0`, the perturbed root is already pinned exactly at zero because the class laws remain probabilities. The displacement certificate is most informative for remote simple returns.

Multiple roots remain qualitatively unstable exactly as in `VIS-054`; Wasserstein control does not repair the classical bifurcation problem of a multiple real zero.

## 5. Prior art and novelty boundary

The only transport theorem used here is classical Kantorovich-Rubinstein duality: Wasserstein-1 distance controls the change in expectation of every Lipschitz test function by its Lipschitz constant. A standard authority is Cédric Villani, **Optimal Transport: Old and New**, Grundlehren der mathematischen Wissenschaften 338, Springer, 2009, DOI `10.1007/978-3-540-71050-9`.

Applying that theorem to `exp(sx)` and `x exp(sx)` on a compact interval is immediate. The logarithmic and Fisher-angle bounds are then elementary calculus, while the root-stability step is the already-persisted `VIS-054` argument. The result should therefore be read as a Mathia-specific representation certificate, not as a new optimal-transport theorem.

The closest internal boundary is `VIS-054`: its coefficient-law estimate is sharper when the gauge atoms are fixed, whereas the present Wasserstein estimate is designed specifically to remain meaningful when the atom locations or finite support move. These are complementary perturbation models rather than independent confirmations of the same empirical claim.

## 6. Boundary conditions and falsification

The compact support bound `[-H,H]` is essential to the uniform exponential Lipschitz constants. Unbounded class laws require exponential-moment/tail assumptions and a different estimate.

More importantly, `epsilon` measures only drift of the two **normalized classwise gauge-value laws after the reciprocal two-ratio geometry has been fixed**. It does not cover changing which cells belong to `P` and `M`, changing the residual tensors, changing their ratio geometry, changing the baseline `kappa`, or recomputing a closure/statistic after perturbation. Those effects can alter the outer map `F` itself and need a separate model-error term before the Fisher-angle inequality can be applied to empirical data.

Likewise, an empirical statement such as `W_1<=epsilon` needs its own sampling/concentration justification. The theorem is deterministic conditional on such a bound and does not provide a statistical confidence interval.

Falsify the result by giving probability laws on `[-H,H]` that violate either Wasserstein moment bound; by violating the derivative bound for `x exp(sx)`; by finding a same-outer-geometry pair whose Fisher curves exceed the propagated global Lipschitz bound; or by producing a simple balance return satisfying the stated margins whose perturbed return fails the `C^1` existence, uniqueness, or displacement conclusion.

## Research consequence

The signed coordinate advocated by `VIS-055` now has a natural support-moving robustness metric. For a frozen empirical construction that can justify the same two-ratio partition and a bounded gauge axis, one need not require identical bin centers or identical finite supports to compare balance geometry: it is enough to control the two class laws in `W_1`.

The next independent step is not another exact identity on the two-ratio model. It is an empirical/model-error question: freeze a concrete residual construction, separate class-law transport error from partition/closure error, and determine whether the latter is small enough that the exact Fisher representation remains a useful approximation. That question should be handled in a later invocation rather than folded into this exact support-drift result.