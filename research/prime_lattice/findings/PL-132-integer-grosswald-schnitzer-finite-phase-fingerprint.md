# PL-132 — Integer Grosswald–Schnitzer compactness yields a finite tail-uniform phase fingerprint

## Claim

Let `p_1<p_2<...` be the rational primes and restrict the Grosswald–Schnitzer controls to integers

`q_n in A_n := Z intersect [p_n,p_(n+1)]`.

For an admissible sequence `q=(q_n)`, let

`phi_q(s)=prod_n (1-p_n^(-s))/(1-q_n^(-s))`

be the Grosswald–Schnitzer nonvanishing quotient on `Re(s)>0`, and let

`R_q(s)=phi_q(s)/phi_q(1-s)`

be its reflection cocycle. Fix a finite prime cutoff `X`, put

`J=J(X)=max{n : p_n<=X}`,

and fix any nondegenerate compact critical-line height interval `I=[a,b]`, `a<b`.

Then there exist finitely many heights

`t_1,...,t_m in I`

and a constant `eta=eta(X,I)>0` such that for every two admissible **integer** Grosswald–Schnitzer sequences `q,r`,

`(q_1,...,q_J) != (r_1,...,r_J)`

implies

`max_(1<=k<=m) |R_q(1/2+i t_k)-R_r(1/2+i t_k)| >= eta`.

Thus a finite vector of exact critical-line phase values identifies every integer Grosswald–Schnitzer generator below any prescribed finite cutoff, **uniformly over the entire arbitrary admissible integer tail**. The separation is robust in the topological sense: different prefix classes remain a positive distance apart in this finite fingerprint.

The result is non-effective. It proves existence of `m`, sample locations, and a positive separation margin, but gives no useful explicit numerical bound for them. It therefore resolves the accepted finite-integer fingerprint clue in the existence/stability sense while leaving an effective sample-complexity problem separate.

**Evidence/status:** `EXACT-DERIVED + POSITIVE-IDENTIFIABILITY + CLUE-RESOLUTION`.

This is not an RH mechanism. All members of the Grosswald–Schnitzer family already share the zeta zero divisor in `Re(s)>0`; the theorem concerns recoverability of the discrete generator prefix from a phase observable.

## Step 1: the integer control space is compact with a finite prefix quotient

For each `n`,

`A_n=Z intersect [p_n,p_(n+1)]`

is a nonempty finite discrete set. Hence

`Q_Z = prod_(n>=1) A_n`

is compact in the product topology. Since the product is countable, it is also metrizable, although metrizability is not needed for the separation argument.

For fixed `X`, define the prefix map

`P_X(q)=(q_1,...,q_J)`.

Its range

`P_X(Q_Z)=prod_(1<=n<=J) A_n`

is finite. For every prefix value `alpha`, the cylinder

`C_alpha={q in Q_Z : P_X(q)=alpha}`

is clopen and compact. This finite clopen quotient is the load-bearing arithmetic difference from the real Grosswald–Schnitzer control space used in `PL-130`.

## Step 2: the phase-arc map is continuous in the full arbitrary tail

Define

`Phi_I : Q_Z -> C(I)`

by

`Phi_I(q)(t)=R_q(1/2+i t)`.

The map is continuous for the product topology on `Q_Z` and the uniform norm on `C(I)`.

The required uniform tail estimate is already implicit in the growth analysis of `PL-131`, but it is useful to record it explicitly. For

`s=1/2+i t`, `t in I`,

put

`H_s(x)=log(1-x^(-s))`, `x>1`,

using the branch given by the absolutely convergent logarithmic series. Differentiating in the real variable `x` gives

`partial_x H_s(x)=s x^(-s-1)/(1-x^(-s))`.

On the bounded height interval `I`, there is a constant `C_I` such that for all `x>=2`,

`|partial_x H_s(x)| <= C_I x^(-3/2)`.

Therefore, uniformly for every admissible `q_n in [p_n,p_(n+1)]`,

`|H_s(p_n)-H_s(q_n)| <= C_I (p_(n+1)-p_n) p_n^(-3/2)`.

