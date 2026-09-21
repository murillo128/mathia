# AF-476 — Compressibility profiles force Hamming-cube lower conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-RESTRICTION`, `APPROXIMATE-SPARSITY`, `QUANTITATIVE-FIDELITY`, `NONLINEAR-TARGET`, `SCALE-AWARE`, `MINIMAX-LOWER-BOUND`, `NO-NOVELTY-CLAIM`

## Claim

AF-475 converts a best-`s`-term tail profile into an achieved resolution-dependent Hilbert conditioning bound for the canonical coordinate embedding. Its explicit boundary was that this was only an upper bound: a different nonlinear Hilbert representation might conceivably beat the power-law or polylogarithmic deterioration.

The profile itself already contains a matching nonlinear obstruction whenever it permits a sufficiently large amount of mass to remain spread over many private coordinates.

Let `A` be a finite or countable alphabet and let

\[
\tau_s(\mu)
=
\inf_{S\subset A,\ |S|\le s}\mu(A\setminus S),
\]

with nonincreasing `phi:N->[0,1]` and

\[
\mathcal C_\phi
=
\{\mu\in\operatorname{Prob}(A):\tau_s(\mu)\le\phi(s)\text{ for every }s\ge1\}.
\tag{1}
\]

Fix `0<delta<=1`. For an integer `k>=1`, assume

\[
\phi(k)\ge\frac\delta2
\tag{2}
\]

and that `A` contains at least `2k+1` distinct atoms. Then `C_phi` contains a scaled isometric copy of the `k`-dimensional Hamming cube whose edges have `d_1`-length `delta/k` and whose antipodes have `d_1`-distance exactly `delta`.

Consequently, for every Hilbert space `H` and every globally `1`-Lipschitz map

\[
F:(\mathcal C_\phi,d_1)\to H,
\]

there is an antipodal pair `mu,nu in C_phi` with

\[
d_1(\mu,\nu)=\delta
\]

but

\[
\boxed{
\|F(\mu)-F(\nu)\|_H
\le
\frac\delta{\sqrt{k}}.
}
\tag{3}
\]

Therefore any resolution-`delta` inverse estimate

\[
\|F(\mu)-F(\nu)\|_H
\ge
\frac1K d_1(\mu,\nu)
\qquad
\text{whenever }d_1(\mu,\nu)\ge\delta
\tag{4}
\]

must satisfy

\[
\boxed{K\ge\sqrt{k}.}
\tag{5}
\]

Define the profile breadth visible at scale `delta` by

\[
N_\phi(\delta)
=
\sup\left\{k\ge1:\phi(k)\ge\frac\delta2\right\},
\tag{6}
\]

with the additional finite-alphabet cutoff `2k+1<=|A|` when needed. Then the optimal normalized Hilbert condition number at resolution `delta` obeys

\[
\boxed{
K^{\mathrm{opt}}_{\phi,H}(\delta)
\ge
\sqrt{N_\phi(\delta)}.
}
\tag{7}
\]

If `N_phi(delta)=infinity`, no finite resolution-`delta` condition number is possible for a globally Lipschitz Hilbert representation.

Thus the inverse tail profile is not merely a resource consumed by the AF-475 coordinate construction. It is also a **metric lower-bound resource** seen by every nonlinear Hilbert encoding with controlled upper sensitivity.

## Exact cube construction

Choose distinct atoms

\[
a_0,a_1,b_1,\ldots,a_k,b_k
\]

and set

\[
\varepsilon=\frac\delta2\le\frac12.
\]

For each sign vector `omega in {-1,+1}^k`, define

\[
\mu_\omega
=
(1-\varepsilon)\delta_{a_0}
+
\frac{\varepsilon}{k}
\sum_{j=1}^k
\begin{cases}
\delta_{a_j},&\omega_j=+1,\\
\delta_{b_j},&\omega_j=-1.
\end{cases}
\tag{8}
\]

Because `epsilon<=1/2`, the common atom has mass at least every private atom. Hence for `1<=s<=k`, the best `s`-term approximation keeps the common atom and `s-1` private atoms, giving

\[
\tau_s(\mu_\omega)
=
\varepsilon\frac{k-s+1}{k}
\le\varepsilon.
\tag{9}
\]

Since `phi` is nonincreasing and `(2)` holds,

\[
\varepsilon
\le
\phi(k)
\le
\phi(s)
\qquad(1\le s\le k).
\tag{10}
\]

