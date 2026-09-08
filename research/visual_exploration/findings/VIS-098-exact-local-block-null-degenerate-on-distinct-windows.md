# VIS-098 — exact local-block reassembly is singleton when delay windows are distinct

## Claim

Let

`a=(a_1,...,a_N)`

be a finite real sequence, fix `1<=m<N`, and write its consecutive delay windows as

`w_i=(a_i,...,a_(i+m-1))`, `1<=i<=N-m+1`.

Assume the windows `w_i` are pairwise distinct. Then the unordered multiset of length-`(m+1)` blocks, together with the first delay window, uniquely determines the complete ordered window path and hence the original sequence.

Equivalently, the static transition multigraph `D_m(a)` from `VIS-094` has exactly one Eulerian trail beginning at the supplied first window. Under pairwise window distinctness, `D_m(a)` is just the directed simple path

`w_1 -> w_2 -> ... -> w_(N-m+1)`.

Therefore a **nontrivial exact local-block-preserving reassembly control requires repeated delay-window values and genuine Eulerian ambiguity**. Repeated windows are necessary for such ambiguity, though not sufficient: a graph with repeats may still have a unique compatible Eulerian trail.

For a finite real vector drawn from any law absolutely continuous with respect to Lebesgue measure on `R^N`, pairwise equality of two distinct fixed-length delay windows has probability zero. Thus, for generic continuous data in this precise measure-theoretic sense, the exact `(m+1)`-block-preserving reassembly null is almost surely a singleton.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DE-BRUIJN/EULERIAN SPECIALIZATION + NEGATIVE NULL-DEGENERACY CONTROL + NO-NOVELTY-CLAIM`.

This is not a statement that zeta-zero gaps are random or that their delay windows are known to be pairwise distinct. Its consequence is procedural and mathematical: before using an exact local-block-preserving ensemble to test a higher-order path statistic, one must first prove or check that the admitted exact block inventory actually permits more than one compatible traversal.

## 1. Distinct windows force a directed simple path

By `VIS-094`, each length-`(m+1)` block

`(x_1,...,x_(m+1))`

is exactly the directed transition

`(x_1,...,x_m) -> (x_2,...,x_(m+1))`.

Hence the unordered `(m+1)`-block multiset is equivalent to the directed edge-occurrence multiset

`{ w_i -> w_(i+1) : 1<=i<=N-m }`.

If the `w_i` are pairwise distinct, no vertex appears at two different positions in the original path. Consequently:

- `w_1` has indegree `0` and outdegree `1`;
- `w_(N-m+1)` has indegree `1` and outdegree `0`;
- every intermediate `w_i` has indegree `1` and outdegree `1`.

Moreover each outgoing edge of an intermediate vertex is the unique edge `w_i -> w_(i+1)`. Starting from `w_1`, there is therefore exactly one legal next edge, then exactly one legal edge from its head, and so on until the terminal window. The edge multiset itself reconstructs the unique ordered chain.

The original scalar sequence follows immediately: `w_1` supplies `a_1,...,a_m`, and each successive head window supplies the next scalar coordinate as its final component.

Thus the exact block-preserving control class contains only the observed sequence whenever all delay windows are distinct.

## 2. Eulerian ambiguity needs a collision in the quotient graph

`VIS-094` identifies the information discarded by a static transition graph as the distinguished Eulerian traversal of its edge occurrences. The present result sharpens the admission boundary for exploiting that loss.

If all value-quotiented vertices are distinct, there is no traversal choice to lose. Alternative Eulerian assemblies become possible only after two or more window occurrences collapse to the same vertex value, creating the possibility of multiple entrance/exit pairings or cycle reorderings. A repeated vertex is only a necessary condition: degree constraints or the surrounding graph can still force one Eulerian trail.

This explains why the explicit collision in `VIS-097` is structurally special rather than generic. For its two `m=3` witness sequences, the ten three-windows occupy only six distinct values. In particular `000`, `001`, and `100` repeat. Those repeated base windows support the two closed local cycles whose order can be swapped while preserving the complete length-four block inventory; the level-four area-area commutator then detects that swapped assembly.

The chronology capacity proved by `VIS-097` is therefore real, but its exact matched-null geometry relies on precisely the type of repeated-window structure absent from a generic continuous delay path.

## 3. Generic continuous data make the exact null singleton

Let `A=(A_1,...,A_N)` have a joint distribution absolutely continuous with respect to Lebesgue measure on `R^N`. For fixed distinct indices `i<j`, the event

`W_i=W_j`

imposes the coordinate equalities

`A_(i+r)=A_(j+r)`, `0<=r<m`.

At least one of these is a nontrivial linear equality between distinct coordinates, so the event lies in a proper affine-linear subset of `R^N` and has Lebesgue measure zero. There are only finitely many pairs `(i,j)`. A finite union of these collision events therefore also has probability zero.

Hence almost surely all fixed-`m` delay windows are distinct, and by the preceding theorem the exact `(m+1)`-block-preserving Eulerian reassembly ensemble contains only the original traversal.

This genericity statement is deliberately limited. The unfolded gaps between Riemann zeros form a deterministic arithmetic sequence, not a sample from an assumed absolutely continuous law. Numerically distinct floating-point or high-precision gap triples do not prove exact mathematical noncollision either. For a concrete zeta dataset, exact or quantized collision structure must be stated at the actual representation being tested.

## 4. Consequence for the open level-four source-specificity test

The accepted `CLUE-zeta-critical-strip-multiscale-geometry` currently asks for a three-delay level-four statistic to be tested against controls preserving the first/last three-windows and the complete unordered length-four-block multiset. `VIS-097` shows why that is the right **information quotient** when such a control is nondegenerate. The present result shows that exact preservation is not automatically a usable **ensemble**.

Before evaluating any source-specific fourth-level signature statistic, apply a null-admission gate:

1. form the value-quotiented three-window transition multigraph of the source data at the exact representation being used;
2. determine whether the fixed endpoints and exact edge-occurrence multiset admit more than one Eulerian trail;
3. only if more than one traversal exists may exact local-four-block-preserving reassembly provide a nontrivial matched ensemble.

If the exact graph has a unique trail, one must change the null rather than pretend an exact reassembly ensemble exists. Possible replacements include a pre-registered quantization/coarsening that deliberately creates repeated states, an approximate block-matching criterion, a distributional or moment-matched local-block model, or a generative higher-order point-process control.

Those replacements are mathematically different controls. Their tolerance, binning, state identification, or model class can itself create or erase a level-four signature effect and must therefore be fixed before confirmation. In particular, the exact equality conclusions of `VIS-096` no longer transfer automatically when the control preserves local blocks only approximately; any resulting lower-level or local-block leakage must be measured explicitly.

This does not kill the level-four route. It sharpens its next question from “does level four differ from an exact block-preserving shuffle?” to “can one construct a **nondegenerate, pre-registered matched null** that removes the admitted local information without either fixing the entire path or introducing enough approximation freedom to manufacture the residual?”

## 5. Prior art and novelty assessment

The de Bruijn/Eulerian reconstruction viewpoint is classical. Pavel A. Pevzner, Haixu Tang, and Michael S. Waterman, **An Eulerian path approach to DNA fragment assembly**, *Proceedings of the National Academy of Sciences* 98:17 (2001), 9748–9753, DOI `10.1073/pnas.171285098`, represents fixed-length words by prefix/suffix transitions and explains assembly ambiguity through alternative entrance/exit pairings around repeats. Modern assembly reviews likewise describe unambiguous sequence as nonbranching graph paths and repeats as the source of branch structure.

No novelty is claimed for the graph fact that a directed simple path has one Eulerian traversal, for de Bruijn reconstruction, or for the measure-zero genericity of exact equality under an absolutely continuous law.

The Mathia-specific contribution is the control audit: after `VIS-097` opened level four as a genuine chronology carrier, the seemingly natural exact local-four-block-preserving source-specificity null can collapse to a singleton on continuous-valued delay data. This is a necessary admission check before interpreting any higher-order signature separation as source-specific evidence.

## Boundary and falsification

The pairwise-distinct-window hypothesis is sufficient, not necessary, for uniqueness. Repeated windows do not imply multiple Eulerian trails; one must inspect the actual directed multigraph and endpoint constraints.

The finding does not establish that:

- exact three-window collisions never occur in the deterministic zeta gap sequence;
- a finite numerical representation with no observed equal triples proves mathematical noncollision;
- quantized or approximate local-block-preserving controls are invalid;
- a generative control matching lower-order spectral statistics cannot test level-four source specificity;
- fourth-level path signatures are useless or reducible to local blocks;
- the explicit `VIS-097` collision is defective. On the contrary, its repeated windows are exactly what makes its alternative Eulerian assembly possible.

Falsify the main theorem by giving a finite sequence with pairwise distinct fixed-`m` delay windows for which the exact directed `(m+1)`-block edge multiset and first window admit two different Eulerian traversals. Such an example would contradict the one-outgoing-edge induction above.

Falsify the genericity corollary by exhibiting an absolutely continuous joint law on `R^N` assigning positive probability to equality of two distinct delay windows.

## Visual consequence

No canonical PNG is retained. The useful visual picture is a graph-theoretic boundary: a chain of distinct delay states has no reassembly freedom, while repeated states can create branch/cycle structure and hence multiple compatible traversals. The exact statement is clearer and stronger than a rendered example.

## Research consequence

The level-four branch remains open, but its next decisive test must begin with **matched-null nondegeneracy**. The exact local-four-block quotient from `VIS-096`/`VIS-097` is a valid theoretical information boundary, not automatically a practical resampling scheme for continuous-valued arithmetic data.

A source-specific level-four claim is meaningful only after the control construction is shown to have genuine alternative realizations and after any coarsening or approximate matching needed to obtain them is itself audited for leakage and representation dependence. This narrows `CLUE-zeta-critical-strip-multiscale-geometry` without resolving it.