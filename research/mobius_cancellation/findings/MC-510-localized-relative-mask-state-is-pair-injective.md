# MC-510 — Localized gauge-invariant cross-root state becomes pair-injective

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-RATIONAL-RECONSTRUCTION · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-509` shows that a sufficiently long localized tuple of one-row moving mask roots becomes an injective address for the source prime. There is an important representation objection to using that fact directly: `MC-487` already proved that the individual inverse shifts `h q^{-1}` are affine gauge. The physically meaningful cross-root mask should therefore first quotient that one-row gauge.

After doing so, source-addressing does not disappear. It moves from integer reconstruction to **rational reconstruction of the ordered source pair**. Moreover, before the full reconstruction threshold, the same determinant geometry gives a quantitative upper bound on the multiplicity of every exact relative-state fibre.

Fix an odd conductor prime `p`, a fixed nonzero shift `h`, a nonzero residue `a mod p`, and an interval

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
M_z=\prod_{\ell\in\mathcal S_z}\ell,
\qquad
N_z=pM_z.
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
\lambda_\ell(q,r):=q r^{-1}\pmod\ell,
\tag{5}
\]

and the retained state is

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
N_z\mid q r'-q'r.
}
\tag{8}
\]

Localization gives the sharper deterministic determinant bound

\[
\boxed{
|q r'-q'r|
\le (Q+H)^2-Q^2
=H(2Q+H).
}
\tag{9}
\]

Write

\[
B:=H(2Q+H).
\tag{10}
\]

Then

\[
\boxed{
N_z>B
\quad\Longrightarrow\quad
(q,r)\mapsto\Lambda_z(q,r)
\text{ is injective on the ordered distinct-prime source pairs}.}
\tag{11}
\]

The same argument gives a useful pre-reconstruction statement. For a fixed state `sigma`, let

\[
\mathcal F_\sigma
=\{(q,r):\Lambda_z(q,r)=\sigma\}
\tag{12}
\]

inside the localized repeated-residue source family. Then

\[
\boxed{
|\mathcal F_\sigma|
\le
1+2\left\lfloor\frac{B}{N_z}\right\rfloor
\left(
1+\left\lfloor\frac{H}{p\min I}\right\rfloor
\right).
}
\tag{13}
\]

In particular, whenever

\[
H<p\min I,
\tag{14}
\]

every exact relative-state fibre satisfies

\[
\boxed{
|\mathcal F_\sigma|
\le
1+2\left\lfloor\frac{B}{N_z}\right\rfloor.
}
\tag{15}
\]

Thus the exact relative tuple does not stay a large recurrent class until a sudden reconstruction transition. Its worst-case multiplicity is already charged by the remaining rational-reconstruction uncertainty `B/N_z`.

Since `h` is fixed, deleting its finitely many prime divisors and the single conductor prime does not change primorial growth:

\[
\log M_z=(1+o(1))z.
\tag{16}
\]

Consequently the full pair-reconstruction threshold still costs only logarithmic mask depth. In a dyadic block `I=[Q,2Q]`, where `H=Q`, `(11)` becomes the sufficient condition

\[
pM_z>3Q^2,
\tag{17}
\]

improving the earlier coarse `4Q^2` tariff. When `Q^2/p\to\infty`, a depth

\[
z=(1+\varepsilon)\log(3Q^2/p)
\tag{18}
\]

for any fixed `epsilon>0` is sufficient asymptotically, subject to `z<min I`. The number of retained lower-prime coordinates is still only of order

\[
\frac{\log(Q^2/p)}{\log\log(Q^2/p)}.
\tag{19}
\]

The frontier consequence is negative but sharper than pair injectivity alone:

> **quotienting the affine one-row mask gauge delays source identification, but exact relative-state recurrence is already depleted before the reconstruction threshold. At depth `z`, a state fibre is quantitatively limited by the unresolved determinant range `B/(pM_z)`; once that ratio falls below one, the state names the ordered pair itself.**

Therefore the surviving hard-mask route cannot obtain averaging merely by conditioning on an ever longer exact relative root tuple. A useful theorem must exploit a deliberately coarser state before it approaches rational-reconstruction capacity, control how many distinct exact states push forward to the same physical conductor coordinate, exploit endpoint/cutoff geometry before exact conditioning, or create a signed/complex pre-aggregation relation.

No estimate for the anti-diagonal collision excess of `MC-506`, for `M(x)`, or for zeta zeros follows.

## 1. The relative coordinate is exactly the affine-gauge quotient

For an active common lower prime `ell<min(q,r)` with `ell` not dividing `h`, `MC-502` gives the native plus/minus forbidden roots `(3)`. The first nonzero root is a unit. Normalizing it to `1` by multiplication with `-q h^{-1}` gives

\[
-hq^{-1}(-qh^{-1})=1\pmod\ell,
\]

while the opposite-root coordinate becomes

\[
hr^{-1}(-qh^{-1})=-qr^{-1}\pmod\ell.
\]

This removes the branchwise inverse-dilation gauge identified by `MC-487` while retaining the **relative** position of the two oriented nonzero roots. Equivalently, the ratio of the two native nonzero root coordinates is `-q r^{-1}`. The plus/minus root orientation is physical, so no arbitrary choice is needed to decide which shifted root is normalized.

The complete-period collision invariant from `MC-502` is only the special event

\[
\lambda_\ell(q,r)=-1
\iff
\ell\mid q+r.
\tag{20}
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
\tag{21}
\]

The moduli in `S_z` are pairwise coprime, hence

\[
M_z\mid q r'-q'r.
\tag{22}
\]

The repeated conductor-residue condition `(1)` supplies one more independent modulus. Modulo `p`,

\[
q r'-q'r\equiv a^2-a^2\equiv0,
\]

and `(p,M_z)=1`. This proves `(8)`.

This is the elementary uniqueness mechanism behind modular rational reconstruction: equality of bounded rational residues forces the cross determinant to be a multiple of the reconstruction modulus.

## 3. Localization gives the sharp interval determinant tariff

Every product `q r'` and `q'r` lies in the same interval

\[
[Q^2,(Q+H)^2].
\]

Therefore their difference satisfies `(9)` directly. This is slightly sharper than the earlier estimate obtained by separately bounding the two source differences.

If `N_z>B`, divisibility `(8)` forces

\[
q r'-q'r=0.
\]

Hence

\[
\frac qr=\frac{q'}{r'}.
\tag{23}
\]

Both fractions are reduced because each ordered pair consists of distinct primes. Equality in `(23)` therefore forces

\[
q=q',\qquad r=r',
\]

proving `(11)`.

The generic rational-reconstruction uniqueness bound with only independent numerator and denominator size would naturally be quadratic in the ambient scale. Localization replaces the relevant uncertainty by the width of the product interval, `B=H(2Q+H)`, which is `O(QH)` for narrow blocks.

## 4. Exact relative-state fibres are list-bounded before injectivity

Fix a nonempty fibre `F_sigma` and a reference pair `(q_0,r_0)` in it. For any `(q,r)` in the same fibre, `(8)` gives an integer `k` such that

\[
q r_0-q_0r=kN_z.
\tag{24}
\]

By `(9)`,

\[
|k|\le\left\lfloor\frac{B}{N_z}\right\rfloor.
\tag{25}
\]

There are therefore at most `2 floor(B/N_z)+1` possible determinant levels. The zero level contributes only the reference pair: if `k=0`, then `q/r=q_0/r_0`, and reducedness again forces `(q,r)=(q_0,r_0)`.

For a fixed nonzero `k`, suppose `(q,r)` and `(q',r')` are two solutions of `(24)`. Subtracting the two equations gives

\[
r_0(q-q')=q_0(r-r').
\tag{26}
\]

Because `q_0` and `r_0` are distinct primes, they are coprime. Hence for some integer `t`,

\[
q-q'=tq_0,
\qquad
r-r'=tr_0.
\tag{27}
\]

All source primes lie in the same nonzero conductor residue class, so `p` divides `q-q'`. Since `q_0` is nonzero modulo `p`, `(27)` forces `p|t`. Distinct same-level solutions are therefore separated in the `q` coordinate by at least

