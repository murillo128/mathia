# PL-227 — LCM-conditioned Bost–Connes KMS states collapse to the profinite-zero gauge state

## Claim

The most canonical **state-level** normalization of the shrinking Bost–Connes divisibility corners left open by `PL-225` and `PL-226` has a nonzero weak-* limit, but the limit erases all temperature and cyclotomic arithmetic information.

Let

\[
\mathcal A_{BC}=C^*(\mathbb Q/\mathbb Z)\rtimes\mathbb N^\times,
\qquad
\mathcal D=C^*(\mathbb Q/\mathbb Z)\cong C(\widehat{\mathbb Z}),
\]

let `E:A_BC -> D` be the prime-gauge expectation from `PL-219`, and put

\[
P_m:=\mu_m\mu_m^*.
\]

For any real `beta>0`, any Bost--Connes `KMS_beta` state `phi`, and any `m>=1`, define the normalized corner state

\[
\psi_{\phi,m}(x)
:=\frac{\phi(P_m x P_m)}{\phi(P_m)}
=m^\beta\phi(P_m x P_m),
\]

using the exact KMS mass `phi(P_m)=m^{-beta}`.

Now take the canonical divisibility-cofinal sequence

\[
L_N:=\operatorname{lcm}(1,2,\ldots,N).
\]

Then for **every** choice of inverse temperatures `beta_N>0` and every choice of corresponding `KMS_(beta_N)` states `phi_N`,

\[
\boxed{
\psi_{\phi_N,L_N}\xrightarrow[N\to\infty]{w^*}
\omega_0:=\delta_0\circ E,
}
\]

where `delta_0` is evaluation at the zero point of `Zhat`. Equivalently, on every cyclotomic character,

\[
\boxed{\omega_0(e(r))=1\qquad(r\in\mathbb Q/\mathbb Z),}
\]

while every nonzero prime-gauge degree has expectation zero.

The convergence is stronger than a fixed-temperature statement: the temperatures may vary arbitrarily with `N`, may cross `1`, may pass through `1/2`, and the low-temperature extremal KMS state may vary with `N`. The full divisibility conditioning removes all of that information.

Moreover,

\[
\omega_0(P_n)=1\qquad(n\ge1),
\]

so `omega_0` is not a `KMS_beta` state for any finite `beta>0`, because every such KMS state must satisfy `phi(P_n)=n^{-beta}`. Thus the nonzero normalized tail exists only by leaving the equilibrium family and collapsing onto a boundary state that contains no Riemann-zero selector.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

No analytic continuation of zeta is used anywhere in this finding.

## 1. The lcm sequence is the correct all-exponent exhaustion

The primorial sequence increases the support of an exponent vector but keeps each included exponent equal to one. That is insufficient to kill an arbitrary rational cyclotomic phase: a denominator containing `p^k` with `k>1` need not divide a square-free primorial.

The lcm sequence instead has

\[
v_p(L_N)=\max\{k:p^k\le N\}=\lfloor\log_p N\rfloor,
\]

so for every fixed prime `p`,

\[
v_p(L_N)\longrightarrow\infty.
\]

Equivalently, every fixed positive integer `q` divides `L_N` for all `N>=q`. In the profinite completion this is exactly

\[
L_N\longrightarrow0\quad\text{in }\widehat{\mathbb Z}.
\]

Hence `L_N` is a canonical exponent-lattice exhaustion that goes to infinity in every fixed prime coordinate while tending to the profinite zero under the arithmetic diagonal compactification.

The proof below works for any net `(m_i)` such that every fixed integer divides `m_i` eventually. `L_N` is simply the canonical one-parameter choice.

## 2. Corner conditioning transports a cyclotomic character by multiplication by `m`

The standard Bost--Connes covariance gives

\[
\mu_m^*e(r)\mu_m=e(mr).
\]

Therefore

\[
\begin{aligned}
P_m e(r)P_m
&=\mu_m\mu_m^*e(r)\mu_m\mu_m^*\\
&=\mu_m e(mr)\mu_m^*\\
&=\rho_m(e(mr)).
\end{aligned}
\]

By the KMS corner identity already used in `PL-224`,

\[
\phi(\rho_m(e(s)))=m^{-\beta}\phi(e(s)),
\]

so the normalized state satisfies the exact formula

\[
\boxed{
\psi_{\phi,m}(e(r))=\phi(e(mr)).
}
\]

