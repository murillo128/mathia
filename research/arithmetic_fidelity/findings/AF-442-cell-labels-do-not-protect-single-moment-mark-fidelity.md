# AF-442 — Cell labels do not protect single-moment mark fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `MINIMAL-LIFT-OBSTRUCTION`, `FINITE-MOMENT-NONIDENTIFIABILITY`, `CLASSICAL-PRONY-GEOMETRY`, `NO-NOVELTY-CLAIM`

## Claim

AF-440 proves that one sufficiently high reciprocal-square moment recovers a linearly growing prefix of discrete shell marks when the support skeleton is fixed exactly. AF-441 shows that this positive result remains uniform under support jitter if the *realized support coordinates themselves* are retained, while unmarked finite moment prefixes recover collision fibers as soon as support coordinates become latent.

The next proposed weakening in AF-441 was to retain only shell/cell provenance rather than the realized support coordinate. That weakening already fails for the same single high-order scalar moment used by the positive recovery theorem.

Fix

\[
0<\rho<\frac12,
\qquad
I_k=[k-\rho,k+\rho],
\]

and let `A\subset\mathbb R` be a finite alphabet with at least two values. Choose any nonzero `\alpha\in A`, two distinct marks `u,v\in A`, and shells `1\le j<m`. Put

\[
\Delta:=v-u\ne0,
\qquad s:=2N.
\]

Consider source configurations with one support point `r_k\in I_k` in every shell and mark `a_k\in A`, observed only through the shell labels together with the scalar moment

\[
M_N(r,a)=\sum_{k\ge1}a_k r_k^{-2N}.
\]

Then for every `\rho>0` there is `N_0` such that for every `N\ge N_0` one can find two admissible configurations `(r,a)` and `(\widetilde r,b)` satisfying:

- `r_k,\widetilde r_k\in I_k` for every `k`, so the retained shell/cell provenance is identical;
- `a_k=b_k` for every `k\ne m`, while `a_m=u` and `b_m=v`;
- `r_k=\widetilde r_k` for every `k\ne j`;
- the earlier mark is shared and nonzero, `a_j=b_j=\alpha`;
- nevertheless

\[
\boxed{M_N(r,a)=M_N(\widetilde r,b).}
\tag{1}
\]

Moreover the required support displacement is exponentially small in `N`. Taking `r_k=k` and defining

\[
q_N:=\frac{\Delta}{\alpha}\left(\frac jm\right)^{2N},
\]

one exact compensating choice is

\[
\boxed{
\widetilde r_j
=j(1-q_N)^{-1/(2N)},
}
\tag{2}
\]

for all sufficiently large `N`, and therefore

\[
\boxed{
\widetilde r_j-j
\sim
\frac{j}{2N}\frac{\Delta}{\alpha}
\left(\frac jm\right)^{2N}.
}
\tag{3}
\]

Thus retaining only interval/cell identity is not enough to inherit AF-440's high-moment mark recovery. A later discrete mark change can be hidden exactly by an arbitrarily small latent displacement of one earlier support point inside its already-known cell.

## Exact two-coordinate compensation

Take a baseline support skeleton `r_k=k`. Let the two mark sequences agree everywhere except at shell `m`, where

\[
a_m=u,
\qquad
b_m=v=u+\Delta.
\]

At the earlier shell `j`, give both sources the same nonzero mark `\alpha`. Keep every support coordinate fixed except the second source's `j`-th coordinate.

Equality of moments is equivalent to

\[
\alpha j^{-s}+u m^{-s}
=
\alpha\widetilde r_j^{-s}+(u+\Delta)m^{-s},
\]

or

\[
\widetilde r_j^{-s}
=j^{-s}-\frac{\Delta}{\alpha}m^{-s}.
\tag{4}
\]

Factoring out `j^{-s}` gives

\[
\widetilde r_j^{-s}
=j^{-s}(1-q_N),
\]

which yields `(2)` whenever `1-q_N>0`.

Because `j<m`, one has

