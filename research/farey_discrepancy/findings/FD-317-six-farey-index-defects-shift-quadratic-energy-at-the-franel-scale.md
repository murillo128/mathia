# FD-317 — Six Farey-index defects shift quadratic energy at the Franel scale

**Status:** `EXACT-DERIVED + PRIME-ORDER-FAMILY + FRANEL-SCALE-ENERGY-SHIFT + ENDPOINT-LOCALIZATION`.

`FD-316` constructs, for every prime `p>=7`, a reflection-symmetric reassembly of the genuine directed denominator edges of `F_p` with exactly six noninteger Hall--Shiu stitches. The present finding quantifies the cumulative quadratic discrepancy cost of that reassembly.

Let

`N_p = sum_(m<=p) phi(m)`

be the number of Farey gaps and let

`E_p = sum_(k=1)^(N_p-1) (x_k-k/N_p)^2`

for the genuine Farey grid. Let `E_p^*` be the same energy for the FD-316 reassembled grid obtained by swapping `E_1,E_2` and, symmetrically, their reflected excursions.

Then

`boxed(E_p^* - E_p = C/p + O(log p/p^2))`

with

`C = 5/3 + 12 log 2 - 8 log 3 + (pi^2/3)(4 log 3 - (16/3) log 2 - 17/18)`

and numerically

`C = 0.383660034465780... > 0`.

Thus a fixed set of six local stitch defects can change the complete quadratic rank-grid energy on the exact `1/p` power scale. Since the classical Franel--Landau criterion is sensitive to quadratic discrepancy on that same power scale, this is a genuine asymptotic control-design obstruction rather than only a finite nondegeneracy example.

The perturbation is nevertheless endpoint-localized. For every sublinear even-mode cutoff `q=o(p)`, if `Delta d_(2r)` denotes the change in the even Dirichlet coefficient between the two grids, then

`boxed(p sum_(r<=q) |Delta d_(2r)|^2 = O((q/p)^3) -> 0)`.

This last statement concerns the energy of the **difference vector itself**. It does not imply that the difference of the two restricted spectral energies is negligible, because the cross term with the original Farey discrepancy remains uncontrolled.

## 1. Geometry of the two swapped excursions

Use the notation of FD-316. The first two prime-order excursions are

- `E_1`, from `1/p` to `2/p`, with `L_1=(p+1)/2` gaps;
- `E_2`, from `2/p` to `3/p`, with `L_2=floor(p/3)+1` gaps.

Write the discrepancy at a point `x_k` as

`D_k = x_k - k/N_p`.

Inside `E_1`, after `r` local gaps, write the discrepancy as `A_r` for `1<=r<=L_1`. Inside `E_2`, after `s` local gaps, write it as `B_s` for `1<=s<=L_2`.

After swapping the two excursions, the `E_2` points are translated left by `1/p` and their ranks are shifted earlier by `L_1). Hence every `B_s` is shifted by the same amount

`delta_B = L_1/N_p - 1/p`.

Likewise the translated `E_1` points are shifted right by `1/p` and their ranks are delayed only by `L_2), so every `A_r` is shifted by

`delta_A = 1/p - L_2/N_p`.

The right-hand reflected swap contributes exactly the same energy change. Therefore the total energy difference is the exact finite identity

`boxed(
E_p^* - E_p
 = 2[
   2 delta_B sum_(s=1)^L2 B_s + L_2 delta_B^2
 + 2 delta_A sum_(r=1)^L1 A_r + L_1 delta_A^2
 ])
`.

No approximation has entered yet.

## 2. Exact first-excursion moment

Between `1/p` and `2/p`, the interior Farey fractions are exactly

`1/q,  p/2 < q < p`.

Thus the points encountered after leaving `1/p` are

`1/(p-1), 1/(p-2), ..., 1/((p+1)/2), 2/p`.

Consequently

`sum A_r
 = sum_(q=(p+1)/2)^(p-1) 1/q
   + 2/p
   - L_1(L_1+3)/(2N_p)`.

Using

`N_p = (3/pi^2)p^2 + O(p log p)`

and the elementary harmonic-number expansion gives

`boxed(sum A_r = log 2 - pi^2/24 + O(log p/p))`.

Also

`delta_A
 = (1 - pi^2/9)/p + O(log p/p^2)`.

## 3. Exact second-excursion moment

Between `2/p` and `3/p`, an interior reduced fraction has numerator only `1` or `2`.

The numerator-one points are

`1/q,  p/3 < q < p/2`.

