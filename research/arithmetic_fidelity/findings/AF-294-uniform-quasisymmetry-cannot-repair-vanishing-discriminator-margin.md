# AF-294 — Uniform quasisymmetry cannot repair vanishing discriminator margin

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `TARGET-RELATIVE`, `NONLINEAR`, `QUASISYMMETRIC`, `CONDITIONING`, `NO-NOVELTY-CLAIM`

## Claim

AF-293 shows that an invertible linear change of coefficient coordinates can turn the finite-eta boundary-zero margin from vanishing to order one only by paying a condition number on the reciprocal scale of the raw margin. The same obstruction extends beyond linear or Hilbert geometry.

Let `(X,d_X)` and `(Y,d_Y)` be metric spaces, let `D` be a nonempty discriminant subset of `X`, let `x in X` be the nominal object, and let `a != x` be an anchor used to normalize scale. Define the relative discriminator margin

\[
\rho_X(x;D,a)
:=
\frac{\operatorname{dist}_X(x,D)}{d_X(x,a)}.
\]

Let `F:X -> Y` be an injective representation map and transport the target structure honestly:

\[
x' = F(x),
\qquad
D'=F(D),
\qquad
a'=F(a).
\]

Assume `F` is `eta`-quasisymmetric on the relevant set `{x,a} union D`, meaning that `eta:[0,infinity)->[0,infinity)` is an increasing homeomorphism with `eta(0)=0` and

\[
\frac{d_Y(F(u),F(v))}{d_Y(F(u),F(w))}
\le
\eta\!\left(
\frac{d_X(u,v)}{d_X(u,w)}
\right)
\]

whenever the displayed ratios are defined. Then

\[
\boxed{
\frac{1}{\eta\!\left(1/\rho_X\right)}
\le
\rho_Y(F(x);F(D),F(a))
\le
\eta(\rho_X),
}
\]

with the lower bound interpreted as `0` when `rho_X=0`.

Consequently, for any sequence of problems and representations with one **uniform** distortion function `eta`,

\[
\rho_{X_N}\longrightarrow0
\quad\Longrightarrow\quad
\rho_{Y_N}\longrightarrow0.
\]

Thus **no uniformly quasisymmetric nonlinear change of representation can turn a vanishing normalized discriminator margin into a nonvanishing one while preserving the same target discriminant**. A successful nonlinear repair must therefore make the relative metric distortion itself degenerate with problem size, change the target/bad set, add genuinely new information, or leave the quasisymmetric category.

This strictly strengthens AF-293's bounded-condition linear obstruction. Quasisymmetry is designed to control relative rather than absolute distances, so it is the natural nonlinear regularity class for the normalized margins used in the recent eta zero-count findings.

## Exact setwise distortion theorem

For each `d in D`, put

\[
r_d
:=
\frac{d_X(x,d)}{d_X(x,a)},
\qquad
R_d
:=
\frac{d_Y(F(x),F(d))}{d_Y(F(x),F(a))}.
\]

Quasisymmetry with the ordered triple `(x,d,a)` gives

\[
R_d\le\eta(r_d).
\]

Swapping the last two points gives

\[
\frac1{R_d}
\le
\eta\!\left(\frac1{r_d}\right),
\]

hence

\[
R_d
\ge
\frac1{\eta(1/r_d)}.
\]

Define

\[
h(t):=
\begin{cases}
1/\eta(1/t),&t>0,\\
0,&t=0.
\end{cases}
\]

Because `eta` is an increasing homeomorphism, both `eta` and `h` are increasing and continuous. Also

\[
\rho_X=\inf_{d\in D}r_d,
\qquad
\rho_Y=\inf_{d\in D}R_d.
\]

The pointwise lower bound therefore yields

\[
\rho_Y
\ge
\inf_{d\in D}h(r_d)
\ge
h\!\left(\inf_{d\in D}r_d\right)
=
\frac1{\eta(1/\rho_X)}.
\]

For the upper bound, choose a sequence `d_j in D` with `r_{d_j} -> rho_X`. Then

\[
\rho_Y
\le
\liminf_j R_{d_j}
\le
\lim_j\eta(r_{d_j})
=
\eta(\rho_X).
\]

No smoothness, linearity, convexity, finite dimensionality, Hilbert structure, or attainment of the distance to `D` is required. The result is only a relative-metric consequence of quasisymmetry plus honest transport of the discriminant.

An immediate limiting corollary is stronger than ordinary norm equivalence. If a single `eta` controls an entire family `F_N` and `rho_N -> 0`, then

\[
0\le\rho'_N\le\eta(\rho_N)\longrightarrow\eta(0)=0.
\]

Therefore a fixed controlled nonlinear geometry may alter the **rate** at which a margin collapses, but cannot change collapse into a positive asymptotic margin.

## What a successful nonlinear repair must pay

Suppose instead that a family `F_N` has distortion functions `eta_N` and succeeds in producing

\[
\rho'_N\ge c>0
\]

while

