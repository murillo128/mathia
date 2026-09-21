# MC-446 — Source-frame box mean square has a quadratic occupancy threshold

**Status:** `EXACT-DERIVED` · `CLASSICAL-IDENTITY` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the incomplete translated-correlation branch isolated by `MC-413`. For a primitive Dirichlet character `chi (mod q)` define, for `1 <= H <= q`,

\[
S_H(u,a):=\sum_{k=1}^{H}\chi(u+k+a)\overline{\chi(u+k)},
\qquad u,a\pmod q.
\tag{1}
\]

The complete two-parameter mean square over the translation/start variables is exactly

\[
\boxed{
E_q(H):=\sum_{u\bmod q}\sum_{a\bmod q}|S_H(u,a)|^2
=\sum_{1\le k,l\le H}|c_q(k-l)|^2,
}
\tag{2}
\]

where `c_q` is the Ramanujan sum. Equivalently,

\[
E_q(H)=H\varphi(q)^2+2\sum_{r=1}^{H-1}(H-r)|c_q(r)|^2.
\tag{3}
\]

If `H <= P^-(q)`, where `P^-(q)` is the least prime factor of `q`, then every nonzero difference `|k-l|<H` is coprime to `q`, so

\[
\boxed{
E_q(H)=H\varphi(q)^2+H(H-1)|\mu(q)|^2.
}
\tag{4}
\]

In particular, for squarefree `q`,

\[
E_q(H)=H\varphi(q)^2+H(H-1).
\tag{5}
\]

Thus the full ambient `(u,a)` box has root-mean-square correlation of order `sqrt(H)` when `varphi(q)\asymp q`: strong collective cancellation is genuinely present before completion.

However, the CRT/source-frame family from `MC-413` occupies only a weighted subset of this `q^2`-point box. Aggregate all divisor-pair contributions mapping to the same pair `(u,a)` into a complex weight `W(u,a)` and consider

\[
T:=\sum_{u,a\bmod q}W(u,a)S_H(u,a).
\tag{6}
\]

Cauchy--Schwarz and `(2)` give

\[
|T|\le \|W\|_2\sqrt{E_q(H)},
\tag{7}
\]

whereas the pointwise bound `|S_H(u,a)| <= H` gives

\[
|T|\le H\|W\|_1.
\tag{8}
\]

Define the effective occupancy

\[
R_{\mathrm{eff}}(W):=\frac{\|W\|_1^2}{\|W\|_2^2}.
\tag{9}
\]

For the generic ambient-box `L^2` estimate `(7)` to beat the trivial estimate `(8)`, it is necessary that

\[
\boxed{
R_{\mathrm{eff}}(W)>\frac{E_q(H)}{H^2}.
}
\tag{10}
\]

Hence in the squarefree rough range `H <= P^-(q)`,

\[
\boxed{
R_{\mathrm{eff}}(W)>
\frac{\varphi(q)^2}{H}+\frac{H-1}{H}.
}
\tag{11}
\]

When `varphi(q)\asymp q`, the leading requirement is

\[
R_{\mathrm{eff}}(W)\gtrsim \frac{q^2}{H}.
\tag{12}
\]

Since `R_eff(W)` is at most the cardinality of the support of `W`, merely embedding a sparse family of CRT/source frames into the full `(u,a)` box and applying the exact ambient mean square plus Cauchy cannot provide a source-frame gain unless the family occupies roughly `q^2/H` effective points. This is a **quadratic occupancy barrier for generic ambient `L^2` averaging**, not a no-go for structured dispersion on the arithmetic image of the divisor-pair map.

The accepted averaged-qVdC clue is therefore narrowed rather than killed. The full box proves that incomplete translated correlations possess collective cancellation, but it also proves that this cancellation is too diluted to help an arbitrary sparse source family. Any viable continuation must exploit arithmetic structure of the actual map

\[
(d,e)\longmapsto
\left(
 u_{d,e},a_{d,e}
\right)
=\left(
 r[d,e]^{-1},h[d,e]^{-1}
\right)\pmod q,
\tag{13}
\]

with `r=0 (mod e)` and `r=-h (mod d)`, rather than treating its image as an unstructured subset of the ambient box.

No new bound for `M(x)`, a twisted Mertens sum, or an individual incomplete character correlation follows.

## 1. Primitive autocorrelation gives the exact box moment

For a primitive Dirichlet character modulo `q`, `MC-413` records the classical identity

