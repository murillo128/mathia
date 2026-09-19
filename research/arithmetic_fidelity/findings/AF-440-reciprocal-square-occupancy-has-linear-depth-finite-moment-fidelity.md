# AF-440 — Reciprocal-square occupancy has linear-depth finite-moment fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-SUPERINCREASING-PRINCIPLE`, `ARITHMETIC-FIDELITY`, `FINITE-PREFIX-RECOVERY`, `SOURCE-CLASS-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-439 shows that the first `N` Euler/Stieltjes moments do not determine nearby pole locations when an admissible control may move `N+1` support points continuously while keeping unit residues. The obstruction disappears partially—and quantitatively—once the support skeleton is fixed and the remaining shell marks belong to a discrete separated alphabet.

Let `A\subset\mathbb R` be a finite alphabet with at least two values, and define

\[
\delta:=\min_{a\ne b\in A}|a-b|>0,
\qquad
D:=\max A-\min A>0.
\]

For an infinite mark sequence `a=(a_m)_{m\ge1}\in A^{\mathbb N}`, set

\[
F_a(z):=\sum_{m\ge1}\frac{a_m}{m^2-z}
=\sum_{k\ge1}S_k(a)z^{k-1},
\qquad |z|<1,
\]

where

\[
S_k(a):=\sum_{m\ge1}a_m m^{-2k}.
\]

Then equality of the first `N` Taylor/moment coefficients forces agreement on an explicit initial shell segment:

\[
\boxed{
S_k(a)=S_k(b)\ (1\le k\le N)
\quad\Longrightarrow\quad
a_m=b_m\text{ for every }m\text{ with }Dm\le\delta(2N-1).
}
\]

In fact the highest retained coefficient `S_N` alone already has this property.

For the binary occupancy class `A=\{0,1\}`, this becomes

\[
\boxed{
S_N(a)=S_N(b)
\quad\Longrightarrow\quad
a_m=b_m\qquad(1\le m\le 2N-1).
}
\]

Thus, after restricting AF-439's broad moving-node class to the **exact reciprocal-square support ladder with binary unit-residue occupancy**, a finite Euler moment prefix is no longer completely non-identifying. Its highest moment certifies a shell-occupancy prefix whose depth grows at least linearly with the retained moment order.

This is not global injectivity. The theorem only localizes every possible same-prefix ambiguity beyond the certified shell depth; it does not assert that different admissible tails actually collide, nor does it classify them.

## Exact derivation

Fix `N>=1` and write

\[
s:=2N.
\]

Suppose `a\ne b`, and let `m` be their first differing shell. Since the alphabet is `\delta`-separated,

\[
|a_m-b_m|\ge\delta.
\]

For every later shell,

\[
|a_j-b_j|\le D.
\]

Therefore

\[
\begin{aligned}
|S_N(a)-S_N(b)|
&=\left|
(a_m-b_m)m^{-s}
+\sum_{j>m}(a_j-b_j)j^{-s}
\right|\\
&\ge
\delta m^{-s}-D\sum_{j>m}j^{-s}.
\end{aligned}
\tag{1}
\]

Because `x^{-s}` is positive and strictly decreasing,

\[
\sum_{j>m}j^{-s}
<\int_m^\infty x^{-s}\,dx
=\frac{m^{1-s}}{s-1}.
\tag{2}
\]

Combining `(1)` and `(2)` gives

\[
|S_N(a)-S_N(b)|
>
m^{-s}\left(\delta-\frac{Dm}{s-1}\right).
\tag{3}
\]

More exactly, define

\[
\Delta_{N,m}
:=
\delta m^{-2N}
-D\sum_{j>m}j^{-2N}.
\tag{4}
\]

Whenever

\[
Dm\le\delta(2N-1),
\tag{5}
\]

the strict inequality in `(2)` implies

\[
\boxed{\Delta_{N,m}>0.}
\tag{6}
\]

Hence two sequences whose first disagreement occurs at such an `m` cannot have the same value of `S_N`. Equality of `S_N` therefore forces equality of every shell satisfying `(5)`, proving the claim.

For `A=\{0,1\}`, one has `\delta=D=1`, so `(5)` is simply

