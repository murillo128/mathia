# WI-069 — freeing both Yang shifts moves the coefficient wall into a power-index slope slice

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It narrows the positive escape left open by WI-068. The actual Yang `k`-average does make the unsliced three-variable prime system finite complexity, but it does not by itself turn the power-coefficient lock into the coefficient-free free-shift average covered by existing linear-forms theorems.

For fixed reduced coefficients `r,q`, the exact source shifts are

\[
(h_1,h_2)=(rk,qk).
\]

If one promotes `h_1,h_2` to independent variables, the four prime forms become the bounded-coefficient system

\[
(m,\ m-h_1,\ n,\ n-h_2),
\]

but the source then occupies only the one-dimensional slope slice `(h_1,h_2)=(rk,qk)` inside the two-dimensional free-shift box. For `1\le k\le K`, that slice has density exactly `1/(rqK)` in the natural rectangle of side lengths `rK` and `qK`. In the cyclic model its normalized selector has **exact Fourier support of cardinality `rqK`**. Thus a termwise attempt to recover the source slice from a coefficient-free free-shift theorem pays a factor `rqK`; logarithmic relative error cannot absorb this on the source long-shift range, where the public Yang scaling gives `K\asymp Y/\max(r,q)` and hence

\[
rqK\asymp Y\min(r,q)\ge Y.
\]

The coefficient wall therefore has a precise conservation law: keeping the source one-dimensional shift variable leaves the growing coefficients `r,q`; freeing the shifts removes those coefficients from the prime forms but reintroduces them as a power-index projection back to the source slope. A successful Shao--Teräväinen-style repair must do something genuinely stronger than either black-box step: aggregate the **whole changing-slope base family** before applying the theorem, prove an anisotropic/slice-uniform estimate normalized by the source cardinality, or exploit additional arithmetic cancellation in the slope selector.

## 1. Exact source lock

The pinned public Yang source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For fixed prime-power bases `b_1,b_2`, put

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g.
\tag{1}
\]

The exact equal-lock swap in `scripts/t2_swaps.py` is

\[
m'=m-rk,\qquad n'=n-qk,
\tag{2}
\]

so the off-diagonal four-prime object contains the affine forms

\[
\boxed{
L_1=m,\qquad L_2=m-rk,\qquad L_3=n,\qquad L_4=n-qk.
}
\tag{3}
\]

The public paper states the structured shift range as

\[
K\asymp \frac{Y}{\max(r,q)}
\tag{4}
\]

on windows of length `Y` in the long-range welding regime. The exact physical cutoffs and moving strip boundaries do not affect the algebra below; restricting `k` to a shorter interval only replaces `K` by that interval length.

WI-039 and WI-040 already establish the first side of the dichotomy. As a three-variable system in `(m,n,k)`, (3) is finite complexity, but its coefficient norm is at least `max(r,q)/2` after **every** lattice-preserving reparameterization. Published Green--Tao/Bienvenu/MRSTT transference therefore does not black-box cover the dominant power-sized reduced coefficients.

WI-068 leaves open a different thought: because the source genuinely averages over `k`, perhaps one can use a free-shift finite-complexity theorem such as Shao--Teräväinen Theorem 2.7 rather than asking for a fixed-shift twin-pair estimate. The exact geometry of that lift is what is audited here.

## 2. The coefficient-free lift has one extra shift dimension

Introduce the two physical pair shifts

\[
h_1=rk,\qquad h_2=qk.
\tag{5}
\]

If `h_1,h_2` are allowed to vary independently, (3) becomes

\[
\boxed{
\widetilde L_1=m,\qquad
\widetilde L_2=m-h_1,\qquad
\widetilde L_3=n,\qquad
\widetilde L_4=n-h_2.
}
\tag{6}
\]

The four homogeneous coefficient rows in variables `(m,n,h_1,h_2)` are

\[
(1,0,0,0),\quad
(1,0,-1,0),\quad
(0,1,0,0),\quad
(0,1,0,-1).
\tag{7}
\]

They are a fixed finite-complexity system with coefficient size `1`. This is the attractive coefficient-free interface.

But the Yang source is **not** the full `(h_1,h_2)` average. It is the slope line

\[
\boxed{
\mathcal L_{r,q}(K)
:=\{(rk,qk):1\le k\le K\}.
}
\tag{8}
\]

The natural independent-shift rectangle containing it is

\[
\mathcal R_{r,q}(K)
:=\{1,\ldots,rK\}\times\{1,\ldots,qK\}.
\tag{9}
\]

There are exactly

\[
|\mathcal L_{r,q}(K)|=K,
\qquad
|\mathcal R_{r,q}(K)|=rqK^2,
\tag{10}
\]

hence

\[
\boxed{
\frac{|\mathcal L_{r,q}(K)|}{|\mathcal R_{r,q}(K)|}
=\frac1{rqK}.
}
\tag{11}
\]

This is not a boundary artifact or a rough density estimate. It is the exact cardinality cost of replacing the one booked source shift by two independent coefficient-free shifts.

