# VIS-052 — fixed Fisher-gauge balance returns obey a Descartes sign budget

## Claim

Assume the nondegenerate two-ratio Fisher configuration of `VIS-049` together with the exact one-coordinate finite-gauge reduction of `VIS-050`. Thus `0<|kappa|<1`, the active cells split into reciprocal ratio classes `P,M`, and along a fixed real log-gauge direction `h`

`G_x(s)=H_x exp(-s h_x)/Z(s)`

one has

`kappa_h(s)=F(q_h(s))`,

where

`F(q)=kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)`

and

`q_h(s)=log E_(pi_P)[exp(s h)]-log E_(pi_M)[exp(s h)]`.

Let

`a_1<a_2<...<a_K`

be the distinct values taken by `h` on the active support, and define the two classwise value distributions

`alpha_j = pi_P{h=a_j}`,
`beta_j  = pi_M{h=a_j}`,
`c_j     = alpha_j-beta_j`.

Delete zero entries from the ordered coefficient sequence `(c_1,...,c_K)` and let `V(c)` be its number of sign changes. Since both class laws are probabilities,

`sum_j c_j=0`.

If the two weighted `h`-distributions are not identical, then the exact balance-return set of the Fisher angle is finite and obeys the following global bound.

1. Define

   `D_h(s)=E_(pi_P)[exp(s h)]-E_(pi_M)[exp(s h)]`
   `      =sum_j c_j exp(a_j s)`.

   Then

   `kappa_h(s)=kappa  <=>  q_h(s)=0  <=>  D_h(s)=0`.

2. The total number of real zeros of `D_h`, counted with multiplicity, is at most `V(c)`. Equivalently, the Fisher angle can return exactly to its baseline value at at most `V(c)` real gauge parameters when multiplicity is counted on the underlying balance equation.

3. Let

   `r=min{j>=1 : Delta_j != 0}`

   be the first unmatched class cumulant from `VIS-051`. The compulsory baseline balance point `s=0` has multiplicity exactly `r` as a zero of `D_h`. Hence

   `r <= V(c)`

   and the total multiplicity of all **nonzero** exact balance returns is at most

   `V(c)-r`.

   In particular, if `V(c)=r`, then `s=0` is the unique exact balance return on the entire real gauge path. The special case `V(c)=1` therefore forces `r=1` and gives global uniqueness immediately.

4. If `s_0` is a balance point of multiplicity `m` for `D_h`, then the Fisher-angle defect

   `kappa_h(s)-kappa`

   has a zero of multiplicity exactly `2m` at `s_0`. Exact returns are therefore tangential in the angle statistic: the normalized cosine does not cross its baseline value transversely on this nondegenerate two-ratio locus.

If every `c_j` vanishes, the two finite weighted `h`-distributions are identical and `VIS-051` already gives the complementary case `kappa_h(s)=kappa` for every real `s`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GENERALIZED-DESCARTES + REPRESENTATION CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that empirical zeta/CUE residuals satisfy the exact two-ratio hypothesis, that the generalized Descartes rule is new, or that a small sign budget carries arithmetic information.

## 1. Exact angle returns are zeros of one exponential polynomial

Write the class moment-generating functions as

`M_P(s)=sum_j alpha_j exp(a_j s)`,
`M_M(s)=sum_j beta_j exp(a_j s)`.

Both are strictly positive for every real `s`. The exact coordinate from `VIS-050` is

`q_h(s)=log[M_P(s)/M_M(s)]`.

Therefore

`q_h(s)=0 <=> M_P(s)=M_M(s) <=> D_h(s)=0`.

`VIS-050` independently proves, for `0<|kappa|<1`, that

`F(q)=kappa <=> q=0`.

Combining the two statements shows that no additional angle-return mechanism is hidden by the nonlinear Fisher normalization: every exact return is exactly a balance of the two classwise exponential moments.

This also gives the useful identity

`D_h(s)=M_M(s)[exp(q_h(s))-1]`.

Because `M_M(s)>0`, `D_h` and `q_h` have the same zero set and the same multiplicity at every balance point.

## 2. Generalized Descartes bounds the full real return set

Set

`x=exp(s)>0`.

Then

`D_h(log x)=sum_j c_j x^(a_j)`.

This is a generalized real polynomial with strictly ordered real exponents. Multiplying by the positive monomial `x^(-a_1)` changes neither its positive zeros nor their multiplicities and leaves the ordered coefficient signs unchanged.

The classical generalized Descartes rule of signs states that a nonzero generalized polynomial

`g(x)=sum_(j=1)^K d_j x^(lambda_j)`,

with real `lambda_1<...<lambda_K`, has at most as many positive zeros, counted with multiplicity, as there are sign changes in its nonzero ordered coefficient sequence. Applying that rule to the `c_j` gives at most `V(c)` positive roots in `x`, hence at most `V(c)` real roots in `s` because `x=exp(s)` is a smooth bijection with nonzero derivative.

For completeness, the reason the real-exponent extension works is the same Rolle induction behind the ordinary rule. After removing a lowest monomial, differentiating lowers the number of terms by one after a positive monomial rescaling; Rolle's theorem transfers any excess positive-root multiplicity to the derivative, while the coefficient-sign bookkeeping loses at most the initial sign variation. Iterating gives the sign-variation bound without requiring integer exponents.

Thus the apparent possibility of repeatedly leaving and re-entering the same Fisher angle along one declared gauge direction is not unconstrained. It is controlled by the ordered signed difference of the two classwise `h`-value laws.

