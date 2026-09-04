# ANF-032 — sharp Montgomery--Taylor energy forces local two-point packing

**Status:** `EXACT-DERIVED + FINITE-CONFIGURATION-COMPACTNESS + THREE-POINT-RIGIDITY + STRUCTURAL-BOUNDARY`. `ANF-030` identifies the exact Montgomery--Taylor extremizer `J_MT`, with nonnegative spatial transform `R_MT`, and `ANF-031` proves that the positive zero set of `R_MT` is strictly sum-free. Those two facts already force a quantitative three-point consistency law on the abstract finite-configuration closure `K` of `ANF-020`, without assuming stationarity or a Palm realization.

For every fixed physical scale `L>0` there is a constant `kappa_L>0` such that any finite configuration `X` whose `J_MT` energy is within `delta` of the sharp value `1` can be made locally two-point sparse at scale `L/2` by deleting at most a fraction

\[
\boxed{
\frac{2\delta}{\kappa_L}
}
\]

of its points. More precisely, after that deletion every interval of length strictly less than `L/2` contains at most two surviving points.

Consequently, if a hypothetical measure `mu_* in K` were dominated by the sharp Montgomery--Taylor budget `nu_MT`, then **every fixed physical scale becomes asymptotically two-point** along any convex finite-configuration approximation to `mu_*`: for each fixed `L`, the mean fraction of points that must be removed to eliminate all bounded three-point clusters tends to zero.

This advances the realizability/compactness gap left by `ANF-031`. Band restriction does not erase all three-point consistency: the exact sum-free obstruction survives quantitatively on every fixed physical scale. What remains possible is only a genuinely nonuniform scale-escape mechanism, because the constant `kappa_L` can deteriorate as `L->infinity` and the weak-* topology does not control the spectral effect of a vanishing fraction of exceptional points strongly enough to pass directly to growing `L`.

## 1. Sharp Montgomery--Taylor excess is a positive pair energy

Use the notation of `ANF-030`:

\[
J_{\rm MT}\ge0,
\qquad
R_{\rm MT}=\widehat J_{\rm MT}\ge0,
\qquad
R_{\rm MT}(0)=1,
\]

and

\[
\int J_{\rm MT}\,d\nu_{\rm MT}=1.
\tag{1}
\]

For a finite configuration

\[
X=\{x_1,\ldots,x_n\}\subset\mathbb R
\]

of distinct points, its normalized diffraction `mu_X` from `ANF-020` satisfies

\[
\begin{aligned}
\int J_{\rm MT}\,d\mu_X
&=
\frac1n\sum_{i,j=1}^{n}R_{\rm MT}(x_i-x_j)\\
&=
1+
\frac2n\sum_{1\le i<j\le n}R_{\rm MT}(x_i-x_j).
\end{aligned}
\tag{2}
\]

Define the nonnegative sharp-energy excess

\[
\boxed{
\Delta(X)
:=
\int J_{\rm MT}\,d\mu_X-1
=
\frac2n\sum_{i<j}R_{\rm MT}(x_i-x_j)
\ge0.
}
\tag{3}
\]

Thus approaching the sharp Montgomery--Taylor face is exactly the same as driving a positive pair energy to zero per particle.

## 2. Sum-free zeros give a positive triple gap on every bounded scale

Fix `L>0` and consider the compact simplex

\[
\mathcal D_L
:=
\{(a,b):a\ge0,\ b\ge0,\ a+b\le L\}.
\tag{4}
\]

Define

\[
H(a,b)
:=
R_{\rm MT}(a)
+R_{\rm MT}(b)
+R_{\rm MT}(a+b).
\tag{5}
\]

`H` is continuous and nonnegative. It is in fact strictly positive on `D_L`. If `a=0` or `b=0`, this follows from `R_MT(0)=1`. If `a,b>0` and `H(a,b)=0`, nonnegativity would force

\[
R_{\rm MT}(a)
=R_{\rm MT}(b)
=R_{\rm MT}(a+b)
=0,
\]

