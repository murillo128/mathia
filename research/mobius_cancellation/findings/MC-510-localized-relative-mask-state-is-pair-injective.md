# MC-510 — Localized gauge-invariant cross-root state becomes pair-injective

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-RATIONAL-RECONSTRUCTION · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-509` shows that a sufficiently long localized tuple of one-row moving mask roots becomes an injective address for the source prime. There is an important representation objection to using that fact directly: `MC-487` already proved that the individual inverse shifts `h q^{-1}` are affine gauge. The physically meaningful cross-root mask should therefore first quotient that one-row gauge.

After doing so, source-addressing does not disappear. It moves from integer reconstruction to **rational reconstruction of the ordered source pair**.

Fix an odd conductor prime `p`, a nonzero shift `h`, a nonzero residue `a mod p`, and an interval

\[
I\subset [Q,Q+H]
\]

of diameter at most `H`. Consider ordered pairs of distinct source primes `(q,r)` in `I` satisfying

\[
q\equiv r\equiv a\pmod p.
\tag{1}
\]

Choose `z<min I` and put

\[
\mathcal S_z
=\{\ell\le z:\ \ell\text{ prime},\ \ell\ne p,\ \ell\nmid h\},
\qquad
M_z=\prod_{\ell\in\mathcal S_z}\ell.
\tag{2}
\]

At a common lower prime `ell`, the plus/minus first-exit hard mask from `MC-502` has the three candidate forbidden roots

\[
0,\qquad -h q^{-1},\qquad h r^{-1}\pmod\ell.
\tag{3}
\]

Multiplication by the unit `-q h^{-1}` sends `(3)` to the oriented normalized configuration

\[
0,\qquad 1,\qquad -q r^{-1}\pmod\ell.
\tag{4}
\]

Thus the gauge-invariant relative coordinate carried by the oriented cross-root pair is

\[
\lambda_\ell(q,r):=q r^{-1}\pmod\ell.
\tag{5}
\]

Let

\[
\Lambda_z(q,r)
=(\lambda_\ell(q,r))_{\ell\in\mathcal S_z}.
\tag{6}
\]

If two localized ordered pairs have the same relative state,

\[
\Lambda_z(q,r)=\Lambda_z(q',r'),
\tag{7}
\]

then

\[
\boxed{
pM_z\mid q r'-q'r.
}
\tag{8}
\]

The localization gives the deterministic determinant bound

\[
\boxed{
|q r'-q'r|\le 2H(Q+H).
}
\tag{9}
\]

Consequently

\[
\boxed{
pM_z>2H(Q+H)
\quad\Longrightarrow\quad
(q,r)\mapsto\Lambda_z(q,r)
\text{ is injective on the ordered distinct-prime source pairs}.}
\tag{10}
\]

This is the gauge-corrected analogue of `MC-509`. The one-row profile crosses its CRT reconstruction threshold when its modulus exceeds the source **width**. The oriented relative cross-root profile crosses its rational-reconstruction threshold when its modulus exceeds the localized **cross-product uncertainty**, of order `QH` rather than `H`.

Since

\[
\log M_z=(1+o(1))z,
\tag{11}
\]

the extra price is still only logarithmic mask depth. Whenever

\[
R:=\frac{2H(Q+H)}p\to\infty,
\]

any fixed `epsilon>0` and

\[
z=(1+\varepsilon)\log R
\tag{12}
\]

put the state in the injective regime for all sufficiently large scales, subject to `z<min I`. In a dyadic block `I=[Q,2Q]`, the sufficient threshold is

\[
pM_z>4Q^2,
\tag{13}
\]

so, when `Q^2/p -> infinity`, one may take for example

\[
z=(1+\varepsilon)\log(Q^2/p).
\tag{14}
\]

The number of retained lower-prime coordinates is then only of order

\[
\frac{\log(Q^2/p)}{\log\log(Q^2/p)}.
\tag{15}
\]

The key frontier consequence is negative but representation-correct:

> **quotienting the affine one-row mask gauge delays source identification, but does not turn the exact growing cross-root state into a recurrent coarse class. At rational-reconstruction depth it can name the ordered source pair itself.**

Therefore the surviving hard-mask route cannot obtain averaging merely by conditioning on an ever longer exact **relative** root tuple. A useful theorem has to exploit quantitative structure of the map from many distinct pair states to the physical conductor pushforward, use a deliberately coarser state below the reconstruction threshold, exploit endpoint/cutoff geometry before exact conditioning, or create a signed/complex pre-aggregation relation.

No estimate for the anti-diagonal collision excess of `MC-506`, for `M(x)`, or for zeta zeros follows.

## 1. The relative coordinate is exactly the affine-gauge quotient

For an active common lower prime `ell<min(q,r)` with `ell` not dividing `h`, `MC-502` gives the native plus/minus forbidden roots `(3)`. The first nonzero root is a unit. Normalizing it to `1` by multiplication with `-q h^{-1}` gives

\[
-hq^{-1}(-qh^{-1})=1
\pmod\ell,
\]

while the opposite-root coordinate becomes

\[
hr^{-1}(-qh^{-1})=-qr^{-1}
\pmod\ell.
\]

This removes the branchwise inverse-dilation gauge identified by `MC-487` while retaining the **relative** position of the two oriented nonzero roots. Equivalently, the ratio of the two native nonzero root coordinates is `-q r^{-1}`. The plus/minus root orientation is physical, so no arbitrary choice is needed to decide which shifted root is normalized.

The complete-period collision invariant from `MC-502` is only the special event

\[
\lambda_\ell(q,r)=-1
\iff
\ell\mid q+r.
\tag{16}
\]

Thus the `q+r` totient factor of `MC-502` is a very coarse projection of the full relative state `(6)`: it records at which primes one distinguished value occurs, whereas `(6)` keeps the actual relative residue at every retained prime.

## 2. Equality of relative states gives a rational congruence

Suppose `(7)` holds. For every `ell in S_z`, all four source primes are units modulo `ell`, and

\[
q r^{-1}\equiv q'(r')^{-1}\pmod\ell.
\]

Cross multiplication gives

\[
q r'\equiv q'r\pmod\ell.
\tag{17}
\]

The moduli in `S_z` are pairwise coprime, hence

\[
M_z\mid q r'-q'r.
\tag{18}
\]

The repeated conductor-residue condition `(1)` supplies one more independent modulus. Modulo `p`,

\[
q r'-q'r\equiv a^2-a^2\equiv0,
\]

and `(p,M_z)=1`. This proves `(8)`.

This is exactly the elementary uniqueness mechanism behind modular rational reconstruction: equality of two bounded rational residues forces their cross determinant to be a multiple of the reconstruction modulus.

## 3. Localization improves the generic rational-reconstruction tariff

The interval hypothesis is stronger than merely bounding every numerator and denominator by `Q+H`. Write

\[
D:=q r'-q'r.
\]

Using

\[
D=q(r'-r)+r(q-q'),
\]

and the facts `|r'-r|<=H`, `|q-q'|<=H`, `q,r<=Q+H`, one obtains `(9)`:

\[
|D|\le2H(Q+H).
\]

If the modulus `pM_z` is strictly larger than this bound, divisibility `(8)` forces `D=0`. Therefore

\[
\frac qr=\frac{q'}{r'}.
\tag{19}
\]

Both fractions are reduced because each pair consists of distinct primes. Hence equality in `(19)` forces

\[
q=q',\qquad r=r',
\]

proving `(10)`.

The generic rational-reconstruction uniqueness bound with only `q,r<=Q+H` would naturally be quadratic in `Q+H`. Localization replaces that by `O(QH)`. For narrow source blocks `H=o(Q)`, this is a genuine reduction in the amount of modular profile information needed to identify the pair.

## 4. Relation to MC-509 and the live collision question

`MC-509` establishes that the gauge-dependent one-row root tuple identifies `q` once `pM_z>H`. One might object that this source-addressing effect is irrelevant because `MC-487` can remove the individual inverse shifts by a branchwise affine coordinate change.

The present result performs that quotient explicitly. The surviving common-core state is not the pair of absolute root tuples; it is the relative residue `q/r` modulo the growing primorial. Even this quotient becomes pair-injective once the modulus exceeds the localized cross-product uncertainty.

This changes how the accepted full-profile clue should be read. There are now three distinct representation scales:

1. a short fixed local tuple, which remains programmable without localization by `MC-508`;
2. an intermediate relative tuple below rational-reconstruction depth, which is genuinely coarser than source-pair identity and may still support useful averaging;
3. an exact sufficiently long relative tuple, which has enough capacity to reconstruct the ordered pair and therefore supplies no repeated-class averaging by itself.

The anti-diagonal statistic of `MC-506` remains downstream of all three. Injective pair state does **not** imply dispersed conductor coordinate `t=x+j`, and it does not prevent many different pair states from sending mass to the same anti-diagonal. What `(10)` removes is only the idea that exact full-profile **recurrence** can be treated as a free averaging resource after correcting for the affine gauge.

A positive continuation must therefore avoid conditioning away the source population. It needs a theorem about how the continuum of distinct relative states acts on the exact clipped coefficient profiles and the physical addition coordinate, or a theorem using a coarser state whose fibre size is quantitatively charged before the rational-reconstruction threshold.

## Prior art and novelty boundary

The general mathematics is classical modular rational reconstruction. Paul S. Wang, M. J. T. Guy and J. H. Davenport, *P-adic reconstruction of rational numbers*, ACM SIGSAM Bulletin **16** (1982), no. 2, 2–3, DOI `10.1145/1089292.1089293`, proves the classical bounded-numerator/bounded-denominator uniqueness and reconstruction mechanism via continued fractions. The elementary determinant argument above is the same uniqueness principle.

No novelty is claimed for rational reconstruction, CRT, the determinant test, or primorial growth. The line-specific contribution is the **representation-correct specialization** to the surviving first-exit hard-mask frontier: after quotienting the affine inverse-shift gauge of `MC-487`, the oriented plus/minus lower-prime state is the modular rational `q/r`, and tight source localization improves the generic reconstruction threshold from a full `Q^2` scale to the cross-product uncertainty `QH`.

A targeted literature audit on 24 September 2026 found the expected rational-reconstruction theory and no reason to claim a new general number-theory theorem. The durable result is the corrected information-budget boundary for this exact source representation.

## Boundaries and falsification tests

- **Oriented cross-root state.** The theorem keeps the physical plus/minus orientation. If the two shifted forbidden roots are deliberately made unlabeled, additional finite symmetries of the normalized three-point set must be quotiented separately.
- **Common-core primes only.** The state uses primes `ell<=z<min I`, so every retained prime lies below both source primes. One-sided tail primes between `q` and `r`, moving cutoffs, and endpoint data are not needed for the injectivity statement.
- **Distinct primes.** Diagonal pairs `q=r` are excluded. Their ratio is identically one and cannot be reconstructed as two independent source labels from `(6)`.
- **Repeated conductor block.** The extra factor `p` in `(8)` uses `q,r,q',r' congruent a mod p`. Without that condition, the reconstruction modulus is only `M_z` unless separate conductor data are retained.
- **Sufficient, not sharp, threshold.** Equation `(10)` is a deterministic uniqueness condition. It is not claimed to give the exact first scale at which every physical source family becomes injective.
- **Root state is not clipped coefficient state.** Distinct relative root tuples can still produce the same finite clipped coefficient vector, and equal or unequal clipped vectors require their own analysis.
- **Pair identity is not cancellation.** A lossless pair label gives no sign estimate, no anti-diagonal dispersion, and no character-sum saving.
- **Complete-period overlap stays coarse.** `MC-502` uses only collision events `lambda_ell=-1`; pair injectivity of the full tuple does not upgrade that logarithmic/totient coherence into a conductor-power effect.
- **No hidden zero information.** The proof uses only finite congruence algebra, localization, CRT/primorial growth, and the classical rational-reconstruction uniqueness principle.

## Consequence

The gauge objection to `MC-509` is now discharged at the pair level. The exact growing lower-prime state that survives the affine normalization is a modular encoding of the rational source ratio `q/r`; on a localized source block it becomes pair-injective once its primorial modulus exceeds `O(QH/p)`. Exact full-profile conditioning therefore ceases to be an averaging device even after quotienting the one-row gauge.

The live hard-mask question is narrower: either obtain collision control from an **intermediate, deliberately lossy relative state** before it reaches rational-reconstruction capacity, prove structure in the map from many distinct pair states to the physical anti-diagonal pushforward, exploit the moving cutoff/endpoints, or introduce a genuine signed/complex pre-aggregation mechanism. Another appeal to recurrence of the exact growing root profile is closed.