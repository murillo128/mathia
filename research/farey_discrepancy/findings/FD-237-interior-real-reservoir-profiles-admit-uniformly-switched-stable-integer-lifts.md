# FD-237 — Interior real reservoir profiles admit uniformly switched-stable integer lifts

- **Date:** 2026-09-20
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response lattice / integer occupancy / response-space quantization / switched stability / source realizability
- **Depends on:** FD-236, FD-234, FD-226, FD-225
- **Classification:** `DERIVED + EXACT + INTEGER-LIFT + UNIMODULAR-DIVISOR-RESPONSE + SOURCE-REALIZATION + DISCRETENESS-NONOBSTRUCTION`

## Claim

FD-236 leaves two distinct issues on the physical side of the growing-block construction: the response topology must be refined below the natural quadratic capacity scale, and a coefficient-level real filling must ultimately be realized by integer prime occupancies. The second issue can be separated cleanly from the first.

On every finite divisor block the exact Mertens response map is an integer unimodular triangular transformation. Quantizing in **response coordinates**, rather than rounding the reservoir coefficients independently, therefore produces an integer occupancy vector whose coefficient displacement is only divisor-sized and whose switched-response displacement is uniformly bounded.

For `D>=1`, define

\[
(\mathscr A_D a)(m)
=
\sum_{d\le m}
 a(d)M\!\left(\left\lfloor\frac md\right\rfloor\right),
\qquad 1\le m\le D,
\tag{1}
\]

and set `y(0)=0` for any response vector `y=(y(1),...,y(D))`. Let `a in R^D`, write

\[
y=\mathscr A_D a,
\tag{2}
\]

choose nearest integers

\[
q(m)=\operatorname{nint}(y(m)),
\qquad q(0)=0,
\tag{3}
\]

with any fixed tie convention, and define

\[
\boxed{
 a^{\mathbb Z}(n)
 =
 \sum_{d\mid n}
 \bigl(q(d)-q(d-1)\bigr).
}
\tag{4}
\]

Then:

\[
\boxed{
 a^{\mathbb Z}\in\mathbb Z^D,
 \qquad
 \mathscr A_Da^{\mathbb Z}=q,
}
\tag{5}
\]

and, writing `tau(n)` for the divisor function,

\[
\boxed{
 |a^{\mathbb Z}(n)-a(n)|\le\tau(n)
 \qquad(1\le n\le D).
}
\tag{6}
\]

For the switched rows used in FD-225--FD-236,

\[
\mathcal R_j(h)
=
(E-I)^{r_j}(\mathscr A_Dh)(2^j),
\qquad r_j\in\{1,4\},
\tag{7}
\]

whenever the whole stencil satisfies `2^{j+r_j}<=D`, the quantization error obeys

\[
\boxed{
 |\mathcal R_j(a^{\mathbb Z}-a)|
 \le 2^{r_j-1}
 \le 8.
}
\tag{8}
\]

Thus the physical source response, which carries the factor `2` from a prime flip in the FD-226 reservoir model, changes by at most

\[
\boxed{16}
\tag{9}
\]

on every switched row. In particular, integerization preserves any `O(1)` switched target and is negligible for every future response normalization `S_{N,j}` with

\[
\min_{0\le j<J(N)}S_{N,j}\longrightarrow\infty.
\tag{10}
\]

There is also an exact box-lifting statement. Let `K_n` be integer reservoir capacities. If the real profile lies at least `tau(n)` inside every occupancy boundary,

\[
\boxed{
 \tau(n)\le a(n)\le K_n-\tau(n)
 \qquad(1\le n\le D),
}
\tag{11}
\]

then

\[
\boxed{
 0\le a^{\mathbb Z}(n)\le K_n
 \qquad(1\le n\le D).
}
\tag{12}
\]

Hence `a^Z` is a genuine integer reservoir filling. In the scale-adapted cells of FD-226, where

\[
K_n\asymp nL_N,
\qquad
L_N=\frac{N}{D\log N},
\tag{13}
\]

and `L_N->infinity`, the required relative boundary margin is only `O(1/L_N)`: the elementary bound `tau(n)<=n` already suffices. Therefore **integrality is not an additional asymptotic obstruction for reservoir profiles that remain even vanishingly far inside the physical capacity box**.

