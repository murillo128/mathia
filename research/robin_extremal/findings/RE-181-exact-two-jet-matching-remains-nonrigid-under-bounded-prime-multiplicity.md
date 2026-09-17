# RE-181 — Exact two-jet matching remains non-rigid under bounded prime multiplicity

**Status:** `EXACT-DERIVED + CONSTRUCTIVE-CONTROL + ORDINARY-PRIME-SUPPORT + MULTIPLICITY-012 + EXACT-TWO-JET-MATCHING + KV-FIDELITY + TRANSIENT-ROBIN-AMBIGUITY + RE-180-EARLY-TARIFF-SCALE-ATTAINED + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-173, RE-175, RE-179, RE-180.

`RE-180` shows that once the relaxed signed model is returned to honest ordinary-prime multiplicities, exact Mertens value plus exact first Euler boundary slope force a second deletion set of cardinality at least

\[
\Omega\!\left(\frac{\sqrt p}{\log p}\right)
\]

unless the repair pays the remote KV-weighted reset budget of `RE-179`. That result prices the local branch but does not decide whether the branch is realizable.

It is realizable at that early-support scale.

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
   satisfies
   \[
   \boxed{D_{Q_p}(1+)=D_{Q_p}'(1+)=0;}
   \tag{2}
   \]
4. its Chebyshev discrepancy obeys
   \[
   \boxed{
   |\vartheta_{Q_p}(x)-\vartheta(x)|
   \ll \sqrt p\log p+(\log x)^3
   \qquad(x\ge2p),
   }
   \tag{3}
   \]
   and hence, for every fixed `b>0`,
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
6. the first positive repair packet lies near `16p`, the first negative repair packet lies near `32p`, and each uses
   \[
   \boxed{
   \Theta\!\left(\frac{\sqrt p}{\log p}\right)
   }
   \tag{6}
   \]
   distinct ordinary primes.

Thus **two exact Euler boundary coordinates still do not rigidify the transient Robin prefix**, even after ordinary-prime support, nonnegative integer multiplicity, a fixed multiplicity cap, and arbitrarily strong fixed KV relative fidelity are imposed simultaneously. The local early-deletion scale forced by `RE-180` is actually attained in the first repair shell; exact equality still requires an infinite continuation, as it must already for the zeroth coordinate by `RE-172`.

The construction uses an explicit two-shell quantizer. At each later scale, two disjoint narrow ordinary-prime shells have different Euler slopes. Their signed `H`-masses span the two-dimensional boundary residual over the reals; prime density discretizes those two real masses with a smaller residual. Iterating on geometrically increasing shells drives the residual to zero while keeping both boundary series absolutely convergent.

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

The deletion packet contributes `(-d_p,-b_p)` to the `(H,B)` boundary vector. It therefore suffices to construct a repair on ordinary primes `q>=16p` whose absolutely convergent signed boundary vector is exactly

\[
\boxed{(d_p,b_p).}
\tag{12}
\]

No repair occurs below `16p`. Consequently the `RE-173` calculation at observation height `8p` is unchanged. With its normalization `Z_p=2+o(1)`, every deleted `q in [2p,3p]` contributes a positive amount comparable with `1/p`, and

\[
\frac{\sqrt p\log p}{Z_p}
\sum_{q\in D_p}
\log q\,[h(q)-h(8p)]
\asymp1.
\tag{13}
\]

This proves (5) once the exact repair is constructed.

## 2. A two-shell ordinary-prime quantizer

Extend `A` to real `t>1` by the formula in (7). The elementary expansion of `log(1+1/(t-1))` gives

\[
A(t)=\log t+O\!\left(\frac{\log t}{t}\right),
\qquad
A'(t)=\frac1t+O\!\left(\frac{\log t}{t^2}\right).
\tag{14}
\]

For large `x`, put

\[
\delta_x:=(\log x)^{-4}
\]

and take two disjoint shells

\[
I_x=[x,x(1+\delta_x)],
\qquad
J_x=[2x,2x(1+\delta_x)].
\tag{15}
\]

The PNT with the line's already anchored KV error gives

\[
\vartheta(x(1+\delta_x))-\vartheta(x)
\sim \delta_x x,
\tag{16}
\]

because `exp(-aV(x))=o((log x)^(-4))`. Dividing the corresponding prime count by the shell scale, or equivalently using `H(q)asymp1/q`, yields

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

For a residual `r=(r_H,r_B)`, define

\[
M_x(r):=|r_B|+\log x\,|r_H|.
\tag{18}
\]

Assume

\[
M_x(r)\le c_0(\log x)^{-6}
\tag{19}
\]

for a sufficiently small fixed `c_0`. Put

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

Hence the real system

\[
u+v=r_H,
\qquad
a_xu+b_xv=r_B
\tag{21}
\]

has a unique solution with

\[
\boxed{|u|+|v|\ll M_x(r).}
\tag{22}
\]

Interpret `u` and `v` as signed target `H`-masses. By (17), (19), and (22), either shell contains much more total `H`-mass than the required target. In `I_x`, choose distinct primes greedily with the sign of `u` until their `H`-sum is the largest one not exceeding `|u|`; do the same in `J_x` for `v`. Every shell atom has `H(q)=O(1/x)`, so each scalar rounding error is `O(1/x)`.

Across a shell, (14) also gives an `A`-variation of `O(delta_x)`. Therefore the signed prime vector selected from the two shells leaves a residual `r'=(r_H',r_B')` satisfying

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

