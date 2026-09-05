# XF-043 — super-mesoscopic buffers suppress far-tail gap-shape replenishment

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `STRUCTURAL/BOUNDARY`. XF-042 isolates the only exterior mechanism that can oppose nonlinear Cauchy relaxation of a finite gap block: nonuniform exterior replenishment of the block shape. That exterior should not be treated as one indivisible forcing term. Once a physical buffer separates the block from the remote zeros, the exact differenced zero-motion identity of XF-014 gives a stronger cancellation for the **far** exterior than the raw centered-mismatch norm suggests.

For a block of `N` gaps near height `T`, with block gaps bounded above by `b_*`, let the far exterior begin at physical distance at least `D` from both ends of the block. In the Rodgers--Tao real-simple regime, if

\[
D=R(T)\log T,
\qquad R(T)\to\infty,
\qquad R(T)=o(T/\log T),
\tag{1}
\]

then the net far-tail contribution to the block shape energy is bounded by

\[
\boxed{
|\mathcal R_{\rm far}|
\ll
\frac{r_I\sqrt N}{D},
}
\tag{2}
\]

provided only that the block has the source-scale upper envelope `b_*\ll1/\log T`. No pointwise upper or lower bound on any remote gap is required. Combining (2) with XF-042 gives

\[
\boxed{
D^+r_I
\le
-\lambda_I r_I
+F_I^{\rm near}
+O\!\left(\frac{\sqrt N}{D}\right),
\qquad
\lambda_I=\frac{2N}{b_*^2(N-1)^2},
}
\tag{3}
\]

where `F_I^{near}` contains only exterior gaps inside the chosen buffer. Thus the remote tail is an additive input whose stationary shape scale is at most

\[
\boxed{
\frac{\sqrt N/D}{\lambda_I}
\ll
\frac{b_*^2N^{3/2}}{D}
}
\tag{4}
\]

in `r_I`, or, after normalizing by the source spacing `s~4pi/log T`,

\[
\boxed{
A_I:=\frac{r_I}{s\sqrt N}
\quad\Longrightarrow\quad
A_{I,{\rm far}\text{-}{\rm floor}}
\ll_C
\frac{Ns}{D}.
}
\tag{5}
\]

For the full fixed-time memory scale `N=O(log^2 T)` and the source-valid super-mesoscopic buffer `D=R(T)log T`, this is `O(1/R(T))=o(1)`. Consequently, **far zeros cannot sustain an order-one memory-scale gap-shape obstruction once a diverging physical buffer is inserted. Any such persistent obstruction must be replenished from inside the near buffer.** This is the finite-window dynamical analogue of the far-tail geometric localization in XF-019, but it applies directly to the exact shape-relaxation inequality of XF-042.

The result does not make the full exterior forcing negligible down to the inverse-buffer target `M^-2`. At very small shape amplitude the additive `O(sqrt(N)/D)` input can compete with relaxation. The durable conclusion is the scale separation (5): the remote tail can support at most a core-span/buffer-ratio shape floor by this mechanism. Closing the Xi argument still requires control, cancellation, or multiscale propagation through the near buffer.

## 1. Split the exact exterior contribution before estimating it

Work at a real-simple time at which XF-014 applies. Let

\[
I=\{a,a+1,\ldots,a+N-1\},
\qquad
\bar g_I=\frac1N\sum_{i\in I}g_i,
\qquad
\nu_i=g_i-\bar g_I,
\qquad
r_I^2=\sum_{i\in I}\nu_i^2.
\tag{6}
\]

XF-014 gives

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{7}
\]

For any exterior subset `E`, define its exact net contribution to the `i`th gap velocity by

\[
A_i^E:=\sum_{k\in E}c_{ik}(g_k-g_i).
\tag{8}
\]

If

\[
Q_I:=\frac12r_I^2,
\tag{9}
\]

then the contribution of `E` to `Q_I'` is exactly

\[
\boxed{
\mathcal R_E
=2\sum_{i\in I}\nu_i A_i^E.
}
\tag{10}
\]

