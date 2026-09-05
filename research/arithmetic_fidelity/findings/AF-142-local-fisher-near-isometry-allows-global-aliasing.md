# AF-142 — Local Fisher near-isometry allows persistent global aliasing

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `QUANTITATIVE-SEPARATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-141 identifies Fisher-information loss under a parameter-independent statistical compression with the conditional score-projection defect. A natural quantitative hope is that if this defect is uniformly tiny — equivalently, if the compressed Fisher metric is arbitrarily close to the source Fisher metric — then the whole statistical experiment should be approximately recoverable.

That implication is false without an additional **global identifiability / no-aliasing gate**.

There is a sequence of one-dimensional, connected, strictly positive, smooth statistical models and deterministic parameter-independent compressions for which:

1. the compressed Fisher metric is a uniform near-isometry,
   \[
   I_{Y,n}(\theta)=\delta_n^2 I_{X,n}(\theta),
   \qquad
   \delta_n=\frac{n}{\sqrt{n^2+1}}\longrightarrow1;
   \tag{1}
   \]
2. nevertheless two distinct parameter values remain **exactly aliased after compression**;
3. the recovery/Le Cam deficiency of the full experiment is bounded below by one fixed positive constant independent of `n`.

Consequently there is no universal function `F` with

\[
F(\delta)\longrightarrow0
\qquad(\delta\uparrow1)
\tag{2}
\]

such that every statistical compression satisfying the Fisher lower bound

\[
I_Y(\theta)\succeq \delta^2 I_X(\theta)
\qquad\text{for all }\theta
\tag{3}
\]

must satisfy a whole-experiment recovery bound

\[
\delta_{\rm rec}\le F(\delta).
\tag{4}
\]

Thus **near-perfect local/tangent fidelity does not control global recoverability**. A compression may preserve every infinitesimal parameter direction almost isometrically while folding distant parameter values onto exactly the same retained law.

## Construction

Let

\[
\mathbb T=\mathbb R/(2\pi\mathbb Z)
\]

and fix the strictly positive smooth density

\[
q(u)=\frac{e^{\cos u}}{Z},
\qquad
Z=\int_0^{2\pi}e^{\cos u}\,du.
\tag{5}
\]

Write

\[
J:=\int_0^{2\pi}\sin^2(u)q(u)\,du>0.
\tag{6}
\]

Take the connected open parameter interval

\[
\Theta=\left(-\frac14,\pi+\frac14\right)\subset\mathbb R.
\tag{7}
\]

For every even integer `n>=2`, define the source observation

\[
X_n=(Y_n,Z_n)\in\mathbb T^2
\]

by conditional independence given `theta` and

\[
Y_n\mid\theta\sim q(y-n\theta)\,dy,
\qquad
Z_n\mid\theta\sim q(z-\theta)\,dz.
\tag{8}
\]

Equivalently,

\[
p_{n,\theta}(y,z)
=q(y-n\theta)q(z-\theta).
\tag{9}
\]

Compress deterministically by forgetting the second coordinate:

\[
K_n(y,z)=y.
\tag{10}
\]

All source and retained densities are smooth and strictly positive. The channel is independent of `theta`. The source experiment is globally identifiable on `Theta`: equality of the `Z_n` laws forces parameter equality modulo `2pi`, and the interval diameter is strictly less than `2pi`.

## Fisher near-isometry

Because

\[
\log q(u)=\cos u-\log Z,
\]

the source score is

\[
S_{X,n,\theta}(Y_n,Z_n)
=n\sin(Y_n-n\theta)+\sin(Z_n-\theta).
\tag{11}
\]

The retained score is

\[
S_{Y,n,\theta}(Y_n)
=n\sin(Y_n-n\theta).
\tag{12}
\]

Both sine terms have mean zero under their translated `q` laws. Conditional independence therefore gives

\[
I_{X,n}(\theta)
=\mathbb E_\theta[S_{X,n,\theta}^2]
=(n^2+1)J,
\tag{13}
\]

while

\[
I_{Y,n}(\theta)
=\mathbb E_\theta[S_{Y,n,\theta}^2]
=n^2J.
\tag{14}
\]

Hence for every `theta in Theta`,

\[
\boxed{
I_{Y,n}(\theta)
=\frac{n^2}{n^2+1}I_{X,n}(\theta)
=\delta_n^2 I_{X,n}(\theta),
\qquad
\delta_n=\frac{n}{\sqrt{n^2+1}}.
}
\tag{15}
\]

In the terminology of Yamaguchi--Nozawa, the statistic is therefore `delta_n`-almost sufficient from the viewpoint of Fisher metrics, and

\[
\delta_n\uparrow1.
\tag{16}
\]

AF-141 gives the same calculation as a score-projection defect: the entire lost Fisher information is the order-one `Z_n` score variance `J`, while the retained `Y_n` score energy grows like `n^2J`. Relative local distortion therefore vanishes even though the discarded coordinate continues to carry a fixed global distinction.

## Exact global aliasing

Choose the two interior parameter values

\[
\theta_0=0,
\qquad
\theta_1=\pi.
\tag{17}
\]

Because `n` is even,

\[
n\pi\in2\pi\mathbb Z.
\]

Therefore the retained distributions coincide exactly:

\[
q(y-n\theta_0)=q(y)
=q(y-n\theta_1),
\tag{18}
\]

so

\[
\boxed{
P_{n,0}K_n=P_{n,\pi}K_n.
}
\tag{19}
\]

The source distributions do not coincide. Their `Y_n` factors are common, but their `Z_n` factors are

\[
q(z)\,dz
\quad\text{and}\quad
q(z-\pi)\,dz.
\tag{20}
\]

Set

\[
c:=\left\|q(z)\,dz-q(z-\pi)\,dz\right\|_{\rm TV}.
\tag{21}
\]

Since

\[
q(z-\pi)=\frac{e^{-\cos z}}{Z}
\]

and this is not equal almost everywhere to `q(z)`,

\[
c>0.
\tag{22}
\]

Tensoring both measures with the same `Y_n` law preserves total variation, hence

\[
\boxed{
\|P_{n,0}-P_{n,\pi}\|_{\rm TV}=c
\qquad\text{for every even }n.
}
\tag{23}
\]

The compression has therefore turned two source laws separated by a fixed positive amount into one identical retained law.

## Whole-experiment recovery remains bounded away from zero

For the full experiment

\[
\mathcal E_n=(P_{n,\theta})_{\theta\in\Theta},
\]

define recovery deficiency exactly as in AF-126, now with the supremum over this continuous parameter family:

\[
\delta_{\rm rec}(K_n;\mathcal E_n)
:=
\inf_R
\sup_{\theta\in\Theta}
\left\|
P_{n,\theta}-(P_{n,\theta}K_n)R
\right\|_{\rm TV},
\tag{24}
\]

where `R` ranges over Markov kernels from the retained observation space back to the source space.

The pairwise lower-bound argument of AF-126 does not require finiteness of the parameter family. For every proposed recovery `R`, applying the triangle inequality to `theta_0=0` and `theta_1=pi`, then using contraction of total variation under `R`, gives

\[
2\sup_\theta
\|P_{n,\theta}-(P_{n,\theta}K_n)R\|_{\rm TV}
\ge
\|P_{n,0}-P_{n,\pi}\|_{\rm TV}
-
\|P_{n,0}K_n-P_{n,\pi}K_n\|_{\rm TV}.
\tag{25}
\]

By `(19)` and `(23)`,

\[
2\sup_\theta
\|P_{n,\theta}-(P_{n,\theta}K_n)R\|_{\rm TV}
\ge c.
\tag{26}
\]

Taking the infimum over `R` yields

\[
\boxed{
\delta_{\rm rec}(K_n;\mathcal E_n)
\ge\frac c2>0
\qquad\text{for every even }n.
}
\tag{27}
\]

Combining `(16)` and `(27)` gives the quantitative separation:

\[
\boxed{
\delta_n\to1
\quad\text{while}\quad
\inf_n\delta_{\rm rec}(K_n;\mathcal E_n)
\ge\frac c2>0.
}
\tag{28}
\]

This proves the nonexistence of a universal implication `(3) => (4)` with `F(delta)->0` using only the Fisher near-isometry constant.

## What the example isolates

The obstruction is not loss of tangent rank. At every parameter value, the retained one-dimensional Fisher metric is positive and approaches the source metric multiplicatively. Nor is the obstruction a singular support or a disconnected parameter set: all densities are strictly positive and smooth, and `Theta` is one connected open interval.

The failure is **global folding**. The map from parameters to retained laws contains an `n`-fold periodic carrier `theta -> q(.-n theta)`. Its differential is large everywhere, so local metric information is excellent, but globally distinct parameters can land on the same retained distribution. The discarded `Z_n` coordinate carries exactly the provenance needed to choose the correct sheet of that covering-like map.

This separates three claims that must not be conflated:

\[
\text{small score-projection defect}
\not\Rightarrow
\text{global injectivity of the retained experiment}
\not\Rightarrow
\text{small whole-experiment deficiency}.
\tag{29}
\]

A Fisher lower bound is therefore a **local differential gate**, not a complete fidelity certificate.

## Prior art and novelty assessment

The ingredients are strongly classical and no theorem-level novelty is claimed.

Kaori Yamaguchi and Hiraku Nozawa, **“On statistics which are almost sufficient from the viewpoint of the Fisher metrics,”** *Information Geometry* 7 (2024), 543--553, DOI `10.1007/s41884-024-00160-1`, arXiv:`2305.04199`, define `delta`-almost sufficiency through the Fisher-metric inequality `delta^2 g <= g' <= g` and characterize the retained metric in terms of the residual log-density derivative. Their framework is the direct prior art for the local near-isometry notion used in `(15)`.

