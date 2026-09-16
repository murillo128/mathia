# FD-154 — Finite-prime avoidance anchors give exact finite-depth coercivity

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact positive construction / growing-anchor boundary / finite-depth coercivity
- **Depends on:** FD-147, FD-151, FD-152, FD-153

## Claim

FD-151--FD-153 quantify a real obstruction for **rank-initial** divisor-closed anchors: bounded parent distortion forces the anchor into positive coefficient mass, and central or supertypical rank anchors then pay a residual child-depth law. That phase diagram is not universal over all divisor-closed anchors.

A fixed finite set of prime coordinates gives an explicit escape. Let

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
D_{S,T}:=\{n\in V_T:(n,P_S)=1\}.
\tag{3}
\]

This anchor is divisor-closed. Put

\[
R_{S,T}:=V_T\setminus D_{S,T}.
\tag{4}
\]

For every `m in R_(S,T)`, let

\[
q_S(m):=(m,P_S),
\qquad
c_S(m):=m/q_S(m).
\tag{5}
\]

Because `m` is squarefree, `q_S(m)` is a nontrivial squarefree divisor of `P_S`, `c_S(m) in D_(S,T)`, and

\[
1\le\omega(q_S(m))\le s.
\tag{6}
\]

Therefore the direct edge

\[
(c_S(m),m)
\tag{7}
\]

is a positive divisibility-ancestry edge of depth at most `s`. Let

\[
E_{S,T}:=\{(c_S(m),m):m\in R_{S,T}\}
\tag{8}
\]

and put uniform edge mass on these edges,

\[
\eta_{S,T}(c_S(m),m):=|R_{S,T}|^{-1}.
\tag{9}
\]

Then for every nonempty `A subseteq R_(S,T)`, every edge entering a vertex of `A` comes directly from the anchor and no other edge of `E_(S,T)` can cross its cut. Hence

\[
\eta_{S,T}(\partial A)=\frac{|A|}{|R_{S,T}|},
\qquad
\nu_T(A)=\frac{|A|}{|V_T|},
\tag{10}
\]

so the anchored Cheeger constant is exactly

\[
\boxed{
 h_{D_{S,T}}(\nu_T,\eta_{S,T})
 =\frac{|V_T|}{|R_{S,T}|}.
}
\tag{11}
\]

More strongly, this is not merely binary coercivity. For every real or complex function `u` on `V_T` with `u=0` on `D_(S,T)` and every `1<=q<infinity`,

\[
\boxed{
 \|u\|_{L^q(V_T,\nu_T)}
 =
 \left(\frac{|R_{S,T}|}{|V_T|}\right)^{1/q}
 \|\nabla u\|_{L^q(E_{S,T},\eta_{S,T})}.
}
\tag{12}
\]

For `q=infinity` the two norms are equal. Thus a finite-prime avoidance anchor plus a bounded-depth direct ancestry relation gives an **exact uniformly coercive Dirichlet frame**, not just a complement-cut lower bound.

The endpoint marginals also have `T`-uniform distortion. The child marginal is exactly uniform on the unanchored set,

\[
\eta_{S,T}^+(m)=|R_{S,T}|^{-1}
\qquad(m\in R_{S,T}),
\tag{13}
\]

so

\[
K_{S,T}=\frac{|V_T|}{|R_{S,T}|}.
\tag{14}
\]

For `d in D_(S,T)`, the number of children assigned to `d` is at most `2^s-1`, one for each nontrivial squarefree divisor of `P_S`. Hence

\[
\eta_{S,T}^-(d)
\le\frac{2^s-1}{|R_{S,T}|}
=(2^s-1)K_{S,T}\nu_T(d),
\tag{15}
\]

so one may take

\[
P_{S,T}\le(2^s-1)K_{S,T}.
\tag{16}
\]

Finally, the squarefree local densities give

\[
\boxed{
 \nu_T(D_{S,T})
 \longrightarrow
 a_S:=\prod_{p\in S}\frac{p}{p+1},
 \qquad
 \nu_T(R_{S,T})
 \longrightarrow1-a_S.
}
\tag{17}
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
\tag{18}
\]

All three resources — anchor exposure, endpoint distortion, and ancestry depth — are therefore bounded in `T` for every fixed finite `S`.

The sharpest elementary instance is a single fixed prime `ell`. Then

