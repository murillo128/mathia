# XF-031 — triple-discriminant taper has an exact nonlinear product rule

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `STRUCTURAL/BOUNDARY`. XF-029 showed only at arithmetic-lattice quadratic order that a slow taper localizes overlapping three-root discriminants through a Cauchy commutator, while XF-030 supplied the exact finite-gap scalar contrast law for one triple. The missing algebraic question can now be answered at full nonlinear finite-gap level: for a finitely supported taper, every explicit localization defect enters through a discrete first difference of the taper, and the signed cubic exterior kernel of XF-030 is itself an exact discrete coboundary.

Let

\[
g_i=x_{i+1}-x_i>0,
\qquad
y_i=\log g_i,
\qquad
d_j=y_{j+1}-y_j,
\]

and let the normalized three-root discriminant be

\[
\mathcal J_j=F(d_j),
\qquad
\phi_j:=F'(d_j)
= -\frac{(r_j-1)(r_j+2)(2r_j+1)}{(r_j+1)(r_j^2+r_j+1)},
\qquad
r_j=\frac{g_{j+1}}{g_j},
\]

as in XF-030. For any finitely supported real sequence `a_j`, define

\[
\mathcal K_a:=\sum_j a_j\mathcal J_j.
\]

Then on every real-simple slice on which the Xi gap flow is defined,

\[
\boxed{
\mathcal K_a'
=\sum_i\bigl(a_{i-1}\phi_{i-1}-a_i\phi_i\bigr)y_i'.
}
\tag{1}
\]

The coefficient has the exact centered product rule

\[
\boxed{
\begin{aligned}
a_{i-1}\phi_{i-1}-a_i\phi_i
={}&\frac{a_{i-1}+a_i}{2}(\phi_{i-1}-\phi_i)\\
&+\frac{\phi_{i-1}+\phi_i}{2}(a_{i-1}-a_i).
\end{aligned}}
\tag{2}
\]

Thus the part created specifically by changing the taper is proportional to the **first discrete difference** `a_{i-1}-a_i` at arbitrary positive gaps. Since XF-030 gives `F''<0` and `phi(r)` decreases from `2` to `-2` on `(0,infinity)`,

\[
\left|\frac{\phi_{i-1}+\phi_i}{2}\right|<2,
\tag{3}
\]

so the explicit taper coefficient is uniformly bounded by `2|a_{i-1}-a_i|`. This is an exact nonlinear localization statement, not a lattice expansion.

It still does **not** prove monotonicity or a uniform `O(1/M)` error for a width-`M` taper: `y_i'=(\log g_i)'` can be singular near a collision, and the sign of the locally constant-weight bulk term remains open. Near collision one must retain the positive pair-coverage mechanism of XF-028 rather than estimate (2) by absolute values. Away from collision, (1)--(3) identify precisely what must be controlled.

## 1. Exact finite-gap summation by parts

The derivation uses only the one-dimensional shape reduction of XF-030. Since

\[
d_j'=y_{j+1}'-y_j',
\]

one has

\[
\begin{aligned}
\mathcal K_a'
&=\sum_j a_jF'(d_j)d_j'\\
&=\sum_j a_j\phi_j(y_{j+1}'-y_j').
\end{aligned}
\tag{4}
\]

Because `a` has finite support, ordinary index summation by parts is exact and has no convergence boundary term. The coefficient of `y_i'` receives `+a_{i-1}\phi_{i-1}` from the triple starting at `i-1` and `-a_i\phi_i` from the triple starting at `i`, giving (1).

Writing

\[
\bar a_i=\frac{a_{i-1}+a_i}{2},
\qquad
\bar\phi_i=\frac{\phi_{i-1}+\phi_i}{2},
\]

then gives the elementary product rule

\[
a_{i-1}\phi_{i-1}-a_i\phi_i
=\bar a_i(\phi_{i-1}-\phi_i)
+\bar\phi_i(a_{i-1}-a_i),
\tag{5}
\]

which is (2). The first term is the finite-gap bulk coefficient with a locally averaged weight. The second vanishes identically wherever the taper is locally constant.

This answers the first algebraic half of the accepted overlap/taper clue: the nonlinear translated-triple observable really does admit a summation-by-parts organization in which the *new* localization coefficient is a taper difference. What remains is analytic rather than algebraic: showing that the resulting term is lower order in the source-relevant regime, or constructing a growing-buffer counterexample where it is not.

## 2. The XF-030 cubic exterior kernel is itself a coboundary