This does not solve the positive-lift problem of FD-232--FD-236. A candidate real filling may still be forced against the lower or upper capacity boundary, may fail because a physical cell does not contain enough free primes, or may violate source constraints not represented by independent reservoir counts. The result removes only the integer-lattice part of source realization. It shows that any surviving obstruction must be boundary/capacity/coherence-sensitive, not merely a consequence of replacing real coefficients by integer multiplicities.

## 1. The finite divisor-response matrix is unimodular

The matrix of `A_D` in the standard bases is lower triangular. Its `(m,d)` entry is

\[
M\!\left(\left\lfloor\frac md\right\rfloor\right)
\qquad(d\le m),
\]

and every diagonal entry is

\[
M(1)=1.
\]

Thus its determinant is one. More usefully, FD-225 gives the exact inverse for any finite response `y` with `y(0)=0`:

\[
\boxed{
(\mathscr A_D^{-1}y)(n)
=
\sum_{d\mid n}
\bigl(y(d)-y(d-1)\bigr).
}
\tag{14}
\]

The right side has integer coefficients. Consequently

\[
\mathscr A_D^{-1}(\mathbb Z^D)=\mathbb Z^D,
\]

so `A_D` is an integer unimodular change of lattice coordinates. Equation (4) is simply (14) applied to the integer response vector `q`; this proves (5).

This is the structural reason response-space quantization is preferable to independently rounding the occupancies. Independent coefficient rounding can create a response error whose size accumulates through the Mertens matrix. Rounding `y` first makes the response error uniformly at most `1/2` in every coordinate, and unimodularity then pulls that rounded response back to an integer coefficient vector automatically.

## 2. Pulling a half-unit response error back costs only `tau(n)`

Set

\[
e(m)=q(m)-y(m),
\qquad e(0)=0.
\tag{15}
\]

Nearest-integer rounding gives

\[
|e(m)|\le\frac12.
\tag{16}
\]

Since `a=A_D^{-1}y` and `a^Z=A_D^{-1}q`, formula (14) gives

\[
\begin{aligned}
 a^{\mathbb Z}(n)-a(n)
 &=
 \sum_{d\mid n}
 \Bigl(e(d)-e(d-1)\Bigr).
\end{aligned}
\tag{17}
\]

Every summand has absolute value at most one. There are `tau(n)` divisors, so

\[
|a^{\mathbb Z}(n)-a(n)|
\le
\tau(n),
\]

which proves (6). No analytic estimate for `M` is used: the loss is determined only by the exact divisor inverse.

FD-234 is the special case where the real response target is `-M(mN)/2`. There the same mechanism was written as the difference between the canonical real block-Mertens correction and its nearest-integer response repair. The present statement shows that the phenomenon is not special to that target: **every** real reservoir profile has a nearby integer profile obtained by quantizing its exact response.

## 3. Switched rows see only the original half-unit quantization error

Let

\[
h=a^{\mathbb Z}-a.
\]

By construction,

\[
\mathscr A_Dh=e.
\tag{18}
\]

Therefore, for any switched row whose full stencil remains inside `1,...,D`,

\[
\mathcal R_j(h)
=
(E-I)^{r_j}e(2^j).
\tag{19}
\]

Expanding the finite difference and using (16),

\[
\begin{aligned}
|\mathcal R_j(h)|
&\le
\frac12
\sum_{t=0}^{r_j}\binom{r_j}{t}\\
&=
2^{r_j-1}.
\end{aligned}
\tag{20}
\]

This proves (8). For the current scheduler `r_j in {1,4}`, the coefficient-level error is at most eight on every row, independently of `N`, `D`, `j`, the size of `a`, and the Mertens function.

In the source construction a selected free prime contributes twice the divisor response, so the corresponding physical switched perturbation is at most sixteen. Hence a real construction satisfying bounded switched rows remains a bounded switched construction after integerization. More generally, if a future finer quotient from the FD-236 frontier uses scales `S_{N,j}` satisfying (10), then

\[
\max_{j<J(N)}
\frac{|\mathcal R_j(a^{\mathbb Z}-a)|}{S_{N,j}}
\longrightarrow0.
\tag{21}
\]

