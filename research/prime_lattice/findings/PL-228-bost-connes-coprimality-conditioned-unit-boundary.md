# PL-228 — All-prime coprimality conditioning lands on the Bost–Connes unit boundary, not on an RH-sensitive half-axis

## Claim

There is a canonical all-prime conditioning complementary to the lcm/divisibility conditioning of `PL-227`. Let

\[
\mathcal A_{BC}=C^*(\mathbb Q/\mathbb Z)\rtimes\mathbb N^\times,
\qquad
P_n=\mu_n\mu_n^*,
\]

and for a finite set `F` of rational primes define

\[
Q_F=\prod_{p\in F}(1-P_p).
\]

On the exponent lattice, `Q_F` is the indicator of the event

\[
v_p(n)=0\qquad(p\in F),
\]

so it removes every state divisible by one of the inspected primes. For a `KMS_beta` state `Phi`, `beta>0`, normalize the corresponding corner by

\[
\Psi_{\Phi,F}(x)
=\frac{\Phi(Q_FxQ_F)}{\Phi(Q_F)}.
\]

The denominator is exact and state-independent:

\[
\boxed{
\Phi(Q_F)=\prod_{p\in F}(1-p^{-\beta}).
}
\]

As `F` exhausts the primes, the conditioned states have a complete weak-* limit, but the limit detects only the **classical Bost–Connes phase transition at `beta=1`**.

For `0<beta<=1`, where the Bost–Connes KMS state is unique,

\[
\boxed{
\Psi_{\beta,F}\xrightarrow{w^*}\omega_{\mathrm{Haar}}
:=m_{\widehat{\mathbb Z}^{\times}}\circ E,
}
\]

where `E:A_BC->C(Zhat)` is the prime-gauge expectation and `m_(Zhat^times)` is normalized Haar measure on the profinite unit group. More strongly, for every reduced `a/q`, once `F` contains every prime divisor of `q`,

\[
\boxed{
\Psi_{\beta,F}(e(a/q))
=\frac{\mu(q)}{\varphi(q)},
}
\]

independently of `beta`. These are exactly the normalized Ramanujan/Fourier coefficients of Haar measure on `Zhat^times`.

For `beta>1`, every KMS state is a barycenter of the symmetry-broken extremal Gibbs states indexed by `rho in Zhat^times`. If `nu` is the corresponding probability measure on `Zhat^times`, then

\[
\boxed{
\Psi_{\Phi,F}\xrightarrow{w^*}\omega_\nu,
\qquad
\omega_\nu(x)=\int_{\widehat{\mathbb Z}^{\times}}
\rho(E(x))\,d\nu(\rho).
}
\]

Thus the same conditioning that is universal below and at the phase transition recovers exactly the symmetry-breaking boundary measure above it. In an extremal low-temperature state it converges to the corresponding arithmetic ground-state character.

The mass of the all-unit event explains the dichotomy:

\[
\prod_p(1-p^{-\beta})
=\begin{cases}
0,&0<\beta\le1,\\
\zeta(\beta)^{-1}>0,&\beta>1.
\end{cases}
\]

This is a **decisive negative/control for the canonical all-prime coprimality/sieve completion as an RH mechanism**. It is genuinely infinite-prime and it preserves nontrivial cyclotomic/Galois data in the low-temperature phase, so it is stronger than a finite-prime Toeplitz reduction. But its only intrinsic boundary is `beta=1`, and the limiting data are precisely the already-classical Bost–Connes unit-boundary data. No `1/2` localization, analytic continuation into the critical strip, zero divisor, Weil positivity, or Hilbert–Pólya spectrum is generated.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. The sieve projection is the exponent-zero face

The range projection `P_p=mu_p mu_p^*` belongs to the cyclotomic diagonal and, in the standard divisibility representation, is the indicator of `p|n`. Hence

\[
Q_F=\prod_{p\in F}(1-P_p)
\]

is the projection onto the finite-prime face on which all inspected exponent coordinates vanish. Writing