so `a`, `b`, and `a+b` would all lie in the positive Montgomery--Taylor zero set. This is impossible by the strict sum-free theorem of `ANF-031`.

Compactness therefore gives the exact bounded-scale constant

\[
\boxed{
\kappa_L
:=
\min_{(a,b)\in\mathcal D_L}H(a,b)
>0.
}
\tag{6}
\]

Hence every ordered triple `x<y<z` with span `z-x<=L` obeys

\[
\boxed{
R_{\rm MT}(y-x)
+R_{\rm MT}(z-y)
+R_{\rm MT}(z-x)
\ge\kappa_L.
}
\tag{7}
\]

This is the quantitative form of the additive obstruction that remains valid before any thermodynamic, stationary, or Palm limit is taken.

## 3. A cell with many points must pay Montgomery--Taylor energy

Fix an offset `s in R` and partition the line into half-open cells

\[
I_k^{(s)}
=[s+kL,s+(k+1)L),
\qquad k\in\mathbb Z.
\tag{8}
\]

Let

\[
m_k:=|X\cap I_k^{(s)}|.
\]

For one cell with `m_k>=3`, write

\[
E_k
:=
\sum_{\{i,j\}\subset X\cap I_k^{(s)}}
R_{\rm MT}(x_i-x_j).
\tag{9}
\]

Every triple of points in the cell has span `<L`, so (7) applies. Summing (7) over all unordered triples in that cell counts each unordered pair exactly `m_k-2` times. Therefore

\[
(m_k-2)E_k
\ge
\kappa_L\binom{m_k}{3},
\]

and hence

\[
\boxed{
E_k
\ge
\frac{\kappa_L}{6}m_k(m_k-1)
\qquad(m_k\ge3).
}
\tag{10}
\]

Using only the within-cell pairs in (3),

\[
\begin{aligned}
\Delta(X)
&\ge
\frac2n
\sum_{k:m_k\ge3}E_k\\
&\ge
\frac{\kappa_L}{3n}
\sum_{k:m_k\ge3}m_k(m_k-1).
\end{aligned}
\tag{11}
\]

Since `m(m-1)>=3(m-2)` for every integer `m>=3`, define the cell overflow

\[
\mathcal O_{L,s}(X)
:=
\sum_k(m_k-2)_+.
\tag{12}
\]

Then (11) gives the simple linear bound

\[
\boxed{
\frac{\mathcal O_{L,s}(X)}{|X|}
\le
\frac{\Delta(X)}{\kappa_L}.
}
\tag{13}
\]

Thus one may delete at most `O_{L,s}(X)` points and leave no more than two points in any cell of this partition.

## 4. Two shifted partitions remove every bounded three-point cluster

Apply (13) to the two offsets

\[
s=0,
\qquad
s=L/2.
\tag{14}
\]

For each partition, delete all but two points from every overfull cell, and let `Y subseteq X` be the set surviving both deletions. The union bound and (13) give

\[
\boxed{
\frac{|X\setminus Y|}{|X|}
\le
\frac{2\Delta(X)}{\kappa_L}.
}
\tag{15}
\]

Every interval of length strictly less than `L/2` is contained in a cell of at least one of the two shifted length-`L` partitions. Therefore

\[
\boxed{
|Y\cap I|\le2
\quad
\text{for every interval }I\text{ with }|I|<L/2.
}
\tag{16}
\]

Equivalently, after deleting the fraction in (15), every triple of surviving points has diameter at least `L/2`.

The statement is uniform over all finite configurations and uses no density, ordering model, stationarity, ergodicity, or probabilistic representation.

## 5. The local three-point law survives the abstract convex closure `K`

Let `lambda` be a finite convex combination of finite-configuration diffraction measures,

\[
\lambda
=
\sum_r w_r\mu_{X_r},
\qquad
w_r\ge0,
\qquad
\sum_r w_r=1.
\tag{17}
\]

Its sharp excess is

\[
\Delta(\lambda)
:=
\int J_{\rm MT}\,d\lambda-1
=
\sum_r w_r\Delta(X_r).
\tag{18}
\]