This form keeps together the favorable exterior sink and the mismatch part separated in XF-042. That is important for the remote tail: estimating the centered mismatch field alone throws away a cancellation already present in the differenced zero-motion equation.

Choose fixed exterior cutoff indices `K_-<a` and `K_+\ge a+N` and split

\[
E_{\rm far}
=\{k\le K_-\}\cup\{k\ge K_+\},
\tag{11}
\]

with physical separations

\[
x_a-x_{K_-+1}\ge D,
\qquad
x_{K_+}-x_{a+N}\ge D.
\tag{12}
\]

The remaining exterior gaps form `E_near`. For an interval in time, the same decomposition can be used as long as the fixed cutoff labels retain the separations (12); the theorem is otherwise an instantaneous statement.

## 2. The far gap-velocity tail has an exact telescoping reduction

The key identity from XF-014 is

\[
\boxed{
c_{ik}(g_k-g_i)
=
\frac1{x_{i+1}-x_{k+1}}
-
\frac1{x_i-x_k}.
}
\tag{13}
\]

For `k>i`, write

\[
A_k=x_k-x_i,
\qquad
B_k=x_{k+1}-x_{i+1},
\qquad
C_k=x_{k+1}-x_i=A_{k+1}=B_k+g_i.
\tag{14}
\]

Then

\[
\left|c_{ik}(g_k-g_i)\right|
\le
\left(\frac1{A_k}-\frac1{A_{k+1}}\right)
+
\frac{g_i}{B_k(B_k+g_i)}.
\tag{15}
\]

Summing from `K_+` to infinity therefore gives

\[
\boxed{
\sum_{k\ge K_+}
\left|c_{ik}(g_k-g_i)\right|
\le
\frac1{x_{K_+}-x_i}
+g_i\sum_{k\ge K_+}
\frac1{(x_{k+1}-x_{i+1})^2}.
}
\tag{16}
\]

The first term is a literal telescoping endpoint. The left tail has the symmetric estimate

\[
\boxed{
\sum_{k\le K_-}
\left|c_{ik}(g_k-g_i)\right|
\le
\frac1{x_i-x_{K_-+1}}
+g_i\sum_{k\le K_-}
\frac1{(x_i-x_k)^2}.
}
\tag{17}
\]

Because of (12), the endpoint terms are `O(1/D)` uniformly in `i in I`. The remaining question is only a reciprocal-square count of remote zeros. Crucially, the remote gap amplitudes `g_k` have disappeared.

## 3. Rodgers--Tao counting makes the reciprocal-square tail `O(log T/D)`

Suppose the block lies at height comparable with `T`, and `1\ll D=o(T)`. The global zero-counting estimate recorded in XF-020 implies, uniformly on the relevant real-simple slices,

\[
N_t([u,u+L])
\ll
L\log T+\log^2T+\frac{L^2}{T}
\tag{18}
\]

whenever `u\asymp T` and `0<L\le T/2`. Partition the zeros to the right of `u+D` into dyadic shells

\[
2^mD\le x_k-u<2^{m+1}D.
\tag{19}
\]

For shells remaining at height `\asymp T`, (18) gives

\[
\sum_{x_k-u\ge D}\frac1{(x_k-u)^2}
\ll
\sum_m
\left(
\frac{\log T}{2^mD}
+
\frac{\log^2T}{4^mD^2}
+
\frac1T
\right).
\tag{20}
\]

The first two sums are geometric. The `1/T` term occurs for only `O(log(T/D))` shells. Zeros beyond the comparable-height region are handled by the global bound `N_t([0,Y])\ll Y\log Y`, which contributes `O(log T/T)`. Hence

\[
\boxed{
\sum_{x_k-u\ge D}\frac1{(x_k-u)^2}
\ll
\frac{\log T}{D}
+
\frac{\log^2T}{D^2}
+
\frac{\log T}{T}.
}
\tag{21}
\]

The left tail satisfies the same bound, using the corresponding lower-height shells and the even symmetry/global growth of the zero set for the remote remainder.