For `s>=k+1`, the tail is zero. Thus every cube vertex lies in `C_phi`.

If two sign vectors differ in `r` coordinates, exactly `r` private atoms of mass `epsilon/k` move to their paired locations, so

\[
\boxed{
 d_1(\mu_\omega,\mu_\eta)
=
\frac{2\varepsilon}{k}d_H(\omega,\eta)
=
\frac\delta{k}d_H(\omega,\eta).
}
\tag{11}
\]

Edges therefore have source length `delta/k`, while antipodes have source length `delta`.

## Hilbert obstruction

Set

\[
f(\omega)=F(\mu_\omega).
\]

The Hilbert/Enflo cube inequality used already in AF-464 is

\[
\mathbb E_\omega
\|f(\omega)-f(-\omega)\|_H^2
\le
\sum_{j=1}^k
\mathbb E_\omega
\|f(\omega)-f(\omega^{(j)})\|_H^2.
\tag{12}
\]

Because `F` is globally `1`-Lipschitz and each source edge has length `delta/k`, every term on the right is at most `(delta/k)^2`. Therefore

\[
\mathbb E_\omega
\|f(\omega)-f(-\omega)\|_H^2
\le
\frac{\delta^2}{k}.
\tag{13}
\]

At least one antipodal pair consequently satisfies `(3)`. Its source distance is exactly `delta` by `(11)`, so any lower estimate `(4)` forces `(5)`.

No linearity, barycentricity, coordinate representation, reconstruction algorithm, or finite-dimensional target assumption is used. The only destination assumptions are Hilbert geometry and a normalized global upper Lipschitz bound.

## Relation to AF-464 and AF-475

AF-464 embeds a full-mass Hamming cube into the hard `k`-sparse simplex and proves that arbitrary Lipschitz nonlinear Hilbert encoders pay distortion at least `sqrt(k)`. AF-476 inserts the same metric mechanism **inside a prescribed soft-compressibility profile and at a prescribed absolute resolution**. The common head absorbs the mass that must remain highly compressible, while a tail of total mass `delta/2` carries the `k` independent switches.

AF-475 supplies the complementary achieved upper bound

\[
K_\phi(\delta)
=
\inf_{2\phi(s)<\delta}
\frac{\sqrt{s}}{1-2\phi(s)/\delta}
\tag{14}
\]

for the canonical coordinate map. AF-476 shows that the appearance of a square root of an effective support scale is not merely an artifact of that map. Any Hilbert representation with bounded upper sensitivity must pay at least the square root of the largest cube dimension whose permitted tail mass still reaches half the demanded resolution.

The two thresholds are deliberately different. AF-475 needs a support scale where the unresolved two-source tail is **strictly below** the demanded resolution; AF-476 uses a scale where one source may still hide tail mass `delta/2`. For arbitrary profiles a sharp downward jump can separate these scales. For regular decay laws they have the same asymptotic order.

## Regular-profile consequences

Suppose first that the profile has two-sided polynomial order: for all sufficiently large `s`,

\[
a s^{-\alpha}
\le
\phi(s)
\le
A s^{-\alpha}
\tag{15}
\]

with `a,A,alpha>0`. Then

\[
N_\phi(\delta)
\asymp
\delta^{-1/\alpha}
\qquad(\delta\downarrow0),
\]

and `(7)` gives

\[
K^{\mathrm{opt}}_{\phi,H}(\delta)
=
\Omega\!\left(\delta^{-1/(2\alpha)}\right).
\tag{16}
\]

Combined with AF-475,

\[
\boxed{
K^{\mathrm{opt}}_{\phi,H}(\delta)
\asymp
\delta^{-1/(2\alpha)}
}
\tag{17}
\]

up to constants depending on the profile parameters. Thus the exponent `1/(2alpha)` from AF-475 is minimax-sharp over the whole class `C_phi`, even against nonlinear Hilbert encoders.

Likewise, if for large `s`

\[
a e^{-C s^\beta}
\le
\phi(s)
\le
A e^{-c s^\beta}
\tag{18}
\]

with positive constants, then

\[
N_\phi(\delta)
\asymp
\left(\log\frac1\delta\right)^{1/\beta},
\]

so

\[
\boxed{
K^{\mathrm{opt}}_{\phi,H}(\delta)
\asymp
\left(\log\frac1\delta\right)^{1/(2\beta)}.
}
\tag{19}
\]

