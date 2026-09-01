# WP-078 — Möbius primitive of the positive cover cocycle is positive on prime powers and indefinite off them

**Status:** `EXACT-DERIVED + CLASSICAL-MOBIUS-IDENTITY + DECISIVE-POSITIVITY-OBSTRUCTION + MATHIA-SPECIALIZATION`.

`WP-074`–`WP-076` produce a canonical positive trace-class cocycle from the pointed Prime-Circle root-cover geometry. The natural next test is whether the ordinary divisor-lattice Möbius primitive of that positive cocycle can solve the remaining prime-power support problem *without* leaving the positive cone.

It almost does, but in a very rigid way. Let

\[
Q_n:=nW_n^*L^{-1}W_n-L^{-1}\succeq0,
\qquad Q_1:=0,
\]

be the inverse-scale defects of `WP-074`, where

\[
W_ne_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad L=N+\frac12I.
\]

Define their divisor-Möbius primitive

\[
\boxed{
M_n:=\sum_{d\mid n}\mu(d)Q_{n/d}.
}
\tag{1}
\]

Then:

1. every `M_n` is self-adjoint diagonal trace class;
2. its ordinary trace is exactly
   \[
   \boxed{\operatorname{Tr}M_n=\Lambda(n);}
   \tag{2}
   \]
3. for every prime power `n=p^k`,
   \[
   \boxed{
   M_{p^k}=Q_{p^k}-Q_{p^{k-1}}
   =\rho_{p^{k-1}}(Q_p)\succeq0,
   \qquad
   \operatorname{Tr}M_{p^k}=\log p,
   }
   \tag{3}
   \]
   where
   \[
   \rho_n(D):=nW_n^*DW_n;
   \tag{4}
   \]
4. if `n` has at least two distinct prime divisors, then
   \[
   \boxed{
   \operatorname{Tr}M_n=0,
   \qquad
   M_n\neq0,
   \qquad
   M_n\text{ is indefinite};
   }
   \tag{5}
   \]
5. consequently the exact critical finite scalar is available from the same pointed-cover system as
   \[
   \boxed{
   \operatorname{Tr}(M_n)
   \langle e_0,W_ne_0\rangle
   =\frac{\Lambda(n)}{\sqrt n},
   }
   \tag{6}
   \]
   but the operation that kills mixed composites is not positivity: it is Möbius cancellation through nonzero trace-zero indefinite operators.

Thus the positive cocycle has a sharper structure than the local Boolean supertrace of `WP-018`: **its Möbius primitive remains genuinely positive exactly on the prime-power fibers that carry Mangoldt mass.** However, the same primitive is necessarily indefinite on every mixed-prime integer. Taking positive parts, absolute values, or other standard sign repairs then restores unwanted composite mass.

This closes the direct escape “Möbius-invert the positive `Q_n` cocycle and retain positivity.” It does not rule out a nonlinear support-dependent rank mechanism, an explicit primitive-ray restriction, or a genuinely nonseparable global/cohomological construction before positivity.

## 1. The positive cover defect is an operator-valued multiplicative cocycle

`WP-076` proves at zero shift that

\[
\boxed{
Q_{mn}=\rho_n(Q_m)+Q_n
=\rho_m(Q_n)+Q_m,
}
\tag{7}
\]

with `rho_n` as in (4). Since the normalized cover operators satisfy

\[
W_mW_n=W_{mn}=W_nW_m,
\]

one also has on the diagonal operator algebra

\[
\boxed{
\rho_m\rho_n=\rho_{mn}=\rho_n\rho_m.
}
\tag{8}
\]

For a diagonal trace-class operator

\[
De_j=d_je_j,
\]

the action is explicitly

\[
(\rho_nD)e_k
=
\left(\sum_{r=0}^{n-1}d_{nk+r}\right)e_k.
\tag{9}
\]

Hence `rho_n` preserves positivity and, for diagonal trace-class `D`, preserves the ordinary trace:

\[
\boxed{
\operatorname{Tr}(\rho_nD)=\operatorname{Tr}D.
}
\tag{10}
\]

