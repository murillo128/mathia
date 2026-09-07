# XF-088 — Xi endpoint pole needs a logarithmic trapezoid counterterm

**Status:** `EXACT-DERIVED` + `SOURCE-SPECIFIC-ENDPOINT` + `SINGULAR-QUADRATURE` + `BRIDGE-CORRECTION`. XF-087 identifies the exact periodic power-sum heat law with the composite trapezoidal discretization of the canonical one-sided Volterra equation, but deliberately leaves the singular endpoint outside its smooth consistency estimate. XF-052 gives the missing source normal form at `t=0`: below the first prime frequency,

\[
\mathcal Z_0(\xi)=B(\xi)
=-\frac1{4\xi}+\frac74+\frac{\xi}{24}+O(\xi^2).
\]

The simple pole is not harmless under naive trapezoidal sampling. Even after the two periodic half-endpoints are matched to the exact zero mode `P_0=N`, the punctured grid sum for the pole differs from its finite-part Volterra convolution by a term of size `log(1/Delta)` in the **vector field**. On the XF-071 guarded band that defect is not merely nonvanishing; if left unsubtracted across the ordinary `K asymp q log log T` range, its weighted selector resource grows.

There is, however, an exact repair. Let

\[
Y_\alpha(\xi):=\frac{\xi_+^{\alpha-1}}{\Gamma(\alpha)},
\qquad
\tau:=\left.\partial_\alpha Y_\alpha\right|_{\alpha=0},
\]

so that `tau(ξ)=1/ξ` for `ξ>0`. If the open-positive datum is

\[
F(\xi)=-\frac c\xi+b(\xi),
\qquad c>0,
\]

with `b` smooth near zero, then the frequency mesh `Delta` has a distinguished endpoint representative

\[
\boxed{
\widetilde F_{\Delta,N}
=
-c\tau
+
\left(\frac{\Delta N}{2}+c\log\Delta\right)\delta_0
+b_+.
}
\tag{1}
\]

Here `b_+` is any smooth half-line extension agreeing with `b` near zero. The `Delta N/2` term is exactly the continuum image of the two half-weight trapezoid endpoints in XF-087. The new term `c log Delta delta_0` is forced by the pole. With this single logarithmic counterterm, the exact punctured-grid convolution differs from the distributional convolution of `(1)` by a vector-field error

\[
\boxed{
E_m
:=\xi_m\left[
\Delta\left(NF(\xi_m)+\sum_{i=1}^{m-1}F(\xi_i)F(\xi_{m-i})\right)
-
(\widetilde F_{\Delta,N}*\widetilde F_{\Delta,N})(\xi_m)
\right]
=
O_b\!\left(\frac1m+m\Delta^2\right),
}
\tag{2}
\]

uniformly while `xi_m=m Delta` stays in a fixed sufficiently small interval. For the actual Xi endpoint `c=1/4` and `b=B+1/(4xi)` is analytic. At the XF-071/XF-087 scales,

\[
\Delta\asymp q^{-3/2},
\qquad
M=q^2,
\qquad
J\asymp q^{1/4},
\qquad
K\asymp q\log\log T,
\]

the complete guarded defect therefore satisfies

\[
\boxed{
\frac1{4M^2}
\sum_{m=J}^{K}I_m|E_m|^2
=
O\!\left(
q^{-1}(\log\log T)^3
+q^{-3}(\log\log T)^7
\right)
=o(1),
}
\tag{3}
\]

where `I_m` is the exact XF-086 sideband weight. Thus the **known endpoint pole itself is compatible with the guarded periodic Volterra bridge, but only after an explicit logarithmic endpoint renormalization or an equivalent analytic subtraction**.

The negative half is equally important. If one keeps only the natural density endpoint `Delta N/2 delta_0` and omits `c log Delta delta_0`, then already for the pure pole

\[
\boxed{
E_m^{\rm naive}
=
2c^2\log\frac1\Delta+O\!\left(\frac1m\right),
}
\tag{4}
\]

