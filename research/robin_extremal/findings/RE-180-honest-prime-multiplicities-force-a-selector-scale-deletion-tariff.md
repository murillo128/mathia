# RE-180 — Honest prime multiplicities force a selector-scale deletion tariff

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + NONNEGATIVE-INTEGER-MULTIPLICITY + TWO-JET-MATCHING + DELETION-CARDINALITY + HYBRID-LOCAL-REMOTE-TARIFF + KV-RESET-BUDGET + ROBIN-SCALE-CONDITIONING + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-175, RE-176, RE-179.

`RE-179` reduces exact two-jet repair to a sharp dichotomy: either a Robin-scale amount of the forced negative centered workload is paid near the selector, or the remote tail carries a sufficiently large KV-weighted reset budget. Its proof intentionally allows relaxed signed integer coefficients, so the first branch is left as an unpriced escape.

For an **honest ordinary-prime multiplicity profile** that branch is not free. If

\[
m_Q(q)\in\mathbf Z_{\ge0},
\qquad
c_q:=m_Q(q)-1,
\]

then every negative coefficient is exactly

\[
c_q=-1.
\]

An ordinary prime can be deleted once, but it cannot contribute an arbitrarily large negative atom. Combining this one-sided granularity with the two-jet centered debt yields a source-specific support-size tariff.

Retain the canonical `RE-173` deletion packet

\[
D_p\subset[2p,3p],
\qquad
c_q=-1\quad(q\in D_p),
\]

with

\[
d_p:=\sum_{q\in D_p}H(q)
\asymp\frac1{\sqrt p\log p},
\qquad
H(q):=\log\frac q{q-1}.
\]

Fix `lambda>3`. Assume all modifications outside `D_p` occur at ordinary primes `q>=lambda p`, the Mertens value and first Euler boundary slope match exactly,

\[
D_Q(1+)=D_Q'(1+)=0,
\]

and the relevant boundary sums converge absolutely. Put

\[
B(q):=\frac{\log q}{q-1},
\qquad
A(q):=\frac{B(q)}{H(q)},
\qquad
a_D:=\frac{\sum_{q\in D_p}B(q)}{d_p},
\]

and

\[
K_D(q):=B(q)-a_DH(q)=H(q)(A(q)-a_D).
\]

As in `RE-179`, on `q>=lambda p`,

\[
\delta_{\lambda,p}
:=\inf_{q\ge\lambda p}(A(q)-a_D)
\ge\log(\lambda/3)-o(1)>0.
\]

Then exact two-jet matching forces

\[
\boxed{
\sum_{\substack{q\ge\lambda p\\m_Q(q)=0}}K_D(q)
\ge\delta_{\lambda,p}d_p.
}
\tag{1}
\]

For honest multiplicities each summand in (1) comes from a **distinct deleted ordinary prime**. Moreover uniformly for `q>=lambda p`,

\[
\boxed{
K_D(q)
\le
\frac{C_\lambda+o(1)}p,
\qquad
C_\lambda:=\sup_{u\ge\lambda}\frac{\log(u/2)}u
\le\frac1{2e}.
}
\tag{2}
\]

Consequently, if

\[
N_{\rm del}(\infty)
:=\#\{q\ge\lambda p:m_Q(q)=0\},
\]

then

\[
\boxed{
N_{\rm del}(\infty)
\ge
\left(\frac{\delta_{\lambda,p}}{C_\lambda}+o(1)\right)pd_p
\gg_\lambda\frac{\sqrt p}{\log p}.
}
\tag{3}
\]

The required negative repair support is therefore on the same cardinality scale as the original `RE-173` deletion packet itself, since

\[
|D_p|\asymp pd_p\asymp\frac{\sqrt p}{\log p}.
\tag{4}
\]

This conclusion does **not** use the KV envelope. It is already forced by two exact Euler coordinates plus the one-sided granularity of honest prime multiplicities.

There is also a localization form that joins directly with `RE-179`. Assume in addition

\[
|\Delta\vartheta(x)|
\le C_bxe^{-bV(x)},
\qquad
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}.
\]

For `Y>=lambda p`, define the number of repair deletions below `Y`,

\[
N_{\rm del}(Y)
:=\#\{q\in[\lambda p,Y):m_Q(q)=0\},
\]

and let `z_1,z_2,...` be the starts of maximal negative sign-phase fragments meeting `[Y,infinity)`, with

\[
\mathcal R_b^-(Y):=\sum_j e^{-bV(z_j)},
\qquad
\ell_{\rm KV}(Y):=\frac{\log Y}{V(Y)}.
\]

