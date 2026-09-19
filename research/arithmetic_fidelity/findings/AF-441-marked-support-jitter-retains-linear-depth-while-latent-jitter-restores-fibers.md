# AF-441 — Marked support jitter retains linear-depth fidelity while latent jitter restores moment fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `MARKED-SUPPORT-LIFT`, `FINITE-PREFIX-RECOVERY`, `FINITE-PREFIX-NONIDENTIFIABILITY`, `CLASSICAL-SUPERINCREASING/PRONY-PRINCIPLES`, `NO-NOVELTY-CLAIM`

## Claim

AF-439 and AF-440 leave an apparent gap between continuously movable support, where every finite Euler moment prefix has local pole-moving fibers, and the exact reciprocal-square support ladder with discrete marks, where one sufficiently deep moment recovers a linearly growing initial mark segment.

The decisive distinction is not merely the numerical size of support perturbation. It is whether the perturbed support provenance itself survives as retained data.

Fix a finite alphabet `A` with at least two real values. Let `delta>0` be the minimum distance between two distinct alphabet values and let `D>0` be the alphabet diameter. Fix

\[
0\le \rho<\frac12,
\qquad
r_m\in[m-\rho,m+\rho].
\]

Because `rho<1/2`, the shell intervals are disjoint and every admissible support sequence `r=(r_m)` is strictly increasing. For an infinite mark sequence

\[
a=(a_m)_{m\ge1}\in A^{\mathbb N},
\]

define the depth-`N` scalar moment

\[
M_N(r,a):=\sum_{m\ge1}a_m r_m^{-2N}.
\]

Consider first the **marked-support compression**

\[
T_N(r,a):=(r,M_N(r,a)),
\]

which retains the actual possibly jittered support skeleton while compressing the mark sequence to one scalar.

If two mark sequences first differ at shell `m`, then

\[
\boxed{
|M_N(r,a)-M_N(r,b)|
\ge
\delta(m+\rho)^{-2N}
-D\sum_{j>m}(j-\rho)^{-2N}.
}
\tag{1}
\]

Therefore the first `L` marks are forced whenever

\[
\boxed{
\frac D\delta
\left(\frac{L+\rho}{L+1-\rho}\right)^{2N}
\left(1+\frac{L+1-\rho}{2N-1}\right)
<1.
}
\tag{2}
\]

The criterion is uniform over the whole jitter tube and gives linear-depth recovery. If `s=2N` and `m_s=floor(c(s-1))`, then the left side of the shellwise version of `(2)` converges to

\[
\boxed{
\frac D\delta(1+c)
\exp\!\left(-\frac{1-2\rho}{c}\right).
}
\tag{3}
\]

Hence every positive `c` satisfying

\[
\frac D\delta(1+c)e^{-(1-2\rho)/c}<1
\tag{4}
\]

gives recovery through `m<=c(2N-1)+o(N)`. Such a `c` exists for every `rho<1/2`. One conservative explicit choice is

\[
c_0=\frac{1-2\rho}{2\log(2D/\delta)}.
\tag{5}
\]

Now drop the support marking and retain only the finite moment prefix

\[
U_N(r):=
\left(
\sum_{m\ge1}r_m^{-2},
\sum_{m\ge1}r_m^{-4},
\ldots,
\sum_{m\ge1}r_m^{-2N}
\right).
\]

For every fixed `N>=1` and every arbitrarily small `rho>0`, this unmarked map is noninjective inside the `rho`-tube around the exact integer skeleton. There are distinct increasing support sequences `r` and `r_tilde`, both arbitrarily close to `r_m=m`, with

\[
\boxed{U_N(r)=U_N(r_{\mathrm{tilde}}).}
\tag{6}
\]

The collision can move only `N+1` shells, and each moved shell keeps the unit-residue Stieltjes form `1/(r_m^2-z)`.

Thus arbitrarily small continuous support jitter has opposite consequences depending on whether support provenance survives the compression:

\[
\boxed{
\text{retained support}\Rightarrow\text{positive finite-depth mark fidelity},
\qquad
\text{latent movable support}\Rightarrow\text{exact finite-prefix support fibers}.
}
\tag{7}
\]

Retaining the entire jittered skeleton is only a sufficient provenance lift. This finding does not claim that it is minimal.

## Exact marked-support derivation

