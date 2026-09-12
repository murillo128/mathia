# AF-293 — General Hilbert mixing trades eta zero-count margin for condition number

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `ZERO-COUNT`, `TARGET-RELATIVE`, `CONDITIONING`, `NON-DIAGONAL`, `NO-NOVELTY-CLAIM`

## Claim

AF-292 proves that every positive diagonal Hilbert renorming leaves a vanishing normalized zero-count margin for RH-relevant eta truncations. Allowing a fully non-diagonal positive-definite coefficient metric changes the answer, but only by moving the same instability into the conditioning of the metric itself.

Let

\[
\eta_N(s)=\sum_{n=1}^N(-1)^{n-1}n^{-s},
\qquad
b^{(N)}=\bigl((-1)^{n-1}\bigr)_{n=1}^N,
\]

and let `Gamma` be a fixed compact rectifiable Jordan curve contained in `Re(s)>0` on which `eta` has no zero. Write

\[
\alpha:=\min_{z\in\Gamma}\operatorname{Re}z>0,
\qquad
H_N(x):=\left(\sum_{n\le N}n^{-2x}\right)^{1/2}.
\]

For a Hermitian positive-definite matrix `G`, measure coefficient perturbations by

\[
\|c\|_G=(c^*Gc)^{1/2},
\]

and let

\[
\delta^{(G)}_{\Gamma,N}
:=
\frac{\operatorname{dist}_G(b^{(N)},\Delta_{\Gamma,N})}
{\|b^{(N)}\|_G},
\]

where `Delta_{Gamma,N}` is AF-290's boundary-zero discriminant. Let

\[
\kappa(G)=\frac{\lambda_{\max}(G)}{\lambda_{\min}(G)}.
\]

For a condition-number budget `K>=1`, define

\[
\mathcal D_{\Gamma,N}(K)
:=
\sup_{G>0:\,\kappa(G)\le K}
\delta^{(G)}_{\Gamma,N}.
\]

Then, for all sufficiently large `N`,

\[
\boxed{
\mathcal D_{\Gamma,N}(K)
\asymp_{\Gamma}
\min\left\{
1,
\frac{\sqrt K}{\sqrt N\,H_N(\alpha)}
\right\}.
}
\]

Thus **bounded-condition non-diagonal mixing cannot change the AF-291 collapse law even by a power of `N`**. More generally, a nonvanishing normalized margin is possible only once

\[
\boxed{
\kappa(G_N)\gtrsim_{\Gamma} N H_N(\alpha)^2.
}
\]

This threshold is also sufficient up to contour-dependent constants. Consequently the sharp condition-number scale for removing the collapse is

\[
\boxed{
\kappa(G_N)\asymp
\begin{cases}
N, & \alpha>1/2,\\[1mm]
N\log N, & \alpha=1/2,\\[1mm]
N^{2-2\alpha}, & 0<\alpha<1/2.
\end{cases}
}
\]

If `G=A^*A` comes from an invertible linear coordinate transform `A`, then `kappa(G)=kappa_2(A)^2`. The threshold becomes

\[
\boxed{
\kappa_2(A_N)
\asymp
\sqrt N\,H_N(\alpha)
\asymp_{\Gamma}
\bigl(\delta^{(I)}_{\Gamma,N}\bigr)^{-1}.
}
\]

So unrestricted linear mixing can indeed make the eta zero-count margin order one, but the required transform is ill conditioned at exactly the reciprocal scale of the raw normalized margin. It does not eliminate the conditioning bill; it relocates it into the representation map.

## Exact distance in an arbitrary Hilbert coefficient metric

For fixed `z`, define the standard Euclidean Riesz vector

\[
r_z=(n^{-\overline z})_{n=1}^N,
\]

so that

\[
L_z(c)=\sum_{n\le N}c_n n^{-z}=r_z^*c.
\]

The dual norm of evaluation under `||.||_G` is

\[
\|L_z\|_{G,*}
=(r_z^*G^{-1}r_z)^{1/2}.
\]

The same Hilbert-space projection used in AF-290 therefore gives

\[
\operatorname{dist}_G(b^{(N)},\ker L_z)
=
\frac{|\eta_N(z)|}{(r_z^*G^{-1}r_z)^{1/2}},
\]

and hence

\[
\boxed{
\delta^{(G)}_{\Gamma,N}
=
\min_{z\in\Gamma}
\frac{|\eta_N(z)|}
{(b^{(N)*}Gb^{(N)})^{1/2}
 (r_z^*G^{-1}r_z)^{1/2}}.
}
\]

Common scalar multiplication of `G` cancels exactly, so only the projective shape of the ellipsoid matters.

There is also a universal upper bound independent of `G`. Cauchy-Schwarz in the `G` geometry gives

\[
|\eta_N(z)|
=|r_z^*b^{(N)}|
\le
\|b^{(N)}\|_G\,\|L_z\|_{G,*},
\]

so

\[
\delta^{(G)}_{\Gamma,N}\le1.
\]

An arbitrary metric can therefore at most turn the target into an order-one relative margin; it cannot produce a normalized radius larger than one.

