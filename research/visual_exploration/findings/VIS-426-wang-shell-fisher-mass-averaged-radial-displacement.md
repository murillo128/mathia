# VIS-426 — Wang shell Fisher mass gives an averaged radial representative-displacement tariff

## Claim

Continue the power-filtered GAF notation of `VIS-425`:

`P_N(w)=sum_(j=0)^N c_j xi_j w^j`,

`Y_N(r)=sum_(j=0)^N c_j^2 r^(2j)`,

and let

`p_j(r)=c_j^2 r^(2j)/Y_N(r)`

be the normalized radial coefficient law. Define the unit feature vector

`u_r(j)=c_j r^j/sqrt(Y_N(r))`.

Then `||u_r||_2=1` and the exact radial speed is

`||u_r'||_2^2 = Var_r(J)/r^2 = Upsilon_N(r)/4`,

where `Upsilon_N(r)=4 Var_r(J)/r^2` is the Fisher/covariance density from `VIS-425`.

Consequently, for every `a<=r<r+h<=b`,

`||u_(r+h)-u_r||_2^2 <= (h/4) integral_r^(r+h) Upsilon_N(v) dv`.

If

`M_[a,b]=integral_a^b Upsilon_N(v) dv`,

then averaging over all radial starts for which the step remains in the shell gives

`1/(b-a-h) integral_a^(b-h) ||u_(r+h)-u_r||_2^2 dr`

`<= h^2 M_[a,b]/[4(b-a-h)]`.

Equivalently, for the normalized radial covariance

`C_N(r,t)=<u_r,u_t>`,

one has

`1/(b-a-h) integral_a^(b-h) [1-C_N(r,r+h)] dr`

`<= h^2 M_[a,b]/[8(b-a-h)]`.

Thus an `L^1` shell bound on Fisher mass does not merely control an integrated derivative statistic: it gives an exact **average radial representative-displacement tariff**. It also gives the exceptional-set estimate

`|{r in [a,b-h]: ||u_(r+h)-u_r||_2 > epsilon}|/(b-a-h)`

`<= h^2 M_[a,b]/[4 epsilon^2 (b-a-h)]`.

For a Wang shell `I_s=[a_s,b_s]` of width `Delta_s=b_s-a_s=2^(-s)`, `VIS-425` gives

`M_s <= 2 F_beta(s)/(1-2^(-(s-1)))`.

Writing `h=eta Delta_s`, `0<eta<1`, therefore yields

`1/(Delta_s-h) integral_(a_s)^(b_s-h) ||u_(r+h)-u_r||_2^2 dr`

`<= eta^2 Delta_s F_beta(s)/[2(1-eta)(1-2^(-(s-1)))]`.

Hence whenever the Wang source bound has `F_beta(s)<=C_beta/Delta_s`, the mean squared radial displacement at a fixed relative sub-shell step `eta` is `O_beta(eta^2)` uniformly in the shell index and truncation order. In particular, for `eta=o(1)`, the representative is radially continuous **in shell average / outside a quantitatively small exceptional set**, even though `VIS-425` does not supply a useful uniform pointwise bound for every radius.

**Evidence/status:** `EXACT-DERIVED + TRANSFERRED-FROM-SOURCE-BOUND + REPRESENTATION/GEOMETRY + OBSTRUCTION + NO-NOVELTY-CLAIM`.

No zero-persistence estimate, pair-correlation improvement, uniform-in-radius modulus, new GAF theorem, or RH consequence is claimed.

## 1. Exact feature-speed identity

Differentiate the normalized coefficient vector. Since

`Y_N'(r)/Y_N(r)=2 E_r[J]/r`,

one obtains componentwise

`u_r'(j)=u_r(j)[j-E_r[J]]/r`.

Taking the squared Hilbert norm gives

`||u_r'||_2^2`
`= sum_j p_j(r)[j-E_r[J]]^2/r^2`
`= Var_r(J)/r^2`
`= Upsilon_N(r)/4`.

This is an intrinsic identity for the normalized radial representative; no probabilistic approximation or asymptotic passage is used.

For `t=r+h`, the fundamental theorem of calculus and Cauchy-Schwarz give