Put `s=2N>1` and suppose `a` and `b` first differ at shell `m`. Earlier terms cancel because both candidates use the same retained support skeleton. The first differing coefficient has magnitude at least `delta`, while every later coefficient difference has magnitude at most `D`. Hence

\[
\begin{aligned}
|M_N(r,a)-M_N(r,b)|
&\ge \delta r_m^{-s}-D\sum_{j>m}r_j^{-s}\\
&\ge \delta(m+\rho)^{-s}-D\sum_{j>m}(j-\rho)^{-s},
\end{aligned}
\]

which proves `(1)`.

For the decreasing function `f(x)=(x-rho)^{-s}`, the integral test gives

\[
\sum_{j>m}(j-\rho)^{-s}
\le
(m+1-\rho)^{-s}
\left(1+\frac{m+1-\rho}{s-1}\right).
\tag{8}
\]

Combining `(1)` and `(8)` yields the shellwise sufficient condition

\[
\frac D\delta
\left(\frac{m+\rho}{m+1-\rho}\right)^s
\left(1+\frac{m+1-\rho}{s-1}\right)<1.
\tag{9}
\]

Both factors on the left increase with `m` when `rho<1/2`, so checking `(9)` at `m=L` proves agreement through every earlier shell. This gives `(2)`.

The theorem is therefore worst-case over all retained support skeletons satisfying the jitter bound. Exact integer positions are not required once their actual perturbed values remain part of the representation.

## Linear-depth asymptotics

Take `m_s=floor(c(s-1))`. Then

\[
1+\frac{m_s+1-\rho}{s-1}\longrightarrow1+c,
\]

and

\[
s\log\left(\frac{m_s+\rho}{m_s+1-\rho}\right)
\longrightarrow-\frac{1-2\rho}{c}.
\]

This proves `(3)`. Because `1-2rho>0`, the exponential factor tends to zero as `c` decreases to zero, so a positive linear recovery coefficient always exists.

For `(5)`, `D>=delta`, so `c_0<1`. Moreover

\[
e^{-(1-2\rho)/c_0}=(2D/\delta)^{-2},
\]

and therefore

\[
\frac D\delta(1+c_0)e^{-(1-2\rho)/c_0}
<\frac\delta{2D}\le\frac12.
\]

Thus `(4)` holds with slack for `c_0`. This coefficient is deliberately conservative, not optimal.

At `rho=0`, AF-440 has the sharper reciprocal-square cutoff `Dm<=delta(2N-1)`. The present estimate gives up that sharp constant in exchange for uniformity over a continuous jitter tube.

## Why latent jitter immediately restores the AF-439 fiber

The positive theorem uses a load-bearing hypothesis: the support skeleton is retained. Once competing sources may move their supports independently while only finitely many moments survive, the earlier-shell cancellation in `(1)` is unavailable.

AF-439 supplies the exact local obstruction. Fix any `N+1` distinct integer shells `j_0,...,j_N>=2` and set `x_k=j_k^{-2}`. Varying only the final elementary-symmetric coefficient of the monic polynomial with roots `x_k` preserves the first `N` power sums by Newton identities while moving every root. Hence there is a nonconstant local family `x_k(tau)` satisfying

\[
\sum_{k=0}^{N}x_k(\tau)^\ell
=
\sum_{k=0}^{N}x_k(0)^\ell,
\qquad
1\le\ell\le N.
\tag{10}
\]

Define the moved shell coordinate by

\[
r_{j_k}(\tau):=x_k(\tau)^{-1/2}
\]

and leave all unselected shells unchanged. Continuity of `x -> x^{-1/2}` implies that for every prescribed positive `rho`, a sufficiently small nonzero `tau` keeps every moved coordinate within its `rho`-interval. For `rho<1/2` the intervals remain disjoint, so the perturbed support remains ordered.

Equation `(10)` is exactly equality of the first `N` coordinates of `U_N`. Meanwhile

\[
\frac{x_k(\tau)}{1-zx_k(\tau)}
=
\frac1{r_{j_k}(\tau)^2-z},
\]

so every moved pole still has residue `-1`.

Therefore no positive jitter radius makes the unmarked finite moment prefix injective on a source class that permits independent continuous shell movement. The failure is identifiability, not numerical conditioning.

## Provenance is the load-bearing resource

The result separates two information structures that can look superficially identical when described only as “support uncertainty.”

