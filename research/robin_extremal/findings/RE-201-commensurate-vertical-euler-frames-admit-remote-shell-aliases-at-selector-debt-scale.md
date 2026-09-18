# RE-201 — Commensurate vertical Euler frames admit remote-shell aliases at selector debt scale

**Status:** `EXACT-DERIVED + COMPLEX-EULER-SAMPLING + MULTIPLICATIVE-ALIASING + ORDINARY-PRIME-REALIZATION + SELECTOR-DEBT-SCALE + KV-FIDELITY + INTEGER-MULTIPLICITIES + REPRESENTATION-LIMIT`.

**Parent findings:** RE-194, RE-200.

`RE-200` shows that a vertical Euler frame can resolve `K` honest prime directions stably inside one fixed multiplicative shell. That statement is correct but does not yet imply global source coercivity. The particular dual grid used there,

\[
t_k=\frac{2\pi k}{W},\qquad 0\le k<K,
\tag{1}
\]

has an exact logarithmic alias period `W`: multiplying a prime location by `exp(mW)` leaves every sampled Fourier phase unchanged when `m` is an integer. Ordinary-prime multiplicity can compensate the accompanying reciprocal-amplitude loss.

This produces a source-level near-kernel at exactly the reciprocal scale relevant to the Robin matched-control program.

Put

\[
V(Q):=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}}.
\tag{2}
\]

Fix `W>0`, let `K=K(Q)->infinity` satisfy

\[
\log K=o(V(Q)),
\tag{3}
\]

and define the selector reciprocal scale

\[
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{4}
\]

There exist two disjoint finite sets of ordinary primes `P_Q` and `R_Q`, with coefficients `+1` on `P_Q` and `-1` on `R_Q`, such that:

1. `P_Q subset [Q,e^WQ]` and `|P_Q| asy sqrt(Q)/log Q`, so

\[
\sum_{q\in P_Q}\frac1q\asymp d_Q.
\tag{5}
\]

2. `R_Q` lies in a remote shell `[Lambda Q(1-o(1)), Lambda e^WQ(1+o(1))]`, where

\[
\Lambda=e^{mW}=Q^{o(1)},\qquad m\in\mathbb N,
\qquad \log K\ll mW\ll V(Q).
\tag{6}
\]

3. With the exact Euler atom

\[
H_q(s):=\log(1-q^{-s})^{-1}
\tag{7}
\]

and discrepancy

\[
D_Q(s):=
\sum_{q\in P_Q}H_q(s)-
\sum_{r\in R_Q}H_r(s),
\tag{8}
\]

one has

\[
\boxed{
\max_{0\le k<K}
|D_Q(1+it_k)|=o(d_Q).
}
\tag{9}
\]

4. Before the remote shell is reached, the reciprocal/Euler debt is still fully present:

\[
\sum_{q\in P_Q}H_q(1)=\Theta(d_Q).
\tag{10}
\]

5. Starting from ordinary prime multiplicity one, the perturbation uses only multiplicities `{0,1,2}`. Moreover, for every fixed `b>0`, its Chebyshev discrepancy satisfies

\[
|\Delta\vartheta(x)|
=o\!\left(xe^{-bV(x)}\right)
\tag{11}
\]

uniformly on the affected scales.

Thus the `RE-200` DFT frame has linear stable dimension **inside one logarithmic fundamental domain**, but the same commensurate samples admit selector-scale ordinary-prime aliases on a remote shell. Vertical Fourier capacity and global source coercivity are different questions.

## 1. The sampling grid has an exact multiplicative alias period

For the first Euler harmonic, the sampled response of a prime is

\[
q^{-1-it_k}=q^{-1}e^{-it_k\log q}.
\tag{12}
\]

Let

\[
\Lambda=e^{mW},\qquad m\in\mathbb N.
\tag{13}
\]

Then

\[
e^{-it_k\log\Lambda}
=
 e^{-2\pi i km}=1
\tag{14}
\]

