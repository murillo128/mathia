# AF-320 — Eight-prime middle-singular recovery is repaired by the fifth harmonic

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SELF-INVERSIVE`, `SOURCE-SPECIFIC-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

Let `p_1,...,p_8` be distinct rational primes, let `t\ne0`, and set

\[
z_j=p_j^{-it}\in S^1,
\qquad
s_r=\sum_{j=1}^8 z_j^r
    =F_P(rt),
\qquad
F_P(u)=\sum_{j=1}^8p_j^{-iu}.
\tag{1}
\]

Assume the phase configuration is centered,

\[
s_1=F_P(t)=0.
\tag{2}
\]

Then the four harmonics

\[
\boxed{(s_2,s_3,s_4,s_5)}
\tag{3}
\]

determine the complete unordered phase multiset `\{z_1,...,z_8\}` exactly.

The point is not that four harmonics generically suffice — AF-316 already gives the sharper generic statement. The new source-specific fact is that rational-prime arithmetic removes the only deeper degeneration that blocks a one-step repair of the first even-support singularity.

Write

\[
P_Z(w)=\prod_{j=1}^8(w-z_j)
      =\sum_{k=0}^8(-1)^ke_kw^{8-k},
\qquad
E=e_8=\prod_{j=1}^8z_j\in S^1.
\tag{4}
\]

From centering and Newton's identities,

\[
e_2=-\frac{s_2}{2},
\qquad
e_3=\frac{s_3}{3},
\qquad
e_4=\frac{s_2^2-2s_4}{8}.
\tag{5}
\]

If `e_4\ne0`, AF-316 recovers the product phase directly from the middle self-inversive coefficient,

\[
E=\frac{e_4}{\overline{e_4}},
\tag{6}
\]

so `s_2,s_3,s_4` already recover the full polynomial.

If instead

\[
e_4=0,
\tag{7}
\]

then a rational-prime common-time configuration necessarily satisfies

\[
\boxed{s_3\ne0.}
\tag{8}
\]

Indeed, if `s_3=0`, then `e_1=e_3=e_4=0`; self-inversivity also gives `e_5=e_7=0`, so `P_Z` is an even polynomial. Its roots therefore split into four antipodal pairs. Those pairs force at least two independent exact integer-character relations among the normalized phases, contradicting AF-310's theorem that the relation lattice of distinct rational-prime phases at one nonzero time is cyclic.

Once `(8)` is known, the fifth Newton identity and self-inversivity recover the missing product phase exactly:

\[
5e_5=s_5-\frac56s_2s_3,
\qquad
e_5=E\overline{e_3}=\frac{E\overline{s_3}}{3},
\tag{9}
\]

hence

\[
\boxed{
E=\frac{6s_5-5s_2s_3}{10\overline{s_3}}.
}
\tag{10}
\]

All remaining coefficients then follow from

\[
e_{8-k}=E\overline{e_k}.
\tag{11}
\]

Thus the ambient middle-singular stratum found in AF-317--AF-318 is a genuine failure set for the generic low-harmonic formula, but it is **not** an unrecoverable stratum on the rational-prime source class: one additional harmonic closes it exactly.

Equivalently, a hypothetical eight-prime middle-singular hit must obey the explicit dyadic and fifth-harmonic constraints

\[
\boxed{F_P(4t)=\frac12F_P(2t)^2,}
\tag{12}
\]

\[
\boxed{F_P(3t)\ne0,}
\tag{13}
\]

and

\[
\boxed{
\left(\prod_{j=1}^8p_j\right)^{-it}
=
\frac{6F_P(5t)-5F_P(2t)F_P(3t)}
     {10\overline{F_P(3t)}}.
}
\tag{14}
\]

There is also an exact extremal exclusion:

\[
\boxed{|F_P(2t)|<4}
\tag{15}
\]

at every such singular prime hit. The bound `\le4` follows from `(12)` and `|F_P(4t)|\le8`; equality would force all fourth powers `z_j^4` to have the same phase, placing seven independent fourth-power relations in the normalized character lattice and again contradicting AF-310.

No claim is made that `(3)` is a minimal global representation, that a singular prime hit exists, or that the recovery is uniformly well-conditioned.

## 1. The middle singularity is visible in the harmonic data

For a centered configuration `s_1=e_1=0`. Newton's identities give

\[
2e_2=-s_2,
\qquad
3e_3=s_3,
\tag{16}
\]

and

\[
s_4+e_2s_2+4e_4=0.
\tag{17}
\]

Substituting `e_2=-s_2/2` into `(17)` yields

\[
8e_4=s_2^2-2s_4,
\tag{18}
\]

which is the third formula in `(5)`. Therefore the generic recovery map of AF-316 can detect its own failure stratum from the retained harmonics:

\[
e_4=0
\iff
s_4=\frac12s_2^2.
\tag{19}
\]

For the prime phases `(1)`, equation `(19)` is exactly `(12)`.

This matters for fidelity rather than merely for algebraic bookkeeping. The compression does not silently cross an unknown singular set: the same output data expose whether the middle self-inversive phase closure is usable. The remaining question is what additional information is required precisely on that detected stratum.

## 2. A deeper singularity would force global antipodal symmetry

Assume now `e_4=0`. If also `s_3=0`, then `(16)` gives `e_3=0`. Unit-circle roots make the coefficient system self-inversive:

\[
e_{8-k}=E\overline{e_k},
\qquad 0\le k\le8.
\tag{20}
\]

Since `e_1=e_3=0`, equation `(20)` gives

\[
e_7=e_5=0.
\tag{21}
\]

Together with `e_4=0`, every odd coefficient of `P_Z` vanishes:

\[
P_Z(w)
=w^8+e_2w^6+e_6w^2+E.
\tag{22}
\]

Hence

\[
P_Z(-w)=P_Z(w).
\tag{23}
\]

The root multiset is therefore invariant under `z\mapsto-z`: the eight labelled phases can be partitioned into four pairs `(a_r,b_r)` with

\[
z_{b_r}=-z_{a_r}.
\tag{24}
\]

Each pair supplies an integer-character relation

\[
\left(\frac{z_{b_r}}{z_{a_r}}\right)^2=1.
\tag{25}
\]

The four pair-difference exponent vectors are independent in the sum-zero character lattice of the eight labelled coordinates. After normalizing by any one phase, at least two — in fact four — independent relations remain.

AF-310 proves that for distinct rational primes at a common nonzero time the normalized integer-character relation lattice has rank at most one. Therefore `(24)` is impossible for `(1)`, proving `(8)`.

This is narrower than the failed six-to-eight extrapolation killed by AF-317 and AF-318. Those findings show that `e_4=0` alone does not force antipodal geometry and is even compatible with ambient relation rank one. The present argument uses the **strictly smaller** deeper stratum

\[
e_4=0,
\qquad e_3=0,
\tag{26}
\]

which does force evenness. Rational-prime arithmetic excludes `(26)` even though it cannot exclude the full middle-singular stratum.

## 3. The fifth harmonic recovers the lost product phase

Newton's identity at order five is

\[
s_5-e_1s_4+e_2s_3-e_3s_2+e_4s_1-5e_5=0.
\tag{27}
\]

On the centered middle-singular stratum, `e_1=s_1=e_4=0`, so using `(16)` gives

\[
5e_5
=s_5+e_2s_3-e_3s_2
=s_5-\frac56s_2s_3.
\tag{28}
\]

Self-inversivity at the coefficient pair `(e_3,e_5)` gives

\[
e_5=E\overline{e_3}
    =\frac{E\overline{s_3}}{3}.
\tag{29}
\]

Because `(8)` guarantees `s_3\ne0` on the rational-prime source class, equations `(28)` and `(29)` can be solved for `E`, producing `(10)`.

The full polynomial is then determined. On this singular branch one may write it explicitly as

\[
P_Z(w)
=
w^8
-\frac{s_2}{2}w^6
-\frac{s_3}{3}w^5
-\frac{E\overline{s_3}}{3}w^3
-\frac{E\overline{s_2}}{2}w^2
+E.
\tag{30}
\]

Thus `s_2,s_3,s_5` already determine the singular configuration; `s_4` is redundant there because of `(19)`. Globally, however, `s_4` is what identifies whether the generic or singular reconstruction formula applies, yielding the exact source-class representation `(3)`.

Equation `(10)` also imposes the unit-modulus consistency condition

\[
\boxed{
|6s_5-5s_2s_3|=10|s_3|.
}
\tag{31}
\]

Any proposed eight-prime singular incidence must satisfy `(12)`, `(13)`, and `(31)` before more delicate arithmetic information is considered.

## 4. The singular second harmonic cannot reach its ambient extremum

Equation `(12)` gives

\[
|F_P(2t)|^2
=2|F_P(4t)|
\le16,
\tag{32}
\]

so `|F_P(2t)|\le4`.

Suppose equality held. Then `|F_P(4t)|=8`. Since `F_P(4t)` is a sum of eight unit complex numbers, equality in the triangle inequality forces

\[
z_1^4=z_2^4=\cdots=z_8^4.
\tag{33}
\]

After normalization by `z_8`, each coordinate

\[
u_j=z_j/z_8,
\qquad 1\le j\le7,
\]

satisfies `u_j^4=1`. Hence the seven independent vectors `4e_j` belong to the normalized relation lattice. This contradicts AF-310's rank-one theorem and proves `(15)`.