The total absolute `H`-mass used in this step is `O(M_x(r))`. This is the only discretization lemma needed below.

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

The shells `I_(x_j)` and `J_(x_j)` are pairwise disjoint and all lie above `8p`. Start with

\[
r^{(0)}:=(d_p,b_p).
\tag{25}
\]

By (9) and (11),

\[
M_0:=M_{x_0}(r^{(0)})\ll\frac1{\sqrt p},
\tag{26}
\]

which is `o(L_0^(-6))`. Apply the quantizer at `x_0`, subtract its signed prime vector, and repeat at `x_1,x_2,...`.

Writing

\[
M_j:=M_{x_j}(r^{(j)}),
\]

(23) gives

\[
M_{j+1}
\ll
L_j^{-4}M_j+
\frac{L_j}{x_j}.
\tag{27}
\]

For sufficiently large `p`, the implied constant times `L_j^(-4)` is at most `1/8` for every `j`. The invariant `M_j<<L_j^(-6)` is preserved, so every later shell has enough primes. Moreover

\[
\boxed{
M_j
\ll
8^{-j}M_0+
\frac{L_j}{x_j}.
}
\tag{28}
\]

Thus `r^(j)->0`.

Assign coefficient `+1` to every repair prime selected with positive sign and `-1` to every repair prime selected with negative sign. Since all shells are disjoint from one another and from `D_p`, no prime is modified twice. With the initial packet included,

\[
c_q:=m_{Q_p}(q)-1\in\{-1,0,1\},
\]

which proves (1).

The absolute `H`-mass at stage `j` is `O(M_j)`, so

\[
\sum_q |c_q|H(q)<\infty.
\tag{29}
\]

All stage-`j` primes are comparable with `x_j`, hence

\[
\sum_q |c_q|B(q)
\ll
\sum_{j\ge0}L_jM_j
<\infty.
\tag{30}
\]

Since the residual boundary vector tends to zero, the repair satisfies

\[
\sum_{q\notin D_p}c_qH(q)=d_p,
\qquad
\sum_{q\notin D_p}c_qB(q)=b_p.
\tag{31}
\]

Restoring the initial negative packet gives

\[
\boxed{
\sum_q c_qH(q)=0,
\qquad
\sum_q c_qB(q)=0.
}
\tag{32}
\]

By `RE-175`, these are exactly

\[
D_{Q_p}(1+)=0,
\qquad
D_{Q_p}'(1+)=-\sum_qc_qB(q)=0,
\]

with both boundary sums absolutely convergent. This proves (2).

## 4. The first repair attains the RE-180 early-deletion scale

The first stage has a fixed sign pattern. Put

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

Solving

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

and hence

\[
|u_0|\asymp|v_0|\asymp d_p.
\tag{36}
\]

The scalar rounding error in either shell is `O(1/p)=o(d_p)`. Thus the first shell near `16p` duplicates `H`-mass `Theta(d_p)`, while the first shell near `32p` deletes `H`-mass `Theta(d_p)`. Since `H(q)\asymp1/p` on both fixed-multiple shells,

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

This realizes, in the first negative repair shell, the same selector-scale cardinality that `RE-180` forces from below when the local branch is used. The complete exact control still has infinite support; the claim is sharpness of the **early local scale**, not finiteness of the total repair support.

## 5. The exact repair remains below every fixed KV relative envelope

