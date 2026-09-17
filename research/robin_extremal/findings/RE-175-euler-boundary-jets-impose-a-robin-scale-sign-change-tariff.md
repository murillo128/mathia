# RE-175 — Euler boundary jets impose a Robin-scale sign-change tariff

**Status:** `EXACT-DERIVED + PRIME-SUPPORTED + EULER-BOUNDARY-JET + CHEBYSHEV-SIGN-TARIFF + RE-173-DETECTED + ROBIN-SCALE-CONDITIONING + SOURCE-FIDELITY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-169, RE-172, RE-173, RE-174.

`RE-173` shows that exact Mertens normalization, ordinary-prime support, integer multiplicities and very strong KV fidelity still permit an order-one transient Robin excursion when the compensating source tail is allowed to be infinite. `RE-174` restores uniqueness if one observes the Euler discrepancy at an unbounded sequence of high temperatures, but the earliest-prime signal is exponentially small and therefore badly conditioned at the Robin selector scale.

There is a sharper intermediate invariant at the opposite edge of the Euler half-plane.

For a prime-supported multiplicity perturbation

\[
c_q:=m_Q(q)-1,
\tag{1}
\]

put, for `s>1`,

\[
F_s(q):=-\log(1-q^{-s}),
\qquad
D_Q(s):=\sum_q c_q F_s(q).
\tag{2}
\]

Whenever the relevant weighted series converge, the right boundary jet of `D_Q` at `s=1` is

\[
D_Q^{(j)}(1+)=\sum_q c_q J_j(q),
\qquad
J_j(q):=\left.\partial_s^jF_s(q)\right|_{s=1}.
\tag{3}
\]

The zeroth coordinate is exactly the Mertens charge,

\[
J_0(q)=H(q):=\log\frac q{q-1},
\tag{4}
\]

while the first boundary slope is

\[
J_1(q)=-\frac{\log q}{q-1}.
\tag{5}
\]

Two conclusions follow.

1. **Finite boundary jets force oscillation of the prime multiplicity perturbation.** For every fixed `K`, once all modified primes are sufficiently large, a nonzero perturbation satisfying
   \[
   D_Q^{(j)}(1+)=0,
   \qquad 0\le j\le K,
   \tag{6}
   \]
   must have at least `K+1` sign changes in the sequence of nonzero coefficients `c_q` ordered by increasing prime.

2. **The one-sign-change control of RE-173 is already detected by the first slope at Robin scale.** For that construction,
   \[
   \boxed{
   |D_{Q_p}'(1+)|
   \ge
   \bigl(\log(16/3)-o(1)\bigr)d_p
   \asymp
   \frac1{\sqrt p\log p},
   }
   \tag{7}
   \]
   where `d_p` is the Mertens debt created by its deletion packet. Hence
   \[
   \boxed{
   \sqrt p\log p\,|D_{Q_p}'(1+)|\gg1.
   }
   \tag{8}
   \]

Thus the exact-Mertens escape in `RE-173` does not require the coefficient-recovery regime of `RE-174` to become visible. One additional scalar boundary invariant, the first Euler slope, sees its delayed positive compensation at the **same normalization as the order-one Robin excursion**.

This does not prove source rigidity. It replaces the one-dimensional Mertens null direction by a hierarchy: matching `K+1` boundary coordinates forces at least `K+1` alternations between deletion and duplication packets. The next escape therefore has to become increasingly interlaced in prime scale rather than merely move one compensating tail farther out.

## 1. Boundary jets of a prime-supported Euler discrepancy

For `s>1`, expand

\[
F_s(q)
=\sum_{n\ge1}\frac{q^{-ns}}n.
\tag{9}
\]

Termwise differentiation gives, for `j>=1`,

\[
\boxed{
J_j(q)
=(-\log q)^j
\sum_{n\ge1} n^{j-1}q^{-n}.
}
\tag{10}
\]

In particular,

\[
J_j(q)
=(-1)^j\frac{(\log q)^j}{q}
\left(1+O_j(q^{-1})\right).
\tag{11}
\]

Assume for a fixed `K` that

\[
\boxed{
\sum_q |c_q|\frac{(\log q)^K}{q}<\infty.
}
\tag{12}
\]

Then every series in (3) for `0<=j<=K` converges absolutely. Moreover the derivatives of (9) for `s>=1` are dominated by constant multiples of `(log q)^j/q`, so dominated convergence identifies (3) with the right derivatives of the Euler discrepancy at the boundary.

There is no need for either `Z_Q(s)` or `zeta(s)` separately to be finite at `s=1`. The object being differentiated is their convergent logarithmic **difference**. For `j=0`, condition `D_Q(1+)=0` is exactly

\[
\sum_q c_q\log\frac q{q-1}=0,
\tag{13}
\]

the Mertens matching used in `RE-169` and `RE-173`.

The tail in `RE-173` satisfies (12) for every fixed `K`: its selected tail primes grow at least geometrically, so

\[
\sum_j\frac{(\log q_j)^K}{q_j}<\infty.
\tag{14}
\]

Hence all fixed boundary jets used below are legitimate on that control.

## 2. The boundary-jet kernels form an eventual Chebyshev system

Write

\[
x=\log q,
\qquad
\Phi_j(x):=J_j(e^x),
\qquad 0\le j\le K.
\tag{15}
\]

From (9)--(10), uniformly with any fixed number of `x`-derivatives,

\[
\Phi_j(x)
=(-1)^j x^j e^{-x}
+O_{j,K}(x^j e^{-2x})
\qquad (x\to\infty).
\tag{16}
\]

For `0<=r<=K`, consider the initial Wronskian

\[
W_r(x)
:=W(\Phi_0,\ldots,\Phi_r)(x).
\tag{17}
\]

The leading model functions are `(-1)^j x^j e^{-x}`. Multiplication of all columns by `e^{-x}` contributes `e^{-(r+1)x}`, while the Wronskian of the signed monomials is constant. Therefore (16) gives

\[
\boxed{
W_r(x)
=
C_r e^{-(r+1)x}(1+o(1)),
\qquad
C_r=(-1)^{r(r+1)/2}\prod_{m=0}^{r}m!\ne0.
}
\tag{18}
\]

Consequently, for every fixed `K` there is `X_K` such that all initial Wronskians `W_0,...,W_K` are nonzero on `[X_K,infinity)`. The family

\[
\{\Phi_0,\ldots,\Phi_K\}
\tag{19}
\]

is therefore an extended Chebyshev system on that ray: every nonzero linear combination has at most `K` zeros there, counted with multiplicity. One can obtain this directly from (18) by the standard repeated-Rolle/Wronskian argument; no external zero theorem is needed below beyond that elementary criterion.

This is the structural point. Near the Euler boundary, the jet basis is asymptotically

\[
e^{-x},\ xe^{-x},\ x^2e^{-x},\ldots,
\tag{20}
\]

so finite Euler jets are ordinary moment coordinates of the log-prime location, up to exponentially smaller corrections.

## 3. Vanishing `K`-jets require at least `K+1` sign changes

Assume the modified primes all satisfy `log q>X_K`, condition (12) holds, and

\[
D_Q^{(j)}(1+)=0,
\qquad 0\le j\le K.
\tag{21}
\]

Suppose, toward a contradiction, that the ordered nonzero coefficient sequence `c_q` has only `r<=K` sign changes.

Choose one point of the `x`-axis in each of the `r` gaps where the sign changes occur. Choose another `K-r` distinct points between `X_K` and the first modified prime. These are `K` distinct prescribed zeros. Since the span of (19) has dimension `K+1`, there is a nonzero generalized polynomial

\[
G(x)=\sum_{j=0}^{K}a_j\Phi_j(x)
\tag{22}
\]

vanishing at all of them.

The Chebyshev zero bound says that `G` has no further zero on `[X_K,infinity)` and that every prescribed zero is simple: an additional zero or a multiple prescribed zero would give more than `K` zeros counted with multiplicity. Hence the sign of `G` flips exactly at the prescribed points. After multiplying `G` by `-1` if necessary, its sign on the modified primes agrees with the sign of `c_q`. Thus

\[
\sum_q c_qG(\log q)>0.
\tag{23}
\]

Absolute convergence follows from (12). But by (21),

\[
\sum_q c_qG(\log q)
=
\sum_{j=0}^{K}a_jD_Q^{(j)}(1+)
=0,
\tag{24}
\]

a contradiction. Therefore

\[
\boxed{
\#\{\text{sign changes of nonzero }c_q\}\ge K+1.
}
\tag{25}
\]

The indexing is worth making explicit. Exact Mertens matching alone is the `K=0` case and forces at least one sign change, consistent with the negative-then-positive control of `RE-173`. Matching the Mertens value **and** the first boundary slope is `K=1` and forces at least two sign changes. Every additional matched Euler derivative raises the required alternation count by one.

This theorem is qualitative in the general case: it counts source oscillations but does not yet lower-bound their spatial separation or their Robin effect. The particular geometry of `RE-173`, however, gives a quantitative first-slope estimate.

## 4. RE-173 pays a first-slope debt at exactly the Robin scale

Recall the `RE-173` construction. It deletes primes

\[
D_p\subset[2p,3p]
\tag{26}
\]

and duplicates compensating primes only at scales at least `16p`, first in `[16p,17p]` and then in an increasing infinite tail. Put

\[
d_p:=\sum_{r\in D_p}H(r)
\asymp\frac1{\sqrt p\log p}.
\tag{27}
\]

Exact Mertens matching says that the positive compensators `C_p^+` carry exactly the same `H`-mass:

\[
\sum_{q\in C_p^+}H(q)=d_p.
\tag{28}
\]

Factor the first derivative as

\[
-J_1(q)=H(q)A(q),
\qquad
A(q):=
\frac{\log q}{(q-1)\log(q/(q-1))}.
\tag{29}
\]

The elementary inequalities

\[
\frac1q<H(q)<\frac1{q-1}
\tag{30}
\]

give

\[
\boxed{
\log q<A(q)<\frac q{q-1}\log q.
}
\tag{31}
\]

Since deletions have coefficient `-1` and compensators coefficient `+1`,

\[
D_{Q_p}'(1+)
=
\sum_{r\in D_p}H(r)A(r)
-
\sum_{q\in C_p^+}H(q)A(q).
\tag{32}
\]

For `r in D_p`,

\[
A(r)
\le
\left(1+o(1)\right)\log(3p),
\tag{33}
\]

whereas every positive compensator has `q>=16p`, so

\[
A(q)>\log(16p).
\tag{34}
\]

Using equal `H`-mass (28),

\[
\begin{aligned}
D_{Q_p}'(1+)
&\le
 d_p\left[(1+o(1))\log(3p)-\log(16p)\right]\\
&=
-\left(\log(16/3)-o(1)\right)d_p.
\end{aligned}
\tag{35}
\]

Therefore

\[
\boxed{
|D_{Q_p}'(1+)|
\ge
\left(\log(16/3)-o(1)\right)d_p
\asymp
\frac1{\sqrt p\log p}.
}
\tag{36}
\]

The normalized Robin excursion in `RE-173` is order one because its deletion debt is exactly on the scale `(sqrt(p) log p)^{-1}`. Equation (36) shows that the first boundary Euler slope has the same conditioning:

\[
\boxed{
\sqrt p\log p\,|D_{Q_p}'(1+)|\gg1.
}
\tag{37}
\]

This is materially different from the high-temperature diagnostic in `RE-174`. Taking `s` large isolates the earliest changed prime but suppresses its signal like a high power of that prime. Taking a derivative at `s=1` instead compares the **logarithmic location** of equal Mertens mass. Moving the compensating mass from scale `p` to scale `16p` costs a constant `log 16` rather than a power of `p`.

## 5. Representation audit

The same source discrepancy now has three useful representations, with very different conditioning.

The Mertens representation uses only the scalar

\[
\sum_q c_qH(q).
\tag{38}
\]

It is blind to where positive and negative `H`-mass sits once their totals agree, which is exactly the null direction exploited by `RE-173`.

The high-temperature representation of `RE-174` uses `F_s(q)` for large `s`. It is excellent for uniqueness because the smallest changed prime eventually dominates, but that localization has an exponential price: the observable is essentially `q^{-s}`.

The boundary-jet representation instead uses

\[
J_j(q)
\sim
(-1)^j\frac{(\log q)^j}{q}.
\tag{39}
\]

After changing coordinate to `x=log q`, these are exponentially weighted polynomial moments. They do not recover individual primes from finitely many coordinates; they measure how Mertens-weighted signed mass is distributed across log-prime scale. That is precisely why the first slope sees the delayed `RE-173` compensator without paying the coefficient-recovery cost of `RE-174`.

The **generic** part of the argument is the Chebyshev/moment sign-change principle: a signed measure orthogonal to `K+1` moment-like test functions needs at least `K+1` alternations. The **source-specific** part is that the ordinary-prime Euler factors supply exactly these kernels, their zeroth jet is the Mertens normalization already present in the Robin decomposition, and the `RE-173` excursion creates Mertens mass of size `(sqrt(p) log p)^{-1}` before repaying it at a separated prime scale.

Thus this finding is not another reformulation of `RE-174`. It identifies an observable whose conditioning is naturally aligned with the Robin source coordinate rather than with exact coefficient recovery.

## 6. Adversarial review and remaining escape

**This is not a proof of Robin or RH.** The first Euler boundary slope is an additional source invariant. Nothing here proves that the existing KV envelope, the Robin inequality itself, or the CA selector automatically controls `D_Q'(1+)`. The result says what one extra source coordinate would kill the specific `RE-173` control, not that the ordinary problem already supplies that coordinate for free.

