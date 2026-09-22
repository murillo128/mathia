# NB-283 — first-free jet neutralization factors exactly through reduced zero sampling

- **Date:** 2026-09-22
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-052, NB-280, NB-281, NB-282
- **Classification:** `EXACT-DERIVED + BLASCHKE-DEFLATION + FIRST-FREE-JET-COST + REDUCED-ZERO-SAMPLING + PYTHAGOREAN-EXCESS + NB-282-STRENGTHENING + NEGATIVE/ROUTE-NARROWING + PRIOR-ART-AUDITED`

## Claim

`NB-282` shows that the first source-dependent residual jet at a finite packet of zeta zeros can be neutralized by an actual finite Dirichlet source with only `N` active atoms and with an explicit cutoff satisfying `log M=O(N log N)`. It leaves open whether that neutralization is expensive in the actual Nyman/Hardy synthesis norm.

There is an exact first reduction of that norm question. After removing the forced zeta zero divisor, the first-free-jet constraints become **ordinary value interpolation at the distinct zero sites**. Consequently the unrestricted ambient `H^2` cost is not a new jet coercivity: it is exactly a scalar multiple of the reduced zero-sampling/Burnol defect already identified in `NB-280`.

Let

\[
Z=\{(\rho_j,m_j):1\le j\le N\}
\tag{1}
\]

be a finite packet of distinct nontrivial zeta zeros with `Re rho_j>1/2`, where `m_j` is the actual multiplicity. Let

\[
B_Z(s)=\prod_{j=1}^N b_{\rho_j}(s)^{m_j}
\tag{2}
\]

be the finite half-plane Blaschke product carrying the actual multiplicities, with arbitrary unimodular normalization, and let

\[
B_{\mathrm{red}}(s)=\prod_{j=1}^N b_{\rho_j}(s)
\tag{3}
\]

be the **reduced** product carrying each distinct site once, with any unimodular normalization.

For a finite Dirichlet polynomial

\[
P(s)=\sum_{n\le M}a_n n^{-s},
\qquad
Q_P(s)=P(s)-P(1),
\tag{4}
\]

define the Nyman source term and residual

\[
F_P(s):=\frac{\zeta(s)}sQ_P(s),
\qquad
r_P(s)=\frac1s-F_P(s).
\tag{5}
\]

The factor `Q_P(1)=0` removes the pole of `zeta` at `s=1`, so `F_P` is an admissible `H^2(Re s>1/2)` source term. Since `zeta` vanishes to order `m_j` at every `rho_j`, there is a unique

\[
h_P\in H^2(\Re s>1/2)
\tag{6}
\]

such that

\[
F_P=B_Zh_P,
\qquad
\|F_P\|_{H^2}=\|h_P\|_{H^2}.
\tag{7}
\]

Let

\[
p_Z(s)
=P_{K_{B_Z}}k_1(s)
=\frac{1-\overline{B_Z(1)}B_Z(s)}s,
\qquad
k_1(s)=\frac1s.
\tag{8}
\]

Then the following are equivalent:

\[
r_P^{(m_j)}(\rho_j)=p_Z^{(m_j)}(\rho_j)
\quad(1\le j\le N),
\tag{9}
\]

and

\[
\boxed{
 h_P(\rho_j)=\frac{\overline{B_Z(1)}}{\rho_j}
 \quad(1\le j\le N).
}
\tag{10}
\]

Thus the first free jet problem becomes ordinary point sampling after division by the full zero divisor.

The minimum ambient Hardy cost of `(10)` is

\[
\boxed{
\mathcal C_{\mathrm{amb}}(Z)
=
|B_Z(1)|^2
\bigl(1-|B_{\mathrm{red}}(1)|^2\bigr).
}
\tag{11}
\]

One minimizer is

\[
h_*(s)
=
\overline{B_Z(1)}\,p_{\mathrm{red}}(s),
\qquad
p_{\mathrm{red}}(s)
=
\frac{1-\overline{B_{\mathrm{red}}(1)}B_{\mathrm{red}}(s)}s.
\tag{12}
\]

