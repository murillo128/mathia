# AF-134 — Backward witness saturation is the minimal compositional lift

**Status:** `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `MINIMAL-LIFT`, `COMPOSITION-GATE`, `OBSERVABILITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-133 shows that stagewise fidelity is not compositional merely because each stage admits a small recovery defect. The recovery used at one stage must also respect the information quotient declared by the next stage. This leaves a constructive question: given a chain of fixed recoveries and fixed baseline witness classes, what is the **smallest** enlargement of those witness classes that makes the chain compositional?

For finite sets `X_0,...,X_n`, let

\[
H_i:=\left\{\mu\in\mathbb R^{X_i}:\sum_x\mu(x)=0\right\}
\]

be the zero-mass residual spaces. Let each

\[
A_i\subset H_i^*
\]

be a fixed nonempty compact convex centrally symmetric witness body containing `0`, with induced seminorm

\[
p_i(\mu):=h_{A_i}(\mu)=\max_{f\in A_i}\langle\mu,f\rangle.
\tag{1}
\]

Let prescribed Markov recoveries

\[
R_i:X_i\rightsquigarrow X_{i-1},\qquad i=1,\ldots,n,
\]

induce linear residual maps

\[
L_i:H_i\to H_{i-1},\qquad L_i\mu=\mu R_i,
\tag{2}
\]

and dual pullbacks `L_i^*:H_{i-1}^*\to H_i^*`.

Define the **backward witness saturation** recursively by

\[
B_0:=A_0,
\qquad
B_i:=\operatorname{conv}\!\left(A_i\cup L_i^*B_{i-1}\right).
\tag{3}
\]

Then:

1. Every `B_i` is again a nonempty compact convex centrally symmetric witness body containing `0`.
2. Every prescribed recovery becomes nonexpansive in the saturated witness geometries:
   \[
   L_i^*B_{i-1}\subseteq B_i,
   \qquad
   h_{B_{i-1}}(L_i\mu)\le h_{B_i}(\mu).
   \tag{4}
   \]
   Equivalently, the AF-133 witness-transport coefficient of `R_i` is at most `1` after saturation.
3. The saturation is **minimal by inclusion**. If witness bodies `C_i` satisfy
   \[
   A_i\subseteq C_i
   \quad\text{and}\quad
   L_i^*C_{i-1}\subseteq C_i
   \tag{5}
   \]
   for every `i`, then
   \[
   B_i\subseteq C_i
   \qquad\text{for every }i.
   \tag{6}
   \]
   Thus `(3)` is the smallest normalized witness enrichment that retains every baseline observable while making the declared recovery chain compositional with coefficient at most one.
4. Writing
   \[
   q_i(\mu):=h_{B_i}(\mu),
   \]
   the saturation has the exact seminorm recursion
   \[
   \boxed{
   q_i(\mu)=\max\left\{p_i(\mu),\ q_{i-1}(L_i\mu)\right\}.
   }
   \tag{7}
   \]
   Hence
   \[
   \boxed{
   q_i(\mu)
   =
   \max_{0\le j\le i}
   p_j\!\left(L_{j+1}L_{j+2}\cdots L_i\mu\right),
   }
   \tag{8}
   \]
   where the term `j=i` uses the identity map.
5. Equivalently, the saturated witness body is
   \[
   \boxed{
   B_i
   =
   \operatorname{conv}\!\left(
   \bigcup_{j=0}^{i}
   L_i^*L_{i-1}^*\cdots L_{j+1}^*A_j
   \right).
   }
   \tag{9}
   \]
   Thus a witness required upstream is transported backward through every recovery on which later reconstruction depends.
6. The remaining blind subspace is exactly
   \[
   \boxed{
   \ker q_i
   =
   \bigcap_{j=0}^{i}
   \left(L_{j+1}\cdots L_i\right)^{-1}
   \ker p_j.
   }
   \tag{10}
   \]
   Consequently the saturated representation has no nonzero blind residual iff
   \[
   \operatorname{span} B_i=H_i^*.
   \tag{11}
   \]
   If `(11)` holds, **every** admissible compositional enrichment satisfying `(5)` is already nondegenerate on `H_i`; no coarser witness quotient can support that prescribed recovery chain while retaining the baseline witnesses.
7. For fixed recoveries, saturation is a closure operation on witness families: it is extensive, monotone, and idempotent.

The same construction gives a weighted version. If positive caps `c_i` are prescribed and one only requires witness-transport coefficient at most `c_i`, the minimal bodies are

\[
B_0^{(c)}=A_0,
\qquad
B_i^{(c)}
=
\operatorname{conv}\!\left(
A_i\cup c_i^{-1}L_i^*B_{i-1}^{(c)}
\right),
\tag{12}
\]

