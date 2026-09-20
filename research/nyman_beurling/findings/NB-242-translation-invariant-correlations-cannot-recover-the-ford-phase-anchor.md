# NB-242 — Translation-invariant correlations cannot recover the Ford phase anchor

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-BOUNDARY + ALL-ORDER-RELATIVE-CORRELATION + PHASE-ANCHOR-OBSTRUCTION + NB-240/NB-241-REFINEMENT + SOURCE-ONLY`.

`NB-240` showed that the published short-interval pair-correlation machinery is too coarse for the Ford packet, and `NB-241` sharpened the vertical side: first-order local tests need carrier-scale complexity `Theta(X/H)` to distinguish a half-period pair of matched packets. That left a genuine possibility open in `NB-241`: perhaps a **carrier-resolved two-point or higher-order statistic** could distinguish the packets even when a smooth first-order statistic cannot.

There is an exact obstruction to that route whenever the statistic remains internal to the zero configuration, meaning that it depends on ordinate **differences** but has no external phase anchor relative to the selected height `t`.

For the same half-period twins from `NB-241`, every translation-invariant `k`-point correlation statistic is **exactly identical for every `k` and every test resolution**, including tests oscillating at or above the Ford carrier. The complete autocorrelation measures coincide, so their Fourier transforms — the full power spectra — coincide at every frequency. Nevertheless the anchored Ford coefficient changes sign because a half carrier-period translation multiplies the one-point Fourier phase by `-1`; after the existing `Theta(J)` population and `1/J` residue normalization, the exact Ford contributions remain separated by order one.

Thus **carrier-scale resolution is necessary but not sufficient for correlation-based detectors**. A viable source theorem must also retain an **absolute anchor** tying each ordinate to `t` (or an equivalent arithmetic phase reference). Increasing the order of an unanchored spacing/correlation statistic, even without any bandwidth restriction, cannot recover the missing Ford phase.

## 1. The Ford twins and the missing coordinate

Retain the normalized Ford variables of `NB-241`,

\[
\tau:=H(\gamma-t),
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH,
\qquad
\omega:=\frac XH=YJ,
\tag{1}
\]

with `Y` bounded above and below by positive constants on the current diagonal. Fix a sufficiently small constant `delta>0`, put

\[
M:=\lfloor\delta J\rfloor,
\qquad
a:=\frac{2\pi}{\omega},
\qquad
h:=\frac a2=\frac{\pi}{\omega},
\tag{2}
\]

and define

\[
\mu_J
:=
\frac1M\sum_{j=0}^{M-1}\delta_{ja},
\qquad
\nu_J
:=
\frac1M\sum_{j=0}^{M-1}\delta_{ja+h}.
\tag{3}
\]

Thus `nu_J` is exactly the translate of `mu_J` by the half carrier period `h`. The two packets have the same population, the same common Ford depth, the same internal spacing, and the same packet diameter. Their physical translation is

\[
\frac hH
=
\frac{\pi}{X}
\asymp
\frac1R.
\tag{4}
\]

`NB-241` used this translation to prove a first-order resolution lower bound. The point here is different: **every statistic that quotients out common translation has discarded exactly the coordinate that the Ford carrier needs.**

## 2. Exact invariance of every relative `k`-point statistic

Let `k>=2`, and let `Phi` be any bounded measurable test on `R^(k-1)`. Define the relative `k`-point statistic

\[
\mathcal C_{k,\Phi}(\mu)
:=
\int_{\mathbb R^k}
\Phi(\tau_2-\tau_1,\ldots,\tau_k-\tau_1)
\,d\mu(\tau_1)\cdots d\mu(\tau_k).
\tag{5}
\]

The same statement holds if diagonal tuples are omitted, if the statistic is written as a sum over distinct atoms, or if `Phi` itself depends on `J` and oscillates on a moving scale.

### Lemma

For every finite `k>=2` and every admissible `Phi`,

\[
\boxed{
\mathcal C_{k,\Phi}(\nu_J)
=
\mathcal C_{k,\Phi}(\mu_J).
}
\tag{6}
\]

There is **no smoothness, bandwidth or derivative hypothesis** on `Phi`.

### Proof

Write `T_h mu` for translation of a measure by `h`. Under the change of variables

\[
\tau_i'=\tau_i+h,
\qquad 1\le i\le k,
\]

all relative coordinates are unchanged:

\[
\tau_i'-\tau_1'
=
\tau_i-\tau_1.
\tag{7}
\]

Therefore

\[
\mathcal C_{k,\Phi}(T_h\mu)
=
\mathcal C_{k,\Phi}(\mu).
\tag{8}
\]

Since `nu_J=T_h mu_J`, (6) follows. The same bijection preserves distinctness of tuples, so excluding diagonals does not change the conclusion. `square`

This is stronger than the first-order estimate in `NB-241`. There the two packets become distinguishable once the test reaches derivative scale `omega=YJ`. Here even a relative-coordinate test with arbitrarily high oscillation remains exactly blind, because resolution does not repair the quotient by common translation.

## 3. Full pair correlation knows the power spectrum, not the carrier phase

For the two-point case, the obstruction has a familiar harmonic form. Let

\[
\widetilde\mu(A):=\mu(-A)
\]

and define the autocorrelation measure

\[
\mathcal A_\mu:=\mu*\widetilde\mu.
\tag{9}
\]

A common translation cancels between the two factors, so

\[
\boxed{
\mathcal A_{\nu_J}=\mathcal A_{\mu_J}
}
\tag{10}
\]

**as measures**, not merely after testing them at one scale. Hence the two packets have identical pair-difference data at every separation.

With the Fourier convention

\[
\widehat\mu(\xi)
:=
\int e^{i\xi\tau}\,d\mu(\tau),
\]

we have

\[
\widehat{\mathcal A_\mu}(\xi)
=
|\widehat\mu(\xi)|^2.
\tag{11}
\]

Translation by `h` changes only Fourier phase:

\[
\widehat\nu_J(\xi)
=
e^{i\xi h}\widehat\mu_J(\xi),
\qquad
|\widehat\nu_J(\xi)|
=
|\widehat\mu_J(\xi)|.
\tag{12}
\]

At the Ford carrier,

\[
\omega h=\pi,
\]

and the lattice in (3) gives

\[
\widehat\mu_J(\omega)=1,
\qquad
\widehat\nu_J(\omega)=-1.
\tag{13}
\]

Thus even **complete carrier-frequency autocorrelation data** supplies

\[
|\widehat\mu_J(\omega)|^2
=
|\widehat\nu_J(\omega)|^2
=1,
\tag{14}
\]

while the signed one-point coefficient needed by the Ford residue differs by `2`.

This is the precise phase loss. A carrier-retuned pair statistic can detect that a coherent lattice exists, but without an external origin it cannot tell whether that lattice sits on the `+1` or `-1` carrier phase.

## 4. Depth conditioning and higher correlation order do not restore the anchor

The obstruction is not removed by recording Ford depth. Give the `j`-th atom an arbitrary mark `d_j` and translate the ordinate while carrying the mark with the atom:

\[
(\tau_j,d_j)
\longmapsto
(\tau_j+h,d_j).
\tag{15}
\]

Any marked statistic built from the depths and relative ordinates,

\[
\Phi(
 d_{j_1},\ldots,d_{j_k};
 \tau_{j_2}-\tau_{j_1},\ldots,
 \tau_{j_k}-\tau_{j_1}
),
\tag{16}
\]

is still unchanged exactly. In particular, restricting every point to the same bounded critical Ford layer does not break the symmetry.

Nor does increasing `k`. Equation (6) holds separately for every finite order, and in fact the conclusion is simply the group symmetry of the complete relative configuration: all internal distances and all relative tuples are preserved by a common translation. An arbitrarily rich hierarchy of translation-invariant spacing statistics can at best reconstruct the packet **modulo translation**. The Ford observable is not translation-invariant, so that quotient is one dimension too aggressive.

This sharpens the open escape recorded in `NB-241`. A nonlinear two-point or higher-order theorem may still be useful, but **its usefulness cannot come solely from resolving more internal zero geometry**. It must retain some absolute phase information relative to the selected height or import a zeta-specific relation that fixes that phase indirectly.

## 5. The exact Ford residue still separates the matched controls

The phase ambiguity is not a harmless gauge for the source observable. For a common bounded Ford depth `d`, the transition contribution has the form already isolated in `NB-241`,

\[
\mathcal R
=
\frac{e^{-r-d}}{J}
\sum_j
F(\tau_j)e^{i\omega\tau_j},
\tag{17}
\]

with `F(0)>0` and `F` continuous. Choose `delta` in (2) small enough that both twin packets lie in a fixed patch where

\[
\Re F(\tau)\ge\frac34F(0).
\tag{18}
\]

On `mu_J` every carrier phase is `+1`; on `nu_J` every carrier phase is `-1`. Exactly as in the matched-control estimate of `NB-241`, this gives

\[
\boxed{
\liminf_{J\to\infty}
|\mathcal R_{\mu_J}-\mathcal R_{\nu_J}|
\ge
\frac32\,\delta F(0)e^{-r-d}
>0.
}
\tag{19}
\]

Combining (6) with (19) produces the decisive mismatch:

\[
\boxed{
\text{all finite-order unanchored correlation data agree exactly,}
\quad
\text{while the Ford residue differs by order one.}
}
\tag{20}
\]

Unlike the resolution bound in `NB-241`, this statement does not disappear when the correlation test is retuned to frequency `omega`. It is a phase-anchor obstruction rather than a bandwidth obstruction.

## 6. Consequence for pair-correlation routes after NB-240

`NB-240` concluded that a useful two-point theorem must be local in height, conditioned in Ford depth, and retuned from mean-zero spacing to the carrier scale `1/R`. The present result adds a fourth requirement.

A standard difference statistic contains factors of the form

\[
e^{iX(\gamma_j-\gamma_k)}
=
e^{i\omega(\tau_j-\tau_k)}.
\tag{21}
\]

For both twins this relative phase is identical. What the source residue needs instead is the anchored factor

\[
e^{iX(\gamma_j-t)}
=
e^{i\omega\tau_j}.
\tag{22}
\]

The distinction is not semantic. Equation (21) is invariant under

\[
\gamma_j\mapsto\gamma_j+\frac\pi X
\quad\text{for all }j
\]

up to the corresponding common phase cancellation between the two points, whereas (22) changes sign under that half-period translation.

Therefore the viable target is not merely “carrier-scale pair correlation.” It must be **carrier-scale and anchored**: for example an estimate of the signed local zero current itself, a mixed correlation with a fixed external phase reference, or a theorem that couples the packet to an arithmetic object whose phase relative to `t` is known. The `R^{-1} zeta'/zeta` observable isolated in `NB-237` already has exactly this anchored one-point character.