The same structure is visible directly in the signed cubic field. Fix a root `z` exterior to all triples in the active group under consideration and set

\[
A_{j,z}:=\frac1{(x_j-z)(x_{j+1}-z)}.
\tag{6}
\]

A one-line subtraction gives

\[
\boxed{
A_{j,z}-A_{j+1,z}
=\frac{g_j+g_{j+1}}
{(x_j-z)(x_{j+1}-z)(x_{j+2}-z)}.
}
\tag{7}
\]

The right-hand side is exactly the cubic exterior kernel multiplying `2 phi_j` in XF-030. Therefore the contribution of this fixed far exterior root to the tapered sum is

\[
\begin{aligned}
2\sum_j a_j\phi_j(A_{j,z}-A_{j+1,z})
&=2\sum_i(a_i\phi_i-a_{i-1}\phi_{i-1})A_{i,z}.
\end{aligned}
\tag{8}
\]

So the cubic kernel is not merely rapidly decaying: across translated triples it is an exact discrete derivative of a positive inverse-square two-root kernel. Equation (8) transfers that derivative onto the same product `a phi` that appears in (1).

There is one important boundary. A root lying inside the active region is not exterior to every translated triple, so one must not apply (8) across triples that contain that root by silently retaining the exterior decomposition. Equation (1), derived directly from the complete gap dynamics, has no such bookkeeping problem and remains the global exact identity. Equation (8) is the clean far-exterior interpretation of the same summation-by-parts structure.

For Xi zeros the far-root sum after (8) remains absolutely convergent: `A_{i,z}` decays quadratically in the root distance. The gain is therefore not convergence alone but that slow spatial variation of `a phi` can now be charged explicitly against an absolutely summable kernel.

## 3. The contrast flux is a positive conductance acting on reciprocal gaps

The remaining bulk coefficient also has an exact positive-conductance representation. Put

\[
h_i:=\frac1{g_i}.
\]

For two adjacent gaps `p=g_i`, `q=g_{i+1}`, direct algebra in the XF-030 formula gives

\[
\boxed{
\phi\!\left(\frac qp\right)
=\lambda(p,q)\left(\frac1q-\frac1p\right),
}
\tag{9}
\]

where

\[
\boxed{
\lambda(p,q)
=\frac{pq(q+2p)(2q+p)}
{(p+q)(p^2+pq+q^2)}>0.
}
\tag{10}
\]

Writing `lambda_i=lambda(g_i,g_{i+1})`, equation (9) is

\[
\phi_i=\lambda_i(h_{i+1}-h_i).
\tag{11}
\]

Consequently, for a locally constant taper,

\[
\boxed{
\phi_{i-1}-\phi_i
=\lambda_{i-1}(h_i-h_{i-1})
+\lambda_i(h_i-h_{i+1})
=:(L_\lambda h)_i.
}
\tag{12}
\]

Thus the nonlinear triple-shape gradient is itself a nearest-neighbor positive-conductance flux in the reciprocal-gap variable. This is a stronger structural statement than merely knowing that `F` is strictly concave in `d`: it identifies the exact variable in which adjacent contrast is diffusive.

## 4. The Xi gap flow supplies a second positive-conductance operator on the same variable

XF-018 introduced the collision-safe cross-ratio weights

\[
w_{ik}=c_{ik}g_i g_k,
\qquad
0<w_{ik}\le1,
\tag{13}
\]

where XF-014 writes the exact gap evolution as

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i).
\tag{14}
\]

Since

\[
w_{ik}(h_i-h_k)
=c_{ik}(g_k-g_i),
\tag{15}
\]

define the positive graph Laplacian

\[
(L_wh)_i:=\sum_{k\ne i}w_{ik}(h_i-h_k).
\tag{16}
\]

Equations (14)--(16) give the exact log-gap velocity

\[
\boxed{
y_i'=\frac{g_i'}{g_i}=2h_i(L_wh)_i.}
\tag{17}
\]

Combining (12) and (17), the locally constant-weight bulk density in (1) is therefore

\[
\boxed{
2h_i(L_\lambda h)_i(L_wh)_i.
}
\tag{18}
\]

This puts the unresolved finite-gap sign question into a precise form: it is a correlation between two positive-conductance Laplacians acting on the **same reciprocal-gap field**, one nearest-neighbor and shape-generated (`L_lambda`), the other long-range and cross-ratio-generated (`L_w`). Positivity of each operator separately does not make the pointwise product in (18) nonnegative, so no Lyapunov conclusion is being claimed.

