# AF-254 — Exponential fiber collapse is Baire-generic but Hausdorff-thin

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `OUTPUT-SAMPLING`, `AFFINE-CONSTRAINTS`, `DIOPHANTINE-FIDELITY`, `GENERICITY-SPLIT`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-250--AF-253 use Haar measure and Hausdorff dimension to show that exponential finite-mode cancellation is exceptional. There is a sharp and opposite topological statement: whenever a genuine cancellation target exists, the same bad set is **Baire-generic**.

Let

\[
B:Q\longrightarrow\mathbb C^M
\]

be a nonzero vector trigonometric polynomial on a connected torus `Q` of dimension `s>=1`, and suppose its common zero set

\[
Z_B=\{y\in Q:B(y)=0\}
\]

is nonempty. For `q in Q`, define

\[
\chi_B(q)
:=\limsup_{n\to\infty}
\frac1n\log^+\frac1{\|B(nq)\|_2}.
\tag{1}
\]

Then the superexponential-collapse set

\[
\mathcal R_\infty(B)
:=\{q\in Q:\chi_B(q)=+\infty\}
\tag{2}
\]

is a dense `G_delta` subset of `Q`. Hence

\[
\boxed{
\{q:\chi_B(q)>0\}
\text{ is comeagre in }Q.
}
\tag{3}
\]

At the same time, if `k=dim_R Z_B`, then `k<=s-1` and AF-251 applied to the scalar trigonometric polynomial `G=||B||_2^2` gives

\[
\boxed{
\dim_H\{q:\chi_B(q)>0\}\le k\le s-1.
}
\tag{4}
\]

In particular the positive-collapse set has Haar measure zero, while its complement

\[
\{q:\chi_B(q)=0\}
\tag{5}
\]

has full Haar measure but is meagre.

Thus the notions of "generic phase" split maximally at the exponential fidelity scale:

- measure-generic quotient phases are root-faithful;
- category-generic quotient phases are superexponentially unfaithful.

For the affine setup of AF-253, where `Q=T^d/H`, `q=a+H`, and

\[
R_n(P,a+H)=\|B(nq)\|_2,
\]

this says that whenever `Z_B` is nonempty, a comeagre set of affine classes has

\[
\chi(P,a+H)=+\infty.
\tag{6}
\]

AF-253 then forces **every point of each such affine coset** to lie in its exponential-cancellation set. Conversely, Haar-almost every affine class has `chi=0`, and AF-253 gives root fidelity for Haar-almost every point inside those classes.

If `Z_B` is empty, AF-253 already gives the opposite rigid branch: `inf_Q ||B||>0`, hence `chi=0` for every affine class. The presence or absence of the quotient annihilator set is therefore also the exact gate between topological stability and category-generic catastrophic recurrence.

## Why it matters

AF-251 correctly shows that destructive finite-mode phases are small in Haar measure and Hausdorff dimension. That does **not** make the safe regime topologically robust. The present result shows that every neighborhood of every quotient phase contains phases with arbitrarily severe exponential collapse, and in fact such phases form a residual set.

This closes a potential but misleading route to the source-specific theorem left by AF-253. Continuity of the phase map, density of numerically safe samples, small perturbations, or any argument whose notion of "generic" is only Baire/topological cannot certify `chi=0` for the actual zeta-derived phase. The required input must be quantitative/arithmetic (for example a Diophantine lower bound, a rigidity theorem, or another source property excluding exponential approach to `Z_B`).

The distinction is especially relevant to finite-precision evidence. A computed phase can lie arbitrarily close to quotient classes with `chi=+infinity` even though almost every exact phase in Haar measure has `chi=0`. Numerical neighborhoods therefore cannot by themselves transfer the almost-everywhere theorem to one distinguished arithmetic phase.

## Derivation

For an integer `m>=1` and `N>=1`, put

\[
U_{m,N}
:=\bigcup_{n\ge N}
\left\{q\in Q:\|B(nq)\|_2<e^{-mn}\right\}.
\tag{7}
\]

Each `U_{m,N}` is open by continuity. It is also dense. Fix a nonempty open set `O subset Q` and choose one `z in Z_B`. The fiber of multiplication by `n`,

\[
[n]^{-1}(z)=\{q\in Q:nq=z\},
\tag{8}
\]

is a translate of the `n`-torsion subgroup `Q[n]`. After identifying the connected `s`-torus with `R^s/Z^s`, these fibers form translated grids of mesh `O(1/n)`. Therefore, for every sufficiently large `n`, `[n]^{-1}(z)` meets `O`. For such a preimage `q_n`,

\[
B(nq_n)=B(z)=0,
\]

so `q_n` belongs to the `n`th set in `(7)`. Hence every `U_{m,N}` is dense.

Baire's theorem now gives

\[
\mathcal R_m
:=\bigcap_{N\ge1}U_{m,N}
\tag{9}
\]

as a dense `G_delta`. A point belongs to `R_m` exactly when

\[
\|B(nq)\|_2<e^{-mn}
\]

