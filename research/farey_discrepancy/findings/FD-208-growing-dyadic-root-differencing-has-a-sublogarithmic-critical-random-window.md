# FD-208 — Growing dyadic root differencing has a sublogarithmic critical-random window

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** growing-depth signed root observable / uniform random-multiplicative second moment / depth-cost phase boundary
- **Depends on:** FD-197, FD-206, FD-207
- **Classification:** `EXACT-DERIVED + GROWING-DEPTH-DYADIC-DIFFERENCE + CENTRAL-DELANNOY-RANDOM-MASS + SUBLOG-THRESHOLD + ROUTE-RESTRICTION`

## Claim

`FD-207` leaves growing dyadic differencing depth as one possible escape from its fixed-depth RH-equivalence theorem, while noting that the random coefficient mass is no longer uniform in the depth. That loss can be quantified exactly at the level relevant to the root-aligned Farey comparator.

Let

\[
\Delta(n):=M(2n)-M(n),
\qquad
\mathcal C_q(n):=(T-I)^q\Delta(n),
\qquad
(TF)(n):=F(2n),
\tag{1}
\]

and let the depth now be an arbitrary integer-valued function `q=q(n)>=0`. For the squarefree Rademacher multiplicative source

\[
f(m)=\mu(m)^2\prod_{p\mid m}X_p,
\qquad
A_f(x):=\sum_{m\le x}f(m),
\tag{2}
\]

write

\[
\Delta_f(n):=A_f(2n)-A_f(n),
\qquad
\mathcal C_q^f(n):=(T-I)^q\Delta_f(n).
\tag{3}
\]

Define the coefficient mass

\[
\boxed{
D_q:=\sum_{j=0}^{q}\binom qj^2 2^j.
}
\tag{4}
\]

Then the second moment from `FD-207` admits a **uniform-in-depth** form:

\[
\boxed{
\mathbb E|\mathcal C_q^f(n)|^2
=
\frac6{\pi^2}nD_q
+O\!\left(n^{1/2}D_q\right),
}
\tag{5}
\]

where the implied constant is absolute and (5) holds for every `q>=0`, not merely fixed `q`.

The coefficient `D_q` is the classical central Delannoy number, equivalently the Legendre value `P_q(3)`. More importantly for the present route, it has elementary exponential two-sided bounds

\[
\boxed{
\frac{2^{(5/2)q-1}}{(q+1)^2}
\le D_q\le 8^q
\qquad(q\ge1).
}
\tag{6}
\]

Hence

\[
\boxed{
\log D_q=\Theta(q).
}
\tag{7}
\]

Now use the source-independent root-aligned horizon of `FD-206`,

\[
H_n:=np_n,
\qquad
K_n:=\lfloor\sqrt{H_n}\rfloor,
\tag{8}
\]

where `p_n` is the largest prime at most `n`. The exact Farey realization from `FD-207` is

\[
\mathcal C_q(n)
=
\sum_{j=0}^{q}(-1)^{q-j}\binom qj
S_{2,H_{2^j n}}(p_{2^j n}).
\tag{9}
\]

If the same base-shell normalization as in `FD-207` is applied to the random comparator, then uniformly for arbitrary `q=q(n)`,

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal C_q^f(n)|^2\right]
=
\left(\frac6{\pi^2}+o(1)\right)H_nD_{q(n)}.
}
\tag{10}
\]

Consequently the growing-depth random benchmark stays at the RH-critical **power** scale exactly in the sublogarithmic window:

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal C_{q(n)}^f(n)|^2\right]
=H_n^{1+o(1)}
\iff
q(n)=o(\log n).
}
\tag{11}
\]

If one asks for only a polylogarithmic surcharge, the window is narrower:

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal C_{q(n)}^f(n)|^2\right]
\le H_n(\log H_n)^{O(1)}
\iff
q(n)=O(\log\log n).
}
\tag{12}
\]

There is a matching observation-span boundary. Formula (9) uses root sensors up to the horizon `H_(2^q n)`, and the prime number theorem gives

\[
\frac{H_{2^q n}}{H_n}=4^{q+o(q+\log n)}.
\tag{13}
\]

In particular,