\[
pq_0\ge p\min I.
\tag{28}
\]

An interval of diameter at most `H` contains at most

\[
1+\left\lfloor\frac{H}{p\min I}\right\rfloor
\tag{29}
\]

such points. Multiplying this same-level multiplicity by the number of nonzero determinant levels and adding the unique zero-level pair proves `(13)`.

This is a list-size version of the same rational-reconstruction geometry. It is useful because it quantifies the exact state before the uniqueness threshold instead of describing only the endpoint at which reconstruction becomes complete.

A direct counting corollary is that any finite source-pair population `P` in the same localized residue block occupies at least

\[
\frac{|P|}{
1+2\lfloor B/N_z\rfloor
(1+\lfloor H/(p\min I)\rfloor)}
\tag{30}
\]

distinct exact relative states.

## 5. Relation to MC-509 and the live collision question

`MC-509` establishes that the gauge-dependent one-row root tuple identifies `q` once its CRT modulus exceeds the localized source width. One might object that this source-addressing effect is irrelevant because `MC-487` can remove the individual inverse shifts by a branchwise affine coordinate change.

The present result performs that quotient explicitly. The surviving common-core state is not the pair of absolute root tuples; it is the relative residue `q/r` modulo the growing primorial. Even this quotient becomes pair-injective once its modulus exceeds the localized cross-product uncertainty, and `(13)` now shows how its recurrent fibres thin before that point.

There are consequently three useful representation scales:

1. a short fixed local tuple, which remains programmable without localization by `MC-508`;
2. an intermediate relative tuple below rational-reconstruction depth, which is genuinely coarser than source-pair identity but whose exact fibre multiplicity is already bounded by `(13)`;
3. an exact sufficiently long relative tuple, which reconstructs the ordered source pair and supplies no repeated-class averaging by itself.

