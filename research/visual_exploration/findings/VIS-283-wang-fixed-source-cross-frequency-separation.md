# VIS-283 — Wang's fixed-source prime/source cross is power-small by one-sided frequency separation

## Claim

Keep the compact fixed-source regime of `VIS-274`–`VIS-282`: `H=T^theta` with fixed `0<theta<1`, `L=log T`, `I=(T,T+H]`,

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

and `x=e^(2*pi*q)` with `q` in a fixed compact subset of `(0,infinity)`.

Write the combined source as

`S_x(t)=B_x(t)+E_x(t)`.

From `VIS-278`, uniformly on compact fixed-source windows,

`x S_x(t)=ell(t)+Z(t)+epsilon_x(t)`,

where

`ell(t)=log(t/(2*pi))`,

`Z(t)=zeta'/zeta(3/2-it)=-sum_(n>=2) Lambda(n)n^(-3/2)e^(it log n)`,

and `epsilon_x(t)=O_K(t^-1)`.

Wang's Dirichlet piece is

`D_x(t)=sum_(m>=2) a_m(x)e^(-it log m)`,

`a_m(x)=Lambda(m)/sqrt(m) min(m/x,x/m)`.

Then, uniformly for `x` in every fixed compact `K subset (1,infinity)`,

`integral_I D_x(t) overline(E_x(t)) dt = O_K(1)`,

and

`integral_I D_x(t) overline(S_x(t)) dt = O_K(L)`.

The sharper `D_x`–`E_x` estimate comes from a structural frequency separation. After complex conjugation, the absolutely convergent Dirichlet series `Z` has the same negative temporal frequency orientation as `D_x`, so their product contains frequencies `-log(mn)` rather than differences `log(n/m)`. Since `m,n>=2`, no zero-frequency diagonal exists.

Consequently the entire signed prime/source cross

`-2 Re integral_I D_x(t) overline(S_x(t)) dt`

is power-small after the fixed-`q` pullback and pair-statistic normalization: it contributes

`O_K(1/(H L))`,

hence `o(L^-r)` for every fixed `r>0`.

In particular, the `L^-2` scale isolated in `VIS-278` and `VIS-282` does **not** rely on a cancellation between the exact Dirichlet diagonal profile and the combined source. At fixed source, the cross sector is already negligible. The two surviving coefficient-scale energies are diagonal contributions.

More precisely, combining `VIS-278`, `VIS-282`, and the present cross estimate gives

`(1/H) integral_I |A(x,t)|^2 dt`
` = S_D(x) + x^-2 [log(T/(2*pi))^2 + C_Lambda] + o_K(1)`,

where

`S_D(x)=sum_(m>=2) a_m(x)^2`

and

`C_Lambda=sum_(n>=2) Lambda(n)^2/n^3`.

Thus, if the classical gamma baseline `x^-2 log(T/(2*pi))^2` is kept intact, the constant-order fixed-source field-energy remainder is the positive diagonal profile

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

Under the fixed-`q` packet normalization this is the corresponding `L^-2` profile, up to the already fixed test-function and normalization factors. No cross-term cancellation is needed to produce it.

