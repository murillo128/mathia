# AF-441 — Marked support jitter retains linear-depth fidelity while latent jitter restores moment fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `MARKED-SUPPORT-LIFT`, `FINITE-PREFIX-RECOVERY`, `FINITE-PREFIX-NONIDENTIFIABILITY`, `CLASSICAL-SUPERINCREASING/PRONY-PRINCIPLES`, `NO-NOVELTY-CLAIM`

## Claim

AF-439 and AF-440 leave an apparent gap between two source classes:

- continuously movable support, where every finite Euler moment prefix has local pole-moving fibers; and
- the exact reciprocal-square support ladder with discrete marks, where one sufficiently deep moment recovers a linearly growing initial mark segment.

The decisive distinction is not merely the numerical size of support perturbation. It is whether the perturbed support provenance itself survives as retained/marked data.

Fix a finite alphabet `A subset R` with at least two values and write

\[
\delta:=\min_{a\ne b\in A}|a-b|>0,
\qquad
D:=\max A-\min A>0.
\]

Let

\[
0\le \rho<\frac12,
\qquad
r_m\in[m-\rho,m+\rho],
\qquad
q_m:=r_m^{-2}.
\]

Because `rho<1/2`, the shell intervals are disjoint and every admissible sequence `r=(r_m)` is strictly increasing. For marks `a=(a_m) in A^N`, define

\[
M_N(r,a):=\sum_{m\ge1}a_m r_m^{-2N}.
\]

Consider first the **marked-support compression**

\[
T_N(r,a):=(r,M_N(r,a)),
\]

so the possibly jittered support skeleton is retained while the mark sequence is compressed to one scalar moment.

If `a` and `b` first differ at shell `m`, then

\[
\boxed{
|M_N(r,a)-M_N(r,b)|
\ge
\delta(m+\rho)^{-2N}
-D\sum_{j>m}(j-\rho)^{-2N}.
}
\tag{1}
\]

Consequently the first `L` marks are forced whenever, for every `m<=L`,

\[
\boxed{
\frac D\delta
\left(\frac{m+\rho}{m+1-\rho}\right)^{2N}
\left(1+\frac{m+1-\rho}{2N-1}\right)
<1.
}
\tag{2}
\]

The left side of `(2)` is increasing in `m`, so it is enough to check the endpoint `m=L`.

For every fixed `rho<1/2` and fixed alphabet, this gives a **linear-depth** recovery law. More precisely, if `s=2N` and `m_s=floor(c(s-1))`, then the left side of `(2)` converges to

\[
\boxed{
\frac D\delta(1+c)
\exp\!\left(-\frac{1-2\rho}{c}\right).
}
\tag{3}
\]

Hence every `c>0` satisfying

\[
\frac D\delta(1+c)e^{-(1-2\rho)/c}<1
\tag{4}
\]

gives recovery through `m<=c(2N-1)+o(N)`. Such a positive `c` exists for every `rho<1/2`. For example,

\[
c_0=
\frac{1-2\rho}{2\log(2D/\delta)}
\tag{5}
\]

is a conservative explicit choice: the limit in `(3)` is then strictly below `1`.

Now drop the support marking. Define the **latent-support finite-prefix compression**

\[
U_N(r)
:=
\left(
\sum_{m\ge1}r_m^{-2},
\sum_{m\ge1}r_m^{-4},
\ldots,
\sum_{m\ge1}r_m^{-2N}
\right).
\]

For every fixed `N>=1` and every arbitrarily small `rho>0`, `U_N` is noninjective in every sufficiently small jitter tube around the exact integer skeleton `r_m=m`: there are distinct increasing support sequences `r` and `\widetilde r`, both satisfying

\[
|r_m-m|<\rho,
\qquad
|\widetilde r_m-m|<\rho,
\]

with

\[
\boxed{U_N(r)=U_N(\widetilde r).}
\tag{6}
\]

The collision may be chosen to move only `N+1` shells, with every moved shell retaining the unit-residue Stieltjes form