Now take `D=R(T)log T` as in (1). Then

\[
\frac{\log T}{D}=\frac1R,
\qquad
\frac{\log^2T}{D^2}=\frac1{R^2},
\qquad
\frac{\log T}{T}=o(1/R),
\tag{22}
\]

where the last relation uses `R=o(T/log T)`. If the block obeys the source-scale upper envelope

\[
0<g_i\le b_*\le Cs,
\qquad
s\asymp\frac1{\log T},
\tag{23}
\]

then (16)--(17) and (21)--(22) yield

\[
\boxed{
\max_{i\in I}|A_i^{\rm far}|
\ll_C
\frac1D.
}
\tag{24}
\]

No bound on `g_k` for `k in E_far` was used. This is stronger than applying the raw conductance estimate `c_{ik}=O(D^{-2})` term by term, because the telescoping part of (13) sums the potentially irregular remote gap field before zero counting is invoked.

## 4. Far-tail forcing enters the shape equation only at buffer order

From (10), Cauchy--Schwarz and (24),

\[
\boxed{
|\mathcal R_{\rm far}|
\le
2r_I\sqrt N
\max_{i\in I}|A_i^{\rm far}|
\ll_C
\frac{r_I\sqrt N}{D}.
}
\tag{25}
\]

For the near exterior retain the XF-042 organization. Define

\[
B_i^{\rm near}
:=2\sum_{k\in E_{\rm near}}c_{ik}(g_k-\bar g_I),
\qquad
\widetilde B_i^{\rm near}
:=B_i^{\rm near}-\frac1N\sum_{j\in I}B_j^{\rm near},
\tag{26}
\]

and

\[
F_I^{\rm near}:=
\left(\sum_{i\in I}|\widetilde B_i^{\rm near}|^2\right)^{1/2}.
\tag{27}
\]

Dropping the favorable near-exterior diagonal sink and using the internal coercivity of XF-042 gives

\[
Q_I'
\le
-2\mu_Ir_I^2
+r_IF_I^{\rm near}
+O_C\!\left(\frac{r_I\sqrt N}{D}\right),
\qquad
\mu_I=\frac{N}{b_*^2(N-1)^2}.
\tag{28}
\]

Dividing by `r_I` when positive and using the upper-Dini interpretation at zero yields (3), with `lambda_I=2mu_I`.

Equation (3) is the useful structural statement: **after a broad physical buffer is inserted, the forcing term that remains genuinely uncontrolled is local to that buffer, plus an explicit remote error of order `sqrt(N)/D`.** The infinite exterior has been reduced to a finite near-zone problem at the level of the exact nonlinear shape dynamics.

## 5. Source-scale equilibrium floor is the core-span/buffer ratio

Normalize as in XF-042,

\[
A_I=\frac{r_I}{s\sqrt N}.
\tag{29}
\]

If the near forcing is temporarily suppressed, (3) implies

\[
D^+A_I
\le
-\lambda_IA_I
+O_C\!\left(\frac1{sD}\right).
\tag{30}
\]

Duhamel therefore gives a remote-tail equilibrium floor bounded by

\[
A_{I,{\rm far}\text{-}{\rm floor}}
\ll_C
\frac1{sD\lambda_I}.
\tag{31}
\]

Using `b_*<=Cs` and the definition of `lambda_I`,

\[
\boxed{
\frac1{sD\lambda_I}
\le
\frac{C^2}{2}
\frac{s(N-1)^2}{DN}
\ll_C
\frac{Ns}{D}.
}
\tag{32}
\]

The quantity `Ns` is precisely the expected physical span of an `N`-gap source-scale core. Thus the far-tail forcing floor is controlled by the same macroscopic ratio `core span / buffer width` that appears geometrically in XF-019, but here it follows from the exact gap-velocity cancellation and feeds directly into the nonlinear relaxation estimate.

At the fixed-time memory scale

\[
N\le C_0\log^2T,
\qquad
s\sim\frac{4\pi}{\log T},
\qquad
D=R(T)\log T,
\tag{33}
\]

we get

