# MC-166 — Finite Bost–Connes coefficient insertions preserve the two-sector Möbius phase grading

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `BOUNDARY/CONDITIONAL-GAIN`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue with the canonical number-state representation

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn},
\]

and the square-free phase family used in `MC-163`–`MC-165`,

\[
f_z(n)=
\begin{cases}
\displaystyle\prod_{p\mid n}z_p,&n\text{ squarefree},\\
0,&n\text{ otherwise},
\end{cases}
\qquad |z_p|=1,
\]

with diagonal `D_z\varepsilon_n=f_z(n)\varepsilon_n` and raw prime commutators

\[
C_p^{(z)}=[D_z,S_p].
\tag{1}
\]

Let

\[
\mathcal B=C^*(\mathbb Q/\mathbb Z)\cong C(\widehat{\mathbb Z})
\tag{2}
\]

be the Bost–Connes coefficient algebra in the same representation. Thus every `g\in C(\widehat{\mathbb Z})` acts diagonally by

\[
M_g\varepsilon_n=g(n)\varepsilon_n.
\tag{3}
\]

Consider an arbitrary finite **coefficient-decorated commutator word**

\[
W_z
=M_{g_r}X_rM_{g_{r-1}}\cdots X_2M_{g_1}X_1M_{g_0},
\tag{4}
\]

where every `g_j\in C(\widehat{\mathbb Z})` is fixed independently of the phase parameters `z_p`, and

\[
X_j=\begin{cases}
C_{p_j}^{(z)},&\sigma_j=+1,\\
(C_{p_j}^{(z)})^*,&\sigma_j=-1.
\end{cases}
\]

Write

\[
q(W)=\sum_{j=1}^r\sigma_j.
\tag{5}
\]

Fix a square-free input `n` and its divisibility pattern at the finite set of primes occurring in the word. If the induced basis-state path is illegal then `W_z\varepsilon_n=0`. Otherwise there is a final state `n_W` and a scalar factor `K_{W,\eta}(n;z)`, depending on the coefficient values along the path and on the finitely many local prime phases, such that

\[
\boxed{
W_z\varepsilon_n
=f_z(n)^{q(W)}K_{W,\eta}(n;z)\,\varepsilon_{n_W}.
}
\tag{6}
\]

The crucial point is that inserting arbitrary bounded Bost–Connes coefficient observables changes the **phase-free amplitude** but contributes no additional global input-phase charge.

At the Möbius specialization `z_p=-1` for every prime, `D_z=D_\mu` and on square-free inputs `f_z(n)=\mu(n)\in\{\pm1\}`. Since

\[
q(W)\equiv r\pmod2,
\tag{7}
\]

there exists an ordinary phase-free Bost–Connes operator `T_W\in\mathcal A_{BC}` such that

\[
\boxed{
W_{-1}P_{\rm sf}=T_WD_\mu^{\,r}P_{\rm sf}.
}
\tag{8}
\]

Hence every finite noncommutative polynomial made from raw commutators, their adjoints, and arbitrary coefficient-algebra insertions has the exact normal form

\[
\boxed{
A(\mathcal B,C,C^*)P_{\rm sf}
=T_0P_{\rm sf}+T_1D_\mu P_{\rm sf},
\qquad T_0,T_1\in\mathcal A_{BC}.
}
\tag{9}
\]

Thus the first source-forced escape left open by `MC-165` does **not** create a third Möbius phase sector. Finite coefficient insertions can supply profinite masks, divisibility projectors, and nontrivial transport weights, but at the phase level they still produce only an even sector with no Möbius orientation and an odd sector carrying one linear copy of the original `D_\mu` orientation.

Equation `(9)` is an information classification, not a cancellation theorem. A coefficient-decorated odd sector can still be quantitatively useful if the source-forced `T_1` has a genuinely favorable summation or conditioning property. The theorem says that such a gain must come from that phase-free weighting/transport theorem, not from a newly generated Möbius phase relation.

## 1. Diagonal coefficient insertions do not alter the state path or phase charge

The one-step formulas from `MC-165` are

\[
C_p^{(z)}\varepsilon_m
=b_p^{(z)}(m)\varepsilon_{pm},
\qquad
b_p^{(z)}(m)=f_z(pm)-f_z(m),
\tag{10}
\]

and

\[
(C_p^{(z)})^*\varepsilon_m
=\begin{cases}
\overline{b_p^{(z)}(m/p)}\,\varepsilon_{m/p},&p\mid m,\\
0,&p\nmid m.
\end{cases}
\tag{11}
\]

On a square-free predecessor `s`, every nonzero forward factor is `f_z(s)` times a scalar depending only on the local prime phase and whether `p\mid s`; every nonzero adjoint factor is `\overline{f_z(s)}` times the corresponding local scalar. As proved in `MC-165`, the only temporary squareful excursion in a nonzero raw path is a one-step repeated-prime excursion that must be undone by the matching adjoint before another commutator can contribute a nonzero finite-difference factor.

