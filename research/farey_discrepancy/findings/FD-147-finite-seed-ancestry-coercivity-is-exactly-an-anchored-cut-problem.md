# FD-147 — Finite-seed ancestry coercivity is exactly an anchored cut problem

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact binary-coercivity classification / stronger full-ancestry no-go theorem
- **Depends on:** FD-145, FD-146

## Claim

FD-145 identifies a `Z_2` orientation gauge on ancestry components disconnected from the Möbius anchor. FD-146 shows that restoring connectivity does not make uniformly normalized finite-`L^q` ancestry energy coercive: a fixed-rank wall has vanishing normalized boundary mass. The correct finite-`L^q` obstruction can be stated exactly.

Let `G=(V,E)` be a finite graph, let `D\subseteq V` be a nonempty anchored seed, and let `nu` and `eta` be probability measures on vertices and edges. For a binary orientation

\[
b:V\to\{-1,+1\},\qquad b\equiv1\text{ on }D,
\tag{1}
\]

write

\[
A_b:=\{v\in V:b(v)=-1\}\subseteq V\setminus D.
\tag{2}
\]

For every fixed `1<=q<infinity`, one has the exact identities

\[
\boxed{
\|b-1\|_{L^q(V,\nu)}=2\,\nu(A_b)^{1/q},
\qquad
\|\nabla b\|_{L^q(E,\eta)}=2\,\eta(\partial A_b)^{1/q}.
}
\tag{3}
\]

Consequently the best constant in the anchored inequality restricted to binary orientations,

\[
\|b-1\|_{L^q(V,\nu)}
\le C^{\rm bin}_{q,D}\,
\|\nabla b\|_{L^q(E,\eta)},
\tag{4}
\]

is exactly

\[
\boxed{
C^{\rm bin}_{q,D}
=h_D(\nu,\eta)^{-1/q},
\qquad
h_D(\nu,\eta)
:=
\inf_{\substack{\varnothing\ne A\subseteq V\setminus D\\\nu(A)>0}}
\frac{\eta(\partial A)}{\nu(A)},
}
\tag{5}
\]

with the usual convention that the constant is infinite if an admissible set has zero boundary weight. Thus for the sign-valued source class relevant to the ancestry matched controls, **uniform finite-`L^q` coefficient recovery is equivalent to a uniform anchored cut-exposure bound**. Connectivity is only the endpoint statement that no admissible cut has exactly zero boundary.

Applied to the full squarefree ancestry graph

\[
V_T=\{n\le T:\mu^2(n)=1\},
\qquad
E_T=\{(n,pn):n,pn\in V_T,\ p\text{ prime}\},
\tag{6}
\]

with uniform vertex and edge measures, this gives a stronger seed-compatible obstruction than FD-146. For **every fixed finite prescribed seed** `S`, there is one fixed infinite source agreeing with Möbius on `S` for which, for every finite `q`,

\[
\boxed{
\left(
\frac1{|E_T|}
\sum_{(n,pn)\in E_T}|a_{pn}+a_n|^q
\right)^{1/q}
\asymp_S
(\log T\,\log\log T)^{-1/q},
}
\tag{7}
\]

while

\[
\boxed{
\left(
\frac1{|V_T|}
\sum_{n\in V_T}|a_n-\mu(n)|^q
\right)^{1/q}
\longrightarrow2.
}
\tag{8}
\]

In particular every uniform anchored Poincare constant valid even just for binary Möbius orientations and a fixed finite seed must satisfy

\[
\boxed{
C^{\rm bin}_{q,S}(T)
\gg_S
(\log T\,\log\log T)^{1/q}.
}
\tag{9}
\]

The obstruction is no longer tied to a rank wall. A finite seed itself has only `Theta_S(T/log T)` outgoing ancestry edges, while the full ancestry graph has `Theta(T log log T)` edges. Hence the entire complement of the seed's divisor closure can carry the opposite orientation behind a cut of normalized mass `Theta_S(1/(log T log log T))`.

## 1. Binary orientations are exactly weighted cuts

For any admissible `b`, the left side of (3) vanishes off `A_b` and has magnitude `2` on `A_b`. Hence

\[
\|b-1\|_{L^q(V,\nu)}^q
=2^q\nu(A_b).
\tag{10}
\]

An edge has nonzero gradient precisely when its endpoints have opposite orientations, equivalently when it crosses the cut of `A_b`. Every such gradient has magnitude `2`, so

