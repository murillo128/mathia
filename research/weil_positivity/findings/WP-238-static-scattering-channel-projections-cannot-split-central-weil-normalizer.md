# WP-238 — Static scattering-channel projections cannot split the central Weil normalizer

**Status:** `EXACT-DERIVED + MAASS-SELBERG-POSITIVE-CONTROL + CENTRAL-NORMALIZER-NO-GO + SPHERICAL-MULTIPLICITY-ONE + DECISIVE-NARROWING + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-237` closes the most literal Arthur-height escape suggested by `CLUE-maass-selberg-remainder-sign-interface`: height variation acts only on the boundary part of the positive Maaß–Selberg family and cannot resolve the `T`-independent explicit-formula block into its zero, finite-prime, archimedean, and polar constituents. The accepted clue deliberately leaves a deeper possibility open: perhaps an **orthogonal decomposition of the continuous spectral Hilbert space before scalarization** can isolate a positive component whose scalar distribution is the Weil zero form.

For the ordinary `SL(2)` scattering architecture used by Wong, there is a second exact obstruction one level earlier. The `L`-function-bearing part of the global intertwining operator is already a **central scalar normalizing factor** before the trace is taken. In Wong's notation the global intertwiner factors schematically as

\[
M(\eta,s)=m(\eta,s)\,R(\eta,s),
\tag{1}
\]

where `m(eta,s)` is the scalar quotient of completed `L`-functions and `R(eta,s)` is the normalized intertwining operator assembled from the local normalized factors. On every regular point,