Every feasible finite Nyman source admits the exact orthogonal decomposition

\[
\boxed{
\|F_P\|_{H^2}^2
=
\mathcal C_{\mathrm{amb}}(Z)
+
\|h_P-h_*\|_{H^2}^2.
}
\tag{13}
\]

Therefore the only possible strengthening supplied by the finite arithmetic source restriction is the nonnegative **restricted synthesis excess** above the ambient zero-sampling floor.

If

\[
\mathcal C_M(Z)
:=
\inf\left\{
\|F_P\|_{H^2}^2:
\begin{array}{l}
P\text{ is supported in }\{1,\ldots,M\},\\
P\text{ satisfies the first-free-jet conditions }(9)
\end{array}
\right\},
\tag{14}
\]

with `+infinity` when the affine constraint is infeasible, define

\[
\boxed{
\mathfrak E_M(Z)
:=
\mathcal C_M(Z)-\mathcal C_{\mathrm{amb}}(Z)
\ge0.
}
\tag{15}
\]

Whenever the finite section is feasible,

\[
\boxed{
\mathfrak E_M(Z)
=
\inf_{P\text{ feasible}}
\|h_P-h_*\|_{H^2}^2.
}
\tag{16}
\]

`NB-282` guarantees feasibility for an explicit cutoff `M_Z` with

\[
\log M_Z=O(N\log N).
\tag{17}
\]

Hence first-free-jet neutralization now has an exact two-part price: a universal Burnol-scale ambient term `(11)` plus the genuinely source-native finite-section excess `(15)`.

## 1. Deflating the forced multiplicity divisor

The source term `(5)` has a zero of order at least `m_j` at every `rho_j`, because `zeta` has exactly that order and `Q_P/s` is holomorphic there. For a finite Blaschke product, division by the corresponding inner factor preserves membership and norm in the half-plane Hardy space. Thus

\[
F_P=B_Zh_P,
\qquad
\|F_P\|_2=\|h_P\|_2.
\tag{18}
\]

No asymptotic or zero-separation input is used here.

Differentiate `(5)` exactly `m_j` times at `rho_j`. All derivatives of `zeta` below order `m_j` vanish, so Leibniz gives

\[
F_P^{(m_j)}(\rho_j)
=
\frac{\zeta^{(m_j)}(\rho_j)}{\rho_j}
Q_P(\rho_j).
\tag{19}
\]

Likewise, because `B_Z` has a zero of exact order `m_j`, `(18)` gives

\[
F_P^{(m_j)}(\rho_j)
=
B_Z^{(m_j)}(\rho_j)h_P(\rho_j).
\tag{20}
\]

`NB-281`--`NB-282` identify neutralization of the first source-dependent jet relative to `(8)` with

\[
Q_P(\rho_j)
=
\overline{B_Z(1)}
\frac{B_Z^{(m_j)}(\rho_j)}
     {\zeta^{(m_j)}(\rho_j)}.
\tag{21}
\]

Substituting `(21)` into `(19)` yields

\[
F_P^{(m_j)}(\rho_j)
=
\overline{B_Z(1)}
\frac{B_Z^{(m_j)}(\rho_j)}{\rho_j}.
\tag{22}
\]

Comparing `(22)` with `(20)` and using `B_Z^{(m_j)}(rho_j) != 0` gives exactly `(10)`.

Conversely, `(10)` inserted into `(20)` recovers `(22)`, hence `(21)` and the first-free-jet identity `(9)`. Thus the reduction is an equivalence, not merely a lower bound.

The lower jets `0,...,m_j-1` need no extra condition: both the legal residual and the finite Burnol minimizer already share them by the multiplicity argument of `NB-281`.

## 2. The ambient cost is reduced zero sampling

After the division `(18)`, multiplicity no longer creates Hermite data. The quotient is constrained only by the `N` distinct point values `(10)`. This is why the relevant interpolation geometry uses `B_red`, not the multiplicity-weighted `B_Z`.

Set

\[
v_j=\frac1{\rho_j},
\qquad
c_Z=\overline{B_Z(1)}.
\tag{23}
\]