\[
\left|q_N\right|
=
\left|\frac{\Delta}{\alpha}\right|
\left(\frac jm\right)^{2N}
\longrightarrow0.
\]

Hence `(2)` is well-defined for every sufficiently large `N`, and `\widetilde r_j\to j`. For any prescribed positive `\rho`, eventually

\[
|\widetilde r_j-j|<\rho.
\]

All other support points remain at their integer centers, so both sources retain exactly the same shell labels. Since `\rho<1/2`, shell intervals are disjoint and the support ordering remains canonical.

Equation `(4)` is precisely the equality needed to cancel the later mark change, while every unchanged coordinate cancels term by term. This proves `(1)` exactly.

## Exponential compensation scale

For `q_N\to0`,

\[
(1-q_N)^{-1/(2N)}
=
\exp\!\left(-\frac1{2N}\log(1-q_N)\right)
=
1+\frac{q_N}{2N}+o\!\left(\frac{|q_N|}{N}\right).
\]

Substitution gives `(3)`.

The sign of the support movement is the sign of `\Delta/\alpha`: if the later mark adds positive mass relative to the earlier nonzero mark, the earlier support moves outward and its contribution decreases; if the sign is reversed, it moves inward. Because each shell interval contains a two-sided neighborhood of its center, either direction is admissible once `N` is large enough.

For the binary alphabet `A=\{0,1\}`, choose

\[
\alpha=1,
\qquad u=0,
\qquad v=1.
\]

Then the collision has the especially transparent form

\[
\widetilde r_j
=
j\left(1-\left(\frac jm\right)^{2N}\right)^{-1/(2N)},
\]

with

\[
\widetilde r_j-j
\sim
\frac{j}{2N}\left(\frac jm\right)^{2N}.
\tag{5}
\]

So even in the exact binary occupancy class underlying AF-440, every fixed positive shell uncertainty eventually contains an exact collision that hides a later occupancy change from the single high moment.

## Why high order helps one model and hurts the other

The marked-support theorem in AF-441 compares two mark sequences on one *shared retained skeleton*. Earlier shells then cancel exactly, and the high-order reciprocal weights become superincreasing enough to protect a growing mark prefix.

With only cell labels retained, competing sources may realize different coordinates inside the same earlier cell. The high-order weight hierarchy now creates a different effect. Since `j<m`, the sensitivity of the moment to the earlier support point is much larger than the contribution of the later shell. The later mark contribution has size proportional to `m^{-2N}`, while differentiating the earlier term gives scale

\[
2N|\alpha|j^{-2N-1}.
\]

Their ratio is of order

\[
\frac{j}{2N}\left(\frac jm\right)^{2N},
\]

which is exactly the displacement scale in `(3)`.

Thus increasing `N` simultaneously strengthens fixed-support mark separation and makes the compensating latent support displacement exponentially smaller. The high-order moment does not restore forgotten provenance; it amplifies the leverage of an earlier unknown node enough to absorb a later discrete mark change inside an arbitrarily narrow cell.

## Relation to AF-439, AF-440, and AF-441

AF-439 establishes positive-dimensional equi-moment fibers when enough support coordinates are free and a finite prefix of moments is retained. AF-441 imports that obstruction into arbitrarily thin reciprocal-square jitter tubes for the *support-only* finite prefix `U_N`.

The present result is different in two ways. It keeps the discrete mark variable that AF-440 is trying to recover, and it needs only one latent support coordinate because it targets the one scalar high moment that powers AF-440's strongest finite-depth certificate. The collision is explicit rather than obtained from a dimension count or implicit-function argument.

This closes one of AF-441's proposed minimal-lift tests:

\[
\boxed{
\text{shell/cell identity without realized support position}
\quad\not\Rightarrow\quad
\text{single-high-moment mark fidelity}.
}
\tag{6}
\]

It does **not** show that cell labels fail for every richer compression. Several independent moments can constrain one movable support coordinate, and additional deformation laws or relational data may restore identifiability. The obstruction is specifically to transferring the AF-440/AF-441 single-moment recovery mechanism to a source class where actual support locations are latent inside their cells.