Applying (15) configuration by configuration and averaging shows that, at any fixed `L`, the mean particle fraction that must be removed to obtain (16) is at most

\[
\boxed{
\frac{2\Delta(\lambda)}{\kappa_L}.
}
\tag{19}
\]

Now suppose, for contradiction-testing purposes only, that a dominated abstract witness exists:

\[
\mu_*\in K,
\qquad
0\le\mu_*\le\nu_{\rm MT}.
\tag{20}
\]

By the definition of `K`, choose convex finite-configuration approximants `lambda_j -> mu_*` weak-*. Since `J_MT` is a continuous compact-band test, (1), (3), and domination give

\[
1
\le
\lim_j\int J_{\rm MT}\,d\lambda_j
=
\int J_{\rm MT}\,d\mu_*
\le
\int J_{\rm MT}\,d\nu_{\rm MT}
=1.
\tag{21}
\]

Hence

\[
\boxed{
\Delta(\lambda_j)\longrightarrow0.
}
\tag{22}
\]

Combining (19) and (22), for every fixed `L>0` the mean removable fraction tends to zero. Therefore any sequence realizing a point of the sharp dominated face of `K` must become, after a vanishing particle deletion, locally two-point sparse on **every fixed physical scale**.

This is a genuine finite-configuration consistency condition on `K`; no Palm extension is invoked.

## 6. What this closes and what scale escape still permits

`ANF-031` left open whether band restriction and weak-* convexification could erase the three-point consistency responsible for the stationary Palm contradiction. Equations (6)--(22) show that they cannot erase it at fixed scale. A hypothetical abstract witness cannot retain a positive fraction of particles in bounded three-point clusters while saturating the exact Montgomery--Taylor test.

The surviving loophole is narrower but real. `ANF-031` already notes that the additive defect

\[
z_m+z_n-z_{m+n}
\]

tends to zero along large indices. Correspondingly there is no reason for `kappa_L` to stay uniformly positive as `L->infinity`; indeed the near-additive large zeros force bounded-scale triple gaps to deteriorate along growing scales. Therefore (19) cannot be used with `L=L_j->infinity` without an independent quantitative relation between `kappa_L` and the energy excess.

There is a second obstruction to an immediate closure of `K`. Removing `o(|X|)` particles is small in particle proportion, but coherent interference means it is not automatically small in band diffraction under the weak-* topology used in `ANF-020`. Thus one cannot simply discard the exceptional set in (15) and identify the limiting diffraction with that of a dilute monomer/dimer gas.

The next decisive target is therefore quantitative: control either the decay of `kappa_L` strongly enough to let `L` grow with the approximating configuration, or control the band-spectral contribution of the exceptional vanishing particle fraction. This is also a concrete finite-configuration version of the semidefinite/higher-consistency direction suggested by `CLUE-semidefinite-pair-correlation-horizontal-lift.md`.

## 7. Prior-art, audit, and evidence boundary

No new external theorem is load-bearing. The only analytic input is the exact Montgomery--Taylor extremizer and its nonnegative transform from `ANF-030`, whose literature source is already anchored in `SOURCES.md`; the additive input is the exact sum-free zero-set theorem derived in `ANF-031`. The present contribution is the compact triple gap (6), the exact cell-counting inequality (10)--(13), and its consequence for the convex finite-configuration closure (19)--(22). `SOURCES.md` therefore does not change.

The finite part has a short decisive audit. A failure of (6) would produce `a,b>=0`, `a+b<=L` with all three terms in (5) zero; boundary cases contradict `R_MT(0)=1`, while interior cases contradict `ANF-031`. Equation (10) can be checked by observing that each pair in an `m`-point cell belongs to exactly `m-2` triples. The remaining inequalities are monotone consequences of the nonnegative pair energy.

This finding does **not** establish `K cap {mu:0<=mu<=nu_MT}=empty`. It establishes the strongest fixed-scale conclusion currently available without a Palm realization: any such abstract witness would have to be produced by a scale-escape sequence whose three-point structure is pushed beyond every fixed physical radius while its band diffraction remains nonwhite enough to fit the Montgomery--Taylor cusp.