\[
\boxed{
H_{2^{q(n)}n}=H_n^{1+o(1)}
\iff
q(n)=o(\log n).
}
\tag{14}
\]

Thus the same sublogarithmic depth threshold simultaneously characterizes when the random coefficient tariff and the largest required Farey horizon remain within a subpower factor of the base critical scale.

This does **not** prove that a sublogarithmic growing depth escapes the destination-completeness obstruction of `FD-207`. The fixed-depth inversion there is not uniform in `q`, and a pointwise hypothesis on `C_(q(n))(n)` does not supply one common depth on all binary prefixes needed by that proof. The result here classifies the random/source-cost and observation-span budget of the growing-depth opening; it neither proves nor refutes its deterministic analytic usefulness.

## 1. Uniform second moment for arbitrary depth

Expand (3):

\[
\mathcal C_q^f(n)
=
\sum_{j=0}^{q}(-1)^{q-j}\binom qj
\Delta_f(2^j n),
\tag{15}
\]

where

\[
\Delta_f(2^j n)
=
\sum_{2^j n<m\le2^{j+1}n}f(m).
\tag{16}
\]

The dyadic annuli in (16) are pairwise disjoint. For the squarefree Rademacher multiplicative source,

\[
\mathbb E[f(a)f(b)]
=
\mu(b)^2\mathbf 1_{a=b}.
\tag{17}
\]

Therefore all cross-annulus terms vanish exactly, for every finite `q`, and

\[
\mathbb E|\mathcal C_q^f(n)|^2
=
\sum_{j=0}^{q}\binom qj^2
\sum_{2^j n<m\le2^{j+1}n}\mu(m)^2.
\tag{18}
\]

No fixed-depth assumption has entered.

For completeness, the squarefree count needed here is elementary. Since

\[
\mu(m)^2=\sum_{d^2\mid m}\mu(d),
\]

we have

\[
Q(x):=\sum_{m\le x}\mu(m)^2
=
\sum_{d\le\sqrt x}\mu(d)\left\lfloor\frac{x}{d^2}\right\rfloor
=
\frac6{\pi^2}x+O(\sqrt x).
\tag{19}
\]

Thus

\[
Q(2^{j+1}n)-Q(2^j n)
=
\frac6{\pi^2}2^j n
+O\!\left(2^{j/2}n^{1/2}\right).
\tag{20}
\]

Substituting in (18) yields

\[
\mathbb E|\mathcal C_q^f(n)|^2
=
\frac6{\pi^2}nD_q
+O\!\left(
 n^{1/2}
 \sum_{j=0}^{q}\binom qj^2 2^{j/2}
\right).
\tag{21}
\]

Since `2^(j/2)<=2^j`, the error coefficient in (21) is at most `D_q`. This proves (5) with an absolute constant, uniformly for arbitrary growth of `q=q(n)`.

This uniformity matters. The `Theta_q(n)` notation in `FD-207` is harmless for fixed `q`, but it hides exactly the quantity that must be priced when the depth itself becomes the proposed new degree of freedom.

## 2. The coefficient mass grows exponentially in depth

The exact mass (4) is already sufficient for the phase boundary. The upper estimate is immediate from Vandermonde:

\[
D_q
\le
2^q\sum_{j=0}^{q}\binom qj^2
=
2^q\binom{2q}{q}
\le
8^q.
\tag{22}
\]

For the lower estimate, choose `j=floor(q/2)`. The largest binomial coefficient is at least the average coefficient in `(1+1)^q`, so

\[
\binom q{\lfloor q/2\rfloor}
\ge
\frac{2^q}{q+1}.
\tag{23}
\]

Hence

\[
\begin{aligned}
D_q
&\ge
2^{\lfloor q/2\rfloor}
\binom q{\lfloor q/2\rfloor}^2\\
&\ge
\frac{2^{\lfloor q/2\rfloor+2q}}{(q+1)^2}\\
&\ge
\frac{2^{(5/2)q-1}}{(q+1)^2},
\end{aligned}
\tag{24}
\]

which proves (6)--(7).

For prior-art orientation only, `D_q` is the classical central Delannoy sequence. The standard explicit Legendre expansion

