# MC-497 — Quadratic short-overlap bias requires exceptional interval starts

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces incomplete repeated-residue cross-root interference to a weighted sum against one fixed conductor phase. Fix an odd prime conductor `p`, the quadratic character `chi (mod p)`, a nonzero shift `h (mod p)`, and one repeated source residue `a in F_p^*`. In the physical shortened-source coordinate `m`, put

\[
c:=h a^{-1}\pmod p.
\]

The exact relative phase from `MC-495` is

\[
R_c(0)=0,
\qquad
R_c(m)=\chi(m^2-c^2)\quad(m\ne0),
\tag{1}
\]

where the values at `m=plusminus c` vanish automatically. This is the same rational-character phase as `chi(1-t^{-2})` after the conductor scaling `t=am h^{-1}`, but the present formulation deliberately keeps the **physical additive `m` coordinate**, because source intervals are consecutive in `m` and conductor scaling does not preserve additive intervals.

`MC-496` shows that endpoint-only overlap intervals of length much larger than `p^{1/2}\log p` cannot create order-one bias by classical completion. In the quadratic-character case, the remaining short-overlap branch has a further exact restriction: **large interval bias is possible only at a sparse exceptional set of physical interval starts.**

The complete mean is

\[
\mu_c=\frac1p\sum_{m\bmod p}R_c(m)
=-\frac{1+\chi(-1)}p.
\tag{2}
\]

For `1<=H<=p` and `x in F_p`, put

\[
S_{c,x}(H)=\sum_{j=1}^{H}\bigl(R_c(x+j)-\mu_c\bigr),
\tag{3}
\]

where the interval is read cyclically modulo `p`. Then uniformly in `c ne 0`,

\[
\boxed{
\frac1p\sum_{x\bmod p}|S_{c,x}(H)|^2
\ll H+\frac{H^2}{\sqrt p}.
}
\tag{4}
\]

Consequently, for every `eta>0`, if

\[
E_{c,H}(\eta)=\{x\bmod p:|S_{c,x}(H)|\ge \eta H\},
\]

then

\[
\boxed{
\frac{|E_{c,H}(\eta)|}{p}
\ll \frac1{\eta^2}\left(\frac1H+\frac1{\sqrt p}\right).
}
\tag{5}
\]

Thus as soon as `H -> infinity`, an order-one normalized endpoint bias is confined to a vanishing fraction of physical conductor starts, even when `H` is far below the worst-case Pólya--Vinogradov scale `sqrt(p) log p` used in `MC-496`.

This does **not** give a uniform short-interval bound. It instead converts the unresolved endpoint-only escape into a source-distribution requirement. For any finite collection of physical source intervals `J_i` for the same repeated-residue block, with lengths `H_i`, starts `x_i (mod p)`, and nonnegative reconstruction weights `c_i`, write

\[
M=\sum_i c_iH_i,
\qquad
B=\sum_i c_i S_{c,x_i}(H_i).
\tag{6}
\]

If `|B|>=epsilon M`, then with `eta=epsilon/2`, at least an `epsilon/2` fraction of the weighted interval mass must lie on intervals satisfying

\[
|S_{c,x_i}(H_i)|\ge \frac\epsilon2 H_i.
\tag{7}
\]

Indeed, the complementary intervals contribute at most `(epsilon/2)M`, while every centered interval sum is bounded by a constant multiple of its length; adjusting the absolute constant in `eta` if necessary leaves the same fixed-fraction conclusion. Therefore a quadratic endpoint-only mechanism below the `MC-496` completion threshold must make the **actual first-exit overlap starts concentrate on the exceptional physical conductor sets `(5)`**. Merely producing many short overlaps is not enough.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Quadratic specialization in the physical source coordinate

Define

\[
Q_c(m)=\chi(m^2-c^2)
=\chi(m-c)\chi(m+c)
\tag{8}
\]

for all `m in F_p`. The classical quadratic character-sum identity gives

\[
\sum_{m\bmod p}Q_c(m)=-1.
\tag{9}
\]

The exact source phase `R_c` differs from `Q_c` only at `m=0`, where

