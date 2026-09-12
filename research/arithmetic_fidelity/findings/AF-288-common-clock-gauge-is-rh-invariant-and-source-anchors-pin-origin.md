# AF-288 — Common-clock gauge is RH-invariant, while multiplicatively independent source anchors pin its origin

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `TARGET-RELATIVE`, `GAUGE`, `SOURCE-CONSTRAINT`, `STABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-286 identifies an unknown common sampling-time offset as the coefficient-side gauge

\[
G_\tau:(a_n)_n\longmapsto (a_n n^{-i\tau})_n.
\]

For an ordinary Dirichlet series

\[
F(s)=\sum_{n\ge1}a_n n^{-s},
\]

this gauge is exactly vertical translation:

\[
F_{G_\tau a}(s)=F(s+i\tau).
\]

That elementary identity separates two logically different responses to missing clock provenance.

1. **Quotient the gauge when the downstream target is vertical-translation invariant.** If `F` has a meromorphic continuation, its zero/pole divisor is translated only in imaginary direction:
   \[
   \operatorname{Div}(F(\,\cdot+i\tau))
   =\operatorname{Div}(F)-i\tau.
   \]
   Hence every divisor target depending only on horizontal location is unchanged. In particular, for the Riemann zeta function the predicate
   \[
   \boxed{
   \text{all nontrivial zeros have }\operatorname{Re}\rho=\tfrac12
   }
   \]
   is constant on the complete common-clock orbit. An unknown common origin therefore does **not** need to be recovered merely to decide RH from an exact vertically translated zeta object.

2. **Pin the gauge when the source category itself supplies phase anchors.** Suppose two nonzero source coefficients at indices `m,n>=2` are known a priori and `m,n` are multiplicatively independent, equivalently
   \[
   \frac{\log m}{\log n}\notin\mathbb Q.
   \]
   Then the two observed phases
   \[
   e^{-i\tau\log m},\qquad e^{-i\tau\log n}
   \]
   determine `tau` uniquely on all of `\mathbb R`. For the canonical zeta coefficients on any fixed line `Re(s)=c>1`, the positive known anchors at `m=2` and `n=3` therefore fix the common clock origin exactly.

3. **Exact pinning is not global stable pinning.** The same two-anchor map has arbitrarily remote near-recurrences. There exists a sequence `|tau_j|->infinity` such that
   \[
   \left(e^{-i\tau_j\log m},e^{-i\tau_j\log n}\right)\longrightarrow(1,1).
   \]
   Thus no source-independent global modulus can bound clock displacement from noisy two-anchor phases over an unbounded timing range. A bounded timing prior restores ordinary compact inverse stability; on any interval of diameter at most `pi/log m`, the single `m`-anchor already obeys the explicit inverse-Lipschitz estimate
   \[
   |\tau-\tau'|
   \le
   \frac{\pi}{2\log m}
   \left|e^{-i\tau\log m}-e^{-i\tau'\log m}\right|.
   \]

So the `Theta(1/log N)` coefficient-fidelity calibration scale in AF-286--AF-287 is **not automatically the timing bill of every RH-facing target**. Common-mode timing uncertainty is target-relative: it is free for vertical-translation-invariant targets such as the RH horizontal-zero predicate, exactly removable when the source class contains sufficient phase provenance, and quantitatively costly only when the desired target really depends on the missing vertical origin.

## Vertical translation is the coefficient gauge

For every `s` in a half-plane where the Dirichlet series converges absolutely,

\[
\begin{aligned}
F_{G_\tau a}(s)
&=\sum_{n\ge1}a_n n^{-i\tau}n^{-s}\\
&=\sum_{n\ge1}a_n n^{-(s+i\tau)}\\
&=F(s+i\tau).
\end{aligned}
\]

By uniqueness of analytic continuation, if `F` extends meromorphically to a vertically translation-stable domain, the same identity holds throughout the common continuation domain.

If `rho` is a zero of `F` of multiplicity `k`, then

\[
F_{G_\tau a}(\rho-i\tau)=F(\rho)=0
\]

with the same multiplicity, and conversely every zero arises this way. The same statement holds for poles. Therefore

\[
Z(F_{G_\tau a})=Z(F)-i\tau,
\qquad
P(F_{G_\tau a})=P(F)-i\tau,
\]

including multiplicities.

The real-part multiset is consequently invariant:

\[
\{\!\{\operatorname{Re}\rho:\rho\in Z(F)\}\!\}
=
\{\!\{\operatorname{Re}\rho:\rho\in Z(F_{G_\tau a})\}\!\}.
\]

Any exact target that factors through this horizontal divisor data descends through the common-clock quotient. Examples include membership in a fixed vertical strip, the supremal horizontal displacement of zeros from a declared line, and the yes/no statement that all designated nontrivial zeros lie on `Re(s)=1/2`.

This does **not** make every zero statistic gauge-invariant. Exact ordinates, the height of a first zero, counts inside a fixed vertical window, and any observable tied to an absolute imaginary origin change under the shift. Likewise, `zeta(s+i\tau)` does not retain the standard zeta functional equation with its original vertical origin unchanged; the symmetry is transported together with the gauge. The invariant conclusion here is specifically about horizontal zero geometry, not canonical normalization of the whole completed object.

## Two multiplicatively independent anchors give exact global identifiability

Assume the source category declares nonzero reference coefficients `a_m,a_n` at two indices `m,n`. After coefficient recovery modulo the common offset, the corresponding normalized phase ratios are

\[
u_m(\tau)=\frac{(G_\tau a)_m}{a_m}=e^{-i\tau\log m},
\qquad
u_n(\tau)=\frac{(G_\tau a)_n}{a_n}=e^{-i\tau\log n}.
\]

Suppose two offsets `tau,tau'` produce the same pair. Put `delta=tau-tau'`. Then

\[
e^{-i\delta\log m}=e^{-i\delta\log n}=1.
\]

Hence there are integers `k,l` with

\[
\delta\log m=2\pi k,
\qquad
\delta\log n=2\pi l.
\]

If `delta` is nonzero, then `k,l` are nonzero and

\[
\frac{\log m}{\log n}=\frac{k}{l}\in\mathbb Q,
\]

contradicting multiplicative independence. Thus `delta=0` and

\[
\boxed{\tau=\tau'.}
\]

For `m=2,n=3`, rational dependence would imply `2^l=3^k`, impossible by unique factorization. Therefore two canonical zeta coefficients are enough to remove the exact common-clock ambiguity when the source prior is allowed to be used.

This sharpens AF-286's boundary condition. The gauge nonidentifiability there is exact for an arbitrary complex coefficient class closed under `G_tau`; it is not an unconditional obstruction for a narrower arithmetic source class. Once the source itself fixes two multiplicatively independent coefficient phases, the orbit intersects that source normalization in at most one point.

## Exact identifiability does not imply uniform global calibration

The two-anchor inverse is globally unique but globally ill-conditioned. Set

\[
\alpha=\frac{\log n}{\log m}\notin\mathbb Q
\]

and choose

\[
\tau_q=\frac{2\pi q}{\log m},
\qquad q\in\mathbb N.
\]

Then the first anchor returns exactly to its starting phase:

\[
e^{-i\tau_q\log m}=1,
\]

while the second becomes

\[
e^{-i\tau_q\log n}=e^{-2\pi i q\alpha}.
\]

By the classical Kronecker approximation/equidistribution theorem for irrational rotations, there is a sequence `q_j->infinity` with

\[
q_j\alpha\pmod 1\longrightarrow0.
\]

Therefore

\[
\left(e^{-i\tau_{q_j}\log m},e^{-i\tau_{q_j}\log n}\right)
\longrightarrow(1,1)
\]

although `tau_{q_j}->infinity`.

Consequently there is no function `omega(epsilon)<infinity`, valid for the whole real line, such that anchor-pair discrepancy at most `epsilon` forces

\[
|\tau-\tau'|\le\omega(\epsilon).
\]

In Arithmetic Fidelity language, the exact quotient fiber is trivial after two anchors, but its inverse conditioning over the unbounded orbit is still singular. Source provenance removes exact aliases without supplying a global robust modulus.

A bounded timing prior changes the problem. If `tau,tau'` lie in an interval of diameter at most `pi/log m`, then

