# AF-132 — Wasserstein recovery profiles obey a functional-composition bound

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `WASSERSTEIN-RECOVERY`, `PROFILE-CALCULUS`, `COMPOSITION-GATE`, `QUANTITATIVE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-131 shows that normalized Wasserstein recovery error does not compose as a scalar unless the regularity of the intermediate recovery map is also controlled. It therefore introduces the error/regularity profile

\[
\Phi_{\mathcal A\mid\mathcal B}(t)
:=
\min_R
\left[
 e_{\mathcal A\mid\mathcal B}(R)
 +t\,\bar\kappa_{\mathcal A\mid\mathcal B}(R)
\right],
\qquad t\ge0,
\tag{1}
\]

where `R` recovers experiment `\mathcal A` from experiment `\mathcal B`, `e(R)` is the diameter-normalized worst-parameter Wasserstein reconstruction error, and `\bar\kappa(R)` is the corresponding normalized Wasserstein Lipschitz coefficient.

For finite metric experiments this profile is not merely a convenient one-step bound. It has an exact calculus.

Let

\[
\mathcal A=(P_\theta)_{\theta\in\Theta},\qquad
\mathcal B=(Q_\theta)_{\theta\in\Theta},\qquad
\mathcal C=(S_\theta)_{\theta\in\Theta}
\]

live on finite metric spaces `(X,d_X)`, `(Y,d_Y)`, `(Z,d_Z)` of positive diameters `D_X,D_Y,D_Z`. For a recovery kernel `R:Y\rightsquigarrow X`, define

\[
e_{\mathcal A\mid\mathcal B}(R)
:=
\max_\theta
\frac{W_{1,d_X}(P_\theta,Q_\theta R)}{D_X},
\tag{2}
\]

and

\[
\bar\kappa_{\mathcal A\mid\mathcal B}(R)
:=
\frac{D_Y}{D_X}
\sup_{y\ne y'}
\frac{W_{1,d_X}(R_y,R_{y'})}{d_Y(y,y')}.
\tag{3}
\]

Define `e_{\mathcal B\mid\mathcal C}` and `\bar\kappa_{\mathcal B\mid\mathcal C}` analogously for kernels `T:Z\rightsquigarrow Y`, and similarly for direct kernels `U:Z\rightsquigarrow X`.

Then:

1. the minimum in `(1)` is attained for every `t>=0`, and `\Phi_{\mathcal A\mid\mathcal B}` is finite, continuous, nondecreasing, and concave;
2. its intercept is the AF-130 normalized Wasserstein recovery defect,
   \[
   \boxed{
   \Phi_{\mathcal A\mid\mathcal B}(0)
   =
   \delta_X(\mathcal A\mid\mathcal B);
   }
   \tag{4}
   \]
3. if
   \[
   \delta_{\le L}(\mathcal A\mid\mathcal B)
   :=
   \min_{\bar\kappa(R)\le L}
   e_{\mathcal A\mid\mathcal B}(R),
   \tag{5}
   \]
   with value `+infinity` when no such recovery exists, then
   \[
   \boxed{
   \Phi_{\mathcal A\mid\mathcal B}(t)
   =
   \inf_{L\ge0}
   \left[
   \delta_{\le L}(\mathcal A\mid\mathcal B)+Lt
   \right].
   }
   \tag{6}
   \]
   Thus the profile is exactly the lower affine envelope of the reconstruction-error/regularity Pareto frontier;
4. recovery errors and transport moduli compose simultaneously. For `R:Y\rightsquigarrow X` and `T:Z\rightsquigarrow Y`,
   \[
   e_{\mathcal A\mid\mathcal C}(TR)
   \le
   e_{\mathcal A\mid\mathcal B}(R)
   +
   \bar\kappa_{\mathcal A\mid\mathcal B}(R)
   e_{\mathcal B\mid\mathcal C}(T),
   \tag{7}
   \]
   and
   \[
   \bar\kappa_{\mathcal A\mid\mathcal C}(TR)
   \le
   \bar\kappa_{\mathcal A\mid\mathcal B}(R)
   \bar\kappa_{\mathcal B\mid\mathcal C}(T).
   \tag{8}
   \]
   Consequently the profiles satisfy the **functional-composition bound**
   \[
   \boxed{
   \Phi_{\mathcal A\mid\mathcal C}(t)
   \le
   \Phi_{\mathcal A\mid\mathcal B}
   \!\left(
   \Phi_{\mathcal B\mid\mathcal C}(t)
   \right)
   \qquad(t\ge0).
   }
   \tag{9}
   \]
5. if
   \[
   \delta_{AB}:=
   \delta_X(\mathcal A\mid\mathcal B)
   =
   \min_R e_{\mathcal A\mid\mathcal B}(R)
   \tag{10}
   \]
   and
   \[
   \kappa^*_{AB}
   :=
   \min\left\{
   \bar\kappa_{\mathcal A\mid\mathcal B}(R):
   e_{\mathcal A\mid\mathcal B}(R)=\delta_{AB}
   \right\},
   \tag{11}
   \]
   then the right derivative at the origin exists and is exactly
   \[
   \boxed{
   \Phi'_{\mathcal A\mid\mathcal B}(0+)
   =
   \kappa^*_{AB}.
   }
   \tag{12}
   \]
   The first-order sensitivity of an optimally reconstructed representation to a tiny downstream metric defect is therefore the smallest transport expansion among recovery maps that are already reconstruction-optimal;
6. writing
   \[
   \kappa^{\min}_{AB}
   :=
   \min_R
   \bar\kappa_{\mathcal A\mid\mathcal B}(R),
   \tag{13}
   \]
   the far-penalty slope is
   \[
   \boxed{
   \lim_{t\to\infty}
   \frac{\Phi_{\mathcal A\mid\mathcal B}(t)}{t}
   =
   \kappa^{\min}_{AB}.
   }
   \tag{14}
   \]

Thus the profile interpolates between two different recovery questions. Near `t=0`, reconstruction error is primary and the slope selects the least expansive **among error-optimal inverses**. At large `t`, transport regularity dominates and the slope converges to the least expansive recovery available at any reconstruction error.

Equation `(9)` also iterates. For a chain

\[
\mathcal A_0\leftarrow\mathcal A_1\leftarrow\cdots\leftarrow\mathcal A_n,
\]

one has

\[
\boxed{
\Phi_{\mathcal A_0\mid\mathcal A_n}(t)
\le
\Phi_{\mathcal A_0\mid\mathcal A_1}
\circ
\Phi_{\mathcal A_1\mid\mathcal A_2}
\circ\cdots\circ
\Phi_{\mathcal A_{n-1}\mid\mathcal A_n}(t).
}
\tag{15}
\]

The scalar Wasserstein defect is therefore only the intercept of the compositional state. The profile, or an equivalent representation of its error/regularity frontier, is what can be propagated through a metric-sensitive compression pipeline.

## Derivation

### Finite recovery profiles are attained lower envelopes

For finite `X` and `Y`, the set of Markov kernels `R:Y\rightsquigarrow X` is a compact product of simplices. The map `R\mapsto e(R)` is continuous because finite Wasserstein distance depends continuously on its probability arguments. The coefficient `R\mapsto\bar\kappa(R)` is also continuous: it is the maximum over finitely many pairs `y!=y'` of continuous Wasserstein ratios with fixed positive denominators.

