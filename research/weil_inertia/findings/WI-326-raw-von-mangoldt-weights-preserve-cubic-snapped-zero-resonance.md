# WI-326 — raw von Mangoldt weights preserve the cubic snapped-zero resonance

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

WI-325 showed that the cubic endpoint-carrier resonance from WI-324 survives after the resonant height is snapped to the ordinate of an actual nontrivial zeta zero. Its main remaining source-side caveat was arithmetic weighting: a coherent bare carrier need not remain coherent after inserting von Mangoldt coefficients.

For the **raw positive von Mangoldt weights**, that escape also fails. There are infinitely many integers `M` for which one can choose an actual zeta-zero ordinate `\gamma_M` in the WI-325 snapped interval and a block length

\[
\ell_M\asymp M^{1/3}
\]

such that

\[
\boxed{
\left|
\sum_{1\le j\le \ell_M}
\Lambda(M+j)
 e\!\left(
 \frac{\gamma_M}{2\pi}
 \log\frac{M+j}{M}
 \right)
\right|
\gg M^{1/3}.
}
\]

After the natural square-root normalization one also has

\[
\boxed{
\left|
\sum_{1\le j\le \ell_M}
\frac{\Lambda(M+j)}{\sqrt{M+j}}
 e\!\left(
 \frac{\gamma_M}{2\pi}
 \log\frac{M+j}{M}
 \right)
\right|^2
\gg M^{-1/3},
}
\]

whereas the diagonal energy of the same block is at most

\[
\sum_{1\le j\le \ell_M}
\frac{\Lambda(M+j)^2}{M+j}
\ll M^{-2/3}\log^2 M.
\]

Thus the coherent raw-prime-weighted contribution can exceed its own diagonal scale by a factor tending to infinity at least as fast as

\[
\frac{M^{1/3}}{\log^2 M}.
\]

The point is not that the full BOW source is resonant. The actual Gallagher/BOW coefficient is signed and contains additional structure. The result instead closes a weaker route: **neither actual zero-ordinate membership nor insertion of positive raw von Mangoldt weights is enough to force cancellation of the WI-325 cubic resonance.** Any successful source-side cancellation theorem must use information absent from this model, such as the signed subtraction in `\Lambda-\Lambda^\sharp`, an additional source factor, cancellation with the rest of the natural window, or stronger arithmetic structure.

## 1. A cubic block with positive von Mangoldt mass

Let `X` run through sufficiently large integers and put

\[
\ell=\left\lfloor\frac{X^{1/3}}8\right\rfloor.
\tag{1}
\]

For integers

\[
X\le M\le \left\lfloor\frac{3X}{2}\right\rfloor
\]

define

\[
S(M):=\sum_{1\le j\le\ell}\Lambda(M+j).
\tag{2}
\]

Double-counting the pairs `(M,j)` gives

\[
\sum_M S(M)
=
\sum_n \Lambda(n)
\#\left\{
M:
X\le M\le\left\lfloor\frac{3X}{2}\right\rfloor,
\ 1\le n-M\le\ell
\right\}.
\tag{3}
\]

For every integer `n` in the interior interval

\[
X+\ell\le n\le\left\lfloor\frac{3X}{2}\right\rfloor,
\]

all `\ell` choices `M=n-j`, `1\le j\le\ell`, lie in the allowed `M`-range. Hence

\[
\sum_M S(M)
\ge
\ell\left(
\psi\!\left(\left\lfloor\frac{3X}{2}\right\rfloor\right)
-
\psi(X+\ell-1)
\right).
\tag{4}
\]

The classical prime number theorem in the form

\[
\psi(x)=x+o(x)
\tag{5}
\]

and `\ell=o(X)` give

\[
\sum_M S(M)
\ge
\left(\frac12+o(1)\right)X\ell.
\tag{6}
\]

There are only `(1/2+o(1))X` admissible values of `M`. Therefore at least one of them satisfies

\[
S(M)\ge(1-o(1))\ell,
\tag{7}
\]

and in particular, for all sufficiently large `X`, one can choose `M=M_X` with

\[
\boxed{S(M)\ge\frac\ell2.}
\tag{8}
\]

Taking, for example, a sequence of `X` whose intervals `[X,3X/2]` are pairwise disjoint produces infinitely many such `M`.

This step uses no short-interval prime theorem. The block carrying the mass is selected by averaging ordinary PNT mass over a macroscopic family of starting points.

## 2. Transfer through the WI-325 snapped zero

For each sufficiently large selected `M`, WI-325 supplies an actual nontrivial zeta-zero ordinate `\gamma_M` with

\[
2\pi M\left(M+\frac12\right)
<\gamma_M
\le
2\pi M\left(M+\frac12\right)+2
\tag{9}
\]

and proves that, for

\[
0\le j<L_M,
\qquad
L_M:=\left\lfloor\frac{M^{1/3}}4\right\rfloor,
\tag{10}
\]

the relative carrier

\[
C'_M(j):=
 e\!\left(
 \frac{\gamma_M}{2\pi}
 \log\frac{M+j}{M}
 \right)
\tag{11}
\]

obeys

\[
\Re C'_M(j)>\frac12.
\tag{12}
\]

Because `M\ge X`, equation (1) gives

\[
\ell\le\frac{X^{1/3}}8
\le\frac{M^{1/3}}8<L_M
\tag{13}
\]

for all sufficiently large `X`. Therefore (12) holds for every `1\le j\le\ell` in the positive-mass block selected above.