The constraints are simply

\[
h(\rho_j)=c_Zv_j.
\tag{24}
\]

`NB-280`, applied to the reduced packet, gives

\[
\inf_{h(\rho_j)=v_j}\|h\|_{H^2}^2
=
1-|B_{\mathrm{red}}(1)|^2,
\tag{25}
\]

with minimizer `p_red` from `(12)`. Scaling by `c_Z` proves `(11)`--`(12)`.

Equivalently, if

\[
G^{\mathrm{red}}_{jk}
=
\frac1{\rho_j+\overline{\rho_k}-1},
\tag{26}
\]

then

\[
\mathcal C_{\mathrm{amb}}(Z)
=
|B_Z(1)|^2
v^*(G^{\mathrm{red}})^{-1}v.
\tag{27}
\]

By `NB-280`, the quadratic form in `(27)` is exactly `1-|B_red(1)|^2`. Thus a zero-sampling inverse Gram has not reappeared as an independent source obstruction; it is the same finite model-space defect after the forced multiplicity divisor is removed.

For simple zeros, `B_Z=B_red=:B`, so

\[
\boxed{
\mathcal C_{\mathrm{amb}}(Z)
=
|B(1)|^2\bigl(1-|B(1)|^2\bigr).
}
\tag{28}
\]

Writing the finite Burnol defect as

\[
\delta_Z^2=1-|B(1)|^2,
\tag{29}
\]

this becomes

\[
\mathcal C_{\mathrm{amb}}(Z)
=(1-\delta_Z^2)\delta_Z^2.
\tag{30}
\]

So in any regime where the finite Burnol defect is already small, first-free-jet neutralization has the same small ambient scale; it does not create an order-one Hardy floor by itself.

For arbitrary multiplicities,

\[
|B_Z(1)|\le |B_{\mathrm{red}}(1)|<1,
\tag{31}
\]

and therefore

\[
\boxed{
\mathcal C_{\mathrm{amb}}(Z)
\le
1-|B_{\mathrm{red}}(1)|^2
\le
1-|B_Z(1)|^2.
}
\tag{32}
\]

Thus higher multiplicity does not restore universal ambient coercivity at this first-free-jet level.

## 3. Exact Pythagorean separation of the arithmetic excess

Every feasible quotient `h_P` and the ambient minimizer `h_*` have the same values at all distinct sites. Hence

\[
h_P-h_*
\tag{33}
\]

vanishes at every `rho_j`. For a finite reduced Blaschke product this is equivalent to

\[
h_P-h_*=B_{\mathrm{red}}g_P
\tag{34}
\]

for some `g_P in H^2`.

On the other hand,

\[
h_*\in K_{B_{\mathrm{red}}}
:=H^2\ominus B_{\mathrm{red}}H^2.
\tag{35}
\]

Therefore

\[
\langle h_*,h_P-h_*\rangle=0,
\tag{36}
\]

and

\[
\|h_P\|_2^2
=
\|h_*\|_2^2+
\|h_P-h_*\|_2^2.
\tag{37}
\]

Using `(18)` and `(11)` proves `(13)`. Taking the infimum over the finite Nyman section proves `(15)`--`(16)`.

This is the useful boundary: the ambient Hardy problem is solved exactly, while all arithmetic difficulty is pushed into the distance from `h_*` to the **restricted quotient family** generated by legal finite Nyman sources.

Define

\[
\mathcal H_{M,Z}
:=
\left\{
\frac{\zeta(s)Q_P(s)}{sB_Z(s)}:
P\text{ supported in }\{1,\ldots,M\}
\right\}
\subset H^2.
\tag{38}
\]

Then the feasible affine slice is

\[
\mathcal A_{M,Z}
:=
\left\{
h\in\mathcal H_{M,Z}:
 h(\rho_j)=\frac{\overline{B_Z(1)}}{\rho_j}
 \text{ for every }j
\right\},
\tag{39}
\]

and

\[
\boxed{
\mathfrak E_M(Z)
=
\operatorname{dist}_{H^2}
\bigl(h_*,\mathcal A_{M,Z}\bigr)^2.
}
\tag{40}
\]

