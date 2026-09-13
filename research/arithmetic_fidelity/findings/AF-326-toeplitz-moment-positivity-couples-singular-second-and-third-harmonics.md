# AF-326 — Toeplitz moment positivity couples singular second- and third-harmonic margins

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TRIGONOMETRIC-MOMENT`, `SELF-INVERSIVE`, `QUANTITATIVE-FIDELITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Let

\[
Z=\{z_1,\ldots,z_8\}\subset S^1,
\qquad
s_k=\sum_{j=1}^8 z_j^k,
\]

and assume the centered middle-singular conditions

\[
s_1=0,
\qquad
e_4(Z)=0.
\tag{1}
\]

Then the second and third power sums satisfy the exact moment-cone inequality

\[
\boxed{
|s_3|^2
\le
8\,\frac{(16-|s_2|^2)(32+|s_2|^2)}{64-|s_2|^2}.
}
\tag{2}
\]

In particular,

\[
\boxed{|s_2|\le4}
\tag{3}
\]

and the simpler boundary estimate

\[
\boxed{
4-|s_2|\ge \frac{|s_3|^2}{64}.
}
\tag{4}
\]

Thus approaching the extremal second-harmonic value `|s_2|=4` forces the AF-320 recovery denominator `s_3` to collapse. Conversely, any source-specific lower bound on `|s_3|` immediately becomes a quantitative gap below the extremal second harmonic.

For a hypothetical exact eight-prime middle-singular hit

\[
z_j=p_j^{-it},
\qquad p_j\le H,
\qquad |t|\ge1,
\]

AF-325 supplies an absolute constant `C>0` such that, for sufficiently large `H`,

\[
|F_P(3t)|
\ge
\exp\!\left[-C(\log H)^2\log(e+|t|\log H)\right],
\tag{5}
\]

where `F_P(u)=\sum_{p\in P}p^{-iu}`. Combining `(4)` and `(5)` gives the explicit observable-margin consequence

\[
\boxed{
4-|F_P(2t)|
\ge
\frac1{64}
\exp\!\left[-2C(\log H)^2\log(e+|t|\log H)\right].
}
\tag{6}
\]

Equation `(6)` is conditional on the exact incidence `F_P(t)=0` and `e_4=0`; it does not prove that such an incidence exists. Its role is to propagate the source-specific finite-height separation obtained in AF-325 into a different retained observable rather than leaving the arithmetic modulus attached only to the reconstruction denominator.

## 1. Middle singularity fixes the fourth normalized moment

Put the equal-weight probability measure

\[
\mu_Z=\frac18\sum_{j=1}^8\delta_{z_j}
\]

on the unit circle and write

\[
m_k=\int z^k\,d\mu_Z(z)=\frac{s_k}{8}.
\tag{7}
\]

Because `s_1=e_1=0`, Newton's identity at order four gives

\[
8e_4=s_2^2-2s_4.
\tag{8}
\]

Hence the middle-singular condition in `(1)` is equivalent to

\[
s_4=\frac12s_2^2,
\qquad
m_4=4m_2^2.
\tag{9}
\]

A common rotation `Z\mapsto\rho Z` sends `m_k\mapsto\rho^km_k` and preserves `(9)`. Choose `\rho` so that the rotated second moment is real and nonnegative,

\[
m_2=r\ge0.
\tag{10}
\]

The modulus of `m_3` is unchanged. Equation `(9)` becomes `m_4=4r^2`.

## 2. One Toeplitz principal minor gives the full tradeoff

For every positive measure on `S^1`, the trigonometric moment matrices are positive semidefinite. Apply this only to the four monomials

\[
1,\ z,\ z^2,\ z^4.
\]

Their Gram matrix under `\mu_Z` is, up to harmless transpose convention,

\[
M=
\begin{pmatrix}
1&0&r&4r^2\\
0&1&0&m_3\\
r&0&1&r\\
4r^2&\overline{m_3}&r&1
\end{pmatrix}
\succeq0.
\tag{11}
\]

Direct expansion gives

\[
\det M
=
1-2r^2-8r^4-(1-r^2)|m_3|^2.
\tag{12}
\]

Factoring the first three terms,

\[
1-2r^2-8r^4=(1-4r^2)(1+2r^2),
\]

so positivity implies

\[
\boxed{
(1-r^2)|m_3|^2
\le
(1-4r^2)(1+2r^2).
}
\tag{13}
\]

Since `|m_2|\le1`, the left side of `(13)` is nonnegative and `1+2r^2>0`; therefore `r\le1/2`, which is `(3)` after `|s_2|=8r`.

Substituting

\[
r=\frac{|s_2|}{8},
\qquad
|m_3|=\frac{|s_3|}{8}
\]

into `(13)` yields exactly `(2)`.

This is a trigonometric-moment constraint, not a peculiarity of the AF-320 reconstruction formula. It comes from positivity of the source measure before any attempt to solve for the missing product phase.

## 3. A quadratic gap controls the recovery denominator

For `0\le r\le1/2`, equation `(13)` gives

\[
|m_3|^2
\le
\frac{(1-4r^2)(1+2r^2)}{1-r^2}.
\tag{14}
\]

The elementary inequality

\[
\frac{(1+2r)(1+2r^2)}{1-r^2}\le4,
\qquad 0\le r\le\frac12,
\tag{15}
\]

then implies

\[
|m_3|^2\le4(1-2r).
\tag{16}
\]

