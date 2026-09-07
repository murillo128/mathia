# PF-198 — finite-window Lambert localization preserves the critical Orlicz budget

**Status:** `EXACT-DERIVED + ENDPOINT-LOCALIZATION + POSITIVE/BOUNDARY`. PF-196 proves that the exact-area Lambert coefficient has critical `L log L` cost `O(d(1+a)/cosh a)`, while PF-197 reduces the principal localized vector-gradient endpoint to Ponge-critical matrix-valued `Q C P` pieces. A remaining bookkeeping concern was whether cutting a Lambert body of longitudinal depth `O(a)` into `O(a)` fixed-size pseudodifferential windows would itself destroy that coefficient currency before any operator reassembly is attempted. It does not. For a fixed-overlap Fermi partition, the **sum of the local Luxemburg norms** is still

\[
O\!\left(\frac{d(1+a)}{\cosh a}\right).
\]

The reason is that the relevant `L log L` localization cost is concave in the local `L^1` mass: splitting into `N` pieces inserts only `log N` inside the concentration logarithm, not a multiplicative factor `N`. Since the exact Lambert branch needs only `N=O(1+a)` fixed-width windows, this extra `log(1+a)` is absorbed by the already-present depth logarithm from PF-196. Thus **chart/window count is not a coefficient-level endpoint obstruction** on the exact-area Lambert body. This does not prove uniform Ponge constants for the localized resolvent factors, control their off-diagonal tails, justify weak-`S_1` operator reassembly, construct the endpoint conservative splice, or prove the full relative resolvent is weak trace class.

## Claim

Let

\[
\Phi(t)=t\log(e+t),
\]

with Luxemburg norm `||.||_{L_\Phi}` as in PF-196. On one exact-area PF-191 Lambert module `Q(a)`, let `C_{a,d}` denote the matrix-valued cotangent coefficient entering PF-175/PF-197. On the PF-191 tail, fixed quasi-isometry comparison with the metric-deviation scalar gives

\[
L:=\|C_{a,d}\|_{L^1}\le C\frac dA,
\qquad
B:=\|C_{a,d}\|_{L^\infty}\le Cd,
\qquad A:=\cosh a.
\tag{1}
\]

Choose a smooth partition of unity `chi_1,...,chi_N` on the finite Lambert branch in the Fermi coordinate `tau`, with all windows of one fixed width, uniformly bounded derivatives, and overlap multiplicity at most `kappa`, independent of `a,d`. The finite branch lies before `tau=a`, so the partition may be chosen with

\[
N\le C(1+a).
\tag{2}
\]

Put

\[
C_j=\chi_j C_{a,d}.
\tag{3}
\]

Then

\[
\boxed{
\sum_{j=1}^N\|C_j\|_{L_\Phi}
\le
C\frac dA\log\!\bigl(e+CNA\bigr)
\le
C\frac{d(1+a)}A.
}
\tag{4}
\]

The fixed PF-191 corner correction contributes only `O(d e^{-2a})` in `L log L`, and the outer branch is an isometry. Hence the same bound holds after adjoining a fixed number of corner/outer localization pieces.

For the exact prime/shift family,

\[
\boxed{
\sum_n\sum_j\|C_{n,j}\|_{L_\Phi}<\infty.
}
\tag{5}
\]

by PF-196's prime summability. Equation (5) is purely a **coefficient-localization statement**. It does not assert

\[
\left\|\sum_j Q_j C_j P_j\right\|_{1,\infty}
\lesssim
\sum_j\|C_j\|_{L_\Phi},
\]

nor does it identify the global relative resolvent with such a sum.

## 1. The localization inequality is sublinear in the number of windows

PF-196 proves the elementary Luxemburg estimate

\[
\|u\|_{L_\Phi}
\le
\|u\|_1\log\!\left(e+\frac{\|u\|_\infty}{\|u\|_1}\right)
\tag{6}
\]

for bounded nonzero `u`. Write

\[
L_j=\|C_j\|_1.
\]

Because `0<=chi_j<=1`, every local piece has `||C_j||_infinity<=B`, while bounded overlap gives

\[
\widetilde L:=\sum_jL_j\le\kappa L.
\tag{7}
\]

For fixed `B>0` define

\[
f_B(x)=x\log\!\left(e+\frac Bx\right),\qquad x>0.
\tag{8}
\]

A direct differentiation gives

\[
f_B''(x)
=-\frac{B^2}{x(B+ex)^2}<0.
\tag{9}
\]

Thus `f_B` is concave. Applying (6) to each nonzero piece and Jensen to (8),

\[
\begin{aligned}
\sum_j\|C_j\|_{L_\Phi}
&\le \sum_j f_B(L_j)\\
&\le N f_B(\widetilde L/N)\\
&=\widetilde L\log\!\left(e+\frac{BN}{\widetilde L}\right).
\end{aligned}
\tag{10}
\]

The last expression is increasing in `widetilde L`. Combining (1), (7), and (10) therefore yields

\[
\sum_j\|C_j\|_{L_\Phi}
\le
C\frac dA
\log\!\left(e+CNA\right),
\tag{11}
\]

which is the first inequality in (4).

The important point is the position of `N`: localization inserts it **inside the logarithm**. Treating every window with the global worst-case norm and multiplying by `N` would lose the exact effective-area bookkeeping and is unnecessarily crude.

## 2. The Lambert geometry makes `log N` harmless

PF-191's finite branch is parameterized by

\[
0\le\tau<a
\]

