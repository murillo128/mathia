# PF-234 — the PF-205 symmetric seam normalizer is quadratically flat-comparable

**Status:** `EXACT-DERIVED + TWO-SIDED-FORM-COMPARISON + POSITIVE/ROUTE-NARROWING`. PF-228's exact flat-corridor calculation obtains the decisive dressed scale `sqrt(w_1w_2)/s` only after normalizing the two corridor faces by the symmetric boundary-energy branches of flat seam strips of halfwidths `w_i`. PF-232/PF-233 then reduce the actual hyperbolic corridor geometry to a small shear perturbation of an exact operator-valued diagonal transfer, but the accepted conformal-rectangle clue correctly leaves one apparent local gap: the **actual PF-205 seam normalizer** had only been inserted through a one-sided trial bound in logarithmic coordinates, where the collar width collapses at the ideal endpoints.

That apparent coercivity gap is a coordinate artifact. In PF-205's intrinsic signed Fermi-area coordinate `x=sinh r` around a decomposition cuff, the actual shifted seam form is already a uniformly translation-invariant thin strip,

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad |x|<w,
\]

and its energy differs from the flat strip energy on the **same** rectangle only by coefficient factors between `(1+w^2)^{-1}` and `1+w^2`. Taking the infimum over extensions with equal data on the two boundary components therefore gives the exact two-sided form comparison

\[
\boxed{
(1+w^2)^{-1}\,M_L\tanh(wM_L)
\ \le_{\rm form}\ 
Q_{L,w}^{\rm hyp,+}
\ \le_{\rm form}\ 
(1+w^2)\,M_L\tanh(wM_L),
}
\]

where

\[
M_L=(1-\partial_s^2)^{1/2}
\]

on the cuff circle of length `L`. Equivalently, on tangential Fourier frequency `xi_k=2pi k/L`, if `q_w^{hyp,+}(xi_k)` is the actual symmetric seam-energy multiplier and `mu_k=sqrt(1+xi_k^2)`, then

\[
\boxed{
\frac{\mu_k\tanh(\mu_k w)}{1+w^2}
\le
q_w^{\rm hyp,+}(\xi_k)
\le
(1+w^2)\mu_k\tanh(\mu_k w).
}
\]

For the canonical PF-205 widths `w_n=kappa d_n=O(P_n^{-1})`, the relative error is therefore `1+O(P_n^{-2})`, not merely `1+O(P_n^{-1})`. The flat symmetric normalizer used in PF-228 is thus a quantitatively faithful model of the **actual** PF seam-energy branch across all tangential frequencies, including the crossover `mu w ~ 1`.

This does **not** yet prove the desired actual dressed corridor envelope. PF-233's variable-width corridor transfer and the seam normalizer are naturally diagonalized in different boundary representations, and the physical one-cusp pant introduces finite arcs, boundary-density identifications, `P/H` projections, and end completion. The surviving local obstruction is therefore no longer lower coercivity of the seam normalizer itself. It is the compatibility of this now-controlled normalizer with PF-233's noncommuting operator `T_a`, followed by off-diagonal control of PF-232's shear and the physical pant completion.

## Claim

Let

\[
Q_{L,w}=(-w,w)\times(\mathbb R/L\mathbb Z),
\qquad L>0,\quad 0<w<1,
\tag{1}
\]

be the centered PF-205 seam strip in signed Fermi-area coordinates. Its exact hyperbolic metric and area form are

\[
\boxed{
g_w=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad d\mu=dx\,ds.
}
\tag{2}
\]

For the positive shifted operator used throughout the seam construction, write the quadratic form

\[
\mathfrak e_w[u]
=
\int_{Q_{L,w}}
\left[
(1+x^2)|u_x|^2
+\frac{|u_s|^2}{1+x^2}
+|u|^2
\right]dx\,ds.
\tag{3}
\]

On the same coordinate rectangle define the flat shifted form

\[
\mathfrak e_w^0[u]
=
\int_{Q_{L,w}}
\left(
|u_x|^2+|u_s|^2+|u|^2
\right)dx\,ds.
\tag{4}
\]

For a boundary profile `f` on `R/LZ`, define the **symmetric branch** of each two-boundary energy by prescribing the same trace on both sides and dividing the minimized total energy by two:

\[
q_{L,w}^{\rm hyp,+}[f]
:=\frac12
\inf_{\substack{u(-w,\cdot)=f\\u(w,\cdot)=f}}
\mathfrak e_w[u],
\tag{5}
\]

