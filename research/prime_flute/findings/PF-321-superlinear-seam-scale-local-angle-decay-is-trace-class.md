# PF-321 — superlinear seam-scale local angle decay is trace class

**Status:** `EXACT-DERIVED + ARITHMETIC-SUMMABILITY + OPERATOR-IDEAL-CRITERION + POSITIVE/ROUTE-SHARPENING`.

PF-318 gives a convenient prime-by-prime sufficient condition for the direct physical `L/H` angle: a local squared Hilbert--Schmidt budget of order `(1+log P_n)/P_n^2`. PF-320 then moves the live PDE problem to the **shear-deleted intrinsic local pant angles** `T_{0,n}^{(r)}`, because the actual PF-232 shear already costs only the PF-318 weak-trace budget at angle level.

That reciprocal-prime target is still stronger than the shear-deleted reference problem needs. PF-299 has already proved that the exact tight-pant seam distances

\[
s_n=\frac{h_n+h_{n+1}}2
\]

satisfy

\[
(s_n)\in\bigcap_{q>1}\ell^q\setminus\ell^1.
\]

Combining this with the logarithmic physical-low rank gives a sharper endpoint rule:

\[
\boxed{
\|T_{0,n}^{(r)}\|\le C s_n^q
\quad\text{for any fixed }q>1
\Longrightarrow
\bigoplus_n T_{0,n}^{(r)}\in\mathcal S_1.
}
\]

The logarithmic rank costs nothing at this exponent. More precisely,

\[
\boxed{
\sum_n (1+\log P_n)s_n^q<\infty
\qquad(q>1).
}
\]

Thus **any fixed superlinear gain in the exact seam scale closes the shear-deleted reference channel in strong trace class**, not merely weak trace class. PF-320 may then add the real hypercycle shear as its already-controlled weak-`S_1` perturbation, so the actual direct angle is weak trace class.

This materially changes the local PDE target. One need not force every reference angle down to reciprocal-prime size. It is enough to prove, for example,

\[
\|T_{0,n}^{(r)}\|=O(s_n^2),
\]

or more generally `O(s_n^{1+\varepsilon})` for one fixed `\varepsilon>0`. This is especially relevant to PF-233: after writing `a_n=s_n b_n`, its mass-conjugated transverse operator has the exact scaling `T_{a_n}=s_n^2\widetilde T_n`, while the corridor transfer function

\[
F(x)=\frac{x}{\sinh x}
\]

has no linear term at the origin. That makes a superlinear reference-angle estimate a natural quantity to test. The present finding does **not** assert that the physical `L/H` projection, actual seam normalization, or finite pant completion preserves this cancellation; that remains the local PDE problem.

## Claim

Let `P_n=p_{n-1}` be the prime labels and let

\[
h_n=F_0(p_n)-F_0(p_{n-1}),
\qquad
F_0(x)=\log\cot\frac{\pi}{x},
\]

with exact neighboring-cuff distance

\[
 s_n=\frac{h_n+h_{n+1}}2.
\tag{1}
\]

Then:

1. for every fixed `q>1`,
   \[
   \boxed{
   \sum_n (1+\log P_n)s_n^q<\infty;
   }
   \tag{2}
   \]
2. fix a finite offset set `R`. For every `r\in R`, let
   \[
   T_{n}^{(r)}:H_n\to L_{n+r}
   \]
   be finite-rank operators whose source spaces and target spaces are mutually orthogonal as `n` varies, with
   \[
   \operatorname{rank}T_n^{(r)}
   \le A(1+\log P_n).
   \tag{3}
   \]
   If for some fixed `q>1`
   \[
   \boxed{
   \|T_n^{(r)}\|\le D s_n^q
   }
   \tag{4}
   \]
   uniformly in `n,r` and in the canonical finite sections, then
   \[
   \boxed{
   \bigoplus_nT_n^{(r)}\in\mathcal S_1
   }
   \tag{5}
   \]
   for every `r`, uniformly in the exhaustion, and the finite sum over `r` is also trace class;