\[
\frac1{r_m^2-z}.
\]

Thus **arbitrarily small continuous support jitter has opposite consequences depending on whether support provenance survives the compression**:

\[
\boxed{
\begin{array}{c}
\text{support retained/marked}
\;\Longrightarrow\;
\text{uniform positive finite-depth mark fidelity},\\[2mm]
\text{support latent and independently movable}
\;\Longrightarrow\;
\text{exact finite-prefix support fibers for every }\rho>0.
\end{array}}
\tag{7}
\]

This does not prove that retaining the entire jittered skeleton is a minimal lift. It identifies it as a sufficient provenance lift and shows that the amount of geometric jitter alone is not the correct fidelity parameter.

## Exact marked-support derivation

Put

\[
s:=2N>1.
\]

Suppose `a` and `b` first differ at shell `m`. Earlier terms cancel exactly because both candidates are compared over the same retained support skeleton. At the first differing shell,

\[
|a_m-b_m|\ge\delta,
\]

while every later coefficient difference is bounded by `D`. Therefore

\[
\begin{aligned}
|M_N(r,a)-M_N(r,b)|
&=\left|
(a_m-b_m)r_m^{-s}
+\sum_{j>m}(a_j-b_j)r_j^{-s}
\right|\\
&\ge
\delta r_m^{-s}
-D\sum_{j>m}r_j^{-s}\\
&\ge
\delta(m+\rho)^{-s}
-D\sum_{j>m}(j-\rho)^{-s},
\end{aligned}
\]

which proves `(1)`.

For the decreasing function

\[
f(x)=(x-\rho)^{-s},
\]

the integral test gives

\[
\begin{aligned}
\sum_{j>m}(j-\rho)^{-s}
&\le
(m+1-\rho)^{-s}
+\int_{m+1}^{\infty}(x-\rho)^{-s}\,dx\\
&=
(m+1-\rho)^{-s}
\left(
1+\frac{m+1-\rho}{s-1}
\right).
\end{aligned}
\tag{8}
\]

Combining `(1)` and `(8)`, a sufficient strict-separation condition is

\[
\delta(m+\rho)^{-s}
>
D(m+1-\rho)^{-s}
\left(1+\frac{m+1-\rho}{s-1}\right),
\]

which is exactly `(2)`.

Both factors

\[
\frac{m+\rho}{m+1-\rho}
\qquad\text{and}\qquad
1+\frac{m+1-\rho}{s-1}
\]

increase with `m` when `rho<1/2`. Therefore if `(2)` holds at `m=L`, it holds at every earlier shell. Equality of the marked compression `T_N(r,a)=T_N(r,b)` then forces

\[
a_m=b_m,
\qquad 1\le m\le L.
\]

This is a worst-case theorem over the entire jitter tube: the exact locations `r_m` may vary arbitrarily inside their shell intervals, but once those locations are retained as part of the representation, the same finite-depth guarantee holds uniformly.

## Linear-depth asymptotics

Let

\[
m_s=\lfloor c(s-1)\rfloor,
\qquad c>0.
\]

Then

\[
1+\frac{m_s+1-\rho}{s-1}\longrightarrow 1+c.
\]

Also

\[
\begin{aligned}
s\log\left(\frac{m_s+\rho}{m_s+1-\rho}\right)
&=
s\log\left(
1-\frac{1-2\rho}{m_s+1-\rho}
\right)\\
&\longrightarrow
-\frac{1-2\rho}{c}.
\end{aligned}
\]

This proves `(3)`. Since `1-2rho>0`, the exponential factor tends to zero as `c downarrow 0`, so a positive linear recovery coefficient always exists.

For the explicit value `(5)`, note that `D>=delta`, hence

\[
c_0<\frac1{2\log2}<1.
\]

Moreover

\[
e^{-(1-2\rho)/c_0}
=(2D/\delta)^{-2}.
\]

Therefore

