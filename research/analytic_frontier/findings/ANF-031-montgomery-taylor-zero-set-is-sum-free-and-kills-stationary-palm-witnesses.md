# ANF-031 — the Montgomery--Taylor zero set is sum-free and kills stationary Palm witnesses

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + ADDITIVE-RIGIDITY + DIFFRACTION-DUAL + NEGATIVE/OBSTRUCTION`. `ANF-030` shows that any normalized diffraction witness dominated by the sharp Montgomery--Taylor budget and possessing a positive Palm correlation measure must put all off-diagonal Palm pair mass on the real zero set `Z_MT` of the exact Montgomery--Taylor extremizer. The remaining stationary-process question in `ANF-030` can be closed exactly: the positive zero set is **strictly sum-free**. Consequently no real configuration with three distinct points can have all nonzero pair differences in `Z_MT`, and therefore no positive-intensity stationary point process can realize a diffraction measure dominated by the sharp budget.

Let

\[
\theta:=2^{-1/2},
\qquad
S(x)=
\frac{
\cos(\pi x)-\sqrt2\,\pi x\cot\theta\,\sin(\pi x)
}{1-2\pi^2x^2},
\qquad
R_{\rm MT}(x):=S(x)^2,
\tag{1}
\]

as in `ANF-030`, and write

\[
Z_{\rm MT}:=\{x\in\mathbb R:R_{\rm MT}(x)=0\}.
\tag{2}
\]

Then there is a strictly decreasing sequence `epsilon_n in (0,pi/4)`, `n>=1`, such that

\[
\boxed{
Z_{\rm MT}\cap(0,\infty)
=
\left\{
 z_n:=n+\frac{\varepsilon_n}{\pi}:n\ge1
\right\},
}
\tag{3}
\]

where `epsilon_n` is the unique solution of

\[
(n\pi+\varepsilon_n)\tan\varepsilon_n
=
\theta\tan\theta.
\tag{4}
\]

Moreover

\[
\boxed{
z_m+z_n\notin Z_{\rm MT}
\qquad(m,n\ge1).}
\tag{5}
\]

Hence every set `Lambda subset R` satisfying

\[
(\Lambda-\Lambda)\setminus\{0\}
\subseteq Z_{\rm MT}
\tag{6}
\]

has

\[
\boxed{|\Lambda|\le2.}
\tag{7}
\]

Combining (7) with the Palm support theorem of `ANF-030` gives the main consequence:

\[
\boxed{
\text{no stationary locally finite point process of positive finite intensity has normalized diffraction }
\mu\le\nu_{\rm MT}
\text{ on }(-1,1).
}
\tag{8}
\]

Thus the entire **stationary point-process/Palm realization route** to the sharp universal-affine scalar witness is closed. The residual gap is no longer the construction of an exotic hyperuniform stationary process; it is the strictly larger abstract weak-* convex body `K` from `ANF-020`, whose band-restricted limits need not yet possess a globally realizable positive Palm inverse transform.

## 1. The apparent low-frequency root is removable

The numerator in (1) vanishes when, with

\[
y:=\pi x,
\qquad
A:=\theta\tan\theta,
\tag{9}
\]

one has

\[
y\tan y=A.
\tag{10}
\]

On `(0,pi/2)`, the function `y tan y` is strictly increasing from `0` to `+infinity`. Since `A=theta tan theta`, its unique solution there is

\[
y=\theta.
\tag{11}
\]

But this is exactly where the denominator in (1) also vanishes:

\[
1-2y^2=0.
\]

It is a removable point, not a zero of `S`. This is immediate from the Fourier-integral representation used in `ANF-030`. With

\[
g(u)
=
\frac{\cos(\sqrt2\,u)}{\sqrt2\sin\theta}
\mathbf 1_{[-1/2,1/2]}(u),
\qquad S=\widehat g,
\tag{12}
\]

and `x=theta/pi`, one has `2 pi x=sqrt2`, so oddness removes the imaginary part and

\[
S(\theta/\pi)
=
\frac1{\sqrt2\sin\theta}
\int_{-1/2}^{1/2}\cos^2(\sqrt2\,u)\,du
>0.
\tag{13}
\]

Thus `Z_MT` has no positive zero below the first branch following `pi`.

This cancellation is a necessary stress test. Treating (10) alone as the zero equation would incorrectly insert the spurious point `theta/pi` into `Z_MT` and would destroy the additive argument below.

## 2. All genuine positive zeros are one-sided perturbations of the integers

For each integer `n>=1`, equation (10) has no solution on

\[
(n\pi-\pi/2,n\pi),
\tag{14}
\]

because `tan y<0` there while `A>0`. On

\[
(n\pi,n\pi+\pi/2),
\tag{15}
\]

write

\[
y=n\pi+\varepsilon.
\]

Then (10) becomes

\[
F_n(\varepsilon)
:=(n\pi+\varepsilon)\tan\varepsilon=A,
\qquad 0<\varepsilon<\pi/2.
\tag{16}
\]

`F_n` is strictly increasing on this interval, starts at zero, and diverges at `pi/2`; hence there is exactly one solution `epsilon_n`. There are no other positive branches, proving (3).

The roots move monotonically toward the integers. If `n'>n`, then

