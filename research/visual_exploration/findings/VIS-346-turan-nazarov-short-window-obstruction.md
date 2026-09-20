# VIS-346 — Turán–Nazarov forces fixed Wang phase banks onto rapidly shrinking windows

## Claim

Let

`m(xi)=4(1+i xi)/(4+xi^2)`

be Wang's exact multiplier and let

`M(xi)=sum_j c_j exp(-i b_j xi) m(a_j xi)`

be a fixed finite translated-dilate bank with `a_j>0` and frequency-independent complex coefficients. Group equal translations and define

`S_(b,k)=sum_(j:b_j=b) c_j a_j^(-k)`.

Let `B` be the number of distinct active translations. For `B>=2`, assume those translations are distinct, hence have fixed positive minimum spacing `Delta`.

Fix an integer `r>=2`. Let `J_X subset [X,2X]` be intervals of length `ell_X>0` with `X->infinity`, and suppose

`sup_(xi in J_X) |M(xi)| = O(X^(-r))`.

If `B=1`, then necessarily

`S_(b,k)=0`, `k=1,...,r-1`.

If `B>=2` and

`X * min(ell_X,1)^(B-1) -> infinity`,

then again

`S_(b,k)=0`, `k=1,...,r-1`

for every translation fiber `b`.

More sharply, at the `k`-th induction step let `B_k` be the number of nonzero coefficients among `{S_(b,k)}`. If the lower moments have already vanished and `B_k>=2`, then a nonzero `k`-th moment vector can coexist with the stated `O(X^-r)` window bound only if

`X * min(ell_X,1)^(B_k-1) = O(1)`.

For `B_k=1`, a nonzero moment is impossible on any nonempty interval once `X` is large.

Thus a fixed translated Wang bank cannot evade the fiberwise moment obstruction of `VIS-344` merely by moving to short windows unless those windows shrink at least at the Turán–Nazarov scale allowed by the number of active phase fibers. In the coarse `B`-fiber form, a power-law window `ell_X=X^-alpha` is excluded whenever