The numerator-two points are

`2/q,  2p/3 < q < p,  q odd`.

The endpoint is `3/p`. Hence, independently of their interlacing order,

`sum B_s
 = sum_(p/3<q<p/2) 1/q
 + sum_(2p/3<q<p, q odd) 2/q
 + 3/p
 - [L_2(1+L_1) + L_2(L_2+1)/2]/N_p`.

The two reciprocal sums each contribute `log(3/2)+O(1/p)`, while the rank term contributes `2 pi^2/27 + O(log p/p)`. Therefore

`boxed(sum B_s = 2 log(3/2) - 2 pi^2/27 + O(log p/p))`.

Similarly,

`delta_B
 = (pi^2/6 - 1)/p + O(log p/p^2)`.

## 4. The asymptotic constant

Set

`a = pi^2/6 - 1`,

`b = 1 - pi^2/9`,

`S_A = log 2 - pi^2/24`,

`S_B = 2 log(3/2) - 2 pi^2/27`.

Substituting the previous expansions into the exact finite energy identity gives

`E_p^* - E_p
 = (2/p)[2 a S_B + 2 b S_A + a^2/3 + b^2/2]
   + O(log p/p^2)`.

The bracket simplifies exactly to

`C/2`,

where

`C = 5/3 + 12 log 2 - 8 log 3
     + (pi^2/3)(4 log 3 - (16/3) log 2 - 17/18)`.

Numerically,

`C = 0.383660034465780...`.

In particular, the sign is eventually positive and

`boxed(E_p^* - E_p ~ C/p)`.

The exact rational audits for `p=7,11,13,17` agree with the finite identity before asymptotic expansion. For `p=7`, as already recorded in FD-316,

`E_7^* - E_7 = 383/13230 > 0`.

## 5. Endpoint localization of the perturbation

The excursion permutation changes the point grid only inside the two endpoint windows

`[1/p,3/p]`

and

`[1-3/p,1-1/p]`.

Let `h_p(x)` be the difference between the alternative and genuine discrepancy functions in the natural piecewise-linear interpolation. Reflection makes `h_p` antisymmetric.

The support of `h_p` has total length `O(1/p)`, while its amplitude is `O(1/p)`: the only shifts are a geometric translation by `1/p` and a normalized rank shift of size `(L_1-L_2)/N_p = O(1/p)`.

For an even sine/Dirichlet mode of frequency `r`, the coefficient difference therefore satisfies, after one cancellation from antisymmetry and one first-moment estimate on the endpoint support,

`|Delta d_(2r)| = O(r/p^2)`

uniformly for `r=o(p)`.

Consequently, for every `q=o(p)`,

`p sum_(r<=q) |Delta d_(2r)|^2
 <= O( p * p^-4 * sum_(r<=q) r^2 )
 = O((q/p)^3)`.

Thus the perturbation is asymptotically invisible in every sublinear even-mode band when measured by the norm of the difference vector itself, despite shifting the **total** quadratic discrepancy by `Theta(1/p)`.

This localization is consistent with the endpoint hierarchy isolated by the Visual/Farey work: the six-defect reassembly changes endpoint organization, not an obviously interior low-frequency mechanism.

## 6. Control-design consequence

FD-316 already shows that “all but six stitches are Farey-compatible” is not enough to reconstruct the order. The present result quantifies the cost of those six defects.

A bounded number of strategically located stitch defects can alter the complete quadratic discrepancy at the same `1/p` power scale on which one would hope to distinguish meaningful Farey suppression. Therefore a quotient-level control cannot safely treat exceptional stitches as a negligible contamination merely because their density is `O(p^-2)`.

At the same time, the sublinear-band estimate shows that this particular obstruction is spectrally endpoint-localized. For the accepted clue on spectral-allocation suppression, the next useful matched control should therefore be **state-aware and interior-aware**: it should remember enough about where index defects occur to forbid endpoint rewiring, while still leaving a nondegenerate sample space for testing genuinely interior spectral allocation.

## 7. Boundaries

- The alternative grid is not another Farey sequence.
- The six exceptional denominator labels are not globally the actual reduced denominators of the reconstructed points.
- The asymptotic statement is about the complete quadratic rank-grid energy of this explicit prime family.
- The estimate on `Delta d_(2r)` controls only the norm of the perturbation vector; it does not control the cross term with the original Farey coefficients.
- No lower bound is proved for a genuinely interior sublinear spectral residual.
- No Franel--Landau improvement, Möbius cancellation estimate, or RH consequence is claimed.