## 3. Local cumulant flatness consumes the global zero budget

At `s=0`, both class MGFs equal one, so `D_h(0)=0`. `VIS-051` writes

`q_h(s)=Delta_r s^r/r!+O(s^(r+1))`

when `Delta_r` is the first nonzero class-cumulant difference. Using

`D_h(s)=M_M(s)[exp(q_h(s))-1]`

and `M_M(0)=1` gives

`D_h(s)=Delta_r s^r/r!+O(s^(r+1))`.

Hence the baseline root has multiplicity exactly `r`. The generalized Descartes bound immediately yields

`r<=V(c)`.

More importantly, every other real balance point must fit in the remaining multiplicity budget `V(c)-r`. High-order flatness at the baseline is therefore not merely a local representation effect: it uses up part of the finite global budget for exact re-alignment along that same gauge direction.

This sharpens the interpretation of `VIS-051`. Matching the first several class cumulants can make local finite-difference tests look extremely flat, but it does not create an unlimited family of remote angle-preserving gauges. If the first mismatch order already equals the sign-variation count, no remote exact recovery exists at all.

## 4. Every exact angle return has doubled contact order

Let `s_0` be any zero of `D_h` of multiplicity `m`. By the identity above, `q_h` has the same multiplicity, so for some nonzero `A`,

`q_h(s)=A(s-s_0)^m+O((s-s_0)^(m+1))`.

The exact outer Fisher map from `VIS-050` has the expansion at every balance point `q=0`

`F(q)-kappa=[kappa(1-kappa^2)/8]q^2+O(q^4)`.

The coefficient is nonzero under `0<|kappa|<1`. Therefore

`kappa_h(s)-kappa`

vanishes to order exactly `2m` at `s_0`.

The baseline case `m=r` recovers the `2r` hierarchy in `VIS-051`. The new point is global: **all** exact balance returns along the path have even contact order in the Fisher angle. A plot of the angle can therefore show several apparently flat touches without any sign crossing, but the number and total multiplicity of those touches are still bounded by the class-distribution sign budget.

## 5. Prior art and novelty boundary

Descartes' rule and its extension to generalized polynomials with real exponents are classical. A direct modern exposition is G. J. O. Jameson, **Counting zeros of generalised polynomials: Descartes' rule of signs and Laguerre's extensions**, *The Mathematical Gazette* 90:518 (July 2006), 223–234, DOI `10.1017/S0025557200179628`. The article develops the Rolle-theoretic zero-counting form used here. Broader fewnomial and Chebyshev-system theory contains much stronger general zero-counting machinery than this one-dimensional application requires.

The moment/cumulant part is likewise classical and was already bounded in `VIS-051`. No novelty is claimed for exponential-polynomial zero counting, moment-generating functions, or Descartes' rule.

The durable Mathia contribution is the representation-control composition with the exact Fisher reduction of `VIS-050` and the cumulant hierarchy of `VIS-051`: **the same two class distributions determine both the local flatness order and a finite global budget for exact angle returns.** This prevents visually repeated gauge-robustness pockets from being counted as independent structure before their classwise mass-difference geometry is audited.

## 6. Boundary conditions and falsification

The finite active support, fixed residual tensors, baseline gauge, reciprocal ratio classes, class weights, and one fixed real perturbation field `h` must remain unchanged along the path. Rebinning cells, changing support, refitting residual tensors, recomputing a closure, changing `h`, or changing the statistic between gauge values is outside the claim.

The coefficient sequence is formed after aggregating **all** cells sharing the same `h` value and then deleting zero coefficients before counting sign changes. Counting cellwise signs without this aggregation can overstate the true generalized-polynomial complexity and is not the theorem above.

The nondegenerate condition `0<|kappa|<1` is essential for the exact angle-return equivalence and doubled-contact coefficient. The globally invariant proportional/disjoint degeneracies remain governed by `VIS-048`.

The generalized Descartes bound concerns exact zeros. Near-returns under sampling noise or approximate two-ratio structure require quantitative stability analysis and cannot be counted by thresholding a rendered curve and invoking this theorem unchanged.

Falsify the claim by producing a valid `VIS-050` configuration and fixed `h` for which the nonzero exponential polynomial `D_h` has more real zeros, counting multiplicity, than `V(c)`; by showing that the multiplicity at `s=0` differs from the first unmatched cumulant order of `VIS-051`; by finding an exact Fisher-angle return with `D_h != 0`; or by finding a balance point whose Fisher-angle defect has contact order other than twice the balance multiplicity.

## Research consequence

For a frozen empirical residual comparison that is close enough to the exact two-ratio model to justify this geometry, the next useful diagnostic is not another visually chosen gauge sweep. First aggregate the declared log-gauge field into its two classwise value distributions and inspect the signed mass-difference sequence `c_j` in increasing `h` order.

That sequence gives two exact representation controls before any arithmetic interpretation: its cumulants determine how long the baseline can look locally flat, while its sign variations bound how many exact baseline returns can occur globally. In the particularly clean case `V(c)=r`, a locally `2r`-flat Fisher angle is guaranteed never to recover its baseline at any other finite gauge parameter.

Whether a real zeta/CUE residual table lies near this exceptional geometry, and how the exact zero budget deforms under sampling error or approximate ratio classes, is a separate empirical question. It should be tested on frozen data and predeclared gauge families rather than inferred from a visually smooth angle curve.