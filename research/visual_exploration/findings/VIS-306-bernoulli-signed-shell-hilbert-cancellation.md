# VIS-306 — Bernoulli thinning collapses the signed shell Hilbert remainder to `O_p(x)`

## Claim

The parity- and density-matched Bernoulli control of `VIS-305` reproduces the `x log log x` **absolute local-spacing norm**, but its corresponding **signed Dirichlet-polynomial mean-square remainder is typically only `O(x)`** on the central Wang shell.

Fix large `x`, let

`O_x={n odd : x<=n<=2x}`,
`p=2/log x`,

and let `xi_n`, `n in O_x`, be independent `Bernoulli(p)` variables. Give every occupied site the Wang-scale shell weight

`b_n=(log x)/sqrt(n) min(n/x,x/n)`.

For an interval `I=(T,T+H]`, define

`P_x(t)=sum_(n in O_x) xi_n b_n n^(-it)`

and its signed off-diagonal mean-square remainder

`R_I = integral_T^(T+H) |P_x(t)|^2 dt - H sum_(n in O_x) xi_n b_n^2`.

Uniformly in real `T` and `H>0`,

`|E R_I| << x`,

and

`Var(R_I) << x log^3 x`.

Consequently

`R_I=O_p(x)`.

In particular, whenever `H/x -> infinity`,

`R_I/H -> 0`

in probability. At the boundary isolated in `VIS-304`,

`H asymp x log log x`,

this matched Bernoulli control has `R_I=o_p(H)` even though `VIS-305` gives an `x log log x` absolute reciprocal-spacing scale.