## 7. Prior-art and representation audit

The generic mechanism is classical. Autocorrelation determines Fourier magnitude but loses Fourier phase; translation is one of the standard ambiguities in Fourier phase retrieval. Modern surveys such as Grohs--Koppensteiner--Rathmair, *Phase Retrieval: Uniqueness and Stability* (SIAM Review 62, 2020), treat the general magnitude-only problem, while the homometry/autocorrelation literature studies configurations with identical difference data. No novelty is claimed for the identities (8)--(12).

Likewise, classical Montgomery pair correlation and its modern refinements study ordinate differences. The fresh short-interval theorem audited in `NB-240` changes the height range and admits more horizontal information, but its pair coordinate remains internal to the zero configuration. The present finding does not need any theorem from that literature for its proof.

The line-local contribution is the specialization of this classical phase-loss symmetry to the exact Ford currencies:

\[
h=\frac\pi\omega
=
\frac{\pi H}{X},
\qquad
\frac hH=\frac\pi X\asymp\frac1R,
\tag{23}
\]

combined with the `Theta(J)` critical population and `1/J` residue normalization that turn a mere translation ambiguity into the order-one source separation (19). This materially strengthens the frontier after `NB-241`: **resolution and correlation order cannot substitute for an absolute phase anchor.**

A targeted prior-art search covered Fourier phase retrieval/autocorrelation, homometric point sets, classical and recent zeta pair-correlation work, and higher correlation/spacing statistics. The generic translation ambiguity is standard; the search did not locate a zeta theorem that supplies the missing deterministic, Ford-depth-conditioned absolute carrier phase for the local zero current. Since no external theorem is load-bearing in the proof, no new durable `SOURCES.md` anchor is required.