\[
M_F=\prod_{p\in F}p,
\]

inclusion-exclusion gives

\[
Q_F=\sum_{d\mid M_F}\mu(d)P_d.
\]

For every Bost–Connes `KMS_beta` state, the standard KMS relation gives

\[
\Phi(P_d)=d^{-\beta}.
\]

Therefore

\[
\Phi(Q_F)
=\sum_{d\mid M_F}\mu(d)d^{-\beta}
=\prod_{p\in F}(1-p^{-\beta}).
\]

The projection is nonzero and has positive KMS mass for every finite `F`, so `Psi_(Phi,F)` is always a well-defined state.

This is the opposite tail from `PL-227`. There the lcm corner forces increasingly many lower bounds `v_p>=a_p` and converges to the profinite zero point. Here the sieve face forces `v_p=0` on more and more coordinates. In the positive-energy integer basis this leaves only the vacuum `n=1`, exactly as `PL-225` observed through the strong limit `Q_F->|epsilon_1><epsilon_1|`. In the full cyclotomic diagonal, however, the same valuation-zero condition leaves the entire profinite unit boundary `Zhat^times`; the residue/Galois coordinates survive even after all valuations have been killed.

## 2. Exact conditional Fourier identity

The diagonal projections commute with the cyclotomic generators. The Bost–Connes covariance relation

\[
\mu_d^*e(r)\mu_d=e(dr)
\]

therefore gives

\[
P_de(r)
=\mu_de(dr)\mu_d^*.
\]

Applying the KMS identity yields, for every `beta>0`,

\[
\boxed{
\Phi(P_de(r))=d^{-\beta}\Phi(e(dr)).
}
\]

and hence

\[
\boxed{
\Psi_{\Phi,F}(e(r))
=
\frac{
\sum_{d\mid M_F}\mu(d)d^{-\beta}\Phi(e(dr))
}{
\prod_{p\in F}(1-p^{-\beta})
}.
}
\]

No Euler-product continuation is being used here. This is a finite algebraic identity inside the Bost–Connes system at a real inverse temperature where the KMS state exists.

Moreover, `PL-219` shows that every Bost–Connes KMS state factors through the prime-gauge expectation `E`. Since `Q_F` is gauge fixed, every conditioned state does as well:

\[
\Psi_{\Phi,F}=\Psi_{\Phi,F}\circ E.
\]

Consequently it is enough to determine the conditioned state on the dense cyclotomic Fourier algebra generated by the `e(r)`.

## 3. High temperature: finite-prime conditioning becomes Haar on the units

For `0<beta<=1`, let `Phi_beta` denote the unique KMS state. The classical Bost–Connes formula, already used in `PL-212`, is

\[
\Phi_\beta(e(a/q))
=q^{-\beta}
\prod_{p\mid q}
\frac{1-p^{\beta-1}}{1-p^{-1}}
\]

for `(a,q)=1`.

Fix a reduced `a/q`. A prime `p` not dividing `q` changes only the numerator of `e(a/q)` under `r->pr`; the high-temperature value depends only on the reduced denominator. Hence the factor contributed by such a prime in the conditional numerator is exactly `1-p^{-beta}` and cancels the same denominator factor.

Now suppose `p^k||q`. Put

\[
C_p(\beta)=\frac{1-p^{\beta-1}}{1-p^{-1}}.
\]

The `p`-part of the unconditioned Fourier coefficient is `p^{-k beta}C_p(beta)` for `k>=1`. Conditioning at `p` replaces it by

\[
\frac{
 p^{-k\beta}C_p(\beta)
 -p^{-\beta}h_{k-1}
}{1-p^{-\beta}},
\]

where `h_0=1` and `h_j=p^{-j beta}C_p(beta)` for `j>=1`. Thus

\[
\begin{cases}
-1/(p-1),&k=1,\\
0,&k\ge2.
\end{cases}
\]

The `k=1` identity is exact because

\[
\frac{p^{-\beta}(C_p(\beta)-1)}{1-p^{-\beta}}
=-\frac1{p-1}.
\]