for every sample in (1). Hence

\[
(\Lambda q)^{-1-it_k}
=
\Lambda^{-1}q^{-1-it_k}.
\tag{15}
\]

The remote atom has exactly the same phase and only `Lambda^-1` of the amplitude. Replacing one local first-harmonic atom by about `Lambda` remote atoms therefore recreates its entire sampled vector.

The important issue is whether this ideal alias can be realized with distinct ordinary primes, integer multiplicities, exact Euler atoms and the source-fidelity constraints of this line. It can.

## 2. Ordinary primes realize both the local packet and its remote alias

Let `a>0` be the constant in the Korobov--Vinogradov PNT input already used in `RE-200`,

\[
\vartheta(X)=X+O(Xe^{-aV(X)}).
\tag{16}
\]

Choose an integer `m=m(Q)` satisfying (6), set `Lambda=e^(mW)`, and put

\[
\eta:=e^{-aV(Q)/2}.
\tag{17}
\]

Then

\[
K\eta=o(1),
\qquad
V(\Lambda Q)=(1+o(1))V(Q),
\tag{18}
\]

and a logarithmic interval of half-width `eta` at either scale `Q` or `Lambda Q` contains

\[
\asymp \frac{\eta X}{\log X}
\tag{19}
\]

ordinary primes. This follows from (16) because `eta` dominates the PNT error exponentially.

Take the `K` phase centers

\[
x_j:=\frac{(j+1/2)W}{K},
\qquad
X_j:=Qe^{x_j}.
\tag{20}
\]

The bins

\[
I_j=[X_je^{-\eta},X_je^\eta]
\tag{21}
\]

are disjoint since `eta=o(1/K)`. Let

\[
B:=\left\lfloor c\frac{\sqrt Q}{\log Q}\right\rfloor
\tag{22}
\]

for any fixed `c>0`, and split `B` into integers `B_j=B/K+O(1)`. Because

\[
\frac{\eta Q/\log Q}{B/K}
\asymp K\eta\sqrt Q\to\infty,
\tag{23}
\]

each `I_j` contains enough ordinary primes to choose a set `P_j` of size `B_j`.

Now use the remote bins

\[
J_j=[\Lambda X_je^{-\eta},\Lambda X_je^\eta]
\tag{24}
\]

and choose

\[
N_j:=\lfloor \Lambda B_j\rceil
\tag{25}
\]

distinct primes in `J_j`. The same estimate gives enough primes, because both the available population and the requested population acquire the factor `Lambda`. Put

\[
P_Q:=\bigcup_jP_j,
\qquad
R_Q:=\bigcup_jR_j.
\tag{26}
\]

All bins are mutually disjoint for large `Q`, and `Lambda=Q^o(1)`. No continuous weights, pseudo-primes or multiplicities larger than two are introduced.

## 3. The exact sampled Euler discrepancy is `o(d_Q)`

For `q in I_j`, write `q=X_je^delta` with `|delta|<=eta`. Uniformly for `0<=k<K`,

\[
q^{-1-it_k}
=
X_j^{-1-it_k}
\left(1+O(K\eta)\right).
\tag{27}
\]

Likewise, for `r in J_j`,

\[
r^{-1-it_k}
=
(\Lambda X_j)^{-1-it_k}
\left(1+O(K\eta)\right)
=
\Lambda^{-1}X_j^{-1-it_k}
\left(1+O(K\eta)\right),
\tag{28}
\]

where the second equality is exactly the alias identity (14). Therefore

\[
\left|
\sum_{q\in P_j}q^{-1-it_k}
-
\sum_{r\in R_j}r^{-1-it_k}
\right|
\ll
X_j^{-1}
\left(B_jK\eta+\Lambda^{-1}\right).
\tag{29}
\]

After summing the `K` bins,

\[
\max_{k<K}
\left|
\sum_{q\in P_Q}q^{-1-it_k}
-
\sum_{r\in R_Q}r^{-1-it_k}
\right|
\ll
\frac BQ
\left(
K\eta+\frac{K}{\Lambda B}
\right).
\tag{30}
\]

