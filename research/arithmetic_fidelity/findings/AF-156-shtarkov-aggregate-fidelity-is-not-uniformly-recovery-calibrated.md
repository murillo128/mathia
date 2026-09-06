# AF-156 — Shtarkov aggregate fidelity is not uniformly recovery-calibrated

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-149 introduced the Shtarkov envelope as a source-natural common reference, AF-154 showed that its full likelihood-ray loss has the exact zero set of experiment sufficiency, and AF-155 identified Shtarkov-mass contraction as a restricted Bayes decision defect. These exact statements do **not** extend to a family-uniform approximate equivalence with Le Cam recovery deficiency.

There is an explicit sequence of finite experiments and deterministic compressions for which the experiment becomes asymptotically exactly recoverable in worst-case total variation, and even every individual Shtarkov-reference Pearson loss tends to zero, while both the radial Shtarkov decision defect and the full unnormalized likelihood-ray loss remain order one. In fact the radial defect can tend to its maximal value `1`.

Use the private-label experiment from AF-146 and AF-149,

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\tag{1}
\]

on `X={0,1,...,m}`, and let `K_m` retain `0` while collapsing every private label `1,...,m` to one output `*`. The compressed laws are all identical:

\[
Q_i=P_iK_m=(1-\rho)\delta_0+\rho\delta_*.
\tag{2}
\]

The exact one-sided recovery deficiency is

\[
\boxed{
\delta_m
:=\inf_R\sup_i\|P_i-Q_iR\|_{\rm TV}
=\rho\left(1-\frac1m\right).
}
\tag{3}
\]

The source Shtarkov mass is

\[
\boxed{
C_m=1+(m-1)\rho,
}
\tag{4}
\]

with normalized envelope

\[
M(0)=\frac{1-\rho}{C_m},
\qquad
M(j)=\frac{\rho}{C_m}.
\tag{5}
\]

Its max-normalized likelihood ray from AF-154 is especially simple:

\[
U(0)=\mathbf 1,
\qquad
U(j)=e_j\quad(1\le j\le m).
\tag{6}
\]

Conditioned on the collapsed output `*` under the Shtarkov law, the private label is uniform, so

\[
V(*)=\mathbb E_M[U\mid *]
=\frac1m\mathbf 1.
\tag{7}
\]

Therefore AF-154's normalized full-ray Bayes risk

\[
R_{\rm ray}
:=\mathbb E_{MK}\|U-\mathbb E[U\mid Y]\|_2^2
\tag{8}
\]

and AF-155's radial/envelope Bayes defect

\[
R_{\rm env}
:=1-\frac{C_Y}{C_m}
\tag{9}
\]

coincide exactly in this family:

\[
\boxed{
R_{\rm ray}=R_{\rm env}
=\frac{(m-1)\rho}{1+(m-1)\rho}.
}
\tag{10}
\]

Combining `(3)--(4)` gives the exact comparison

\[
\boxed{
R_{\rm ray}=R_{\rm env}
=\frac{m}{C_m}\,\delta_m.
}
\tag{11}
\]

Thus the distortion factor between the Shtarkov aggregate defects and the true recovery deficiency can grow linearly with the number of experiment members when `C_m` stays bounded.

More sharply, suppose `rho=rho_m -> 0`. Then `delta_m -> 0`, but if

\[
m\rho_m\longrightarrow\lambda\in[0,\infty],
\tag{12}
\]

one has

\[
\boxed{
R_{\rm ray}=R_{\rm env}
\longrightarrow
\frac{\lambda}{1+\lambda},
}
\tag{13}
\]

with the convention that the limit is `1` for `lambda=infinity`. Hence **every limiting aggregate defect between zero and one is compatible with vanishing recovery deficiency**. There is no dimension-free modulus `f(t)->0` as `t->0` such that either `R_env <= f(delta_m)` or `R_ray <= f(delta_m)` holds uniformly over finite experiment size.

The separation survives even after imposing the stronger condition that every individual source-reference Pearson loss tends to zero. AF-149 gives, symmetrically for every member,

\[
\varepsilon_i^{\rm NML}
=C_m\rho\left(1-\frac1m\right)
=C_m\delta_m.
\tag{14}
\]

Choose

\[
\rho_m=m^{-\alpha},
\qquad
\frac12<\alpha<1.
\tag{15}
\]

Then