**Evidence/status:** `EXACT-DERIVED + MATCHED RANDOM CONTROL + SIGNED-CANCELLATION NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not a statement about the actual prime-power support and does not prove cancellation for Wang's true endpoint Hilbert form. It shows that the `log log x` absolute-spacing cost and an `H`-scale **signed** remainder are genuinely different questions even inside the same density/parity control family.

## 1. The signed remainder is a Bernoulli quadratic form

Put

`u_nm=log(n/m)`.

Pairing the `(n,m)` and `(m,n)` terms gives the exact real expansion

`R_I=sum_(n<m; n,m in O_x) c_nm xi_n xi_m`,

where

`c_nm = 4 b_n b_m sin(H u_nm/2) cos((T+H/2)u_nm)/u_nm`.

Hence

`|c_nm| <= 4 b_n b_m/|u_nm|`.

On the shell `[x,2x]`,

`b_n b_m << log^2 x/x`,

while the mean-value theorem for `log` gives

`|u_nm| asymp |n-m|/x`.

Therefore

`|c_nm| << log^2 x/|n-m|`.

This estimate is deliberately phase-blind. The only cancellation used below is the signed structure already present in the exact endpoint kernel together with independent Bernoulli thinning.

## 2. The ensemble mean is only `O(x)`

Because the diagonal has already been removed,

`E[xi_n xi_m]=p^2`

for every `n!=m`. Thus

`E R_I = p^2 R_I^(full)`,

where `R_I^(full)` is the same off-diagonal remainder for the deterministic polynomial supported on **all** odd sites in `O_x` with weights `b_n`.

Apply the classical Montgomery--Vaughan weighted Hilbert inequality to the frequencies

`lambda_n=log n`.

For the odd lattice inside `[x,2x]`, the nearest logarithmic spacing satisfies

`delta_n asymp 1/x`.

Also

`sum_(n in O_x) b_n^2 << log^2 x`.

Therefore

`|R_I^(full)|`
` << sum_(n in O_x) b_n^2/delta_n`
` << x log^2 x`.

Since `p=2/log x`,

`|E R_I| << p^2 x log^2 x << x`.

The `log log x` factor from the sparse nearest-neighbor absolute norm of `VIS-305` is absent already at the ensemble-mean level.

## 3. A direct second-moment bound

For distinct unordered pairs `e={n,m}`, write `Y_e=xi_n xi_m`. If two edges are vertex-disjoint, their Bernoulli products are independent. For one edge,

`Var(Y_e)<=p^2`,

and for two distinct edges sharing one vertex,

`|Cov(Y_e,Y_f)|=p^3(1-p)<=p^3`.

Hence

`Var(R_I)`
` << p^2 sum_(n<m) c_nm^2`
`    + p^3 sum_n (sum_(m!=n) |c_nm|)^2`.

The shell kernel estimate from Section 1 gives, for each fixed `n`,

`sum_(m!=n) c_nm^2 << log^4 x sum_(h>=1) h^(-2) << log^4 x`,

so

`sum_(n<m) c_nm^2 << x log^4 x`.

Likewise

`sum_(m!=n) |c_nm| << log^2 x sum_(h<=x) 1/h << log^3 x`,

and therefore

`sum_n (sum_(m!=n)|c_nm|)^2 << x log^6 x`.

Substituting `p=2/log x` yields

`Var(R_I) << x log^2 x + x log^3 x << x log^3 x`.

Chebyshev then gives, for any fixed sufficiently large constant `A`,

`P(|R_I|>A x) << log^3 x/x -> 0`,

after absorbing the `O(x)` mean. Thus `R_I=O_p(x)` uniformly in the endpoint parameters.

More generally,

`P(|R_I-E R_I|>epsilon H) << x log^3 x/H^2`.

If `H/x->infinity`, both the mean term `O(x/H)` and this variance ratio vanish, proving `R_I/H->0` in probability.

## 4. What the control now says

`VIS-305` showed that the absolute weighted spacing majorant

`sum b_n^2/delta_n`

has expected order `x log log x` after matching prime density and parity. The present calculation shows that this does **not** propagate to the signed endpoint remainder in the same probabilistic control: at `H asymp x log log x`, the signed contribution is smaller by at least a `log log x` factor in probability.

So a matched obstruction at the Wang boundary cannot come merely from ordinary sparse occupancy plus its short-gap harmonic tail. To produce an `H`-scale signed remainder one needs additional coherence: for example arithmetic correlations of the actual prime-power support, phase alignment between those correlations and the endpoint kernel, or a different admissible control deliberately preserving such coherence.

Conversely, this finding is not evidence that the primes enjoy the Bernoulli cancellation. Prime-pair singular series, prime-power structure, and deterministic logarithmic phases are precisely the information discarded by the control.

## Prior art and novelty boundary

The weighted Hilbert step is the same classical Montgomery--Vaughan machinery already used in `VIS-304`.

Concentration and limit theory for sparse Bernoulli quadratic forms are established subjects; for example Shuheng Zhou, **Sparse Hanson--Wright inequalities for subgaussian quadratic forms**, *Bernoulli* 25:3 (2019), 1603--1639, DOI `10.3150/17-BEJ978`, treats Bernoulli-sparsified quadratic forms at a much more general level. Bhaswar B. Bhattacharya, Somabha Mukherjee, and Sumit Mukherjee, **Asymptotic distribution of Bernoulli quadratic forms**, *Annals of Applied Probability* 31:4 (2021), studies sparse Bernoulli quadratic forms in another asymptotic regime.

No new general probability inequality is claimed here. The second-moment argument is elementary. The durable Mathia content is the specialization to the `VIS-305` Wang-matched shell and the resulting separation between its `x log log x` absolute-spacing norm and its `O_p(x)` signed endpoint remainder.

## Dependencies

- `VIS-304`: support-sensitive weighted-Hilbert upper bound on the true prime-power frequencies.
- `VIS-305`: parity- and density-matched Bernoulli control with `x log log x` absolute reciprocal-spacing cost.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue.

## Research consequence

The obvious density/parity Bernoulli control no longer serves as a candidate `H`-scale **signed** obstruction near `H asymp x log log x`: it cancels to `o_p(H)`.

The moving upper-source question is therefore narrower. One must test whether the actual prime-power support carries arithmetic/phase coherence absent from this control, or construct a stronger matched model that preserves the relevant coherence and can genuinely realize an `H`-scale signed endpoint form. A proof that the actual prime-power form is also `O(x)` or otherwise `o(H)` would move Wang's pointwise boundary past `H/log log x`; this finding does not supply that proof.