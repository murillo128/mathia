# AF-306 — Saturated prime fibers lose stable zero margin before exact zero fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SATURATED-DISCRETE-SOURCES`, `KRONECKER-WEYL`, `PRIME-NUMBER-THEOREM`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-305 isolates the exact saturation boundary `k alpha=1`: every admissible source becomes the uniform measure on a `k`-subset, so the continuous barycentric perturbations used in AF-303--AF-305 disappear. Saturation really does change the exact zero problem, but it does **not** restore quantitative zero-margin fidelity.

For a finite `k`-set `A` of rational primes define the saturated equal-weight Dirichlet polynomial

\[
P_A(s)=\frac1k\sum_{p\in A}p^{-s}
\]

and its scale-free pointwise zero margin on the vertical line `Re(s)=sigma` by

\[
\mu_A(\sigma,t)
=
\frac{\left|\sum_{p\in A}p^{-\sigma-it}\right|}
{\sum_{p\in A}p^{-\sigma}}
\in[0,1].
\tag{1}
\]

Then for every integer `k>=2`, every real `sigma`, every `epsilon>0`, and every height threshold `H>0`, there exist disjoint `k`-sets `A,B` of rational primes and a height `t>H` such that

\[
\boxed{
\mu_A(\sigma,t)<\epsilon,
\qquad
\mu_B(\sigma,t)>1-\epsilon.
}
\tag{2}
\]

The two saturated sources can be placed in the same coordinate-deletion fiber by deleting `A union B`, so both retained states are exactly zero. Hence no positive compression-only modulus can separate "near a zero" from "maximally far from a zero" uniformly on the saturated source family. The loss survives even though coefficient freedom has vanished completely.

On the imaginary axis the exact and quantitative questions separate already at the first genuinely discrete case. If `A={p,q,r}` consists of three distinct rational primes, then

\[
\boxed{
P_A(it)\ne0
\quad\text{for every real }t,
}
\tag{3}
\]

but nevertheless

\[
\boxed{
\inf_{t\in\mathbb R}|P_A(it)|=0,
}
\tag{4}
\]

and the infimum is approached at arbitrarily large heights.

Thus a saturated three-prime source is **exactly zero-free on `Re(s)=0` while having no positive zero margin at all**. Exact factorization of the binary point-zero discriminator can therefore coexist with complete failure of stable recovery of distance to the zero set.

This is the categorical distinction left implicit by AF-305: discreteness can remove exact cancellations without supplying a quantitative buffer against them.

## Simultaneous near-zero and near-maximal saturated supports

Fix `k>=2`, `sigma in R`, `epsilon>0`, and `H>0`.

Choose a small relative width `eta>0`. The prime number theorem implies that for all sufficiently large `X`, the interval

\[
[X,(1+\eta)X]
\]

contains at least `2k` rational primes. Choose distinct primes

\[
p_1,\ldots,p_k,q_1,\ldots,q_k
\]

from one such interval and set

\[
A=\{p_1,\ldots,p_k\},
\qquad
B=\{q_1,\ldots,q_k\}.
\]

Write the normalized radial weights

\[
a_j
=
\frac{p_j^{-\sigma}}
{\sum_{m=1}^k p_m^{-\sigma}},
\qquad
b_j
=
\frac{q_j^{-\sigma}}
{\sum_{m=1}^k q_m^{-\sigma}}.
\tag{5}
\]

Because all primes lie in the same fixed relative interval, choosing `eta` sufficiently small makes the `a_j` uniformly close to `1/k`. More precisely,

\[
\sum_{j=1}^k\left|a_j-\frac1k\right|
\longrightarrow0
\qquad(\eta\downarrow0)
\tag{6}
\]

uniformly in the scale `X`; the same holds for `b_j`.

Let

\[
\zeta_j=e^{2\pi i(j-1)/k},
\qquad
1\le j\le k,
\]

so that

\[
\sum_{j=1}^k\zeta_j=0.
\tag{7}
\]

The logarithms of the `2k` distinct primes are linearly independent over `Q`. Indeed, an integer relation among them would exponentiate to a nontrivial multiplicative relation among distinct primes, contradicting unique factorization. Therefore the continuous Kronecker-Weyl theorem makes

