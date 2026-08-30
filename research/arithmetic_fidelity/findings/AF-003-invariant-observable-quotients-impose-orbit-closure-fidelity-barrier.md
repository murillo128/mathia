# AF-003 — Invariant-observable quotients impose an orbit-closure fidelity barrier

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` be a set, let

\[
T:X\to Y
\]

be retained data, let

\[
d:X\to D
\]

be the discriminator whose recovery is being tested, and let `\mathcal A` be a class of admissible observables on `X`. Write

\[
\Phi_{\mathcal A}(x)=(f(x))_{f\in\mathcal A}
\]

for the joint evaluation map into the product of the observable codomains. Then:

1. any lift assembled entirely from observables in `\mathcal A`, or from functions of their joint values, factors through `\Phi_{\mathcal A}`;
2. therefore such lifts can recover `d` from `T` only if
   \[
   T(x)=T(x'),\qquad \Phi_{\mathcal A}(x)=\Phi_{\mathcal A}(x')
   \Longrightarrow d(x)=d(x');
   \]
3. allowing the whole family `\mathcal A` makes this condition sufficient as well: `d` is then exactly recoverable from `(T,\Phi_{\mathcal A})` if and only if it is constant on those joint fibers.

Thus every constrained-observable lift problem has a **maximal admissible quotient**: before optimizing or selecting particular marks, one can ask whether the entire admissible observable class already separates the discriminator conflicts. If it does not, no subfamily, nonlinear recombination, or downstream post-processing of those observables can repair the loss.

For an affine algebraic variety `X` over an algebraically closed field with an action of a reductive algebraic group `G`, take

\[
\mathcal A=k[X]^G,
\]

the invariant regular functions. The joint observable quotient is the affine GIT quotient

\[
\pi:X\to X//G=\operatorname{Spec} k[X]^G.
\]

Classical geometric invariant theory gives a sharper description of its fibers: every fiber of `\pi` contains exactly one closed `G`-orbit, and two points have the same invariant values precisely when their orbit closures contain the same closed orbit. Consequently, invariant regular observables do **not** in general preserve orbit provenance; they preserve only the corresponding closed-orbit / S-equivalence class.

Hence, if a discriminator distinguishes two points `x,x'` such that

