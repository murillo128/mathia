# AF-143 — Fisher near-isometry plus uniform pairwise-TV fidelity need not imply recovery

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `QUANTITATIVE-SEPARATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-142 shows that an arbitrarily small relative Fisher-information defect can coexist with a fixed whole-experiment recovery defect because a retained experiment may fold two distant parameters onto the same law. A natural repair is to add a global no-aliasing requirement, or even a quantitative lower bound saying that retained pairwise distances do not collapse too much.

That repair is still insufficient.

For every fixed

\[
0<\varepsilon<1,
\tag{1}
\]

there is a sequence of one-dimensional, connected, strictly positive, smooth statistical models and deterministic statistics such that:

1. the retained Fisher metric is a uniform near-isometry,
   \[
   I_{T,n}(\theta)
   =\delta_n^2 I_{X,n}(\theta),
   \qquad
   \delta_n^2
   =\frac{n^2+\varepsilon}{n^2+1}
   \longrightarrow1;
   \tag{2}
   \]
2. the retained experiment is globally identifiable;
3. every pair of parameters keeps a fixed fraction of its source total-variation separation,
   \[
   \varepsilon\,
   \|P_{n,\theta}-P_{n,\theta'}\|_{\rm TV}
   \le
   \|Q_{n,\theta}-Q_{n,\theta'}\|_{\rm TV}
   \le
   \|P_{n,\theta}-P_{n,\theta'}\|_{\rm TV};
   \tag{3}
   \]
4. nevertheless the one-sided Le Cam recovery deficiency stays bounded away from zero,
   \[
   \delta_{\rm rec}(T_n;\mathcal E_n)
   \ge
   \frac{1-\varepsilon}{2}\,c>0
   \qquad\text{for every even }n,
   \tag{4}
   \]
   for one constant `c` independent of `n`.

Thus **local Fisher near-isometry plus global injectivity plus a uniform all-pairs metric lower bound still does not control whole-experiment recoverability**. These conditions constrain tangent geometry and binary separation, but they do not force one common reverse channel capable of reconstructing the entire experiment.

Equivalently, for fixed `0<varepsilon<1` there is no universal implication of the form

\[
\left.
\begin{array}{c}
I_T\succeq\delta^2 I_X,\\[2mm]
\|Q_\theta-Q_{\theta'}\|_{\rm TV}
\ge\varepsilon\|P_\theta-P_{\theta'}\|_{\rm TV}
\quad\forall\theta,\theta'
\end{array}
\right\}
\Longrightarrow
\delta_{\rm rec}\le F_\varepsilon(\delta)
\tag{5}
\]

with

\[
F_\varepsilon(\delta)\longrightarrow0
\qquad(\delta\uparrow1)
\tag{6}
\]

based only on those two metric hypotheses.

## Construction

Use the same translated positive density as AF-142,

\[
q(u)=\frac{e^{\cos u}}{Z},
\qquad
Z=\int_0^{2\pi}e^{\cos u}\,du,
\tag{7}
\]

on

\[
\mathbb T=\mathbb R/(2\pi\mathbb Z),
\]

and set

\[
J:=\int_0^{2\pi}\sin^2(u)q(u)\,du>0.
\tag{8}
\]

Take the connected open parameter interval

\[
\Theta=\left(-\frac14,\pi+\frac14\right).
\tag{9}
\]

For every even integer `n>=2`, let

\[
X_n=(Y_n,Z_n,U_n)
\in\mathbb T^2\times\{0,1\},
\]

where, conditionally on `theta`, the three coordinates are independent and

\[
Y_n\mid\theta\sim q(y-n\theta)\,dy,
\qquad
Z_n\mid\theta\sim q(z-\theta)\,dz,
\tag{10}
\]

while

\[
U_n\sim\operatorname{Bernoulli}(\varepsilon)
\tag{11}
\]

is parameter-independent. Relative to Haar measure on the two circles and counting measure on `{0,1}`, the source density is

\[
p_{n,\theta}(y,z,u)
=q(y-n\theta)q(z-\theta)
\varepsilon^u(1-\varepsilon)^{1-u},
\tag{12}
\]

which is strictly positive and smooth in the continuous variables and in `theta`.

Define the deterministic statistic `T_n` by always retaining `Y_n`, and retaining `Z_n` only on the ancillary branch `U_n=1`:

\[
T_n(y,z,u)
=
\begin{cases}
(1,y,z),&u=1,\\
(0,y,\bot),&u=0.
\end{cases}
\tag{13}
\]

The parameter-independent coordinate `U_n` merely determinizes an erasure channel. If stochastic compressions are admitted directly, one may omit `U_n` from the source and reveal `Z_n` independently with probability `varepsilon`; the retained experiment is the same.

Write

\[
P_{n,\theta}=\mathcal L_\theta(X_n),
\qquad
Q_{n,\theta}=P_{n,\theta}T_n.
\tag{14}
\]

## Fisher loss is asymptotically negligible

The ancillary variable has zero score. As in AF-142,

\[
S_{X,n,\theta}
=n\sin(Y_n-n\theta)+\sin(Z_n-\theta),
\tag{15}
\]

so conditional independence and centering give

\[
I_{X,n}(\theta)=(n^2+1)J.
\tag{16}
\]

On the branch `U_n=1`, the statistic retains the complete source score. On the branch `U_n=0`, it retains only `Y_n`; the conditional expectation of the lost `Z_n` score is zero. Hence the retained score is

\[
S_{T,n,\theta}
=
\begin{cases}
n\sin(Y_n-n\theta)+\sin(Z_n-\theta),&U_n=1,\\
n\sin(Y_n-n\theta),&U_n=0.
\end{cases}
\tag{17}
\]

and therefore

\[
\begin{aligned}
I_{T,n}(\theta)
&=\varepsilon(n^2+1)J
 +(1-\varepsilon)n^2J\\
&=(n^2+\varepsilon)J.
\end{aligned}
\tag{18}
\]

Thus

\[
\boxed{
\frac{I_{T,n}(\theta)}{I_{X,n}(\theta)}
=
\frac{n^2+\varepsilon}{n^2+1}
=1-\frac{1-\varepsilon}{n^2+1}
\longrightarrow1
}
\tag{19}
\]

uniformly in `theta`.

AF-141 interprets exactly this difference as score-projection loss. The absolute lost score energy is `(1-varepsilon)J`, while the retained high-frequency `Y_n` score energy grows like `n^2J`. The dimensionless local defect therefore vanishes.

## The retained experiment preserves every pairwise TV distance up to a fixed factor

Let

\[
A_{n,\theta}=\mathcal L_\theta(Y_n,Z_n),
\qquad
B_{n,\theta}=\mathcal L_\theta(Y_n).
\tag{20}
\]

Because `U_n` is independent of `theta`, adjoining it to the source does not change pairwise total variation:

\[
\|P_{n,\theta}-P_{n,\theta'}\|_{\rm TV}
=
\|A_{n,\theta}-A_{n,\theta'}\|_{\rm TV}.
\tag{21}
\]

The two output branches of `T_n` are disjoint. On `U_n=1` the full pair `(Y_n,Z_n)` is visible, while on `U_n=0` only `Y_n` is visible. Total variation therefore decomposes exactly as

\[
\boxed{
\|Q_{n,\theta}-Q_{n,\theta'}\|_{\rm TV}
=
\varepsilon
\|A_{n,\theta}-A_{n,\theta'}\|_{\rm TV}
+(1-\varepsilon)
\|B_{n,\theta}-B_{n,\theta'}\|_{\rm TV}.
}
\tag{22}
\]

Since marginalization from `(Y_n,Z_n)` to `Y_n` contracts total variation,

\[
\|B_{n,\theta}-B_{n,\theta'}\|_{\rm TV}
\le
\|A_{n,\theta}-A_{n,\theta'}\|_{\rm TV}.
\tag{23}
\]

Combining `(21)`--`(23)` gives the uniform two-sided comparison

\[
\boxed{
\varepsilon
\|P_{n,\theta}-P_{n,\theta'}\|_{\rm TV}
\le
\|Q_{n,\theta}-Q_{n,\theta'}\|_{\rm TV}
\le
\|P_{n,\theta}-P_{n,\theta'}\|_{\rm TV}
}
\tag{24}
\]

for every pair `theta,theta'` and every `n`.

