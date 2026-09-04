# AF-108 — Schatten budgets preserve membership; trace and determinant fidelity need tightness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-SCHATTEN-DUALITY`, `TRACE-ESCAPE-OBSTRUCTION`, `CATEGORY-VS-OBSERVABLE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a separable infinite-dimensional complex Hilbert space and let

\[
\mathcal S_p(H),\qquad 1\le p<\infty,
\]

be the Schatten ideals with norms `\|\cdot\|_p`.

AF-106 showed that a stagewise operator constraint survives an assembly when it is closed in the topology actually supplied by that assembly. AF-107 showed that compactness is not preserved merely because every finite stage is compact: collective compactness is the extra family-level gate. Schatten ideals sharpen this distinction because a **uniform ideal-norm budget** already closes the operator category, while scalar observables such as trace and Fredholm determinant can still lose information inside that preserved category.

### 1. A finite Schatten budget is exactly the WOT membership gate

Suppose a net `(T_i)` satisfies

\[
T_i\in\mathcal S_p(H),
\qquad
\sup_i\|T_i\|_p\le C,
\qquad
T_i\longrightarrow T
\quad\text{in WOT in }\mathcal L(H).
\tag{1}
\]

Then

\[
\boxed{T\in\mathcal S_p(H),\qquad \|T\|_p\le C.}
\tag{2}
\]

Equivalently, every closed `\mathcal S_p` ball is WOT-closed as a subset of `\mathcal L(H)`.

Define the WOT Schatten-accessibility cost

\[
a_p^{\rm WOT}(T)
:=
\inf\Bigl\{
\sup_i\|T_i\|_p:
T_i\in\mathcal S_p(H),\ T_i\to T\text{ in WOT}
\Bigr\},
\tag{3}
\]

with `\inf\varnothing=+\infty`. Then

\[
\boxed{
a_p^{\rm WOT}(T)=
\begin{cases}
\|T\|_p,&T\in\mathcal S_p(H),\\[1mm]
+\infty,&T\notin\mathcal S_p(H).
\end{cases}}
\tag{4}
\]

Thus, unlike bare compactness, membership in a finite Schatten class is stable under WOT assembly once the **correct resource norm** is kept uniformly bounded.

### 2. Stagewise Schatten membership without the budget is not enough

Let `(e_n)` be an orthonormal basis and let `Q_n` be the projection onto

\[
\operatorname{span}\{e_1,\ldots,e_n\}.
\tag{5}
\]

Then every `Q_n` has finite rank, hence lies in every `\mathcal S_p`, and

\[
Q_n\longrightarrow I_H
\quad\text{strongly, hence in WOT}.
\tag{6}
\]

But

\[
\|Q_n\|_p=n^{1/p}\longrightarrow\infty,
\qquad
I_H\notin\mathcal S_p(H).
\tag{7}
\]

Therefore

\[
\boxed{
T_i\in\mathcal S_p\text{ for every }i
\not\Rightarrow
\operatorname{WOT}\!\!-\!\lim_iT_i\in\mathcal S_p.
}
\tag{8}
\]

The distinction is not "finite rank versus infinite rank" but **unbudgeted versus uniformly budgeted ideal geometry**.

### 3. Trace-class membership can survive while trace and determinant do not

For each `n`, let

\[
P_n=|e_n\rangle\langle e_n|
\tag{9}
\]

be the rank-one projection onto `\mathbb Ce_n`. Then

\[
P_n\ge0,
\qquad
\|P_n\|_1=\operatorname{Tr}(P_n)=1,
\qquad
P_n\longrightarrow0\text{ in WOT}.
\tag{10}
\]

Part 1 correctly retains the trace-class category: the limit `0` is trace class. But

\[
\operatorname{Tr}(P_n)=1
\not\longrightarrow
0=\operatorname{Tr}(0).
\tag{11}
\]

The same escape is visible to the Fredholm determinant. For every `z\in\mathbb C`,