3. the same conclusion holds for the PF-320 shear-deleted local pant reference angles `T_{0,n}^{(r)}` whenever they obey (3)--(4). PF-320's positive-sum factorization then puts the reassembled shear-deleted direct angle in `\mathcal S_1`;
4. adding the actual PF-232 shear does not require the reference to remain trace class: PF-320 and PF-318 already place the local shear-angle error in the reciprocal-prime Hilbert--Schmidt budget, hence its global contribution in `\mathcal S_{1,\infty}`. Therefore
   \[
   \boxed{
   \text{(4) for the reference angles}
   \Longrightarrow
   Z_{LH}^{\rm actual}\in\mathcal S_{1,\infty}.
   }
   \tag{6}
   \]

The exponent `q>1` is the structural point. No reciprocal-prime comparison between `s_n` and `P_n^{-1}` is required.

## 1. PF-299 remains summable after the logarithmic rank weight

PF-299 proves the stronger dyadic estimate behind `s\in\ell^q`. For `X=2^k` and every fixed `q>1`, Baker--Harman--Pintz's exponent `0.525` gives

\[
\sum_{X\le P_n<2X}s_n^q
\le C_q X^{-\delta(q-1)},
\qquad
\delta=1-0.525=0.475,
\tag{7}
\]

up to harmless adjacent-index changes. The proof uses only the exact telescoping of the logarithmic mesh and the sublinear maximal-gap bound; it is recorded in PF-299.

On the same dyadic block,

\[
1+\log P_n\le C(1+\log X).
\]

Hence

\[
\sum_{X\le P_n<2X}
(1+\log P_n)s_n^q
\le
C_q(1+\log X)X^{-\delta(q-1)}.
\tag{8}
\]

For `X=2^k` the right side is bounded by

\[
C_q(1+k)2^{-\delta(q-1)k},
\]

which is summable in `k`. This proves (2).

This weighted statement is exactly what the physical-low rank needs. The extra `O(\log P_n)` number of low modes does not move the critical exponent away from `q=1`; every fixed power strictly above one still wins geometrically on dyadic prime scales.

## 2. Local superlinear angle decay gives global trace norm directly

For any finite-rank operator,

\[
\|T\|_{\mathcal S_1}
\le \operatorname{rank}(T)\,\|T\|.
\tag{9}
\]

Using (3)--(4),

\[
\|T_n^{(r)}\|_{\mathcal S_1}
\le AD(1+\log P_n)s_n^q.
\tag{10}
\]

Equation (2) therefore gives

\[
\sum_n\|T_n^{(r)}\|_{\mathcal S_1}<\infty.
\tag{11}
\]

For fixed `r` the source and target module spaces are orthogonal, so the local operators form a literal orthogonal direct sum and

\[
\left\|\bigoplus_nT_n^{(r)}\right\|_{\mathcal S_1}
=
\sum_n\|T_n^{(r)}\|_{\mathcal S_1}<\infty.
\tag{12}
\]

A finite sum over neighboring offsets remains trace class. This proves (5).

For the PF-320 reference form, the global shear-deleted direct angle is a two-sided contraction of the orthogonal direct sum of the local intrinsic angles after the positive identity/completion is distributed locally. The trace ideal is two-sided, so the contraction sandwich preserves (12). No global prime-density threshold argument is needed once the local decay is superlinear in `s_n`.

## 3. Why `s_n^2` is a natural reference calculation, not an established answer

PF-233 writes the shear-deleted variable-width corridor after mass conjugation in terms of the transverse operator `T_a`. For the canonical family write

\[
a_n(\theta)=s_n b_n(\theta),
\qquad
1-\eta\le b_n\le1.
\tag{13}
\]

In PF-233's exact form

\[
\tau_{a_n}[y]
=\int a_n^2
\left(
|y'+c_ny|^2+\csc^2\theta|y|^2
\right)d\theta,
\]

with `c_n=a_n'/(2a_n)=b_n'/(2b_n)`. Therefore

\[
\boxed{
T_{a_n}=s_n^2\widetilde T_n
}
\tag{14}
\]

exactly, where `\widetilde T_n` is uniformly form-comparable to the fixed Pöschl--Teller operator under the PF-230/PF-233 tail bounds.

The conjugated cross-transfer factor is