\[
t\mapsto
\bigl(
-t\log p_1,\ldots,-t\log p_k,
-t\log q_1,\ldots,-t\log q_k
\bigr)
\pmod{2\pi}
\tag{8}
\]

dense in the full torus `T^{2k}`. Every nonempty open phase cell is hit at arbitrarily large positive times.

Choose such a time `t>H` for which simultaneously

\[
|p_j^{-it}-\zeta_j|<\rho,
\qquad
|q_j^{-it}-1|<\rho
\tag{9}
\]

for all `j`, where `rho>0` will be chosen small.

For the cancelling support,

\[
\begin{aligned}
\mu_A(\sigma,t)
&=
\left|\sum_{j=1}^k a_j p_j^{-it}\right|\\
&\le
\left|\sum_{j=1}^k a_j(p_j^{-it}-\zeta_j)\right|
+
\left|\sum_{j=1}^k\left(a_j-\frac1k\right)\zeta_j\right|
+
\left|\frac1k\sum_{j=1}^k\zeta_j\right|\\
&\le
\rho
+
\sum_{j=1}^k\left|a_j-\frac1k\right|.
\end{aligned}
\tag{10}
\]

Choose first `eta` and then `rho` so that the right side is below `epsilon`.

For the aligned support,

\[
\begin{aligned}
\mu_B(\sigma,t)
&=
\left|\sum_{j=1}^k b_j q_j^{-it}\right|\\
&\ge
1-
\left|\sum_{j=1}^k b_j(q_j^{-it}-1)\right|\\
&>
1-\rho.
\end{aligned}
\tag{11}
\]

Taking `rho<epsilon` proves (2).

No source coefficient has been adjusted: every nonzero coefficient is exactly `1/k`. The only freedoms are the discrete choice of support and the common observation height.

## Same compression fiber and quantitative failure

Let the coordinate-deletion map discard every coordinate in `A union B`. For the two saturated source vectors

\[
c_A=\frac1k\mathbf 1_A,
\qquad
c_B=\frac1k\mathbf 1_B,
\]

one has

\[
q_D(c_A)=q_D(c_B)=0.
\tag{12}
\]

Yet their normalized margins satisfy (2). Therefore the oscillation of the zero-margin observable on a single compression fiber can be made arbitrarily close to its full possible diameter:

\[
\sup_{c,c'\in q_D^{-1}(0)}
|\mu_c(\sigma,t)-\mu_{c'}(\sigma,t)|
>1-2\epsilon.
\tag{13}
\]

Consequently no recovery `R` depending only on the retained coordinate state can approximate `mu` uniformly with error below `1/2` over the whole saturated family: for any proposed scalar output `R(0)`, one of the two sources in (2) has error at least

\[
\frac{\mu_B-\mu_A}{2}
>
\frac{1-2\epsilon}{2}.
\tag{14}
\]

Letting `epsilon downarrow0` gives the minimax lower bound `1/2` for any compression-only scalar reconstruction of this normalized margin over the family. More importantly for zero-sensitive arguments, there is no positive uniform lower bound on `mu` even though all source coefficients are discrete and fixed.

This is a stable-fidelity obstruction, not yet an exact zero/safe collision.

## Three equal prime terms never vanish on the imaginary axis

Now specialize to

\[
k=3,
\qquad
\sigma=0,
\qquad
A=\{p,q,r\}
\]

with distinct rational primes.

Suppose for contradiction that

\[
p^{-it}+q^{-it}+r^{-it}=0
\tag{15}
\]

for some real `t`. The three summands have unit modulus. Three unit complex numbers can sum to zero only when they are the vertices of a rotated equilateral triangle. Hence, after dividing by one term, the two phase ratios are the two primitive cube roots of unity. In particular there are integers `m,n` and signs such that

\[
t\log(q/p)=2\pi\left(m\pm\frac13\right),
\qquad
 t\log(r/p)=2\pi\left(n\mp\frac13\right).
\tag{16}
\]

Neither right side is zero. Dividing the two equations gives

\[
\frac{\log(q/p)}{\log(r/p)}\in\mathbb Q.
\tag{17}
\]

Clearing denominators in (17) yields a nonzero integer relation among

\[
\log p,\log q,\log r,
\]

which exponentiates to a nontrivial multiplicative relation among the three distinct primes. Unique factorization forbids this. Thus (15) is impossible, proving (3).

The obstruction is specific to **exact** phase closure: the Kronecker orbit is dense but does not hit the equilateral phase point.

## The same three-prime polynomial approaches zero arbitrarily closely

For the same fixed triple `A={p,q,r}`, rational independence of

\[
\log p,\log q,\log r
\]

makes the phase orbit

\[
t\mapsto(p^{-it},q^{-it},r^{-it})
\]

dense in `T^3`. In particular it approaches arbitrarily closely any rotated equilateral triple. Therefore, for every `epsilon>0` and every `H>0`, there exists `t>H` such that

\[
\left|
\frac13\left(p^{-it}+q^{-it}+r^{-it}\right)
\right|<\epsilon.
\tag{18}
\]

Combined with (3), this proves (4) and shows that the infimum is never attained.

The distinction is exact:

\[
\text{zero set empty}
\quad\text{but}\quad
\operatorname{dist}(0,P_A(i\mathbb R))=0.
\tag{19}
\]

A binary zero indicator therefore factors trivially on this source class, while every positive quantitative zero-separation margin fails.

## Prior art and novelty assessment

No novelty claim is made for the ingredients.

- Kronecker-Weyl density for continuous torus flows is classical. Alexandre Bailleul, *Explicit Kronecker-Weyl theorems and applications to prime number races*, Research in Number Theory 8 (2022), Article 43, arXiv:`2007.05763`, gives explicit modern formulations. AF-303 already uses the same theorem for rational-prime logarithms.
- Dirichlet polynomials on vertical lines are classical almost-periodic trigonometric polynomials. The general Bohr/almost-periodic framework explains why torus phase closures are the natural value-set compactifications; the present proof needs only finite-dimensional Kronecker-Weyl.
- The prime number theorem supplies arbitrarily many primes in every fixed relative interval `[X,(1+eta)X]` for sufficiently large `X`, exactly as in AF-303.
- The geometry of three unit vectors summing to zero and the unique-factorization proof of rational independence of prime logarithms are elementary.

The durable Arithmetic Fidelity content is therefore not a new theorem about almost periodic functions. It is the precise diagnosis of the **saturated source boundary isolated by AF-305**: removing all continuous barycentric freedom can restore exact zero-freeness while leaving the target arbitrarily ill-conditioned. Exact discriminator fidelity and stable discriminator fidelity are different resources.

## Boundaries and failure modes

- Equation (2) is a family-level quantitative obstruction. For `sigma!=0`, comparable prime blocks are chosen so their radial weights are close enough to equal for regular-polygon phase cancellation to approximate zero.
- The theorem proves arbitrarily small normalized margin, not an exact zero, for the general saturated family. It must not be used as an exact zero-count collision.
- The exact nonvanishing statement (3) is proved only for three distinct rational-prime terms on `Re(s)=0`. It does not classify exact zeros for `k>=4` or for `sigma!=0`.
- The compression used for (12) deletes the entire chosen support. A source law forcing retained common coordinates may change the fiber geometry.
- A compact height window can avoid the recurrent dangerous phase cells. The obstruction is uniform over unbounded height.
- The normalized margin in (1) is target-specific. A downstream theorem insensitive to small pointwise values may not require this resource.
- The result does not supply analytic continuation, a global zero count, a zeta approximation theorem, or an RH implication.

## Consequence for the research line

AF-305 left exact saturation `k alpha=1` as the first source class where the previous continuous collision mechanisms genuinely stop. AF-306 shows that this boundary must now split into two questions.

For **exact zero fidelity**, the discrete support combinatorics matter and can genuinely remove zeros: a three-prime equal-weight polynomial has no imaginary-axis zero at all.

For **stable zero fidelity**, saturation is already insufficient. Kronecker recurrence drives equal-weight prime supports arbitrarily close to cancelling phase configurations, and two supports in the same deletion fiber can simultaneously realize margins arbitrarily near `0` and `1`.

The next honest saturated-source question is therefore not merely whether two uniform supports can produce an exact zero/safe collision. One must first declare which downstream theorem needs exact zero membership and which needs a positive conditioning margin. Any RH mechanism that transports a zero-sensitive statement through this compression must price the required margin explicitly; discreteness alone cannot supply it.