This is the exact operator setting in which to ask for a primitive divisor contribution. The scalar trace of `Q_n` is `log n`, so the classical arithmetic primitive of that additive degree character is `Lambda(n)`. Equation (1) tests whether that scalar Möbius inversion also has a positive operator lift.

## 2. The trace primitive is exactly von Mangoldt

Because every divisor sum in (1) is finite and each `Q_m` is trace class,

\[
\begin{aligned}
\operatorname{Tr}M_n
&=\sum_{d\mid n}\mu(d)\operatorname{Tr}Q_{n/d}\\
&=\sum_{d\mid n}\mu(d)\log\frac nd\\
&=\Lambda(n).
\end{aligned}
\tag{11}
\]

The last identity is the classical divisor-lattice Möbius inversion

\[
\Lambda=\mu*\log,
\]

already audited in `WP-018`. No novelty is claimed for the scalar identity or for Möbius inversion itself. What is new to the present Mathia branch is that the scalar logarithm is not inserted as an external function: it is `Tr Q_n` for the independently positive pointed-cover defect.

Since

\[
W_ne_0=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_r,
\]

we also have

\[
\langle e_0,W_ne_0\rangle=n^{-1/2}.
\tag{12}
\]

Combining (11) and (12) proves (6). Thus the positive pointed-cover representation now contains all numerical ingredients of the finite Weil prime-power coefficient without using the cyclotomic boundary identity `Phi_n(1)`.

The remaining question is whether the operator primitive `M_n` itself stays positive.

## 3. Prime powers remain inside the positive cone

Let `n=p^k`, `k>=1`. Only `d=1,p` contribute to (1), so

\[
M_{p^k}=Q_{p^k}-Q_{p^{k-1}}.
\tag{13}
\]

Applying the cocycle law (7) to `p^k=p\,p^{k-1}` gives

\[
Q_{p^k}
=\rho_{p^{k-1}}(Q_p)+Q_{p^{k-1}}.
\]

Therefore

\[
\boxed{
M_{p^k}=\rho_{p^{k-1}}(Q_p)\succeq0.
}
\tag{14}
\]

This is stronger than merely observing that its trace is positive. The whole trace-class operator produced by Möbius extraction is positive on every point of a primitive prime ray.

By trace preservation (10),

\[
\operatorname{Tr}M_{p^k}
=\operatorname{Tr}Q_p
=\log p,
\tag{15}
\]

so the disappearance of the exponent `k` also has an operator interpretation: the primitive defect at depth `k` is just the original positive one-step prime defect transported by the positive refinement map `rho_{p^{k-1}}`.

Equivalently, along every divisibility edge one has

\[
\boxed{
Q_{np}-Q_n=\rho_n(Q_p)\succeq0,
\qquad
\operatorname{Tr}(Q_{np}-Q_n)=\log p.
}
\tag{16}
\]

The cover cocycle therefore has a genuine positive logarithmic increment along **every** prime-labeled edge of the divisibility poset.

## 4. Mixed-prime Möbius primitives are nonzero trace-zero operators

The crucial point is that the positive edge law (16) is not selective: it holds equally when the base integer `n` already contains other primes. Prime-power support can therefore emerge only after higher mixed differences.

Write

\[
R=\operatorname{rad}(n),
\qquad
h=\frac nR.
\]

Since the Möbius function is supported on squarefree divisors,

\[
M_n
=\sum_{d\mid R}\mu(d)Q_{hR/d}.
\tag{17}
\]

For `R>1`, use

\[
Q_{hm}=\rho_h(Q_m)+Q_h
\]

and

\[
\sum_{d\mid R}\mu(d)=0
\]

to obtain the exact reduction

\[
\boxed{
M_n=\rho_h(M_R).
}
\tag{18}
\]

Now assume `R` has at least two primes and choose one `p|R`. Put `T=R/p`. Pairing the divisor terms according to whether they contain `p` gives

\[
\begin{aligned}
M_R
&=\sum_{e\mid T}\mu(e)
\left(Q_{pT/e}-Q_{T/e}\right)\\
&=\sum_{e\mid T}\mu(e)\rho_{T/e}(Q_p).
\end{aligned}
\tag{19}
\]

Because the `rho_q` commute and are multiplicative,

\[
\boxed{
M_R
=
\prod_{q\mid T}(\rho_q-I)Q_p,
}
\tag{20}
\]

