# FD-173 — Prime-power annulus hitting exactly classifies sparse midpoint target-rigidity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted temporal acquisition / exact sparse-horizon classification / prime-power recurrence / target-rigidity
- **Depends on:** FD-170, FD-171, FD-172
- **Classification:** `EXACT-DERIVED + SOURCE-RESTRICTED + NECESSARY-AND-SUFFICIENT + SPARSE-ACQUISITION + TARGET-RIGIDITY`

## Claim

`FD-172` proves that dyadic midpoint horizons rigidify the Möbius target inside the multiplicative squarefree source class. The dyadic cover is sufficient but not the exact condition. The exact obstruction is whether an odd prime has an entire **prime-power orbit** that avoids every observed multiplicative annulus.

Let `a` be multiplicative and satisfy

\[
a(1)=1,
\qquad
a(p^r)=0\quad(r\ge2),
\qquad
-1\le a(p)\le1\quad(p\text{ prime}).
\tag{1}
\]

For integer horizons `H>=2`, write

\[
P_a(H):=\mathcal D_{H,a}(1/2),
\qquad
E_H:=P_a(H)-P_\mu(H).
\tag{2}
\]

Let `\mathcal H` be a nonempty set of observed horizons and define its multiplicative-annulus union

\[
U(\mathcal H)
:=
\bigcup_{H\in\mathcal H}(H/2,H].
\tag{3}
\]

Then the following are equivalent:

1. every source satisfying (1) and
   \[
   E_H=0\qquad(H\in\mathcal H)
   \tag{4}
   \]
   is exactly `mu`;
2. for every odd prime `p`, at least one positive power of `p` lies in the observed annulus union:
   \[
   \boxed{
   \forall p\ge3\text{ prime}\quad
   \exists j\ge1:\ p^j\in U(\mathcal H).
   }
   \tag{5}
   \]

Thus sparse midpoint target-rigidity is characterized exactly by **prime-power annulus hitting**. Covering every prime itself is sufficient but unnecessarily strong; a missed prime can still be detected later through one of its higher powers in the midpoint transform.

The same criterion inherits the stability modulus of `FD-172`. If (5) holds and

\[
\sup_{H\in\mathcal H}|E_H|\le\varepsilon,
\tag{6}
\]

then every prime satisfies

\[
\boxed{0\le1+a(p)\le2\varepsilon.}
\tag{7}
\]

For `epsilon<=1/2`, every squarefree `n` therefore obeys

\[
|a(n)-\mu(n)|\le2\varepsilon\,\omega(n),
\tag{8}
\]

and both sides vanish on nonsquarefree `n`.

A notable corollary is that **every fixed integer geometric ladder is target-rigid**:

\[
\boxed{
\mathcal H_B=\{B,B^2,B^3,\ldots\},\quad B\in\mathbb Z,\ B\ge2,
}
\tag{9}
\]

satisfies (5). Hence multiplicative gaps may be arbitrarily large: dyadic bounded-gap coverage is not necessary for exact infinite-horizon rigidity.

## 1. Exact zero error annihilates an entire observed annulus

Use the same transformed source as `FD-172`,

\[
u(n):=1_{2\nmid n},
\qquad
F:=u*a,
\tag{10}
\]

and define its odd prefix

\[
A(x):=\sum_{\substack{m\le x\\m\text{ odd}}}F(m).
\tag{11}
\]

For every odd `m`, squarefree multiplicativity gives

\[
F(m)=\prod_{p\mid m}(1+a(p))\ge0,
\tag{12}
\]

while the exact midpoint identity of `FD-172` is

\[
\boxed{
-2E_H
=
\bigl(A(H)-A(H/2)\bigr)
 +(1+a(2))A(H/2).
}
\tag{13}
\]

Both terms are nonnegative. Also `A(H/2)>=F(1)=1` for every `H>=2`. Consequently, if `E_H=0`, then necessarily

\[
a(2)=-1
\tag{14}
\]

and

\[
A(H)-A(H/2)=0.
\tag{15}
\]

Because (15) is a sum of nonnegative coefficients, it is stronger than a scalar cancellation statement:

\[
\boxed{
F(m)=0
\qquad
\text{for every odd integer }m\in(H/2,H].
}
\tag{16}
\]

In particular, whenever `p^j` belongs to the annulus,

\[
0=F(p^j)=1+a(p),
\tag{17}
\]

so that prime amplitude is forced to its Möbius value.

This is why higher powers matter even though the original source is squarefree-supported. The convolution `F=u*a` repeats the local prime defect `1+a(p)` at **every** positive power `p^j`.

## 2. Prime-power hitting is sufficient

Assume (5) and exact agreement (4). Since `\mathcal H` is nonempty, applying (13) at any observed horizon gives `a(2)=-1`.

Now fix an odd prime `p`. By (5), choose an observed `H` and `j>=1` with

\[
H/2<p^j\le H.
\tag{18}
\]

Equation (16) gives `F(p^j)=0`, and (17) therefore gives

\[
a(p)=-1.
\tag{19}
\]

This holds for every prime. Multiplicativity and squarefree support then force

\[
a(n)=\mu(n)
\qquad(n\ge1).
\tag{20}
\]

So (5) implies target-rigidity.

The same proof is quantitative. From (13), for every observed `H`,

\[
0\le1+a(2)
\le -2E_H,
\tag{21}
\]

and for every odd prime power `p^j\in(H/2,H]`,

\[
0\le1+a(p)=F(p^j)
\le A(H)-A(H/2)
\le -2E_H.
\tag{22}
\]

Since admissible sources always have `E_H<=0`, the uniform error bound (6) gives (7), and the coefficient estimate (8) follows exactly as in `FD-172`.

## 3. Missing one complete prime-power orbit is also necessary

Suppose instead that (5) fails. Then some odd prime `p` satisfies

\[
p^j\notin U(\mathcal H)
\qquad(j\ge1).
\tag{23}
\]

Construct a single permanent admissible source by setting

\[
a_p(2)=-1,
\qquad
a_p(p)=0,
\qquad
a_p(q)=-1\quad(q\ne p\text{ prime}),
\tag{24}
\]

and extending multiplicatively with squarefree support. This source belongs to (1) and differs from Möbius already at `p`.

For its transformed odd coefficients, equation (12) becomes

\[
F_p(m)
=
\begin{cases}
1,&m=p^j\text{ for some }j\ge0,\\
0,&\text{otherwise},
\end{cases}
\tag{25}
\]

where `j=0` is the coefficient at `m=1`. Because `a_p(2)=-1`, the second term of (13) vanishes. For every observed `H>=2`, the coefficient at `1` is below the open annulus, so

\[
-2E_H
=A(H)-A(H/2)
=
\#\{j\ge1:H/2<p^j\le H\}.
\tag{26}
\]

Condition (23) makes the right-hand side zero for every `H\in\mathcal H`. Hence

\[
P_{a_p}(H)=P_\mu(H)
\qquad(H\in\mathcal H),
\tag{27}
\]

while `a_p\ne\mu`. This proves necessity and gives an explicit invisible source for every failure of the hitting condition.

The classification is therefore exact: there are no other sparse-horizon obstructions inside the class (1).

## 4. Arbitrarily sparse geometric ladders still hit every prime-power orbit

Take a fixed integer `B>=2` and `\mathcal H_B={B^k:k>=1}`. Fix an odd prime `p` and put

\[
\alpha=\log_B p.
\tag{28}
\]

If `alpha` is rational, say `alpha=r/s`, then

\[
p^s=B^r.
\tag{29}
\]

Unique factorization forces `B` to be a power of `p`, so some positive power of `p` is itself one of the observed horizons and is therefore in `U(\mathcal H_B)`.

If `alpha` is irrational, the fractional parts `{j alpha}` are dense in the unit interval. This elementary irrational-rotation fact follows, for example, from the pigeonhole principle: arbitrarily close pairs among `0,alpha,...,N alpha (mod 1)` produce arbitrarily small nonzero rotation steps, whose repeated translates form arbitrarily fine circular nets.

Choose `j` with

