# PC-106 — all single-shell Hardy relative moments are cyclotomic-hyperlogarithmic

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `NEGATIVE/OBSTRUCTION` + `DECISIVE-BOUNDARY`. PC-075 isolated the trace-class arithmetic remainder `T_n` of the canonical Hardy/Hankel prime-circle operator, PC-076 and PC-077 computed its first two relative moments, and PC-078 reduced repeated-prime depth to squarefree tensor inflation. PC-103/PC-104 classified finite mixed-shell Hardy traces but explicitly left the constant-shell relative moments and the fixed-conductor Fredholm determinant outside their scope. The exact reduction below closes that finite-moment function-class gap: for every fixed conductor `n>1` and every `k>=1`, `Tr(T_n^k)` is a cyclotomic hyperlogarithmic period with letters in `mu_{2n}` and weight at most `k`. Consequently every Taylor coefficient of `det(I-zT_n)` belongs to the same finite-conductor cyclotomic period algebra.

This is a boundary result, not a zero-set theorem. It does **not** show that the full Fredholm determinant is algebraic, rational, or determined by finitely many periods, and it does not classify its zeros. It shows instead that increasing the finite relative-moment order at one fixed shell cannot escape to an elliptic or otherwise new period class.

## 1. Exact residue-block trace formula

Use the PC-075 residue decomposition

\[
W\Gamma_nW^*=-\frac1n C_n\otimes H_1+T_n,
\]

with

\[
(T_n)_{rs}
=-\frac{c_n(r+s+1)}n D_{(r+s+1)/n},
\qquad
D_a:=H_a-H_1,
\]

and

\[
(D_a)_{uv}
=\frac1{u+v+a}-\frac1{u+v+1}
=\int_0^1 x^{u+v}\bigl(x^{a-1}-1\bigr)\,dx.
\]

PC-075 proves `D_a in S_1` for every `a>0`, hence `T_n in S_1`. For a cyclic residue tuple

\[
r=(r_1,\ldots,r_k)\in\{0,\ldots,n-1\}^k,
\qquad
r_{k+1}=r_1,
\]

put

\[
t_i=r_i+r_{i+1}+1,
\qquad
 a_i=t_i/n.
\]

Taking the operator trace over the finite residue indices and the Hardy indices gives

\[
\boxed{
\operatorname{Tr}(T_n^k)
=\frac{(-1)^k}{n^k}
\sum_r
\left(\prod_{i=1}^k c_n(t_i)\right)
\operatorname{Tr}(D_{a_1}\cdots D_{a_k}).
}
\]

For the generalized Hilbert differences, summing the Hardy indices by their moment representation yields the exact cyclic cube integral

\[
\boxed{
\operatorname{Tr}(D_{a_1}\cdots D_{a_k})
=
\int_{[0,1]^k}
\frac{\prod_{i=1}^k (x_i^{a_i-1}-1)}
{\prod_{i=1}^k(1-x_i x_{i+1})}
\,dx_1\cdots dx_k,
\qquad x_{k+1}=x_1.
}
\]

For `k=1` this means the denominator is `1-x_1^2`; for `k=2` the same edge occurs twice, giving `(1-x_1x_2)^2`.

The integral is ordinary and absolutely convergent. Near `x_i=1`,

\[
|x_i^{a_i-1}-1|=O(1-x_i),
\]

and each denominator obeys `1-x_ix_{i+1} >= 1-x_i`; near `x_i=0` the worst numerator behavior is `x_i^{a_i-1}` with `a_i>0`, which is integrable. This also justifies obtaining the formula from finite geometric sums by dominated convergence rather than by a merely formal interchange.

## 2. The fractional Hilbert offsets disappear after the intrinsic `n`-th-root substitution

The only apparently non-cyclotomic feature of the cube above is the fractional exponent `a_i=t_i/n`. Set

\[
x_i=X_i^n.
\]

Then exactly

\[
(x_i^{t_i/n-1}-1)\,dx_i
=n\bigl(X_i^{t_i-1}-X_i^{n-1}\bigr)\,dX_i,
\]

