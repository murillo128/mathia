# AF-462 — Finite-support simplex boundaries separate anchored from pairwise Hilbert fidelity

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `BOUNDARY-GEOMETRY`, `QUANTITATIVE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

The positivity boundary of the probability simplex gives an exact source-side escape from the cube-completeness mechanism of AF-459, but only for **anchored** discrimination from a boundary law. It does not produce pairwise local bi-Lipschitz fidelity.

Let `A` be countably infinite and

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_{a\in A}\mu(a)=1\right\}.
\tag{1}
\]

Fix `mu_0 in Delta(A)` with finite nonempty support

\[
S=\operatorname{supp}(\mu_0),\qquad |S|=s<\infty.
\tag{2}
\]

For any relative neighborhood `W` of `mu_0` in `Delta(A)`, define its normalized anchored radial carrier

\[
C_W(\mu_0)
=
\left\{
\frac{\mu-\mu_0}{\|\mu-\mu_0\|_1}:
\mu\in W,\ \mu\ne\mu_0
\right\}.
\tag{3}
\]

Then this carrier is independent of `W` and is exactly

\[
\boxed{
C_W(\mu_0)=C_S
:=
\left\{
h\in\ell^1(A):
\sum_a h(a)=0,\ \|h\|_1=1,\ \operatorname{supp}(h_-)\subseteq S
\right\}.
}
\tag{4}
\]

Thus finite support creates a one-sided provenance constraint: mass may leave the active support into arbitrarily many new coordinates, but negative mass can occur only on the original support.

For the paired-cube completion profile `D_k` of AF-459,

\[
\boxed{
D_k(C_S)\ge \left(1-\frac{s}{k}\right)_+.
}
\tag{5}
\]

Hence

\[
\liminf_{k\to\infty}D_k(C_S)\ge1.
\tag{6}
\]

So this boundary carrier stays a positive average `ell^1` distance from every sufficiently large ideal paired sign cube; it is the opposite of the cube-complete regular carriers in AF-460 and AF-461.

There is also an exact anchored Hilbert modulus. Let

\[
J:\Delta(A)\to\ell^2(A),\qquad J(\mu)=(\mu(a))_{a\in A}
\tag{7}
\]

be the canonical one-hot barycentric embedding. Then

\[
\boxed{
\inf_{h\in C_S}\|h\|_2=\frac1{2\sqrt{s}}.
}
\tag{8}
\]

Equivalently, relative to total variation in the probabilistic convention

\[
\operatorname{TV}(\mu,\mu_0)=\frac12\|\mu-\mu_0\|_1,
\tag{9}
\]

the exact anchored lower gain is

\[
\boxed{
\inf_{\mu\ne\mu_0}
\frac{\|J\mu-J\mu_0\|_2}
{\operatorname{TV}(\mu,\mu_0)}
=\frac1{\sqrt{s}},
}
\tag{10}
\]

where the infimum may be restricted to any relative neighborhood of `mu_0`.

However, every such neighborhood still has zero **pairwise** local `ell^1`-to-`ell^2` lower gain:

\[
\boxed{
\inf_{\substack{\mu,\nu\in W\\\mu\ne\nu}}
\frac{\|J\mu-J\nu\|_2}{\|\mu-\nu\|_1}=0.
}
\tag{11}
\]

Therefore positivity/boundary geometry can preserve provenance relative to a distinguished finite-support source without repairing the full local metric geometry around that source.

## Exact derivation

### The anchored radial carrier is exactly the simplex tangent cone section

Take `mu in W`, `mu != mu_0`, and put

\[
h=\frac{\mu-\mu_0}{\|\mu-\mu_0\|_1}.
\]

Then `sum_a h(a)=0` and `||h||_1=1`. If `a notin S`, then `mu_0(a)=0` and `mu(a)>=0`, so `h(a)>=0`. Hence every negative coordinate of `h` lies in `S`, proving

\[
C_W(\mu_0)\subseteq C_S.
\tag{12}
\]

Conversely, take `h in C_S`. Because `S` is finite and `mu_0(a)>0` for every `a in S`, there exists `t_0>0` such that

\[
\mu_0(a)+t h(a)\ge0
\qquad(a\in S)
\]

whenever `0<t<t_0`. Outside `S`, `h(a)>=0`; also `sum_a h(a)=0`. Therefore

\[
\mu_t=\mu_0+t h\in\Delta(A)
\]

for all sufficiently small positive `t`. Since `W` is a relative neighborhood of `mu_0`, one may choose such a `t` with `mu_t in W`, and then

\[
\frac{\mu_t-\mu_0}{\|\mu_t-\mu_0\|_1}=h.
\]

This proves `(4)`.

The important structural point is that the restriction is not a finite-dimensional tangent space. It is a one-sided cone section: arbitrarily many fresh positive coordinates remain available, while negative coordinates retain provenance in the active face `S`.

### Finite support forces large paired-cube defect

Use the AF-459 ideal paired orientation

\[
q^B_\varepsilon
=
\frac1{2k}\sum_{j=1}^k
\varepsilon_j(\delta_{a_j}-\delta_{b_j})
\tag{13}
\]

for `2k` distinct atoms. Every orientation has exactly `k` negative coordinates, each equal to `-1/(2k)`.

Fix `c in C_S`. Since `c` can be negative on at most the `s` atoms of `S`, at least `(k-s)_+` negative coordinates of `q^B_epsilon` occur at coordinates where `c>=0`. At each such coordinate,

\[
(q^B_\varepsilon-c)(a)\le-\frac1{2k}.
\]

Both `q^B_epsilon` and `c` have total mass zero, so their difference has total mass zero and

\[
\|q^B_\varepsilon-c\|_1
=2\|(q^B_\varepsilon-c)_-\|_1
\ge
\frac{(k-s)_+}{k}.
\tag{14}
\]

The bound is uniform in `B`, `epsilon`, and `c`. Taking the carrier distance, then the sign average, then the infimum over paired blocks gives `(5)`.

This directly answers one of the source-law escape questions left by AF-459--AF-461: a finite-support positivity boundary is **tangent-incomplete enough** to remain macroscopically far from large paired sign cubes.

### Exact anchored Hilbert modulus

For any `h in C_S`, zero total mass and unit `ell^1` norm imply

\[
\|h_-\|_1=\|h_+\|_1=\frac12.
\tag{15}
\]

The negative part is supported on at most `s` coordinates, so Cauchy--Schwarz gives

\[
\|h\|_2
\ge\|h_-\|_2
\ge\frac{\|h_-\|_1}{\sqrt{s}}
=\frac1{2\sqrt{s}}.
\tag{16}
\]

The constant is sharp. Put negative mass uniformly on `S`, and for each `N` choose `N` fresh atoms outside `S` and put the positive mass uniformly on them. The resulting `h_N in C_S` has

\[
\|h_N\|_2
=
\frac12\sqrt{\frac1s+\frac1N}
\longrightarrow
\frac1{2\sqrt{s}}.
\tag{17}
\]

Equations `(16)`--`(17)` prove `(8)`, and `(10)` is just the conversion from `ell^1` distance to the probabilistic TV convention.

### Pairwise local fidelity still collapses

Fix any relative neighborhood `W` of `mu_0` and choose `a_0 in S`. For sufficiently small `t>0`, choose two disjoint sets `U_N,V_N subset A\setminus S`, each with `N` atoms, and let `u_N,v_N` be their uniform probability measures. Define

\[
\mu_N=\mu_0-t\delta_{a_0}+t u_N,
\qquad
\nu_N=\mu_0-t\delta_{a_0}+t v_N.
\tag{18}
\]

For `t` small enough these are probability laws in `W`. Their common depletion of `a_0` cancels, so

\[
\mu_N-\nu_N=t(u_N-v_N).
\]

Because the two fresh supports are disjoint,

\[
\|\mu_N-\nu_N\|_1=2t,
\qquad
\|J\mu_N-J\nu_N\|_2=t\sqrt{\frac2N}.
\tag{19}
\]

Therefore

\[
\frac{\|J\mu_N-J\nu_N\|_2}{\|\mu_N-\nu_N\|_1}
=\frac1{\sqrt{2N}}
\longrightarrow0,
\tag{20}
\]

which proves `(11)`.

## What this adds to AF-459--AF-461

AF-459 separates source geometry from target Banach geometry through the average cube-completion profile `D_k(C)`. AF-460 and AF-461 then show that finite-rank linear constraints and regular smooth finite-dimensional nonlinear equality laws remain locally cube-complete: their relevant carriers contain arbitrarily large paired cubes, so ordinary smooth restriction does not evade the target-type obstruction.

AF-462 identifies a qualitatively different source mechanism. At a finite-support point of the positive simplex, the active face imposes a **one-sided sign constraint** that survives normalization. Large paired cubes require `k` independently placeable negative coordinates, while the boundary carrier has only `s` coordinates on which negative mass is allowed. The simple counting mismatch already forces `(5)`.

The same source asymmetry is strong enough for the canonical Hilbert embedding to retain a positive anchored modulus `(8)`, but not strong enough to control arbitrary pairs in the neighborhood. Thus the useful distinction is not merely

\[
\text{cube-poor versus cube-rich},
\]

but also

\[
\text{anchored provenance fidelity versus pairwise metric fidelity}.
\]

A source law can possess the former while decisively failing the latter.

## Prior-art and novelty audit

The geometric ingredients are classical. This finding makes **no novelty claim** for tangent cones of simplices, active-set geometry, sparse-face structure, or the elementary `ell^1`/`ell^2` estimates.

- R. Tyrrell Rockafellar and Roger J-B Wets, *Variational Analysis*, Springer (1998), provides the standard tangent/normal-cone language for constrained sets and active inequalities. The carrier in `(4)` is exactly the unit `ell^1` section of the feasible one-sided tangent cone at a finite-support simplex point.
- Venkat Chandrasekaran, Benjamin Recht, Pablo A. Parrilo, and Alan S. Willsky, **“The Convex Geometry of Linear Inverse Problems,”** *Foundations of Computational Mathematics* 12 (2012), 805--849, DOI `10.1007/s10208-012-9135-7`, is direct prior art for using tangent/descent-cone geometry to characterize what structured restrictions preserve under compression.
- Dennis Amelunxen, Martin Lotz, Michael B. McCoy, and Joel A. Tropp, **“Living on the edge: phase transitions in convex programs with random data,”** *Information and Inference* 3(3) (2014), 224--294, develops descent cones and statistical dimension as quantitative geometric controls for convex recovery.

Those references establish the surrounding convex-geometric language, not the AF-459 profile or the specific constants `(5)` and `(8)` in Mathia's source-law fidelity framework. The derivations here are elementary specializations. The useful contribution is therefore the exact **boundary-separation audit** inside Arithmetic Fidelity: positivity can defeat large-cube completion at a distinguished finite-support source while still failing pairwise local fidelity.

## Boundary and falsification audit

- **Finite support is substantive.** If `mu_0` has infinite support, the proof of `(5)` loses its finite negative-coordinate budget. No analogous lower bound is claimed.
- **This is an anchored statement.** Equation `(8)` concerns directions away from one fixed boundary law. It must not be promoted to a pairwise lower-Lipschitz theorem; `(11)` explicitly falsifies that upgrade.
- **Infinite ambient alphabet is used for sharpness and pairwise collapse.** The constructions in `(17)` and `(18)` spread positive mass over arbitrarily many fresh coordinates. For finite alphabets there is a dimension-dependent cutoff.
- **The one-hot target is canonical but not universally optimal.** The result proves that one natural Hilbert representation has positive anchored gain. It does not prove that every bounded Hilbert marking does, nor that this representation is minimal for an application.
- **Large cube defect is necessary source rigidity, not sufficient fidelity.** AF-459 already shows that staying far from paired cubes only removes one collapse certificate. Other source directions or target mechanisms may still destroy a discriminator.
- **No arithmetic conclusion follows from finite support alone.** The theorem is a generic simplex-boundary result. An arithmetic application must first show that the relevant source comparison is genuinely anchored to a distinguished finite-support law and that this one-sided provenance is the property that must survive.
- **Metric normalization remains explicit.** Equations `(8)` and `(11)` use `ell^1`; equation `(10)` separately records the conventional factor-two conversion to probabilistic total variation.

## Arithmetic specialization

For a later rational-prime application, AF-462 suggests a precise question rather than a conclusion: does the arithmetic object naturally select a distinguished source whose admissible perturbations have an active-face or one-sided provenance constraint, so that the relevant discriminator is **anchored** rather than fully pairwise?

If yes, a boundary mechanism can evade the specific large-cube obstruction even in a Hilbert target. If the application instead requires stable discrimination between arbitrary nearby admissible prime-derived sources, the finite-support simplex mechanism is insufficient by `(11)`. Any successful lift must add structure that prevents the fresh-support cancellation used in `(18)`, rather than merely relying on positivity or finite support at the anchor.
