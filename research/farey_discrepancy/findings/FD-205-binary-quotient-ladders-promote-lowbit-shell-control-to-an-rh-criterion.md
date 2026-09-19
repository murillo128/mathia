# FD-205 — Binary quotient ladders promote lowbit shell control to an RH criterion

- **Date:** 2026-09-19
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** cross-scale quotient alignment / mode-switching telescope / conditional RH criterion
- **Depends on:** FD-201, FD-204
- **Classification:** `EXACT-DERIVED + BINARY-QUOTIENT-LADDER + MODE-SWITCHED-SHELL-TELESCOPING + CONDITIONAL-RH-CRITERION`

## Claim

`FD-204` leaves two gaps: prove a physical Farey bound for the lowbit prime-shell energy, and explain how square-root control of its multiplicative-interval increments could recover absolute Mertens values. The second gap can be closed exactly.

Fix `r=2`, and let `\mathcal G_{2,H}^{\mathrm{lb}}` be the physical-Mobius lowbit energy defined in `FD-204`. If, for every `epsilon>0`,

\[
\boxed{
\mathcal G_{2,H}^{\mathrm{lb}}
=O_\epsilon(H^{1+\epsilon})
}
\tag{1}
\]

holds for all sufficiently large integer horizons `H`, then the Riemann hypothesis follows. More quantitatively, if for some fixed `A>=0`

\[
\boxed{
\mathcal G_{2,H}^{\mathrm{lb}}
=O\!\left(H\log^A H\right)
}
\tag{2}
\]

uniformly for all sufficiently large `H`, then

\[
\boxed{
M(N)
=O\!\left(
N^{1/2}\log^{(A+1)/2}N
\right).
}
\tag{3}
\]

The uniform-all-horizons hypothesis is stronger than necessary. For every sufficiently large integer `n`, choose once and for all a prime

\[
\frac n2<p_n\le n,
\tag{4}
\]

which exists by the prime number theorem, and define two source-independent horizons

\[
H_{n,0}:=np_n,
\qquad
H_{n,1}:=np_n+\frac{p_n+1}{2}.
\tag{5}
\]

For large `n`, `p_n` is odd. It is enough that (1), or respectively (2), hold only on the two-horizon family `H_(n,b)`, `b in {0,1}`.

The mechanism is an exact binary quotient ladder. At `H_(n,b)`, the prime `p_n` lies in the critical square-root shell of `FD-204` and satisfies

\[
\boxed{
\left\lfloor\frac{H_{n,b}}{p_n}\right\rfloor=n,
\qquad
\left\lfloor\frac{2H_{n,b}}{p_n}\right\rfloor=2n+b.
}
\tag{6}
\]

Therefore the native fixed-mode Farey sensor at that shell prime is exactly

\[
S_{2,H_{n,b}}(p_n)
=M(2n+b)-M(n).
\tag{7}
\]

Following the binary prefixes of an arbitrary target `N` makes these increments telescope to `M(N)`. The physical horizon and prime mode are allowed to change at every step; what is kept coherent is the **quotient coordinate**. Thus the outer recovery problem does not require one fixed prime to survive through an unbounded sequence of square-root shells.

This theorem does not prove (1) or (2). It shows that a critical-power analytic bound for the lowbit Farey energy would already be strong enough to imply RH, so after `FD-205` the missing bridge is concentrated in the physical energy estimate rather than in cross-scale recovery.

## 1. Every binary transition is realizable inside a critical prime shell

Fix a sufficiently large `n` and choose `p=p_n` as in (4). For a bit `b in {0,1}`, put

\[
h_0:=0,
\qquad
h_1:=\frac{p+1}{2},
\qquad
H:=np+h_b.
\tag{8}
\]

Because `0<=h_b<p`,

\[
\left\lfloor\frac Hp\right\rfloor=n.
\tag{9}
\]

If `b=0`, then `2h_b/p=0`; if `b=1`, then

\[
\frac{2h_b}{p}
=1+\frac1p,
\]

so in both cases

\[
\left\lfloor\frac{2H}{p}\right\rfloor
=2n+b.
\tag{10}
\]

It remains to check that this mode is actually visible in the square-root shell. Let

\[
K:=\lfloor\sqrt H\rfloor.
\]

Since `p<=n`,

\[
p^2\le np\le H,
\]