The source family is globally identifiable: equality of the `Z_n` translated densities implies equality of parameters modulo `2pi`, and the diameter of `Theta` is less than `2pi`. Equation `(24)` therefore implies that the retained family is globally identifiable as well.

So the obstruction left by AF-142 is not repaired merely by ruling out exact aliases. In this example the retained map is injective and its entire pairwise total-variation geometry has a uniform inverse modulus `1/varepsilon`.

## Whole-experiment recovery still stays a fixed distance away

Choose the same two interior parameters as AF-142,

\[
\theta_0=0,
\qquad
\theta_1=\pi.
\tag{25}
\]

Because `n` is even,

\[
n\pi\in2\pi\mathbb Z,
\]

so the `Y_n` laws coincide at the two parameters:

\[
B_{n,0}=B_{n,\pi}.
\tag{26}
\]

The `Z_n` laws do not. Put

\[
c:=
\|q(z)\,dz-q(z-\pi)\,dz\|_{\rm TV}>0.
\tag{27}
\]

The common `Y_n` and ancillary factors give

\[
\|P_{n,0}-P_{n,\pi}\|_{\rm TV}=c.
\tag{28}
\]

Equation `(22)` and `(26)` give

\[
\|Q_{n,0}-Q_{n,\pi}\|_{\rm TV}
=\varepsilon c.
\tag{29}
\]

