# PC-167 — full refinement homotheties rigidify singular local metrics to universal power laws

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for obtaining a new Prime-Circle/RH mechanism by relaxing PC-166's regularity at the unit circle while keeping a local Riemannian metric intrinsically compatible with the full power-refinement semigroup. The full semigroup removes the log-periodic freedom left by any single discrete scale: on either side of the unit circle every continuous positive-definite metric for which all power maps are homotheties is a universal scalar power of log-radius times one constant matrix. The only regular member is the flat-cylinder metric of PC-166; the singular members add a freely chosen scaling exponent but no primitive-shell arithmetic or new angular geometry.

PC-166 deliberately left a sharp boundary. For a single refinement `z -> z^2`, dropping continuity across the unit circle allows singular or log-periodic self-similar metrics away from that circle. Because the original Prime-Circle construction contains **all** power refinements rather than one preferred scale, the natural next test is whether those singular self-similar degrees of freedom survive simultaneous compatibility with the full semigroup. They do not.

## 1. Full power homothety on one side of the root circle

Work first on either connected component of the punctured plane cut along the unit circle. Put

\[
t=|\log |z||>0,
\qquad
z=\exp(\pm t+i\theta),
\qquad
\theta\in\mathbb R/2\pi\mathbb Z,
\tag{1}
\]

where the sign distinguishes exterior and interior. Every power map

\[
p_n(z)=z^n
\]

acts in these coordinates by

\[
D_n(t,\theta)=(nt,n\theta),
\qquad n\ge2.
\tag{2}
\]

Let `g` be a continuous positive-definite Riemannian metric on this open half-cylinder. No rotational invariance, conformality, diagonal form, or extension to `t=0` is assumed. Write

\[
g=
\begin{pmatrix}dt&d\theta\end{pmatrix}
G(t,\theta)
\begin{pmatrix}dt\\d\theta\end{pmatrix},
\qquad
G(t,\theta+2\pi)=G(t,\theta),
\tag{3}
\]

with `G` continuous, symmetric, and positive definite.

Assume only that **every intrinsic Prime-Circle power refinement is a Riemannian homothety**: for each `n>=2` there is a constant `rho_n>0` such that

\[
D_n^*g=\rho_n^2 g.
\tag{4}
\]

Since `dD_n=nI`, equation (4) is exactly

\[
\boxed{
G(nt,n\theta)=a_nG(t,\theta),
\qquad
a_n:=\frac{\rho_n^2}{n^2}>0.
}
\tag{5}
\]

Composition `D_mD_n=D_{mn}` gives

\[
\rho_{mn}=\rho_m\rho_n,
\qquad
a_{mn}=a_ma_n.
\tag{6}
\]

Thus the homothety factors form a positive multiplicative character before any spectral interpretation is introduced.

## 2. Continuity and rational refinement force a single power exponent

Average the matrix over the angular fiber,

\[
M(t)=\frac1{2\pi}\int_0^{2\pi}G(t,\theta)\,d\theta,
\qquad
h(t)=\operatorname{tr}M(t)>0.
\tag{7}
\]

Because multiplication by `n` preserves normalized Haar measure on the circle, (5) implies

\[
M(nt)=a_nM(t),
\qquad
h(nt)=a_nh(t).
\tag{8}
\]

For positive integers `m,n`, applying (8) first at `t/n` and then at `m(t/n)` gives

\[
h\!\left(\frac mn t\right)
=\frac{a_m}{a_n}h(t).
\tag{9}
\]

Hence the ratio is well defined for every positive rational `q=m/n`. Put

\[
H(x)=\log h(e^x).
\]

Then on the dense additive subgroup `log Q_{>0}`,

\[
H(x+\log q)-H(x)=\log a_q,
\tag{10}
\]

and the right side is independent of `x`. Continuity of `H` makes this additive increment continuous on the dense subgroup, so it extends to a continuous additive function on `R`. Therefore there is a real number `kappa` such that

\[
\log a_q=\kappa\log q,
\qquad
q\in\mathbb Q_{>0}.
\tag{11}
\]

In particular

\[
\boxed{
a_n=n^\kappa,
\qquad
\rho_n=n^{1+\kappa/2}.
}
\tag{12}
\]

The full refinement semigroup has therefore already promoted the arbitrary completely multiplicative homothety data to an ordinary real power law. There is no prime-dependent freedom in the factors: primes only generate the same continuous scaling exponent `kappa`.

## 3. The covering branches remove all angular and log-periodic modulation

Normalize away the forced power law,