\[
q_{L,w}^{0,+}[f]
:=\frac12
\inf_{\substack{u(-w,\cdot)=f\\u(w,\cdot)=f}}
\mathfrak e_w^0[u].
\tag{6}
\]

Let `Q_{L,w}^{hyp,+}` and `Q_{L,w}^{0,+}` denote the associated positive boundary forms/operators in the marked cuff coordinate `s`. Then:

1. for every admissible `u`,
   \[
   \boxed{
   (1+w^2)^{-1}\mathfrak e_w^0[u]
   \le
   \mathfrak e_w[u]
   \le
   (1+w^2)\mathfrak e_w^0[u];
   }
   \tag{7}
   \]
2. hence, by minimization at fixed trace,
   \[
   \boxed{
   (1+w^2)^{-1}Q_{L,w}^{0,+}
   \le_{\rm form}
   Q_{L,w}^{\rm hyp,+}
   \le_{\rm form}
   (1+w^2)Q_{L,w}^{0,+};
   }
   \tag{8}
   \]
3. if
   \[
   M_L=(1-\partial_s^2)^{1/2},
   \tag{9}
   \]
   then the flat symmetric branch is exactly
   \[
   \boxed{
   Q_{L,w}^{0,+}=M_L\tanh(wM_L);
   }
   \tag{10}
   \]
4. because the hyperbolic coefficients in (3) are independent of `s`, the actual symmetric branch also commutes with cuff translations and is diagonal in the same Fourier basis. Writing
   \[
   \xi_k=\frac{2\pi k}{L},
   \qquad
   \mu_k=\sqrt{1+\xi_k^2},
   \tag{11}
   \]
   gives
   \[
   \boxed{
   \frac{\mu_k\tanh(\mu_kw)}{1+w^2}
   \le
   q_w^{\rm hyp,+}(\xi_k)
   \le
   (1+w^2)\mu_k\tanh(\mu_kw)
   }
   \tag{12}
   \]
   for every `k`;
5. in particular, with absolute constants independent of `L,w,k`,
   \[
   \boxed{
   q_w^{\rm hyp,+}(\xi_k)
   \asymp
   \mu_k\min\{\mu_kw,1\}
   =\min\{w\mu_k^2,\mu_k\},
   }
   \tag{13}
   \]
   uniformly for `0<w<=w_0<1`;
6. on the canonical PF-205 tail,
   \[
   w_n=\kappa d_n=O(P_n^{-1}),
   \tag{14}
   \]
   so
   \[
   \boxed{
   Q_{L_n,w_n}^{\rm hyp,+}
   =Q_{L_n,w_n}^{0,+}
   \quad\text{up to two-sided relative form factors }1+O(P_n^{-2}).
   }
   \tag{15}
   \]

If the boundary operator is instead represented in physical hypercycle arclength, then at `x=+-w`

\[
d\sigma=\sqrt{1+w^2}\,ds.
\tag{16}
\]

This introduces only the constant factor `sqrt(1+w^2)=1+O(w^2)` in the representation of the boundary form. Thus the two-sided comparison and its canonical `O(P_n^{-2})` relative accuracy survive the physical boundary-density conversion for the isolated seam strip.

## 1. The two-sided comparison is pointwise in the exact PF metric

Equation (2) is PF-205's universal signed Fermi-area chart, and PF-212 already uses the separated mode energy corresponding to (3). On `|x|<=w`,

\[
1\le1+x^2\le1+w^2,
\tag{17}
\]

and

\[
(1+w^2)^{-1}
\le
(1+x^2)^{-1}
\le1.
\tag{18}
\]

The mass coefficient in (3) is exactly one. Therefore each of the three nonnegative terms in (3) is bounded above by `(1+w^2)` times its flat counterpart and below by `(1+w^2)^{-1}` times its flat counterpart. Integration proves (7).

Nothing singular occurs at the ends of a lift of the cuff: the coordinate `s` is intrinsic arclength along the central geodesic and ranges over `R` in the universal cover or `R/LZ` on the actual closed cuff. The vanishing width seen when the same collar is drawn in PF-231's logarithmic `(x,theta)` rectangle is therefore not a degeneration of the intrinsic collar geometry. It is compression of the infinite `s`-axis into the finite interval `0<theta<pi`.

Because (7) holds for **every** extension with a prescribed common trace, taking the infimum over the same affine trace class proves (8). This is the missing lower-bound step that cannot be obtained by reversing the one-sided constant-in-logarithmic-`x` trial inequality from the conformal clue.

## 2. The flat symmetric branch is exactly the PF-228 normalizer