Hence the objective

\[
R\mapsto e(R)+t\bar\kappa(R)
\tag{16}
\]

is continuous on a compact set and attains its minimum for every `t>=0`.

For each fixed `R`, `(16)` is an affine nondecreasing function of `t`. The pointwise minimum of affine functions is concave, and nonnegative slopes make it nondecreasing. In a finite metric space the coefficient is uniformly bounded. If

\[
m_Y:=\min_{y\ne y'}d_Y(y,y')>0,
\]

then `W_{1,d_X}(R_y,R_{y'})<=D_X`, so

\[
0\le\bar\kappa(R)\le\frac{D_Y}{m_Y}.
\tag{17}
\]

Therefore `\Phi` is globally Lipschitz and in particular continuous. Setting `t=0` in `(1)` gives `(4)` immediately.

Now define `(5)`. For every recovery `R`, choosing `L=\bar\kappa(R)` gives

\[
\inf_L[\delta_{\le L}+Lt]
\le
 e(R)+\bar\kappa(R)t.
\tag{18}
\]

Taking the minimum over `R` gives the `<=` direction of `(6)`. Conversely, whenever `\delta_{\le L}` is finite, compactness gives a minimizing recovery `R_L` with `\bar\kappa(R_L)<=L`, hence

\[
\Phi(t)
\le
 e(R_L)+t\bar\kappa(R_L)
\le
\delta_{\le L}+Lt.
\tag{19}
\]

