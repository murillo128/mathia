# PF-167 — positive primitive-length accumulation is inherited by the exact all-composite shift clone

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + DECISIVE-NEGATIVE/BOUNDARY + LITERATURE-CLASSIFIED`. PF-069 proves that the exact prime flute has a nondegenerate compact interval `I_L subset (0,infinity)` contained in the accumulation set of explicit primitive simple separating lengths. PF-166 proves that the exact all-composite shift clone `p_n -> p_n+1` is asymptotically identical to the prime flute at the level of the complete marked tail translation-length function. Combining the two gives an exact matched-control correction: **the same interval `I_L` is also contained in the accumulation set of primitive simple lengths of the all-composite shift clone.** Consequently the finite-length explosion of primitive counting from PF-077 occurs in that exact all-composite control as well.

The result does not weaken the geometric conclusion of PF-069 or the counting obstruction of PF-077. It changes their arithmetic interpretation. Positive-window non-discreteness of the primitive length spectrum and failure of ordinary prime-geodesic counting are genuine features of this prime-derived surface, but they are not primality selectors and cannot by themselves supply an RH mechanism.

## Claim

Let `X` be the exact prime flute and `X_+` the exact all-composite shift clone of PF-106/PF-125. Let

\[
F:X\longrightarrow X_+
\]

be the globally coherent marking from PF-125, and let `T_N subset X`, `T_N^+ subset X_+` be the matched tails used in PF-166. Write

\[
K_N:=\operatorname{Bilip}(F|_{T_N}),
\qquad K_N\longrightarrow1.
\tag{1}
\]

PF-166 proves that every hyperbolic free-homotopy class `alpha` carried by `T_N` satisfies

\[
\boxed{
K_N^{-1}
\le
\frac{\ell_{X_+}(F_*\alpha)}{\ell_X(\alpha)}
\le
K_N.}
\tag{2}
\]

Let `I_L` be the nondegenerate compact interval produced by PF-069. Then

\[
\boxed{
I_L
\subset
\overline{
\{\ell_{X_+}(\gamma):
\gamma\text{ primitive simple closed geodesic in }X_+\}}
.}
\tag{3}
\]

More precisely, every `L in I_L` is an accumulation point of lengths of primitive simple separating geodesics in `X_+` which are the marked images of the PF-069 separator classes.

If

\[
L_*:=\inf I_L,
\]

then for every `T>L_*`,

\[
\boxed{
\#\{\gamma\subset X_+:
\gamma\text{ primitive simple closed geodesic},\
\ell_{X_+}(\gamma)\le T\}
=\infty.}
\tag{4}
\]

Thus the ordinary primitive-geodesic counting function is already infinite at finite length on both the prime flute and this exact all-composite matched control.

## 1. PF-069 accumulation sequences escape into the tail

Fix `L in I_L`. By PF-069 there is a sequence of explicit PF-004 primitive simple separating classes `alpha_j` associated with four consecutive prime-derived boundary points such that

\[
\ell_X(\alpha_j)\longrightarrow L.
\tag{5}
\]

The construction uses consecutive prime-gap triples with indices tending to infinity. Therefore the supporting four-point blocks, and hence the corresponding separator classes, escape every fixed finite head of the flute. Equivalently, there are tail indices `N_j -> infinity` with

\[
\alpha_j\text{ carried by }T_{N_j}.
\tag{6}
\]

This is the only extra localization fact needed beyond PF-069 and PF-166.

## 2. Uniform marked tail control transports the limit

Apply PF-166 to `alpha_j` in `T_{N_j}`. Equation (2) gives

\[
\left|
\log\frac{\ell_{X_+}(F_*\alpha_j)}{\ell_X(\alpha_j)}
\right|
\le
\log K_{N_j}.
\tag{7}
\]

Since `N_j -> infinity` and `K_N ->1`,

\[
\frac{\ell_{X_+}(F_*\alpha_j)}{\ell_X(\alpha_j)}
\longrightarrow1.
\tag{8}
\]

Together with (5),

\[
\boxed{
\ell_{X_+}(F_*\alpha_j)\longrightarrow L.}
\tag{9}
\]

A homeomorphism preserves simplicity, primitivity of the free-homotopy class, and the separating topological type. The global geodesic representative in `X_+` stays in the matched tail by the separating-cuff argument already proved in PF-166. Hence (9) is an accumulation sequence of primitive simple separating geodesics in the exact all-composite clone. Since `L in I_L` was arbitrary, (3) follows.

No rate from Banks--Freiberg--Maynard and no summability over the primitive orbit family is required. The transfer uses only the uniform multiplicative marked-length error tending to zero on escaping tails.

## 3. The finite-length counting explosion transfers as well

Let `T>L_*`. Choose a nonempty open interval

\[
J\Subset I_L\cap(0,T).
\]

Every point of `J` is an accumulation point of primitive simple clone lengths by (3). In particular `J` contains infinitely many distinct primitive simple clone geodesics. Therefore the clone counting function in (4) is infinite.

The same argument transfers the weighted divergence statement of PF-077: if a nonnegative weight `w(L)` is bounded below by a positive constant on some nonempty `J subset I_L`, then the weighted primitive count over the clone also diverges. Thus ordinary prime-geodesic/Chebyshev counting does not become meaningful merely by replacing the prime labels with this exact all-composite sequence.

## 4. Adversarial interpretation

PF-069 remains an exact arithmetic-to-geometric theorem: Banks--Freiberg--Maynard prime-gap limit geometry feeds the exact prime-flute cross-ratio and produces a positive interval of primitive separating-length accumulation. The new control asks a different question: does that geometric output still distinguish the rational primes once the exact all-composite matched surface is admitted?

It does not. The shift clone was built from composite labels but retains the prime-gap sequence in its ordering, and PF-166 proves that the full marked tail length function becomes asymptotically indistinguishable from the prime surface. Therefore the accumulation interval is a **retained relational-geometric feature**, not evidence that the Laplace/periodic-orbit geometry recognizes primality.

This distinction prevents two overclaims. First, PF-167 does not say the prime and clone primitive length multisets are globally equal; finite-head lengths and finite-scale defects can differ. Second, it does not imply equality of orbit multiplicities inside shrinking windows, full relative Selberg/Ruelle products, resonances, scattering matrices, or discrete Laplace spectra. Infinite assembly can still amplify individually vanishing marked-length errors, as PF-158 already demonstrates for one selected separator family.

The exact conclusion is only what (3)--(4) state: the positive accumulation interval and the resulting failure of finite primitive counting survive an exact all-composite matched control.

## 5. Prior art and novelty boundary

The abstract ingredients are classical. Infinite-type hyperbolic surfaces may have non-discrete length spectrum, and the discrete-length-spectrum regime is a special class; Basmajian--Kim and the recent Fanoni--Fisac work cited in PF-069/PF-077 provide that context. A bilipschitz marking distorts marked closed-geodesic lengths by the same multiplicative constant, and asymptotic length-spectrum equivalence is standard in infinite-type Teichmuller theory; PF-166 already audits this against Yaşar's formulation.

No novelty is claimed for those general facts or for the Banks--Freiberg--Maynard theorem used by PF-069. The durable Mathia-specific result is the exact composition

\[
\boxed{
\text{PF-069 BFM separator sequence}
\;+
\text{PF-166 complete tail marked-length equivalence}
\Longrightarrow
I_L\text{ is also a clone accumulation interval}.}
\tag{10}
\]

This is best classified as a matched-control correction/refinement of the prime-flute interpretation, not as a new general theorem about infinite-type length spectra.

## 6. Falsification core

A later audit can falsify the result only by breaking one of the following exact steps:

1. PF-069 does not actually provide, for every `L in I_L`, a sequence of primitive simple separator classes with lengths tending to `L`;
2. those separator blocks fail to escape every finite head;
3. PF-166's uniform tail estimate (2) does not apply to those classes;
4. `K_{N_j}` fails to tend to `1` along an escaping sequence;
5. the marking can turn a primitive or simple free-homotopy class into a nonprimitive or nonsimple one.

Items 2 and 5 are elementary consequences of the indexed separator construction and of homeomorphism invariance; items 1, 3, and 4 are the persisted PF-069/PF-166 claims. No numerical experiment or unproved prime-gap heuristic enters the transfer.

## Consequence for the research line

PF-069/PF-077 still decisively close the **ordinary** global Selberg/prime-geodesic counting architecture, because bounded positive length windows contain infinitely many primitive simple orbits. PF-167 adds the matched-control conclusion that this pathology itself is not an arithmetic selector: the exact all-composite shift clone has it too.

A surviving prime-specific dynamical mechanism must therefore use information finer than positive-window non-discreteness or infinite primitive counting. It must distinguish the prime surface from the shift clone through a genuinely collective infinite assembly, an operator/scattering/resonance effect not fixed by asymptotic marked-length equivalence, or another intrinsic datum that survives the control audit.