\[
T(x)=T(x'),\qquad \pi(x)=\pi(x'),\qquad d(x)\ne d(x'),
\]

then no lift constructed solely from invariant regular observables can recover `d`. Adding more invariant polynomials cannot help, because the full invariant ring has already been used.

## Derivation

For the general observable-family statement, define the equivalence relation

\[
x\sim_{\mathcal A}x'
\iff
f(x)=f(x')\quad\text{for every }f\in\mathcal A.
\]

Every admissible coordinate `f\in\mathcal A` is constant on `\sim_{\mathcal A}`-classes. Any tuple of such coordinates, and any function of that tuple, remains constant on the same classes. Therefore if `x\sim_{\mathcal A}x'` and `T(x)=T(x')`, no such lift can distinguish the pair. By AF-001, exact recovery of `d` is impossible whenever the pair has different `d`-values.

Conversely, if `d` is constant whenever both `T` and `\Phi_{\mathcal A}` agree, then AF-001 applied to the map

\[
(T,\Phi_{\mathcal A}):X\to Y\times\prod_{f\in\mathcal A}A_f
\]

shows that `d` factors through this joint retained representation. This proves that `\Phi_{\mathcal A}` is the maximal information obtainable when the admissible marks are exactly functions of `\mathcal A`.

The invariant-theory specialization is classical. For a reductive group acting on affine `X`, finite generation of `k[X]^G` provides the affine categorical quotient. Its universal property says every invariant regular morphism factors through `\pi`; geometrically, the quotient classifies closed orbits rather than arbitrary orbits. Each quotient fiber has one closed orbit, and nonclosed orbits in the same fiber specialize toward that closed orbit. Thus the equivalence relation induced by all invariant regular functions is generally coarser than ordinary orbit equivalence.

## Exact model: a one-dimensional torus on the plane

Let

\[
G=\mathbb G_m
\]

act on `X=\mathbb A^2` by

\[
t\cdot(x,y)=(tx,t^{-1}y).
\]

A monomial `x^a y^b` has weight `a-b`, so it is invariant exactly when `a=b`. Therefore

\[
k[x,y]^G=k[xy]
\]

and the quotient map is simply

\[
\pi(x,y)=xy.
\]

Consider

\[
p=(1,0),\qquad q=(0,1),\qquad o=(0,0).
\]

They lie in three distinct `G`-orbits, but

\[
\pi(p)=\pi(q)=\pi(o)=0.
\]

The orbits of `p` and `q` are not closed; both have `o` in their Zariski closures, while `{o}` is the unique closed orbit in the quotient fiber `\pi^{-1}(0)`.

Therefore every invariant polynomial takes the same value on `p`, `q`, and `o`. If retained data `T` also agrees on these points, no invariant-polynomial lift can recover any discriminator that distinguishes, for example, the two axis branches or a nonzero branch point from the origin.

This is stronger than observing that one particular invariant failed. The **entire invariant algebra** fails simultaneously, and the failure is forced by the categorical quotient.

## Why this matters for Arithmetic Fidelity

AF-001 showed that arbitrary marks make minimal lift recovery trivial. AF-002 showed that a fixed finite observable library reduces to classical discernibility/reduct theory. The present result gives the next structurally constrained case: when admissibility is defined by a symmetry principle, the first question is not which invariant coordinates to select but what quotient the whole invariant observable class represents.

This yields a useful two-stage audit:

1. identify the maximal admissible observable quotient `\Phi_{\mathcal A}` or its mathematical replacement;
2. test discriminator constancy on its fibers before attempting minimal generators, sparse selections, coordinates, or downstream operators.

If the discriminator already varies inside one maximal-admissible fiber, the candidate symmetry class is dead for exact recovery. Optimization inside the class is irrelevant.

The GIT example also separates two notions that can otherwise be conflated. **Symmetry forgetting** identifies points intentionally related by the group action, while **orbit-closure collapse** may additionally identify distinct nonclosed orbits because invariant regular functions see only their common closed-orbit degeneration. A claim that an invariant or canonical representation preserves "all structure except gauge" is therefore false in this category unless the relevant objects lie in a locus where quotient fibers are actual orbits, such as an appropriate closed/stable locus.

For future arithmetic applications this gives a precise warning. If an RH construction first passes to an invariant/canonical quotient, one must determine the quotient's actual fibers, not merely name the symmetry being removed. Prime-sensitive provenance can be lost because two genuinely different upstream configurations have the same categorical limit, even when neither is literally a gauge transform of the other.

## Prior art and novelty assessment

The affine quotient

\[
X//G=\operatorname{Spec}k[X]^G
\]

and its universal property are standard invariant theory. For reductive actions, the theorem that every quotient fiber contains a unique closed orbit, with nonclosed orbits identified according to their closed-orbit degeneration, is standard geometric invariant theory; it is a central reason that a categorical quotient is not generally an orbit space.

Mumford, Fogarty, and Kirwan's *Geometric Invariant Theory* is the standard reference. Standard expositions of invariant theory likewise emphasize that knowledge of the invariant ring does not in general give complete information about nonclosed orbits and must be supplemented by orbit-closure and stabilizer data.

No novelty is claimed for these GIT results or for the elementary joint-evaluation lemma. The Mathia-specific contribution is their placement as an **Arithmetic Fidelity admissibility test**: a structurally constrained lift family should first be replaced by its maximal observable quotient, and failure at that level is a no-go theorem for every lift built inside the same observable class.

## Boundaries and failure modes

- The general observable-family statement is exact but deliberately abstract; mathematical content comes from deriving a nontrivial admissible family and understanding its induced quotient.
- The algebraic specialization assumes an affine algebraic setting and a reductive group so that the standard finite-generation and quotient theorems apply in the stated form.
- Equality of invariant-polynomial values should not be conflated with equality of orbits. The obstruction is specifically the stronger orbit-closure equivalence present in the categorical quotient.
- On loci where all relevant orbits are closed and the quotient is geometric, invariant observables may lose only the intended symmetry orbit. The extra orbit-closure obstruction then disappears.
- Allowing non-invariant, semi-invariant, marked, stacky, stabilizer, boundary, or other enriched data changes the admissible family and may refine the quotient. Such an enrichment is genuinely additional information and must be justified independently.
- This finding treats exact deterministic recovery. Approximate discrimination or statistical decision value can survive even when exact invariant recovery fails.
- The result does not establish that any existing Mathia RH line actually performs a GIT quotient; that must be proved inside the concrete line before applying this obstruction.

## Decisive audit test

For any proposed symmetry-constrained or "canonical invariant" lift:

1. specify the full admissible observable class `\mathcal A` independently of the target discriminator;
2. identify, exactly when possible, the equivalence relation induced by equality of all observables in `\mathcal A`;
3. search for a matched pair with equal retained `T`-data and equal maximal-admissible observable data but different discriminator values.

One such pair rules out **every** lift constructed from that observable class, not merely the particular coordinates tried so far.

## Consequence for the line

Treat the **maximal admissible quotient** as the object to analyze before minimal lifts. This replaces repeated feature-by-feature experiments with a stronger structural question: what equivalence relation is forced by the entire admissibility principle?

Invariant theory supplies the first nontrivial model. It shows that a mathematically natural requirement such as symmetry invariance can produce a quotient that forgets more than explicit group labels: nonclosed orbit provenance may collapse to a common closed representative. Future work should look for analogous maximal-observable quotients induced by locality, naturality, positivity, spectralization, or operator-category restrictions and determine whether their fibers admit similarly decisive fidelity barriers.