## A condition-number budget gives the sharp upper bound

Let

\[
\lambda_{\min}=\lambda_{\min}(G),
\qquad
\lambda_{\max}=\lambda_{\max}(G).
\]

For every vector `x`,

\[
\|x\|_G\ge\sqrt{\lambda_{\min}}\,\|x\|_2,
\qquad
\|x\|_{G^{-1}}\ge\frac{1}{\sqrt{\lambda_{\max}}}\,\|x\|_2.
\]

Choose `z_* in Gamma` with `Re(z_*)=alpha`. Since

\[
\|b^{(N)}\|_2=\sqrt N,
\qquad
\|r_{z_*}\|_2=H_N(\alpha),
\]

we obtain

\[
\|b^{(N)}\|_G
\|r_{z_*}\|_{G^{-1}}
\ge
\frac{\sqrt N\,H_N(\alpha)}{\sqrt{\kappa(G)}}.
\]

As in AF-291 and AF-292, local uniform convergence `eta_N -> eta` on the zero-free compact boundary supplies a constant `M_Gamma` such that

\[
|\eta_N(z)|\le M_\Gamma
\qquad(z\in\Gamma)
\]

for all sufficiently large `N`. Therefore every `G` with `kappa(G)<=K` satisfies

\[
\boxed{
\delta^{(G)}_{\Gamma,N}
\le
M_\Gamma
\frac{\sqrt K}{\sqrt N\,H_N(\alpha)}.
}
\]

Together with the universal bound `delta<=1`, this proves the upper half of the claimed budget law.

In particular, if `K` stays bounded, general relational mixing is norm-equivalent to the raw coefficient geometry by constants independent of breadth, so it cannot improve AF-291's asymptotic exponent. To keep `delta^(G)` bounded below by any fixed positive constant, one necessarily needs

\[
K\gtrsim_\Gamma N H_N(\alpha)^2.
\]

## A rank-one-adapted dense metric attains the threshold

The necessary scale is also sufficient. Let

\[
u_N:=\frac{b^{(N)}}{\sqrt N},
\qquad
P_N:=u_Nu_N^*,
\qquad
Q_N:=I-P_N.
\]

For `K>=1`, define the dense non-diagonal metric

\[
\boxed{G_{N,K}=P_N+KQ_N.}
\]

It leaves the nominal eta coefficient ray at unit metric scale while penalizing every Euclidean-orthogonal direction by the factor `K`. Its condition number is exactly `K`, and

\[
G_{N,K}^{-1}=P_N+K^{-1}Q_N.
\]

Because

\[
|u_N^*r_z|^2=\frac{|\eta_N(z)|^2}{N},
\qquad
\|r_z\|_2^2=H_N(\operatorname{Re}z)^2,
\]

we get the exact identity

\[
r_z^*G_{N,K}^{-1}r_z
=
\frac{|\eta_N(z)|^2}{N}
+
\frac1K\left(
H_N(\operatorname{Re}z)^2
-
\frac{|\eta_N(z)|^2}{N}
\right).
\]

Also `||b^(N)||_{G_{N,K}}=sqrt(N)`. Hence the pointwise normalized boundary distance is

\[
\boxed{
R_{N,K}(z)
=
\left[
1+
\frac{N H_N(\operatorname{Re}z)^2/|\eta_N(z)|^2-1}{K}
\right]^{-1/2}.
}
\]

Let

\[
m_\Gamma:=\frac12\min_{z\in\Gamma}|\eta(z)|>0.
\]

For all sufficiently large `N`, `|eta_N(z)|>=m_Gamma` uniformly on `Gamma`; moreover `H_N(Re z)<=H_N(alpha)`. Therefore

\[
\delta^{(G_{N,K})}_{\Gamma,N}
\ge
\left[
1+
\frac{N H_N(\alpha)^2}{K m_\Gamma^2}
\right]^{-1/2}.
\]

This is comparable, with constants depending only on `Gamma`, to

\[
\min\left\{1,\frac{\sqrt K}{\sqrt N H_N(\alpha)}\right\},
\]

which matches the general upper bound. The budget law is therefore sharp.

The construction is genuinely non-diagonal in the canonical Dirichlet-coordinate basis: `P_N` contains all pairwise products `b_j b_k/N`. It is the simplest possible relational repair after AF-292, and it succeeds only by becoming increasingly anisotropic.

## The repair is an almost-one-dimensional noise model

The exact optimizer-scale construction explains why unrestricted SPD renorming would be a misleading escape from AF-292 if its own condition number were not priced.

As `K -> infinity`, the unit ball of `G_{N,K}` collapses toward the single ray direction spanned by `b^(N)`. Perturbations orthogonal to the nominal eta coefficient vector become arbitrarily expensive, while perturbations along that ray mostly rescale the analytic function and therefore do not move its zeros. Correspondingly,

\[
R_{N,K}(z)\longrightarrow1
\]

uniformly on the fixed zero-free boundary for each fixed `N`.

