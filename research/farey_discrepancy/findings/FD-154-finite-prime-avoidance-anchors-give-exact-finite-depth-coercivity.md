# FD-154 — Finite-prime avoidance anchors give exact finite-depth coercivity

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact positive construction / growing-anchor boundary / finite-depth coercivity
- **Depends on:** FD-147, FD-151, FD-152, FD-153

## Claim

FD-151--FD-153 quantify a real obstruction for **rank-initial** divisor-closed anchors: bounded parent distortion forces the anchor into positive coefficient mass, and central or supertypical rank anchors then pay a residual child-depth law. That phase diagram is not universal over all divisor-closed anchors.

Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n):=|V_T|^{-1}.
\tag{1}
\]

Fix a nonempty finite set of primes `S`, write

\[
P_S:=\prod_{p\in S}p,
\qquad s:=|S|,
\tag{2}
\]

and define the prime-avoidance anchor

\[
D_{S,T}:=\{n\in V_T:(n,P_S)=1\},
\qquad
R_{S,T}:=V_T\setminus D_{S,T}.
\tag{3}
\]

For every `m in R_(S,T)`, define its `S`-part and `S`-free core by

\[
q_S(m):=(m,P_S),
\qquad
c_S(m):=m/q_S(m).
\tag{4}
\]

Because `m` is squarefree, `q_S(m)` is a nontrivial squarefree divisor of `P_S`, `c_S(m) in D_(S,T)`, and

\[
1\le\omega(q_S(m))\le s.
\tag{5}
\]

Hence the direct edge `(c_S(m),m)` is a positive divisibility-ancestry edge of depth at most `s`. Let

\[
E_{S,T}:=\{(c_S(m),m):m\in R_{S,T}\}
\tag{6}
\]

and put uniform edge mass on these edges,

\[
\eta_{S,T}(c_S(m),m):=|R_{S,T}|^{-1}.
\tag{7}
\]

Then for every nonempty `A subseteq R_(S,T)`,

\[
\eta_{S,T}(\partial A)=\frac{|A|}{|R_{S,T}|},
\qquad
\nu_T(A)=\frac{|A|}{|V_T|},
\tag{8}
\]

so the anchored Cheeger constant is exactly

\[
\boxed{
 h_{D_{S,T}}(\nu_T,\eta_{S,T})
 =\frac{|V_T|}{|R_{S,T}|}.
}
\tag{9}
\]

More strongly, this is not merely binary coercivity. For every real or complex function `u` on `V_T` with `u=0` on `D_(S,T)` and every `1<=q<infinity`,

\[
\boxed{
 \|u\|_{L^q(V_T,\nu_T)}
 =
 \left(\frac{|R_{S,T}|}{|V_T|}\right)^{1/q}
 \|\nabla u\|_{L^q(E_{S,T},\eta_{S,T})}.
}
\tag{10}
\]

For `q=infinity` the two norms are equal. Thus a finite-prime avoidance anchor plus a bounded-depth direct ancestry relation gives an **exact uniformly coercive Dirichlet frame**.

The endpoint marginals also have `T`-uniform distortion. The child marginal is uniform on the unanchored set, so

\[
K_{S,T}=\frac{|V_T|}{|R_{S,T}|}.
\tag{11}
\]

A parent `d in D_(S,T)` has at most `2^s-1` children, one for each nontrivial squarefree divisor of `P_S`; therefore one may take

\[
P_{S,T}\le(2^s-1)K_{S,T}.
\tag{12}
\]

Finally,

\[
\boxed{
 \nu_T(D_{S,T})
 \longrightarrow
 a_S:=\prod_{p\in S}\frac{p}{p+1},
 \qquad
 \nu_T(R_{S,T})
 \longrightarrow1-a_S.
}
\tag{13}
\]

Consequently

\[
\boxed{
 h_{D_{S,T}}
 =K_{S,T}
 \longrightarrow\frac1{1-a_S},
 \qquad
 \limsup P_{S,T}
 \le\frac{2^s-1}{1-a_S}.
}
\tag{14}
\]

All three resources — anchor exposure, endpoint distortion, and ancestry depth — are therefore bounded in `T` for every fixed finite `S`.

For a single fixed prime `ell`, the construction becomes a one-step matching:

\[
D_{\ell,T}=\{n\in V_T:\ell\nmid n\},
\qquad
R_{\ell,T}=\{\ell d\le T:d\in V_T,\ \ell\nmid d\}.
\tag{15}
\]

In that case

\[
\boxed{
P_{\ell,T}=K_{\ell,T}=h_{D_{\ell,T}}
=\frac{|V_T|}{|R_{\ell,T}|}
\longrightarrow \ell+1.
}
\tag{16}
\]

For `ell=2`, exact one-step coercivity is obtained after anchoring asymptotically `2/3` of the squarefree coefficient space, with both endpoint distortions tending to `3`.

This does not contradict FD-151--FD-153. It identifies their boundary sharply: the expensive child-depth laws arise from anchors aligned with multiplicative **rank**, whereas a prime-avoidance anchor is transverse to one or finitely many prime coordinates and places every remaining coefficient within bounded ancestry distance of the anchor.

## 1. Prime avoidance is a divisor-closed coordinate face

If `n in D_(S,T)` and `d|n`, then `(d,P_S)=1`, so `d in D_(S,T)`. Thus (3) is an admissible divisor-closed anchor in the framework of FD-151.

Every squarefree `m` has the unique decomposition

\[
m=c_S(m)q_S(m),
\qquad
(c_S(m),P_S)=1,
\qquad
q_S(m)|P_S.
\tag{17}
\]

For `m` outside the anchor, `q_S(m)>1`, so its anchored core is reached after removing at most `s` prime factors. This is structurally different from a rank anchor. A rank anchor `omega(n)<=r` leaves coefficients with arbitrarily large residual rank and therefore needs a probabilistic overshoot analysis. The coordinate face (3) absorbs every prime outside `S` into the anchored core and leaves only the finite `S`-coordinate pattern to cross. No Erdos--Kac or Sathe--Selberg width remains.

## 2. The edge measure is an exact Dirichlet sampling frame

The map

\[
m\mapsto(c_S(m),m)
\tag{18}
\]

places exactly one edge in `E_(S,T)` for each `m in R_(S,T)`, and every such edge starts in the anchor. Hence an edge crosses `A subseteq R_(S,T)` if and only if its child lies in `A`, proving (8)--(9).

For the stronger norm identity, let `u=0` on the anchor. Along the unique edge associated with `m`,

\[
\nabla u(c_S(m),m)=u(m)-u(c_S(m))=u(m).
\tag{19}
\]

Therefore

\[
\|\nabla u\|_{L^q(E_{S,T},\eta_{S,T})}^q
=
\frac1{|R_{S,T}|}
\sum_{m\in R_{S,T}}|u(m)|^q,
\tag{20}
\]

whereas

\[
\|u\|_{L^q(V_T,\nu_T)}^q
=
\frac1{|V_T|}
\sum_{m\in R_{S,T}}|u(m)|^q.
\tag{21}
\]

This proves (10) directly. The construction therefore realizes the positive side permitted by the anchored-Cheeger classification of FD-147: the boundary measurement is literally a rescaled copy of the complete unanchored coefficient norm.

For Möbius-oriented coefficients `a_n=mu(n)b(n)` with `b=1` on the anchor, squarefreeness and (17) give

\[
\mu(m)=(-1)^{\omega(q_S(m))}\mu(c_S(m)).
\tag{22}
\]

Hence the signed depth-edge defect is

\[
\boxed{
\left|a_m-(-1)^{\omega(q_S(m))}a_{c_S(m)}\right|
=|b(m)-1|.
}
\tag{23}
\]

For a single prime, `omega(q_S(m))=1`, so (23) is the ordinary one-step defect `|a_(ell d)+a_d|`. Thus the construction respects the signed Möbius ancestry semantics rather than only an abstract graph norm.

## 3. Endpoint distortion stays bounded because only finitely many prime coordinates remain

Each child occurs exactly once, proving (11). A parent `d` can receive one child `dq` for each nontrivial `q|P_S` satisfying `dq<=T`. There are at most `2^s-1` such quotients, so

\[
\eta^-_{S,T}(d)
\le\frac{2^s-1}{|R_{S,T}|}
=(2^s-1)K_{S,T}\nu_T(d),
\tag{24}
\]

which is (12). The factor `2^s-1` is only a convenient uniform bound; no optimality is claimed for `s>1`.