\[
P_q(x)=2^{-q}\sum_{j=0}^{q}\binom qj^2
(x-1)^{q-j}(x+1)^j
\]

specializes at `x=3` to `P_q(3)=D_q`. Equivalently, its generating function is `(1-6z+z^2)^(-1/2)`. None of these classical identifications is needed for (6), the phase boundary, or the Farey conclusion; they only identify the coefficient sequence exposed by the Mathia observable.

## 3. Root-aligned Farey normalization is uniform in depth

`FD-206` proves for every sufficiently large integer `m` that

\[
S_{2,H_m}(p_m)=M(2m)-M(m)=\Delta(m),
\tag{25}
\]

with

\[
H_m=mp_m,
\qquad
K_m=\lfloor\sqrt{H_m}\rfloor.
\]

Applying (25) to `m=2^j n` for every `0<=j<=q` gives (9) exactly. The horizons and terminal shell primes depend only on the scale and prime locations, never on observed Mobius values.

At the base scale, the prime number theorem gives

\[
p_n\sim n,
\qquad
H_n\sim n^2,
\qquad
K_n\sim n,
\qquad
\frac{K_n n}{H_n}=\frac{K_n}{p_n}\to1.
\tag{26}
\]

Multiplying the uniform second moment (5) by `K_n` and using (26) proves (10). The `o(1)` is independent of the chosen depth function because the relative error in (5) is `O(n^(-1/2))` after the common factor `D_q` is removed.

The largest scale needed by (9) is `m=2^q n`. Again by the prime number theorem,

\[
H_{2^q n}
=(2^q n)p_{2^q n}
=(1+o(1))4^q n^2,
\tag{27}
\]

whereas `H_n=(1+o(1))n^2`. This gives the scale statement (13) in the only form used below: logarithmically,

\[
\log\frac{H_{2^q n}}{H_n}
=2q\log2+o(q+\log n).
\tag{28}
\]

Thus a growing-depth construction is not cost-free even before any analytic estimate is attempted: the exact signed coefficient itself has exponentially growing random mass, and the physical Farey data span exponentially separated horizons.

## 4. Two exact depth windows

From (10), retaining the critical power exponent is equivalent to

\[
D_{q(n)}=H_n^{o(1)}=n^{o(1)}.
\tag{29}
\]

The upper bound in (6) shows that `q=o(log n)` implies (29). Conversely, if `q` is not `o(log n)`, then along some subsequence `q>=c log n` for a fixed `c>0`; the lower bound in (6) gives

\[
D_q
\ge
n^{(5c/2)\log2-o(1)},
\tag{30}
\]

so (29) fails by a fixed positive power. This proves (11).

Likewise, `q=O(log log n)` implies `D_q=(log n)^(O(1))` by the upper bound. If instead the random surcharge is polylogarithmic, then the lower bound in (6) forces

\[
q=O(\log\log n),
\]

because the polynomial factor `(q+1)^2` cannot absorb exponential growth in `q`. This proves (12).

Finally, (28) proves the same power threshold for the observation span: `H_(2^q n)/H_n=n^(o(1))` exactly when `q=o(log n)`. Thus there are three qualitatively different regimes:

- fixed or `O(log log n)` depth: the random tariff is at most polylogarithmic over `H_n`;
- `log log n << q << log n`: the tariff can exceed every fixed polylogarithm but is still `H_n^(o(1))`;
- `q` comparable to `log n`: both coefficient mass and observation span incur a fixed power surcharge.

The middle regime is a genuine remaining opening. It is not visible if one records only `Theta_q(H)` for fixed `q` or jumps directly from fixed depth to logarithmic depth.

## 5. What this does and does not close after FD-207

`FD-207` proves that every **fixed** depth is destination-complete: a pointwise square-root bound for `C_q(n)` can be inverted, using bounded physical odd-step defects, to the usual Mertens square-root bound and hence RH. Its proof explicitly allows constants depending on `q`. The present calculation shows that allowing `q` to grow creates a real quantitative regime rather than a formal loophole, but only below logarithmic depth if one wants to preserve the critical random power benchmark.