\[
C_q(t):=\sum_{x\bmod q}\chi(x+t)\overline{\chi(x)}=c_q(t).
\tag{14}
\]

Expand `(1)` and sum its square over `u` and `a`:

\[
E_q(H)
=\sum_{k,l\le H}
\sum_{u,a\bmod q}
\chi(u+k+a)\overline{\chi(u+k)}
\overline{\chi(u+l+a)}\chi(u+l).
\tag{15}
\]

For fixed `u,k,l`, translation in `a` gives

\[
\sum_{a\bmod q}
\chi(u+k+a)\overline{\chi(u+l+a)}
=c_q(k-l).
\tag{16}
\]

The remaining `u`-sum is the conjugate autocorrelation and therefore equals `c_q(l-k)=\overline{c_q(k-l)}`. Thus the `(k,l)` contribution is exactly `|c_q(k-l)|^2`, proving `(2)`.

Separating the diagonal `k=l`, where `c_q(0)=varphi(q)`, and grouping equal nonzero differences yields `(3)`.

If `H <= P^-(q)`, every integer `r` with `1 <= r < H` is coprime to `q`; the standard Ramanujan formula then gives `c_q(r)=mu(q)`. This proves `(4)`, and `(5)` follows when `q` is squarefree.

For prime `p` the specialization is

\[
E_p(H)=H(p-1)^2+H(H-1),
\qquad H\le p.
\tag{17}
\]

So over the `p^2` ambient pairs the mean square is asymptotic to `H` when `H=o(p^2)`, with root mean square asymptotic to `sqrt(H)`. The phenomenon is not a failure of cancellation in the incomplete correlations themselves; the issue is whether the arithmetic source frames sample enough of that cancellation in a usable way.

## 2. Effective occupancy is the exact generic-Cauchy threshold

Let `W` be any finitely supported complex weight on `(Z/qZ)^2`. Multiple divisor pairs that produce the same `(u,a)` are first combined into `W(u,a)`, so collisions are counted correctly rather than artificially inflating the number of source frames.

Applying Cauchy--Schwarz to `(6)` gives `(7)` directly from `(2)`. On the other hand `|S_H|<=H` gives `(8)`. Squaring the strict inequality required for `(7)` to improve `(8)` gives

\[
\|W\|_2^2 E_q(H)<H^2\|W\|_1^2,
\tag{18}
\]

which is exactly `(10)`.

The quantity `R_eff` is the participation ratio of the weight magnitudes: it equals the support size for equal-magnitude weights and decreases when mass is concentrated. Therefore `(11)` is stronger than a mere count of nominal divisor pairs. A source family can contain many pairs but still fail the ambient-L2 threshold if collisions or highly uneven coefficients reduce its effective occupancy.

In the rough squarefree regime and `varphi(q)\asymp q`, the dominant diagonal contribution `H varphi(q)^2` to `(5)` forces the scale `q^2/H`. The off-diagonal term contributes only about one additional effective point. The obstruction is therefore the diagonal energy of the full two-parameter box, not a weakness in estimating the off-diagonal Ramanujan sums.

## 3. Relation to the CRT/source-frame family

For one compatible divisor pair in `MC-413`, set `L=[d,e]`, let `r (mod L)` solve

\[
r\equiv0\pmod e,
\qquad r\equiv-h\pmod d,
\tag{19}
\]

and assume `(de,q)=1`. Writing `n=r+Lk` turns the character phase into

\[
\chi(k+u+a)\overline{\chi(k+u)},
\quad
u\equiv rL^{-1}\pmod q,
\quad
a\equiv hL^{-1}\pmod q.
\tag{20}
\]

`MC-413` proved that after a complete `q`-block, `u` and the divisor-dependent part of `a` disappear into the universal Ramanujan scalar. Hence the live information is precisely in incomplete sums of the form `(1)`.

Equation `(2)` now answers the first natural collective question: if `u` and `a` were free ambient variables, their incomplete correlations have excellent total second moment. Equation `(11)` answers the second: a sparse arithmetic subfamily cannot inherit that gain merely by Cauchy against the full box.

This separates two very different continuations:

1. **Ambient averaging only.** Regard the source frames as arbitrary weighted points in `(Z/qZ)^2` and use no further arithmetic information. Then `(10)`--`(12)` give the necessary occupancy threshold.
2. **Structured source-frame averaging.** Use the special relation `a=hL^{-1}`, the CRT formula for `u`, fibres/collisions of `(d,e)->(u,a)`, factorability of the outer coefficients, dispersion between frames, or a restricted Fourier geometry. The present finding does not bound that route; it identifies it as the only remaining place where the accepted clue can gain over generic ambient `L^2`.

