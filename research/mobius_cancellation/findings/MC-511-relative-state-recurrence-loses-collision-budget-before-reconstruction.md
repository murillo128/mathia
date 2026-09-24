# MC-511 — Relative-state recurrence can lose its collision budget before pair reconstruction

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · ELEMENTARY-COLLISION+FIBRE-BOUND · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-510` shows that the exact gauge-invariant lower-prime state

\[
\Lambda_z(q,r)=\bigl(qr^{-1}\bmod \ell\bigr)_{\ell\in\mathcal S_z}
\]

has localized fibres whose cardinality shrinks with the rational-reconstruction modulus, and eventually becomes pair-injective. The collision target from `MC-506`, however, is not a count of equal relative states: it is a second moment after the physical conductor pushforward. Keeping the source-pair provenance until that pushforward gives a sharper obstruction.

Let `\mathcal P` be any finite family of ordered source pairs from the localized repeated-residue setting of `MC-510`. For each pair `u=(q,r)\in\mathcal P`, let

\[
b_u(t)\ge0,\qquad t\in\mathbf F_p,
\tag{1}
\]

be its exact nonnegative contribution to the physical conductor argument after all retained first-exit, hard-mask, endpoint, and reconstruction restrictions. Thus

\[
c_t=\sum_{u\in\mathcal P}b_u(t),
\qquad
W=\sum_t c_t>0,
\tag{2}
\]

and the total physical collision mass of `MC-506` is

\[
C:=\sum_t c_t^2.
\tag{3}
\]

Write `\sigma(u)=\Lambda_z(u)` for the exact relative state and define the collision mass coming from pairs in the **same** exact state by

\[
C_{\rm same}
:=
\sum_{t\in\mathbf F_p}
\sum_{\sigma}
\left(
\sum_{u:\sigma(u)=\sigma}b_u(t)
\right)^2.
\tag{4}
\]

The remaining collision mass

\[
C_{\rm cross}:=C-C_{\rm same}
\tag{5}
\]

is nonnegative and consists exactly of physical collisions between **different** relative states.

Suppose every exact relative-state fibre contains at most `L` source pairs. Then

\[
\boxed{
C_{\rm same}
\le
L\sum_{u,t}b_u(t)^2.
}
\tag{6}
\]

Define the effective pair-phase participation

\[
R_*:=
\frac{W^2}{\sum_{u,t}b_u(t)^2}.
\tag{7}
\]

Then

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{pL}{R_*}.
}
\tag{8}
\]

Combining this with the `MC-506` collision excess

\[
\Delta
:=
\frac{pC}{W^2}-1
\tag{9}
\]

gives the exact cross-state lower bound

\[
\boxed{
\frac{pC_{\rm cross}}{W^2}
\ge
1+\Delta-\frac{pL}{R_*}.
}
\tag{10}
\]

In particular, if

\[
R_*\ge pL,
\tag{11}
\]

then

\[
\boxed{
C_{\rm cross}
\ge
\Delta\,\frac{W^2}{p}.
}
\tag{12}
\]

So once the effective source/profile population dominates the exact-state fibre budget by the conductor factor `p`, every collision **in excess of the uniform baseline** must already be supportable by collisions between distinct exact relative states. Repeated exact-state recurrence is then incapable, by itself, of explaining the `MC-506` excess.

For a centered conductor kernel `F`, `MC-506` gives

\[
\frac{|\mathcal C_F|}{W}
\le \sigma_F\sqrt\Delta.
\]

Hence any normalized bias `|\mathcal C_F|/W\ge\eta` forces

\[
\Delta\ge\frac{\eta^2}{\sigma_F^2},
\]

and therefore

\[
\boxed{
\frac{pC_{\rm cross}}{W^2}
\ge
1+rac{\eta^2}{\sigma_F^2}-\frac{pL}{R_*}.
}
\tag{13}
\]

The new point is that the recurrence mechanism can become collision-irrelevant **strictly before** `MC-510` reaches pair injectivity.

## 1. Exact collision decomposition

For each state `\sigma`, define

\[
c_{\sigma,t}:=
\sum_{u:\sigma(u)=\sigma}b_u(t).
\tag{14}
\]

Then `c_t=\sum_\sigma c_{\sigma,t}`, so

\[
C
=
\sum_t\left(\sum_\sigma c_{\sigma,t}\right)^2
=
\sum_{t,\sigma}c_{\sigma,t}^2
+
\sum_t\sum_{\sigma\ne\tau}c_{\sigma,t}c_{\tau,t}.
\tag{15}
\]

All terms are nonnegative, which proves that `(4)` is exactly the same-state contribution and `(5)` is the cross-state contribution.

For one state fibre of size `n_\sigma\le L`, pointwise Cauchy gives

\[
\left(\sum_{u:\sigma(u)=\sigma}b_u(t)\right)^2
\le
n_\sigma
\sum_{u:\sigma(u)=\sigma}b_u(t)^2
\le
L
\sum_{u:\sigma(u)=\sigma}b_u(t)^2.
\tag{16}
\]

Summing `(16)` over `t` and `\sigma` proves `(6)`. Equations `(8)` and `(10)` are then only normalization and the identity `pC/W^2=1+\Delta`.

No independence, random model, equidistribution hypothesis, or approximation of the physical coefficient measure is used.

## 2. Substituting the localized rational-reconstruction fibre tariff

In the notation of `MC-510`, put

\[
N_z=pM_z,
\qquad
B=H(2Q+H).
\tag{17}
\]

That finding proves that every exact relative-state fibre satisfies

\[
L
\le
L_z
:=
1+2\left\lfloor\frac{B}{N_z}\right\rfloor
\left(
1+\left\lfloor\frac{H}{p\min I}\right\rfloor
\right).
\tag{18}
\]

Therefore the same-state share of the physical collision second moment obeys the fully source-compatible bound

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{pL_z}{R_*}.
}
\tag{19}
\]

When `H<p\min I`, the spacing factor in `(18)` is one and

\[
L_z
\le
1+rac{2B}{pM_z}.
\tag{20}
\]

Consequently

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{p}{R_*}
+
\frac{2B}{M_zR_*}.
}
\tag{21}
\]

This exposes a threshold different from exact rational reconstruction. Pair injectivity requires roughly

\[
M_z\gtrsim \frac{B}{p},
\tag{22}
\]

whereas same-state collision mass becomes negligible relative to the natural `W^2/p` collision scale already when

\[
R_*\gg p
\qquad\text{and}\qquad
M_zR_*\gg B.
\tag{23}
\]

Equivalently, in a high-participation block the recurrence resource is exhausted around

\[
M_z\asymp \frac{B}{R_*},
\tag{24}
\]

which is parametrically earlier than `(22)` whenever `R_*\gg p`.

For the dyadic specialization `I=[Q,2Q]`, one has `H=Q`, `B=3Q^2`, and `\lfloor H/(p\min I)\rfloor=0`. Thus

\[
\boxed{
\frac{pC_{\rm same}}{W^2}
\le
\frac{p}{R_*}
+
\frac{6Q^2}{M_zR_*}.
}
\tag{25}
\]

If `R_*/p\to\infty` and `M_zR_*/Q^2\to\infty`, then

\[
C_{\rm same}=o(W^2/p),
\tag{26}
\]

even though `M_z` may still be far below the pair-injectivity threshold `3Q^2/p`.

## 3. Representation consequence

`MC-509` and `MC-510` show that longer exact mask states eventually encode source identity. The present estimate shows that one need not wait for that endpoint to lose exact-state recurrence as a plausible **collision carrier**.

The relevant comparison is not merely whether a state repeats. It is whether the repeated-state fibres are large enough, relative to the effective pair-phase participation `R_*`, to contribute at the conductor collision scale `W^2/p`. Equation `(21)` prices that comparison directly.

This matters because the `MC-506` observable is downstream of the relative-state quotient. Distinct exact states can still land on the same physical conductor argument. When `(23)` holds, that many-to-one **cross-state pushforward** is no longer an optional complication: it is where any material collision excess must live.

Thus conditioning on exact relative state has two separate failure regimes:

- at very large `M_z`, `MC-510` says the state reconstructs the ordered pair and offers no repeated-class averaging;
- already at smaller `M_z`, `(21)` can make same-state physical collisions too small to carry even the natural conductor collision scale, provided the exact source/profile measure has sufficiently large `R_*`.

The surviving theorem surface is therefore sharper than “use a coarser state.” A useful coarsening must preserve enough information to constrain the **cross-state map into `t=x+j`** while keeping fibres large enough that its collision budget is not exhausted by `(8)`. Merely stopping the exact relative tuple just before injectivity is not a quantitative criterion.

## 4. Prior art and novelty boundary

The abstract ingredients are elementary. Splitting a second moment by a partition, expanding same-class and cross-class collision terms, and applying Cauchy--Schwarz on fibres are standard. The inverse-square quantity in `(7)` is the same effective-participation/Simpson-collision currency that appears broadly in probability, statistics, and importance-sampling effective-sample-size bookkeeping. A targeted literature check found no basis for a general novelty claim for `(6)`--`(10)`.

The Mathia-specific delta is the combination with the exact localized rational-reconstruction fibre tariff of `MC-510`. That substitution produces the earlier threshold `(23)`--`(25)`: for the actual gauge-invariant first-exit state, recurrent exact-state collisions can become negligible before the state is source-pair injective. No general theorem is claimed beyond this source-specific frontier reduction.

No new entry in `SOURCES.md` is needed for the proof: the collision decomposition and Cauchy estimate are derived here, while the only arithmetic input is the already-audited `MC-510` fibre theorem.

## Boundaries and falsification tests

- **Pair-resolved provenance is required.** The functions `b_u(t)` are the exact nonnegative contributions of each ordered source pair before summing over source labels. If the physical construction has already irreversibly discarded that provenance, `(4)` cannot be reconstructed from the aggregate `c_t` alone.
- **Nonnegative branch only.** The decomposition and upper bound use `b_u(t)\ge0`. A genuinely signed or complex pre-aggregation coefficient is a distinct escape and remains live.
- **`R_*` must be proved from the physical source.** A large raw number of source pairs does not imply large effective participation. Concentrated reconstruction weights or narrow profile support can make `R_*` small.
- **Small same-state collision does not imply small total collision.** Equation `(10)` says exactly the opposite danger: the physical pushforward may merge many distinct states onto the same conductor argument.
- **The fibre bound is an upper bound.** Replacing the true state multiplicity by `L_z` is conservative; sharper source arithmetic can only reduce the same-state collision budget further.
- **No cancellation theorem.** Even if `(26)` holds, `C_{\rm cross}` may be large and may align with the centered conductor phase. The result neither bounds `\Delta` nor the bias itself.
- **Conductor-local.** Outer conductor sums, dyadic/shell decompositions, endpoint tariffs, and global reconstruction still have to be charged.
- **No Möbius or zero conclusion.** There is no new estimate for `M(x)`, no zero-free region, and no RH consequence.

## Consequence

The next audit of the localized hard-mask branch should measure the physical effective participation `R_*` **before** spending effort on deeper exact relative-state conditioning. If `R_*\gg p` and `M_zR_*\gg B`, equations `(21)`--`(26)` already rule out repeated exact-state collisions as the carrier of any material `MC-506` excess. At that point the only nonnegative route left inside this representation is a structured many-to-one pushforward in which distinct gauge-invariant relative states collide after the physical conductor map. That cross-state coupling, rather than exact-state recurrence or eventual source reconstruction, is the load-bearing object to estimate.