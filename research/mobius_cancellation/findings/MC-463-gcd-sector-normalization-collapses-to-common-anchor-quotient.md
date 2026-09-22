# MC-463 — Residual gcd sectors collapse to one common anchor quotient

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `NEGATIVE/OBSTRUCTION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The gcd-sector parameter `d=(s,r_2)` used in `MC-460`--`MC-462` is not an independent source-frame variable. For a fixed outer pair, every compatible residual gcd sector normalizes to the **same reduced modulus**, and the entire one-sided staged family can be aggregated exactly before any positive closure.

Keep the notation

\[
r=g r_1,\qquad r'=g r_2,\qquad h=g h_0,\qquad (r_1,r_2)=1,
\]

and let a residual divisor `s` from the first expanded block contribute. Put

\[
d=(s,r_2),\qquad s=d s_0,
\]

so compatibility forces `d|h_0`. Define once for the fixed outer pair

\[
G=(h_0,r_2),\qquad T=\frac{r_2}{G},\qquad H_0=\frac{h_0}{G},\qquad (H_0,T)=1.
\tag{1}
\]

Then `d|G`, and the sector variables of `MC-461` satisfy the exact identities

\[
\boxed{
(h_1,t)=\frac Gd,
\qquad
t_0=\frac{t}{(h_1,t)}=\frac{r_2}{G}=T.
}
\tag{2}
\]

Thus the anchor modulus `t_0` is **independent of `d`**.

More strongly, if `m` is the integer introduced by

\[
n+h=g r_1 s m
\]

and the second outer divisibility condition is imposed, then every compatible sector has

\[
m=\frac Gd\,(\ell_{s_0}+Tj),
\tag{3}
\]

where `\ell_{s_0}` is the unique residue modulo `T` satisfying

\[
\boxed{
r_1s_0\ell_{s_0}\equiv H_0\pmod T.}
\tag{4}
\]

Consequently

\[
\boxed{
n+h=g r_1G s_0(\ell_{s_0}+Tj),}
\tag{5}
\]

and

\[
\boxed{
\frac n{r'}
=C_{s_0}+r_1s_0j,
\qquad
C_{s_0}=\frac{r_1s_0\ell_{s_0}-H_0}{T}.}
\tag{6}
\]

Equations `(5)`--`(6)` contain **no `d`**. The admissible interval in `j`, the translated-character phase, and the still-unexpanded second residual amplitude therefore depend only on the reduced divisor `s_0`, not on which compatible gcd sector produced it.

For a prime source conductor `p`, on the nonzero character support,

\[
\boxed{
U_{s_0}\equiv \ell_{s_0}T^{-1}\pmod p,
\qquad
D_{s_0}\equiv H_0(r_1Ts_0)^{-1}\pmod p.
}
\tag{7}
\]

Hence all first-block divisors with the same reduced `s_0` have exactly the same source pair `(U,D)`, the same interval, and the same surviving amplitude trajectory. They should be aggregated **before** Cauchy, completion, or any sectorwise absolute bound.

If the original residual block is supported on `s\le S`, define the exact aggregated coefficient

\[
\boxed{
\widetilde\beta(s_0)
:=
\sum_{\substack{d\mid G\\(s_0,r_2/d)=1\\d s_0\le S}}
\beta_{d s_0}.
}
\tag{8}
\]

Then the one-sided staged sum over all compatible residual divisors is exactly the same family as in `MC-460`, but indexed once by `s_0` with coefficient `\widetilde\beta(s_0)`. No sum over gcd sectors remains in the source geometry.

This collapse also sharpens the range gate of `MC-462`. If

\[
T=\frac{r_2}{(h_0,r_2)}<p,
\tag{9}
\]

then canonical representatives `0\le\ell<T` remain distinct modulo `p`, so

\[
U_{s_0}=U_{s'_0}
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod T.
\tag{10}
\]

This requires only `T<p`, not the stronger sectorwise assumption `t=r_2/d<p` used in `MC-461`--`MC-462`.

For one represented anchor, the reduced variables satisfy `s_0\le S`; therefore

\[
\boxed{
N_U\le 1+\frac ST
=1+\frac{S(h_0,r_2)}{r_2}.}
\tag{11}
\]

After reciprocal-shift collisions are aggregated, the bare fixed-anchor moment of `MC-461` still cannot beat the pointwise bound unless the effective participation per represented anchor exceeds `p/L`, where `L` is the common character-interval length. The coefficient-independent global necessary condition is therefore

\[
\boxed{
1+\frac{S(h_0,r_2)}{r_2}>\frac pL,
}
\tag{12}
\]

or, away from the endpoint,

\[
\boxed{
SL\,(h_0,r_2)\gtrsim p r_2.
}
\tag{13}
\]

The internal gcd `d` has disappeared. What matters is the **outer normalized gcd** `G=(h_0,r_2)`.

This changes the next live test. The clue after `MC-462` proposed pricing favourable `d`-sectors separately. That is unnecessary at source-frame level: their apparent variation is a redundant parametrization of the same reduced trajectories. The remaining questions are instead whether outer pairs/shifts with sufficiently large `G` carry enough total weight, whether the aggregated coefficients `\widetilde\beta(s_0)` have enough effective participation inside the `T`-anchor fibres, and whether that participation survives the aligned unexpanded amplitude.

No conductor-power saving, no bound for `M(x)`, and no RH consequence follows.

## 1. The sector modulus normalizes to `T=r_2/G`

From `d=(s,r_2)` and compatibility, `d|r_2` and `d|h_0`, hence `d|G`. Write as in `MC-460`

\[
t=\frac{r_2}{d},\qquad h_1=\frac{h_0}{d}.
\tag{14}
\]

Because division by a common divisor commutes with the gcd,

\[
(h_1,t)
=\left(\frac{h_0}{d},\frac{r_2}{d}\right)
=\frac{(h_0,r_2)}d
=\frac Gd.
\tag{15}
\]

Therefore

\[
t_0
=\frac{r_2/d}{G/d}
=\frac{r_2}{G}
=T,
\tag{16}
\]

which proves `(2)`. Likewise

\[
\frac{h_1}{(h_1,t)}=\frac{h_0}{G}=H_0.
\tag{17}
\]

So both coprime reduced quantities appearing after the gcd extraction are fixed by the outer pair; neither depends on the residual sector.

## 2. The progression itself is sector-independent

The second outer condition in `MC-460` is

\[
t\mid r_1s_0m-h_1.
\tag{18}
\]

Substitute

\[
t=\frac Gd T,
\qquad
h_1=\frac Gd H_0.
\tag{19}
\]

Since `(r_1s_0,t)=1`, reduction of `(18)` modulo `G/d` forces

\[
m\equiv0\pmod{G/d}.
\tag{20}
\]

Write

\[
m=\frac Gd\,\ell.
\tag{21}
\]

Dividing `(18)` by `G/d` gives exactly

\[
T\mid r_1s_0\ell-H_0,
\tag{22}
\]

so `\ell` lies in the unique class `(4)` modulo `T`. Writing `\ell=\ell_{s_0}+Tj` proves `(3)`.

Now substitute into `n+h=g r_1 d s_0m`:

\[
n+h
=g r_1d s_0\frac Gd(\ell_{s_0}+Tj)
=g r_1G s_0(\ell_{s_0}+Tj),
\tag{23}
\]

which is `(5)`. Since `r'=gr_2=gGT`,

