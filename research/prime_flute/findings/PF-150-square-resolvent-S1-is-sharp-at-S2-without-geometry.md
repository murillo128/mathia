# PF-150 — the square-resolvent `S_1` gate is abstractly sharp at `S_2`

**Status:** `EXACT-DERIVED + CLASSICAL-BOUNDARY + NEGATIVE/OBSTRUCTION`. PF-146 isolates the still-open global condition

\[
(P_1+1)^{-2}-(P_0+1)^{-2}\in\mathcal S_1
\]

as a sufficient route to complete wave operators for the exact prime flute and its exact all-composite shift clone. PF-147 shows by the Powers--Størmer/Birman--Koplienko--Solomyak square-root inequality that this condition forces the first relative resolvent into `\mathcal S_2`. The present finding proves that this implication is **abstractly sharp even inside the class of resolvents of nonnegative self-adjoint operators**: the square-resolvent `S_1` hypothesis alone cannot force `\mathcal S_r` for any `r<2`. Therefore the accepted sharp-Schatten clue's interval `1<r<2` cannot be settled by functional calculus from the PF-146 gate; any improvement below `2` must use additional geometric or differential structure of the prime/shift pair.

## Claim

There exist nonnegative self-adjoint operators `P_0,P_1` on a separable Hilbert space such that, with

\[
R_i=(P_i+1)^{-1},\qquad i=0,1,
\tag{1}
\]

one has

\[
\boxed{R_1^2-R_0^2\in\mathcal S_1,}
\tag{2}
\]

while simultaneously

\[
\boxed{
R_1-R_0\in\mathcal S_2
\quad\text{but}\quad
R_1-R_0\notin\mathcal S_r
\text{ for every }1\le r<2.
}
\tag{3}
\]

Thus no implication of the form

\[
R_1^2-R_0^2\in\mathcal S_1
\Longrightarrow
R_1-R_0\in\mathcal S_r
\tag{4}
\]

can hold for all nonnegative self-adjoint pairs when `r<2`.

The counterexample may be chosen diagonal and commuting. Hence the failure below `2` is not a noncommutativity artifact.

## 1. One diagonal sequence hits the endpoint exactly

Work on `\ell^2(\mathbb N)`. Put

\[
d_n:=\frac{1}{8\sqrt n\,\log(n+1)}.
\tag{5}
\]

Then `0<2d_n<1` for every `n`, and

\[
\sum_{n\ge1}d_n^2
=\frac1{64}\sum_{n\ge1}
\frac1{n\log^2(n+1)}
<\infty.
\tag{6}
\]

On the other hand, for every fixed `1\le r<2`,

\[
\sum_{n\ge1}d_n^r
=8^{-r}\sum_{n\ge1}
\frac1{n^{r/2}\log^r(n+1)}
=\infty.
\tag{7}
\]

For completeness, choose

\[
\varepsilon:=\frac{1-r/2}{2}>0.
\]

For all sufficiently large `n`, `\log^r(n+1)\le n^\varepsilon`; hence

\[
\frac1{n^{r/2}\log^r(n+1)}
\ge
n^{-(r/2+\varepsilon)},
\]

and

\[
r/2+\varepsilon
=\frac12+\frac r4<1.
\]

The comparison harmonic series therefore proves (7). Thus the same sequence lies in `\ell^2` but in no `\ell^r` with `1\le r<2`.

## 2. Realize the sequence as an actual resolvent pair

Define bounded positive diagonal operators

\[
R_0e_n=d_ne_n,
\qquad
R_1e_n=2d_ne_n.
\tag{8}
\]

Both are injective positive contractions. Define diagonal self-adjoint operators on their natural domains by

\[
P_i:=R_i^{-1}-1,
\qquad i=0,1.
\tag{9}
\]

Since `0<R_i\le1`, each `P_i` is nonnegative and self-adjoint, and by construction

\[
(P_i+1)^{-1}=R_i.
\tag{10}
\]

The first relative resolvent is simply

\[
R_1-R_0=\operatorname{diag}(d_n).
\tag{11}
\]

Its singular values are the `d_n`, so (6)--(7) give exactly (3).

Meanwhile

\[
R_1^2-R_0^2
=\operatorname{diag}(3d_n^2),
\tag{12}
\]

and therefore

\[
\|R_1^2-R_0^2\|_{\mathcal S_1}
=3\sum_{n\ge1}d_n^2<\infty.
\tag{13}
\]

This proves (2) and the claimed sharpness.

## 3. What this says about PF-146 and PF-147

PF-147 uses the classical square-root estimate

