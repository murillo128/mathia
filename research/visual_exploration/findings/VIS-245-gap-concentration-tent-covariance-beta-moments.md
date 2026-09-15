# VIS-245 — gap concentration–tent covariance collapses to one-dimensional beta moments

## Claim

Continue the symmetric cyclic-gap null of `VIS-240`--`VIS-244`. Normalize the circumference to `1` and let

`X=(X_1,...,X_m) ~ Dirichlet(alpha,...,alpha)`, `alpha>0`.

Keep

`H=sum_i X_i^2`, `C=mH-1`

from `VIS-244`, and the complement-quotiented cut-averaged tent statistic from `VIS-243`,

`bar T = sum_(r in R_m) w_r sum_(i=0)^(m-1) q_u(S_(i,r))`,

where `R_m={1,...,floor(m/2)}`, `w_r=1` except `w_(m/2)=1/2` when `m` is even,

`S_(i,r)=sum_(a=0)^(r-1) X_(i+a)`

and, for `0<u<=1/2`,

`q_u(s)=(1-s)(1-s/u)_+ + s(1-(1-s)/u)_+`.

For a fixed arc length `r`, put

`a=r alpha`, `b=(m-r) alpha`,

`A_r=(alpha+1)/(r alpha+1)`,
`B_r=(alpha+1)/((m-r) alpha+1)`,

and

`g_r(s)=A_r s^2 + B_r(1-s)^2`.

Then

`E[H | S_(i,r)=s]=g_r(s)`.

Define the truncated beta moments

`tau_j(a,b;u)=E[Z^j 1_(Z<=u)]`
`              = (a)_j/(a+b)_j I_u(a+j,b)`, `j=0,...,4`,

for `Z~Beta(a,b)`, with `(x)_j` the rising factorial and `I_u` the regularized incomplete beta function. For two coefficients `A,B`, define

`R_u(a,b;A,B)=sum_(j=0)^4 p_j(A,B;u) tau_j(a,b;u)`

with

`p_0=B`,
`p_1=-B(3+1/u)`,
`p_2=A+3B(1+1/u)`,
`p_3=-(A+B)-(A+3B)/u`,
`p_4=(A+B)/u`.

If

`mu_r=E[q_u(Z)]`, `Z~Beta(a,b)`

is the exact single-arc mean already used in `VIS-240`--`VIS-242`, then

`nu_r=E[H q_u(S_(i,r))]`
`    = R_u(a,b;A_r,B_r)+R_u(b,a;B_r,A_r)`.

Since

`E[H]=(alpha+1)/(m alpha+1)`,

the same-configuration concentration/tent covariance is exactly

`Cov(C,bar T)`
` = m^2 sum_(r in R_m) w_r [nu_r-E[H] mu_r]`.