\[
\|\nabla b\|_{L^q(E,\eta)}^q
=2^q\eta(\partial A_b).
\tag{11}
\]

Conversely every `A\subseteq V\setminus D` is realized by the binary orientation equal to `-1` on `A` and `+1` elsewhere. Taking the supremum of the ratio of (10) and (11) therefore proves (5) exactly.

This is the precise graph-theoretic content behind the qualitative language of FD-145--FD-146. For `q=infinity`, with the support graph of the edge weights understood, every nonconstant binary orientation has both norms equal to `2` whenever its cut has a visible edge. Thus the best binary `L^infinity` constant is `1` exactly when every vertex of positive vertex weight is connected through visible edges to the anchored seed; if a component is disconnected, the constant is infinite. The finite-`q` problem is strictly stronger because it measures the **mass** of the cut rather than merely its existence.

## 2. The full squarefree ancestry graph has `T log log T` edges

Every squarefree child `m>1` has exactly `omega(m)` incoming ancestry edges, one for each prime divisor. Hence

\[
|E_T|
=
\sum_{m\le T}\mu^2(m)\omega(m).
\tag{12}
\]

Equivalently, summing first over the added prime,

\[
|E_T|
=
\sum_{p\le T}
\#\{n\le T/p:\mu^2(n)=1,\ (n,p)=1\}.
\tag{13}
\]

For `x>=1`, the elementary identity `mu^2(n)=sum_(d^2|n) mu(d)` gives uniformly in the prime `p`

\[
\#\{n\le x:\mu^2(n)=1,\ (n,p)=1\}
=
\frac1{\zeta(2)}\frac{p}{p+1}x
+O(\sqrt x).
\tag{14}
\]

Indeed, after inserting the square-divisor identity, the count of multiples coprime to `p` contributes `(1-1/p)x/d^2+O(1)` for `(d,p)=1`; the Euler factor removed at `p` changes `1/zeta(2)` by `(1-1/p^2)^{-1}`, producing `p/(p+1)`.

Substituting `x=T/p` into (13) yields

\[
|E_T|
=
\frac{T}{\zeta(2)}
\sum_{p\le T}\frac1{p+1}
+O\!\left(\sqrt T\sum_{p\le T}p^{-1/2}\right).
\tag{15}
\]

The error is `O(T)`, while the prime number theorem and partial summation give

\[
\sum_{p\le T}\frac1{p+1}
=
\log\log T+O(1).
\tag{16}
\]

Therefore

\[
\boxed{
|E_T|
=
\frac{T}{\zeta(2)}\log\log T+O(T).
}
\tag{17}
\]

This sharpens the merely linear lower bound on `|E_T|` used in FD-146 and is the extra factor responsible for (7)--(9).

## 3. Any fixed finite seed leaves only a prime-thin boundary

Let `S` be any fixed finite set of positive integers on which the synthetic source is required to agree with Möbius. Nonsquarefree seed points impose no extra condition because both the target and the construction below are zero there. Let `D` be the finite divisor closure inside the squarefree integers of

\[
\{1\}\cup\{s\in S:\mu^2(s)=1\}.
\tag{18}
\]

Thus `D` is finite, contains `1`, contains every squarefree seed point, and whenever `m\in D` every squarefree divisor of `m` also lies in `D`.

Define one fixed orientation on all squarefree integers by

\[
b_S(n)=
\begin{cases}
+1,&n\in D,\\
-1,&n\notin D,
\end{cases}
\qquad
 a_n=
\begin{cases}
\mu(n)b_S(n),&\mu^2(n)=1,\\
0,&\mu(n)=0.
\end{cases}
\tag{19}
\]

Then `a_n=mu(n)` on the whole prescribed seed. Because `D` is divisor-closed, an ancestry edge cannot enter `D` from its complement: if `pn\in D`, then `n|pn` forces `n\in D`. Hence every defect edge leaves `D`.

For a fixed `n\in D`, the outgoing crossing edges are obtained by primes `p` with `p\nmid n`, `np<=T`, and `np\notin D`. Only finitely many primes are excluded by the last two local conditions, so

\[
\#\{p:(n,np)\in\partial D\}
=
\pi(T/n)+O_D(1)
=
\frac{T}{n\log T}(1+o(1)).
\tag{20}
\]