Representation audit: the invariance lemma is completely non-arithmetic. Zeta enters through the already established Ford carrier, the critical packet scaling and the fact that the desired source coefficient is anchored to `t`. Consequently this is a source-side information boundary, not a theorem about the actual occurrence of such packets and not a new bound on the Nyman--Beurling approximation distance.

## 8. Adversarial review and falsification boundary

Several qualifications are essential.

First, the theorem concerns **translation-invariant** correlation statistics. A two-point statistic with an explicit dependence on an absolute coordinate — for example on `tau_1` itself, on the center of mass, or on the phase relative to `t` — breaks the symmetry and is not covered by (6). That is precisely the escape identified here.

Second, a finite observation window can itself act as an anchor through boundary effects. The matched packets are chosen inside an arbitrarily small fixed interior patch of the Ford window, with margin larger than the half-period shift. Hard inclusion in that window is therefore identical for the two controls. A smooth height envelope that varies on the carrier scale can distinguish them, but such an envelope is already an anchored carrier-scale observable rather than a pure internal correlation. If the envelope varies only subcarrier-fast, the first-order estimate of `NB-241` makes its effect asymptotically negligible.

Third, the exact equality of relative statistics does not assert that either packet can occur as the zero set of `zeta`. A zeta-specific theorem may forbid the packets by an arithmetic mechanism not encoded by internal correlations. Such a theorem would evade the obstruction and would be precisely the kind of new source input the line seeks.