\[
\frac D\delta(1+c_0)e^{-(1-2\rho)/c_0}
<
\frac D\delta\,2\,(2D/\delta)^{-2}
=
\frac\delta{2D}
\le\frac12.
\]

So `(4)` holds with slack. This coefficient is deliberately conservative; it is only a uniform linear lower bound, not an optimal cutoff.

At `rho=0`, AF-440 gives the sharper exact reciprocal-square cutoff

\[
Dm\le\delta(2N-1).
\]

The present tail estimate sacrifices that sharp constant in exchange for robustness over a whole jitter tube.

## Why latent jitter immediately restores the AF-439 fiber

The positive theorem above depends on one fact that is easy to miss: the support skeleton `r` is part of the retained output. If two candidates may change their support independently while the compression keeps only finitely many moments, the earlier-shell cancellation in `(1)` disappears.

AF-439 gives the exact local obstruction. Fix any `N+1` distinct integer shells

\[
j_0,\ldots,j_N\ge2,
\qquad
x_k=j_k^{-2}.
\]

The monic polynomial with roots `x_k` has elementary symmetric coefficients `e_1,...,e_{N+1}`. Varying only `e_{N+1}` leaves the first `N` power sums unchanged by Newton identities while moving every root. Thus there is a nonconstant local family

\[
x_k(\tau),
\qquad x_k(0)=j_k^{-2},
\]

such that

\[
\sum_{k=0}^{N}x_k(\tau)^\ell
=
\sum_{k=0}^{N}x_k(0)^\ell,
\qquad
1\le\ell\le N.
\tag{9}
\]

Set

\[
r_{j_k}(\tau):=x_k(\tau)^{-1/2}
\]

and leave every unselected shell unchanged. The map `x -> x^{-1/2}` is continuous near each positive `j_k^{-2}`. Hence for **every** prescribed `rho>0`, after shrinking the nonzero parameter `tau` if necessary,

\[
|r_{j_k}(\tau)-j_k|<\rho
\]

for all selected shells. The shell intervals remain disjoint when `rho<1/2`, so the perturbed support remains ordered.

Equation `(9)` then says exactly that the first `N` coordinates of `U_N` are unchanged. Meanwhile every selected Stieltjes term is

\[
\frac{x_k(\tau)}{1-zx_k(\tau)}
=
\frac1{r_{j_k}(\tau)^2-z},
\]

so the pole moves but its residue remains `-1`.

Therefore no positive jitter radius, however small, makes the **unmarked** finite moment prefix injective on a source class that permits independent continuous shell movement. This is an identifiability failure, not a conditioning statement.

## Provenance is the load-bearing resource

The two halves isolate a precise representation boundary.

If the support coordinates are retained, the compression forgets only the mark sequence. The high-order reciprocal weights then form a finite tail-dominating code, and a uniform initial segment of marks survives even when the retained support is not exactly the integer lattice.

If the support coordinates are discarded, continuous node freedom provides `N+1` variables against `N` moment constraints. The Newton/Prony fiber then passes through the Euler source inside every open jitter tube.

So “support known approximately” is not one mathematical condition. There are two distinct information structures:

1. the actual perturbed support is **marked/retained**, although it belongs to a known uncertainty tube; or
2. only the tube is known and the actual support is **latent**, so competing sources may choose different points inside it.

The first admits exact partial recovery; the second is already nonidentified at finite depth.

This gives a concrete Arithmetic Fidelity instance of a broader principle already suggested by marked-spectrum and relational-lift results in this line: uncertainty in a retained coordinate can be much less destructive than forgetting that coordinate and later trying to reconstruct it from a compressed invariant.

## Prior-art and novelty audit

The ingredients are classical, and no novelty is claimed for them.

The marked-support argument is a robust form of the superincreasing/greedy-decoding principle already used in AF-440. Superincreasing knapsacks and their lexicographic/greedy structure are standard; a modern reference is:

- Akshay Gupte, **“Convex hulls of superincreasing knapsacks and lexicographic orderings,”** *Discrete Applied Mathematics* 201, 150–163 (2016), DOI `10.1016/j.dam.2015.08.010`.