for infinitely many `n`. Consequently

\[
\mathcal R_\infty(B)
=\bigcap_{m\ge1}\mathcal R_m
\tag{10}
\]

is again dense `G_delta`, and every point in it satisfies `(2)`. Conversely, `chi_B(q)=+infinity` implies membership in every `R_m`, so `(10)` is exact.

For the size in measure and dimension, define

\[
G(y)=\|B(y)\|_2^2
=\sum_{\lambda=1}^M|B_\lambda(y)|^2.
\tag{11}
\]

This is a nonzero scalar real trigonometric polynomial with zero set `Z_G=Z_B`. Moreover, positive exponential decay of `G(nq)` is equivalent to positive exponential decay of `||B(nq)||_2`, with only the factor two in the logarithmic exponent. Therefore

\[
\{q:\chi_B(q)>0\}=\mathcal E(G)
\tag{12}
\]

in the notation of AF-251. Its Hausdorff bound `(4)` follows directly from AF-251. Since `B` is nonzero and `Z_B` is a proper real-algebraic subset of the connected torus, `k<=s-1`; hence `(4)` implies Haar nullity.

Combining `(3)` and `(4)` gives the claimed category/measure split. No mixing, equidistribution, independence, or arithmetic property of `q` is used in the Baire half; the dense torsion preimage grids alone are enough.

## Prior-art audit

The underlying category-versus-measure phenomenon is classical. The standard model is the set of Liouville numbers: it is well known to be comeagre (equivalently, a dense `G_delta`) while having Hausdorff dimension zero. A recent explicit reference is Johannes Schleischitz, **“Maillet's property and Mahler's conjecture on Liouville numbers fail for matrices,”** *Journal of the Australian Mathematical Society* 119 (2025), 106--127, DOI `10.1017/S1446788725000011`, which recalls this fact at the start of the paper. Classical accounts include John C. Oxtoby, *Measure and Category*.

Baire-category formulations of shrinking-target phenomena are also established. Joseph Rosenblatt and Mrinal Kanti Roychowdhury, **“Geometric and Measure-Theoretic Shrinking Targets in Dynamical Systems,”** arXiv:`1809.09780` (2018; rev. 2019), explicitly study both measure-theoretic and Baire-category visibility for shrinking targets. Their setup is broader and primarily concerns iterates of a fixed transformation; the elementary argument `(7)`--`(10)` here uses the varying multiplication maps `[n]` and exact preimages of a fixed trigonometric zero set.

AF-251 already audits the Łojasiewicz, algebraic-tube, Hausdorff--Borel--Cantelli, and toral shrinking-target ingredients behind `(4)`. AF-253 supplies the quotient-frequency reduction that turns affine whole-fiber collapse into `(1)`.

No novelty is claimed for Baire's theorem, Liouville-type residual/null sets, or category shrinking-target arguments. The durable Arithmetic Fidelity contribution is the exact juxtaposition with AF-251 and AF-253: the same exponential-collapse locus governing finite-mode and affine fidelity is Hausdorff-thin/Haar-null **and simultaneously comeagre**, so topological genericity points in precisely the wrong direction for the source-specific zeta certification problem.

## Boundaries and failure modes

**A cancellation target is required.** If `Z_B` is empty, compactness gives a uniform positive lower bound and the residual-collapse conclusion is false. This is the sharp structural gate.

**The theorem concerns varying source phase, not one fixed arithmetic phase.** Comeagreness does not imply that the actual zeta-derived quotient phase is bad, just as Haar full measure does not imply that it is safe. Both genericity statements are deliberately non-source-specific.

**Category is not a probabilistic model.** Equation `(3)` is not evidence that destructive cancellation is likely. It is a topological instability statement. Equation `(4)` gives the opposite verdict under Haar measure.

**Finite mode remains fixed.** The polynomial `B` and its zero set are fixed while `n` varies. No uniform statement is claimed when the number of co-dominant modes, the quotient dimension, or the coefficients themselves grow with the Li index.

**Exact preimages drive density, not physical perturbation stability.** The residual construction repeatedly changes `q` on finer `1/n` grids. It does not show that one fixed phase trajectory is structurally unstable under a prescribed dynamical perturbation model.

## Research consequence

The affine output-side frontier is now separated into three logically distinct questions. First, `Z_B=empty` gives unconditional quotient-level stability. Second, when `Z_B` is nonempty, Haar and Hausdorff genericity say almost every quotient phase is safe. Third, Baire genericity says no open or residual-topological argument can promote that statement to the distinguished arithmetic phase: the catastrophic set is itself comeagre and even contains a dense `G_delta` of infinite collapse exponent.

Therefore the next source-specific theorem cannot be a genericity upgrade. It must use information genuinely unavailable to the arbitrary quotient phase class and prove directly that the actual zeta/Li quotient orbit avoids `Z_B` at exponential scale, ideally with bounds uniform enough to survive growth of the finite dominant-mode family. That is exactly the arithmetic discriminator still missing after AF-253.