Then

\[
\boxed{
\frac{N_{\rm del}(Y)}p
+
\mathcal R_b^-(Y)
+
\ell_{\rm KV}(Y)e^{-bV(Y)}
\gg_{b,\lambda}
d_p.
}
\tag{5}
\]

Equivalently, using the Robin normalization of `d_p`,

\[
\boxed{
\frac{\log p}{\sqrt p}N_{\rm del}(Y)
+
\sqrt p\log p
\left[
\mathcal R_b^-(Y)
+
\ell_{\rm KV}(Y)e^{-bV(Y)}
\right]
\gg_{b,\lambda}1.
}
\tag{6}
\]

Thus the live `RE-179` dichotomy becomes quantitative in both branches. If the remote weighted reset budget is `o(d_p)`, then

\[
N_{\rm del}(Y)\gg_\lambda\frac{\sqrt p}{\log p}.
\]

Conversely, if the repair uses \(o(\sqrt p/\log p)\) early deletions, then its remote tail must still pay a reset budget of order `d_p`.

## 1. Two exact Euler coordinates force negative centered repair

Separate the repair coefficients `q>=lambda p` into positive and negative parts. Write

\[
P_H:=\sum_{c_q>0}c_qH(q),
\qquad
N_H:=\sum_{c_q<0}(-c_q)H(q),
\]

and define `P_B,N_B` analogously with `B` in place of `H`. Exact matching of the deletion packet gives

\[
P_H-N_H=d_p,
\qquad
P_B-N_B=a_Dd_p.
\tag{7}
\]

Center the first slope at the deletion barycenter:

\[
P_K:=P_B-a_DP_H,
\qquad
N_K:=N_B-a_DN_H.
\]

Equation (7) gives

\[
P_K=N_K.
\tag{8}
\]

Because every repair prime lies beyond the fixed multiplicative gap,

\[
K_D(q)\ge\delta_{\lambda,p}H(q)>0.
\]

Also `P_H=d_p+N_H>=d_p`, so

\[
P_K
=\sum_{c_q>0}c_qK_D(q)
\ge\delta_{\lambda,p}P_H
\ge\delta_{\lambda,p}d_p.
\]

Using (8),

\[
N_K
=\sum_{c_q<0}(-c_q)K_D(q)
\ge\delta_{\lambda,p}d_p.
\tag{9}
\]

For a relaxed signed coefficient model, (9) is only a weighted-mass statement. For an honest multiplicity profile, however,

\[
c_q=m_Q(q)-1<0
\quad\Longrightarrow\quad
m_Q(q)=0,
\quad c_q=-1.
\]

Therefore (9) is exactly (1). This is the point at which the source-faithful multiplicity constraint adds information that the signed model of `RE-179` deliberately discarded.

## 2. A single deleted repair prime has only `O(1/p)` centered leverage

The ratio `A(q)=B(q)/H(q)` satisfies the elementary inequalities from `RE-175`,

\[
\log q<A(q)<\frac q{q-1}\log q.
\]

Since every prime in `D_p` lies in `[2p,3p]`, its `H`-weighted barycenter obeys

\[
a_D\ge\log(2p).
\tag{10}
\]

Also

\[
H(q)\ge\frac1q,
\qquad
B(q)=\frac{\log q}{q-1}.
\]

Hence for `q>=lambda p`,

\[
\begin{aligned}
K_D(q)
&=B(q)-a_DH(q)\\
&\le
\frac{\log q}{q-1}
-
\frac{\log(2p)}q\\
&=
\frac{\log(q/(2p))}{q}
+
\frac{\log q}{q(q-1)}.
\end{aligned}
\tag{11}
\]

Writing `q=up`, the first term is

\[
\frac1p\frac{\log(u/2)}u.
\]

For `u>2`, the function `log(u/2)/u` has global maximum `1/(2e)` at `u=2e`; restricting to `u>=lambda` gives `C_lambda<=1/(2e)`. The second term in (11) is `o(1/p)` uniformly for `q>=lambda p`. This proves (2).

Combining (1) and (2) proves (3). Finally, on the original packet \(q\in[2p,3p]\) one has

\[
H(q)\asymp\frac1p,
\]

so (4) follows directly from the definition of `d_p`.

The cardinality scale is therefore not an artifact of the particular construction of `D_p`: it is the scale forced on **any** honest negative repair by the same two boundary coordinates.

## 3. Local deletions and remote reset budget obey one conservation inequality