\[
m\le2N-1.
\]

The same proof also gives, for integer multiplicities `A=\{0,1,\ldots,B\}`, the guaranteed prefix

\[
m\le\left\lfloor\frac{2N-1}{B}\right\rfloor.
\]

The relevant source resource is therefore not merely discreteness: the recoverable depth depends explicitly on the ratio `\delta/D`, i.e. the minimum mark separation relative to the full admissible mark range.

## Quantitative separation and greedy decoding

Equation `(4)` is a pairwise separation margin. If two admissible sequences first disagree at shell `m` satisfying `(5)`, then

\[
\boxed{
|S_N(a)-S_N(b)|\ge\Delta_{N,m}>0.
}
\]

Thus an exact value of `S_N` identifies the first certified shells, and an additive observation error smaller than `\Delta_{N,m}/2` cannot confuse two feasible sequences whose first disagreement is at shell `m`.

For strict interior shells with

\[
Dm<\delta(2N-1),
\]

the elementary integral bound gives the explicit lower estimate

\[
\Delta_{N,m}
>
m^{-2N}
\left(
\delta-\frac{Dm}{2N-1}
\right).
\tag{7}
\]

At the boundary `Dm=\delta(2N-1)`, the right side of `(7)` vanishes but the exact margin `(4)` remains positive because the sum/integral comparison is strict.

There is also a constructive interpretation. After earlier marks have been decoded and subtracted, changing the candidate value at shell `m` shifts the remaining sum by at least

\[
\delta m^{-2N},
\]

whereas the total range available to all later shells is at most

\[
D\sum_{j>m}j^{-2N}.
\]

Condition `(5)` makes the candidate intervals disjoint. Therefore the certified initial segment can be decoded greedily from the single scalar `S_N`: decide the current shell mark, subtract it, and continue until the tail diameter is no longer smaller than the current alphabet gap.

This is the familiar superincreasing-sequence mechanism in reversed order: an early reciprocal-power weight dominates the entire admissible later tail.

## Stieltjes interpretation

For binary occupancy `\varepsilon_m\in\{0,1\}`,

\[
F_\varepsilon(z)
=\sum_{m\ge1}\frac{\varepsilon_m}{m^2-z}
\]

has a simple pole at `m^2` with residue `-1` exactly when `\varepsilon_m=1`; if `\varepsilon_m=0`, that pole is absent.

AF-439 allowed the support points themselves to move. The first `N` moments then possess an exact local Newton/Prony fiber through the Euler source. The present class removes precisely that continuous freedom:

- pole locations are fixed a priori to `m^2`;
- pole residues/occupancies belong to a separated finite alphabet;
- the high-order moment weights `m^{-2N}` become tail-dominating on a growing initial segment.

Therefore the AF-439 fiber is not an unavoidable property of finite Stieltjes data. It is a property of the **admissible source category**. Once support provenance and a discrete residue law survive the compression, finite data regain a quantifiable amount of exact fidelity.

The result also sharpens what “fixing the reciprocal-square support law” buys. It does not magically make a finite moment prefix globally sufficient; it turns the inverse problem into a discrete positional code with an explicit depth-versus-order guarantee.

## Relation to AF-436, AF-438, and AF-439

AF-436 already used the same tail estimate

\[
\sum_{j>m}j^{-2k}
\le \frac{m^{1-2k}}{2k-1}
\]

to show that, after earlier shells are peeled, shell `m` dominates its residual as `k\to\infty`. That theorem concerns the **complete exact coefficient sequence**, fixed shell depth, and sequential asymptotic recovery.

The present result turns the same hierarchy sideways. For a **single finite order** `N`, it asks how many discrete shell marks are simultaneously protected against every admissible later tail. The answer is at least linear in `N` for binary occupancy: `2N-1` shells are already fixed by `S_N` alone. No limiting process in `N` and no prior-shell estimation is needed for that exact finite certificate.

AF-438 packages the full moment sequence into one Stieltjes transform whose poles jointly carry all shells. AF-439 then proves that a finite Taylor prefix cannot identify nearby pole locations in a broad unit-residue moving-node class. This finding supplies the first direct positive source-class response to that obstruction:

\[
\text{moving continuous support}
\;\Longrightarrow\;
\text{finite-prefix local fibers},
\]

whereas

\[
\text{fixed support + separated discrete marks}
\;\Longrightarrow\;
\text{finite-prefix initial-shell fidelity}.
\]

The remaining question is no longer simply whether a source restriction exists, but how weak that restriction can be while retaining a useful depth law and whether comparable guarantees survive noise or less rigid support uncertainty.

## Prior-art and novelty audit

The proof is elementary and the decoding mechanism is classical. A superincreasing sequence—one in which each weight dominates the sum of all smaller weights—has unique subset-sum decoding by a greedy procedure. This principle is standard in knapsack mathematics and was used explicitly in the Merkle-Hellman trapdoor-knapsack construction:

- Ralph C. Merkle and Martin E. Hellman, **“Hiding Information and Signatures in Trapdoor Knapsacks,”** *IEEE Transactions on Information Theory* 24(5), 525–530 (1978), DOI `10.1109/TIT.1978.1055927`.

The general use of decreasing power moments to expose dominant atoms is likewise classical moment/Prony territory; AF-436 already records Hausdorff moment, support-recovery, and Prony references. No novelty is claimed for superincreasing subset sums, greedy decoding, integral tail comparison, Hausdorff moments, or dominant-atom recovery.

The present contribution is the Arithmetic Fidelity specialization at the exact AF-439 boundary: for the reciprocal-square Stieltjes ladder, the `N`-th moment creates a **finite superincreasing head** whose certified depth can be bounded explicitly from the alphabet separation/range ratio. This identifies one concrete source-side currency—fixed support provenance plus discrete mark separation—that converts finite-prefix non-identifiability into finite-prefix partial recovery.

## Boundaries and falsification checks

- The theorem fixes the support locations `m^{-2}` exactly. It does not survive AF-439's continuously movable support class without an additional location-separation/uncertainty theorem.
- The mark alphabet is finite and separated. If marks range over an interval, `\delta=0` and the argument gives no positive certified depth; continuous residue adjustments can again absorb arbitrarily small differences.
- The result is a **prefix** theorem, not global injectivity. It says any two same-data controls must agree through the certified shell depth; it does not characterize the residual tail fiber.
- The linear cutoff `Dm\le\delta(2N-1)` is a guaranteed bound from a simple integral estimate, not a claimed optimal threshold. For particular `N`, alphabet, or support restrictions, further shells may also be uniquely determined.
- The quantitative margin `(4)` is an absolute scalar separation in the `S_N` coordinate. It does not prove good relative conditioning when `m` and `N` grow jointly; the margin itself can be extremely small.
- For the genuine Euler source all binary occupancies are `1`. The theorem should therefore be read as discrimination against matched subset/occupancy controls on the same shell skeleton, not as discovery of the already-known Euler support.
- Fixing reciprocal-square support is a strong source assumption. An RH-facing transformation must independently preserve or justify that provenance before this theorem can be invoked downstream; otherwise using it would assume exactly the information whose survival is under audit.
- Nothing here distinguishes rational primes, constrains zeta zeros, or implies RH. The result is a source-class fidelity theorem for the Euler shell representation.

A direct falsification would require two admissible mark sequences with equal `S_N` whose first differing shell satisfies `(5)`. Inequalities `(1)`–`(6)` rule such a pair out exactly.

## Consequence for the research line

AF-439's next-step question was to identify a natural source/tail/support class strong enough to restore finite-prefix injectivity or at least quantify the residual fiber. The reciprocal-square discrete-mark class supplies such a quantitative answer without pretending that finite data recover the whole source.

The useful abstraction is broader than this Euler example: **finite compression can recover an initial provenance segment when the retained weights form a tail-dominating code relative to the admissible mark alphabet**. The amount of fidelity is controlled jointly by observation order, support decay, and mark separation.

The next decisive weakening test is to relax the strongest resource one at a time—bounded support jitter, nonbinary but separated residues, or a support law known only within intervals—and determine whether a comparable depth theorem survives. That directly measures which part of the restored fidelity comes from exact provenance and which part comes from discreteness alone.