For any proposed reverse channel `R`, the pairwise argument of AF-126/AF-142 gives

\[
2\sup_{\theta\in\Theta}
\|P_{n,\theta}-Q_{n,\theta}R\|_{\rm TV}
\ge
\|P_{n,0}-P_{n,\pi}\|_{\rm TV}
-
\|Q_{n,0}-Q_{n,\pi}\|_{\rm TV}.
\tag{30}
\]

Using `(28)`--`(29)` and taking the infimum over `R`,

\[
\boxed{
\delta_{\rm rec}(T_n;\mathcal E_n)
\ge
\frac{1-\varepsilon}{2}c
>0
}
\tag{31}
\]

for every even `n`.

Together with `(19)`,

\[
\boxed{
\delta_n\to1
\quad\text{while}\quad
\inf_{n\text{ even}}
\delta_{\rm rec}(T_n;\mathcal E_n)
\ge
\frac{1-\varepsilon}{2}c.
}
\tag{32}
\]

The all-pairs lower bound `(24)` remains fixed throughout this limit.

## What the example isolates

AF-142 separates local Fisher fidelity from global injectivity. AF-143 shows that the next obvious repair also stops too early.

Three increasingly strong properties are present here:

\[
\text{near-isometric tangent Fisher geometry},
\qquad
\text{global identifiability},
\qquad
\text{uniform pairwise-TV separation}.
\tag{33}
\]

None forces small Le Cam recovery deficiency.

The reason is categorical rather than numerical. Pairwise metrics ask how distinguishable two parameter-indexed laws are. Recovery deficiency asks whether **one parameter-independent reverse randomization** reconstructs every law in the experiment simultaneously. That common-kernel compatibility is a higher-order family constraint not encoded by a lower bound on each pairwise distance.

This also explains why the intrinsic Fisher-Rao geometry can look excellent while the experiment is still globally unrecoverable. The Fisher metric is a tangent/path geometry on the parameterized family. Total variation in `(24)` is an ambient pairwise geometry on the image laws. Deficiency tests a stronger simulation relation between the two complete experiments. Good control at the first two levels does not collapse the third to zero.

For Arithmetic Fidelity, the resulting gate is sharper:

> A proposed compression is not quantitatively faithful merely because it is locally near-isometric and globally injective, even if every pairwise discriminator remains uniformly separated. A useful recovery theorem must control a family-level common reconstruction object, or another quantity already known to dominate its deficiency.

## Prior art and novelty assessment

The ingredients and surrounding theory are classical; no theorem-level novelty is claimed.