\[
\|R_1-R_0\|_{\mathcal S_2}^2
\le
\|R_1^2-R_0^2\|_{\mathcal S_1}
\tag{14}
\]

for positive bounded resolvents. The diagonal pair above shows that the exponent `2` cannot be lowered under the same hypothesis without adding structure: the left-hand side can fail every stronger Schatten condition `\mathcal S_r`, `r<2`, while the right-hand trace norm remains finite.

This is stronger than the purely logical statement that PF-147 did not prove the range `1<r<2`. It supplies a countermodel to **any attempt to obtain that range from the square-resolvent `S_1` assumption alone**.

The result also coexists with PF-148. The trace-class pair of squared resolvents in (12) has ordinary first-order Krein theory at the squared-transform level, while its first resolvent difference still fails every `\mathcal S_r` below `2`. Thus the existence of the invariant Krein/Birman--Krein phase supplied by a trace-class squared transform does not, by itself, improve the first-resolvent Schatten exponent.

## 4. Consequence for the accepted sharp-Schatten clue

For the actual prime/shift pair, PF-112 already fixes the lower endpoint

\[
R_1-R_0\notin\mathcal S_1.
\]

PF-146/PF-147 identify one possible route to `\mathcal S_2`: prove the **global** squared-resolvent difference trace class. PF-150 now proves that this route, even if successful, has no abstract functional-calculus mechanism capable of crossing below `2`.

Accordingly the accepted question

\[
R_1-R_0\stackrel{?}{\in}\mathcal S_r
\qquad(1<r<2)
\tag{15}
\]

is genuinely geometric. A positive proof must exploit information absent from the diagonal countermodel, for example the order-`-2` pseudodifferential structure on two-dimensional patches together with quantitative control of the infinite pants/collar/body assembly. Conversely, failure to derive `r<2` from PF-146 is no evidence that the actual prime/shift resolvent fails there.

This also sharpens the all-composite control. If the actual pair eventually satisfies `\mathcal S_r` for every `r>1`, membership in those ideals still cannot be a primality selector because the second member is the exact composite shift clone. The mathematical question would instead be whether the geometry gives a finer **relative** invariant inside that common ideal class.

## 5. Prior art and novelty audit

No new operator-ideal theorem is claimed. The square-root implication used in PF-147 is classical: Powers--Størmer and the broader Birman--Koplienko--Solomyak fractional-power estimates place a trace-class difference of positive squares in the Hilbert--Schmidt difference-of-square-roots regime. Those sources are already anchored in `SOURCES.md` as S18.

The diagonal construction above is elementary and should be regarded as an explicit sharpness witness for that classical exponent, specialized to the exact bounded-transform form used by PF-146/PF-147. Directed prior-art checks recover the standard fractional-power/Schatten theory rather than a new prime-flute theorem. The durable Mathia contribution is the **research boundary**:

\[
\boxed{
\text{global squared-resolvent }\mathcal S_1
\text{ can force }\mathcal S_2,
\text{ but cannot by itself force any }\mathcal S_r,
\ 1\le r<2.
}
\tag{16}
\]

The project-specific value is therefore negative and methodological: it prevents the open `1<r<2` prime/shift problem from being falsely closed by a stronger-looking resolvent-power trace-class statement.

## 6. Audit / falsification core

A later adversary can check the finding without any hyperbolic geometry:

1. verify `d_n in \ell^2` from the logarithmically improved harmonic series;
2. verify `d_n notin \ell^r` for every `1\le r<2` by the comparison in (7);
3. verify `0<R_i\le1`, so `P_i=R_i^{-1}-1` are legitimate nonnegative self-adjoint operators with resolvents exactly `R_i`;
4. compute `R_1-R_0=diag(d_n)` and `R_1^2-R_0^2=diag(3d_n^2)`;
5. conclude `S_1` for the square difference and simultaneous failure of every subquadratic Schatten class for the first difference;
6. keep the boundary honest: this counterexample refutes only an **abstract implication from the PF-146 gate alone** and says nothing negative about extra geometric estimates available for the actual prime/shift Laplacians.

## Consequence for the research line

The operator program now has a clean logical split:

```text
global squared-resolvent S1
    -> complete wave operators                    [PF-146]
    -> first relative resolvent S2                [PF-147]
    -> Krein/Birman-Krein phase via square        [PF-148]

but

    -/-> first relative resolvent S_r, 1 <= r < 2 [PF-150]
```

The remaining `1<r<2` Schatten window is therefore not a functional-calculus corollary waiting to be extracted from the squared-resolvent gate. It is a separate geometric/infinite-assembly problem, exactly as the accepted clue now requires.