Indeed, after clearing the positive denominator, `(15)` is equivalent to

\[
3-2r-6r^2-4r^3\ge0,
\]

whose left side decreases from `3` to `0` on `[0,1/2]`.

Since `|s_2|=8r` and `|s_3|=8|m_3|`, equation `(16)` is precisely `(4)`.

Two consequences are worth separating.

First, AF-320's strict inequality `|s_2|<4` on the rational-prime source class follows immediately from `(4)` together with its exact source theorem `s_3\ne0`. This gives a second proof of that strictness which exposes the quantitative mechanism: the extremal face `|s_2|=4` lies inside the deeper harmonic singularity `s_3=0`.

Second, the implication has the correct direction for conditioning. A small extremal gap permits `s_3` to be only of square-root size; therefore a proof that merely keeps `|s_2|` below `4` qualitatively cannot stabilize AF-320. One needs a quantitative source margin. AF-325 provides exactly such a margin at bounded support height and finite time, and substituting `(5)` into `(4)` gives `(6)`.

## 4. Arithmetic-fidelity consequence

AF-321 showed that the ambient rank-one middle-singular family has no uniform lower bound on `|s_3|`; its closure reaches the regular-octagon fiber where all harmonics below order eight vanish. AF-325 then showed that an actual rational-prime support of bounded height cannot approach that deeper antipodal stratum arbitrarily quickly at finite time.

AF-326 identifies an exact **target-transfer law** between those two statements. The source-specific modulus does not remain hidden in the auxiliary denominator used to reconstruct `E=e_8`: it forces a directly visible gap in the already-retained second harmonic. Schematically, on the exact middle-singular source class,

\[
\text{prime height/time separation}
\Longrightarrow |s_3|\text{ margin}
\Longrightarrow 4-|s_2|\text{ margin}.
\tag{17}
\]

This is useful for the line's general compression question because it illustrates when an arithmetic source restriction genuinely propagates into the target geometry. The first implication is arithmetic/Diophantine (AF-325); the second is source-independent moment positivity `(4)`. Neither ingredient alone supplies `(6)`.

The result does **not** solve the exact eight-prime incidence problem. The live arithmetic question remains whether any common-time prime phase tuple satisfies `s_1=e_4=0` at all. What changes is the admissible geometry of such a hit: at bounded support height and finite time it must stay quantitatively inside the nonextremal region of the second-harmonic moment cone.

## Prior art and novelty assessment

The positivity input is classical trigonometric-moment theory. No novelty is claimed for positive-semidefinite Toeplitz moment matrices, Carathéodory--Fejér/Vandermonde representations, or deriving inequalities from principal minors.

- Barry Simon, *Orthogonal Polynomials on the Unit Circle*, AMS Colloquium Publications 54, Part 2 (2005), DOI `10.1090/coll/054.2`, is an authoritative modern source for unit-circle measures, moments, Toeplitz matrices and the associated positivity framework.
- Nikolaï Nikolski, *Toeplitz Matrices and Operators*, Cambridge University Press (2020), Chapter 5, DOI `10.1017/9781108182577.006`, treats the trigonometric moment problem and positive-definite Toeplitz matrices in a modern operator-theoretic setting.
- The classical Carathéodory--Fejér theorem identifies positive Toeplitz matrices with positive atomic/Vandermonde representations; modern accounts use this as the finite trigonometric moment framework underlying `(11)`.

A targeted literature search found the general moment-cone machinery but no reason to treat the specialized algebraic inequality `(2)` as a new theorem of independent moment theory; it is a direct principal-minor consequence once the Mathia-specific constraint `m_1=0, m_4=4m_2^2` is imposed. The durable contribution here is therefore deliberately narrower: composing that classical positivity constraint with AF-325's rational-prime finite-height modulus produces the explicit second-harmonic resource bound `(6)`.

## Boundaries and failure modes

- Equations `(2)`--`(4)` are source-independent and hold for every equal-weight eight-point unit-circle configuration satisfying `(1)`. They do not distinguish rational primes by themselves.
- Equation `(6)` additionally assumes the rational-prime, bounded-support-height, common nonzero-time hypotheses of AF-325 and is conditional on an exact middle-singular hit.
- The estimate does not prove a lower bound on `|s_3|` from `|s_2|`; the moment inequality runs in the opposite direction. Prime-source information is still essential for stable recovery.
- No claim is made that the constant `1/64` in `(4)` is globally sharp on the equal-weight eight-atom singular variety. The exact inequality `(2)` is the stronger statement retained for later optimization.
- The four-monomial principal minor is only one positivity certificate. Higher Toeplitz minors may impose additional constraints involving `s_3` or higher harmonics; none are claimed here.
- The result concerns the exact centered middle-singular stratum. It does not supply a perturbative bound when `s_1` or `e_4` is merely small.
- No conclusion about zeta zeros, the critical line, zero density, or RH follows from `(2)`--`(6)`.

## Consequence for the research line

The support-height/time-height modulus now reaches two different coordinates of the retained harmonic representation. Future work on exact incidence should therefore keep the two roles separate: `|s_3|` controls inversion of the missing product phase, while `4-|s_2|` measures distance from the extremal second-harmonic face. Any proposed compression that discards the third harmonic but claims to retain equivalent stability must explain how it preserves a comparable target margin rather than relying only on the qualitative inequality `|s_2|<4`.