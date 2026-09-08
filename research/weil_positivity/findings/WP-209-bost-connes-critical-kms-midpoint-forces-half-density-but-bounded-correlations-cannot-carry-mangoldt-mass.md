# WP-209 — Bost–Connes critical KMS midpoint forces the Weil half-density, but bounded correlations cannot carry Mangoldt mass

**Status:** `DERIVED + EXACT + PRIME-LATTICE-CROSS-LINE + BOST-CONNES-KMS + SOURCE-FORCED-HALF-DENSITY + POSITIVE-CORRELATION + MANGOLDT-MASS-OBSTRUCTION + MATCHED-CONTROL + PRIOR-ART-AUDITED + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`PL-220` exposes a genuinely new candidate carrier for the `weil_positivity` question. In the Bost–Connes system, every bounded self-adjoint equilibrium observable has a positive pure-point autocorrelation spectrum on the signed rational-log lattice, and KMS detailed balance relates the atoms at `log q` and `-log q`. Passing to the midpoint of the KMS strip makes that spectrum exactly symmetric. At the **source-selected Bost–Connes critical inverse temperature** `beta=1`, the midpoint inserts precisely the factor

\[
q^{-1/2}.
\]

Thus Bost–Connes thermodynamic geometry supplies something that many earlier Mathia constructions did not: the critical half-density is not manually inserted and does not arise from a relabeling `s -> s-1/2`. It is the square root of the KMS detailed-balance Radon–Nikodym factor at the actual phase boundary.

The same calculation also gives a decisive obstruction. If a bounded Bost–Connes observable were to reproduce the exact finite-place Weil prime-power measure through this positive midpoint correlation, then its unsymmetrized positive spectral weights would have to satisfy

\[
c_{p^k}=\Lambda(p^k)=\log p.
\]

But every bounded correlation vector has finite total spectral mass,

\[
\sum_{q\in\mathbb Q_+^\times}c_q=\phi(X^*X)<\infty,
\]

whereas

\[
\sum_{p,k\ge1}\Lambda(p^k)=\infty.
\]

So the exact Mangoldt carrier is necessarily **non-normalizable** in the bounded GNS correlation geometry. Even the natural attempt to source the logarithm from the time generator fails: applying one energy derivative multiplies the `q`-atom by `log q`, and matching `Lambda(p^k)=log p` then requires `c_{p^k}=1/k`; already the prime subfamily requires `c_p=1`, again giving infinite total mass.

The resulting boundary is unusually sharp:

\[
\boxed{
\text{BC phase boundary }\beta=1
\; + \;
\text{KMS midpoint}
\Longrightarrow
q^{-1/2}\text{ canonically},
}
\]

but

\[
\boxed{
\text{bounded positive KMS correlation}
\not\Longrightarrow
\frac{\Lambda(n)}{\sqrt n}\text{ on all prime powers}.
}
\]

This does **not** kill the Bost–Connes route. It identifies what a surviving version must change: it must use an unbounded/affiliated observable, a distributional KMS vector, or a closable renormalized quadratic form whose positivity is proved independently. It must also derive prime-power support intrinsically and assemble the archimedean and polar sectors in the same sign theorem. A bounded equilibrium two-point function is now a matched control, not a global Weil bridge.

## 1. Positive Bost–Connes autocorrelations live on the rational-log lattice

Let `(A_BC,sigma)` be the rational Bost–Connes `C*`-dynamical system and let `phi_beta` be a `KMS_beta` state. `PL-220` proves that the physical flow is the dense one-parameter subgroup of the compact prime-gauge action,

\[
\sigma_t=\gamma_{z(t)},
\qquad
z_p(t)=p^{it}.
\tag{1}
\]

For bounded `X in A_BC`, its equilibrium autocorrelation

\[
C_X(t)
:=
\phi_\beta(X^*\sigma_t(X))
\tag{2}
\]

has an absolutely and uniformly convergent Fourier expansion

\[
\boxed{
C_X(t)
=
\sum_{q\in\mathbb Q_+^\times}
 c_q(X)q^{it},
\qquad
c_q(X)\ge0,
\qquad
\sum_qc_q(X)=\phi_\beta(X^*X)<\infty.
}
\tag{3}
\]

This is ordinary Hilbert-space positivity: in the GNS representation, `c_q(X)` is the squared norm of the `q`-gauge spectral component of `X Omega`.

For self-adjoint `X`, `PL-220` derives the KMS detailed-balance law

\[
\boxed{
c_{q^{-1}}(X)=q^{-\beta}c_q(X).
}
\tag{4}
\]

No zeta zero data or explicit-formula kernel is used in (3)--(4). They are source properties of the Bost–Connes equilibrium system.

## 2. The KMS midpoint canonically symmetrizes by a half Boltzmann factor

For an analytic element, evaluate the KMS correlation at the middle of its strip:

\[
C_X\!\left(t+\frac{i\beta}{2}\right)
=
\sum_q
q^{-\beta/2}c_q(X)q^{it}.
\tag{5}
\]

For a general bounded `X`, the same midpoint spectral measure is obtained by the standard KMS/GNS spectral calculus or by entire analytic approximation. Define

\[
s_q^{(\beta)}
:=
q^{-\beta/2}c_q(X).
\tag{6}
\]

Then (4) gives exactly

\[
\begin{aligned}
s_{q^{-1}}^{(\beta)}
&=(q^{-1})^{-\beta/2}c_{q^{-1}}(X)\\
&=q^{\beta/2}q^{-\beta}c_q(X)\\
&=s_q^{(\beta)}.
\end{aligned}
\tag{7}
\]

Hence the midpoint correlation has an **even positive** spectral measure on the signed logarithmic lattice. Pairing `q>1` with `q^{-1}` gives

\[
C_X\!\left(t+\frac{i\beta}{2}\right)
=
c_1(X)
+2\sum_{q>1}
q^{-\beta/2}c_q(X)\cos(t\log q),
\tag{8}
\]

with absolute convergence. The factor in (8) is not chosen to imitate a critical line; it is forced by KMS symmetry.

## 3. The actual Bost–Connes phase boundary selects the Weil exponent `1/2`

The thermodynamic boundary of the rational Bost–Connes system is

\[
\boxed{\beta_c=1.}
\tag{9}
\]

For `beta>1`, the canonical Gibbs representation has partition function `zeta(beta)`. At `0<beta<=1`, the Gibbs trace is no longer available and the canonical KMS continuation is the high-temperature type-`III_1` phase; `PL-213` records this boundary and its operator-algebraic interpretation.

Substituting (9) into (8) gives

\[
\boxed{
C_X\!\left(t+\frac i2\right)
=
c_1(X)
+2\sum_{q>1}
\frac{c_q(X)}{\sqrt q}
\cos(t\log q).
}
\tag{10}
\]

This is the exact half-density appearing in the finite-place Weil explicit-formula coefficients. In particular, the `1/2` here is **not** the inverse temperature `beta=1/2` rejected as non-distinguished by `PL-213`. It is half of the source-forced critical inverse temperature because the KMS midpoint takes the square root of detailed balance.

This distinction matters. The chain

\[
\boxed{
\text{BC phase transition }\beta_c=1
\longrightarrow
\text{KMS midpoint }\beta_c/2
\longrightarrow
q^{-1/2}
}
\tag{11}
\]

is intrinsic to the same arithmetic dynamical system. It survives the obvious matched deformation in the sense that changing the critical inverse temperature of a generic KMS system would change the exponent to `beta_c/2`; the rational Bost–Connes source itself is what fixes `beta_c=1`.

## 4. Exact Mangoldt weights make the positive correlation vector non-normalizable

The symmetric finite-place Weil measure, ignoring its eventual global sign orientation, is supported on prime powers with weights

\[
\nu_{\mathrm{fin}}
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\left(
\delta_{\log n}+\delta_{-\log n}
\right).
\tag{12}
\]

Suppose the midpoint positive measure (10) reproduced (12) exactly on positive frequencies. Since both have the same `n^{-1/2}` factor at `beta=1`, necessarily

\[
\boxed{
c_n(X)=\Lambda(n)
\quad(n\ge2).
}
\tag{13}
\]

In particular,

\[
c_{p^k}(X)=\log p
\qquad(p\text{ prime},\ k\ge1),
\tag{14}
\]

and all non-prime-power positive rational grades would have to vanish.

But (3) forces

\[
\sum_qc_q(X)<\infty.
\tag{15}
\]

Equation (13) contradicts (15) immediately. Indeed even the prime-power subseries has infinite mass:

\[
\sum_{p,k\ge1}\Lambda(p^k)=\infty.
\tag{16}
\]

No delicate zero-density or RH input is involved. The obstruction is simply the incompatibility between an exact all-prime Mangoldt distribution and a finite-norm GNS correlation vector.

There is an equivalent formulation directly at the symmetrized level. A bounded positive-definite correlation has a finite positive spectral measure, whereas

\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}=\infty.
\tag{17}
\]

For example, `n^{-1/2}>=n^{-1}` and the classical pole of `zeta(s)` at `s=1` gives divergence of `sum Lambda(n)/n`. Thus the exact finite Weil comb is a positive **locally finite/distributional** object, not the finite spectral measure of one bounded equilibrium vector.

This is stronger than saying that a convenient observable has not yet been found: no bounded `X in A_BC` can satisfy (13).

## 5. The canonical energy-derivative repair also has infinite GNS mass

A natural objection is that the Bost–Connes time generator already carries the logarithmic energy, so perhaps the positive coefficients `c_q` need not themselves equal `Lambda(q)`. Let `delta` denote the generator of the time evolution. On a homogeneous gauge component,

\[
\delta(X_q)=i(\log q)X_q.
\tag{18}
\]

Thus applying one frequency/energy derivative to the positive correlation multiplies its `q`-atom by `log q`. At the KMS midpoint and `beta=1`, the positive-frequency coefficient becomes

\[
\frac{(\log q)c_q(X)}{\sqrt q}.
\tag{19}
\]

To match the Weil coefficient at `q=p^k`, equation (19) requires

\[
(\log p^k)c_{p^k}(X)=\log p,
\]

hence

\[
\boxed{
c_{p^k}(X)=\frac1k.
}
\tag{20}
\]

This still contradicts finite spectral mass. Already the `k=1` subfamily gives

\[
\sum_pc_p(X)=\sum_p1=\infty.
\tag{21}
\]

So the most canonical way to source the logarithm from the Hamiltonian does not repair boundedness. It merely moves the non-normalizability from `log p` amplitudes to unit prime amplitudes.

This calculation is useful because it avoids a false dichotomy. The failure is not specifically that Mangoldt contains a logarithm that a correlation norm cannot know. The Bost–Connes derivation knows `log q` exactly. What fails is the attempt to realize the **infinite prime-power support with the required nondecaying underlying positive mass inside one bounded GNS vector**.

## 6. Aggressive falsification and exact scope

**Does this show that Bost–Connes cannot contribute to Weil positivity?** No. It rules out one precise and unusually natural architecture: a single bounded equilibrium two-point function, optionally with the canonical first energy derivative, whose KMS midpoint is identified termwise with the finite Weil prime-power carrier.

**Is the half-density itself a repackaged insertion?** No in this architecture. Equation (7) forces the square-root Boltzmann factor for every KMS system, and the Bost–Connes source independently fixes its thermodynamic boundary at `beta=1`. What is classical is the KMS mechanism, not the Mathia-specific observation that the actual Bost–Connes critical midpoint lands on the Weil exponent.

**Does `PL-213` already kill this because it says `1/2` is not selected?** No. `PL-213` rules out treating inverse temperature `beta=1/2` or the type-III modular scale as distinguished. Here the relevant number is `beta_c/2=1/2`, coming from the midpoint of the **distinguished boundary `beta_c=1`**. The mechanisms are different.

**Could mixed rational grades pay the mass cost?** Not for a positive autocorrelation measure. Every `c_q` is nonnegative, so adding mixed rational grades only increases the total mass. There is no cancellation available inside (3).

**Could one rescale the whole correlation by a finite constant?** No. A fixed amplification changes all coefficients by the same finite factor and cannot convert the divergent target mass into a finite one.

**Could truncation work?** Yes at every finite prime cutoff. One can choose finite spectral data with the desired coefficients and retain positivity. The obstruction is exactly the global limit. Any proposed limit must therefore state its domain and prove closability or distributional positivity rather than infer it from bounded-vector positivity at each cutoff.

**Could an unbounded affiliated observable work?** Logically yes. Equations (15)--(21) show that such an observable would have to leave the Hilbert-vector regime in precisely the direction needed by the target measure. This is now a concrete surviving test rather than a vague escape: construct a canonical unbounded `X` or quadratic form, prove a dense domain and independent positivity/closability theorem, and show that its KMS-symmetric spectral measure has exact prime-power support before adding the archimedean/polar sectors.

**Does the positive midpoint give the sign of the Weil form?** No. The finite prime term in the conventional Weil explicit formula enters with the opposite orientation from a bare positive measure, and global positivity depends on its assembly with the archimedean and polar pieces. The midpoint correlation supplies at most a positive carrier and a canonical half-density. A separate global sign theorem is still indispensable.

## 7. Prior-art and novelty boundary

No novelty is claimed for the Bost–Connes system, its phase transition, KMS states, spectral detailed balance, GNS positivity, or the Mangoldt coefficients in the explicit formula.

The Bost–Connes arithmetic dynamical system and its `zeta(beta)` partition function are classical and are already anchored in this line's `SOURCES.md` by Bost and Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411--457. `PL-213` audits the high-temperature type-`III_1` continuation and `PL-220` proves the compact-prime-gauge pure-point correlation decomposition and atomwise detailed balance used in (3)--(4).

The KMS midpoint symmetrization in (5)--(8) is the standard square-root detailed-balance transform. A directed literature search across Bost–Connes KMS correlations, detailed balance, midpoint symmetrization, Weil positivity, and critical half-densities found the classical ingredients but no reason to treat their combination here as a historical theorem. No historical novelty claim is made.

The durable Mathia-specific delta is the exact cross-line boundary:

\[
\boxed{
\text{source-forced BC criticality}
\Longrightarrow
\text{exact Weil half-density in a positive KMS midpoint carrier},
}
\tag{22}
\]

while

\[
\boxed{
\text{exact Mangoldt support in that carrier}
\Longrightarrow
\text{infinite GNS mass}.
}
\tag{23}
\]

This is neither another zeta representation nor a zero-defined spectrum. It identifies a genuinely intrinsic positive structure that reaches one required global normalization and then proves exactly where the bounded geometry fails.

## 8. Consequence for the research mandate

The Bost–Connes route deserves a narrower status than either "classicalized" or "promising bridge." The critical midpoint gives a **real source-forced success** absent from generic hand-built positive baths: `q^{-1/2}` follows from the actual arithmetic thermodynamic boundary and KMS symmetry. But bounded equilibrium positivity cannot carry the full Mangoldt comb, and the correlation geometry does not yet generate Gamma or the polar correction.

The next admissible Bost–Connes test is therefore not another bounded observable search. It is an unbounded/domain question:

\[
\boxed{
\text{Can a canonical affiliated or distributional BC observable define a closable KMS-symmetric positive form}
}
\]

whose midpoint spectral measure has exact prime-power support and whose necessary renormalization is supplied by the same finite--archimedean geometry rather than inserted by hand?

A negative theorem showing that every canonical closable KMS-symmetric form still has insufficient mass/support would close this route. A positive construction would still have to derive the archimedean Gamma and polar sectors and prove a global sign theorem independently of RH. Until then, `beta=1 -> beta/2=1/2` is a genuine clue from the geometry, not a Weil-positivity proof.
