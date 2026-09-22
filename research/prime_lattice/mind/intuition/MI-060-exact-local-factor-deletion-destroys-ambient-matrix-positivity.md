# MI-060 — Exact local-factor deletion destroys ambient matrix positivity

**Evidence level:** exact finite-dimensional operator synthesis from [PL-420](../../findings/PL-420-local-factor-schur-inverse-positivity-obstruction.md), refining the source-fidelity obstruction of MI-059.

Retaining the full residue correlation matrix fixes the information loss identified in PL-419, but it does not make the exact local Hardy--Littlewood repair positivity-preserving. On the reduced residue group `U_p`, let `B_p` be the ordinary local-factor matrix and let `G_p` be its entrywise reciprocal. The insertion map

`Phi_(B_p)(R)=B_p circ R`

is completely positive because `B_p>0`. Exact local-factor deletion is its linear Schur inverse

`Phi_(G_p)(R)=G_p circ R`, with `Phi_(G_p) Phi_(B_p)=Id`.

The inverse symbol is indefinite. Its spectrum is

`lambda_1(G_p)=p-1`,

`lambda_perp(G_p)=-(p-1)/(p(p-2))`

with multiplicity `p-2`. Hence `G_p` has inertia `(1,p-2,0)` for every odd prime, and the inverse Schur map is not even positive: applying it to the rank-one PSD matrix `11*` returns `G_p`, which is indefinite. For `p=5` the spectrum is `{4,-4/15,-4/15,-4/15}`, exactly the signed character metric already isolated by PL-415--PL-419.

The important distinction is between **retaining the source coherence** and **preserving ordinary matrix order through the source repair**. PL-419 shows that off-diagonal residue coherences are necessary to determine the signed target. PL-420 shows that even after they are retained, exact division by the local factor cannot be transported through the full PSD cone for free. The negative character modes are not a bad basis choice; they are the Fourier signature of the nonpositive inverse de-aliasing map.

A positive operator route therefore needs an additional theorem about the arithmetic image, not merely a larger covariance matrix. One possibility is a source-specific subcone on which `G_p circ R>=0`; another is a non-Schur enlargement in which exact deletion is represented by a different positive operation. Otherwise the route must accept an indefinite intermediate object and supply a separate divisor-sensitive localization theorem.

**Boundary.** This is an ambient-cone obstruction. Actual prime residue-correlation matrices may satisfy extra arithmetic constraints, and PL-420 does not rule out positivity on such a restricted image. Entrywise positivity also survives because every entry of `G_p` is positive; the failure concerns positive-semidefinite matrix order. The result is finite-dimensional local-factor algebra, not an RH theorem or a signed-supertrace estimate.