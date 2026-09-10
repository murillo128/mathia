# PC-249 — shared-upper rectangular cross-Grams collapse after the Frobenius threshold

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for one of the explicit rectangular-packet escapes left open by PC-248. Let `p<r<q` be distinct primes and let `K_{p,q}` and `K_{r,q}` be the native prime-prime polyphase packets of PC-245/PC-246, so that both have the same `q`-dimensional upper-shell row space. Once

\[
q>pr-p-r,
\tag{1}
\]

their full mixed row-space Gram block satisfies the exact identity

\[
\boxed{
K_{p,q}^{*}K_{r,q}=q\,K_{p,r}^{T}.
}
\tag{2}
\]

Thus retaining the changing rectangular packets and coupling them through their common upper-prime orientation does not create a new pairwise all-scale carrier at fixed lower primes: beyond the finite threshold, the entire mixed block is just the lower-lower packet multiplied by the elementary scalar `q`. For finitely many fixed lower primes, every off-diagonal block of the joint Gram matrix freezes in this way; all remaining non-scalar `q`-dependence lies in the diagonal signed-residue blocks already classified by PC-246--PC-248 as finite Dirichlet-character data.

The number `pr-p-r` is the classical two-generator Frobenius number. No novelty is claimed for that formula, interval-overlap matrices, or piecewise-constant partition geometry. The project-local content is the exact identification (2) for the source-forced Prime-Circle transfer packets and the resulting closure of the most direct shared-row-space interpretation of PC-248's rectangular-packet boundary.

## 1. The rectangular packets as two interval partitions of one upper row space

For primes `a<b`, PC-246 identifies the `b x a` native transfer packet with the overlap matrix of two uniform integer partitions. Equivalently, after scaling the `ab`-point interval by `a`, introduce the unit cells

\[
C_u=[u,u+1),\qquad 0\le u<b,
\tag{3}
\]

and the `a` long cells

\[
A_t^{(a,b)}=
\left[\frac{bt}{a},\frac{b(t+1)}a\right),
\qquad 0\le t<a.
\tag{4}
\]

Then the exact PC-246 overlap formula becomes

\[
\boxed{
K_{a,b}(u,t)=a\,|C_u\cap A_t^{(a,b)}|.
}
\tag{5}
\]

There is no approximation in (5): all endpoints are rational, and multiplying the scaled overlap length by `a` returns the integer overlap count in the original `ab`-point partition.

Now fix `p<r<q`. In their common upper row coordinate `u=0,...,q-1`, define

\[
A_t=
\left[\frac{qt}{p},\frac{q(t+1)}p\right),
\qquad 0\le t<p,
\tag{6}
\]

and

\[
B_s=
\left[\frac{qs}{r},\frac{q(s+1)}r\right),
\qquad 0\le s<r.
\tag{7}
\]

Equation (5) gives simultaneously

\[
K_{p,q}(u,t)=p|C_u\cap A_t|,
\qquad
K_{r,q}(u,s)=r|C_u\cap B_s|.
\tag{8}
\]

Therefore the mixed cross-Gram entry is

\[
\boxed{
(K_{p,q}^{*}K_{r,q})_{t,s}
=pr\sum_{u=0}^{q-1}
|C_u\cap A_t|\,|C_u\cap B_s|.
}
\tag{9}
\]

Unlike the individual Grams in PC-246, this object retains the relative orientation of two different rectangular packets in the same `q`-row space. It is therefore exactly the first pairwise quantity to test before claiming that Gram compression had discarded a useful common-upper-shell relation.

## 2. Frobenius-threshold separation of the two boundary meshes

The only obstruction to replacing the product of the two overlap lengths in (9) by the overlap of all three intervals is a unit cell containing an interior boundary from **both** long partitions.

The interior `p`-partition boundaries are

\[
\frac{qi}{p},\qquad 1\le i<p,
\tag{10}
\]

and the interior `r`-partition boundaries are

\[
\frac{qj}{r},\qquad 1\le j<r.
\tag{11}
\]

Suppose one boundary of each kind lies in the same unit cell `C_u`. Since `q` is coprime to both lower primes, neither boundary is integral, so there are uniquely determined remainders

\[
qi=pu+a,
\qquad 1\le a\le p-1,
\tag{12}
\]

and

\[
qj=ru+b,
\qquad 1\le b\le r-1.
\tag{13}
\]

Multiplying (12) by `r`, (13) by `p`, and subtracting gives

\[
q(ri-pj)=ra-pb.
\tag{14}
\]

Because `p` and `r` are coprime and `i,j` are proper interior indices, `ri-pj` cannot vanish. Hence

\[
q\le |ra-pb|.
\tag{15}
\]

But over the allowed remainder ranges,

\[
|ra-pb|
\le r(p-1)-p
=pr-p-r.
\tag{16}
\]

(The opposite sign gives the same maximum.) Consequently

\[
\boxed{
q>pr-p-r
\quad\Longrightarrow\quad
\text{no unit cell contains boundaries of both meshes.}
}
\tag{17}
\]

