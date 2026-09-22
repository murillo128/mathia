# MC-464 — Normalized-gcd gate makes favorable shifts totient-sparse

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-463` reduces the bare fixed-anchor source-frame admission test for a fixed outer pair to one normalized quotient

\[
T(h_0):=\frac{r_2}{(h_0,r_2)}.
\tag{1}
\]

For prime source conductor `p`, residual support `s_0\le S`, and a common translated-character interval of length `0<L<p`, that test can help only when

\[
1+\frac{S}{T(h_0)}>\frac pL.
\tag{2}
\]

Define

\[
Y:=\frac{SL}{p-L},
\qquad
M:=\lceil Y\rceil-1,
\tag{3}
\]

so `M` is the largest integer strictly smaller than `Y`. Then `(2)` is exactly

\[
T(h_0)\le M.
\tag{4}
\]

The shifts passing this necessary gate are arithmetically sparse in a completely explicit way. Over one complete residue period modulo `r_2`,

\[
\boxed{
N_{r_2}(M)
:=\#\{h_0\bmod r_2:T(h_0)\le M\}
=
\sum_{\substack{T\mid r_2\\T\le M}}\varphi(T).
}
\tag{5}
\]

Indeed, fixing `T|r_2` is equivalent to

\[
(h_0,r_2)=\frac{r_2}{T},
\tag{6}
\]

and the residues in this gcd class are exactly

\[
h_0\equiv \frac{r_2}{T}a\pmod{r_2},
\qquad (a,T)=1,
\tag{7}
\]

of which there are `phi(T)`.

Consequently

\[
\boxed{
\frac{N_{r_2}(M)}{r_2}
\le
\frac{M(M+1)}{2r_2}.
}
\tag{8}
\]

Thus if

\[
M=o(\sqrt{r_2}),
\tag{9}
\]

the shifts for which the `MC-463` support gate can even *possibly* admit fixed-anchor gain occupy density `o(1)` modulo `r_2`. Conversely, for such shifts to occupy a fixed positive proportion of a full `r_2`-period, a necessary scale is

\[
M\gtrsim \sqrt{r_2}.
\tag{10}
\]

In the non-endpoint regime `L\le (1-\eta)p`, where `Y\asymp_\eta SL/p`, this becomes the branch-specific averaged range requirement

\[
\boxed{
SL\gtrsim_\eta p\sqrt{r_2}
}
\tag{11}
\]

for a positive-density supply of shifts that merely pass the bare support gate.

There is a complementary short-shift obstruction. For `1\le h_0\le H`, every shift with `T(h_0)\le M` has the unique form

\[
h_0=\frac{r_2}{T}a,
\qquad
T\mid r_2,
\qquad
T\le M,
\qquad
(a,T)=1.
\tag{12}
\]

Hence

\[
\boxed{
\#\{1\le h_0\le H:T(h_0)\le M\}
=
\sum_{\substack{T\mid r_2\\T\le M}}
\#\left\{1\le a\le \frac{HT}{r_2}:(a,T)=1\right\}.
}
\tag{13}
\]

In particular, there are **no** such nonzero shifts when

\[
\boxed{H<\frac{r_2}{M},}
\tag{14}
\]

and generally

\[
\boxed{
\#\{1\le h_0\le H:T(h_0)\le M\}
\le
\frac{H}{r_2}\frac{M(M+1)}2+M.
}
\tag{15}
\]

When `H\ge r_2/M`, the endpoint term `M` is itself `O(HM^2/r_2)`, so the admissible-shift proportion is again `O(M^2/r_2)`.

Equations `(5)`--`(15)` sharpen the live clue after `MC-463`. A large outer gcd `G=(h_0,r_2)` is not merely a condition to be averaged over later: the exact gcd-class decomposition shows that strong compression `T=r_2/G\le M` is rare unless the residual/interval budget is already large enough to make `M` at least square-root scale in `r_2`. A short `q`-van der Corput shift range has an additional entrance cost `H\ge r_2/M` before it can meet even one nonzero favorable normalized-gcd class.

This is only a **necessary-support classification**. A shift counted in `(5)` or `(13)` still need not have enough effective aggregated coefficient participation, and the surviving aligned amplitude from `MC-460` remains uncontrolled. Sparse favorable shifts could also be deliberately selected by a non-uniform method, in which case the diagonal/positivity cost of that selection must be priced separately. No conductor-power saving, no improved bound for `M(x)`, and no RH consequence follows.

## 1. Exact gcd-class count

For any residue `h_0 (mod r_2)`, put

\[
G=(h_0,r_2),
\qquad
T=r_2/G.
\tag{16}
\]

Then `T|r_2`. Conversely, fix `T|r_2` and put `G=r_2/T`. The condition `(h_0,r_2)=G` holds exactly when

\[
h_0=Ga
\]

with `a` a unit modulo `T`. Reduction modulo `r_2=GT` therefore identifies the gcd class with `(\mathbf Z/T\mathbf Z)^\times`, proving that its cardinality is `phi(T)`. Summing over `T\le M` gives `(5)`.

The complete family of gcd classes satisfies the classical identity

\[
\sum_{T\mid r_2}\varphi(T)=r_2,
\tag{17}
\]

which is simply the partition of all residues by their gcd with `r_2`. The truncated family in `(5)` is therefore a literal initial segment of that partition in the normalized quotient `T`.

For the crude but uniform bound `(8)`, use only

\[
\varphi(T)\le T
\]

and discard the restriction `T|r_2`:

\[
N_{r_2}(M)
\le
\sum_{T\le M}T
=
\frac{M(M+1)}2.
\tag{18}
\]

No divisor-function loss is needed.

If the zero residue is excluded from a shift average, the `T=1` class contributes at most one residue and may simply be removed from `(5)`; none of the scale conclusions changes.

## 2. The exact support gate determines the threshold `M`

The `MC-463` coefficient-independent gate is `(2)`. Since `L<p`,

\[
1+\frac ST>\frac pL
\quad\Longleftrightarrow\quad
\frac ST>\frac{p-L}{L}
\quad\Longleftrightarrow\quad
T<\frac{SL}{p-L}=Y.
\tag{19}
\]

Because `T` is a positive integer, this is equivalent to `T\le M` with `M=\lceil Y\rceil-1`, proving `(4)` with no asymptotic approximation.

When `L\le(1-\eta)p`,

\[
\frac{SL}{p}
\le Y
\le
\frac1\eta\frac{SL}{p},
\tag{20}
\]

so the threshold is comparable, up to an `eta`-dependent constant, to the heuristic quantity `SL/p` already used after `MC-462`--`MC-463`. Equation `(11)` is therefore the exact shift-density consequence of the earlier per-shift support gate away from the near-complete endpoint.

Near `L=p`, `(3)` correctly records that the bare fixed-anchor second moment has little room to improve the pointwise estimate; that endpoint was already separated in `MC-449` and should not be reinterpreted through the rough approximation `Y\sim SL/p`.

## 3. Short shift ranges have an additional entrance gate

For a positive integer shift `h_0`, fixing `T=T(h_0)` gives `(12)`. The correspondence is unique because `T=r_2/(h_0,r_2)` is determined by `h_0`.

Therefore the number of favorable shifts in `[1,H]` is exactly `(13)`. Dropping coprimality gives

\[
\#\left\{1\le a\le \frac{HT}{r_2}:(a,T)=1\right\}
\le
\frac{HT}{r_2}+1,
\tag{21}
\]

and hence

\[
\#\{1\le h_0\le H:T(h_0)\le M\}
\le
\frac H{r_2}
\sum_{\substack{T\mid r_2\\T\le M}}T
+
\#\{T\mid r_2:T\le M\}.
\tag{22}
\]

Bounding the two terms by `M(M+1)/2` and `M` gives `(15)`.

Moreover every positive shift in the `T` class is at least `r_2/T`. If `T\le M`, then

\[
h_0\ge\frac{r_2}{T}\ge\frac{r_2}{M},
\tag{23}
\]

which proves `(14)`.

Thus a method averaging only normalized shifts `h_0\le H` cannot even access the favourable-gcd branch unless

\[
HM\ge r_2.
\tag{24}
\]

Substituting the non-endpoint size `M\asymp SL/p` gives the additional necessary scale

\[
\boxed{HSL\gtrsim p r_2}
\tag{25}
\]

up to the same endpoint/comparability qualifications.

## 4. What this does and does not say about averaged differencing

The exact count does not assume any probability model for the shifts. It simply classifies the residue classes on which the already-proved `MC-463` support gate is open.

For an unweighted full-period average over `h_0 (mod r_2)`, `(8)` is the relevant occupancy statement. If `M=o(\sqrt{r_2})`, almost every shift fails the gate before the aggregated coefficient or surviving residual amplitude is inspected.

For a finite interval of positive shifts, `(13)`--`(15)` give the corresponding deterministic count. When `H\ge r_2/M`, the proportion of admissible shifts remains `O(M^2/r_2)`; below that entrance scale there are none.

A deliberately weighted differencing inequality could concentrate on the rare favorable gcd classes. This finding does not rule that out. It changes the burden of proof: such a method cannot cite generic shift averaging as the source of the gain. It must show that the selected sparse shift set supports a positive/difference kernel whose diagonal and Fourier mass do not erase the hoped-for conductor saving. The positive-kernel barriers in `MC-416`--`MC-421` are relevant constraints, but no automatic transfer to this sparse divisor-class selection is asserted here.

Likewise, a rare favorable shift could have a disproportionately large outer coefficient. Equation `(5)` counts geometry, not coefficient mass. The clue remains open until the actual outer weights and the aligned second residual amplitude are propagated through the estimate.

## 5. Prior art and novelty boundary

The gcd-class parametrization `(6)`--`(7)`, the fact that a gcd class has `phi(T)` residues, and the divisor identity `(17)` are elementary classical number theory. NIST DLMF §27.2 defines Euler's totient as the cardinality of a reduced residue system and points to Apostol, *Introduction to Analytic Number Theory* (1976), for the standard multiplicative-number-theory background; DLMF §27.3 records the standard multiplicative formula for `phi`. No novelty is claimed for these facts.

The `q`-van der Corput/source-frame context and the support condition being counted are specific to the already-persisted `MC-455` and `MC-461`--`MC-463` chain. A targeted literature check on 22 September 2026 found no need for a new analytic theorem: once `MC-463` has reduced the source gate to `T=r_2/(h_0,r_2)`, the present shift-density statement is an elementary consequence of the classical gcd partition. The Mathia contribution claimed here is therefore only the **branch-specific consequence** `(5)`--`(15)` and the resulting necessary scale tests `(11)` and `(25)`, not the underlying totient identities or gcd counting.

## Boundaries and falsification tests

- **Passing is not saving.** Equations `(5)` and `(13)` count shifts that pass a necessary support-size gate. They do not prove sufficient coefficient participation or any estimate for the full staged kernel.
- **Uniform averaging is not mandatory.** Sparse favorable shifts could be selected deliberately. Any such escape must price the selected-shift positive kernel, diagonal, and Fourier mass rather than treating selection as free.
- **Coefficient mass can be nonuniform.** Totient sparsity is a count, not a bound on the actual outer `(r,r',h)` weights. A small set could in principle carry substantial mass.
- **The endpoint `L\approx p` is separate.** The exact threshold `(3)` should be used there; the approximation `Y\asymp SL/p` is only valid away from `L=p`.
- **Normalized versus original shifts must not be conflated.** The count is for `h_0=h/g` at fixed outer pair after the `MC-459` normalization. Any upstream average in the original shift `h` must account for the multiplicity introduced by `g=(r,r')`.
- **No source-amplitude estimate is supplied.** The aligned factor `B_\beta(C_{s_0}+r_1s_0j)` remains the central analytic unknown.
- **No circular zeta input is used.** Everything here is finite gcd/totient arithmetic plus the previously derived support gate.

## Consequence for the research line

The outer-gcd question left by `MC-463` now has a first exact answer. Strong normalized-gcd compression is not typical unless the residual-support/interval budget is itself large: over a full `r_2` shift period, the fraction of shifts that can pass the bare fixed-anchor support gate is at most `O(M^2/r_2)`, with `M` given exactly by `(3)`. A positive-density supply therefore requires square-root-scale `M`, and a short shift range must first satisfy `HM\ge r_2` to touch any favorable nonzero class.

The next calculation should no longer average the gcd gate heuristically. It should propagate the **actual outer shift weights** into the divisor-class decomposition `(5)` or `(13)`. If the relevant differencing weights are sufficiently flat across normalized shifts, `(8)`/`(15)` can turn this support sparsity into a quantitative outer-mass obstruction. If the weights are deliberately concentrated on favorable classes, that concentration becomes the object to price against the positive-kernel/diagonal cost. Only after that outer gate survives is it useful to attack the aligned residual amplitude.