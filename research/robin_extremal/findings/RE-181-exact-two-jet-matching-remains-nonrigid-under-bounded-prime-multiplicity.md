# RE-181 — Exact two-jet matching remains non-rigid under bounded prime multiplicity

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + EXACT-TWO-JET-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-180-TARIFF-SHARP + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-175, RE-179, RE-180.

`RE-180` shows that once the relaxed signed model is returned to honest ordinary-prime multiplicities, exact Mertens value plus exact first Euler boundary slope force a second deletion set of cardinality at least

\[
\Omega\!\left(\frac{\sqrt p}{\log p}\right)
\]

unless the repair pays the remote KV-weighted reset budget of `RE-179`. That result prices the local branch but does not decide whether the branch is actually realizable.

It is realizable, at the same cardinality scale.

For every sufficiently large selector scale `p`, there exists an ordinary-prime-supported source `Q_p` with multiplicities

\[
\boxed{m_{Q_p}(q)\in\{0,1,2\}}
\tag{1}
\]

such that:

1. `Q_p` agrees with the ordinary prime source below `2p`;
2. it contains the canonical `RE-173` deletion packet `D_p subset [2p,3p]` and has no compensating modification before `16p`;
3. its Euler discrepancy
   \[
   D_{Q_p}(s):=\sum_q (m_{Q_p}(q)-1)\,[-\log(1-q^{-s})]
   \]
   satisfies the two exact right-boundary conditions
   \[
   \boxed{D_{Q_p}(1+)=D_{Q_p}'(1+)=0;}
   \tag{2}
   \]
4. its Chebyshev discrepancy obeys the explicit uniform bound
   \[
   \boxed{
   |\vartheta_{Q_p}(x)-\vartheta(x)|
   \ll \sqrt p\log p+(\log x)^3
   \qquad(x\ge2p),
   }
   \tag{3}
   \]
   hence, for every fixed `b>0`,
   \[
   |\vartheta_{Q_p}(x)-\vartheta(x)|
   \ll_b x\exp[-bV(x)],
   \qquad
   V(x)=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}};
   \tag{4}
   \]
5. before any repair is visible, the normalized Robin source coordinate of `RE-173` still moves by order one:
   \[
   \boxed{
   \mathcal A_{p,8p}(Q_p)-\mathcal A_{p,8p}(P)\asymp1;
   }
   \tag{5}
   \]
6. the first positive repair packet lies near `16p`, while the first negative repair packet lies near `32p`, and each uses
   \[
   \boxed{
   \Theta\!\left(\frac{\sqrt p}{\log p}\right)
   }
   \tag{6}
   \]
   distinct ordinary primes.

Thus the one-sided deletion tariff of `RE-180` is order-sharp inside the bounded multiplicity class `{0,1,2}`. More importantly, **two exact Euler boundary coordinates still do not rigidify the transient Robin prefix**, even after ordinary-prime support, nonnegative integer multiplicity, a fixed multiplicity cap, and arbitrarily strong fixed KV relative fidelity are all imposed simultaneously.

The construction uses an explicit two-shell quantizer. At each later scale, two disjoint narrow ordinary-prime shells have different Euler slopes. Their signed `H`-masses span the two-dimensional boundary residual over the reals; prime density then discretizes those two real masses with an error smaller than the next residual. Iterating on geometrically increasing shells makes the residual tend to zero while keeping both boundary series absolutely convergent.

## 1. Boundary coordinates and the initial Robin excursion

Retain the notation of `RE-173` and `RE-175`:

\[
H(q):=\log\frac q{q-1},
\qquad
B(q):=\frac{\log q}{q-1},
\qquad
A(q):=\frac{B(q)}{H(q)}.
\tag{7}
\]

The first two right-boundary Euler kernels are

\[
J_0(q)=H(q),
\qquad
J_1(q)=-B(q).
\tag{8}
\]

Let `D_p subset [2p,3p]` be the `RE-173` packet of

\[
N_p=\left\lfloor\frac{\sqrt p}{\log p}\right\rfloor
\]

distinct ordinary primes, each deleted once. Put

\[
d_p:=\sum_{q\in D_p}H(q)
\asymp\frac1{\sqrt p\log p},
\qquad
b_p:=\sum_{q\in D_p}B(q),
\qquad
a_D:=\frac{b_p}{d_p}.
\tag{9}
\]

Since `D_p subset [2p,3p]` and

\[
A(t)=\log t+O\!\left(\frac{\log t}{t}\right),
\tag{10}
\]

we have