The majorant is summable. Indeed Bertrand's postulate gives `p_(n+1)<=2p_n`; since `x^(-3/2)` is decreasing,

`(p_(n+1)-p_n) p_n^(-3/2) <= 2^(3/2) integral_[p_n,p_(n+1)] x^(-3/2) dx`,

and the intervals `[p_n,p_(n+1)]` telescope through the positive axis. Hence the logarithmic Grosswald–Schnitzer factor differences converge uniformly in both `q` and `t in I`.

Now let a net (or sequence, since `Q_Z` is metrizable) `q^(k)` converge to `q` in the product topology. For any fixed `N`, the first `N` coordinates are eventually exactly equal because each `A_n` is discrete. The common uniform tail bound then makes `log phi_(q^(k))` converge uniformly to `log phi_q` on the critical-line arc. The same holds at `1-s`, so

`||Phi_I(q^(k))-Phi_I(q)||_infinity -> 0`.

Thus `Phi_I` is continuous without freezing or truncating the tail.

## Step 3: phase-arc injectivity gives a positive separation between integer prefix cylinders

`PL-131` proves a stronger global fact for the original **real** Grosswald–Schnitzer class: if two reflection cocycles agree on any critical-line set with a finite accumulation point, then the complete generator sequences agree. In particular,

`Phi_I(q)=Phi_I(r) => q=r`

for all `q,r in Q_Z`.

Thus `Phi_I` is injective on the compact integer control space. For two distinct integer prefix values `alpha != beta`, the compact image sets

`K_alpha=Phi_I(C_alpha)`,

`K_beta=Phi_I(C_beta)`

are disjoint compact subsets of the metric space `C(I)`. Consequently

`Delta_(alpha,beta) := inf{ ||f-g||_infinity : f in K_alpha, g in K_beta } > 0`.

There are only finitely many prefix classes, so the minimum over all distinct pairs exists and is positive:

`Delta_X(I) := min_(alpha!=beta) Delta_(alpha,beta) > 0`.

Equivalently, if two admissible integer tails differ anywhere below `X`, then their **whole phase arcs** are separated by the same tail-uniform positive margin `Delta_X(I)`.

This is stronger than pointwise injectivity. The positive gap comes from compactness plus the finite discrete prefix quotient; it would be false as a uniform statement if distinct prefixes could approach one another continuously.

## Step 4: compactness compresses the separating arc to finitely many phase samples

The image

`K=Phi_I(Q_Z)`

is compact in `C(I)`. Every compact subset of `C(I)` is uniformly equicontinuous. A direct proof avoids invoking any additional structure: for any `epsilon>0`, cover `K` by finitely many uniform balls of radius `epsilon/3`; choose a common continuity scale for their finitely many center functions. Any member of `K` then varies by less than `epsilon` at points within that scale.

Take `epsilon=Delta_X(I)/4`. There is `delta>0` such that for every `f in K`,

`|t-u|<delta => |f(t)-f(u)|<Delta_X(I)/4`.

Choose a finite `delta`-net

`S={t_1,...,t_m} subset I`.

If `P_X(q)!=P_X(r)`, then

`||Phi_I(q)-Phi_I(r)||_infinity >= Delta_X(I)`.

Because `I` is compact, the supremum is attained at some `t_* in I`. Choose `t_k in S` with `|t_k-t_*|<delta`. The triangle inequality gives

`|R_q(1/2+i t_k)-R_r(1/2+i t_k)|`

`>= Delta_X(I)-Delta_X(I)/4-Delta_X(I)/4`

`= Delta_X(I)/2`.

Therefore the claimed theorem holds with

`eta(X,I)=Delta_X(I)/2 > 0`.

No unwrapped phase branch is needed: the fingerprint uses the complex unit-circle values of `R_q`, so there is no `2 pi` ambiguity.

## Why this does not contradict the real-control obstruction in PL-130

`PL-130` proves that every prescribed finite collection of natural phase samples and jets has exact aliases when the controls `q_n` vary continuously over the real prime gaps. The present theorem does not challenge that result. It uses a topological feature that disappears in the real class.

