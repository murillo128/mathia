# XF-029 — triple-discriminant tapers localize through a Cauchy commutator at lattice order

**Status:** `EXACT-DERIVED` + `PERTURBATIVE` + `CANDIDATE-NEW-STRUCTURE` + `STRUCTURAL/BOUNDARY`. XF-027 gives a normalized block discriminant with exact square production and affine cancellation of the exterior field, while XF-028 shows that positive overlap makes every covered collision wall strongly positive at order `1/epsilon^2`. The remaining taper question is whether slowly varying overlap moves localization loss into derivatives of the taper rather than charging the full taper mass.

For three-root blocks the answer is **yes at quadratic order around the arithmetic lattice**. Let `I_j={j,j+1,j+2}`, let `J_j` be the XF-027 normalized discriminant, and set

\[
\mathcal K_a=\sum_j a_j\mathcal J_j,
\qquad
g_j=h(1+\varepsilon u_j),
\qquad
v_j=u_{j+1}-u_j.
\]

Define the positive Cauchy graph Laplacian

\[
(Lf)_i=\sum_{k\ne i}\frac{f_i-f_k}{(i-k)^2}.
\]

Then

\[
\mathcal J_j=-\log2-\frac{3\varepsilon^2}{4}v_j^2+O(\varepsilon^3),
\]

and the lattice linearization of the exact XF-014 gap flow is

\[
u_i'=-\frac{2}{h^2}(Lu)_i,
\qquad
v_i'=-\frac{2}{h^2}(Lv)_i.
\]

Therefore

\[
\mathcal K_a'
=\frac{3\varepsilon^2}{h^2}\langle v,aLv\rangle
+O\!\left(\frac{\varepsilon^3}{h^2}\right).
\tag{1}
\]

The weighted Cauchy form has the exact identity

\[
\begin{aligned}
\langle v,aLv\rangle
={}&\frac12\sum_{i<k}\frac{a_i+a_k}{(i-k)^2}(v_i-v_k)^2\\
&+\frac12\sum_i(La)_i v_i^2.
\end{aligned}
\tag{2}
\]

Thus the desired localization split really occurs in the perturbative model: the first term is nonnegative bulk production, and **all taper localization enters through the Cauchy derivative `La`**. For a smooth width-`M` taper `a_i=A(i/M)`, with fixed compactly supported `C^2` profile `A`, one has

\[
\|La\|_{\ell^\infty}\le \frac{C_A}{M}.
\tag{3}
\]

If `v` is supported in a core where `a_i\ge a_*>0`, then

\[
\langle v,aLv\rangle
\ge
\frac{a_*}{2}\langle v,Lv\rangle
-
\frac{C_A}{2M}\|v\|_2^2.
\tag{4}
\]

For a lattice mode of wavelength `N`, the Cauchy symbol is of order `1/N`, so the taper loss relative to bulk production is `O(N/M)`. This matches the existing Xi scale budget: XF-007 places fixed-time memory at `N(T)\asymp(\log T)^2` gaps, whereas the XF-020 physical buffer `D(T)=R(T)\log T` contains `M(T)\asymp R(T)(\log T)^2` gaps. Hence `N(T)/M(T)=O(1/R(T))=o(1)`.

This is **not** a finite-gap Xi theorem. A nonconstant taper does not make the quadratic form sign-definite automatically, and the full nonlinear derivative of the normalized discriminant has not yet been reorganized into an analogous commutator identity. The result validates the taper clue only at the lattice second variation and identifies the correct localization operator and scale.

## 1. Triple-discriminant Hessian

Translate one three-root block to `0<p<p+q`. For `n=3`, XF-027 has `N=3`; the squared Vandermonde and centered quadratic span are

\[
\Delta^2=p^2q^2(p+q)^2,
\qquad
V=\frac23(p^2+pq+q^2).
\]

Hence

\[
\mathcal J(p,q)
=2\log p+2\log q+2\log(p+q)
-3\log\!\left[\frac23(p^2+pq+q^2)\right].
\tag{5}
\]

Set `p=h(1+epsilon u)` and `q=h(1+epsilon w)`. The common scale cancels. At `(u,w)=(0,0)`, `J=-log 2`; the first variation vanishes; and direct differentiation of (5) gives Hessian

\[
\begin{pmatrix}
-3/2&3/2\\
3/2&-3/2
\end{pmatrix}.
\]

