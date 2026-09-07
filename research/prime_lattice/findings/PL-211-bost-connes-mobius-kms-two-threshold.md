# PL-211 — Bost–Connes Möbius KMS geometry separates the half-support threshold from parity coherence

## Claim

The source-forced arithmetic escape left after `PL-210` can be tested inside the canonical Bost–Connes divisibility algebra without manufacturing prime channels. Its range projections satisfy exact multiplicative relations forced by integer divisibility, and they admit a canonical finite-prime observable whose diagonal values are precisely the Möbius sign with the squareful states killed.

That test produces **two different thresholds**:

- `beta=1/2` is exactly the threshold at which the global square-free support has nonzero KMS `L^2` mass;
- `beta=1` is the threshold above which the alternating Möbius orientation itself becomes coherent as an `L^2` limit.

More precisely, let `S_n` denote the Bost–Connes multiplicative isometry and put

\[
E_n=S_nS_n^*.
\]

For a finite set `F` of rational primes define

\[
Q_p=1-2E_p+E_{p^2},
\qquad
M_F=\prod_{p\in F}Q_p.
\]

In the standard divisibility representation, `Q_p` has values `1,-1,0` according as `v_p(n)=0,1,>=2`, so `M_F` is the finite-coordinate Möbius observable. For every `KMS_beta` state `phi_beta`, `beta>0`, the KMS relation and the exact prime-divisibility projection relations give

\[
\phi_\beta(E_n)=n^{-\beta},
\]

and consequently

\[
\boxed{
\phi_\beta(M_F)=\prod_{p\in F}(1-p^{-\beta})^2,
\qquad
\|M_F\|_{2,\phi_\beta}^2
=\phi_\beta(M_F^2)
=\prod_{p\in F}(1-p^{-2\beta}).
}
\]

Thus the `1/2` boundary is a second-moment/square-free-support threshold. It is already present before any zero divisor, analytic continuation, functional equation, or phase-sensitive Möbius cancellation enters. In fact it is unchanged if the `-1` Möbius phase at each prime is replaced by an arbitrary unimodular prime phase while the same square-free support is retained.

For the actual Möbius phase, the finite observables behave as follows when `F` exhausts the primes:

\[
\begin{array}{ll}
0<\beta\le 1/2:& M_F\to0\quad\text{in KMS }L^2,\\[2mm]
1/2<\beta\le1:& \|M_F\|_2\to\zeta(2\beta)^{-1/2}>0,
\quad\text{but }(M_F)\text{ is not }L^2\text{-Cauchy},\\[2mm]
\beta>1:& M_F\text{ is }L^2\text{-Cauchy and converges to a nonzero Möbius vector.}
\end{array}
\]

In the low-temperature Gibbs region `beta>1`, the limit has

\[
\|M_\infty\|_2^2=\frac1{\zeta(2\beta)},
\qquad
\phi_\beta(M_\infty)=\frac1{\zeta(\beta)^2}.
\]

By contrast, for every `0<beta<=1`, the finite KMS expectations satisfy

\[
\phi_\beta(M_F)\longrightarrow0.
\]

