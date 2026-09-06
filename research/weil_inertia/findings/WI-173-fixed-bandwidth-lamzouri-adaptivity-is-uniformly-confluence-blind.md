# WI-173 — fixed-bandwidth Lamzouri adaptivity is uniformly confluence-blind

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + SUPPORT-BARRIER`. WI-140 shows that, for any fixed Lamzouri window, an isolated simple off-real conjugate pair can confluence to a real double while the complete finite deficit tends to zero quadratically. WI-142 strengthens this to arbitrary **preassigned** continuous detector families by choosing the horizontal depth below their continuity scale. A remaining quantifier loophole is to choose the Lamzouri test window *after seeing the off-line depth*, perhaps concentrating the window near its support edge so that its complex continuation amplifies that particular pair.

That loophole is also closed at every fixed Fourier bandwidth. Let `eta` be any real even Lamzouri window with

\[
\operatorname{supp}\eta\subset(-\lambda,\lambda),
\qquad
\int_{\mathbb R}\eta(u)^2\,du=1,
\]

and let `Delta_eta(y)` be the complete Proposition 2.1 deficit for the isolated simple conjugate pair `x+iy,x-iy`, `y>0`. Then

\[
\boxed{
\sup_{\eta}\Delta_\eta(y)
=2\sinh^2(4\pi\lambda y).
}
\tag{A}
\]

The supremum is sharp and is approached by even windows whose squared mass concentrates near the two support edges. Equivalently, if

\[
\sigma:=2\lambda
\]

is the Fourier-support radius of the pair-correlation profile `eta^2 * eta^2`, then

\[
\boxed{
\sup_{\eta}\Delta_\eta(y)
=2\sinh^2(2\pi\sigma y)
=8\pi^2\sigma^2y^2+O_\sigma(y^4).
}
\tag{B}
\]

Thus **even post-hoc optimization over the entire admissible window class cannot produce a positive count charge for a pair whose normalized horizontal depth tends to zero while the bandwidth stays bounded**. In zeta variables,

\[
y=\left|\beta-\frac12\right|\frac{\log T}{2\pi},
\]

so every bandwidth-`sigma` Lamzouri square-kernel deficit obeys

\[
\boxed{
\Delta_\eta
\le
2\sinh^2\!\left(\sigma\left|\beta-\frac12\right|\log T\right).
}
\tag{C}
\]

To force even a fixed local charge `c>0` from this isolated-pair mechanism, a necessary condition is

\[
\boxed{
\sigma\left|\beta-\frac12\right|\log T
\ge
\operatorname{arsinh}\sqrt{\frac c2}.
}
\tag{D}
\]

Consequently a hypothetical sequence of off-line zeros with `|beta-1/2| log T -> 0` defeats **every bounded-support adaptive Lamzouri window**, not only every fixed or preassigned one. The current unconditional arithmetic interface has `sigma<=1`; modest extension to any other fixed support still does not supply a uniform per-exception charge. A scalar-window route to an individual-zero RH conclusion therefore needs either support growing inversely with the horizontal depth, or genuinely new zeta-specific interaction/anti-confluence information. No unconditional simple-critical-zero proportion changes in this finding.

## 1. Primary-source interface and exact one-pair formula

The primary source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), Proposition 2.1 and Section 3. Proposition 2.1 takes a real even `eta` supported in `(-lambda,lambda)`, normalized by

\[
\widehat{\eta^2}(0)=\int\eta^2=1,
\]

and uses the entire kernel

\[
K_\eta(\xi):=\widehat{\eta^2}(\xi).
\tag{1}
\]

For a finite conjugation-invariant multiset `Z`, write

\[
Q_\eta(\mathcal Z)
:=\sum_{z,s\in\mathcal Z}K_\eta(z-s)^2,
\qquad
\Delta_\eta(\mathcal Z)
:=Q_\eta(\mathcal Z)-(2N-n),
\tag{2}
\]

where `N` counts multiplicity and `n` is the number of simple real elements. Lamzouri proves `Delta_eta>=0`.

WI-140 computes the isolated non-real pair exactly. For

\[
\mathcal Z_y=\{x+iy,x-iy\},
\qquad y>0,
\]

put

\[
t_\eta(y)
:=\int_{\mathbb R}\eta(u)^2\sinh^2(2\pi uy)\,du.
\tag{3}
\]

Then `N=2`, `n=0`, and

\[
\boxed{
\Delta_\eta(y)
=Q_\eta(\mathcal Z_y)-4
=8t_\eta(y)+8t_\eta(y)^2.
}
\tag{4}
\]

The associated Lamzouri tensor has exact nonzero eigenvalues

\[
\lambda_+(y)=2(1+t_\eta(y)),
\qquad
\lambda_-(y)=-2t_\eta(y).
\tag{5}
\]

The literature-backed input here is Lamzouri's universal finite inequality and his support convention. Equations (4)--(5) are the already persisted WI-140 reconstruction. The uniform optimization below is a new exact consequence of those formulas, not attributed to the preprint.

## 2. The whole adaptive window family has an exact envelope

Because `eta^2>=0`, has total mass one, and is supported in `(-lambda,lambda)`, while `sinh^2(2 pi u y)` is even and strictly increasing in `|u|` for `y>0`, equation (3) gives

\[
0\le t_\eta(y)
<\sinh^2(2\pi\lambda y).
\tag{6}
\]

The strict inequality reflects the open support convention for each individual window. The right side is nevertheless the exact supremum: take a sequence of normalized real even windows whose squared mass is concentrated in shrinking neighborhoods of `+lambda` and `-lambda`. Then

\[
t_{\eta_j}(y)
\longrightarrow
\sinh^2(2\pi\lambda y).
\tag{7}
\]

Since `8t+8t^2` is strictly increasing for `t>=0`, (4), (6), and (7) yield

\[
\begin{aligned}
\sup_\eta\Delta_\eta(y)
&=8\sinh^2(2\pi\lambda y)
  \left(1+\sinh^2(2\pi\lambda y)\right)\\
&=8\sinh^2(2\pi\lambda y)\cosh^2(2\pi\lambda y)\\
&=\boxed{2\sinh^2(4\pi\lambda y)}.
\end{aligned}
\tag{8}
\]

This proves (A). The same calculation gives a uniform bound for the magnitude of the negative eigenvalue itself:

\[
\boxed{
\sup_\eta |\lambda_-(y)|
=2\sinh^2(2\pi\lambda y).
}
\tag{9}
\]

Thus adaptivity does not merely fail for one optimized Montgomery--Taylor profile. Even the most edge-concentrated profile permitted by the support budget has a negative eigenvalue and a complete finite deficit that vanish quadratically as the pair conflues.

There is no compactness or regularity subtlety hiding in the supremum. Proposition 2.1 only needs an `L^2` window for the finite inequality; Lamzouri later uses smooth compactly supported windows for the zeta pair-correlation passage. Smooth even bump pairs can approximate the same edge concentration arbitrarily closely, so the supremum is unchanged in the smooth source-compatible subclass.

## 3. Fourier support is exactly the resource that pays for horizontal depth

Set

\[
q_\eta:=\eta^2.
\]

Then

\[
K_\eta=\widehat{q_\eta},
\qquad
K_\eta^2=\widehat{q_\eta*q_\eta}.
\tag{10}
\]

Since `q_eta` is supported in `(-lambda,lambda)`, the real pair-correlation spectral profile

\[
q_\eta*q_\eta
\]

is supported in `(-2lambda,2lambda)`. Therefore define the arithmetic Fourier-support radius

\[
\boxed{\sigma:=2\lambda.}
\tag{11}
\]

In this notation (8) becomes (B):

\[
\boxed{
\sup_\eta\Delta_\eta(y)
=2\sinh^2(2\pi\sigma y).
}
\tag{12}
\]

For fixed `sigma`, Taylor expansion at zero gives

\[
\boxed{
\sup_\eta\Delta_\eta(y)
=8\pi^2\sigma^2y^2+O_\sigma(y^4).
}
\tag{13}
\]

This is a quantitative Paley--Wiener-type tradeoff in elementary form: bounded spectral support bounds how rapidly the entire kernel can react in the imaginary direction. No deep Paley--Wiener theorem is needed for (12); it follows directly from the compact-support integral in (3). The classical support/exponential-type principle is only the surrounding harmonic-analysis interpretation.

Lamzouri's actual unconditional zeta application chooses

\[
\eta\in C_c^\infty((-1/2,1/2)),
\]

so `lambda=1/2` and

\[
\boxed{\sigma=1.}
\tag{14}
\]

Section 3 explicitly notes that `q_eta*q_eta` is then supported in `[-1,1]`, exactly the range to which the unconditional Montgomery pair-correlation lemma is applied. Thus the fixed-bandwidth hypothesis in this finding is not artificial: `sigma=1` is the current source-evaluable interface.

## 4. Zeta normalization turns the envelope into a support-depth law

Lamzouri rescales a zeta zero `rho=beta+i gamma` to

\[
z_\rho
=i\left(\rho-\frac12\right)\frac{\log T}{2\pi}.
\tag{15}
\]

The functional equation supplies the conjugate partner in this rescaled multiset, and the normalized horizontal depth is

\[
\boxed{
y_T
=\left|\beta-\frac12\right|\frac{\log T}{2\pi}.}
\tag{16}
\]

Substituting (16) into (12) gives

\[
\boxed{
\Delta_\eta
\le
2\sinh^2\!\left(
\sigma\left|\beta-\frac12\right|\log T
\right).
}
\tag{17}
\]

For a zero closer than the natural `1/log T` horizontal scale,

\[
\left|\beta-\frac12\right|\log T\to0,
\tag{18}
\]

all bounded-bandwidth adaptive windows satisfy

\[
\boxed{
\sup_\eta\Delta_\eta
=2\sigma^2\left|\beta-\frac12\right|^2\log^2T
+o\!\left(\left|\beta-\frac12\right|^2\log^2T\right)
\to0
}
\tag{19}
\]

when `sigma` is fixed. In particular the support-one family obeys

\[
\boxed{
\sup_\eta\Delta_\eta
\le2\sinh^2\!\left(
\left|\beta-\frac12\right|\log T
\right).
}
\tag{20}
\]

Conversely, if one wants this isolated pair to contribute at least a fixed amount `c>0`, (17) makes the necessary bandwidth condition

\[
2\sinh^2\!\left(
\sigma\left|\beta-\frac12\right|\log T
\right)
\ge c,
\]

or equivalently

\[
\boxed{
\sigma
\ge
\frac{\operatorname{arsinh}\sqrt{c/2}}
{\left|\beta-\frac12\right|\log T}.
}
\tag{21}
\]

Thus a **uniform order-one charge for arbitrarily shallow individual off-line pairs requires unbounded Fourier support** unless another theorem first supplies a lower bound on their normalized horizontal depth. Extending the current arithmetic interface from support one to any larger but fixed `sigma` only rescales the depth at which confluence becomes invisible; it does not remove the individual-exception obstruction.

## 5. Quantifier improvement over the earlier confluence barriers

WI-140 proves, for each fixed window `eta`,

\[
\Delta_\eta(y)\to0
\qquad(y\to0).
\tag{22}
\]

WI-142 then permits the detector itself to vary with matrix size but keeps the detector fixed before the adversarial depth is chosen: at each size one chooses `y` below that detector's continuity scale. That is a diagonal argument of the form

\[
\forall F_N\ \exists y_N:\quad F_N(\mathcal A_{y_N})\approx F_N(\mathcal A_0).
\tag{23}
\]

Equation (12) reverses the problematic quantifiers for the entire fixed-bandwidth Lamzouri window class:

\[
\boxed{
\lim_{y\to0^+}
\sup_{\substack{\eta:\,\int\eta^2=1\\
\operatorname{supp}(\eta^2*\eta^2)\subset[-\sigma,\sigma]}}
\Delta_\eta(y)
=0.
}
\tag{24}
\]

So the analyst may first observe the actual depth `y`, then choose the best admissible profile specifically for that pair; the uniform envelope still kills any positive charge. The same statement automatically contains finite, infinite, growing, and configuration-dependent portfolios of Lamzouri square kernels as long as their support radii remain uniformly bounded.

This is distinct from WI-156. WI-156 shows that post-hoc selection among separately valid scalar censuses does not beat the Montgomery--Taylor **aggregate support-one proportion constant** when the arithmetic limits are available. Equation (24) instead addresses the RH-facing anti-confluence question: it proves that even the strongest adaptive local slack obtainable from the whole bounded-bandwidth Lamzouri family cannot charge an arbitrarily shallow individual off-line pair.

## 6. Stress tests and scope boundary

This is a finite zero-side barrier, not a zeta counterexample. A real zeta zero does not occur as an isolated two-point universe: it interacts with all other zeros, and those interactions may contain source-specific information absent from the isolated pair. Therefore (21) does **not** rule out a many-body theorem at fixed support which proves that actual zeta configurations cannot sustain shallow off-line pairs. Such a theorem would be precisely the new interaction/anti-confluence input requested by the research mandate.

The finding also does not limit the critical Gram-defect mechanism used to improve the simple-critical proportion above Montgomery--Taylor. Those improvements exploit local geometry of already-certified simple critical zeros and do not claim a uniform charge on each off-line pair through the scalar Lamzouri deficit.

Nor does (21) say that wider support is sufficient. It gives only a necessary bandwidth to obtain an order-one isolated-pair charge from this square-kernel architecture. Evaluating a `T`-dependent support radius growing like the reciprocal horizontal depth would require arithmetic uniformity far beyond the currently used support-one pair-correlation theorem. A successful route could instead avoid that cost by proving a lower horizontal gap, a collective interaction theorem, a singular observable with an independently justified source identity, or another statistic that does not reduce to the Lamzouri scalar square-kernel deficit.

Multiplicity remains explicit. The control uses one **simple** off-real conjugate pair because that is the hardest confluence axis identified in WI-140 and WI-170. The endpoint at `y=0` is a real double, not a simple critical zero. The theorem therefore sharpens rather than erases the distinction between off-line mass, critical-line multiplicity, and proof slack.

## 7. Prior-art and novelty audit

The recent primary source is Lamzouri, arXiv:2609.02882v1. Proposition 2.1 supplies the window/support setup and finite Hilbert inequality; Section 3 specializes to `eta in C_c^infty((-1/2,1/2))`, observes that `eta^2*eta^2` is supported in `[-1,1]`, and applies the unconditional pair-correlation theorem in that support range. Remark 3.4 invokes the Carneiro--Chandee--Littmann--Milinovich one-delta theorem to show that the Montgomery--Taylor constant is optimal for Lamzouri's aggregate scalar method. Those are literature-backed facts and are not claimed here as new.

The support/exponential-type relationship for Fourier transforms of compactly supported functions is classical Paley--Wiener theory. The exact inequality (6) is even more elementary: it is simply the expectation bound for the increasing function `sinh^2(2 pi u y)` under the probability density `eta^2`. No novelty is claimed for that harmonic-analysis principle or for the hyperbolic-function identities used in (8).

The internal precursors are WI-140, WI-141, WI-142, WI-153, and WI-156. WI-140 derives the exact one-window pair formula; WI-141--WI-142 close fixed and preassigned continuous spectral refinements; WI-153 closes the bounded-depth signed scalar aggregate objective at support one; WI-156 closes finite adaptive selection among separate scalar censuses at the Montgomery--Taylor aggregate constant. None of those findings takes the supremum over the whole Lamzouri window class **after the horizontal depth is known** and computes it exactly.

A targeted search around the September 2026 Lamzouri preprint, adaptive support-one test functions, off-line pair depth, and classical Paley--Wiener/Bernstein growth located the standard compact-support/exponential-type literature but no source stating the pair envelope (8), the support-depth law (21), or its anti-confluence consequence. That absence is not used as a priority claim.

The durable Mathia deduction is therefore the exact quantifier-strengthened barrier

\[
\boxed{
\text{bounded Fourier support}
\Longrightarrow
\sup_{\text{adaptive Lamzouri windows}}
\text{isolated-pair deficit}=O(y^2)
\Longrightarrow
\text{no uniform individual off-line charge at confluence}.
}
\]

For the RH-facing program, this makes the missing information requirement sharper. Optimizing the support-one test function is not merely numerically insufficient: even an oracle choosing the best admissible Lamzouri window separately for each off-line depth cannot create a count gap. The next viable scalar-window escape must pay for support that grows as in (21); otherwise the route must cease to be a one-pair scalar-window argument and import genuine zeta-specific interaction or anti-confluence structure.