uniformly on any growing grid block with `m Delta ->0`. For Xi, `c=1/4`, so the leading defect is `(1/8) log(1/Delta)`. This rules out a direct appeal to the smooth trapezoidal estimate of XF-087 for the unsubtracted XF-052 carrier. The source-to-grid interface must either subtract the explicit pole/reference before sampling, carry the counterterm in its endpoint normalization, or prove an exactly equivalent renormalized formulation.

## 1. The half-line analytic family fixes the finite-part normalization

XF-053 already uses the standard analytic family `Y_alpha` to organize endpoint-supported and polyhomogeneous distributions. Its convolution law is exact:

\[
Y_\alpha*Y_\beta=Y_{\alpha+\beta}.
\tag{5}
\]

For `xi>0`, expansion of `1/Gamma(alpha)` at zero gives

\[
Y_\alpha(\xi)
=
\frac1\xi
\left[
\alpha+\alpha^2(\log\xi+\gamma)+O(\alpha^3)
\right],
\tag{6}
\]

where `gamma` is Euler's constant. Therefore

\[
\boxed{
\tau(\xi)=\frac1\xi,
\qquad
(\tau*\tau)(\xi)
=
\frac{2(\log\xi+\gamma)}\xi,
\qquad \xi>0.
}
\tag{7}
\]

This is the canonical finite-part convolution associated with the analytic family; no ordinary divergent integral is being assigned a value by hand.

There is a similarly explicit formula for convolution with a regular half-line factor. Let `b` be `C^2` on `[0,xi_0]`, extend it smoothly with compact support on the positive half-line, and write the extension as `b_+`. For `0<xi<xi_0`, expansion of

\[
(Y_\alpha*b_+)(\xi)
=
\frac1{\Gamma(\alpha)}
\int_0^\xi
\eta^{\alpha-1}b(\xi-\eta)\,d\eta
\tag{8}
\]

at `alpha=0` yields

\[
\boxed{
(\tau*b_+)(\xi)
=
b(\xi)(\log\xi+\gamma)
+
\int_0^\xi
\frac{b(\xi-\eta)-b(\xi)}\eta\,d\eta.
}
\tag{9}
\]

The integrand in the last term has a removable singularity at zero. Equations `(7)` and `(9)` isolate every nonintegrable contribution of the simple pole before any grid estimate is attempted.

## 2. The punctured lattice produces harmonic numbers exactly

Put

\[
\xi_i=i\Delta,
\qquad
F_i:=-\frac{c}{i\Delta}+b(i\Delta),
\qquad
x:=\xi_m=m\Delta.
\tag{10}
\]

The pure-pole part of the interior grid convolution is elementary:

\[
\begin{aligned}
\Delta\sum_{i=1}^{m-1}
\frac{c^2}{(i\Delta)((m-i)\Delta)}
&=
\frac{c^2}{\Delta}
\sum_{i=1}^{m-1}\frac1{i(m-i)}\\
&=
\boxed{
\frac{2c^2H_{m-1}}x
},
\end{aligned}
\tag{11}
\]

using

\[
\frac1{i(m-i)}=\frac1m\left(\frac1i+\frac1{m-i}\right).
\tag{12}
\]

The pole-regular cross term has an equally useful exact split. Define

\[
D_{\Delta,m}b
:=
\Delta\sum_{i=1}^{m-1}
\frac{b(x-i\Delta)-b(x)}{i\Delta}.
\tag{13}
\]

Then symmetry under `i -> m-i` gives

\[
\boxed{
-\,c\Delta\sum_{i=1}^{m-1}
\left[
\frac{b(x-i\Delta)}{i\Delta}
+
\frac{b(i\Delta)}{(m-i)\Delta}
\right]
=
-2c\,b(x)H_{m-1}
-2cD_{\Delta,m}b.
}
\tag{14}
\]

Finally put

\[
R_{\Delta,m}b
:=
\Delta\sum_{i=1}^{m-1}
b(i\Delta)b(x-i\Delta).
\tag{15}
\]

The full periodic trapezoid convolution from XF-087 is therefore