\[
\{j\alpha\}>1-\log_B2.
\tag{30}
\]

With `k=ceil(j alpha)`, equation (30) is equivalent to

\[
k-\log_B2<j\alpha<k,
\tag{31}
\]

hence

\[
B^k/2<p^j<B^k.
\tag{32}
\]

Thus every odd prime-power orbit hits some observed annulus, proving (9) from the exact classification.

This is a sharper boundary than multiplicative-gap coverage. A ladder with ratio `B>2` leaves large open regions of the positive axis uncovered, but a fixed prime defect cannot stay inside those gaps forever: its powers recur through the logarithmic annulus window. Exact infinite-horizon target-rigidity can therefore survive arbitrarily large fixed multiplicative gaps.

The price is loss of locality. For `B=2`, each prime `p` is detected at a horizon below `2p`, which gave the finite-prefix statement in `FD-172`. For `B>2`, the first detected power of a given prime may occur far above `p`; the exact recurrence argument alone gives no useful uniform source-scale-to-horizon bound. Infinite exact rigidity and efficient finite-scale certification are distinct questions.

## 5. Representation audit, prior art, and boundaries

This result stays entirely inside the midpoint representation of `FD-170`--`FD-172`. It does not add a new observable. The additional step is to classify exactly which sparse time sets intersect enough of the **positive transformed defect support** to distinguish Möbius.

The generic layer is a nonnegative-measure hitting argument: exact zero on an interval sum kills every nonnegative atom in that interval. The source-specific layer is stronger and genuinely arithmetic: squarefree multiplicativity makes one prime defect reappear at the whole orbit `p,p^2,p^3,...` in `u*a`. That repetition is precisely why the correct sparse-sampling object is a prime-power orbit rather than the prime location itself.

A focused prior-art search around Farey midpoint ranks, Möbius inversion, sparse Farey sampling, multiplicative sources, and prime-power annulus observation recovered the standard midpoint symmetry/rank formulas, ordinary Dirichlet-convolution machinery, and general multiplicative-function literature, but no direct statement of this necessary-and-sufficient sparse-horizon criterion. The geometric-ladder corollary uses only the elementary density of irrational rotations and unique factorization. No new external theorem is load-bearing, so `SOURCES.md` needs no update.

The hypotheses remain decisive. Without multiplicativity or the lower bound `a(p)>=-1`, the transformed coefficients need not be nonnegative and `FD-171`-type signed pulse cancellation can return. The upper bound `a(p)<=1` is inherited from `FD-172` but is not load-bearing for the exact classification. The theorem is still target-rigidity relative to Möbius, not pairwise injectivity among arbitrary admissible sources.

Nor does sparse target-rigidity itself improve the Franel--Landau discrepancy estimate. It says which temporal observation sets identify the Möbius source once a strong source architecture is assumed; it supplies no new cancellation estimate at the RH-critical scale and no destination coercivity for the nonlocal Franel norm.

## Research consequence

`FD-172` left open a characterization of horizon sets sufficient for restricted-source midpoint rigidity. The answer is not a bounded multiplicative-gap condition. It is exactly the orbit-hitting condition (5), and that distinction matters: even the exponentially sparse ladder `B^k` works for every fixed integer `B>=2` because higher powers of each prime eventually enter one observed half-annulus.

The live finite-scale problem is now sharper. Exact infinite-horizon identifiability can be extremely sparse, while useful certification through source scale `X` depends on quantitative recurrence of the logarithmic prime orbits into the observation windows. Separately, weakening multiplicativity to squarefree/ternary sources remains open, as does pairwise sparse inversion. None of these source-identification questions substitutes for the missing bridge from coefficient coercivity to an RH-critical Franel--Landau bound.

## Related findings

- `FD-170` — consecutive midpoint horizons invert the unrestricted source through the odd-indicator convolution.
- `FD-171` — unrestricted sparse midpoint sensing has an exact permanent null direction whenever a horizon is omitted.
- `FD-172` — dyadic midpoint horizons rigidify the bounded squarefree multiplicative Möbius target with a prime-defect stability modulus.