Therefore

\[
\mathcal J(p,q)
=-\log2-\frac{3\varepsilon^2}{4}(w-u)^2+O(\varepsilon^3).
\tag{6}
\]

Summing translated blocks gives

\[
\mathcal K_a
=-(\log2)\sum_j a_j
-\frac{3\varepsilon^2}{4}\sum_j a_jv_j^2
+O(\varepsilon^3).
\tag{7}
\]

Thus the overlapped triple discriminant is, at lattice quadratic order, the negative weighted nearest-neighbor Dirichlet energy of the normalized gap perturbation.

## 2. Cauchy linearization of the exact gap flow

XF-014 gives

\[
g_i'=2\sum_{k\ne i}c_{ik}(g_k-g_i),
\qquad
c_{ik}=\frac1{(x_i-x_k)(x_{i+1}-x_{k+1})}>0.
\tag{8}
\]

At the arithmetic lattice `x_i=ih`, `c_{ik}=1/[h^2(i-k)^2]`. Insert `g_i=h(1+\varepsilon u_i)`. The first variation of the conductance multiplies an already first-order gap difference, so it contributes only at second order. The first variation of (8) is

\[
u_i'=-\frac2{h^2}(Lu)_i.
\tag{9}
\]

Because `L` is translation invariant in the index, the forward difference commutes with it, so

\[
v_i'=-\frac2{h^2}(Lv)_i.
\tag{10}
\]

Differentiating (7) yields (1). For constant `a`, the quadratic production is nonnegative because `L` is positive. The only new issue is multiplication by a localization taper.

## 3. Exact summation by parts

Write `Q_a(v)=<v,aLv>`. Pairing the ordered terms `(i,k)` and `(k,i)` gives

\[
(a_iv_i-a_kv_k)(v_i-v_k)
=
\frac{a_i+a_k}{2}(v_i-v_k)^2
+
\frac{a_i-a_k}{2}(v_i^2-v_k^2).
\tag{11}
\]

After summing over unordered pairs, the second term is itself an exact pairwise integration by parts:

\[
\sum_{i<k}\frac{(a_i-a_k)(v_i^2-v_k^2)}{(i-k)^2}
=
\sum_i(La)_iv_i^2.
\tag{12}
\]

Equations (11)--(12) give (2). The positive term keeps the Cauchy Dirichlet production, while the complete localization defect is encoded by `La`, not by the mass of `a`.

## 4. Width-`M` tapers pay `O(1/M)`

Let `a_i=A(i/M)` with fixed compactly supported `C^2` profile `A`. Pairing the `r` and `-r` terms gives

\[
(La)_i
=
\sum_{r\ge1}\frac{2A(s)-A(s+r/M)-A(s-r/M)}{r^2},
\qquad s=i/M.
\tag{13}
\]

For `r\le M`, Taylor's theorem makes the numerator `O(r^2/M^2)`, so these `O(M)` terms contribute `O(1/M)`. For `r>M`, boundedness of `A` and `\sum_{r>M}r^{-2}=O(1/M)` give the same scale. This proves (3).

For `a_i\ge0`, (2) immediately gives

\[
Q_a(v)\ge-\frac{C_A}{2M}\|v\|_2^2.
\tag{14}
\]

If `v` is supported where `a_i\ge a_*>0`, then every pair with `v_i-v_k\ne0` has at least one endpoint in that core, so `a_i+a_k\ge a_*`. Since

\[
\langle v,Lv\rangle=\sum_{i<k}\frac{(v_i-v_k)^2}{(i-k)^2},
\]

one obtains (4). Widening the taper therefore converts localization into a quantitative buffer-width error; it does not supply exact monotonicity for free.

## 5. Compatibility with the Xi buffer scale

For `v_j=e^{ij\theta}`, the symbol of `L` is

\[
\ell(\theta)
=\sum_{r\ne0}\frac{1-e^{ir\theta}}{r^2}
=\frac{\theta(2\pi-\theta)}2,
\qquad0\le\theta\le2\pi.
\tag{15}
\]

A mode of wavelength `N` has `theta=2pi/N`, so

\[
\ell_N=\frac{2\pi^2}{N}\left(1-\frac1N\right)\asymp\frac1N.
\tag{16}
\]