**Boundary jets require stronger tail summability.** Exact Mertens matching needs roughly `sum |c_q|/q<infinity`; the first slope needs `sum |c_q| log q/q<infinity`, and the `K`-jet statement uses (12). The geometric tail of `RE-173` satisfies every fixed requirement, but a more diffuse infinite control could deliberately leave this class.

**Finite jets do not restore full rigidity.** Equation (25) is a sign-change tariff, not injectivity. A redesigned control with two or more interlaced deletion/duplication bands may match both `D_Q(1+)` and `D_Q'(1+)` while retaining a transient Robin excursion. Higher jets force further alternation but still leave infinitely many source degrees of freedom.

**The eventual Chebyshev statement is asymptotic.** It applies once the modified primes exceed a threshold depending on fixed `K`. This is exactly the selector regime relevant here, where the modification scale tends to infinity, but it is not asserted uniformly over small primes.

**The quantitative lower bound is geometry-specific.** The constant-gap estimate (36) uses the clean separation `[2p,3p]` versus `[16p,infinity)` of `RE-173`. The abstract sign theorem alone does not imply a comparable lower bound for an arbitrary oscillatory control whose positive and negative packets may interlace on very nearby scales.

The next falsification target is therefore concrete: construct, if possible, a prime-supported integer control with at least two sign changes, exact

