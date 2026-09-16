# RE-173 — Infinite prime-supported exact Mertens compensation survives KV fidelity

**Status:** `EXACT-DERIVED + PRIME-SUPPORT-INFINITE-CONTROL + EXACT-MERTENS-MATCHING + INTEGER-MULTIPLICITY + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-172-BOUNDARY + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-153, RE-169, RE-172.

`RE-172` proves an exact finite injectivity theorem: a finite rational multiplicity perturbation supported on ordinary prime labels cannot preserve the ordinary Mertens normalization unless it is trivial. The boundary left open there is whether an **infinite** prime-supported integer perturbation can evade the largest-prime valuation argument while still staying inside the quantitative source envelopes used by the Robin control program.

It can.

Let

\[
H(q):=\log\frac q{q-1},
\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
\tag{1}
\]

For every sufficiently large selector scale `p`, there is a prime-supported source `Q_p` with multiplicities only in

\[
\boxed{\{0,1,2\}}
\tag{2}
\]

such that:

1. `Q_p` agrees with the ordinary prime source below `2p`;
2. its Mertens normalization is **exactly ordinary**,
   \[
   \boxed{\Gamma(Q_p)=\gamma;}
   \tag{3}
   \]
3. for every fixed `b>0`, its discrepancy from the ordinary Chebyshev source satisfies, uniformly for `x>=2p`,
   \[
   \boxed{
   |\vartheta_{Q_p}(x)-\vartheta(x)|
   \ll_b x e^{-bV(x)};
   }
   \tag{4}
   \]
   in fact the left side is only `O(sqrt(p)+(log x)^2)`;
4. before the compensating tail starts, the normalized `RE-169` Robin source coordinate moves by order one. More precisely, with
   \[
   \mathcal A_{p,U}(Q)
   :=
   \frac{\sqrt p\log p}{Z_p}
   \int_{p+p^\alpha}^{U}
   (t-\vartheta_Q(t))(-h'(t))\,dt,
   \qquad Z_p=2+o(1),
   \tag{5}
   \]
   one can arrange
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_p)-\mathcal A_{p,8p}(P)
   \asymp 1.
   }
   \tag{6}
   \]

The complete perturbation has infinite support. Its Mertens correction is absolutely summable, and the infinite tail repays the finite post-selector debt exactly. Thus the finite rigidity of `RE-172` is genuinely a **compactness theorem**, not a selector-rigidity theorem: ordinary-prime support, integer multiplicities, exact `Gamma=gamma`, and arbitrarily strong fixed Korobov--Vinogradov relative fidelity can coexist with an order-one transient Robin displacement.

This rules out a natural hoped-for closure after `RE-172`. The missing source information cannot be supplied merely by extending the finite prime-support argument to a KV-controlled infinite tail.

## 1. Create an order-one prime-supported Robin excursion

Fix

\[
N_p:=\left\lfloor\frac{\sqrt p}{\log p}\right\rfloor.
\tag{7}
\]

By the prime number theorem, for all sufficiently large `p` the interval `[2p,3p]` contains far more than `N_p` primes. Choose a set `D_p` of exactly `N_p` such primes and delete one copy of each from the ordinary source. Thus the multiplicity becomes zero on `D_p` and remains one elsewhere for the moment.

Put

\[
d_p:=\sum_{r\in D_p}H(r).
\tag{8}
\]

Since

\[
\frac1r<H(r)<\frac1{r-1},
\tag{9}
\]

we have

\[
\boxed{
 d_p\asymp \frac1{\sqrt p\log p}.
}
\tag{10}
\]

Take `U=8p`. Up to that height no compensation has yet been introduced. A deleted prime `r` contributes

\[
\log r\,[h(r)-h(8p)]
=H(r)-\log r\,h(8p)
\tag{11}
\]

to the difference of the integrals in (5). For `2p<=r<=3p`,

\[
H(r)\ge\frac1{3p},
\qquad
\log r\,h(8p)
\le -\log\left(1-\frac1{8p}\right)
\le\frac1{8p-1}.
\tag{12}
\]

Hence, for sufficiently large `p`,

\[
\frac1{6p}
\le
\log r\,[h(r)-h(8p)]
\ll\frac1p.
\tag{13}
\]

Summing over `N_p` deleted primes and using `Z_p=2+o(1)` gives

\[
\frac{\sqrt p\log p}{Z_p}
\sum_{r\in D_p}
\log r\,[h(r)-h(8p)]
\asymp 1,
\tag{14}
\]

which is (6). The lower endpoint in (5) causes no issue because `p+p^alpha<2p` for every fixed `alpha<1` and sufficiently large `p`.

The Chebyshev discrepancy created by this whole deletion packet is tiny on the KV scale:

\[
\sum_{r\in D_p}\log r
=O(\sqrt p).
\tag{15}
\]

Thus the excursion is already realized on ordinary prime labels with integer multiplicity change. What remains is to repay its Mertens debt **exactly** without leaving the same fidelity class.

## 2. Reduce the remaining exact debt below one prime atom

Use ordinary primes in the disjoint block `[16p,17p]` as positive compensators, i.e. duplicate selected primes so their multiplicity becomes two.

The PNT gives `gg p/log p` primes in this block. Each has

\[
H(q)\asymp\frac1p,
\tag{16}
\]

so the sum of `H(q)` over the whole block is `gg 1/log p`, much larger than `d_p`. Enumerate these primes increasingly and take the longest initial segment `C_p` for which

\[
\sum_{q\in C_p}H(q)<d_p.
\tag{17}
\]

The segment exists and is nonempty for large `p`. Define the residual

\[
r_0
:=
d_p-\sum_{q\in C_p}H(q).
\tag{18}
\]

The next unused prime in `[16p,17p]` would cross `d_p`, so

\[
0<r_0\ll\frac1p.
\tag{19}
\]

The strict positivity deserves emphasis. Equality in (17) after finitely many compensators would give a nontrivial finite rational relation among the values `H(q)` on ordinary primes, forbidden by `RE-172`. Thus the finite prime lattice can approach the target to one-atom precision, but it cannot land on it exactly.

The compensating block also has only

\[
|C_p|=O\left(\frac{\sqrt p}{\log p}\right)
\tag{20}
\]

members, hence contributes `O(sqrt(p))` additional Chebyshev mass. After the two finite packets the source discrepancy is still `O(sqrt(p))`, while the unresolved Mertens debt is only `O(1/p)`.

## 3. An infinite ordinary-prime tail fills the residual exactly

The last step is an elementary subsum construction that deliberately has no largest modified prime.

Suppose `0<r_j<=1/4`. By the PNT, once `r_j` is sufficiently small there is an ordinary prime `q_{j+1}` in the fixed-ratio interval

\[
\boxed{
\frac{2}{r_j}
\le q_{j+1}
\le
\frac{5}{2r_j}.
}
\tag{21}
\]

Duplicate that prime and set

\[
r_{j+1}:=r_j-H(q_{j+1}).
\tag{22}
\]

The elementary bounds (9) give

\[
H(q_{j+1})
\ge\frac1{q_{j+1}}
\ge\frac25 r_j,
\tag{23}
\]

and

\[
H(q_{j+1})
\le\frac1{q_{j+1}-1}
\le\frac{r_j}{2-r_j}
\le\frac47r_j.
\tag{24}
\]

Consequently

\[
\boxed{
\frac37r_j
\le r_{j+1}
\le\frac35r_j.
}
\tag{25}
\]

So every residual stays positive and tends geometrically to zero. In particular,

\[
\boxed{
\sum_{j\ge1}H(q_j)=r_0
}
\tag{26}
\]

exactly.

The selected primes are automatically distinct and increasing. Indeed, by (25),

\[
q_{j+2}
\ge\frac2{r_{j+1}}
\ge\frac{10}{3r_j}
>
\frac5{2r_j}
\ge q_{j+1}.
\tag{27}
\]

Moreover `r_0<<1/p`, so the first tail prime lies beyond a fixed multiple of `p`, in particular beyond the finite compensation block for all sufficiently large `p`.

This is the exact place where finite rigidity disappears. Every finite truncation leaves the strictly positive residual `r_j`; only the limit of the infinite ordinary-prime tail reaches zero.

## 4. Exact Mertens normalization and absolute convergence

Define the final multiplicity perturbation by

\[
c_q=
\begin{cases}
-1,&q\in D_p,\\
+1,&q\in C_p\cup\{q_j:j\ge1\},\\
0,&\text{otherwise}.
\end{cases}
\tag{28}
\]

Thus the final multiplicities are exactly `0`, `1`, or `2`.

Using (18) and (26),

\[
\begin{aligned}
\sum_q c_qH(q)
&=-d_p
+\sum_{q\in C_p}H(q)
+\sum_{j\ge1}H(q_j)\\
&=-d_p+(d_p-r_0)+r_0\\
&=0.
\end{aligned}
\tag{29}
\]

The series is absolutely convergent, because

\[
\sum_q |c_q|H(q)
=d_p+\sum_{q\in C_p}H(q)+r_0
=2d_p<\infty.
\tag{30}
\]

Therefore the difference between the generalized Mertens integrals of `Q_p` and the ordinary source converges absolutely and equals (29). Since the ordinary constant is `gamma`,

\[
\boxed{\Gamma(Q_p)=\gamma.}
\tag{31}
\]

Equivalently, the infinite Euler-factor ratio

\[
\prod_q\left(\frac q{q-1}\right)^{c_q}
\tag{32}
\]

converges absolutely in logarithm and has value one.

There is no conflict with `RE-172`: that proof requires a largest modified prime. Here every finite partial product is nontrivial, and exact equality occurs only after passing to the infinite limit.

## 5. The infinite compensation is far smaller than every fixed KV envelope

It remains to check that exact compensation did not buy its freedom by destroying the quantitative source fidelity.

The two finite packets contribute `O(sqrt(p))` total logarithmic prime mass by (15) and (20). For the infinite tail, (25)--(27) show that the selected primes grow at least geometrically. Hence the number of tail primes up to `x` is `O(log x)`, and therefore

\[
\sum_{q_j\le x}\log q_j
=O((\log x)^2).
\tag{33}
\]

It follows uniformly for `x>=2p` that

\[
\boxed{
|\vartheta_{Q_p}(x)-\vartheta(x)|
\ll \sqrt p+(\log x)^2.
}
\tag{34}
\]

Now fix any `b>0`. Since

\[
bV(x)=o(\log x),
\tag{35}
\]

for all sufficiently large `x` one has, for example,

\[
x e^{-bV(x)}\ge x^{3/4}.
\tag{36}
\]

For `x>=2p`, the right side dominates both `sqrt(p)` and `(log x)^2`. Thus (34) proves (4).

In particular, if the ordinary source satisfies a KV PNT estimate

\[
\vartheta(x)=x+O\bigl(xe^{-aV(x)}\bigr)
\tag{37}
\]

for some absolute `a>0`, then for every fixed `0<b<=a`, the controlled source also satisfies

\[
\boxed{
\vartheta_{Q_p}(x)
=x+O_b\bigl(xe^{-bV(x)}\bigr)
}
\tag{38}
\]

uniformly throughout the modified tail. The infinite exact correction is therefore not merely PNT-small; relative to the ordinary source it is negligible against **every preassigned fixed KV exponent**.

## 6. Adversarial checks and scope

**The control is genuinely infinite.** `RE-172` rules out exact equality after any finite stage. Equation (25) also gives an explicit positive residual at every finite truncation.

**The Mertens limit is legitimate.** The logarithmic Euler-factor correction is absolutely summable by (30); no conditional rearrangement is being used.

**Prime support is exact.** Every changed label is an ordinary prime. The construction never inserts a generalized real label or a composite integer label.

**Multiplicity fidelity is integer but not ordinary multiplicity-one fidelity.** Deleted primes have multiplicity zero and duplicated primes have multiplicity two. Thus this is still a matched synthetic source, not the actual ordinary prime set. The result says that the `RE-172` arithmetic gate of ordinary-prime support plus integer multiplicity is insufficient once noncompact controls are admitted; it does not trivialize the stronger requirement that every ordinary prime occur exactly once.

**The excursion is before compensation.** The measurement height `8p` lies after the deletion block `[2p,3p]` and before the finite positive block `[16p,17p]`; the infinite tail begins later still. Hence (6) is a genuine transient prefix effect rather than cancellation measured after the fact.

**The source remains quantitatively PNT-faithful.** Equation (34) is much smaller than a KV envelope. The infinite support itself is therefore not a hidden loss of source regularity.

**No claim is made that this is an admissible CA counterexample.** The construction is a falsification control for source information. It shows that the package `prime support + integer multiplicity + exact Mertens normalization + KV PNT fidelity` still fails to determine the selected finite Robin prefix. A proof for the actual primes must consume more source-specific information than this package contains.

## 7. Prior-art and representation audit

The generic subsum phenomenon used in Section 3 is classical: positive null sequences with divergent total mass have very flexible subseries, and modern treatments include Armengol Gasull and Francesc Manosas, *Subseries and signed series*, Communications on Pure and Applied Analysis **18** (2019), 479--492, DOI `10.3934/cpaa.2019024`. The divergence of the reciprocal-prime series and fixed-ratio prime occupancy are classical as well. No novelty is claimed for those ingredients.

The proof above is deliberately more explicit than invoking an abstract subsum theorem: after a finite coarse correction, each residual is reduced by a prime chosen in a fixed-ratio interval at reciprocal scale, which simultaneously gives exact convergence and the logarithmic Chebyshev-mass bound needed for the KV audit.

A targeted prior-art search found the expected literature on subsums/achievement sets, reciprocal-prime divergence, and Mertens products, but no source combining this infinite prime-supported subsum mechanism with exact Mertens normalization, a KV Chebyshev envelope, and the transient `RE-153` Robin coordinate. The line-specific contribution is that splice, not a new theorem about abstract subseries.

The only load-bearing prime-distribution input is the ordinary PNT, already available in much stronger KV form in the line's source anchors. No new external theorem is required, so `SOURCES.md` is unchanged.

Representation-wise, `RE-172` exposed a triangular finite Euler-factor lattice. The present finding identifies its exact quotient boundary: completion of that lattice under absolutely summable `H(q)` tails acquires nontrivial null directions even while the associated Chebyshev path remains far below every fixed KV envelope. The information lost by passing from finite to completed support is therefore mathematically real, not bookkeeping.

## 8. Research consequence

The question posed at the end of `RE-172` is answered on the negative-rigidity side. The combination

\[
\boxed{
\text{ordinary-prime support}
+
\text{integer multiplicities}
+
\Gamma(Q_p)=\gamma
+
\text{KV-sized cumulative discrepancy}
}
\tag{39}
\]

still admits an order-one transient post-selector Robin displacement once infinite support is allowed.

Therefore the next closure cannot be “prove that the finite valuation argument survives by continuity.” It does not. Nor can it come from strengthening the fixed KV exponent or from demanding exact Mertens normalization: the constructed tail beats every such fixed envelope while matching `Gamma` exactly.

A genuinely source-faithful theorem now has to couple the CA selector to information that this delete/duplicate tail cannot preserve—for example multiplicity-one occupancy, a selector-conditioned local prime-count constraint, or another invariant that detects *where and how* future Euler factors may repay the Robin debt rather than only their total Mertens charge. This is the sharper boundary exposed by the matched control.

**Provenance:** derived against default-branch snapshot `ec5a5c17c6741b10e6351a350c89c28e64f36155`; stable finding prefix `RE`; no adversarial sidecar was open; no clue-state, `mind/**`, README, graph, or source-registry mutation required.