\[
D_{\ell,T}=\{n\in V_T:\ell\nmid n\},
\qquad
R_{\ell,T}=\{\ell d\le T:d\in V_T,\ \ell\nmid d\},
\tag{19}
\]

and `d -> ell d` is a bijective one-step matching. In this case

\[
\boxed{
P_{\ell,T}=K_{\ell,T}=h_{D_{\ell,T}}
=\frac{|V_T|}{|R_{\ell,T}|}
\longrightarrow \ell+1.
}
\tag{20}
\]

For `ell=2`, exact one-step coercivity is obtained after anchoring asymptotically `2/3` of the squarefree coefficient space, with both endpoint distortions tending to `3`.

This does not contradict FD-151--FD-153. It identifies their boundary sharply: the expensive child-depth laws arise from anchors aligned with multiplicative **rank**, whereas a prime-avoidance anchor is transverse to one or finitely many prime coordinates and places every remaining coefficient within bounded ancestry distance of the anchor.

## 1. The prime-avoidance set is a divisor-closed coordinate face

If `n in D_(S,T)` and `d|n`, then `(d,P_S)=1`, so `d in D_(S,T)`. Thus (3) is an admissible divisor-closed anchor in the framework of FD-151.

Every squarefree `m` has a unique decomposition

\[
m=c_S(m)q_S(m),
\qquad
(c_S(m),P_S)=1,
\qquad
q_S(m)|P_S.
\tag{21}
\]

For `m` outside the anchor, `q_S(m)>1`. The core `c_S(m)` lies in the anchor and the quotient uses at most `s` prime factors. This proves that every unanchored coefficient is directly visible from the anchor through the depth-`s` relation (8).

The distinction from a rank anchor is structural. A rank anchor `omega(n)<=r` leaves coefficients with arbitrarily large residual rank and therefore needs a probabilistic overshoot analysis. The coordinate face (3) removes **all** primes outside `S` into the anchored core and leaves only the finite `S`-coordinate pattern to cross. No Erdős--Kac or Sathe--Selberg width remains.

## 2. The edge measure is an exact Dirichlet sampling frame

The map

\[
m\mapsto(c_S(m),m)
\tag{22}
\]

places exactly one edge in `E_(S,T)` for each `m in R_(S,T)`. Every edge has its parent in the anchor. Therefore, for `A subseteq R_(S,T)`, an edge crosses `A` if and only if its child belongs to `A`. Equation (10) follows immediately, and taking the infimum over nonempty `A` proves (11).

For the stronger norm identity, let `u=0` on the anchor. Along the unique edge associated with `m`,

\[
\nabla u(c_S(m),m)
=u(m)-u(c_S(m))=u(m).
\tag{23}
\]

Hence

\[
\|\nabla u\|_{L^q(E_{S,T},\eta_{S,T})}^q
=
\frac1{|R_{S,T}|}
\sum_{m\in R_{S,T}}|u(m)|^q,
\tag{24}
\]

whereas

\[
\|u\|_{L^q(V_T,\nu_T)}^q
=
\frac1{|V_T|}
\sum_{m\in R_{S,T}}|u(m)|^q.
\tag{25}
\]

Dividing (25) by (24) proves (12). Thus this construction realizes the positive direction that the anchored-Cheeger classification of FD-147 permits: the boundary measurement is literally a rescaled copy of the entire unanchored coefficient norm.

For Möbius orientations `a_n=mu(n)b(n)`, with `b=1` on the anchor, the same edge has

\[
|a_m+(-1)^{\omega(q_S(m))}a_{c_S(m)}|
=|b(m)-1|
\tag{26}
\]

when the depth edge records the parity of the `S`-prime quotient. In the single-prime case this is the ordinary one-step defect `|a_(ell d)+a_d|`. Thus the construction is compatible with the signed ancestry semantics rather than merely with an abstract graph norm.

## 3. Endpoint distortion stays bounded because the residual coordinate set is finite

Each child occurs once, proving (13)--(14). A parent `d` can receive one child `dq` for each nontrivial `q|P_S` satisfying `dq<=T`. There are at most `2^s-1` such quotients, so

\[
\eta^-_{S,T}(d)
\le\frac{2^s-1}{|R_{S,T}|}.
\tag{27}
\]

Since `nu_T(d)=1/|V_T|`, (15)--(16) follow. The factor `2^s-1` is only a convenient uniform bound; no claim is made that it is optimal for `s>1`.