## Prior-art and novelty audit

Unknown-node/unknown-amplitude moment inversion is classical Prony territory. The general fact that fixing too few moments leaves equi-moment parameter families is standard; modern geometric treatments explicitly describe such sets as Prony leaves or equi-moment varieties. See Dmitry Batenkov, Gil Goldman, Yehonatan Salman, and Yosef Yomdin, **“Algebraic Geometry of Error Amplification: the Prony leaves,”** arXiv:1702.05338 (2017), and the related Prony-variety literature.

Local sensitivity and instability of Prony inversion with movable nodes are likewise established prior art. See Dmitry Batenkov and Yosef Yomdin, **“On the accuracy of solving confluent Prony systems,”** *SIAM Journal on Applied Mathematics* 73(1), 134–154 (2013), DOI `10.1137/110836584`, arXiv:1106.1137. For a broader geometric treatment, see Dmitry Batenkov and Yosef Yomdin, **“Local and global geometry of Prony systems and Fourier reconstruction of piecewise-smooth functions,”** in *Operator-Related Function Theory and Time-Frequency Analysis*, Abel Symposia 9, 57–76 (2015), DOI `10.1007/978-3-319-08557-9_2`, arXiv:1301.1187.

The exact two-coordinate calculation `(2)` is elementary and no novelty is claimed for the underlying inverse-problem mechanism. The Arithmetic Fidelity contribution recorded here is the placement and quantitative scale of that classical ambiguity at the AF-440/AF-441 boundary: on the reciprocal-square shell carrier, retaining cell provenance but forgetting the realized node already permits an exact occupancy collision, and the compensating movement decays like `(j/m)^{2N}/N`.

This also separates the present claim from near-collision super-resolution results, which study stable recovery from richer spectral data. Here the issue is exact noninjectivity of one scalar compressed observable on a source class with one latent node coordinate, not noisy reconstruction from a sufficiently informative measurement family.

## Boundaries and falsification checks

- The theorem is an **existence obstruction** on the admissible source class. It does not say every mark change can be hidden from every baseline source.
- A shared earlier nonzero mark `\alpha` is required. Every finite alphabet with at least two values contains at least one nonzero value, so such sources exist, but a particular source with all earlier marks zero may not admit this two-coordinate compensation.
- The support uncertainty must contain a two-sided neighborhood of the nominal shell point. The stated symmetric cells provide that. One-sided constraints require matching the sign of the permitted support movement.
- The result concerns the single scalar `M_N`. It does not prove equality of the whole prefix `(M_1,\ldots,M_N)`.
- The collision preserves shell labels and order but not the realized support skeleton. Therefore it does not contradict AF-441's positive marked-support theorem.
- The displacement tends to zero exponentially for fixed `j<m`; this is an exact identifiability statement, not merely a conditioning estimate.
- The proof allows arbitrary unchanged tails because they cancel identically between the two sources.
- Nothing here distinguishes rational primes, constrains zeta zeros, or implies RH. The theorem isolates a representation-level provenance requirement for the reciprocal-square Euler-style carrier.

A direct falsification would require a positive `\rho`, fixed `j<m`, and arbitrarily large `N` for which the explicit coordinate `(2)` either leaves `I_j` or fails to satisfy `(4)`. Convergence `q_N\to0` places `(2)` inside `I_j` eventually, and substitution into `(4)` proves the equality algebraically.

## Consequence for the research line

The minimal-lift search should no longer treat shell identity or a narrow uncertainty interval as a plausible substitute for retaining the realized support coordinate when the downstream observable is a single high-order moment. **Provenance at cell resolution is too coarse.**

The remaining constructive question is sharper: what information weaker than the full realized skeleton but stronger than cell identity prevents these support/mark trades? Natural candidates include a low-dimensional deformation law tying support motions together, several independent moments whose Jacobian removes the one-node compensation, or relational support data that makes the realized coordinates recoverable without storing them explicitly.

Any such lift should be tested against explicit compensated collisions before being credited with arithmetic fidelity.