\[
\det(I+zP_n)=1+z,
\qquad
\det(I+z\,0)=1.
\tag{12}
\]

Hence

\[
\boxed{
\text{WOT fidelity of the trace-class category}
\not\Rightarrow
\text{fidelity of trace or Fredholm determinant}.
}
\tag{13}
\]

The lost datum is not trace-class membership. It is **where the trace mass lives**: the unit mass in (9) moves through mutually orthogonal modes and becomes invisible to every fixed finite-dimensional/compact observation while remaining visible to the identity operator used by the trace.

### 4. For positive trace-class families, no trace-mass escape is the exact trace gate

Let `(A_i)` be a net of positive trace-class operators such that

\[
A_i\ge0,
\qquad
A_i\to A\text{ in WOT},
\qquad
\sup_i\operatorname{Tr}(A_i)<\infty.
\tag{14}
\]

By part 1, `A\in\mathcal S_1(H)` and `A\ge0`. Moreover

\[
\boxed{
\operatorname{Tr}(A)
\le
\liminf_i\operatorname{Tr}(A_i).
}
\tag{15}
\]

Fix any increasing sequence of finite-rank orthogonal projections

\[
E_m\uparrow I_H
\quad\text{strongly}.
\tag{16}
\]

Then the following are equivalent:

\[
\boxed{
\operatorname{Tr}(A_i)\to\operatorname{Tr}(A)
}
\tag{17}
\]

and

\[
\boxed{
\lim_{m\to\infty}
\limsup_i
\operatorname{Tr}\bigl((I-E_m)A_i\bigr)=0.
}
\tag{18}
\]

Equation (18) is a trace-tightness condition: eventually, uniformly along the net tail, arbitrarily little positive trace mass remains outside one finite-dimensional window. It is exactly what fails for `(P_n)` in (9).

The criterion is basis-independent in substance. Equivalently, for every `\varepsilon>0` there is a finite-rank projection `E` such that eventually

\[
\operatorname{Tr}((I-E)A_i)<\varepsilon.
\tag{19}
\]

### 5. Positivity plus trace conservation upgrades WOT to trace norm and restores determinants

Under (14), if the equivalent conditions (17)--(18) hold, then

\[
\boxed{
\|A_i-A\|_1\longrightarrow0.
}
\tag{20}
\]

Consequently the Fredholm determinants converge locally uniformly:

\[
\boxed{
\det(I+zA_i)\longrightarrow\det(I+zA)
\quad\text{locally uniformly for }z\in\mathbb C.
}
\tag{21}
\]

Thus the positive trace-class hierarchy has three genuinely different levels:

\[
\boxed{
\begin{array}{c}
\sup_i\|A_i\|_1<\infty + \mathrm{WOT}
\Rightarrow
\text{trace-class membership survives},\\[1mm]
\text{plus trace tightness}
\Longleftrightarrow
\text{trace survives},\\[1mm]
\text{positivity + trace survival}
\Rightarrow
\mathcal S_1\text{-norm convergence}
\Rightarrow
\text{Fredholm determinant survives}.
\end{array}}
\tag{22}
\]

This separates **category fidelity** from **observable fidelity** and identifies the missing coherence datum explicitly.

## Derivation

### 1. Schatten duality proves WOT closure of bounded ideal balls

First assume `1<p<\infty` and let `q` be the conjugate exponent. For every finite-rank operator `R`, WOT convergence gives

\[
\operatorname{Tr}(R^*T_i)
\longrightarrow
\operatorname{Tr}(R^*T),
\tag{23}
\]

because `\operatorname{Tr}(R^*T)` is a finite linear combination of matrix coefficients of `T`.

Schatten Hölder duality gives

\[
|\operatorname{Tr}(R^*T_i)|
\le
\|R\|_q\|T_i\|_p
\le C\|R\|_q.
\tag{24}
\]

Passing to the limit,

\[
|\operatorname{Tr}(R^*T)|\le C\|R\|_q.
\tag{25}
\]