\[
Q_c(0)=\chi(-c^2)=\chi(-1),
\qquad
R_c(0)=0.
\tag{10}
\]

Thus `R_c-mu_c` differs from `Q_c+1/p` by the centered one-point mass

\[
-\chi(-1)\left(\mathbf 1_{m=0}-\frac1p\right).
\tag{11}
\]

For an interval of length `H<=p`, the sum of `(11)` has total start-mean-square `O(H)`. It therefore does not change the scale in `(4)`.

The representation `(8)` exposes the relevant Legendre autocorrelation without changing the source coordinate. This point is essential: the normalization `t=am h^{-1}` is a bijection of `F_p` and is harmless for complete sums, but a consecutive interval in `m` becomes an arithmetic progression of step `a h^{-1}` in `t`, not a consecutive interval. The second-moment argument below is therefore carried out directly for `Q_c(m)`.

## 2. Complete shifted correlations give the second moment

For `d in F_p`, define

\[
C_c(d)=\sum_{m\bmod p}Q_c(m)Q_c(m+d).
\tag{12}
\]

At `d=0`,

\[
C_c(0)=p-2.
\tag{13}
\]

For `d ne 0, plusminus 2c`, the product

\[
(m^2-c^2)((m+d)^2-c^2)
\tag{14}
\]

has four distinct roots and is not a square, so the classical Weil bound gives

\[
C_c(d)=O(\sqrt p).
\tag{15}
\]

For `d=plusminus2c`, one root is doubled; removing the square factor leaves a nondegenerate quadratic character sum, so in fact `C_c(d)=O(1)`. Hence `(15)` holds uniformly for every nonzero `d` and every `c ne0`.

Centering `Q_c` changes each complete correlation only by `O(1/p)`. Expanding the square in a physical interval of length `H` therefore gives

\[
\sum_{x\bmod p}
\left|\sum_{j=1}^{H}(Q_c(x+j)+1/p)\right|^2
\ll pH+\sqrt p\,H^2.
\tag{16}
\]

The centered point defect `(11)` has start-mean-square `O(H)`. Using `|A+B|^2<=2|A|^2+2|B|^2` proves `(4)`, and Chebyshev immediately gives `(5)`.

The bound is intentionally average-over-start rather than uniform. It says that below the completion threshold the obstruction cannot be generic endpoint geometry: it must be arithmetic concentration of the **actual physical source starts** on a sparse exceptional set.

## 3. Weighted endpoint consequence

Take the exact endpoint-only expansion from `MC-496` after grouping one repeated-residue opposite-root contribution into its physical `m`-interval intersections. The weights multiplying those interval sums are nonnegative. Centering contributes only `mu_c M=O(M/p)`, so an order-one negative cross-root term requires an order-one centered aggregate `B` as in `(6)`.

Split the intervals into good and bad according to `(7)`. Up to the harmless fixed centering constant described above, the good contribution is at most a fixed fraction of `M`. Therefore a fixed order-one total bias forces a fixed fraction of the weighted interval mass onto bad intervals. Equation `(5)` says that, at any fixed length `H`, the available bad physical starts occupy only

\[
O_\epsilon\left(p/H+\sqrt p\right)
\tag{17}
\]

residue classes.

This is the new proof obligation. A surviving source mechanism must show that the exact first-exit endpoint map sends a substantial fraction of its reconstruction mass into those rare classes, or else use the lower-prime pair-sieve/internal arithmetic or a genuinely `q`-dependent pre-aggregation sign/phase that lies outside the endpoint-only model.

## 4. Why ordinary Burgess is not a free replacement

There is a tempting but invalid shortcut: transform `(8)` into an ordinary character and then apply the classical Burgess bound for `sum chi(n)`. For `m ne -c`, set

\[
u=\frac{m-c}{m+c}.
\tag{18}
\]

Then, away from the exceptional points,

\[
\chi(m^2-c^2)=\chi(u),
\tag{19}
\]

because the remaining factor `4c^2/(1-u)^2` is a square. But an additive interval in the physical variable `m` becomes a fractional-linear image in `u`, not an additive interval. The ordinary one-dimensional Burgess theorem therefore does not transfer by this coordinate change.