This matches the polylogarithmic order of the AF-475 coordinate upper bound.

The lower hypotheses in `(15)` and `(18)` are essential. An upper compressibility estimate alone cannot force a lower conditioning cost: the actual class may be much thinner than the envelope used to upper-bound it.

## Prior-art and novelty audit

The nonlinear metric ingredient is classical and was already audited in AF-464. In particular:

- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8, 103–105 (1969), DOI `10.1007/BF02589549`, introduced the cube/metric method behind this kind of nonlinear Hilbert obstruction.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665–678 (2020), DOI `10.4007/annals.2020.192.2.8`, gives the modern exact metric-type framework used in AF-464.
- Ronald A. DeVore, **“Nonlinear approximation,”** *Acta Numerica* 7, 51–150 (1998), DOI `10.1017/S0962492900002816`, is the approximation-class background for encoding source regularity through best-term decay, as already used in AF-475.

No novelty is claimed for Enflo type, Hamming-cube distortion, or approximation classes. The line-specific result is the exact construction `(8)` placing a dimension-`k` metric cube inside `C_phi` at tail mass `delta/2`, and the resulting match between the **inverse profile scale** and the best possible resolution-dependent Hilbert conditioning. This closes the explicit minimax-sharpness question left open by AF-475 for regular profiles.

No new source class or external theorem beyond the literature already audited in AF-464 and AF-475 is required, so the existing source ledger is sufficient for this finding.

## Boundary and falsification audit

- **The lower bound is for stable fidelity, not injectivity.** A nonlinear map may remain one-to-one while its inverse modulus deteriorates like `sqrt(k)`.
- **A controlled upper modulus is load-bearing.** The normalization `Lip(F)<=1` is without loss only when distortion is measured by the ratio of upper and lower moduli. Arbitrarily steep encoders can amplify the tail cube by paying the same sensitivity elsewhere.
- **The theorem needs actual cube vertices in the admitted source class.** It applies to the full envelope class `C_phi`; a narrower arithmetic subclass may exclude these independent private-tail switches and have substantially better conditioning.
- **The lower bound uses `0<delta<=1`.** This keeps the common head at least as heavy as every private tail atom and gives the exact tail formula `(9)`. The high-resolution regime `delta->0` relevant to AF-475 is fully covered.
- **Finite alphabets cap the certificate.** The construction needs `2k+1` distinct atoms. The arithmetic prime alphabet has no such cutoff.
- **For arbitrary discontinuous profiles, `(7)` need not match the achieved bound `(14)` by a universal constant.** The sharp-order conclusions `(17)` and `(19)` use regular two-sided decay.
- **A one-sided upper tail law does not imply the minimax lower rates.** To infer `(16)` or `(19)` for a concrete source family, one must show that comparable tail breadth is actually realizable, not merely that every source is bounded above by a decay envelope.
- **The source metric is `d_1`.** A different arithmetic, Wasserstein, Hellinger, phase, or provenance metric changes the cube geometry and requires its own audit.
- **No rational-prime discriminator is created by the obstruction.** The theorem prices how much Hilbert compression can preserve from a source family; it does not identify which retained relation distinguishes rational primes from matched controls.

## Arithmetic-fidelity consequence

AF-475 suggested computing an arithmetic compressibility profile and evaluating the coordinate condition curve at the downstream discrimination scale. AF-476 adds the converse question: **how much independent tail breadth is genuinely realizable inside the arithmetic source class at that same scale?**

If a prime-derived family contains the head-plus-private-tail cubes `(8)`, or a comparable metric cube of dimension `k(delta)`, then every Lipschitz Hilbert representation must pay at least `sqrt(k(delta))` inverse conditioning at resolution `delta`. Fast profile decay helps only because it limits how many independent switches can carry enough total mass to remain visible at that resolution.

This gives a sharper source-side program. For a concrete arithmetic carrier, determine both an upper approximation profile and a lower realizable-complexity profile. If they match, the compression cost is pinned from both sides. If they differ, the gap itself identifies the missing arithmetic rigidity: the source may be much thinner than its best-term envelope because number-theoretic relations forbid the generic private-tail degrees of freedom used by `(8)`.

That distinction is exactly what a prime-specific fidelity theory needs. The generic envelope says how much information **could** hide below compression; the arithmetic realization question says how much of that hidden freedom the rational-prime source actually possesses.