Taking the infimum over `L` gives the reverse inequality. Thus `(6)` is exact.

This also shows why one arbitrary inverse is not the correct retained object. Recoveries that are dominated simultaneously in reconstruction error and transport regularity never support the lower envelope; only the Pareto frontier can affect downstream bounds.

### Reconstruction error and transport regularity obey compatible composition laws

Fix `R:Y\rightsquigarrow X` and `T:Z\rightsquigarrow Y`. For each `theta`, the Wasserstein triangle inequality gives

\[
W_{1,d_X}(P_\theta,S_\theta T R)
\le
W_{1,d_X}(P_\theta,Q_\theta R)
+
W_{1,d_X}(Q_\theta R,S_\theta T R).
\tag{20}
\]

AF-131's kernel transport estimate gives

\[
W_{1,d_X}(Q_\theta R,S_\theta T R)
\le
\kappa(R)
W_{1,d_Y}(Q_\theta,S_\theta T),
\tag{21}
\]

where `\kappa(R)` is the unnormalized Wasserstein Lipschitz coefficient. Dividing by `D_X`, inserting the normalization in `(3)`, and maximizing over `theta` proves `(7)`.

For `(8)`, take `z!=z'`. Applying the same transport estimate twice yields

\[
W_{1,d_X}((T_z)R,(T_{z'})R)
\le
\kappa(R)
W_{1,d_Y}(T_z,T_{z'})
\le
\kappa(R)\kappa(T)d_Z(z,z').
\tag{22}
\]

Multiplying by `D_Z/D_X` factors exactly as

\[
\frac{D_Z}{D_X}
=
\frac{D_Y}{D_X}\frac{D_Z}{D_Y},
\tag{23}
\]

which gives `(8)` for the normalized coefficients.

Combining `(7)` and `(8)`, for every `t>=0`,

\[
\begin{aligned}
&e_{\mathcal A\mid\mathcal C}(TR)
+t\bar\kappa_{\mathcal A\mid\mathcal C}(TR)\\
&\qquad\le
 e_{\mathcal A\mid\mathcal B}(R)
 +
 \bar\kappa_{\mathcal A\mid\mathcal B}(R)
 \left[
 e_{\mathcal B\mid\mathcal C}(T)
 +t\bar\kappa_{\mathcal B\mid\mathcal C}(T)
 \right].
\end{aligned}
\tag{24}
\]

For fixed `R`, minimize the bracket over `T`; then minimize over `R`. Since direct recoveries from `C` to `A` include all factor-through-`B` composites `TR`, one obtains

\[
\Phi_{\mathcal A\mid\mathcal C}(t)
\le
\min_R
\left[
 e_{\mathcal A\mid\mathcal B}(R)
 +
 \bar\kappa_{\mathcal A\mid\mathcal B}(R)
 \Phi_{\mathcal B\mid\mathcal C}(t)
\right],
\]

which is exactly `(9)` by definition `(1)`.

The inequality can be strict. A direct `C->A` recovery may exploit structure unavailable to recoveries forced to factor through `B`. Equation `(9)` is therefore a compositional upper bound, not an assertion that `B` is a sufficient intermediate representation.

### The origin slope selects the least expansive reconstruction-optimal recovery

Let

\[
\delta:=\min_R e(R),
\qquad
\kappa^*:=\min\{\bar\kappa(R):e(R)=\delta\}.
\tag{25}
\]

The set of error-optimal recoveries is nonempty and compact, so the second minimum exists. Choose an error-optimal `R^*` with coefficient `\kappa^*`. Then

\[
\Phi(t)
\le
\delta+\kappa^*t,
\tag{26}
\]

and therefore

\[
\limsup_{t\downarrow0}
\frac{\Phi(t)-\delta}{t}
\le\kappa^*.
\tag{27}
\]

For each `t>0`, choose a profile minimizer `R_t`. Equation `(26)` and `e(R_t)>=\delta` imply

\[
\delta
\le
 e(R_t)
\le
\Phi(t)
\le
\delta+\kappa^*t.
\tag{28}
\]

Hence `e(R_t)->\delta` as `t\downarrow0`. Along every sequence `t_j\downarrow0`, compactness supplies a subsequence with `R_{t_j}->R_0`. Continuity gives `e(R_0)=\delta`, so `\bar\kappa(R_0)>=\kappa^*` by definition. On the other hand optimality and `(26)` give

\[
e(R_t)+t\bar\kappa(R_t)
\le
\delta+t\kappa^*,
\tag{29}
\]

which, since `e(R_t)>=\delta`, implies

\[
\bar\kappa(R_t)\le\kappa^*.
\tag{30}
\]

Therefore every convergent subsequence of `\bar\kappa(R_t)` tends to `\kappa^*`. Finally

\[
\frac{\Phi(t)-\delta}{t}
=
\frac{e(R_t)-\delta}{t}
+
\bar\kappa(R_t)
\ge
\bar\kappa(R_t).
\tag{31}
\]

Equations `(27)`, `(30)`, and `(31)` force the quotient to converge to `\kappa^*`, proving `(12)`.

This is stronger than saying that some exact or nearly exact inverse is regular. The derivative identifies the regularity of the best inverse **subject to already achieving the optimal reconstruction defect**. Any lower-slope recovery must pay a positive intercept penalty and only becomes competitive farther along the profile.

### The large-penalty slope selects the globally least expansive recovery

Let

\[
\kappa^{\min}:=\min_R\bar\kappa(R).
\]

Since `e(R)>=0`,

\[
\Phi(t)\ge t\kappa^{\min}.
\tag{32}
\]

Choose a recovery `R_{\min}` attaining `\kappa^{\min}`. Because `e(R_{\min})<=1` for diameter-normalized Wasserstein error,

\[
\Phi(t)
\le
 e(R_{\min})+t\kappa^{\min}
\le
1+t\kappa^{\min}.
\tag{33}
\]

Divide `(32)`--`(33)` by `t` and let `t->infinity`; this proves `(14)`.

Concavity is consistent with the two slopes: the profile may switch from low-error/high-expansion recoveries to higher-error/lower-expansion recoveries as the downstream penalty grows. The slope therefore cannot increase with `t`.

### Chain composition follows by induction

Apply `(9)` first to `\mathcal A_0,\mathcal A_1,\mathcal A_n`, then recursively to the remaining tail. Every profile is nondecreasing, so replacing the tail profile by its own upper composition bound preserves the inequality. This gives `(15)`.

At `t=0`, the first three-stage consequence is

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
\Phi_{\mathcal A\mid\mathcal B}
\!\left(
\delta_Y(\mathcal B\mid\mathcal C)
\right).
}
\tag{34}
\]

Using the origin supporting line `(26)` then gives

\[
\boxed{
\delta_X(\mathcal A\mid\mathcal C)
\le
\delta_X(\mathcal A\mid\mathcal B)
+
\kappa^*_{AB}
\delta_Y(\mathcal B\mid\mathcal C).
}
\tag{35}
\]

Equation `(34)` is at least as strong as `(35)` and can be strictly stronger away from the origin because the profile is free to trade a little more first-stage reconstruction error for a much less expansive inverse.

## Sharpness on the AF-131 squeezing example

AF-131 constructs, for every `0<epsilon<1`, a three-state chain in which `A` has the equilateral metric, `B` has two distinguished states at distance `epsilon` inside a diameter-one space, the first map `A->B` is bijective, and the second map merges those two nearby states.

For that chain,

\[
\delta_X(\mathcal A\mid\mathcal B)=0,
\qquad
\delta_Y(\mathcal B\mid\mathcal C)=\frac\varepsilon2,
\qquad
\delta_X(\mathcal A\mid\mathcal C)=\frac12.
\tag{36}
\]

Every exact recovery from `B` to `A` has normalized transport coefficient at least `1/epsilon`, and the deterministic inverse attains exactly `1/epsilon`. Hence `(12)` gives

\[
\Phi'_{\mathcal A\mid\mathcal B}(0+)
=\frac1\varepsilon.
\tag{37}
\]

Equation `(34)` and the exact inverse give

\[
\frac12
=\delta_X(\mathcal A\mid\mathcal C)
\le
\Phi_{\mathcal A\mid\mathcal B}
\!\left(\frac\varepsilon2\right)
\le
\frac1\varepsilon\frac\varepsilon2
=\frac12.
\tag{38}
\]

Therefore

\[
\boxed{
\Phi_{\mathcal A\mid\mathcal B}
\!\left(\frac\varepsilon2\right)
=\frac12,
}
\tag{39}
\]

and both the profile bound and the origin-slope amplification are sharp on the same explicit finite compression chain. The profile is measuring a real pipeline fragility rather than only reorganizing a loose estimate.

## Relationship to AF-126, AF-129, AF-130, and AF-131

AF-126 identifies ordinary Le Cam recovery deficiency as the correct whole-experiment approximate defect in total variation. There the scalar defect itself composes because every stochastic recovery is automatically nonexpansive for total variation.

AF-129 shows that restricting admissible witnesses changes the dual recovery geometry. AF-130 specializes metric-local witnesses to normalized Wasserstein-1 recovery, where short-scale discrepancies are deliberately discounted. AF-131 then proves that once the retained geometry is metric-sensitive, exact or approximate reconstruction error alone is not enough for composition: one must also know how strongly the chosen inverse expands retained distances.

AF-132 closes that immediate structural gap. The pair `(error,regularity)` is naturally summarized by the lower Pareto envelope `Phi`; that envelope has an exact intercept, exact endpoint slopes, and a functional-composition inequality. In this finite setting it therefore provides a self-contained state variable for the part of downstream stability controlled by Wasserstein reconstruction and transport regularity.

This does **not** say that every structural-fidelity problem should be scalarized into one profile. It says that after AF-130 has explicitly chosen the metric-local/Wasserstein category, the profile is the minimal obvious refinement of the scalar defect needed to propagate the particular error amplification exposed by AF-131.

## Prior art and novelty assessment

The mathematical ingredients are classical.

- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419--1455 (1964), DOI `10.1214/AOMS/1177700372`. Role: classical approximate-sufficiency and deficiency framework underlying AF-126 and the experiment-comparison side of the construction.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), especially Chapter 6, DOI `10.1017/CBO9780511666353.007`. Role: authoritative treatment of deficiencies and of deficiencies relative to restricted classes of decision problems, supplying the classical statistical language behind AF-129--AF-130.
- Yann Ollivier, **“Ricci curvature of Markov chains on metric spaces,”** *Journal of Functional Analysis* 256(3), 810--864 (2009), DOI `10.1016/j.jfa.2008.11.001`. Role: primary prior art for measuring a Markov kernel by the local Wasserstein ratio `W_1(R_y,R_{y'})/d(y,y')`; the multiplicative transport estimate in `(8)` is the standard Lipschitz/contraction behavior of such kernels.
- D. A. Edwards, **“On the Kantorovich--Rubinstein theorem,”** *Expositiones Mathematicae* 29(4), 387--398 (2011), DOI `10.1016/j.exmath.2011.06.005`. Role: authoritative Kantorovich--Rubinstein duality background for the metric-local witness interpretation and kernel transport estimate.
- Stephen Boyd and Lieven Vandenberghe, ***Convex Optimization***, Cambridge University Press (2004), especially the standard dual-function observation that a pointwise infimum of affine functions is concave. Role: generic convex-analysis background for the lower-envelope geometry of `(1)`; the finite proof above is direct.

A targeted search across statistical-experiment deficiency, restricted decision classes, Wasserstein Markov contraction, and recovery tradeoff language did not establish that equations `(6)`, `(9)`, or `(12)` form a new named theorem in those literatures. They should therefore be treated as a direct finite synthesis of classical deficiency, Wasserstein contraction, and elementary parametric optimization. **No novelty claim is made.**

The Arithmetic Fidelity value is organizational and diagnostic: AF-131's warning that scalar metric-local defect is not compositional can be upgraded to an exact profile calculus, and the local slope has a concrete structural meaning that can be checked on candidate recovery maps.

## Boundary conditions and falsification checks

1. **Finite compactness is used materially.** Attainment and the exact origin-slope statement use compact finite kernel spaces and continuity. An infinite-space extension would need separate tightness, lower-semicontinuity, existence, and metric-domain hypotheses; it must not be inferred from this result.

2. **The metrics must remain intrinsic.** As in AF-130--AF-131, choosing `d_X,d_Y,d_Z` after seeing the desired inverse can manufacture a favorable profile. The theorem only audits a category whose metrics are independently part of the retained/source structure.

3. **The composition statement is one-sided.** Direct recovery may outperform every route factoring through the declared intermediate experiment. Equality in `(9)` requires additional sufficiency or factorization structure and is not claimed.

4. **The profile is not a complete invariant of recovery geometry.** Distinct sets of recovery kernels can have the same lower `(e,kappa)` envelope while differing in algebraic, topological, spectral, or arithmetic structure. AF-132 controls the metric-local propagation problem only.

5. **The penalty parameter is a calculus variable.** Actual normalized Wasserstein recovery defects lie in `[0,1]`, while `(1)` is defined for all `t>=0` so that the Pareto envelope and asymptotic slope are mathematically visible. Large-`t` behavior need not correspond to an actually realized downstream defect.

6. **Zero intercept does not imply a safe pipeline.** If `Phi(0)=0` but `Phi'(0+)` is large, exact stagewise recoverability coexists with severe sensitivity to the next compression. AF-131's `1/epsilon` example realizes precisely this case.

7. **No prime-specific fidelity follows.** Nothing here supplies an intrinsic arithmetic metric, a canonical recovery kernel, or a rational-prime discriminator. A concrete RH line must prove that its own representation induces the required metric category before this profile calculus can constrain it.

## Consequences for Arithmetic Fidelity

The README asks for composition laws that certify what is lost at an intermediate stage and cannot be recreated downstream. AF-126 supplied such a law in the unrestricted total-variation category. AF-131 showed that the same scalar law fails after imposing metric-local witnesses. AF-132 identifies the corresponding replacement: **propagate a recovery profile, not only an intercept.**

This gives a sharper audit for future compression pipelines. For a candidate intermediate representation, it is not enough to report that the current discriminator is reconstructible or nearly reconstructible. One should ask whether the reconstruction lies on a favorable error/regularity frontier, because the origin slope determines first-order downstream amplification and the full profile determines the best bound after a finite later defect.

The result also exposes a reusable pattern for other restricted fidelity categories. Whenever a downstream discrepancy is transported through a recovery by a category-specific modulus, the scalar reconstruction defect is unlikely to be compositionally closed. The next research question is therefore not to assume that the Wasserstein profile generalizes automatically, but to determine which other admissible witness geometries admit an intrinsic recovery modulus and an analogous profile composition theorem.