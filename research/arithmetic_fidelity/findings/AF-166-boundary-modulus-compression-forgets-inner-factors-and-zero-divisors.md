# AF-166 — Boundary-modulus compression forgets inner factors and zero divisors

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MINIMAL-LIFT-STRUCTURE`, `PHASE/ORIENTATION`, `NO-NOVELTY-CLAIM`

## Claim

Boundary magnitude is an exact example of a compression that can preserve a rich analytic envelope while erasing the entire zero-bearing factor.

Let `0<p<=infinity`, let `H^p(D)` be the Hardy space on the unit disk, and for nonzero `f in H^p(D)` let `f*` denote its nontangential boundary function. Define the boundary-modulus compression

\[
\mathcal M(f)=|f^*|\quad\text{a.e. on }\mathbb T.
\tag{1}
\]

The classical canonical factorization can be written

\[
f=B_fS_fO_f,
\tag{2}
\]

where `B_f` is a Blaschke product carrying the disk zeros of `f`, `S_f` is a zero-free singular inner factor, and `O_f` is outer. Since both inner factors have boundary modulus one almost everywhere,

\[
\boxed{
\mathcal M(f)=|O_f^*|.
}
\tag{3}
\]

Consequently the compression `(1)` retains the outer magnitude data but is blind to both pieces of the inner factor. More sharply, after fixing the canonical outer representative `O_\rho` with positive value at the origin for a realizable boundary magnitude `rho`, the complete fiber is

\[
\boxed{
\mathcal M^{-1}(\rho)
=
\{I O_\rho:I\text{ inner}\}.
}
\tag{4}
\]

Thus the exact information discarded by boundary modulus is not an unspecified generic "phase": it is the **inner-factor coordinate**. Its Blaschke component is precisely the part that carries the disk zero divisor.

For every finite Blaschke product `B`,

\[
\boxed{
\mathcal M(Bf)=\mathcal M(f),
}
\tag{5}
\]

while, provided the inserted zeros do not cancel against a denominator because `B` is analytic and bounded in the disk, the zero divisor of `Bf` is the zero divisor of `f` plus the zero divisor of `B`, counted with multiplicity. In particular, taking the outer control `f=1`, arbitrary finite zero multisets can be inserted without changing the retained boundary modulus at all.

Therefore any downstream observable of the form

\[
T(f)=\Phi(\mathcal M(f))
\tag{6}
\]

is **provably non-faithful to the disk zero divisor** on any admissible family closed under multiplication by a nonconstant finite Blaschke product. No later operation acting only on `T(f)` can reconstruct which Blaschke zero set was present.

This gives an exact compression/lift hierarchy:

1. modulus alone retains the outer factor but not the zero-bearing inner factor;
2. modulus plus a zero-divisor/Blaschke mark recovers the disk-zero target but still does not recover a singular inner factor;
3. modulus plus the full inner factor recovers the Hardy function once the outer normalization is fixed;
4. in a finite, boundary-regular setting, a much smaller phase mark -- the boundary winding number -- recovers only the **total zero multiplicity**, not the zero locations.

So the appropriate lift is task-relative: a zero-count endpoint needs less structure than a zero-divisor endpoint, and a zero-divisor endpoint needs less than full analytic-function recovery.

## Derivation

### Canonical factorization makes the lost coordinate explicit

For a nonzero Hardy function, standard inner--outer factorization gives

\[
f=I_fO_f,
\qquad
I_f=B_fS_f,
\tag{7}
\]

up to the usual unimodular normalization. The inner factor satisfies

\[
|I_f^*(e^{it})|=1
\quad\text{for a.e. }t,
\tag{8}
\]

and hence

\[
|f^*|=|O_f^*|
\quad\text{a.e.}
\tag{9}
\]

The outer factor is constructed from its boundary modulus. With the normalization `O_\rho(0)>0`, one may write

\[
O_\rho(z)
=
\exp\left(
\frac1{2\pi}
\int_0^{2\pi}
\frac{e^{it}+z}{e^{it}-z}
\log\rho(e^{it})\,dt
\right),
\tag{10}
\]

for the standard admissible `rho` arising from a nonzero Hardy function. Thus two normalized outer functions with the same boundary modulus coincide.

Now suppose `\mathcal M(f)=rho`. Factor `f=IO`. Equation `(9)` says `|O^*|=rho`, so the outer uniqueness just noted gives `O=O_\rho` up to a unimodular constant, which can be absorbed into `I`. Conversely every inner `I` satisfies `|I^*|=1` a.e., so `IO_\rho` lies in the same modulus fiber. This proves `(4)`.

The fiber description is stronger than merely saying that phase is absent. It identifies the exact quotient:

\[
H^p\setminus\{0\}
\xrightarrow{\ \mathcal M\ }
\{\text{admissible boundary magnitudes}\}
\]

collapses all admissible inner factors above a fixed outer representative.

### The zero divisor lies entirely in the Blaschke coordinate

The inner factor has the classical refinement

\[
I_f=c\,B_fS_f,
\qquad |c|=1,
\tag{11}
\]

where the Blaschke factor `B_f` has exactly the disk zeros of `f`, counted with multiplicity, and `S_f` is zero-free in the disk. The outer factor is also zero-free.

For `a in D`, let `b_a` be the normalized elementary Blaschke factor with zero at `a`. On the unit circle,

\[
|b_a(e^{it})|=1.
\tag{12}
\]

Therefore the pair

\[
f_0(z)=1,
\qquad
f_a(z)=b_a(z)
\tag{13}
\]

is a decisive matched control:

\[
\mathcal M(f_0)=\mathcal M(f_a)=1,
\tag{14}
\]

but `f_0` has no disk zero while `f_a` has a zero at `a`.

More generally, for any finite multiset

\[
Z=\{a_1,\ldots,a_m\}\subset\mathbb D
\]

with repetitions allowed, the finite Blaschke product

\[
B_Z=\prod_{j=1}^m b_{a_j}
\tag{15}
\]

satisfies

\[
\mathcal M(B_Z)=1
\tag{16}
\]

and has zero divisor exactly `Z`. Hence one single modulus fiber contains functions with arbitrary finite zero counts and arbitrary finite zero locations.

This proves a direct fiberwise no-go theorem. Let `D_0(f)` be any discriminator that changes when a finite Blaschke zero is inserted. If the admissible class contains both `f` and `Bf` for some such insertion, then

\[
\mathcal M(f)=\mathcal M(Bf),
\qquad
D_0(f)\ne D_0(Bf),
\tag{17}
\]

so `D_0` is not constant on the compression fiber. By the basic AF-001 criterion, no map from modulus data alone can recover `D_0` exactly.

The same obstruction applies to every further scalarization, positive functional, integral, moment, norm, or other observable that factors through `\mathcal M`: once `(17)` has occurred, post-processing cannot separate the collapsed pair.

## A task-relative lift hierarchy

The factorization also gives a clean example where there is no single meaningful notion of "the" missing information.

### Zero divisor

If the endpoint is only the disk zero divisor, the singular inner factor is irrelevant. Supplying `B_f` (equivalently, its zero multiset with multiplicities, modulo a unimodular normalization) alongside `\mathcal M(f)` is sufficient for that endpoint. Full boundary phase would be excessive.

### Full Hardy function

If the endpoint is the full analytic function, a zero-divisor mark is insufficient because different singular inner factors have the same modulus and the same disk zeros. Supplying the complete inner factor `I_f`, together with the normalized outer factor already determined by `\mathcal M(f)`, reconstructs `f` exactly.

Equivalently, where `f^*` is nonzero almost everywhere, the pair

\[
\left(|f^*|,\frac{f^*}{|f^*|}\right)
\tag{18}
\]

recovers the boundary function `f^*`; Hardy boundary uniqueness then recovers `f`. This is the full phase lift rather than the target-specific zero lift.

### Zero count only

There is an intermediate target. Restrict to functions in the disk algebra that are nonzero on the unit circle and have finitely many disk zeros. The argument principle gives

\[
N(f)
=
\operatorname{wind}\left(
\frac{f}{|f|}\Big|_{\mathbb T}
\right),
\tag{19}
\]

where `N(f)` is total disk-zero multiplicity. For a finite Blaschke product of degree `m`, this winding number is `m`.

Thus a single integer-valued phase statistic repairs the **zero-count** endpoint even though it does not locate the zeros. The functions `z^m` and an arbitrary degree-`m` finite Blaschke product have the same modulus and the same phase degree but can have completely different zero locations.

This yields a concrete strict hierarchy of endpoint needs:

\[
\text{boundary modulus}
\;<\;
\text{modulus + phase degree}
\;<\;
\text{modulus + Blaschke divisor}
\;<\;
\text{modulus + full inner factor},
\tag{20}
\]

where the ordering means increasing ability to recover the declared targets, not a universal bit-count comparison.

## Prior art and novelty assessment

All analytic ingredients are classical.

- Peter L. Duren, *Theory of H^p Spaces*, Academic Press, 1970 (Dover reprint 2000), is a standard source for Hardy-space boundary theory, inner--outer/canonical factorization, Blaschke products, and outer functions.
- John B. Conway, *Functions of One Complex Variable II*, Graduate Texts in Mathematics 159, Springer, 1995, DOI `10.1007/978-1-4612-0817-4`, Chapter 20, gives a standard treatment of Hardy spaces on the disk and factorization in the Nevanlinna/Hardy setting.
- José Ángel Peláez and Jouni Rättyä's surrounding literature and, more directly for the definitions used here, José Ángel Peláez/Girela-style surveys are not needed for the proof; an accessible primary expository reference is Daniel Girela, **"Inner Functions in Lipschitz, Besov, and Sobolev Spaces,"** *Abstract and Applied Analysis* (2011), Article ID 626254, DOI `10.1155/2011/626254`, which explicitly recalls that Blaschke products have unimodular boundary values, carry the zero sequence, and that an inner function factors into Blaschke and singular inner pieces.

No novelty is claimed for inner--outer factorization, Blaschke products, the argument principle, or reconstruction of an outer factor from boundary modulus.

The Arithmetic Fidelity contribution is the **compression audit** obtained by assembling these classical facts in the line's language: boundary modulus has an exactly identifiable fiber coordinate, the zero-bearing portion of that coordinate can vary arbitrarily while the retained object is unchanged, and different downstream endpoints require strictly different lifts. This is a reusable no-go test for proposals that impose absolute value, power, positivity, or modulus-only boundary data before a zero-sensitive claim.

AF-004 is related but not duplicate. AF-004 studies finite Fourier power-spectrum phase ambiguity and how higher-order correlations can repair it under nondegeneracy. AF-166 instead identifies a canonical infinite-dimensional analytic quotient: the complete Hardy inner factor is invisible to boundary magnitude, and the Blaschke subfactor is exactly the hidden zero divisor.

## Boundary conditions and falsification checks

- The theorem is about Hardy-space boundary-modulus compression. An arbitrary analytic function outside a Hardy/Smirnov-type class may not have the boundary values or canonical factorization used above.
- Equation `(4)` uses the standard admissibility conditions for a boundary modulus and a fixed normalization of the outer factor. It should not be read as saying that every positive measurable function is an `H^p` boundary modulus.
- For an infinite Blaschke product, unimodular boundary values are an almost-everywhere statement, not necessarily continuous pointwise boundary data. The finite matched controls `(13)--(16)` avoid this issue entirely.
- The singular inner factor is zero-free in the disk. It obstructs full-function recovery but does not change the disk zero divisor.
- The winding formula `(19)` requires the stated boundary regularity and nonvanishing boundary values. It is not asserted for a general `H^p` boundary function.
- A zero-divisor lift is sufficient only for the zero-divisor endpoint. It does not recover singular inner structure or the full analytic function.
- The no-go theorem requires the admissible family to contain the matched inner-factor alternatives. A concrete application may evade it by an independently proved constraint that fixes or forbids the relevant inner factors. Such a constraint is exactly the extra structure that must be exhibited; it cannot be inferred from modulus data itself.
- Multiplying by a finite Blaschke factor changes the analytic object while preserving its boundary modulus. This is a matched-control test, not a claim that every concrete arithmetic family is closed under Blaschke multiplication.
- No direct statement about the Riemann zeta or xi zero divisor follows. To use this audit in an RH-facing construction, one must first place the actual analytic object in a compatible disk/half-plane Hardy or Smirnov framework and verify that the proposed compression really factors through boundary modulus while the admissible control family remains valid.

## Cross-line consequence

This finding gives a precise mechanism behind the broad warning that positivity or absolute-value operations can erase the discriminator they are later asked to explain. If a `weil_positivity`, `prime_lattice`, `prime_circle`, or other candidate passes from a complex analytic carrier to boundary modulus/power data and only afterwards asks for zero-sensitive structure, the immediate audit question is now exact:

> Is the candidate's admissible analytic class rigid enough to fix the inner/Blaschke factor from information not contained in the modulus?

If not, a Blaschke-matched control proves that the zero-sensitive endpoint has already been lost. If only zero count is needed, a winding/phase-degree mark may suffice; if the full divisor is needed, substantially richer marking is unavoidable.

This is a clue-generation principle for the concrete lines, not evidence that any one of their current objects satisfies the required Hardy-space hypotheses.
