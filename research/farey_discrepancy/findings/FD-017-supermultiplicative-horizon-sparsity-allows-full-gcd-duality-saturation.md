# FD-017 — supermultiplicative horizon sparsity allows full GCD-duality saturation

**Status:** `EXACT-DERIVED + VARIABLE-FRESHNESS-DIAGONALIZATION + FULL-ASYMPTOTIC-SATURATION + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`. `FD-016` proves that, for a fixed planted prefix depth `R`, one unrestricted real source can make arbitrarily many sufficiently separated horizon ratios approach the finite equality constant `C_R`. Letting the fresh prefix depth grow with the horizon gives a qualitatively stronger obstruction: if successive sampled horizons become multiplicatively farther apart, the **same source can asymptotically attain the full one-horizon constant `zeta(2)`**.

Let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
C_R=(K_R^{-1})_{11}
=\sum_{r\le R}\frac{\mu(r)^2}{J_2(r)},
\qquad
Z:=\zeta(2),
\tag{1}
\]

and for a real sequence `A(1),A(2),...` define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H}
\tag{2}
\]

whenever the horizon vector is nonzero.

The quantitative diagonal form is the following. Let

\[
H_0<H_1<H_2<\cdots,
\qquad
R_j\ge2,
\qquad
\delta_j>0,
\tag{3}
\]

satisfy

\[
H_j\ge R_j^2
\quad(j\ge0),
\qquad
\left\lfloor\frac{H_j}{R_j}\right\rfloor>H_{j-1}
\quad(j\ge1).
\tag{4}
\]

Then there exists a **single real sequence** `A` such that

\[
\boxed{
R_{H_j}>C_{R_j}-\delta_j
\qquad(j\ge0).
}
\tag{5}
\]

In particular, if `R_j -> infinity` and `delta_j -> 0`, then `FD-003` gives `C_(R_j) -> Z` and the universal one-horizon inequality `R_H<=C_H<=Z`, so

\[
\boxed{
R_{H_j}\longrightarrow Z=\zeta(2).
}
\tag{6}
\]

Consequently, for **every** increasing horizon sequence satisfying

\[
\boxed{
\frac{H_j}{H_{j-1}}\longrightarrow\infty,
}
\tag{7}
\]

there exists one unrestricted real source `A` for which (6) holds along that prescribed horizon sequence. Thus common-source consistency on increasingly isolated horizons does not merely fail to produce a fixed saturation gap: it permits asymptotic saturation of the entire sharp GCD-duality constant.

This is a theorem about the unrestricted source relaxation used to diagnose the information content of cross-horizon coherence. It is not a construction of the Mertens function, a bounded-increment source, or a Farey discrepancy counterexample.

## 1. Variable-depth fresh-prefix interpolation

For each stage `j`, write

\[
u^{(j)}:=K_{R_j}^{-1}e_1.
\tag{8}
\]

Then

\[
u_1^{(j)}=C_{R_j},
\qquad
(u^{(j)})^TK_{R_j}u^{(j)}=C_{R_j}.
\tag{9}
\]

At horizon `H_j`, put

\[
x_{j,d}:=\left\lfloor\frac{H_j}{d}\right\rfloor,
\qquad1\le d\le R_j.
\tag{10}
\]

Because `H_j>=R_j^2`, these first `R_j` floor quotients are pairwise distinct, exactly as in `FD-016`. Condition (4) also gives

\[
x_{j,d}\ge x_{j,R_j}>H_{j-1}
\qquad(1\le d\le R_j),
\tag{11}
\]

so every coordinate used for the new equality-ray prefix lies strictly above the entire source range fixed at the previous stage.

Construct `A` inductively. At stage `j`, assign every still-unassigned source value in `(H_(j-1),H_j]` to zero except the fresh locations (10), and prescribe

\[
A(x_{j,d})=t_j u_d^{(j)}
\qquad(1\le d\le R_j),
\tag{12}
\]

where `t_j` is chosen only after all inherited lower source values are fixed. For `j=0`, make the analogous assignment below `H_0`.

The first `R_j` coordinates of the horizon vector are therefore exactly `t_j u^(j)`. Every coordinate with `d>R_j` samples a source location strictly below `x_(j,R_j)`, hence contributes only already-fixed data or a zero assigned independently of `t_j`. Thus

\[
\boxed{
m^{(H_j)}=t_j\widetilde u^{(j)}+b_j,}
\tag{13}
\]

where `widetilde u^(j)` is `u^(j)` embedded in the first `R_j` coordinates and `b_j` has those first `R_j` coordinates equal to zero. Crucially, `b_j` is independent of `t_j`.

The top-left `R_j x R_j` block of `K_(H_j)` is exactly `K_(R_j)`, so

\[
(\widetilde u^{(j)})^TK_{H_j}\widetilde u^{(j)}=C_{R_j}.
\tag{14}
\]

Hence

\[
E_{H_j}
=t_j^2C_{R_j}
+2t_j(\widetilde u^{(j)})^TK_{H_j}b_j
+b_j^TK_{H_j}b_j,
\tag{15}
\]

while

\[
A(H_j)=t_j u_1^{(j)}=t_jC_{R_j}.
\tag{16}
\]

For each fixed stage the two coefficients involving `b_j` are finite and independent of `t_j`. Therefore

\[
R_{H_j}
=\frac{t_j^2C_{R_j}^2}{E_{H_j}}
\longrightarrow C_{R_j}
\qquad(|t_j|\to\infty).
\tag{17}
\]