When an untapered infinite sum is not independently justified, (18) should be read locally, on indices where the finitely supported taper is constant. The finding does not assert convergence of `sum_j J_j` on the full Xi zero set.

## 5. Compatibility with the lattice and collision regimes

Near an arithmetic lattice,

\[
g_i=h(1+\varepsilon u_i),
\qquad
\phi_i=-\frac32\varepsilon(u_{i+1}-u_i)+O(\varepsilon^2).
\tag{19}
\]

Substituting (19) and the XF-029 linearized Cauchy gap flow into (1), then performing the ordinary symmetric pair summation, recovers the weighted Cauchy form

\[
\mathcal K_a'
=\frac{3\varepsilon^2}{h^2}\langle v,aLv\rangle
+O(\varepsilon^3/h^2)
\]

and hence the `La` commutator of XF-029. There is no conflict between the first-difference product rule here and the `La` potential there: the latter appears after the first-difference taper term is paired with the translation-invariant Cauchy flow and summed once more.

At the opposite collision limit, `phi` remains bounded but `y_i'` is singular. Therefore the estimate obtained from (3),

\[
\left|
\sum_i\bar\phi_i(a_{i-1}-a_i)y_i'
\right|
\le
2\sum_i|a_{i-1}-a_i|\,|y_i'|,
\tag{20}
\]

is not a uniform collision estimate. XF-028 supplies the correct local information there: a covered collapsing pair has positive leading coefficient `8W_k/epsilon^2`. Any eventual nonlinear taper theorem must combine that pair-coverage positivity with (1)--(3), not replace the collision analysis by an absolute-value bound on (20).

This also blocks an overly strong interpretation of a width-`M` taper. Although `|a_i-a_{i-1}|=O(1/M)` for a smooth profile, summing (20) does not by itself yield `O(1/M)` total loss, because neither the number of transition sites nor `|y_i'|` is uniformly bounded by the present argument.

## 6. Stress tests and falsification boundary

A hard taper has order-one first differences, so (2) permits the same large boundary flux already seen in XF-027. Slow tapering removes that *coefficient* obstruction exactly, but it does not establish the sign of the bulk term (18). The two failure modes are therefore cleanly separated rather than hidden in one exterior-field remainder.

A decisive positive continuation would prove a coercive or signed comparison for the sum of (18), with an error controlling the second term in (2) by taper variation on the available Xi buffer. Such a theorem must reduce to XF-029 near the lattice and respect XF-028 near collision. A decisive negative continuation would construct growing-buffer positive-gap configurations for which the taper differences tend to zero while the adverse contribution in (1) remains comparable to or larger than the bulk production.

The identity is universal for ordered one-dimensional logarithmic repulsion once the XF-014 gap equation is available. It is therefore not an Xi-specific selector. Xi-specific value would enter only through source-valid control of the reciprocal-gap field, the cross-ratio network, collision coverage, or the super-mesoscopic buffer.

## 7. Prior-art and novelty boundary

The underlying Vandermonde/Stieltjes structure, one-dimensional log-gas flow, discrete summation by parts, and positive graph Laplacians are classical. The relevant general log-gas and nonlocal-diffusion anchors are already recorded in `SOURCES.md`. A targeted search of deterministic log-gas/Calogero heat-flow literature and the spacing-ratio literature found many statistical uses of adjacent-gap ratios but did not identify a theorem matching the specific normalized-three-root observable together with (1), (7), and the reciprocal-gap conductance factorization (9)--(18).

No external theorem is load-bearing here: equations (1)--(18) are exact algebra from XF-014, XF-018, and XF-030. Accordingly no new `SOURCES.md` entry is required, and absence of an exact literature match is not used as proof of general novelty. The durable Mathia-local content is the exact nonlinear localization interface for the active triple-discriminant route.

## 8. Consequence for `xi_flow`

The accepted overlap-discriminant taper clue is now narrower. Its first open question — whether full finite-gap overlap admits a discrete summation-by-parts organization that moves the explicit localization defect onto taper differences — has a positive exact answer for three-root blocks. Moreover the bulk coefficient and the full Xi log-gap velocity can both be written as positive-conductance operators on reciprocal gaps.

The clue is **not resolved** because the decisive inequality is still missing. The remaining target is to compare the two Laplacians in (18) strongly enough that a width-growing taper error from (2) is lower order, while using XF-028 to cover the singular collision regime. If such a comparison fails, the correct obstruction should now be expressible as a finite-gap misalignment of `L_lambda h` and `L_w h` that survives a growing buffer, rather than as an unspecified exterior-flux defect.