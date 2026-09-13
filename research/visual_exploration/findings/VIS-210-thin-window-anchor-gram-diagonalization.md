# VIS-210 — thin active windows diagonalize the one-cancellation anchor Gram kernel

## Claim

Work in the one-cancellation regime of `VIS-203` and with the exact six-anchor Gram reduction of `VIS-209`. Let

`lambda_r = L_tri + r`, `1 <= r <= R`,

with integer `R>=2`, and let

`C_r = {2 lambda_r, 3 lambda_r-1, 4 lambda_r-2, 4 lambda_r, 5 lambda_r-2, 6 lambda_r-3}`.

For the fluctuation vectors `Psi_r` of `VIS-209`, write

`G_rs = <Psi_r,Psi_s> = sum_(c in C_r cap C_s) alpha_r(c) alpha_s(c)`.

Then the following exact support statement holds:

> If `L_tri > 5R-5`, then `C_r cap C_s` is empty for every `r != s`.

Consequently the Gram matrix is diagonal:

`G_rs = 0` for `r != s`,

and

`G_rr = sum_(c in C_r) alpha_r(c)^2`.

In particular,

`||G||_op = max_(1<=r<=R) G_rr`.

There is also an exact near-boundary refinement. If

`L_tri > 4R-3`,

then every possible off-diagonal anchor collision has already been excluded except the collision between the `6 lambda-3` and `5 lambda-2` anchor families. Such a surviving collision is possible only on the integer resonance

`L_tri = 5s - 6r + 1`

for some shell indices `1<=r,s<=R`, where the `6 lambda_r-3` anchor meets `5 lambda_s-2`. Thus the region immediately below the diagonal cone is not a generic dense-coupling regime: it is a sparse explicitly parameterized resonance fringe.

**Evidence/status:** `EXACT-DERIVED + STRUCTURAL + FLUCTUATION-FRONTIER + NO-NOVELTY-CLAIM`.

No estimate for the diagonal energies `G_rr`, no useful sign law for them beyond positivity, no statement outside the one-cancellation regime, and no RH criterion is claimed.

## 1. Collision equations reduce to six affine families

The six anchor families are affine functions of the shell index:

- `2L_tri + 2r`;
- `3L_tri + 3r - 1`;
- `4L_tri + 4r - 2`;
- `4L_tri + 4r`;
- `5L_tri + 5r - 2`;
- `6L_tri + 6r - 3`.

Consider a collision between a larger-slope family `A(L_tri+r)+b_A` and a smaller-slope family `C(L_tri+s)+b_C`, with `A>C`. Equality is equivalent to

`(A-C)L_tri = C s - A r + b_C-b_A`.

Because `1<=r,s<=R`, any positive collision value satisfies

`L_tri <= [C R - A + b_C-b_A]/(A-C)`.

This is an exact finite reduction: no asymptotic estimate, probability model, or visual inference remains.

Equal-slope families cause no off-diagonal exception. For the same anchor family, equality forces `r=s`. The only two distinct families with equal slope are `4 lambda-2` and `4 lambda`; their cross-collision would require `4(r-s)=2`, impossible for integer shell indices.

## 2. The worst collision is the adjacent `6/5` pair

Maximizing the preceding collision bound over the available offsets gives the following worst value for each unequal pair of slopes:

| larger/smaller slope | largest possible collision value of `L_tri` |
| --- | ---: |
| `6/5` | `5R-5` |
| `6/4` | `2R-3/2` |
| `6/3` | `R-4/3` |
| `6/2` | `R/2-3/4` |
| `5/4` | `4R-3` |
| `5/3` | `3R/2-2` |
| `5/2` | `2R/3-1` |
| `4/3` | `3R-3` |
| `4/2` | `R-1` |
| `3/2` | `2R-2` |

For `R>=2`, every entry is at most `5R-5`. Therefore `L_tri>5R-5` rules out every unequal-slope collision, and the equal-slope check above rules out the rest. This proves pairwise disjointness of the `C_r`.

The constant is not an artifact of a coarse estimate. The `6/5` collision equation is

`6(L_tri+r)-3 = 5(L_tri+s)-2`,

hence

`L_tri = 5s-6r+1`.

Taking `r=1`, `s=R` gives `L_tri=5R-5`, so for `R>=2` the outer boundary itself can contain an off-diagonal collision. At `R=2`, the `5/4` family can also attain the same boundary value; this does not affect the strict collision-free cone.

The next-largest family bound is `4R-3`. Hence once `L_tri>4R-3`, only the `6/5` equation can still produce an off-diagonal intersection. This gives the stated sparse resonance fringe.

## 3. Gram diagonalization is then exact

`VIS-209` already proved

`G_rs = sum_(c in C_r cap C_s) alpha_r(c) alpha_s(c)`.

Inside the cone `L_tri>5R-5`, the intersection is empty whenever `r!=s`, so every cross-shell covariance vanishes exactly. For `r=s`, the six anchors are distinct in the present regime and

`G_rr = sum_(c in C_r) alpha_r(c)^2 >= 0`.

Thus the entire fluctuation Gram problem separates into independent shell energies. Since a diagonal positive-semidefinite matrix has operator norm equal to its largest diagonal entry,

`||G||_op = max_r sum_(c in C_r) alpha_r(c)^2`.

This is stronger than saying distant shells are approximately decorrelated: in this thin-window cone the particular one-cancellation fluctuation vectors from `VIS-209` have exactly disjoint finite support.

## 4. What this removes and what remains

The result closes one possible source of difficulty in the `VIS-209` fluctuation frontier. Cross-shell Gram growth cannot arise merely from complicated overlap among the six affine anchor families when the active window is narrower than the exact collision cone.

It does **not** make the remaining analytic problem trivial. The diagonal energies still contain the shell probabilities

`rho_lambda(c)`

and the exact signed shell coefficients through `alpha_r(c)`. Any useful bound or asymptotic still has to control those weights uniformly in the regime relevant to the Riemann problem. Outside `L_tri>5R-5`, sparse anchor resonances may couple shells, and below `4R-3` additional affine families can collide.

The next mathematically distinct question is therefore not another support calculation. It is whether the diagonal energy profile

`E_r = sum_(c in C_r) alpha_r(c)^2`

has a strong enough uniform decay or concentration law in the admissible one-cancellation regime, and how that law changes when the explicit resonance set is entered. That requires a new probabilistic/asymptotic argument and is intentionally left outside this finding.

## Prior-art and novelty audit

The diagonal-Gram consequence of disjoint vector support is elementary linear algebra and is not claimed as novel. The affine collision calculation is likewise an elementary finite consequence of the six exact anchor locations already derived in `VIS-209`; it does not invoke an external theorem.

No external literature source is needed to justify the claim, and no general theorem about banded Gram matrices, sparse resonances, or covariance localization is claimed. The durable content here is only the exact specialization to the Mathia one-cancellation anchor system: the collision-free cone `L_tri>5R-5`, the `4R-3` single-family fringe boundary, and the explicit surviving `6/5` resonance equation.