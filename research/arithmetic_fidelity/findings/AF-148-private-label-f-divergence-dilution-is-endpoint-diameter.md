# AF-148 — Private-label f-divergence dilution is exactly the endpoint-diameter boundary

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-F-DIVERGENCE-SPECIALIZATION`, `STRUCTURAL-CLASSIFICATION`, `FAMILY-COMPLEXITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-146 and AF-147 show two very different family-size penalties for the same private-label compression: the optimized common-reference Pearson chi-square profile grows like `m`, while the optimized common-reference KL profile grows like `log m`, even though the exact one-sided recovery deficiency is the same in both cases. This is not a coincidence peculiar to those two divergences. The entire phenomenon is already classified by the reverse-support penalty from AF-050 and by the classical endpoint diameter of a Csiszar `f`-divergence.

Fix `m>=2` and `0<rho<=1`. On

\[
X=\{0,1,\ldots,m\}
\]

consider the finite experiment

\[
P_i=(1-\rho)\delta_0+\rho\delta_i,
\qquad i=1,\ldots,m,
\tag{1}
\]

and the compression `K` that fixes `0` and sends every private label `i>=1` to one common symbol `*`. Hence all compressed laws are equal:

\[
Q_i=P_iK=(1-\rho)\delta_0+\rho\delta_*.
\tag{2}
\]

Let `f:[0,\infty)\to(-\infty,+\infty]` be convex and lower semicontinuous, finite on `(0,\infty)`, with `f(1)=0`. Write

\[
f_0=f(0),
\qquad
f_\infty=\lim_{t\to\infty}\frac{f(t)}{t},
\tag{3}
\]

with either endpoint allowed to be `+infinity`. For a full-support prior `lambda=(lambda_1,...,lambda_m)`, let

\[
M_\lambda=\sum_i\lambda_iP_i,
\qquad
N_\lambda=M_\lambda K,
\tag{4}
\]

and define the common-reference `f`-divergence data-processing loss

\[
\varepsilon_i^{(f)}(\lambda)
=
D_f(P_i\|M_\lambda)
-
D_f(Q_i\|N_\lambda).
\tag{5}
\]

Define the optimized family profile

\[
\Gamma_f(K;\mathcal E_m)
=
\inf_{\lambda\in\Delta_m^\circ}
\max_i\varepsilon_i^{(f)}(\lambda).
\tag{6}
\]

Then:

1. every output divergence in `(5)` vanishes, and for every `i`
   \[
   \boxed{
   \varepsilon_i^{(f)}(\lambda)
   =
   \rho\,\Phi_f(\lambda_i),
   }
   \qquad
   \Phi_f(p)
   :=
   p f(1/p)+(1-p)f_0;
   \tag{7}
   \]
   thus the common-reference loss on this family is exactly `rho` times AF-050's reverse-support penalty;

2. `Phi_f` is nonincreasing on `(0,1]`, so the uniform prior is always a minimizer of `(6)` and
   \[
   \boxed{
   \Gamma_f(K;\mathcal E_m)
   =
   \rho\,\Phi_f(1/m)
   =
   \rho\left[
   \frac1m f(m)
   +\left(1-\frac1m\right)f_0
   \right];
   }
   \tag{8}
   \]
   uniqueness of the uniform minimizer is not claimed when `Phi_f` has flat pieces;

3. AF-146's exact minimax recovery calculation is metric-independent here and gives
   \[
   \boxed{
   \delta_{\rm rec}(K;\mathcal E_m)
   =
   \rho\left(1-\frac1m\right),
   }
   \tag{9}
   \]
   hence the exact profile-to-recovery ratio is
   \[
   \boxed{
   \frac{\Gamma_f(K;\mathcal E_m)}
        {\delta_{\rm rec}(K;\mathcal E_m)}
   =
   \frac{\Phi_f(1/m)}{1-1/m};
   }
   \tag{10}
   \]

4. if both endpoint constants are finite, set
   \[
   C_f:=f_0+f_\infty.
   \tag{11}
   \]
   Then the classical sharp `f`-divergence/total-variation bound gives, and here one can also verify directly,
   \[
   \boxed{
   \Gamma_f(K;\mathcal E_m)
   \le
   C_f\,\delta_{\rm rec}(K;\mathcal E_m),
   }
   \tag{12}
   \]
   for every `m`, while
   \[
   \boxed{
   \lim_{m\to\infty}
   \frac{\Gamma_f(K;\mathcal E_m)}
        {\delta_{\rm rec}(K;\mathcal E_m)}
   =C_f.
   }
   \tag{13}
   \]
   Thus the private-label family asymptotically saturates the classical endpoint-diameter constant;