Thus the localization loss in (4) is smaller than memory-scale Cauchy production by `O(N/M)`. XF-007 gives `N(T)\asymp(\log T)^2`, while XF-020 allows `D(T)=R(T)\log T`, with `R(T)\to\infty`. Since `h_T\sim4\pi/\log T`, the available taper width in gap indices is

\[
M(T)\asymp\frac{D(T)}{h_T}\asymp R(T)(\log T)^2,
\]

and therefore

\[
\frac{N(T)}{M(T)}=O\!\left(\frac1{R(T)}\right)=o(1).
\tag{17}
\]

At lattice order there is no scale mismatch: the super-mesoscopic buffer is parametrically wide enough to make the taper commutator lower order relative to a fixed-time-memory Cauchy mode. This does not assert a spectral cutoff or equivalent estimate for actual Xi gaps.

## 6. Stress test: the commutator has a genuine wrong-sign direction

The second term in (2) has no fixed sign. Take `a_0=1`, all other `a_i=0`, and the finitely supported gap-difference perturbation

\[
v_0=1,
\quad v_1=v_{-1}=2,
\quad v_R=v_{-R}=-\frac52,
\quad R\ge3,
\]

with all other entries zero. Its total sum is zero, so it is the forward difference of a compactly supported bounded gap perturbation. Since only `a_0` is nonzero,

\[
Q_a(v)=v_0(Lv)_0
=
\frac{\pi^2}{3}-4+\frac5{R^2}<0
\qquad(R\ge3).
\tag{18}
\]

Thus localization can reverse the quadratic sign. The content of (3)--(4) is more precise: smooth widening forces the possible negative commutator down to the `1/M` scale. A fixed hard-edge counterexample therefore does not settle the current route; a decisive nonlinear obstruction would need to survive as the buffer grows.

## 7. Boundary with XF-027 and XF-028

XF-027 works at full finite gap and gives each block

\[
\mathcal J_j'=4\|q^{(j)}\|_2^2+4\langle q^{(j)},e^{(j)}\rangle,
\tag{19}
\]

with affine exterior cancellation and cubic distant-root leakage. XF-028 shows that overlap adds positive `8W_k/epsilon^2` production at every covered isolated collision. XF-029 handles the opposite, near-equilibrium regime: the shape Hessian reduces to `v`, the Cauchy gap flow is translation invariant, and overlap produces the exact commutator (2).

These mechanisms are compatible but not yet unified. Near collision the Vandermonde barrier gives the dominant positive sign; near the arithmetic lattice the shape Hessian gives positive Cauchy production with an `O(1/M)` taper loss; between these regimes no theorem currently controls the full finite-gap aggregate flux. The next useful result should either interpolate between those controls while keeping XF-027's far-field cancellation, or exhibit a growing-buffer finite-gap configuration where an order-one negative defect survives.

## 8. Prior-art and novelty boundary

The Cauchy operator, its small-frequency half-Laplacian behavior, and broad nonlocal localization mechanisms are classical and already delimited in `SOURCES.md` through the discrete nonlocal-diffusion and fractional-Laplacian anchors used by XF-007, XF-008, and XF-017. A targeted prior-art audit found the expected broad IMS/commutator landscape for nonlocal Dirichlet forms, but no theorem about this specific sliding normalized-discriminant observable.

No external theorem is load-bearing here. The triple-discriminant Hessian follows directly from XF-027, the lattice flow is established in XF-014/XF-007, and (11)--(12) are elementary pair symmetrization. No general novelty is claimed for the nonlocal localization identity itself, and no `SOURCES.md` change is required.

The durable line-specific content is the exact identification of the **taper derivative seen by the overlapped discriminant at lattice order**: it is the same Cauchy operator that drives gap relaxation, and its width-`M` cost matches the super-mesoscopic Xi buffer budget.

## 9. Consequence for `xi_flow`

The taper clue survives initial research and should remain active with a sharper target. Discrete summation by parts is no longer merely plausible: at the arithmetic-lattice second variation it is exact, and localization loss depends on `La`, not on total taper mass.

The next decisive step is nonlinear. Starting from (19), seek an exact finite-gap analogue of (2), or a coercive inequality whose error is controlled by a nonlocal derivative of the block-start weights. A useful bound should reduce to (4) near equilibrium, preserve the `1/epsilon^2` collision positivity of XF-028, and retain the cubic far-field cancellation of XF-027. If every such nonlinear candidate instead develops an order-one defect independent of `M`, that would be the correct obstruction to persist next.