The literature boundary is consistent with that distinction. Mauduit and Sárközy's classical Legendre-sequence work (*Acta Arithmetica* 82 (1997), 365--377, DOI `10.4064/aa-82-4-365-377`) and subsequent pseudorandom-sequence literature give the familiar `O(sqrt(p) log p)` worst-case aperiodic-correlation scale. Rena Chu's recent *Short character sums of inhomogeneous polynomials* (arXiv:`2609.04092`, submitted 3 September 2026) explicitly notes that nontrivial short bounds for one-variable inhomogeneous polynomial character sums remain open in general, giving `X^2+1` as an example. That statement does **not** prove that the special reducible polynomial `X^2-c^2` is itself an open case, and the present finding makes no such claim. A targeted audit did not identify a theorem that supplies a Burgess-scale worst-case bound for this exact shifted Legendre autocorrelation.

So `(4)`--`(5)` should not be read as a substitute for a missing uniform theorem. Their value is different: they prove that the only short physical endpoint intervals capable of mattering are exceptional starts, and they quantify how sparse those starts are.

## Prior art and novelty boundary

- Complete quadratic and quartic character-sum bounds used in `(12)`--`(16)` are classical Weil theory; no novelty is claimed.
- Mean-square expansion over interval starts and Chebyshev are classical harmonic/probabilistic bookkeeping.
- Aperiodic Legendre autocorrelation and higher correlation measures are established pseudorandom-sequence topics; the classical `sqrt(p) log p` worst-case completion scale predates this line.
- Chu's 2026 result is cited only as a boundary on importing a generic inhomogeneous-polynomial Burgess theorem. It is not evidence that this special reducible polynomial has no stronger theorem.
- The durable Mathia delta is the specialization of those classical ingredients to the exact `MC-495` cross-root phase **in the physical source coordinate** and the resulting source-frame admission condition: below the `MC-496` completion threshold, endpoint-only cancellation requires weighted concentration of actual first-exit interval starts on the exceptional sets `(5)`.

## Boundaries and falsification tests

- **Quadratic character only.** The factorization `(8)` and especially clean autocorrelation calculation use `chi^2=1`. Higher-order characters need their own shifted-rational correlation audit.
- **Physical additive coordinate.** The theorem controls consecutive intervals in the shortened source variable `m`. Conductor scaling is used only for complete identities; it must not be used to turn a physical interval into a unit-step interval in another coordinate.
- **Average over starts, not a maximum.** A single adversarial start may still have a large short sum. This finding cannot close the short-overlap branch without source information on where its starts land.
- **Endpoint-only model.** Internal pair-sieve variation inside the overlap interval, or a source-derived `q`-dependent sign/phase before aggregation, is intentionally outside the theorem.
- **Cyclic conductor intervals.** Integer `m`-intervals of length at most `p` descend directly to the cyclic model modulo `p`; endpoint defects at the singular classes change only `O(1)` terms.
- **No independence assumption.** Equation `(5)` is deterministic. Conversely, treating first-exit starts as random without proving a source-distribution statement would add an unsupported hypothesis.
- **Worst-case Burgess remains unimported.** Any future use of a sub-square-root uniform estimate must cite a theorem whose hypotheses cover the exact shifted-product/rational phase, not merely ordinary `sum chi(n)`.

## Consequence for the research line

The endpoint-only loophole from `MC-496` is now split cleanly in the exact source coordinate. Long overlaps are uniformly harmless by completion; short overlaps can be dangerous only if the actual source endpoint map concentrates reconstruction mass on a sparse exceptional set of physical conductor starts. The next meaningful endpoint calculation is therefore **not another generic character-sum estimate**: it is the distribution, with the true first-exit weights retained, of the physical start residues of the overlap intervals relative to the exceptional sets in `(5)`.

If that source map is sufficiently dispersed, the endpoint-only branch closes even below the Pólya--Vinogradov threshold. If it is not, the concentration pattern itself becomes a concrete arithmetic object to explain. In parallel, the lower-prime pair-sieve profile and genuinely `q`-dependent pre-aggregation asymmetry remain independent live channels.