The exact Euler factors add only a lower-order remainder. At `Re(s)=1`,

\[
H_q(s)=q^{-s}+O(q^{-2}),
\tag{31}
\]

uniformly in `Im(s)`. Hence the local prime-power remainder is `O(B/Q^2)`, while the remote remainder is

\[
O\!\left(
\frac{\Lambda B}{(\Lambda Q)^2}
\right)
=
O\!\left(\frac{B}{\Lambda Q^2}\right).
\tag{32}
\]

Combining (30)--(32),

\[
\max_{k<K}|D_Q(1+it_k)|
\ll
\frac BQ
\left(
K\eta+
\frac{K}{\Lambda B}+
\frac1Q
\right).
\tag{33}
\]

Every factor in parentheses tends to zero. Since `B/Q asy d_Q`, this proves (9).

At `k=0`, the same estimate says the final value at `s=1` is `o(d_Q)`. But at every cutoff after the local shell and before the remote shell, only `P_Q` has appeared. Since `H_q(1)=1/q+O(1/q^2)`,

\[
\sum_{q\in P_Q}H_q(1)
\asymp \frac BQ
\asymp d_Q,
\tag{34}
\]

which proves the transient selector-scale debt (10).

## 4. The alias is compatible with honest multiplicities and KV fidelity

Give every prime in `P_Q` coefficient `+1` and every prime in `R_Q` coefficient `-1`. Relative to the ordinary-prime baseline multiplicity one, this means duplicating each local prime and deleting each remote prime. Reversing all signs simply swaps the roles. In either case all multiplicities remain in `{0,1,2}`.

The local Chebyshev excursion is at most

\[
O(B\log Q)=O(\sqrt Q),
\tag{35}
\]

while the remote excursion is at most

\[
O(\Lambda B\log(\Lambda Q))
=
\Lambda Q^{1/2+o(1)}.
\tag{36}
\]

For every fixed `b>0`,

\[
\sqrt Q=o(Qe^{-bV(Q)})
\tag{37}
\]

and, because `log Lambda=o(V(Q))`,

\[
\Lambda Q^{1/2+o(1)}
=o\!\left(\Lambda Qe^{-bV(\Lambda Q)}\right).
\tag{38}
\]

Between the two shells the discrepancy is only the local quantity (35), and after the remote shell the bound (36) is constant while the KV envelope grows. This proves (11).

Thus the alias is not purchased by leaving the ordinary-prime source class or by violating the source envelope. Its cost is geometric: the repair moves to a multiplicatively remote shell and uses `Lambda=Q^o(1)` times as many distinct ordinary primes there.

## Representation audit

The generic mechanism is standard Fourier aliasing after the logarithmic change of variables. Sampling `exp(-itx)` on the arithmetic grid `t_k=2pi k/W` identifies `x` only modulo `W`. Equivalently, Mellin phase on a commensurate vertical grid cannot distinguish multiplicative scales differing by `exp(mW)`.

That generic observation is not the line-specific result. The source-specific pullback is (22)--(38): the alias can be realized by actual ordinary primes, with integer `{0,1,2}` multiplicities, reciprocal mass at the selector scale `d_Q`, exact Euler factors rather than first-harmonic surrogates, and every fixed KV source envelope. This is the part relevant to `robin_extremal`.

`RE-200` therefore remains valid exactly as stated. Its singular-value theorem conditions the restriction of the observation operator to one fixed shell. `RE-201` shows that this restriction is not a global inverse estimate once multiplicatively separated source support is allowed.

## Adversarial self-review

**Is the alias only a first-harmonic artifact?** No. The higher Euler harmonics are bounded in (31)--(32) and are a factor `Q^-1` below the selector reciprocal scale. They do not restore stable separation on this packet.