\[
\boxed{
\mathcal T_{\Delta,N}(F)_m
=
\Delta N F_m
+
\frac{2c^2H_{m-1}}x
-2cb(x)H_{m-1}
-2cD_{\Delta,m}b
+R_{\Delta,m}b.
}
\tag{16}
\]

Nothing asymptotic has entered so far.

## 3. The logarithmic delta counterterm removes the whole mesh-scale divergence

Let

\[
d_{\Delta,N}:=\frac{\Delta N}{2}+c\log\Delta.
\tag{17}
\]

Using `(7)`--`(9)` and `delta_0*F=F`, the positive restriction of the convolution of `(1)` is

\[
\begin{aligned}
(\widetilde F_{\Delta,N}^{*2})(x)
={}&
\frac{2c^2(\log x+\gamma)}x
-2c\left[
b(x)(\log x+\gamma)+D_mb
\right]\\
&+R_mb
+2d_{\Delta,N}\left(-\frac cx+b(x)\right),
\end{aligned}
\tag{18}
\]

where

\[
D_mb
:=
\int_0^x\frac{b(x-\eta)-b(x)}\eta\,d\eta,
\qquad
R_mb
:=
\int_0^x b(\eta)b(x-\eta)\,d\eta.
\tag{19}
\]

Because `x=m Delta`, the `c log Delta` part of `(17)` changes `log x` into `log m`; the `Delta N/2` part produces exactly `Delta N F_m`. Subtracting `(18)` from `(16)` gives the exact identity

\[
\boxed{
\begin{aligned}
\mathcal T_{\Delta,N}(F)_m
-(\widetilde F_{\Delta,N}^{*2})(x)
={}&
2c\bigl(H_{m-1}-\log m-\gamma\bigr)
\left(\frac cx-b(x)\right)\\
&-2c\bigl(D_{\Delta,m}b-D_mb\bigr)
+\bigl(R_{\Delta,m}b-R_mb\bigr).
\end{aligned}
}
\tag{20}
\]

This formula is the main structural statement. The dangerous `log Delta` term has disappeared exactly; all remaining pieces are ordinary harmonic-number or smooth quadrature errors.

The cancellation is not a convention-free miracle. Replacing `Y'_0` by another fixed finite-part representative changes it only by an endpoint delta and therefore changes the finite constant in `(17)`, but **cannot remove the mesh-dependent coefficient `c log Delta`**. Any fixed endpoint normalization leaves a `log(1/Delta)` mismatch as the mesh is refined.

## 4. The remaining defect is small in the exact guarded resource

The standard harmonic asymptotic gives

\[
H_{m-1}-\log m-\gamma=O(m^{-1}).
\tag{21}
\]

For the difference quotient in `(19)`, write

\[
\frac{b(x-\eta)-b(x)}\eta
=-\int_0^1 b'(x-s\eta)\,ds.
\tag{22}
\]

Its derivative is bounded by `O(||b''||_infinity)`. Elementary rectangle/trapezoid comparison therefore gives, uniformly for `0<x<=xi_0`,

\[
|D_{\Delta,m}b-D_mb|
\ll_b
\Delta,
\qquad
|R_{\Delta,m}b-R_mb|
\ll_b
\Delta.
\tag{23}
\]

Multiplying `(20)` by `x=m Delta` proves

\[
\boxed{
|E_m|
\ll_b
m^{-1}+m\Delta^2.
}
\tag{24}
\]

For the actual endpoint source, XF-052 gives

\[
c=\frac14,
\qquad
b(\xi)=B(\xi)+\frac1{4\xi}
=\frac74+\frac{\xi}{24}+O(\xi^2),
\tag{25}
\]

and `b` is analytic on a fixed neighborhood of the positive endpoint before the first prime atom. Thus the constants in `(23)`--`(24)` are fixed source constants.

Now use the exact XF-086 sideband resource

\[
\mathcal R(E)
=
\frac1{4M^2}\sum_{m=J}^{K}I_m|E_m|^2,
\qquad
I_m\asymp_g m^4.
\tag{26}
\]

From `(24)`,

