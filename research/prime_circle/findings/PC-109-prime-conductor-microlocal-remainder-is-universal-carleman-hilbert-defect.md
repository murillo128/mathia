# PC-109 — prime-conductor microlocal remainder is a universal Carleman–Hilbert defect

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-108 leaves a geometry-forced non-scalar recentering or microlocal conductor limit as the most immediate escape from its fixed-coordinate strong-limit obstruction. The canonical conductor-resolving embedding can be classified exactly. If the prime residue coordinate `r` is rescaled to the physical mesh coordinate `r/p in [0,1)`, then the complete PC-075 trace-class remainder `T_p` converges strongly to a universal continuous/discrete Hankel defect

\[
\boxed{\mathcal D=C-VHV^*},
\]

where `C` is the classical Carleman operator on `L^2(R_+)`, `H` is the classical Hilbert matrix, and `V` embeds sequences as functions constant on unit intervals. Moreover, after removing the singular lowest-Hardy corner already isolated by PC-108, the remainder converges **in Hilbert--Schmidt norm** to the compact universal operator

\[
\boxed{\mathcal K=\mathcal D-P_0\mathcal DP_0},
\qquad
\boxed{\|\mathcal K\|_{\mathcal S_2}^2=\gamma-4+5\log2}.
\]

Thus the nonzero `S_2` mass that escaped to moving conductor coordinates in PC-108 can indeed be recovered by the natural microlocal rescaling, but what it recovers is completely independent of the prime conductor: it is the discretization defect between the continuous Carleman kernel and the unit-cell Hilbert matrix. This closes the most canonical conductor-microlocal repair as a source of new Prime-Circle arithmetic. It does not rule out non-affine, cross-level, or otherwise geometry-forced recenterings that retain arithmetic before taking the limit.

## 1. The canonical conductor mesh turns the prime remainder into a step approximation

Use the exact prime formula from PC-108. In the PC-075 residue decomposition, for `0<=r,s<p`, Hardy indices `a,b>=0`, and

\[
t=r+s+1,
\qquad m=a+b,
\]

we have

\[
\boxed{
(T_p)_{(r,a),(s,b)}
=
\frac1p
\left(
\frac1{m+t/p}-\frac1{m+1}
\right).
}
\]

Define the canonical affine-mesh isometry

\[
J_p:\mathbb C^p\longrightarrow L^2(0,1),
\qquad
J_pe_r=\sqrt p\,\mathbf1_{[r/p,(r+1)/p)}.
\]

Let

\[
\widehat T_p=(J_p\otimes I)T_p(J_p^*\otimes I),
\]

extended by zero off the step-function subspace. On the rectangle

\[
I_r\times I_s,
\qquad I_r=[r/p,(r+1)/p),
\]

its `(a,b)` integral kernel is exactly

\[
\boxed{
k^{(p)}_{ab}(x,y)
=
\frac1{m+(r+s+1)/p}-\frac1{m+1}.
}
\]

For fixed `m`, the mesh point `(r+s+1)/p` differs from `x+y` by at most `1/p`. The continuum kernel forced by this scaling is therefore

\[
\boxed{
k_{ab}(x,y)
=
\frac1{a+b+x+y}-\frac1{a+b+1}.
}
\]

The only non-square-integrable cell is `a=b=0`, exactly the lowest-Hardy corner already separated in PC-108.

## 2. The escaping PC-108 residual has a nonzero Hilbert--Schmidt microlocal limit

Let

\[
A_p=Q_pT_pQ_p,
\qquad
R_p=T_p-A_p,
\]

with `Q_p` the lowest-Hardy-coordinate projection as in PC-108. Thus `R_p` has zero `(a,b)=(0,0)` block. Define `\mathcal K` on

\[
\mathcal H=L^2(0,1)\otimes\ell^2(\mathbb Z_{\ge0})
\]

by the kernel

\[
(\mathcal K)_{ab}(x,y)
=
\begin{cases}
0,&a=b=0,\\[2mm]
\displaystyle
\frac1{a+b+x+y}-\frac1{a+b+1},&a+b\ge1.
\end{cases}
\]

For `m>=1`, put

