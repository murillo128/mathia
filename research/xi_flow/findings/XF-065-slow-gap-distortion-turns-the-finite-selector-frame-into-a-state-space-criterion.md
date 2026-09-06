# XF-065 — slow gap distortion turns the finite selector frame into a state-space criterion

**Status:** `EXACT-DERIVED` + `FINITE-STATE-FRAME` + `NONLINEAR-MEASUREMENT` + `STRUCTURAL/REPAIR`. XF-064 proves that the exact moved-point selector has the XF-063 lower frame after fixed positive **tangent** heat time, using tangent heat only to obtain a small Fourier-Wiener parameter. The measurement theorem itself is more general. After removing the irrelevant uniform translation, a purely geometric bound on displacement oscillation and adjacent gap distortion already controls the Wiener norm strongly enough to make every quadratic-and-higher selector term perturbative on the shrinking Xi slow cone.

Use the XF-062--XF-064 scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
N=2M,
\tag{1}
\]

and the same fixed nonzero envelope `g` with

\[
\chi:=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{\mathbb R}|\chi(u)|^2\,du>0.
\tag{2}
\]

For an arbitrary real `N`-periodic displacement `a=(a_j)`, write

\[
c:=\frac1N\sum_j a_j,
\qquad
b_j:=a_j-c,
\tag{3}
\]

and define the two finite-state geometry parameters

\[
A:=\|b\|_{\ell^\infty},
\qquad
D:=\|\Delta b\|_{\ell^\infty}=\|\Delta a\|_{\ell^\infty}.
\tag{4}
\]

Thus `A` measures displacement oscillation after quotienting out translation, while `D` is exactly the maximum relative gap distortion in index coordinates: if `x_j=s(j+a_j)`, then

\[
\frac{x_{j+1}-x_j}{s}-1=\Delta a_j.
\tag{5}
\]

Let

\[
\mathfrak W(b)
:=\frac1{\sqrt N}\sum_\ell|\widehat b_\ell|
\tag{6}
\]

be the normalized discrete Wiener norm. Then there is an absolute constant `C_0` such that every periodic displacement satisfies the interpolation estimate

\[
\boxed{
\mathfrak W(b)
\le
C_0\left(A+\sqrt{AND}\right).
}
\tag{7}
\]

No heat equation and no spectral-support assumption enters (7).

Now use the XF-063 frame bands

\[
B_T^{\rm in}
=
\left[
2q^{-3/2},
\frac{C\log\log T}{q}
\right],
\qquad
B_T^{\rm out}
=
\left[
q^{-3/2},
\frac{(C+1)\log\log T}{q}
\right],
\tag{8}
\]

and put

\[
\theta_-:=q^{-3/2},
\qquad
\theta_+:=\frac{(C+1)\log\log T}{q},
\qquad
W:=\mathfrak W(b).
\tag{9}
\]

Define the three dimensionless measurement parameters

\[
\alpha:=\frac WM,
\qquad
\beta:=\theta_+W,
\qquad
\gamma:=\theta_-^{-1}\frac{W}{M^2}.
\tag{10}
\]

For the exact moved selector

\[
\mathcal N_{M,a}(\theta)
:=
\sum_{j\in\mathbb Z}
 g\!\left(\frac{j+a_j}{M}\right)
 e^{-i\theta(j+a_j)},
\tag{11}
\]

let `\mathcal L^{(c)}_{M,b}` denote its first variation in `b` about the uniformly translated lattice `j+c`:

\[
\mathcal L^{(c)}_{M,b}(\theta)
:=
\sum_j b_j
\left[
\frac1M g'\!\left(\frac{j+c}{M}\right)
-i\theta g\!\left(\frac{j+c}{M}\right)
\right]
 e^{-i\theta(j+c)}.
\tag{12}
\]

Equip selector functions with the XF-060--XF-064 norm

\[
\|F\|_{X_T}^2
:=
M\int_{B_T^{\rm out}}
(M\theta^2)^2|F(\theta)|^2\,d\theta,
\tag{13}
\]

and define the finite-state third-difference energy

\[
\mathcal Q_M(B;b)
:=
M^3\sum_{\xi_\ell\in B}
|e^{i\xi_\ell}-1|^6|\widehat b_\ell|^2.
\tag{14}
\]

Then, whenever `alpha+beta` is sufficiently small,

