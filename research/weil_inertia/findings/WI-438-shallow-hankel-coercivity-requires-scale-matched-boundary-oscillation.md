# WI-438 — shallow Hankel coercivity requires scale-matched boundary oscillation, not merely noncompactness

Status: `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + DECISIVE-BARRIER + STRUCTURAL-REDIRECTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parent: `WI-437`

## Claim

`WI-437` proves that compact cross-channel operators are asymptotically blind to the normalized shallow Kunik defect packets, so any viable Hankel escape must contain a noncompact component. Noncompactness is nevertheless far from sufficient. For a classical bounded-symbol Hankel operator, the relevant local quantity is the **Poisson/Garsia mean oscillation of the symbol at the defect scale**.

Let

\[
H_\varphi=P_-M_\varphi|_{\mathcal H_+},
\qquad \varphi\in L^\infty(\mathbb R),
\tag{1}
\]

and let `k_{r,gamma}` be the normalized upper-half-plane Hardy kernel centered at `gamma` and height `r`, normalized so that

\[
|k_{r,\gamma}(t)|^2
=P_r(t-\gamma)
:=\frac1\pi\frac{r}{r^2+(t-\gamma)^2}.
\tag{2}
\]

Define the Poisson variance

\[
\mathcal V_\varphi(r,\gamma)
:=
(P_r*|\varphi|^2)(\gamma)
-
|(P_r*\varphi)(\gamma)|^2.
\tag{3}
\]

Then

\[
\boxed{
\|H_\varphi k_{r,\gamma}\|_2^2
\le \mathcal V_\varphi(r,\gamma).
}
\tag{4}
\]

Consequently, at every common Lebesgue point of `varphi` and `|varphi|^2`,

\[
\boxed{
\|H_\varphi k_{r,\gamma}\|_2\longrightarrow0
\qquad(r\downarrow0).
}
\tag{5}
\]

Such points form a full-measure set. Therefore **no single fixed bounded Hankel symbol can provide an ordinate-uniform positive shallow-defect quantum**: there is no `c>0` and `r_0>0` for which

\[
\|H_\varphi k_{r,\gamma}\|_2\ge c
\tag{6}
\]

holds for every `gamma in R` and every `0<r<r_0`. The same conclusion holds for every finite fixed portfolio of bounded symbols, since the intersection of their Lebesgue-point sets still has full measure.

There is a stronger uniform statement for locally regular symbols. If `varphi` is bounded and uniformly continuous, then

\[
\boxed{
\sup_{\gamma\in\mathbb R}
\|H_\varphi k_{r,\gamma}\|_2
\longrightarrow0
\qquad(r\downarrow0),
}
\tag{7}
\]

whether or not `H_varphi` is compact. More generally, the convergence is uniform over every uniformly bounded, equicontinuous family of symbols. Thus a source-derived family cannot evade the shallow barrier merely by leaving Hartman's compact class; it must retain order-one **local oscillation at spatial scale comparable to the horizontal defect depth**.

This distinction is strict. For every fixed `omega>0`,

\[
\varphi_\omega(t)=e^{-i\omega t}
\tag{8}
\]

produces a noncompact Hankel operator of norm one, but on the exact normalized shallow Hardy packet

\[
\boxed{
\|H_{\varphi_\omega}k_{r,\gamma}\|_2^2
=1-e^{-2\omega r}
\longrightarrow0
}
\tag{9}
\]

uniformly in `gamma`. Hence global noncompactness can come entirely from translation behavior at infinity while remaining useless at arbitrarily small defect scales.

For the one-zero Kunik block of `WI-437`, with

\[
r_-=(1-\theta)d,
\qquad
r_+=(1+\theta)d,
\qquad 0<\theta<1,
\tag{10}
\]

the normalized positive Hardy channel is exactly `k_{r_-,gamma}` up to the fixed Fourier normalization/unimodular identification. Therefore, if `g_+=G_+/||G_+||_2` and `g_-=G_-/||G_-||_2`,

\[
\boxed{
|\langle H_\varphi g_+,g_-\rangle|
\le
\mathcal V_\varphi((1-\theta)d,\gamma)^{1/2}.
}
\tag{11}
\]

At every Lebesgue point this tends to zero as `d downarrow 0`; for bounded uniformly continuous `varphi` it tends to zero uniformly in `gamma`. By contrast, the canonical Kunik pairing from `WI-437` remains

\[
\frac{\int G_+G_-}
{\|G_+\|_2\|G_-\|_2}
=\sqrt{1-\theta^2}.
\tag{12}
\]

So a fixed bounded Hankel correction with vanishing small-scale mean oscillation is lower order relative to the canonical `m^2/d` defect energy even when the Hankel operator itself is noncompact.

The correct post-`WI-437` gate is therefore not merely the Calkin class. A viable bounded-symbol Hankel mechanism must establish, independently from the off-line divisor, a lower bound on `mathcal V_varphi(r,gamma)` at the actual defect ordinate with `r asymp d`. A fixed uniformly continuous symbol cannot do this. A scale-dependent family can evade the theorem only by losing equicontinuity at the same scale; the exact model `varphi_d(t)=e^{-it/d}` has order-one variance at `r asymp d`, making explicit the required `1/d` frequency scale. Whether zeta's source side supplies and controls such scale-matched roughness without importing the target zero is the remaining arithmetic question.

## 1. Reproducing-kernel estimate

Because `k_{r,gamma}` lies in `H_+`,

\[
H_\varphi k_{r,\gamma}
=P_-(\varphi k_{r,\gamma}).
\tag{13}
\]

Orthogonal projection gives

\[
\|H_\varphi k_{r,\gamma}\|_2^2
=
\|\varphi k_{r,\gamma}\|_2^2
-
\|P_+(\varphi k_{r,\gamma})\|_2^2.
\tag{14}
\]

The first term is exactly the Poisson average

\[
\|\varphi k_{r,\gamma}\|_2^2
=(P_r*|\varphi|^2)(\gamma).
\tag{15}
\]

Since `k_{r,gamma}` is a unit vector in `H_+`,

\[
\begin{aligned}
\|P_+(\varphi k_{r,\gamma})\|_2^2
&\ge
|\langle P_+(\varphi k_{r,\gamma}),k_{r,\gamma}\rangle|^2\\
&=
|\langle \varphi k_{r,\gamma},k_{r,\gamma}\rangle|^2\\
&=
|(P_r*\varphi)(\gamma)|^2.
\end{aligned}
\tag{16}
\]

Subtracting proves (4). The right side is the standard Poisson/Garsia variance used in Hardy-space BMO theory; no zeta-specific input enters this inequality.

If `gamma` is a common Lebesgue point of `varphi` and `|varphi|^2`, the Poisson approximate identity gives

\[
(P_r*\varphi)(\gamma)\to\varphi(\gamma),
\qquad
(P_r*|\varphi|^2)(\gamma)\to|\varphi(\gamma)|^2,
\tag{17}
\]

so `mathcal V_varphi(r,gamma)->0`, proving (5). Since `varphi in L^infty`, both functions are locally integrable and the common Lebesgue-point set has full measure.

This already disproves an ordinate-uniform lower quantum for every fixed `L^infty` symbol. It does **not** prove that a particular countable set of zeta ordinates must contain a Lebesgue point of a source symbol: a null exceptional set can contain an arbitrary prescribed countable set. The arithmetic burden is therefore precise rather than eliminated. To use a fixed bounded symbol at every possible off-line zero, one must prove from the source that the relevant zeta ordinates land in persistent local-oscillation points, or else use a mechanism outside this fixed bounded-symbol class.

## 2. Uniform small-scale blindness for uniformly continuous symbols

The uniform statement can be proved without invoking any abstract VMO theorem. Let

\[
M=\|\varphi\|_\infty,
\qquad
\omega_\varphi(\delta)
:=
\sup_{|x-y|\le\delta}|\varphi(x)-\varphi(y)|.
\tag{18}
\]

Constants have zero Hankel part, so

\[
\|H_\varphi k_{r,\gamma}\|_2^2
\le
\int_{\mathbb R}
P_r(t-\gamma)
|\varphi(t)-\varphi(\gamma)|^2dt.
\tag{19}
\]

Split at `|t-gamma|=delta`. The inner region contributes at most `omega_varphi(delta)^2`; on the outer region the squared difference is at most `4M^2`. Since

\[
\int_{|x|>\delta}P_r(x)dx
=
\frac2\pi\arctan\!\frac r\delta
\le
\frac{2r}{\pi\delta},
\tag{20}
\]

we obtain the explicit uniform bound

\[
\boxed{
\sup_\gamma
\|H_\varphi k_{r,\gamma}\|_2^2
\le
\omega_\varphi(\delta)^2
+
\frac{8M^2r}{\pi\delta}.
}
\tag{21}
\]

Taking, for example, `delta=sqrt(r)` proves (7). If a family `F` satisfies

\[
\sup_{\varphi\in F}\|\varphi\|_\infty<\infty
\tag{22}
\]

and has a common modulus of continuity tending to zero, the same estimate is uniform over `F`. Thus even a non-precompact family of noncompact Hankel operators is harmless at shallow scale if its symbols remain uniformly equicontinuous there. The necessary escape is loss of **local** regularity at the defect scale, not merely loss of operator compactness or norm precompactness.

## 3. An exact noncompact but shallow-blind witness

Take `varphi_omega(t)=exp(-i omega t)` with `omega>0`. In the Paley--Wiener realization `H_+ ~= L^2(0,infty)`, multiplication by `varphi_omega` shifts Fourier frequency down by `omega`. The Hankel projection keeps exactly the input frequencies in `(0,omega)`. Hence, on the infinite-dimensional subspace `L^2(0,omega)`, `H_{varphi_omega}` acts isometrically onto `L^2(-omega,0)` after translation. Therefore

\[
\|H_{\varphi_\omega}\|=1
\tag{23}
\]

and the operator is noncompact.

For the normalized kernel profile used in `WI-437`,

\[
u_{r,\gamma}(\xi)
=\sqrt{2r}\,e^{-r\xi}e^{-i\gamma\xi},
\qquad \xi>0,
\tag{24}
\]

we obtain exactly

\[
\begin{aligned}
\|H_{\varphi_\omega}u_{r,\gamma}\|_2^2
&=
\int_0^\omega 2r e^{-2r\xi}d\xi\\
&=1-e^{-2\omega r}.
\end{aligned}
\tag{25}
\]

This is independent of `gamma` and tends to zero linearly in `r`. The Garsia bound is sharp here: since

\[
P_r*\varphi_\omega
=e^{-\omega r}\varphi_\omega,
\qquad
P_r*|\varphi_\omega|^2=1,
\tag{26}
\]

we have

\[
\mathcal V_{\varphi_\omega}(r,\gamma)
=1-e^{-2\omega r},
\tag{27}
\]

exactly matching (25).

This example kills the tempting converse of `WI-437`: `H_varphi` can be maximally noncompact in the elementary partial-isometry sense while its normalized shallow-defect response still vanishes uniformly.

It also exposes the scale needed to escape. If instead `omega=omega(r)` varies with the depth, then

\[
\|H_{e^{-i\omega(r)t}}k_{r,\gamma}\|_2^2
=1-e^{-2r\omega(r)}.
\tag{28}
\]

An order-one response requires `r omega(r)` to stay bounded away from zero. At the Kunik scale `r=(1-theta)d`, the model frequency must therefore reach order `1/d`. This is an exact model calculation, not a general Fourier-support theorem for arbitrary symbols, but it identifies the natural scale that any source construction must confront.

## 4. Consequence for the live Kunik/Hardy route

For the one-defect Kunik block, `WI-437` gives the exact Fourier profiles

\[
\widehat G_+(\xi)
=-2\pi m e^{-r_-\xi}e^{-i\gamma\xi},
\qquad
\widehat G_-(-\xi)
=-2\pi m e^{-r_+\xi}e^{+i\gamma\xi}.
\tag{29}
\]

After normalization, the positive profile is exactly (24) with `r=r_-`; the negative profile is another unit Hardy kernel after the fixed reflection. Therefore Cauchy--Schwarz and (4) give (11).

Using `WI-437`'s exact product of channel norms,

\[
\|G_+\|_2\|G_-\|_2
=
\frac{\pi m^2}{d\sqrt{1-\theta^2}},
\tag{30}
\]

we also get the unnormalized estimate

\[
|\langle H_\varphi G_+,G_-\rangle|
\le
\frac{\pi m^2}{d\sqrt{1-\theta^2}}
\mathcal V_\varphi((1-\theta)d,\gamma)^{1/2}.
\tag{31}
\]

Thus whenever the Poisson variance tends to zero, the Hankel correction is `o(m^2/d)` relative to the canonical reciprocal-depth defect energy. For bounded uniformly continuous symbols this is uniform in the ordinate, so it cannot supply the missing source-side coercive quantum against an arbitrarily shallow defect.

The surviving bounded-symbol route must therefore supply **scale-matched nonvanishing Poisson variance** at the actual zero ordinate. A fixed finite Fourier combination, a fixed Bohr almost-periodic symbol, or any other bounded uniformly continuous symbol is excluded from a uniform first-defect detector by (21), even if its Hankel operator is noncompact because of behavior at infinity. A parameter family remains possible only if its small-scale modulus deteriorates with `d`; then the source side must control that deterioration independently of the unknown divisor.

## 5. Prior art and novelty audit

No novelty or priority claim is made for the harmonic-analysis ingredients.

- Donald Sarason, **Functions of vanishing mean oscillation**, *Transactions of the American Mathematical Society* **207** (1975), 391--405, DOI `10.1090/S0002-9947-1975-0377518-3`, is classical prior art for vanishing mean oscillation and its relation to `H^infty+C`. It supports the distinction between small local oscillation and global compact-symbol structure.
- Vladimir V. Peller, **Hankel Operators and Their Applications**, Springer Monographs in Mathematics (2003), DOI `10.1007/978-0-387-21681-2`, is a standard reference for Hardy-space Hankel operators, BMO/VMO connections, reproducing kernels, and compactness theory.
- Ana Čolović, **Reproducing Kernel Thesis of Hankel Operators on Weighted Hardy Spaces**, *Integral Equations and Operator Theory* **97** (2025), article 10, DOI `10.1007/s00020-025-02795-w`, records the modern reproducing-kernel/Garsia-norm framework and the equivalence of the corresponding testing norm with BMO in the classical setting.
- Konstantin M. Dyakonov, **Extremal problems in BMO and VMO involving the Garsia norm**, arXiv:2404.05565 (2024), uses the standard Poisson variance `P(|f|^2)-|Pf|^2` as the Garsia quantity. The present proof needs only the elementary estimate (14)--(16).
- `WI-437` already anchors Hartman's compact-Hankel theorem and proves compact blindness on the exact Kunik packets. The present result is not another compactness theorem: the explicit symbol (8) is noncompact and still uniformly shallow-blind.

A targeted search around Hankel reproducing-kernel tests, Garsia mean oscillation, BMO/VMO and compactness found the classical local-oscillation machinery above. Repository-local frontier checks against `WI-437` and the earlier compact-correction barriers found no stored statement that a **noncompact** bounded Hankel operator can nevertheless be uniformly blind on the Kunik shallow family, nor the exact exponential witness (25) in this role. Those observations are recorded only as an audit outcome, not as a claim of mathematical priority.

## 6. Boundary and falsification

This finding narrows one live mechanism; it does not rule out all mixed-frequency bootstraps.

1. A general noncompact cross-channel operator need not be a bounded-symbol Hankel operator and is not covered by (4).
2. A fixed `L^infty` symbol may have a null exceptional set of persistent local oscillation, and the set of zeta ordinates is itself countable. The almost-everywhere statement alone therefore does not exclude a zeta-specific coincidence; an actual proof must control the symbol at those ordinates.
3. A scale-dependent family whose oscillation frequency grows like `1/d` or faster can retain order-one response. Such a family is useful only if the source side controls it uniformly without choosing it from the unknown off-line zero.
4. Unbounded or singular multipliers lie outside the present bounded-symbol estimate as an operator-class statement and need their own domain/closability analysis.
5. The theorem gives no new simple-zero proportion and no RH implication by itself. Its value is a decisive barrier: after `WI-437`, **noncompactness is only a global necessary condition; the actual shallow-defect gate is source-controlled local mean oscillation at scale `d`**.

Accordingly, the next serious Hankel candidate should be tested first for its Poisson variance on the exact packet scale. If that variance vanishes, Calkin noncompactness does not rescue it. If it remains order one, the load-bearing question is whether that roughness is genuinely source-derived and available independently of the defect divisor.