`||u_t-u_r||_2`
`<= integral_r^t ||u_v'||_2 dv`,

so

`||u_t-u_r||_2^2`
`<= (t-r) integral_r^t ||u_v'||_2^2 dv`
`= h/4 integral_r^(r+h) Upsilon_N(v) dv`.

## 2. Averaging spends Fisher mass only once

Integrate the preceding inequality over `r in [a,b-h]`. Fubini gives

`integral_a^(b-h) integral_r^(r+h) Upsilon_N(v) dv dr`

`<= h integral_a^b Upsilon_N(v) dv`
`= h M_[a,b]`,

because each `v` belongs to an interval `[r,r+h]` for a set of starts of length at most `h`. Therefore

`integral_a^(b-h) ||u_(r+h)-u_r||_2^2 dr`

`<= h^2 M_[a,b]/4`.

The loss relative to a pointwise estimate is explicit: dividing by the available start length `b-a-h` converts the shell `L^1` Fisher budget into an average displacement bound, not a supremum bound.

Since `u_r` and `u_t` are unit vectors with nonnegative real coordinates,

`||u_t-u_r||_2^2 = 2[1-C_N(r,t)]`,

which yields the covariance-deficit form in the claim. Markov's inequality applied to the same integral gives the exceptional-set estimate.

## 3. Wang-shell scaling

For `I_s=[a_s,b_s]`, `Delta_s=2^(-s)`, insert the exact integrated Fisher tariff from `VIS-425`:

`M_s <= 2F_beta(s)/(1-2^(-(s-1)))`.

With `h=eta Delta_s`,

`h^2 M_s/[4(Delta_s-h)]`

`<= eta^2 Delta_s F_beta(s)/[2(1-eta)(1-2^(-(s-1)))]`.

Thus the borderline source growth `F_beta(s)=O_beta(Delta_s^(-1))`, which made the shell-integrated Fisher mass `O_beta(Delta_s^(-1))`, still permits a scale-free averaged representative bound at relative displacement `eta Delta_s`:

`average ||u_(r+eta Delta_s)-u_r||_2^2 = O_beta(eta^2)`.

The same calculation shows why the stronger pointwise route remains unavailable. An `L^1` derivative budget can concentrate on a narrow radial subset. The estimate controls the average and the measure of bad starting radii, but it cannot rule out a small set carrying large local displacement.

## 4. What this changes in the persistence question

`VIS-425` showed that replacing the shell-integrated Fisher mass by the worst pointwise covariance density loses a full factor of shell width. The present identity makes the corresponding geometric consequence precise: radial representative motion at sub-shell scale can be charged directly to the integrated Fisher budget and is small on average when `h=o(Delta_s)`.

This closes one over-pessimistic interpretation of the Wang geometry, but it does **not** close the persistence problem. A persistence or small-value lemma that requires uniform control at every radius cannot use this estimate unchanged. To exploit it, the destination argument would need to tolerate an exceptional set of starting radii, average the relevant local probability/correlation quantity over radius, or prove separately that the remaining boundary strips contribute acceptably.

That distinction is the current boundary: **integrated Fisher mass is strong enough for average radial geometry, but not automatically for uniform zero persistence**.

## 5. Prior-art and evidence boundary

The feature-speed identity is an elementary Hilbert-space/Fisher calculation for the normalized monomial coefficient map. The averaging step is only the fundamental theorem of calculus, Cauchy-Schwarz, Fubini, and Markov. No novelty is claimed for these general inequalities.

The research-specific content is the exact combination with the persisted Wang-shell tariff in `VIS-425`, which converts that source bound into the stated shell-average displacement and covariance-deficit estimates. The Wang source attribution, shell notation, and `F_beta` bound are inherited only at the strength already audited there; this finding does not strengthen Wang's theorem or import an unstated persistence lemma.

The decisive next test is therefore not another maximum-geometry estimate. It is to inspect the actual persistence/localization step and determine whether its destination cost can be reformulated in an averaged or exceptional-set-tolerant form without losing the target exponent. Until that is proved, the result remains a geometric tariff and obstruction diagnostic rather than a persistence theorem.
