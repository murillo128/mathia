# XF-038 — vanishing log-gap variation rigidifies the cross-ratio network to the Cauchy form

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `SOURCE-SPECIFIC` + `STRUCTURAL/STABILITY`. XF-031 rewrites the nonlinear triple-discriminant route in terms of a nearest-neighbor positive-conductance operator `L_lambda` and the full cross-ratio operator `L_w`; XF-037 shows that the borderline source-side hypothesis `M V_M=O(1)` forces the total logarithmic gap variation on the active super-mesoscopic Xi block to vanish. These two facts combine more strongly than a pointwise near-lattice statement: once that total variation vanishes, the **entire cross-ratio conductance network is uniformly Cauchy in quadratic-form sense on every sub-buffer scale**.

Let a real-simple block contain gaps

\[
g_0,\ldots,g_{2M-1}>0,
\qquad
D_M:=\sum_{j=0}^{2M-2}\left|\log\frac{g_{j+1}}{g_j}\right|.
\tag{1}
\]

For gap indices `i<k`, XF-018 defines

\[
w_{ik}
=
\frac{g_i g_k}
{(x_k-x_i)(x_{k+1}-x_{i+1})}.
\tag{2}
\]

If both indices lie in the active block and `r=k-i`, then

\[
\boxed{
\frac{e^{-3D_M}}{r^2}
\le w_{ik}\le
\frac{e^{3D_M}}{r^2}.
}
\tag{3}
\]

Thus `D_M=o(1)` implies

\[
\boxed{
\sup_{0\le i<k<2M}
\left|r^2w_{ik}-1\right|=o(1).
}
\tag{4}
\]

The comparison is uniform all the way from adjacent gaps to separations of order `M`; it is not a fixed-separation lattice expansion.

There is also a boundary-stable form version. Fix `beta>0`, let `I` be an interval of `N` gap indices contained in the active block and at index distance at least `beta M` from both block boundaries, and extend a real sequence `f` supported in `I` by zero to the full zero configuration. Define

\[
\mathcal E_w(f)
:=\sum_{i<k}w_{ik}(f_i-f_k)^2,
\tag{5}
\]

and the arithmetic-lattice Cauchy form

\[
\mathcal E_C(f)
:=\sum_{i<k}\frac{(f_i-f_k)^2}{(i-k)^2}.
\tag{6}
\]

Then, for all sufficiently large `M`, there is a constant `C_beta` depending only on `beta` such that

\[
\boxed{
 e^{-3D_M}\mathcal E_C(f)
-\frac{C_\beta e^{D_M}}{M}\|f\|_2^2
\le
\mathcal E_w(f)
\le
 e^{3D_M}\mathcal E_C(f)
+\frac{C_\beta e^{D_M}}{M}\|f\|_2^2.
}
\tag{7}
\]

Moreover the full-line Cauchy form has the elementary exterior Poincare bound

\[
\boxed{
\mathcal E_C(f)\ge\frac1N\|f\|_2^2.
}
\tag{8}
\]

Consequently

\[
\boxed{
D_M=o(1),\quad \frac NM=o(1)
\quad\Longrightarrow\quad
\sup_{0\ne f:\,\operatorname{supp}f\subset I}
\left|
\frac{\mathcal E_w(f)}{\mathcal E_C(f)}-1
\right|=o(1).
}
\tag{9}
\]

For the Xi source package of XF-036--XF-037, take

\[
M=R(T)\log^2T,
\qquad R(T)\to\infty,
\tag{10}
\]

under the borderline hypothesis `M V_M=O(1)`. XF-037 gives `D_M=o(1)`. At the fixed-time memory scale of XF-007, `N(T)\asymp\log^2T`, so

\[
\frac{N(T)}{M(T)}=O\!\left(\frac1{R(T)}\right)=o(1).
\tag{11}
\]

Hence on every memory-scale interval sitting a fixed-fraction distance inside the super-mesoscopic buffer,

\[
\boxed{
\mathcal E_w(f)=(1+o(1))\mathcal E_C(f)
}
\tag{12}
\]