\[
\log(2p)+o(1)
\le a_D\le
\log(3p)+o(1).
\tag{11}
\]

The deletion packet contributes `(-d_p,-b_p)` to the `(H,B)` boundary vector. It is therefore enough to construct a repair on ordinary primes `q>=16p` whose absolutely convergent signed boundary vector is exactly

\[
\boxed{(d_p,b_p).}
\tag{12}
\]

No repair occurs below `16p`. Consequently the `RE-173` calculation at the observation height `8p` is unchanged. In particular, with its normalization `Z_p=2+o(1)`, every deleted `q in [2p,3p]` contributes a positive amount comparable with `1/p`, so

\[
\frac{\sqrt p\log p}{Z_p}
\sum_{q\in D_p}
\log q\,[h(q)-h(8p)]
\asymp1.
\tag{13}
\]

This is exactly (5). The problem is therefore purely whether the two-dimensional debt (12) can be repaid without leaving the source-fidelity class.

## 2. A two-shell prime quantizer

Extend `A` from primes to real `t>1` by the same formula in (7). From the elementary expansion of `log(1+1/(t-1))`,

\[
A(t)=\log t+O\!\left(\frac{\log t}{t}\right),
\qquad
A'(t)=\frac1t+O\!\left(\frac{\log t}{t^2}\right).
\tag{14}
\]

For a large real scale `x`, put

\[
\delta_x:=(\log x)^{-4},
\]

and consider the two disjoint shells

\[
I_x=[x,x(1+\delta_x)],
\qquad
J_x=[2x,2x(1+\delta_x)].
\tag{15}
\]

The PNT with the already anchored KV error gives

\[
\vartheta(x(1+\delta_x))-\vartheta(x)
\sim \delta_x x,
\tag{16}
\]

because `exp(-aV(x))=o((log x)^(-4))`. Hence each shell contains total `H`-mass

\[
\boxed{
\sum_{q\in I_x}H(q)
\asymp
\sum_{q\in J_x}H(q)
\asymp
\frac1{(\log x)^5}.
}
\tag{17}
\]

Now let `r=(r_H,r_B)` be a two-coordinate residual and define

\[
M_x(r):=|r_B|+\log x\,|r_H|.
\tag{18}
\]

Assume

\[
M_x(r)\le c_0(\log x)^{-6}
\tag{19}
\]

for a sufficiently small fixed `c_0`. Set

\[
a_x:=A(x),
\qquad
b_x:=A(2x).
\]

By (14),

\[
b_x-a_x=\log2+o(1).
\tag{20}
\]

Therefore the real system

\[
u+v=r_H,
\qquad
a_xu+b_xv=r_B
\tag{21}
\]

has a unique solution satisfying

\[
\boxed{|u|+|v|\ll M_x(r).}
\tag{22}
\]

Interpret `u` and `v` as signed target `H`-masses. Equation (17), together with (19)--(22), provides far more prime `H`-mass than is needed in either shell. In `I_x`, choose primes greedily with the sign of `u` until their `H`-sum is the largest one not exceeding `|u|`; do the same in `J_x` for `v`. Since every atom in the two shells has `H(q)=O(1/x)`, the two scalar rounding errors are each `O(1/x)`.

Across either narrow shell, (14) gives

\[
A(q)-A(x)=O(\delta_x)
\]

in `I_x`, and the analogous estimate relative to `A(2x)` in `J_x`. Thus the signed prime vector selected from the two shells leaves a residual `r'=(r_H',r_B')` satisfying

\[
\boxed{
|r_H'|\ll\frac1x,
\qquad
|r_B'|
\ll
\frac{M_x(r)}{(\log x)^4}
+
\frac{\log x}{x}.
}
\tag{23}
\]

The total absolute `H`-mass used in this quantization step is `O(M_x(r))`.

This lemma is the only discretization input. It is not a density or continuum approximation of the original Robin extremal problem: it is an explicit statement about selecting distinct **ordinary primes** with coefficient `+1` or `-1` in two concrete shells.

## 3. Iteration gives exact two-jet matching with multiplicities `{0,1,2}`

Set

\[
x_j:=16\cdot4^j p,
\qquad
L_j:=\log x_j,
\qquad
\delta_j:=L_j^{-4}.
\tag{24}
\]

The shells `I_(x_j)` and `J_(x_j)` are pairwise disjoint, and every one lies above `8p`. Start with the repair residual

\[
r^{(0)}:=(d_p,b_p).
\tag{25}
\]

By (9) and (11),

\[
M_0:=M_{x_0}(r^{(0)})\ll\frac1{\sqrt p},
\tag{26}
\]

