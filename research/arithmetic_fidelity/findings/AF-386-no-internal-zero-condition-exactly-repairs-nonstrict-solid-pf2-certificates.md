# AF-386 — No-internal-zero condition exactly repairs nonstrict solid PF2 certificates

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF2` · `LOG-CONCAVITY` · `ZERO-PATTERN` · `SUPPORT-CONNECTIVITY` · `CERTIFICATE-COMPRESSION` · `NEGATIVE/REPAIR` · `NO-NOVELTY-CLAIM`

## Claim

AF-382 and AF-385 use strict lower-order positivity to compress order-two translation total nonnegativity to adjacent/solid sampled minors. At order two, the exact obstruction to simply replacing that strictness by nonnegativity is **internal zeros**.

Let

\[
K_f(u,x)=f(u-x),\qquad f:\mathbb R\to[0,\infty)
\]

with `f` continuous, and let `h_m>0` satisfy `h_m\to0`. Define the solid order-two sampled determinants

\[
C_{2,h_m}(d)
:=f(dh_m)^2-f((d-1)h_m)f((d+1)h_m),
\qquad d\in\mathbb Z.
\tag{1}
\]

Then the following are equivalent:

1. `K_f` is totally nonnegative of order two on `\mathbb R\times\mathbb R`;
2. the positivity set
   \[
   I_f:=\{x\in\mathbb R:f(x)>0\}
   \tag{2}
   \]
   is an interval (possibly empty), and
   \[
   C_{2,h_m}(d)\ge0
   \tag{3}
   \]
   for every `m` and every `d\in\mathbb Z`.

Thus the strict first-order resource used in AF-382/AF-385 is stronger than necessary at order two. The exact qualitative repair is **support connectivity / no internal zeros**. Once that one bit of zero-pattern geometry is retained, shrinking-mesh solid minors recover the full `PF_2` target even when the profile vanishes at support boundaries.

Without that resource, the implication fails as strongly as possible: there are continuous nonnegative profiles for which `(3)` holds on **every sufficiently fine uniform lattice**, yet a continuum `2\times2` translation minor is strictly negative.

## Exact counterexample when support connectivity is dropped

Let

\[
\tau(x)=(1-|x|)_+,
\qquad
f(x)=\tau(x+2)+\tau(x-2).
\tag{4}
\]

The two positive components of `f` are

\[
(-3,-1)\quad\text{and}\quad(1,3),
\tag{5}
\]

separated by the internal zero interval `[-1,1]`. Each individual tent is log-concave on its support.

Fix any mesh `0<h<1`. For every `d\in\mathbb Z`, put `x=dh`. If `x-h,x,x+h` lie in one positive component, log-concavity of the tent gives

\[
f(x)^2\ge f(x-h)f(x+h).
\tag{6}
\]

If the three points do not lie in one component, the right-hand product in `(6)` is zero. Indeed, when `f(x)=0`, two positive endpoints would either lie in the same support interval, forcing their midpoint `x` into that interval, or lie in different components, which would require their separation `2h` to exceed the support gap `2`. Both are impossible for `h<1`. If `f(x)>0` but one neighbor leaves its component, that neighbor contributes zero.

Hence

\[
C_{2,h}(d)\ge0
\tag{7}
\]

for every integer offset `d` and every `0<h<1`. In particular, `(3)` holds for any shrinking mesh sequence eventually contained in `(0,1)`.

Nevertheless `K_f` is not `TN_2`. Take increasing rows and columns

\[
u_1=0<u_2=\frac52,
\qquad
x_1=\frac12<x_2=2.
\tag{8}
\]

Their difference matrix is

\[
\begin{pmatrix}
-\frac12 & -2\\
2 & \frac12
\end{pmatrix},
\tag{9}
\]

so `(4)` gives

\[
\bigl(f(u_i-x_j)\bigr)_{i,j=1}^2
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\tag{10}
\]

whose determinant is `-1`.

Therefore **nonnegative solid minors on arbitrarily fine lattices do not determine continuum `TN_2` on the unrestricted nonnegative class**. The local sampled inequalities cannot see that two individually log-concave components are globally separated by a zero gap.

## Why no internal zeros are sufficient

Assume now that `I_f` in `(2)` is an interval and that `(3)` holds. If `I_f` is empty, the result is trivial. Otherwise set

\[
g(x)=\log f(x),\qquad x\in I_f.
\tag{11}
\]

Fix a compact interval `J` contained in the interior of `I_f`. For all sufficiently large `m`, every grid point needed to interpolate `J` and its nearest neighbors lies inside `I_f`. At those points, `(3)` can be divided by positive values and written additively as

\[
2g(dh_m)
\ge
 g((d-1)h_m)+g((d+1)h_m).
\tag{12}
\]

Equivalently, the first grid differences

\[
\Delta_{d,m}
:=g((d+1)h_m)-g(dh_m)
\tag{13}
\]

are nonincreasing in `d`. The piecewise-linear interpolation of `g` on the `h_m\mathbb Z` grid is therefore concave on the grid interval covering `J`.

Because `g` is continuous on a compact neighborhood of `J` and `h_m\to0`, these piecewise-linear interpolants converge uniformly to `g` on `J`. A uniform limit of concave functions is concave. Thus `g` is concave on every compact subinterval of `I_f`, hence on all of `I_f`.

The positivity set is itself an interval, so extending `\log f` by `-\infty` outside `I_f` makes it an extended-real concave function. Therefore `f` is log-concave in the standard sense.

Classical Pólya-frequency theory identifies nonnegative log-concave functions on the line exactly with `PF_2` functions, i.e. translation kernels

\[
(u,x)\longmapsto f(u-x)
\tag{14}
\]

that are `TN_2`. Hence `(2)` plus `(3)` imply the full target.

The converse is classical and immediate at the sampled level: `TN_2` gives `(3)`, while a nonzero `PF_2` profile is log-concave and therefore has convex one-dimensional positivity support, i.e. no internal zeros. This proves the equivalence.

## What AF-382 and AF-385 were really paying for

AF-382 assumes `f>0`, takes logarithms of the sampled matrix, and telescopes local mixed differences to recover arbitrary sampled rectangles. AF-385 uses positive lower-order sampled minors to invoke a finite-matrix recognition theorem before taking the vanishing-mesh limit.

At order two, AF-386 separates two logically different roles hidden inside that strictness:

- **local shape control:** the solid determinant `(1)` forces discrete concavity of `\log f` wherever the three sampled values are positive;
- **zero-pattern control:** connected positivity support prevents local inequalities from becoming vacuous across an internal gap.

The first is carried by the sampled determinants themselves. The second is not. Strict positivity supplied both at once, but is not the minimal resource.

This is a direct Arithmetic Fidelity example of a small relational lift. The lost datum is not another real-valued moment, derivative, spectrum, or determinant. It is the topology/order geometry of the zero set: whether positive regions belong to one interval. Retaining that qualitative relation converts a non-faithful local compression into a target-complete one.

## Discrete analogue and prior-art boundary

The mechanism is classical. For a nonnegative sequence, adjacent log-concavity inequalities

\[
a_n^2\ge a_{n-1}a_{n+1}
\tag{15}
\]

are not by themselves the usual `PF_2` condition when internal zeros are allowed. The standard repair is exactly the no-internal-zero condition. The smallest toy obstruction is already

\[
(\ldots,0,1,0,0,1,0,\ldots),
\tag{16}
\]

which satisfies every adjacent inequality `(15)` but has a negative nonlocal Toeplitz `2\times2` minor.

The continuous two-tent construction `(4)` is the shrinking-mesh counterpart of the same phenomenon. Its purpose is therefore not to claim a new PF2 characterization, but to close the specific boundary left open by AF-382/AF-385: **vanishing spatial mesh does not repair missing support connectivity.** A topological zero-pattern resource survives as an independent requirement even when metric sampling resolution tends to zero.

Relevant prior art includes:

- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968), especially the classical `PF_2` / log-concavity theory and translation-kernel formulation.
- Francesco Brenti, ***Unimodal, Log-Concave and Pólya Frequency Sequences in Combinatorics***, Memoirs of the AMS **81**(413) (1989), DOI `10.1090/memo/0413`. Role: standard discrete distinction between log-concavity inequalities and Pólya-frequency behavior when zero patterns/internal zeros are present.
- Adrien Saumard and Jon A. Wellner, **“Log-concavity and strong log-concavity: a review,”** *Statistical Surveys* **8** (2014), 45–114, DOI `10.1214/14-SS107`, especially Proposition 2.3 identifying one-dimensional log-concave functions with `PF_2` functions.
- Antoine Marie Bogso, **“MRL order, log-concavity and an application to peacocks,”** *Stochastic Processes and their Applications* **125**(4) (2015), 1282–1306, DOI `10.1016/j.spa.2014.10.015`. Role: modern TP2 support-geometry formulation; its TP2 criterion makes explicit that the positive set must obey a lattice/support compatibility condition in addition to positivity on that set.

No novelty is claimed for the PF2/log-concavity/no-internal-zero equivalence. The exact two-tent counterexample and shrinking-grid reformulation are elementary consequences organized to identify the missing resource in Mathia's current certificate-compression chain.

## Fidelity consequence

AF-386 sharpens the hierarchy around AF-383–AF-385.

For order two, unrestricted one-axis/solid sampling has a **zero-pattern failure mode** that survives arbitrarily fine resolution. The missing information is not more samples at the same local stencil; every sufficiently fine solid sample can pass. What matters is a relation between separated positive regions that the local stencil never crosses.

With no internal zeros retained, the same one-parameter sampled solid family becomes target-complete in the shrinking-mesh limit. Thus, at this order, support connectivity is an exact minimal qualitative lift from local log-concavity tests to global translation `TN_2`.

This also warns against treating finer sampling as a universal substitute for provenance or topology. A compression can have vanishing metric mesh while still preserving a disconnected equivalence structure that hides a decisive global minor. Resolution and relational breadth are different resources.

For higher determinant order, no analogous claim is established here. Zero patterns of totally nonnegative matrices and higher-order Pólya-frequency functions are substantially richer; AF-386 does not show that support connectivity alone repairs AF-385 for `k\ge3`.

## Riemann-facing boundary

The result has no direct RH consequence. It does, however, refine how a total-positivity route should account for source assumptions. At the first nontrivial `PF_2` layer, requiring strict positivity everywhere is unnecessarily strong if the arithmetic/analytic profile naturally has support boundaries: connected positivity support plus the solid inequalities suffice.

Conversely, if an RH-facing transformed profile can develop internal zero gaps, arbitrarily fine local determinant sampling cannot by itself certify even order-two translation total nonnegativity. One must either prove the no-internal-zero property independently or retain a certificate family that directly crosses the separated components.

That distinction is exactly the line's mandate: identify which property survives the compression and which small additional structure must be carried for the target to remain recoverable.

## Boundaries and falsification checks

The theorem concerns continuous nonnegative scalar translation profiles and order two only. Continuity is used to pass shrinking-grid concavity to the continuum; without it, a dense sampled family need not determine unsampled values.

The positivity-set condition means `\{f>0\}` is an interval, not merely that the closed support `\overline{\{f>0\}}` is connected. A profile that vanishes at an interior point while remaining positive on both sides has an internal zero and is excluded, as required by log-concavity.

The two-tent example is not a counterexample to AF-382 or AF-385 because it violates their strict lower-order hypotheses. It shows those hypotheses cannot simply be weakened from `>0` to `\ge0` while retaining the same conclusion.

The claim that no internal zeros are the exact repair is specific to `PF_2`. Higher-order total nonnegativity has additional minor/zero-pattern constraints, so this result must not be extrapolated to the `PF_\infty` target used in Riemann-facing total-positivity criteria.

Finally, support connectivity is target information, not rational-prime identity. Many arithmetic and nonarithmetic profiles share it. AF-386 therefore improves the compression theory but does not itself distinguish ordinary primes from matched controls.