5. conversely, the family-size dilution obstruction is unbounded exactly when the relevant endpoint diameter is infinite. If `f_0<infinity` and `f_infinity=+infinity`, then
   \[
   \Phi_f(1/m)
   =
   f_0+\frac{f(m)-f_0}{m}
   \longrightarrow+\infty.
   \tag{14}
   \]
   Choosing
   \[
   \rho_m=\frac{1}{\Phi_f(1/m)}
   \tag{15}
   \]
   for all sufficiently large `m` gives
   \[
   \delta_{\rm rec}(K;\mathcal E_m)\to0,
   \qquad
   \Gamma_f(K;\mathcal E_m)=1.
   \tag{16}
   \]
   If instead `f_0=+infinity`, then `Gamma_f=+infinity` for every `m>=2` and every `rho>0` because every full-support common mixture assigns positive mass to private labels absent from `P_i`.

Therefore the Pearson and KL examples are two points on one exact phase diagram. For this canonical family-collapse control, **dimension-free calibration of the raw common-reference `f`-loss against recovery deficiency occurs precisely in the finite-endpoint-diameter regime; infinite endpoint diameter permits vanishing recovery defect with order-one or infinite common-reference loss.**

This does **not** say that every finite-diameter `f`-loss is a general recovery certificate. AF-144's Pearson and AF-147's KL bounds use special Bayes/Petz or chain-rule mechanisms that construct one common reverse channel. The present result classifies the calibration behavior of this adversarial family only; bounded endpoint diameter removes this particular family-size pathology but does not supply a reverse kernel in an arbitrary experiment.

## Derivation

### The private-label loss is AF-050's reverse support penalty

For a full-support prior `lambda`, the source mixture is

\[
M_\lambda
=(1-\rho)\delta_0
+\rho\sum_{j=1}^m\lambda_j\delta_j.
\tag{17}
\]

All `Q_i` equal `N_lambda`, so

\[
D_f(Q_i\|N_\lambda)=0.
\tag{18}
\]

For fixed `i`, the likelihood ratio `P_i/M_lambda` equals `1` at `0`, `1/lambda_i` at private symbol `i`, and `0` at every private symbol `j!=i`. Therefore

\[
\begin{aligned}
D_f(P_i\|M_\lambda)
&=(1-\rho)f(1)
 +\rho\lambda_i f(1/\lambda_i)
 +\rho\sum_{j\ne i}\lambda_j f(0)\\
&=\rho\left[
\lambda_i f(1/\lambda_i)
 +(1-\lambda_i)f_0
\right]\\
&=\rho\Phi_f(\lambda_i),
\end{aligned}
\tag{19}
\]

which proves `(7)`. The same scalar function `Phi_f` appeared in AF-050 as the exact reverse `f`-divergence cost of restricting a law to a support cell retaining mass `p`. Here the common mixture assigns retained mass `lambda_i` to the private support of member `i`, so the two constructions are literally the same binary penalty.

### Convexity makes the uniform prior minimax

Assume first `f_0<infinity`. Put `t=1/p>=1`. Then

\[
\Phi_f(p)
=f_0+\frac{f(t)-f_0}{t}.
\tag{20}
\]

For a convex function, the secant slope

\[
\frac{f(t)-f(0)}{t-0}
\tag{21}
\]

is nondecreasing in `t`. Hence `(20)` is nondecreasing in `t=1/p`, equivalently `Phi_f(p)` is nonincreasing in `p`.

If `f_0=+infinity`, then `Phi_f(p)=+infinity` for every `0<p<1`, so the same minimax conclusion holds in the extended sense.

Every full-support prior has

\[
\min_i\lambda_i\le\frac1m.
\tag{22}
\]

Since `Phi_f` is nonincreasing,

\[
\max_i\Phi_f(\lambda_i)
=
\Phi_f(\min_i\lambda_i)
\ge
\Phi_f(1/m).
\tag{23}
\]