Therefore, once `F` contains the prime support of `q`,

\[
\Psi_{\beta,F}(e(a/q))
=
\begin{cases}
\displaystyle\prod_{p\mid q}-\frac1{p-1},&q\text{ square-free},\\[3mm]
0,&q\text{ not square-free},
\end{cases}
=
\boxed{\frac{\mu(q)}{\varphi(q)}}.
\]

For a reduced fraction, the Ramanujan sum satisfies `c_q(a)=mu(q)`, while normalized Haar measure on the compact multiplicative group `Zhat^times` has Fourier transform

\[
\int_{\widehat{\mathbb Z}^{\times}}
e^{2\pi i a u/q}\,dm(u)
=\frac{c_q(a)}{\varphi(q)}.
\]

Hence the conditioned Fourier coefficients are eventually **exactly** those of Haar measure, not merely asymptotic. Density of the cyclotomic characters in `C(Zhat)`, together with gauge diagonalization, proves the weak-* convergence on the whole Bost–Connes algebra.

This makes the information loss especially sharp. Although the conditioning event has KMS mass tending to zero for every `beta<=1`, the normalized limit exists and is independent of `beta`; it is the symmetric Haar mixture of the arithmetic boundary characters.

## 4. Low temperature: the same conditioning recovers the symmetry-breaking boundary measure

For `beta>1`, an extremal KMS state `Phi_(beta,rho)` has the standard Gibbs realization on `ell^2(N)`, with

\[
H\epsilon_n=(\log n)\epsilon_n
\]

and cyclotomic diagonal

\[
e(r)\epsilon_n=\rho(e(nr))\epsilon_n.
\]

Thus

\[
\Phi_{\beta,\rho}(Q_Fe(r))
=
\frac1{\zeta(\beta)}
\sum_{\substack{n\ge1\\(n,M_F)=1}}
\frac{\rho(e(nr))}{n^\beta}.
\]

Because `beta>1`, this series is absolutely summable. For each fixed `n>1`, an exhausting family `F` eventually contains one prime divisor of `n`, so the coprimality indicator tends to zero; the term `n=1` survives. Dominated convergence therefore gives

\[
\Phi_{\beta,\rho}(Q_Fe(r))
\longrightarrow
\frac{\rho(e(r))}{\zeta(\beta)}.
\]

At the same time,

\[
\Phi_{\beta,\rho}(Q_F)
=\prod_{p\in F}(1-p^{-\beta})
\longrightarrow\frac1{\zeta(\beta)}.
\]

After normalization,

\[
\boxed{
\Psi_{\beta,\rho,F}(e(r))\longrightarrow\rho(e(r)).
}
\]

Gauge diagonalization again upgrades this to weak-* convergence of states to the arithmetic boundary state `rho o E`.

The complete low-temperature KMS simplex is the probability simplex on `Zhat^times`. If

\[
\Phi=\int\Phi_{\beta,\rho}\,d\nu(\rho),
\]

then the denominator `Phi(Q_F)` is independent of `rho`, so the same dominated-convergence argument passes through the barycenter and yields

\[
\Psi_{\Phi,F}\xrightarrow{w^*}
\int(\rho\circ E)\,d\nu(\rho).
\]

Thus all-prime coprimality conditioning does retain genuinely arithmetic information above `beta=1`: it strips off the Gibbs multiplicative orbit and recovers exactly the boundary measure that already parameterizes spontaneous symmetry breaking. It does not create a new spectral invariant.

## 5. Adelic prior art makes the phase boundary classical

The conclusion has close classical prior art in the adelic formulation of the Bost–Connes phase transition. Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proceedings of the American Mathematical Society* **130**(10) (2002), 2999–3003, DOI `10.1090/S0002-9939-02-06449-3`, works with

\[
R=\prod_p\mathbb Z_p,
\qquad
W=R^*=\prod_p\mathbb Z_p^*.
\]

He records for the Bost–Connes scaling measures that

