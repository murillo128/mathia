# PF-201 — global-to-local Cwikel factorization removes the regular-body off-diagonal remainder

**Status:** `EXACT-DERIVED + ENDPOINT-LOCALIZATION + POSITIVE/BOUNDARY`. PF-197 identifies the localized two-dimensional relative gradient form with the critical matrix-valued `L log L` Cwikel problem, PF-198 proves that a fixed-window partition preserves the prime-summable critical Orlicz budget, PF-199 removes weak-trace counting loss for genuinely two-sided finite-color localized operators, and PF-200 makes the regular Lambert-body local Cwikel constants uniform. PF-200 still left the **external off-diagonal resolvent tails** created by its right-hand input cutoffs as a separate reassembly gate. For the regular Lambert-body coefficient sector, those tails are not intrinsic: one can avoid creating them.

The key observation is to localize only on the **coefficient side** and collect all regular windows into one Hilbert direct sum. Interior elliptic regularity gives a bounded global-to-local square-function map

\[
f\longmapsto
\bigl(\Lambda J_\alpha\vartheta_\alpha dR_k f\bigr)_\alpha,
\]

where `alpha=(n,j)` ranges over the PF-198 regular windows, `vartheta_alpha=1` on the support of the localized coefficient, `J_alpha` transports the fixed-buffer chart to the fixed torus model, and `Lambda=(1+Delta_{T^2})^{1/2}`. The middle critical operators are then block diagonal:

\[
D_\alpha=\Lambda^{-1}M_{\widetilde C_\alpha}\Lambda^{-1}.
\]

Their weak-trace counting functions add exactly, while PF-198 gives a summable total `L log L` budget. Consequently the **full regular Lambert-body principal coefficient contribution**, with the global resolvents left uncut on their input/output sides, is already in `S_{1,infinity}`. The off-diagonal/cutoff remainder of the PF-200 proof architecture is therefore eliminated for this sector rather than estimated.

This does not prove that the complete prime/shift first relative resolvent is weak trace class. Module-end/cuff and true-short-collar transition sectors, the endpoint conservative splice, the remaining scalar/density and identification terms, and any coefficient pieces outside the uniform regular-body family still require their own endpoint control.

## Claim

Work in the exact-area prime/shift comparison on the regular Lambert-body region supplied by PF-191 and used in PF-198--PF-200. Let

\[
R_k=(\Delta_k+1)^{-1},\qquad G_k=dR_k,
\qquad k\in\{g,h\},
\tag{1}
\]

and let `C^reg` be the cotangent coefficient from PF-175 restricted to the regular Lambert-body sector. Use PF-198's fixed-width partition

\[
C^{\rm reg}=\sum_{\alpha} C_\alpha,
\qquad \alpha=(n,j),
\tag{2}
\]

where the coefficient supports and slightly enlarged regular chart buffers have uniformly bounded overlap. For each `alpha`, choose a fixed-profile cutoff `vartheta_alpha` with

\[
\vartheta_\alpha=1
\quad\text{on}\quad
\operatorname{supp}C_\alpha,
\tag{3}
\]

supported inside the corresponding PF-200 regular chart. Let `J_alpha` denote the fixed recentering/trivialization/zero-extension into the common torus model used in PF-200, with the uniformly bounded metric/bundle identifications absorbed into the transported coefficient.

Put

\[
\Lambda=(1+\Delta_{\mathbb T^2})^{1/2}
\tag{4}
\]

on that fixed torus bundle and define the global-to-local maps

\[
A_k f
:=
\bigl(\Lambda J_\alpha\vartheta_\alpha G_k f\bigr)_\alpha
\in
\bigoplus_\alpha L^2(\mathbb T^2,E).
\tag{5}
\]

Then there is a constant `C`, independent of the Lambert depths and of the number of windows, such that

\[
\boxed{
\|A_k f\|_{\ell^2(L^2)}
\le C\|f\|_{L^2},
\qquad k\in\{g,h\}.
}
\tag{6}
\]

Let `C_tilde_alpha` be the transported matrix coefficient and define