\[
F(t,\theta)=t^{-\kappa}G(t,\theta).
\tag{13}
\]

Equations (5) and (12) become exact invariance

\[
\boxed{F(nt,n\theta)=F(t,\theta)}
\qquad(n\ge2).
\tag{14}
\]

The crucial extra information relative to a one-scale self-similarity equation is that every point has all `n` angular preimages. For every `j=0,...,n-1`,

\[
F(t,\theta)
=
F\!\left(\frac tn,\frac{\theta+2\pi j}{n}\right).
\tag{15}
\]

Applying `D_m` to that preimage gives the exact rational-refinement relation

\[
\boxed{
F(t,\theta)
=
F\!\left(
\frac mn t,
\frac mn(\theta+2\pi j)
\right).
}
\tag{16}
\]

Fix `t,theta` and any target angle `phi`. Choose `m=n+1` and choose `j_n` so that the grid point `2pi j_n/n` approaches `phi-theta` modulo `2pi`. Modulo one angular period, the second coordinate on the right of (16) is

\[
\theta+\frac\theta n+\frac{2\pi j_n}{n},
\]

while its radial coordinate is `(1+1/n)t`. Both converge to `(t,phi)`. Continuity and (16) therefore yield

\[
F(t,\phi)=F(t,\theta).
\tag{17}
\]

So `F` is angle-independent. Write it as `F_0(t)`. Equation (14), its inverse branches, and finite compositions then give

\[
F_0(qt)=F_0(t)
\qquad(q\in\mathbb Q_{>0}).
\tag{18}
\]

Positive rational scalings are dense in `R_{>0}`, and continuity now forces `F_0` to be constant. Consequently

\[
\boxed{
G(t,\theta)=t^\kappa G_0
}
\tag{19}
\]

for one constant symmetric positive-definite matrix `G_0`.

This is the exact rigidity statement. It uses no rotational hypothesis: angular uniformity is **derived** from the complete family of power-map covering branches. It also kills the log-periodic escape explicitly left by PC-166. A single equation such as `f(2t)=2^kappa f(t)` permits the standard power law times an arbitrary `log 2`-periodic modulation. Simultaneous Prime-Circle refinement at all integer scales removes the preferred logarithmic period and leaves only the power law.

If one metric is defined on both sides of the unit circle and the same global homothety constants `rho_n` apply, both components have the same exponent `kappa`; their constant matrices may differ until an additional boundary or inversion condition relates them.

## 4. PC-166 is exactly the unique regular member

Equation (19) classifies not only the singular escape but also its regular boundary. If `g` extends continuously and positively across the original unit circle `t=0`, then positive definiteness of the limiting metric excludes both degeneration (`kappa>0`) and blow-up (`kappa<0`). Hence

\[
\boxed{\kappa=0.}
\tag{20}
\]

After matching the two sides, (19) becomes precisely the constant logarithmic-cylinder metric of PC-166. Its homothety factors are then

\[
\rho_n=n.
\tag{21}
\]

Conversely every `kappa != 0` member is singular at the very locus on which the Prime-Circle vertices live. The only extra local degree of freedom obtained by abandoning regularity is therefore a **scalar radial power**. There is no new angular tensor, no shell-dependent local coefficient, and no preferred prime scale.

This also gives a matched boundary control. On a cutoff circle `t=epsilon`, the induced tangential metric is merely

\[
g_{\theta\theta}(\epsilon)=\epsilon^\kappa (G_0)_{\theta\theta}.
\tag{22}
\]

After removing the common divergent or vanishing scalar, the angular metric is the ordinary flat circle. Every root shell therefore has exactly the same normalized local angular geometry it had before the singular metric was introduced. A boundary renormalization cannot recover primitive/new-vertex information from (19) because that information never entered the metric coefficients.

As another stress test, demanding that all `D_n` be isometries simply selects `rho_n=1`, hence `kappa=-2` from (12). This is a special **universal scaling normalization**, not a prime-derived exponent. More generally every prescribed power-law homothety character selects one real `kappa`; the Prime-Circle root data themselves do not choose among them once regularity has been abandoned.

## 5. The associated local differential operator remains prime-blind

The two-dimensional form (19) makes the operator boundary especially transparent. Write

\[
G_0^{-1}=
\begin{pmatrix}
\alpha&\beta\\
\beta&\gamma
\end{pmatrix},
\qquad
\alpha>0,
\qquad
\alpha\gamma-\beta^2>0.
\tag{23}
\]

Because the dimension is two,

\[
\sqrt{\det g}\,g^{-1}
=\sqrt{\det G_0}\,G_0^{-1}
\]