**Does the construction require fractional multiplicity `Lambda`?** No. The remote population is the integer `N_j=round(Lambda B_j)`. The rounding loss is the `K/(Lambda B)` term in (33), which vanishes.

**Are there enough ordinary primes in the tiny bins?** Yes under exactly the same KV PNT regime as `RE-200`. The requested local population is `B/K=Q^(1/2-o(1))`, while a bin contains `eta Q/log Q=Q^(1-o(1))` primes. The remote request and availability both gain the factor `Lambda`.

**Can the large remote population violate the Chebyshev envelope?** No. Its total Chebyshev mass is only `Lambda Q^(1/2+o(1))`, whereas the available KV envelope at that scale is `Lambda Q^(1-o(1))`.

**Does this already reproduce the full `RE-188`/`RE-199` matched control?** No. The construction makes a selector-scale reciprocal/Euler debt transient and hides it from the commensurate vertical samples, but it does not simultaneously impose all exact Mertens/jet constraints of those findings or prove an order-one Robin destination displacement for this particular packet. It is a stable source-noncoercivity result for the proposed vertical frame, not a complete Robin countermodel.

**Could a different vertical sampling set avoid the alias?** Possibly. Exact shell periodicity comes from the arithmetic grid (1). Incommensurate or jittered heights destroy the exact identity (14). The next question is then quantitative: simultaneous Diophantine approximation may still create approximate remote aliases, but the required multiplicative distance could become large enough to conflict with source fidelity or the available repair geometry. That is not settled here.

## Prior-art audit

Fourier sampling aliasing and the Mellin/Fourier correspondence in logarithmic coordinates are classical. A targeted search found the expected generic literature on Mellin transforms, logarithmic sampling and Fourier aliasing, as well as analytic-number-theory work treating vertical Dirichlet polynomials as trigonometric sums. No external theorem from that literature is load-bearing here.

The only arithmetic input needed for the realization is the same Korobov--Vinogradov PNT estimate already anchored for this research line. Consequently `SOURCES.md` needs no new durable dependency.

## Literature status

The abstract alias identity (14) is elementary and classical. The useful line-specific statement is that the alias survives the pullback to honest ordinary-prime Euler factors at selector reciprocal scale, with exact integer multiplicities and KV fidelity. It exposes a concrete failure mode of using a single commensurate DFT panel as a global Robin source discriminator.

## Caveats

The result is approximate at scale `o(d_Q)`, not exact equality of the sampled Euler values. It uses a remote shell with multiplicative displacement `Lambda=Q^o(1)` and does not cover observation families that include a continuum of imaginary heights. It also does not claim that the chosen local packet by itself realizes the exact Robin destination functional used elsewhere in the line.

The theorem does not prove RH, Robin's inequality, a zero-free region or full source non-identifiability. It narrows the complex-sampling frontier by showing that the most natural commensurate vertical frame from `RE-200` still has selector-scale near-kernels once shell index is allowed to vary.

## Next experiment

Replace the arithmetic height grid by two incommensurate vertical panels, or by a deterministic jittered panel with the same `O(K)` height budget, and quantify the cheapest multiplicative shift `Lambda` for which all phases can be matched to selector-scale accuracy. The relevant problem is a simultaneous-approximation tradeoff between spectral irregularity, remote-shell distance, ordinary-prime population and KV fidelity.

If every `K=Theta(log Q)` bounded-height design still admits a `Lambda=Q^o(1)` selector-scale alias, the vertical scalar channel remains stably noncoercive even beyond the commensurate DFT representation. If suitably noncommensurate samples force `Lambda` to grow too fast, that would identify the first genuinely source-discriminating complex panel in this branch.

## Sources

- `RE-194`, for the selector reciprocal precision scale `d_Q~1/(sqrt(Q)log Q)`.
- `RE-200`, for the commensurate vertical DFT frame and the same KV prime-placement input.
- `RE-015`, for the standard Korobov--Vinogradov PNT envelope already anchored in `SOURCES.md`.