\[
D_Q(1+)=D_Q'(1+)=0,
\tag{40}
\]

KV-scale source fidelity, and an order-one transient Robin excursion before final compensation. If that succeeds, the same question can be repeated for successively higher finite jets. If it fails for a quantitative reason tied to the selector geometry, that failure would be a genuinely stronger source-rigidity mechanism than the scalar Mertens normalization.

## 7. Prior-art boundary

The qualitative machinery behind Section 3 belongs to classical Chebyshev-system and sign-change theory; no novelty is claimed for that general principle. A fresh literature check found standard work on Chebyshev systems and zero/sign-change criteria, including S. Musin, *The Chebyshev systems and zeros of a function* (arXiv:0903.1908), as well as the broader classical theory of T-systems and moment problems.

No external theorem is load-bearing here: the particular kernels are handled by the explicit expansion (10), their eventual Chebyshev property follows from the Wronskian asymptotic (18), and the sign-change contradiction is written out in Section 3. Accordingly this pass does not add a new source anchor to `SOURCES.md`.

What appears specific to this research line is the **connection** between those generic moment coordinates and the matched-control boundary exposed by `RE-173`: the zeroth Euler jet is exactly the Mertens debt, while the first derivative prices delayed repayment by log-prime distance and detects that construction on the same `(sqrt(p) log p)^{-1}` scale as its Robin excursion.

## 8. Durable consequence

`RE-173` established that one exact boundary charge is too weak; `RE-174` showed that an unbounded high-temperature family recovers the whole source but at poor conditioning. The present result isolates a middle regime:

\[
\boxed{
\text{finite Euler boundary jets}
\quad\Longrightarrow\quad
\text{finite sign-change complexity tariffs}.
}
\tag{41}
\]

For the current one-sign-change matched control, the first slope is already enough and is quantitatively well conditioned. Therefore the surviving source-level escape is no longer simply an infinite delayed tail. It must either:

- oscillate between deletions and duplications with increasing sign complexity as more boundary coordinates are matched;
- use a tail too diffuse for the relevant boundary derivatives to exist absolutely; or
- exploit a mechanism showing that finite Euler-jet matching can coexist with the Robin excursion despite those oscillation costs.

The central unresolved question is now whether ordinary-prime/CA structure supplies any finite or slowly growing amount of this boundary information **without assuming an Euler observable by hand**. That is the point at which this source-rigidity hierarchy could reconnect to the actual Robin problem.