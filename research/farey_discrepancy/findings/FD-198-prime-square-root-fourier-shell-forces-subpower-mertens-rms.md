# FD-198 — Prime square-root Fourier shells force subpower Mertens RMS at the critical half-Sobolev budget

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** square-root Fourier shell / reciprocal-prime Mertens sampling / simultaneous recovery barrier
- **Depends on:** FD-117, FD-193, FD-196, FD-197
- **Classification:** `EXACT-DERIVED + PRIME-SHELL-MEAN-SQUARE + SIMULTANEOUS-RECOVERY + NEGATIVE/POSITIVE-ENERGY-OVERCOERCIVITY`

## Claim

`FD-196` identifies the half-Sobolev estimate

\[
\mathcal E_{H,1/2}(K)
:=
\sum_{k\le K}\frac{|\mathcal B_H(k)|^2}{k}
=
O_\varepsilon(H^{1+\varepsilon}),
\qquad K\asymp\sqrt H,
\]

as a sufficient route to RH-scale pointwise Mertens recovery. The same positive energy, however, simultaneously controls many Mertens values much more strongly than the one-row estimate reveals.

Let

\[
\mathcal B_H(k)
=
\sum_{d\mid k}d\,M\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
K=\lfloor\sqrt H\rfloor,
\]

and let

\[
\mathcal P_K
=
\{p\text{ prime}:K/2<p\le K\}.
\]

For every prime `p in P_K`,

\[
\boxed{
\mathcal B_H(p)-\mathcal B_H(1)
=
p\,M\!\left(\left\lfloor\frac Hp\right\rfloor\right).
}
\tag{1}
\]

Hence the centered prime shell has the exact identity

\[
\boxed{
\mathcal C_H
:=
\sum_{p\in\mathcal P_K}
\frac{|\mathcal B_H(p)-\mathcal B_H(1)|^2}{p}
=
\sum_{p\in\mathcal P_K}
p\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2.
}
\tag{2}
\]

The shell lies entirely inside the square-root band and satisfies

\[
\boxed{
\mathcal C_H
\le
(2+o(1))\,\mathcal E_{H,1/2}(K).
}
\tag{3}
\]

Consequently,

\[
\boxed{
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\le
(4+o(1))
\frac{\mathcal E_{H,1/2}(K)}{K}.
}
\tag{4}
\]

The prime number theorem gives

\[
|\mathcal P_K|
\sim \frac{K}{2\log K}.
\tag{5}
\]

Moreover the quotient samples in (4) are distinct for all sufficiently large `H`: if `p<q` are odd primes in `P_K`, then

\[
\frac Hp-\frac Hq
=
\frac{H(q-p)}{pq}
\ge
\frac{2H}{K^2}
\ge2,
\tag{6}
\]

so their floors cannot coincide. All these samples have size `Theta(K)`.

It follows that if

\[
\mathcal E_{H,1/2}(K)=H^{\gamma+o(1)},
\tag{7}
\]

then their root-mean-square Mertens value obeys

\[
\boxed{
\left(
\frac1{|\mathcal P_K|}
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\right)^{1/2}
\ll
K^{\gamma-1+o(1)}.
}
\tag{8}
\]

In particular, the `FD-196` critical half-Sobolev budget

\[
\mathcal E_{H,1/2}(K)=O_\varepsilon(H^{1+\varepsilon})
\tag{9}
\]

forces

\[
\boxed{
\left(
\frac1{|\mathcal P_K|}
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\right)^{1/2}
=
K^{o(1)}.
}
\tag{10}
\]

Equivalently, for every `eta>0` the RMS in (10) is `O_eta(K^eta)` along any horizon family on which (9) holds uniformly for every epsilon.

This is substantially stronger on this reciprocal-prime sample than the pointwise RH-scale target `M(n)=O_\varepsilon(n^{1/2+\varepsilon})` at `n=Theta(K)`. It does not prove that (9) is false and does not show that RH cannot imply (9); it shows that the positive energy proposed in `FD-196` carries a simultaneous sparse-shell consequence that is invisible in the one-row dual estimate.

The random-multiplicative benchmark of `FD-197` lands exactly on the opposite scale. Its half-Sobolev mean has exponent `gamma=3/2`, and (8) then gives the natural square-root RMS scale

\[
K^{1/2+o(1)}.
\tag{11}
\]

Thus the missing half power between `FD-197` and the `FD-196` critical budget is equivalently a demand to compress a whole reciprocal-prime Mertens shell from square-root RMS to subpower RMS.

## 1. The prime modes are two-term divisor rows

For prime `p`, the only divisors are `1` and `p`. Therefore

\[
\mathcal B_H(p)
=
M(H)
+
p\,M\!\left(\left\lfloor\frac Hp\right\rfloor\right).
\tag{12}
\]

Since

\[
\mathcal B_H(1)=M(H),
\tag{13}
\]

subtracting the zero-frequency divisor row gives (1), and squaring with weight `1/p` gives the exact identity (2).