\[
f_m(u)=\frac1{m+u}-\frac1{m+1}.
\]

Since

\[
|f_m'(u)|=\frac1{(m+u)^2}\le\frac1{m^2}
\qquad(0\le u\le2),
\]

the step approximation satisfies, pointwise on every residue rectangle,

\[
\left|
f_m\!\left(\frac{r+s+1}{p}\right)-f_m(x+y)
\right|
\le\frac1{pm^2}.
\]

There are `m+1` Hardy pairs `(a,b)` with `a+b=m`. Consequently

\[
\begin{aligned}
\bigl\|
(J_p\otimes I)R_p(J_p^*\otimes I)-\mathcal K
\bigr\|_{\mathcal S_2}^2
&\le
\frac1{p^2}
\sum_{m\ge1}\frac{m+1}{m^4}\\
&\longrightarrow0.
\end{aligned}
\]

Hence

\[
\boxed{
(J_p\otimes I)R_p(J_p^*\otimes I)
\longrightarrow\mathcal K
\quad\text{in }\mathcal S_2.
}
\]

This is the missing topology in PC-108: in the fixed residue embedding the same `R_p` tends strongly to zero while retaining nonzero `S_2` mass, whereas the conductor-scale embedding follows that moving mass and produces a genuine nonzero compact limit.

Because Hilbert--Schmidt convergence preserves the norm and PC-108 computed the exact escaped mass,

\[
\boxed{
\|\mathcal K\|_{\mathcal S_2}^2
=
\lim_{p\to\infty\atop p\ {m prime}}
\|R_p\|_{\mathcal S_2}^2
=
\gamma-4+5\log2
=0.0429515677\ldots .
}
\]

Thus the constant left unexplained geometrically by the fixed-coordinate limit in PC-108 is exactly the squared Hilbert--Schmidt norm of the continuum discretization defect below.

## 3. The continuum operator is exactly Carleman minus the embedded Hilbert matrix

Identify

\[
L^2(0,1)\otimes\ell^2(\mathbb Z_{\ge0})
\cong L^2(\mathbb R_+)
\]

by sending the component `(a,x)` to the coordinate

\[
u=a+x.
\]

Let `C` be the classical Carleman operator

\[
(Cg)(u)=\int_0^\infty\frac{g(v)}{u+v}\,dv,
\]

and let

\[
V:\ell^2(\mathbb Z_{\ge0})\longrightarrow L^2(\mathbb R_+),
\qquad
Ve_a=\mathbf1_{[a,a+1)}.
\]

For the classical Hilbert matrix

\[
H_{ab}=\frac1{a+b+1},
\]

the operator `VHV^*` has the step kernel

\[
(VHV^*)(a+x,b+y)=\frac1{a+b+1}.
\]

Therefore the continuum kernel from Section 1 is exactly

\[
\boxed{
\mathcal D:=C-VHV^*.
}
\]

If `P_0` denotes multiplication by `1_[0,1)`, then the compact residual limit is precisely

\[
\boxed{
\mathcal K=\mathcal D-P_0\mathcal DP_0.
}
\]

In words: all cells except the singular origin cell form a Hilbert--Schmidt correction between the continuous Carleman kernel and its unit-cell Hilbert discretization.

The lowest cell itself is the limit of the PC-108 finite-Hilbert corner. Indeed, after the same mesh embedding, `A_p` has kernel

\[
a_p(x,y)
=
\frac{p}{r+s+1}-1
\qquad(x\in I_r,\ y\in I_s).
\]

On functions supported away from `0`, this converges in norm to the kernel `1/(x+y)-1`; such functions are dense, while `\|A_p\|<=\pi+1` uniformly. Hence

\[
\boxed{
J_pA_pJ_p^*
\longrightarrow
P_0\mathcal DP_0
\quad\text{strongly}.
}
\]

Combining this with the `S_2` convergence of the residual gives the full microlocal conductor limit

\[
\boxed{
(J_p\otimes I)T_p(J_p^*\otimes I)
\longrightarrow
C-VHV^*
\quad\text{strongly}.
}
\]