\[
D_\alpha
:=
\Lambda^{-1}M_{\widetilde C_\alpha}\Lambda^{-1},
\qquad
D:=\bigoplus_\alpha D_\alpha.
\tag{7}
\]

For the weak-trace counting quasi-norm

\[
q(T):=\sup_{\sigma>0}\sigma N_T(\sigma)
\tag{8}
\]

used in PF-199, the torus Cwikel--Solomyak estimate audited in PF-196/PF-200 and PF-198 give

\[
q(D_\alpha)
\le C\|C_\alpha\|_{L\log L},
\tag{9}
\]

and therefore

\[
\boxed{
q(D)
\le
\sum_\alpha q(D_\alpha)
\le
C\sum_{n,j}\|C_{n,j}\|_{L\log L}
\le
C\sum_n
\frac{d_n(1+a_n)}{\cosh a_n}
<\infty.
}
\tag{10}
\]

Finally, the regular-body coefficient contribution to the PF-175 first-resolvent form factors **without any external resolvent cutoff** as

\[
\boxed{
T_{\rm reg}
:=(G_h)^*M_{C^{\rm reg}}G_g
=A_h^* D A_g.
}
\tag{11}
\]

Hence the ideal property gives

\[
\boxed{
T_{\rm reg}\in\mathcal S_{1,\infty},
\qquad
q(T_{\rm reg})
\le
C\sum_n
\frac{d_n(1+a_n)}{\cosh a_n}
<\infty.
}
\tag{12}
\]

Equation (12) concerns the complete regular Lambert-body **principal cotangent-coefficient term** of the exact-area comparison. It is stronger than the PF-200 statement for the two-sided principal pieces because no terms of the form `vartheta dR(1-vartheta')` are introduced at all.

## 1. Local `H^2` regularity gives a global square-function bound

PF-200 proves that, after recentering, every regular Lambert-body source/target metric belongs to one uniformly elliptic `C^1` family on a fixed-buffer chart. Let `U_alpha` be the support region of `vartheta_alpha` and let `V_alpha` be one fixed enlargement still contained in that regular chart. For

\[
u=R_k f,
\tag{13}
\]

we have

\[
(\Delta_k+1)u=f.
\tag{14}
\]

The fixed-buffer interior estimate used already in PF-200 gives

\[
\|u\|_{H^2(U_\alpha)}
\le
C\left(
\|f\|_{L^2(V_\alpha)}
+
\|u\|_{H^1(V_\alpha)}
\right),
\tag{15}
\]

with the same `C` for all regular windows on both metrics. Fixed-profile multiplication and the fixed torus transport then give

\[
\|\Lambda J_\alpha\vartheta_\alpha d u\|_2
\le C\|u\|_{H^2(U_\alpha)}.
\tag{16}
\]

The enlarged windows `V_alpha` have uniformly bounded overlap. Squaring (15)--(16), summing over `alpha`, and using bounded overlap yields

\[
\sum_\alpha
\|\Lambda J_\alpha\vartheta_\alpha dR_k f\|_2^2
\le
C\left(
\|f\|_2^2
+
\|R_k f\|_{H^1(k)}^2
\right).
\tag{17}
\]

The global resolvent energy identity gives

\[
\|R_k f\|_{H^1(k)}\le C\|f\|_2.
\tag{18}
\]

Equations (17)--(18) prove (6).

This is the crucial distinction from summing local **operator ideals** window by window. The number of Lambert windows never appears: the localized resolvent factors are assembled first as an `ell^2` square-function map, and bounded spatial overlap controls that map at the Hilbert-space level.

## 2. The critical singular-value bookkeeping lives in the coefficient direct sum

For each window, the middle operator in (7) is exactly the fixed-torus critical Cwikel--Solomyak model. PF-200 already unpacked Ponge's reduction to this torus estimate. Thus (9) uses no new endpoint theorem.

For the Hilbert direct sum `D=direct_sum D_alpha`, singular values are the multiset union of the block singular values, equivalently

\[
N_D(\sigma)
=
\sum_\alpha N_{D_\alpha}(\sigma).
\tag{19}
\]