\[
\boxed{
\|\mathcal N_{M,a}-\mathcal L^{(c)}_{M,b}\|_{X_T}
\le
C_g'\,(\alpha+\beta+\gamma)
\mathcal Q_M(( -\pi,\pi];b)^{1/2},
}
\tag{15}
\]

with `C_g'` depending only on the fixed window and the fixed outer-band constant `C`. Moreover the translated linearization has exactly the XF-063 frame constant,

\[
\boxed{
\|\mathcal L^{(c)}_{M,b}\|_{X_T}^2
\ge
\left(\frac{C_g}{4}+o(1)\right)
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in});b\bigr),
}
\tag{16}
\]

uniformly in the translation `c`.

Consequently, for **any** family of finite states satisfying

\[
\alpha+\beta+\gamma=o(1)
\tag{17}
\]

and the relative band-concentration condition

\[
\mathcal Q_M\!\left(
(-\pi,\pi]\setminus
(B_T^{\rm in}\cup-B_T^{\rm in});b
\right)
=o\!\left(
\mathcal Q_M(B_T^{\rm in}\cup-B_T^{\rm in};b)
\right),
\tag{18}
\]

one has the exact finite-state lower frame

\[
\boxed{
\|\mathcal N_{M,a}\|_{X_T}^2
\ge
\left(\frac{C_g}{4}+o(1)\right)
\mathcal Q_M
\bigl(B_T^{\rm in}\cup(-B_T^{\rm in});b\bigr).
}
\tag{19}
\]

No tangent trajectory appears in (15)--(19). In particular, a Duhamel comparison of the true finite-amplitude zero flow with the arithmetic-lattice tangent semigroup is **sufficient but not logically necessary** for the measurement step. One may instead prove the state-space conditions (17)--(18) directly for a real-simple Xi transition slice.

At the Mathia scales, (7) gives the explicit sufficient criterion

\[
\boxed{
A=o\!\left(\frac q{\log\log T}\right),
\qquad
AD=o\!\left((\log\log T)^{-2}\right)
\Longrightarrow
\alpha+\beta+\gamma=o(1).
}
\tag{20}
\]

For bounded displacement oscillation `A=O(1)`, it is enough that

\[
\boxed{
D=o\!\left((\log\log T)^{-2}\right).
}
\tag{21}
\]

This is far weaker than tangent heat smoothing at the level of adjacent gaps. XF-064 gives `D=O(q^{-1/2})` in its tangent model; (21) only asks for a vanishing relative gap distortion on the doubly logarithmic scale. The genuinely hard dynamical condition is therefore no longer nonlinear evaluation of the selector. It is to force the actual finite-amplitude transition state into the slow `H^3` band (18), while retaining the transition-scale mass that the frame is meant to detect.

This still does **not** produce an upper bound for the de Bruijn--Newman constant. Nothing here proves (18) for Xi, proves that a critical nonlinear transition defect survives until such a state is reached, or crosses a collision/complex-root interval. The finding only removes an unnecessary trajectory-level requirement from the downstream measurement gate.

## 1. Uniform translation is an exact null direction of the frame problem

Write `a=c+b` as in (3). Then

\[
\mathcal N_{M,a}(\theta)
=
e^{-i\theta c}
\sum_j
 g\!\left(\frac{j+c+b_j}{M}\right)
 e^{-i\theta(j+b_j)}.
\tag{22}
\]

Introduce the shifted envelope

\[
g_c(x):=g(x+c/M).
\tag{23}
\]

Its Fourier transform differs from `chi` only by a unit-modulus phase, so

\[
\operatorname{supp}\widehat g_c\subset(-1,1),
\qquad
\int|\widehat g_c|^2=C_g,
\tag{24}
\]

with all window seminorms used by XF-063--XF-064 unchanged. Hence the uniformly shifted lattice contribution vanishes identically on `B_T^{out}` by the same Poisson-support argument as before, and the linearized frame about `j+c` has the same constant as the frame about `j`.

This is important for the nonlinear gate. An arbitrarily large common displacement does not broaden selector sidebands. Only the **oscillatory part** `b` can do so, and all third-difference energies are unchanged by removing `c`.

## 2. A discrete Wiener interpolation bound from oscillation and gap distortion

Let principal periodic frequencies be

