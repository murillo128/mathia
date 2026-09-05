# WP-151 — Normalized resultant mass escape is exhaustion-dependent even at the root

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + CYCLOTOMIC-RESULTANT + NORMALIZED-LAPLACIAN + MASS-ESCAPE + EXHAUSTION-DEPENDENCE + REGULARIZATION-CONTROL + MATCHED-GRAPH-CONTROL + PRIOR-ART-AUDITED`

## Claim

`WP-150` proved that every positive vertex-local finite-energy renormalization of the all-prime resultant graph erases each fixed arithmetic edge. For the canonical symmetric normalized Laplacian this gives only finite-core bilinear convergence to the identity, and `WP-150` deliberately left open one possible escape: normalized adjacency mass could move to shell indices tending to infinity, so a cutoff-dependent identification of test vectors might try to follow that mass.

For the resultant graph this moving-mass escape is **not intrinsic to the infinite arithmetic object**. There are two increasing connected finite exhaustions of the same all-prime shell graph, both using the same canonical resultant weights and the same symmetric degree normalization, for which the normalized adjacency applied to the fixed root state `delta_1` has incompatible strong behavior:

\[
\boxed{
\|N_i^{\mathrm{star}}\delta_1\|\longrightarrow1,
\qquad
\|N_i^{\mathrm{cube}}\delta_1\|\longrightarrow0.
}
\tag{1}
\]

In both exhaustions every fixed matrix coefficient tends to zero, so

\[
N_i\delta_1\rightharpoonup0.
\tag{2}
\]

Thus the first exhaustion has pure escape of unit norm to newly introduced prime directions and no strong limit on `delta_1`, while the second has strong convergence to zero. Equivalently, the normalized Laplacians

\[
\mathcal L_i=I-N_i
\tag{3}
\]

both converge weakly to the identity on the root, but only the cube-dominant exhaustion converges strongly there.

The contrast is exact. It comes from two canonical finite subgeometries already forced by the cyclotomic-resultant support: fresh primes form a weighted star around `1`, while all square-free products of a fresh prime block form a weighted Boolean cube. Because the fresh-prime total weight diverges, either geometry can be made to dominate an arbitrary previously included finite core while still producing a genuine full exhaustion.

Therefore the residual mass mentioned in `WP-150` cannot by itself define a Mathia-native positive global object. Any construction that follows it must supply an additional **canonical global exhaustion/test-space identification** and survive a change-of-regularization audit. Positivity of the finite normalized graph operators does not choose that identification, and the all-prime resultant geometry admits mutually incompatible choices.

This does not rule out a separately justified shell-size cutoff, a source-forced completion, a nonlocal renormalization, or a finite--archimedean construction that determines its own topology before normalization. It rules out treating unspecified normalized mass escape as intrinsic evidence for a Weil-positive limit.

## 1. The exact fresh-prime weights

Use the normalized cyclotomic-resultant graph from `WP-145`--`WP-150`:

\[
J_{m,n}
=
\frac{\log|\operatorname{Res}(\Phi_m,\Phi_n)|}
{\sqrt{\varphi(m)\varphi(n)}}\ge0,
\qquad m\ne n.
\tag{4}
\]

Apostol's cyclotomic-resultant theorem makes `J_{m,n}` nonzero exactly when one index is a prime-power multiple of the other. In particular, for every prime `p` not dividing `m`, `WP-148` derived the spectator-invariant fresh-prime edge

\[
J_{m,mp}=a_p,
\qquad
\boxed{a_p:=\frac{\log p}{\sqrt{p-1}}.}
\tag{5}
\]

The positive tail diverges:

\[
\sum_p a_p=\infty.
\tag{6}
\]

For example, for all sufficiently large primes `a_p\ge 1/p`, so Euler's divergence of `\sum_p1/p` suffices. At the same time

\[
M:=\sup_p a_p<\infty,
\tag{7}
\]

because `a_p\to0`.

For a finite connected induced shell set `F`, let

\[
d_F(v)=\sum_{u\in F\setminus\{v\}}J_{v,u},
\qquad
N_F=D_F^{-1/2}J_FD_F^{-1/2}.
\tag{8}
\]

We regard `N_F` as an operator on the ambient `ell^2(N)` by extending it by zero outside `F`. The symmetric normalized Laplacian is `I-N_F` on the nonisolated finite graph. Every graph used below is connected.

## 2. Fresh primes give an exact weighted star

Fix a finite connected core `C` containing `1`, and choose distinct primes

\[
P=\{p_1,\ldots,p_r\}
\tag{9}
\]

all larger than every element of `C`. Set

\[
F^{\mathrm{star}}=C\cup P.
\tag{10}
\]

Each new prime `p_j` is connected to `1` with weight `a_{p_j}`. It has no other edge to `C`: if `c\in C\setminus\{1\}`, then `c<p_j`, `c` has no prime factor `p_j`, and neither ratio `p_j/c` nor `c/p_j` is an integral prime power. Distinct new primes likewise have no resultant edge between them.

Hence, if

\[
A(P)=\sum_{p\in P}a_p,
\qquad
D=d_C(1),
\tag{11}
\]

then every new prime is a genuine leaf of degree `a_p`, while the new root degree is `D+A(P)`. Its contribution to the squared norm of the normalized adjacency vector is therefore

\[
\sum_{p\in P}
\left|
\frac{a_p}{\sqrt{(D+A(P))a_p}}
\right|^2
=
\frac{A(P)}{D+A(P)}.
\tag{12}
\]

Because the omitted old-core contribution is nonnegative,

\[
\boxed{
\|N_{F^{\mathrm{star}}}\delta_1\|^2
\ge
\frac{A(P)}{D+A(P)}.
}
\tag{13}
\]

Since the tail in (6) diverges, a finite fresh block can make `A(P)` arbitrarily larger than the entire pre-existing root degree.

This is not a numerical approximation or a graph analogy. It is an exact induced weighted star inside the cyclotomic-resultant graph.

## 3. The same fresh primes give an exact weighted Boolean cube

Use the same kind of finite core `C` and a fresh prime block `P`, but now adjoin **all square-free products** of primes in `P`:

\[
Q(P)
=
\left\{
\prod_{p\in S}p:S\subseteq P
\right\},
\qquad
F^{\mathrm{cube}}=C\cup Q(P).
\tag{14}
\]

The root `1` already lies in both pieces. Every nontrivial vertex of `Q(P)` is larger than every element of `C`, and its prime factors all lie in `P`. Therefore no new cube vertex is joined to an old vertex of `C\setminus\{1\}`.

Inside `Q(P)`, two vertices have nonzero resultant weight exactly when their subsets differ by toggling one prime. If that prime is `p`, equation (5) gives edge weight exactly `a_p`, independently of the remaining spectator factors. Thus `Q(P)` is the weighted Boolean cube whose direction `p` has conductance `a_p`.

Every cube vertex has internal weighted degree

\[
A(P)=\sum_{p\in P}a_p.
\tag{15}
\]

Only the root also retains its old-core edges, so its total degree is `D+A(P)`. The new neighbors of the root are the singleton primes, and their contribution to the normalized adjacency norm is

\[
\sum_{p\in P}
\frac{a_p^2}{(D+A(P))A(P)}
=
\frac{B(P)}{A(P)(D+A(P))},
\qquad
B(P):=\sum_{p\in P}a_p^2.
\tag{16}
\]

By (7),

\[
B(P)\le M A(P).
\tag{17}
\]

Let

\[
T_C
:=
\sum_{\substack{v\in C\\J_{1,v}>0}}
\frac{J_{1,v}^2}{d_C(v)}<\infty.
\tag{18}
\]

The fresh cube has no edges to those old vertices, so their degrees remain `d_C(v)`. Consequently the **entire** root norm is

\[
\|N_{F^{\mathrm{cube}}}\delta_1\|^2
=
\frac{T_C+B(P)/A(P)}{D+A(P)}
\le
\boxed{
\frac{T_C+M}{D+A(P)}.
}
\tag{19}
\]

Again (6) lets a finite fresh block make `A(P)` arbitrarily large. Therefore the same arithmetic weights that create nearly unit escaped norm in the star completion create arbitrarily small escaped norm once their square-free spectator cube is included.

## 4. Two genuine full exhaustions have incompatible strong limits

The previous comparison can be promoted from two finite test graphs to two **bona fide increasing exhaustions of the whole resultant graph**.

Choose once and for all a nested sequence of finite connected cores

\[
C_1\subset C_2\subset\cdots,
\qquad
\bigcup_r C_r=\mathbb N,
\qquad
1\in C_1.
\tag{20}
\]

Such a sequence exists because the resultant graph is connected: for `n=\prod_jp_j^{e_j}`, one reaches `n` from `1` by successively multiplying by the prime powers `p_j^{e_j}`.

### Star-dominant exhaustion

Starting from the previous stage together with the next core `C_r`, choose a finite block `P_r` of entirely new primes, all larger than the current finite set, with

\[
A(P_r)\ge rD_r,
\tag{21}
\]

where `D_r` is the root degree before adding `P_r`. This is always possible by (6). Let the new stage be the union with these prime leaves.

The stages are finite, connected, nested, and contain every `C_r`, hence exhaust all shell indices. Equation (13) gives

\[
\|N_r^{\mathrm{star}}\delta_1\|^2
\ge
\frac{r}{r+1}.
\tag{22}
\]

The normalized adjacency of any finite weighted graph is a contraction, so the norm is at most one. Therefore

\[
\boxed{
\|N_r^{\mathrm{star}}\delta_1\|\to1.
}
\tag{23}
\]

### Cube-dominant exhaustion

Repeat the construction independently. Before stage `r`, adjoin the next connected core and calculate its finite numbers `D_r,T_r`. Choose a fresh prime block `P_r`, larger than the whole current set, with `A(P_r)` so large that

\[
\frac{T_r+M}{D_r+A(P_r)}\le\frac1r.
\tag{24}
\]

Then adjoin the full square-free cube `Q(P_r)`. The stages again form a finite connected nested exhaustion of all shell indices. Equation (19) gives

\[
\boxed{
\|N_r^{\mathrm{cube}}\delta_1\|^2\le\frac1r,
\qquad
N_r^{\mathrm{cube}}\delta_1\to0
\text{ strongly}.
}
\tag{25}
\]

Equations (23) and (25) prove the exhaustion dependence asserted in (1).

## 5. Both exhaustions have the same fixed-coordinate limit

The contrast does not contradict `WP-150`. Along either exhaustion, the root degree tends to infinity. For every fixed shell `n\ne1`, once `n` is present its normalized coefficient is

\[
\langle\delta_n,N_i\delta_1\rangle
=
\frac{J_{1,n}}
{\sqrt{d_i(1)d_i(n)}}
\longrightarrow0.
\tag{26}
\]

Hence all fixed coordinates vanish. Since `\|N_i\|\le1`, finite-support vectors are dense, and therefore

\[
N_i\delta_1\rightharpoonup0
\tag{27}
\]

for both exhaustions.

In the star-dominant exhaustion, (23) and (27) show that the vector has no strong limit: asymptotically unit norm escapes through ever newer prime leaves. In the cube-dominant exhaustion, (25) says that the same normalized mass is absorbed by the growing spectator cube and disappears strongly at the root.

Thus the finite-core identity limit of `WP-150` is genuine, but it does **not** determine how much norm survives outside every fixed core. That quantity depends on how the all-prime graph is completed at infinity.

## 6. Matched control and why the escaped norm is not arithmetic evidence

The star/cube contrast uses exact arithmetic subgraphs, but the operator phenomenon is generic. Take any positive sequence `a_j` with

\[
\sum_ja_j=\infty,
\qquad
\sup_ja_j<\infty.
\tag{28}
\]

A weighted star with leaf weights `a_j` has normalized root-adjacency norm exactly one. Completing the same directions to a Boolean cube in which every vertex sees all direction weights gives root norm squared

\[
\frac{\sum_ja_j^2}{(\sum_ja_j)^2},
\tag{29}
\]

which tends to zero under (28). The resultant arithmetic supplies the particular weights (5) and, importantly, supplies **both subgeometries exactly** through spectator invariance. But once symmetric degree normalization is applied, the surviving-versus-vanishing norm contrast is ordinary graph geometry rather than a special Mangoldt or Weil signature.

This is a matched-control failure for the proposed escape: a positive moving state extracted solely because `N_i\delta_1` retains norm in one cutoff cannot be interpreted as new arithmetic positivity. The same behavior is reproduced by a free weighted star with no zeta, Gamma factor, explicit formula, or global arithmetic data.

## 7. Prior art and novelty audit

The generic ingredients are classical. The symmetric normalized graph Laplacian `I-D^{-1/2}AD^{-1/2}` is standard; see Fan R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics 92, American Mathematical Society, 1997. Infinite weighted graph Laplacians, unbounded degree, and exhaustion-based spectral definitions are also standard subjects; for example, Bobo Hua and Lili Wang, *Dirichlet p-Laplacian eigenvalues and Cheeger constants on symmetric graphs*, Advances in Mathematics **364** (2020), 106997, DOI `10.1016/j.aim.2020.106997`, explicitly treats finite exhaustions of infinite weighted graphs. Those classical monotone Dirichlet quantities are not the object claimed here: the present issue is that recomputing the **induced finite-graph degree normalization** changes the moving normalized-adjacency state with the cutoff.

The arithmetic support itself is classical: T. M. Apostol, *Resultants of cyclotomic polynomials*, Proceedings of the American Mathematical Society **24** (1970), 457--462, DOI `10.1090/S0002-9939-1970-0251010-X`. `WP-148` and `WP-149` already specialized that theorem to the exact normalized fresh-prime and spectator weights used above.

Targeted searches for strong/exhaustion convergence of normalized graph Laplacians, induced-subgraph degree normalization, weighted hypercubes, and cyclotomic-resultant graph Laplacians located the standard graph-theoretic frameworks but no treatment of this exact all-prime resultant construction. The novelty claim is therefore narrow: **equations (12)--(25) exhibit two explicit full exhaustions of the Mathia resultant graph whose canonical normalized root response has incompatible strong behavior**. No generic graph-theory novelty is claimed, and the result is not a new RH-equivalent criterion.

## 8. Consequence for the Weil-positivity mandate

`WP-148`--`WP-150` left a precise tension. The raw resultant graph has independent finite-cutoff Dirichlet positivity and exact prime-power support, but its all-prime energy space collapses. Local degree normalization restores bounded positive cutoff operators, but every fixed arithmetic edge disappears. The remaining hope was that arithmetic information might survive in the mass moving outside every fixed core.

`WP-151` shows that this residual mass is **not a canonical limit datum of the infinite resultant graph under unspecified finite regularization**. One can make it asymptotically unit at the root or make it vanish strongly while exhausting exactly the same arithmetic object and using exactly the same positive normalization.

Accordingly, a viable continuation must add structure before interpreting escaped mass. At minimum it must specify a Mathia-forced global exhaustion or identification, prove why that choice is intrinsic rather than hand-picked, and test whether the resulting object is stable under matched regularizations that preserve the arithmetic construction. More ambitiously, a successful route may need the source-forced/nonlocal or finite--archimedean coupling already left open by `WP-150`, where the global geometry itself determines the completion rather than relying on a cutoff-dependent normalized graph state.

What is now closed is the inference

\[
\boxed{
\text{positive normalized finite cutoffs}
+\text{mass escaping fixed cores}
\;\Longrightarrow\;
\text{intrinsic global positive arithmetic state}.
}
\tag{30}
\]

The premise is real, but the putative state depends on the exhaustion geometry before any Weil finite/archimedean matching is attempted.