`alpha < 1/(B-1)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL TURAN-NAZAROV PROPAGATION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The claim is a fixed-bank obstruction. It does not exclude windows at or below the displayed shrinking scale, banks whose translation count or spacing changes with `X`, scale-dependent or ill-conditioned coefficients, frequency-dependent/adaptive coefficients, or signed source estimates that do not require multiplier smallness throughout a window.

## 1. Wang's tail reduces each order to one exponential polynomial

`VIS-343` gives the large-frequency expansion

`m(z)=sum_(ell=1)^K beta_ell z^(-ell)+O(|z|^(-K-1))`,

with every `beta_ell != 0`. Hence, for the translated bank,

`M(xi)=sum_(ell=1)^K beta_ell xi^(-ell) P_ell(xi)+O(|xi|^(-K-1))`,

where

`P_ell(xi)=sum_b S_(b,ell) exp(-i b xi)`.

Assume inductively that all fiber moments below order `k` vanish. On `J_X subset [X,2X]`, for `k<r`,

`P_k(xi)=beta_k^(-1) xi^k M(xi)+O(X^-1)`,

so

`sup_(J_X)|P_k| = O(X^(k-r)+X^-1) = O(X^-1)`.

The question is therefore whether a fixed nonzero exponential polynomial can be `O(X^-1)` on a window whose length may shrink with `X`.

## 2. A fixed reference interval gives a coefficient-scale lower bound

For `B_k>=2`, let `Delta_k` be the minimum spacing among the active frequencies in `P_k`. Because the bank is fixed, `Delta_k>0`.

Choose a fixed length `L_k` satisfying

`L_k Delta_k >= 4(B_k-1)`.

For every sufficiently large `X`, place an interval `I_X` of length `L_k` containing a subinterval of `J_X` of length

`e_X=min(ell_X,L_k)`.

The finite exponential-sum calculation already used in `VIS-345` gives, independently of the location of `I_X`,

`RMS_(I_X)(P_k) >= (1/sqrt(2)) (sum_b |S_(b,k)|^2)^(1/2)`.

Therefore

`sup_(I_X)|P_k| >= (1/sqrt(2)) ||S_k||_2`.

This lower bound uses only the fixed coefficient vector and the fixed phase separation. The smallness interval itself need not resolve the phase spacing.

## 3. Turán–Nazarov propagates smallness from the short window

For an exponential polynomial with `B_k` terms and purely imaginary exponents, the classical measurable Turán–Nazarov inequality gives an absolute constant `A` such that for every measurable `E subset I`,

`sup_I |P| <= (A |I|/|E|)^(B_k-1) sup_E |P|`.

There is no exponential real-part factor here because the exponents are `-i b`.

Apply this to `P_k`, the fixed reference interval `I_X`, and a subinterval `E_X subset J_X cap I_X` of length `e_X`. Combining with the previous lower bound gives

`sup_(J_X)|P_k|`
` >= sup_(E_X)|P_k|`
` >= (1/sqrt(2)) (e_X/(A L_k))^(B_k-1) ||S_k||_2`.

If `S_k` is nonzero, all factors except `e_X` are fixed positive constants. But the Wang-window hypothesis gave

`sup_(J_X)|P_k|=O(X^-1)`.

Hence a nonzero `k`-th moment vector requires

`X e_X^(B_k-1)=O(1)`.

When `B_k=1`, `P_k` is a single phase of constant modulus `|S_(b,k)|`, so the same conclusion is stronger: nonzero `S_(b,k)` is incompatible with `O(X^-1)` on any nonempty window.

If `ell_X` stays bounded below, `e_X` is bounded below and the contradiction is immediate. If `ell_X->0`, then eventually `e_X=ell_X`. Since `B_k<=B`, the coarse condition

`X min(ell_X,1)^(B-1)->infinity`

forces `X e_X^(B_k-1)->infinity` as well. Therefore `S_(b,k)=0` for every fiber.

Induction over `k=1,...,r-1` proves the claim.

## 4. The remaining fixed-bank escape is quantitatively microscopic

`VIS-345` required the actual smallness window to be long enough to resolve the translation gaps. The present argument removes that requirement by using a fixed phase-resolving reference interval only to certify that the exponential polynomial is not globally tiny, then propagating that information into the short window with Turán–Nazarov.

For a fixed bank with `B>=2`, a power-law window

`ell_X=X^-alpha`

can therefore escape this obstruction only at the coarse level

`alpha >= 1/(B-1)`.

This threshold is a necessary escape condition from the present argument, not a construction of such cancellation and not a sharp sufficiency theorem. At the induction level, the relevant exponent is the number `B_k` of fibers that actually survive in the `k`-th moment polynomial.

Once the moments through order `r-1` vanish, the within-fiber Vandermonde argument of `VIS-344` applies unchanged: any active translation fiber producing order `r` needs at least `r` distinct dilation scales. Thus moving to ordinary fixed-width, mesoscopic, or only mildly shrinking windows does not create a new asymptotic smoothing resource for a fixed finite bank.

## Prior-art audit

The propagation-of-smallness inequality is classical. F. L. Nazarov, **Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type**, *Algebra i Analiz* 5:4 (1993), 3–66; English translation *St. Petersburg Mathematical Journal* 5:4 (1994), 663–717, establishes local estimates of Turán type for exponential polynomials. In the purely imaginary-frequency case used here, the measurable-set inequality has the algebraic exponent `B_k-1` and no growth factor from real parts of the exponents.

Omer Friedland and Yosef Yomdin, **An observation on the Turán–Nazarov inequality**, *Studia Mathematica* 218:1 (2013), 27–39, DOI `10.4064/sm218-1-2`, treats the same classical inequality and extensions of its measurable-set size parameter. No novelty is claimed for Turán–Nazarov itself.

The Mathia-specific step is the coupling of that classical propagation theorem with the exact Wang inverse-frequency moment expansion (`VIS-343`), the translation-fiber decomposition (`VIS-344`), and the fixed-interval phase-frame lower bound (`VIS-345`). This converts an unresolved qualitative escape — "perhaps the cancellation lives only on short moving windows" — into an explicit shrinking-window obligation.

## Dependencies

- `VIS-343`: large-frequency expansion of Wang dilates and inverse-scale moment/Vandermonde structure.
- `VIS-344`: translated banks split cancellation into independent phase fibers in the uniform tail.
- `VIS-345`: fixed-length phase-resolving frame lower bound for each moment exponential polynomial.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose short-window escape is narrowed here.

## Research consequence

For fixed finite translated Wang banks, **ordinary finite-window localization is no longer an open escape**. A surviving fixed-bank construction must place its cancellation on windows shrinking at least on the scale allowed by the number of active phase fibers; even that regime is merely not excluded by this argument.

The live Wang source question should therefore focus on genuinely scale-dependent phase geometry, growing or coalescing banks, adaptive/frequency-dependent coefficients, or signed arithmetic structure of the normalized Chebyshev-theta remainder `G`. Any such mechanism still has to survive coefficient conditioning, finite-frequency leakage, and the downstream derivative repayment isolated by the earlier Wang findings.