Choose a finite nonzero `t_j` large enough to obtain (5). Later stages alter only source values above `H_j`, so they cannot change any previously constructed horizon vector. Induction gives one globally defined sequence satisfying all inequalities simultaneously.

The argument is the fixed-depth interpolation mechanism of `FD-016`, but the quantifiers are different: every stage receives its own finite equality-ray prefix, and the prefix depth may diverge because the horizon separation keeps those load-bearing source locations fresh.

## 2. Diverging multiplicative gaps supply a diverging fresh prefix

Assume (7) and write

\[
\rho_j:=\frac{H_j}{H_{j-1}}.
\tag{18}
\]

For all sufficiently large `j`, define

\[
R_j:=
\left\lfloor
\min\left\{\sqrt{H_j},\frac{\rho_j}{2}\right\}
\right\rfloor.
\tag{19}
\]

Both quantities inside the minimum tend to infinity, so

\[
R_j\longrightarrow\infty.
\tag{20}
\]

The first term in (19) gives `H_j>=R_j^2`. The second gives

\[
\frac{H_j}{R_j}
\ge 2H_{j-1},
\tag{21}
\]

for all sufficiently large `j`; therefore `floor(H_j/R_j)>H_(j-1)`. The hypotheses of the variable-depth theorem hold on the tail of the prescribed horizon sequence. Taking, for example, `delta_j=1/j`, equation (5) and the `FD-003` estimate

\[
0\le Z-C_R\le\frac ZR
\tag{22}
\]

give

\[
R_{H_j}>Z-\frac{Z}{R_j}-\frac1j.
\tag{23}
\]

On the other hand, the sharp one-horizon dual inequality gives `R_(H_j)<=C_(H_j)<=Z`. Squeezing proves (6).

This formulation does not require a geometric progression, integrality of `rho_j`, squarefreeness of any dilation, or a preselected growth law. The only input is that each next horizon eventually lies far enough beyond the previous one to expose a growing number of unused floor-quotient coordinates.

## 3. Relation to the fixed-dilation gap and to the Farey/Mertens target

There is no conflict with `FD-014` or `FD-015`. Those findings show that a **fixed or prescribed nearby multiplicative relation** can force a positive two-horizon incompatibility because the same source coordinates are reused by incompatible entries of the GCD equality ray. Here the multiplicative separation itself diverges. The amount of equality-ray data that can be placed entirely above the previous horizon therefore also diverges, and the finite constants `C_(R_j)` approach `Z`.

The distinction sharpens the coherence boundary. `FD-016` already showed that a fixed `Q`-geometric chain can jointly approach `C_(Q-1)`, which lies within `O(1/Q)` of `Z`. The present diagonal theorem says that once the available fresh depth tends to infinity, the residual `O(1/R)` loss can be driven to zero **within one source sequence**. Merely increasing the number of increasingly isolated horizons cannot amplify a coherence gap; it erases the relaxation-level gap asymptotically.

For the physical source `A=M`, this construction is inadmissible. The chosen values can jump arbitrarily, are scaled independently on fresh blocks, and need not have increments in `{-1,0,1}` or satisfy the exact Möbius divisor relations beyond the floor-sampling identity. Thus (6) proves no large values of the Mertens function and gives no Franel or RH consequence.

Instead it identifies what a successful cumulative argument must prevent. A cross-horizon theorem that uses only unrestricted common-source consistency cannot obtain a persistent gain from a hierarchy whose successive multiplicative gaps tend to infinity. To escape the obstruction it must retain substantial overlap between successive floor-quotient sets, exploit arithmetic restrictions of the true Möbius source, or introduce genuinely Farey-specific information. `FD-009` marks the opposite danger: sufficiently dense exact horizon data can become a reconstruction of the Möbius prefix. The live regime remains the nontrivial middle ground between **dense reconstructive coherence** and **asymptotically fresh interpolable coherence**.

## 4. Prior art, novelty boundary, and falsification controls

The GCD-matrix factorization, inverse coordinate constant `C_R`, and estimate (22) are the existing `FD-003` inputs. `FD-016` supplies the fixed-depth planting mechanism on which the diagonalization is based. Floor quotients and their combinatorial structure are classical; relevant neighboring work includes J.-P. Cardinal, *Symmetric matrices related to the Mertens function* (arXiv:0811.3701), and J. C. Lagarias--D. H. Richman, *The floor quotient partial order*, Advances in Applied Mathematics **153** (2024), 102615, together with their later family of floor-quotient orders. A targeted search did not identify this variable-depth common-source interpolation statement, but no broad novelty claim is made from search absence, and no theorem from those papers is needed here.

The exact falsification points are elementary. The first `R_j` floor quotients must be distinct; the smallest of them must lie above `H_(j-1)`; every inherited tail contribution must be independent of `t_j`; and the principal kernel block must remain `K_(R_j)`. Conditions (4) ensure the first two, the inductive assignment ensures the third, and the ambient-independent GCD kernel ensures the fourth. The passage from (5) to (6) additionally requires `R_j -> infinity` and the known `C_R -> Z` bound. The reduction from (7) to (4) is exactly the choice (19)--(21).

No statement is made for bounded multiplicative spacing, for sparse schedules that still contain infinitely many strongly overlapping adjacent pairs, or for the actual Mertens source. The durable conclusion is narrower and exact: **supermultiplicatively separated horizon sampling is asymptotically noncoercive in the unrestricted source class, even when all horizon vectors are required to come from one common sequence.**