is constant. Up to the usual overall sign convention, the Laplace--Beltrami operator is therefore

\[
\boxed{
\Delta_g
=t^{-\kappa}
\left(
\alpha\,\partial_t^2
+2\beta\,\partial_t\partial_\theta
+\gamma\,\partial_\theta^2
\right).
}
\tag{24}
\]

The angular coordinate still separates into the ordinary integer Fourier modes. The local coefficients contain neither exact order, `phi(n)`, `Lambda(n)`, Ramanujan sums, cyclotomic resultants, nor old/new incidence. Any spectral distinction obtained by choosing a domain, a boundary condition, or one value of `kappa` is therefore not yet a Prime-Circle arithmetic mechanism; those choices would have to be derived separately from the root geometry and survive a matched control.

Indeed, erase the primitive-shell labels entirely but keep the same circle and the same power maps. Equations (1)--(24) are unchanged. This is a decisive matched-control failure for the proposed local-metric repair: its complete invariant content is already present in the prime-blind refinement semigroup.

The conclusion is intentionally narrower than a statement about every singular differential operator. A shell-dependent singular potential, nonlocal boundary operator, or domain condition derived independently from actual old/new root incidence is outside (4) and is not ruled out here. What is ruled out is the idea that **the full power-refinement homothety of a local metric itself** can supply the missing arithmetic coupling.

## 6. Prior-art and novelty audit

The classical ingredients are separated from the Prime-Circle conclusion.

- Continuous scale invariance leading to power laws, and one preferred discrete scaling ratio allowing log-periodic modulation, are standard. Didier Sornette's review, *Discrete scale invariance and complex dimensions*, Physics Reports 297:5 (1998), 239--270, DOI `10.1016/S0370-1573(97)00076-8`, is a direct prior-art anchor for that distinction. PC-166's one-map log-periodic boundary is therefore a standard discrete-scale phenomenon rather than a new arithmetic signal.
- The step from (10) to (12) is the elementary continuous Cauchy/exponential functional-equation mechanism on the dense subgroup `log Q_{>0}`. No novelty is claimed for power-law rigidity under dense scale invariance.
- Riemannian homotheties and constant-coefficient metrics in logarithmic coordinates are classical differential geometry. PC-166 already classified the regular Prime-Circle member.
- The angular-rigidity step (15)--(19) uses the specific complete family of circle covering maps carried by the Prime-Circle refinement system, but it is an elementary consequence of their dense rational preimage grids. Targeted searches for self-similar/homothetic metrics, discrete scale invariance, and power-map metrics did not locate an RH mechanism attached to this construction. Absence of a wording match is not treated as novelty evidence.

No historical novelty is claimed for scale invariance, power laws, log-periodicity, or homothetic metrics. The durable contribution is the line-specific no-go: **once all intrinsic power refinements are imposed simultaneously, dropping regularity at the unit circle does not open a hidden local two-dimensional metric family; it opens only the universal scalar exponent `kappa`.**

This is also distinct from Bost--Connes/cyclotomic dynamics. Those frameworks attach arithmetic structure to the action and its state/representation theory. Here the metric classification uses only the naked power maps, and the matched-control calculation shows exactly why no such arithmetic data are generated by local homothety alone.

## 7. Scope, falsifiers, and surviving frontier

The assumptions that carry the theorem are explicit and falsifiable:

1. the metric is local Riemannian data on one or both open sides of the unit circle;
2. it is continuous and positive definite there, though it may be singular at the unit circle itself;
3. every power refinement acts by a global Riemannian homothety with a position-independent factor.

Removing any of these assumptions can create a larger class, but it also introduces genuinely new structure. In particular, the result does **not** rule out shell-dependent or anchor-dependent nonlocal operators, old/new couplings inserted before a local metric compression, geometry-forced singular potentials or domains that are not homothety metrics, growing-level or renormalized cross-level operators, or the global uniformization/monodromy branch retained by PC-017. It also does not claim that an arbitrarily chosen member of (19) has a particular spectral type; the no-go is that its local coefficients and scaling character are universal and prime-blind.

What it does rule out is the natural singular continuation of the PC-166 route:

\[
\text{full power refinement}
\longrightarrow
\text{singular self-similar local metric}
\longrightarrow
\text{new prime-sensitive 2D operator}
\longrightarrow
\text{RH}.
\]

Within the homothety class, the second arrow has already collapsed to `t^kappa G_0`. The only regular choice is PC-166's flat logarithmic cylinder, while every singular choice substitutes a free scale exponent for regularity without recovering any primitive-shell information.