\[
\mu_\beta(W)=\prod_p(1-p^{-\beta})
\]

is positive exactly for `beta>1`, and that in this region probability measures on `W` parameterize the scaling measures/KMS states. For `beta<=1`, `mu_beta(W)=0`; the canonical invariant scaling measure is an explicit product of local measures whose density relative to local Haar is proportional to `|a|_p^(beta-1)`. On `Z_p^*` that density is constant, so conditioning a finite set of local coordinates to be units gives Haar on those coordinates independently of `beta`. The finite-prime Fourier derivation above is the algebraic version of this product-measure fact.

Accordingly no novelty claim is made. The durable delta for this line is the closure of a specific surviving `prime_lattice` escape after `PL-225` and `PL-227`: passing to the **dual all-prime sieve face** does produce a nontrivial boundary state, but the boundary is the already-known profinite-unit/Galois boundary of Bost–Connes theory and its threshold is exactly the classical phase transition at `beta=1`.

The foundational Bost–Connes source remains source 5 in `research/prime_lattice/SOURCES.md`; `PL-212` and `PL-219` supply the already-audited KMS Fourier formula and gauge diagonalization used above. Neshveyev's adelic theorem is used here as the closest novelty/prior-art control.

## 6. RH relevance and matched controls

The result closes a natural infinite-prime route rather than merely another finite-prime observable. The finite projections `Q_F` converge strongly to the integer vacuum in the positive-energy representation (`PL-225`), yet their normalized KMS conditioning retains the whole cyclotomic unit boundary. This precisely separates what the bare exponent lattice loses from what the Bost–Connes arithmetic extension retains.

That retained information is nevertheless not the missing RH rigidity. Below and at the phase transition it is forced to the universal Haar boundary. Above the phase transition it is exactly the arbitrary probability measure `nu` already allowed by the KMS simplex. The construction supplies neither a self-adjoint operator with zeta-zero spectrum nor a positivity identity constraining zeros, and it never analytically continues a Gibbs/KMS object into the critical strip.

There is also a generic product-measure control behind the normalization: independent valuation coordinates with local mass `P(v_p=0)=1-p^{-beta}` exhibit the same zero-versus-positive mass transition when `sum_p p^{-beta}` changes from divergent to convergent. Rational-prime specificity enters through the cyclotomic identification of the residual all-zero-valuation face with `Zhat^times` and its Ramanujan/Galois Fourier data. That arithmetic specificity is real, but it is already the classical Bost–Connes symmetry-breaking invariant rather than a new `Re(s)=1/2` mechanism.

No analytic-continuation claim is made anywhere in this finding.

## Boundaries and falsification tests

The claim is specific to the canonical Bost–Connes sieve projections and KMS states. It does not rule out an adelic/Weil trace formula, a target-relative Nyman coupling, an unbounded relative modular construction, or a renormalization that introduces additional source-forced arithmetic data before taking the all-prime limit.

The finding would require correction or narrowing if any of the following failed:

1. `P_p` were not the diagonal divisibility projection and `Q_F` were not the finite local-unit event;
2. the KMS relation failed to give `Phi(P_d)=d^(-beta)` or `Phi(P_d e(r))=d^(-beta)Phi(e(dr))`;
3. the unique `0<beta<=1` cyclotomic KMS formula used in `PL-212` were incorrect;
4. the local conditional calculation for `p^k||q` failed to give `-1/(p-1)` at `k=1` and `0` at `k>=2`;
5. normalized Haar measure on `Zhat^times` did not have Fourier coefficient `c_q(a)/varphi(q)=mu(q)/varphi(q)` for reduced `a/q`;
6. the `beta>1` extremal Gibbs series did not permit dominated convergence after imposing `(n,M_F)=1`;
7. the low-temperature KMS simplex were not parameterized by probability measures on `Zhat^times`; or
8. conditioned KMS states failed to inherit the gauge expectation from `PL-219`.

All of these are exact, classical, or finite-algebraic checks and none assumes RH.