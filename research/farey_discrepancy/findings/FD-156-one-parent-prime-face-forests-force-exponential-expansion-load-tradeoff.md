# FD-156 — One-parent prime-face forests force an exponential expansion/load tradeoff

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact obstruction / one-parent ancestry / prime-coordinate face resource law
- **Depends on:** FD-151, FD-154, FD-155

## Claim

FD-155 proves that the direct one-edge-per-child frame of FD-154 pays parent distortion of order `2^|S|` when a finite prime-avoidance anchor uses many coordinates, but deliberately leaves open whether a different ancestry measure on the same anchor can avoid that cost. For every **one-parent** divisibility architecture, the direct frame is already optimal for the combined expansion/parent-load resource.

Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1}.
\tag{1}
\]

Fix a nonempty finite set of primes `S`, put

\[
P_S:=\prod_{p\in S}p,
\qquad s:=|S|,
\tag{2}
\]

and retain the prime-avoidance anchor

\[
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
R_{S,T}:=V_T\setminus D_{S,T}.
\tag{3}
\]

Assume `T>=P_S`. A one-parent divisibility forest chooses, for every `m in R_(S,T)`, exactly one parent

\[
\pi(m)\mid m,
\qquad
\pi(m)<m,
\tag{4}
\]

and uses only the edges

\[
E_T^\pi:=\{(\pi(m),m):m\in R_{S,T}\}.
\tag{5}
\]

Because the parent map strictly decreases integers, every chain eventually reaches the divisor-closed anchor. Let `eta_T` be any nonnegative probability measure on `E_T^pi`; its edge weights need not be uniform. Define the anchored Cheeger constant as in FD-151,

\[
h_{S,T}^\pi
:=
\inf_{\varnothing\ne A\subseteq R_{S,T}}
\frac{\eta_T(\partial A)}{\nu_T(A)},
\tag{6}
\]

and define the anchor-side parent distortion

\[
P_{S,T}^\pi
:=
\max_{d\in D_{S,T}}
\frac{\eta_T^-(d)}{\nu_T(d)}.
\tag{7}
\]

Then every such one-parent forest satisfies the exact universal tradeoff

\[
\boxed{
 h_{S,T}^\pi
 \le
 \frac{P_{S,T}^\pi}{2^s-1}.
}
\tag{8}
\]

Equivalently, any uniformly positive anchored expansion `h_(S,T)^pi>=c>0` forces

\[
\boxed{
 P_{S,T}^\pi\ge c(2^s-1).
}
\tag{9}
\]

The factor is sharp. The uniform direct star of FD-154 has

\[
h_{S,T}^{\rm dir}=K_{S,T}:=\frac{|V_T|}{|R_{S,T}|},
\qquad
P_{S,T}^{\rm dir}=(2^s-1)K_{S,T},
\tag{10}
\]

by FD-155, so equality holds in (8).

Thus rerouting children through longer unique-parent chains can reduce the maximum load at the anchor, but only by losing expansion elsewhere. It cannot improve the product law

\[
\boxed{
\frac{P_{S,T}^\pi}{h_{S,T}^\pi}\ge2^s-1.
}
\tag{11}
\]

Consequently the double-exponential thinning cost found in FD-155 is not merely an artifact of its direct star once one requires positive expansion. Let

\[
a(S):=\prod_{p\in S}\frac{p}{p+1}
\tag{12}
\]

be the limiting anchored squarefree mass, and let `s_alpha` be the least coordinate count for which some finite prime set can have `a(S)<=alpha`. FD-155 proves

\[
s_\alpha=\exp\!\bigl(\alpha^{-1+o(1)}\bigr)
\qquad(\alpha\downarrow0).
\tag{13}
\]

Therefore every one-parent prime-avoidance family with fixed expansion `h>=c>0` and limiting anchor exposure at most `alpha` obeys

\[
P\ge c(2^{s_\alpha}-1),
\tag{14}
\]

and hence, in the same fixed-coordinate-then-thinning order of limits as FD-155,

\[
\boxed{
\log\log P
\ge
\alpha^{-1+o(1)}.
}
\tag{15}
\]

The remaining architecture escape on this anchor is therefore genuinely **multi-parent**: a construction must let a child receive/use several ancestry edges, or must leave the finite-prime coordinate-face geometry itself. Merely choosing a cleverer unique ancestor for each coefficient cannot remove the exponential coordinate bill.

## 1. The pure `S`-divisors form a forced Boolean root packet

Consider the nontrivial squarefree divisors of `P_S`,

\[
B_S:=\{q:q\mid P_S,\ q>1\}.
\tag{16}
\]

