# AF-321 — Rank-one eight-point singular recovery has no uniform harmonic conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `SELF-INVERSIVE`, `STABILITY-OBSTRUCTION`, `NEGATIVE/OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-320 proves exact recovery of the product phase on the rational-prime eight-point middle-singular branch by retaining the harmonics

\[
H(Z)=(s_2(Z),s_3(Z),s_4(Z),s_5(Z)),
\qquad
s_r(Z)=\sum_{z\in Z}z^r,
\tag{1}
\]

because source arithmetic excludes the deeper singularity `s_3=0`. The remaining question is whether the elementary source restriction used there — cyclic normalized character lattice, hence relation rank at most one — also supplies **quantitative conditioning**.

It does not.

There is a sequence of exact centered eight-point unit-circle configurations `Z_n` satisfying

\[
e_4(Z_n)=0,
\qquad
\operatorname{rank}_{\mathbb Z}L(Z_n)=1,
\tag{2}
\]

for which

\[
H(Z_n)\longrightarrow0,
\qquad
E(Z_n):=e_8(Z_n)=\prod_{z\in Z_n}z\longrightarrow1,
\tag{3}
\]

and necessarily

\[
s_3(Z_n)\ne0,
\qquad
|s_3(Z_n)|\longrightarrow0.
\tag{4}
\]

Thus

\[
\boxed{
\inf\{|s_3(Z)|:\ Z\text{ lies in the AF-318 rank-one middle-singular family}\}=0.
}
\tag{5}
\]

More strongly, exact product-phase recovery from `(1)` is not uniformly continuous on that rank-one family. If

\[
\rho=e^{i\pi/8},
\qquad
Z_n'=\rho Z_n,
\tag{6}
\]

then common rotation preserves centeredness, `e_4=0`, and the normalized character-relation lattice, while