hence `p<=K`. On the other hand `p>n/2`, so `2p>n` and therefore, integrally, `n+1<=2p`. As `h_b<p`,

\[
H<p(n+1)\le2p^2.
\]

Thus `K<2p`, equivalently `p>K/2`. We have proved

\[
\boxed{
K/2<p\le K.
}
\tag{11}
\]

The same inequalities also give a useful scale comparison. Because

\[
H<p(n+1)\le n(n+1)<(n+1)^2,
\]

we have `K<=n`, while (11) and `p>n/2` give `K>n/2`. Hence

\[
\boxed{K\asymp n}
\tag{12}
\]

with absolute constants.

Equation (7) now follows directly from the exact prime-row identity of `FD-201`. No source inversion or approximation is involved: `S_(2,H)(p)` is the centered fixed-mode difference of the native signed Farey/divisor coefficients at horizons `H` and `2H`.

## 2. Critical lowbit energy gives square-root bounds for every binary transition

For the prime shell of the horizon `H`, let `m` be its number of primes. `FD-204` proves the exact point-evaluation estimate

\[
|S_{2,H}(p)|^2
\le
\left(1+\lfloor\log_2m\rfloor\right)
N_{\mathrm{lb}}(S)
=
\left(1+\lfloor\log_2m\rfloor\right)
\frac{\mathcal G_{2,H}^{\mathrm{lb}}}{K}.
\tag{13}
\]

Since `m<=K`, the resistance factor is `O(log K)`. Also `K^2<=H<(K+1)^2`, so

\[
\frac HK=O(K).
\tag{14}
\]

Under the explicit polylogarithmic hypothesis (2), equations (12)--(14) therefore give, uniformly in the chosen bit,

\[
\begin{aligned}
|M(2n+b)-M(n)|^2
&=|S_{2,H_{n,b}}(p_n)|^2\\
&\ll
(\log K)\frac{H\log^A H}{K}\\
&\ll
n\log^{A+1}n.
\end{aligned}
\tag{15}
\]

Thus

\[
\boxed{
|M(2n+b)-M(n)|
\ll
n^{1/2}\log^{(A+1)/2}n.
}
\tag{16}
\]

The power-scale version is identical. If (1) holds, then for any target `delta>0` choose the energy exponent small enough that the extra factor from `H^epsilon` together with `log K` is absorbed into `n^(2delta)`. This yields

\[
\boxed{
|M(2n+b)-M(n)|
=O_\delta(n^{1/2+\delta})
}
\tag{17}
\]

for both bits and all sufficiently large `n`.

The important point is that (16)--(17) hold for **both possible next binary digits**. Control only of the doubling increment `M(2n)-M(n)` would reach powers of two and their fixed multiples, but would not recover arbitrary Mertens values. The second digit-realizing horizon in (5) removes exactly that gap.

## 3. Binary prefixes telescope to the absolute Mertens function

Write an arbitrary positive integer `N` in binary as

\[
N=(1b_1b_2\cdots b_T)_2,
\qquad b_j\in\{0,1\}.
\]

Define its successive binary prefixes by

\[
n_0:=1,
\qquad
n_j:=2n_{j-1}+b_j
\quad(1\le j\le T).
\tag{18}
\]

Then `n_T=N`, and exactly

\[
M(N)
=M(n_J)
+
\sum_{j=J+1}^{T}
\bigl(M(n_j)-M(n_{j-1})\bigr)
\tag{19}
\]

for any fixed prefix index `J`. Choose `J` after the finitely many small prefixes for which the asymptotic energy hypothesis or the prime selector is not yet available; `M(n_J)` is then an absorbed constant.

Each summand in (19) has the form controlled by (16), with `n=n_(j-1)` and `b=b_j`. Moreover, if `k=T-j+1` binary digits remain after the prefix `n_(j-1)`, then

\[
n_{j-1}
=\left\lfloor\frac{N}{2^k}\right\rfloor
\le\frac{N}{2^k}.
\tag{20}
\]

Therefore the square-root costs form a convergent geometric series:

\[
\sum_{j=J+1}^{T} n_{j-1}^{1/2}
\le
N^{1/2}\sum_{k\ge1}2^{-k/2}
=O(N^{1/2}).
\tag{21}
\]

Using `log n_(j-1)<=log N` in (16), equations (19)--(21) give precisely

\[
M(N)
=O\!\left(
N^{1/2}\log^{(A+1)/2}N
\right),
\]

