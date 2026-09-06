# AF-159 — Barycentric Pearson loss calibrates optimal recovery deficiency

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-FIDELITY`, `POSITIVE-REFERENCE-CONSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-158 shows that Pearson data-processing loss relative to a propagated common reference is quantitatively equivalent to the recovery error of the **Bayes reverse selected by that same reference**, but it does not give a converse bound in terms of the **optimal** Le Cam recovery deficiency. The missing condition can be isolated exactly: if the source reference is itself a mixture of the experiment members, then every common approximate reverse also approximately recovers the reference. Under a bounded likelihood-ratio condition, this is enough to calibrate the Pearson loss to the optimal reverse rather than to one preselected Bayes reverse.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite sample space `X`, let

\[
K:X\rightsquigarrow Y
\]

be a stochastic compression, and define the one-sided recovery deficiency

\[
\delta_{\rm rec}(K;\mathcal E)
:=
\min_{R:Y\rightsquigarrow X}
\max_i\|P_i-P_iKR\|_{\rm TV},
\tag{1}
\]

with normalized total variation.

Choose a **barycentric source reference**

\[
M=\sum_{j=1}^m\pi_jP_j,
\qquad \pi\in\Delta_m,
\tag{2}
\]

that dominates every member, and write

\[
L_M
:=
\max_i\left\|\frac{dP_i}{dM}\right\|_\infty<\infty.
\tag{3}
\]

Propagate the same source reference through the compression and define the worst-member Pearson data-processing loss

\[
\Gamma_M(K;\mathcal E)
:=
\max_i
\left[
\chi^2(P_i\|M)
-
\chi^2(P_iK\|MK)
\right].
\tag{4}
\]

Then

\[
\boxed{
4\,\delta_{\rm rec}(K;\mathcal E)^2
\le
\Gamma_M(K;\mathcal E)
\le
L_M(L_M+2)\,\delta_{\rm rec}(K;\mathcal E).
}
\tag{5}
\]

The lower inequality is the common-reference recovery direction already established in AF-144/AF-158. The new point is the upper inequality against the **best possible common reverse**. It holds because barycentricity makes recovery of all experiment members automatically recover `M` at the same worst-case total-variation scale.

Consequently, for any sequence of finite experiments/compressions with barycentric references satisfying

\[
\sup_n L_{M_n}<\infty,
\tag{6}
\]

one has the two-sided asymptotic equivalence

\[
\boxed{
\Gamma_{M_n}\to0
\iff
\delta_{\rm rec}(K_n;\mathcal E_n)\to0.
}
\tag{7}
\]

This gives a direct answer to the family-complexity obstruction in AF-156--AF-158: a common-reference divergence can be calibrated to optimal recovery, but the calibration requires both a **reference that is recoverable whenever the declared experiment is recoverable** and a **uniform bound on the likelihood complexity relative to that reference**.

There is a source-only way to optimize the latter condition. Define the barycentric domination radius

\[
\Lambda_{\rm bar}(\mathcal E)
:=
\min_{M\in\operatorname{conv}(\mathcal E)}
\sup_{P\in\operatorname{conv}(\mathcal E)}
\left\|\frac{dP}{dM}\right\|_\infty.
\tag{8}
\]

In the finite setting the minimum exists, is finite, depends only on the convex hull of the experiment, and satisfies

\[
1\le\Lambda_{\rm bar}(\mathcal E)\le m.
\tag{9}
\]

The upper bound follows from the uniform mixture of the listed members. If `M_bar` is any minimizer in `(8)`, then `(5)` specializes to

\[
\boxed{
4\delta_{\rm rec}^2
\le
\Gamma_{M_{\rm bar}}
\le
\Lambda_{\rm bar}(\Lambda_{\rm bar}+2)\delta_{\rm rec}.
}
\tag{10}
\]

A minimizing barycentric reference need not be unique, so `(8)` canonically selects the **best universal calibration constant**, not necessarily a unique reference or a unique Pearson defect. The theorem holds for every minimizer.

## Derivation

### A bounded-density continuity lemma for Pearson divergence

The upper bound rests on an elementary continuity estimate. Let `(P,M)` and `(P',M')` be two pairs of probability measures on the same finite space such that

\[
P\le L M,
\qquad
P'\le L M'
\tag{11}
\]

pointwise for some finite `L`. Put

\[
\eta=\|P-P'\|_{\rm TV},
\qquad
\zeta=\|M-M'\|_{\rm TV}.
\tag{12}
\]