with seminorm recursion

\[
q_i^{(c)}(\mu)
=
\max\left\{
p_i(\mu),
c_i^{-1}q_{i-1}^{(c)}(L_i\mu)
\right\}.
\tag{13}
\]

Thus the cost of demanding a quantitatively regular inverse propagates backward multiplicatively through the chain. The result is deliberately relative to **fixed normalized baseline witness bodies and fixed recoveries**; without those constraints, arbitrary rescaling or changing the inverse would make a claim of minimality meaningless.

## Derivation

### Convex-hull support functions give the exact recursion

Because `A_i` and `B_{i-1}` are compact, convex, centrally symmetric, and contain `0`, so is `L_i^*B_{i-1}`. The convex hull of the union has the same properties, proving part 1.

For any two nonempty compact sets `K_1,K_2`, linear maximization over their convex hull gives

\[
h_{\operatorname{conv}(K_1\cup K_2)}
=
\max\{h_{K_1},h_{K_2}\}.
\tag{14}
\]

Moreover

\[
h_{L_i^*B_{i-1}}(\mu)
=
\max_{f\in B_{i-1}}\langle\mu,L_i^*f\rangle
=
\max_{f\in B_{i-1}}\langle L_i\mu,f\rangle
=q_{i-1}(L_i\mu).
\tag{15}
\]

Equations `(3)`, `(14)`, and `(15)` give `(7)`. In particular

\[
q_{i-1}(L_i\mu)\le q_i(\mu),
\]

which is the primal seminorm form of `(4)` and exactly the AF-133 condition `\kappa(R_i)\le1`.

Iterating `(7)` gives `(8)`. Applying the dual recursion instead gives `(9)`.

### Minimality is forced one stage at a time

Let `(C_i)` satisfy `(5)`. Since `B_0=A_0\subseteq C_0`, assume inductively that `B_{i-1}\subseteq C_{i-1}`. Then

\[
L_i^*B_{i-1}
\subseteq
L_i^*C_{i-1}
\subseteq
C_i.
\tag{16}
\]

Also `A_i\subseteq C_i`. Since `C_i` is convex,

\[
\operatorname{conv}(A_i\cup L_i^*B_{i-1})
\subseteq C_i,
\]

which is `B_i\subseteq C_i`. Induction proves `(6)`.

The weighted statement is identical after replacing the compatibility condition by

\[
L_i^*C_{i-1}\subseteq c_iC_i.
\tag{17}
\]

Any such `C_i` must contain `c_i^{-1}L_i^*B_{i-1}^{(c)}` as well as `A_i`, forcing `(12)`.

### The blind space is an observability intersection

A maximum of nonnegative seminorms vanishes exactly when every term vanishes. Applying this to `(8)` yields `(10)`.

Because `q_i=h_{B_i}` and `B_i` is centrally symmetric,

\[
\ker q_i
=
\{\mu:\langle\mu,f\rangle=0\ \forall f\in B_i\}
=(\operatorname{span}B_i)^\perp.
\tag{18}
\]

In finite dimension `(18)` is `{0}` iff `\operatorname{span}B_i=H_i^*`, proving `(11)`.

This is the same structural pattern as an observability test. Repeatedly transported output functionals eliminate the state directions invisible to every observation. Here the transported witness classes eliminate residual directions that would otherwise be silently discarded even though a later recovery needs them.

### Saturation is a closure operation

Let `\operatorname{Sat}_R(A)=B` denote recursion `(3)` for fixed recoveries. Extensivity follows from `A_i\subseteq B_i`. Monotonicity follows by induction from monotonicity of linear images and convex hull. For idempotence, use `(4)`: applying the same recursion to `B` gives

\[
\operatorname{conv}(B_i\cup L_i^*B_{i-1})=B_i,
\]

so `\operatorname{Sat}_R(\operatorname{Sat}_R(A))=\operatorname{Sat}_R(A)`.

The fixed points are therefore exactly the witness families already closed under every required backward pullback.

## AF-133 counterexample: exact repair restores the forgotten distinction

AF-133 uses

\[
X=\{0,1,2\},
\qquad
Y=\{a,b,c\},
\]

with total-variation witness geometry on `X` and the degenerate witness seminorm

\[
p_Y(\nu)=|\nu(c)|
\]

on `Y`, which forgets redistribution between `a` and `b`. Its exact raw recovery is the bijection

\[
a\mapsto0,
\qquad
b\mapsto1,
\qquad
c\mapsto2.
\]

Pulling the full total-variation witness body on `X` back through this bijection gives the full total-variation witness body on `Y`. The baseline `|\nu(c)|` witness body lies inside that body, so `(3)` yields precisely the full total-variation witness geometry on `Y`.

