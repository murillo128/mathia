# PL-384 — Two incommensurate prime shifts already have the full continuous-semigroup commutant

**Evidence:** `EXACT-DERIVED + PRIOR-ART-AUDITED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-383`.

**Related findings:** `PL-017`, `PL-018`, `PL-019`, `PL-382`, `PL-383`.

**Status:** `THE-AMBIENT-NYMAN-DILATION-REPRESENTATION-LOSES-PRIME-LATTICE-DISCRETENESS-ALREADY-AT-THE-COMMUTANT-LEVEL, WITHOUT-ADJOINING-ADJOINTS. ANY-BOUNDED-OPERATOR-COMMUTING-WITH-THE-TWO-PRIME-DILATIONS-D_2-AND-D_3-AUTOMATICALLY-COMMUTES-WITH-EVERY-REAL-DILATION-D_r, r>=1. HENCE-THE-JOINT-COMMUTANT, BICOMMUTANT, AND-HYPERINVARIANT-SUBSPACE-DATA-OF-THE-TWO-PRIME-SAMPLES-ARE-IDENTICAL-TO-THOSE-OF-THE-FULL-CONTINUOUS-RIGHT-SHIFT-SEMIGROUP. THIS-DOES-NOT-IDENTIFY-THE-ACTUAL-NONSELFADJOINT-ALGEBRA-GENERATED-BY-D_2,D_3-WITH-THE-CONTINUOUS-SEMIGROUP-ALGEBRA, AND-IT-DOES-NOT-APPLY-AUTOMATICALLY-AFTER-RESTRICTION-TO-THE-NYMAN-STEP-SPACE. THE-SURVIVING-RH-ROUTE-MUST-USE-THE-ORIENTED-DISCRETE-ACTION, A-DISTINGUISHED-TARGET/SUBSPACE, OR-ANOTHER-STRUCTURE-NOT-DETERMINED-BY-THE-AMBIENT-COMMUTANT`.

## Claim

Let `D_r`, `r>=1`, be the normalized dilation isometries on `L^2((0,1),dx)` from `PL-382`, and let

\[
\mathcal C_{2,3}:=\{D_2,D_3\}',
\qquad
\mathcal C_{\mathrm{cont}}:=\{D_r:r\ge1\}'.
\]

Then

\[
\boxed{\mathcal C_{2,3}=\mathcal C_{\mathrm{cont}}.}
\tag{PL384-1}
\]

More generally, if `a,b>1` and `log a/log b` is irrational, then

\[
\boxed{\{D_a,D_b\}'=\{D_r:r\ge1\}'.}
\tag{PL384-2}
\]

Consequently

\[
\{D_2,D_3\}''=\{D_r:r\ge1\}'',
\tag{PL384-3}
\]

and the hyperinvariant subspaces determined by the two-prime tuple are exactly those determined by the full continuous dilation semigroup.

This strengthens the ambient negative conclusion of `PL-383` in a topology-sensitive direction. `PL-383` showed that adjoining adjoints and taking strong closure recovers the full continuous semigroup and then all of `B(L^2)`. The present statement does **not** adjoin adjoints: two incommensurate prime samples already determine exactly the same bounded commutant as the continuous right-shift flow.

## 1. Logarithmic coordinates

Use the unitary from `PL-382`,

\[
(Jf)(y)=e^{-y/2}f(e^{-y}),
\qquad
J:L^2((0,1))\to L^2(\mathbb R_+),
\]

for which

\[
JD_{e^t}J^{-1}=S_t,
\tag{PL384-4}
\]

where

\[
(S_tf)(y)=
\begin{cases}
f(y-t),&y\ge t,\\
0,&0\le y<t.
\end{cases}
\tag{PL384-5}
\]

The family `(S_t)_{t>=0}` is the standard strongly continuous right-shift semigroup. Every `S_t` is an isometry and hence injective.

Thus it is enough to prove that if `u,v>0` have irrational ratio, then

\[
\{S_u,S_v\}'=\{S_t:t\ge0\}'.
\tag{PL384-6}
\]

## 2. Commutation survives positive subtraction

Let `X` be bounded and suppose

\[
XS_u=S_uX,
\qquad
XS_v=S_vX,
\]

with `0<u<v`. Since

\[
S_v=S_uS_{v-u},
\]

we have

\[
S_uXS_{v-u}
=XS_uS_{v-u}
=XS_v
=S_vX
=S_uS_{v-u}X.
\]

Because `S_u` is injective, left cancellation is legitimate and gives

\[
\boxed{XS_{v-u}=S_{v-u}X.}
\tag{PL384-7}
\]

This is the key point. No adjoint, inverse shift, or self-adjoint closure has been introduced. The difference of two sampled times appears because the **commutation equations themselves can be cancelled through an injective semigroup element**.

Repeated subtraction therefore gives the Euclidean algorithm. Starting with `r_0=v`, `r_1=u`, define