**Evidence/status:** `LITERATURE+DERIVED + EXACT REGIME SPECIALIZATION + FOURIER/NONRESONANCE CONTROL + BOTTLENECK RESOLUTION + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, new mean-value theorem, uniform statement for growing source, new prime-power invariant, or RH implication is claimed.

## 1. Fixed-source coefficients are absolutely summable

For `x` in a compact `K=[x_0,x_1] subset (1,infinity)`, the coefficients of `D_x` satisfy a uniform `ell^1` bound.

For `m<=x`, only finitely many `m<=x_1` occur. For `m>x`,

`a_m(x)=x Lambda(m)m^(-3/2)`,

so

`sum_(m>x) |a_m(x)| <= x_1 sum_(m>=2) Lambda(m)m^(-3/2) < infinity`.

Hence

`sup_(x in K) sum_m |a_m(x)| < infinity`.

The same argument gives

`sup_(x in K) sum_m |a_m(x)|/log m < infinity`.

Likewise the coefficients

`b_n=Lambda(n)n^(-3/2)`

of `-Z(t)` are absolutely summable. These elementary compact-source facts justify all termwise integrations below and provide summable majorants independent of `T`.

## 2. The residual Dirichlet cross has no diagonal

Using the absolutely convergent series,

`overline(Z(t))=-sum_(n>=2) b_n e^(-it log n)`.

Therefore

`D_x(t) overline(Z(t))`
` = -sum_(m,n>=2) a_m(x)b_n e^(-it log(mn))`.

For every `m,n>=2`,

`|integral_T^(T+H) e^(-it log(mn)) dt| <= 2/log(mn) <= 2/log 4`.

Absolute summability of the coefficient product gives

`integral_I D_x(t) overline(Z(t)) dt = O_K(1)`.

This is the decisive structural point. The ordinary mean square `|D_x|^2` contains frequency differences `log(n/m)` and therefore a true diagonal at `m=n`, producing the `H S_D(x)` term of `VIS-282`. The cross with `Z`, by contrast, contains frequency sums `log(mn)`. Its frequency support is bounded away from zero, so there is no `H`-sized diagonal to cancel against either `S_D` or `C_Lambda`.

This is ordinary Fourier/Dirichlet-series nonresonance, not a new orthogonality theorem.

## 3. The signed D–E cross is actually `O_K(1)`

Wang defines

`B_x(t)=log(t+2)/x`.

The reconstruction in `VIS-278` therefore gives

`x E_x(t)`
` = ell(t)-log(t+2)+Z(t)+epsilon_x(t)`.

Now

`ell(t)-log(t+2)`
` = -log(2*pi)+log(t/(t+2))`
` = -log(2*pi)+O(t^-1)`.

The constant part contributes only `O_K(1)` against `D_x`, because

`integral_I D_x(t) dt`
` = sum_(m>=2) a_m(x) integral_I e^(-it log m) dt`
` = O_K(sum_m |a_m(x)|/log m)`
` = O_K(1)`.

The `Z` part is `O_K(1)` by the previous section. Finally, since `D_x` is uniformly bounded by its `ell^1` coefficient norm,

`integral_I |D_x(t) epsilon_x(t)| dt`
` = O_K(H/T)`
` = o_K(1)`.

Thus

`integral_I D_x(t) overline(E_x(t)) dt = O_K(1)`.

This strictly sharpens the `O_K(H)` Cauchy–Schwarz envelope used in `VIS-279`. That earlier finding was sufficient to remove the apparent `L^-3/2` floor; the present signed reconstruction shows that even its residual `L^-2` envelope is not active in the fixed-source regime.

## 4. The combined prime/source cross is dominated by the slowly varying gamma baseline

For the full source `S_x=B_x+E_x`, the residual `Z` and reconstruction-error pieces contribute only `O_K(1)` as above. It remains to pair `D_x` with

`ell(t)/x = log(t/(2*pi))/x`.

Termwise integration by parts gives, for every `m>=2`,

`integral_I ell(t)e^(-it log m) dt`
` = O(L/log m) + O(H/(T log m))`.

Summing against `a_m(x)` yields

`integral_I D_x(t) ell(t) dt = O_K(L)`.

Hence

`integral_I D_x(t) overline(S_x(t)) dt = O_K(L)`.

This agrees with Wang's direct `D_x`–`B_x` estimate recorded in `VIS-280`, but now the whole combined source has been reconstructed. The only reason the full cross is `O(L)` rather than `O(1)` is the slowly varying classical gamma baseline; the arithmetic residual itself has no stationary frequency channel with `D_x`.

## 5. Fixed-source energy separates into diagonal sectors through constant order

Expand

`|A|^2=|D_x|^2+|S_x|^2-2 Re(D_x overline(S_x))`.

`VIS-282` gives

`integral_I |D_x|^2 dt = H S_D(x)+O_K(1)`.

`VIS-278` gives

`integral_I |S_x|^2 dt`
` = H x^-2 [log(T/(2*pi))^2+C_Lambda+o_K(1)]`.

The present finding gives

`integral_I D_x overline(S_x) dt = O_K(L)=o(H)`.

Therefore

`(1/H) integral_I |A|^2 dt`
` = S_D(x)+x^-2[log(T/(2*pi))^2+C_Lambda]+o_K(1)`.

This is the requested recombination at the signed-cross level. It does not produce a cancellation. Instead it reveals that, in this fixed-source representation, the first coefficient-scale arithmetic correction is a direct sum of two diagonal energies separated by temporal-frequency orientation.

If one expands relative to `L=log T` rather than retaining the exact gamma baseline, writing `c=log(2*pi)` gives

`x^-2 log(T/(2*pi))^2`
` = x^-2 L^2 - 2c x^-2 L + c^2 x^-2`.

Accordingly the constant-order field-energy profile becomes

`S_D(x)+(c^2+C_Lambda)/x^2`.

The `c^2` piece is purely classical normalization. The normalization-invariant arithmetic remainder after keeping the gamma baseline intact is `Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