\[
\mathcal R(E)
\ll_g
\frac1{M^2}
\left(
\sum_{m=J}^{K}m^2
+
\Delta^4\sum_{m=J}^{K}m^6
\right).
\tag{27}
\]

At the XF-071 scales `M=q^2`, `Delta asy q^{-3/2}`, and `K asy q log log T`, this is exactly `(3)`. In particular the known simple pole does not consume the `o(1)` guarded margin once it is renormalized in the mesh-matched way.

The lower guard `J` is not even needed for convergence of `(27)` at the stated upper cutoff; it remains needed elsewhere in XF-071 for the nonlinear hidden-mode quotient. Here it only improves the pointwise bound at the first retained mode.

## 5. Omitting the counterterm fails before any Xi-specific subtlety appears

Take instead the apparently natural endpoint representative

\[
\widetilde F^{\rm naive}_{\Delta,N}
=-c\tau+\frac{\Delta N}{2}\delta_0+b_+,
\tag{28}
\]

which matches the periodic zero mode but includes no logarithmic pole correction. Since

\[
\widetilde F_{\Delta,N}
=
\widetilde F^{\rm naive}_{\Delta,N}
+c\log\Delta\,\delta_0,
\tag{29}
\]

we have on the open positive half-line

\[
\widetilde F_{\Delta,N}^{*2}
=
(\widetilde F^{\rm naive}_{\Delta,N})^{*2}
+2c\log\Delta\,F.
\tag{30}
\]

Combining `(20)`, `(24)`, and `xF(x)=-c+O(x)` gives

\[
\boxed{
\begin{aligned}
E_m^{\rm naive}
&:=x\left[
\mathcal T_{\Delta,N}(F)_m
-(\widetilde F^{\rm naive}_{\Delta,N})^{*2}(x)
\right]\\
&=
-2c^2\log\Delta
+O\!\left(x|\log\Delta|+m^{-1}+m\Delta^2\right).
\end{aligned}
}
\tag{31}
\]

Thus whenever `m -> infinity` and `m Delta ->0`, equation `(4)` follows. In the Xi case, the coefficient is exactly `2c^2=1/8`.

On a macroscopic fraction of the standard visible range `m asy K`, this fixed-in-`m` vector error would carry selector resource of order

\[
\frac{K^5}{M^2}\log^2\!\frac1\Delta,
\tag{32}
\]

which grows on `K asy q log log T`, `M=q^2`. Hence the singularity cannot be dismissed on the grounds that `Delta ->0`; ordinary trapezoidal refinement makes the unrenormalized discrepancy worse.

This is also a useful falsification control for future source dictionaries. Any proposed extraction that effectively samples the raw `-1/(4xi)` carrier and then invokes XF-087 without a pole subtraction must reproduce `(31)`. If it instead reports a smooth `O(Delta^2)` consistency error, the endpoint normalization has been silently lost.

## 6. Interpretation for the Gaussian/reference route

The finding does not say that the periodic node count should literally be changed. Algebraically,

\[
\frac{\Delta N}{2}+c\log\Delta
=
\frac\Delta2
\left(N+\frac{2c}{\Delta}\log\Delta\right),
\tag{33}
\]

so the counterterm can be viewed as a subleading zero-mode correction, but XF-085--XF-086 deliberately use the exact node budget `N=2q^2`. For the live bridge the cleaner interpretation is **reference subtraction**: carry the deterministic endpoint pole/background analytically, and realize/transport only the renormalized guarded fluctuation moments.

That interpretation matches the role of XF-073. Its Gaussian/Appell construction is a relative quotient precisely to avoid treating a large deterministic reference as part of the finite root state. XF-088 adds a quantitative condition to that philosophy: when the quotient is converted into XF-087 grid data, its endpoint normalization must be strong enough to remove the `c log Delta` finite-part mismatch, not merely the leading flat-density term.

The result is endpoint-local and does not depend on root reality, labels, or a collision-free interval. It is a distribution/convolution statement on the same one-sided carrier already made collision-safe in XF-051.