Expand

\[
f(s)=\sum_{k\in\mathbb Z}\widehat f_k e^{i\xi_ks}.
\tag{19}
\]

For the flat form and one Fourier mode, the minimizing extension solves

\[
-v''+\mu_k^2v=0,
\qquad
v(-w)=v(w)=\widehat f_k.
\tag{20}
\]

The even solution is

\[
v_k(x)
=\widehat f_k\frac{\cosh(\mu_kx)}{\cosh(\mu_kw)}.
\tag{21}
\]

Its total two-boundary energy is

\[
2\mu_k\tanh(\mu_kw)|\widehat f_k|^2.
\tag{22}
\]

The factor `1/2` in (6) therefore gives

\[
q_{L,w}^{0,+}[f]
=\sum_k
\mu_k\tanh(\mu_kw)|\widehat f_k|^2,
\tag{23}
\]

which is exactly (10). This is the symmetric flat seam branch `q_i=mu tanh(mu w_i)` used in PF-228's explicit corridor inversion.

The actual PF metric is also independent of `s`, so its minimizing problem preserves each Fourier mode. Applying (8) to a single Fourier datum gives (12) directly. Thus no mode mixing is hidden inside the actual seam normalizer itself.

The elementary bounds `tanh y asymp min(y,1)` for `y>=0` then give (13). The actual hyperbolic seam has the same low-frequency `wM_L^2` behavior, the same high-frequency first-order `M_L` behavior, and the same transition at tangential scale `1/w` as the flat reference.

## 3. Canonical PF widths make the flat replacement quadratically accurate

PF-205 fixes

\[
w_n=\kappa d_n,
\qquad
d_n=P_n^{-1}(1+o(1)),
\tag{24}
\]

with fixed sufficiently small `kappa`. Therefore

\[
w_n^2=O(P_n^{-2}).
\tag{25}
\]

Substituting into (8) gives

\[
(1-O(P_n^{-2}))Q_{L_n,w_n}^{0,+}
\le_{\rm form}
Q_{L_n,w_n}^{\rm hyp,+}
\le_{\rm form}
(1+O(P_n^{-2}))Q_{L_n,w_n}^{0,+},
\tag{26}
\]

after enlarging the finite head. This error is smaller than PF-232's reciprocal-prime shear scale `O(P_n^{-1})` and much smaller than the order-one seam-to-corridor width ratio that PF-228 is designed to exploit.

In particular, the canonical seam normalizer cannot lose a factor comparable to `s_n/w_n`, create an extra inverse width, or erase the low-band scale merely because the logarithmic graph width tends to zero at `theta=0,pi`. Any such loss would contradict the intrinsic form comparison (26).

A useful operator consequence is available without assuming commutation with later corridor operators. From (8), on the positive boundary-energy space,

\[
(Q_{L,w}^{\rm hyp,+})^{-1}
\le
(1+w^2)(Q_{L,w}^{0,+})^{-1}
\tag{27}
\]

in form order, with the reverse lower bound as well. Equivalently the comparison maps

\[
(Q_{L,w}^{\rm hyp,+})^{-1/2}(Q_{L,w}^{0,+})^{1/2}
\quad\text{and}\quad
(Q_{L,w}^{0,+})^{-1/2}(Q_{L,w}^{\rm hyp,+})^{1/2}
\tag{28}
\]

extend boundedly with norms `1+O(w^2)`. This permits bounded-ideal insertion of the actual seam normalization once a corridor block is expressed on the **same** trace space. It does not, however, identify that trace-space conversion for PF-233 or make the corridor and seam spectral variables commute.

## 4. Relation to the logarithmic-coordinate endpoint singularity

PF-231 represents a complete corridor between ultraparallel axes on `(0,s)x(0,pi)`. In that chart the inward hypercycle at distance `rho=arsinh w` is

\[
x=f_\rho(\theta)
=\operatorname{arsinh}(w\sin\theta),
\tag{29}
\]

so its displayed logarithmic width vanishes as `theta` approaches `0` or `pi`. Its physical arclength density is correspondingly singular. These two facts describe the same coordinate compression of an intrinsically complete hypercycle.

The PF-205 strip instead retains the geodesic Fermi coordinate `s`, in which the two seam boundaries are simply `x=+-w`, all coefficients are independent of `s`, and the two-sided coercivity (7) is global. Pulling the resulting boundary energy through the exact hypercycle reparameterization cannot destroy positivity or coercivity; it only changes the boundary representation.