\[
\boxed{
M(\eta,s)^{-1}M'(\eta,s)
=
\frac{m'(\eta,s)}{m(\eta,s)}I
+
R(\eta,s)^{-1}R'(\eta,s).
}
\tag{2}
\]

The entire scalar explicit-formula channel is therefore proportional to the identity on the representation fiber. A fixed orthogonal **reducing channel projection** can change which representation channels are retained, but it cannot split the arithmetic constituents inside `m'/m`: every retained channel receives the same scalar logarithmic derivative. In the classical Riemann-zeta spherical specialization the obstruction is stronger still. The relevant `K`-fixed principal-series line is one-dimensional, so the only fiberwise orthogonal projections are `0` and `I`.

The nontrivial-zero term, the Mangoldt prime-power term, the Gamma term, and the polar terms are not separate operator eigenspaces hidden inside (2). They appear only **after** the scalar logarithmic derivative has been converted into a Weil explicit formula by analytic continuation, contour displacement, the functional equation, and the Euler expansion in its convergence half-plane. Consequently an ordinary static channel decomposition made after the global scalar normalizer has formed is too late to provide the sign-preserving projection sought by the clue.

This does not rule out a genuinely new projection/compression that changes the scattering evolution itself, a moving spectral subbundle with connection terms, a non-spherical or multi-cusp matrix normalizer with richer global structure, or a finite–archimedean construction acting before the scalar normalizing factor is formed. It rules out the narrower but canonical proposal that the already-positive Maaß–Selberg continuous spectrum secretly contains orthogonal **static scattering channels** corresponding separately to the zeta zero divisor and its explicit-formula companions.

## 1. Wong's `L`-function channel is central before the explicit formula is taken

The bounded cross-line read authorized by `CLUE-maass-selberg-remainder-sign-interface`, namely `PL-253` at revision `ff734900b636e6ab0e0e06e70a813682d18fea05`, identifies the positive object correctly: Arthur truncation gives an `L^2` inner product of truncated Eisenstein series, while the logarithmic derivative of the scattering/intertwining normalizer enters the continuous spectral term. The primary source is Tian An Wong, *Explicit formulas for the spectral side of the trace formula of SL(2)*, Acta Arith. 195 (2020), 149–175, arXiv:1608.02296.

In Wong's general principal-series setup the unnormalized global intertwining operator is separated into a scalar normalizing factor built from completed Hecke `L`-functions and a normalized operator assembled from local normalized intertwiners. Suppressing tensor-product notation that is irrelevant to the present algebra gives (1). Since the scalar factor commutes with every operator on the fiber, differentiating immediately yields (2).

This same separation is visible directly on the spectral side. The logarithmic derivative of the global scalar normalizer contributes a term of the form

\[
\frac{m'(\eta,s)}{m(\eta,s)}
\operatorname{tr}\rho(f,\eta,s),
\tag{3}
\]

while the normalized intertwiner contributes separately through a trace involving `R^{-1}R'`. Wong explicitly identifies the scalar-normalizer term as the one whose `L`-function logarithmic derivative is converted to the Riemann–Weil explicit formula.

For the classical spherical quotient relevant to zeta, the formula becomes especially transparent:

\[
\boxed{
m(s)=\frac{\xi(s)}{\xi(1+s)},
}
\tag{4}
\]

in Wong's trace-formula parameter. His Theorem 1.1 rewrites the distribution built from `m'/m` as a sum involving the nontrivial zeros of `zeta`, the von Mangoldt terms, the real-place Gamma contribution, and the elementary/polar terms. Thus the desired arithmetic pieces have already been merged into one scalar meromorphic function **before** the explicit-formula decomposition exposes them again.

## 2. A fixed reducing channel projection retains the whole scalar normalizer

Let `H_s` be a representation fiber on which (1) acts, and let

\[
P:H_s\to H_s,
\qquad P=P^*=P^2,
\tag{5}
\]

be a fixed orthogonal projection defining a genuine scattering channel. To interpret `PH_s` as an independent component of the same scattering system, require the usual reducing condition for the normalized evolution on the spectral interval under consideration,

\[
PR(\eta,s)=R(\eta,s)P.
\tag{6}
\]

Then the restricted intertwiner is

\[
M_P(\eta,s)
=
P M(\eta,s)|_{PH_s}
=
m(\eta,s)R_P(\eta,s),
\tag{7}
\]

and therefore

\[
\boxed{
M_P^{-1}M_P'
=
\frac{m'}m I_{PH_s}+R_P^{-1}R_P'.
}
\tag{8}
\]

Nothing about the choice of a nonzero reducing channel changes the scalar factor. In particular, if a linear spectral readout takes a trace against a positive test operator on `PH_s`, the scalar part always has the form

\[
\frac{m'}m\,w_P(s),
\qquad
w_P(s)=\operatorname{tr}_{PH_s}(\text{channel test operator}),
\tag{9}
\]

with the **same `m'/m` multiplying the whole channel weight**.

This is the exact sense in which channel projection has rank one on the arithmetic decomposition: it can alter the multiplicity/test weight attached to the scalar normalizer, or annihilate the channel entirely, but it has no operator coordinate that distinguishes a zero contribution from a prime contribution or a Gamma contribution inside `m'/m`.

Equation (8) is independent of positivity. It is simply centrality. Positivity enters in the Maaß–Selberg theorem that supplies the nonnegative truncated `L^2` form. The important logical point is that the positive theorem does not manufacture additional eigenspaces inside the scalar normalizer. Therefore orthogonally decomposing the already-formed scattering fiber cannot make the zero-divisor part inherit a sign that the full scalar logarithmic derivative did not have.

## 3. Zeros, primes, Gamma, and poles arise by analytic decomposition, not Hilbert-space decomposition

Write the scalar-normalizer distribution schematically, in the zeta specialization, as

\[
D_m(g)
:=-\frac1{4\pi}
\int_{\mathbb R}
\frac{m'}m(ir)\,\widehat g(ir)\,dr.
\tag{10}
\]

Wong's explicit-formula calculation gives

\[
\boxed{
D_m(g)
=
W(g)+P_{\rm fin}(g)+A_\infty(g)+C_{\rm pol}(g),
}
\tag{11}
\]

where `W` is the nontrivial-zero functional and the remaining symbols denote the finite-prime, archimedean, and polar/evaluation contributions in the chosen normalization.

The right side of (11) is not obtained by first decomposing the continuous spectral Hilbert space as

\[
H=H_{\rm zeros}\oplus H_{\rm primes}\oplus H_\infty\oplus H_{\rm pol}.
\tag{12}
\]

No such decomposition occurs in the source. Instead the pieces arise from different terms in the analytic treatment of **one scalar meromorphic logarithmic derivative**. The zeros enter as residues when a contour is displaced; the prime powers enter by the Euler expansion in the half-plane of absolute convergence; Gamma and conductor/polar terms enter through completion, the functional equation, and the archimedean logarithmic derivative.

Therefore a fixed channel projector `P` applied before taking the trace does not become four different coefficients on the four terms of (11). It first produces a channel-weighted version of the same scalar object, as in (9), and only afterwards can an explicit-formula calculation decompose that new scalar distribution. If the channel weight changes the test transform, it changes the **entire** explicit-formula distribution associated with that test; it does not reveal a pre-existing Hilbert subspace whose trace is `W(g)` while the prime/Gamma terms lie in an orthogonal complement.

This distinguishes the present obstruction from `WP-237`. There the deficient coordinate was the external Arthur height `T`: every arithmetic constituent occupied the same constant `T` mode. Here the deficient coordinate is an internal static scattering-channel label: every retained channel sees the same central scalar normalizer. Both failures are rank-one phenomena, but at different structural levels.

## 4. The Riemann-zeta spherical channel has no nontrivial fiberwise projection at all

The `SL(2)(Z)` zeta specialization is stronger than the general centrality statement. Wong works on the spherical continuous spectrum, and the principal-series `K`-fixed subspace is one-dimensional. This is standard spherical representation theory: a spherical principal series has a unique `K`-fixed vector up to scalar.

Hence, at every regular spectral parameter,

\[
\dim H_s^K=1,
\qquad
\operatorname{Proj}(H_s^K)=\{0,I\}.
\tag{13}
\]

There is no nontrivial orthogonal channel split available inside the exact scalar zeta channel. Keeping the spherical line keeps `m'/m`; removing it removes `m'/m`.

One can of course decompose the **direct integral over spectral parameter** by a measurable set `A`, giving multiplication by `1_A(r)`. That is a spectral-window projection, not a multiplicity/channel decomposition at fixed `r`. It merely replaces the test transform in (10) by a windowed transform. A hard window is generally outside the smooth Paley–Wiener/Mellin class used in the explicit formula; a smoothed spectral multiplier is an admissible new test only when the corresponding analytic/support conditions are proved. Either way it weights the scalar normalizer as a whole. It does not identify zeros, primes, Gamma, and poles with orthogonal scattering channels.

This matters for the research mandate because Weil positivity quantifies over a full admissible positive-type test class. A test-dependent or target-engineered spectral window that happens to suppress some explicit-formula terms for selected tests would not be an independently positive fixed geometric form on that class.

## 5. Matched control: the obstruction is structural, not zeta-specific

Replace the arithmetic normalizer by any nonzero scalar meromorphic scattering factor `a(s)` and write

\[
M_a(s)=a(s)R(s).
\tag{14}
\]

Then for every fixed reducing channel,

\[
(M_a)_P^{-1}(M_a)_P'
=
\frac{a'}a I_{PH_s}+R_P^{-1}R_P'.
\tag{15}
\]

The same inability to split constituents of `a'/a` holds whether `a` contains zeta, another automorphic `L`-function, a finite Blaschke product, or an unrelated scalar scattering determinant. Thus the no-go does not derive arithmetic rigidity from positivity. It says that **central scalarization has erased the channel coordinate one would need to perform the proposed projection**.

This is a useful matched control against a false Mathia-specific success. Seeing the full completed zeta in a positive global scattering system is exceptional arithmetically, as `WP-024` already emphasized; but once that information has been compressed into a scalar normalizer, ordinary channel orthogonality cannot decide which analytic terms of its logarithmic derivative should inherit positivity.

## 6. Aggressive falsification and exact scope

Several apparent escapes do not contradict the claim because they change the construction being tested.

**Non-spherical multiplicity does not by itself help.** A higher-dimensional representation fiber can have many reducing projections, but the factor `(m'/m)I` remains central on every one. Such projections may change the normalized-intertwiner term `R^{-1}R'`; they do not split the analytic constituents of the same scalar `m`.

**Changing the character `eta` changes the `L`-function.** Decomposing the automorphic spectrum into different Hecke-character sectors can produce different normalizing factors `m(eta,s)`. That is useful representation theory, but it is not a zero-versus-prime-versus-Gamma decomposition of the Riemann-zeta normalizer inside one fixed `eta` sector.

**A moving projector is a new connection problem.** If `P=P(s)` varies with spectral parameter and one differentiates a moving compressed evolution rather than simply restricting (2), terms involving `P'(s)` or a Berry/Grassmannian connection can appear. The present result does not rule that out. Such terms are additional geometric data, however, and their sign is not inherited automatically from the central scalar factor or from the static orthogonal decomposition. `WP-186` is already a warning that signed phase derivatives can reappear precisely when one leaves pointwise projector positivity.

**A non-reducing compression is not an orthogonal decomposition.** If `P` does not reduce `R`, forming an effective operator on `PH` can introduce Schur/Feshbach self-energies and genuinely alter the scattering response. That is a different candidate mechanism. It must derive its compression canonically from Mathia and prove an independent sign theorem; the present no-go does not prejudge it.

**Multiple cusps or genuinely matrix-valued global normalizers remain open.** A system whose global arithmetic normalizer is itself matrix/operator valued, with source-forced noncommuting finite and archimedean data before determinant/scalarization, could evade the centrality argument. Merely embedding the same scalar `m` as a diagonal block does not.

**Operations before global normalizer formation remain open.** The strongest surviving interpretation of the accepted clue is now to act before the local factors have collapsed into the scalar quotient `m`, or to change the local-to-global assembly so that finite-prime and archimedean sectors remain coupled operatorially when positivity is proved. This is exactly the kind of nonseparable pre-scalar geometry emphasized by `WP-234`--`WP-236`.

**Explicit-formula subtraction is not an escape.** Once (11) is known, one can algebraically subtract `P_fin+A_infty+C_pol` and isolate `W`. But unless those subtractions are themselves forced as independently signed geometric summands, this is the target-defined repackaging excluded by the branch mandate.

## 7. Prior-art and novelty audit

No novelty is claimed for normalized intertwining operators, their scalar `L`-function normalizing factors, the Arthur–Selberg continuous spectrum, spherical multiplicity one, or Wong's explicit-formula calculation. Wong's paper is the direct source for the factorization and for the separation of the scalar-normalizer and normalized-intertwiner contributions. Standard spherical representation theory gives the one-dimensionality of the `K`-fixed line; for a modern explicit statement in the `GL_n` principal-series setting see Peter Humphries, *Archimedean newform theory for GL_n*, J. Inst. Math. Jussieu 24 (2025), 41–116, DOI `10.1017/S1474748024000227`, whose spherical-representation discussion records that the `K`-fixed subspace is one-dimensional.

The relevant internal controls are distinct. `WP-024` already shows that modular scattering contains completed-zeta data but ordinary unitarity/Maaß–Selberg positivity does not imply Weil positivity. `WP-170`--`WP-186` audit passive and projective positive realizations of the **archimedean Gamma phase**. `WP-237` proves that **Arthur-height** filtering cannot resolve the explicit-formula block. None of those states the present channel-level obstruction: once the global `L`-function has entered the continuous spectrum as the central scalar normalizer `m`, a static reducing orthogonal decomposition has no operator coordinate with which to separate the analytic constituents later exposed by the explicit formula.

A bounded literature search found the expected classical sources for the factorization and spherical multiplicity-one statement, but no separate theorem advertised as this exact no-go. That absence is not a historical novelty proof. The substantive Mathia delta is the use of those standard facts as a **decisive falsifier of one specific surviving research interface** from the accepted Maaß–Selberg clue.

## Consequence for the research line

The Maaß–Selberg route has now failed two canonical projection coordinates for complementary reasons. Arthur-height variation is too coarse because the whole explicit distribution is `T`-independent (`WP-237`). Static scattering-channel decomposition is too coarse because the `L`-function-bearing response is already central and scalar before the explicit formula is taken (this finding).

The surviving obligation is correspondingly sharper. A viable construction must intervene **before central scalar normalizer formation**, or genuinely modify that formation through a source-forced non-reducing/moving/matrix-valued finite–archimedean mechanism with its own geometric sign theorem. Merely decomposing the existing positive truncated Eisenstein space into ordinary fixed scattering channels cannot turn Wong's lower bound into the global Weil positivity criterion.