Split the negative centered debt (9) at a cutoff `Y`. The early part satisfies, by (2),

\[
\sum_{\substack{\lambda p\le q<Y\\m_Q(q)=0}}K_D(q)
\le
\frac{C_\lambda+o(1)}pN_{\rm del}(Y).
\tag{12}
\]

For the tail `q>=Y`, use `0<K_D(q)<B(q)`. On each maximal negative sign-phase fragment starting at `z`, the same Stieltjes argument as in `RE-179` gives

\[
\sum_{q\text{ in fragment}}(-c_q)B(q)
\ll_b
e^{-bV(z)}
+
\int_{\text{fragment}}e^{-bV(t)}\frac{dt}{t}.
\]

Summing the disjoint fragments and using the one-sided KV Laplace estimate gives

\[
\sum_{\substack{q\ge Y\\c_q<0}}(-c_q)K_D(q)
\ll_b
\mathcal R_b^-(Y)
+
\ell_{\rm KV}(Y)e^{-bV(Y)}.
\tag{13}
\]

Equations (9), (12), and (13) yield

\[
\delta_{\lambda,p}d_p
\ll_{b,\lambda}
\frac{N_{\rm del}(Y)}p
+
\mathcal R_b^-(Y)
+
\ell_{\rm KV}(Y)e^{-bV(Y)},
\]

which is (5), and (6) follows from

\[
d_p\asymp\frac1{\sqrt p\log p}.
\]

Unlike the raw branch statement in `RE-179`, (5) assigns a common Robin-scale currency to local source granularity and remote oscillatory capacity.

## 4. What this does and does not close

**The early-repair branch is priced, not eliminated.** There are `asymp p/log p` ordinary primes in any fixed multiplicative interval at scale `p`, far more than the required `asymp sqrt(p)/log p` deletions. The KV envelope near the selector is also much larger than the resulting `asymp sqrt(p)` Chebyshev excursion. So the theorem does not rule out a highly interlaced local repair. It shows that such a repair must consume selector-scale discrete source support.

**The one-sided multiplicity floor is essential.** If one permits relaxed signed coefficients `c_q=-M` with arbitrarily large `M`, the cardinality conclusion is false: one prime can carry many units of negative centered mass. The theorem applies to genuine multiplicities `m_Q(q)>=0`; this is exactly the ordinary-prime/integer-granularity information absent from the relaxed capacity model.

**There is no symmetric positive-support bound without an upper multiplicity cap.** Positive coefficients may be arbitrarily large when `m_Q(q)` is unbounded. If one additionally restricts `m_Q(q)<=M_0` for a fixed `M_0`, then exact zeroth-coordinate matching already forces `Omega_{lambda,M_0}(sqrt(p)/log p)` distinct duplicated repair primes as well. The new content of (3) is that the negative side needs no such upper bound.

**The first Euler slope remains extra information.** As in `RE-175`--`RE-179`, nothing here derives `D_Q'(1+)=0` from Robin's criterion. The result prices what exact two-jet source fidelity would force if that coordinate is legitimately available.

**The protected multiplicative gap remains load-bearing.** The positive constant `delta_{lambda,p}` comes from `lambda>3`. If repair is allowed to overlap the deletion shell, the centered first-slope separation can collapse.

## 5. Representation and prior-art audit

The generic part is elementary: a nonnegative integer multiplicity can lose an ordinary prime at most once, and a positive weighted debt divided by the maximum weight gives a support-cardinality lower bound. The prior-art search found the expected Beurling generalized-prime and Mertens literature, together with general Euler-product multiplicity formalism, but no result needed as a new load-bearing theorem. No `SOURCES.md` update is required.

The line-specific content is the coupling of that one-sided atomic granularity to the centered two-jet debt of `RE-179`. The kernel is not arbitrary: `K_D=B-a_DH` is fixed by the actual selector deletion packet, its total forced negative mass is on the Robin scale `d_p`, and ordinary-prime placement beyond a fixed multiplicative gap gives the uniform `O(1/p)` leverage bound. This converts a continuous source-capacity alternative into a discrete selector-scale support cost.

The correct next question is therefore sharper than “can the repair happen early?” It is whether genuine CA/Robin selector structure can tolerate or forbid a **second deletion set of cardinality `Theta(sqrt(p)/log p)`** interlaced near the selector while the positive duplication mass simultaneously matches the two Euler coordinates and the KV envelope. If it can, two boundary jets remain non-rigid even after honest multiplicity is restored; if it cannot, the obstruction would finally use source-faithful combinatorics rather than another scalar capacity estimate.