\[
\delta_m\sim m^{-\alpha}\to0,
\qquad
\max_i\varepsilon_i^{\rm NML}
\sim m^{1-2\alpha}\to0,
\tag{16}
\]

while

\[
\boxed{
R_{\rm ray}=R_{\rm env}\longrightarrow1.
}
\tag{17}
\]

So the obstruction is not merely that a bad common reference makes each model look far away. The Shtarkov reference gives a vanishing recovery certificate for **every individual member**, yet its radial mass statistic and its unnormalized whole-ray `ell_2` aggregation can still report order-one loss because the envelope reference places almost all of its mass on the union of many individually rare private alternatives.

This sharpens the current Arithmetic Fidelity frontier. The Shtarkov likelihood ray remains an exact canonical coordinate for sufficiency, and propagated Shtarkov-reference Pearson losses remain valid one-way recovery certificates. What fails is **family-uniform approximate calibration of source-natural aggregate geometry**. Approximate fidelity must therefore state the downstream decision/recovery target and its scaling with experiment complexity; exact-zero completeness alone is not enough.

## Derivation

### Exact recovery deficiency

After `K_m`, every `Q_i` is the same law `(2)`. Any reverse kernel can distinguish source `0` from the private sector because the outputs `0` and `*` are distinct, but after seeing `*` it must choose one probability vector `r=(r_1,...,r_m)` over the private labels, independent of `i`.

The recovered law for member `i` is

\[
(1-\rho)\delta_0+\rho\sum_jr_j\delta_j,
\]

so

\[
\|P_i-Q_iR\|_{\rm TV}
=\rho(1-r_i).
\tag{18}
\]

Minimizing the worst case maximizes `min_i r_i`, whose optimum is `1/m` at the uniform reverse. Hence `(3)` follows. This is exactly the minimax reverse already identified in AF-146 and AF-149.

### Shtarkov ray geometry of the private-label family

The pointwise likelihood envelope is

\[
s(0)=1-\rho,
\qquad
s(j)=\rho,
\]

which gives `(4)--(5)`. Dividing the full likelihood vector by its envelope gives `(6)`: all models tie at the shared point `0`, while private point `j` is the `j`th coordinate ray.

The Shtarkov output law is

\[
q(0)=\frac{1-\rho}{C_m},
\qquad
q(*)=\frac{m\rho}{C_m}.
\tag{19}
\]

At `0`, the likelihood ray is observed without loss. At `*`, the posterior under `M` is uniform on `j=1,...,m`, proving `(7)`. For each private source point,

\[
\left\|e_j-\frac1m\mathbf1\right\|_2^2
=1-\frac1m.
\tag{20}
\]

Therefore

\[
\begin{aligned}
R_{\rm ray}
&=q(*)\left(1-\frac1m\right)\\
&=\frac{m\rho}{C_m}\frac{m-1}{m}\\
&=\frac{(m-1)\rho}{C_m}.
\end{aligned}
\tag{21}
\]

At the output, all `Q_i` coincide, so the output Shtarkov mass is `C_Y=1`. AF-155 then gives

\[
R_{\rm env}=1-\frac1{C_m}
=\frac{(m-1)\rho}{C_m},
\tag{22}
\]

which proves `(10)`. Equation `(11)` follows by comparing with `(3)`.

### Asymptotic phase diagram

If `rho_m -> 0`, then `(3)` immediately gives `delta_m -> 0`. Meanwhile

\[
(m-1)\rho_m\to\lambda
\]

whenever `m rho_m -> lambda`, so `(10)` gives `(13)`.

This yields three qualitatively different regimes for the same asymptotically recoverable experiments:

- if `m rho_m -> 0`, then the Shtarkov aggregate defects also vanish;
- if `m rho_m -> lambda in (0,infinity)`, they converge to `lambda/(1+lambda)`;
- if `m rho_m -> infinity`, they converge to `1`.

The transition is controlled by the **union envelope mass** of the private sector, not by the per-member recovery error.

For the stronger separation `(15)--(17)`, when `1/2<alpha<1`,

\[
C_m=1+(m-1)m^{-\alpha}\sim m^{1-\alpha}.
\]

Thus

\[
\varepsilon_i^{\rm NML}
=C_m\delta_m
\sim
m^{1-\alpha}m^{-\alpha}
=m^{1-2\alpha}\to0,
\]