When `S={ell}`, every participating anchor parent has one possible child `ell d`. Parent and child distortions then coincide exactly with the Cheeger constant, proving (16).

This is a concrete realization of the positive-density escape left open by FD-151. It also shows why ancestry depth is not a universal complexity parameter: depth one can be perfectly coercive once the anchor cuts across a prime coordinate rather than across multiplicative rank.

## 4. The anchor and complement have explicit squarefree densities

For fixed `S`, imposing `(n,P_S)=1` on squarefree integers removes the exponent-one option at each `p in S`. The finite-prime squarefree count gives

\[
|D_{S,T}|
=
\frac{T}{\zeta(2)}
\prod_{p\in S}\frac{p}{p+1}
+O_S(\sqrt T),
\tag{25}
\]

while

\[
|V_T|=\frac{T}{\zeta(2)}+O(\sqrt T).
\tag{26}
\]

This proves (13). It is exactly the finite-set extension of the one-prime squarefree-coprimality count already derived in FD-147.

For `S={ell}`, the anchor mass tends to `ell/(ell+1)` and the complement mass to `1/(ell+1)`. The case `ell=2` minimizes the anchor mass among one-coordinate faces. With several fixed primes, `a_S=prod_(p in S)p/(p+1)` decreases while the depth and endpoint constants remain finite in `T`; their dependence on `S` is the explicit price.

The qualifier **fixed** `S` is essential. Letting `S=S_T` grow changes both the ancestry depth and the parent-load factor and enters a different resource regime. No uniform statement for growing `S` is claimed here.

## 5. Consequence for the current Farey frontier

The construction is a positive theorem for the ancestry-coercivity subproblem, but it is not a new route to RH by itself. The anchor (3) fixes the true Möbius orientation on a macroscopic arithmetic subset. In the one-prime case it fixes a fraction `ell/(ell+1)` of all squarefree coefficients; for `ell=2` this is `2/3`. The rest are then recovered by the same prime-multiplication parity relation that defines Möbius on squarefree integers.

Accordingly, FD-151--FD-153 should not be read as saying that bounded-distortion positive ancestry needs `sqrt(log log T)` or `log log T` depth in general. Those depth laws are exact for **rank anchors**. A source-native theorem can evade them through a transversal arithmetic anchor, and FD-154 proves that this escape is mathematically realizable rather than merely an artifact of an upper bound.

The missing burden is therefore now more specific. Any use of such an anchor in a Farey proof must explain how the Farey observable supplies the macroscopic anchored source information without already reconstructing the Möbius coefficients. After that, the resulting coercive norm still has to transfer stably to the Franel--Landau destination rather than merely encode the target source.

This is where the information-budget gate of FD-144 becomes decisive. FD-154 passes the cut-exposure gate exactly, but it does so by spending a large, explicit source constraint. The next useful theorem should quantify that source-information expenditure for proposed Farey-native anchors, not extend the rank-tail phase diagram again.

## 6. Prior-art and novelty boundary

Dirichlet Poincare inequalities, weighted Cheeger constants, and matching/coordinate-face constructions on finite graphs are classical. A fresh literature audit found the expected general graph `p`-Laplacian and Dirichlet-Cheeger framework; no external theorem from that literature is load-bearing here. The exact norm identity (10) follows directly from the one-edge-per-child construction.

Likewise, (25) is a finite-prime extension of squarefree counting already proved and used inside FD-147. No new analytic-number-theory input is required, so `SOURCES.md` needs no additional dependency.

No broad novelty is claimed for matchings, coordinate faces, or squarefree local densities. The Mathia-specific contribution is their exact placement inside the FD-147--FD-153 ancestry model: they realize bounded-distortion finite-depth coercivity, prove that the rank-depth phase laws are not universal over divisor-closed anchors, and isolate macroscopic source anchoring rather than ancestry depth as the remaining admissibility question.

The finding is falsified if `D_(S,T)` is not divisor-closed, if some unanchored squarefree `m` lacks the unique `S`-free core (17), if an edge of (6) requires more than `s` prime adjunctions, or if direct finite evaluation violates (8)--(10). It must not be cited as a source-native Farey anchor, as evidence that the macroscopic anchor is non-circular, or as an RH-strength estimate.