When `S={ell}`, each participating anchor parent has exactly one possible child `ell d`, so the parent and child distortions coincide exactly with the Cheeger constant, giving (20).

This is the concrete escape that FD-151 leaves open when the anchor has positive coefficient mass. It also shows why merely increasing ancestry depth is not the correct universal complexity parameter: a depth-one relation can be perfectly coercive once the anchor cuts across a prime coordinate rather than across multiplicative rank.

## 4. The anchor and complement have explicit squarefree densities

For fixed `S`, imposing `(n,P_S)=1` on squarefree integers removes the `p`-local exponent-one option for each `p in S`. The standard squarefree count with finitely many excluded primes gives

\[
|D_{S,T}|
=
\frac{T}{\zeta(2)}
\prod_{p\in S}\frac{p}{p+1}
+O_S(\sqrt T),
\tag{28}
\]

while

\[
|V_T|=\frac{T}{\zeta(2)}+O(\sqrt T).
\tag{29}
\]

This proves (17). It is the finite-set extension of the one-prime squarefree-coprimality count already derived in FD-147.

For a single prime `ell`, (28) gives anchor mass `ell/(ell+1)` and complement mass `1/(ell+1)`. The case `ell=2` minimizes the anchor mass among one-coordinate faces. With several fixed primes, `a_S=prod_(p in S)p/(p+1)` can be made smaller while the depth and endpoint constants remain finite in `T`; their dependence on `S` is the explicit cost.

The important qualifier is **fixed** `S`. Letting `S=S_T` grow changes both the depth and the parent-load factor and enters a different resource regime. No uniform statement in growing `S` is claimed here.

## 5. What this does and does not buy for Farey discrepancy

The construction is a positive theorem for the ancestry coercivity subproblem, but it is not a new route to RH by itself. The anchor (3) fixes the true Möbius orientation on a macroscopic arithmetic subset. In the one-prime case it already fixes a fraction `ell/(ell+1)` of all squarefree coefficients; for `ell=2` that is `2/3`. The remaining coefficients are then recovered by the very prime-multiplication relation that defines Möbius parity.

So the result changes the interpretation of the frontier rather than solving the destination problem. FD-151--FD-153 should not be read as saying that bounded-distortion positive ancestry needs `sqrt(log log T)` or `log log T` depth in general. Those depth laws are exact for **rank anchors**. A source-native theorem could evade them through a transversal arithmetic anchor, and FD-154 proves that this possibility is not merely formal.

Conversely, the construction makes the missing burden more explicit. Any use of such an escape in a Farey proof must explain how the Farey observable supplies the macroscopic anchor information without already reconstructing the Möbius source. The correct next audit is therefore not another rank-tail estimate. It is an information/destination test: quantify how much source information a proposed Farey-native anchor reveals, whether that information is independently present in the Farey geometry, and whether the resulting coercive norm transfers stably to the Franel--Landau target rather than simply encoding the target coefficients.

This is precisely where the later information-budget gate of FD-144 becomes relevant. The present construction passes the cut-exposure gate spectacularly, but only by spending a large, explicit source constraint.

## 6. Prior-art and novelty boundary

Dirichlet Poincaré inequalities, weighted Cheeger constants, and coordinate-face/matching constructions on finite graphs are classical. A fresh literature audit found the expected general graph `p`-Laplacian/Cheeger theory and Dirichlet-boundary framework; no external theorem from that literature is load-bearing here. The exact norm identity (12) follows directly from the one-edge-per-child construction.

Likewise, the squarefree local density in (28) is a finite-prime extension of the count already proved and used in FD-147. No new analytic-number-theory input is required, so `SOURCES.md` needs no additional dependency.

No broad novelty is claimed for stars, matchings, coordinate faces, or squarefree local densities. The Mathia-specific contribution is the exact placement of this elementary construction inside the FD-147--FD-153 ancestry model: it realizes bounded-distortion finite-depth coercivity, proves that the rank-depth phase laws are not universal over divisor-closed anchors, and isolates macroscopic source anchoring rather than ancestry depth as the remaining admissibility question.

The finding is falsified if `D_(S,T)` is not divisor-closed, if some unanchored squarefree `m` has no unique `S`-free core, if an edge of (8) requires more than `s` prime adjunctions, or if direct finite evaluation violates (10)--(12). It must not be cited as a source-native Farey anchor, as evidence that the macroscopic anchor is non-circular, or as a new RH-strength estimate.