Thus response-space integrality survives a much finer topology than the `L_N4^j` normalization ruled out by FD-236. Only a genuinely sub-unit or exact-response topology can detect this lattice quantization itself; an `O(1)` physical target can at most change its absolute constant.

## 4. Interior real fills lift to physical integer occupancies

Let the `n`th reservoir contain exactly `K_n` available primes, so a physically admissible occupancy count belongs to

\[
\{0,1,\ldots,K_n\}.
\]

Under (11), estimate (6) gives

\[
a^{\mathbb Z}(n)
\ge
 a(n)-\tau(n)
\ge0,
\]

and similarly

\[
a^{\mathbb Z}(n)
\le
 a(n)+\tau(n)
\le K_n.
\]

Together with integrality this proves (12). Because the FD-226 reservoirs are disjoint sets of free primes, an integer count in this interval is realized simply by choosing that many primes from the corresponding cell. The exact floor-table representation then gives precisely the integer response `q` constructed above.

For the scale-adapted reservoirs, write the uniform lower capacity bound as

\[
K_n\ge c\,L_Nn
\qquad(1\le n\le D)
\tag{22}
\]

for some fixed `c>0` in the FD-226 prime-resolution regime. Since

\[
\tau(n)\le n,
\tag{23}
\]

it is enough for a relative interior parameter `eta_N` to satisfy

\[
\eta_N cL_N\ge1
\tag{24}
\]

and

\[
\eta_NK_n
\le a(n)\le
(1-\eta_N)K_n.
\tag{25}
\]

When `L_N->infinity`, one may take `eta_N=O(1/L_N)`. Thus the lattice safety margin is asymptotically negligible compared with each reservoir capacity. Any fixed positive relative interior is far more than is needed.

This separates two notions that can otherwise be conflated. **Integer occupancy is cheap in the interior; reaching the interior may be hard.** The one-sided questions of FD-232--FD-236 concern precisely whether the arithmetic correction can be placed in, or lifted into, the positive capacity region while keeping the required fine switched response. The present theorem says that once such a real interior point has been found, converting it to actual multiplicities costs only a bounded switched perturbation.

## 5. Consequences for the current frontier

The result rules out one candidate explanation for the surviving gap between coefficient algebra and a physical source. The gap cannot be attributed merely to real versus integer reservoir coefficients as long as a real solution has divisor-sized coordinatewise slack.

It also sharpens the response-scale requirement left by FD-236. A future nonvacuous quotient must indeed be much finer than `L_N4^j`, but making it finer does not immediately resurrect an integrality obstruction. Any row scale tending to infinity uniformly still quotients out the integerization error, and the bounded-target regime of FD-225 remains stable up to an absolute constant. Therefore a source-level obstruction must use information that response rounding cannot erase: contact with a capacity face, shortage or correlation of free primes, or additional exact coherence between reservoir choices.

Conversely, the theorem does **not** say that every coefficient-level positive lift is physically realizable. If a proposed real profile has `a(n)<tau(n)` or `K_n-a(n)<tau(n)` on important cells, response quantization can cross a capacity boundary. Nor does it address source constraints that couple different reservoirs rather than merely bounding their independent occupancies. Those are now the discrete realization questions worth retaining.

## 6. Prior-art boundary and verdict

The algebra used here is classical. An integer triangular matrix with diagonal entries one is unimodular, and the explicit inverse (14) is the Möbius/divisor inversion already derived in FD-225. Nearest-integer quantization is elementary. No general novelty is claimed for either fact and no new external source is load-bearing.

The research-specific content is their combination with the exact FD-226 reservoir representation and the switched rows of the Farey-discrepancy construction: quantizing the **response** rather than the occupancy gives an integer source filling with divisor-sized coefficient error and a uniformly bounded switched error, while preserving the physical capacity box under an asymptotically negligible interior margin.

**Verdict.** Integer multiplicities are not an independent asymptotic obstruction for interior scale-adapted reservoir profiles. The divisor-response lattice is unimodular, so every real fill with `tau(n)` coordinatewise slack admits an integer lift that changes every current switched row by at most eight at coefficient level, or sixteen in the physical prime-flip response. After FD-236, the live obstruction therefore remains one-sided boundary/capacity/coherence control at a finer response scale, not coefficient integrality itself.