Using the public long-range scaling (4),

\[
\boxed{
rqK\asymp Y\min(r,q).}
\tag{12}
\]

In particular `rqK\gg Y`. Since the relevant Yang windows have polynomial length in the ambient scale (`Y\asymp X^\vartheta`, with `\vartheta>1/2` in the printed long-window interface), the source line is power-sparse inside the independent-shift rectangle even before using the fact that `r,q` themselves are power-sized on dominant Mertens mass.

The alternate matched-scale normalization reconstructed in WI-051--WI-053 gives the same conclusion in its cell variables: whatever precise bookkeeping convention is used for the physical `K`, the ratio is always the exact quantity `1/(rqK)` once the two shift ranges are `rK` and `qK`.

## 3. Exact cyclic Fourier projection costs `rqK` modes

The thin-slice issue is sharper than a visual dimension count. It has an exact Fourier formulation.

Let

\[
G=\mathbb Z/(rK)\mathbb Z\times\mathbb Z/(qK)\mathbb Z
\tag{13}
\]

and let

\[
H=\{(rk,qk):k\in\mathbb Z/K\mathbb Z\}\subseteq G.
\tag{14}
\]

The map from `Z/KZ` is injective, so

\[
|H|=K,
\qquad
|G|=rqK^2,
\qquad
[G:H]=rqK.
\tag{15}
\]

Let `H^perp` be the annihilator subgroup in the character group `G^`. Classical finite-group orthogonality gives

\[
|H^\perp|=[G:H]=rqK
\tag{16}
\]

and the exact identity

\[
\boxed{
[rqK]\,1_H(x)
=\sum_{\chi\in H^\perp}\chi(x).
}
\tag{17}
\]

The left side is the selector normalized to have ambient mean `1`. Therefore for any function `F:G\to\mathbb C`,

\[
\boxed{
\frac1K\sum_{x\in H}F(x)
=
\sum_{\chi\in H^\perp}
\mathbb E_{x\in G}F(x)\chi(x).
}
\tag{18}
\]

Thus the most direct Fourier/nilsequence projection of the free-shift average back to the exact Yang line contains **`rqK` separate character modes with coefficient one**.

Suppose a black-box free-shift theorem supplied, uniformly for every admissible bounded-complexity character twist, only

\[
\left|\mathbb E_G F\chi-\text{main}_\chi\right|\le\varepsilon_X.
\tag{19}
\]

Termwise insertion into (18) gives at best

\[
\boxed{
\text{source-slice error}\le rqK\,\varepsilon_X.
}
\tag{20}
\]

Consequently any purely termwise route requires

\[
\varepsilon_X=o((rqK)^{-1}).
\tag{21}
\]

A fixed logarithmic saving `\varepsilon_X=(\log X)^{-A}` cannot meet (21) on the polynomial long-shift range (12), for any fixed `A`.

Equation (20) is **not** a lower bound on the true prime error and does not prove that the Fourier modes add coherently. It proves the narrower black-box statement needed here: a full free-shift asymptotic or individual logarithmically-saving character estimates do not automatically recover the power-index Yang slope slice. One needs a square-function/orthogonality gain across the projection modes, a source-specific cancellation, or a theorem already normalized by the sparse slice.

## 4. Equivalent formulation: the large coefficients have only moved into the support constraint

There are now two exact representations of the same cell.

### Source-faithful representation

Use variables `(m,n,k)` and forms

\[
(m,m-rk,n,n-qk).
\tag{22}
\]

The domain has the correct dimension and the source `k`-average is explicit, but the prime forms have power-sized coefficients `r,q`. WI-040 shows that no `GL_3(Z)` change removes them.

### Coefficient-free representation

Use variables `(m,n,h_1,h_2)` and forms

\[
(m,m-h_1,n,n-h_2).
\tag{23}
\]

The prime forms now have fixed coefficients, but the domain must satisfy

\[
\boxed{q h_1-r h_2=0}
\tag{24}
\]

with the primitive spacing selecting exactly (8). Parameterizing (24) by its primitive integer direction gives back `(h_1,h_2)=(rk,qk)` and therefore returns to (22). Treating `(h_1,h_2)` as free removes (24) and enlarges the source by the exact index (15).

So the large arithmetic data cannot disappear by this lift:

\[
\boxed{
\text{large coefficients in the forms}
\quad\longleftrightarrow\quad
\text{large-index slope selector in the domain}.}
\tag{25}
\]

This is the non-unimodular analogue, at the free-shift interface, of the coefficient-content invariant in WI-040.

## 5. Relation to Shao--Teräväinen and WI-068

Shao--Teräväinen, *The Bombieri--Vinogradov theorem for nilsequences*, Discrete Analysis 2021:21, Theorem 2.7, proves a prime-pattern asymptotic for finite-complexity affine-linear systems of fixed size in genuine free summation variables, for almost all moduli in its stated range. WI-068 correctly repaired an earlier overclaim by observing that the theorem opens a free-shift rectangle but does not control a prescribed fixed twin-prime slice.

