# XF-021 — centered convex gap entropies have collision-positive compact-boundary spikes

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `STRUCTURAL/BOUNDARY`. XF-018--XF-020 moved the broad-buffer program away from the singular centered quadratic carrier by localizing the uncentered gap square and delaying removal of the neutral mean/span mode. There is a general reason this carrier change is necessary. For the exact positive-conductance gap diffusion of XF-014, any differentiable convex **single-gap entropy** that genuinely penalizes compression below a positive reference spacing develops an arbitrarily large *positive* boundary flux under compact localization when the first exterior gap approaches a collision.

More precisely, let `Phi:(0,infinity)->R` be differentiable and convex, and suppose `Phi'(h)=0` for some reference spacing `h>0`. Let `alpha_i>=0` be finitely supported localization weights. If `Phi` is sensitive to compressed gaps, in the precise sense that `Phi'(a)<0` for some `0<a<h`, then at any right support edge `r` with `alpha_r>0` and `alpha_{r+1}=0` one can hold every other local gap fixed, set `g_r=a`, and let the exterior adjacent gap `g_{r+1}=epsilon` tend to zero. The localized entropy derivative then satisfies

\[
\boxed{E_\alpha'(t)\to+\infty\qquad(\epsilon\downarrow0).}
\]

Conversely, if this positive collision spike is to be excluded for every compressed boundary value using convexity alone, then `Phi'(a)=0` for every `0<a<h`, so `Phi` is constant on `(0,h)` and is blind to precisely the gap compression that a collision-preventing entropy must detect.

Thus a compactly localized convex entropy cannot simultaneously be **centered at a positive lattice spacing, compression-sensitive, and collision-safe from above** using only the universal ordered gap-diffusion structure. This is not a statement that Xi actually realizes the adversarial boundary geometry. It is a no-go for source-free convex-entropy closure: a successful Xi argument must add exterior gap information, abandon compact single-site centering, or use a nonlocal/signed organization such as the uncentered cross-ratio carrier of XF-018.

## 1. General weighted convex-entropy identity

On every real-simple Xi slice covered by XF-014,

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=c_{ki}>0.
\tag{1}
\]

Let `alpha=(alpha_i)` be a finitely supported nonnegative weight sequence and define

\[
E_\alpha:=\sum_i\alpha_i\Phi(g_i).
\tag{2}
\]

Absolute convergence of the pointwise gap equation from XF-014 justifies differentiating the finite sum. Pairing `(i,k)` and `(k,i)` gives the exact identity

\[
\boxed{
E_\alpha'
=2\sum_{i<k}c_{ik}(g_k-g_i)
\bigl(\alpha_i\Phi'(g_i)-\alpha_k\Phi'(g_k)\bigr).
}
\tag{3}
\]

If `alpha_i=alpha_k`, the pair contribution is

\[
-2\alpha_i c_{ik}(g_i-g_k)
\bigl(\Phi'(g_i)-\Phi'(g_k)\bigr)\le0
\tag{4}
\]

by convexity. Equation (4) is the usual internal entropy dissipation of XF-014. All sign trouble is therefore introduced by localization, through pairs on which the weights differ.

The hard-block formula of XF-014 is the special case `alpha_i=1` on a finite interval and zero outside. Smooth compact tapers are included as well by taking `alpha_i=psi_i^2`.

## 2. The adjacent support edge has an exact `1/epsilon` positive spike

Because `alpha` has finite support, any nonzero localization has an extreme right index `r` with

\[
\alpha_r>0,
\qquad
\alpha_{r+1}=0.
\tag{5}
\]

For adjacent gaps the exact conductance is

\[
\boxed{c_{r,r+1}=\frac1{g_r g_{r+1}}.}
\tag{6}
\]

Fix a compressed boundary value `a>0` and set

\[
g_r=a,
\qquad
g_{r+1}=\epsilon>0.
\tag{7}
\]

The single pair `(r,r+1)` contributes to (3)

\[
\begin{aligned}
B_{r,r+1}(\epsilon)
&=2\frac{\epsilon-a}{a\epsilon}
\alpha_r\Phi'(a)\\
&=2\alpha_r\Phi'(a)
\left(\frac1a-\frac1\epsilon\right).
\end{aligned}
\tag{8}
\]

Therefore, whenever

\[
\Phi'(a)<0,
\tag{9}
\]

one has the exact asymptotic

\[
\boxed{
B_{r,r+1}(\epsilon)
=\frac{2\alpha_r|\Phi'(a)|}{\epsilon}+O(1)
\longrightarrow +\infty.
}
\tag{10}
\]

This is the dangerous sign: the boundary contribution is not merely uncontrolled in absolute value; it can overwhelm the negative internal entropy production in the direction that destroys an upper Lyapunov estimate.

The singularity is genuinely localized to the adjacent crossing pair. Hold all other gaps in a fixed positive configuration while `epsilon->0`. Every term of (3) except `(r,r+1)` stays bounded: any other denominator contains at least one fixed positive intervening span. Hence

\[
\boxed{E_\alpha'=\frac{2\alpha_r|\Phi'(a)|}{\epsilon}+O(1)\to+\infty.}
\tag{11}
\]