Thus the abstract minimal-lift theorem makes the AF-133 obstruction exact: **for that recovery, compositional repair cannot preserve the quotient that identifies `a` and `b`; the smallest admissible repair restores the very distinction the quotient erased.** This is not merely one convenient side channel. Minimality says that every witness enrichment making the exact inverse nonexpansive and retaining the baseline tests must contain those transported upstream witnesses.

## Consequences for Arithmetic Fidelity

AF-133 supplied a compatibility test for a proposed recovery. AF-134 supplies the converse design calculation: when compatibility fails, it computes the least witness enrichment that would repair the declared chain.

This separates three outcomes that should not be conflated:

- **cheap repair:** `B_i` remains strongly degenerate, so only a small additional quotient-visible structure is required;
- **expensive repair:** `B_i` becomes a norm but remains quantitatively weak, so all residual directions must survive even if with poor conditioning;
- **quotient annihilation:** the transported witnesses already span the full dual and the proposed chain cannot coexist with any nontrivial blind quotient at that stage.

The theorem therefore gives a falsifiable minimal-lift audit for a concrete compression pipeline. One should not ask vaguely whether marking, phase, provenance, or boundary information might help. Fix the downstream witnesses and the recovery actually needed upstream, pull those witnesses backward, and test whether the resulting saturation is a modest enrichment or effectively reconstructs the discarded object.

The result does **not** choose a canonical witness family, a canonical recovery, or a prime-specific discriminator. Those remain category-specific mathematical questions. In particular, a different recovery may have a much smaller saturation, and allowing arbitrary witness renormalization can change numerical transport coefficients. The theorem is a conditional exact calculation once those choices are independently justified.

## Prior art and novelty assessment

No novelty claim is made for the functional-analytic ingredients or the closure construction.

- Giulia De Pasquale, Kevin D. Smith, Francesco Bullo, and Maria Elena Valcher, **“Dual Seminorms, Ergodic Coefficients and Semicontraction Theory,”** *IEEE Transactions on Automatic Control* 69(5), 3040–3053 (2024), DOI `10.1109/TAC.2023.3302788`. Role: induced matrix seminorms, invariant kernels/quotients, and contraction coefficients; this is the closest direct prior art for AF-133's transport coefficient and the nonexpansive condition used here.
- H. H. Schaefer and M. P. Wolff, ***Topological Vector Spaces***, 2nd ed., Graduate Texts in Mathematics 3, Springer (1999), DOI `10.1007/978-1-4612-1468-7`. Role: standard locally convex-space language in which families of seminorms generate the coarsest topology making the declared observations continuous. AF-134's max/pullback recursion is the finite-dimensional quantitative analogue of adjoining the seminorms needed to make specified linear maps continuous/nonexpansive.
- R. Tyrrell Rockafellar, ***Convex Analysis***, Princeton University Press (1970), especially §13 on support functions. Role: standard support-function/convex-set duality underlying `(14)`–`(15)` and the representation of seminorms by symmetric convex witness bodies.
- R. E. Kalman, **“Mathematical Description of Linear Dynamical Systems,”** *Journal of the Society for Industrial and Applied Mathematics, Series A: Control* 1(2), 152–192 (1963), DOI `10.1137/0301010`. Role: classical observability/minimal-realization precedent for the principle that only the observable quotient is determined by outputs and that iterated transported observations characterize the retained state. Equation `(10)` is an abstract finite-chain analogue of an unobservable-subspace intersection, not a new observability theorem.

The exact formulas `(3)`–`(13)` are elementary consequences of these standard structures. Their Arithmetic Fidelity value is organizational and diagnostic: they turn AF-133's qualitative quotient-compatibility obstruction into a **minimal repair calculation** for a staged compression pipeline. Any future novelty claim must come from a nontrivial, intrinsically justified witness/recovery category or from an arithmetic application, not from the saturation theorem itself.

## Decisive audit for future applications

Given a proposed chain of compressions and recoveries:

1. freeze the witness classes that correspond to the actual downstream decisions/observables rather than choosing them after seeing the answer;
2. justify the recovery maps independently of the desired discriminator;
3. compute the saturation `(3)` or weighted saturation `(12)`;
4. inspect `(10)` and `(11)` to determine exactly which blind directions remain;
5. kill a claimed lightweight repair if the saturation already spans the full dual or otherwise contains essentially the information the compression was supposed to discard.

For the eventual rational-prime application, the useful case is not merely that a side mark exists. The mark must arise from an independently admissible category, and its backward saturation through the intended analytic/spectral pipeline must preserve the rational-prime discriminator without degenerating into a disguised copy of the original prime data.