\[
R_{a_n}=F(s_n\widetilde T_n^{1/2}),
\qquad
F(x)=\frac{x}{\sinh x}.
\tag{15}
\]

Since

\[
F(x)=1-\frac{x^2}{6}+O(x^4)
\qquad(x\to0),
\tag{16}
\]

the identity/principal part itself carries no low/high mixing in any representation where the physical split is respected, and the first formal transfer correction is quadratic in `s_n`.

Equation (16) is **not** promoted here to an `O(s_n^2)` physical-angle theorem. The operators `\widetilde T_n` are unbounded; the physical Fourier split lives in the actual cuff coordinate; PF-233's mass conjugation is nontrivial; and the complete one-cusp-pant contribution contains the common completion retained by the accepted direct-angle clue. The live question is precisely whether these representation/completion steps preserve a fixed superlinear gain on the retained-low/high intrinsic angle.

The value of (2)--(6) is that they identify the correct payoff if even a weak superlinear gain survives: one does not need to sharpen it all the way to `P_n^{-1}`.

## 4. Prior art and novelty audit

No standalone operator-theory or prime-gap novelty is claimed. The only external arithmetic input is Baker, Harman and Pintz, *The Difference Between Consecutive Primes, II*, Proceedings of the London Mathematical Society **83** (2001), 532--562, whose `0.525` short-interval exponent is already audited as S6 in `SOURCES.md` and used in PF-299. The weighted summability (2) is an elementary corollary of PF-299's dyadic proof. The inequality `\|T\|_{\mathcal S_1}\le\operatorname{rank}(T)\|T\|`, two-sided ideal stability, and the Taylor expansion of `x/\sinh x` are classical.

The project-specific content is the synthesis: PF-299's critical seam exponent, PF-318's logarithmic physical-low rank, PF-320's intrinsic-angle localization, and PF-233's exact scaled transfer representation together show that **superlinear seam-scale decay is already endpoint-complete for the shear-deleted direct channel**. The existing reciprocal-prime criterion remains valid but is no longer the weakest useful local target.

## 5. Boundaries and falsification

1. **Conditional local PDE estimate.** This finding does not prove (4) for the actual shear-deleted pant angle. It proves what follows if such a bound is obtained.
2. **Fixed exponent above one.** An estimate `o(s_n)` with no summable quantitative majorant is not enough. The argument needs a fixed `q>1` or another envelope `a_n` satisfying `sum (1+log P_n)a_n<infinity`.
3. **Intrinsic angle, not raw seam block.** PF-319 remains in force. A small perturbation in corridor form or transfer coordinates does not automatically bound a raw seam-normalized mixed block. The target in (4) is the local intrinsic angle used by PF-320.
4. **Completion is not discarded.** The common finite-pant/cusp completion in the accepted clue must remain in the local positive form. Equation (16) is only a guide to the diagonal corridor contribution, not permission to omit completion terms.
5. **Shear remains only weak trace at the current proof strength.** The reference becoming trace class does not upgrade PF-320's actual shear correction beyond the already established weak-`S_1` endpoint.
6. **No conclusion about the conditional channel.** `T_H` from PF-315--PF-316 remains an independent gate for the full physical `P/H` angle.
7. **No RH conclusion.** Closing this direct-angle gate would remove one operator-ideal obstruction inside the Prime Flute program; it would not prove a zeta-zero correspondence, the critical line, or RH.

A refutation of the new implication would have to break PF-299's weighted dyadic summability, the logarithmic low-rank bound, or the PF-320 contraction-sandwich reassembly. The open mathematical issue is instead whether the local shear-deleted pant angle has any fixed superlinear seam-scale gain.

## Consequence for the research line

The accepted direct-angle clue should now treat

\[
\boxed{
\|T_{0,n}^{(r)}\|=O(s_n^{1+\varepsilon})
\quad\text{for one fixed }\varepsilon>0
}
\]

as an endpoint-complete positive outcome. This is weaker and more geometry-native than demanding reciprocal-prime decay module by module. PF-233 suggests testing first whether its quadratic small-`s_n` transfer cancellation survives the physical `L/H` representation and the full common pant completion. If it does, the shear-deleted reference direct angle is already trace class; PF-320 then adds the real shear at the established weak-trace cost.