\[
\xi_\ell=\frac{2\pi\ell}{N},
\qquad
m_\ell=e^{i\xi_\ell}-1,
\qquad
-\frac N2<\ell\le\frac N2.
\tag{25}
\]

Because `b` has zero mean, `\widehat b_0=0`. Fix an integer `1<=K<=N/2`. For the low modes, Cauchy--Schwarz and Parseval give

\[
\begin{aligned}
\frac1{\sqrt N}
\sum_{0<|\ell|\le K}|\widehat b_\ell|
&\le
\frac{\sqrt{2K}}{\sqrt N}\|b\|_2\\
&\le A\sqrt{2K}.
\end{aligned}
\tag{26}
\]

For the high modes, insert one discrete derivative:

\[
\begin{aligned}
\frac1{\sqrt N}
\sum_{|\ell|>K}|\widehat b_\ell|
&\le
\frac1{\sqrt N}
\left(\sum_{|\ell|>K}|m_\ell|^{-2}\right)^{1/2}
\|\Delta b\|_2\\
&\le
D
\left(\sum_{|\ell|>K}|m_\ell|^{-2}\right)^{1/2}.
\end{aligned}
\tag{27}
\]

For `|ell|<=N/2`,

\[
|m_\ell|
=2\sin\frac{\pi|\ell|}{N}
\ge\frac{4|\ell|}{N}.
\tag{28}
\]

Therefore

\[
\sum_{|\ell|>K}|m_\ell|^{-2}
\le
\frac{N^2}{8K},
\tag{29}
\]

and

\[
\boxed{
\mathfrak W(b)
\le
A\sqrt{2K}
+\frac{DN}{\sqrt{8K}}.
}
\tag{30}
\]

Choosing `K` nearest `DN/(4A)` when this lies above one, and `K=1` otherwise, proves (7). The estimate is translation-free and deterministic. It says that broadband Fourier mass can only coexist with small adjacent distortion if its total amplitude is correspondingly small.

## 3. XF-064 already contains an arbitrary-state nonlinear remainder estimate

The analytic expansion used in XF-064 is algebraic in the state. With the shifted envelope `g_c`, it reads

\[
\mathcal N_{M,a}
=
\mathcal L^{(c)}_{M,b}
+
\sum_{n+k\ge2}T^{(c)}_{n,k}[b^{n+k}],
\tag{31}
\]

because the uniformly translated baseline is zero on the outer band. Compact Fourier support still gives disjoint sidebands for each power `b^r`, and the discrete Wiener tame estimate preserves one copy of the third-difference norm.

Exactly as in XF-064, terms with `k>=1` satisfy

\[
\frac{\|T^{(c)}_{n,k}[b^{n+k}]\|_{X_T}}
{\mathcal Q_M(( -\pi,\pi];b)^{1/2}}
\ll_g
\frac{(n+k)^3}{n!k!}
\alpha^n\beta^{k-1},
\tag{32}
\]

while the pure-envelope terms `k=0`, `n>=2`, satisfy

\[
\frac{\|T^{(c)}_{n,0}[b^n]\|_{X_T}}
{\mathcal Q_M(( -\pi,\pi];b)^{1/2}}
\ll_g
\frac{n^3}{n!}
\theta_-^{-1}M^{-1}\alpha^{n-1}.
\tag{33}
\]

The factorials make the complete nonlinear series absolutely summable. If `alpha+beta` is below a fixed constant, the terms with total degree at least two sum to

\[
O_g(\alpha+\beta+\gamma),
\tag{34}
\]

which proves (15). The tangent semigroup in XF-064 was used only to deduce one convenient estimate for `W`; it is absent from (31)--(34).

## 4. The translated lattice has the same lower frame

XF-063 obtains its lower frame from Poisson summation and strict sideband disjointness: periodic Fourier spacing is `pi/M`, while `supp chi subset (-1,1)` gives sideband half-width `1/M`. Replacing `g` by `g_c` multiplies each sideband by a phase but changes neither its support nor its `L^2` mass. Therefore the XF-063 argument gives (16) with no dependence on `c`.

If (18) holds, then

\[
\mathcal Q_M(( -\pi,\pi];b)^{1/2}
=
(1+o(1))
\mathcal Q_M(B_T^{in}\cup-B_T^{in};b)^{1/2}.
\tag{35}
\]

