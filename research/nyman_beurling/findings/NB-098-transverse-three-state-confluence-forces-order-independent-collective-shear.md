# NB-098 — transverse three-state confluence forces order-independent collective shear

**Status:** `EXACT-DERIVED + CANONICAL-BLASCHKE-GEOMETRIC-CONTROL + THREE-STATE-TRANSVERSE-CONFLUENCE + ORDER-INDEPENDENT-COLLECTIVE-SHEAR + QUARTIC-CONDITIONING-BLOWUP + NEGATIVE-METHOD-BOUNDARY`.

`NB-097` proves that the canonically deflated half-line state Gram has unit Schur pivots for every fixed finite distinct zero set and that every two-state subsystem is uniformly conditioned, even through arbitrarily close distinct-point collisions. That leaves a specific half-line question: can the unit-triangular canonical shear nevertheless become singular collectively when three or more states crowd?

Yes, already for three states. There is an explicit family of **synthetic right-half-plane state parameters** for which every pair remains within the uniform two-state bound of `NB-097`, every canonical pivot stays exactly one, but the three-state canonical Gram has condition number of order `epsilon^-4`. The blow-up occurs for all six deflation orders. Thus no separation-insensitive, dimension-free conditioning theorem can follow from canonical half-line Blaschke geometry alone; any such theorem for the actual zeta divisor must use additional source-specific information.

Fix `a>0` and a nonzero real `c`. For sufficiently small `epsilon>0`, put

\[
\lambda_1=a+i\epsilon,
\qquad
\lambda_2=a+c\epsilon,
\qquad
\lambda_3=a-i\epsilon.
\tag{1}
\]

All three parameters lie in the open right half-plane and are pairwise distinct. Let

\[
G_{rs}
=\frac{2\sqrt{a_ra_s}}{\lambda_r+\overline{\lambda_s}},
\qquad
a_r=\Re\lambda_r,
\tag{2}
\]

be the normalized half-line exponential-state Gram, let `T` be the exact canonical deflation matrix of `NB-095`, and define

\[
C_\epsilon=T^*GT.
\tag{3}
\]

Then, for **every permutation of the three factors**, the positive-diagonal Cholesky factor

\[
C_\epsilon=R_\epsilon^*R_\epsilon,
\qquad
(R_\epsilon)_{11}=(R_\epsilon)_{22}=(R_\epsilon)_{33}=1,
\tag{4}
\]

satisfies

\[
|(R_\epsilon)_{13}|
=\frac{4a|c|}{1+c^2}\,\epsilon^{-1}+O_{a,c}(1),
\qquad
|(R_\epsilon)_{23}|
=\frac{4a|c|}{1+c^2}\,\epsilon^{-1}+O_{a,c}(1),
\tag{5}
\]

while `(R_epsilon)_(12)=O_c(1)`. Consequently

\[
\boxed{
\kappa_2(C_\epsilon)=\Theta_{a,c}(\epsilon^{-4}).
}
\tag{6}
\]

This is a genuinely collective three-state failure. No pair develops an unbounded canonical condition number, and the determinant remains exactly one.

## 1. Exact triangular square root of the canonically deflated Cauchy Gram

For arbitrary ordered distinct right-half-plane parameters `lambda_1,...,lambda_d`, the raw Cauchy Gram `(2)` has the explicit upper-triangular factorization

\[
G=Q^*Q,
\tag{7}
\]

where, for `j<=k`,

\[
Q_{jk}
=
\frac{2\sqrt{a_ja_k}}
     {\lambda_j+\overline{\lambda_k}}
\prod_{\ell<j}
\frac{\overline{\lambda_k}-\overline{\lambda_\ell}}
     {\overline{\lambda_k}+\lambda_\ell},
\qquad
Q_{jk}=0\quad(j>k).
\tag{8}
\]

This is the standard Cauchy/Takenaka--Malmquist triangularization written in the normalization used by `NB-095`--`NB-097`; direct multiplication gives `(7)`.

The exact canonical-deflation matrix from the partial-fraction calculation of `NB-095` is upper triangular with