This identity is valid for every real `beta>0` and every `KMS_beta` state. It does not use the low-temperature Gibbs trace and therefore does not cross a phase-transition or continuation boundary.

Now fix `r=a/q in Q/Z`. Once `q|L_N`,

\[
L_Nr=0\quad\text{in }\mathbb Q/\mathbb Z,
\]

and hence, **exactly rather than asymptotically**,

\[
\psi_{\phi_N,L_N}(e(r))
=\phi_N(e(0))
=1.
\]

Thus every fixed cyclotomic Fourier mode is eventually sent to its value at the profinite zero, uniformly over the temperature and over the choice of KMS state.

## 3. Gauge invariance upgrades the character calculation to the full C*-algebra

Every Bost--Connes KMS state is invariant under the full prime-gauge torus by `PL-219`. The projection `P_m` is itself gauge invariant. Therefore each conditioned state is gauge invariant:

\[
\psi_{\phi,m}\circ\gamma_z=\psi_{\phi,m}.
\]

Averaging over the gauge torus gives

\[
\boxed{
\psi_{\phi,m}=\psi_{\phi,m}\circ E.
}
\]

On the diagonal `D`, finite linear combinations of the characters `e(r)` are norm dense. The previous section says that for every such finite trigonometric polynomial `d`,

\[
\psi_{\phi_N,L_N}(d)=d(0)
\]

for all sufficiently large `N`, independently of `beta_N` and `phi_N`. Since all states have norm one, density yields

\[
\psi_{\phi_N,L_N}|_{\mathcal D}
\xrightarrow{w^*}
\delta_0.
\]

For arbitrary `x in A_BC`,

\[
\psi_{\phi_N,L_N}(x)
=\psi_{\phi_N,L_N}(E(x))
\longrightarrow
\delta_0(E(x)).
\]

Hence

\[
\boxed{
\psi_{\phi_N,L_N}\xrightarrow{w^*}\delta_0\circ E.
}
\]

This is a full-algebra weak-* theorem, not merely convergence on the algebraic core.

## 4. The limit destroys both KMS temperature and cyclotomic arithmetic

The support projections themselves lie in the diagonal. Using the standard Bost--Connes relation

\[
P_n=\rho_n(1)
=\frac1n\sum_{ns=0}e(s),
\]

we obtain

\[
\omega_0(P_n)
=\frac1n\sum_{ns=0}\delta_0(e(s))
=1.
\]

Thus the limiting state regards every fixed divisibility corner as full mass. By contrast, every finite-temperature KMS state satisfies

\[
\phi_\beta(P_n)=n^{-\beta}<1
\qquad(n>1).
\]

So `omega_0` cannot be a finite-temperature KMS state. The normalization has not produced a new equilibrium completion of the Bost--Connes phase diagram; it has left that family.

The cyclotomic arithmetic collapses just as sharply. Low-temperature extremal KMS states distinguish arithmetic symmetry data through their values on `e(r)`. High-temperature states have their own divisor/exponential formulas there. Under lcm conditioning all of these values become

\[
e(r)\longmapsto1.
\]

Hence the limiting state forgets the Galois label, the phase-transition sector, the inverse temperature, and the nontrivial rational phase itself.

In particular there is no special behavior at `beta=1/2`. The same limit is obtained if `beta_N` is constantly `1/2`, constantly any other positive number, or varies arbitrarily with `N`.

## 5. Relation to PL-224--PL-226

`PL-224` proves that finite cyclotomic corner products collapse to one lcm corner. `PL-225` shows that the unnormalized all-prime corner net collapses strongly to zero in the standard positive-energy representation. `PL-226` then proves that no scalar renormalization of the associated KMS-GNS vectors yields a nonzero norm limit.

A distinct natural escape remains after those results: instead of trying to renormalize the operator or its GNS vector, normalize the **positive functional supported on each shrinking corner** and take a weak-* limit of states. This is a genuinely different topology and, unlike the vector renormalization of `PL-226`, it does produce a nonzero limit.

The present theorem classifies that limit for the canonical full-divisibility exhaustion. The answer is nevertheless negative for the RH program:

\[
\boxed{
\text{normalized lcm conditioning}
\longrightarrow
\text{profinite-zero gauge state},
}
\]

with complete loss of the KMS and cyclotomic data that made the Bost--Connes system arithmetic.