The next useful calculation should therefore be a **restricted-frame second moment or dispersion form**, not another full-box moment. In particular, one should test whether fixing/grouping `a=hL^{-1}` and averaging only over the compatible `u`-fibres produces a diagonal smaller than the `H varphi(q)^2` ambient tariff after the divisor weights are inserted.

## 4. Prior art and novelty boundary

The primitive-character autocorrelation `(14)`, Ramanujan sums, their values at coprime shifts, and finite Plancherel are classical. Equation `(2)` is an immediate exact consequence of those identities; no novelty is claimed for the ambient box moment itself.

The broader problem of gaining cancellation in incomplete sums before completion is also established prior art. Fouvry--Kowalski--Michel, *The sliding-sum method for short exponential sums* (arXiv:1307.0135), develops interval and generalized-arithmetic-progression estimates precisely in ranges where straightforward Fourier completion is insufficient. Fouvry--Kowalski--Michel--Raju--Rivat--Soundararajan, *On short sums of trace functions* (arXiv:1508.00512), strengthens this perspective around the square-root range. Irving, *Estimates for Character Sums and Dirichlet L-Functions to Smooth Moduli* (IMRN 2016; arXiv:1503.07156), uses the q-analogue of van der Corput to exploit modulus factorization in short primitive character sums.

Those references show that incomplete oscillatory sums and collective transformations of them are a classical analytic surface. They do not, by themselves, provide an estimate for the specific well-factorable CRT image `(13)` or its effective occupancy. Conversely, `(10)`--`(12)` do not improve any of those classical short-sum estimates.

A targeted audit on 21 September 2026 found standard full-family moment/short-sum machinery but no source establishing the **specific effective-occupancy threshold obtained by inserting the `MC-413` CRT/source-frame family into the full `(u,a)` second moment**. Absence from this bounded audit is not a novelty proof. The durable contribution claimed here is only the branch-specific no-go: full ambient second-moment cancellation is insufficient for a sparse source family unless its effective occupancy crosses `(10)`, so the retained-variable program must now exploit the arithmetic subset itself.

## Boundaries and falsification tests

- **Primitivity is required for `(14)` in the stated form.** Imprimitive characters have extra conductor/presentation structure and must be reduced to their primitive conductor before comparison.
- **The rough simplification is conditional on `H <= P^-(q)`.** If `H` exceeds the least prime factor, some differences share factors with `q` and `|c_q(r)|` can be larger; use the exact formula `(3)` rather than `(4)`--`(12)`.
- **Squarefreeness matters in `(5)`.** For non-squarefree `q`, `mu(q)=0`, so the coprime off-diagonal Ramanujan contribution in `(4)` vanishes; the exact statement `(2)` remains valid.
- **A common interval length `H` is assumed.** The CRT family in applications may have variable incomplete lengths. A dyadic decomposition, maximal inequality, or a genuinely variable-length second moment is required before importing `(11)` unchanged.
- **Collisions are not free occupancy.** Distinct divisor pairs with the same `(u,a)` must be combined into `W`; `R_eff` then records the actual weighted image rather than the number of preimages.
- **The obstruction is only to generic ambient `L^2` plus Cauchy.** A structured subset may admit a much sharper restricted moment, a bilinear/dispersion estimate, or cancellation in the weights. This finding does not rule those out.
- **The relation `a=hL^{-1}` is unused by the ambient box.** It may be the principal retained variable rather than an inconvenience. A future argument that uses it is outside the no-go proved here.
- **No zero-free region, RH-scale Mertens estimate, or random-walk model is imported.** The derivation is finite character harmonic analysis plus the CRT coordinates already established in `MC-413`.

## Consequence for the research line

The accepted averaged-qVdC clue survives, but its naive version is closed. The ambient two-parameter box exhibits `sqrt(H)`-scale RMS cancellation, yet its diagonal energy forces a source family of effective size about `q^2/H` before plain Cauchy can convert that cancellation into an aggregate improvement.

The live question is now narrower and more arithmetic: **does the actual well-factorable CRT image `(d,e)->(u,a)` have a restricted second moment, fibre decomposition, or dispersion structure whose diagonal cost is parametrically below the full-box `q^2/H` occupancy threshold?** If not, averaging incomplete q-vdC correlations over source frames will merely relocate the source-depth tariff rather than reduce it.