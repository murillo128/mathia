# PC-143 — gap-two top band locks on average but not in operator norm

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY` + `CLUE-RESOLUTION`. PC-142 proved that, for every level divisible by `6`, the primitive-shell inverse-square chord Laplacian has exactly `E_N` eigenvalues at or above the gap-two threshold and a uniform `N^2`-scale cliff below them. `CLUE-gap2-tail-eigenspace-locking` left open whether the corresponding top eigenspace itself approaches the exact gap-two matching space.

Along the primorials the answer splits sharply by topology. The normalized Frobenius overlap **does** converge to one: asymptotically almost every direction in the isolated top band is carried by the local gap-two matching. But the worst principal angle **does not** converge to zero. A CRT-constructible exceptional local constellation leaves an order-`N^2` off-diagonal coupling for every primorial from `30` onward. Thus the top band becomes matching-like in density, while retaining sparse non-matching directions at operator-norm scale.

This resolves the accepted clue without producing an RH mechanism. It substantially classicalizes the average organization of the PC-139/PC-142 macroscopic tail, but also proves that uniform eigenspace locking is false.

## 1. Setup and the exact isolated band

Let

\[
N_x:=\prod_{p\le x}p,
\qquad
U_x:=(\mathbb Z/N_x\mathbb Z)^\times,
\]

with `x>=5`, and let `L_x=L_{N_x}^{int}` be the primitive-shell inverse-square chord Laplacian

\[
\langle f,L_xf\rangle
=
\sum_{\{a,b\}\subset U_x}
\frac{|f(a)-f(b)|^2}{4\sin^2(\pi(a-b)/N_x)}.
\tag{1}
\]

Write

\[
w_h(N):=\frac1{4\sin^2(\pi h/N)},
\qquad
\beta_N:=2w_2(N).
\tag{2}
\]

The gap-two primitive edges form the matching `mathcal E_x` of PC-139, with

\[
E_x=|\mathcal E_x|=\prod_{3\le p\le x}(p-2).
\tag{3}
\]

For each edge `e={a,a+2}` put

\[
u_e:=\frac{e_a-e_{a+2}}{\sqrt2},
\qquad
V_x:=\operatorname{span}\{u_e:e\in\mathcal E_x\},
\]

and let `P_x` be the orthogonal projection onto `V_x`. The selected-edge Laplacian is exactly

\[
A_x=\beta_{N_x}P_x.
\tag{4}
\]

Write

\[
L_x=A_x+R_x,
\qquad R_x\succeq0.
\tag{5}
\]

PC-142 proves an explicit bound

\[
\|R_x\|\le\rho_{N_x}<\beta_{N_x},
\tag{6}
\]

and, with

\[
c_6=\frac1{4\pi^2}-\frac5{216}>0,
\]

\[
\beta_{N_x}-\rho_{N_x}>c_6N_x^2.
\tag{7}
\]

It also proves that the spectral projection `Q_x` of `L_x` onto eigenvalues at least `beta_{N_x}` has exactly

\[
\operatorname{rank}Q_x=E_x=\operatorname{rank}P_x.
\tag{8}
\]

Hence the principal-angle question is well posed with no ambiguity about the target band.

## 2. The matching vectors see asymptotically negligible remainder energy on average

Let `M_x` be the set of vertices covered by the gap-two matching, so `|M_x|=2E_x`. Since the matching edge itself has been removed from `R_x`, for a normalized edge vector `u_e` one has

\[
\langle u_e,R_xu_e\rangle
=\frac12\bigl(d_R(a)+d_R(a+2)\bigr),
\tag{9}
\]

where `d_R(v)` is the weighted degree of `v` in the remainder graph. Summing over the disjoint matching gives

\[
\boxed{
\operatorname{tr}(P_xR_xP_x)
=\frac12\sum_{a\in M_x}d_R(a).
}
\tag{10}
\]

For a signed fixed offset `h`, let `r_x(h)` be the fraction of matched vertices `a` for which `a+h` is again primitive, with the unique gap-two partner contribution deleted when `h=+/-2`. Then

\[
\frac{\operatorname{tr}(P_xR_xP_x)}{E_xN_x^2}
=
\sum_{h\ne0}
\frac{w_h(N_x)}{N_x^2}\,r_x(h),
\tag{11}
\]

where offsets are represented symmetrically modulo `N_x`.

For every fixed `h` other than the deleted partner, CRT forces

\[
\boxed{r_x(h)\longrightarrow0.}
\tag{12}
\]

Indeed, one orientation of a matching edge asks simultaneously that the three translates `a`, `a+2`, and `a+h` avoid zero modulo every prime `p<=x`. For every sufficiently large prime relative to fixed `h`, those are three distinct residue classes, so the conditional local factor relative to the two-point matching is

\[
\frac{p-3}{p-2}=1-\frac1{p-2}.
\tag{13}
\]

The product of these factors tends to zero because the prime harmonic series diverges. The opposite orientation uses the translate pattern `{-2,0,h}` and has the same conclusion. At the unused `+/-2` direction, divisibility by `3` makes the count identically zero.

The inverse-square kernel makes this pointwise sieve decay summable uniformly. If `d_N(h)=min(h,N-h)`, then

\[
\sin(\pi h/N)\ge\frac{2d_N(h)}N
\]

gives

\[
\boxed{
0\le\frac{w_h(N)}{N^2}
\le\frac1{16d_N(h)^2}.
}
\tag{14}
\]

The right-hand side is summable over signed offsets, independently of `N`. Splitting (11) at any fixed distance `H`, applying (12) to the finite inner part, and then sending `H` to infinity in the uniform `1/h^2` tail proves

\[
\boxed{
\frac{\operatorname{tr}(P_xR_xP_x)}{E_xN_x^2}
\longrightarrow0.
}
\tag{15}
\]

Thus a typical matching direction sees only `o(N_x^2)` remainder energy even though `R_x` itself has order-`N_x^2` norm.

## 3. Frobenius/average eigenspace locking follows from the PC-142 cliff

Let `Q_x^perp=I-Q_x` and let

\[
L_{x,-}:=Q_x^\perp L_xQ_x^\perp.
\]

Its spectrum lies below `rho_{N_x}` by PC-142. Set

\[
X_x:=Q_x^\perp P_x.
\]

Using `L_xP_x=beta_{N_x}P_x+R_xP_x` and invariance of `Q_x^perp` gives the exact Sylvester relation

\[
(\beta_{N_x}I-L_{x,-})X_x
=-Q_x^\perp R_xP_x.
\tag{16}
\]

Therefore

\[
\|X_x\|_F
\le
\frac{\|R_xP_x\|_F}{\beta_{N_x}-\rho_{N_x}}.
\tag{17}
\]

Since `R_x` is positive semidefinite,

\[
\|R_xP_x\|_F^2
=\operatorname{tr}(P_xR_x^2P_x)
\le
\|R_x\|\operatorname{tr}(P_xR_xP_x)
\le
\rho_{N_x}\operatorname{tr}(P_xR_xP_x).
\tag{18}
\]

Both `rho_{N_x}` and `beta_{N_x}` are `Theta(N_x^2)`, while (7) gives a fixed positive `N_x^2` gap. Combining (15)--(18),

\[
\boxed{
\frac1{E_x}\|Q_x^\perp P_x\|_F^2
\longrightarrow0.
}
\tag{19}
\]

For equal-rank projections,

\[
\|Q_x^\perp P_x\|_F^2
=E_x-\operatorname{tr}(P_xQ_x).
\]

Hence

\[
\boxed{
\frac1{E_x}\operatorname{tr}(P_xQ_x)
\longrightarrow1.
}
\tag{20}
\]

Equation (20) proves the normalized-Frobenius/average half of the accepted clue. The numerical overlaps `0.996344`, `0.996299`, and `0.996450` at `N=30,210,2310` are therefore finite precursors of a genuine asymptotic statement, although the proof gives no useful finite convergence rate.

## 4. Uniform locking is impossible: an exceptional CRT constellation survives at every scale

The average statement does not upgrade to operator norm. For every primorial `N_x` with `x>=5`, choose by CRT a residue `a` satisfying

\[
a\equiv5\pmod6,
\qquad
a\equiv2\pmod p\quad(5\le p\le x).
\tag{21}
\]

Then `a`, `a+2`, and `c:=a+6` are all primitive. The pair `{a,a+2}` is a gap-two matching edge. But `c` is **unmatched**: `c-2=a+4` is divisible by `3`, while `c+2=a+8` is divisible by `5`.

Take

\[
u=\frac{e_a-e_{a+2}}{\sqrt2}\in V_x.
\]

Because `e_c` lies in `V_x^perp`, the `c` coordinate of the off-diagonal block is untouched by projection. The two edges from `c` to the support of `u` have gaps `6` and `4`, so

\[
\left|\langle e_c,(I-P_x)L_xP_xu\rangle\right|
=
\frac{w_4(N_x)-w_6(N_x)}{\sqrt2}.
\tag{22}
\]

Consequently, with

\[
B_x:=(I-P_x)L_xP_x,
\]

\[
\boxed{
\|B_x\|
\ge
\frac{w_4(N_x)-w_6(N_x)}{\sqrt2}.
}
\tag{23}
\]

The full regular-polygon inverse-square Laplacian has eigenvalues `k(N-k)/2`, so its norm is `N^2/8` at even `N`. The primitive internal graph is an edge subgraph, hence

\[
\|L_x\|\le\frac{N_x^2}{8}.
\tag{24}
\]

Since `Q_x` is a spectral projection, `[L_x,Q_x]=0`. Therefore

\[
B_x=(I-P_x)[L_x,P_x]P_x
=(I-P_x)[L_x,P_x-Q_x]P_x,
\]

and

\[
\|B_x\|
\le2\|L_x\|\,\|P_x-Q_x\|.
\tag{25}
\]

Using (23)--(25),

\[
\|P_x-Q_x\|
\ge
\frac{4\bigl(w_4(N_x)-w_6(N_x)\bigr)}{\sqrt2\,N_x^2}.
\tag{26}
\]

Since

\[
\frac{w_k(N)}{N^2}\longrightarrow\frac1{4\pi^2k^2}
\]

for fixed `k`, we obtain the explicit obstruction

\[
\boxed{
\liminf_{x\to\infty}\|P_x-Q_x\|
\ge
\frac5{144\sqrt2\,\pi^2}
=0.00248767\ldots>0.
}
\tag{27}
\]

For equal-rank orthogonal projections this norm is the sine of the worst principal angle. Thus the worst principal angle cannot converge to zero, even though the average squared sine does.

## 5. Interpretation: density-one localization with sparse operator-scale defects

Equations (20) and (27) give a clean two-scale answer:

\[
\boxed{
\frac1{E_x}\operatorname{tr}(P_xQ_x)\to1,
\qquad
\liminf\|P_x-Q_x\|>0.
}
\tag{28}
\]

The mechanism is elementary but structurally useful. Conditioning on a gap-two primitive pair, any **fixed additional translate** is removed with probability tending to one as more prime sieves are imposed; the summable `1/h^2` chord kernel then forces average decoupling. Yet CRT always permits exceptional finite constellations, and one such three-vertex pattern already carries an order-`N_x^2` coupling. A vanishing fraction of exceptional matching directions is therefore enough to prevent operator-norm convergence while disappearing from normalized Frobenius overlap.

This distinction matters for the Prime-Circle program. The dominant top-band eigenspace is asymptotically local in an average sense, so its bulk organization cannot be treated as unexplained global arithmetic structure. Any surviving information in that band must be sought in sparse exceptional directions, finer internal spacings, their arithmetic placement, or cross-level transport rather than in the density-one projector geometry.

## 6. Prior-art and novelty audit

The ingredients are classical. Fixed finite patterns in reduced residue systems are sieve/CRT objects; nearby systematic literature includes H. L. Montgomery and R. C. Vaughan, **On the distribution of reduced residues**, *Annals of Mathematics* 123 (1986), 311–333, DOI `10.2307/1971274`, and Farzad Aryan, **The distribution of k-tuples of reduced residues**, *Mathematika* 61 (2015), 72–88, DOI `10.1112/S0025579314000151`. The subspace-separation step is in the classical Davis--Kahan/Sylvester perturbation framework; see Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7 (1970), 1–46, DOI `10.1137/0707001`.

Directed searches across reduced-residue inverse-square Laplacians, cosecant-square primitive-shell spectra, matching-subspace principal angles, and reduced-residue spectral projectors did not expose the specific dichotomy (28). That absence is not evidence of historical priority. No theorem-level novelty is claimed for CRT pattern thinning, dominated convergence, or subspace perturbation separately; the durable contribution is the exact boundary they impose on the already-canonical PC-139/PC-142 Prime-Circle band.

There is no new RH criterion here. The result introduces no spectral parameter, zeta divisor, gamma factor, functional equation, or critical-line involution. Rather, it narrows where a nonclassical mechanism could still reside: not in the average top-band eigenspace, but potentially in its sparse exceptional directions or their dynamics across levels.

## 7. Falsification surface and consequences

1. The trace identity (10) can be checked directly from the matching basis and the remainder graph.
2. For every fixed offset not equal to the deleted partner, exact CRT counts of the relevant three-point pattern divided by the two-point matching count must tend to zero; failure for one fixed offset falsifies (12).
3. The uniform chord bound (14) must dominate the normalized weights for every `N` and offset, making the dominated-convergence step in (15) independent of unproved prime-pattern conjectures.
4. Equation (20) depends on the exact PC-142 band count and `N^2` gap. A revision of that theorem would require re-auditing the projector argument.
5. The CRT residue (21) must exist for every primorial from `30` onward, with `a,a+2,a+6` primitive and `a+6` unmatched. Direct finite construction at any such level checks the operator-norm obstruction.
6. The result deliberately does not classify the exceptional directions, their count beyond what elementary pattern products imply, or their transport under `N_x -> N_{x'}`. Those remain possible carriers of information not seen by normalized Frobenius overlap.

The accepted `CLUE-gap2-tail-eigenspace-locking` is therefore resolved with a split verdict: **supported in normalized Frobenius/average geometry, refuted in worst-principal-angle/operator-norm geometry**.