which proves (3).

Likewise, (17) and the same geometric telescope give

\[
M(N)=O_\delta(N^{1/2+\delta})
\]

for every `delta>0`. By the classical Littlewood--Mertens criterion anchored in `SOURCES.md`, this is equivalent to the Riemann hypothesis. Hence (1) implies RH.

## 4. What the criterion changes

`FD-204` correctly stopped short of an RH consequence because one shell controls increments

\[
M\!\left(\left\lfloor\frac{2H}{p}\right\rfloor\right)
-
M\!\left(\left\lfloor\frac H p\right\rfloor\right),
\]

not absolute values. A naive attempt to telescope with one fixed prime is geometrically doomed: a fixed `p` belongs to a square-root shell only while `H` stays within a bounded multiplicative range around `p^2`.

The binary ladder shows that fixed-mode persistence is unnecessary. At each step one reselects a prime `p_n\asymp n` and a horizon `H\asymp n^2` so that the **quotient endpoints**, rather than the physical mode, match the next binary prefix. The transition

\[
n\longmapsto 2n+b
\]

is realized exactly by floors, and the critical shell condition survives the reselection. Thus the source increments from different physical horizons compose without any interpolation error.

This closes the finite/cross-scale recovery half of the post-`FD-204` program. A uniform critical-power estimate for `\mathcal G_(2,H)^lb` is now not merely suggestive of RH-sized local cancellation: it is a sufficient RH criterion. In particular, the squarefree Rademacher benchmark `E \mathcal G_(2,H)^lb=O(H\log H)` from `FD-204` sits at the correct power scale for the criterion. That expectation is only a comparator; it gives no deterministic bound for the physical Mobius source and is not evidence that (1) holds.

The criterion is also deliberately one-way. RH by itself supplies pointwise `M(x)=O_epsilon(x^(1/2+epsilon))`, but that does not automatically control the correlated multiscale lowbit energy at size `H^(1+o(1))`. No converse is claimed.

## 5. Representation, prior-art and boundary audits

The representation audit is clean. The chosen horizons and prime modes depend only on the target integer and prime locations, never on observed Mobius values. Each transition is read directly from the centered fixed-mode Farey coefficient identity of `FD-201`, and the lowbit norm is the same transform-side projection audited in `FD-204`. The cross-scale telescope occurs only after these exact physical observations have been identified with quotient-coordinate increments.

The only external analytic inputs are already anchored in `SOURCES.md`: the prime number theorem supplies a prime in `(n/2,n]` for all sufficiently large `n`, and Titchmarsh's standard Littlewood criterion converts the final `M(N)=O_epsilon(N^(1/2+epsilon))` estimate into RH. A targeted prior-art search around Farey--Mertens formulas, Mertens increment criteria, dyadic/binary Mertens decompositions and RH criteria found the classical Farey/Mertens literature and the standard Mertens growth criterion, but no direct use of source-independent prime-shell horizon reselection to realize both binary transitions and telescope the `FD-204` observation family. The binary-prefix argument and prime-in-a-half-interval input themselves are elementary; novelty is claimed only for their combination with this exact Farey prime-shell sensor.

The assumptions must remain uniform in the required horizon family. An averaged, Cesaro, density-one or random-expectation bound for `\mathcal G_(2,H)^lb` does not provide the transition estimate for every binary prefix and therefore does not imply the theorem as stated. Likewise, controlling only one of the two bits is insufficient for arbitrary targets.

No clue status changes. The accepted local clues concern different ordering or Jordan-occupation mechanisms. No formalization issue is opened: the finite binary-transition lemma is elementary, while the substantive unresolved input is the analytic physical-energy estimate.

## Conclusion

The remaining cross-scale obstruction after `FD-204` is not intrinsic. Every binary Mertens transition `M(2n+b)-M(n)` can be realized exactly by a prime mode lying in a critical square-root Farey shell at a source-independent horizon `H\asymp n^2`. Binary prefixes then telescope those shell increments to every absolute `M(N)`, with only a geometric summation cost.

Consequently a uniform critical-power bound `\mathcal G_(2,H)^lb=H^(1+o(1))` would imply the RH-scale Mertens estimate and hence RH. The live bottleneck is now singular: prove, from Farey arithmetic itself, a deterministic `H^(1+o(1))` bound for the physical lowbit multiscale energy (or identify why that target is false).