Kaori Yamaguchi and Hiraku Nozawa, **“On statistics which are almost sufficient from the viewpoint of the Fisher metrics,”** *Information Geometry* 7 (2024), 543--553, DOI `10.1007/s41884-024-00160-1`, define quantitative almost-sufficiency through a Fisher-metric lower bound and show that the induced Fisher-Rao metric is bi-Lipschitz equivalent to the source metric. Their result is direct prior art for interpreting `(19)` as strong local metric retention. It does not identify that condition with Le Cam recovery deficiency.

Abram Kagan and Lawrence Shepp, **“A Sufficiency Paradox: An Insufficient Statistic Preserving the Fisher Information,”** *The American Statistician* 59(1) (2005), 54--56, DOI `10.1198/000313005X21041`, and David Pollard, **“A note on insufficiency and the preservation of Fisher information,”** arXiv:`1107.3797`, give the classical warning that Fisher information and statistical sufficiency are not interchangeable without the relevant regularity/support hypotheses. Their exact-equality mechanism differs from the present positive-density near-isometry sequence.

AF-126 already records the classical Le Cam/Blackwell boundary and proves that pairwise total-variation losses are only lower-bound witnesses for recovery deficiency, not a complete characterization. AF-142 adds a smooth positive connected family in which local Fisher near-isometry fails because of exact global aliasing. The present construction combines those boundaries and removes the aliasing loophole by retaining a fixed fraction of every source pairwise-TV distance.

A targeted literature audit located the Fisher almost-sufficiency and insufficiency precedents above but did not locate this exact combined sequence. That search boundary is not evidence of novelty. The durable contribution here is the explicit smooth counterexample showing that the **global no-aliasing repair suggested by AF-142 is still quantitatively too weak**.

## Boundary conditions and falsification tests

1. **The Fisher near-isometry is relative.** The discarded Fisher energy is the fixed amount `(1-varepsilon)J`; the retained carrier grows like `n^2J`. A theorem controlling an absolute score defect, rather than a dimensionless relative loss, is not refuted by this example.

2. **The pairwise lower bound has fixed constant `varepsilon`.** The example does not exploit pairwise distances collapsing to zero relative to their source values. Choosing `varepsilon=1/2`, for example, preserves at least half of every source total-variation distance while the recovery deficiency is still at least `c/4`.

3. **The ancillary coordinate is not mathematical information about `theta`.** It is parameter-independent and can be removed by viewing `(13)` as the equivalent randomized erasure channel. The obstruction is therefore not created by hiding a second parameter signal in `U_n`.

4. **Whole-experiment deficiency is stronger than pairwise geometry.** AF-126 already shows this in finite experiments. AF-143 should not be read as claiming a new abstract deficiency theorem; it supplies a smooth connected positive-density realization that simultaneously satisfies the Fisher and uniform pairwise gates now live in this line.

5. **A stronger positive theorem may still exist.** Conditions involving a uniform reverse kernel, likelihood-ratio reconstruction, bounded conditional score plus a global experiment-level modulus, or another quantity known to upper-bound Le Cam deficiency are outside the counterexample unless they reduce to `(2)` and `(3)` alone.

6. **There is no arithmetic conclusion yet.** The finding only sharpens the generic fidelity audit. An RH-facing application must still identify a source-natural statistical or operator category and prove that its retained structure supplies a family-level recovery mechanism rather than only local or pairwise separation.

## Consequences for Arithmetic Fidelity

AF-142's proposed extra gate must be upgraded. **Global injectivity is necessary to remove exact aliases but is not a quantitative recovery principle.** Even adding a uniform pairwise-TV lower bound leaves a fixed common-reconstruction defect.

The next positive target should therefore not be another scalar or pairwise metric. A candidate theorem must expose structure that controls one common reconstruction across the full declared family: for example a quantitative likelihood-ratio factorization, a uniform reverse channel, a deficiency-dominating divergence/profile with a proved converse, or an application-specific compatibility theorem strong enough to imply one of those.

This narrows the role of Fisher geometry in the line. Source-natural Fisher metrics and the score-projection identity remain useful diagnostics for **where infinitesimal information is lost**, but they cannot certify global arithmetic fidelity by themselves, even after ordinary aliasing and pairwise collapse have been ruled out.