so the factor `n^k` cancels the residue-block normalization. Therefore

\[
\boxed{
\operatorname{Tr}(T_n^k)
=(-1)^k
\int_{[0,1]^k}
\frac{P_{n,k}(X_1,\ldots,X_k)}
{\prod_{i=1}^k\left(1-(X_iX_{i+1})^n\right)}
\,dX_1\cdots dX_k,
}
\]

where

\[
\boxed{
P_{n,k}(X)
=
\sum_{r_1,\ldots,r_k=0}^{n-1}
\left(\prod_{i=1}^k c_n(t_i)\right)
\prod_{i=1}^k
\left(X_i^{t_i-1}-X_i^{n-1}\right)
\in\mathbb Z[X_1,\ldots,X_k].
}
\]

This is the key exact reduction. All conductor dependence is now in an **integer polynomial numerator** and the finite cyclotomic edge denominators `1-(X_iX_{i+1})^n`. In particular every summand in `P_{n,k}` is divisible by `prod_i(1-X_i)`, so the rational representation retains the endpoint cancellation that made the original trace finite.

No Mellin parameter or zeta function has been inserted. The formula is forced directly by the residue offsets of the prime-circle Hardy remainder.

## 3. The rational cube is linearly reducible with cyclotomic letters

Factor each edge denominator as

\[
1-u^n=\prod_{\xi\in\mu_n}(1-\xi u).
\]

Thus, when eliminating a variable `X_i`, its singular factors are parallel copies of

\[
1-\xi X_{i-1}X_i,
\qquad
1-\eta X_iX_{i+1},
\qquad \xi,\eta\in\mu_n.
\]

Their mixed resultant in `X_i` is, up to a nonzero cyclotomic scalar,

\[
\boxed{
\eta X_{i+1}-\xi X_{i-1},
}
\]

while resultants of two factors incident on the same neighbor contribute only coordinates and cyclotomic constants. Hence eliminating one independent-set vertex produces exactly the affine/link singularity class used in PC-103, now with several parallel cyclotomic phases per edge rather than one.

The rest of the PC-103 parity argument therefore applies unchanged. For an even cycle, eliminating one color class removes all bilinear edges and leaves only coordinate/affine/link factors whose zeros are in `mu_n`. For an odd cycle, the only possible terminal degree-two obstruction is a binomial

\[
A-BX^2,
\qquad A/B\in\mu_n,
\]

which factors over `mu_{2n}`. Repeated factors at `k=2` do not change the irreducible polynomial-reduction set, and `k=1` already factors through `1-X^{2n}`.

Panzer's linearly-reducible hyperlogarithmic integration framework, together with the cyclotomic multiple-polylogarithm setting of Goncharov already anchored in `SOURCES.md`, then gives

\[
\boxed{
\operatorname{Tr}(T_n^k)
\in
\mathbb Q(\mu_{2n})\cdot \operatorname{MPV}_{\le k}(2n)
\qquad(n>1,\ k\ge1).
}
\]

The factors with phase `1` can create endpoint poles in intermediate partial fractions, but this does not invalidate the statement. The original rational cube is absolutely convergent; endpoint-regularized hyperlogarithmic reductions must be combined before the regulator is removed, and the finite limit remains in the same cyclotomic period algebra. Equivalently, one can run polynomial reduction on the unexpanded factored denominator and use the numerator's endpoint zeroes.

## 4. Every fixed-conductor Fredholm coefficient is in the same period algebra

Because `T_n` is trace class,

\[
D_n(z):=\det(I-zT_n)
\]

is an entire Fredholm determinant. Write

\[
D_n(z)=\sum_{m\ge0} d_{n,m}z^m,
\qquad d_{n,0}=1.
\]

Newton's identities give the coefficient recurrence

\[
\boxed{
m\,d_{n,m}
=-\sum_{j=1}^m d_{n,m-j}\operatorname{Tr}(T_n^j).
}
\]

Since products of cyclotomic multiple-polylogarithm values reduce by the shuffle algebra without leaving the fixed cyclotomic alphabet, the moment theorem implies coefficientwise