An inserted `M_g` is diagonal. It multiplies the current basis vector by `g(s)` and leaves the state unchanged. Therefore it neither creates a new path nor changes which predecessor supplies the next commutator coefficient. In particular, the set of square-free states at which the phase-bearing finite differences are evaluated is exactly the same as for the undecorated raw word.

Every such square-free evaluation state differs from the initial square-free `n` only by toggling primes in the finite word. Therefore

\[
f_z(s)=f_z(n)\chi_s(z),
\tag{12}
\]

where `\chi_s` is a Laurent monomial in only those local `z_p`. Multiplying the `r` commutator/adjoint factors gives

\[
f_z(n)^{N_+-N_-}=f_z(n)^{q(W)}.
\tag{13}
\]

All coefficient values `g_j(s_j)`, local finite-difference constants, and local Laurent monomials are absorbed into `K_{W,\eta}(n;z)`. This proves `(6)`.

The argument allows the coefficient elements themselves to be norm-completed elements of `C(\widehat{\mathbb Z})`; only the **number of insertions and commutator letters** is finite. No finite-character or bounded-conductor assumption is needed.

## 2. After Möbius specialization the stripped amplitudes are profinite-continuous on each path cell

Let `P(W)` be the finite prime set appearing in `(4)`. A local divisibility pattern `\eta` determines a clopen cylinder

\[
U_\eta\subset\widehat{\mathbb Z}
\tag{14}
\]

by prescribing, for each `p\in P(W)`, whether the input lies in `p\widehat{\mathbb Z}`. On any nonzero path cell, every intermediate basis state has the form

\[
s_j=\frac{m_j}{d_j}n
\tag{15}
\]

for fixed positive integers `m_j,d_j`, with the required divisibility by `d_j` already enforced by the clopen domain.

Multiplication by an integer is continuous on `\widehat{\mathbb Z}`, and division by `d_j` is continuous on the clopen subgroup `d_j\widehat{\mathbb Z}`. Consequently

\[
x\longmapsto g_j\!\left(\frac{m_j}{d_j}x\right)
\tag{16}
\]

is continuous on the corresponding path cell. At Möbius phase all remaining local finite-difference factors are fixed real constants determined by the finite support path. Hence, after stripping the factor `\mu(n)^r`, the path amplitude is the restriction of a continuous function on `U_\eta`.

The local support projections are themselves coefficient-algebra projections. In the canonical Bost–Connes representation

\[
P_p=S_pS_p^*
=\frac1p\sum_{ps=0}e(s),
\tag{17}
\]

so finite intersections of `P_p` and `I-P_p` lie in `\mathcal B`.

For a fixed cell the final state has the form `n_W=(m/d)n`. A continuous stripped weight `k(n)` on that cell is implemented by a standard crossed-product monomial of the form

\[
S_mM_hS_d^*P_{U_\eta},
\tag{18}
\]

with `h(y)=k(dy)` after absorbing the cell restriction into the coefficient. Such monomials belong to the Bost–Connes semigroup crossed product. Summing over the finitely many local support cells produces `T_W\in\mathcal A_{BC}` and proves `(8)`.

This step is stronger than merely saying the coefficients are independent of `z`: it locates the entire stripped finite-word transport back inside the ordinary phase-free Bost–Connes algebra.

## 3. Finite decorated polynomials form only two Möbius phase sectors

Let `A(\mathcal B,C,C^*)` be a finite linear combination of words `(4)`, allowing different lengths, primes, adjoint patterns, and coefficient insertions. Apply `(8)` to each monomial and split by commutator-word parity. The finite sum of even stripped transports is an operator `T_0\in\mathcal A_{BC}`, and the finite sum of odd stripped transports is `T_1\in\mathcal A_{BC}`. Since `D_\mu^2P_{\rm sf}=P_{\rm sf}`, equation `(9)` follows.

This gives a convenient module formulation of the boundary:

\[
\operatorname{Alg}_{\rm fin}(\mathcal B,\{C_p,C_p^*:p\in\mathbb P\})P_{\rm sf}
\subset
\mathcal A_{BC}P_{\rm sf}
+\mathcal A_{BC}D_\mu P_{\rm sf}.
\tag{19}
\]

The inclusion is the relevant statement; no claim is made that every operator on the right is generated by the decorated commutators.

The two summands have different information roles. The first can retain rich Bost–Connes arithmetic structure but no phase from the diagnostic family. The second contains exactly one terminal copy of the Möbius orientation, masked and transported by an ordinary Bost–Connes operator. Coefficient insertion can therefore improve the **quality of the mask** without changing the number of global Möbius phase degrees of freedom.

## 4. This sharpens, but does not eliminate, the coefficient-algebra escape

`MC-143` proved that the continuous coefficient algebra itself cannot uniformly encode the square-free Möbius sign with error below `1`. `MC-144` then showed that canonical number-state diagonals of arbitrary bounded Bost–Connes observables collapse to that same profinite-continuous coefficient class. `MC-165` classified finite raw commutator/adjoint words but explicitly left coefficient-algebra insertions outside scope.