\[
F_{n'}(\varepsilon)>F_n(\varepsilon)
\qquad(0<\varepsilon<\pi/2),
\tag{17}
\]

so uniqueness in (16) gives

\[
\boxed{
0<\varepsilon_{n'}<\varepsilon_n.}
\tag{18}
\]

The first displacement is already below `pi/4`. Indeed

\[
F_1(\pi/4)=\frac{5\pi}{4}>A,
\tag{19}
\]

while `F_1(0)=0`, so

\[
\boxed{0<\varepsilon_n\le\varepsilon_1<\pi/4.}
\tag{20}
\]

Numerically, only as a check and not as evidence,

\[
z_1=1.057278291008855\ldots,
\qquad
z_2=2.030067530128160\ldots .
\tag{21}
\]

The proof below uses only the exact monotonicity and interval bounds (18)--(20).

## 3. The positive zero set is strictly sum-free

Take any `m,n>=1`. By (3),

\[
\pi(z_m+z_n)
=(m+n)\pi+\varepsilon_m+\varepsilon_n.
\tag{22}
\]

Equation (20) gives

\[
0<\varepsilon_m+\varepsilon_n<\pi/2,
\tag{23}
\]

so the sum lies in the same positive-tangent branch in which the unique zero `z_{m+n}` occurs. But (18) gives

\[
\varepsilon_{m+n}<\varepsilon_m
<\varepsilon_m+\varepsilon_n.
\tag{24}
\]

Therefore

\[
z_m+z_n
>
z_{m+n},
\tag{25}
\]

while both points lie strictly between `m+n` and `m+n+1/2`. Since Section 2 proves that this interval contains exactly one zero, namely `z_{m+n}`, the sum cannot itself be a zero. This proves (5).

The argument is stronger than asymptotic nonresonance. The zeros satisfy

\[
z_n=n+O(n^{-1}),
\]

so additive near-collisions become arbitrarily close at large index; for example the defect `z_m+z_n-z_{m+n}` tends to zero along large comparable indices. What matters is the **strict ordering** in (24), not a uniform gap. This distinction prevents an invalid attempt to obtain a quantitative energy gap for arbitrary finite configurations from the present theorem.

## 4. Three points are already impossible

Suppose a real set `Lambda` contains three distinct points

\[
x_1<x_2<x_3
\]

and satisfies (6). Put

\[
a:=x_2-x_1>0,
\qquad
b:=x_3-x_2>0.
\tag{26}
\]

Then (6) forces

\[
a,b,a+b=x_3-x_1
\in Z_{\rm MT}\cap(0,\infty).
\tag{27}
\]

Write `a=z_m` and `b=z_n`. Equation (5) says `a+b` is not in `Z_MT`, contradicting (27). Hence no such triple exists and (7) follows.

This is an exact finite combinatorial obstruction: `Z_MT` is not merely discrete or asymptotically lattice-like. Its precise one-sided displacement from the integers is incompatible with the additive relation carried by every ordered triple of real points.

## 5. Positive-intensity stationary Palm realizations are impossible

Let `Xi` be a stationary locally finite point process on `R` with finite intensity `rho>0`, and let its normalized positive Palm correlation measure be

\[
\eta=\delta_0+\eta^\circ,
\qquad \eta^\circ\ge0.
\tag{28}
\]

Assume its full normalized diffraction `mu` is dominated on the tested band by

\[
\nu_{\rm MT}
=a_{\rm MT}\delta_0+a_{\rm MT}|h|dh.
\tag{29}
\]

`ANF-030` applies the exact Montgomery--Taylor extremizer and forces

\[
R_{\rm MT}\,\eta^\circ=0,
\qquad
\operatorname{supp}\eta^\circ\subseteq Z_{\rm MT}.
\tag{30}
\]

Because `R_MT(0)=1`, (30) also excludes off-diagonal mass at displacement zero, so coincident multiplicities are absent almost surely.

The reduced Palm measure is the reduced second-moment measure of the stationary process. By the Campbell identity, for any bounded observation window the expected number of ordered distinct pairs whose displacement lies in a compact subset of `R\setminus Z_MT` is zero. The count itself is nonnegative, hence it vanishes almost surely. Exhausting the complement of the closed discrete set `Z_MT` and the line by countably many compact windows shows that almost surely

\[
(x-y)\in Z_{\rm MT}
\qquad
\text{for every two distinct points }x,y\in\Xi.
\tag{31}
\]

Section 4 then implies that every realization contains at most two points on the whole real line. But stationarity gives

\[
\mathbb E N_\Xi([0,L])=\rho L
\tag{32}
\]

for every `L>0`, whereas the global two-point bound gives

\[
\mathbb E N_\Xi([0,L])\le2.
\tag{33}
\]

Letting `L->infinity` forces `rho=0`, contradicting the assumed positive intensity. This proves (8).

Equivalently: the open question (32) in `ANF-030` has the strongest possible negative answer. There is not merely no **positive-density** configuration whose difference support lies in `Z_MT`; there is no deterministic configuration with three distinct points at all.

## 6. What this closes, and what it does not

`ANF-030` already excluded every stationary candidate having diffuse off-diagonal Palm mass. The present result removes the remaining singular/crystalline Palm escape. A stationary process cannot evade the exact extremizer by concentrating pair separations on its discrete zeros, because the zeros themselves cannot support the additive triangle relation among three ordered points.

Therefore no stationary point process -- determinantal, renewal, lattice, perturbed lattice, quasicrystalline, singular, mixed, or otherwise -- can provide the sharp band-dominated witness **provided its diffraction/Palm pair is an honest positive stationary realization in the normalization of `ANF-030`**. The earlier model-specific obstructions remain useful diagnostics, but they are no longer needed to rule out this entire realization class.

This does **not** yet prove

\[
K\cap\{\mu:0\le\mu\le\nu_{\rm MT}\}=\varnothing
\tag{34}
\]

for the abstract convex body `K` of `ANF-020`. `K` is defined only from weak-* limits of band-restricted convex combinations of finite diffraction measures. Such a band limit is not automatically supplied with a globally defined positive Palm inverse transform satisfying the consistency assumptions used in Section 5. The strict sum-free theorem also gives no uniform positive lower bound on finite `R_MT`-energy: the additive defect between large zeros tends to zero. Thus one cannot pass from the three-point exclusion to (34) by a compactness argument that ignores scale escape.

The surviving scalar problem has consequently become a **realizability/compactness gap** rather than a search over familiar stationary processes. A complete no-go would follow from a theorem showing that any `mu in K` dominated by `nu_MT` admits enough positive correlation/Palm structure for the equality argument of `ANF-030` and the three-point consistency used here to survive the weak-* limit. Conversely, a counterexample must exploit precisely the loss of such global consistency under band restriction and scale escape.

## 7. Prior-art and novelty boundary

The load-bearing external input remains the exact Montgomery--Taylor / Carneiro--Chandee--Littmann--Milinovich extremizer already anchored in `SOURCES.md` and reconstructed in `ANF-030`. The root classification above is an exact derivation from its explicit formula, and the process contradiction uses only the standard Palm/Campbell interpretation already assumed in `ANF-030`.

The **sum-free conclusion itself is not new within the current public research-artifact prior art**. The repository `ainta/zeta-simple-zeros`, released as version `0.1.0` on 10 August 2026 and present at commit `040c5e899e658aed7b56a2a87f501798fe10761d` on 11 August 2026, derives the equivalent positive-zero equation

\[
x\tan(\pi x)=c>0
\]

for the optimized Montgomery--Taylor overlap kernel and proves directly by the tangent-addition formula that `x`, `y`, and `x+y` cannot all be positive zeros: otherwise one obtains `x^2+xy+y^2+c^2=0`. Its three-point certificate then uses the same bounded-triangle consequence to prove positivity of `k(u)^2+k(v)^2+k(u+v)^2` on `u,v>=0`, `u+v<=4`; a finite verifier supplies a quantitative lower bound. This artifact was already anchored in `SOURCES.md` as prior art for the consecutive-gap/block-defect mechanism.

Accordingly, (5) should be classified as **public-artifact prior art plus an independent exact rederivation**, not as a Mathia novelty claim. What remains specific to the present finding is the complete branchwise root description (3)--(4), the monotone displacement proof (18)--(20), and especially the diffraction/Palm consequence (8), which turns the additive zero-set obstruction into a no-go for every positive-intensity stationary realization at the sharp Montgomery--Taylor budget. The Ainta repository describes itself as a research draft generated with GPT-5.6 Sol and invites independent verification; it is useful prior art, not peer review or an external correctness certificate for the present argument.

## 8. Decisive audit and next frontier

The decisive audit of the exact part is finite. It is enough to falsify any one of the following statements: the removable root at `theta`, uniqueness of the root on each positive tangent branch, monotone decrease of `epsilon_n`, or the bound `2 epsilon_1<pi/2`. Equations (13), (16)--(20) establish all four directly. The numerical root values in (21) are dispensable.

The decisive next question is no longer whether a stationary hyperuniform process can be engineered with the right cusp, reciprocal structure, or singular support. It is:

\[
\boxed{
\text{Does band-dominated membership in the finite-configuration closure }K
\text{ force any positive three-point/Palm consistency that survives scale escape?}
}
\tag{35}
\]

A positive answer strong enough to recover (31) would combine `ANF-030` and the present sum-free theorem into a complete universal-affine scalar no-go. A negative answer should exhibit an explicit sequence of convex finite configurations whose band diffraction converges under `nu_MT` while its off-band/autocorrelation structure escapes so that no stationary positive Palm realization remains.