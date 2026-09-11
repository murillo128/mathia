# AF-269 — Finite-total zero transport still breaks exact Bohr recurrence

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `ALMOST-PERIODICITY`, `INFINITE-ZERO-SURGERY`, `TRANSPORT-OBSTRUCTION`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-268 proves that every nontrivial **finite** signed zero surgery leaves a transient `C_0(R)` defect on a right-half-plane vertical logarithmic-derivative trace, so it cannot preserve exact Bohr almost periodicity. The same obstruction extends to a genuinely infinite class: count-preserving zero rearrangements with **finite total paired displacement** are still transient.

Fix real numbers

\[
\sigma>b.
\tag{1}
\]

Let

\[
A=(\alpha_j)_{j\ge1},
\qquad
B=(\beta_j)_{j\ge1}
\tag{2}
\]

be locally finite multisets contained in the half-plane `Re z <= b`, listed with multiplicity and paired so that

\[
\boxed{
\mathsf T(A,B):=\sum_{j\ge1}|\alpha_j-\beta_j|<\infty.
}
\tag{3}
\]

Think of `B` as removed zeros and `A` as inserted zeros. Define the paired logarithmic-derivative defect

\[
D(s)
:=
\sum_{j\ge1}
\left(
\frac1{s-\alpha_j}-\frac1{s-\beta_j}
\right).
\tag{4}
\]

Then the series is normally convergent away from the two multisets and therefore defines a meromorphic function whose residue divisor is `A-B`. On the observation line `s=\sigma+it`, the convergence is uniform on the whole real axis and

\[
\boxed{
D_\sigma(t):=D(\sigma+it)\in C_0(\mathbb R),
\qquad
\|D_\sigma\|_\infty
\le
\frac{\mathsf T(A,B)}{(\sigma-b)^2}.
}
\tag{5}
\]

Consequently, if `D_sigma` is Bohr uniformly almost periodic, then

\[
D_\sigma\equiv0.
\tag{6}
\]

Normal meromorphic continuation then forces `D\equiv0`, so every residue of `D` vanishes and the signed divisor is trivial:

\[
\boxed{A=B\quad\text{as multisets after cancellation}.}
\tag{7}
\]

Equivalently, **no nontrivial count-preserving zero rearrangement of finite total paired displacement can preserve an exact Bohr-almost-periodic logarithmic-derivative source trace on a line strictly to the right of the divisor.**

For the completed-zeta setting, suppose an order-one matched control `F` differs from `xi` by such a paired signed zero divisor, and let

