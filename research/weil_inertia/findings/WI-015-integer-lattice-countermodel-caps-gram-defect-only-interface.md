# WI-015 — an exact integer-lattice countermodel caps the Gram-defect-only support-one interface at 56/83

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY + DECISIVE-NEGATIVE` for the **collapsed support-one Gram-defect interface** described below. The master inequality `S >= H_MT N + tr Psi(M) - o(N)` is the stability bridge already audited in WI-009; the exact Montgomery--Taylor kernel is the same bandwidth-one kernel used there. Periodic integer-gap witnesses are direct prior art from `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`, so no novelty is claimed for the witness strategy. The new durable point is the exact self-contained audit that a sparse integer-lattice configuration keeps the **entire spectral defect** in the quadratic branch of `Psi`, so the obstruction is not limited to a chosen pair-energy lower witness or to a finite Bellman horizon.

## 1. Precise scope and claim

Let

\[
H=H_{\rm MT}
=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

and let `M` be the limiting Montgomery--Taylor Gram matrix of the retained simple critical-line atoms. The stability bridge used in WI-009--WI-012 has the form

\[
\boxed{
S\ge HN+\mathcal D(M)-o(N),
\qquad
\mathcal D(M)=\operatorname{tr}\Psi(M),
}
\tag{1}
\]

where `S=N_0^s(T,2T)` and

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

Consider a downstream argument that, after reaching (1), uses only

1. the exact limiting Montgomery--Taylor Gram geometry of the simple atoms;
2. their ordering/span or mean-gap bookkeeping; and
3. arbitrary post-processing of the full quantity `D(M)` (including the exact Fenchel dual of WI-012).

Then those data alone cannot force

\[
\boxed{
\frac SN>\frac{56}{83}=0.67469879518\ldots.
}
\tag{2}
\]

Indeed there is an explicit periodic integer-gap Gram model of density `56/83` for which **the full exact spectral defect**, not merely a lower witness for it, is small enough that (1) is satisfied with strict room.

This is an information-loss obstruction. It is not a claim that the actual zeros of `zeta` realize the periodic model, and it is not an upper bound on what the uncollapsed Weil matrix/inertia argument can prove if it retains additional information about the exceptional block.

## 2. The periodic model

Use the cyclic word of 56 positive gaps

\[
\boxed{
(1,1,2,\underbrace{1,2,1,2,\ldots,1,2}_{26\ \text{copies of }(1,2)},1).
}
\tag{3}
\]

It contains 29 gaps equal to `1` and 27 gaps equal to `2`, hence its normalized physical length is

\[
29+2\cdot27=83.
\]

Repeat the word periodically on the integer line. There are therefore 56 retained atoms per period of length 83, giving the density

\[
r=\frac{56}{83}.
\tag{4}
\]

The word has exactly two cyclic occurrences of adjacent gaps `(1,1)`. Consequently the number `C_j` of positive-oriented retained pairs at integer displacement `j`, per period, satisfies

\[
C_1=29,
\qquad
C_2=27+2=29,
\qquad
C_j\le56\quad(j\ge3).
\tag{5}
\]

The remaining `27/83` of the scalar zero-count budget is deliberately left unspecified. That is exactly the information discarded when the exceptional contribution has already been compressed into (1).

## 3. Integer Montgomery--Taylor overlaps

For the Montgomery--Taylor window, write

\[
k(x)=\frac{K(x)}{K(0)},
\qquad
w(x)=k(x)^2.
\]

At every positive integer `j`, product-to-sum gives the exact formula already used in WI-013,

\[
\boxed{
k(j)=\frac{(-1)^{j+1}}{2\pi^2j^2-1},}
\qquad
\boxed{w_j:=w(j)=\frac1{(2\pi^2j^2-1)^2}.}
\tag{6}
\]

The important extra fact here is spectral. For any finite subset of integer positions, each row of its Gram matrix sees at most one atom at each of the two displacements `+j,-j`. Since `pi>3`,

\[
|k(j)|
=\frac1{2\pi^2j^2-1}
<\frac1{17j^2}.
\]

Also

\[
\sum_{j\ge1}\frac1{j^2}<2,
\]

for example because `1/j^2 < 1/(j(j-1))` for `j>=2` and the latter tail telescopes. Hence every off-diagonal row sum is strictly below

\[
2\sum_{j\ge1}|k(j)|<\frac4{17}<1.
\tag{7}
\]

Gershgorin therefore places every eigenvalue `lambda` of every finite Gram section in

\[
1-\frac4{17}<\lambda<1+\frac4{17}<2.
\tag{8}
\]

Thus the kink of `Psi` at `2` is never reached on this model. The complete spectral defect collapses **exactly** to pair energy:

\[
\boxed{
\mathcal D(M)
=\operatorname{tr}(M-I)^2
=\sum_{i\ne j}|M_{ij}|^2.
}
\tag{9}
\]

This is the load-bearing step. It means that no more sophisticated evaluation of the exact Fenchel supremum in WI-012 can extract hidden spectral slack from this model: (9) is already the exact optimum.

## 4. A fully rational upper bound for the defect density

Let `d` denote the limiting defect per retained atom over longer and longer periodic sections. From (5) and (9),

\[
d
\le
\frac{29}{28}(w_1+w_2)
+2\sum_{j\ge3}w_j.
\tag{10}
\]

Use the classical rational enclosure

\[
\frac{333}{106}<\pi.
\]

Put `p_0=333/106` and

\[
W_1=\frac1{(2p_0^2-1)^2},
\quad
W_2=\frac1{(8p_0^2-1)^2},
\quad
W_3=\frac1{(18p_0^2-1)^2}.
\]

Then `w_j<W_j` for `j=1,2,3`, while for every `j>=4`,

\[
w_j
<\frac{W_1}{j^4}.
\]

The elementary tail estimate

\[
\sum_{j\ge4}\frac1{j^4}
\le\frac1{4^4}+\int_4^\infty x^{-4}\,dx
=\frac7{768}
\]

gives

\[
\begin{aligned}
d
&<
\frac{29}{28}(W_1+W_2)
+2W_3
+2W_1\frac7{768}\\[1mm]
&=
\frac{162573416279317361240279735011471}
{50235720092655657646453476240181344}\\[1mm]
&<\boxed{\frac{13}{4000}}.
\end{aligned}
\tag{11}
\]

The final inequality has exact positive margin

\[
\frac{13}{4000}-d_{\rm upper}
=
\frac{21646063181672690959189461534949}
{1569866252895489301451671132505667000}>0.
\tag{12}
\]

No numerical optimization or interval table enters this estimate.

## 5. A matching rational upper bound for the baseline

Set `x=1/sqrt(2)`. Alternating Taylor bounds give

\[
\cos x
\ge
1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}
+\frac{x^8}{8!}-\frac{x^{10}}{10!}
=\frac{88280819}{116121600},
\]

and

\[
\frac{\sin x}{x}
\le
1-\frac{x^2}{3!}+\frac{x^4}{5!}-\frac{x^6}{7!}
+\frac{x^8}{9!}
=\frac{5334193}{5806080}.
\]

Therefore

\[
x\cot x
=\frac{\cos x}{\sin x/x}
>\frac{827498}{10^6},
\]

with exact margin

\[
\frac{88280819/116121600}{5334193/5806080}
-\frac{827498}{10^6}
=
\frac{3455443}{2667096500000}>0.
\]

Hence

\[
\boxed{H<\frac{336251}{500000}=0.672502.}
\tag{13}
\]

## 6. Self-consistency at density 56/83

From (4), (11), and (13),

\[
H+rd<r
\]

follows already from

\[
r\left(1-\frac{13}{4000}\right)
=
\frac{27909}{41500}
>
\frac{336251}{500000}>H.
\tag{14}
\]

The exact rational margin in the middle inequality is

\[
\frac{27909}{41500}-\frac{336251}{500000}
=\frac{167}{41500000}>0.
\tag{15}
\]

Take `K` periods, so that the retained simple-atom count is `S_K=56K+O(1)` and the normalized span/total-count budget is `N_K=83K+O(1)`. Boundary terms in the pair sum are `o(K)`. Equations (9)--(15) therefore give

\[
HN_K+\mathcal D(M_K)
<S_K-cK+o(K)
\]

for some absolute `c>0`. Thus the limiting periodic model satisfies the same collapsed stability inequality (1) with strict room.

Consequently, **no proof that has already forgotten everything except (1), the exact Montgomery--Taylor simple Gram matrix, and scalar span/count information can rule out `S/N=56/83`.** In particular, optimizing the exact Fenchel dual, taking arbitrarily long finite-range connection-Laplacian witnesses, or finding a perfect Bellman subaction cannot by itself cross (2) unless some additional zeta-specific constraint is imported.

## 7. Prior art and novelty audit

The closest direct prior art is `trmdy/zeta-simple-zeros-673137`, `docs/campaign-2.md`. It explicitly uses balanced periodic integer-gap words to create phase-locked low-energy configurations and reports a numerical ceiling near `0.674826` for its **pure pair-energy** certificate class. The same document uses periodic-orbit cycle means as mandatory screens for Bellman/transfer-operator candidates.

Therefore:

- no novelty is claimed for integer-gap adversaries, balanced words, or periodic-orbit screening;
- no novelty is claimed for the exact integer formula (6), which is elementary and already used in WI-013;
- no priority claim is made for the idea that phase-locked integer configurations obstruct support-one pair-energy optimization.

The useful extra deduction for this line is the spectral observation (7)--(9): on a sufficiently sparse integer subset, the *full* `tr Psi(M)` itself equals pair energy because the whole spectrum remains below the kink at `2`. This promotes the obstruction from a limitation of a selected pair-energy witness family to a limitation of the **already-collapsed exact Gram-defect interface**. The conclusion is independently derived here with rational bounds; the upstream numerical ceiling is not imported as established evidence.

## 8. Boundaries and falsification tests

This finding is deliberately narrower than a no-go theorem for all support-one Weil/inertia arguments.

### The model is not asserted to be a zeta-zero configuration

Actual zeta zeros satisfy arithmetic constraints not represented by an arbitrary periodic gap word. A theorem excluding (3), or any neighborhood of it with enough quantitative strength, would evade the barrier. That would be **new input**, not a better optimization of the same collapsed data.

### The uncollapsed exceptional block can evade the barrier

WI-004 keeps positive remainder terms involving the exceptional contribution `Q`, including negative spectral mass and unused positive-inertia budget. WI-005--WI-007 show that naive depth-only pricing can be screened, but a genuinely new invariant coupling the simple Gram block to multiple/off-line blocks is not covered by (2).

### Wider support or new arithmetic can evade the barrier

Support `>1`, higher correlations, new prime-side moments, or any other arithmetic theorem that forbids the phase-locked model lies outside the interface being capped.

### The asymptotic-kernel scope matters

The countermodel is exact for the limiting Montgomery--Taylor kernel. The existing zeta bridge proves the kernel approximation uniformly on bounded normalized spans and handles tails separately. A proposed finite-`T` argument claiming to beat (2) solely from the same limiting interface must identify which additional uniform/tail information invalidates the periodic construction; otherwise it has not escaped the obstruction.

A direct falsification test is therefore precise: derive from established zeta input an additional inequality, absent from (1), that the periodic model (3) violates by a positive density. Merely improving the optimization of `D(M)` cannot do so because (9) already evaluates that quantity exactly.

## 9. Consequence for the research line

WI-012 showed that fixed-block pinching was artificial and that the global Fenchel dual legitimately recovers cross-boundary Gram information. The present finding identifies the next, deeper ceiling: **even the exact global simple-zero spectral defect can be too small on an admissible kernel model to force a substantially larger proportion.**

The most valuable next routes therefore have to add information rather than optimize the same scalar defect harder:

\[
\boxed{
\text{uncollapsed simple/exceptional block interaction}
}
\]

or

\[
\boxed{
\text{a zeta-specific spacing/correlation constraint that forbids the integer-lattice adversary},
}
\]

with support `>1` / new prime-side arithmetic remaining the other established escape. This does not make further support-one numerical improvements impossible below `56/83`; it says that crossing that explicit threshold requires a genuinely stronger interface than (1) plus the simple Montgomery--Taylor Gram geometry alone.