Then

\[
\boxed{
\left|
\chi^2(P\|M)-\chi^2(P'\|M')
\right|
\le
2L\eta+L^2\zeta.
}
\tag{13}
\]

Indeed, Pearson divergence has the variational representation

\[
1+\chi^2(P\|M)
=
\sup_g\left\{2\,\mathbb E_Pg-\mathbb E_Mg^2\right\}.
\tag{14}
\]

The optimizer is `g=dP/dM`. Under `(11)` it lies in `[0,L]`, so the supremum may be restricted to that common interval for both pairs. For every `0\le g\le L`, normalized total-variation duality gives

\[
|\mathbb E_Pg-\mathbb E_{P'}g|
\le L\eta,
\tag{15}
\]

and, since `0\le g^2\le L^2`,

\[
|\mathbb E_Mg^2-\mathbb E_{M'}g^2|
\le L^2\zeta.
\tag{16}
\]

Using `|\sup F-\sup F'|\le\sup|F-F'|` in `(14)` proves `(13)`.

This estimate is not claimed as new. It is a direct bounded-likelihood-ratio specialization of classical variational and reverse-divergence continuity ideas. Its role here is to expose the exact constant needed by the recovery argument.

### Any common reverse of the experiment also reverses a barycentric reference

Let `R_*` attain the finite minimum in `(1)` and write

\[
\delta=\delta_{\rm rec}(K;\mathcal E),
\qquad
\widetilde P_i=P_iKR_*.
\tag{17}
\]

By definition,

\[
\|P_i-\widetilde P_i\|_{\rm TV}\le\delta
\qquad\forall i.
\tag{18}
\]

Because `M` is the same convex combination `(2)`, its recovered version is

\[
\widetilde M
:=MKR_*
=
\sum_j\pi_j\widetilde P_j.
\tag{19}
\]

Convexity of total variation therefore gives

\[
\boxed{
\|M-\widetilde M\|_{\rm TV}
\le
\sum_j\pi_j\|P_j-\widetilde P_j\|_{\rm TV}
\le\delta.
}
\tag{20}
\]

This is exactly the step unavailable for a generic external reference. Approximate recovery of the declared family says nothing in general about an unrelated probability law, even if that law is otherwise a very natural center.

The domination condition also propagates through channels. From

\[
P_i\le L_M M
\tag{21}
\]

one gets

\[
P_iK\le L_M MK
\quad\text{and}\quad
\widetilde P_i=P_iKR_*\le L_M MKR_*=L_M\widetilde M.
\tag{22}
\]

Thus both pairs `(P_i,M)` and `(\widetilde P_i,\widetilde M)` satisfy the same likelihood-ratio ceiling.

### Data processing plus bounded continuity gives the converse

Pearson divergence obeys data processing, so

\[
\chi^2(P_iK\|MK)
\ge
\chi^2(P_iKR_*\|MKR_*)
=
\chi^2(\widetilde P_i\|\widetilde M).
\tag{23}
\]

Hence the memberwise loss in `(4)` satisfies

\[
\begin{aligned}
\varepsilon_i(M,K)
&:=
\chi^2(P_i\|M)-\chi^2(P_iK\|MK)\\
&\le
\chi^2(P_i\|M)-\chi^2(\widetilde P_i\|\widetilde M).
\end{aligned}
\tag{24}
\]

Apply `(13)` with `L=L_M`, `eta<=delta`, and `zeta<=delta` from `(18)--(20)`. This yields

\[
\varepsilon_i(M,K)
\le
L_M(L_M+2)\delta.
\tag{25}
\]

Taking the maximum over `i` proves the upper inequality in `(5)`.

For the lower inequality, AF-144/AF-158 constructs the Bayes reverse associated with the propagated reference `M` and proves memberwise

\[
4\|P_i-P_iKR_M\|_{\rm TV}^2
\le
\varepsilon_i(M,K).
\tag{26}
\]

Since the optimal deficiency cannot exceed the worst error of that particular reverse,

\[
\delta_{\rm rec}
\le
\max_i\|P_i-P_iKR_M\|_{\rm TV},
\tag{27}
\]

and maximizing `(26)` proves the lower half of `(5)`.

### The barycentric domination radius is a convex-hull quantity

The set `conv(E)` is compact on a finite sample space. For fixed `M`, the map

\[
P\mapsto\left\|\frac{dP}{dM}\right\|_\infty
\tag{28}
\]

is convex in `P` on the dominated face, and the extended-valued objective in `(8)` is lower semicontinuous in `M`. A finite convex mixture placing positive weight on every support-contributing member dominates the entire hull, so the minimum is finite and attained.

The definition uses only `conv(E)`, hence is unchanged by duplicating experiment members or adjoining redundant mixtures. For the particular finite presentation with `m` members, the uniform mixture

\[
M_{\rm unif}=\frac1m\sum_iP_i
\tag{29}
\]

satisfies `P_i<=m M_unif` for all `i`, and therefore every mixture in the hull also satisfies `P<=m M_unif`. This proves `(9)`.

The radius `(8)` should not be confused with the unrestricted order-infinity information radius. The restriction `M in conv(E)` is mathematically substantive here: it is what makes `(20)` follow from recovery of the experiment.

## Exact arithmetic/analytic stress test: the local `p=2` Euler-factor family

Use the local arithmetic family already audited in AF-157--AF-158,

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right),
\tag{30}
\]