\[
\boxed{
A_{I,{\rm far}\text{-}{\rm floor}}
=O_{C,C_0}(1/R(T))=o(1).
}
\tag{34}
\]

Equivalently, for any fixed `a>0`, if `A_I>=a` then for sufficiently large `R(T)` the far-tail term in (28) is a vanishing fraction of the internal Cauchy dissipation. An order-one memory-scale irregularity cannot be maintained by the remote zeros beyond a super-mesoscopic buffer.

XF-020 already proves that such buffers are source-compatible: the same choice `D=R(T)log T` contains `asymp R(T)log^2T` zeros with vanishing relative counting error. No extension of the bounded-parameter local counting theorem is required.

## 6. Stress tests and hard boundary

The theorem does **not** control `F_I^{near}`. The buffer can contain strongly irregular gaps, and those gaps may replenish the core at exactly the rate required by XF-042. The result relocates the obstruction; it does not remove it.

The estimate also does not force the shape to the inverse-buffer amplitude used in XF-035--XF-041. Equation (34) gives an `O(1/R)` remote floor at the full memory scale, whereas `M^-2` is much smaller for the available source buffers. A proof that needs inverse-buffer precision must either exploit additional cancellation in the far term, iterate the estimate across nested buffers, or control the near zone strongly enough that the effective tail starts much farther away.

The core upper envelope `g_i<=b_*<=Cs` is substantive and must hold over any time interval on which (3) is integrated. As in XF-042, no autonomous maximum principle supplies it for a finite block. No lower-gap bound is needed. Remote gaps require no pointwise envelope at all.

The cutoffs in (12) must remain physically separated. If a fixed buffer collapses during the evolution, the estimate must be restarted with a new valid decomposition; no claim is made across a collision or outside the real-simple regime.

Finally, (21) is an aggregate counting consequence, not a local rigidity theorem. It does not bound individual conductances, endpoint velocities, or near-buffer gaps. Those stronger statements remain unavailable.

## 7. Prior art and novelty boundary

Long-range exterior tails are standard in the analysis of fractional and other nonlocal diffusion equations; modern regularity theory explicitly keeps nonlocal tail norms as part of local estimates. No novelty is claimed for the generic principle that a Cauchy-type kernel has algebraically decaying exterior influence, for dyadic summation of a counting measure, or for Duhamel/input-to-state estimates.

Rodgers--Tao are the primary source for the Xi zero-motion law and global `O(log^2 T)` zero counting, both already anchored in `SOURCES.md`. XF-014 supplies the exact absolutely convergent differenced identity (13), while XF-020 supplies the source-valid super-mesoscopic counting scale. No new external theorem is load-bearing, so `SOURCES.md` does not need expansion.

The Mathia-local content is the combination relevant to the live Xi obstruction: the far part of XF-042's exterior replenishment admits the cancellation (13), which removes remote gap amplitudes and turns the infinite tail into the explicit input `O(sqrt(N)/D)`. This produces the source-scale shape floor (32)--(34) and shows that persistent order-one memory-scale structure must be fed from the **near buffer**, not from arbitrarily remote zeros. No bibliographic novelty claim is made beyond that repository-specific structural consequence.

## 8. Consequence for `xi_flow`

The finite-window frontier is now narrower than in XF-042. The phrase “exterior replenishment” should no longer treat all exterior scales equally. With the source-valid buffer of XF-020, the remote part of the exact nonlinear gap dynamics is quantitatively harmless above the `O(Ns/D)` shape scale. At the full fixed-time memory scale this threshold can be made `o(1)` by taking `R(T)->infinity`.

The next sharp question is therefore whether the **near-buffer mismatch** can itself be propagated outward or canceled. A promising positive route would apply (3) on nested or overlapping windows, transferring the uncontrolled shell outward while paying a summable sequence of core-span/buffer ratios. A negative route would construct a matched real-rooted heat flow in which a finite-width moving shell continually feeds the inner block at the XF-042 threshold despite remote-tail suppression. Either outcome would address the remaining dynamical escape at the correct spatial scale.