Summing over the finite set `D`, and writing

\[
\kappa_D:=\sum_{n\in D}\frac1n>0,
\tag{21}
\]

we obtain the exact first-order boundary asymptotic

\[
\boxed{
B_D(T):=|\partial D\cap E_T|
=
\kappa_D\frac{T}{\log T}(1+o(1)).
}
\tag{22}
\]

Together with (17),

\[
\boxed{
\frac{B_D(T)}{|E_T|}
=
\zeta(2)\kappa_D
\frac{1+o(1)}{\log T\,\log\log T}.
}
\tag{23}
\]

This is the anchored cut exposure seen by the uniform edge measure.

## 4. The seed-complement source defeats every finite `L^q`

For a squarefree ancestry edge, as in FD-145,

\[
a_{pn}+a_n
=
\mu(n)\bigl(b_S(n)-b_S(pn)\bigr).
\tag{24}
\]

Thus the defect has magnitude `2` exactly on `partial D` and vanishes everywhere else. Equations (22)--(23) give, for every fixed `1<=q<infinity`,

\[
\begin{aligned}
\left(
\frac1{|E_T|}
\sum_{E_T}|a_{pn}+a_n|^q
\right)^{1/q}
&=
2\left(\frac{B_D(T)}{|E_T|}\right)^{1/q}\\
&=
2\bigl(\zeta(2)\kappa_D+o(1)\bigr)^{1/q}
(\log T\,\log\log T)^{-1/q},
\end{aligned}
\tag{25}
\]

which proves the stronger form of (7).

On the coefficient side, `D` is fixed while

\[
|V_T|\sim \frac{T}{\zeta(2)}.
\tag{26}
\]

Outside `D`, the source has `a_n=-mu(n)` at every squarefree point. Hence

\[
\left(
\frac1{|V_T|}
\sum_{n\in V_T}|a_n-\mu(n)|^q
\right)^{1/q}
=
2\left(1-\frac{|D|}{|V_T|}\right)^{1/q}
\longrightarrow2,
\tag{27}
\]

proving (8).

Applying the exact cut identity (5) with uniform weights and `A=V_T\setminus D` gives

\[
h_D(T)
\le
\frac{B_D(T)/|E_T|}{(|V_T|-|D|)/|V_T|}
=
\zeta(2)\kappa_D
\frac{1+o(1)}{\log T\,\log\log T}.
\tag{28}
\]

Therefore

\[
\boxed{
C^{\rm bin}_{q,D}(T)
\ge
\left(
\frac{\log T\,\log\log T}
{\zeta(2)\kappa_D}
\right)^{1/q}(1+o(1)),
}
\tag{29}
\]

which proves (9) with an explicit seed-dependent leading constant.

For the smallest anchor `D={1}`, the whole obstruction is carried by the prime fan out of `1`: `B_D(T)=pi(T)`. The full graph has `~T log log T/zeta(2)` edges, so the visible bridge from the absolute orientation anchor occupies only `~zeta(2)/(log T log log T)` of the normalized edge mass.

## 5. What changes relative to FD-145 and FD-146

FD-145 says that if the high-rank component is disconnected from the anchor, its orientation is completely free: the relevant cut has zero observed boundary. FD-146 restores every edge and shows with a fixed-rank wall that the boundary can still have vanishing normalized mass.

FD-147 identifies these as the zero-mass and small-mass versions of one exact object. For binary Möbius orientations, there is no additional analytic mystery in the coefficient-to-ancestry step: the best finite-`L^q` constant is exactly the reciprocal `q`-th root of the anchored cut ratio (5). In particular, checking only connectivity or a selected family of rank cuts cannot establish binary coercivity; one must control **all source-admissible anchored cuts under the actual observation weights**.

The finite-seed construction also strengthens the quantitative no-go. FD-146 made the source agree with Möbius on every squarefree integer of rank at most a fixed `R_0`, which is far more anchoring than an arbitrary prescribed finite seed requires. Keeping only the finite divisor closure of the actual seed shrinks the transition boundary to prime order and improves the forced divergence from the FD-146 bound to at least `(log T log log T)^(1/q)` for every fixed finite seed.

This does not contradict the `L^infinity` observation in FD-146. Every boundary defect in (24) still has full size `2`, so the sup norm sees it immediately. The distinction is exact: `L^infinity` asks whether a bridge exists; finite `L^q` asks how much normalized observation mass the bridge carries.