The uniform prior attains equality, proving `(8)`. Strict decrease is not automatic for a general convex generator, so no unnecessary uniqueness claim is made.

### Finite endpoint diameter gives a uniform calibration constant

Assume `f_0` and `f_infinity` are finite. Convexity and `f(1)=0` imply that the secant slopes from `1` obey

\[
\frac{f(t)}{t-1}\le f_\infty,
\qquad t>1,
\tag{24}
\]

because their increasing limit is the recession slope `f_infinity`. Setting `t=1/p` gives

\[
p f(1/p)
\le
(1-p)f_\infty.
\tag{25}
\]

Therefore

\[
\Phi_f(p)
\le
(1-p)(f_0+f_\infty)
=(1-p)C_f.
\tag{26}
\]

At `p=1/m`, equations `(8)` and `(9)` yield `(12)`.

Moreover

\[
\Phi_f(1/m)
=f_0+\frac{f(m)-f_0}{m}
\longrightarrow
f_0+f_\infty=C_f,
\tag{27}
\]

while `1-1/m -> 1`, proving `(13)`.

The constant is invariant under the standard generator ambiguity

\[
f(t)\mapsto f(t)+c(t-1),
\tag{28}
\]

because this sends `f_0 -> f_0-c` and `f_infinity -> f_infinity+c`. The exact finite-`m` quantity `Phi_f` is invariant for the same reason, as already recorded in AF-050.

### Infinite endpoint diameter reproduces and generalizes the dilution examples

If `f_0<infinity` but `f_infinity=+infinity`, convexity gives the extended limit

\[
\frac{f(m)}{m}\to+\infty,
\tag{29}
\]

so `(14)` follows. The scaling `(15)` is eventually in `(0,1]`; substituting it into `(8)` gives `Gamma_f=1`, while `(9)` gives

\[
\delta_{\rm rec}
=
\frac{1-1/m}{\Phi_f(1/m)}
\to0.
\tag{30}
\]

Thus the AF-146 Pearson construction (`Phi_f(1/m)=m-1`) and AF-147 KL construction (`Phi_f(1/m)=log m`) are instances of one general endpoint-growth obstruction, not qualitatively separate pathologies.

If `f_0=+infinity`, equation `(19)` is already infinite because `1-lambda_i>0` for every member under every full-support prior when `m>=2`. This is the opposite endpoint singularity: the source member assigns zero mass to reference-positive labels and the divergence charges those zeros infinitely.

## Examples

The exact formula `(8)` recovers and extends the recent metric-specific calculations:

- **Pearson chi-square:** `f(t)=(t-1)^2`, `f_0=1`, `f_infinity=+infinity`, so
  \[
  \Gamma_f=\rho(m-1),
  \]
  reproducing AF-146.
- **Kullback--Leibler:** `f(t)=t\log t`, `f_0=0`, `f_infinity=+infinity`, so
  \[
  \Gamma_f=\rho\log m,
  \]
  reproducing AF-147.
- **Squared Hellinger:** `f(t)=(\sqrt t-1)^2`, `f_0=f_infinity=1`, so
  \[
  \Gamma_f
  =2\rho\left(1-\frac1{\sqrt m}\right),
  \qquad
  \frac{\Gamma_f}{\delta_{\rm rec}}\to2.
  \]
- **Total variation:** `f(t)=|t-1|/2`, `f_0=f_infinity=1/2`, so
  \[
  \Gamma_f
  =\rho\left(1-\frac1m\right)
  =\delta_{\rm rec}
  \]
  exactly on this family.
- **Reverse KL:** `f(t)=-\log t` has `f_0=+infinity`, so the common-reference profile is infinite for every nontrivial private-label family despite finite recovery deficiency.

These examples show why choosing a superficially gentler divergence can remove the family-size blow-up without solving the underlying common-recovery problem. Total variation is perfectly calibrated on this control because its endpoint diameter is finite, but AF-143 already shows that preserved pairwise total-variation geometry does not by itself produce one reverse channel for a whole experiment.

## Prior art and novelty assessment

No theorem-level novelty is claimed for the `f`-divergence ingredients.