Let `W_j` be the total absolute Chebyshev mass of the modifications in the two stage-`j` shells. Since each selected prime is comparable with `x_j`, while its `H`-weight is comparable with `1/x_j`,

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

The initial packet contributes only `O(sqrt(p))`, so (40) proves (3), including points lying inside a partially traversed shell.

For every fixed `b>0`,

\[
bV(x)=o(\log x),
\]

so eventually

\[
x e^{-bV(x)}\ge x^{3/4}.
\tag{41}
\]

Uniformly for `x>=2p`, the right side dominates both `sqrt(p)log p` and `(log x)^3` once `p` is sufficiently large. This proves (4). Combining it with the ordinary PNT/KV estimate already anchored in the line also gives a fixed KV PNT envelope for `Q_p` itself for every exponent below the ordinary one.

The construction therefore does not buy exact two-jet matching by leaving the quantitative source class. Its extra complexity is in **which ordinary primes are deleted or duplicated**, not in a large aggregate counting error.

## 6. What this closes and what remains open

**Two boundary jets remain non-rigid under bounded honest multiplicity.** `RE-173` needed one exact boundary charge and a one-sign compensating tail. `RE-175` detected that tail with the first slope, and `RE-179`--`RE-180` priced every two-jet repair. The present construction pays the local price and survives. Thus the package

\[
\text{ordinary-prime support}
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

**The second selector-scale deletion set is therefore not itself an obstruction.** Genuine CA/Robin structure would have to forbid its *placement pattern* or couple it to another source quantity; cardinality alone cannot close the matched-control escape.

**The construction does not preserve actual multiplicity one.** It is a matched synthetic source with deletions and duplications. The theorem says that bounded integer multiplicity is still not the missing ordinary-prime invariant; it does not claim a deformation of the actual prime source while retaining multiplicity one.

**The first slope remains extra information rather than a Robin-native observable.** Exact two-jet non-rigidity says that even granting this extra coordinate does not close the escape. A Robin proof still needs a genuinely selector-native restriction, a stronger joint source invariant, or enough Euler information to cross the conditioning boundary identified by `RE-174` and `RE-178`.

**Higher-dimensional continuation is plausible but not automatic.** The two-shell lemma works because two separated slopes span the two boundary coordinates with uniformly bounded condition number. Matching `K+1` jets would require a controlled `(K+1)`-shell moment matrix together with enough prime mass and rounding precision. `RE-178` already warns that shallow scalar jets are exponent-neutral, so merely adding a few coordinates need not produce Robin closure.

The immediate frontier is therefore no longer whether the `RE-180` local branch exists. It does. The source-specific question is whether **genuine CA selector geometry forbids the required interlaced delete/duplicate pattern**, or whether one needs a genuinely joint moment/integrality invariant beyond the first two boundary coordinates.

## 7. Prior-art and representation audit

The generic mathematical ingredients are classical. Signed and subsum representations of small targets belong to the literature on signed series and achievement sets; nearby references include Armengol Gasull and Francesc Mañosas, *Subseries and signed series*, Communications on Pure and Applied Analysis **18** (2019), 479--492, DOI `10.3934/cpaa.2019024`, and Szymon Glab and Jacek Marchwicki, *Levy--Steinitz theorem and achievement sets of conditionally convergent series on the real plane*, Journal of Mathematical Analysis and Applications **459** (2018), 476--489, DOI `10.1016/j.jmaa.2017.10.034`. Beurling-prime perturbation theory is broader neighboring literature.

Those results are not load-bearing here. The proof uses the explicit two-shell quantizer above, ordinary-prime PNT density already anchored in `SOURCES.md`, and the line's own Euler kernels. The prior-art search found no theorem asserting the line-specific conjunction of bounded `{0,1,2}` multiplicity on ordinary prime labels, exact value-and-slope matching at `s=1`, arbitrary fixed KV relative fidelity, and a preserved selector-scale transient Robin excursion.

The representation split is clear. The two-dimensional residual-correction mechanism is generic finite-dimensional approximation. The Robin-specific content is the target vector `(d_p,a_Dd_p)` created by the selector packet, the fixed-multiple prime shells that make the first negative repair have exactly selector-scale cardinality, the Euler boundary interpretation of `(H,B)`, and the absence of any repair before the order-one Robin measurement at `8p`.

No new external theorem is needed as a load-bearing dependency, so `SOURCES.md` requires no update.