while `(10)` has numerator `(m-1)m^{-alpha}->infinity`, so both aggregate risks tend to `1`.

### Why the aggregate defects disagree with recovery

There is no contradiction with AF-149's Pearson recovery certificate. For the Shtarkov Bayes reverse,

\[
4\|P_i-P_iKR_M\|_{\rm TV}^2
\le\varepsilon_i^{\rm NML}
\]

holds separately for every `i`, and in `(15)` both sides indeed vanish. Nor is there a contradiction with AF-154's exact-zero theorem: for every finite `m` and `rho>0`, the compression is not sufficient and `R_ray>0`.

The issue is **uniform topology as the experiment dimension grows**. AF-154 packages all `m` likelihood coordinates into an unnormalized Euclidean ray loss,

\[
R_{\rm ray}
=\frac1{C_m^2}\sum_i\varepsilon_i^{\rm NML}.
\tag{23}
\]

In the symmetric private-label family, each coordinate loss becomes tiny while there are enough coordinates for their aggregate to remain macroscopic. Simultaneously, the Shtarkov envelope is designed to dominate the union of all model-private likelihood peaks, so its own probability law assigns total private-sector mass

\[
q(*)=\frac{m\rho}{1+(m-1)\rho},
\tag{24}
\]

which can tend to one even though every original experiment member visits its private point with probability `rho->0`.

This is a clean instance of the line's distinction between **source-natural coordinates** and **destination-calibrated conflict**. The Shtarkov law is a canonical way to coordinatize the source experiment; it is not automatically the probability weighting appropriate to every downstream decision or recovery notion.

## Falsification and boundaries

The obstruction depends essentially on allowing the number of experiment members to grow. For fixed finite `m`, `(11)` gives a finite comparison factor and no asymptotic separation of this type is possible. The finding therefore does not refute Shtarkov likelihood-ray geometry as a local coordinate system or exact sufficiency invariant.

It also does not say that all normalized aggregates fail. Dividing or reweighting likelihood-ray coordinates changes the geometry and may restore a useful family-uniform calibration for a declared decision class. No such replacement is established here. In particular, a normalization chosen only to force this example to work would not yet be a canonical Arithmetic Fidelity mechanism.

The private-label control is intentionally non-arithmetic. That is a strength for the present no-go statement: any proposed general theory claiming that raw Shtarkov radial or unnormalized ray loss is a family-uniform proxy for recoverability must already survive this finite control before primes or Beurling systems are relevant.

## Prior art and novelty assessment

The components used here are classical or already established in the Arithmetic Fidelity corpus. Shtarkov's normalized maximum-likelihood distribution and minimax-regret interpretation are classical; see Yuri M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (1987), and Andrew R. Barron, Jorma Rissanen, and Bin Yu, **“The Minimum Description Length Principle in Coding and Modeling,”** *IEEE Transactions on Information Theory* 44(6), 2743–2760 (1998), DOI `10.1109/18.720554`. Deficiency and decision-theoretic comparison of statistical experiments are classical; see Erik Torgersen, *Comparison of Statistical Experiments*, Cambridge University Press (1991), especially the deficiency framework and its relation to decision risks.

Targeted searches for combinations of Shtarkov/NML with Le Cam deficiency and approximate comparison of experiments did not identify a standard theorem stating the exact private-label phase diagram `(10)--(17)`. No novelty claim is made from that absence. The durable contribution recorded here is the exact Mathia-level obstruction obtained by putting the classical Shtarkov geometry of AF-149/AF-154/AF-155 against the already-audited recovery control of AF-146: **exact-zero sufficiency geometry need not induce a family-uniform approximate recovery geometry, even when every coordinate-wise Shtarkov Pearson certificate vanishes.**

## Consequence for the line

The source-natural Shtarkov program should not be discarded. It has now isolated a more precise design requirement. A future fidelity quantity intended for approximate preservation must specify both:

1. a source-natural representation/reference that does not introduce arbitrary labels or priors; and
2. a destination-relevant decision/recovery aggregation whose constants remain controlled under the experiment complexity relevant to the application.

For later prime or Beurling stress tests, this means that preserving a canonical source envelope or its exact sufficiency zero set is not enough. The decisive question is whether the proposed compression keeps the **arithmetic decision class of interest** distinguishable with quantitatively stable calibration rather than merely preserving a source-natural aggregate.