The threshold in (17) is exactly the classical Frobenius number `g(p,r)=pr-p-r` for two coprime generators. This identification is conceptually useful but not needed as an imported theorem: inequalities (14)--(16) prove the separation directly. For a modern proof and historical account of the two-generator Frobenius formula, see Melvyn B. Nathanson, *Commutative algebra and the linear diophantine problem of Frobenius*, arXiv:1611.07415 (2016), https://arxiv.org/abs/1611.07415.

## 3. Exact collapse of the mixed rectangular cross-Gram

Under (17), each unit cell contains a boundary of at most one of the two long partitions. Thus, on every `C_u`, at least one of the two indicator functions `1_{A_t}` and `1_{B_s}` is constant. It follows exactly that

\[
|C_u\cap A_t|\,|C_u\cap B_s|
=
|C_u\cap A_t\cap B_s|.
\tag{18}
\]

Summing (18) over the unit partition and using (9),

\[
(K_{p,q}^{*}K_{r,q})_{t,s}
=pr|A_t\cap B_s|.
\tag{19}
\]

Scaling the common upper interval by `q`,

\[
|A_t\cap B_s|
=q\left|
\left[\frac tp,\frac{t+1}p\right)
\cap
\left[\frac sr,\frac{s+1}r\right)
\right|.
\tag{20}
\]

Apply the same interval-overlap formula (5) to the lower pair `(p,r)`. Its row index is `s` and column index is `t`, so

\[
K_{p,r}(s,t)
=pr\left|
\left[\frac tp,\frac{t+1}p\right)
\cap
\left[\frac sr,\frac{s+1}r\right)
\right|.
\tag{21}
\]

Combining (19)--(21) proves

\[
\boxed{
K_{p,q}^{*}K_{r,q}=qK_{p,r}^{T}
\qquad(q>pr-p-r).
}
\tag{22}
\]

This is entrywise equality of the complete mixed block, not equality after a trace, determinant, spectral ordering, average, or asymptotic limit. The upper prime contributes no modular residue at all to this off-diagonal block once the boundary meshes are separated.

## 4. Joint finite families add no new shared-orientation information

Fix distinct lower primes

\[
p_1<\cdots<p_m
\tag{23}
\]

and let `q` be a prime larger than `p_m` and every pairwise Frobenius threshold:

\[
q>Q_0:=
\max_{1\le i<j\le m}
(p_ip_j-p_i-p_j).
\tag{24}
\]

Concatenate all rectangular packets in their common upper row space,

\[
\mathcal K_q=
\bigl[K_{p_1,q}\ \cdots\ K_{p_m,q}\bigr].
\tag{25}
\]

PC-246 gives the diagonal blocks

\[
K_{p_i,q}^{*}K_{p_i,q}
=p_iqI_{p_i}-L_{p_i,q\bmod p_i},
\tag{26}
\]

while (22) gives every off-diagonal block. Hence there is a fixed, `q`-independent block matrix `G_0`, determined only by the lower-prime list, such that

\[
\boxed{
\mathcal K_q^{*}\mathcal K_q
=qG_0-
\operatorname{diag}
\bigl(
L_{p_1,q\bmod p_1},\ldots,
L_{p_m,q\bmod p_m}
\bigr).
}
\tag{27}
\]

Explicitly, the diagonal block of `G_0` is `p_i I_{p_i}` and, for `i<j`, its `(i,j)` block is `K_{p_i,p_j}^{T}` with the adjoint in the reversed position.

Equation (27) is the information boundary relevant to PC-248. Before this calculation, one possible escape was that replacing each rectangle by its individual Gram `K_{p,q}^*K_{p,q}` had destroyed relative orientation in the shared upper-shell row space. It does destroy orientation in general, but for this source-forced fixed-lower prime family **the missing pairwise orientation carries no additional upper-prime information after the finite threshold**. Every off-diagonal mixed block is fixed up to `q`; all non-scalar upper-prime variation remains in the diagonal residue matrices already classified by PC-247 and PC-248.

In particular, any fixed readout of the joint Gram after removing the elementary scalar dependence still factors through the same finite signed-residue tuple

\[
q\longmapsto
\bigl([q]_{p_1},\ldots,[q]_{p_m}\bigr),
\qquad
[q]_{p_i}\in
(\mathbb Z/p_i\mathbb Z)^\times/\{\pm1\},
\tag{28}
\]

so the finite-character classicalization of PC-248 applies unchanged to this enlarged Gram-level input.

## 5. Exact controls and the strict boundary

For `p=3`, `r=5`, the lower packet is

\[
K_{3,5}^{T}
=
\begin{pmatrix}
3&2&0&0&0\\
0&1&3&1&0\\
0&0&0&2&3
\end{pmatrix}.
\tag{29}
\]

Since `pr-p-r=7`, every prime `q>7` satisfies

\[
K_{3,q}^{*}K_{5,q}
=q
\begin{pmatrix}
3&2&0&0&0\\
0&1&3&1&0\\
0&0&0&2&3
\end{pmatrix}.
\tag{30}
\]