Equation `(9)` connects those boundaries. Arbitrary continuous coefficient insertions at finite word depth do not synthesize a new phase carrier: after exact reduction they are absorbed into the ordinary Bost–Connes transports `T_0,T_1`. In particular, simply increasing coefficient conductor, replacing finite cyclotomic polynomials by arbitrary norm-completed coefficient elements, or interleaving such elements between more raw commutators does not escape the support-versus-linear-orientation phase classification.

There is nevertheless a genuine residual question. An odd-sector source-forced operator `T_1D_\mu` might have a better-conditioned aggregate readout than the raw `D_\mu` table even though it carries only one phase copy. Proving such a gain would require an independent estimate showing that the Bost–Connes weighting/transport makes the relevant partial sums easier to control without itself hiding a same-exponent Mertens statement. The present theorem does not rule that out.

## 5. Prior art and novelty audit

The Bost–Connes coefficient algebra, canonical number-state representation, and semigroup relations are classical; see J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411–457, DOI `10.1007/BF01589495`. The realization of the Bost–Connes algebra as a semigroup crossed product is standard; see M. Laca and I. Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, and M. Laca, *From Endomorphisms to Automorphisms and Back: Dilations and Full Corners*, Journal of the London Mathematical Society **61** (2000), 893–904, DOI `10.1112/S0024610799008492`.

More generally, homogeneous-word/gauge bookkeeping and the fact that degree-zero coefficient multipliers do not create a new crossed-product degree are standard operator-algebraic phenomena. The phase charge in `(6)` should not be confused with a claim that Mathia discovered a new general grading theorem.

A targeted search for Bost–Connes coefficient-decorated prime commutators, Möbius commutator words, coefficient insertions, and Möbius phase gradings did not locate this exact square-free specialization. Search absence is not evidence of novelty, and the derivation is elementary once the canonical represented action and the earlier `MC-165` path lemma are fixed. Accordingly the finding makes **no novelty claim**.

The durable delta is line-specific: `MC-165` left source-forced coefficient-algebra insertions as an explicit candidate escape. Equations `(6)`–`(9)` show exactly what finite insertions can and cannot change at the Möbius phase level.

## Boundaries and falsification tests

- **Square-free input sector.** Equations `(8)`–`(9)` are restricted on the right by `P_sf`. They classify the sector contributing nonzero Möbius coefficients, not arbitrary squareful starting states.
- **Finite operator depth.** There are finitely many commutator letters and coefficient insertions. Infinite series, resolvents, norm/strong closures of the decorated algebra, unbounded functional calculus, and limiting constructions are outside the theorem even though each inserted coefficient element may itself be norm-completed in `C(\widehat Z)`.
- **Coefficient algebra only.** The inserted source operators are diagonal elements of `C^*(Q/Z)`. Arbitrary semigroup/crossed-product operators inserted as independent new letters, modular conjugations, Hamiltonian functions, twisted commutators, or other non-diagonal source operations are not classified here.
- **Phase-independent coefficients.** The `g_j` are fixed independently of the diagnostic phase family. A `z`-dependent coefficient can inject phase by definition and requires a separate naturalness and circularity audit.
- **No claim that coefficients are arithmetically empty.** `T_0,T_1` may retain rich profinite, divisibility, and transport information. The theorem classifies Möbius orientation charge, not all arithmetic information.
- **No automatic conditioning gain.** The normal form does not imply that bounding an observable built from `T_1D_mu` is easier, equivalent, or harder than bounding `M(x)`. That transfer must be proved separately and tested against the conditioning/re-encoding barriers already exposed in `MC-158`–`MC-160`.
- **Target-tailored coefficient choices remain suspect.** `MC-143` rules out a single continuous coefficient function that uniformly recovers Möbius orientation, but finite-range or target-informed masks can still be chosen. Such choices are not validated merely because they lie in `\mathcal B`.
- **No RH input.** The proof uses exact basis action, profinite continuity, and finite path decomposition only. It invokes no zero-free region, contour shift, explicit formula, or RH-equivalent estimate.
- **Direct falsification.** A counterexample is a finite decorated word and square-free input for which `(6)` fails, or a Möbius-specialized word whose stripped amplitude cannot be represented by an ordinary Bost–Connes transport as in `(8)`. The diagonal coefficient steps and the one-step commutator formulas exhaust all letters of the stated word class.

## Consequence for the line

Finite source-forced Bost–Connes coefficient insertions do not escape the two-sector phase boundary. They can reshape the transport around the Möbius sign, including with arbitrary continuous profinite coefficients, but every finite decorated polynomial still reduces on square-free inputs to an ordinary Bost–Connes sector plus an ordinary Bost–Connes transport carrying one linear `D_\mu` factor.

The next useful coefficient-based question is therefore quantitative rather than representational: whether a **canonically forced** odd-sector transport `T_1` has an independently provable summation/conditioning advantage that survives the line's target-reencoding and matched-control tests. A route that claims success only because coefficient insertions look more noncommutative, or because they hide the sign inside an arbitrary mask, is now classified by `(9)` rather than opened as a new phase mechanism.