# WI-074 — Scalar lcm projection loses the linked-shift sparsity; sparse-moduli large sieve is not a black-box bridge

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It sharpens one escape hatch left open by WI-071--WI-073.

WI-071 showed that the two-dimensional physical-shift support

\[
(h_1,h_2)=(rk,qk),\qquad (r,q)=1,
\]

is sparse inside the full free-shift square because

\[
\operatorname{lcm}(|h_1|,|h_2|)=rq|k|.
\]

A natural response is to project every source pair to the scalar modulus

\[
L:=\operatorname{lcm}(|h_1|,|h_2|)
\]

and try to import a sparse-moduli large sieve. That projection does **not** preserve the source's two-dimensional sparsity. In the exact Yang source, a single fixed reduced slope already makes the scalar `L`-support positive-density: the off-diagonal prime-power leg pair `(b_1,b_2)=(2,4)` has `(r,q)=(1,2)`, hence `L=2|k|`, so its scalar projection contains every even integer in the corresponding `k`-range. If equal legs are retained, `(r,q)=(1,1)` gives `L=|k|` and the scalar projection is the full integer interval. Thus the `O(Z log^2 Z)` count of **pairs** with `lcm(h_1,h_2)<=Z` cannot be reinterpreted as a sparse set of scalar lcm values.

The closest sparse-large-sieve prior art located in this audit is genuinely scalar-modulus technology. Baker--Munsch--Shparlinski control large-sieve sums over sparse scalar modulus sequences through additive energy; Halupczok--Munsch treat scalar moduli that are values of multivariate polynomials. Neither printed theorem is a black-box estimate for a weighted two-dimensional incidence selector such as `(rk,qk)` or for Yang's locked four-prime covariance. The viable large-sieve target therefore has to retain factorization/direction information: for example a source-weighted two-dimensional incidence large sieve, or an exact transform to scalar `L` that carries the reduced slope/factorization weights rather than discarding them.

## 1. Exact source geometry

The pinned public Yang reproduction source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

For a pair of prime-power legs `b_1,b_2`, write

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g.
\tag{1}
\]

Then `(r,q)=1`, and the equal-lock swap used in the one-sided fourth-moment ledger is

\[
m'=m-rk,\qquad n'=n-qk.
\tag{2}
\]

Thus the two physical prime shifts are

\[
\boxed{h_1=rk,\qquad h_2=qk.}
\tag{3}
\]

The coprimality in (1) gives the exact identities

\[
\boxed{
\gcd(|h_1|,|h_2|)=|k|,
\qquad
L:=\operatorname{lcm}(|h_1|,|h_2|)=rq|k|.
}
\tag{4}
\]

Because each original leg is a prime power, each reduced factor `r,q` is either `1` or a prime power, with distinct prime bases when both exceed `1`.

WI-071 used (4) in the two-dimensional direction: the number of ordered integer pairs `(u,v)` with `lcm(u,v)=n` is `d(n^2)`, so

\[
\#\{(u,v):\operatorname{lcm}(u,v)\le Z\}
=
\sum_{n\le Z}d(n^2)
\ll Z(\log Z)^2.
\tag{5}
\]

That is highly sparse relative to a free `Z x Z` square. Equation (5), however, is a count of **incidences/pairs**, not of distinct scalar values `n`.

## 2. The scalar lcm projection is already dense on fixed source slopes

Take the explicit off-diagonal source cell

\[
(b_1,b_2)=(2,4).
\]

Then `g=2`, `r=1`, `q=2`, so

\[
(h_1,h_2)=(k,2k),
\qquad
L=\operatorname{lcm}(|k|,2|k|)=2|k|.
\tag{6}
\]

As `k` runs through any ordinary integer interval allowed by the source cell, `L` runs through the corresponding interval of even integers. Therefore the scalar lcm support of this single off-diagonal slope has relative density `1/2` in its natural ambient interval. This conclusion does not rely on the equal-leg diagonal.

If equal legs `b_1=b_2` are included in the source sum, then `r=q=1`, and

