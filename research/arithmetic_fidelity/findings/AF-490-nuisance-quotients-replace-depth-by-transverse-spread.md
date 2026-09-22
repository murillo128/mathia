# AF-490 — Nuisance quotients replace raw depth by transverse spread

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `NUISANCE-QUOTIENT`, `MINIMAX-RESOLUTION`, `DIRICHLET-SAMPLING`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

The depth resource isolated in AF-487–AF-489 is not invariant under nuisance parameters. In a norm-bounded deterministic channel, an unrestricted nuisance subspace removes exactly the component of the discriminator lying inside that subspace. The sharp recovery scale is therefore controlled by the **quotient norm** of the discriminator, not by its raw norm.

Let `V` be a linear subspace of `R^m`, let `s in R^m`, and observe

\[
z=v-\theta s+u,
\qquad v\in V,
\qquad \|u\|_{\ell_p}\le \rho,
\qquad 1\le p\le\infty.
\]

The scalar `theta` is the target and `v` is an unrestricted nuisance. Define

\[
d_p(s,V):=\inf_{v\in V}\|s-v\|_{\ell_p}.
\]

If `d_p(s,V)>0`, the deterministic minimax worst-case absolute error for estimating `theta` is exactly

\[
\boxed{R_p(\rho;s,V)=\frac{\rho}{d_p(s,V)}}.
\]

If `d_p(s,V)=0`, then `s in V` and `theta` is non-identifiable: every change in the target can be absorbed by the nuisance.

For a single exponential with **unknown positive amplitude**, logarithms make the nuisance space `V=span{1}`. Consequently the relevant sampling resource is

\[
\inf_{c\in\mathbb R}\|s-c\mathbf 1\|_p,
\]

not `||s||_p`. Translating every sample deeper by the same amount leaves this quotient norm unchanged. In the original multiplicative experiment the invariance is stronger: a common shift of all sampling locations can be absorbed exactly into the unknown amplitude. Hence a fixed-width window does **not** become more informative merely by moving to larger absolute depth when amplitude is unrestricted.

This sharpens the interpretation of AF-487–AF-489. Their raw-depth laws are correct for the fixed-known-amplitude family used there. Once amplitude becomes nuisance, the constant direction is quotiented out and only **transverse spread** of the sample positions remains.

## Exact additive quotient theorem

For a datum `z`, define the feasible target set

\[
\Theta(z)
=
\{\theta:\operatorname{dist}_p(z+\theta s,V)\le\rho\}.
\]

Assume first that `d:=d_p(s,V)>0`. If `theta_1,theta_2 in Theta(z)`, choose `v_1,v_2 in V` and residuals `u_1,u_2` with `||u_j||_p<=rho` such that

\[
z=v_j-\theta_j s+u_j.
\]

Subtracting gives

\[
(\theta_1-\theta_2)s-(v_1-v_2)=u_2-u_1.
\]

Taking distance to `V`, using homogeneity of the quotient norm, yields

\[
|\theta_1-\theta_2|d
\le
\|u_2-u_1\|_p
\le 2\rho.
\]

Because `theta -> dist_p(z+theta s,V)` is convex, `Theta(z)` is an interval; because `d>0`, it is bounded. Its midpoint therefore estimates every feasible target with error at most

\[
\frac{\operatorname{diam}\Theta(z)}2
\le
\frac{\rho}{d}.
\]

This proves the upper bound.

For the matching lower bound, finite-dimensionality guarantees a best approximant `v_* in V` with

\[
\|s-v_*\|_p=d.
\]

Set

\[
\delta=\frac{2\rho}{d}.
\]

Take one parameter state with target `theta_0=0` and nuisance `v_0=0`, and another with target `theta_1=delta` and nuisance `v_1=delta v_*`. Their noiseless centers differ by

\[
\delta(v_*-s),
\]

whose norm is exactly `2rho`. The midpoint of those two centers lies in both radius-`rho` noise balls. Thus one observation has two admissible explanations whose targets are separated by `2rho/d`, so every estimator incurs error at least `rho/d` on one of them. Together with the upper bound,

\[
R_p(\rho;s,V)=\frac{\rho}{d_p(s,V)}.
\]

If `d_p(s,V)=0`, then `s in V`; replacing `theta` by `theta+delta` and `v` by `v+delta s` leaves the noiseless datum unchanged. No finite uniform recovery radius exists.

## Dual certificate and optimal linear recovery

Let `p*` be the Hölder-dual exponent. Finite-dimensional quotient duality gives

\[
d_p(s,V)
=
\sup\Big\{|\langle w,s\rangle|:
\|w\|_{p^*}\le1,
\;\langle w,v\rangle=0\ \forall v\in V\Big\}.
\]