\[
T_{kk}
=
\prod_{\ell<k}
\frac{\lambda_k+\overline{\lambda_\ell}}
     {\lambda_k-\lambda_\ell},
\tag{9}
\]

and, for `r<k`,

\[
T_{rk}
=
-\frac{2\sqrt{a_ra_k}}
       {\lambda_k-\lambda_r}
\prod_{\substack{\ell<k\\ \ell\ne r}}
\frac{\lambda_r+\overline{\lambda_\ell}}
     {\lambda_r-\lambda_\ell}.
\tag{10}
\]

Hence

\[
M:=QT,
\qquad
C=T^*GT=M^*M.
\tag{11}
\]

Moreover

\[
|Q_{kk}|
=\prod_{\ell<k}
\left|
\frac{\lambda_k-\lambda_\ell}
     {\lambda_k+\overline{\lambda_\ell}}
\right|,
\qquad
|T_{kk}|=|Q_{kk}|^{-1},
\tag{12}
\]

so every diagonal entry of `M` has modulus one. Multiplying rows of `M` by unit phases therefore produces exactly the positive-diagonal Cholesky factor `R`; in particular all off-diagonal magnitudes and both singular-value condition numbers are unchanged. This is an explicit realization of the unit-pivot statement in `NB-097`.

## 2. A transverse three-way collision creates an inverse-epsilon shear

Use the order displayed in `(1)`. Substituting `(1)` into `(8)`--`(10)` gives

\[
M_{12}
=
-\frac{4i\sqrt a\sqrt{a+c\epsilon}}
       {(c-i)(2a+c\epsilon+i\epsilon)},
\tag{13}
\]

so

\[
M_{12}\longrightarrow -\frac{2i}{c-i}.
\tag{14}
\]

The third-column entries are

\[
M_{13}
=
-\frac{2a\bigl(
4a^2c+4ac^2\epsilon-4a\epsilon
+c^3\epsilon^2-i c^2\epsilon^2
-3c\epsilon^2-i\epsilon^2
\bigr)}
{\epsilon(a+i\epsilon)(c-i)(c+i)(2a+c\epsilon+i\epsilon)},
\tag{15}
\]

and

\[
M_{23}
=
\frac{4\sqrt a\sqrt{a+c\epsilon}(ac-\epsilon)(2a+c\epsilon-i\epsilon)}
{\epsilon(a+i\epsilon)(1+c^2)(2a+c\epsilon+i\epsilon)}.
\tag{16}
\]

Therefore

\[
\boxed{
\epsilon M_{13}\longrightarrow
-\frac{4ac}{1+c^2},
\qquad
\epsilon M_{23}\longrightarrow
\frac{4ac}{1+c^2}.
}
\tag{17}
\]

The diagonal phases remain harmless:

\[
M_{11}=1,
\qquad
M_{22}\longrightarrow\frac{c+i}{c-i},
\qquad
M_{33}\longrightarrow\frac{-c+i}{c+i},
\tag{18}
\]

all of modulus one. Row phase normalization therefore turns `(17)` directly into the magnitude statement `(5)`.

The geometry of `(1)` matters. If `c=0`, all three points approach `a` tangentially along the same vertical line and the `epsilon^-1` coefficient in `(17)` vanishes. The blow-up is a **transverse** confluence effect, not a claim that every triple collision is singular. This path dependence is also why a genuine repeated zeta zero cannot be modeled by taking an arbitrary distinct-point collision limit; its confluent/Jordan state system remains a separate problem.

## 3. Quartic conditioning blow-up, despite bounded pairs and unit pivots

Put

\[
K:=\frac{4a|c|}{1+c^2}>0.
\tag{19}
\]

From `(5)`,

\[
\|R_\epsilon\|_2\ge |(R_\epsilon)_{13}|
=K\epsilon^{-1}+O(1).
\tag{20}
\]

For a unit upper-triangular `3 x 3` matrix,

\[
(R_\epsilon^{-1})_{23}=-(R_\epsilon)_{23},
\tag{21}
\]

so

\[
\|R_\epsilon^{-1}\|_2
\ge K\epsilon^{-1}+O(1).
\tag{22}
\]