The prime-power derivative kinks of `S_D` from `VIS-282` therefore survive this recombination; there is no equal-scale signed cross available to erase them. Whether a later packet integration projects some of that profile away for a particular test function is a different question.

## 6. Fixed-`q` consequence

The fixed-source change of variables contributes `d alpha=(2*pi/L)dq`, and the normalized pair statistic contributes the usual factor proportional to `1/(H L)`.

The full cross `O_K(L)` therefore contributes

`O_K(L) * O(L^-1) * O((H L)^-1) = O_K(1/(H L))`,

which is smaller than every fixed inverse power of `L`.

By contrast, each `H`-sized constant-order diagonal energy contributes at order `L^-2`. Thus the profile `Q_gamma(e^(2*pi*q))` is present at the coefficient scale before packet projection, while the prime/source cross is not.

`VIS-281` already shows that the `A_I -> A` zero-window localization error is also power-small. Combining that fact with the present result means that neither localization nor signed prime/source interference is needed to understand the fixed-source field energy through `L^-2`; the remaining coefficient-scale information is diagonal.

This statement remains local to fixed compact `q`. If `x=x(T)` grows, absolute coefficient bounds, Wang's global uniform errors, and the available frequency margins must be re-audited.

## 7. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), especially equations (2.7)–(2.9), Lemma 2.5, Proposition 2.6, and the mean-value/cross-term estimates in its proof. Wang supplies the decomposition and the coefficient sequence used here.

The combined-source reconstruction comes from the same Landau explicit-formula route already audited in `VIS-277`–`VIS-278`, ultimately through Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh, **An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function**, *Acta Arithmetica* 214 (2024), together with the classical zeta functional equation.

Absolute convergence of the Dirichlet series on `Re(s)=3/2`, termwise integration, and the absence of a zero frequency when exponentials with frequencies `log m` and `log n` combine as `log(mn)` are classical elementary Fourier/Dirichlet-series facts. No novelty is claimed for that mechanism.

The durable Mathia result is the regime-specific audit: the `O_K(H)` D–E envelope in `VIS-279` can be sharpened to `O_K(1)` after the signed source reconstruction is used, and the complete fixed-source prime/source cross is power-small after packet normalization. This resolves the explicit open recombination question left by `VIS-282` without inventing a new analytic-number-theory theorem.

No untouched confirmation-zero data or numerical fitting are used.

## Dependencies

- `VIS-274`: fixed physical-source coordinate and packet normalization.
- `VIS-277`–`VIS-278`: signed and normalization-invariant reconstruction of the combined source.
- `VIS-279`: earlier Cauchy–Schwarz localization of the D–E cross to at most `L^-2`.
- `VIS-280`: direct D–B cross is power-small.
- `VIS-281`: zero-window localization is power-small.
- `VIS-282`: exact fixed-source Dirichlet diagonal profile `S_D(x)`.

## Research consequence

The signed-cross recombination question left by `VIS-282` is resolved: at fixed source the Dirichlet and combined-source sectors do not cancel at `L^-2`; their cross is power-small because the arithmetic residual has the wrong temporal-frequency orientation for a diagonal resonance.

After the exact gamma baseline is retained, the coefficient-scale field-energy profile is therefore the positive diagonal sum

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

A subsequent invocation should treat any further simplification, packet projection, or relation of `Q_gamma` to an existing arithmetic transform as a new thread rather than extending the present one.