uniformly over all test fields on that interval. In this source-rigid regime, the nonlinear cross-ratio network therefore cannot retain an order-one deformation of the Cauchy energy at the mesoscopic carrier scale.

This is **not** the missing Xi-flow Lyapunov theorem. It does not derive `V_M=O(1/M)`, does not imply pointwise relative convergence of `(L_wf)_i` where cancellations may make the lattice value tiny, and does not sign the nonlinear cross-product `h_i(L_lambda h)_i(L_w h)_i` from XF-031. Its role is narrower: once the borderline compactness gate has been crossed, deformation of the long-range conductance network itself is no longer a leading-order source of misalignment on sub-buffer scales.

## 1. Total log-gap variation makes every internal span quasi-arithmetic

For any two active indices `a,b`, telescoping (1) gives

\[
\left|\log\frac{g_b}{g_a}\right|
\le D_M.
\tag{13}
\]

Fix `i<k`, put `r=k-i`, and use `g_i` as the local scale. Every gap appearing in either denominator span of (2) satisfies

\[
e^{-D_M}g_i\le g_j\le e^{D_M}g_i.
\tag{14}
\]

Therefore

\[
r e^{-D_M}g_i
\le x_k-x_i
=\sum_{j=i}^{k-1}g_j
\le r e^{D_M}g_i,
\tag{15}
\]

and likewise

\[
r e^{-D_M}g_i
\le x_{k+1}-x_{i+1}
=\sum_{j=i+1}^{k}g_j
\le r e^{D_M}g_i.
\tag{16}
\]

At the same time

\[
e^{-D_M}g_i^2\le g_i g_k\le e^{D_M}g_i^2.
\tag{17}
\]

Dividing (17) by the product of (15)--(16) gives (3). No approximation to root positions, density law, or continuum operator is used. The only input is the exact XF-018 cross-ratio coefficient and the total multiplicative distortion of the gaps.

For `r=1`, XF-018 gives `w_{i,i+1}=1` exactly; (3) is deliberately weaker there but keeps one formula for all separations.

Equation (4) follows immediately when `D_M=o(1)`. Notice that a common rescaling of every gap cancels from (2), so no absolute mean-spacing estimate is needed for this deterministic step. What matters is shape variation, exactly the quantity XF-037 collapses.

## 2. Exterior cross-ratio tails cost only the inverse buffer width

Uniform comparison inside the block is not enough for a full-line Dirichlet form because a supported test field still interacts with zeros outside the active block. XF-018 supplies the needed exact tail control.

For an active index `i`, let the first gap index outside the block on the right be `2M` and set

\[
L=2M-i.
\]

When `L\ge2`, XF-018 gives

\[
\sum_{k\ge2M}w_{ik}
\le
\log\left(
1+\frac{g_i}{x_{2M}-x_{i+1}}
\right).
\tag{18}
\]

The denominator contains `L-1` active gaps, each at least `e^{-D_M}g_i`, so

\[
\boxed{
\sum_{k\ge2M}w_{ik}
\le
\log\left(1+\frac{e^{D_M}}{L-1}\right)
\le\frac{e^{D_M}}{L-1}.
}
\tag{19}
\]

The left tail is identical by symmetry. Hence if `i` is at index distance at least `beta M` from both boundaries,

\[
\sum_{k\notin\{0,\ldots,2M-1\}}w_{ik}
\le\frac{C_\beta e^{D_M}}{M}.
\tag{20}
\]

The arithmetic Cauchy kernel satisfies the parallel elementary estimate

\[
\sum_{k\notin\{0,\ldots,2M-1\}}
\frac1{(i-k)^2}
\le\frac{C_\beta}{M}.
\tag{21}
\]

This is the reason for keeping the test field away from the active-buffer edge. If its support reaches an edge, the first uncontrolled exterior gap may be adjacent and the exterior row mass is no longer `O(1/M)`. The fixed-fraction interior condition is a real boundary hypothesis, not cosmetic bookkeeping.