The strict inequality in (22) is not merely a proof artifact. For `p=5`, `r=7`, the threshold is `23`; at the boundary value `q=23`, direct exact overlap arithmetic gives

\[
K_{5,23}^{*}K_{7,23}-23K_{5,7}^{T}
=
\begin{pmatrix}
0&0&0&0&0&0&0\\
0&0&-1&1&0&0&0\\
0&0&1&-2&1&0&0\\
0&0&0&1&-1&0&0\\
0&0&0&0&0&0&0
\end{pmatrix}
\ne0.
\tag{31}
\]

Thus a simultaneous boundary crossing really does create a finite correction below or at the separation threshold. The theorem is a genuine eventual exact stabilization statement, not an identity valid for every upper level.

As a matched nonarithmetic control, the derivation uses only the uniform-partition/all-one-mask structure after (5). If arbitrary coprime lower integers `a<r` are equipped artificially with all-one short masks, the same proof gives

\[
K_{a,q}^{*}K_{r,q}=qK_{a,r}^{T}
\qquad(q>ar-a-r,\ (q,ar)=1).
\tag{32}
\]

So the collapse mechanism itself belongs to elementary commensurable interval geometry. Prime cyclotomy supplies the all-one mask canonically at prime levels; primality is not what generates the stabilization.

## 6. Prior-art and novelty audit

Three ingredients must be separated.

First, overlap matrices of piecewise-constant partitions and their Gram/composition relations are standard linear/projection geometry. No novelty is claimed for representing a finite packet through interval intersections.

Second, `pr-p-r` is the classical Frobenius number for two coprime generators, historically due to the nineteenth-century two-denomination Frobenius/Sylvester problem. Nathanson's arXiv:1611.07415 gives a modern proof and explicitly records the formula. Equation (17) is an elementary boundary-separation reformulation of the same numerical threshold, not a new Frobenius theorem.

Third, PC-245 already places the ambient weighted-cover star words in classical affine/polyphase `ax+b` operator architecture, with Cuntz and the Toeplitz affine-semigroup literature anchored in `research/prime_circle/SOURCES.md`. The present theorem does not claim a new operator algebra.

The project-local delta is narrower: the source-forced **rectangular native prime transfer packets** singled out by PC-248 satisfy the exact eventual cross-Gram factorization (22), and therefore their shared-upper relative orientation cannot supply an additional fixed-lower all-scale arithmetic variable. A targeted literature search over uniform partition overlaps, finite projection/mass matrices, Frobenius thresholds, and Beatty/floor formulations found the expected classical ingredients but no need to invoke an absence claim: the research consequence follows from the exact reduction itself.

There is no new bridge to the Riemann zeros here. On the contrary, the result removes one natural place where information lost by separate Gram compression might have survived.

## 7. Boundary of the obstruction

The chain closed by this finding is

\[
\boxed{
\text{fixed lower prime family}
\to
\text{rectangular native transfers in one shared upper-prime row space}
\to
\text{pairwise/joint Gram geometry}
\to
\text{new upper-prime RH carrier}.
}
\tag{33}
\]

The theorem is intentionally not a statement that the complete rectangular matrices `K_{p,q}` themselves become identical after normalization. Their canonical `q`-row coordinates still vary, and a readout that depends on those absolute row labels rather than only their mutual inner products lies outside (22)--(27). Such a construction would have to justify why that row-coordinate dependence is intrinsic rather than a chosen representation.

Likewise, the result does not cover a lower-prime set growing with `q` so that the Frobenius threshold is never uniformly passed, several independent upper primes coupled before contraction, native composite cyclotomic masks with nontrivial coefficients, or an infinite-dimensional/source-forced topology taken before fixed-lower stabilization. The nonlinear/off-circle/global-uniformization sectors of the Prime-Circle mandate are untouched.

Accordingly, simply retaining the rectangles and taking their common-row cross-Grams is no longer a distinct escape from PC-248. Any surviving rectangular-packet mechanism must use information beyond the eventual pairwise Gram geometry: a genuinely growing modulus, canonical row-coordinate-sensitive operation, multi-upper relation, or another source-forced structure that evades (17).

## Falsification checks

The claim is exactly auditable. Starting from PC-246 equation `K_{a,b}(u,t)=|I_u\cap J_t|`, rescale to verify (5). For any proposed counterexample to (22), locate a unit cell containing both an interior `p` boundary and an interior `r` boundary; equations (12)--(16) force `q<=pr-p-r`, so no such cell can exist in the claimed range. With boundary separation established, check (18) cell by cell and sum to obtain (19)--(22).

Finite exact controls are also immediate. For `(p,r)=(3,5)`, verify (30) for `q=11`; for `(5,7)`, verify both (22) at `q=29` and the nonzero threshold correction (31) at `q=23`. For a finite lower-prime family, assemble the concatenated matrix and check every block of (27). Failure of any one of these exact identities changes the conclusion; otherwise the fixed-lower shared-upper pairwise orientation is completely exhausted by the lower-lower packet and the already-known diagonal signed-residue data.
