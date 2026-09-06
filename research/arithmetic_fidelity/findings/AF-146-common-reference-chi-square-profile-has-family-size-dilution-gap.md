# AF-146 — Common-reference chi-square recovery has a family-size dilution gap

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `NEGATIVE/OBSTRUCTION`, `FAMILY-COMPLEXITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-144 gives a positive finite-experiment certificate: the optimized common-reference Pearson chi-square loss

\[
\Gamma_{\chi^2}(K;\mathcal E)
\]

upper-bounds one-sided Le Cam recovery deficiency through

\[
4\,\delta_{\rm rec}(K;\mathcal E)^2
\le
\Gamma_{\chi^2}(K;\mathcal E),
\]

and the two quantities vanish on exactly the same sufficient channels. AF-145 then shows that this certificate composes coherently when one reference mixture is propagated along a Markov pipeline.

That zero-set agreement does **not** extend to a family-size-uniform quantitative equivalence. There are finite experiments for which the Bayes reverse selected by the optimizing common reference is already a minimax-optimal recovery channel, while the optimized chi-square profile remains order one and the actual recovery deficiency tends to zero.

For integers `m>=2` and parameters `0<rho<=1`, let

\[
\Theta_m=\{1,\ldots,m\},
\qquad
X_m=\{0,1,\ldots,m\},
\]

and define the source experiment

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i\in\Theta_m.
\tag{1}
\]

Let the compression

\[
K_m:X_m\rightsquigarrow Y,
\qquad
Y=\{0,*\},
\]

be deterministic with

\[
K_m(0)=0,
\qquad
K_m(j)=*
\quad(1\le j\le m).
\tag{2}
\]

Thus every compressed law is identical:

\[
Q_i:=P_iK_m
=(1-\rho)\delta_0+\rho\delta_*.
\tag{3}
\]

Then the exact whole-experiment recovery defect is

\[
\boxed{
\delta_{\rm rec}(K_m;\mathcal E_{m,\rho})
=
\rho\left(1-\frac1m\right).
}
\tag{4}
\]

For AF-144's reference-optimized Pearson profile one has exactly

\[
\boxed{
\Gamma_{\chi^2}(K_m;\mathcal E_{m,\rho})
=
\rho(m-1).
}
\tag{5}
\]

Hence throughout this family

\[
\boxed{
\Gamma_{\chi^2}
=
m\,\delta_{\rm rec}.
}
\tag{6}
\]

The optimizing prior in `(5)` is the uniform prior, and its Bayes/Petz reverse is exactly a minimax-optimal recovery channel for `(4)`. Therefore the gap is not caused by choosing a poor reverse kernel: it belongs to the chi-square certificate itself.

In particular, choosing

\[
\rho_m=\frac1m
\tag{7}
\]

gives

\[
\delta_{\rm rec}
=
\frac{m-1}{m^2}
\longrightarrow0,
\tag{8}
\]

while

\[
\Gamma_{\chi^2}
=
\frac{m-1}{m}
\longrightarrow1.
\tag{9}
\]

Consequently there is no family-size-independent modulus `omega` with

\[
\omega(t)\to0
\quad(t\downarrow0)
\]

such that every finite experiment and stochastic compression satisfy

\[
\Gamma_{\chi^2}(K;\mathcal E)
\le
\omega\!\left(\delta_{\rm rec}(K;\mathcal E)\right).
\tag{10}
\]

AF-144 remains a valid sufficient recovery certificate and remains exact at zero. What fails is a dimension-free converse quantitative topology when the declared control family is allowed to grow.

## Derivation

### The compression erases only the private label

Equation `(3)` is immediate from `(1)--(2)`: all parameters put the same mass `1-rho` on the shared symbol `0` and the same mass `rho` on a private symbol that `K_m` maps to `*`.

Because all compressed laws are identical, any reverse channel

\[
R:Y\rightsquigarrow X_m
\]

produces one common recovered law

\[
S=Q_iR
\]

for every `i`. Conversely any probability law `S` on `X_m` is realizable as `Q_iR` by taking both rows of `R` equal to `S`. Therefore

\[
\delta_{\rm rec}(K_m;\mathcal E_{m,\rho})
=
\inf_{S\in\Delta(X_m)}
\max_{1\le i\le m}
\|P_i-S\|_{\rm TV}.
\tag{11}
\]

The problem is the Chebyshev radius of the symmetric finite set `(P_i)` in total variation.

### Symmetry makes the minimax recovery explicit

Permuting the private labels `1,...,m` leaves the family `(P_i)` invariant. For any candidate `S`, average all its private-label permutations. Convexity of total variation and of the maximum imply that this symmetrization cannot increase the objective in `(11)`. Thus an optimum may be taken in the form

\[
S_a(0)=1-ma,
\qquad
S_a(j)=a
\quad(1\le j\le m),
\tag{12}
\]

with `0<=a<=1/m`.

For every `i`, direct substitution gives

\[
\|P_i-S_a\|_{\rm TV}
=
\frac12
\left(
|ma-\rho|
+|\rho-a|
+(m-1)a
\right).
\tag{13}
\]

For `a<=rho/m`, this equals

\[
\rho-a,
\tag{14}
\]

which decreases up to `a=rho/m`. For `rho/m<=a<=rho`, it equals

\[
(m-1)a,
\tag{15}
\]

which increases from that point. If `a>=rho`, the value is `ma-rho`, again increasing. Therefore the exact minimizer is

\[
a_*=\frac\rho m,
\tag{16}
\]

and `(4)` follows:

\[
\|P_i-S_{a_*}\|_{\rm TV}
=
\rho-\frac\rho m
=
\rho\left(1-\frac1m\right).
\]

Operationally, the optimal recovery retains `0` exactly and, on observing `*`, chooses one private label uniformly. It cannot know which label was erased, but the erased event itself has probability only `rho`.

### The optimized common-reference chi-square loss pays for prior dilution

Let

\[
\lambda=(\lambda_1,\ldots,\lambda_m)
\in\Delta^\circ(\Theta_m)
\]

be any full-support prior. Its source mixture is

\[
M_\lambda
=(1-\rho)\delta_0
+\rho\sum_{j=1}^m\lambda_j\delta_j.
\tag{17}
\]

Since all output laws coincide, the output mixture is exactly `Q_i`, so

\[
\chi^2(Q_i\|M_\lambda K_m)=0.
\tag{18}
\]

The source Pearson divergence is also explicit. On the shared symbol `0` the likelihood ratio is one. On private symbol `i` it is `1/lambda_i`, while on every other private symbol the numerator vanishes. Hence

\[
\begin{aligned}
\chi^2(P_i\|M_\lambda)
&=
\rho\lambda_i
\left(\frac1{\lambda_i}-1\right)^2
+
\rho\sum_{j\ne i}\lambda_j\\
&=
\rho\left(\frac1{\lambda_i}-1\right).
\end{aligned}
\tag{19}
\]

Therefore AF-144's memberwise loss is

\[
\varepsilon_i(\lambda)
=
\rho\left(\frac1{\lambda_i}-1\right),
\tag{20}
\]

and

\[
\max_i\varepsilon_i(\lambda)
=
\rho\left(\frac1{\min_i\lambda_i}-1\right).
\tag{21}
\]

For every probability vector on `m` points,

\[
\min_i\lambda_i\le\frac1m,
\]

with equality exactly at the uniform prior. Thus

\[
\inf_{\lambda\in\Delta^\circ(\Theta_m)}
\max_i\varepsilon_i(\lambda)
=
\rho(m-1),
\]

which proves `(5)`.

### The optimizing Bayes reverse is already minimax optimal

At the uniform prior, `(17)` becomes

\[
M_*(0)=1-\rho,
\qquad
M_*(j)=\frac\rho m.
\tag{22}
\]

The associated Bayes reverse from AF-144 satisfies

\[
R_*(0\mid0)=1,
\qquad
R_*(j\mid*)=\frac1m.
\tag{23}
\]

Therefore

\[
Q_iR_*
=(1-\rho)\delta_0
+\frac\rho m\sum_{j=1}^m\delta_j
=S_{a_*}.
\tag{24}
\]

But `S_{a_*}` is exactly the minimizer derived in `(16)`. Thus

\[
\sup_i\|P_i-Q_iR_*\|_{\rm TV}
=
\delta_{\rm rec}(K_m;\mathcal E_{m,\rho}).
\tag{25}
\]

This separates two possible explanations for a loose recovery bound. Here there is no inverse-selection problem: the common-reference construction chooses an optimal inverse. The slack lies entirely in using Pearson likelihood-ratio loss as the quantitative certificate for that inverse.

### Rare high-relative-information events create the gap

The mechanism is visible directly in `(20)`. Under the optimizing reference, parameter `i` assigns probability `rho` to a private symbol whose reference probability is only `rho/m`; the likelihood ratio there is `m`. Total variation charges the erased private-label event according to its absolute probability `rho`. Pearson chi-square additionally amplifies it by the inverse reference weight.

For fixed `m`, this is only a constant-factor discrepancy:

\[
\Gamma_{\chi^2}=m\delta_{\rm rec},
\]

and both quantities tend to zero together as `rho->0`. The obstruction appears when the control family grows: the common probability reference must divide its private mass among more alternatives, so its minimum prior weight shrinks even though the absolute probability of the erased region may shrink at the same time.

The scaling `rho_m=1/m` isolates this effect sharply. Recovery can ignore which rare private label occurred at cost `O(1/m)`, while the corresponding likelihood-ratio spike remains `O(m)` on an `O(1/m^2)` reference atom, leaving an `O(1)` Pearson loss.

## Prior art and novelty assessment

No novelty is claimed for the general fact that an unbounded `f`-divergence such as Pearson chi-square cannot be controlled from total variation without additional likelihood-ratio or support regularity. The present finite family is a direct Arithmetic Fidelity diagnostic specialization that makes the obstruction interact with **whole-experiment recovery**, reference-prior optimization, and family size.

- Friedrich Liese, **“φ-divergences, sufficiency, Bayes sufficiency, and deficiency,”** *Kybernetika* 48(4), 690–713 (2012). Liese relates `φ`-divergences to sufficiency, Bayes sufficiency, and Le Cam deficiency, and characterizes deficiency using a normalized **class** of convex divergences rather than one fixed Pearson profile. This is stronger prior-art context against treating one divergence as a complete quantitative experiment metric.
- Igal Sason and Sergio Verdú, **“f-Divergence Inequalities,”** *IEEE Transactions on Information Theory* 62(11), 5973–6006 (2016), DOI `10.1109/TIT.2016.2603151`, arXiv:`1508.00335`. They develop systematic inequalities among `f`-divergences and emphasize reverse-Pinsker-type upper bounds under boundedness assumptions on relative information. This supplies the established boundary behind the exploding likelihood ratios in `(20)`.
- Li Gao, Haojian Li, Iman Marvian, and Cambyse Rouzé, **“Sufficient Statistic and Recoverability via Quantum Fisher Information,”** *Communications in Mathematical Physics* 405, article 180 (2024), DOI `10.1007/s00220-024-05053-z`, arXiv:`2302.02341`. Their recoverability theorem is the stronger quantum prior art specialized in AF-144 to obtain the one-way chi-square-loss-to-Petz-recovery bound. AF-146 does not weaken that theorem; it shows that its Pearson certificate has no family-size-uniform converse against Le Cam recovery error.

AF-050 and AF-051 are nearby but distinct internal boundaries. They study distance from a stochastic channel to a zero-error support-fidelity set and show, respectively, the binary retained-mass geometry of rowwise `f`-divergence repair and the representation sensitivity of quadratic/Brier repair. The present claim concerns a different object: **the relation between AF-144's reference-optimized Pearson data-processing loss and AF-126's minimax common reverse-simulation error for an entire experiment.**

The reusable new line-level conclusion is therefore not a new divergence inequality. It is the exact family-complexity warning `(6)--(10)`: zero-set equivalence plus a correct common inverse does not make a divergence profile a uniformly calibrated measure of approximate structural fidelity.

## Boundary conditions and falsification tests

1. **This does not contradict AF-144.** AF-144 proves
   \[
   4\delta_{\rm rec}^2\le\Gamma_{\chi^2}.
   \]
   AF-146 disproves only a family-size-independent converse modulus. The forward certificate remains valid.

2. **The exact-zero boundary is unchanged.** For every fixed finite `m`, `(6)` gives
   \[
   \Gamma_{\chi^2}=0
   \iff
   \delta_{\rm rec}=0.
   \]
   The separation requires a sequence of growing experiments.

3. **The family-size factor is not attributed to Bayes suboptimality.** The uniform-prior Bayes reverse attains the minimax deficiency exactly. Any attempted explanation of the gap through a better reverse kernel is therefore falsified by `(23)--(25)`.

4. **The example is intentionally non-arithmetic.** It establishes a generic quantitative obstruction required by the README's theory-first mandate. It does not show that a concrete arithmetic control family exhibits the same prior-dilution regime.

5. **A restricted converse may still exist.** Bounds on likelihood ratios, a uniform lower bound on admissible reference weights, bounded effective family complexity, or a different divergence family can remove this counterexample. Sason--Verdú-type reverse inequalities indicate exactly why such regularity assumptions are mathematically substantive rather than technical decoration.

6. **Fixed-cardinality controls are not ruled out.** When `m` is fixed, `(6)` is a perfectly controlled linear comparison. The obstruction is to transferring AF-144 into an arithmetic setting whose matched-control family becomes richer with scale without separately auditing the growth of the common-reference likelihood ratios.

## Arithmetic Fidelity consequence

AF-144 and AF-145 identify a particularly attractive positive mechanism: one source-natural reference can simultaneously generate an additive forward information-loss budget and a coherently compositional reverse channel. AF-146 adds a necessary calibration gate before that mechanism can be treated as a useful compression certificate.

For an arithmetic family `\mathcal E_N` whose number or effective complexity of matched controls grows with scale, small Le Cam recovery error does not by itself imply that a common-mixture Pearson profile remains small. A useful chi-square route must additionally establish at least one source-grounded control on the reference geometry: for example uniformly bounded relevant likelihood ratios, nonvanishing effective reference weights, a bounded-complexity reduction of the control family, or another theorem that prevents the rare-high-ratio mechanism above.

This sharpens the current family-level frontier. The right question is no longer merely whether one common reverse channel exists or composes. One must also ask whether the **certificate used to prove that recovery is quantitatively calibrated to the complexity of the declared discriminator family**, rather than becoming large solely because the reference probability is diluted among many matched alternatives.