It would be incorrect to combine the two findings and declare the sublogarithmic regime RH-equivalent. When `q=q(n)` varies with the target, a pointwise estimate for `C_(q(n))(n)` does not provide the same depth at all binary prefixes. Moreover the repeated inversion constants and discrete-integration losses in `FD-207` are not uniform in `q`. A separate theorem would be required to show that any particular growing-depth hypothesis can be inverted without losing the critical exponent.

Conversely, logarithmic depth is already unattractive for the exact comparator tested here. Even before deterministic Mobius arithmetic enters, `D_q` has become a fixed power of the base scale and the sensor reaches a largest Farey horizon a fixed power beyond `H_n`. Such a construction could still be useful only if an additional signed aggregation changes the coefficient geometry before positivity; it cannot be advertised as retaining the same critical random budget merely by increasing the order of `(T-I)`.

This leaves two concrete live directions consistent with the current frontier:

1. test whether a **sublogarithmic** growing depth admits a uniform source-side inversion or a genuinely non-pointwise estimate that is not reducible to the fixed-depth theorem;
2. replace the binomial dilation polynomial altogether by an aggregate signed cross-scale relation whose coefficient `l^2` mass grows more slowly than `D_q` while still eliminating the destination-complete root component.

The second direction is distinct from simply choosing a larger `q`: equation (5) shows that for the binomial `(T-I)^q` family, the random second moment sees the complete weighted coefficient mass with no hidden cross-annulus cancellation.

## 6. Prior-art, representation and falsification audit

A targeted external search confirms that the sequence in (4) is classical: it is the central Delannoy sequence and equals `P_q(3)` for Legendre polynomials. Standard Legendre references also give the generating function `(1-6z+z^2)^(-1/2)`. No novelty is claimed for that binomial identity, for Delannoy numbers, or for the fact that they grow exponentially.

Those external facts are not load-bearing. Equations (18)--(24) give a self-contained derivation of the uniform second moment and the exponential two-sided bounds needed for the depth thresholds. The only asymptotic arithmetic input used to identify the Farey base scale and largest root horizon is the prime number theorem, already anchored in `SOURCES.md`. Therefore no source-list update is needed.

The representation audit is exact. Each term in (9) is a physical root-aligned Farey sensor from `FD-206`; no random coefficient is substituted into the physical theorem. The Rademacher source is used only as the same comparator as `FD-197` and `FD-207`, and (5) is explicitly a statement about its expectation. The base normalization `K_n` is kept because the destination coordinate is indexed by the base quotient `n`; for growing `q`, the additional physical observation span is separately exposed by (13)--(14) rather than hidden inside that normalization.

The main falsification boundary is equally explicit. `q=o(log n)` is a necessary and sufficient condition only for preserving the **power exponent of this random comparator and observation span**. It is not a sufficient condition for a deterministic Farey estimate, not an RH criterion, and not evidence that the physical Mobius source realizes random behavior. A future result showing a different signed coefficient family with smaller source-side mass would not contradict this finding; it would leave the `(T-I)^q` family.

No clue status changes. The accepted local clues concern distinct Farey-order/Jordan mechanisms. No formalization handoff is opened: the finite identities and phase bounds are elementary and stable, while the mathematically live work lies in the nonuniform-depth inversion/aggregation question rather than in machine-checking (18)--(24).

## Conclusion

Growing dyadic differencing is a real opening left by `FD-207`, but it has a sharp budget. The squarefree-random second moment of the depth-`q` root coefficient is multiplied by

\[
D_q=\sum_j\binom qj^2 2^j,
\]

an exponentially growing central-Delannoy mass. After exact root-aligned Farey normalization, the comparator remains `H^(1+o(1))` **if and only if** `q=o(log n)`, and remains within `H` times a fixed polylogarithm **if and only if** `q=O(log log n)`. The largest required Farey horizon has the same sublogarithmic power threshold.

Thus the growing-depth escape has been narrowed from an unpriced possibility to a specific window. Fixed depth remains RH-equivalent by `FD-207`; logarithmic depth already pays a polynomial random and observation-scale surcharge; only genuinely sublogarithmic depth, or a different aggregate signed coefficient geometry, remains compatible with the critical-power comparator without further cancellation.