\[
\rho_N\longrightarrow0.
\]

The exact upper bound forces

\[
\boxed{
\eta_N(\rho_N)\ge c.
}
\]

Hence there cannot exist any single distortion function `eta` controlling all `F_N`. The nonlinear repair must become increasingly singular in **relative** geometry exactly at the shrinking discriminator scale.

This gives a representation-independent conditioning bill. For linear maps AF-293 measured it by a spectral condition number. For nonlinear maps there need not be one canonical scalar condition number, but the family of relative distortion functions records the same phenomenon: a representation that claims to create a uniform target margin must cease to have uniform geometric control at the source margin scale.

This also separates two statements that are easy to conflate:

- a nonlinear representation may substantially change the numerical size or decay exponent of a margin;
- a uniformly controlled nonlinear representation cannot turn a margin tending to zero into one bounded away from zero.

For example, replacing a metric `d` by its snowflake `d^alpha`, `0<alpha<1`, changes a relative margin exactly from `rho` to `rho^alpha`. This can make a tiny margin much larger numerically, but `rho^alpha -> 0` whenever `rho -> 0`. The improvement reflects a fixed scale distortion rather than recovered discriminator information.

## Bi-Lipschitz and linear specialization

If `F` is bi-Lipschitz with constants `0<m<=L`,

\[
m\,d_X(u,v)
\le
d_Y(F(u),F(v))
\le
L\,d_X(u,v),
\]

then it is quasisymmetric with

\[
\eta(t)=Kt,
\qquad
K:=\frac{L}{m}.
\]

The general theorem reduces to

\[
\boxed{
K^{-1}\rho_X
\le
\rho_Y
\le
K\rho_X.
}
\]

Therefore an order-one repaired margin `rho_Y>=c` requires

\[
K\ge\frac{c}{\rho_X}.
\]

For an invertible linear map `A` between Euclidean coefficient spaces,

\[
m=\sigma_{\min}(A),
\qquad
L=\sigma_{\max}(A),
\qquad
K=\kappa_2(A).
\]

So the quasisymmetric theorem recovers AF-293's linear conditioning law at the correct representation level: the relevant relative-distortion cost is the transform condition number `kappa_2(A)`, while AF-293's SPD metric condition number is its square when `G=A^*A`.

This agreement is useful because it shows that AF-293 was not an artifact of quadratic norms or spectral matrix estimates. Its basic obstruction is a metric one: controlled representations cannot create relative separation from an honestly transported failure set.

## Eta zero-count consequence

Apply the theorem to the finite eta coefficient problem from AF-290--AF-293. Let

\[
X_N=\mathbb C^N
\]

with its canonical Euclidean metric,

\[
x_N=b^{(N)}=\bigl((-1)^{n-1}\bigr)_{n=1}^N,
\qquad
a_N=0,
\]

and let

\[
D_N=\Delta_{\Gamma,N}
\]

be the boundary-zero discriminant for a fixed zero-free compact Jordan curve `Gamma` in `Re(s)>0`. Write

\[
\alpha=\min_{z\in\Gamma}\operatorname{Re}z>0,
\qquad
H_N(\alpha)=\left(\sum_{n\le N}n^{-2\alpha}\right)^{1/2}.
\]

AF-291 and AF-293 give the canonical normalized margin scale

\[
\rho_N
=
\frac{\operatorname{dist}(b^{(N)},\Delta_{\Gamma,N})}
{\|b^{(N)}\|_2}
\asymp_{\Gamma}
\frac1{\sqrt N\,H_N(\alpha)},
\]

so in particular `rho_N -> 0`.

Now let `F_N` be any nonlinear representation of the coefficient problem into metric spaces `Y_N`, normalize by `F_N(0)`, and require that the target bad set is exactly the transported boundary-zero discriminant `F_N(Delta_{Gamma,N})`. If the family is uniformly `eta`-quasisymmetric, then

\[
\boxed{
\rho'_N
\le
\eta\!\left(ho_N\right)
\longrightarrow0.
}
\]

Thus the open nonlinear escape left by AF-293 is substantially narrowed: **nonlinearity by itself is not a resource**. Any representation family that produces an order-one zero-count margin must have distortion functions `eta_N` satisfying

\[
\eta_N\!\left(
\Theta_{\Gamma}\left((\sqrt N H_N(\alpha))^{-1}\right)
\right)
\gtrsim1.
\]

In the bi-Lipschitz subcase this becomes

\[
K_N
\gtrsim_{\Gamma}
\sqrt N\,H_N(\alpha),
\]

which is exactly the AF-293 transform-conditioning threshold. For a contour whose left edge is `alpha=1/2-epsilon`, this is polynomial:

\[
K_N\gtrsim_{\Gamma}N^{1/2+\varepsilon}.
\]

The nonlinear theorem therefore preserves the central AF-293 interpretation while removing the linearity assumption: a representation can enlarge the target margin only by paying comparable relative-geometric distortion, unless it changes what counts as the target or carries additional structure not present in the original metric problem.

