# VIS-430 — target autocorrelation bounds finite-window hitting

## Claim

Let `(X,m)` carry a measure-preserving flow `tau(u)`, let `E` have mass `mu>0`, and define `H_E(x)=inf{|u|:x tau(u) in E}` and `L_rho(x)=int_(-rho)^rho 1_E(x tau(u))du`. Then

`m{H_E>rho} <= Var(L_rho)/((2rho mu)^2+Var(L_rho))`.

Moreover

`Var(L_rho)=int_(-2rho)^(2rho)(2rho-|s|)[C_E(s)-mu^2]ds`,

where `C_E(s)=int 1_E(x)1_E(x tau(s))dm(x)`.

For torus translation with frequencies `omega`, if `f_E=1_E-mu` has Fourier coefficients `fhat(k)` and `lambda_k=<k,omega>`, then

`Var(L_rho)=4 sum_(k!=0)|fhat(k)|^2 sin^2(rho lambda_k)/lambda_k^2`

when no nonzero resonance occurs. For the Wang prime-log torus, unique factorization gives exactly that nonresonance.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL SECOND-MOMENT METHOD + NO-NOVELTY-CLAIM`.

## Derivation

Tonelli and invariance give `E[L_rho]=2rho mu` and the autocorrelation formula for `E[L_rho^2]`. Since `{L_rho>0}` implies a hit, Paley-Zygmund at threshold zero gives `m{H_E<=rho}>=E[L_rho]^2/E[L_rho^2]`. Parseval gives the torus formula.

## Consequence and boundary

Combined with `VIS-429`, target mass supplies a lower quiet-tail floor while target autocorrelation supplies an upper quiet-tail certificate. A quiet event is Haar-rare if `Var(L_rho)=o(rho^2 mu^2)`. A weak bound proves no anomaly; it identifies target-indicator Fourier mass near prime-log small divisors as the next object to inspect. The indicator may have infinitely many modes even when the Wang amplitude is a finite Laurent polynomial, so `VIS-423` cannot be substituted without an approximation theorem.

The probability step is classical Paley-Zygmund/second-moment machinery; no new general hitting theorem, mixing law, selector anomaly, or RH consequence is claimed.

## Dependencies

- `VIS-419`: prime-torus Haar self-null.
- `VIS-425`: Wang amplitude/flow setup.
- `VIS-428`: fixed-shell saturation.
- `VIS-429`: target-rarity lower tail.