## 7. Stress tests and evidence boundary

**Pure pole.** Set `b=0`. Equation `(20)` reduces exactly to

\[
\mathcal T_{\Delta,N}(F)_m
-(\widetilde F_{\Delta,N}^{*2})(x)
=
\frac{2c^2}{x}
\bigl(H_{m-1}-\log m-\gamma\bigr),
\tag{34}
\]

so the repaired vector defect is `O(1/m)` and the unrepaired one is `(4)`. This isolates the effect from every zeta-specific smooth coefficient.

**Constant regular part.** If `b=b_0`, then `D_{Delta,m}b=D_mb=0`; only the ordinary constant-convolution rectangle error and the same harmonic correction remain. No hidden derivative estimate is needed.

**Dependence on `N`.** The entire defect `(20)` is independent of `N`. This is a stringent check: the `Delta N/2` delta in `(1)` is exactly equivalent to the two half endpoints and must cancel the `Delta N F_m` term algebraically. The logarithmic counterterm is a genuinely different endpoint effect.

**Choice of finite-part scale.** Adding a fixed multiple of `delta_0` to `tau` shifts only the `O(1)` endpoint normalization. It cannot cancel `log Delta` for a refining family. Thus the need for a mesh-dependent logarithmic term is invariant under fixed renormalization conventions.

**Positive heat time.** No uniform `t>0` theorem is claimed here. XF-053 already shows that finite heat jets can develop polyhomogeneous/logarithmic endpoint structure. Equation `(3)` proves the source endpoint `t=0` consistency and identifies the exact pole counterterm, but a complete continuum-to-grid theorem over a fixed heat interval must show that the Gaussian/reference transport carries the corresponding positive-time renormalized background, or subtract that deterministic background before the quadrature comparison. This is now the live dynamic residual.

**Transition mass.** Nothing here proves that `Lambda>0` forces order-one guarded mass. That remains independent exactly as in XF-087 and the accepted source-to-selector clue.

## 8. Prior-art and novelty boundary

Hadamard finite-part distributions, the analytic family `xi_+^{alpha-1}/Gamma(alpha)`, harmonic-number asymptotics, and product-integration methods for endpoint singularities are classical. A targeted audit found the expected finite-part convolution and singular-quadrature literature, including general Hadamard finite-part treatments and product-integration rules. No external theorem is load-bearing here: `(5)`--`(9)` are derived directly from the analytic family already used in XF-053, and the lattice identities `(11)`--`(20)` are elementary.

No novelty is claimed for singular quadrature or finite-part regularization in isolation. The durable Mathia delta is the exact **matching calculation at the XF-087/XF-071 scales**: the Xi coefficient `c=1/4` forces a `c log Delta delta_0` correction beyond the periodic density endpoint; without it the vector-field defect is logarithmically large, while with it the entire known endpoint background has `o(1)` error in the exact guarded selector resource. `SOURCES.md` therefore needs no new load-bearing anchor.

## 9. Consequence for `xi_flow`

XF-087 reduced the dynamic source bridge to continuum Volterra versus periodic trapezoid consistency and correctly marked the endpoint singularity as the hard exception to its smooth estimate. XF-088 resolves the first layer of that exception.

The raw XF-052 source **cannot** be sampled directly into the periodic trapezoid with only `P_0=N`; the simple pole already creates a divergent logarithmic mismatch. But the mismatch is completely explicit and one-dimensional. After subtracting the pole or inserting the equivalent endpoint counterterm `(1)`, the remaining `t=0` convolution defect is `o(1)` in precisely the guarded `X(B)` resource used by XF-086 and transported by XF-071.

The live interface is therefore narrower than “control an arbitrary singular endpoint quadrature.” It must prove that the actual Gaussian/reference Xi extraction implements this pole renormalization coherently over the required positive heat interval, including the weaker logarithmic/polyhomogeneous terms generated from the endpoint. If that succeeds, the known `-1/(4xi)` source singularity itself is no longer a continuum-to-grid obstruction. The separate positive-`Lambda` transition-coercivity gate is unchanged.