Fourth, the all-order statement applies to statistics formed from simultaneous translation-invariant tuples. It does not say that every conceivable nonlinear functional of a point configuration is blind; a functional may secretly encode an origin or another external reference.

Fifth, the order-one separation uses the same source profile and diagonal Ford regime as `NB-241`. If a future representation changes the carrier, profile or normalization, the phase-anchor calculation must be redone for that exact observable.

A decisive falsification would be a statistic expressible purely through the marked relative coordinates (16), invariant under common translation, that takes different values on the explicitly translated twins. Equation (8) rules this out identically. What remains open is whether actual zeta structure yields an anchored microlocal cancellation estimate, or fixes the absolute packet phase through another arithmetic relation.

## 9. Consequence for the live frontier

The source-side target is now narrower than the one left by `NB-240`--`NB-241`. A future zero theorem must preserve four pieces of information simultaneously: the selected Ford height window, the near-one depth mark, ordinate resolution at `Theta(1/R)`, and an **absolute phase anchor relative to `t`**. The first three without the fourth still admit the exact half-period twins.

Equivalently, an internal spacing theorem can certify that a carrier-scale coherent clump exists but cannot determine the sign/phase with which that clump enters the logarithmic-derivative current. The missing information is one-point or externally anchored, not another order of unanchored correlation.

This removes a broad apparent escape from `NB-241`: simply upgrading from first-order statistics to arbitrarily detailed pair or higher relative correlations does not solve the Ford transition. The next useful source result must either estimate the anchored `R^{-1} zeta'/zeta` current directly or supply a genuinely zeta-specific mechanism that pins the carrier phase of every admissible critical clump.