\[
0\le \frac{|\tau-\tau'|\log m}{2}\le\frac\pi2
\]

and

\[
\left|e^{-i\tau\log m}-e^{-i\tau'\log m}\right|
=2\sin\!\left(\frac{|\tau-\tau'|\log m}{2}\right).
\]

Using `sin x >= 2x/pi` on `[0,pi/2]` gives

\[
\boxed{
|\tau-\tau'|
\le
\frac{\pi}{2\log m}
\left|e^{-i\tau\log m}-e^{-i\tau'\log m}\right|.
}
\]

Thus one anchor already gives a quantitative local clock chart once the allowed orbit segment is shorter than a half turn. The second anchor is needed for global exact uniqueness, not for local conditioning around a known clock window.

## RH consequence is target-relative, not a new RH criterion

Apply the vertical-translation statement to

\[
\zeta_\tau(s):=\zeta(s+i\tau).
\]

Its nontrivial zeros are precisely

\[
\rho_\tau=\rho-i\tau,
\]

where `rho` runs over the nontrivial zeros of `zeta`, with multiplicity. Therefore

\[
\operatorname{Re}\rho_\tau=\operatorname{Re}\rho.
\]

It follows immediately that

\[
\boxed{
\zeta \text{ satisfies RH}
\iff
\zeta(\,\cdot+i\tau) \text{ has every shifted nontrivial zero on }\operatorname{Re}s=\tfrac12
}
\]

for every real `tau`.

This is not a new equivalent criterion for RH; it is a quotient statement about acquisition provenance. If an exact analytic carrier is known only up to common vertical translation, the missing clock origin does not erase the discriminator that RH asks about. A mechanism that insists on recovering absolute zero heights or exact coefficient phases before asking the RH yes/no question may therefore be retaining more provenance than the final target requires.

Independent rowwise jitter from AF-287 is different. There is generally no single `tau` for which the perturbed observations equal one vertical translate of the source, so the divisor need not move rigidly in imaginary direction. The present result removes only the **common-mode** timing gauge from the RH information bill; it does not make arbitrary timing perturbations harmless.

## Prior art and novelty assessment

No novelty is claimed for vertical translations of Dirichlet series, irrational torus recurrence, or the invariance of real parts under vertical translation.

G. H. Hardy and Marcel Riesz, *The General Theory of Dirichlet's Series*, Cambridge Tracts in Mathematics and Mathematical Physics 18 (Cambridge University Press, 1915), is the classical general-Dirichlet-series background already relevant to AF-286. Modern Bohr-transform treatments likewise identify vertical translation with multiplicative phase rotation of Dirichlet coefficients; see Andreas Defant, Domingo García, Manuel Maestre, and Pablo Sevilla-Peris, *Dirichlet Series and Holomorphic Functions in High Dimensions* (Cambridge University Press, 2019), especially the Bohr-vision discussion connecting prime coordinates and Kronecker approximation.

The recurrence argument is an immediate specialization of the classical Kronecker theorem: an irrational rotation has arbitrarily close returns to the identity. The proof above needs only the irrationality of `log n/log m`, which for multiplicatively independent integers follows directly from unique factorization.

The retained Arithmetic Fidelity content is the **target/source split** applied to the timing obstruction created in AF-286 and quantitatively closed in AF-287. Common-clock uncertainty has three different statuses depending on what is retained: it is an exact gauge on arbitrary complex coefficient sources, it is pinned by arithmetic phase anchors in a constrained source class, and it disappears entirely after quotienting to horizontal zero geometry such as the RH predicate. Treating all three as one coefficient-recovery problem overprices the required provenance.

## Boundaries and failure modes

- The vertical-translation identity assumes the frequency system is the ordinary Dirichlet system `log n`. General Dirichlet series have the analogous action `a_n -> a_n e^{-i tau lambda_n}`.
- The divisor statement requires a meromorphic continuation on the translated domain. No continuation theorem is proved here.
- RH invariance concerns the horizontal location of the shifted nontrivial zero set. It does not preserve absolute zero ordinates, fixed-height windows, or the standard completed-zeta normalization without transporting the vertical origin as well.
- Exact two-anchor calibration assumes the reference coefficients and their phases are genuinely known and nonzero. If they are themselves unknown, estimated, or only known modulo another symmetry, the argument does not pin the gauge.
- Multiplicative independence is essential for global uniqueness. If `m^r=n^s` for nonzero integers `r,s`, the two phase periods have a common nonzero clock period.
- Global exact uniqueness is not robust over unbounded `tau`; Kronecker recurrence makes remote offsets arbitrarily hard to distinguish from finite-precision anchor phases.
- The displayed local inverse modulus uses a bounded clock interval. Its constant is not a global Diophantine bound and should not be extrapolated to arbitrary offsets.
- The result does not weaken AF-287's `Theta(1/log N)` requirement for recovering an arbitrary `N`-coefficient vector under adversarial rowwise jitter. It only shows that coefficient-level timing fidelity is stronger than necessary for some downstream targets and some constrained sources.
- No new zero-free region, zero-density estimate, simplicity result, critical-line proportion, or proof of RH follows.

## Decisive audit test

When a proposed RH mechanism treats timing or phase provenance as mandatory side information, first classify the target under the common-clock action.

If the target is constant on

\[
F(s)\mapsto F(s+i\tau),
\]

then common clock origin should be quotiented out rather than reconstructed. For zero-divisor targets, test whether only real parts matter or whether absolute ordinates enter essentially.

If the target is not gauge-invariant, inspect the declared source class before charging the full AF-286 coefficient-calibration bill. Known phases at two multiplicatively independent coefficient indices remove the exact ambiguity; a bounded clock prior can also turn a single anchor into a stable local chart. Only after those source constraints are exhausted should missing common-clock provenance be treated as an irreducible lift.

Finally separate exact and stable recovery. Two anchors have singleton exact fibers but no global uniform inverse modulus on an unbounded clock orbit. Any quantitative use must therefore state a timing range, a Diophantine condition, additional anchors, or another source regularity that supplies the required conditioning.

## Consequence for the research line

The common-clock branch opened in AF-286 is now target-classified. **At the RH yes/no level, common clock origin is not an information bottleneck:** vertical translation preserves every zero real part, so the RH discriminator descends exactly to the gauge quotient. If absolute phase provenance is needed by an intermediate mechanism, the canonical zeta source already contains multiplicatively independent coefficient anchors that pin the origin exactly, although robust global calibration still requires a bounded timing range or quantitative recurrence control.

This removes a false universal timing requirement from the finite-prefix acquisition story. The next useful timing questions are narrower: which intermediate RH mechanisms genuinely depend on absolute imaginary origin rather than horizontal zero geometry; which source constraints make that dependence stably recoverable; and how independent, non-common-mode timing errors propagate through those target-specific quotients.