\[
\begin{aligned}
\frac n{r'}
&=\frac{r_1s_0(\ell_{s_0}+Tj)-H_0}{T}\\
&=\frac{r_1s_0\ell_{s_0}-H_0}{T}+r_1s_0j,
\end{aligned}
\tag{24}
\]

proving `(6)`.

The interval restriction on `j` comes from the original bounds on `n` together with positivity of the parametrized integer. Equation `(23)` shows that these bounds also depend only on `s_0`. Thus the sector collapse is not merely a congruence identity: it preserves the actual incomplete interval.

## 3. Source coordinates and the surviving amplitude also forget `d`

On nonzero character support, all factors that are inverted modulo `p` are coprime to `p`. Factoring the constants in `(23)`--`(24)` and rescaling the step `T` gives

\[
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})},
\tag{25}
\]

with `(7)`. The second residual divisor sum remains

\[
\overline{B_\beta(C_{s_0}+r_1s_0j)}.
\tag{26}
\]

Both are functions of `s_0` and `j` only. Therefore, whenever two original divisors `s=d s_0` and `s'=d's_0` occur with

\[
d,d'\mid G,
\qquad
(s_0,r_2/d)=(s_0,r_2/d')=1,
\tag{27}
\]

they contribute scalar coefficients multiplying the **same** inner trajectory. Summing those coefficients proves the aggregation formula `(8)`.

The condition `(s_0,r_2/d)=1` is exactly what ensures `(d s_0,r_2)=d`. Any additional nonzero-character support restriction can only remove terms from `(8)` and does not alter the collapse.

There is no polynomial coefficient penalty forced by this regrouping. For arbitrary coefficients,

\[
\sum_{s_0}|\widetilde\beta(s_0)|^2
\le
\tau(G)
\sum_{\substack{s\le S\\(s,r_2)\mid h_0}}
|\beta_s|^2,
\tag{28}
\]

because each `s_0` aggregates at most `\tau(G)` divisors `d|G`; this is Cauchy inside each fibre followed by the one-to-one decomposition `s=d s_0` with `d=(s,r_2)`. In particular, for ordinary arithmetic-size `G`, the regrouping itself creates at most a divisor-function loss, not a conductor-power loss.

Equation `(28)` is only an upper bound. Cancellation inside `\widetilde\beta` may make the effective participation substantially smaller, so it cannot be reversed into a lower bound.

## 4. The exact anchor partition needs only `T<p`

Equation `(4)` shows that the start residue is first determined by the unit class `s_0 mod T`, not by a residue modulo the larger sector modulus `t`. Choose `0\le\ell_{s_0}<T`. If `T<p`, then reduction of these canonical representatives modulo `p` is injective. Hence

\[
U_{s_0}=U_{s'_0}
\Longleftrightarrow
\ell_{s_0}=\ell_{s'_0}
\Longleftrightarrow
s_0\equiv s'_0\pmod T,
\tag{29}
\]

because multiplication and inversion by `H_0r_1^{-1}` are bijections on the unit classes modulo `T`. This proves `(10)`.

This strictly weakens the earlier sufficient condition `t<p`. A sector can have `t\ge p` while the true reduced anchor modulus `T=t/(h_1,t)` is below `p`; after normalization, such a sector is still covered by the exact anchor-fibre description.

If `T\ge p`, additional collisions of the canonical `\ell` representatives modulo `p` can occur. The common quotient representation remains exact, but `(10)` and the simple cardinality gate below require a separate collision count in that regime.

## 5. The support gate is an outer-gcd gate, not a sector-gcd gate

Under `T<p`, one anchor corresponds to one residue class

\[
s_0\equiv a\pmod T.
\tag{30}
\]

Every represented reduced divisor has `s_0\le S`, so one anchor contains at most

\[
1+\frac ST
=1+\frac{SG}{r_2}
\tag{31}
\]

source points before reciprocal-shift collisions. This proves `(11)`.

Let `R_U` be the number of represented anchors after the aggregation `(8)`, and let `W(U,D)` denote the resulting bare source weights after equal `(U,D)` points are merged. Then

\[
R_{\rm eff}(W)
=\frac{\|W\|_1^2}{\|W\|_2^2}
\le
R_U\left(1+\frac ST\right).
\tag{32}
\]

The exact fixed-anchor character moment from `MC-461` can beat the pointwise length-`L` bound only if

\[
R_{\rm eff}(W)>R_U\frac pL.
\tag{33}
\]

Combining `(32)` and `(33)` proves the obstruction `(12)` and its scale form `(13)`.

For any single sector, `MC-462` gave

\[
1+\frac{S(h_1,t)}{r_2}
=1+\frac{SG}{d r_2}.
\tag{34}
\]

The apparent `d`-dependence in `(34)` comes from artificially forbidding the other compatible divisors before Cauchy. Once all divisors that generate the same reduced trajectory are aggregated, the maximal source support is governed by `(31)`. Thus sectorwise support gates remain valid necessary tests inside a chosen decomposition, but the **natural full-family gate** is `(12)`.

## 6. Prior-art and novelty boundary

The identities `(15)`--`(24)` are elementary gcd extraction, CRT/congruence normalization, and finite regrouping. Equation `(28)` is Cauchy, and `(31)` is a residue-class count. No novelty is claimed for any of those operations.

The relevant modern well-factorable/dispersion literature already audited in `MC-456` routinely keeps convolution variables separated only while they play genuinely different analytic roles before Cauchy/dispersion. A targeted current literature search around well-factorable dispersion, gcd decompositions, and reciprocal character variables found the same broad analytic language but no theorem whose hypotheses directly identify or estimate the branch-specific normalized family `(4)`--`(8)`. That absence is not evidence of novelty and is not used as such.

The durable Mathia delta is internal and narrower: the exact `MC-460` gcd-sector decomposition contained a redundant parameter. Removing it shows that `MC-461`'s anchor quotient is globally `T=r_2/(h_0,r_2)`, extends the clean anchor regime from sectorwise `t<p` to `T<p`, and replaces the proposed sum over favourable residual gcd sectors by one aggregated coefficient family.

## Boundaries and falsification tests

- **The collapse is for a fixed outer pair and normalized shift.** `G=(h_0,r_2)` changes when the outer variables or shift change. It is not a global constant across the whole Möbius source sum.
- **The surviving `B_\beta` amplitude is still present.** Aggregation over `d` is exact because `(26)` is sector-independent, but no estimate is obtained for its correlation with the character phase.
- **Aggregation can reduce participation.** Destructive cancellation among the `\beta_{d s_0}` can make `\widetilde\beta(s_0)` sparse or small. The divisor-function upper bound `(28)` supplies no lower spread estimate.
- **`T<p` is load-bearing only for the simple fibre identity.** The common quotient representation `(3)`--`(8)` remains exact for `T\ge p`; only the injective reduction used in `(10)`--`(13)` fails without a collision count.
- **Reciprocal-shift collisions remain possible.** Distinct `s_0` in one anchor can coincide modulo `p` after inversion if the integer range wraps by `p`; weights must still be merged before computing participation.
- **No sectorwise positivity should precede `(8)`.** Applying Cauchy or absolute values separately in `d` discards exact coefficient aggregation between identical source/amplitude trajectories. Such a proof is valid as an upper bound but cannot claim that the `d`-sector count is an intrinsic source-frame cost.
- **The outer gcd may itself be rare.** Passing `(12)` requires large enough `G=(h_0,r_2)` when `S` and `L` are short. Whether those outer pairs/shifts carry enough total weight is now the next quantitative question.

## Consequence for the live branch

The `MC-462` frontier should be reformulated before any weighted completion is attempted. Do not sum favourable residual gcd sectors as though they were independent source families. First replace the original residual coefficients by `\widetilde\beta(s_0)` through `(8)` and work with the common quotient

\[
T=\frac{r_2}{(h_0,r_2)}.
\]

In the clean regime `T<p`, discard every outer pair/shift that fails `(12)`. For the survivors, measure actual participation of the aggregated coefficients in the reciprocal shifts and keep the aligned amplitude `(26)` through the first oscillatory estimate.

The next obstruction test is therefore at the **outer-gcd level**: quantify how much weight can lie on pairs with `SL(h_0,r_2)\gtrsim p r_2`, then determine whether `\widetilde\beta` has enough spread there. The internal `d`-sector bookkeeping is no longer a live source-frame mechanism.