Therefore

\[
\sigma N_D(\sigma)
\le
\sum_\alpha q(D_\alpha),
\tag{20}
\]

which proves the first part of (10). PF-198 supplies

\[
\sum_j\|C_{n,j}\|_{L\log L}
\le
C\frac{d_n(1+a_n)}{\cosh a_n},
\tag{21}
\]

and PF-196 proves the prime-tail summability of the right-hand side. Thus `D` is a well-defined weak-trace operator; in particular, the tails of its block direct sum converge in operator norm because their weak-trace counting bound tends to zero.

PF-199's exact finite-color counting observation reappears here in a cleaner place: orthogonality is automatic in the **auxiliary coefficient direct sum**, rather than being forced by two-sided multiplication on the external source/target Hilbert spaces.

## 3. The factorization is exact and does not create an off-diagonal remainder

Because `vartheta_alpha=1` on `supp C_alpha`,

\[
M_{\vartheta_\alpha}M_{C_\alpha}M_{\vartheta_\alpha}
=M_{C_\alpha}.
\tag{22}
\]

For each finite set `F` of windows, the definition of `A_k` and `D_alpha` gives the exact algebraic identity

\[
\begin{aligned}
A_{h,F}^*D_F A_{g,F}
&=
\sum_{\alpha\in F}
(G_h)^*M_{\vartheta_\alpha}
J_\alpha^*\Lambda
\left(\Lambda^{-1}M_{\widetilde C_\alpha}\Lambda^{-1}\right)
\Lambda J_\alpha
M_{\vartheta_\alpha}G_g\\
&=
\sum_{\alpha\in F}
(G_h)^*M_{C_\alpha}G_g.
\end{aligned}
\tag{23}
\]

The uniformly bounded zero-order chart/bundle identifications cancel or are absorbed into the transported matrix coefficient exactly as in PF-197/PF-200. Since `D_F` converges to `D` in operator norm and `A_g,A_h` are bounded, the left-hand side converges in operator norm to `A_h^*DA_g`.

On the right, the coefficient partition is locally finite and sums pointwise to `C^reg`; the coefficients are uniformly bounded in the exact-area tail. Hence the form defined by the finite partial sums converges to the PF-175 regular-body coefficient form. This proves (11).

The weak ideal property now gives

\[
q(A_h^*DA_g)
\le
\|A_h\|\,\|A_g\|\,q(D),
\tag{24}
\]

and (12) follows.

The important methodological consequence is exact: the earlier decomposition