## Prior art and novelty assessment

The general geometry used here is classical and no broad novelty is claimed.

- Quasisymmetric maps were introduced precisely to control **relative** metric distortion. A standard reference is Juha Heinonen, *Lectures on Analysis on Metric Spaces*, Springer, 2001, especially the chapters on the basic theory of quasisymmetric maps, DOI `10.1007/978-1-4613-0131-8`. The displayed two-sided relative-distance estimate is an immediate setwise consequence of the defining inequality; it is not claimed as a new theorem in metric geometry.
- The interpretation of a distance to a bad or ill-posed set as a conditioning quantity is classical. James W. Demmel, “On condition numbers and the distance to the nearest ill-posed problem,” *Numerische Mathematik* 51(3), 251--289 (1987), DOI `10.1007/BF01400115`, is the canonical reference already underlying AF-290--AF-293.
- James Renegar, “Is It Possible to Know a Problem Instance Is Ill-Posed?: Some Foundations for a General Theory of Condition Numbers,” *Journal of Complexity* 10(1), 1--56 (1994), DOI `10.1006/jcom.1994.1001`, develops a general condition/ill-posedness framework beyond one specific linear-algebra problem.
- Peter Bürgisser and Felipe Cucker, *Condition: The Geometry of Numerical Algorithms*, Springer, 2013, DOI `10.1007/978-3-642-38896-5`, gives a systematic geometric treatment of condition and discriminant structure.

The retained Arithmetic Fidelity contribution is the synthesis at the current research frontier: normalized discriminator margins are relative-distance observables, so quasisymmetry supplies the correct nonlinear invariance class. Applied to AF-293, it proves that every uniformly controlled nonlinear representation still inherits vanishing eta zero-count margin. The only possible representation-only escape is therefore **non-uniform relative distortion**, not merely nonlinearity.

A targeted literature check found extensive classical theories of quasisymmetric distortion and distance-to-ill-posedness, but no basis for treating their combination here as a novel general theorem. The value of the finding is the exact transfer principle and its consequence for the Mathia conditioning program.

## Boundaries and failure modes

- The target discriminant must be the honest transported set `F(D)`. If a new representation uses a different bad set `E subset Y`, the theorem says nothing about `dist(F(x),E)` until the relation between `E` and `F(D)` is proved. Changing the target can be mathematically legitimate, but it is a category change rather than a coordinate repair of the same problem.
- The normalization anchor is transported as `F(a)`. A different denominator can create apparent margin improvement by rescaling the reference quantity; that change requires a separate audit.
- The theorem applies to nonlinear maps and to embeddings into a larger ambient metric space as long as the relevant relative distances are uniformly quasisymmetrically controlled. Merely adding deterministic coordinates does not evade it if the resulting embedding remains uniformly quasisymmetric.
- A genuinely enriched lift carrying information not determined by the original object is not just a representation map `F:X->Y` of the same data. Such added marking can change fidelity and is outside this obstruction.
- Noninjective compressions are not quasisymmetric embeddings. Their fibers can destroy distinctions outright and must be analyzed by the quotient/fiber tools elsewhere in this line rather than by AF-294.
- A family may be quasisymmetric for every fixed `N` while its distortion function worsens with `N`. AF-294 does not rule such a family out; it identifies the required loss of **uniform** control as the price of repair.
- Fixed quasisymmetric distortion can change asymptotic rates. AF-294 preserves the qualitative property `rho_N -> 0`, not the exact decay exponent unless stronger distortion information such as bi-Lipschitz or power-type bounds is available.
- The theorem concerns relative distance to a discriminant. It does not state that every notion of conditioning, recoverability, or statistical distinguishability is metric or quasisymmetric.
- For the eta application, the conclusion concerns stability of a finite zero count on a fixed contour. It does not establish zero locations, simplicity, the global zero divisor, or RH.
- Degenerating distortion is not automatically illegitimate. A source-natural mathematical structure could force it for independent reasons. What AF-294 forbids is claiming a free fidelity improvement from a nonlinear reparameterization while leaving its worsening relative geometry unpriced.

## Consequence for the research line

AF-293 left three broad representation-level possibilities: nonlinear coordinates, a target-relevant quotient that removes nuisance directions, or additional structure that changes the fidelity problem. AF-294 closes a large part of the first branch.

A uniformly quasisymmetric nonlinear representation cannot repair the vanishing normalized eta discriminator margin. This includes every uniformly bi-Lipschitz change and, more generally, any fixed relative-distortion geometry even when it is strongly nonlinear and can alter decay rates.

The next useful nonlinear question is therefore not “can a nonlinear map enlarge the margin?” It is whether a **source-natural family can justify the required degeneration of relative distortion at the discriminator scale without merely encoding the target answer**. In parallel, quotient or enrichment proposals must state explicitly whether they preserve `F(D)` or alter the target category. That separation prevents nonlinear coordinate freedom from becoming an unpriced escape hatch from the conditioning obstruction.