No cancellation from the remaining bulk or far exterior can remove this leading term without adding information beyond the universal positive-conductance identity.

## 3. Convex centering gives an exact dichotomy

Suppose now that the entropy is centered at a positive reference spacing `h`:

\[
\Phi'(h)=0.
\tag{12}
\]

For a differentiable convex function, `Phi'` is nondecreasing. Thus for every `0<a<h`,

\[
\Phi'(a)\le0.
\tag{13}
\]

There are only two possibilities.

If `Phi'(a)<0` for at least one `a<h`, then choosing that value at the compact support edge gives the positive collision spike (11).

If no such `a` exists, then (13) forces

\[
\Phi'(a)=0
\qquad(0<a<h),
\tag{14}
\]

and consequently

\[
\boxed{\Phi\text{ is constant on }(0,h).}
\tag{15}
\]

Such an entropy assigns no increasing cost at all as a gap is compressed from `h` toward zero. It therefore cannot serve as a coercive detector of the approach to collision on the compressed side.

This yields the obstruction in a compact form:

\[
\boxed{
\begin{array}{c}
\text{convex + centered at }h>0+\text{ compact localization}\\[1mm]
\Longrightarrow\\[1mm]
\text{either compression blindness below }h\\
\text{or an arbitrarily positive adjacent-collision boundary flux.}
\end{array}}
\tag{16}
\]

The theorem is one-sided in exactly the way a Lyapunov argument needs. A large *negative* boundary spike would only help an estimate of the form `E'<=0`; the obstruction is that every compression-sensitive centered convex entropy necessarily admits the opposite sign.

## 4. Weighted-mean centering retains the obstruction for two broad explicit classes

The fixed-reference theorem above does **not** by itself imply the same statement for an arbitrary family whose center moves with the weighted mean. If

\[
\mu_\alpha
=\frac{\sum_i\alpha_i g_i}{A},
\qquad
A:=\sum_i\alpha_i,
\tag{17}
\]

then differentiating an energy whose profile depends on `mu_alpha` produces an additional `mu_alpha'` term, and `mu_alpha'` can itself be of order `1/epsilon` in the boundary test. That term must be included rather than discarded. Two natural centered classes nevertheless retain the same positive collision obstruction exactly.

First consider a translation-centered profile

\[
\Phi_h(g)=\varphi(g-h),
\qquad
\varphi\in C^1\text{ convex},
\qquad
\varphi'(0)=0,
\tag{18}
\]

and set

\[
p_i:=\varphi'(g_i-\mu_\alpha),
\qquad
\bar p:=\frac1A\sum_i\alpha_i p_i.
\tag{19}
\]

Choose the right support-edge gap `g_r=a`, hold all other supported gaps fixed, and let the first exterior gap `g_{r+1}=epsilon` tend to zero. From the exact conductance equation, the only singular supported-gap derivative is

\[
g_r'=-\frac{2}{\epsilon}+O(1),
\qquad
g_i'=O(1)\quad(i\ne r,\ \alpha_i>0),
\tag{20}
\]

so

\[
\mu_\alpha'=-\frac{2\alpha_r}{A\epsilon}+O(1).
\tag{21}
\]

For

\[
E_\alpha=\sum_i\alpha_i\varphi(g_i-\mu_\alpha),
\]

exact differentiation therefore yields

\[
\boxed{
E_\alpha'
=\frac{2\alpha_r}{\epsilon}(\bar p-p_r)+O(1).
}
\tag{22}
\]

Thus the precise sign criterion is `bar p>p_r`. In particular, choose `g_r=a` as the smallest supported gap and choose every other supported gap larger than `mu_alpha`. If the compressed boundary value is genuinely detected so that

\[
p_r=\varphi'(a-\mu_\alpha)<0,
\tag{23}
\]

then convexity and `varphi'(0)=0` give `p_i>=0>p_r` on the other supported gaps, hence `bar p-p_r>0`; the positive `1/epsilon` spike survives the moving-center correction.

Second, let `f` be twice differentiable and convex and use the Bregman-centered profile

\[
\Phi_h(g)
=f(g)-f(h)-f'(h)(g-h).
\tag{24}
\]

Here

\[
\partial_h\Phi_h(g)=-f''(h)(g-h),
\tag{25}
\]

so at `h=mu_alpha` the entire moving-center contribution cancels exactly:

\[
\sum_i\alpha_i\partial_h\Phi_h(g_i)
=-f''(\mu_\alpha)\sum_i\alpha_i(g_i-\mu_\alpha)=0.
\tag{26}
\]

Moreover

\[
\partial_g\Phi_h(g)=f'(g)-f'(h).
\tag{27}
\]