- Imre Csiszar, **“Information-type measures of difference of probability distributions and indirect observations,”** *Studia Scientiarum Mathematicarum Hungarica* 2, 299--318 (1967), is foundational prior art for convex divergences under indirect observation and data processing.
- Friedrich Liese and Igor Vajda, **“On Divergences and Informations in Statistics and Information Theory,”** *IEEE Transactions on Information Theory* 52(10), 4394--4412 (2006), DOI `10.1109/TIT.2006.881731`, is authoritative prior art for general `f`-divergences, statistical information, sufficiency, and deficiency.
- Igal Sason and Sergio Verdu, **“f-Divergence Inequalities,”** *IEEE Transactions on Information Theory* 62(11), 5973--6006 (2016), DOI `10.1109/TIT.2016.2603151`, records the classical range bound
  \[
  0\le D_f(P\|Q)\le f(0)+f^*(0)
  \]
  (citing Vajda) and proves the sharp ratio theorem
  \[
  \sup_{P\ne Q}
  \frac{D_f(P\|Q)}{\|P-Q\|_1}
  =\frac12\bigl(f(0)+f^*(0)\bigr),
  \]
  where `f^*(0)=f_infinity`. In the convention `TV=||P-Q||_1/2`, the sharp constant is therefore exactly `C_f=f_0+f_infinity`, the same constant approached in `(13)`.
- AF-050 already derives the exact reverse-support penalty `Phi_f(p)` and its endpoint taxonomy. AF-148 is the private-label/common-reference specialization that exposes AF-146 and AF-147 as instances of that earlier general structure and identifies their family-size behavior with the classical sharp endpoint-diameter constant.

The durable Arithmetic Fidelity contribution is therefore organizational and diagnostic rather than a new information-theory theorem: **the private-label control completely classifies which raw common-reference `f`-profiles suffer a family-size dilution gap.** The answer is not “Pearson bad, KL better”; it is the endpoint geometry of the chosen divergence. This closes metric-by-metric exploration of this control family as a source of qualitatively new behavior.

## Boundary conditions and falsification tests

1. **This is a control-family theorem, not a universal recovery theorem.** Equations `(8)`--`(16)` classify the declared private-label experiment. They do not imply `Gamma_f <= C delta_rec` for arbitrary experiments, nor do they construct a common reverse kernel for a general `f`.

2. **Uniform is an optimizer, not always the unique optimizer.** Flat regions of `Phi_f` can make nonuniform priors equally good. Any uniqueness claim needs additional strictness assumptions on the generator.

3. **Full-support priors are load-bearing for the stated profile.** Allowing zero prior weights can remove experiment members from the common reference and changes both support and recovery semantics. The profile in `(6)` deliberately follows AF-144/AF-147's full-family common-reference convention.

4. **Endpoint values are generator-normalization invariant only in combination.** `f_0` and `f_infinity` separately shift under addition of `c(t-1)`, but `C_f` and `Phi_f` do not. Interpret the phase diagram through those invariant combinations.

5. **Finite endpoint diameter only kills this family-size pathology.** Hellinger and total variation remain boundedly calibrated on the private-label family, but AF-143 prevents promoting that fact to family-level recoverability without an additional common-kernel theorem.

6. **Infinite diameter can arise from either endpoint, with different mechanisms.** `f_infinity=+infinity` makes increasingly rare reference weight on the true private label expensive as `m` grows; `f_0=+infinity` makes every reference-positive label absent from a given member immediately singular. Conflating the two hides the support directionality already isolated in AF-050.

7. **No arithmetic conclusion follows.** The private-label experiment is an abstract matched control. An RH-facing application still must derive a source-natural experiment, compression, discriminator, and compatibility object from arithmetic rather than selecting an `f`-profile because it has favorable endpoint calibration.

## Consequence for the research line

AF-146 and AF-147 should no longer motivate a search over additional `f`-divergences merely to improve their `m`-dependence on the same private-label control. AF-050 plus the present specialization already gives the exact answer for the whole Csiszar class: finite endpoint diameter yields bounded calibration on this family, infinite endpoint diameter permits dilution, and the precise finite-`m` penalty is `Phi_f(1/m)`.

The live question remains the one emphasized by AF-143--AF-145: **which source-natural, family-wide retained quantity forces one compatible reverse channel, and how does its calibration behave when the control family grows?** Changing the scalar divergence can alter the certificate's conditioning, but it does not replace the common-recovery compatibility requirement.