and hence

\[
\boxed{
M_n
=
\rho_{n/\operatorname{rad}(n)}
\prod_{\substack{q\mid n\\q\ne p}}(\rho_q-I)Q_p.
}
\tag{21}
\]

Equation (21) already displays the structural transition: the first difference along one prime is positive, but every additional distinct prime inserts a signed factor `rho_q-I`.

To prove that these higher mixed differences do not vanish accidentally, use the exact tail of `Q_p` from `WP-074`:

\[
(Q_p)_{kk}
=
\frac{a_p}{(k+1/2)^3}+O_p(k^{-5}),
\qquad
 a_p=\frac{p^2-1}{12p^2}>0.
\tag{22}
\]

If a diagonal sequence satisfies

\[
d_k=a k^{-3}+O(k^{-4}),
\]

then (9) gives

\[
(\rho_qD)_{kk}
=a q^{-2}k^{-3}+O_q(k^{-4}).
\tag{23}
\]

Consequently each factor `rho_q-I` multiplies the leading `k^{-3}` coefficient by the nonzero scalar `q^{-2}-1`, while the outer `rho_h` multiplies it by `h^{-2}`. Therefore (21) has the nonzero asymptotic

\[
\boxed{
(M_n)_{kk}
=
a_p h^{-2}
\prod_{\substack{q\mid R\\q\ne p}}
(q^{-2}-1)
\,k^{-3}
+O_n(k^{-4}),
}
\tag{24}
\]

where `h=n/R`. Since every factor in the displayed leading coefficient is nonzero,

\[
\boxed{M_n\ne0}
\]

for every integer with at least two distinct prime factors.

On the other hand, (11) gives

\[
\operatorname{Tr}M_n=\Lambda(n)=0
\]

for every such integer. A nonzero self-adjoint trace-class operator of trace zero cannot be positive or negative semidefinite: otherwise its trace would have the corresponding strict sign. Hence `M_n` has both positive and negative spectral mass. This proves (5).

For example,

\[
M_{pq}=Q_{pq}-Q_p-Q_q
=(\rho_q-I)Q_p
=(\rho_p-I)Q_q
\tag{25}
\]

for distinct primes `p,q`. It already has trace zero and is nonzero, so the failure of positivity occurs at the first mixed-prime square.

## 5. Positive repairs necessarily reintroduce composite mass

For a mixed-prime `n`, write the Jordan decomposition

\[
M_n=(M_n)_+-(M_n)_-.
\]

By (5), both pieces are nonzero. Since the trace vanishes,

\[
\operatorname{Tr}(M_n)_+
=
\operatorname{Tr}(M_n)_-
>0,
\tag{26}
\]

and therefore

\[
\boxed{
\operatorname{Tr}|M_n|
=2\operatorname{Tr}(M_n)_+>0.
}
\tag{27}
\]

Thus the standard ways of turning the primitive into a positive operator — positive part, absolute value, squaring, or any faithful positive readout detecting its nonzero spectral mass — cannot retain exact Mangoldt support. They assign positive mass to mixed composites that the ordinary trace cancels exactly.

This mirrors `WP-018` but is not the same construction. There the selector is an alternating supertrace of local residual energies on a Boolean cube. Here the *input* is the much stronger positive pointed-cover cocycle whose one-prime primitive remains positive as an operator. The obstruction appears only when the divisor geometry asks for a second distinct-prime difference.

The result also complements `WP-031`: that finding rules out one fixed place-additive positive quadratic feature whose nullspace is supposed to encode mixed support. Here no such place-additive feature is assumed. The failure is instead internal to the canonical Möbius primitive of the positive cover cocycle.

## 6. Matched controls and novelty audit

The classification uses only:

- the block-replication isometries `W_n`;
- the positive trace-class cocycle `Q_n` and its exact semigroup law;
- the ordinary divisor-poset Möbius function;
- the `k^{-3}` tail forced by the block Jensen defect.

It does not use zeta zeros, the zeta functional equation, primality beyond choosing primitive generators of integer degree, or any special global arithmetic property of `Q`. The same operator calculation therefore survives in a matched cyclic-cover degree system carrying the same block-refinement representation. This is a local/semigroup support theorem, not evidence that the global arithmetic completion has been found.