This removes a specific false fork in the accepted conformal clue: there is no need to prove a lower bound by treating `f_rho(theta)` as a positive-width function on `(0,pi)`. The correct lower bound is already intrinsic before the endpoint-compacting coordinate change.

What remains nontrivial is that PF-233's corridor product structure is most transparent in the logarithmic `theta` representation, whereas (10)--(12) are most transparent in the intrinsic cuff coordinate `s`. The exact reparameterization between those descriptions is therefore now the place where noncommutation must be paid, not a missing lower bound for the seam form.

## 5. Prior-art and novelty audit

Fermi coordinates around a hyperbolic geodesic and the metric `dr^2+cosh^2(r)ds^2` are classical. Hyperbolic cylinders in exactly this form also appear, for example, in C. Guillarmou and L. Guillopé, *The determinant of the Dirichlet-to-Neumann map for surfaces with boundary*, International Mathematics Research Notices (2007), article `rnm099`, DOI `10.1093/imrn/rnm099`. General comparison of Dirichlet-to-Neumann operators with first-order boundary operators is standard spectral geometry; A. Girouard, M. Karpukhin, M. Levitin, and I. Polterovich, *The Dirichlet-to-Neumann map, the boundary Laplacian, and Hörmander's rediscovered manuscript*, Journal of Spectral Theory 12 (2022), 195--225, DOI `10.4171/JST/399`, is representative modern context.

No novelty is claimed for Fermi coordinates, separation in a translation-invariant strip, the scalar identity `mu tanh(mu w)` for equal boundary data on a flat strip, variational form comparison, or general DtN pseudodifferential behavior. A structure-directed literature search did not identify a source whose theorem is the PF-specific statement needed here: the exact PF-205 **signed Fermi-area** seam form is two-sided comparable on the same width `w_n` to the specific flat symmetric normalizer used in PF-228, with relative error `1+O(w_n^2)=1+O(P_n^{-2})` uniformly over all tangential frequencies.

The proof of (7)--(15) is self-contained from the persisted PF-205/PF-212 metric formula and elementary one-dimensional minimization. The external literature is methodological and novelty context, not a theorem dependency.

## 6. Falsification and boundary checks

1. The result concerns the **symmetric/equal-value branch** of the two-sided PF-205 seam strip, because that is the branch used in PF-228's `w/s` calibration. It does not claim that every two-boundary matrix entry equals its flat counterpart.
2. Equation (8) is a form comparison, not an equality of actual and flat DtN operators. The actual Fourier multiplier need not have a closed elementary formula; only the sharp-enough two-sided envelope (12) is asserted.
3. Translation invariance and Fourier diagonalization are statements in the intrinsic marked cuff coordinate `s`. After reparameterization to PF-233's logarithmic `theta` trace space, the normalizer need not commute with `A`, `T_a`, multiplication by `a`, or the corridor cross block.
4. The physical boundary measure at `x=+-w` differs from `ds` by the constant `sqrt(1+w^2)` for the isolated seam strip. This is harmless here, but the later corridor-to-pant boundary identification is not reduced to this constant and still requires explicit control.
5. The complete Fermi strip is the local seam normalizer. The actual one-cusp pant corridor has finite cuff arcs and an end completion; this finding does not identify those with the complete-axis PF-233 model.
6. PF-232 controls full positive-form shear, not the off-diagonal DtN block after normalization. This finding does not upgrade that form estimate into the required cross-block perturbation theorem.
7. Nothing here proves the final `sqrt(w_nw_{n+1})/s_n` dressed estimate, the physical `P/H` projected estimate, PF-222 weak-`S_1` reassembly, wave-operator equivalence, determinant/resonance control, prime/clone separation, or an RH implication.

## Consequences for the research line

The accepted conformal-rectangle clue no longer needs a two-sided coercivity theorem for the **seam normalizer itself**: PF-234 supplies it intrinsically and, on canonical widths, with quadratic relative accuracy. The flat symmetric normalizer that creates PF-228's `w/s` suppression is not an artificial spectral scale; it is the correct all-frequency model of the actual PF-205 seam branch up to `1+O(P_n^{-2})`.

The local route is therefore narrower. Combine the exact boundary reparameterization with PF-233's operator-valued corridor transfer and determine whether the resulting noncommuting normalized cross block still has the PF-228 low-band amplitude and high-mode envelope. Then control PF-232's small shear at the **cross-block** level and account for physical `P/H` projections plus finite-pant completion. A failure must now occur in those compatibility/completion operations, not in loss of seam-normalizer coercivity caused by logarithmic endpoint degeneration.