Hence any support-edge value `a<mu_alpha` with `f'(a)<f'(mu_alpha)` has the same positive adjacent-collision pole as in the fixed-center argument. In particular, every `C^2` strictly convex generator has this property. The standard centered quadratic is the special case `f(g)=g^2/2`.

So weighted-mean centering is **not** covered for an arbitrary differentiable `h`-dependent convex profile. What survives durably is the exact translation-centered sign criterion (22), together with the Bregman class in which the moving-center derivative cancels by the weighted-mean constraint. These classes are already broad enough to show that replacing the centered quadratic by a standard convex moving-center entropy does not automatically remove the boundary obstruction.

## 5. Why the uncentered carrier of XF-018 escapes the bad sign

The uncentered square deliberately violates the centering hypothesis. With

\[
\Phi(g)=\frac12g^2,
\qquad
\Phi'(g)=g>0,
\tag{28}
\]

the same adjacent support-edge contribution is

\[
2\alpha_r\frac{\epsilon-a}{\epsilon},
\tag{29}
\]

which tends to `-infinity` as `epsilon->0`. That singularity is harmless for an upper dissipation estimate. More importantly, XF-018 reorganizes the positive localization error so that the natural coefficient is

\[
w_{ik}=c_{ik}g_i g_k\le1,
\tag{30}
\]

with the nonadjacent cross-ratio tails aggregated in XF-019 and made source-scale compatible in XF-020.

Equation (16) therefore explains the carrier tradeoff structurally. **Centering before localization asks the entropy derivative to change sign below the equilibrium spacing; compact localization then converts that negative derivative into a positive collision pole.** Keeping the gap factor uncentered preserves the favorable sign and renormalizes the dangerous conductance, but leaves the neutral mean/span mode to be removed nonlocally.

This strengthens the motivation for the XF-018--XF-020 route: the unresolved mean-removal problem is not an inconvenience that can obviously be bypassed by choosing a cleverer convex single-gap entropy. Within the compact fixed-reference convex class, the collision obstruction is unavoidable; Section 4 shows that two broad standard moving-mean classes retain it as well.

## 6. Stress tests and exact boundary of the no-go

The construction does **not** assert that the actual Xi zero configuration contains an arbitrarily collapsing exterior gap next to a prescribed compressed boundary gap. Its role is the line-specific matched-control test. The local geometry is compatible with the universal ordered logarithmic-repulsion ODE, and finite real-rooted polynomial backward-heat controls of the type used in XF-006 can realize arbitrary positive local gap data before collision. Therefore ordering, convexity, and the exact conductance formula alone cannot exclude (11).

The result also does not rule out the following escapes:

- an Xi-specific lower-gap or signed exterior estimate that quantitatively prevents the adversarial boundary regime;
- a noncompact localization whose weights never terminate, provided its infinite tail and entropy are genuinely summable;
- a nonlocal entropy or multiblock functional in which mean removal is encoded through pairwise/span terms rather than a single-site centered convex profile;
- signed cancellations that use more than the one-sided convexity estimate;
- the collision-safe uncentered cross-ratio organization of XF-018--XF-020.

A taper whose final positive weight is extremely small does not give a source-free uniform repair. For each `alpha_r>0`, however small, equation (10) allows `epsilon` to be chosen still smaller. Thus capacitary decay of the geometric cutoff cost in XF-017 and the present collision pole address different issues: the former controls many weak long-range interactions, while the latter is a single arbitrarily singular adjacent crossing.

## 7. Prior art and novelty boundary

Convex entropy dissipation for symmetric Markov/graph generators and contraction mechanisms for ordered one-dimensional singular repulsive systems are standard; Guillin--Le Bris--Monmarche, already anchored in `SOURCES.md`, provides an appropriate modern prior-art boundary for the latter. The broad fact that localization creates boundary flux is likewise standard.

A targeted search around Dyson/log-gas entropy methods, singular repulsive particle systems, and localized convex entropy did not identify an Xi-flow theorem that packages the specific dichotomy (16). No novelty claim is made for the elementary convexity fact or for the adjacent `1/(g_r g_{r+1})` conductance. The durable contribution is their exact combination at the current Xi-flow frontier: **every compact single-gap convex entropy that actually detects compression below a positive local equilibrium has an unbounded positive collision boundary mode.** No new external theorem is load-bearing, so `SOURCES.md` needs no additional anchor.

## 8. Consequence for `xi_flow`

XF-020 left the main task as organizing the near-buffer and mean/span flux after the far exterior had become negligible. XF-021 removes one tempting shortcut: replacing the centered quadratic by another compactly localized convex single-gap entropy cannot solve the collision side of that problem unless the new entropy becomes blind to compressed gaps.

The next useful search should therefore stay with genuinely nonlocal mean removal. In particular, the most promising exact target is whether the uncentered square/cross-ratio identity can be combined across overlapping blocks or with a span functional so that **mean removal occurs through signed boundary cancellation rather than through a centered single-gap derivative**. A positive identity of that kind would avoid the dichotomy above; a negative result should be formulated at that nonlocal level rather than by testing further convex pointwise entropies.