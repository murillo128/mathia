# FD-213 — Dyadic-band profile lifting preserves switched blindness at every integer

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** all-integer switched root filter / dyadic-band profile lifting / bounded-source countermodel / cross-ray coherence boundary
- **Depends on:** FD-206, FD-208, FD-212
- **Classification:** `EXACT-DERIVED + ALL-INTEGER-SWITCHED-NULL + BOUNDED-SOURCE-REALIZATION + DYADIC-MANTISSA-SEPARATION + CRITICAL-RANDOM-COST + REPRESENTATION-BOUNDARY`

## Claim

`FD-212` constructed a bounded source whose period-three switched root filter vanishes on one dyadic ray while its summatory function grows strictly faster than square root. Its decisive open test was whether imposing the same diagonal estimate at **every integer** would couple different dyadic rays strongly enough to kill that Floquet mode.

For the natural dyadic-band extension of the `FD-212` schedule, it does not.

Let

\[
\Delta_A(n):=A(2n)-A(n),
\qquad
\mathcal C_q^A(n):=(T-I)^q\Delta_A(n)=(T-I)^{q+1}A(n),
\qquad
(TF)(n):=F(2n).
\tag{1}
\]

Define the source-independent depth schedule on **all** positive integers by

\[
q(n)=q_j,
\qquad
j=\lfloor\log_2 n\rfloor,
\qquad
q_j=
\begin{cases}
0,&j\equiv0\pmod3,\\
3,&j\equiv1,2\pmod3.
\end{cases}
\tag{2}
\]

Then there exists a real source `(u_m)` with

\[
|u_m|\le1,
\qquad
A(N):=\sum_{m\le N}u_m,
\tag{3}
\]

such that

\[
\boxed{
\mathcal C_{q(n)}^A(n)=0
\qquad\text{for every }n\ge1,
}
\tag{4}
\]

while along an explicit interior point of every third dyadic band,

\[
N_m:=3\,2^{3m-1},
\tag{5}
\]

one has

\[
\boxed{
|A(N_m)|\asymp N_m^\alpha,
\qquad
\alpha=\frac43\log_2\!\frac{1+\sqrt5}{2}
\approx0.9256558848>\frac12.
}
\tag{6}
\]

Thus the remaining all-integer opening after `FD-212` is not closed by additive/summatory coherence alone. A bounded source can realize the same supercritical switched Floquet multiplier while annihilating the selected diagonal root filter at **every integer**, not merely at powers of two.

The mechanism is a general profile-lifting fact: dyadic dilation preserves the mantissa `n/2^floor(log2 n)`. Any sublinear-growth null mode on the scale index can therefore be tensored with a Lipschitz profile that vanishes at the two band endpoints. The endpoint zeros stitch neighboring bands with uniformly bounded source increments, while the dilation recurrence remains purely in the scale coordinate.

This remains a representation-boundary result, not a Möbius counterexample. The source below is bounded but not asserted to be squarefree-supported or multiplicative. Consequently (4)--(6) show that **bounded increments plus all-integer observation are insufficient** for the scale-varying diagonal criterion; they do not show that the physical Möbius source can realize the blind mode.

## 1. A profile-lifting lemma for dyadic switched recurrences

Let `(r_j)_(j>=0)` be positive integers and let `(a_j)` satisfy

\[
(E-I)^{r_j}a_j=0,
\qquad
(Ea)_j=a_{j+1},
\tag{7}
\]

for every `j`. Assume also that for some constants `C>0` and `rho<2`,

\[
|a_j|\le C\rho^j.
\tag{8}
\]

Let `h:[1,2]->R` be any nonzero Lipschitz function with

\[
h(1)=h(2)=0.
\tag{9}
\]

For an integer `N>=1`, write

\[
j(N):=\lfloor\log_2N\rfloor,
\qquad
t(N):=\frac{N}{2^{j(N)}}\in[1,2).
\tag{10}
\]

Define

\[
\boxed{
A(N):=\varepsilon\,a_{j(N)}h(t(N)),
\qquad A(0):=0,
}
\tag{11}
\]

where `epsilon>0` will be chosen below.

The key identity is exact. If `n` belongs to the dyadic band `[2^j,2^(j+1))`, then for every `k>=0`,

\[
j(2^kn)=j+k,
\qquad
t(2^kn)=t(n).
\tag{12}
\]

Hence

\[
T^kA(n)=\varepsilon a_{j+k}h(t(n)),
\tag{13}
\]

and therefore