which is much smaller than `L_0^(-6)` for large `p`. Apply the two-shell quantizer at `x_0`, subtract its signed prime vector, and repeat at `x_1,x_2,...`.

If

\[
M_j:=M_{x_j}(r^{(j)}),
\]

then (23) gives

\[
M_{j+1}
\ll
L_j^{-4}M_j+
\frac{L_j}{x_j}.
\tag{27}
\]

For sufficiently large `p`, the implied constant times `L_j^(-4)` is at most `1/8` for every `j`. The bound `M_j<<L_j^(-6)` is then preserved inductively, so every later shell has enough ordinary primes for the next quantization step. Moreover

\[
\boxed{
M_j
\ll
8^{-j}M_0+
\frac{L_j}{x_j}.
}
\tag{28}
\]

In particular `r^(j)->0`.

Assign coefficient `+1` to every repair prime selected with positive sign and `-1` to every repair prime selected with negative sign. The repair shells are disjoint from one another and from `D_p`, so no prime is ever modified twice. With the initial deletion packet included,

\[
c_q:=m_{Q_p}(q)-1\in\{-1,0,1\},
\]

which proves (1).

The absolute `H`-mass used at stage `j` is `O(M_j)`. Hence (28) gives

\[
\sum_q |c_q|H(q)<\infty.
\tag{29}
\]

Likewise, all primes at stage `j` are comparable with `x_j`, so

\[
\sum_q |c_q|B(q)
\ll
\sum_{j\ge0}L_jM_j
<\infty.
\tag{30}
\]

Since the residual boundary vector tends to zero, (25), (29), and (30) yield the exact repair identities

\[
\sum_{q\notin D_p}c_qH(q)=d_p,
\qquad
\sum_{q\notin D_p}c_qB(q)=b_p.
\tag{31}
\]

After restoring the initial negative packet,

\[
\boxed{
\sum_q c_qH(q)=0,
\qquad
\sum_q c_qB(q)=0.
}
\tag{32}
\]

By `RE-175`, these are precisely

\[
D_{Q_p}(1+)=0,
\qquad
D_{Q_p}'(1+)=-\sum_qc_qB(q)=0,
\]

so (2) follows with legitimate absolutely convergent boundary sums.

## 4. The first repair saturates the RE-180 deletion tariff

The first quantization stage is more structured than the later ones. Put

\[
a_0=A(16p),
\qquad
b_0=A(32p).
\]

Equations (11) and (14) give

\[
a_0-a_D\ge\log(16/3)-o(1)>0,
\qquad
b_0-a_0=\log2+o(1).
\tag{33}
\]

Solving the initial real system

\[
u_0+v_0=d_p,
\qquad
a_0u_0+b_0v_0=a_Dd_p
\tag{34}
\]

gives

\[
v_0
=-\frac{a_0-a_D}{b_0-a_0}d_p<0,
\qquad
u_0=d_p-v_0>0,
\tag{35}
\]

and therefore

\[
|u_0|\asymp|v_0|\asymp d_p.
\tag{36}
\]

The scalar rounding error in either shell is only `O(1/p)=o(d_p)`. Thus the first shell near `16p` duplicates `H`-mass `Theta(d_p)`, while the first shell near `32p` deletes `H`-mass `Theta(d_p)`. Since `H(q)asymp1/p` on both fixed-multiple shells,

\[
\boxed{
\#\{q\in I_{16p}:c_q=+1\}
\asymp
\#\{q\in J_{16p}:c_q=-1\}
\asymp
p d_p
\asymp
\frac{\sqrt p}{\log p}.
}
\tag{37}
\]

This is exactly the support scale forced from below by `RE-180`. The second selector-scale deletion set is not merely an abstract escape allowed by that theorem; it can be placed on ordinary primes at a fixed multiplicative distance and completed to exact two-jet matching by a sparse infinite continuation.

## 5. The exact repair remains below every fixed KV relative envelope

Let `W_j` be the total absolute Chebyshev mass of the modifications made in the two stage-`j` shells. Since each selected prime is comparable with `x_j`, while its `H`-weight is comparable with `1/x_j`,

\[
W_j\ll x_jL_jM_j.
\tag{38}
\]

Using `x_j=16\cdot4^jp`, (26), and (28),

\[
W_j
\ll
2^{-j}\sqrt p\,L_j
+
L_j^2.
\tag{39}
\]

Therefore the total absolute modified Chebyshev mass below any `x` is

\[
\ll
\sqrt p\log p+(\log x)^3.
\tag{40}
\]