Therefore a surviving infinite-prime Bost--Connes route cannot consist merely of conditioning on increasingly deep divisibility corners and renormalizing their mass. It must use a genuinely relative/noncommuting observable, modular or trace relation, additive/Mobius target, adelic quotient, or another source-forced coupling that does not collapse under the same cofinal-divisibility test.

## 6. Prior-art and novelty audit

The Bost--Connes algebra, its cyclotomic diagonal `C*(Q/Z) ~= C(Zhat)`, the semigroup isometries, the KMS relation `phi(P_m)=m^{-beta}`, the profinite/finite-adele model, and the KMS phase structure are classical. Source 5 in `research/prime_lattice/SOURCES.md` remains the primary literature anchor. `PL-219`, `PL-224`, `PL-225`, and `PL-226` already audit the specific gauge, corner, weak-completion, and KMS-GNS ingredients used here.

A targeted literature audit around Bost--Connes KMS corners, finite-adele/profinite measure models, induced/corner KMS states, primitive ideals, and boundary constructions found no basis for a novelty claim for the ingredients or for the idea of studying corner-supported states. The exact cofinal-lcm convergence lemma above should therefore be treated as an elementary derived consequence of the classical system.

The durable Mathia delta is narrower: it closes a live state-level normalization escape left after the operator/GNS negatives `PL-225` and `PL-226`, and it identifies the exact information-loss endpoint. No theorem novelty is claimed.

The limit is also structurally non-RH-selective. Its proof uses only gauge invariance, the KMS scaling of divisibility projections, and the torsion fact that every rational phase has finite order. The Riemann zero divisor, the functional equation, and analytic continuation do not enter.

## 7. Boundaries and adversarial controls

**Weak-* convergence of states is not operator convergence.** The theorem does not claim that the normalized operators `L_N^beta P_(L_N)` converge in any operator topology; `PL-226` shows why the corresponding GNS scaling is badly behaved.

**The limit is not a KMS continuation.** `omega_0` violates the finite-temperature KMS projection law and should not be interpreted as a state at `beta=0`, `1/2`, `1`, or infinity.

**Cofinal prime powers are essential for the cyclotomic collapse.** A square-free primorial tail does not annihilate every rational character, because denominators may contain arbitrarily high fixed prime powers. The lcm sequence, or an equivalent divisibility-cofinal net, is the correct test.

**The theorem does not classify arbitrary counterterms or relative modular objects.** One may insert phase-dependent observables before conditioning, compare two conditioned states, take logarithmic derivatives, or use unbounded weights. Those are new constructions and require separate canonicity and matched-control tests.

**The profinite zero is arithmetic but not zero-sensitive.** Reaching `0 in Zhat` uses exact rational divisibility and therefore is not merely an arbitrary Beurling relabeling. But the resulting state has forgotten the nontrivial arithmetic phase data rather than converted it into a Riemann-zero constraint.

## Falsification / audit tests

The finding would require correction or narrowing if any of the following failed:

1. every Bost--Connes `KMS_beta` state with `beta>0` did not satisfy `phi(P_m)=m^{-beta}`;
2. `mu_m^* e(r) mu_m=e(mr)` failed;
3. the KMS corner identity did not give `phi(rho_m(e(s)))=m^{-beta}phi(e(s))`;
4. KMS states were not invariant under the full prime-gauge action used in `PL-219`;
5. every fixed denominator `q` did not divide `L_N=lcm(1,...,N)` eventually;
6. the characters `e(r)` were not norm dense in the cyclotomic diagonal; or
7. `delta_0(E(P_n))` were not equal to one.

All seven checks are exact and independent of RH.

## Consequence for `prime_lattice`

The canonical all-prime Bost--Connes tail now has three sharply different but jointly negative completions. Unnormalized corners vanish strongly (`PL-225`); scalar-renormalized KMS-GNS vectors have no nonzero norm limit (`PL-226`); and normalized corner **states** do converge weak-* but collapse to the temperature-independent profinite-zero gauge state (`PL-227`).

This removes a broad class of “renormalize the shrinking divisibility tail” proposals without touching genuinely relative, noncommuting, additive, or Weil-sensitive constructions. Any further Bost--Connes use of the exponent lattice must preserve some arithmetic observable through the infinite-prime limit rather than merely force every fixed divisibility condition and cyclotomic phase into its trivial value.