\[
(h_1,h_2)=(k,k),\qquad L=|k|,
\tag{7}
\]

so the scalar projection contains every integer in the corresponding range. If a later analytic reduction removes or exactly cancels the equal-leg cells, (6) remains a robust positive-density counterexample to the inference that two-dimensional lcm sparsity automatically yields sparse scalar lcm values.

Hence

\[
\boxed{
\text{2-D lcm incidence sparsity}
\not\Longrightarrow
\text{sparse scalar lcm support}.
}
\tag{8}
\]

The sparsity in WI-071 is carried by **direction/factorization incidence**, not by the scalar number `L` alone.

This statement is global. On a separately isolated high-slope cell with fixed large `rq`, the set `L=rq|k|` is of course an arithmetic progression of density `1/(rq)` in a common scalar interval. But exploiting that cellwise sparsity requires retaining `rq` and summing the resulting estimates over the source slope family; it is no longer a projection of the whole Yang support to an unlabelled sparse scalar-modulus set.

## 3. Scalar factorization multiplicity is small but does not restore sparsity

There is nevertheless useful arithmetic structure left after introducing `L`. For fixed `L`, a reduced Yang slope representation satisfies

\[
rq\mid L,
\qquad
k=L/(rq),
\tag{9}
\]

with coprime `r,q`, each equal to `1` or a prime power. The number of prime-power divisors of `L`, counted with the available exponents, is at most `Omega(L)`. Therefore the number of ordered reduced-slope choices is bounded by

\[
\boxed{
\#\{(r,q): rq\mid L,\ (r,q)=1,\ r,q\text{ prime-power-or-1}\}
\le (1+\Omega(L))^2
=O((\log L)^2).
}
\tag{10}
\]

Once `(r,q)` is fixed, `k` is determined by (9). This is only a bound on reduced-slope representations; the original common factor `g`, coefficient weights, overlap geometry, boundary restrictions, and prime-power multiplicities can carry additional source information.

Equation (10) is therefore **not** a sparse-modulus theorem. It says instead that a scalar-`L` reorganization may still be viable if the analytic transform preserves a polylogarithmic family of factorization/direction labels. That is a more precise target than treating `L` itself as a sparse sequence.

## 4. What the closest sparse-large-sieve theorems actually control

Roger C. Baker, Marc Munsch and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659, prove large-sieve estimates for **one-dimensional scalar sequences of moduli**. Their basic large-sieve object is of the form

\[
\sum_j\ \sum_{\substack{a\bmod m_j\\(a,m_j)=1}}
\left|\sum_n a_n e(an/m_j)\right|^2,
\tag{11}
\]

with savings tied to additive-energy information about the scalar modulus sequence `(m_j)`. The paper treats monomial, polynomial, Piatetski--Shapiro and convex sparse sequences, among other examples. This is directly relevant prior art for any proposal that truly reduces Yang to a sparse scalar-modulus family, but it does not itself supply such a reduction.

Karin Halupczok and Marc Munsch, **Large sieve estimate for multivariate polynomial moduli and applications**, *Monatshefte für Mathematik* 197 (2022), 463--478, arXiv:2110.13257, likewise use several variables to **generate a scalar polynomial modulus**. Their theorem is not a large sieve on an arbitrary two-coordinate physical-shift incidence relation.

Thus the word “multivariate” does not remove the interface mismatch. Yang's unresolved object is a coupled four-prime covariance supported on the line family `(rk,qk)` with source weights depending on the coefficient legs and cell geometry. Neither theorem may be invoked merely from the set-theoretic count (5).

No impossibility is claimed for large-sieve methods in general. The prior-art conclusion is narrower:

\[
\boxed{
\text{off-the-shelf sparse scalar-moduli large sieve}
\quad\text{does not black-box consume}\quad
\text{Yang's 2-D lcm incidence sparsity}.
}
\tag{12}
\]

## 5. Consequence for the WI-071 escape hatch

WI-071 deliberately left open “a Hilbert/large-sieve inequality adapted directly to this sparse lcm incidence set.” The present audit separates two very different interpretations of that phrase.

The weak interpretation is now closed: **project to `L=lcm(h_1,h_2)`, observe that the original pair set was sparse, and apply a theorem for sparse scalar moduli.** Equations (6)--(8) show that the required scalar sparsity has disappeared before the large sieve is applied.

The strong interpretation remains live and is now more precise. A useful theorem would have to do at least one of the following:

1. estimate the weighted two-dimensional incidence family `(rk,qk)` directly, normalized to its source cardinality;
2. reorganize by scalar `L` while retaining factorization/direction labels `(r,q)` and the source weights, exploiting the polylogarithmic reduced-slope multiplicity (10);
3. isolate high-slope scalar progressions `L=rqk` and prove estimates strong enough to survive the subsequent sum over source slopes;
4. find a nontrivial higher-dimensional large-sieve embedding whose separation parameter reflects the actual Yang incidence geometry rather than the full free-shift square.

These routes are compatible with WI-070's multivariate polynomial representation and WI-073's conclusion that any successful reboxing must be non-Cartesian/source-adapted.

## 6. Prior-art and novelty boundary

No novelty is claimed for large-sieve theory, the identity `gcd(a,b) lcm(a,b)=ab`, divisor counting, or the Baker--Munsch--Shparlinski / Halupczok--Munsch theorems. A structure-level search around sparse-modulus large sieves, polynomial moduli, multidimensional large sieve, and the existing Mathia Yang findings located no stored result already making the scalar-projection distinction above. WI-071 recorded two-dimensional lcm sparsity and left a generic large-sieve escape; WI-072 quantified source-agnostic `L^p` selector losses; WI-073 ruled out Cartesian coordinate pruning. None of those claims that the set of scalar lcm values is sparse.

The durable Mathia deduction is the exact source-specific boundary: **the pair sparsity lives in incidence/factorization, and can vanish completely under scalar lcm projection.** The literature audit then identifies why the closest sparse-moduli large sieves do not automatically target what remains.

Primary references:

- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, *Additive energy and a large sieve inequality for sparse sequences*, Mathematika 68:2 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659.
- Karin Halupczok and Marc Munsch, *Large sieve estimate for multivariate polynomial moduli and applications*, Monatshefte für Mathematik 197 (2022), 463--478, arXiv:2110.13257.
- Yang reproduction source: `JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, especially `scripts/t2_swaps.py` for the exact common-`k` swap geometry.

## 7. Boundary conditions and decisive falsification tests

1. **High-slope slices remain eligible.** For fixed large `rq`, `L=rqk` is genuinely sparse in a common scalar interval. The finding only says that this must be treated as a labelled/cellwise family and that summing over slopes is part of the analytic burden.
2. **A scalar transform may still exist.** If Yang's full weighted covariance can be rewritten exactly as scalar-modulus character sums with factorization weights whose total cost is polylogarithmic, then (10) becomes an asset rather than an obstruction.
3. **Two-dimensional large sieves are outside the no-go.** A theorem on directionally separated frequency points, divisor incidences, or another source-faithful 2-D embedding could exploit the sparsity that scalar projection discards.
4. **Source cancellation may bypass support counting.** Exact cancellation in the full `S1-2S2+S3` combination or signed cancellation across coefficient cells is not constrained by this finding.
5. **The low-slope witness is a representation test, not a claim that it dominates the hard analytic mass.** If a future reduction proves all low-slope/equal-leg cells negligible or exactly soluble and leaves only a high-slope family, the positive-density examples (6)--(7) cease to describe that restricted residual. One must then rerun the scalar-support count on the actual surviving family.

A decisive falsifier of the program consequence would be an authoritative theorem whose hypotheses directly control Yang's weighted common-`k` covariance after scalar lcm projection **without** requiring sparse scalar `L` support and without reintroducing a power loss through slope/factorization multiplicity. Short of that, any “sparse-moduli large sieve” proposal must specify where the direction labels and source weights go; scalar lcm sparsity alone is not available.