Since `P_S<=T`, all of them belong to `V_T`, and since each contains at least one prime of `S`, all belong to `R_(S,T)`. Their number is

\[
|B_S|=2^s-1=:N_S.
\tag{17}
\]

Every parent chain starting from `q in B_S` consists only of divisors of `q`. The only divisor of `q` that is coprime to `P_S` is `1`. Hence **every vertex of `B_S` lies in the forest component rooted at the anchor vertex `1`**, independently of how the parent map is chosen.

Remove the root `1` from that component. Its outgoing forest edges

\[
(1,v_1),\ldots,(1,v_J)
\tag{18}
\]

split the component into disjoint full descendant branches `A_1,...,A_J`. Put

\[
n_j:=|A_j\cap B_S|,
\qquad
w_j:=\eta_T(1,v_j).
\tag{19}
\]

Discard branches with `n_j=0`. Since the branches partition all pure `S`-divisors,

\[
\sum_j n_j=N_S.
\tag{20}
\]

Their root-edge weights satisfy

\[
\sum_j w_j
\le
\eta_T^-(1).
\tag{21}
\]

Because `1 in D_(S,T)` and `nu_T(1)=1/|V_T|`, the definition of parent distortion gives

\[
\eta_T^-(1)
\le
\frac{P_{S,T}^\pi}{|V_T|}.
\tag{22}
\]

Weighted averaging of (20)--(22) yields a branch `A_j` with

\[
\frac{w_j}{n_j}
\le
\frac{P_{S,T}^\pi}{|V_T|N_S}.
\tag{23}
\]

This is the entire obstruction: the prime-coordinate Boolean packet has `2^s-1` forced descendants of a single anchor root, while the one-parent hypothesis forces the root mass to split into disjoint branches.

## 2. A full descendant branch has exactly one boundary edge

For the branch selected above, every child of a vertex in `A_j` that belongs to the root component is again in `A_j`, and every non-root vertex has exactly one parent. Consequently the only forest edge crossing the full branch is its root edge `(1,v_j)`. Therefore

\[
\eta_T(\partial A_j)=w_j.
\tag{24}
\]

Moreover `A_j` contains its `n_j` pure divisors, so

\[
\nu_T(A_j)
=\frac{|A_j|}{|V_T|}
\ge
\frac{n_j}{|V_T|}.
\tag{25}
\]

Testing this one set in the anchored Cheeger quotient and using (23) gives

\[
\begin{aligned}
h_{S,T}^\pi
&\le
\frac{w_j}{\nu_T(A_j)}\\
&\le
\frac{w_j|V_T|}{n_j}\\
&\le
\frac{P_{S,T}^\pi}{N_S}
=
\frac{P_{S,T}^\pi}{2^s-1}.
\end{aligned}
\tag{26}
\]

This proves (8). Notice what is absent from the proof: no uniform edge weights, no child-marginal hypothesis, no bound on ancestry depth, no prime number theorem, and no asymptotic estimate. The finite Boolean packet alone forces the tradeoff as soon as `T>=P_S`.

If a root edge has zero weight, its positive-size descendant branch already has zero boundary and `h=0`; the same argument includes that degenerate case automatically.

## 3. Direct stars are product-optimal, while sequential rerouting moves the bill

The direct frame of FD-154 sends every child straight to its `S`-free core. FD-155 shows that, for `T>=P_S`, the root `1` then has all `2^s-1` pure `S`-divisors as direct children. With uniform edge weights this gives exactly (10), and therefore

\[
\frac{P_{S,T}^{\rm dir}}{h_{S,T}^{\rm dir}}
=2^s-1.
\tag{27}
\]

So (11) is sharp over the complete one-parent class.

A complementary construction shows why minimizing `P` alone is misleading. Order

\[
S=\{p_1<\cdots<p_s\}
\tag{28}
\]

and, for every nonanchor `m`, remove its largest `S`-prime,

\[
\pi_{\max}(m)
:=
\frac{m}{\max\{p\in S:p\mid m\}}.
\tag{29}
\]

Give every forest edge mass `1/|R_(S,T)|`. The `S`-free core is preserved along each chain. Every anchor vertex has at most one child for each prime of `S`, while the root has exactly the `s` children `p_1,...,p_s`; hence

\[
P_{S,T}^{\rm seq}=sK_{S,T}.
\tag{30}
\]

This is exponentially smaller than the direct parent load. But every descendant subtree has at most `2^(s-1)` vertices: once its first active `S`-prime is fixed, only larger primes can be adjoined below it in the reverse orientation. For any nonempty `A subseteq R_(S,T)`, let `M(A)` be the vertices of `A` whose parent lies outside `A`. The descendant subtrees rooted at `M(A)` cover `A`, so