If the actual support coordinates are retained, uncertainty means only that the retained coordinates may lie anywhere in known disjoint intervals. The compression forgets the mark sequence but not where its coefficients live. High-order reciprocal weights then form a tail-dominating code and an initial mark segment survives uniformly.

If only the intervals are known and the actual support coordinates are latent, competing sources may choose different points inside those intervals. The Newton/Prony fiber then passes through the Euler source inside every open jitter tube.

So small geometric error and forgotten provenance are not interchangeable. A coordinate can vary continuously without destroying the discriminator when its realized value is retained; forgetting that same coordinate can create exact fibers even when the allowed variation is arbitrarily small.

## Prior-art and novelty audit

The ingredients are classical, and no novelty is claimed for them.

The marked-support proof is a robust version of the superincreasing/greedy-decoding principle already used in AF-440. Superincreasing knapsacks and their lexicographic structure are standard; a modern reference is Akshay Gupte, **“Convex hulls of superincreasing knapsacks and lexicographic orderings,”** *Discrete Applied Mathematics* 201, 150–163 (2016), DOI `10.1016/j.dam.2015.08.010`.

Interval uncertainty in knapsack weights is also established robust-optimization prior art. Michele Monaci and Ulrich Pferschy, **“On the Robust Knapsack Problem,”** *SIAM Journal on Optimization* 23(4), 1956–1982 (2013), DOI `10.1137/120880355`, studies optimization under interval-valued item weights. That literature is neighboring language rather than a theorem source for `(1)`–`(7)`.

The latent-support obstruction is the classical truncated-moment/Newton/Prony phenomenon specialized in AF-439. Finite atomic recovery and support-separation conditions are standard Prony theory; see Stefan Kunis, Thomas Peter, Tim Römer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490, 31–47 (2016), DOI `10.1016/j.laa.2015.10.023`.

The Arithmetic Fidelity contribution recorded here is the exact placement of these classical mechanisms at the AF-439/AF-440 boundary: inside an arbitrarily thin reciprocal-square jitter tube, finite-prefix behavior changes from local nonidentifiability to linearly deep exact mark recovery according to whether support provenance is retained.

## Boundaries and falsification checks

- The positive theorem retains the **actual** jittered support skeleton, not merely the interval labels. It is a sufficient provenance lift, not a minimal-lift theorem.
- The negative theorem lets competing sources choose different support positions. It does not contradict recovery conditional on one shared retained skeleton.
- `rho<1/2` guarantees disjoint shell intervals and canonical ordering. It is sufficient, not asserted sharp for every marked model.
- Criterion `(2)` is sufficient, not necessary; the integral estimate can underestimate the true recoverable depth.
- The coefficient `(5)` is conservative. AF-440 is sharper when `rho=0`.
- Exact mark recovery may still be extremely ill-conditioned because the positive separation margin can be tiny. Noise tolerance is a separate question.
- The alphabet must be finite and separated. Continuous amplitudes have no positive `delta`, so this proof gives no exact mark discrimination.
- Retaining the full support skeleton may be more side information than an RH-facing construction can canonically justify. A downstream application must explain why that provenance survives naturally.
- Nothing here distinguishes rational primes, constrains nontrivial zeta zeros, or implies RH. This is a finite-data representation theorem for the Euler reciprocal-square shell carrier.

A counterexample to the marked theorem would require one retained support skeleton and two alphabet mark sequences with equal `M_N` whose first difference satisfies `(9)`. Inequalities `(1)` and `(8)` rule this out. A counterexample to the latent theorem would require injectivity of `U_N` on a positive open jitter tube, contradicting the AF-439 Newton family after shrinking its parameter into that tube.

## Consequence for the research line

The AF-439/AF-440 boundary should no longer be phrased only as “how much support jitter is allowed?” The sharper question is **which support information survives the compression**.

Exact integer support positions are not needed for a uniform linear-depth mark theorem when the realized jittered skeleton remains marked. Conversely, arbitrarily tiny latent support freedom restores exact finite-prefix collision fibers.

The next minimal-lift problem is therefore to weaken the support mark itself: retain only interval/cell identity, ordering plus quantitative separation, a low-dimensional deformation law, or another canonical provenance summary, and ask whether any such coarser lift still makes the finite-moment fibers target-pure. Only after that identifiability gate should noisy Padé/Prony/Stieltjes conditioning be priced on the resulting source class.