The singular origin block is not compact: the compression of the Carleman kernel to `(0,1)` retains its scale-invariant singularity at zero. For example, normalized test functions supported on the shrinking dyadic intervals `(2^{-k-1},2^{-k})` converge weakly to zero while their compressed-Carleman images have norms bounded below by dilation invariance. Subtracting the rank-one constant kernel does not change noncompactness. Thus the full limit is not a compact Hilbert--Polya candidate; the only compact part produced by following the escaped PC-108 mass is `\mathcal K`.

## 4. The microlocal limit has lost all prime arithmetic

The conductor-resolving limit is nontrivial, but its formula contains no arithmetic datum:

\[
\boxed{
\mathcal D=C-VHV^*,
\qquad
\mathcal K=\mathcal D-P_0\mathcal DP_0.
}
\]

There is no surviving `p`, Ramanujan sum, primitive-residue selector, divisor pattern, von Mangoldt weight, or cyclotomic parameter. Primality was used only before the limit to obtain the uniform PC-108 mesh formula; after that reduction, every prime follows the same rational Riemann-sum geometry.

In particular, a regularized determinant such as

\[
\det{}_2(I-z\mathcal K)
\]

would be a perfectly legitimate determinant of a fixed universal Hilbert--Schmidt operator, but it would no longer be a determinant carrying prime-shell arithmetic. Matching it to zeta would require an additional external identification or a new geometry-forced arithmetic operation. The present result therefore does **not** claim that the spectrum of `\mathcal K` has been explicitly diagonalized or that no analytic transform of it can be written; it establishes the narrower and decisive point required by the Prime-Circle program: the canonical affine microlocal recovery of the PC-108 escaped mass classicalizes before any zeta-specific spectral information appears.

## 5. Prior-art and novelty audit

The operator-theoretic objects in the limit are classical. Magnus and Rosenblum, already anchored in `research/prime_circle/SOURCES.md` for PC-075, give the classical Hilbert-matrix spectral theory. Pushnitski--Yafaev's Hankel-operator framework, also already anchored there, treats discrete and integral Hankel model operators and is a direct warning against treating the appearance of a Carleman/Hilbert channel as new arithmetic spectral structure. A directed audit additionally found Yafaev's *Hankel and Toeplitz operators: continuous and discrete representations*, *Opuscula Mathematica* 37 (2017), 189--218, DOI `10.7494/OpMath.2017.37.1.189`, which explicitly develops relations between Hankel operators on `ell^2(Z_+)` and `L^2(R_+)`. This places the continuous/discrete comparison itself firmly in classical operator theory.

No theorem-level historical novelty is claimed for the Carleman operator, the Hilbert matrix, step-function discretizations, or Hilbert--Schmidt kernel convergence. The durable Prime-Circle result is the exact identification of the **specific PC-075/PC-108 prime-conductor remainder** under its canonical conductor mesh, including the fact that the escaped norm `gamma-4+5 log 2` becomes exactly the `S_2` norm of the universal off-origin Carleman--Hilbert discretization defect.

The novelty/falsification control is therefore passed only as an internal negative classification: the candidate microlocal mechanism survives as a nonzero operator limit, but fails the arithmetic-retention requirement of the Prime-Circle mandate.

## 6. Consequence for the surviving Hardy/Hankel boundary

PC-108 showed

\[
\text{fixed residue embedding}
\longrightarrow
\text{universal Hilbert corner + escaping }S_2\text{ mass}.
\]

The present result follows that mass at conductor scale and obtains

\[
\boxed{
\text{affine conductor recentering}
\longrightarrow
\text{universal Carleman--Hilbert defect}.
}
\]

Thus merely replacing the fixed residue embedding by the natural continuum mesh does not restore arithmetic; it changes **where** the universal Hankel boundary layer is seen. The compact part is real and nonzero, but it is already prime-blind.

A surviving conductor-limit mechanism must therefore do something genuinely outside this classification before taking `p->infinity`: for example retain cross-level arithmetic in a joint operator before the PC-075 residue split, use a geometry-forced non-affine/multiscale recentering whose limiting kernel still contains primitive/divisor data, or form a non-finite interaction that is not reducible to the single-conductor rational mesh. Those are open boundaries, not positive evidence.