At `beta=1/2` this is incompatible with interpreting the KMS continuation as analytic continuation of the Gibbs Möbius expectation: the analytically continued scalar `1/zeta(1/2)^2` is finite and nonzero, whereas the canonical finite-prime KMS observable converges to zero in `L^2`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION` for the route

\[
\text{canonical Bost--Connes divisibility law}
+\text{KMS continuation}
+\text{Möbius prime orientation}
\longrightarrow
\text{RH-sensitive critical-line mechanism}.
\]

The negative is deliberately restricted to this canonical finite-prime Möbius/KMS completion. It does not rule out other Bost–Connes observables, adelic/Weil completions, target-relative constructions, or arithmetic operators that import genuinely phase-sensitive global data before the KMS averaging.

## 1. The local observable is forced by the exponent lattice

The Bost–Connes semigroup already realizes the exponent lattice through

\[
S_mS_n=S_{mn},
\qquad
\sigma_t(S_n)=n^{it}S_n.
\]

Its range projection `E_n=S_nS_n^*` is the projection onto the divisibility sector `n|m` in the standard `ell^2(N)` representation. For distinct primes the range projections satisfy the source-forced coprime law

\[
E_{p^a}E_{q^b}=E_{p^a q^b},
\]

and for one prime they are nested,

\[
E_{p^a}E_{p^b}=E_{p^{\max(a,b)}}.
\]

Therefore the polynomial

\[
Q_p=1-2E_p+E_{p^2}
\]

is not an arbitrary label attached to the prime direction. On the exponent coordinate `v_p` it evaluates exactly as

\[
Q_p(v_p)=
\begin{cases}
1,&v_p=0,\\
-1,&v_p=1,\\
0,&v_p\ge2.
\end{cases}
\]

Hence, for finite `F`,

\[
M_F=\prod_{p\in F}Q_p
\]

reads the Möbius orientation on those prime coordinates and kills a state as soon as one of the inspected coordinates contains a square. For every fixed integer `n`, enlarging `F` eventually gives the ordinary value `mu(n)` in the standard diagonal representation.

The key algebraic identity is

\[
\boxed{Q_p^2=1-E_{p^2}.}
\]

Thus the square of the oriented observable forgets the sign completely and becomes the local square-free-support projection. For finite `F`,

\[
M_F^2=\prod_{p\in F}(1-E_{p^2}).
\]

This exact support/orientation separation is what generates the two different thresholds below.

## 2. KMS gives exact multiplicative moments at every temperature

The time evolution makes every `S_n` analytic and

\[
\sigma_{i\beta}(S_n)=n^{-\beta}S_n.
\]

For any `KMS_beta` state, the KMS identity therefore gives

\[
\begin{aligned}
\phi_\beta(E_n)
&=\phi_\beta(S_nS_n^*)\\
&=\phi_\beta(S_n^*\sigma_{i\beta}(S_n))\\
&=n^{-\beta}\phi_\beta(S_n^*S_n)\\
&=n^{-\beta}.
\end{aligned}
\]

This calculation is independent of the symmetry breaking for `beta>1`: although the Bost–Connes system has many extremal KMS states there, all of them have the same moments on these divisibility range projections.

Because products belonging to distinct prime coordinates collapse to the corresponding integer divisibility projection, the KMS expectation factorizes exactly on every finite family of such local polynomials. In particular,

\[
\phi_\beta(Q_p)
=1-2p^{-\beta}+p^{-2\beta}
=(1-p^{-\beta})^2,
\]

and

\[
\phi_\beta(Q_p^2)=1-p^{-2\beta}.
\]

Multiplying over `F` proves the two boxed formulas in the claim.

This is a genuinely arithmetic cross-prime law in the narrow sense demanded after `PL-210`: the relations are forced by ordinary integer divisibility rather than by freely chosen finite-rank labels. The calculation therefore tests a source-forced family that the programmable controls of `PL-208`--`PL-210` do not themselves supply.

## 3. The critical half is exactly a square-free-support threshold

Let `F_P={p:p<=P}`. From

\[
\|M_{F_P}\|_2^2
=\prod_{p\le P}(1-p^{-2\beta})
\]

and the standard convergence criterion for prime Euler products,

\[
\sum_p p^{-2\beta}
\begin{cases}
=\infty,&0<\beta\le1/2,\\
<\infty,&\beta>1/2,
\end{cases}
\]

we obtain

\[
\|M_{F_P}\|_2^2\longrightarrow
\begin{cases}
0,&0<\beta\le1/2,\\[1mm]
\zeta(2\beta)^{-1},&\beta>1/2.
\end{cases}
\]

Equivalently, the decreasing square-free projections

\[
S_{F_P}=M_{F_P}^2
=\prod_{p\le P}(1-E_{p^2})
\]

have a nonzero limiting KMS mass exactly when `beta>1/2`.

The reason this cannot by itself be an RH mechanism is visible before any further analysis: the number `1/2` entered only through the **second moment** `p^{-2 beta}`. The sign orientation has disappeared from `M_F^2`.

There is an exact phase-blind matched control. For arbitrary `omega_p in T`, define

\[
Q_{p,\omega}
=1+(\omega_p-1)E_p-\omega_p E_{p^2}.
\]

It takes the values `1,omega_p,0` for `v_p=0,1,>=2`. Therefore

\[
Q_{p,\omega}^*Q_{p,\omega}=1-E_{p^2}
\]

for every unimodular phase. Every such prime-phase orientation has the **same** `beta=1/2` norm threshold. The half boundary is consequently support information, not a discriminator selecting the Möbius orientation or the untwisted Riemann zeta function.

This is the Bost–Connes analogue of the information boundary already seen from a different direction in `PL-021`: standard Bohr `H^2` also singles out `1/2` through square summability of the square-free Möbius coefficient vector. The present calculation is not a repeat of that Hardy-space fact, because it uses the canonical arithmetic KMS state and exact divisibility projections; what repeats is the diagnosis that the bare half-threshold is an `L^2` support phenomenon.

## 4. Möbius orientation stays incoherent until `beta>1`

The nonzero norm for `beta>1/2` does not mean that the oriented observables converge. Take `P<Q` and write

\[
T_{P,Q}=\{p:P<p\le Q\}.
\]

Because the prime blocks factor under the KMS moments,

\[
\begin{aligned}
\|M_{F_Q}-M_{F_P}\|_2^2
&=A_P\bigl(1+A_{P,Q}-2B_{P,Q}\bigr),\\
A_P&=\prod_{p\le P}(1-p^{-2\beta}),\\
A_{P,Q}&=\prod_{P<p\le Q}(1-p^{-2\beta}),\\
B_{P,Q}&=\prod_{P<p\le Q}(1-p^{-\beta})^2.
\end{aligned}
\]

If `1/2<beta<=1`, then `A_P` converges to the positive number

\[
A_\infty=\zeta(2\beta)^{-1},
\]

but for every fixed `P`,

\[
B_{P,Q}\longrightarrow0
\qquad(Q\to\infty),
\]

because `sum_p p^{-beta}` diverges throughout that range. Also

\[
A_{P,Q}\longrightarrow A_\infty/A_P.
\]

Hence, taking `Q->infinity` and then `P->infinity`,

\[
\|M_{F_Q}-M_{F_P}\|_2^2\longrightarrow2A_\infty>0.
\]

So the net is not `L^2`-Cauchy anywhere in `1/2<beta<=1`. The square-free sector has positive mass, but infinitely many occupied prime coordinates continue to flip the total parity.

For `beta>1`, both prime sums

\[
\sum_p p^{-\beta},
\qquad
\sum_p p^{-2\beta}
\]

converge. The tail products `A_{P,Q}` and `B_{P,Q}` then tend uniformly to `1` as `P->infinity`, so the displayed distance tends to zero. Thus the finite Möbius observables converge in the GNS `L^2` space precisely in the ordinary Euler-product/Gibbs region `beta>1`.

The two thresholds have different meanings:

\[
\boxed{
\beta=1/2:\ \text{square-free support survives in second moment},
\qquad
\beta=1:\ \text{global Möbius parity becomes coherent}.}
\]

The first is phase blind; the second is controlled by the first-order prime occupation sum and coincides with the established Bost–Connes thermodynamic/Euler-product boundary tracked in `PL-024`.

## 5. The high-temperature KMS state does not analytically continue the Möbius Euler expectation

When `beta>1`, the ordinary Gibbs representation is available. The normalized Gibbs expectation of the limiting diagonal Möbius observable is

\[
\begin{aligned}
\phi_\beta(M_\infty)
&=\frac1{\zeta(\beta)}
  \sum_{n\ge1}\mu(n)n^{-\beta}\\
&=\frac1{\zeta(\beta)^2},
\end{aligned}
\]

and

\[
\|M_\infty\|_2^2
=\frac1{\zeta(\beta)}
  \sum_{n\ge1}\mu(n)^2n^{-\beta}
=\frac1{\zeta(2\beta)}.
\]

These are ordinary absolutely convergent Dirichlet/Euler identities. No continuation has been used.

For `0<beta<=1`, the Bost–Connes KMS formalism still supplies equilibrium states, but the finite-prime expectations obey

\[
\phi_\beta(M_{F_P})
=\prod_{p\le P}(1-p^{-\beta})^2
\longrightarrow0.
\]

At `beta=1/2`, meanwhile, the meromorphic continuation of the scalar function `1/zeta(beta)^2` is finite and nonzero because `zeta(1/2) != 0`. Therefore

\[
\boxed{
\lim_{P\to\infty}\phi_{1/2}(M_{F_P})=0
\neq
\frac1{\zeta(1/2)^2}.}
\]

Even more strongly, `M_{F_P}->0` in the KMS `L^2` norm at that temperature.

This is the analytic-continuation boundary required by the research contract. The high-temperature KMS extension is mathematically meaningful, but it is **not** analytic continuation of the Möbius Gibbs expectation. One cannot pass from the identity valid for `beta>1` to the critical strip by replacing the non-trace-class Gibbs state with the KMS state and keeping the same scalar Euler interpretation.

## 6. Prior art and novelty audit

The ambient ingredients are classical. The Bost–Connes system, its multiplicative isometries, time evolution, zeta partition function, KMS phase transition, and arithmetic symmetry are already registered in `research/prime_lattice/SOURCES.md` via Bost--Connes (1995). `PL-024` already records the exact log-prime covariance and the fact that KMS states below `beta=1` are not an analytic continuation of the ordinary partition trace.

A literature cross-check against Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proc. Amer. Math. Soc.* **130** (2002), 2999--3003, DOI `10.1090/S0002-9939-02-06449-3`, confirms the classical product-measure picture behind the finite-prime calculation: the canonical adelic KMS measure factorizes over rational primes and the high-temperature uniqueness boundary is `beta=1`. The exact formulas above do not require importing Neshveyev's ergodicity theorem; they follow directly from the KMS identity and the divisibility projection relations.

A targeted novelty search around Bost--Connes Möbius observables, square-free projections, KMS moments, and `zeta(2 beta)` did not expose a standard theorem stated as the two-threshold result above. Absence of a search hit is **not** used as novelty evidence. No novelty is claimed for the Euler products, the Bost--Connes algebra, or the KMS state structure. The durable delta is the line-specific matched control: once `PL-210` demands a source-forced cross-prime arithmetic relation, the most canonical divisibility/Möbius relation still separates `1/2` into phase-blind support mass while genuine parity coherence remains at the ordinary `beta=1` Euler boundary.

## 7. Adversarial boundaries

**This is not a no-go theorem for Bost–Connes and RH.** The Bost–Connes observable algebra contains much richer arithmetic information, and known RH-equivalent inequalities can be hosted inside related quantum-statistical formulations. The negative concerns the specific idea that the canonical divisibility projections plus the KMS continuation of the finite Möbius orientation already convert `1/2` into a zero-localizing mechanism.

**The `1/2` threshold is real, not dismissed as accidental.** The square-free-support projection has positive KMS mass exactly for `beta>1/2`. What the matched phase control proves is that this threshold is insensitive to the orientation whose cancellation is relevant to `1/zeta`; therefore the existence of the threshold alone does not distinguish Riemann arithmetic from arbitrary prime-phase orientations.

**Nonconvergence for `1/2<beta<=1` does not say that no weaker or renormalized limit exists.** Distributional, target-relative, martingale-renormalized, or operator-valued limits could be studied. Any such repair must show what arithmetic datum survives that is lost by the `L^2` calculation, and it must not simply insert the analytically continued `1/zeta` as a counterterm.

**The finite-prime net is canonical only after choosing the divisibility/Möbius observable.** Other arithmetic observables may have different thresholds. A successful escape must explain why its observable is forced by the Riemann problem and why its critical behavior is sensitive to the zero divisor rather than only to prime-density moments.

**The argument is real-temperature, not a complex KMS analytic continuation.** KMS states are indexed here by positive real `beta`. The comparison with `1/zeta(beta)^2` is used only to disprove the naive identification with the scalar analytic continuation; no complex-temperature KMS state is asserted.

## Falsification / audit tests

The finding would be materially falsified or narrowed if any of the following failed:

1. the Bost--Connes range projections satisfy the stated coprime and prime-power divisibility relations;
2. the KMS identity does not imply `phi_beta(E_n)=n^(-beta)` for every `KMS_beta` state;
3. `Q_p=1-2E_p+E_(p^2)` does not have local values `1,-1,0` or fails `Q_p^2=1-E_(p^2)`;
4. the finite-prime moments do not factor into the displayed Euler products;
5. `prod_p(1-p^(-2 beta))` has its positivity threshold somewhere other than `beta=1/2`;
6. the Möbius net is `L^2`-Cauchy for some `1/2<beta<=1`, contrary to the explicit tail-distance formula; or
7. the finite-prime KMS expectations at `beta=1/2` converge to the scalar analytic continuation `1/zeta(1/2)^2` rather than to zero.

Items 1--4 are exact algebra/KMS calculations. Items 5--7 reduce to classical prime Euler-product convergence and the displayed distance identity.

## Consequence for the research line

`PL-210` showed that even irreducible noncommuting prime channels remain programmable unless their relations are forced by arithmetic. The Bost--Connes divisibility projections provide precisely such a forced relation, so they are a legitimate next stress test rather than another manufactured operator model.

The result is negative but informative. A canonical rational-prime system really does distinguish `1/2`, yet the distinguished quantity is only the survival of square-free support in a second moment. The Möbius orientation that could carry cancellation information does not become a coherent KMS `L^2` object until `beta>1`, and the high-temperature KMS state does not analytically continue its Gibbs Euler expectation.

Accordingly, the next source-forced operator candidate must do more than couple prime coordinates multiplicatively or exhibit a half-threshold. It must retain **phase-sensitive global arithmetic information across the `beta=1` coherence failure** and connect that information to analytic continuation or a completed positivity/duality statement. A `1/2` boundary that remains unchanged under arbitrary unimodular prime phases fails the line's Helson/phase falsification control and should not be promoted as an RH mechanism.