\[
H(Z_n')
=(\rho^2s_2(Z_n),\rho^3s_3(Z_n),\rho^4s_4(Z_n),\rho^5s_5(Z_n))
\longrightarrow0
\tag{7}
\]

but

\[
E(Z_n')=\rho^8E(Z_n)=-E(Z_n).
\tag{8}
\]

Consequently

\[
\boxed{
\|H(Z_n)-H(Z_n')\|\longrightarrow0,
\qquad
|E(Z_n)-E(Z_n')|=2.
}
\tag{9}
\]

The exact inverse supplied by AF-320 therefore has no uniform modulus on the larger class singled out only by the currently known character-rank arithmetic restriction. Its closure contains a symmetry-enhanced collision fiber over `H=0` carrying **every** product phase in `S^1`.

This obstruction is not caused by colliding phase nodes: the limiting configuration is a regular octagon with uniformly separated roots. The instability comes from the chosen low-harmonic compression losing the common rotational/product-phase coordinate on a high-symmetry boundary stratum.

At that boundary, the first seven power sums are identically blind to the product phase, while the eighth harmonic restores it exactly:

\[
s_r=0\quad(1\le r\le7),
\qquad
s_8=-8E.
\tag{10}
\]

Hence `s_8` is the first power-sum harmonic that separates this particular closure fiber. No claim is made that it is a globally minimal lift among arbitrary observables or that retaining it gives a uniform inverse on the full eight-point source class.

## 1. A regular octagon lies on the deeper singular boundary

Set

\[
a=e^{i\pi/8},
\qquad
q=a^2=e^{i\pi/4},
\tag{11}
\]

and let `Z_0` be the eight roots of

\[
P_0(w)=w^8+1.
\tag{12}
\]

Thus

\[
Z_0=\{a\omega^k:0\le k\le7\},
\qquad
\omega=e^{i\pi/4}.
\tag{13}
\]

This is a regular octagon. The root-of-unity sum gives

\[
s_r(Z_0)=0
\qquad(1\le r\le7),
\tag{14}
\]

while every root satisfies `z^8=-1`, so

\[
s_8(Z_0)=-8.
\tag{15}
\]

The constant coefficient of `(12)` is

\[
E(Z_0)=e_8(Z_0)=1.
\tag{16}
\]

In particular `Z_0` is centered and lies on both singular conditions used by AF-320:

\[
e_4(Z_0)=0,
\qquad
s_3(Z_0)=0.
\tag{17}
\]

As expected, its normalized character lattice has high rank: the regular octagon is a torsion configuration and therefore is excluded from a nonzero rational-prime common-time orbit by AF-310. The point of `Z_0` is not to model a prime hit, but to identify the boundary approached by rank-one matched controls.

## 2. The AF-318 rank-one family accumulates on the regular octagon

The regular octagon belongs to the closure of the exact middle-singular family used in AF-318 in a particularly direct way.

Remove the antipodal pair `{a,-a}` from `Z_0` and call the remaining six-point configuration `B_0`. Polynomial division gives

\[
\frac{w^8+1}{w^2-q}
=w^6+qw^4+q^2w^2+q^3,
\tag{18}
\]

because `q^4=-1`. Comparing with

\[
P_{B_0}(w)
=w^6-e_1w^5+e_2w^4-e_3w^3+e_4w^2-e_5w+e_6
\tag{19}
\]

yields

\[
e_1(B_0)=0,
\qquad
e_2(B_0)=q\ne0,
\qquad
e_4(B_0)=q^2.
\tag{20}
\]

Therefore the AF-317 antipodal-extension phase is exactly

\[
A(B_0)=\frac{e_4(B_0)}{e_2(B_0)}=q=a^2,
\tag{21}
\]

so appending `{a,-a}` reconstructs `Z_0`.

The six remaining unit directions can be ordered cyclically with turning gaps `\pi/4,\pi/4,\pi/2,\pi/4,\pi/4,\pi/2`. Their sum is zero and every turning gap is strictly between `0` and `\pi`, so they form a strictly convex equilateral hexagon. Thus `B_0` lies in the nondegenerate marked equilateral-hexagon moduli used by AF-318, and `(20)` places it in the open set

\[
D=\{B:e_2(B)\ne0\}.
\tag{22}
\]

AF-318 proves that `D` contains a dense residual subset `D_*` such that the associated middle-singular eight-point extension `Z(B)` has normalized integer-character relation lattice exactly of rank one. Choose

\[
B_n\in D_*,
\qquad
B_n\longrightarrow B_0.
\tag{23}
\]

The map

\[
A(B)=\frac{e_4(B)}{e_2(B)}\in S^1
\tag{24}
\]

is continuous near `B_0`. Choose the local square-root branch `a(B)` with

\[
a(B)^2=A(B),
\qquad
a(B)\longrightarrow a,
\tag{25}
\]

and define

\[
Z_n=B_n\sqcup\{a(B_n),-a(B_n)\}.
\tag{26}
\]

Then every `Z_n` is centered, satisfies `e_4(Z_n)=0`, and has normalized relation rank exactly one, while

\[
Z_n\longrightarrow Z_0.
\tag{27}
\]

All power sums and elementary symmetric coefficients are continuous functions of the roots, so `(14)`, `(16)`, and `(27)` give exactly `(3)`.

Finally, `s_3(Z_n)` cannot vanish. On an eight-point centered unit-circle configuration, the simultaneous conditions

\[
e_4=0,
\qquad
s_3=0
\tag{28}
\]

force `e_1=e_3=e_4=e_5=e_7=0` by Newton identities and self-inversivity, hence an even root polynomial and four antipodal pairs. As in AF-320, that geometry gives more than one independent normalized character relation. It is incompatible with the rank-one property of `Z_n`. Therefore `s_3(Z_n)\ne0` for every `n`, while `(14)` and `(27)` force `s_3(Z_n)\to0`, proving `(4)` and `(5)`.

So the exact exclusion `s_3\ne0` has **zero quantitative margin** on the class defined by the same elementary character-rank restriction that produced it.

## 3. Rotation turns the vanishing margin into an exact non-uniformity theorem

The preceding sequence already proves that no positive lower bound for the AF-320 denominator can follow from rank-one character arithmetic alone. A common rotation strengthens this to failure of every uniform recovery modulus.

For `\rho\in S^1`, write

\[
\rho Z=\{\rho z:z\in Z\}.
\tag{29}
\]

Then

\[
s_r(\rho Z)=\rho^r s_r(Z),
\qquad
e_k(\rho Z)=\rho^ke_k(Z),
\qquad E(\rho Z)=\rho^8E(Z).
\tag{30}
\]

Thus centeredness and `e_4=0` are preserved. The normalized phase ratios are unchanged, because the common factor `\rho` cancels. Hence the normalized integer-character relation lattice, including its rank, is also unchanged.

Take `\rho=e^{i\pi/8}`. Equations `(3)` and `(30)` give `(7)`, so both compressed outputs tend to the same point `0\in\mathbb C^4`. But `\rho^8=-1`, and therefore `(8)` holds. Since `|E(Z_n)|=1`,

\[
|E(Z_n)-E(Z_n')|
=|E(Z_n)+E(Z_n)|
=2.
\tag{31}
\]

This proves `(9)`.

On the rank-one singular family the target `E` is nevertheless pointwise determined by `H`: rank one forbids `s_3=0`, and the purely algebraic AF-320 identity

\[
E
=\frac{6s_5-5s_2s_3}{10\overline{s_3}}
\tag{32}
\]

applies. Therefore `(9)` is not a failure of exact identifiability. It is a strict separation between

\[
\text{exact fidelity}
\quad\text{and}\quad
\text{uniformly stable fidelity}.
\tag{33}
\]

No map from `H(Z)` to `E(Z)` on this rank-one family can be uniformly continuous, and no continuous extension of that exact inverse exists at the closure point `H=0`.

The full closure fiber is larger than the two-phase witness `(8)`. For arbitrary `\rho\in S^1`, the rotated regular octagon `\rho Z_0` has

\[
H(\rho Z_0)=0,
\qquad
E(\rho Z_0)=\rho^8.
\tag{34}
\]

Because `\rho\mapsto\rho^8` is onto `S^1`,

\[
\boxed{
\{E(Z):Z\in\overline{\mathcal S_*},\ H(Z)=0\}=S^1,
}
\tag{35}
\]

where `\mathcal S_*` denotes the rank-one AF-318 singular family together with all common rotations. Every target phase is therefore represented over the same limiting low-harmonic datum.

## 4. The eighth harmonic is the first power-sum separator of the boundary fiber

The family `(34)` can be written intrinsically as the roots of

\[
w^8+E,
\qquad E\in S^1.
\tag{36}
\]

For every such regular octagon, root-of-unity cancellation gives

\[
s_r=0
\qquad(1\le r\le7).
\tag{37}
\]

At order eight, each root satisfies `z^8=-E`, so

\[
\boxed{s_8=-8E.}
\tag{38}
\]

Therefore no representation formed solely from any subset of the first seven power sums can distinguish the product phase on this closure fiber. The eighth power sum separates it exactly:

\[
E=-\frac{s_8}{8}.
\tag{39}
\]

This gives a precise minimality statement **within harmonic order at this boundary**: all orders below eight are blind, while order eight is faithful to the missing phase. It does not imply that `s_8` is the smallest arbitrary nonlinear mark, nor that adding `s_8` produces a globally well-conditioned parameterization of all centered eight-point configurations.

The distinction matters for Arithmetic Fidelity. Formula `(32)` repairs the middle singularity using a low-order relational identity when `s_3\ne0`; equation `(38)` shows what happens as that denominator loses margin. At the symmetry-enhanced boundary, the missing provenance has become an entire `S^1` gauge fiber and cannot be reconstructed continuously from the retained low harmonics.

## Arithmetic-fidelity consequence

AF-310 supplies a sharp **exact** arithmetic restriction: a common nonzero rational-prime time orbit has normalized character-relation rank at most one. AF-320 uses that restriction correctly to exclude the deeper exact degeneration `s_3=0` and obtain pointwise recovery.

AF-321 shows the limit of that information. Relation rank is a discrete incidence invariant; it is not a quantitative distance from higher-rank character strata. Rank-one middle-singular controls can approach a torsion regular octagon arbitrarily closely while the AF-320 denominator tends to zero. Consequently,

\[
\boxed{
\text{cyclic character rank alone cannot yield a uniform lower bound on }|F_P(3t)|
}
\tag{40}
\]

for a hypothetical eight-prime middle-singular hit.

This is a no-go statement about what follows from the **currently extracted source invariant**, not about the full rational-prime orbit. The rotated controls used in `(9)` need not themselves arise from the same fixed rational-prime support and common time. Their role is to show that every argument which remembers only centeredness, the middle-singular identity, and rank-one normalized character data leaves zero conditioning margin.

A genuine prime-source stability theorem must therefore introduce information finer than character rank: for example quantitative Diophantine separation of prime-log phases from the high-rank torsion/symmetry strata, a source-specific incidence estimate, or an additional retained mark whose value does not collapse on the regular-octagon boundary. This is exactly the qualitative-to-quantitative gap left open by AF-320.

The result also sharpens a general line-wide principle. Exact recoverability on a nonclosed admissible class is not enough for stable compression. One must audit the closure of the class: if a sequence approaches a larger fiber of the compressed representation while the target remains separated, any exact inverse loses uniform continuity before exact injectivity fails on the class itself.

## Prior art and novelty assessment

No broad novelty is claimed for moment inversion instability, Prony/Vandermonde conditioning, self-inversive polynomials, or regular-polygon power-sum identities.

- Dmitry Batenkov and Yosef Yomdin, **“Geometry and Singularities of the Prony mapping,”** *Journal of Singularities* 10 (2014), 1--25, DOI `10.5427/jsing.2014.10a`, studies the global geometry and singularities of moment/Prony inversion and its connections to Vieta and Vandermonde maps. It is direct prior art for treating loss of conditioning as geometry of a moment map rather than as a peculiarity of one reconstruction formula.
- Ankur Moitra, **“Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices,”** *Proceedings of STOC 2015*, 821--830, DOI `10.1145/2746539.2746561`, gives sharp noisy-recovery and Vandermonde conditioning thresholds controlled by frequency cutoff and source separation. It is representative prior art for quantitative stability of finite spectral/moment reconstruction.
- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, LMS Lecture Note Series 352, Cambridge University Press (2010), pp. 312--321, DOI `10.1017/CBO9780511721274.020`, is standard prior art for the unit-circle coefficient reciprocity used throughout AF-317--AF-320.

Those theories prevent interpreting “moment recovery can be ill-conditioned” as a new principle. The present obstruction is more specific and deliberately narrower: the limiting regular octagon has eight distinct, uniformly separated nodes, so the displayed loss of stability is **not** a node-collision phenomenon. It comes from restricting to the low-harmonic chart `(1)` on the centered middle-singular source class, whose closure acquires a rotational/product-phase fiber invisible through harmonic order seven.

No targeted prior-art claim is made that this exact rank-one eight-point boundary mechanism is new. Its durable role is to close a concrete Mathia question: the AF-310 rank-one arithmetic invariant that suffices for AF-320's exact recovery does not also provide its conditioning.

## Boundaries and failure modes

- No rational-prime middle-singular hit is constructed. The theorem is compatible with the possibility that the actual prime-log source stays quantitatively far from the regular-octagon boundary for deeper arithmetic reasons.
- The sequence `Z_n` is supplied nonconstructively by AF-318's dense residual rank-one subset. It proves absence of a uniform margin but does not give an explicit algebraic rank-one sequence or a rate for `|s_3(Z_n)|`.
- Common rotation preserves the normalized character lattice but generally does not preserve membership in one fixed rational-prime common-time orbit. Equation `(9)` is therefore a matched-control obstruction to arguments using only the rank invariant, not a pair of prime-source counterexamples.
- AF-320 remains exactly correct: on the rational-prime source class, and more generally on every rank-one middle-singular configuration here, `s_3\ne0` and formula `(32)` recovers `E` pointwise.
- The theorem gives no lower bound, upper bound, or asymptotic law for `|F_P(3t)|` on actual prime phases.
- The regular-octagon nodes do not collide. The result should not be paraphrased as a Vandermonde-separation failure; the unstable coordinate is a symmetry/provenance direction killed by the retained harmonic orders.
- The `s_8` statement is minimal only among power-sum harmonics on the regular-octagon boundary fiber. It neither proves global minimality among all admissible lifts nor uniform conditioning after adding `s_8`.
- The closure argument is specialized to support eight and the AF-318 antipodal-extension family. No automatic higher-even-support analogue is claimed.
- No zeta zero, critical-line statement, zero-density estimate, or RH consequence follows.

## Consequence for the research line

The eight-point middle-singular problem now separates cleanly into three levels.

First, **ambient exact recovery fails** for the generic low-harmonic formula on `e_4=0` (AF-317--AF-318). Second, **source-relative exact recovery is repaired** by the fifth harmonic because prime character rank excludes the deeper exact degeneration (AF-320). Third, **source-relative stability is still open**: AF-321 proves that the character-rank information used for exact repair has zero quantitative margin and cannot by itself control conditioning.

The next useful step is therefore not another exact character-rank exclusion. It is either a quantitative prime-log incidence/separation theorem against the high-symmetry singular strata, or a representation-level repair that retains a stable provenance coordinate before the low-harmonic compression reaches the regular-octagon closure fiber.