\[
|A|\le2^{s-1}|M(A)|.
\tag{31}
\]

Each member of `M(A)` contributes a distinct crossing edge of weight `1/|R_(S,T)|`. Therefore

\[
\frac{\eta_T(\partial A)}{\nu_T(A)}
\ge
\frac{K_{S,T}}{2^{s-1}}.
\tag{32}
\]

Equality is attained by the full branch rooted at `p_1`: because `T>=P_S`, it contains exactly the `2^(s-1)` pure divisors of `P_S` containing `p_1`, and it has one crossing edge. Thus

\[
\boxed{
h_{S,T}^{\rm seq}
=
\frac{K_{S,T}}{2^{s-1}},
\qquad
P_{S,T}^{\rm seq}=sK_{S,T}.
}
\tag{33}
\]

Sequential rerouting has therefore not defeated FD-155's resource issue. It has transferred the exponential factor from anchor congestion into a narrow descendant cut. The exact universal statement is not that every forest must have exponential `P`; it is that **fixed expansion and small `P` cannot coexist once the Boolean coordinate dimension grows**.

## 4. Thinning the anchor remains double-exponentially expensive at fixed expansion

For a fixed prime set `S`, FD-154 gives the limiting anchor density

\[
a(S)=\prod_{p\in S}\frac{p}{p+1}.
\tag{34}
\]

FD-155 proves that among `s`-element prime sets the first `s` primes minimize this density, and that the least `s=s_alpha` capable of `a(S)<=alpha` satisfies (13). Combining that coordinate lower bound with (9) gives (14) immediately.

Taking logarithms twice,

\[
\log\log P
\ge
\log s_\alpha+O(1)
=
\alpha^{-1+o(1)},
\tag{35}
\]

which is (15). Thus the direct frame's double-exponential parent load was quantitatively sharp for fixed expansion within the whole one-parent prime-face family, even though its particular location of that load at the root was not forced.

This also explains the relation to FD-151. The general complement-cut inequality there gives only

\[
P\ge h\frac{1-a(S)}{a(S)},
\tag{36}
\]

which becomes roughly reciprocal in the anchor mass. The new Boolean-root cut is much stronger for the prime-avoidance geometry because it uses the `2^s-1` distinct pure coordinate states that are all forced to descend from the same anchor point. It is therefore a geometry-specific strengthening, not a contradiction to the universal mass law.

## 5. Prior-art, scope, and falsification boundary

The ingredients are elementary and classical: the nontrivial divisors of a squarefree product form a punctured Boolean lattice, and deleting a root from a tree partitions it into descendant branches. A targeted literature audit found the expected Boolean-lattice, rooted-tree, spanning-tree, and divisor-poset background, but no load/anchored-expansion statement matching (8) in the present Möbius prime-face setting. No external theorem is load-bearing: (8) is the finite argument (16)--(26), and the thinning asymptotic is imported only from the already persisted FD-155.

The evidence classification is therefore **EXACT-DERIVED / NEGATIVE-OBSTRUCTION**. The potentially new content is the identification of the forced pure-prime Boolean packet as a sharp resource certificate for one-parent ancestry, not the underlying Boolean lattice or tree facts themselves.

The hypotheses are essential. Equation (8) is a theorem for a single-parent forest on the FD-154 prime-avoidance anchor. It does **not** apply to a DAG in which a child can receive several parent edges, to signed edge measures, to a different divisor-closed anchor, or to a non-ancestry transform. It also does not establish that a multi-parent construction can succeed; it only identifies where this obstruction stops applying.

The result is falsified if some `q|P_S`, `q>1`, can terminate at an anchor other than `1`; if the one-parent root branches fail to partition the `2^s-1` pure divisors; if a full descendant branch can have a second crossing forest edge; or if the direct FD-154 frame fails to attain equality in (8). All of these are finite structural checks.

## 6. Consequence for the Farey frontier

FD-155 left open the possibility that its double-exponential parent load was simply a bad choice of edge measure. FD-156 closes that escape for the broadest natural unique-parent repair: arbitrary rerouting, arbitrary depths, and arbitrary nonnegative edge weights cannot improve the sharp combined law `P/h>=2^s-1`.

The remaining architecture question is therefore narrower. To thin a prime-coordinate anchor while keeping conditioning and coercivity moderate, a candidate must use genuinely multi-parent mixing or a different anchor geometry; a unique ancestry chain per coefficient is insufficient. Even then, the source-provenance and Franel--Landau destination gates remain untouched: no ancestry construction matters for RH unless the required anchor orientation is available from Farey data without circular Möbius reconstruction and the resulting norm controls the RH-equivalent discrepancy at the critical scale.