Thus the apparent stabilization is not free discovery of a better coefficient geometry. The metric has encoded increasingly strong prior knowledge that the admissible error is almost parallel to the nominal source. In the limit, it has nearly excluded the very directions that can create a boundary zero.

The quantitative theorem makes that circularity measurable. The transform condition number required to make the target margin order one is

\[
\kappa_2(A_N)
\asymp
\sqrt N H_N(\alpha),
\]

which is the reciprocal of the raw AF-291 margin up to the fixed boundary constants. Exactly as much conditioning as was lost in the original representation must be injected into the new coordinates.

## Critical-strip consequence

If `Gamma` surrounds a point on the critical line as an interior point, then its leftmost real part satisfies

\[
0<\alpha<\frac12.
\]

The sharp condition threshold is therefore

\[
\kappa(G_N)\asymp N^{2-2\alpha},
\qquad
\kappa_2(A_N)\asymp N^{1-\alpha}.
\]

For a contour with left edge `alpha=1/2-epsilon`,

\[
\kappa(G_N)\asymp N^{1+2\varepsilon},
\qquad
\kappa_2(A_N)\asymp N^{1/2+\varepsilon}.
\]

AF-292 showed that coordinatewise scaling cannot improve the critical-strip margin exponent. AF-293 now shows that fully relational linear mixing can remove the margin collapse only by paying a polynomially diverging anisotropy whose exponent is exactly determined by the same boundary-evaluation breadth.

This is a stronger separation than a simple diagonal-versus-dense distinction. **The live resource is not whether the metric mixes coordinates; it is how much distortion the representation is allowed to introduce.**

## Prior art and novelty assessment

The underlying mathematics is classical, and no broad novelty is claimed.

- The distance-to-ill-posedness interpretation and zero-count conditioning language are inherited from AF-290 and its classical sources, especially James W. Demmel, **“On condition numbers and the distance to the nearest ill-posed problem,”** *Numerische Mathematik* 51(3), 251–289 (1987), DOI `10.1007/BF01400115`.
- Positive-definite changes of inner product, spectral condition numbers, dual norms, and norm-equivalence estimates are standard finite-dimensional matrix analysis; Roger A. Horn and Charles R. Johnson, ***Matrix Analysis***, 2nd ed., Cambridge University Press (2012/2013), DOI `10.1017/CBO9781139020411`, is a standard reference already used elsewhere in this line.
- The numerical-linear-algebra literature studies optimization and design of SPD preconditioners and condition numbers extensively. The theorem here does not claim a new general preconditioning principle; it solves the specific finite-eta boundary-zero margin problem under an explicit condition-number budget.

A targeted prior-art search found general work on optimal SPD/structured preconditioning and condition-number optimization, but no reason to treat the elementary spectral inequalities or the rank-one metric construction as novel. The retained result is the Arithmetic Fidelity specialization: the best zero-count margin under a condition budget has the exact asymptotic profile `min(1,sqrt(K)/(sqrt(N)H_N(alpha)))`, so the cost of escaping AF-291 is quantitatively identical to the conditioning that the new representation itself introduces.

## Boundaries and failure modes

- The metric may depend on `N` and may be dense. The upper bound therefore applies even to highly target-designed linear Hilbert geometries, provided their spectral condition number is controlled.
- The lower construction is adapted to the nominal eta coefficient vector. It should not be interpreted as a source-natural metric for arbitrary Dirichlet coefficient families. Its role is to prove sharpness of the condition-number threshold and expose what unrestricted metric choice can hide.
- `kappa(G)` is a coordinate-distortion bill relative to the canonical Euclidean coefficient geometry. If a future representation has an independently justified non-Euclidean native metric, that geometry must be audited on its own terms rather than rejected merely because it looks anisotropic in these coordinates.
- The theorem concerns finite zero count on one fixed compact contour. It does not control zero locations, multiplicities, growing-height windows, the global zero divisor, or RH.
- The result rules out only **uniformly well-conditioned linear Hilbert mixing** as a free escape. It does not rule out a nonlinear representation, a target-relevant quotient that genuinely removes nuisance directions, a non-Hilbert topology, or a structural relation that provides anisotropy for independent mathematical reasons.
- A diverging condition number is not itself a proof of uselessness. The obstruction is that a proposed repair cannot claim improved fidelity merely by choosing a metric whose distortion already carries the reciprocal conditioning bill. An independent reason for that metric could still make it meaningful.

## Consequence for the research line

AF-292's open phrase “non-diagonal relational mixing” can now be split sharply.

A bounded-condition relational change of Hilbert geometry is insufficient: it preserves the raw AF-291 decay up to constants. An unbounded-condition change can stabilize the target, and the sharp required distortion is `sqrt(N)H_N(alpha)` at the coordinate-transform level. The simplest dense metric attains that threshold by collapsing admissible noise toward the nominal eta ray.

The next useful escape test should therefore not ask merely whether mixing helps. It should ask whether a **source-natural relational representation supplies the required anisotropy without importing the target answer**, or whether a quotient/nonlinear topology reduces the breadth of genuinely target-relevant perturbation directions before the AF-290 discriminant is evaluated.