The notation in `(40)` means the infimum of the squared distance from `h_*` to the affine set; it does not assert that the infimum is attained for every finite section.

## 4. Relation to the finite synthesis matrix of NB-282

The exact decomposition also identifies what the matrix proposed in `NB-282` is measuring.

For `2<=n<=M`, let

\[
\Phi_n(s)
=
\frac{\zeta(s)}s\bigl(n^{-s}-n^{-1}\bigr),
\tag{41}
\]

let

\[
R_M=(\langle\Phi_n,\Phi_m\rangle)_{2\le n,m\le M},
\tag{42}
\]

and let

\[
U_{j,n}=n^{-\rho_j}-n^{-1}.
\tag{43}
\]

The first-free-jet target in the original Dirichlet coordinates is

\[
y_j^*
=
\overline{B_Z(1)}
\frac{B_Z^{(m_j)}(\rho_j)}
     {\zeta^{(m_j)}(\rho_j)}.
\tag{44}
\]

Whenever `U` has full row rank, the least finite-section synthesis cost is the standard constrained quadratic minimum

\[
\boxed{
\mathcal C_M(Z)
=
(y^*)^*
\bigl(U R_M^{-1}U^*\bigr)^{-1}
y^*.
}
\tag{45}
\]

The natural atoms `(41)` are linearly independent, so `R_M` is positive definite. `NB-282` supplies an explicit subcollection of `N` columns of `U` with nonzero determinant once `M` reaches its stated sparse cutoff, and therefore guarantees the full-row-rank hypothesis there.

Combining `(45)` with `(11)`--`(16)` gives the exact factorization

\[
\boxed{
(y^*)^*
\bigl(U R_M^{-1}U^*\bigr)^{-1}
y^*
=
|B_Z(1)|^2
\bigl(1-|B_{\mathrm{red}}(1)|^2\bigr)
+
\mathfrak E_M(Z).
}
\tag{46}
\]

Thus the inverse finite-section form suggested in `NB-282` contains two logically distinct pieces. The first is already determined by universal Hardy/Blaschke geometry. The second is the actual finite arithmetic synthesis penalty.

Equation `(46)` is not an estimate of `mathfrak E_M`. It isolates the quantity that must now be estimated.

## 5. Boundaries and adversarial checks

Several distinctions are load-bearing.

First, the ambient minimizer

\[
F_*=B_Zh_*
\tag{47}
\]

is an `H^2` function with exactly the required local jet data, but **need not be realizable by any finite Dirichlet/Nyman section**. Claiming otherwise would erase precisely the arithmetic restriction measured by `mathfrak E_M`.

Second, the full multiplicity product `B_Z` and the reduced product `B_red` play different roles. `B_Z` is forced by the zero divisor of `zeta` and is what may be divided out of every source term. After that division, the first-free-jet conditions become one ordinary value constraint per distinct site, so the interpolation defect is controlled by `B_red`. Replacing `B_red` by `B_Z` in `(11)` would incorrectly count already-deflated multiplicity information a second time.

Third, `(10)` uses the **actual** multiplicities and the actual nonzero derivatives `zeta^{(m_j)}(rho_j)`. No simplicity assumption enters the theorem. The simple-zero formula `(28)` is only a corollary.

Fourth, the argument is finite. No infinite Blaschke product, limit interchange, meromorphic continuation across a limiting divisor, or asymptotic density statement is needed. It therefore does not conflict with the finite-versus-infinite obstruction isolated in `NB-278`.

Fifth, this result does not assert that right-half zeros exist, that a Ford compatibility packet is realized by actual zeta zeros, or that `mathfrak E_M` is small. It says that **if** a finite packet of actual zeros is given, the unrestricted first-free-jet Hardy cost factors as `(11)`, and any stronger finite-Nyman obstruction must live in the excess `(15)`.

A direct falsification checklist is:

- find a legal finite source `F_P` for which division by the finite inner factor `B_Z` changes the Hardy norm;
- find a packet for which `(19)` or `(20)` fails at the actual multiplicity;
- find a neutralizing source satisfying `(21)` but violating the quotient values `(10)`;
- find a quotient satisfying `(10)` whose ambient minimum is not `(11)`;
- find a feasible source for which the orthogonal decomposition `(13)` fails;
- find a full-rank finite section for which the constrained minimum `(45)` differs from the left side of `(46)`.

Each item is an exact functional-analytic or finite-dimensional identity, not a numerical heuristic.

## 6. Prior-art and novelty audit

The Hardy/model-space ingredients used above are classical: finite Blaschke division, `H^2=K_B\oplus BH^2`, reproducing-kernel interpolation, and the minimum-norm interpolant at finitely many points. `NB-280` already records the line-specific identification of the canonical data `1/rho_j` with the finite Burnol defect. No novelty is claimed for those ingredients.

A fresh literature audit also finds the established local-interpolation bridge between the classical half-plane Hardy space and Hilbert spaces of ordinary Dirichlet series. In particular, Olsen--Seip show that bounded sequences in `Re s>1/2` have the same interpolation status for the square-summable Dirichlet-series Hilbert space and classical `H^2`, and later work develops related zero-set/local interpolation results. Those results reinforce that unrestricted analytic or Dirichlet-series interpolation should not itself be mistaken for a Nyman-specific obstruction.

They do not, however, identify the rank-dependent affine family `(39)`, preserve the special `zeta Q_P/s` synthesis geometry under a natural finite cutoff, or estimate the excess `(40)` for the neutralizing data `(44)`. The line-local content here is therefore the exact collision of `NB-281`--`NB-282` with the Blaschke quotient: it shows that the ambient part of the first-free-jet synthesis cost is already exhausted by reduced zero sampling and isolates the remaining finite Nyman penalty as `mathfrak E_M`.

No new external theorem is load-bearing beyond the standard Hardy/Blaschke interpolation machinery already represented in `SOURCES.md`. The fresh Dirichlet-series interpolation literature is contextual rather than required for the proof, so `SOURCES.md` does not change.

## 7. Consequence for the research frontier

`NB-282` removed support length as a plausible first-free-jet obstruction once `log M` exceeds the explicit `O(N log N)` threshold. The present factorization removes a second possible false lead: the unrestricted Hardy norm needed to realize those jet values is not a new source-native quantity either.

The next finite question is therefore sharply separated from zero-only geometry:

\[
\boxed{
\text{estimate }\mathfrak E_M(Z)
=
\operatorname{dist}_{H^2}
\bigl(h_*,\mathcal A_{M,Z}\bigr)^2
\text{ at the Ford-coupled cutoff.}
}
\tag{48}
\]

A lower bound of order one for `(48)` would be genuinely arithmetic: it would say that finite legal Nyman sources stay a macroscopic distance from an ambient Hardy interpolant that already has the correct first-free jets. Conversely, a construction with `mathfrak E_M(Z)=o(1)` for the relevant packet/cutoff would close the first-free-jet route even at the synthesis-cost level and force the investigation toward higher/global data or a different observable.

This target is stricter than ordinary interpolation. It asks for quantitative approximation of a **specific** model-space minimizer by a finite, zeta-weighted Dirichlet quotient family under a coupled cutoff. General local interpolation theorems do not by themselves provide that rate.

## Conclusion

First-free Nyman jet neutralization has an exact quotient-space factorization. Dividing the legal source term by the full multiplicity Blaschke product converts the free-jet conditions into the ordinary values

\[
h(\rho_j)=\frac{\overline{B_Z(1)}}{\rho_j}.
\]

The minimum ambient Hardy cost is therefore exactly

\[
|B_Z(1)|^2
\bigl(1-|B_{\mathrm{red}}(1)|^2\bigr),
\]

and every finite Nyman realization pays that universal amount plus the orthogonal excess `mathfrak E_M(Z)`. Thus neither finite support length nor unrestricted first-free-jet Hardy interpolation is the missing coercivity. The remaining live quantity is the restricted finite Nyman synthesis gap `(48)`, which is now separated cleanly from the Burnol/Blaschke defect.