# NB-161 — Collapsing Jordan transport forces conditioning blowup

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + CLASSICAL-TRANSPORT-MECHANISM + TARGET-CONDITIONED + DECISIVE-METHOD-BOUNDARY

`NB-160` removes fixed sign separation as an escape: if the positive and negative Jordan supports stay more than a sufficiently large fixed number of Poisson widths apart, routine local zero density forces an `Omega(log G)` adverse reservoir. That leaves the opposite geometry—interlacing or collapsing the two signs so that the same local zeros see both pieces.

There is a complementary obstruction at the collapsing end. For the exterior Poisson kernel at fixed horizontal offset, response to a zero-mass signed measure is Lipschitz in the vertical sampling height. Consequently the response is controlled by the optimal transport distance between the positive and negative Jordan masses. If those two masses can be coupled across a scale `epsilon_G -> 0`, then an order-`c_G` target response is impossible under bounded total-variation conditioning. More quantitatively, **conditioning times Jordan transport length has a positive target-dependent lower bound**.

This does not rule out fixed-width interlacing. It identifies it as the actual unresolved geometry between the two already-closed extremes: large fixed sign separation exports an adverse reservoir by `NB-160`, while transport collapse to `o(1)` kills target gain by the present result.

## Claim

Fix `a>0`. Let `nu` be any finite real signed Borel measure on `R` with zero total mass and Jordan decomposition

\[
\nu=\nu^+-\nu^-.
\]

Write

\[
M:=\nu^+(\mathbb R)=\nu^-(\mathbb R)>0,
\qquad
V:=\|\nu\|_{\rm TV}=2M.
\]

For `x in [a,a+1]` and `gamma in R`, define the exterior Poisson response

\[
Q_\nu(x,\gamma)
:=
\int_{\mathbb R}
\frac{x}{x^2+(\gamma-t)^2}
\,d\nu(t).
\]

Let

\[
\mathsf W_1(\nu^+,\nu^-)
:=
\inf_{\pi\in\Pi(\nu^+,\nu^-)}
\int_{\mathbb R^2}|s-t|\,d\pi(s,t)
\]

be the unnormalized one-dimensional transport cost between the equal Jordan masses, and define the mean optimal transport length

\[
\ell(\nu)
:=
\frac{\mathsf W_1(\nu^+,\nu^-)}{M}.
\]

Then uniformly in `x in [a,a+1]` and `gamma in R`,

\[
\boxed{
|Q_\nu(x,\gamma)|
\le
\frac{9}{8\sqrt3\,a^2}\,
\mathsf W_1(\nu^+,\nu^-)
=
\frac{9}{16\sqrt3\,a^2}\,V\,\ell(\nu).
}
\]

Now let `nu_G` be a sampler family with a distinguished positive target scale `c_G>0`, and put

\[
C_G:=\frac{V_G}{c_G}.
\]

If at even one target point `(x_G,gamma_G)` with `x_G in [a,a+1]` the sampler has positive gain

\[
Q_{\nu_G}(x_G,\gamma_G)\ge q\,c_G
\]

for some fixed `q>0`, then necessarily

\[
\boxed{
C_G\,\ell(\nu_G)
\ge
\frac{16\sqrt3}{9}\,q a^2.
}
\]

In particular, if the two Jordan measures admit a coupling supported on

\[
|s-t|\le\varepsilon_G,
\]

then `ell(nu_G)<=epsilon_G` and hence

\[
\boxed{
C_G\,\varepsilon_G
\ge
\frac{16\sqrt3}{9}\,q a^2.
}
\]

Therefore:

- bounded conditioning `C_G=O(1)` forbids transport collapse `epsilon_G=o(1)` whenever order-`c_G` target gain is required;
- conversely, forcing the two signs to cancel pairwise on scale `epsilon_G` while retaining fixed target gain costs at least `C_G=Omega(1/epsilon_G)` total-variation conditioning.

For the zeta-zero sampler used in `NB-148` through `NB-160`, take

\[
x_G=1+a-\beta,
\]

so `x_G in (a,a+1)` for every nontrivial zero `rho=beta+i gamma`. Thus the estimate applies directly to the same Poisson response

\[
Q_G(\rho)
=
\int
\frac{1+a-\beta}{(1+a-\beta)^2+(\gamma-t)^2}
\,d\nu_G(t).
\]

## Derivation

For fixed `x>0` and `gamma`, set

\[
K_{x,\gamma}(t)
:=
\frac{x}{x^2+(\gamma-t)^2}.
\]

Its derivative in the sampling height is

\[
\partial_t K_{x,\gamma}(t)
=
\frac{2x(\gamma-t)}{\bigl(x^2+(\gamma-t)^2\bigr)^2}.
\]

Writing

\[
u:=\frac{|\gamma-t|}{x},
\]

we get

\[
|\partial_t K_{x,\gamma}(t)|
=
\frac{2u}{x^2(1+u^2)^2}.
\]

The scalar function `2u/(1+u^2)^2` on `u>=0` is maximized at `u=1/sqrt(3)` with value `9/(8sqrt(3))`. Hence

\[
\operatorname{Lip}(K_{x,\gamma})
\le
\frac{9}{8\sqrt3\,x^2}
\le
L_a,
\qquad
L_a:=\frac{9}{8\sqrt3\,a^2}.
\]

Take any coupling `pi in Pi(nu^+,nu^-)`. Since its marginals are the two Jordan measures,

\[
\begin{aligned}
Q_\nu(x,\gamma)
&=
\int_{\mathbb R^2}
\bigl(K_{x,\gamma}(s)-K_{x,\gamma}(t)\bigr)
\,d\pi(s,t).
\end{aligned}
\]