\[
\boxed{
d_{n,m}
\in
\mathbb Q(\mu_{2n})\cdot\operatorname{MPV}_{\le m}(2n).
}
\]

This is deliberately **not** promoted to a classification of the full entire function or its zero set. An infinite power series whose individual coefficients are classical periods can still have a highly nontrivial zero distribution. The exact conclusion is only that no new finite-order period class is hiding in the single-shell relative determinant expansion.

## 5. Controls against the earlier exact results

The new integral has several independent checks.

1. `k=1` reduces to the relative trace already evaluated in PC-076, including its parity-twisted von Mangoldt collapse. Thus the general cyclotomic-period bound is intentionally much weaker than the exact logarithmic simplification at first order.
2. `k=2` reduces to the second relative trace of PC-077, which simplifies further to radical/divisor data. Again the all-order period theorem is a function-class statement, not a claim that higher moments cannot admit stronger arithmetic simplifications.
3. Direct finite-section checks of the residue-block operator agree with the transformed `k=3` cube. For `n=2` the transformed integral gives `0.1325724306...` versus `0.1325724267...` from a 200-by-residue finite section; for `n=3` it gives `0.3693754781...` versus `0.3693754716...`. These numerics are controls only; the evidence is the exact substitution and polynomial-reduction proof.
4. PC-078 remains compatible: repeated-prime depth tensor-inflates the already-classified squarefree remainder, so it cannot create a different finite-moment period class.

The result would be falsified if the block formula for `T_n` failed, if the `x=X^n` substitution left a nonintegral exponent, or if polynomial reduction of the parallel cyclotomic cycle generated a noncyclotomic irreducible factor before the terminal odd-cycle binomial. The displayed identities isolate those checks explicitly.

## 6. Prior-art and novelty audit

The **period class** is classical. Panzer's hyperlogarithm algorithms provide the standard linear-reducibility mechanism, and Goncharov's cyclotomic multiple-polylogarithm framework provides the root-of-unity value algebra; both are already durable anchors in `research/prime_circle/SOURCES.md` from PC-100--PC-104. Standard trace-class Fredholm theory supplies the determinant/trace-power relation used in Section 4.

Directed searches for Hilbert-matrix/Hankel trace powers, generalized-Hilbert perturbation determinants, and cyclotomic multiple-polylogarithmic Hankel traces found the broad classical Fredholm/Hankel literature and modern integrable-operator uses of Hankel determinants, but no reason to claim a historically new function class here. Absence of the exact Ramanujan-Hilbert specialization from those searches is **not** treated as novelty evidence.

The durable Prime-Circle contribution is narrower and exact: the particular trace-class remainder forced by the roots-of-unity Hardy decomposition has all of its fixed-conductor moments, including the squarefree higher moments left open by PC-077/PC-078, inside the same cyclotomic hyperlogarithmic universe already encountered for finite mixed-shell cycles.

## 7. RH consequence and remaining boundary

This closes a natural escape route from the earlier Hardy results:

\[
\boxed{
\text{fixed shell }T_n
\to
\text{higher relative moments}
\to
\text{new finite period class}
}
\]

cannot occur. At every finite order the data are classical cyclotomic hyperlogarithmic periods. In particular, merely computing `Tr(T_n^3), Tr(T_n^4), ...` cannot by itself manufacture the missing RH ingredients: there is still no geometry-forced free complex parameter, gamma factor, `s\leftrightarrow1-s` symmetry, positivity criterion tied to the critical line, or Riemann-zero divisor.

What remains open is genuinely more global. The theorem does not classify the zero set of `D_n(z)`, does not control an infinite-conductor or cross-level determinant formed **before** expansion, and does not cover a singular conductor-scaling limit in which the alphabet itself grows. PC-104 already handles every fixed finite nonconstant mixed-shell word; together the two results say that any surviving Hardy mechanism must use an intrinsically organized infinite-level limit or another non-finite operation, not simply a larger finite word or a higher fixed-shell relative moment. The nonlinear uniformization/monodromy branch of PC-017 remains outside this Hardy analysis.