The scalar identity `Lambda=mu*log` and Möbius inversion on divisor/incidence posets are classical; `WP-018` already records that prior-art boundary. A directed literature audit of operator-valued Möbius inversion, incidence algebras, and semigroup cocycles did not identify a known theorem matching the specific `Q_n` classification above. No novelty claim is based on that absence. The Mathia-specific durable content is the exact interaction between the already-derived positive cover cocycle and classical Möbius inversion: positivity survives precisely on prime-power primitives and fails by a provable nonzero trace-zero mixed difference as soon as two distinct primes interact.

## 7. Boundary of the obstruction

This finding rules out only the direct linear Möbius primitive of the `Q_n` cocycle as a globally positive support selector. It does **not** rule out:

1. the nonlinear rank/volume selector of `WP-030`;
2. an explicit restriction to primitive prime rays before forming a positive form;
3. a non-faithful quotient that kills every mixed `M_n` for an independently geometric reason;
4. a genuinely nonseparable finite–archimedean coupling formed before the positivity theorem;
5. a cohomological/intersection construction in which an alternating local trace is controlled by a separate global sign theorem.

Any use of items 2–5 must still pass the line mandate: the restriction or quotient must be intrinsic rather than fitted to `Lambda`, and the same structure must generate the archimedean/polar terms and the final Weil sign without importing zero data.

Nor does (6) solve the finite Weil quadratic form. It realizes the exact scalar coefficient, but `WP-005` and `WP-074` still show that lifting the positive prime-ray Poisson Gram data to the required Weil autocorrelation multiplier introduces an indefinite subtraction. `WP-076`–`WP-077` further show that the obvious pointed-cover digamma mixing and semigroup-compatible basepoint averaging do not supply the missing global interaction.

## 8. Exact falsification surface

The claim can be refuted by any of the following exact failures:

1. failure of the zero-shift cocycle law (7) for the `Q_n` of `WP-074`;
2. failure of trace preservation (10) for the diagonal trace-class operators used here;
3. failure of the classical trace identity (11);
4. a prime power `p^k` for which (14) is not positive;
5. a mixed-prime `n` for which the factorization (21) fails;
6. failure of the nonzero leading asymptotic (24);
7. a mixed-prime `M_n` that is nevertheless positive or negative semidefinite despite being nonzero and trace zero.

All of these statements are exact and require neither RH nor analytic continuation.

## Research consequence

The pointed-cover branch now has an unusually precise local picture:

```text
positive cover cocycle Q_n
    -> every prime edge has positive increment with trace log p
    -> divisor Möbius primitive M_n
       -> prime-power fiber: positive transported one-step defect
       -> mixed-prime fiber: nonzero trace-zero indefinite mixed difference
    -> Tr(M_n) = Lambda(n)
    -> root-cover overlap = n^(-1/2)
    -> finite Weil coefficient Lambda(n)/sqrt(n)
```

So the remaining finite-support problem is no longer “where can `Lambda` come from?” The same pointed-cover geometry supplies a positive logarithmic edge anomaly and the critical half-weight, while classical incidence inversion extracts the exact Mangoldt scalar. The obstruction is sharper: **the cancellation that removes mixed composites is itself an indefinite higher mixed difference.**

A successful global Weil geometry must therefore do more than assemble these positive local defects or apply their Möbius primitive. It must provide a larger intrinsic quotient, grading, boundary coupling, or cohomological pairing in which the mixed cancellation and the archimedean/polar completion participate in one independently positive global theorem.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
- `research/weil_positivity/findings/WP-031-place-additive-positive-quadratic-readouts-cannot-select-prime-powers.md`
- `research/weil_positivity/findings/WP-074-pointed-cover-inverse-scale-defect-has-positive-log-degree-trace-but-poisson-weil-lift-is-indefinite.md`
- `research/weil_positivity/findings/WP-076-shifted-cover-digamma-mixing-is-a-positive-semigroup-cocycle-coboundary.md`
- `research/weil_positivity/findings/WP-077-semigroup-invariant-basepoint-averaging-is-pointed-plus-haar-and-haar-kills-cover-defects.md`