Combining (15), (16), (17), and (35) with the reverse triangle inequality yields (19). Thus the exact finite-displacement response is framed whenever the **state itself** lies in the required geometric and spectral region, regardless of how it arrived there.

## 5. Scale reduction at `N=2q^2`

From `N=2M=2q^2`, equation (7) becomes

\[
W
\ll
A+q\sqrt{AD}.
\tag{36}
\]

Substitution into (10) gives

\[
\alpha
\ll
\frac{A}{q^2}
+
\frac{\sqrt{AD}}q,
\tag{37}
\]

\[
\beta
\ll
\frac{A\log\log T}{q}
+
(\log\log T)\sqrt{AD},
\tag{38}
\]

and

\[
\gamma
\ll
\frac{A}{q^{5/2}}
+
\frac{\sqrt{AD}}{q^{3/2}}.
\tag{39}
\]

Equations (37)--(39) prove (20). For `A=O(1)`, (21) follows immediately.

The contrast with XF-064 is deliberate. The tangent heat estimate `W=O(sqrt(q))` gives the sharper error `O(log log T/sqrt(q))` for arbitrary bounded initial tangents. The new state-space route gives only `O((log log T)sqrt(D))` under bounded oscillation. It is weaker numerically but stronger logically: it can be verified on a nonlinear state without proving that state is close to a tangent heat trajectory.

## 6. Stress tests and failure modes

A uniform translation has `b=0`, hence `A=D=W=0`, and both sides of the frame vanish. This removes a false dependence on absolute root position.

For a coherent slow displacement wave with `A=O(1)` and wavelength `asymp q`, one has `D=O(q^{-1})`. Then (38) gives `beta=O(log log T/sqrt(q))=o(1)` directly, even without invoking tangent heat. The measurement nonlinearity is therefore small for the geometric reason one would expect: neighboring roots move almost together.

The XF-061 sparse one-root defect passes the measurement-smallness test if its amplitude is scaled by `M^{-1}`, but it fails the band-concentration hypothesis (18) at time zero. This is not a loophole. XF-062 was introduced precisely because a static sparse defect can place critical third-difference mass outside the slow cone.

Conversely, a checkerboard or near-collision state with order-one adjacent distortion has `D=asymp1`, so (20)--(21) do not apply. The theorem does not cross collisions and does not claim that arbitrary finite-amplitude configurations are perturbative merely because the selector frequency tends to zero.

Finally, (18) is a relative concentration statement. Small measurement parameters alone do not prevent high-frequency `H^3` energy from dominating the state. The remaining dynamical problem cannot be reduced to pointwise gap regularity only.

## 7. Prior-art and novelty boundary

A targeted audit of nonuniform sampling, perturbed exponential bases, and classical frame stability again finds the neighboring Kadec/Paley--Wiener tradition and modern perturbed trigonometric interpolation results already noted in XF-064. Those theories study stability of sampling or exponential systems under node perturbation; they do not supply the Mathia-specific shrinking-band estimate (15), the third-difference normalization (14), or the state-space reduction (20) tied to the `q^2` Xi selector scale.

No external frame theorem is load-bearing here. Equations (7) and (15)--(20) follow from elementary discrete Fourier splitting plus the exact compact-sideband expansion already proved in XF-063--XF-064. No new `SOURCES.md` anchor is therefore required, and no broad novelty claim is made for Wiener interpolation or perturbation stability themselves.

## 8. Consequence for `xi_flow`

The nonlinear destination demanded by the current `xi_flow` frontier can now be stated without reference to a tangent trajectory. At a real-simple post-transition slice, it is enough to establish a finite-state package: nontrivial third-difference mass in the XF-063 inner band, negligible `H^3` mass outside that band, and displacement geometry satisfying (20) (or any stronger condition implying (17)). The exact moved Xi selector then has an order-one lower frame by (19), while XF-059--XF-060 make the corresponding source selector norm `o(1)`.

What remains genuinely dynamical is to show that a hypothetical positive-`Lambda` transition must pass through such a state **before its critical defect disappears**. One route is still a nonlinear-to-tangent Duhamel comparison, but it is no longer the only route. Direct nonlinear smoothing or entropy estimates that produce (18), together with a transition-defect survival theorem, would now suffice. This removes trajectory closeness itself from the list of indispensable conclusions and isolates the two state properties that actually feed the source contradiction.