## 3. Quadratic-form comparison

Split each full-line energy into pairs whose two indices lie in the active block and pairs with one supported endpoint outside that block. Denote the internal pieces by `E_w^B` and `E_C^B` and the exterior tails by `T_w` and `T_C`.

Equation (3) gives

\[
e^{-3D_M}\mathcal E_C^B(f)
\le\mathcal E_w^B(f)
\le e^{3D_M}\mathcal E_C^B(f).
\tag{22}
\]

Because `f` vanishes outside `I`, equations (20)--(21) give

\[
0\le T_w
\le\frac{C_\beta e^{D_M}}M\|f\|_2^2,
\qquad
0\le T_C
\le\frac{C_\beta}M\|f\|_2^2.
\tag{23}
\]

Using

\[
\mathcal E_w=\mathcal E_w^B+T_w,
\qquad
\mathcal E_C=\mathcal E_C^B+T_C,
\]

and discarding positive terms in the appropriate direction yields (7).

The estimate is a spectral comparison on the whole finite-dimensional subspace of fields supported in `I`; it is not proved mode by mode. In particular, no Fourier representation of the actual nonuniform root configuration is being assumed.

## 4. A one-line Cauchy exterior inequality makes the comparison relative

Let

\[
I=\{a,a+1,\ldots,a+N-1\}.
\]

For each `i in I`, the left exterior of `I` contributes

\[
\sum_{k\le a-1}\frac{f_i^2}{(i-k)^2}
=f_i^2\sum_{r\ge i-a+1}\frac1{r^2}.
\tag{24}
\]

Since `1<=i-a+1<=N`, comparison with the integral of `x^{-2}` gives

\[
\sum_{r\ge i-a+1}\frac1{r^2}
\ge\frac1{i-a+1}
\ge\frac1N.
\tag{25}
\]

Summing (24)--(25) proves (8). Combining (7) with (8) gives the explicit Rayleigh-quotient enclosure

\[
 e^{-3D_M}-C_\beta e^{D_M}\frac NM
\le
\frac{\mathcal E_w(f)}{\mathcal E_C(f)}
\le
 e^{3D_M}+C_\beta e^{D_M}\frac NM.
\tag{26}
\]

Equation (9) is now immediate.

This estimate also explains the scale boundary. When `N=o(M)`, the uncontrolled exterior of the source block is lower order relative to the intrinsic Cauchy energy of an `N`-site test field. For `N=Theta(M)`, the `O(1/M)` exterior row mass lives at the same order as the lowest Cauchy energy on the support, so no asymptotic relative statement follows from this argument alone.

## 5. Xi specialization and the `L_lambda`/`L_w` frontier

XF-037 proves that the source-side condition

\[
M V_M=O(1)
\tag{27}
\]

combined with translated Xi counting gives

\[
D_M=o(1).
\tag{28}
\]

Substitution into (26) proves (12) at every scale `N=o(M)`. The fixed-time memory carrier of XF-007 is particularly well matched: it occupies `Theta(log^2 T)` gaps, while the source buffer contains `R(T)` times as many.

This removes one possible nonlinear loophole in the active conductance picture. XF-031's `L_w` is not merely equal to the Cauchy graph Laplacian at the exact arithmetic lattice; **after the XF-037 source-rigidity step, its whole Dirichlet form is asymptotically the Cauchy form on the mesoscopic carrier, uniformly over all supported test fields**.

The conclusion is intentionally about quadratic forms. Pointwise relative convergence such as

\[
(L_wf)_i=(1+o(1))(L_Cf)_i
\]

is false as a general inference from (3), because the Cauchy sum can have cancellations. Nor does form equivalence make

\[
\sum_i h_i(L_\lambda h)_i(L_wh)_i
\]

positive: that is a mixed correlation, not either Dirichlet form separately. XF-032's pointwise sign counterexample therefore remains relevant as a warning about the wrong proof shape, even though a source-rigid growing block can no longer sustain an order-one deformation of the `L_w` energy kernel.