Equivalently, among all linear functionals that annihilate the nuisance and are normalized by `⟨w,s⟩=1`,

\[
\inf\|w\|_{p^*}
=
\frac1{d_p(s,V)}.
\]

For such a minimizing `w`, the estimator

\[
\widehat\theta=-\langle w,z\rangle
\]

satisfies

\[
|\widehat\theta-\theta|
=|\langle w,u\rangle|
\le
\rho\|w\|_{p^*}
=
\frac{\rho}{d_p(s,V)}.
\]

So the exact minimax law has a direct fidelity interpretation: **the recoverable part of a discriminator is precisely the part surviving projection to the quotient by nuisance directions**. The primal distance `d_p(s,V)` and the dual annihilating witness `w` are two descriptions of the same surviving information.

## Unknown amplitude in the single-exponential channel

Extend the local family of AF-489 by allowing the moving atom's amplitude to be unknown:

\[
F_{a,q}(s)=G(s)+a q^{-s},
\qquad a>0,
\qquad q>1,
\]

with known `G`. After subtracting `G`, write `theta=log q`, `alpha=log a`, and suppose first that the logarithmic residual channel is additive,

\[
z_k=\alpha-\theta s_k+u_k,
\qquad \|u\|_p\le\rho.
\]

Here `V=span{1}`, hence

\[
R_p
=
\frac{\rho}{d_p(s,\operatorname{span}\{\mathbf1\})}
=
\frac{\rho}{\inf_c\|s-c\mathbf1\|_p}.
\]

For every common shift `t`,

\[
d_p(s+t\mathbf1,\operatorname{span}\{\mathbf1\})
=d_p(s,\operatorname{span}\{\mathbf1\}).
\]

Absolute sampling depth has disappeared from the invariant because it lies in exactly the same direction as the unknown log-amplitude nuisance.

This is not merely an artifact of logarithmic coordinates. In the original noiseless residual channel,

\[
a e^{-\theta(s_k+t)}
=
\bigl(ae^{-\theta t}\bigr)e^{-\theta s_k}.
\]

For unrestricted `a>0`, the map `a -> a e^{-theta t}` is a bijective reparametrization at each target `theta`. A source-relative multiplicative noise class is unchanged by this reparametrization. Therefore translating an entire sampling window by `t` produces an **exactly equivalent statistical experiment** for estimating `theta`. A fixed-width translated window has identical minimax difficulty at every depth.

## Growing-prefix law: the AF-489 exponents survive for a different reason

Let

\[
s_k=s_*+kh,
\qquad k=0,\ldots,N,
\qquad h>0.
\]

The constant `s_*` is annihilated by the amplitude quotient. By symmetry, for every finite `p`, `c=s_*+Nh/2` is a minimizer, so

\[
d_p(s,\operatorname{span}\{\mathbf1\})
=
h\left(\sum_{k=0}^N\left|k-\frac N2\right|^p\right)^{1/p}.
\]

For `1<=p<infinity`,

\[
d_p(s,\operatorname{span}\{\mathbf1\})
\sim
\frac{hN^{1+1/p}}{2(p+1)^{1/p}}.
\]

For `p=infinity`,

\[
d_\infty(s,\operatorname{span}\{\mathbf1\})
=\frac{hN}{2}.
\]

Thus an expanding fixed-step prefix still gives the same coarse powers found in AF-489,

\[
R_{N,p}\asymp N^{-1-1/p}
\quad(1\le p<\infty),
\qquad
R_{N,\infty}\asymp N^{-1},
\]

but their meaning changes. The gain is produced by the **growing span and centered dispersion of the sample locations**, not by moving the whole experiment to large absolute `s`. For finite `p`, sample count also enlarges the centered `ell_p` spread; for `p=infinity`, only half the total span matters.

## Return to bounded multiplicative relative noise

Now observe the residual atom under the AF-489-style source-relative perturbation

\[
y_k-G(s_k)
=a e^{-\theta s_k}(1+\xi_k),
\qquad
\|\xi\|_p\le\varepsilon,
\qquad
0<\varepsilon\le\varepsilon_0<1.
\]

Taking logarithms gives

\[
z_k=\alpha-\theta s_k+\eta_k,
\qquad
\eta_k=\log(1+\xi_k).
\]

Since

\[
|\log(1+x)|\le\frac{|x|}{1-\varepsilon_0},
\]

we have

\[
\|\eta\|_p
\le
\frac{\varepsilon}{1-\varepsilon_0}.
\]

The additive theorem therefore gives

\[
R_{N,p}
\le
\frac{\varepsilon}
{(1-\varepsilon_0)d_p(s,\operatorname{span}\{\mathbf1\})}.
\]