The anti-diagonal statistic of `MC-506` remains downstream of all three. Distinct pair states can still send mass to the same physical addition coordinate `t=x+j`. Therefore shrinking exact-state fibres does **not** by itself prove conductor dispersion or bound the collision excess.

What `(13)` removes is a weaker escape route: one cannot treat an intermediate exact relative tuple as an unspecified large recurrent class. Its available averaging population must be paid for explicitly through `B/N_z` and the within-level spacing factor. If those tariffs are too small, any remaining gain has to come from aggregation across distinct states or from information not preserved by exact-state conditioning.

## Prior art and novelty boundary

The general mathematics is classical modular rational reconstruction. Paul S. Wang, M. J. T. Guy and J. H. Davenport, *P-adic reconstruction of rational numbers*, ACM SIGSAM Bulletin **16** (1982), no. 2, 2–3, DOI `10.1145/1089292.1089293`, gives the classical bounded-numerator/bounded-denominator uniqueness and reconstruction mechanism via continued fractions. The determinant divisibility argument here is the same uniqueness principle.

The fibre estimate `(13)` is an elementary lattice-line/list-counting refinement of that same geometry: after fixing the reconstruction residue, bounded determinant levels label parallel Diophantine lines, and the repeated conductor residue class spaces points along each line. No novelty is claimed for rational reconstruction, CRT, lattice-line counting, the determinant test, or primorial growth.

The line-specific contribution is the **representation-correct specialization** to the surviving first-exit hard-mask frontier: after quotienting the affine inverse-shift gauge of `MC-487`, the oriented plus/minus lower-prime state is the modular rational `q/r`; tight source localization gives both the `O(QH)` reconstruction uncertainty and the explicit pre-reconstruction fibre tariff `(13)`.

A targeted literature audit on 24 September 2026 found the expected rational-reconstruction theory and no basis for a new general number-theory novelty claim. The durable result is the corrected information-budget boundary for this exact source representation.

## Boundaries and falsification tests

- **Fixed shift.** The primorial asymptotic `(16)` uses the line's fixed shift `h`, as in the first-exit setup of `MC-502`. The exact divisibility, determinant and fibre bounds do not require the asymptotic statement; for a moving `h`, one must explicitly account for the logarithmic mass of excluded prime divisors.
- **Oriented cross-root state.** The theorem keeps the physical plus/minus orientation. If the two shifted forbidden roots are deliberately made unlabeled, additional finite symmetries of the normalized three-point set must be quotiented separately.
- **Common-core primes only.** The state uses primes `ell<=z<min I`, so every retained prime lies below both source primes. One-sided tail primes between `q` and `r`, moving cutoffs and endpoint data are not needed for the theorem.
- **Distinct primes.** Diagonal pairs `q=r` are excluded. Their ratio is identically one and cannot be reconstructed as two independent source labels from `(6)`.
- **Repeated nonzero conductor residue.** The factor `p` in `(8)` and the same-level spacing in `(28)` both use `q,r,q',r' congruent a mod p` with `a` nonzero. Without that condition, the reconstruction modulus is only `M_z` unless separate conductor data are retained, and the `p min I` spacing factor disappears.
- **Sufficient, not exact, thresholds.** Equations `(11)` and `(13)` are deterministic upper bounds. They do not claim to identify the first physical scale at which every source family becomes injective or to give the exact fibre size.
- **Root state is not clipped coefficient state.** Distinct relative root tuples can still produce the same finite clipped coefficient vector, and equal or unequal clipped vectors require their own analysis.
- **Pair identity is not cancellation.** A lossless pair label, or a small exact-state fibre, gives no sign estimate, anti-diagonal dispersion or character-sum saving.
- **Complete-period overlap stays coarse.** `MC-502` uses only collision events `lambda_ell=-1`; pair reconstruction from the full tuple does not upgrade that logarithmic/totient coherence into a conductor-power effect.
- **No hidden zero information.** The proof uses only finite congruence algebra, localization, CRT/primorial growth and elementary rational-reconstruction geometry.

## Consequence

The gauge objection to `MC-509` is discharged at the pair level, and the intermediate regime is now quantitatively priced. The exact growing lower-prime state that survives affine normalization is a modular encoding of the rational source ratio `q/r`; on a localized repeated-residue block, its fibre multiplicity is at most `(13)` and it becomes pair-injective once `pM_z>H(2Q+H)`.

The live hard-mask question is therefore narrower: obtain collision control from a **deliberately lossy relative state** whose fibres remain large for a proved reason, prove structure in the map from many distinct exact pair states to the physical anti-diagonal pushforward, exploit the moving cutoff/endpoints, or introduce a genuine signed/complex pre-aggregation mechanism. Another appeal to unspecified recurrence of the exact growing relative profile is closed.