\[
\boxed{
(T-I)^{r_j}A(n)
=
\varepsilon h(t(n))(E-I)^{r_j}a_j
=0
}
\tag{14}
\]

for **every** integer in band `j`.

It remains to show that (11) is the summatory function of a uniformly bounded source. Let `L` be a Lipschitz constant for `h`. If `N` and `N-1` lie in the same band `j`, then

\[
|A(N)-A(N-1)|
\le
\varepsilon |a_j|\frac{L}{2^j}
\le
\varepsilon CL\left(\frac\rho2\right)^j.
\tag{15}
\]

At a band boundary `N=2^j`, equation (9) gives `A(N)=0`. The preceding integer lies in band `j-1` with mantissa

\[
2-2^{-(j-1)},
\]

so again by (9) and Lipschitz continuity,

\[
|A(2^j-1)|
\le
\varepsilon |a_{j-1}|L\,2^{-(j-1)}
\le
\varepsilon CL\left(\frac\rho2\right)^{j-1}.
\tag{16}
\]

Because `rho/2<1`, the right sides of (15)--(16) are uniformly bounded in `j`. Choosing `epsilon` small enough makes

\[
|A(N)-A(N-1)|\le1
\qquad(N\ge1).
\tag{17}
\]

Thus

\[
u_N:=A(N)-A(N-1)
\tag{18}
\]

defines a genuine bounded source with `|u_N|<=1` and summatory function `A`.

This lemma isolates why all-integer additive coherence is weaker than it first appears. The dilation operator does not mix dyadic mantissas. The only coupling needed to turn independently scaled band profiles into one summatory function occurs at adjacent integers, and endpoint zeros remove the potentially growing boundary jump.

## 2. Apply the lemma to the FD-212 Floquet mode

`FD-212` gives the period-three recurrence

\[
(E-I)^{r_j}a_j=0,
\qquad
(r_j)=(1,4,4,1,4,4,\ldots),
\tag{19}
\]

with Floquet form

\[
a_{3m}=\lambda^m,
\qquad
a_{3m+1}=\lambda^m,
\qquad
a_{3m+2}=c_2\lambda^m,
\tag{20}
\]

where

\[
\lambda=-\frac{7+3\sqrt5}{2}=-\varphi^4,
\qquad
c_2=-\frac{5+3\sqrt5}{10},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\tag{21}
\]

Its per-dyadic-step growth is

\[
\rho=|\lambda|^{1/3}=\varphi^{4/3}\approx1.89954762695<2,
\tag{22}
\]

so the hypothesis (8) holds. Choose the concrete profile

\[
\boxed{
h(t)=(t-1)(2-t).}
\tag{23}
\]

It is Lipschitz on `[1,2]`, vanishes at both endpoints, and satisfies `h(3/2)=1/4`. The profile-lifting lemma therefore produces a bounded source for which, with `r_j=q_j+1`,

\[
\mathcal C_{q(n)}^A(n)
=(T-I)^{r_{j(n)}}A(n)=0
\tag{24}
\]

for every positive integer `n`. This proves (4).

To retain the supercritical growth, take the interior point

\[
N_m=3\,2^{3m-1}=\frac32\,2^{3m}.
\tag{25}
\]

It lies in band `j=3m` with mantissa exactly `3/2`, so

\[
A(N_m)
=
\frac\varepsilon4\lambda^m.
\tag{26}
\]

Since

\[
|\lambda|^m=(2^{3m})^\alpha,
\qquad
\alpha=\log_2\rho,
\tag{27}
\]

and `N_m` is a fixed multiple of `2^(3m)`, equations (26)--(27) give (6).

The fact that `A(2^j)=0` is deliberate, not a loss: the endpoint zeros are what make the all-integer summatory realization uniformly Lipschitz. The supercritical mass lives at fixed interior mantissa instead of at the dyadic endpoints.

## 3. The random-cost audit is unchanged

The all-integer schedule (2) is exactly the dyadic-band extension already identified in `FD-212`. It uses only depths `q=0` and `q=3`, with Delannoy coefficient masses

\[
D_0=1,
\qquad
D_3=63.
\tag{28}
\]

By the exact squarefree-Rademacher calculation of `FD-208` quoted in `FD-212`, the root-aligned normalization therefore still satisfies

\[
\boxed{
\mathbb E\!\left[K_n|\mathcal C_{q(n)}^f(n)|^2\right]
=\Theta(H_n).
}
\tag{29}
\]