\[
\vartheta dR
=
\vartheta dR\vartheta'
+
\vartheta dR(1-\vartheta')
\tag{25}
\]

is unnecessary for the regular coefficient sector. The second term in (25) was a remainder only because the local pseudodifferential proof was being forced to live entirely on the external Hilbert space. The global-to-local factorization moves the critical operator to the auxiliary torus direct sum and requires only the bounded map `Lambda vartheta dR`, so no corresponding external off-diagonal operator is generated.

## 4. What remains outside the result

PF-201 removes one analytic gate but does not close the accepted weak-endpoint clue. It does not treat:

- the finitely many **per-module** windows deliberately excluded from the PF-200 regular family because they touch physical cuffs, module ends, corner corrections, or later assembly interfaces;
- the complete PF-183 true-short-collar transition family or the still-missing endpoint exact-area conservative splice;
- any coefficient sector whose buffered chart family does not have the uniform local ellipticity/regularity and bounded-overlap structure used in (15)--(17);
- the scalar/density part of the PF-175 form and the final source/target identification bookkeeping needed for one global first-relative-resolvent statement;
- any claim that weak `S_1` implies ordinary trace class, complete wave operators, equality of scattering matrices/resonances, or an RH statement.

A fixed number of exceptional **head** pieces is harmless, but a fixed number of exceptional pieces in every tail module is still an infinite family and must receive a prime-summable endpoint estimate. Likewise, the present argument does not manufacture the global exact-area marking whose collar splices remain under investigation.

Thus the analytic frontier is narrower than PF-200's equation `control the nonprincipal/off-diagonal/interface remainder`: for the regular Lambert-body principal coefficient the external off-diagonal part is gone. What remains is the genuinely geometric/interface family and the lower-order/global-identification completion.

## Prior-art and novelty audit

The critical torus estimate for

\[
\Lambda^{-1}M_u\Lambda^{-1}
\in\mathcal S_{1,\infty}
\]

with `u in L log L` is classical Cwikel--Solomyak theory, audited in PF-196/PF-200 through Sukochev--Zanin and Ponge (S20 in `research/prime_flute/SOURCES.md`). Ponge's matrix-valued theorem and compact-support reduction are prior art; so are the ideal property of weak Schatten classes, direct-sum singular-value counting, standard fixed-buffer interior `H^2` regularity, and bounded-overlap square-function summation. No novelty is claimed for any of those ingredients.

A targeted literature search around critical Cwikel localization, bounded-overlap partitions, direct sums, and weak-Schatten reassembly located the expected general Cwikel/Solomyak and local elliptic machinery but no source that performs this exact prime-flute global-to-local factorization. Search absence is not used as a novelty theorem.

The project-specific deduction is the combination (5)--(12): **PF-200's uniform local Sobolev control is strong enough to remove the external input cutoffs altogether; PF-198's coefficient pieces can be placed in an auxiliary direct sum where the critical weak-trace counting is genuinely block diagonal.** This converts the entire regular Lambert-body principal coefficient sector into a global weak-`S_1` operator and shows that the off-diagonal remainder previously attached to that sector was proof-architectural rather than geometric.

## Falsification and boundary checks

A later adversary can audit PF-201 by:

1. checking that every `C_alpha` from PF-198 assigned to the regular family admits a slightly enlarged PF-200 chart with a cutoff `vartheta_alpha=1` on its support and that those enlarged supports retain uniformly bounded overlap;
2. verifying PF-200's uniform ellipticity/`C^1` bounds on both source and exact-area target metrics over those buffers;
3. applying the fixed-buffer local `H^2` estimate to the **global** resolvent equation `(Delta_k+1)u=f`, summing its squared local bounds, and checking (17) without multiplying by the number of windows;
4. checking the fixed torus/trivialization norm equivalence needed to identify `||Lambda J_alpha vartheta_alpha du||_2` with the local `H^1` norm of `vartheta_alpha du`;
5. applying the torus critical estimate separately to each transported matrix coefficient and using PF-198/PF-196 to prove (10);
6. checking the direct-sum counting identity (19) and the weak-ideal inequality (24);
7. expanding finite partial sums as in (23) and verifying that the coefficient-side cutoffs disappear because of (22), with no right/input cutoff inserted anywhere;
8. refusing to include any physical interface, collar-splice, scalar-density, or final identification term unless it separately satisfies the hypotheses of the same direct-sum construction or has another proved endpoint estimate.

PF-201 is refuted or must be narrowed if the regular enlarged windows do not have bounded overlap, if the source/target local `H^2` constants are not uniform for the actual global resolvents, if the torus transport used in PF-200 cannot be made compatible with the square-function bound, or if the coefficient partition does not reproduce the PF-175 regular-body form in the limit. A failure confined to the explicitly excluded interface/splice sectors would realize the stated boundary rather than refute the theorem.

## Consequences for the research line

PF-197--PF-200 progressively removed the local theorem, coefficient fragmentation, operator counting, and uniform principal-constant obstructions. PF-201 removes the remaining **regular-body external off-diagonal reassembly** by changing the factorization rather than estimating that remainder.

For the accepted weak-trace clue, the regular exact-area Lambert body is therefore no longer the main analytic bottleneck at the principal coefficient level. The next decisive work should concentrate on the infinite family of module-end/cuff and true-short-collar transition sectors, especially the endpoint conservative splice, and then on the lower-order/identification terms needed to assemble one complete first-relative-resolvent statement. A future global weak-`S_1` claim must still prove those pieces; PF-201 supplies only the regular-body sector.