Therefore `VIS-242`, `VIS-244`, and the present identity give the complete exact covariance matrix of `(C,bar T)` under every fixed symmetric-Dirichlet parameter `alpha`: both marginal variances and their cross-covariance are finite explicit beta/Dirichlet expressions. The cross term is simpler than `Var(bar T)`: it requires only one-dimensional truncated beta moments through order four, not two-arc overlap classes.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DIRICHLET-NEUTRALITY + NUISANCE-COVARIANCE CALIBRATION + NO-NOVELTY-CLAIM`.

This does **not** give the full joint law of `(C,bar T)`, the conditional law of `bar T` after fitting `alpha`, an exact law for `alpha_hat(C)`, a prime residual, or an RH consequence.

## 1. Conditioning on one arc makes the quadratic concentration elementary

Fix one forward cyclic arc `A` of `r` gaps and write

`S=sum_(j in A) X_j`.

Dirichlet aggregation gives

`S~Beta(r alpha,(m-r) alpha)`.

Conditional on `S=s`, the normalized coordinates inside the arc,

`(X_j/s)_(j in A)`,

form a symmetric `r`-component Dirichlet vector with parameter `alpha`; the normalized coordinates outside the arc,

`(X_j/(1-s))_(j notin A)`,

form the corresponding `(m-r)`-component symmetric Dirichlet vector. These two subcompositions are independent of the aggregate mass in the usual Dirichlet neutrality decomposition.

For a symmetric `n`-component Dirichlet vector `Y` with parameter `alpha`,

`E[sum_j Y_j^2]=(alpha+1)/(n alpha+1)`.

Therefore

`E[H|S=s]`
` = s^2 (alpha+1)/(r alpha+1)`
`   +(1-s)^2 (alpha+1)/((m-r) alpha+1)`
` = g_r(s)`.

This is the key simplification: although `H` uses every gap, its conditional expectation given one arc mass is only a quadratic polynomial in that one beta variable.

## 2. Multiplying by the tent kernel needs only moments through degree four

For `u<=1/2`, the two support pieces of `q_u` are disjoint. On `0<=s<=u`,

`q_u(s)=(1-s)(1-s/u)`
`      =1-(1+1/u)s+s^2/u`.

Also

`g_r(s)=B_r-2B_r s+(A_r+B_r)s^2`.

Their product is the quartic polynomial

`sum_(j=0)^4 p_j(A_r,B_r;u) s^j`

with the coefficients displayed in the claim. Hence the near-zero contribution to

`E[g_r(S)q_u(S)]`

is exactly

`R_u(a,b;A_r,B_r)`.

For the near-one contribution set `t=1-s`. Then `t~Beta(b,a)` and

`g_r(1-t)=A_r-2A_r t+(A_r+B_r)t^2`.

The same quartic calculation applies with

`(a,b,A_r,B_r) -> (b,a,B_r,A_r)`,

giving

`R_u(b,a;B_r,A_r)`.

Adding the two support pieces proves the formula for `nu_r`.

Each truncated moment has the standard exact form

`tau_j(a,b;u)=(a)_j/(a+b)_j I_u(a+j,b)`,

so no multidimensional numerical integration is required for this cross-covariance.

## 3. Cyclic exchangeability gives the global covariance

The half-circle representation from `VIS-243` is

`bar T=sum_(r in R_m) w_r sum_i q_u(S_(i,r))`.

Because `H` is invariant under cyclic relabeling of the gaps,

`Cov(H,q_u(S_(i,r)))`

depends on `r` but not on the starting index `i`. There are exactly `m` starts for each `r`. Thus

`Cov(H,bar T)`
` = m sum_(r in R_m) w_r`
`   [E[Hq_u(S_(0,r))]-E[H]mu_r]`
` = m sum_(r in R_m) w_r [nu_r-E[H]mu_r]`.

Finally `C=mH-1`, so

`Cov(C,bar T)=m Cov(H,bar T)`,

which gives the displayed `m^2` formula.

Together with

`Var(C)`

from `VIS-244` and

`Var(bar T)`

from `VIS-242`--`VIS-243`, this completes the exact fixed-`alpha` second-moment block for the pair `(C,bar T)`.

## 4. What this closes and what remains open

The same-sample nuisance problem from the accepted clue had two logically distinct parts.

First, one needed to know whether the fitting statistic `C` and confirmation statistic `bar T` are dependent strongly enough that a fixed plug-in treatment is unjustified. The present formula answers that quantitatively: their covariance is an explicit, computable function of `(m,alpha,u)`, and it need not vanish.

Second, one needs a valid law for testing `bar T` after `alpha` has been inferred from the same realization. Exact covariance alone does not provide that law. In particular, `alpha_hat(C)` is nonlinear and the conditional distribution of `bar T` given `C` is not determined by the covariance matrix.

The exact second-moment block can support diagnostics, implementation audits, or a separately justified asymptotic approximation, but no Gaussian or linear-regression approximation is asserted here. An exact same-configuration calibration still requires either the conditional/full joint law, or an independently validated procedure that carries the fitted nuisance through the null.

## 5. Prior art and novelty boundary

The ingredients are classical properties of the Dirichlet distribution: aggregation to beta marginals, neutrality of subcompositions, and polynomial moments. `VIS-240` already anchors these facts to the standard Dirichlet/spacings literature, including Kotz, Balakrishnan, and Johnson, *Continuous Multivariate Distributions*, and Pyke's classical spacings survey. `VIS-242` records the broader prior-art boundary for exact functionals of spacings.

No novelty is claimed for conditional Dirichlet decomposition, Simpson-type concentration, incomplete-beta moments, covariance propagation, or the general idea of nuisance covariance. The Mathia-specific result is the exact specialization linking the particular concentration channel `C` from `VIS-244` to the endpoint-quotiented tent statistic `bar T` from `VIS-241`--`VIS-243`.

## Boundaries and falsification

The result assumes one symmetric Dirichlet parameter shared by all cyclic gaps, the complement-symmetric cut-averaged tent statistic, and `0<u<=1/2`. It does not apply unchanged to asymmetric Dirichlet laws, mixtures, endpoint-sensitive statistics, or stronger prime-spacing controls.

A direct algebraic falsification is to recompute `E[H|S=s]` from Dirichlet moments or expand the quartic product and obtain different coefficients. A numerical falsification is to simulate or integrate any fixed `(m,alpha,u)` and find a covariance between `C` and `bar T` inconsistent with the exact formula beyond numerical error.

As an internal audit, direct symmetric-Dirichlet simulation at representative parameter values agrees with the formula, but that computation is only a check of the derivation, not independent evidence or part of the claim.

## Research consequence

The accepted prime-phase confirmation clue no longer lacks the cross term of its same-configuration nuisance calibration. Under fixed `alpha`, the mean vector and complete covariance matrix of `(C,bar T)` are now explicit: `VIS-244` gives the concentration moments, `VIS-242`--`VIS-243` give the tent moments, and this finding gives their covariance.

The remaining same-sample gate is sharper rather than solved. A future confirmation may either freeze `alpha` from held-out/theoretical information and use the fixed-parameter tent law, or derive/validate the conditional or full joint calibration needed to pass from the observed `C` through `alpha_hat(C)` to a valid residual for `bar T`. Covariance alone must not be mistaken for that final nuisance correction.
