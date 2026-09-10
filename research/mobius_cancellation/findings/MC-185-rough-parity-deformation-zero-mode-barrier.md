# MC-185 — Rough parity deformation leaves the global zero mode as an independent power-scale obligation

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-184` shows that, for polynomial windows below the unconditional squarefree-variance frontier, the unsigned support of the logarithmically rough Möbius coefficient already has much stronger centered short-interval variance than the signed target. A natural next attempt is therefore to deform the squarefree rough support continuously by the parity variable and extrapolate from easier positive weights to the Möbius sign.

That interpolation step is indeed cheap at fixed-power scale, but **centered variance does not carry the zero mode needed by the signed endpoint**. The missing center is exactly a macroscopic rough Möbius increment, and controlling it at the variance target scale costs the same local-to-global exponent appearing in `MC-177`.

Fix

\[
H=X^\theta,
\qquad
0<\theta<1,
\qquad
y=c\log X,
\qquad
0<c<\min(\theta,1-\theta),
\tag{1}
\]

and write

\[
\beta_y(n)=\mu^2(n)\mathbf 1_{P^-(n)>y},
\qquad
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}
=(-1)^{\omega(n)}\beta_y(n).
\tag{2}
\]

For `x in [X,2X]` define the parity-deformation polynomial

\[
P_x(z)
:=
\sum_{x<n\le x+H}\beta_y(n)z^{\omega(n)}.
\tag{3}
\]

Then

\[
P_x(1)=\sum_{x<n\le x+H}\beta_y(n),
\qquad
P_x(-1)=\sum_{x<n\le x+H}g_y(n)=:R_y(x,H).
\tag{4}
\]

Because every contributing integer is at most `3X` and every one of its prime factors exceeds `y`,

\[
\deg P_x
\le
K_X:=\left\lfloor\frac{\log(3X)}{\log y}\right\rfloor
=O\!\left(\frac{\log X}{\log\log X}\right).
\tag{5}
\]

Thus the same Chebyshev mechanism used in `MC-093`--`MC-094` shows that values on a fixed positive interval determine the parity endpoint `z=-1` with only

\[
\exp(O(K_X))=X^{o(1)}
\tag{6}
\]

loss. In particular, if one controls **centered** variance at a stable family of `K_X+1` Chebyshev nodes in `[0,1]`, the centered variance at `z=-1` transfers with only subpower loss.

However, let

\[
\overline P_X(z)
:=
\frac1X\int_X^{2X}P_x(z)\,dx.
\tag{7}
\]

Then orthogonality to constants gives the exact decomposition

\[
\boxed{
\int_X^{2X}|R_y(x,H)|^2\,dx
=
\int_X^{2X}|R_y(x,H)-\overline P_X(-1)|^2\,dx
+X|\overline P_X(-1)|^2.
}
\tag{8}
\]

The second term is not a harmless centering constant. If

\[
G_y(t):=\sum_{n\le t}g_y(n),
\tag{9}
\]

then the additive-window identity `R_y(x,H)=G_y(x+H)-G_y(x)` gives

\[
\boxed{
X\overline P_X(-1)
=
H\bigl(G_y(2X)-G_y(X)\bigr)+O(H^2+H).
}
\tag{10}
\]

Consequently, in order for the zero-mode term in `(8)` to fit a fixed-power target

\[
X|\overline P_X(-1)|^2
\le
X^{1+o(1)}H^{2-\eta},
\qquad 0<\eta\le1,
\tag{11}
\]

one must have

\[
\boxed{
G_y(2X)-G_y(X)
\ll
X^{1+o(1)}H^{-\eta/2}+H.
}
\tag{12}
\]

For `H=X^theta`, this is the exponent

\[
\max\!\left(1-\frac{\theta\eta}{2},\theta\right),
\tag{13}
\]

exactly the local-to-global exponent ledger in `MC-177`. Thus a proof that regularizes only the **centered fluctuations** of the positive parity deformations cannot by itself yield the uncentered rough Möbius variance required by `MC-180`: the missing zero mode is already a global rough-Mertens-scale obligation.

This obstruction is robust against changing the polynomial center. If `C_X(z)` is any degree-at-most-`K_X` polynomial independent of `x` with `C_X(-1)=0`, then Chebyshev interpolation forces the endpoint discrepancy `\overline P_X(-1)` to reappear at one of the positive nodes up to the same `X^{o(1)}` factor. One cannot choose a clever positive-side centering that simultaneously matches the easy means and deletes the Möbius endpoint mean at fixed-power cost.

The conclusion is therefore narrow but decisive for the current frontier: **`MC-184`'s unsigned support variance plus low-degree parity interpolation is not enough. A viable parity deformation must also supply an independent signed estimate for its zero mode, or use a statistic in which that coarse mode is coupled rather than subtracted.**

## 1. The parity deformation has only sublogarithmic degree

On the support of `beta_y`, every prime factor of `n` is larger than `y` and occurs exactly once. If `omega(n)=k`, then

\[
n>y^k.
\tag{14}
\]

For every term in `(3)`, `n<=2X+H<=3X`, hence

\[
y^k<3X,
\]

which proves `(5)`. This bound is source-forced by the logarithmic rough cutoff and is at least as strong for the present purpose as the primorial/factorial degree bound used for the annular Hamming deformation in `MC-093`.

Let `z_0,\ldots,z_{K_X}` be the affine images in `[0,1]` of the roots of `T_{K_X+1}`. For any real polynomial `Q` of degree at most `K_X`, exact interpolation on those nodes followed by the one-interval Chebyshev extremal inequality gives

\[
|Q(-1)|
\le
L_X\max_j|Q(z_j)|,
\tag{15}
\]

where one may take

\[
L_X
\ll
\Lambda_{K_X}T_{K_X}(3).
\tag{16}
\]

Here `Lambda_K=O(log(K+1))` is the Chebyshev-node Lebesgue constant. Since

\[
T_K(3)\le(3+\sqrt8)^K,
\tag{17}
\]

`(5)` gives

\[
\boxed{L_X=X^{o(1)}.}
\tag{18}
\]

This is only classical polynomial interpolation applied to the source-forced degree ceiling. No arithmetic cancellation is used.

## 2. Centered positive-node control does transfer — but only to centered parity

The average `(7)` is itself a polynomial of degree at most `K_X`. Put

\[
Q_x(z):=P_x(z)-\overline P_X(z).
\tag{19}
\]

Applying `(15)` pointwise in `x`, squaring, and using `max_j |a_j|^2<=sum_j|a_j|^2` gives

\[
\int_X^{2X}|Q_x(-1)|^2\,dx
\le
L_X^2
\sum_{j=0}^{K_X}
\int_X^{2X}|Q_x(z_j)|^2\,dx.
\tag{20}
\]

The number of nodes is also `X^{o(1)}`. Therefore, if for some fixed `eta>0` one could prove uniformly across those positive nodes that

\[
\int_X^{2X}
|P_x(z_j)-\overline P_X(z_j)|^2\,dx
\le
X^{1+o(1)}H^{2-\eta},
\tag{21}
\]

then

\[
\boxed{
\int_X^{2X}
|R_y(x,H)-\overline P_X(-1)|^2\,dx
\le
X^{1+o(1)}H^{2-\eta}.
}
\tag{22}
\]

So interpolation conditioning is not the difficulty. This is the useful part of the deformation: a sublogarithmic family of easier bias values is enough to transport a fixed-power centered estimate all the way to parity.

But `(22)` is not the `MC-180` input. The target there is the uncentered second moment of `R_y`, and `(8)` shows exactly what is still missing.

## 3. The missing center is a macroscopic rough Möbius increment

From `(4)` and `(9)`,

\[
R_y(x,H)=G_y(x+H)-G_y(x).
\tag{23}
\]

Integrating and changing variables in the first term,

\[
\begin{aligned}
X\overline P_X(-1)
&=
\int_X^{2X}\bigl(G_y(x+H)-G_y(x)\bigr)\,dx\\
&=
\int_{2X}^{2X+H}G_y(u)\,du
-
\int_X^{X+H}G_y(u)\,du.
\end{aligned}
\tag{24}
\]

Since `|g_y(n)|<=1`, for real `u,v`

\[
|G_y(u)-G_y(v)|\le |u-v|+1.
\tag{25}
\]

Replacing `G_y(u)` by `G_y(2X)` in the first boundary integral and by `G_y(X)` in the second therefore costs `O(H^2+H)`. This proves `(10)`.

Now `(11)` implies

\[
|\overline P_X(-1)|
\le
H^{1-\eta/2}X^{o(1)}.
\tag{26}
\]

Combining `(10)` and `(26)` gives `(12)`. Conversely, `(12)` with the corresponding uniform `o(1)` control is enough to make the center term fit `(11)`. The zero-mode budget is therefore not an artifact of the proof technique; it is the exact scalar component separated by the `L^2` orthogonal decomposition `(8)`.

At the currently unconditional support-variance range of `MC-184`, `theta<6/11`. For the strongest variance currency `eta=1`, the boundary error `H` in `(12)` is subordinate and the center requires

\[
G_y(2X)-G_y(X)
\ll
X^{1-\theta/2+o(1)}.
\tag{27}
\]

This is already a fixed-power signed cancellation statement. At `theta` approaching `6/11`, its exponent approaches `8/11`; the support theorem itself does not provide it.

`MC-180` and `MC-181` further show why this is not merely an arbitrary rough-number side condition. The logarithmic rough/full transforms have only subpower complexity on the relevant dilation-stable families. Any attempt to obtain the full Möbius variance through the rough representation must therefore explain where a genuinely signed source estimate such as `(12)` comes from rather than treating the endpoint center as an innocuous normalization.

## 4. Changing the center cannot hide the obstruction

One might try to avoid `(8)` by subtracting a more convenient polynomial main term `C_X(z)` with

\[
C_X(-1)=0,
\tag{28}
\]

so that the deformed quantity agrees with `R_y` at the signed endpoint. This merely moves the zero mode into the positive-node estimates.

Set

\[
D_X(z):=\overline P_X(z)-C_X(z).
\tag{29}
\]

If `deg C_X<=K_X`, then `deg D_X<=K_X`, and `(15)` gives

\[
|\overline P_X(-1)|
=|D_X(-1)|
\le
L_X\max_j|D_X(z_j)|.
\tag{30}
\]

For every node,

\[
\int_X^{2X}|P_x(z_j)-C_X(z_j)|^2\,dx
=
\int_X^{2X}|P_x(z_j)-\overline P_X(z_j)|^2\,dx
+X|D_X(z_j)|^2.
\tag{31}
\]

Hence `(30)`--`(31)` imply

\[
\boxed{
\max_j
\int_X^{2X}|P_x(z_j)-C_X(z_j)|^2\,dx
\ge
\frac{X|\overline P_X(-1)|^2}{L_X^2}.
}
\tag{32}
\]

Since `L_X=X^{o(1)}`, any degree-compatible center that forces the endpoint main term to vanish must pay essentially the same fixed-power zero-mode energy at some positive node. The obstruction is therefore invariant under the natural polynomial recenterings compatible with exact parity interpolation.

Allowing a center of much larger degree can of course defeat `(30)` algebraically, but then the center itself carries information not present in the source deformation and the low-degree reconstruction argument no longer applies. Such a construction would need an independent arithmetic justification; it is not a free normalization.

## 5. Relation to `MC-184`, `MC-093`--`MC-094`, and `MC-177`

`MC-184` controls the `z=1` unsigned support after subtracting its natural positive mean, with variance `X^{1+o(1)}H^{1/2}` for `theta<6/11`. The present result explains why that strong support regularity cannot simply be interpolated to `z=-1`: one needs a family of parity biases, not one endpoint, and even a hypothetical family of equally strong **centered** estimates would leave `(12)` untouched.

`MC-093`--`MC-094` already proved the general low-degree Chebyshev lesson for a different Huxley--Watt/Hamming deformation: fixed-gap interpolation does not spend a polynomial exponent, and only a sublogarithmic number of stable bias samples is required. The interpolation mechanism here is therefore explicitly **not new**. The new line-specific content is applying the same rate audit to the actual rough squarefree short-interval coefficient isolated by `MC-180`--`MC-184`, where centering is unavoidable on the support-like positive side, and then identifying the exact zero-mode term that survives.

`MC-177` derived the general signed local-variance-to-Mertens exponent

\[
\max(1-\theta\eta/2,\theta).
\tag{33}
\]

Equation `(13)` reproduces exactly that exponent from the center of the rough parity deformation. This agreement is a consistency check and a structural warning: the deformation has not created a cheaper local-to-global bridge merely by making the positive-bias fluctuations more regular.

## 6. Prior art and novelty assessment

The weighted squarefree family `mu^2(n) z^{omega(n)}` is a standard Selberg--Delange object; the general Landau--Selberg--Delange machinery is already anchored in this line by `MC-S14` (Granville--Koukoulopoulos), and no novelty is claimed for introducing the weight `z^{omega(n)}`. The additional rough cutoff in `(2)` is the existing `MC-180` source object.

The approximation-theoretic input is also classical. `MC-093` cites Eichinger--Yuditskii's pointwise Remez formulation for the one-interval Chebyshev extremal mechanism, and `MC-094` cites Günttner for logarithmic Chebyshev-node Lebesgue constants. A targeted literature check around `mu^2(n)z^{omega(n)}`, Selberg--Delange, short intervals, Chebyshev interpolation, and parity deformation did not identify an external theorem that removes the endpoint mean by centered positive-bias variance alone. No novelty claim is made for the abstract interpolation inequalities.

The durable contribution is the **source-specific composition** `(8)`--`(13)` and the recentering obstruction `(30)`--`(32)`: after the unsigned-support variance of `MC-184`, low-degree parity interpolation can transport fluctuation estimates but cannot manufacture the signed coarse mode. That separates two proof obligations that a naive support-to-parity continuation would otherwise conflate.

## 7. Boundaries and falsification tests

- The result does not say that parity deformation is useless. It says that **centered** positive-bias control alone is insufficient. A source-natural theorem that also controls the signed center, or a coupled statistic that never discards it, remains a valid escape.
- Equation `(20)` requires control at a stable family of `K_X+1` positive nodes, or another parameter set with a separately audited interpolation constant. `MC-184` supplies only the single `z=1` endpoint and is not being silently upgraded to the whole family.
- No Selberg--Delange asymptotic is used to bound the endpoint `z=-1`. Doing so at a fixed-power level would risk reintroducing the Mertens/zero-free problem that this line is trying to explain.
- The exact mean decomposition `(8)` uses the uniform measure on `x in [X,2X]`. Other positive measures produce an analogous constant component but require their own boundary identity; this finding does not assert the same formula verbatim for arbitrary weights.
- The error `O(H^2+H)` in `(10)` uses only `|g_y|<=1`. It is subordinate to the first term in `(12)` precisely in the parameter regime encoded by `(13)`; it must not be dropped outside that regime.
- The recentering obstruction `(32)` assumes a center of degree at most `K_X`, the natural class if centering is to remain inside the same exact deformation. Higher-degree or nonpolynomial centers are not ruled out, but their extra information must be justified independently.
- No new bound for `R_y`, `G_y`, `M(x)`, or the zeta zero set is proved.

The claim is falsified if the degree ceiling `(5)` fails, if the Chebyshev transfer factor is not subpower, if the orthogonal decomposition `(8)` or boundary identity `(10)` is incorrect, or if a degree-`K_X` recentering satisfying `(28)` can avoid the lower bound `(32)`.

## Consequence for the active frontier

After `MC-184`, the tempting next move was to use the now-controlled squarefree rough support as the easy end of a parity interpolation. The present result closes the simplest version of that move. **Support regularity and parity interpolation solve only the fluctuating part; the coarse signed mode survives with exactly the local-to-global power cost.**

The next useful source-side theorem must therefore do more than prove centered variance for weights `beta_y(n)z^{omega(n)}`. It must either produce an independent bound for the endpoint mean `(12)`, retain a signed coarse coefficient together with the local fluctuations in one estimate, or expose a parity-sensitive bilinear/Type-II mechanism whose cancellation acts before the zero mode is separated. A proposal that subtracts a positive-bias main term and then extrapolates without pricing `(10)` has not yet crossed the remaining Möbius barrier.