\[
r_{k-1}=q_kr_k+r_{k+1},
\qquad
0<r_{k+1}<r_k.
\tag{PL384-8}
\]

If `u/v` is irrational the algorithm never terminates, and

\[
r_k\longrightarrow0.
\tag{PL384-9}
\]

Applying (PL384-7) repeatedly shows that `X` commutes with every `S_{r_k}`.

## 3. Arbitrarily small commuting times force the full semigroup

Fix `t>=0`. For each sufficiently large `k`, choose

\[
m_k=\left\lfloor\frac{t}{r_k}\right\rfloor.
\]

Then

\[
0\le t-m_kr_k<r_k,
\]

so

\[
m_kr_k\longrightarrow t.
\tag{PL384-10}
\]

Since `X` commutes with `S_{r_k}`, it also commutes with every positive integer power

\[
S_{m_kr_k}=S_{r_k}^{m_k}.
\]

Strong continuity gives

\[
S_{m_kr_k}\xrightarrow{\mathrm{SOT}}S_t.
\]

For every `f in L^2(R_+)`, boundedness of `X` therefore yields

\[
XS_tf
=\lim_kXS_{m_kr_k}f
=\lim_kS_{m_kr_k}Xf
=S_tXf.
\]

Hence `X` commutes with every `S_t`, proving

\[
\{S_u,S_v\}'\subseteq\{S_t:t\ge0\}'.
\]

The reverse inclusion is immediate, so (PL384-6) holds.

For the prime pair

\[
u=\log2,
\qquad
v=\log3,
\]

irrationality of `u/v` follows from unique factorization: a rational relation `n log 2=m log 3` would imply `2^n=3^m`. Conjugating (PL384-6) by `J` proves (PL384-1). The same proof gives (PL384-2).

## 4. What this erases, and what it does not

The result closes a natural nonselfadjoint **commutant-based** escape left open by `PL-383`. Any construction that remembers the ambient prime-dilation tuple only through its joint commutant cannot distinguish the discrete prime sampling from the full continuous dilation semigroup. The same is true of the bicommutant by taking commutants of (PL384-1), and of hyperinvariant-subspace data because hyperinvariance is defined through the commutant.

This loss is not arithmetic-specific. The proof works for every pair of positive incommensurate times. Thus a commutant invariant that appears already from `D_2,D_3` fails the line's generic-frequency control: replacing `log 2,log 3` by any irrationally related pair gives exactly the same collapse.

Two scope limits are essential.

First, (PL384-1) does **not** imply that the weak-, strong-, or norm-closed nonselfadjoint algebra generated by `S_u,S_v` equals the algebra generated by all `S_t`. Equality of commutants gives equality of bicommutants, but a nonselfadjoint algebra need not equal its bicommutant. The oriented positive semigroup generated by the prime samples can therefore retain information that its commutant forgets.

Second, this is an ambient `L^2((0,1))` result. On Bagchi's invariant Nyman step space the integer dilations restrict to the RH-relevant tuple, but noninteger dilations such as `D_{3/2}` need not preserve that subspace. The factorization used in the cancellation step therefore does not automatically exist inside the restricted representation. No claim is made that the commutant of the restricted pair `T_2,T_3` equals a continuous-semigroup commutant.

These are precisely the structures that remain live: the actual one-sided integer semigroup, its action on the distinguished Nyman subspace/target, and target-relative defects not determined by the ambient commutant.

## 5. Prior-art and novelty audit

The continuous right-shift model, its strong continuity, and the logarithmic equivalence with the Nyman dilation family are classical and already audited in `PL-382`. `PL-383` already derived the stronger self-adjoint/SOT collapse after adjoining adjoints. The present commutant identity uses only the semigroup law, injectivity, the Euclidean algorithm, strong continuity, and irrationality of the two sampled times.

A targeted search of the right-shift-semigroup, translation-semigroup, Wiener--Hopf/commutant, and commuting-isometry literature found the continuous model and its operator theory as standard background, but no source was located that would justify claiming novelty for the exact two-incommensurate-samples formulation. No theorem novelty is claimed. The durable contribution is the route-specific negative inference: **even before adjoints are adjoined, passing from the ambient sampled tuple to its commutant has already erased the discrete prime timing.**

## 6. Falsification conditions

This finding should be corrected or withdrawn if any of the following fails:

1. the logarithmic conjugacy `JD_{e^t}J^{-1}=S_t` from `PL-382`;
2. injectivity of the right shifts, which is needed for the cancellation in (PL384-7);
3. the Euclidean-algorithm deduction that irrational `u/v` produces positive remainders tending to zero;
4. strong continuity of `(S_t)`, which is needed to pass from the commuting times `m_kr_k` to arbitrary `t`;
5. the distinction between commutant/bicommutant equality and equality of the actual nonselfadjoint generated algebras.

Subject to those controls, (PL384-1)--(PL384-3) are exact.