Therefore

\[
|Q_\nu(x,\gamma)|
\le
L_a
\int|s-t|\,d\pi(s,t).
\]

Taking the infimum over couplings gives

\[
|Q_\nu(x,\gamma)|
\le
L_a\mathsf W_1(\nu^+,\nu^-)
=
L_a M\ell(\nu)
=
\frac{L_a}{2}V\ell(\nu).
\]

If `Q_{nu_G}(x_G,gamma_G)>=q c_G`, then

\[
q c_G
\le
\frac{L_a}{2}V_G\ell(\nu_G)
=
\frac{L_a}{2}c_G C_G\ell(\nu_G),
\]

and division by `c_G` proves

\[
C_G\ell(\nu_G)
\ge
\frac{2q}{L_a}
=
\frac{16\sqrt3}{9}qa^2.
\]

If a coupling is supported on `|s-t|<=epsilon_G`, then its transport cost is at most `M_G epsilon_G`, so `ell(nu_G)<=epsilon_G`; the final conditioning lower bound follows immediately.

No zero-counting theorem, height asymptotic, atomicity assumption, support compactness, or polynomial lower-height condition is used. The estimate is purely local in the Poisson geometry and holds before summing over zeros.

## What this changes after NB-160

The phrase “make the signs interlace or collapse on the `O(1)` Poisson-width scale” in `NB-160` contains two mathematically different possibilities. The present estimate rules out genuine **collapse** under bounded conditioning. If almost all positive Jordan mass can be matched to negative Jordan mass across distances `o(1)`, then the Poisson kernel cannot distinguish the two measures strongly enough to produce fixed target gain. Increasing the number of alternating atoms does not change this: the relevant quantity is transport cost, not cardinality.

This also shows that minimum support separation is not the right variable inside the interlaced regime. Two supports may have distance zero because they are densely interwoven, while their mass distributions still have an order-one optimal transport length. Conversely, pairwise sign alternation on a very fine mesh has small transport length and therefore becomes invisible to every fixed-offset Poisson probe unless total variation grows reciprocally.

The surviving bounded-conditioning geometry is consequently narrow:

\[
\boxed{
\text{Jordan supports must overlap/interlace locally, but their mass transport cannot collapse below a fixed scale.}
}
\]

Combined with `NB-160`, a bounded-conditioning height-only selector cannot use either of the two simple extremes:

- **separated signs:** sufficiently large fixed support separation forces the routine `Omega(log G)` adverse-zero reservoir;
- **collapsed signs:** `ell(nu_G)=o(1)` forces `Q_G/c_G=o(1)` uniformly and loses the target.

What remains is fixed-width `Theta(1)` transport with enough local sign overlap to defeat the separated-reservoir argument. That is a much more specific target than generic “interlacing.”

## Conditioning as the price of fine cancellation

The inequality can be read as an uncertainty relation for this sampler architecture:

\[
\boxed{
\text{target gain}
\lesssim_a
\text{conditioning}\times\text{Jordan transport length}.
}
\]

Thus fine signed cancellation is not free. If a construction uses increasingly close positive/negative pairs at scale `epsilon_G`, it must amplify their coefficients by at least `Omega(1/epsilon_G)` relative to the distinguished target mass. This is exactly the kind of conditioning loss that earlier findings treated as a separate escape currency; the present result shows that sign-collapse and conditioning are quantitatively coupled rather than independent.

This observation also prevents a misleading limiting argument. A sequence of highly oscillatory signed measures may converge weakly to zero while retaining large total variation. The Poisson response can stay nontrivial only because the conditioning diverges fast enough to compensate for the shrinking transport scale. Weak cancellation alone is therefore not a bounded-cost route to selectivity.

## Prior-art and novelty audit

The transport inequality itself is classical in mechanism: it is the elementary coupling direction behind Kantorovich--Rubinstein duality, specialized here to the one-dimensional Poisson kernel. The proof above is included in full, so no external optimal-transport theorem is load-bearing.

A fresh literature search found the expected general theory relating Lipschitz test functions to Wasserstein/Kantorovich--Rubinstein distance and separate harmonic-analysis literature on derivative bounds for Poisson kernels. Searches combining Nyman--Beurling, zeta Poisson sampling, and Wasserstein/optimal transport did not locate this target-conditioned application or the conditioning-versus-Jordan-transport boundary. Accordingly, no novelty is claimed for the transport inequality itself; the line-local contribution is the exact identification of **optimal Jordan transport length as the missing geometric currency between `NB-160`'s separated-support obstruction and the proposed interlaced escape**.

Because the proof is elementary and self-contained, `SOURCES.md` needs no new load-bearing anchor.

## Boundary and decisive next test

This result does **not** rule out sign measures with order-one optimal transport length whose supports nevertheless overlap densely, and it does not show that such a measure avoids an adverse zero reservoir. It also allows collapsing pairs when conditioning grows at the required reciprocal rate. Those are genuine remaining regimes, not omissions hidden by the estimate.

The next sharp question is therefore no longer whether opposite signs can merely be placed close together. It is whether a zero-mass sampler with

\[
C_G=O(1),
\qquad
\ell(\nu_G)\asymp1,
\qquad
\operatorname{dist}(\operatorname{supp}\nu_G^+,\operatorname{supp}\nu_G^-)=O(1)
\]

can simultaneously keep order-`c_G` target gain and make the routine local zero population cancel rather than export an `Omega(log G)` adverse lobe. A proof or counterexample in that fixed-width interlaced regime would close the geometric gap left jointly by `NB-160` and `NB-161`.