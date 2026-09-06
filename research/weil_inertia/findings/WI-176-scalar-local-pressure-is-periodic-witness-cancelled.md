# WI-176 — scalar local pressure is period-33 cancelled under a universal scalar tax

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ROUTE-SPECIFIC-BARRIER + CLASSICAL-FRAMEWORK + NO-NOVELTY-CLAIM`. WI-175 proved period-33 cancellation for every fixed nonnegative linear gap pressure. The same obstruction is in fact independent of linearity: an arbitrary translation-covariant scalar local potential, including a nonlinear or source-conditioned one, cannot evade the witness if the global proof ultimately replaces that potential by one universal scalar tax valid on the same witness class. The only load-bearing ingredients are phase averaging, the interval-certified WI-019 witness, and the fact that a universal scalar tax must dominate the witness's own normalized potential average.

No unconditional simple-critical-zero proportion changes here. The finding closes a proof architecture that the live source-cover clue still listed as a possible escape.

## 1. Abstract scalar-potential architecture

Fix a block size `m>=2`. For an ordered `m`-point Montgomery--Taylor translation Gram block `B`, let

\[
D(B)=\operatorname{tr}\Psi(G_B)
\]

be the same single-profile Gram defect used throughout WI-011--WI-026. Let `P(B)` now be **any real-valued translation-covariant scalar local potential** defined on the block state. It may be nonlinear in the consecutive gaps, may use several gaps jointly, and may depend on source quantities such as the MT kernel values determined by those gaps. No linear decomposition `P=\sum_j\alpha_jg_j` is assumed.

Suppose a universal local theorem proves

\[
\boxed{D(B)+P(B)\ge C}
\tag{1}
\]

for every block in the intended deterministic source class, with `C>=0` for the nontrivial lower-bound regime.

Suppose further that the global shifted-block assembly retains `P` only through a **single universal scalar tax** `\tau` and produces

\[
\boxed{
R(C,\tau)=\frac{mH_{\rm MT}-\tau}{m-C},
\qquad 0\le C<m,
\qquad mH_{\rm MT}-\tau>0.
}
\tag{2}
\]

The normalization in (2) means that after averaging block positions, the total contribution of `P` per ambient zero is bounded above by `\tau/m`. The precise derivation of the tax is irrelevant here. What matters is universality: when the same accounting is evaluated on the admissible period-33 witness of density `r`, it must pay at least that witness's normalized scalar-potential average.

This includes WI-175 as the special case `P(B)=\sum_j\alpha_jg_j`, where the phase average is `\bar P=A/r` and the tax is `\tau=A`.

## 2. Period-33 phase average

Use the interval-certified positive periodic MT configuration from WI-019/WI-026. Its retained density is

\[
r=\frac{67361}{100000},
\tag{3}
\]

its full directed pair energy per atom satisfies

\[
d<d_*:=
\frac{1637}{10^6}
+
\frac{45379580714321}{74507812500000000000},
\tag{4}
\]

and WI-026 records

\[
H_{\rm MT}<H_*:=\frac{672500704}{10^9},
\tag{5}
\]

with exact margin

\[
\delta:=r(1-d_*)-H_*
=
\frac{46091743024440123119}
{7450781250000000000000000}
>\frac6{10^6}.
\tag{6}
\]

Cut the infinite witness at each of its `33` starting phases. Let `B_a` be the resulting `m`-point block and write

\[
D_a:=D(B_a),\qquad P_a:=P(B_a),\qquad
\bar P:=\frac1{33}\sum_{a=1}^{33}P_a.
\tag{7}
\]

WI-026's positive-energy argument is independent of the pressure and gives

\[
\boxed{
\frac1{33}\sum_{a=1}^{33}D_a<md_*.
}
\tag{8}
\]

Averaging the universal local inequality (1) over all phases therefore yields

\[
\boxed{C<md_*+\bar P.}
\tag{9}
\]

No formula for `\bar P` is needed. This is the point at which linearity disappears from the argument.

## 3. A universal scalar tax must pay the witness average

Under the normalization of (2), one block of `m` retained points contributes one local scalar potential value before the complete shift average. The period-33 witness has retained-point density `r` relative to the ambient normalization. Therefore its potential contribution per ambient zero is

\[
r\bar P.
\]

If `\tau` is a universal scalar upper tax for the same deterministic accounting class, it must satisfy

\[
\boxed{\tau\ge r\bar P.}
\tag{10}
\]

This is the exact general replacement for WI-175's identity `A=r(A/r)`. If the proposed global tax is obtained from a zeta-specific restriction that the period-33 configuration does not satisfy, then (10) need not hold and the present theorem does not apply; that is a genuine escape rather than a loophole in the calculation.

## 4. Exact cancellation is independent of the shape of `P`

Subtract the assembled output (2) from the witness density. Since `m-C>0`,

\[
\begin{aligned}
r-R(C,\tau)
&=
\frac{r(m-C)-mH_{\rm MT}+\tau}{m-C}\\
&=
\frac{m(r-H_{\rm MT})-rC+\tau}{m-C}.
\end{aligned}
\tag{11}
\]

Using (9), (10), and `H_{\rm MT}<H_*`,

\[
\begin{aligned}
m(r-H_{\rm MT})-rC+\tau
&>m(r-H_*)-r(md_*+\bar P)+\tau\\
&=m\bigl(r(1-d_*)-H_*\bigr)
   +(\tau-r\bar P)\\
&\ge m\delta.
\end{aligned}
\tag{12}
\]

Hence

\[
\boxed{
r-R(C,\tau)>\frac{m\delta}{m-C}.
}
\tag{13}
\]

Because `0<=C<m`, the factor `m/(m-C)>=1`. Equation (6) therefore gives

\[
r-R(C,\tau)>\delta>\frac6{10^6}.
\tag{14}
\]

With `r=0.673610`, every nontrivial instance of (1)--(2) satisfying the universal-tax condition (10) obeys

\[
\boxed{
R(C,\tau)<\frac{673604}{10^6}=0.673604.
}
\tag{15}
\]

The same exact ceiling as WI-026/WI-175 survives, but now the local scalar potential may be arbitrarily nonlinear and finite-range/source-conditioned.

## 5. What is actually closed

The obstruction does not say that nonlinear source information is useless. It says that **nonlinearity is lost if the global proof compresses it back to one universal scalar tax**. The period-33 orbit then supplies both sides of the dual accounting: it upper-bounds the universal local floor through (9) and lower-bounds the scalar tax through (10), leaving only its already-certified Gram-defect margin.

Thus the following variants do not constitute an escape by themselves:

- replacing a linear gap pressure by `P(g_i,g_{i+1},...)` with arbitrary nonlinear finite interaction range;
- conditioning `P` on local MT kernel values or other source variables determined by the same periodic block;
- using several scalar local terms and then summing them into one scalar potential before applying one universal global tax;
- adding a finite-memory/coboundary correction to `P`, since its period average vanishes and therefore does not change `\bar P`.

A genuine escape must break a hypothesis above. Examples are a global assembly that retains a vector/state-resolved observable rather than one scalar tax, a source-specific global constraint that actually excludes the WI-019 periodic witness, several independent profiles whose information is not compressed to one scalar local potential, coupling to the exceptional indefinite block, or new arithmetic/support information.

## 6. Prior-art and novelty audit

The abstract language is classical. Ergodic optimization studies suprema of `\int P\,d\mu` over invariant measures; a periodic configuration supplies an invariant measure and therefore a mandatory lower test for any universal scalar supremum. See Oliver Jenkinson, *Ergodic Optimization*, DCDS 15 (2006), 197--224, DOI `10.3934/dcds.2006.15.197`. For finite-range/locally constant observables on subshifts, the rotation-set framework and density of periodic rotation vectors are classical; see Krystyna Ziemian, *Rotation sets for subshifts of finite type*, Fundamenta Mathematicae 146 (1995), 189--201, DOI `10.4064/fm-146-2-189-201`.

Inside the zeta-specific corpus, WI-014 already uses the classical zero-periodic-mean obstruction for Bellman coboundaries; WI-026 phase-averages one fixed four-point pressure; WI-175 extends that calculation to every nonnegative linear position-weighted gap pressure. The public `tawanerguo-cn/zeta-simple-zeros` Bellman development likewise uses finite-memory potentials/coboundaries, but the targeted audit found no established statement there or in the `trmdy` follow-up that derives the general nonlinear scalar-tax cancellation (9)--(15) from the WI-019 period-33 witness. Absence of such a statement is not a priority claim.

The durable Mathia contribution is therefore route-specific: the clue's remaining phrase “nonlinear/source-conditioned pressure” is not by itself an escape. It survives only if its **global accounting remains non-scalar or witness-excluding**.

## 7. Consequence for the live source-cover program

WI-175 showed that pressure-vector shape disappears under full phase averaging. WI-176 shows that even preserving nonlinear local shape does not help if the global bridge subsequently remembers only one universal scalar tax. The next source-cover attempt should therefore carry source/state information through the global assembly itself rather than design a more elaborate local scalar penalty and scalarize it at the end.

A decisive positive test must exhibit the non-scalar object that survives summation and explain why the period-33 invariant measure cannot simultaneously saturate its components. A decisive negative test may instead construct a source-realizable periodic/aperiodic family that saturates that richer object. Merely changing the formula for a scalar local pressure is now a closed route above `67.3604%` under the hypotheses of this finding.