Interval uncertainty in knapsack weights is also an established robust-optimization topic. For example:

- Michele Monaci and Ulrich Pferschy, **“On the Robust Knapsack Problem,”** *SIAM Journal on Optimization* 23(4), 1956–1982 (2013), DOI `10.1137/120880355`.

That literature studies feasibility/optimization under uncertain item weights, not the marked-versus-latent finite-moment fidelity question here; it is cited as neighboring language rather than as a theorem source for `(1)`–`(7)`.

The unmarked-support obstruction is the classical truncated-moment/Newton/Prony phenomenon specialized in AF-439. Finite atomic recovery from moments and the role of support separation are standard Prony theory; for example:

- Stefan Kunis, Thomas Peter, Tim Römer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490, 31–47 (2016), DOI `10.1016/j.laa.2015.10.023`.

No claim is made that marked coordinates, interval robustness, superincreasing decoding, Newton fibers, or separated-support Prony recovery are new theories. The contribution recorded here is the exact boundary at the AF-439/AF-440 frontier: inside the same arbitrarily thin reciprocal-square jitter tube, finite-prefix behavior changes from local nonidentifiability to linearly deep exact mark recovery depending on whether support provenance is retained by the compression.

## Boundaries and falsification checks

- The marked theorem retains the **actual** jittered skeleton `r`, not merely the interval label `[m-rho,m+rho]`. It is therefore a sufficient provenance lift, not a proof that coarse interval labels alone suffice.
- The latent negative theorem allows competing sources to choose different support positions inside the same jitter tube. It does not contradict recovery conditional on a shared retained support.
- The restriction `rho<1/2` guarantees disjoint shell intervals and a canonical shell ordering. It is a clean sufficient regime, not a claimed sharp threshold for every possible marked model.
- Criterion `(2)` is sufficient, not necessary. The integral bound is intentionally simple and may underestimate the true recoverable depth.
- The linear coefficient from `(5)` is conservative. AF-440 is sharper at `rho=0`.
- Exact mark recovery can coexist with very poor conditioning: the separation margin in `(1)` may be extremely small as `m` and `N` grow. Noise tolerance remains a separate quantitative problem.
- The alphabet is finite and separated. Continuous mark amplitudes have `delta=0`, so this dominance proof supplies no exact mark discrimination.
- The theorem does not identify the jittered support from the moment once that support is discarded. AF-439 shows the opposite for every finite prefix.
- Retaining the full support skeleton may be more side information than an RH-facing construction can canonically justify. A genuine downstream application must explain why this provenance survives naturally rather than insert it as an auxiliary label.
- Nothing here distinguishes rational primes, constrains nontrivial zeta zeros, or implies RH. The result is a finite-data representation theorem for the Euler reciprocal-square shell carrier.

A direct falsification of the marked statement would require one retained support skeleton in the declared jitter tube and two alphabet mark sequences with equal `M_N` whose first differing shell satisfies `(2)`. Inequalities `(1)` and `(8)` rule this out. A falsification of the latent statement would require injectivity of `U_N` on some positive open jitter tube, contradicting the explicit AF-439 Newton family after restricting its parameter sufficiently.

## Consequence for the research line

The AF-439/AF-440 boundary is now sharper. The next question should not be phrased only as “how much support jitter is allowed?” The correct question is **which support information survives the compression**.

Exact support coordinates are not needed for a uniform linear-depth mark theorem: a continuously jittered skeleton is compatible with recovery when that skeleton remains marked. Conversely, arbitrarily tiny latent support freedom is enough to restore exact finite-prefix collision fibers.

The next minimal-lift problem is therefore to weaken the support mark itself. Candidate tests include retaining only interval/cell identity, relative ordering plus quantitative separation, a low-dimensional deformation law, or another canonical provenance summary, and asking whether any of those coarser lifts still make finite moment fibers target-pure. Only after such an identifiability theorem should noisy Padé/Prony/Stieltjes conditioning be priced on that source class.