\[
\mathcal R_f(s)
:=\frac{f'}{f}(s)-A_\Gamma(s)
\tag{8}
\]

use the fixed Riemann archimedean completion term from AF-266--AF-268. Hadamard factorization gives on `Re s>b`

\[
\mathcal R_F(s)-\mathcal R_\xi(s)
=c+D(s)
\tag{9}
\]

for a constant `c`; the genus-one reciprocal corrections and the zero-free exponential ambiguity are absorbed into `c`. Since constants are almost periodic and AF-268 gives

\[
\mathcal R_\xi(\sigma+i\,\cdot)\in AP(\mathbb R),
\tag{10}
\]

any control satisfying

\[
\mathcal R_F(\sigma+i\,\cdot)\in AP(\mathbb R)
\tag{11}
\]

must have `D_sigma=0`, hence the same zero divisor as `xi`. In particular, a control with an absolutely convergent ordinary or general Dirichlet logarithmic-derivative source on that line cannot be obtained from `xi` by a nontrivial finite-total-displacement zero rearrangement.

Thus an exact recurrent source law pushes the remaining infinite-surgery escape into a sharper regime:

\[
\boxed{
\text{nontrivial AP-preserving zero rearrangement}
\Longrightarrow
\text{every admissible pairing has }\sum_j|\alpha_j-\beta_j|=\infty,
}
\tag{12}
\]

unless the control changes the source law through structure not represented by the paired divisor defect.

## Exact derivation

### 1. Finite paired transport gives a normally convergent meromorphic defect

For each pair,

\[
\frac1{s-\alpha_j}-\frac1{s-\beta_j}
=
\frac{\alpha_j-\beta_j}
{(s-\alpha_j)(s-\beta_j)}.
\tag{13}
\]

Let `K` be a compact subset of the plane avoiding `A union B`. Because both multisets are locally finite, only finitely many `alpha_j` or `beta_j` lie in any fixed bounded neighborhood of `K`. After removing finitely many indices, both denominators in `(13)` have modulus at least `1` uniformly on `K`. Hence the tail is dominated by

\[
|\alpha_j-\beta_j|,
\tag{14}
\]

which is summable by `(3)`. The Weierstrass `M`-test gives normal convergence on `K`. Therefore `(4)` defines a meromorphic function, and at any point `z` its residue is exactly

\[
\operatorname{mult}_A(z)-\operatorname{mult}_B(z).
\tag{15}
\]

This step is why the result is stronger than merely knowing convergence on one vertical line: if the defect later vanishes on an open right half-plane, the signed divisor itself is forced to vanish.

### 2. The full vertical defect is transient

Put

\[
\delta:=\sigma-b>0.
\tag{16}
\]

For every real `t` and every point of either multiset,

\[
|\sigma+it-\alpha_j|\ge\delta,
\qquad
|\sigma+it-\beta_j|\ge\delta.
\tag{17}
\]

Equation `(13)` therefore gives the uniform bound

\[
\left|
\frac1{\sigma+it-\alpha_j}
-
\frac1{\sigma+it-\beta_j}
\right|
\le
\frac{|\alpha_j-\beta_j|}{\delta^2}.
\tag{18}
\]

Summing proves uniform convergence on the whole line and the norm estimate in `(5)`.

Every finite partial sum of `(4)` belongs to `C_0(R)`: after pairing, each term is `O(|t|^{-2})` as `|t|->infinity`. Since `C_0(R)` is closed in the supremum norm and the partial sums converge uniformly by `(18)`, their limit `D_sigma` also lies in `C_0(R)`.

This is the decisive extension of AF-268. An infinite edit is not automatically recurrent merely because infinitely many zero heights are touched. If the total displacement is summable, its vertical Cauchy response is still a uniform limit of transients and therefore remains transient.

### 3. Exact almost periodicity forces the signed divisor to cancel

AF-268 proves the elementary structural fact

\[
AP(\mathbb R)\cap C_0(\mathbb R)=\{0\}.
\tag{19}
\]

Hence `(5)` immediately implies `(6)` whenever `D_sigma` is almost periodic.

The function `D` from `(4)` is holomorphic on the open half-plane `Re s>b`. Since it vanishes on the entire vertical line `Re s=sigma`, the identity theorem gives

\[
D(s)=0
\qquad(\Re s>b).
\tag{20}
\]

The normally convergent series already defines one meromorphic continuation away from the locally finite support `A union B`. The meromorphic identity theorem therefore makes `D` identically zero on its domain. Its residues `(15)` all vanish, proving `(7)`.

Notice that this conclusion does not depend on the chosen pairing once a finite-cost pairing exists. If *some* pairing has finite total displacement, exact almost periodicity forces the underlying signed divisor itself to be zero.

### 4. Order-one completed functions introduce only a constant logarithmic ambiguity

For an order-one entire matched control, Hadamard factorization uses genus-one primary factors. After common zeros are cancelled and the remaining zeros are paired as in `(2)`, logarithmic differentiation has the form

\[
\frac{F'}F(s)-\frac{\xi'}\xi(s)
=
(a_F-a_\xi)
+
\sum_j
\left[
\frac1{s-\alpha_j}+\frac1{\alpha_j}
-
\frac1{s-\beta_j}-\frac1{\beta_j}
\right].
\tag{21}
\]

Apart from finitely many points near the origin, `(3)` also makes

\[
\sum_j
\left|\frac1{\alpha_j}-\frac1{\beta_j}\right|
<\infty,
\tag{22}
\]

because

\[
\left|\frac1{\alpha_j}-\frac1{\beta_j}\right|
=
\frac{|\alpha_j-\beta_j|}{|\alpha_j\beta_j|}
\le
|\alpha_j-\beta_j|
\tag{23}
\]

once both moduli exceed `1`. Thus all reciprocal corrections in `(21)` combine with `a_F-a_xi` into one constant `c`, leaving `(9)`.

If both completed residuals are in `AP(R)`, then `c+D_sigma` is almost periodic. The constant `c` is almost periodic, so `D_sigma` is almost periodic; `(19)` then forces it to vanish. The conclusion concerns the **zero divisor** even if the zero-free constant/exponential factor is not separately normalized. If both functions also satisfy the same Riemann reflection symmetry, the remaining exponential slope is forced to zero; one value normalization then fixes the residual scalar, as in AF-018.

### 5. The obstruction is exact but has no transport-to-category lower modulus

AF-268 gives for every `h in C_0(R)`

\[
\frac12\|h\|_\infty
\le
\operatorname{dist}_\infty(h,AP(\mathbb R))
\le
\|h\|_\infty.
\tag{24}
\]

Combining `(5)` and `(24)` yields for a nontrivial finite-transport defect

\[
0<
\operatorname{dist}_\infty(D_\sigma,AP)
\le
\frac{\mathsf T(A,B)}{(\sigma-b)^2}.
\tag{25}
\]

There is no converse lower bound in terms of `mathsf T(A,B)` alone: different paired moves can cancel strongly in their Cauchy response. So finite transport is a **categorical exclusion criterion**, not a stable inverse estimate. This is consistent with AF-267, where carefully balanced finite surgeries can make the vertical defect arbitrarily small while remaining outside `AP(R)` exactly.

## What this changes in the Arithmetic Fidelity audit

AF-268 left infinite/distributed zero rearrangements as an explicit escape from the finite-surgery argument. The present theorem removes a substantial part of that escape. Merely distributing the surgery over infinitely many heights is not enough: if the total amount by which zeros are transported is summable, the induced defect still dies at infinity and cannot coexist with an exact recurrent Dirichlet-source trace.

The remaining global alternative is therefore more expensive. A nontrivial zero-side control that stays inside the exact Bohr source category must either have no finite-total-displacement matching to the original divisor, or must alter the source representation by a genuinely recurrent/global component rather than by a summable transient Cauchy perturbation. In particular, a sequence of tiny local zero moves is excluded when their total displacement is finite, even though no individual move need be detectable by a positive uniform margin.

This sharpens the current line frontier without assuming RH. The useful resource is not "more precision" on the same metric; it is a category-level compatibility between a discrete Dirichlet source and globally recurrent vertical behavior. The next live question is correspondingly narrower: **can an RH-relevant off-critical alternative preserve the exact source category only through infinite-transport/global rearrangement, and what additional zeta-specific structure rules out or controls that regime without simply reinstating the full Euler product as an assumption?**

## Prior art and novelty assessment

The almost-periodic and divisor ingredients sit inside mature classical theory. S. Yu. Favorov, **“Almost periodic divisors, holomorphic functions, and holomorphic mappings,”** *Bulletin des Sciences Mathématiques* 127(10), 859--883 (2003), DOI `10.1016/j.bulsci.2003.06.001`, characterizes divisors of holomorphic and meromorphic almost-periodic functions using the Bohr compactification and associated cohomological data. Favorov and N. D. Parfyonova, **“Meromorphic almost periodic functions,”** *Matematychni Studii* 13(2), 190--198 (2000), DOI `10.30970/ms.13.2.190-198`, develop the meromorphic almost-periodic category and its zero/pole structure. S. Yu. Favorov and O. I. Udodova, **“Uniqueness theorems for almost periodic objects,”** *Bukovinian Mathematical Journal* 9(1) (2021), DOI `10.31861/bmj2021.01.03`, give uniqueness theorems for almost-periodic functions, measures, multisets, and meromorphic functions under asymptotic agreement hypotheses.

Those results are stronger and broader in their own almost-periodic settings than any claim of a new general divisor theory here. No novelty is claimed for almost-periodic divisor rigidity, meromorphic uniqueness, Hadamard factorization, or the elementary `AP cap C_0` mechanism inherited from AF-268.

The Arithmetic Fidelity contribution is the **specific finite-total-transport audit of the current zeta zero-surgery control class**: the simple paired Cauchy estimate `(18)` converts a summable infinite divisor displacement into a `C_0` defect and therefore shows that exact right-half-plane source recurrence excludes every such infinite matched rearrangement. This turns AF-268's qualitative "infinite surgery remains open" boundary into the sharper necessary escape `(12)`.

## Boundaries and failure modes

- Finite total paired displacement is sufficient for the obstruction, not necessary. Infinite-cost rearrangements may still have a `C_0` defect through stronger grouped cancellation, or may produce a genuinely almost-periodic defect. Neither possibility is classified here.
- The theorem assumes a count-preserving pairing of the signed divisor. Controls that insert unmatched infinite mass, change zero density, introduce poles, or alter the completion category require a different audit.
- The half-plane separation `Re alpha_j, Re beta_j <= b < sigma` is essential to the simple uniform bound `(18)`. For the nontrivial zeta zero strip one may take `b=1` and any `sigma>1`; no claim is made for a line passing through the divisor.
- `mathsf T(A,B)` is a pairing cost for two infinite locally finite multisets, not the ordinary Wasserstein-1 distance between finite probability measures. No optimal-transport theorem is being invoked.
- Almost periodicity still does not distinguish rational primes from arbitrary absolutely convergent discrete general-Dirichlet sources. This is a discrete-source recurrence obstruction, not yet a rational-prime-specific invariant.
- The result does not prove RH. The genuine `xi` source is almost periodic in `Re s>1` whether or not its actual zero divisor satisfies RH. The theorem only constrains how a *different* matched control can alter that divisor while remaining in the same exact recurrent source category.
- Exact category membership has no positive robustness radius. A family may have positive but arbitrarily small distance to `AP(R)` even though every member is excluded exactly.
- The prior-art uniqueness literature warns against interpreting the result as a new theory of almost-periodic zero sets. Its role is local to the Arithmetic Fidelity classification of which zero-side perturbations can coexist with the retained source category.

## Evidence classification

`EXACT-DERIVED` for normal convergence of the paired Cauchy series, the `C_0` vertical trace, the transport upper bound, and the resulting exact exclusion of nontrivial finite-total-displacement rearrangements. `LITERATURE+DERIVED` for the Hadamard/order-one embedding and the placement of this mechanism inside classical almost-periodic divisor/meromorphic uniqueness theory. No broad novelty claim is made.