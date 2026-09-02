# PC-142 — gap-two matching has an exact macroscopic spectral cliff

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY`. PC-139 proved that the primitive-shell inverse-square chord Laplacian on a primorial has at least
\[
E_x=\prod_{3\le p\le x}(p-2)
\]
eigenvalues above the gap-two threshold
\[
\beta_N=\frac{1}{2\sin^2(2\pi/N)},
\]
while `CLUE-gap2-tail-eigenspace-locking` found numerically that the count is exactly `E_x` at `N=30,210,2310` and that the corresponding eigenspace is almost the gap-two matching space. The spectral-count half of that clue admits an exact proof, and in fact does not require squarefreeness.

For every `N` divisible by `6`, remove the disjoint primitive gap-two edges from the primitive-shell Laplacian. The remaining operator is dominated by an explicit period-six ambient graph on all residues coprime to `6`. Its weighted degree can be evaluated by the classical cosecant-square identities, giving an operator-norm bound strictly below `beta_N`. Consequently the gap-two matching contributes **exactly all** eigenvalues at or above `beta_N`, and the `E_N`th and `(E_N+1)`st eigenvalues are separated by a uniform positive multiple of `N^2`.

This validates the observed spectral cliff exactly. It does **not** prove asymptotic eigenspace locking: the remaining principal-angle question is finer than the coarse operator-norm domination used here.

## 1. Primitive gap-two edges give an exact rank-`E_N` projector

Let
\[
U(N):=(\mathbb Z/N\mathbb Z)^\times
\]
and let `L_N^int` denote the primitive-shell inverse-square chord Laplacian,
\[
\langle f,L_N^{\rm int}f\rangle
=
\sum_{\{a,b\}\subset U(N)}
\frac{|f(a)-f(b)|^2}
     {4\sin^2(\pi(a-b)/N)}.
\tag{1}
\]

Assume `6|N`. Define
\[
\mathcal E_N
:=
\bigl\{\{a,a+2\}:a,a+2\in U(N)\bigr\}.
\tag{2}
\]
As in PC-139, divisibility by `3` makes this an exact matching. If `a,a+2` are units, then modulo `3` they are the two nonzero classes, so neither `a-2` nor `a+4` can be a unit. Thus no primitive vertex belongs to two edges of `mathcal E_N`.

The number of edges is the elementary CRT count
\[
\boxed{
E_N
=
\frac N2
\prod_{\substack{p\mid N\\p>2}}
\left(1-\frac2p\right).
}
\tag{3}
\]
Indeed, modulo `2^e` there are `2^{e-1}` admissible starts, while modulo each odd `p^e` there are `p^{e-1}(p-2)` starts. For the primorial
\[
N_x=\prod_{p\le x}p
\]
this reduces to the PC-139 formula
\[
E_{N_x}=\prod_{3\le p\le x}(p-2).
\tag{4}
\]

Every edge in `mathcal E_N` has weight
\[
w_2(N)=\frac{1}{4\sin^2(2\pi/N)}
\]
and its two-vertex Laplacian has the nonzero eigenvalue
\[
\beta_N=2w_2(N)=\frac{1}{2\sin^2(2\pi/N)}.
\tag{5}
\]

Let
\[
V_N
:=
\operatorname{span}
\{e_a-e_{a+2}:\{a,a+2\}\in\mathcal E_N\}.
\tag{6}
\]
Because the edges are disjoint, their difference vectors are mutually orthogonal. Hence the Laplacian formed only from the gap-two edges is exactly
\[
\boxed{
A_N=\beta_N P_{V_N},
\qquad
\operatorname{rank}A_N=E_N.
}
\tag{7}
\]

Write
\[
L_N^{\rm int}=A_N+R_N,
\qquad
R_N\succeq0.
\tag{8}
\]
PC-139 used only positivity of `R_N` to obtain `lambda_{E_N}(L_N^int)>=beta_N`. The missing step is an upper bound on the first eigenvalue below that matching band.

## 2. A period-six ambient graph dominates the entire remainder

Put
\[
N=6M
\]
and consider the larger vertex set
\[
W_6(N)
:=
\{a\bmod N:(a,6)=1\}.
\tag{9}
\]
It consists of the two residue classes `1,5 mod 6`, each containing `M` vertices. Form the same inverse-square chord graph on `W_6(N)`, but delete **all** its gap-two edges. Call the resulting weighted Laplacian `\mathcal R_{6,N}`.

The primitive remainder `R_N` is the induced primitive part of this graph with further vertices and incident edges removed. More precisely, if `f` on `U(N)` is extended by zero to `W_6(N)`, then every energy term of `R_N` occurs in `\mathcal R_{6,N}` and the latter has only additional nonnegative terms. Therefore
\[
\boxed{
\langle f,R_Nf\rangle
\le
\langle \widetilde f,\mathcal R_{6,N}\widetilde f\rangle,
\qquad
\|R_N\|\le\|\mathcal R_{6,N}\|.
}
\tag{10}
\]

The ambient graph is weighted regular. Its degree is explicit. Within one residue class modulo `6`, the differences are `6r`, `1<=r<M`, so
\[
\sum_{r=1}^{M-1}
\frac{1}{4\sin^2(\pi r/M)}
=
\frac{M^2-1}{12}.
\tag{11}
\]
Between the two residue classes, a shifted cosecant sum gives
\[
\sum_{r=0}^{M-1}
\frac{1}{4\sin^2(\pi(r+2/3)/M)}
=
\frac{M^2}{3}.
\tag{12}
\]
Equation (12) is the standard identity
\[
\sum_{r=0}^{M-1}\csc^2\!\left(\frac{\pi(r+\alpha)}M\right)
=
M^2\csc^2(\pi\alpha)
\]
at `alpha=2/3`.

Each vertex has exactly one deleted gap-two neighbor, of weight `w_2(N)`. Hence the weighted degree of `\mathcal R_{6,N}` is
\[
\boxed{
d_6(N)
=
\frac{5M^2-1}{12}-w_2(N).
}
\tag{13}
\]

For every positive weighted graph Laplacian,
\[
\lambda_{\max}\le2\,d_{\max}.
\]
Therefore
\[
\boxed{
\|R_N\|
\le
\rho_N
:=
2d_6(N)
=
\frac{5M^2-1}{6}-\beta_N.
}
\tag{14}
\]

The bound deliberately forgets every prime divisor beyond `2` and `3`. That loss of arithmetic information is useful here: if even this much larger six-wheel remainder lies below the gap-two band, then so does the true primitive remainder.

## 3. The six-wheel remainder lies uniformly below the matching band

Since
\[
\frac{2\pi}{N}=\frac{\pi}{3M}
\]
and `sin y<y` for `y>0`,
\[
\boxed{
\beta_N
=
\frac{1}{2\sin^2(\pi/(3M))}
>
\frac{9M^2}{2\pi^2}.
}
\tag{15}
\]

The elementary inequality
\[
54>5\pi^2
\]
implies
\[
\frac{5M^2-1}{12}
<
\frac{9M^2}{2\pi^2}
<
\beta_N.
\tag{16}
\]
Using (14), this is exactly
\[
\boxed{
\rho_N<\beta_N.
}
\tag{17}
\]

More is available: the separation is uniformly macroscopic. From (14)--(15),
\[
\begin{aligned}
\beta_N-\rho_N
&=
2\beta_N-\frac{5M^2-1}{6}\\
&>
M^2\left(\frac9{\pi^2}-\frac56\right)+\frac16\\
&=
N^2\left(\frac1{4\pi^2}-\frac5{216}\right)+\frac16.
\end{aligned}
\tag{18}
\]
Thus with
\[
\boxed{
c_6
:=
\frac1{4\pi^2}-\frac5{216}
=
0.0021821477\ldots>0,
}
\tag{19}
\]
one has
\[
\boxed{
\beta_N-\rho_N>c_6N^2.
}
\tag{20}
\]

This is the key strengthening over the finite numerical observation. The cliff does not merely survive along the tested primorials: a positive `N^2`-scale lower bound follows already from the universal local obstruction modulo `6`.

## 4. Exactly `E_N` eigenvalues lie at or above `beta_N`

Order the eigenvalues of `L_N^int` decreasingly,
\[
\lambda_1\ge\lambda_2\ge\cdots.
\]

Because `R_N` is positive semidefinite and `A_N` has `E_N` eigenvalues equal to `beta_N`,
\[
\lambda_{E_N}(L_N^{\rm int})
\ge
\beta_N.
\tag{21}
\]

For the next eigenvalue, Weyl's inequality and (7), (14) give
\[
\lambda_{E_N+1}(L_N^{\rm int})
\le
\lambda_{E_N+1}(A_N)+\|R_N\|
=
\rho_N
<
\beta_N.
\tag{22}
\]

Therefore
\[
\boxed{
\#\{j:\lambda_j(L_N^{\rm int})\ge\beta_N\}=E_N
\qquad(6\mid N).
}
\tag{23}
\]

The spectral gap itself satisfies
\[
\boxed{
\lambda_{E_N}(L_N^{\rm int})
-
\lambda_{E_N+1}(L_N^{\rm int})
>
c_6N^2.
}
\tag{24}
\]

For primorials, (4) turns (23) into
\[
\boxed{
\#\{j:\lambda_j(L_{N_x}^{\rm int})\ge\beta_{N_x}\}
=
\prod_{3\le p\le x}(p-2).
}
\tag{25}
\]

Thus the `N=30,210,2310` spectral counts in `CLUE-gap2-tail-eigenspace-locking` were not a finite coincidence. The proposed `N=30030` computation is unnecessary as a falsifier of the **count** or the existence of a macroscopic cliff; both are now exact for every level divisible by `6`.

## 5. What this resolves — and what it does not

The result resolves the spectral-separation half of the clue. The gap-two CRT matching is not merely a convenient min-max witness for some high modes: its dimension is exactly the number of primitive-shell eigenvalues above its own natural edge threshold. Moreover, that band is isolated from the rest by a uniform `N^2`-scale gap.

It does **not** follow that the corresponding invariant subspace converges to `V_N`. The proof controls `R_N` by the norm of a much larger period-six graph and is intentionally insensitive to the off-diagonal block
\[
P_{V_N^\perp}R_NP_{V_N}.
\tag{26}
\]
A Davis--Kahan type estimate based only on the coarse norm bound (14) is therefore not strong enough to recover the observed squared principal cosines near `0.99`, let alone prove convergence to `1`.

The remaining question is now cleaner. Since the spectral band is rigorously isolated, one can study the spectral projector `P_N^top` onto the `E_N` eigenvalues in (23) without ambiguity. The relevant quantities are
\[
\frac1{E_N}\operatorname{tr}(P_{V_N}P_N^{\rm top})
\]
for average/Frobenius locking and
\[
\|P_{V_N}-P_N^{\rm top}\|
\]
for the worst principal angle. These need not have the same asymptotic behavior. Any surviving nonlocal arithmetic information must enter through the organization of this isolated band, not through its cardinality or its separation scale.

## 6. Prior-art and RH audit

The ingredients used for the proof are classical. The `csc^2` identities and full regular-polygon inverse-square matrices belong to the Calogero--Perelomov trigonometric framework already anchored in `research/prime_circle/SOURCES.md`; the bound `lambda_max(L)<=2d_max`, Weyl monotonicity, min-max, and Davis--Kahan subspace perturbation are standard spectral theory.

A directed graph-theory audit also checked the nearby unitary-Cayley literature. Klotz and Sander, **Some Properties of Unitary Cayley Graphs**, *Electronic Journal of Combinatorics* 14 (2007), R45, DOI `10.37236/963`, and subsequent unitary-Cayley spectral work use **all** residues as vertices and connect `a,b` when `a-b` is a unit. That is structurally different from the present object, whose vertices themselves are reduced residues and whose complete pair interaction is weighted by inverse squared chord distance. Searches across reduced-residue Laplacians, cosecant-square spectra, and unitary-Cayley graphs did not expose the exact period-six domination (10)--(24). This absence is not evidence of historical priority.

There is also no new RH criterion here. PC-139 already showed that the primorial count `E_x` is
\[
2C_{2,x}\left(\frac{\varphi(N_x)}{N_x}\right)^2N_x
\]
and therefore carries the classical Hardy--Littlewood local factor times the same Mertens/Nicolas scale classicalized further in PC-137/PC-140. PC-141 independently kills fixed Fourier edge windows. The present theorem strengthens the **spectral localization boundary**: all eigenvalues above the natural shortest-primitive-chord threshold have exactly the classical CRT count, so new information can only lie in their eigenspace geometry, internal spacing below/within the band, or cross-level transport.

No functional equation, spectral parameter, gamma factor, critical-line involution, or zeta-zero divisor is produced by the cliff itself.

## 7. Falsification surface

The theorem has direct finite controls.

1. For every `N` divisible by `6`, CRT enumeration must give (3), and the gap-two primitive edges must be vertex-disjoint.
2. The two period-six degree sums must equal (11) and (12), so deleting the unique gap-two neighbor must give (13).
3. Direct diagonalization must show exactly `E_N` eigenvalues at or above `beta_N`. In particular the counts are `3,15,135` at `N=30,210,2310`.
4. The `(E_N+1)`st eigenvalue must obey the explicit upper bound `rho_N` in (14), while the `E_N`th must be at least `beta_N`.
5. The band gap must satisfy (24). Failure at any single level divisible by `6` would falsify the domination or eigenvalue argument.
6. No claim is made that the top spectral projector converges to `P_{V_N}`. The existing near-locking numerics remain evidence for a strictly finer question, now isolated from uncertainty about the eigenvalue count.