The initial packet `D_p` contributes only `O(sqrt(p))`, so (40) proves (3), uniformly also inside a partially traversed shell.

For every fixed `b>0`,

\[
bV(x)=o(\log x),
\]

so eventually

\[
x e^{-bV(x)}\ge x^{3/4}.
\tag{41}
\]

Uniformly for `x>=2p`, the right side dominates both `sqrt(p)log p` and `(log x)^3`. This proves (4). In particular, combining (4) with the ordinary PNT/KV estimate from the line's existing Bellotti anchor shows that `Q_p` itself inherits a fixed KV PNT envelope for every exponent below the ordinary one.

The construction therefore does not pay for exact two-jet matching by leaving the quantitative source class. Its extra complexity is genuinely in **which ordinary primes are deleted or duplicated**, not in a large aggregate counting error.

## 6. What this closes and what remains open

**Two boundary jets are not source-rigid even under bounded honest multiplicity.** `RE-173` needed only one exact boundary charge and a one-sign compensating tail. `RE-175` detected that tail with the first slope, and `RE-179`--`RE-180` showed what any two-jet repair must pay. The present construction pays exactly that price and survives. Thus the package

\[
\text{ordinary primes}
+
 m_Q\in\{0,1,2\}
+
\text{exact Mertens value}
+
\text{exact first slope}
+
\text{KV fidelity}
\]

still does not determine the selected finite Robin prefix.

**The RE-180 cardinality tariff is order-sharp, not merely necessary.** The first negative repair shell already has `Theta(sqrt(p)/log p)` distinct deletions. No larger power-scale support is forced by the first two Euler coordinates alone.

**The construction does not preserve actual multiplicity one.** It is a matched synthetic source with deletions and duplications. The result therefore strengthens the warning that bounded integer multiplicity is still not the missing ordinary-prime invariant; it does not claim a deformation of the actual prime source within multiplicity one, which would of course leave no freedom.

**The first slope remains extra information rather than a Robin-native observable.** Exact two-jet non-rigidity says that even granting this extra source coordinate does not close the matched-control escape. A Robin proof still needs either a genuinely selector-native restriction on the placement pattern, a stronger joint source invariant, or enough Euler information to cross the conditioning boundary identified by `RE-174` and `RE-178`.

**Higher-dimensional continuation is plausible but not automatic.** The two-shell lemma works because two separated slopes span the two boundary coordinates with uniformly bounded condition number. Matching `K+1` jets would require a controlled `(K+1)`-shell moment matrix together with enough prime mass and rounding precision. `RE-178` warns that shallow scalar jets are exponent-neutral, so merely iterating this construction dimension by dimension would not itself produce a Robin closure.

The immediate frontier is therefore no longer whether the `RE-180` local branch exists. It does. The remaining source-specific question is whether **genuine CA selector geometry forbids the required interlaced delete/duplicate pattern**, or whether one needs a genuinely joint moment/integrality invariant beyond the first two boundary coordinates.

## 7. Prior-art and representation audit

The generic mathematical ingredients are classical. Signed and subsum representations of small targets belong to the literature on signed series and achievement sets; nearby references include Armengol Gasull and Francesc Mañosas, *Subseries and signed series*, Communications on Pure and Applied Analysis **18** (2019), 479--492, DOI `10.3934/cpaa.2019024`, and Szymon Glab and Jacek Marchwicki, *Levy--Steinitz theorem and achievement sets of conditionally convergent series on the real plane*, Journal of Mathematical Analysis and Applications **459** (2018), 476--489, DOI `10.1016/j.jmaa.2017.10.034`. Beurling-prime perturbation theory is also broad neighboring literature.

Those results are not load-bearing here. The proof uses the explicit two-shell quantizer above, ordinary-prime PNT density already anchored in `SOURCES.md`, and the line's own Euler kernels. The prior-art search found no theorem asserting the line-specific conjunction of bounded `{0,1,2}` multiplicity on ordinary prime labels, exact value-and-slope matching at `s=1`, arbitrary fixed KV relative fidelity, and a preserved selector-scale transient Robin excursion.

The representation split is therefore clear. The two-dimensional residual-correction mechanism is generic finite-dimensional approximation. The Robin-specific content is the target vector `(d_p,a_Dd_p)` created by the selector packet, the fixed-multiple prime shells that make the first negative repair have exactly selector-scale cardinality, the Euler boundary interpretation of `(H,B)`, and the fact that no repair appears before the order-one Robin measurement at `8p`.

No new external theorem is needed as a load-bearing dependency, so `SOURCES.md` requires no update.