The present calculation addresses the remaining optimistic sentence in WI-068 more precisely. The Yang source certainly has an average over `k`, but at a fixed cell that one variable moves **both** pair shifts along the locked direction `(r,q)`. It is not the two-dimensional free-shift average (23). Therefore one cannot consume Theorem 2.7 cellwise by saying merely that “the source already averages over the shift.”

There are two possible theorem interfaces:

1. apply a finite-complexity theorem directly to the genuine three-variable source system (22), which returns to the fixed/polylog coefficient boundary of WI-039--WI-040; or
2. apply a coefficient-free theorem to (23), then project to (24), which incurs the power-index thin-slice problem (11)--(21).

This does **not** contradict the positive free-shift statement in WI-068. It says that the actual Yang average is not that free shift at fixed `(r,q)`.

## 6. What remains genuinely open

The finding deliberately does not rule out three harder escapes.

First, one may aggregate over the entire changing base family `(r,q)` **before** invoking a theorem. The union of many slope lines is not one fixed `H`, and its source Mertens weights may have exploitable arithmetic structure. Such a proof must derive the exact global weight after the change `(r,q,k)\mapsto(h_1,h_2)` and control it; the present result does not assert that the union remains power-sparse.

Second, an anisotropic prime-pattern theorem could be uniform on the source line itself, with error normalized by `K` rather than by the ambient `rqK^2` shift volume. This would be genuinely new slice/coefficient uniformity of exactly the kind already isolated by WI-039, WI-047, WI-053, and WI-068.

Third, a Hilbert-space or large-sieve argument could beat the `l^1` projection cost in (20) by exploiting orthogonality across the `rqK` annihilator modes. Such a gain would have to be proved for the actual four-prime/local-main residual; it does not follow from a collection of separate logarithmically-saving estimates.

These are meaningful distinctions. The result closes the cheap cellwise route, not the Yang one-sided fourth-moment program.

## 7. Prior-art and novelty audit

The subgroup identity (17) is elementary finite Fourier analysis, and no novelty is claimed for it, for dimension counting, for the fact that parametrizing an integer line reintroduces its primitive direction coefficients, or for the general principle that an average over an ambient box need not control a sparse slice.

The literature-backed theorem boundaries are already anchored in `SOURCES.md`: Green--Tao's finite-complexity framework, Bienvenu's polylogarithmic coefficient extension, MRSTT 2026's fixed-coefficient transference interface, and Shao--Teräväinen 2021 Theorem 2.7. A targeted prior-art check around linear equations in primes on convex bodies, large-index sublattices, and growing coefficients located no black-box theorem whose printed hypotheses simultaneously give fixed-coefficient free-shift asymptotics and density-normalized control on the power-index Yang slope slice. That bounded negative search is **not** used as an impossibility or priority claim.

The new exact deduction recorded here is the Yang-specific combination of the source lock with that theorem boundary: the seemingly coefficient-free lift has source density `1/(rqK)`, and its normalized cyclic selector has exactly `rqK` Fourier modes. This converts the vague “source shift average may restore the theorem interface” possibility left in WI-068 into a precise gate.

## 8. Decisive verification / falsification gate

Narrow or retire this finding if any of the following fails.

1. Reconstruct (2) from the pinned `t2_swaps.py` equal-lock identity and verify the reduced coefficients (1).
2. Check that the independent-shift lift is exactly (6) and that imposing the source relation gives (8)/(24).
3. Verify the cardinalities (10)--(11) for arbitrary positive integers `r,q,K`.
4. In the cyclic model, verify that (14) has size `K`, index `rqK`, and therefore the character identity (17).
5. Keep the conclusion restricted to **cellwise** freeing/projection. Do not infer from (11) that the union over the full `(r,q)` Mertens ledger has the same density or Fourier cost.
6. If a proposed theorem directly estimates the source slice with error normalized by `K`, or proves joint cancellation across `H^perp`, then (20) is not the relevant consumer and this barrier is bypassed.

## 9. Consequence for `weil_inertia`

The arithmetic decision tree after WI-068 is now sharper:

\[
\boxed{
\begin{array}{c}
\text{keep one source shift }k\\[1mm]
\Downarrow\\[-1mm]
\text{correct source dimension, but coefficients }r,q
\end{array}
\qquad\text{or}\qquad
\begin{array}{c}
\text{free }h_1,h_2\\[1mm]
\Downarrow\\[-1mm]
\text{fixed coefficients, but source index }rqK.
\end{array}}
\tag{26}
\]

Thus the next serious positive route should **not** be another cellwise invocation of a free-shift prime-pattern theorem followed by a naive restriction to `(rk,qk)`. The evidence-changing target is either a global cross-slope regrouping of the full prime-power base ledger, a density-normalized anisotropic/slice theorem, or an `L^2`/large-sieve mechanism that controls the annihilator family collectively. Those are genuinely different inputs; the simple statement “Yang already averages over `k`” is no longer sufficient to bridge WI-068.