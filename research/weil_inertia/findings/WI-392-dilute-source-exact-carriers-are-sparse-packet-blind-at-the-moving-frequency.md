# WI-392 — dilute source-exact carriers are sparse-packet blind at the moving frequency

**Status:** `EXACT-DERIVED + CLASSICAL-WEIL-IDENTITY + SOURCE-EXACT + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-391 opens the first positive RH-side floor in the fixed-width source-exact program by putting only

\[
\epsilon_R=\frac{c}{\log R}
\]

of the one-lobe `L^2` mass into a carrier packet near frequency `R`, while separating the two physical lobes by a distance `A` satisfying

\[
A\to\infty,
\qquad
A=o(\log\log R).
\tag{1}
\]

That mechanism is necessarily **collective** at the carrier frequency. It cannot simultaneously turn one, or any sufficiently sparse packet, of off-critical zeros near ordinate `R` into an order-one defect.

More precisely, retain the exact WI-391 construction. Let

\[
g_R=\sqrt{1-\epsilon_R}\,\phi+\sqrt{\epsilon_R}\,\nu_R
\]

on a fixed interval `[-L/2,L/2]`, where `phi` is fixed real-even `C_c^\infty`, the real-even carrier `nu_R` has uniformly bounded `L^\infty` norm and support in the same interval, and its Fourier mass is concentrated near `\pm R`. Let `chi_A` be the exact Desogus source-slot cutoff at

\[
x=e^A,
\]

put

\[
p_{A,R}=\chi_A g_R,
\]

and form the separated odd trial

\[
f_{A,R}(y)
=p_{A,R}(y-A/2)-p_{A,R}(-y-A/2).
\tag{2}
\]

For a nontrivial zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad |\delta|<\frac12,
\]

lying in any fixed-width carrier packet

\[
|\gamma-R|\le\Delta,
\tag{3}
\]

the individual zero term in Weil's quadratic functional obeys, for every fixed integer `M>=1`,

\[
\boxed{
|T_\rho(f_{A,R})|
\ll_{L,\Delta,M}
 e^{A|\delta|}
 \left(
 \frac1{\log R}
 +\frac{e^{-A}}{A^2}
 +R^{-2M}
 \right).
}
\tag{4}
\]

Here `T_rho` denotes the standard Hermitian zero-side summand

\[
T_\rho(f)
=\widetilde f(\rho)\,
 \overline{\widetilde f(1-\overline\rho)}
\tag{5}
\]

in centered logarithmic coordinates. Equation (4) is an absolute-value estimate, so it makes no sign or cancellation assumption and survives the functional-equation/conjugation symmetries.

Uniformly throughout the critical strip this gives

\[
\boxed{
|T_\rho(f_{A,R})|
\ll
q(A,R):=
\frac{e^{A/2}}{\log R}
+\frac{e^{-A/2}}{A^2}
+e^{A/2}R^{-2M}.
}
\tag{6}
\]

Under the exact WI-391 scale condition (1),

\[
\boxed{q(A,R)\longrightarrow0.}
\tag{7}
\]

Consequently, if `M_off(A,R)` denotes the total multiplicity of off-critical zeros in the fixed carrier packet (3), counting whatever functional-equation/conjugation copies are included in the chosen symmetric zero sum, then

\[
\boxed{
\left|\sum_{\rho\ \mathrm{off\ line}\atop |\Im\rho-R|\le\Delta}
T_\rho(f_{A,R})\right|
\ll M_{\rm off}(A,R)\,q(A,R).
}
\tag{8}
\]

In particular every packet satisfying

\[
M_{\rm off}(A,R)q(A,R)\to0
\tag{9}
\]

is asymptotically invisible at order-one scale to the **moving-frequency channel** which creates WI-391's positive RH floor.

For WI-391's explicit diagonal choice

\[
R=\exp(\exp(A^2)),
\tag{10}
\]

one has

\[
q(A,R)
\ll
e^{-A^2+A/2}
+\frac{e^{-A/2}}{A^2}
+e^{A/2-2M e^{A^2}}
\ll \frac{e^{-A/2}}{A^2},
\tag{11}
\]

so the concrete sparse-packet regime

\[
\boxed{
M_{\rm off}(A,R)=o(A^2e^{A/2})
}
\tag{12}
\]

cannot perturb the order-one carrier floor by an order-one amount. With `A=log(k+1)`, this includes

\[
M_{\rm off}=o\!\left(\sqrt{k+1}\,\log^2(k+1)\right).
\tag{13}
\]

The conclusion is deliberately local in **ordinate** and in **mechanism**. It does not say that the whole trial is blind to a fixed off-line zero at bounded ordinate. The fixed base profile `phi` remains present with coefficient tending to one, and separated compactly supported tests can have exponentially large response to a fixed off-line zero as `A` grows. Nor does (8) bound the contribution of all off-line zeros outside the moving packet. What it closes is the hoped-for bootstrap in which the same dilute high-frequency packet that obtains an order-one RH contribution from `Theta(log R)` critical-line zeros would also charge each sparse off-line zero near `R` by order one.

## 1. The exact zero-side Hermitian product

Bombieri's formulation of Weil's quadratic functional starts from the classical explicit-formula functional `T` and the multiplicative autocorrelation

\[
h=f*\overline f^{\,*}.
\]

For the Mellin transform

\[
\widetilde f(s)=\int_0^\infty f(x)x^{s-1}\,dx,
\]

multiplicative convolution and the involution give the classical identity

\[
\widetilde h(s)
=\widetilde f(s)
 \overline{\widetilde f(1-\overline s)}.
\tag{14}
\]

Hence the zero side is a sum of the terms (5). Under RH, `1-overline(rho)=rho`, so these become the positive squares used in WI-391. Off the line they are indefinite cross-products instead; this is exactly the signature distinction that the canonical research mandate requires us to preserve.

Pass to centered logarithmic coordinates by writing

\[
H(y)=e^{y/2}f(e^y),
\qquad
F(z)=\int_{\mathbb R}H(y)e^{izy}\,dy.
\tag{15}
\]

Then

\[
\widetilde f(1/2+iz)=F(z).
\]

For

\[
\rho=\frac12+\delta+i\gamma
\]

the two factors in (5) are therefore evaluations at

\[
z_-=\gamma-i\delta,
\qquad
z_+=\gamma+i\delta.
\tag{16}
\]

Thus

\[
|T_\rho(f)|
\le |F(z_-)|\,|F(z_+)|.
\tag{17}
\]

Nothing in (14)--(17) assumes RH. The only later use of the critical strip is the classical bound `|delta|<1/2`.

## 2. A fixed-width carrier has only `sqrt(epsilon_R)` amplitude at one complex frequency

Write

\[
P_{A,R}(z)
:=\int_{-L/2}^{L/2}p_{A,R}(s)e^{izs}\,ds.
\tag{18}
\]

First ignore the source perforation. On every fixed horizontal strip `|Im z|<=1/2`, integration by parts for the fixed smooth base gives, for every `M`,

\[
|\widehat\phi(z)|
\ll_{L,M}(1+|\Re z|)^{-M}.
\tag{19}
\]

WI-388's carrier has fixed support and uniformly bounded `L^\infty` norm. Hence also a uniformly bounded `L^1` norm, and therefore

\[
|\widehat\nu_R(z)|\ll_L1
\qquad(|\Im z|\le1/2).
\tag{20}
\]

At `|Re z-R|<=Delta`, or symmetrically near `-R`, equations (19)--(20) yield

\[
|\widehat g_R(z)|
\ll_{L,\Delta,M}
R^{-M}+\sqrt{\epsilon_R}.
\tag{21}
\]

This is the basic dilution law. The sideband can have a pointwise lower bound of size `sqrt(epsilon_R)` on the real axis, which is enough to generate an order-one RH sum after `Theta(log R)` critical-line zeros are accumulated, but one selected spectral point receives only `O(sqrt(epsilon_R))` amplitude.

## 3. Exact source perforation costs only its tiny slot measure

Let

\[
\eta_A=1-\chi_A,
\qquad
r_{A,R}=\eta_A g_R,
\]

so that

\[
p_{A,R}=g_R-r_{A,R}.
\tag{22}
\]

WI-390/WI-391 give for the standard centered source slots

\[
0\le\eta_A\le1,
\qquad
\mu_A:=|\operatorname{supp}\eta_A|
\ll_L\frac1{\sqrt{x}\log x},
\qquad x=e^A.
\tag{23}
\]

Thus

\[
\boxed{
\mu_A\ll_L\frac{e^{-A/2}}{A}.
}
\tag{24}
\]

The WI-388 carrier construction also gives `||g_R||_infty <<_L 1`, uniformly in `R`: the fixed base is bounded and `sqrt(epsilon_R) nu_R` is uniformly bounded. Therefore

\[
\|r_{A,R}\|_1
\le \|g_R\|_\infty\mu_A
\ll_L\mu_A.
\tag{25}
\]

For `|Im z|<=1/2` and support `[-L/2,L/2]`,

\[
|\widehat r_{A,R}(z)|
\le e^{L/4}\|r_{A,R}\|_1
\ll_L\mu_A.
\tag{26}
\]

Combining (21), (22), and (26), uniformly for the two packets around `+R` and `-R`,

\[
\boxed{
|P_{A,R}(z)|
\ll_{L,\Delta,M}
\sqrt{\epsilon_R}+\mu_A+R^{-M}
}
\tag{27}
\]

whenever `||Re z|-R|<=Delta` and `|Im z|<=1/2`.

This estimate is stronger than the `L^2` source-transfer bounds needed in WI-390. Here only a single complex evaluation is being controlled, so the vanishing **measure** of the removed source slots and the uniform `L^infty` carrier bound suffice; no logarithmic energy estimate is required.

## 4. Physical separation can amplify horizontal depth only by `e^(A|delta|)`

The odd reflected trial (2) has transform

\[
F_{A,R}(z)
=e^{izA/2}P_{A,R}(z)
-e^{-izA/2}P_{A,R}(-z).
\tag{28}
\]

No evenness of the perforated lobe is needed for this formula. If `z=gamma-i delta`, then

\[
|e^{\pm izA/2}|\le e^{A|\delta|/2}.
\]

For `|gamma-R|<=Delta`, both `z` and `-z` fall under (27). Therefore

\[
\boxed{
|F_{A,R}(\gamma-i\delta)|
\ll
 e^{A|\delta|/2}
 \left(
 \sqrt{\epsilon_R}+\mu_A+R^{-M}
 \right).
}
\tag{29}
\]

The identical estimate holds at `gamma+i delta`. Inserting the two bounds into (17), and using `(a+b+c)^2<=3(a^2+b^2+c^2)`, gives

\[
|T_\rho(f_{A,R})|
\ll
 e^{A|\delta|}
 \left(
 \epsilon_R+\mu_A^2+R^{-2M}
 \right).
\tag{30}
\]

Substituting `epsilon_R=c/log R` and (24) is exactly (4).

A depth-sensitive version is worth retaining. If a packet is known to satisfy

\[
|\delta|\le\delta_*<\frac12,
\]

then

\[
\boxed{
|T_\rho|
\ll
\frac{e^{A\delta_*}}{\log R}
+\frac{e^{-A(1-\delta_*)}}{A^2}
+e^{A\delta_*}R^{-2M}.
}
\tag{31}
\]

Thus the full-strip estimate (6) is simply the worst case `delta_*=1/2`.

## 5. Why the WI-391 scale forces sparse-packet blindness

The first term of (6) satisfies

\[
\frac{e^{A/2}}{\log R}
=\exp\!\left(\frac A2-\log\log R\right)
\longrightarrow0
\tag{32}
\]

under (1). The source-mask term tends to zero because

\[
\frac{e^{-A/2}}{A^2}\to0,
\tag{33}
\]

and the last term is negligible for every fixed `M` once `R->infinity` under the same scale separation. This proves (7).

Summing absolute values over any selected off-line packet proves (8). No hypothesis about pair correlation, multiplicity statistics, cancellation between functional-equation partners, or the sign of their indefinite block is used. The threshold (9) is therefore a hard visibility threshold for this particular carrier architecture.

For the explicit WI-391 schedule (10), `log R=e^(A^2)`, and (11)--(13) follow immediately. Notice what sets the uniform threshold there: the pure carrier contribution is fantastically smaller,

\[
\frac{e^{A/2}}{\log R}=e^{-A^2+A/2},
\]

while the exact source perforation leaves the larger but still vanishing leakage `e^(-A/2)/A^2`. Thus once the carrier is pushed superlogarithmically far out, the source-slot mask, not the carrier itself, is the leading co-moving sparse-defect visibility channel.

## 6. This does not contradict Bombieri completeness or the earlier finite-defect detectors

Bombieri's 2000 theorem says something qualitatively stronger about the **full cofinal Weil form**: if only finitely many nontrivial zeros are off the line, sufficiently large finite truncations have exactly half as many negative eigenvalues as off-line zeros. WI-236 records the corresponding lesson for this research line: finite-packet detection is complete; sparse escape occurs through loss of uniform spectral margin, not through an inability of the full form to see a finite defect.

WI-247 likewise records that RH failure forces a finite odd negative/zero-mode witness in the localized Bombieri/Suzuki framework. There is therefore no contradiction between those facts and (7). The present result concerns one highly anisotropic **scalar sequence of tests** whose spectral mass is deliberately diluted as `1/log R` and moved to infinity.

WI-205 and WI-206 give a close but different negative result on the prime side: an isolated near-line zero residue is sub-diagonal in the WI-195 Gallagher source norm, and changing the local window shape cannot repair that scale mismatch. The current deduction is not another proof of that statement. It acts directly on the zero-side Hermitian product of the WI-391 source-exact carrier and includes the hyperbolic amplification caused by an arbitrary horizontal displacement `|delta|<1/2`. The conclusion is nevertheless structurally parallel: **an observable can obtain an order-one collective effect from a dense reservoir while giving each exceptional object only a vanishing tariff.**

## 7. Prior-art and novelty audit

The load-bearing identities are classical. Weil's 1952 criterion and Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000), supply the multiplicative-autocorrelation quadratic functional and the off-line Hermitian pairing (14). Bombieri also proves the finite-truncation negative-index theorem cited above. The exponential-type estimate behind (19), and the elementary bound of a compactly supported Fourier transform on a fixed horizontal strip, are standard Paley--Wiener/Fourier facts.

Recent operator-theoretic work does not remove the dilution issue. Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v2, 17 Aug 2026), unifies the localized Weil form with Bombieri/Yoshida/Connes--Consani constructions and studies the cofinal finite-interval operator; it does not provide an order-one lower bound for the response of the particular `1/log R` moving carrier to one co-moving off-line zero. The Desogus source-slot construction used in WI-390/WI-391 supplies exact arithmetic admissibility, not a different zero-side sampling law.

A targeted search around `Weil quadratic form + high-frequency modulation/carrier + off-critical zeros + Paley--Wiener` located the classical global criteria and finite-truncation work, but no theorem packaging the scale comparison (4)--(13) for a moving dilute source-exact packet. This is **not** a priority claim. Mathia's claimed novelty is only the exact consequence for the already-defined WI-391 architecture, including the source-perforation leakage term and its explicit visibility threshold.

## 8. Boundary of the no-go

Several stronger mechanisms are outside this finding.

First, a zero whose ordinate stays fixed while `R->infinity` is not in the carrier packet (3). The base profile is not diluted, and physical separation can exponentially amplify its off-line evaluation. The present estimate must not be used to conclude that WI-391 loses Bombieri's individual-defect information globally.

Second, a packet with multiplicity comparable to or larger than `1/q(A,R)` can contribute at order one even under the crude absolute bound. No zero-density theorem is being asserted here that rules such a packet in or out.

Third, a matrix or multi-test construction may coherently accumulate many `o(1)` evaluations in an eigenvalue even when any one scalar trial cannot. This is precisely the type of finite-inertia information that WI-236 says is absent from a single vanishing-margin direction.

Fourth, changing the scale relation can change the conclusion. If `A` were comparable to `log log R`, the hyperbolic factor from a deeply off-line zero could balance the `1/log R` dilution. WI-391 needs the strict sublogarithmic condition (1) to certify its phase-stable RH floor, and (32) shows that the same condition is what kills the individual co-moving tariff.

## Research consequence

Do not try to turn WI-391 into a zero-defect bootstrap by arguing that its **same moving sideband** automatically charges each off-line zero near the carrier frequency. The exact scale budget forbids that: the RH floor is obtained by summing a `1/log R` weight over `Theta(log R)` ordinary critical-line zeros, while a sparse exceptional packet has no compensating count.

The useful surviving splice is now sharper. Keep the carrier as a source-exact way to defeat the RH recurrence/compactness barrier, but obtain individual off-line coercivity from a second channel that does **not** dilute with `R`: the fixed base profile, a matrix/inertia family retaining finite-packet directions, or another source-justified observable. Any proposed bootstrap should expose that two-channel bookkeeping explicitly rather than asking the carrier floor itself to do both jobs.

## Evidence status

- `CLASSICAL-WEIL-IDENTITY`: equations (14)--(17), including the off-line Hermitian product, are the standard multiplicative-autocorrelation form of Weil's explicit formula.
- `EXACT-DERIVED`: equations (21), (24)--(33), the packet bound (8), and the explicit threshold (12) are direct inequalities from WI-388--WI-391's already-persisted construction.
- `SOURCE-EXACT`: the bound is for the actual perforated lobe `p=chi g`, not the unperforated carrier.
- `DECISIVE-NEGATIVE`: it closes the route in which WI-391's moving dilute sideband is itself expected to give an order-one tariff to a sparse co-moving off-line packet.
- `NON-ESTABLISHED-RH`: no new zero-free theorem, simple-zero proportion, or RH conclusion is claimed.