Finite-rank operators are dense in `\mathcal S_q`, so (25) extends to a bounded functional on `\mathcal S_q`. The classical duality

\[
(\mathcal S_q)^*=\mathcal S_p
\tag{26}
\]

therefore supplies `B\in\mathcal S_p` with `\|B\|_p\le C` and

\[
\operatorname{Tr}(R^*B)=\operatorname{Tr}(R^*T)
\tag{27}
\]

for every finite-rank `R`. Taking rank-one `R` shows that all matrix coefficients of `B` and `T` agree, hence `B=T`. This proves (2) for `p>1`.

For `p=1`, use instead the classical duality

\[
\mathcal K(H)^*=\mathcal S_1(H),
\tag{28}
\]

where `\mathcal K(H)` is the compact-operator space with operator norm. The same estimate for finite-rank `R` is

\[
|\operatorname{Tr}(R^*T)|
\le C\|R\|,
\tag{29}
\]

and finite-rank operators are norm dense in `\mathcal K(H)`. The resulting functional on `\mathcal K(H)` is represented by a trace-class operator with the same rank-one coefficients as `T`, proving (2).

For (4), any admissible net has `\|T\|_p\le\sup_i\|T_i\|_p`, while the constant net `T_i=T` realizes cost `\|T\|_p` whenever `T\in\mathcal S_p`. If `T\notin\mathcal S_p`, part 1 rules out every finite-cost net.

### 2. The projection control isolates the resource blow-up

The singular values of `Q_n` are exactly `n` copies of `1`, so

\[
\|Q_n\|_p^p=n.
\tag{30}
\]

For each `x\in H`, `Q_nx\to x` in norm, proving (6). The identity on an infinite-dimensional Hilbert space is not compact and therefore belongs to no finite Schatten ideal. This proves (7)--(8).

AF-107's compactness control and the present Schatten control are therefore complementary. Compactness can be retained by a common compact envelope of all repaired unit balls; Schatten membership can instead be retained by a uniform ideal-norm budget even when no such collective norm-compact envelope is supplied.

### 3. Why WOT cannot see escaped trace mass

For (9), fixed vectors `x,y\in H` satisfy

\[
\langle P_nx,y\rangle
=
\langle x,e_n\rangle\langle e_n,y\rangle
\longrightarrow0,
\tag{31}
\]

so `P_n\to0` in WOT.

More generally, on a uniformly trace-norm-bounded family, WOT convergence determines pairing against every compact operator. Indeed, finite-rank operators are operator-norm dense in `\mathcal K(H)` and

\[
|\operatorname{Tr}(K^*(A_i-A))|
\le
\|K\|\,\|A_i-A\|_1.
\tag{32}
\]

The uniform `\mathcal S_1` bound lets finite-rank convergence extend to all compact `K`.

But the trace itself is pairing with

\[
I_H\in\mathcal L(H)\setminus\mathcal K(H).
\tag{33}
\]

Thus no contradiction exists between WOT convergence of a uniformly trace-class-bounded family and failure of trace convergence. The topology tests compact windows; trace also counts mass that can drift outside every fixed compact window.

### 4. Trace lower semicontinuity and the exact tightness criterion

For every finite-rank projection `E`, WOT convergence implies

\[
\operatorname{Tr}(EA_i)\to\operatorname{Tr}(EA).
\tag{34}
\]

Since `A_i\ge0`,

\[
0\le\operatorname{Tr}(EA_i)\le\operatorname{Tr}(A_i).
\tag{35}
\]

Taking the lower limit and then increasing finite-rank projections to the identity gives

\[
\operatorname{Tr}(A)
=
\sup_m\operatorname{Tr}(E_mA)
\le
\liminf_i\operatorname{Tr}(A_i),
\tag{36}
\]

which is (15).

For fixed `m`, positivity and trace cyclicity give

