# XF-120 — full q-scale Xi prefix admits collision-saturated exact realizations

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC` + `COLLISION-SATURATED-REALIZATION` + `DECISIVE-STATIC-NEGATIVE` + `MATCHED-CONTROL` + `COLLISION-SAFE`. XF-119 closes the full q-scale static source gate: if `c_m=\widehat\mu_m` are the XF-118 normalized Xi moments through degree `K`, then the prescribed degree `N=2q^2` admits an exact equal-weight unit-circle realization. A remaining possibility was that this stronger realization theorem might also force the admissible real-divisor fiber away from the collision boundary. It does not.

The Toeplitz near-isometry of XF-118 is strong enough to **reserve almost the entire Xi node budget for an invisible collision crystal**. More precisely, write

\[
\varepsilon_K:=\|T_K(c)-I\|_{\rm op}=o(1),
\qquad
\frac KN\to0.
\tag{1}
\]

There is a sequence `n=o(N)` with `n/K->infinity` such that the same raw prefix

\[
P_m=Nc_m,
\qquad 1\le m\le K,
\tag{2}
\]

is realized by a degree-`N` unit-circle polynomial having exactly

\[
R=\frac{N-n}{2}
\tag{3}
\]

distinct prescribed simple double collisions at the realization slice. Hence

\[
\boxed{
\frac{2R}{N}=1-o(1),
}
\tag{4}
\]

so **all but `o(N)` roots can participate in simultaneous double collisions while the complete full-q-scale Xi moment prefix remains exact**. The exact periodic backward-heat trajectory through that slice has finite periodic Newman threshold equal to the slice itself.

Thus XF-119 removes static source infeasibility, but it does not create any static transition margin. At the current natural q-scale, the actual Xi source prefix is compatible not merely with some real-divisor realization, but with realizations lying asymptotically as deep as possible on the collision boundary. Any upper-bound mechanism must therefore use heat-time coherence, information beyond the admitted prefix, or another Xi-specific cross-scale constraint; a single-slice q-scale moment theorem cannot separate the source from transition.

## 1. Near-isometry survives after reserving almost all node slots

Keep the XF-118/XF-119 scaling

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a=N\Delta\asymp q^{1/2},
\tag{5}
\]

\[
L=\log a+c,
\qquad
K=\left\lfloor\frac L\Delta\right\rfloor
\asymp a^3\log a,
\qquad
N\asymp a^4,
\tag{6}
\]

so `K/N->0`. Let

\[
E_K:=T_K(c)-I,
\qquad
\|E_K\|_{\rm op}=\varepsilon_K=o(1).
\tag{7}
\]

The first observation is a reserved-budget version of the XF-119 realization bridge. Suppose `n<=N` is a node count and define a new normalized target by

\[
d_0:=1,
\qquad
d_m:=\frac Nn c_m,
\qquad 1\le |m|\le K.
\tag{8}
\]

Because the diagonal of `E_K` is zero,

\[
\boxed{
T_K(d)-I
=
\frac Nn\bigl(T_K(c)-I\bigr),
}
\tag{9}
\]

and hence

\[
\boxed{
\|T_K(d)-I\|_{\rm op}
=
\frac Nn\varepsilon_K.
}
\tag{10}
\]

Therefore, whenever

\[
\frac{N\varepsilon_K}{n}\to0,
\qquad
\frac nK\to\infty,
\tag{11}
\]

the complete XF-119 Poisson-deconvolution argument applies to `d` with node count `n`: backward `1/K` Poisson inflation preserves Toeplitz near-isometry, the representing measure is `1/K`-regular, forward Poisson smoothing gives a uniformly positive and bounded density with the moments `d_m` exactly restored, and Gilboa--Peled gives an equal-weight quadrature for every sufficiently large prescribed count `n>=CK`.

Consequently there are unit-circle nodes `\nu_1,\ldots,\nu_n` satisfying

\[
\boxed{
\sum_{j=1}^n \nu_j^m
=
n d_m
=
N c_m,
\qquad 1\le m\le K,
}
\tag{12}
\]

up to the harmless reflection convention already noted in XF-119. Thus a target originally normalized to `N` nodes may be carried by far fewer nodes, provided the scaling of the off-diagonal moments still leaves the finite Toeplitz section asymptotically equal to identity.

The hypotheses `(11)` allow `n/N` to vanish. For example put

\[
\theta_K
:=
\sqrt{\varepsilon_K}
+
\sqrt{\frac KN},
\tag{13}
\]

and choose an even integer `n` with

\[
\frac nN=\theta_K+o(\theta_K).
\tag{14}
\]

The rounding is harmless because `\theta_KN>=\sqrt{KN}->infinity`. Moreover

\[
\frac nN\to0,
\tag{15}
\]

while

\[
\frac{N\varepsilon_K}{n}
\le
\frac{\varepsilon_K}{\theta_K+o(\theta_K)}
=o(1)
\tag{16}
\]

and

\[
\frac nK
\ge
(1+o(1))
\frac{\sqrt{K/N}}{K/N}
=
(1+o(1))\sqrt{\frac NK}
\to\infty.
\tag{17}
\]

Thus `(11)` holds with only `o(N)` compensator nodes. No rate for the XF-118 convergence `\varepsilon_K->0` is required.

A simpler fixed-fraction form is also useful. For every fixed `0<\rho<1`, take `n=(1-\rho)N+O(1)`. Then `(10)` is still `o(1)` and `n/K->infinity`, so a fraction `\rho+o(1)` of the degree can be reserved with no diagonal argument. Equation `(13)` merely pushes this fixed-fraction freedom to the sharp asymptotic conclusion `(4)`.

## 2. The reserved degree can be filled by an exactly invisible collision crystal

Choose `n` as above with the same parity as the even integer `N`, and set

\[
R:=\frac{N-n}{2}.
\tag{18}
\]

Since `n/N->0` and `K/N->0`,

\[
R\sim\frac N2,
\qquad
R>K
\tag{19}
\]

for all sufficiently large scales. Let `A(w)` be the degree-`n` unit-circle polynomial whose roots are the quadrature nodes from `(12)`. For a phase `\phi`, introduce exactly the collision block used in XF-099/XF-101,

\[
\boxed{
C_\phi(w):=(w^R-e^{i\phi})^2.
}
\tag{20}
\]

Its `R` distinct roots are the solutions of `w^R=e^{i\phi}`, each with multiplicity exactly two. Its raw power sums are

\[
P_m^C
=
2e^{im\phi/R}
\sum_{r=0}^{R-1}e^{2\pi i mr/R},
\tag{21}
\]

so

\[
\boxed{
P_m^C=0,
\qquad 1\le m<R.
}
\tag{22}
\]

Because `R>K`, the entire collision block is exactly invisible to the complete XF-118 prefix.

There are only finitely many phases `\phi` for which a root of `C_\phi` is also a root of `A`. Choose any other phase and define

\[
\boxed{
F(w):=A(w)C_\phi(w).
}
\tag{23}
\]

Then `F` has degree

\[
\deg F=n+2R=N,
\tag{24}
\]

all of its roots lie on the unit circle, and every one of the `R` crystal locations is an exact simple double root of the total polynomial. Additivity of raw power sums under unions of root multisets, together with `(12)` and `(22)`, gives

\[
\boxed{
P_m^F=Nc_m,
\qquad 1\le m\le K.
}
\tag{25}
\]

Thus `F` is an **exact degree-`N`, equal-weight, real-divisor realization of the full natural q-scale Xi source prefix**, just as in XF-119, but now

\[
N-n=2R=N(1-o(1))
\tag{26}
\]

of its root slots belong to prescribed simultaneous double collisions.

This is materially stronger than the XF-099 collision crystal. XF-099 makes every low power sum vanish and therefore is only a generic destination falsifier; it does not match the actual Xi source prefix. Here the nonzero source-specific prefix from XF-118 is restored **exactly** by the `o(N)` compensator sector, while the remaining `1-o(1)` fraction of the degree is free to sit in the same collision-invisible symmetry block.

## 3. The matched carrier lies exactly on a periodic Newman transition slice

Let `F_t` be the exact normalized periodic backward-heat trajectory through `(23)` at time `t=0`, using the convention of XF-067/XF-087/XF-099/XF-101. Since every root of `F_0` lies on the unit circle, the Pólya--Benz/Kabluchko real-zero-preserver input already used in XF-098/XF-101 gives

\[
F_t\text{ real-rooted in the periodic coordinate for every }t\ge0.
\tag{27}
\]

At each crystal site the root multiplicity is exactly two because the phase was chosen away from the roots of `A`. The collision-safe local law of XF-002 therefore gives, for the corresponding physical squared gap,

\[
D(t)=8t+O(t^2).
\tag{28}
\]

For every finite scale this makes the pair nonreal for all sufficiently small negative `t`. Hence the trajectory is not fully real-rooted arbitrarily close below zero, while `(27)` makes it fully real-rooted from zero onward. Its finite periodic transition threshold is therefore exactly

\[
\boxed{
\Lambda_{\rm per}(F)=0.
}
\tag{29}
\]

No factorization of the heat evolution into the `A` and `C_\phi` sectors is being assumed. As in XF-101, only three collision-safe facts are used: the exact multiplicity at the chosen slice, the local discriminant normal form below that slice, and global forward preservation of real-rootedness.

Equation `(29)` is deliberately a **single-slice** transition statement. It does not yet extend the XF-101/XF-104 arbitrary-`tau` construction to the full XF-118 q-scale time history. Doing that would require control of the full-q-scale moment cone at a later target slice, or another way to reserve collision slots coherently under the triangular heat dynamics. The present theorem proves the sharper static fact that the exact Xi source prefix itself has zero separation from the transition boundary.

## 4. Stress tests: why the asymptotically saturated collision block is legitimate

The only potentially dangerous step is scaling the target moments from `c_m` to `d_m=(N/n)c_m` while `N/n->infinity`. Coefficientwise smallness alone would not justify this. Equation `(9)` does: the entire finite Toeplitz deviation scales by exactly the same factor, and the choice `(13)` guarantees that its operator norm still tends to zero. Thus every positivity and local-regularity estimate in XF-119 survives with uniform constants after sufficiently large scale.

The shrinking compensator also has enough nodes for exact equal-weight quadrature. Equation `(17)` gives `n/K->infinity`, whereas XF-119 only needs `n>=CK`. Hence the construction does not use a weighted measure, fractional node count, or rounding of weights at any stage.

The collision block does not perturb any visible target moment. Its cancellation is algebraic, not asymptotic, and `(22)` covers the entire visible band because `R>K`. Nor can accidental overlap with the compensator turn the prescribed doubles into higher-order roots: the single phase parameter avoids the finite set of forbidden values.

Finally, the result does not say that the full Xi function itself has a transition at this slice. It constructs a matched finite periodic control inside exactly the source interface admitted by XF-118/XF-119: prescribed degree, equal weights, unit-circle divisor geometry, and exact first-`K` source moments. The theorem therefore falsifies any **static** transition-coercivity principle whose hypotheses reduce to that interface. Xi-specific information outside it may still rule out the control.

## 5. Consequence for the live Xi-flow fork

XF-119 showed that full q-scale source positivity is not merely a weighted Toeplitz statement: it enters the exact finite real-divisor class at the Xi node budget. XF-120 shows that this additional exactness supplies no static collision margin at all. The same prefix can be carried by a polynomial for which a fraction `1-o(1)` of all roots are simultaneously at simple double collisions and whose periodic Newman threshold is the observation slice itself.

The q-scale source branch is therefore now separated cleanly from the remaining dynamic gate:

\[
\boxed{
\text{full q-scale Xi source moments}
\not\Longrightarrow
\text{positive distance from periodic transition}
}
\tag{30}
\]

within the admitted finite periodic state space, even after enforcing exact degree, equal weights, and real-divisor geometry.

This does **not** reprove the stronger time-history nonidentifiability of XF-101/XF-104 at the larger XF-118 cutoff. That is precisely the surviving test. A useful next theorem would have to show either that full-q-scale Toeplitz coercivity remains sufficiently strong along the relevant positive-time trajectory to repeat the reserved-budget construction at arbitrary target `tau`, or that the heat-time coherence itself destroys the collision-saturated freedom. If neither can be extracted from the q-scale resource, the program should move to information outside the autonomous prefix rather than strengthen the already solved static moment problem again.

## 6. Prior-art and evidence boundary

The external ingredients remain exactly those already anchored in `SOURCES.md`: Gilboa--Peled supplies prescribed-node-count equal-weight quadrature after the XF-119 Poisson regularization, and the periodic backward-heat real-zero-preserver input is already anchored through the Pólya--Benz/Kabluchko literature. The trigonometric moment problem, roots-of-unity cancellation, and the collision normal form are likewise established ingredients.

A targeted prior-art check found the classical truncated trigonometric moment literature and general Chebyshev-type quadrature theory, but no additional theorem is load-bearing here. No absolute novelty claim is made for those ingredients. The line-specific step is the **reserved-budget rescaling of the XF-118 Toeplitz near-isometry**, which allows the XF-119 realization theorem to be applied on only `o(N)` compensator nodes and thereby imports the XF-099 collision crystal into the actual full-q-scale Xi source fiber. Since no new external dependency is introduced, `SOURCES.md` is unchanged.