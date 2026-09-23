# WI-416 — Oracle Blaschke targeting has zero finite-TV infimum on discrete defect sets

**Status:** `CLASSICAL-PRIOR-ART + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-409](./WI-409-bsy-already-supplies-summable-positive-horizontal-defect.md), [WI-411](./WI-411-vertical-translations-obey-height-area-budget.md), [WI-415](./WI-415-count-quantum-height-depth-budget-is-t-over-delta.md).

## Claim

WI-415 proved that a source-independent finite-TV mixture of translated Blaschke charges pays an asymptotically sharp `T/delta` budget when it must deliver a fixed count quantum throughout a positive-area height-depth rectangle. It left one explicit escape: an oracle-like mixture adapted only to the discrete exceptional ordinates can evade a continuum area estimate.

That escape is not merely outside the proof of WI-415. In the unconstrained target-adaptive model its TV coercivity collapses completely.

For

\[
q_{a,b}(\gamma,d)
=
\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\qquad a,d>0,
\tag{1}
\]

let

\[
E=\{(\gamma_j,d_j):1\le j\le N\}
\subset \mathbb R\times(0,\infty)
\tag{2}
\]

be any finite target set. For every required quantum `Q>0` and every `epsilon>0`, there exists a **positive finite atomic measure**

\[
\nu=\sum_{j=1}^N w_j\,\delta_{(a_j,b_j)},
\qquad
\|\nu\|_{\rm TV}=\sum_j w_j<\varepsilon,
\tag{3}
\]

such that every individual kernel value in the finite sum is finite and

\[
Q_\nu(\gamma_j,d_j)
:=\int q_{a,b}(\gamma_j,d_j)\,d\nu(a,b)
\ge Q
\qquad (1\le j\le N).
\tag{4}
\]

Consequently

\[
\boxed{
\inf\left\{
\|\nu\|_{\rm TV}:
\nu\ge0,\ Q_\nu\ge Q\text{ on }E
\right\}=0.
}
\tag{5}
\]

The conclusion remains true if exact probe-target coincidence is forbidden. Therefore no positive source-budget lower bound can be recovered from the **number, spacing, local density, or Riemann--von Mangoldt count of a finite discrete exceptional set alone** when translated Blaschke centers may be chosen after seeing that set.

This is a barrier for an oracle-adaptive detector class, not a statement about source-generated zeta observables. It does not exclude any zero and does not imply RH.

## 1. Exact finite-set construction

Choose arbitrary weights

\[
w_j>0,
\qquad
\sum_{j=1}^N w_j<\varepsilon,
\tag{6}
\]

and put

\[
L_j=\frac{Q}{w_j}.
\tag{7}
\]

At equal vertical center, the single-probe response is

\[
q_{a,\gamma_j}(\gamma_j,d_j)
=
\log\frac{a+d_j}{|a-d_j|},
\tag{8}
\]

which diverges as `a -> d_j`. Hence choose `a_j>0`, distinct from every target depth `d_k`, so close to `d_j` that

\[
\log\frac{a_j+d_j}{|a_j-d_j|}>L_j.
\tag{9}
\]

The exclusion of the finitely many values `d_k` costs nothing: every punctured neighborhood of `d_j` contains admissible choices.

We now also move the vertical center away from the target, so the construction does not use the singular point `(a,b)=(d_j,gamma_j)`. Set

\[
R_j=e^{2L_j}>1.
\tag{10}
\]

Because of (9),

\[
(a_j+d_j)^2>R_j(a_j-d_j)^2.
\tag{11}
\]

Therefore

\[
r_j^2
:=
\frac{(a_j+d_j)^2-R_j(a_j-d_j)^2}{R_j-1}
>0.
\tag{12}
\]

Take, for example,

\[
b_j=\gamma_j+r_j.
\tag{13}
\]

Substituting (12) into (1) gives exactly

\[
q_{a_j,b_j}(\gamma_j,d_j)=L_j.
\tag{14}
\]

Thus the atom indexed by `j` contributes

\[
w_j q_{a_j,b_j}(\gamma_j,d_j)
=w_jL_j=Q
\tag{15}
\]

to its own target. Every cross term is nonnegative because

\[
(\gamma-b)^2+(a+d)^2
>
(\gamma-b)^2+(a-d)^2
\qquad(a,d>0).
\tag{16}
\]

Moreover all cross terms are finite: by construction `a_j` is unequal to every `d_k`, so the denominator in (1) is strictly positive at every target. Hence

\[
Q_\nu(\gamma_j,d_j)\ge Q
\tag{17}
\]

for all `j`, while (6) makes the total variation arbitrarily small. This proves (5).

The logarithmic singularity is doing all the work. Decreasing a coefficient `w_j` does not weaken the attainable target response, because one can move the corresponding probe exponentially closer to the target scale so that its kernel value grows like `Q/w_j`.

## 2. Why zero counts and spacing cannot repair WI-415

The lower bound in WI-415 is an area theorem. At a fixed depth `d`, every unit of coefficient TV has total vertical response area at most `2 pi d`, so asking one source-independent mixture to cover an interval of length `T` forces TV of order `T/d`.

A finite exceptional set has zero vertical area. The construction above shows that replacing continuum coverage by coverage only at those points does not merely weaken the constant in WI-415: it destroys every positive TV lower bound. Even if the target ordinates have a prescribed minimum spacing, even if their number is known exactly, and even if their density is bounded by the sharpest available zero-counting estimate, each target can be assigned an arbitrarily small coefficient whose response is restored by moving its probe sufficiently close in `(a,b)`.

Thus a route of the form

\[
\text{WI-415 continuum budget}
+\text{Riemann--von Mangoldt / spacing information}
\Longrightarrow
\text{discrete exceptional-set budget}
\]

cannot work without an additional **non-oracular constraint on the probes**. Counting information controls how many targets exist; it does not prevent target-adaptive logarithmic concentration.

The same observation applies to every bounded height window of hypothetical off-critical zeta zeros, since that target set is finite. A countable global exceptional set may also be covered with summable coefficients if one allows extended nonnegative potentials; however, the finite-window statement already suffices for the asymptotic source-budget obstruction and avoids any convergence convention for an infinite mixture.

## 3. What a viable discrete mechanism must add

The theorem isolates the missing structure. A useful discrete defect detector must make the probe family unavailable **before** the exceptional set is known, or impose a quantitative regularity condition that prevents concentration at individual targets. Examples of genuinely extra structure include a probe measure generated from prime/source-side data, an absolute-continuity or bounded-density condition in `(a,b)`, a bandwidth or transport constraint, a fixed lattice/mesh with independently justified resolution, or another arithmetic/spectral invariant that couples probe placement to zeta without reading off the zero locations first.

Merely requiring finite TV is insufficient. Nor can local zero spacing by itself supply the missing regularity: the own-target construction (12)--(15) is independent for each target and survives arbitrary separation between targets.

This sharpens the interpretation of WI-415. Its positive-area hypothesis is not a technical convenience that can be replaced by a sufficiently dense discrete set using only counting estimates. It is the source of the coercive budget. Once the target is allowed to be a target-adaptive discrete set, the infimum drops from order `T/delta` to exactly zero.

## 4. Prior-art and novelty audit

The mechanism is a concrete logarithmic-potential phenomenon, not a claim of a new potential-theory theorem. Classical potential theory treats countable sets as polar; see Thomas Ransford, *Potential Theory in the Complex Plane*, Cambridge University Press, 1995, especially the treatment of polar sets in Chapter 3 and logarithmic capacity in Chapter 5, DOI `10.1017/CBO9780511623776`. The present finite-set construction is elementary and stronger for the narrow purpose here because it gives the required positive atomic translated-Blaschke mixture explicitly and keeps every sampled kernel value finite.

The zeta/Blaschke setting is likewise classical. Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:`0804.4829` (2008; revised 2009), derives half-plane Poisson--Schwarz factorisations involving the Blaschke zeros of zeta. WI-409--WI-415 already record the relevant Balazard--Saias--Yor and translated-Blaschke identities used by this line.

A targeted prior-art audit found the classical polarity/capacity principle and zeta Blaschke factorisation, but no reason to regard the elementary concentration construction itself as a priority claim. None is made. The line-specific contribution recorded here is the **programmatic no-go**: the discrete/oracle escape explicitly left by WI-415 has zero finite-TV cost unless independent source-side structure prevents target-adaptive concentration.

## Consequence

The remaining discrete escape after WI-415 is now sharply split in two. In the unconstrained oracle model it is too powerful to yield any source-budget contradiction at all:

\[
\boxed{
\text{finite discrete target set}
+\text{target-adaptive translated Blaschke probes}
\Longrightarrow
\inf \|\nu\|_{\rm TV}=0.
}
\]

Therefore the next useful step is **not** to combine the continuum `T/delta` budget with finer zero counts or spacing estimates. Any viable defect-to-zero bootstrap along this branch must instead derive probe placement or probe regularity independently from the prime/source side, or introduce a different invariant whose coercivity survives restriction to a sparse discrete exceptional set.