This centering is observation-native. Both `B_H(1)` and `B_H(p)` are retained signed Farey Fourier/divisor-transform coordinates; no source coefficient or off-band information is inserted.

## 2. The full positive energy controls the whole shell

By the elementary inequality `|u-v|^2<=2|u|^2+2|v|^2`,

\[
\begin{aligned}
\mathcal C_H
&\le
2\sum_{p\in\mathcal P_K}\frac{|\mathcal B_H(p)|^2}{p}
+
2|\mathcal B_H(1)|^2
\sum_{p\in\mathcal P_K}\frac1p \\
&\le
2\mathcal E_{H,1/2}(K)
+
2\mathcal E_{H,1/2}(K)
\sum_{p\in\mathcal P_K}\frac1p.
\end{aligned}
\tag{14}
\]

The prime number theorem implies

\[
|\mathcal P_K|=O(K/\log K),
\tag{15}
\]

and because `p>K/2` on the shell,

\[
\sum_{p\in\mathcal P_K}\frac1p
\le
\frac{2|\mathcal P_K|}{K}
=
O(1/\log K)
=
o(1).
\tag{16}
\]

This proves (3). Since every shell prime also satisfies `p>K/2`, equation (2) gives

\[
\frac K2
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\le
\mathcal C_H,
\tag{17}
\]

which proves (4).

Combining (4) with the asymptotic (5) yields

\[
\frac1{|\mathcal P_K|}
\sum_{p\in\mathcal P_K}
\left|M\!\left(\left\lfloor\frac Hp\right\rfloor\right)\right|^2
\ll
\frac{\log K}{K^2}\,
\mathcal E_{H,1/2}(K).
\tag{18}
\]

Since `H=K^2+O(K)`, substituting (7) and taking square roots proves (8).

## 3. Why this changes the `FD-196` target

The one-row theorem of `FD-196` is deliberately target-wise: at `sigma=1/2`, an energy exponent `gamma=1` recovers one geometric witness with the RH-facing exponent `1/2`. Equation (18) shows that the same positive energy cannot spend its budget independently on all rows. The prime modes already contain `Theta(K/log K)` distinct quotient witnesses of size `Theta(K)`, and their squared errors all enter the same nonnegative budget.

At `gamma=1`, the simultaneous consequence is therefore not merely square-root-scale control at those witnesses but subpower RMS. At the `FD-197` random-multiplicative exponent `gamma=3/2`, the shell instead has the square-root scale expected from a random-walk model. The half-power spectral deficit can therefore be restated without Sobolev terminology:

> the critical positive half-Sobolev theorem must suppress the reciprocal-prime Mertens shell by a factor `K^(1/2-o(1))` in RMS relative to the random-multiplicative baseline.

This does not invalidate the critical energy as a sufficient theorem. It does make clear that proving it by uniform positive suppression of all square-root-band modes asks for considerably more than the standard pointwise RH exponent on a sparse but growing family of source coordinates.

A more economical route to RH may therefore need an indefinite cross-mode or cross-horizon statistic that preserves the contractive divisor inverse without forcing every prime shell simultaneously into subpower RMS. That is a research direction, not a theorem established here.

## 4. Representation and hostile checks

The argument stays in the exact representation of `FD-117/FD-196`. The shell uses a subset of the already retained modes, and the only new operation is the observable difference `B_H(p)-B_H(1)`. Equation (1) is an exact divisor-row identity; there is no approximate inversion or hidden source access.

The distinctness check matters. Without (6), an RMS over primes could repeatedly sample the same Mertens coordinate and overstate the amount of simultaneous information. For `p,q` in the dyadic prime shell, prime spacing alone gives a real quotient separation at least two, so the `Theta(K/log K)` samples are genuinely different.

The conclusion is also norm-specific. It concerns the positive half-Sobolev band energy from `FD-196`. A signed statistic may permit cancellations between modes that (14) intentionally discards, and another destination norm need not pay this simultaneous RMS tariff. Thus the finding narrows the positive-energy route; it does not create a general information lower bound for all Farey observations.

## 5. Prior-art and formalization gates

The floor-quotient Möbius recurrence and isolated values `M(floor(H/d))` are classical and already anchored in this line by Deléglise--Rivat. General distributional and mean-value questions for the Mertens function are also classical; for example Nathan Ng, *The Distribution of the Summatory Function of the Möbius Function*, Proc. London Math. Soc. **89** (2004), 361--389, studies a conditional limiting distribution and weak-Mertens consequences under RH plus additional zero-moment hypotheses.

A targeted search for mean-square estimates on the specific reciprocal-prime sample `M(floor(H/p))`, with `p` restricted to a square-root dyadic shell, did not locate a direct analogue of (2)--(10). No external theorem beyond the prime number theorem is load-bearing here, and PNT is already anchored in `SOURCES.md`; that file is therefore unchanged.

No formalization issue is opened. The finite core is the two-divisor identity (12), a quadratic triangle inequality, and elementary separation of reciprocal-prime samples. The substantive content is its asymptotic interaction with the `FD-196`/`FD-197` phase diagram rather than a new reusable formal combinatorial lemma.