and let `K` retain the first exponent coordinate while merging the last two.

For

\[
M_\pi=\pi P_1+(1-\pi)P_2,
\tag{31}
\]

the two active worst-case likelihood ratios are

\[
\frac{P_2(1)}{M_\pi(1)}=\frac4{4-\pi},
\qquad
\frac{P_1(3)}{M_\pi(3)}=\frac3{1+2\pi}.
\tag{32}
\]

Balancing them gives

\[
\pi_*=\frac8{11},
\qquad
\boxed{
\Lambda_{\rm bar}=\frac{11}{9},
}
\tag{33}
\]

with barycentric reference

\[
M_*
=
\frac8{11}P_1+\frac3{11}P_2
=
\left(\frac{48}{77},\frac{20}{77},\frac9{77}\right).
\tag{34}
\]

The optimal reverse on the merged output returns the second source coordinate with probability `5/7` and the third with probability `2/7`. Both members then have the same exact recovery error,

\[
\boxed{
\delta_{\rm rec}=\frac1{49}.
}
\tag{35}
\]

Direct Pearson calculation gives

\[
\varepsilon_1(M_*,K)=\frac{11}{9135},
\qquad
\varepsilon_2(M_*,K)=\frac{704}{82215},
\tag{36}
\]

so

\[
\boxed{
\Gamma_{M_*}=\frac{704}{82215}.
}
\tag{37}
\]

The theorem becomes the exact numerical check

\[
\frac4{2401}
\le
\frac{704}{82215}
\le
\frac{319}{3969},
\tag{38}
\]

where the right endpoint is

\[
\frac{11}{9}
\left(\frac{11}{9}+2\right)
\frac1{49}.
\]

Thus the mechanism is non-vacuous on an arithmetic/analytic source family: the same finite compression has a source-mixture reference with a small intrinsic domination radius, and its propagated Pearson loss is sandwiched by the actual optimal common-recovery defect.

## Why this differs from the Shtarkov reference

AF-149 shows that the Shtarkov envelope reference solves the stronger unrestricted domination problem

\[
C
=
\inf_M
\max_i\left\|\frac{dP_i}{dM}\right\|_\infty,
\tag{39}
\]

where `M` ranges over all probability references. This can give a smaller domination constant than `(8)`, but the minimizer need not belong to `conv(E)`.

That difference explains the boundary exposed in AF-157--AF-158. If the Shtarkov reference lies outside the experiment hull, an optimal reverse satisfying

\[
P_iKR\approx P_i
\quad\forall i
\]

need not satisfy

\[
M_*KR\approx M_*.
\]

Therefore the continuity bridge `(20)` is unavailable, and the Shtarkov Pearson profile is naturally calibrated to its own source-selected Bayes reverse rather than uniformly to the optimized Le Cam reverse.

The AF-156 private-label family makes this distinction concrete. Every mixture of its members keeps source mass `1-rho` at the shared point `0`, whereas the normalized Shtarkov envelope changes that mass by the envelope normalization. Except in the trivial no-conflict case, the Shtarkov reference is therefore outside the convex hull. The growing-family failure of a converse to optimal deficiency is consistent with `(5)` rather than contradicting it.

This yields a useful design tradeoff:

- unrestricted reference optimization can minimize source domination complexity but may lose automatic recoverability of the reference;
- barycentric reference optimization preserves automatic recoverability under every common reverse, at the price of a potentially larger domination radius.