Kaori Yamaguchi, **“Characterization of delta-almost sufficient statistics via KL divergence,”** RIMS Kôkyûroku 2318 (2025), develops a KL-divergence characterization of the same almost-sufficiency notion. This reinforces that Fisher/KL near-retention is an established quantitative local-information framework rather than an Arithmetic Fidelity invention.

Abram Kagan and Lawrence Shepp, **“A Sufficiency Paradox: An Insufficient Statistic Preserving the Fisher Information,”** *The American Statistician* 59(1) (2005), 54--56, DOI `10.1198/000313005X21041`, give a different exact-equality warning: Fisher information can be preserved by an insufficient statistic in a regular example with a support/density-zero subtlety. David Pollard, **“A note on insufficiency and the preservation of Fisher information,”** arXiv:`1107.3797`, explains the score-measurability and differentiability-in-quadratic-mean mechanism and places that phenomenon near Le Cam's comparison-of-experiments viewpoint.

The present result is not a restatement of the Kagan--Shepp pathology: here every density is strictly positive, exact Fisher equality is not claimed, and instead a sequence of local Fisher distortions tends to zero while a fixed global aliasing defect remains. It is also compatible with the exact sufficiency boundary in AF-013/AF-126: the retained experiment is not sufficient because the two source laws in `(17)` become identical after compression.