For integer controls, the low-prefix range is finite. Distinct prefix cylinders are compact, disjoint, and separated before finite sampling. For real controls, the set of pairs with different low prefixes is not closed away from the diagonal: two distinct prefix values can be arbitrarily close. Injectivity of the full phase arc therefore supplies no positive uniform prefix gap, and the tail can exploit the continuous degrees of freedom constructed in `PL-130` to create exact finite-dimensional aliases.

The resulting boundary is sharp at the level currently proved:

- real controls: no fixed finite natural phase fingerprint is locally identifying (`PL-130`);
- real or integer controls: an accumulating exact phase set is globally identifying (`PL-131`);
- integer controls: for every fixed finite prefix, **some finite phase-sample fingerprint already separates all possible arbitrary tails** (present result).

Thus integer discreteness really does collapse the information requirement from an analytic germ to a finite observation vector for each fixed finite prefix.

## Prior-art and novelty audit

The external analytic ingredient is classicalized by the preceding line. Grosswald–Schnitzer supply the admissible deformation class and its analytic nonvanishing quotient in `Re(s)>0`; `PL-131` derives reflection-phase injectivity on every nontrivial critical-line arc. No novelty is claimed for compactness of a countable product of finite spaces, positive distance between disjoint compact sets, or finite-grid approximation of a compact family in `C(I)`.

Targeted searches around Grosswald–Schnitzer modified zeta functions, integer generator restrictions, finite critical-line phase samples, inverse recovery, and compactness did not locate a source stating this finite-prefix fingerprint consequence. That absence is not used as a broad literature novelty claim. The durable contribution here is the exact derived bridge: once `PL-131` is available, the **integer** restriction converts global arc injectivity into finite tail-uniform low-prefix identifiability by a short compactness argument.

Primary literature already audited by `PL-125` through `PL-131`:

- Emil Grosswald, F. J. Schnitzer, “A class of modified zeta and L-functions,” *Pacific Journal of Mathematics* **74**(2) (1978), 357–364. DOI: https://doi.org/10.2140/pjm.1978.74.357.

No `SOURCES.md` entry is added because this finding introduces no new external source beyond the already-audited Grosswald–Schnitzer literature.

## Adversarial boundaries

The theorem is **non-effective**. `Delta_X(I)` is proved positive as the distance between finitely many compact image sets, but no computable lower bound is obtained. Likewise the finite sampling set is obtained from uniform equicontinuity, not from an explicit formula for `m` or the sample locations. An effective inverse theorem would need quantitative control absent here.

The cutoff `X` must be fixed. The theorem does not assert that one finite sample vector reconstructs the entire infinite generator sequence, nor does it give bounds uniform as `X->infinity`.

The full arbitrary integer tail remains active. The proof does not truncate, freeze, or assume finite support; that point is essential because tail-frozen uniqueness was already excluded as progress by the clue.

The theorem is phase-sensitive, not modulus-sensitive. On the critical line `|R_q|=1` for every admissible real sequence, so magnitude-only observables remain blind.

The proof depends on exact Grosswald–Schnitzer arc injectivity from `PL-131`. Generic compactness alone cannot create arithmetic information: if the phase-arc map were noninjective between two prefix cylinders, their image distance would be zero and the argument would fail immediately.

Finally, this supplies no RH localization. All admissible controls have the same nontrivial zero divisor by construction. The theorem distinguishes generator systems inside an isozero family; it does not show that the shared zeros lie on `Re(s)=1/2`.

## Consequence for the prime-lattice line

The accepted finite-integer phase-fingerprint clue is resolved at the existence level. Integer Grosswald–Schnitzer discreteness is not merely a numerical convenience: for every fixed low-prime window it creates a finite clopen quotient whose classes remain positively separated under the injective critical-line phase arc, and compactness then compresses that separation to finitely many samples.

The remaining quantitative problem is different and should not reopen finite-fingerprint existence. A future direction would need to estimate `Delta_X(I)`, produce explicit sampling heights and sample complexity as functions of `X` and `I`, or prove useful asymptotics for the conditioning of the inverse problem. Such estimates could still be difficult and arithmetically meaningful, but the yes/no identifiability question posed by the clue is closed.