The next constructive question is correspondingly sharper. To derive the borderline resource rather than assume it, one still needs a dynamical estimate coupling the nearest-neighbor flux variation to `L_w`, or a signed tapered derivative that closes a bootstrap before (27) is known. If (27) is obtained, the long-range operator itself is already on the correct Cauchy carrier at memory scale; any surviving adverse term must come from the mixed nonlinear correlation, taper/edge effects, a sparse microfold, or failure of the bootstrap into the source-rigid regime.

## 6. Stress test: finite total variation is not enough

The hypothesis `D_M=o(1)` cannot be replaced by merely bounded log-gap variation if one wants asymptotic equality with the Cauchy kernel.

Take an exact geometric gap progression

\[
g_j=Cq^j,
\qquad q>0.
\tag{29}
\]

For a separation `r=k-i`, direct summation in (2) gives, when `q\ne1`,

\[
\boxed{
w_{i,i+r}
=
\frac{q^{r-1}(q-1)^2}{(q^r-1)^2}.}
\tag{30}
\]

The limit `q->1` is `1/r^2`, but for fixed `q\ne1` the large-`r` behavior is not Cauchy; for example, when `q>1` it is exponentially small in `r`. More subtly, taking `q=e^{c/M}` gives total log variation of order `c` across an `M`-scale block. At separations `r=Theta(M)`, (30) approaches a nontrivial `c`-dependent deformation of `1/r^2`, not the arithmetic coefficient.

This matched control is consistent with the theorem: (3) gives only constant-factor comparability when `D_M=Theta(1)`. XF-036--XF-037 are exactly what remove that persistent macroscopic deformation for the Xi source under (27). Thus the source rigidity is load-bearing; the Cauchy recovery is not a universal consequence of positive gaps or of the cross-ratio formula alone.

## 7. Prior-art and novelty boundary

Spectral equivalence of nonlocal Dirichlet forms under controlled mesh distortion, discretizations of fractional Laplacians on nonuniform or quasi-uniform meshes, and Cauchy/fractional diffusion are broad classical and numerical-analysis themes. The discrete nonlocal-diffusion prior-art boundary is already anchored in `research/xi_flow/SOURCES.md` through Ciaurri--Roncal--Stinga--Torrea--Varona, and a targeted audit of neighboring nonuniform-grid and nonlocal variational literature found the expected general framework.

No external theorem is load-bearing here. Equations (3), (7), and (26) are direct finite inequalities from the exact XF-018 cross-ratio coefficient, its telescoping tail bound, and the XF-037 total-variation conclusion. No claim of general novelty is made for quasi-uniform spectral comparison, and absence of an exact literature match is not used as evidence. No `SOURCES.md` change is required.

The durable Mathia-local content is the **scale-exact bridge** between the source-rigidity resource and the active Xi-flow operator: vanishing total log-gap variation forces `L_w` back to the arithmetic Cauchy energy uniformly on every `o(M)` carrier, in particular on the `log^2 T` fixed-time-memory scale inside the `R(T)log^2T` source buffer.

## 8. Consequence for `xi_flow`

The accepted overlap/discriminant route remains unresolved, but the possible failure mechanism is narrower. Under the borderline compactness hypothesis, the long-range cross-ratio graph cannot hide a different mesoscopic spectral geometry: its energy is asymptotically Cauchy. Therefore a positive continuation may legitimately use the lattice Cauchy form as the leading mesoscopic `L_w` energy **after** the XF-037 rigidity gate, with an error controlled by `D_M+N/M` rather than by a formal small-amplitude expansion.

What still has to be proved is upstream and mixed: derive `V_M=O(1/M)` (or an equivalent compactness resource) from the exact dynamics, or sign the tapered mixed `L_lambda`/`L_w` correlation strongly enough to bootstrap into that regime while preserving XF-028 collision coverage. A negative continuation must now produce a source-compatible sparse/mixed obstruction rather than an order-one deformation of the long-range conductance kernel on the mesoscopic carrier.