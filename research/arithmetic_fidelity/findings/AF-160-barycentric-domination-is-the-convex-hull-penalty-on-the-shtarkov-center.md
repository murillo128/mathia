# AF-160 — Barycentric domination is the convex-hull penalty on the Shtarkov center

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `STRUCTURAL-RIGIDITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-159 introduced the barycentric domination radius as the source complexity that makes a propagated Pearson loss quantitatively comparable with **optimal** Le Cam recovery deficiency. AF-149--AF-158 use the unrestricted Shtarkov/NML reference as the canonical source center. The exact gap between those two choices can be isolated.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite sample space `X`. Write

\[
s(x)=\max_i P_i(x),
\qquad
C=\sum_x s(x),
\qquad
M_{\rm Sh}(x)=\frac{s(x)}{C},
\tag{1}
\]

for the pointwise envelope, Shtarkov mass, and normalized Shtarkov reference. Ignore points with `s(x)=0`, since every member vanishes there. Define the max-normalized likelihood rays

\[
U_i(x)=\frac{P_i(x)}{s(x)}\in[0,1],
\qquad
\max_i U_i(x)=1.
\tag{2}
\]

AF-159's barycentric domination radius is

\[
\Lambda_{\rm bar}(\mathcal E)
:=
\min_{M\in\operatorname{conv}(\mathcal E)}
\sup_{P\in\operatorname{conv}(\mathcal E)}
\left\|\frac{dP}{dM}\right\|_\infty.
\tag{3}
\]

Then the following identities hold exactly.

First, the convex-hull supremum reduces to the same pointwise envelope that defines the Shtarkov center:

\[
\boxed{
\Lambda_{\rm bar}
=
\min_{M\in\operatorname{conv}(\mathcal E)}
\max_{x:s(x)>0}\frac{s(x)}{M(x)}.
}
\tag{4}
\]

Equivalently, with order-infinity Rényi divergence

\[
D_\infty(P\|Q)
=
\log\max_{x:P(x)>0}\frac{P(x)}{Q(x)},
\tag{5}
\]

one has

\[
\boxed{
\Lambda_{\rm bar}
=
C\exp\!\left(
\inf_{M\in\operatorname{conv}(\mathcal E)}
D_\infty(M_{\rm Sh}\|M)
\right).
}
\tag{6}
\]

Thus the extra cost of requiring the reference to be recoverable from recovery of the experiment is exactly the one-sided order-infinity Rényi divergence from the unrestricted Shtarkov center to the experiment convex hull. Define

\[
G_{\rm hull}(\mathcal E)
:=\frac{\Lambda_{\rm bar}}{C}.
\tag{7}
\]

Then

\[
\boxed{
G_{\rm hull}
=
\exp d_\infty(M_{\rm Sh},\operatorname{conv}(\mathcal E)),
\qquad
 d_\infty(M_{\rm Sh},\mathcal H)
:=\inf_{M\in\mathcal H}D_\infty(M_{\rm Sh}\|M).
}
\tag{8}
\]

Here `d_infty` is a directed divergence-to-set quantity, not a metric.

Second, `(4)` has an exact finite zero-sum-game dual. If `M_\pi=\sum_i\pi_iP_i`, then

\[
\frac{M_\pi(x)}{s(x)}
=\sum_i\pi_iU_i(x).
\tag{9}
\]

Hence

\[
\boxed{
\frac1{\Lambda_{\rm bar}}
=
\max_{\pi\in\Delta_m}
\min_{x:s(x)>0}
\sum_i\pi_iU_i(x)
=
\min_{\nu\in\Delta(X_s)}
\max_i
\sum_x\nu(x)U_i(x),
}
\tag{10}
\]

where `X_s={x:s(x)>0}`. The first player chooses a barycentric mixture of experiment members; the second chooses the source point where that mixture gives the weakest fraction of the envelope. The dual player instead chooses a distribution over source points and minimizes the largest expected max-normalized likelihood coordinate.

These formulas sharpen AF-159's bounds to an exact structural split:

\[
\boxed{
C\le\Lambda_{\rm bar}\le m,
}
\tag{11}
\]

and, more importantly,

\[
\boxed{
\Lambda_{\rm bar}=C
\iff
M_{\rm Sh}\in\operatorname{conv}(\mathcal E).
}
\tag{12}
\]

So there is **no barycentric price at all** exactly when the canonical order-infinity/Shtarkov center is already a mixture of the experiment members. Otherwise the penalty is measured exactly by `(8)`, rather than by family size alone.

Combining `(6)` with AF-159 gives a source-factorized optimal-recovery calibration. For a barycentric minimizer `M_bar`, put

\[
d_{\rm hull}
:=d_\infty(M_{\rm Sh},\operatorname{conv}(\mathcal E)),
\qquad
\Lambda_{\rm bar}=C e^{d_{\rm hull}}.
\tag{13}
\]

Then AF-159 yields

\[
\boxed{
4\delta_{\rm rec}^2
\le
\Gamma_{M_{\rm bar}}
\le
C e^{d_{\rm hull}}
\left(Ce^{d_{\rm hull}}+2\right)
\delta_{\rm rec}.
}
\tag{14}
\]

The complexity entering optimal-recovery calibration therefore separates into two conceptually different source quantities: unrestricted envelope complexity `C`, and the additional **convex-hull mismatch** `e^{d_hull}` forced by requiring the reference to be automatically recoverable whenever the declared experiment is recoverable.

## Derivation

### The barycentric radius depends on the envelope

Fix a dominating `M in conv(E)`. For any `P in conv(E)`,

\[
\left\|\frac{dP}{dM}\right\|_\infty
=
\max_x\frac{P(x)}{M(x)}.
\]

Because evaluation at each `x` is linear and `conv(E)` has vertices among the listed `P_i`,

\[
\sup_{P\in\operatorname{conv}(\mathcal E)}P(x)
=s(x).
\tag{15}
\]

For a finite sample space the two suprema commute:

\[
\begin{aligned}
\sup_{P\in\operatorname{conv}(\mathcal E)}
\max_x\frac{P(x)}{M(x)}
&=
\max_x
\sup_{P\in\operatorname{conv}(\mathcal E)}
\frac{P(x)}{M(x)}\\
&=
\max_x\frac{s(x)}{M(x)}.
\end{aligned}
\tag{16}
\]

Taking the minimum over barycentric `M` proves `(4)`.

### The penalty is the directed order-infinity projection of the Shtarkov center

By `(1)`,

\[
\frac{s(x)}{M(x)}
=C\frac{M_{\rm Sh}(x)}{M(x)}.
\tag{17}
\]

Therefore for every dominating barycentric `M`,

\[
\log\max_x\frac{s(x)}{M(x)}
=
\log C+D_\infty(M_{\rm Sh}\|M).
\tag{18}
\]

Taking the infimum over `conv(E)` and exponentiating proves `(6)--(8)`.

This also gives a short proof of the lower bound in `(11)`. For every probability law `M`,

\[
\max_x\frac{s(x)}{M(x)}
\ge
\frac{\sum_xs(x)}{\sum_xM(x)}
=C.
\tag{19}
\]

Equivalently, the unrestricted minimizer is `M_Sh`, the classical order-infinity Rényi/Shtarkov center.

The equality case is rigid. If a barycentric `M` attains value `C`, then

\[
s(x)\le C M(x)\qquad\forall x.
\tag{20}
\]

Both sides sum to `C`, so every inequality in `(20)` must be equality:

\[
s(x)=CM(x)\qquad\forall x,
\]

hence `M=M_Sh`. Thus equality can occur inside the barycentric problem exactly when `M_Sh` itself lies in the experiment hull, proving `(12)`.

The upper bound `Lambda_bar<=m` is AF-159's uniform-mixture bound: for

\[
M_{\rm unif}=\frac1m\sum_iP_i
\]

one has `P_i<=m M_unif` for every member and hence `s<=m M_unif`.

### The maximin game on Shtarkov likelihood rays

Write a barycentric reference as

\[
M_\pi=\sum_i\pi_iP_i,
\qquad \pi\in\Delta_m.
\]

Using `(2)`,

\[
M_\pi(x)=s(x)\sum_i\pi_iU_i(x).
\tag{21}
\]

Therefore

\[
\max_x\frac{s(x)}{M_\pi(x)}
=
\frac1{\min_x\sum_i\pi_iU_i(x)},
\tag{22}
\]

with the usual convention that a zero denominator gives infinite radius. A uniformly positive mixture exists on `X_s`, so the optimum has positive denominator. Minimizing `(22)` over `pi` gives the first equality in `(10)`.

The payoff

\[
A(\pi,x)=\sum_i\pi_iU_i(x)
\tag{23}
\]

is bilinear after the point player is allowed a mixed strategy `nu in Delta(X_s)`. Finite von Neumann minimax / linear-programming duality gives

\[
\max_{\pi\in\Delta_m}\min_{\nu\in\Delta(X_s)}
\sum_{i,x}\pi_i\nu(x)U_i(x)
=
\min_{\nu\in\Delta(X_s)}\max_{\pi\in\Delta_m}
\sum_{i,x}\pi_i\nu(x)U_i(x).
\tag{24}
\]

The inner minimum on the left is attained at a point mass in `x`, and the inner maximum on the right at a point mass in `i`, yielding the second equality in `(10)`.

There is also a useful normalization identity behind the lower bound. For every `pi`,

\[
\mathbb E_{M_{\rm Sh}}
\left[\sum_i\pi_iU_i(X)\right]
=
\sum_x\frac{s(x)}C\frac{M_\pi(x)}{s(x)}
=
\frac1C.
\tag{25}
\]

Thus the minimum of the game payoff over `x` can never exceed its Shtarkov mean `1/C`. Equality occurs precisely when the payoff is constant on `X_s`, which is again the condition `M_pi=M_Sh`.

## Matched-control stress test: private labels attain the full barycentric penalty

Use the private-label family from AF-146/AF-149/AF-156,

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\qquad 0<\rho<1.
\tag{26}
\]

The envelope and Shtarkov mass are

\[
s(0)=1-\rho,
\qquad
s(j)=\rho,
\qquad
C=1+(m-1)\rho.
\tag{27}
\]

Every barycentric reference has the form

\[
M_\pi(0)=1-\rho,
\qquad
M_\pi(j)=\rho\pi_j.
\tag{28}
\]

Hence

\[
\max_x\frac{s(x)}{M_\pi(x)}
=
\max\left\{1,\frac1{\min_j\pi_j}\right\}.
\tag{29}
\]

The optimum is the uniform mixture, so

\[
\boxed{
\Lambda_{\rm bar}=m,
\qquad
G_{\rm hull}=\frac{m}{1+(m-1)\rho}.
}
\tag{30}
\]

This family saturates AF-159's generic `Lambda_bar<=m` bound for every `rho`, even when the unrestricted Shtarkov complexity is small. For example, if

\[
\rho_m=\frac{\lambda}{m}
\qquad(\lambda>0),
\]

then

\[
C_m\to1+\lambda,
\qquad
G_{\rm hull}\sim\frac{m}{1+\lambda}\to\infty.
\tag{31}
\]

So bounded Shtarkov mass by itself does **not** control the price of forcing the reference into the experiment hull. The obstruction is geometric: the NML center redistributes mass across the union of mutually private alternatives in a way no single mixture of the original members can reproduce with bounded pointwise likelihood ratio.

In the game picture, `U_i(0)=1` for every `i`, while `U_i(j)=1_{i=j}` on the private sector. Thus

\[
\max_\pi\min_x\sum_i\pi_iU_i(x)
=
\max_\pi\min_j\pi_j
=
\frac1m,
\]

which recovers `(30)` without manipulating the references directly. The dual optimum places no weight on the common point and distributes its mass uniformly over the private labels.

This is a line-specific matched control rather than an arithmetic example. It proves that the hull mismatch is a genuinely independent complexity axis, not an artifact of the local Euler-factor family or of a particular compression.

## Arithmetic/analytic stress test: the local `p=2` Euler-factor family has only a small hull penalty

AF-157--AF-159 use

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right).
\tag{32}
\]

AF-157 gives the Shtarkov reference and mass

\[
M_{\rm Sh}
=\left(\frac{16}{25},\frac6{25},\frac3{25}\right),
\qquad
C=\frac{25}{21},
\tag{33}
\]

while AF-159 finds the optimal barycentric reference

\[
M_{\rm bar}
=\left(\frac{48}{77},\frac{20}{77},\frac9{77}\right),
\qquad
\Lambda_{\rm bar}=\frac{11}{9}.
\tag{34}
\]

The exact hull penalty is therefore

\[
\boxed{
G_{\rm hull}
=
\frac{\Lambda_{\rm bar}}C
=
\frac{77}{75},
\qquad
 d_{\rm hull}=\log\frac{77}{75}.
}
\tag{35}
\]

Indeed,

\[
\max_x\frac{M_{\rm Sh}(x)}{M_{\rm bar}(x)}
=
\frac{77}{75},
\]

with equality on the first and third coordinates. Thus the barycentric calibration penalty in this arithmetic control is not primarily caused by a large separation between the NML center and the experiment hull: the directed order-infinity mismatch is only about `2.7%` multiplicatively.

This exact contrast with `(30)` is useful. Two finite experiments can have comparably small Shtarkov masses while differing radically in whether their canonical source center is representable, or nearly representable, by a recoverable barycentric reference.

## Falsification and boundaries

The result is source geometry only. It does not itself analyze a compression `K`, prove approximate recoverability, or improve the Le Cam deficiency of any experiment. Its role is to decompose the source constant that enters AF-159's compression theorem.

The divergence in `(8)` is directional. Small `D_infty(M_Sh||M_bar)` means the barycentric reference pointwise dominates the Shtarkov center up to a small factor; it does not imply a symmetric total-variation, KL, or reverse-`D_infty` statement without additional assumptions.

The exact game dual uses finiteness. Analogues on infinite sample or parameter spaces require compactness/measurability hypotheses and a justified minimax theorem; no such extension is asserted here.

The quantity is invariant under duplicating experiment members or adjoining redundant mixtures, because `conv(E)`, `s`, `C`, and the feasible barycentric-reference set are unchanged. A parameter-list-dependent reformulation of `(10)` must preserve this convex-hull invariance to be intrinsic to the experiment.

The private-label family also blocks an overinterpretation of Shtarkov mass as the unique relevant notion of family complexity. `C` can remain bounded while `Lambda_bar/C` diverges. Conversely, a large family size is not by itself an obstruction: if the Shtarkov center lies in the convex hull, the hull penalty is exactly one regardless of the number of listed members.

Finally, none of `(4)--(14)` identifies a rational-prime discriminator or establishes an RH-facing implication. A later prime/Beurling application must still specify the experiment/control class and compression whose recoverability encodes the arithmetic distinction of interest.

## Prior art and novelty assessment

The unrestricted center in this finding is classical. Shtarkov's normalized maximum-likelihood construction identifies the normalized pointwise likelihood envelope as the minimax-regret universal distribution: Yu. M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 3–17 (1987/English translation 1988).

The closest modern information-radius language is Barış Nakiboğlu, **“The Rényi Capacity and Center,”** *IEEE Transactions on Information Theory* 65(2), 841–860 (2019), DOI `10.1109/TIT.2018.2861002`, arXiv:`1608.02424`. That paper defines Rényi radius as `sup_w D_alpha(w||q)`, proves the capacity/radius center theorem for `alpha in (0,infinity]`, and gives the explicit order-infinity formulas: the capacity is the logarithm of the total pointwise envelope mass and the center is the normalized envelope. Its discussion also treats constrained variants of Rényi capacity. Semih Yagli, Yücel Altuğ, and Sergio Verdú, **“Minimax Rényi Redundancy,”** *IEEE Transactions on Information Theory* 64(5), 3715–3733 (2018), DOI `10.1109/TIT.2018.2803070`, is neighboring prior art for minimax Rényi-divergence redundancy and redundancy-capacity formulations.

Against that literature, equations `(4)--(12)` should be read conservatively. The identification of the unrestricted Shtarkov law with the order-infinity Rényi center is standard, and the restriction to `conv(E)`, the directed `D_infty` penalty, and the zero-sum-game dual are elementary finite convex/minimax consequences of that framework plus AF-159's barycentric recovery requirement. Targeted searches did not identify this exact package stated as a recovery-calibration decomposition, but **no novelty claim is made from that absence**. The durable Mathia contribution is the explicit structural bridge: AF-159's barycentric domination constant is precisely the unrestricted Shtarkov complexity multiplied by the order-infinity cost of moving the canonical center into the recoverable convex hull.

## Consequence for the line

AF-159's reference-selection tradeoff can now be audited before any compression is studied. The source side separates into:

\[
\text{unrestricted envelope complexity}
\times
\text{recoverable-center hull penalty}
=
C\,G_{\rm hull}
=
\Lambda_{\rm bar}.
\]

For future finite experiment/control families, the first source question is therefore not merely whether a canonical Shtarkov center exists. One can ask exactly whether it lies in the experiment hull, and if not, compute or bound the game value `(10)` or the directed order-infinity projection `(8)`. A bounded `C` with an unbounded hull penalty predicts that source-natural NML geometry and optimal-recovery calibration will diverge; a bounded hull penalty shows that the two reference philosophies remain quantitatively close.

This gives Arithmetic Fidelity a sharper reusable gate for later prime/generalized-prime tests: **before interpreting a canonical source reference as a stable recovery coordinate, measure the cost of forcing that reference into the class of objects that every admissible common reverse is guaranteed to recover.**