\[
\operatorname{Tr}(A_i)
=
\operatorname{Tr}(E_mA_i)
+
\operatorname{Tr}((I-E_m)A_i),
\tag{37}
\]

where the second term is nonnegative because it equals

\[
\operatorname{Tr}\bigl(A_i^{1/2}(I-E_m)A_i^{1/2}\bigr).
\tag{38}
\]

If (17) holds, then by (34)

\[
\operatorname{Tr}((I-E_m)A_i)
\to
\operatorname{Tr}((I-E_m)A)
\tag{39}
\]

for each fixed `m`; the right-hand side decreases to zero as `m\to\infty`, proving (18).

Conversely, assume (18). Given `\varepsilon>0`, choose `m` so the limsup in (18) is below `\varepsilon`. Equations (34) and (37) give

\[
\limsup_i\operatorname{Tr}(A_i)
\le
\operatorname{Tr}(E_mA)+\varepsilon
\le
\operatorname{Tr}(A)+\varepsilon.
\tag{40}
\]

Combine with (15) and let `\varepsilon\downarrow0` to obtain (17).

### 5. Positive no-escape assembly is trace-norm assembly

Assume now (17). Choose a finite-rank projection `E` such that

\[
\operatorname{Tr}((I-E)A)<\varepsilon
\tag{41}
\]

and, by (18), eventually

\[
\operatorname{Tr}((I-E)A_i)<2\varepsilon.
\tag{42}
\]

On the finite-dimensional corner `E\mathcal L(H)E`, WOT convergence implies convergence in every matrix norm, hence

\[
\|E(A_i-A)E\|_1\to0.
\tag{43}
\]

For a positive trace-class operator `B`, Schatten Hölder applied to

\[
EB(I-E)=EB^{1/2}B^{1/2}(I-E)
\]

gives

\[
\|EB(I-E)\|_1
\le
\sqrt{\operatorname{Tr}(EB)}
\sqrt{\operatorname{Tr}((I-E)B)}.
\tag{44}
\]

The traces `\operatorname{Tr}(A_i)` are uniformly bounded, while (41)--(42) make the tails small. Decomposing `A_i-A` into its four `E/(I-E)` corners, the diagonal tail satisfies

\[
\|(I-E)(A_i-A)(I-E)\|_1
\le
\operatorname{Tr}((I-E)A_i)
+
\operatorname{Tr}((I-E)A),
\tag{45}
\]

and the two off-diagonal corners are controlled by (44) for `A_i` and `A`. Equations (41)--(45), followed by `\varepsilon\downarrow0`, prove (20).

Fredholm determinant is continuous in trace norm. A standard determinant estimate is

\[
|\det(I+B)-\det(I+C)|
\le
\|B-C\|_1
\exp\!\bigl(1+\|B\|_1+\|C\|_1\bigr).
\tag{46}
\]

Apply (46) to `B=zA_i`, `C=zA`. On every bounded `z`-set the exponential factor is uniformly bounded because the traces are bounded, while `\|A_i-A\|_1\to0`. This proves the local uniform convergence (21).

## Exact controls and failure modes

### Category membership and scalar invariants are different claims

Part 1 says only that the WOT limit remains in the declared Schatten ideal under a finite ideal-norm budget. It does not make every functional on that ideal WOT-continuous.

The rank-one escape (9) is the decisive control: the category is perfectly preserved while the trace and determinant change discontinuously. Therefore a later argument cannot infer trace-formula or determinant fidelity merely from "all approximants and the limit are trace class."

### Positivity is not enough

Every `P_n` in (9) is positive. Positivity plus a trace-norm budget still permits complete escape of trace mass. The extra datum is (18), not positivity itself.

This matters for positivity-based RH programs: a positive/PSD construction can survive an operator limit while the scalar quantity intended to encode arithmetic mass does not.

### Trace tightness is stronger than bounded trace

A uniform bound

\[
\sup_i\operatorname{Tr}(A_i)<\infty
\tag{47}
\]