The relevant question for a concrete compression is therefore not merely which center is most canonical, but which source-center property is needed by the downstream recovery target.

## Prior art and novelty assessment

The ingredients of this finding are classical, and no novelty claim is made for the statistical inequalities themselves.

Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/AOMS/1177700372`, and Erik Torgersen, *Comparison of Statistical Experiments*, Cambridge University Press (1991), provide the deficiency/randomization framework used in `(1)`.

Friedrich Liese, **“phi-divergences, sufficiency, Bayes sufficiency, and deficiency,”** *Kybernetika* 48(4), 690–713 (2012), gives a particularly close prior-art bridge: for binary experiments, normalized families of phi-divergences characterize Le Cam distance, and Theorem 4.2 bounds differences of suitable phi-divergences by deficiency. Pearson divergence is globally unbounded and falls outside the finite-curvature normalization used there, so a bounded-likelihood-ratio restriction is precisely the kind of extra regularity needed to obtain a finite linear modulus for Pearson-type quantities.

Igal Sason and Sergio Verdú, **“f-Divergence Inequalities,”** *IEEE Transactions on Information Theory* 62(11), 5973–6006 (2016), DOI `10.1109/TIT.2016.2603151`, systematically develop divergence inequalities under bounded relative information and reverse-Pinsker-type assumptions. This confirms that bounded likelihood ratios as a route from total variation to unbounded divergences are established information-theoretic prior art.

Targeted searches did not identify the exact Mathia packaging `(5)`--`(10)`: propagated Pearson **data-processing loss**, a **barycentric** common reference, and the **optimal common reverse deficiency** combined through the same source-mixture weights. That absence is not treated as evidence of novelty. The durable contribution recorded here is the explicit bridge needed by the current Arithmetic Fidelity corpus and the explanation of why the convex-hull constraint repairs the specific endpoint-calibration gap left by AF-158.

## Falsification and boundaries

The barycentric condition is sufficient, not claimed necessary. More general references could satisfy a recovery-stability inequality

\[
\|M-MKR\|_{\rm TV}
\le c\max_i\|P_i-P_iKR\|_{\rm TV}
\tag{40}
\]

for structural reasons other than literal membership in the convex hull. In such a class the same proof would give a modified constant `2L+cL^2`. No such broader canonical class is established here.

The likelihood-ratio ceiling is also substantive. Without bounded `L_M`, Pearson divergence is not uniformly continuous in total variation, and no finite constant of the form `(13)` can be expected. Thus `(5)` does not remove the complexity gate identified by AF-156; it identifies one exact form of that gate.

The constant `L(L+2)` is a clean universal bound from the variational proof, not claimed optimal. Sharper reverse-divergence inequalities may improve it for special likelihood ranges or reference geometries. The finding concerns existence of a stable modulus, not best constants.

The theorem is finite as stated. Infinite or nondominated experiments require measurable-kernel, attainment, and integrability control from full Le Cam theory; `(8)` can also fail to have a finite or attained center without compactness/tightness assumptions.

A minimizing barycentric reference need not be unique. Consequently the scalar `Lambda_bar` is intrinsic to the convex hull, while the particular loss `Gamma_Mbar` may depend on which minimizer is selected. Do not call that loss canonical without an additional uniqueness or selection theorem.

Finally, the local Euler-factor calculation is a stress test of the theorem, not evidence for RH. No rational-prime discriminator or zero-selecting mechanism has yet been shown to possess a uniformly bounded barycentric domination radius at the scales relevant to zeta.

## Consequence for the line

AF-156--AF-158 left a precise tension: the Shtarkov likelihood geometry is source-natural and has exact sufficiency semantics, but its approximate defect is calibrated to a source-selected reverse rather than uniformly to the optimal Le Cam reverse. AF-159 identifies a complementary route. **Reference recoverability and likelihood complexity are separate gates.** Membership of the reference in the experiment convex hull supplies the first automatically; bounded domination supplies the second quantitatively.

For later arithmetic and Beurling control families, this creates a concrete test before a common-reference compression can be trusted: determine whether there is a mathematically natural barycentric reference whose domination radius stays controlled as the family and scale grow. If such references exist, Pearson data-processing loss becomes a genuine two-sided proxy for optimal recoverability by `(5)`. If every barycentric reference has diverging domination radius, that divergence is itself an explicit obstruction showing why a source-natural quadratic fidelity score cannot remain uniformly calibrated to the arithmetic decision class.