Since `\Lambda(n)\ge0`, there is no coefficient-sign cancellation inside that block. Equations (8) and (12) yield

\[
\begin{aligned}
\left|
\sum_{j=1}^{\ell}\Lambda(M+j)C'_M(j)
\right|
&\ge
\Re\sum_{j=1}^{\ell}\Lambda(M+j)C'_M(j)\\
&>
\frac12 S(M)\\
&\ge\frac\ell4.
\end{aligned}
\tag{14}
\]

As `M\in[X,3X/2]`, one has `\ell\asymp M^{1/3}` along the selected sequence. Hence

\[
\boxed{
\left|
\sum_{j=1}^{\ell}\Lambda(M+j)C'_M(j)
\right|
\gg M^{1/3}.
}
\tag{15}
\]

The common factor `M^{i\gamma_M}` omitted by the relative normalization has modulus one, so (15) is equally a statement about the corresponding block of the carrier `n^{i\gamma_M}`.

## 3. Square-root normalization beats the block diagonal scale

Set

\[
W_M:=
\sum_{j=1}^{\ell}
\frac{\Lambda(M+j)}{\sqrt{M+j}}C'_M(j).
\tag{16}
\]

Again using positivity and (12),

\[
|W_M|
\ge
\Re W_M
>
\frac{S(M)}{2\sqrt{M+\ell}}
\ge
\frac{\ell}{4\sqrt{M+\ell}}.
\tag{17}
\]

Therefore

\[
\boxed{|W_M|^2\gg M^{-1/3}.}
\tag{18}
\]

For comparison, the diagonal energy of exactly the same weighted block is

\[
E_M:=
\sum_{j=1}^{\ell}
\frac{\Lambda(M+j)^2}{M+j}.
\tag{19}
\]

For large `M`, `M+j<2M` on this block, while the elementary bound `\Lambda(n)\le\log n` gives

\[
E_M
\le
\frac{\ell\log^2(2M)}{M}
\ll M^{-2/3}\log^2 M.
\tag{20}
\]

Combining (18) and (20),

\[
\boxed{
\frac{|W_M|^2}{E_M}
\gg
\frac{M^{1/3}}{\log^2 M}
\longrightarrow\infty.
}
\tag{21}
\]

Here `E_M>0` for the selected blocks because (8) makes `S(M)>0`. Thus the ratio is well defined.

Equation (21) is a useful stress test for any proposed argument that tries to obtain the distinguished-twist saving merely by comparing a raw von-Mangoldt-weighted twisted sum with its diagonal `L^2` mass. On these selected snapped-zero blocks, the coherent square is parametrically larger than that diagonal scale.

## 4. What this rules out, and what it does not

The obstruction is deliberately source-specific but still narrower than the full BOW problem.

It **does rule out** the proposed weak mechanism in which the WI-325 resonance was expected to disappear automatically after inserting positive raw von Mangoldt weights. PNT guarantees that among the resonant starting positions there are infinitely many cubic subblocks carrying the expected total von Mangoldt mass, and the WI-325 sector control then turns positivity of those coefficients into coherence rather than cancellation.

It **does not** establish resonance for the actual signed/smoothed BOW source. In particular:

- the live source problem contains the signed subtraction `\Lambda-\Lambda^\sharp`; cancellation between its components is not modeled here;
- no additional coefficient or source factor from the exact BOW reduction is inserted unless it is identically positive and slowly varying enough to preserve the argument, which is not assumed here;
- (15)--(21) concern a cubic coherent subblock, not the complete Gallagher/BOW interval, so terms outside the subblock could cancel it;
- the zero `\rho_M` whose ordinate is `\gamma_M` need not be an off-critical bow zero;
- no lower bound for the complete distinguished twisted covariance follows.

Accordingly, this finding does not close the live distinguished-twist clue. It removes one more generic escape and sharpens the remaining gate: any cancellation theorem must exploit **signed source structure, the full-window geometry, or a relation specific to the selected bow zero beyond its ordinate and raw prime mass**.

## 5. Evidence and prior-art boundary

The ingredients have separate provenance.

1. The snapped-zero sector estimate (9)--(12) is the exact line-local result WI-325, itself based on WI-324's logarithmic Taylor resonance and the explicit zero-count theorem of Hasanalizade--Shen--Wong already anchored for this line.
2. The only new external theorem used here is the classical prime number theorem `\psi(x)=x+o(x)`. The averaging argument (3)--(8), its insertion into the WI-325 sector, and the diagonal comparison (16)--(21) are exact deductions.
3. No claim is made that the displayed selected-height phenomenon is absent from the broader exponential-sum literature. A bounded prior-art audit over von-Mangoldt-weighted logarithmic-phase sums and short exponential sums over primes found extensive generic cancellation literature but no source needed for this exact line-specific deduction. That absence is not used as a priority claim.

The result is therefore recorded as `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`: exact relative to WI-325 and classical PNT, and decisive only against the weak route described above.

## Research consequence

Do not expect positive raw prime weights to de-exceptionalize the cubic endpoint carrier. The next source-side test must retain the feature this counterexample omits. The cleanest target is the **actual signed coefficient** `\Lambda-\Lambda^\sharp` on the same snapped cubic blocks: either prove that the subtraction destroys the PNT-selected coherence, or construct a compatible family where enough signed mass survives. A different admissible route is a rigorous full-window estimate showing that the remainder outside every coherent cubic subblock necessarily cancels the subblock at the distinguished twist.