prevents total mass blow-up but not migration into higher modes. Condition (18) controls **location relative to finite-dimensional compact windows**, not only quantity.

The distinction is the operator analogue of tightness versus bounded total mass in measure convergence.

### The positive theorem does not automatically extend to signed/non-normal trace-class families

For positive operators, trace is total trace mass and the tail terms in (37)--(45) are nonnegative. For general trace-class operators, cancellations can hide large positive and negative/singular-value mass. A suitable observable-fidelity theorem then needs control of `|A_i|`, polar data, or another variation/tightness condition; bare convergence of scalar traces is not enough.

Thus the positivity hypothesis in parts 4--5 is load-bearing rather than decorative.

### No arithmetic specificity follows from Schatten or trace tightness alone

Schatten budgets, positivity, and compact-window tightness are generic operator-theoretic properties. They do not distinguish rational primes from matched controls.

An RH-facing application must derive the relevant ideal bound and no-escape condition intrinsically from the arithmetic/geometric construction and then prove that the surviving trace/determinant actually contains a rational-prime discriminator. Imposing a trace-tight family by hand would simply encode the desired continuity into the admissibility class.

## Prior art and novelty assessment

The operator-theoretic ingredients are classical. **No theorem-level novelty is claimed.**

- Barry Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society, Providence, RI (2005), DOI `10.1090/surv/120`. Role: authoritative source for Schatten ideals and their duality, trace-class convergence theory, trace, Fredholm determinants, and determinant inequalities/continuity. The AMS table of contents explicitly treats trace ideals, convergence theorems, trace, determinant, and Fredholm theory.
- E. Seiler and B. Simon, **“An inequality among determinants,”** *Proceedings of the National Academy of Sciences of the USA* 72(9), 3277–3278 (1975), DOI `10.1073/pnas.72.9.3277`. Role: primary determinant-inequality background for quantitative continuity estimates of Fredholm determinants under trace-ideal perturbations.

The WOT closure of uniformly bounded Schatten balls follows directly from classical Schatten duality; the positive trace-tightness criterion is the standard no-mass-escape mechanism written in operator form; and trace-norm continuity of the Fredholm determinant is classical trace-ideal theory. The projection examples are standard finite-rank controls.

The durable Arithmetic Fidelity result is therefore organizational and categorical rather than a claim of new operator theory: **the resource norm that preserves an operator category need not preserve the observable extracted from that category.** In the trace-class case, a finite `\mathcal S_1` budget prevents loss of membership, but trace/determinant fidelity requires a second, spatially coherent no-escape condition.

## Consequences for Arithmetic Fidelity

AF-106 supplied the generic closure rule, and AF-107 showed that compactness needs collective family coherence because compact operators are not WOT/SOT closed under ordinary operator-norm-bounded approximation. AF-108 adds a different repair mechanism and a new audit layer:

\[
\boxed{
\text{stagewise property}
\;<\;
\text{budgeted category fidelity}
\;<\;
\text{observable fidelity}.
}
\tag{48}
\]

For Schatten classes, the middle gate is an ideal-norm budget. For positive trace observables, the final gate is trace tightness/no mass escape. Those gates answer different questions and cannot be substituted for one another.

For later RH-facing spectral, resolvent, heat-kernel, trace-formula, or determinant constructions, this gives a concrete falsification protocol. Before crediting a limiting scalar observable, verify separately:

1. which operator topology the construction actually supplies;
2. which uniform ideal norm keeps the assembled operator inside the required Schatten category;
3. whether the scalar trace mass is tight rather than escaping through modes invisible to fixed compact tests;
4. only then, whether trace-norm/determinant continuity transports the intended arithmetic discriminator.

A construction that proves only "every finite approximation is trace class" fails already at gate 2. A construction that proves a uniform trace-class budget but no no-escape principle can still fail at gate 3 exactly as `(P_n)` does. This is the precise operator-theoretic version of the line's central warning: **survival of the carrier does not imply survival of the discriminator read from that carrier.**