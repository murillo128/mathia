# AF-131 — Wasserstein recovery composition needs transport regularity

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `WASSERSTEIN-RECOVERY`, `COMPOSITION-GATE`, `QUANTITATIVE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-126 shows that ordinary total-variation recovery deficiency has a directed triangle inequality: approximate recovery errors compose subadditively because every Markov kernel contracts total variation. AF-130 replaces total variation by normalized Wasserstein-1 recovery when admissible witnesses are metric-local. That replacement changes the composition law in a load-bearing way. **A scalar Wasserstein recovery defect does not compose by itself across changing retained metrics; one must also control the transport regularity of the intermediate recovery map.**

Let

\[
\mathcal A=(P_\theta)_{\theta\in\Theta},\qquad
\mathcal B=(Q_\theta)_{\theta\in\Theta},\qquad
\mathcal C=(S_\theta)_{\theta\in\Theta}
\]

be finite experiments on finite metric spaces `(X,d_X)`, `(Y,d_Y)`, and `Z`, respectively. Assume `X` and `Y` have positive diameters

\[
D_X=\operatorname{diam}(X),\qquad
D_Y=\operatorname{diam}(Y).
\]

Define the directed normalized Wasserstein recovery defect

\[
\delta_X(\mathcal A\mid\mathcal B)
:=
\inf_{R:Y\rightsquigarrow X}
\max_\theta
\frac{W_{1,d_X}(P_\theta,Q_\theta R)}{D_X}.
\tag{1}
\]

For a recovery kernel `R:Y\rightsquigarrow X`, define its **normalized transport Lipschitz coefficient**

\[
\bar\kappa(R)
:=
\sup_{y\ne y'}
\frac{W_{1,d_X}(R_y,R_{y'})/D_X}
     {d_Y(y,y')/D_Y}
=
\frac{D_Y}{D_X}
\sup_{y\ne y'}
\frac{W_{1,d_X}(R_y,R_{y'})}{d_Y(y,y')}.
\tag{2}
\]

Also write

\[
e_X(R;\mathcal A,\mathcal B)
:=
\max_\theta
\frac{W_{1,d_X}(P_\theta,Q_\theta R)}{D_X}.
\tag{3}
\]

Then every intermediate recovery kernel satisfies the exact composition bound

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
 e_X(R;\mathcal A,\mathcal B)
 +
 \bar\kappa(R)\,
 \delta_Y(\mathcal B\mid\mathcal C).
}
\tag{4}
\]

Consequently

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
\inf_R
\left[
 e_X(R;\mathcal A,\mathcal B)
 +
 \bar\kappa(R)\,
 \delta_Y(\mathcal B\mid\mathcal C)
\right].
}
\tag{5}
\]

For `L>=0`, define the `L`-regular recovery defect

\[
\delta_{X,\le L}(\mathcal A\mid\mathcal B)
:=
\inf_{\bar\kappa(R)\le L}
 e_X(R;\mathcal A,\mathcal B).
\tag{6}
\]

Then

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
\delta_{X,\le L}(\mathcal A\mid\mathcal B)
+
L\,\delta_Y(\mathcal B\mid\mathcal C).
}
\tag{7}
\]

Thus the ordinary unit-coefficient triangle law survives in the metric-local category only when the relevant recovery can be chosen normalized-Wasserstein nonexpansive, `\bar\kappa(R)<=1`. Exact recoverability alone is insufficient.

This is not merely a weakness of the proof. There are genuine finite compression chains for which

\[
\delta_X(\mathcal A\mid\mathcal B)=0,
\qquad
\delta_Y(\mathcal B\mid\mathcal C)=\varepsilon/2,
\qquad
\delta_X(\mathcal A\mid\mathcal C)=1/2,
\tag{8}
\]

for every `0<epsilon<1`. Hence

\[
\delta_X(\mathcal A\mid\mathcal C)
>
\delta_X(\mathcal A\mid\mathcal B)
+
\delta_Y(\mathcal B\mid\mathcal C).
\tag{9}
\]

In the same example every exact recovery from `B` to `A` has

\[
\bar\kappa(R)\ge1/\varepsilon,
\tag{10}
\]

and the amplification term in `(4)` is sharp:

\[
\frac1\varepsilon\cdot\frac\varepsilon2=\frac12.
\tag{11}
\]

The correct compositional object for metric-local fidelity is therefore not the scalar defect alone. It is at least the **error/regularity tradeoff** of admissible recovery maps. A convenient summary is the recovery profile

\[
\Phi_{\mathcal A\mid\mathcal B}(t)
:=
\inf_R
\left[e_X(R;\mathcal A,\mathcal B)+t\bar\kappa(R)\right],
\tag{12}
\]

for which `(5)` becomes

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
\Phi_{\mathcal A\mid\mathcal B}
\!\left(\delta_Y(\mathcal B\mid\mathcal C)\right).
}
\tag{13}
\]

A representation can therefore be exactly recoverable at one stage while remaining compositionally fragile because every exact inverse expands short retained distances into order-one source distances.

## Derivation

### A Markov recovery kernel transports Wasserstein error by its Lipschitz coefficient

For probability measures `mu,nu` on `Y`, a finite Markov kernel `R:Y\rightsquigarrow X` satisfies

\[
W_{1,d_X}(\mu R,\nu R)
\le
\kappa(R)W_{1,d_Y}(\mu,\nu),
\tag{14}
\]

where

\[
\kappa(R)
:=
\sup_{y\ne y'}
\frac{W_{1,d_X}(R_y,R_{y'})}{d_Y(y,y')}.
\tag{15}
\]

One direct proof uses Kantorovich--Rubinstein duality. If `f:X->R` is `1`-Lipschitz, then

\[
(Rf)(y):=\sum_x R(x\mid y)f(x)
\]

obeys

\[
|(Rf)(y)-(Rf)(y')|
\le
W_{1,d_X}(R_y,R_{y'})
\le
\kappa(R)d_Y(y,y').
\tag{16}
\]

Thus `Rf` is `kappa(R)`-Lipschitz on `Y`, and duality gives `(14)`. After dividing the two Wasserstein distances by their respective diameters, `(14)` becomes

\[
\frac{W_{1,d_X}(\mu R,\nu R)}{D_X}
\le
\bar\kappa(R)
\frac{W_{1,d_Y}(\mu,\nu)}{D_Y}.
\tag{17}
\]

The coefficient `(15)` is the standard Wasserstein/Dobrushin-type contraction coefficient of the kernel; Ollivier's coarse Ricci curvature uses exactly the same local ratio in the same-metric Markov-chain setting.

### Composition carries recovery error through the intermediate inverse

Fix recovery kernels

\[
R:Y\rightsquigarrow X,
\qquad
T:Z\rightsquigarrow Y.
\]

For every parameter `theta`, the triangle inequality and `(17)` give

\[
\begin{aligned}
\frac{W_{1,d_X}(P_\theta,S_\theta T R)}{D_X}
&\le
\frac{W_{1,d_X}(P_\theta,Q_\theta R)}{D_X}
+
\frac{W_{1,d_X}(Q_\theta R,S_\theta T R)}{D_X}\\
&\le
 e_X(R;\mathcal A,\mathcal B)
+
\bar\kappa(R)
\frac{W_{1,d_Y}(Q_\theta,S_\theta T)}{D_Y}.
\end{aligned}
\tag{18}
\]

Take the maximum over `theta`, then minimize over `T`. Finite compactness gives an optimizer for the second-stage recovery, yielding `(4)`. Minimizing over `R` gives `(5)`, and restricting to `\bar\kappa(R)<=L` gives `(7)`.

Compare this with AF-126. For total variation every stochastic map has contraction coefficient at most one, independent of any extra geometry. That universal fact is exactly why ordinary Le Cam deficiency has an unweighted directed triangle inequality. Wasserstein recovery has no analogous universal unit bound when the intermediate inverse is allowed to expand the declared metric.

### A three-state compression chain makes the failure exact

Fix `0<epsilon<1`. Let

\[
X=\{0,1,2\}
\]

with the equilateral metric

\[
d_X(i,j)=1\qquad(i\ne j),
\tag{19}
\]

so `D_X=1`. Let

\[
Y=\{a,b,c\}
\]

with

\[
d_Y(a,b)=\varepsilon,
\qquad
d_Y(a,c)=d_Y(b,c)=1,
\tag{20}
\]

so `D_Y=1`. Take `Theta={0,1,2}` and the source experiment

\[
P_0=\delta_0,
\qquad
P_1=\delta_1,
\qquad
P_2=\delta_2.
\tag{21}
\]

The first deterministic compression `K:X->Y` sends

\[
0\mapsto a,
\qquad
1\mapsto b,
\qquad
2\mapsto c.
\tag{22}
\]

Thus

\[
Q_0=\delta_a,
\qquad
Q_1=\delta_b,
\qquad
Q_2=\delta_c.
\tag{23}
\]

As a set map this compression is bijective, so the deterministic inverse recovers `A` exactly and

\[
\delta_X(\mathcal A\mid\mathcal B)=0.
\tag{24}
\]

But every exact recovery must send `a` to `delta_0` and `b` to `delta_1`. Therefore

\[
\bar\kappa(R)
\ge
\frac{W_{1,d_X}(\delta_0,\delta_1)}{d_Y(a,b)}
=
\frac1\varepsilon.
\tag{25}
\]

The first compression has preserved exact identity while squeezing two source states from distance `1` to distance `epsilon`; its inverse is necessarily expansive.

Now apply a second deterministic compression `L:Y->Z` that merges `a` and `b` but keeps `c` separate:

\[
a,b\mapsto u,
\qquad
c\mapsto v.
\tag{26}
\]

Then the final experiment is

\[
S_0=S_1=\delta_u,
\qquad
S_2=\delta_v.
\tag{27}
\]

To recover `B` from `C`, choose after `u` the measure

\[
\mu=\frac12\delta_a+\frac12\delta_b
\]

and after `v` return `delta_c`. This gives worst-case Wasserstein error `epsilon/2`. No recovery can do better, because for every candidate measure `mu`,

\[
\varepsilon
=W_{1,d_Y}(\delta_a,\delta_b)
\le
W_{1,d_Y}(\delta_a,\mu)
+
W_{1,d_Y}(\mu,\delta_b),
\tag{28}
\]

so at least one of the first two errors is at least `epsilon/2`. Hence

\[
\delta_Y(\mathcal B\mid\mathcal C)=\frac\varepsilon2.
\tag{29}
\]

For direct recovery of `A` from `C`, the same argument on the equilateral pair `0,1` gives

\[
\delta_X(\mathcal A\mid\mathcal C)=\frac12.
\tag{30}
\]

Equations `(24)`, `(29)`, and `(30)` prove `(8)`--`(9)`. The exact inverse of `(22)` has normalized coefficient `1/epsilon`, and applying `(4)` yields exactly

\[
0+\frac1\varepsilon\frac\varepsilon2=\frac12,
\]

so the regularity factor is not an artifact of a loose estimate.

## Relationship to AF-126, AF-129, and AF-130

AF-126's total-variation deficiency has a directed triangle inequality because total variation is contracted by every stochastic recovery kernel. AF-129 shows that restricting witnesses changes the dual recovery geometry, and AF-130 identifies metric-local witnesses with normalized Wasserstein-1 recovery.

AF-131 shows that this category change also changes **composition**. Once the defect is metric-sensitive, the downstream error must be transported through the chosen upstream recovery. Its amplification is controlled by the recovery kernel's Wasserstein Lipschitz coefficient. The scalar value `delta_X(A|B)` forgets that regularity and is therefore not sufficient to predict stability under later compression.

This supplies a precise version of the README's composition question. For metric-local fidelity, an exact stagewise inverse is not enough; one needs an inverse whose modulus is compatible with the metric retained at the intermediate layer. The profile `(12)` records the resulting Pareto tradeoff between approximation accuracy and metric amplification.

## Prior art and novelty assessment

The ingredients are classical.

- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419--1455 (1964), DOI `10.1214/AOMS/1177700372`. Role: classical deficiency/approximate-sufficiency framework and the total-variation composition background used in AF-126.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), especially Chapter 6, DOI `10.1017/CBO9780511666353.007`. Role: authoritative treatment of deficiencies, distances, and comparison relative to restricted decision classes; direct prior art for AF-129's decision-class-relative viewpoint.
- Yann Ollivier, **“Ricci curvature of Markov chains on metric spaces,”** *Journal of Functional Analysis* 256(3), 810--864 (2009), DOI `10.1016/j.jfa.2008.11.001`. Role: primary prior art for measuring a Markov kernel by the local Wasserstein ratio `W_1(R_y,R_{y'})/d(y,y')`; positive coarse Ricci curvature is precisely a contraction statement of this type.
- D. A. Edwards, **“On the Kantorovich--Rubinstein theorem,”** *Expositiones Mathematicae* 29(4), 387--398 (2011), DOI `10.1016/j.exmath.2011.06.005`. Role: authoritative KR duality background for the Lipschitz proof of `(14)` and the metric-local witness geometry already used in AF-130.

A targeted literature search did not justify treating `(4)`--`(13)` as a new theorem of probability, optimal transport, or statistical decision theory. The contraction estimate `(14)` is standard, and restricted deficiencies are classical. The result is best classified as a direct finite synthesis of those languages plus an explicit sharp counterexample to the naive unit-triangle rule. No novelty claim is made.

The Arithmetic Fidelity value is the resulting audit principle: **when the admissible witness geometry changes with the retained representation, composition requires carrying the regularity of the recovery map, not merely its reconstruction error.**

## Boundary conditions and falsification checks

1. **The metrics must be independently justified.** A metric chosen after seeing the desired inverse can hide its expansion. The coefficient `bar-kappa` is meaningful only when `d_X` and `d_Y` belong to the declared retained/source structure.

2. **Diameter normalization is part of the claim.** It removes arbitrary global rescaling of each metric. The counterexample does not rely on an unused diameter witness: all three source and intermediate states occur as hypotheses, and the third state supplies the genuine order-one scale against which `a` and `b` become close.

3. **Exact recovery does not imply regular recovery.** Equation `(25)` is the decisive finite obstruction. Any application that proves only a set-theoretic or stochastic inverse has not controlled downstream metric stability.

4. **The coefficient is recovery-dependent.** A non-optimal reconstruction error may buy a much smaller transport coefficient. For composition the correct object is therefore the tradeoff profile `(12)` or a constrained defect such as `(6)`, not the Lipschitz constant of one arbitrarily selected inverse.

5. **The unit triangle is recovered under a genuine regularity gate.** If an `L=1` recovery is available at the relevant first-stage error, `(7)` gives the ordinary subadditive law. More generally the exact multiplier is the admitted normalized transport modulus.

6. **No prime-specific conclusion follows.** The theorem does not supply a canonical metric or regular inverse for any prime-derived construction. A concrete RH application must derive both the retained metric and a non-collapsing recovery profile from its own mathematics.

## Consequences for Arithmetic Fidelity

AF-130 showed that metric-local witnesses can preserve exact distinguishability on every finite metric space while weakening short-scale differences. AF-131 adds the compositional consequence: **short-scale squeezing can be harmless at one stage and catastrophic after a later merge, because the exact inverse must re-expand the squeezed scale.**

For future geometric, spectral, or arithmetic pipelines, stagewise claims of `zero defect` are therefore not compositional certificates in a metric-sensitive category. Each stage must propagate an admissible inverse modulus, or equivalently enough of the error/regularity profile to control the next transformation. This is a concrete instance of the broader Arithmetic Fidelity principle that a property can survive an individual compression yet fail to survive a pipeline unless the structure needed to transport that property is itself retained.