The specific synthesis — a positive smooth near-isometric Fisher sequence with a uniform Le Cam/recovery-deficiency lower bound produced by global aliasing — was not located in the targeted prior-art audit. That search boundary is not evidence of novelty, so the finding remains `NO-NOVELTY-CLAIM`. Its durable value is the exact counterexample and the resulting audit gate for this research line.

## Boundary conditions and falsification tests

1. **The separation is global, not infinitesimal.** On sufficiently small parameter neighborhoods the periodic aliasing may be absent. The finding therefore does not contradict local recovery statements with explicit radius/injectivity assumptions.

2. **The Fisher comparison is relative.** The absolute lost information is `J`, not a vanishing number. What tends to zero is the fractional metric loss `1/(n^2+1)`. Any theorem using an absolute score-defect bound rather than a relative near-isometry must be checked separately.

3. **The source metric grows with `n`.** This is intentional: it shows that a dimensionless Fisher distortion constant alone cannot control global deficiency. A positive theorem may need additional normalization, diameter, curvature, injectivity-radius, Lipschitz, or global divergence assumptions.

4. **The retained family is globally non-identifiable.** If a proposed theorem assumes injectivity of `theta -> P_theta K`, this exact example is excluded. Such an assumption is therefore a substantive extra fidelity gate, not a consequence of near-Fisher preservation.

5. **The lower bound is whole-family and exact.** It does not depend on estimating the optimal recovery kernel. One exact collision plus one positive source total-variation separation already forces `(27)`.

6. **This is not yet arithmetic fidelity.** The example establishes a general compression theorem boundary. Applying it to rational-prime discrimination still requires a source-natural statistical family and an arithmetic-relevant global collision or non-collision theorem at the actual compression layer.

## Consequence for the current frontier

AF-141 showed that a Fisher-based carrier must preserve the arithmetic-relevant score directions. AF-142 adds a separate obligation: **even arbitrarily good preservation of all local score directions is insufficient unless the retained experiment is globally non-aliasing on the declared control family.**

A future statistical Arithmetic Fidelity argument therefore needs at least two quantitatively distinct gates. First, control the local score/Fisher defect. Second, control global identification — for example by a lower bound on retained divergence or total variation between relevant distant controls, an injectivity theorem with quantitative inverse modulus, or an explicit recovery bound for the whole experiment.

This is precisely the kind of extra structure that a local metric cannot manufacture after compression. In later prime applications, a source-natural Fisher geometry may certify that infinitesimal arithmetic directions survive while still missing a global matched control that lands on the same retained representation. Such controls must be tested independently at the retained-law layer.