A matching lower bound follows from a two-point construction. Let `c_*` minimize `||s-c1||_p` and put

\[
r=\delta(c_*\mathbf1-s),
\qquad
\delta=
\frac{\varepsilon}{d_p(s,\operatorname{span}\{\mathbf1\})}.
\]

Choose two interior target values separated by `delta` and shift their log-amplitudes by `delta c_*`. Their noiseless log-signals differ by `r`. The coordinatewise geometric midpoint is a common observation with relative perturbations

\[
\xi^{(0)}=e^{r/2}-1,
\qquad
\xi^{(1)}=e^{-r/2}-1.
\]

Because `||r||_infinity<=||r||_p=epsilon<1`,

\[
\|e^{\pm r/2}-1\|_p
\le
\frac{e^{1/2}}2\|r\|_p
<\varepsilon.
\]

Hence both explanations are admissible and every estimator has worst-case error at least

\[
\frac{\varepsilon}
{2d_p(s,\operatorname{span}\{\mathbf1\})}.
\]

Therefore, uniformly for `epsilon<=epsilon_0<1`,

\[
\boxed{
R_{N,p}
=\Theta_{\varepsilon_0}\!\left(
\frac{\varepsilon}
{d_p(s,\operatorname{span}\{\mathbf1\})}
\right).}
\]

The multiplicative-noise constants are not claimed to be exact. The common-shift invariance of the unrestricted-amplitude experiment, however, is exact.

## Falsification and boundary audit

- The exact minimax identity is an additive finite-dimensional theorem. The multiplicative relative-noise statement is only a constant-factor local equivalence obtained through logarithms and a two-point construction.
- The amplitude must be unrestricted and positive for exact translation equivalence. Bounds or priors on `a` can make absolute depth informative again by preventing arbitrary absorption of a common shift.
- The result does not say that nuisance always destroys depth. It destroys exactly the component of `s` lying in the nuisance subspace; extra structure can restore that direction.
- A known amplitude corresponds to `V={0}` and recovers the raw norm `d_p(s,{0})=||s||_p`, so AF-489 is the zero-nuisance special case rather than a contradiction.
- Multiple nuisance parameters replace `span{1}` by their full sample-space nuisance subspace. The theorem then measures only the discriminator component transverse to all of them.
- The theorem is deterministic minimax. Stochastic priors, random errors, Bayesian restrictions, or probabilistic coupling can alter the optimal risk.
- Recovering `theta` remains distinct from proving arithmetic provenance. A rational-prime mark or another discrete discriminator would still need to survive the same quotient/compression.

## Prior-art and novelty audit

The general ingredients are classical. No broad novelty is claimed for the quotient-norm theorem itself.

- Distance to a subspace and its dual characterization by annihilating functionals are standard finite-dimensional Hahn–Banach / quotient-space duality.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`, gives the classical optimal-recovery/minimax viewpoint in which indistinguishable nearby objects determine worst-case estimation difficulty.
- Amir Beck and Yonina C. Eldar, **“Regularization in Regression with Bounded Noise: A Chebyshev Center Approach,”** *SIAM Journal on Matrix Analysis and Applications* 29(2), 606–625 (2007), DOI `10.1137/060656784`, treats worst-case regression under norm-bounded noise through feasible-set geometry.
- Unknown-intercept regression and nuisance elimination are classical special cases of quotienting a parameterized signal by an unobserved linear direction.

The Arithmetic Fidelity contribution is the structural specialization and interpretation across AF-487–AF-489: **a resource visible before compression can cease to be a resource after quotienting by nuisance symmetry**. In the unknown-amplitude Dirichlet atom, absolute depth is exactly such a false resource; centered spread is the invariant that actually survives. This supplies a concrete theorem-level instance of the line's central question—what properties survive compression, and what mathematical object measures the surviving discriminator.

## Relationship to AF-487–AF-489

AF-487 established the critical single-window resolution law for a fixed known amplitude. AF-488 showed that pointwise critical relative noise makes earlier history unable to improve the horizon order. AF-489 showed that a fixed global `ell_p` budget can make accumulated samples useful, with raw sensitivity `||s||_p`.

AF-490 identifies a previously hidden boundary shared by all three: those depth statements use a known amplitude as an anchor. If amplitude is promoted to an unrestricted nuisance, the anchor disappears and the correct sensitivity is the quotient norm

\[
\|[s]\|_{\ell_p/V}
=d_p(s,V).
\]

For the one-amplitude model, `V=span{1}`. The expanding-prefix exponents of AF-489 survive only because the sample **spread** grows with `N`; a pure translation to larger depth contributes nothing. The broader lesson is that fidelity resources should be evaluated only after quotienting by the nuisance symmetries of the actual observation model.