before the actual cutoff to the corner model, and its area-coordinate metric is

\[
g=\frac{dy^2}{1+y^2}+(1+y^2)d\tau^2,
\tag{12}
\]

independent of the Lambert depth `a`. The relevant `y`-width stays uniformly bounded on the PF-191 tail. A fixed-width translated Fermi cover therefore has bounded overlap and needs only (2).

Since `A=cosh a`,

\[
\log(e+CNA)
\le
C(1+a)+C\log(1+a)
\le C(1+a).
\tag{13}
\]

Equations (11)--(13) prove (4). PF-196 then gives, for the exact prime/shift sequence,

\[
\sum_n\frac{d_n(1+a_n)}{\cosh a_n}<\infty,
\tag{14}
\]

which proves (5).

The same fixed-window construction also means that the **cutoff functions themselves** can be chosen from translates of one bounded family: overlap number and every prescribed finite set of cutoff-derivative bounds are independent of `a`. Together with PF-191's universal source metric (12), this removes window count and cutoff scaling as automatic sources of Lambert-depth growth. It does **not** by itself prove a uniform bound for Ponge's operator constant `C_{P_j,Q_j}` because the actual localized two-metric resolvent parametrices and their off-diagonal remainders still have to be controlled quantitatively.

## 3. Relation to the critical Cwikel route

PF-197 shows that after compact localization the principal two-dimensional gradient term is a corner of Ponge's matrix-valued critical operator

\[
Q M_C P\in\mathcal S_{1,\infty},
\qquad
\|QM_CP\|_{1,\infty}\le C_{P,Q}\|C\|_{L\log L}.
\tag{15}
\]

PF-198 supplies the missing coefficient-side fragmentation estimate for using such local pieces along a long Lambert body. If a later argument proves that the relevant localized factors have constants within a fixed-polynomial Lambert-depth envelope and that the off-diagonal/cutoff terms can be reassembled in a summable endpoint ideal, then (4)--(5) show that **splitting the coefficient into the required fixed windows does not consume an additional depth power**.

But weak `S_1` is a quasi-Banach endpoint and bounded geometric overlap does not automatically imply lossless operator counting. No operator-level finite-color inequality is asserted here. In particular, pseudodifferential factors are nonlocal before the cutoff/remainder decomposition, and a fixed-color family is not automatically an orthogonal direct sum merely because the coefficient supports are disjoint.

## Prior art and novelty assessment

The Luxemburg estimate (6), the use of finite-overlap partitions, and the concavity calculation (9) are elementary Orlicz/localization facts; no novelty is claimed for them. Ponge's matrix-valued critical Cwikel estimate is prior art already audited in PF-197 and recorded as S20 in `research/prime_flute/SOURCES.md`. A targeted search around `L log L` Luxemburg localization, partitions of unity, and Ponge-critical Cwikel localization did not identify a theorem that performs the prime-flute global operator reassembly, and search absence is not treated as evidence of novelty.

The project-specific deduction is (4)--(5): **for the exact PF-191 Lambert profile, an `O(a)` fixed-window localization preserves the same `O(d(1+a)/cosh a)` critical coefficient scale already found in PF-196**. This narrows PF-197's family-uniformity gate by removing one concrete possible source of depth loss: coefficient fragmentation by the necessary local chart count.

## Falsification and boundary checks

A later adversary can test PF-198 by:

1. verifying the PF-196 Luxemburg estimate (6) and differentiating (8) to obtain (9);
2. checking Jensen's direction in (10) and the bounded-overlap inequality (7);
3. checking from PF-191 that the finite Lambert branch has longitudinal extent at most `a`, fixed-width Fermi windows have `N=O(1+a)`, and the relevant cross-section stays uniformly bounded;
4. inserting `L<=Cd/cosh a` and `B<=Cd` into (10) without assuming an unavailable lower bound for `L`;
5. verifying that the corner correction remains `O(d e^{-2a})` in the same Orlicz currency;
6. summing (4) with PF-196's exact prime-tail estimate;
7. rejecting any attempted upgrade from (5) to a global weak-`S_1` operator bound that does not separately control Ponge constants, off-diagonal resolvent tails, commutators, and finite-color counting/reassembly.

The finding would be overclaimed if read as proving any of the following, none of which is asserted:

- uniform critical Cwikel constants for the full normalized PF module family;
- trace-class or weak-`S_1` bounds for every off-diagonal or commutator term;
- an operator-level direct-sum decomposition from finite coloring alone;
- the endpoint conservative collar splice;
- the complete first relative resolvent is in `S_{1,infinity}`;
- PF-190's `log^2(n)/n` envelope is removed;
- wave equivalence, a spectral prime/clone distinction, or any RH consequence.

## Consequences for the research line

PF-196 showed that the exact Lambert coefficient can pay one critical concentration logarithm. PF-197 showed that the required local matrix-valued weak-`S_1` theorem already exists. PF-198 now shows that **ordinary fixed-scale localization of that coefficient does not spend another polynomial factor in the Lambert depth**: the `O(a)` window count appears only as `log O(a)` and is absorbed by the same depth currency.

The analytic frontier should therefore stop treating the number of local Lambert charts as an independent endpoint threat. The remaining operator gate is sharper: prove quantitative control of the actual localized resolvent/parametrix factors and every off-diagonal/cutoff remainder, then justify the weak-`S_1` finite-color reassembly itself. Those are operator-level questions; the coefficient partition budget is now closed.