The strict inequality is qualitative. Nothing here supplies a uniform positive gap below `4`; exact character-rank exclusion does not by itself control how closely the prime-log orbit may approach high-rank torsion strata.

## 5. Prior art and novelty boundary

No novelty is claimed for Newton identities, self-inversive coefficient reciprocity, finite-moment reconstruction, or the general theory of zeros of Dirichlet/exponential polynomials.

- I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), is standard background for Newton identities and the conversion between elementary symmetric coefficients and power sums.
- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, LMS Lecture Note Series 352, Cambridge University Press (2010), pp. 312--321, DOI `10.1017/CBO9780511721274.020`, is direct prior art for the conjugate-reciprocal coefficient structure used in `(20)`.
- Stefan Kunis, Thomas Peter, Tim Römer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.023`, is representative classical/modern prior art for reconstructing finitely supported measures from moment data. The present theorem exploits the much more specialized unit-circle, equal-weight, centered and prime-source structure rather than claiming a new general moment-reconstruction theory.
- Willian D. Oliveira, **“Zeros of Dirichlet polynomials via a density criterion,”** *Journal of Number Theory* 203 (2019), 80--94, DOI `10.1016/j.jnt.2018.02.001`, studies zero-free half-planes and density criteria for Dirichlet polynomials; it does not decide the isolated simultaneous harmonic incidence `(12)`--`(14)`.
- Janne Heittokangas, Kazuya Ishizaki, Ilpo Laine, and Katsuya Tohge, **“Value distribution of exponential polynomials and their role in the theories of complex differential equations and oscillation theory,”** *Bulletin of the London Mathematical Society* 55 (2023), 2235--2280, DOI `10.1112/blms.12719`, surveys common-zero/factorization theory for exponential polynomials, including Shapiro-type results concerning **infinitely many** common zeros. That theory does not by itself exclude one isolated imaginary-axis common zero of the specific functions appearing here.

The algebraic formulas in this finding are elementary consequences of those classical structures. The durable Arithmetic Fidelity contribution is the source-relative boundary: AF-317--AF-318 show that the ambient middle-singular geometry survives the elementary rank-one prime compatibility test, while AF-320 shows that the next degeneration needed to defeat fifth-harmonic phase recovery does **not** survive it. This is exactly a case where a source constraint repairs a compression failure without pretending that the whole singular stratum was impossible.

## Boundaries and failure modes

- The theorem assumes eight **distinct rational primes** and one common nonzero time. The exclusion of `s_3=0` uses AF-310 and therefore the multiplicative independence of those prime generators.
- The recovered object is the unordered phase multiset `\{p_j^{-it}\}`. The theorem does not recover the labels, the primes themselves, or the time `t` from the harmonic tuple.
- Nothing here proves that an eight-prime centered middle-singular hit exists. Equations `(12)`--`(14)` and `(31)` are necessary constraints on such a hit, not an existence theorem.
- No minimality is claimed for `s_5`. A different nonlinear or marked representation might repair the same singular stratum with other data.
- Exact recovery is not stable recovery. Formula `(10)` divides by `s_3`, and the argument proves only `s_3\ne0`, not a quantitative lower bound on `|s_3|`. Conditioning may therefore deteriorate arbitrarily near the deeper antipodal stratum.
- The strict bound `(15)` is not a uniform separation theorem: no constant `\delta>0` with `|F_P(2t)|\le4-\delta` is established.
- The result does not contradict AF-318. AF-318 proves that `e_4=0` contains an ambient residual rank-one family; AF-320 excludes only the additional `e_3=0` degeneration for the rational-prime source class.
- The argument is specialized to support eight. No claim is made that the next harmonic always repairs every higher even-support middle singularity.
- No zeta zero, critical-line statement, zero-density estimate, or RH implication follows.

## Consequence for the research line

The first unresolved even-support recovery problem is now more sharply stratified.

AF-316 gives exact low-harmonic recovery away from `e_4=0`. AF-317 and AF-318 show that `e_4=0` is a real ambient singular family and cannot be dismissed by torsion, global antipodal symmetry, or character-rank arguments alone. AF-320 adds the source-specific next step: within the rational-prime common-time class, the deeper sub-stratum `e_4=e_3=0` is impossible, so the fifth harmonic reconstructs the product phase everywhere on the remaining singular branch.

The live arithmetic question therefore remains **incidence**, not representation existence: can the prime-log orbit satisfy `F_P(t)=0` together with `F_P(4t)=F_P(2t)^2/2` at all? If it can, the phase configuration is still exactly recoverable from one additional harmonic. What remains unresolved is whether that incidence is arithmetically impossible and, separately, whether the exact fifth-harmonic repair has any useful uniform conditioning.