All entries of `R_epsilon` and `R_epsilon^-1` are `O_(a,c)(epsilon^-1)`, hence both norms are `Theta_(a,c)(epsilon^-1)`. Since `C_epsilon=R_epsilon^*R_epsilon`,

\[
\kappa_2(C_\epsilon)
=\kappa_2(R_\epsilon)^2
=\Theta_{a,c}(\epsilon^{-4}),
\tag{23}
\]

proving `(6)`. In particular,

\[
\liminf_{\epsilon\downarrow0}
\epsilon^4\kappa_2(C_\epsilon)
\ge
\left(\frac{4a|c|}{1+c^2}\right)^4.
\tag{24}
\]

This does not evade the controls of `NB-097`; it saturates their boundary. Every two-point subsystem still has canonical shear bounded by `2` and therefore uniformly bounded condition number. For example, the pair `(lambda_1,lambda_2)` has

\[
|\chi_{12}|\longrightarrow\frac{2}{\sqrt{1+c^2}}\le2.
\tag{25}
\]

The other two pairs obey the same universal theorem. Every leading principal determinant of the full canonical Gram remains exactly one as well. The bad singular value is therefore produced by collective triangular shear, not by a bad pair, a determinant tax, or a collapsing Schur pivot.

## 4. The blow-up cannot be repaired by reordering the three factors

The canonical coordinates depend on the deflation order, so an obvious escape is to choose a better ordering before taking the crowded limit. For this three-state family that does not help.

Apply `(8)`--`(10)` separately to each of the six permutations of `(lambda_1,lambda_2,lambda_3)`. In every case the resulting upper-triangular square root `M^(pi)` satisfies

\[
\boxed{
\epsilon M^{(\pi)}_{13}
\longrightarrow
-\frac{4ac}{1+c^2},
\qquad
\epsilon M^{(\pi)}_{23}
\longrightarrow
\frac{4ac}{1+c^2}.
}
\tag{26}
\]

Only the unit diagonal phases change with the permutation. Hence the positive-diagonal Cholesky factor again has the two divergent magnitudes in `(5)`, and `(23)` holds for every ordering. This is stronger than exhibiting one unfortunate sequential deflation: **the transverse three-state obstruction is order-independent at leading scale**.

## 5. Prior-art boundary and consequence for the Nyman line

The ingredients used to derive `(7)`--`(12)` live in classical Cauchy-kernel and Takenaka--Malmquist geometry, and confluent Cauchy systems are a classical subject. The contemporary Nyman/Blaschke boundary already recorded in `SOURCES.md` is Ziad's 2026 finite Blaschke/arithmetic Gram split. A targeted audit found no statement there, or in the checked Takenaka--Malmquist/confluent-Cauchy literature, of the specific canonical Nyman causal-deflation phenomenon `(17)`--`(26)`. No external theorem is load-bearing for the calculation, so `SOURCES.md` does not require expansion and no priority claim is made from the bounded search.

The result is deliberately a **matched geometric control**, not an actual-zero theorem. The parameters `(1)` are arbitrary right-half-plane points; they are not asserted to be zeta zeros. Therefore `NB-098` does not show that the actual off-critical zeta divisor, if one exists, has unbounded canonical conditioning, and it does not contradict the fixed-`F` constants in `NB-095`. For every fixed positive `epsilon`, the selected set is fixed and its condition number is finite; the divergence appears only as the set itself degenerates.

What `(6)` does rule out is the generic next step suggested after `NB-097`: there is **no separation-insensitive uniform half-line bound on the canonical shear based only on distinct right-half points, unit pivots, and bounded two-state interactions**. Any useful growing-divisor theorem for the actual Nyman source must now use a genuinely additional resource: zeta-specific restrictions on admissible zero configurations, quantitative separation/zero-density information strong enough to control collective shear, a representation that handles crowded/confluent states differently, or a later finite-window/target mechanism that does not require uniformly conditioning this half-line canonical coordinate system.

The remaining target-awareness boundary is unchanged. Even perfect control of the actual zero-state Gram would still have to be converted into a statement about the fixed Nyman target rather than generator geometry alone.