Nothing in the profile lift pays a growing coefficient or random-energy tariff. The all-integer blind construction stays inside the same critical-random-cost regime as the sparse-ray one.

This matters for the Farey representation boundary. `FD-206--208` identify these dyadic Mertens/root filters with signed combinations of source-independent root-aligned Farey sensors. The obstruction is therefore not created by moving to an unrelated abstract transform: it occurs in the same dilation family that was introduced to avoid the positive-energy overcoercion of `FD-198--206`.

## 4. What the all-integer countermodel rules out

The next test stated in `FD-212` has a definitive bounded-source answer. **Cross-ray additive coherence does not kill the switched Floquet mode.** The reason is structural: doubling preserves the normalized position inside a dyadic band, so a switched scale recurrence and a within-band profile separate exactly.

Consequently no argument can prove a scale-varying diagonal RH criterion for all bounded sources from only the following ingredients:

1. `|u_n|=O(1)` or equivalently a uniformly Lipschitz summatory function;
2. pointwise control of the selected root filter at every integer;
3. the dyadic dilation geometry encoded by `T`;
4. critical random cost of the selected filters.

The construction satisfies stronger data than a square-root estimate: its selected observable is identically zero at every integer while its summatory function has exponent `alpha>1/2`.

What remains open is therefore genuinely arithmetic. The physical Möbius source has squarefree support and a global multiplicative compatibility absent from (18). An all-integer diagonal criterion for Möbius could still be valid, but any proof must now use such Möbius-specific structure, or impose a scheduler whose dependence on `n` genuinely mixes dyadic mantissas rather than depending only on the band index `floor(log2 n)`.

This also separates the new obstruction from `FD-211`. A fixed finite family controlled simultaneously at every scale is square-root complete when its gcd has no annular root. Here the same two harmless filters are still selected one at a time, and the selection pattern is constant across each dyadic band. The tensor lift preserves the switched monodromy everywhere because simultaneous control is never restored.

## 5. Prior-art and novelty boundary

The surrounding mathematics is classical. Periodic-coefficient difference equations and Floquet multipliers provide the scale-index viewpoint already noted in `FD-212`. Dilation/refinement equations likewise exploit the fact that dyadic scaling separates scale from a normalized within-cell coordinate, and their regularity is classically related to transition matrices and spectral radii; see, for example, Colella--Heil, *Characterizations of Scaling Functions: Continuous Solutions*, SIAM J. Matrix Anal. Appl. (DOI `10.1137/S0895479892225336`). Discrete scale invariance and log-periodic power-law profiles are also standard themes; see Sornette, *Discrete-scale invariance and complex dimensions*, Phys. Rep. 297 (1998).

The prior-art search found no direct treatment of the present all-integer switched root-sensor problem, the `(0,3,3)` Farey/Mertens schedule, or the endpoint-zero profile lift used to realize its supercritical Floquet mode as a bounded summatory source. No external theorem is load-bearing here: equations (12)--(17) prove the lifting directly, so no new durable source anchor is required.

Novelty is claimed only for that exact specialization and consequence. In particular, this is not a claim that tensor-product constructions for dilation equations or switching-induced instability are new in general.

## 6. Falsification and audit boundary

The proof has three exact points that should be checked independently.

First, for every integer `n` in band `j`, verify that all numbers `2^k n` remain at the same dyadic mantissa and move to bands `j+k`; any floor failure in (12) would break the all-integer lift.

Second, verify both increment cases (15)--(16). The condition `rho<2` is essential. If the Floquet multiplier had per-step modulus at least `2`, the profile construction would no longer guarantee a uniformly bounded source merely from Lipschitz endpoint vanishing.

Third, substitute (20)--(21) into the phase pattern `(1,4,4)` from `FD-212`. No new characteristic polynomial is introduced here; the present result inherits exactly the previously proved switched recurrence and changes only its source realization.

A numerical sanity check of the explicit choice (23), using `epsilon=0.1`, gave maximum switched-filter residual below `1.4e-13` for `1<=n<5000` in double precision and maximum source increment below `0.075` on the same range. This is only a check of the formulas, not evidence needed by the proof.

The construction does **not** satisfy Möbius multiplicativity, does not claim ternary coefficients, and does not touch the accepted or resolved local clues. It should not be used to infer failure of any physical Möbius estimate. Its precise consequence is narrower: the `FD-212` cross-ray-coherence escape is closed for the bounded-source relaxation, so the next nontrivial gate is multiplicative/squarefree source fidelity or a genuinely mantissa-mixing observation rule.