## 6. Prior-art and novelty boundary

The graph-theoretic relation between cut expansion, Poincare/spectral coercivity and Dirichlet boundary conditions is classical. Nearby general formulations include Matthias Keller and Delio Mugnolo, *General Cheeger inequalities for p-Laplacians on graphs*, Nonlinear Analysis **147** (2016), 80--95, DOI `10.1016/j.na.2016.07.011`, and Bobo Hua and Lili Wang, *Dirichlet p-Laplacian eigenvalues and Cheeger constants on symmetric graphs*, Advances in Mathematics **364** (2020), 106997, DOI `10.1016/j.aim.2020.106997`. No novelty is claimed for Cheeger theory or for testing a functional inequality on indicator/sign functions.

Those papers are prior-art boundaries rather than load-bearing inputs: (3)--(5) are immediate finite identities and are proved here directly. The arithmetic content specific to this line is the splice with the complete squarefree Möbius ancestry graph, especially the asymptotic edge count (17) and the fixed-seed divisor-closure cut (22)--(29). The only asymptotic inputs needed there are the squarefree counting law and the prime number theorem already anchored in `SOURCES.md`; no new external theorem is load-bearing.

## 7. Stress tests and limits

The construction is a single fixed infinite source, not a horizon-by-horizon choice. Enlarging the prescribed finite seed changes only the fixed finite divisor closure `D` and the constant `kappa_D`; it does not change the `1/(log T log log T)` boundary scale.

The result is deliberately restricted to local ancestry gradients and binary orientations. A source-independent weighting that gives every admissible macroscopic cut a uniformly positive boundary mass would defeat the argument. Equation (5) says exactly what must be proved for such a weighting; it does not claim that no such weighting exists.

Likewise, a genuinely nonlocal Farey/Fourier functional can bypass the cut model by coupling coefficients that are not adjacent in the prime-ancestry graph. FD-147 makes no no-go claim for that destination-side route. Nor does the exact binary constant in (5) identify the best Poincare constant over arbitrary real-valued `b`; classical Cheeger theory relates those larger function classes to isoperimetry, but equality with (5) is asserted only for `{-1,+1}` orientations.

As a finite regression check, direct enumeration of the full squarefree ancestry graph for `T=100,1000,10000` and the seed `{1,6,10}` verified that the number of nonzero defect edges equals the boundary obtained by summing the outgoing prime children of the squarefree divisor closure exactly at each tested horizon.

## 8. Falsifiable next test

A proposed source-native ancestry weighting `eta_T` should now be audited by its anchored Cheeger exposure before any finite-`L^q` coercivity claim is attempted. For the vertex weight `nu_T` induced by the target coefficient norm, compute or bound

\[
h_{D,T}
=
\inf_{\varnothing\ne A\subseteq V_T\setminus D}
\frac{\eta_T(\partial A)}{\nu_T(A)}.
\tag{30}
\]

If `h_{D,T}->0`, a binary source immediately gives a matched obstruction with coercivity constant at least `h_{D,T}^{-1/q}`. If `h_{D,T}` stays uniformly positive for every fixed seed, the entire binary cut obstruction of FD-145--FD-147 is defeated, and the independent information-budget obstruction of FD-144 becomes relevant again.

For the existing uniform normalization the test is already decided negatively by (28). The next genuinely different coefficient-side candidate must therefore derive nonuniform weights from the Farey/Franel destination itself and prove uniform anchored expansion under those weights, rather than adding more local edges to a graph that is already complete.

## Conclusion

For sign-valued Möbius orientations, quantitative anchor exposure is not merely a heuristic requirement: it is exactly an anchored cut constant. On the complete uniformly weighted squarefree ancestry graph, every fixed finite Möbius seed is separated from almost all coefficients by only a prime-thin boundary. Consequently one fixed seed-compatible source has

\[
\boxed{
\text{finite-}L^q\text{ ancestry defect}
\asymp_S
(\log T\,\log\log T)^{-1/q},
\qquad
\text{coefficient error}\to2,
}
\tag{31}
\]

and any corresponding binary coercivity constant diverges at least like `(log T log log T)^(1/q)`. The live local route is therefore no longer “connect the anchor” or even “expose fixed-rank walls”; it is to prove a **uniform anchored expansion law for the actual Farey-induced weights**.