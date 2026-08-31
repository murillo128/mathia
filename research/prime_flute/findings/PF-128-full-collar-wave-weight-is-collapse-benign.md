# PF-128 — the full collapsing collar is benign for the inverse-volume scattering weight

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-060 identified collapsing short collars as the main obstruction to importing bounded-geometry localization arguments, PF-127 showed that a fixed central part of a matched collapsing collar is Schatten-benign for every `S_r`, `r>1`, and the accepted sharp-Schatten clue records Güneysu--Thalmaier's inverse-unit-ball-volume criterion as a natural no-injectivity-radius scattering test. The present calculation treats the **entire standard collar**. A boundary-to-boundary comparison of collars with core lengths `L` and `L'=e^t L` has unweighted metric-deviation mass `O(|t|^q L)` in every `L^q`, `q>=1`, while the inverse-unit-ball-volume weighted `L^1` cost is only `O(|t|)`, uniformly as `L->0`. For PF-004 canonical prime/shift-clone separators, PF-109 gives `|t|=O(P^-3)`, so collapse does not amplify the matched deformation in this scattering weight. This is a local thin-part result only: it does not sum all thin components, control collar/body commutators, prove global wave operators, or prove a Schatten class for the complete relative resolvent.

## Claim

For `0<L<L_0`, let

\[
C_L=(-w(L),w(L))\times \mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

with the standard hyperbolic collar metric

\[
g_L=dr^2+L^2\cosh^2r\,d\theta^2,
\qquad \theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Let

\[
L'=e^tL,
\qquad |t|\le t_0,
\tag{3}
\]

where `t_0` is fixed, and choose `L_0=L_0(t_0)` small enough that both collars are in the pinching regime. Put

\[
A(L):=\frac{L}{\sinh(L/2)}.
\tag{4}
\]

The exact area coordinate

\[
\boxed{x=L\sinh r}
\tag{5}
\]

identifies the full collar with

\[
(-A(L),A(L))\times\mathbb S^1
\]

and gives

\[
\boxed{
g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2,
\qquad d\mu_L=dx\,d\theta.}
\tag{6}
\]

Define

\[
\alpha:=\frac{A(L')}{A(L)}
\tag{7}
\]

and map the two **full** collars boundary-to-boundary by

\[
\Phi_{L,L'}(x,\theta)=(\alpha x,\theta).
\tag{8}
\]

If `h:=Phi_{L,L'}^*g_{L'}`, then relative to `g_L` its two pointwise metric eigenvalues are

\[
\boxed{
\lambda_r(x)=\frac{x^2+L^2}{x^2+c},
\qquad
\lambda_\theta(x)=\alpha^2\frac{x^2+c}{x^2+L^2},
\qquad
c:=\left(\frac{L'}\alpha\right)^2.}
\tag{9}
\]

Let

\[
D_{L,L'}(x)
:=
\max\bigl\{|\log\lambda_r(x)|,|\log\lambda_\theta(x)|,|\log\alpha|\bigr\}.
\tag{10}
\]

Then, uniformly for `|t|<=t_0` and sufficiently small `L`, there is a constant depending only on `t_0` such that

\[
\boxed{
D_{L,L'}(x)
\le
C_{t_0}|t|\frac{L^2}{x^2+L^2}
\qquad (|x|<A(L)).}
\tag{11}
\]

Consequently, for every `q>=1`,

\[
\boxed{
\int_{C_L}D_{L,L'}^q\,d\mu_L
\le C_{q,t_0}|t|^q L.}
\tag{12}
\]

There is also a universal `c_0>0` such that every point `z=(x,theta)` in a sufficiently short embedded standard collar satisfies the ambient unit-ball lower bound

\[
\boxed{
\mu_L(B_{g_L}(z,1))
\ge
c_0\min\left\{1,\sqrt{L^2+x^2}\right\}.}
\tag{13}
\]

Therefore

\[
\boxed{
\int_{C_L}
\frac{D_{L,L'}(z)}{\mu_L(B_{g_L}(z,1))}
\,d\mu_L(z)
\le C_{t_0}|t|.}
\tag{14}
\]

The zeroth-order metric deviation `delta_{g,h}` of Güneysu--Thalmaier is, in dimension two and under the present uniform quasi-isometry bound, comparable above by `D_{L,L'}`. Thus the same local estimate holds with their deviation:

\[
\boxed{
\int_{C_L}
\mu_L(B_{g_L}(z,1))^{-1}
\delta_{g_L,h}(z)
\,d\mu_L(z)
\le C_{t_0}|t|.}
\tag{15}
\]

Equation (15) is only a **local contribution** to their global scattering criterion; no completeness of wave operators is inferred here.

Finally, for a PF-004 canonical separating geodesic whose four endpoint labels lie in a tail beginning at a prime `P`, let `L` be its exact prime-flute length and `L_+` the matched exact shift-clone length. PF-109 gives

\[
\left|\log\frac{L_+}{L}\right|=O(P^{-3})
\tag{16}
\]

uniformly even when `L->0`. Hence the full standard collar obeys

\[
\boxed{
\int_{C_L}D_{L,L_+}^q\,d\mu_L
=O(P^{-3q}L),
\qquad
\int_{C_L}
\frac{\delta_{g_L,h_+}}{\mu_L(B(z,1))}
\,d\mu_L
=O(P^{-3}).}
\tag{17}
\]

So the loss of injectivity radius consumes at most the geometric `L` suppression in the unweighted `L^1` defect; it does **not** turn a matched `O(P^-3)` logarithmic length change into a larger local scattering cost.

## 1. Exact area coordinates turn the growing-width collar into a bounded strip

From (5),

\[
dx=L\cosh r\,dr,
\qquad
L^2\cosh^2r=L^2+x^2.
\]

Substituting into (2) proves (6). At the standard collar boundary,

\[
|x|
=L\sinh w(L)
=\frac{L}{\sinh(L/2)}
=A(L),
\tag{18}
\]

so the coordinate domain has bounded width even though

\[
w(L)\sim\log(4/L)\to\infty.
\]

Indeed,

\[
A(L)=2-\frac{L^2}{12}+O(L^4).
\tag{19}
\]

This is the first useful cancellation: the full standard collar has area

\[
2A(L)=4+O(L^2),
\]

and its growing Fermi width is exactly absorbed by the shrinking angular circumference.

Under (8), the target metric pulls back as

\[
\begin{aligned}
h
&=
\frac{\alpha^2dx^2}{L'^2+\alpha^2x^2}
+
(L'^2+\alpha^2x^2)d\theta^2\\
&=
\frac{dx^2}{x^2+c}
+
\alpha^2(x^2+c)d\theta^2,
\end{aligned}
\tag{20}
\]

which gives (9). Its pulled-back area density is exactly

\[
d\mu_h=\alpha\,dx\,d\theta.
\tag{21}
\]

Thus the volume-ratio deviation is also governed by `log alpha`.

## 2. The metric deformation is concentrated on an area-`O(L)` core

Differentiate `log A(L)` with respect to logarithmic length:

\[
\frac{d}{d\log L}\log A(L)
=
1-\frac L2\coth\frac L2
=O(L^2).
\tag{22}
\]

Integrating (22) from `L` to `L'=e^tL` gives

\[
\boxed{|\log\alpha|\le C_{t_0}|t|L^2.}
\tag{23}
\]

Also

\[
\frac c{L^2}
=\frac{e^{2t}}{\alpha^2},
\tag{24}
\]

so, for bounded `t`,

\[
|c-L^2|\le C_{t_0}|t|L^2,
\qquad
c\asymp_{t_0}L^2.
\tag{25}
\]

The first eigenvalue in (9) therefore satisfies

\[
|\log\lambda_r(x)|
\le
C_{t_0}|t|\frac{L^2}{x^2+L^2}.
\tag{26}
\]

Since

\[
\log\lambda_\theta=2\log\alpha-\log\lambda_r,
\tag{27}
\]

(23), (26), and the bounded coordinate range `|x|<=A(L)` imply (11).

At `x=0` the metric change is genuinely of order `|t|`; for example `lambda_theta(0)=e^{2t}` exactly. The small integral in (12) is therefore **not** a uniform-norm artifact. It comes from localization: order-one relative distortion is confined to `|x|=O(L)`, while away from the core it decays like `L^2/x^2`.

For `q>=1`, (11) and (6) give

\[
\begin{aligned}
\int_{C_L}D^q\,d\mu_L
&\le
C|t|^q
\int_{-A(L)}^{A(L)}
\left(\frac{L^2}{x^2+L^2}\right)^qdx\\
&=
C|t|^qL
\int_{-A(L)/L}^{A(L)/L}
(1+u^2)^{-q}du\\
&\le C_{q,t_0}|t|^qL,
\end{aligned}
\tag{28}
\]

proving (12). In fact the same calculation works for every `q>1/2`; only `q>=1` is needed here.

## 3. Collapse of unit-ball volume cancels exactly one factor of `L`

Set

\[
s(x):=L\cosh r=\sqrt{L^2+x^2}.
\tag{29}
\]

This is the circumference scale of the parallel curve through `(r,theta)`. We prove (13) directly inside the embedded collar, so no ambient injectivity-radius estimate is imported.

Fix a small universal `eta>0`, say `eta=1/8`. For `L` sufficiently small the collar width is much larger than `eta`. From any point of the collar, at least one of the two radial directions contains an interval of length `eta` staying inside the collar. Along such an interval,

\[
e^{-\eta}s(x)
\le L\cosh(r+u)
\le e^{\eta}s(x),
\tag{30}
\]

because `|d(log cosh r)/dr|=|tanh r|<=1`.

Take an angular interval whose normalized `theta`-width is a fixed small multiple of

\[
\min\{1,s(x)^{-1}\}.
\]

Every point in the resulting one-sided Fermi rectangle can be joined to the center by first moving radially and then angularly with total length below `1`, while its area is bounded below by a universal multiple of

\[
\eta\,s(x)\min\{1,s(x)^{-1}\}
=\eta\min\{s(x),1\}.
\]

The rectangle lies inside the embedded collar and inside `B(z,1)`, proving (13).

Now combine (11), (13), and `dmu=dx dtheta`. On the region `s(x)<=1`,

\[
\frac{D(x)}{\mu(B(z,1))}
\le
C|t|\frac{L^2}{(x^2+L^2)^{3/2}},
\tag{31}
\]

and

\[
L^2\int_{-1}^{1}
\frac{dx}{(x^2+L^2)^{3/2}}
\le 2.
\tag{32}
\]

On the complementary part of the bounded `x`-strip the unit-ball volume has a positive lower bound and the integral is `O(|t|L^2)`. This proves (14).

For Güneysu--Thalmaier, if `A_{g,h}` is the positive cotangent-bundle comparison endomorphism in dimension `m=2`, their deviation is

\[
\delta_{g,h}(z)
=2\sinh\left(
\frac12
\max_{\lambda\in\operatorname{spec}A_{g,h}(z)}
|\log\lambda|
\right).
\tag{33}
\]

The eigenvalues of `A_{g,h}` are reciprocal to the corresponding tangent-metric eigenvalues, so the maximum logarithmic deviation is the same quantity controlled in (10), up to the included density term. For `|t|<=t_0`, `D` is uniformly bounded, hence

\[
\delta_{g,h}\le C_{t_0}D.
\tag{34}
\]

Equations (14) and (34) give (15). The same estimate holds, with changed constants, if the target metric is used in the ball-volume weight, because `g_L` and `h` are uniformly quasi-isometric for bounded `t`.

## 4. What this removes from the global operator/scattering frontier

PF-127 treated only a fixed central Fermi collar `|r|<R`. A possible remaining failure mode was that the **rest** of the standard collar, whose width grows like `log(1/L)`, might reintroduce a divergent geometric weight when unit-ball volumes collapse.

PF-128 removes that mechanism at the metric-deviation level. The full collar admits an exact boundary-to-boundary comparison in which

```text
full Fermi width              ~ log(1/L)
area-coordinate width         ~ 4
unweighted L^1 metric defect  = O(|t| L)
unit-ball inverse penalty     ~ 1/sqrt(L^2+x^2)
weighted collar cost          = O(|t|).
```

For the exact prime/shift control, PF-109 inserts the much smaller

\[
|t|=O(P^{-3}),
\]

so each matched canonical pinching collar contributes `O(P^-3)` rather than an amplified reciprocal-gap or reciprocal-length term.

This is still **not** enough to apply the global Güneysu--Thalmaier corollary. One would have to show that the complete metric comparison can be arranged so that the weighted deviation is integrable over *all* of the surface, including pant bodies, cusp transition zones, collar/body interfaces, and every thin component relevant to the ambient unit-ball function. Nor does (15) imply a Schatten estimate: Güneysu--Thalmaier's theorem is a wave-operator criterion, not a Schatten theorem.

The surviving sharp-Schatten clue is therefore narrowed once more. A failure of global `S_r`, `r>1`, or of the corresponding wave/scattering comparison can no longer be attributed merely to the unbounded width of a single standard collapsing collar under the matched deformation. It must come from global assembly, from an uncontrolled family of thin components, or from an operator/interface effect not captured by the zeroth-order metric weight.

## 5. Prior art and novelty audit

No novelty is claimed for the collar lemma, Fermi coordinates, the formula `g=dr^2+L^2 cosh^2(r)dtheta^2`, elementary changes of variables, or local volume estimates inside an embedded collar. The coordinate `x=L sinh r` is simply the exact area coordinate for this standard model.

The relevant operator-theoretic prior art is B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, arXiv:1709.01612. Their Corollary A shows that for complete quasi-isometric metrics with Ricci curvature bounded below, finiteness of

\[
\int \mu_j(x,1)^{-1}\delta_{g,h}(x)\,d\mu_j(x)
\]

(for one of the metrics) implies existence and completeness of the two-Hilbert-space wave operators. They deliberately remove any injectivity-radius assumption. PF-128 does **not** reprove or strengthen that theorem; it computes its potentially dangerous local weight on the matched degenerating collar.

Directed searches for the combination of hyperbolic standard-collar degeneration, metric comparison under `L'/L=e^t`, the Güneysu--Thalmaier inverse-volume weight, and relative/Schatten resolvent estimates did not locate the exact bounds (11)--(17). The durable Mathia content is narrower and project-specific:

\[
\boxed{
\text{PF-109 matched prime/shift pinching}
+
\text{full exact collar area coordinate}
\Longrightarrow
\text{no local inverse-volume amplification beyond }O(P^{-3}).
}
\]

This is an adversarial boundary result. The same collar estimate holds for arbitrary matched hyperbolic collars and is therefore **not prime-specific**; its value is that it removes a natural noncompactness obstruction from the all-composite control program rather than producing an RH signal.

## 6. Audit / falsification core

A later review can check the result through the following finite chain:

1. verify the standard collar width (1), metric (2), and boundary identity `L sinh w(L)=L/sinh(L/2)`;
2. substitute `x=L sinh r` and verify both the exact metric and exact area density in (6);
3. check that `Phi(x,theta)=(alpha x,theta)` maps the full source collar boundary to the full target collar boundary and derive (9), (20), and (21);
4. differentiate `log A(L)` to obtain (22), then prove (23)--(25) for bounded `t`;
5. derive the pointwise logarithmic metric-deviation bound (11), noting explicitly that the core distortion remains order `|t|`;
6. integrate the exact profile to obtain (12);
7. construct the one-sided Fermi rectangle inside `B(z,1)` and verify the volume lower bound (13);
8. compute the elementary weighted integral (31)--(32) to obtain (14);
9. compare the logarithmic metric eigenvalue bound with Güneysu--Thalmaier's exact deviation (33) to obtain the **local** criterion contribution (15), without claiming the global theorem's hypothesis;
10. insert PF-109's uniform canonical-separator estimate only at the final specialization (16)--(17).

A refutation would have to break one of these explicit geometric identities or inequalities. A later failure to sum all collars or control global interfaces would not refute PF-128; it would identify precisely the still-open global obstruction that this finding excludes from its claim.