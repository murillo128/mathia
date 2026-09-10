# AF-252 — Torsion affine cosets have a finite-orbit collapse dichotomy

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `AFFINE-TORSION-BOUNDARY`, `DIOPHANTINE-FIDELITY`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-251 proves that for a nonzero trigonometric polynomial the phase generators producing exponentially small values have Hausdorff dimension bounded by the dimension of the polynomial's zero set, and that the same argument localizes to every connected **homogeneous** subtorus. Its explicit remaining boundary is an affine torsion coset, where multiplication by `n` moves the starting component instead of preserving it.

That boundary has an exact finite-orbit dichotomy.

Let

\[
P(x)=\sum_{k\in F}c_k e^{2\pi i\langle k,x\rangle},
\qquad x\in\mathbb T^d,
\tag{1}
\]

be a nonzero trigonometric polynomial. Let `H\le \mathbb T^d` be a connected subtorus of dimension `r\ge 1`, and let

\[
C=a+H
\tag{2}
\]

be an affine coset whose class `[a]\in \mathbb T^d/H` has finite order `q`. Define the exceptional generators intrinsic to `C` by

\[
\mathcal E_C(P)
=
\left\{\alpha\in C:
\limsup_{n\to\infty}
\frac{-\log |P(n\alpha)|}{n}>0
\right\},
\tag{3}
\]

with `-\log 0=+\infty`.

There is a representative `b\in C` of exact order `q` in `\mathbb T^d`, so that

\[
C=b+H,
\qquad qb=0.
\tag{4}
\]

For `j=0,\ldots,q-1`, write

\[
C_j=jb+H,
\qquad
Z_j=\{x\in C_j:P(x)=0\}.
\tag{5}
\]

Then exactly one of the following two regimes holds.

### Catastrophic affine collapse

If

\[
P|_{C_j}\equiv0
\tag{6}
\]

for at least one residue `j`, then

\[
\boxed{\mathcal E_C(P)=C}
\tag{7}
\]

and in fact every `\alpha\in C` has exact zeros

\[
P(n\alpha)=0
\tag{8}
\]

for every positive `n\equiv j\pmod q`.

### Finite-orbit nondegenerate regime

If no restriction `P|_{C_j}` is identically zero, let

\[
K=\max_{0\le j<q}\dim_{\mathbb R} Z_j,
\tag{9}
\]

ignoring empty `Z_j`. If every `Z_j` is empty, then `\mathcal E_C(P)=\varnothing`. Otherwise

\[
\boxed{
\dim_H\mathcal E_C(P)\le K\le r-1.
}
\tag{10}
\]

Thus a torsion affine constraint does **not** create an intermediate generic failure mode. It either places one periodically visited component completely inside the cancellation variety, causing exact recurrent collapse for every point of the starting coset, or the AF-251 codimension bound survives after splitting the integers into finitely many residue classes.

The catastrophic branch also has an exact finite Fourier test. Let

\[
\rho:\mathbb Z^d\to\widehat H
\tag{11}
\]

be restriction of ambient characters to `H`. For each residue `j` and restricted character `\lambda\in\rho(F)`, define

\[
A_{j,\lambda}
=
\sum_{\substack{k\in F\\\rho(k)=\lambda}}
 c_k e^{2\pi i j\langle k,b\rangle}.
\tag{12}
\]

Then

\[
\boxed{
P|_{C_j}\equiv0
\iff
A_{j,\lambda}=0
\text{ for every }\lambda\in\rho(F).
}
\tag{13}
\]

So affine catastrophic collapse is not a vague resonance condition: after the torsion order and character identifications on `H` are known, it is a finite system of coefficient cancellations.

## Why it matters

AF-251 showed that exact homogeneous integer-linear relations among finitely many phases cannot by themselves make destructive exponential cancellation typical. Its proof could not simply absorb affine torsion constraints because the orbit of a point in `a+H` visits different translates of `H`.

Equations `(7)` and `(10)` close that precise boundary. The affine translation matters only through a **finite orbit of components**. If every visited component sees a genuinely nonzero restricted polynomial, the same exponential shrinking-target argument remains codimension-lowering. If one component is annihilated identically, the obstruction becomes much stronger than exceptional Diophantine recurrence: every starting phase in `C` is forced to hit exact cancellation periodically.

For Arithmetic Fidelity this isolates a reusable distinction between two kinds of source constraint. A source may merely reduce the admissible phase manifold, in which case generic fidelity survives intrinsically on that manifold; or it may align an entire periodically visited component with the compression kernel, in which case no metric genericity argument can help. The latter is detectable by finite character data through `(13)`.

## Derivation / evidence

### 1. A torsion quotient class has a torsion representative

Let `\pi:\mathbb T^d\to\mathbb T^d/H` be the quotient map. Since `\pi(a)` has order `q`,

\[
qa\in H.
\tag{14}
\]

Because `H` is a connected torus, multiplication by `q` is surjective on `H`. Choose `h_0\in H` with

\[
qh_0=qa.
\tag{15}
\]

Set `b=a-h_0`. Then `b+H=a+H` and `qb=0`. Moreover `b` has exact order `q`: if `mb=0`, then `m\pi(a)=0`, so `q\mid m`; together with `qb=0` this proves `(4)`.

This representative removes a possible hidden drift inside `H`. For `\alpha=b+h\in C` and `n\equiv j\pmod q`,

\[
n\alpha
=nb+nh
=jb+nh
\in C_j.
\tag{16}
\]

Hence multiplication visits exactly the finite family `C_0,\ldots,C_{q-1}` according to the residue of `n` modulo `q`.

### 2. One identically vanishing component forces periodic exact cancellation

Assume `P|_{C_j}\equiv0`. Equation `(16)` gives `n\alpha\in C_j` for every `\alpha\in C` and every `n\equiv j\pmod q`. Therefore `P(n\alpha)=0` on an infinite arithmetic progression for every `\alpha\in C`, so the limsup in `(3)` is `+\infty`. This proves `(7)`.

No equidistribution, approximation theorem, or asymptotic estimate is involved in this branch.

### 3. Otherwise AF-251 reruns residue by residue

Assume each `P|_{C_j}` is nonzero. Translation identifies each `C_j` isometrically with `H\cong\mathbb T^r`, and the restriction is again a finite trigonometric polynomial in intrinsic torus coordinates. Therefore its zero set is a compact real-analytic/algebraic subset of dimension at most `r-1`.

Fix `c>0` and define

\[
E_n^C(c)
=\{\alpha\in C:|P(n\alpha)|<e^{-cn}\}.
\tag{17}
\]

For `n\equiv j\pmod q`, the compact Łojasiewicz inequality for the fixed nonzero restriction `P|_{C_j}` places `n\alpha` within

\[
\delta_{n,j}=C_j e^{-\sigma_j n}
\tag{18}
\]

of `Z_j`, for suitable `C_j,\sigma_j>0`. Since there are only `q` residues, no uniformity over an infinite family is needed.

The map

\[
C\to C_j,
\qquad b+h\mapsto jb+nh,
\tag{19}
\]

is, after translating source and target by `b` and `jb`, multiplication by `n` on `H`. It is a degree-`n^r` covering and each local inverse sheet scales intrinsic distances by `1/n`.

Let `k_j=\dim_{\mathbb R}Z_j`. Repeating the fixed-set covering step of AF-251, for every `\eta>0` the `\delta_{n,j}`-tube around `Z_j` can be covered by

\[
O(\delta_{n,j}^{-(k_j+\eta)})
\tag{20}
\]

balls of radius comparable to `\delta_{n,j}`. Pulling them back through `(19)` covers `E_n^C(c)` by

\[
O(n^r\delta_{n,j}^{-(k_j+\eta)})
\tag{21}
\]

balls of radius `O(\delta_{n,j}/n)`.

For any `s>K`, choose `\eta>0` with `K+\eta<s`. Summing the `s`-cost over one residue class gives

\[
\sum_{\substack{n\ge1\\n\equiv j\ (q)}}
O\!\left(
 n^{r-s}\delta_{n,j}^{s-k_j-\eta}
\right)<\infty,
\tag{22}
\]

because `\delta_{n,j}` decays exponentially. The finite union over residues also converges. Hausdorff--Borel--Cantelli therefore yields

\[
\dim_H\left(\limsup_n E_n^C(c)\right)\le K.
\tag{23}
\]

Taking the countable union over positive rational `c` proves `(10)`. If every `Z_j` is empty, compactness and finiteness of the component family give a uniform positive lower bound for `|P|` on `\bigcup_jC_j`, so `(17)` is eventually empty and `\mathcal E_C(P)=\varnothing`.

Exactly as in AF-251, outside `\mathcal E_C(P)` one has

\[
|P(n\alpha)|^{1/n}\longrightarrow1,
\tag{24}
\]

so every unbounded output sampling is root-faithful; membership in `\mathcal E_C(P)` is equivalent to the existence of an infinite retained subsequence with strictly smaller root rate.

### 4. Character grouping exactly detects the catastrophic branch

For `h\in H`, group the Fourier expansion of `P(jb+h)` by the restricted character `\rho(k)`:

\[
P(jb+h)
=
\sum_{\lambda\in\rho(F)}
A_{j,\lambda}\,\lambda(h).
\tag{25}
\]

Distinct characters of the compact abelian group `H` are linearly independent. Hence `(25)` vanishes identically if and only if every grouped coefficient vanishes, proving `(13)`.

This criterion also shows why affine translation is genuinely different from the homogeneous Li case in AF-251: translation inserts root-of-unity phases into groups of ambient modes that become the same character on `H`, allowing exact cancellation that is impossible at the origin merely from positivity of the Li multiplicities.

### 5. The catastrophic Li branch is real, not only formal

Take `d=2`, the diagonal subtorus

\[
H=\{(t,t):t\in\mathbb T\},
\tag{26}
\]

and the order-two translate represented by

\[
b=(0,1/2).
\tag{27}
\]

For the Li-shaped mode with multiplicities `m=(1,1)`,

\[
P_m(x_1,x_2)
=-2\cos(2\pi x_1)-2\cos(2\pi x_2).
\tag{28}
\]

On the homogeneous diagonal,

\[
P_m(t,t)=-4\cos(2\pi t),
\tag{29}
\]

which is not identically zero. On the affine component `b+H`, however,

\[
P_m(t,t+1/2)
=-2\cos(2\pi t)-2\cos(2\pi t+\pi)=0
\tag{30}
\]

identically. Thus the origin argument used in AF-251 cannot be extended to arbitrary affine torsion translates: a torsion shift can turn a nonzero homogeneous restriction into complete periodic cancellation.

## Prior-art audit

The analytic and Hausdorff-dimension ingredients in the nondegenerate branch are exactly the classical ingredients already audited in AF-251: the compact Łojasiewicz distance inequality, polynomial/semialgebraic covering complexity, and Hausdorff--Borel--Cantelli. No new shrinking-target theorem is needed.

Torsion cosets and translates of subtori are standard objects in Diophantine geometry of algebraic tori. Michel Laurent's **“Équations diophantiennes exponentielles,”** *Inventiones Mathematicae* 78 (1984), 299--327, DOI `10.1007/BF01388597`, is classical neighboring prior art for the structure of intersections with finitely generated multiplicative groups and torsion-coset phenomena. It is not invoked to prove `(7)`--`(13)`; the finite orbit here follows directly from the elementary quotient-torus calculation `(14)`--`(16)`.

The shrinking-target literature for toral endomorphisms, including Hill--Velani's **“The Shrinking Target Problem for Matrix Transformations of Tori,”** *Journal of the London Mathematical Society* 60 (1999), 381--398, studies iterates of a fixed toral endomorphism hitting shrinking targets. The present sequence uses the varying maps `M_n:x\mapsto nx` and finitely many translated analytic zero varieties, so those dimension formulas are not being imported.

A targeted search across torsion-coset, affine-subtorus, trigonometric-polynomial, and toral shrinking-target literature did not locate this exact finite-residue synthesis. No broad novelty is claimed: the group-theoretic reduction and Fourier criterion are elementary/classical, while the durable contribution here is the exact closure of AF-251's affine-torsion boundary inside the Arithmetic Fidelity framework.

## Boundaries and failure modes

**Torsion in the quotient is essential.** If `[a]\in\mathbb T^d/H` has infinite order, the orbit visits infinitely many affine components. The finite-residue proof gives no uniform Łojasiewicz exponent, covering constant, or zero-set dimension control over that infinite family. No conclusion for irrational affine translates is claimed here.

**Connectedness of `H` is used twice.** It makes multiplication by `q` surjective, which produces the torsion representative `b`, and makes multiplication by `n` a degree-`n^r` covering with the intrinsic torus geometry used in `(19)`--`(22)`. Disconnected subgroup constraints require a separate component analysis.

**The catastrophic branch is componentwise, not pointwise.** An individual exact hit or an exceptionally approximable orbit does not imply `(6)`. Equation `(6)` means the whole periodically visited affine component lies in the zero variety, equivalently the finite grouped coefficients `(12)` all vanish.

**Codimension smallness still does not exclude the arithmetic source.** In the nondegenerate branch `(10)` is a genericity statement. A specific zeta-derived phase vector can still lie in `\mathcal E_C(P)` even when that set has Hausdorff codimension at least one.

**No RH consequence is claimed.** The result classifies one structural boundary in the finite-mode Li cancellation problem. It supplies neither the affine constraints actually obeyed by Riemann-zero phases nor the source-specific Diophantine theorem needed to exclude their membership in the thin nondegenerate exceptional set.

## Consequences for the research line

AF-251's homogeneous-subtorus result now extends exactly to every torsion affine coset except for one sharply characterized obstruction: a periodically visited component on which the relevant trigonometric mode vanishes identically. The obstruction can be checked by the finite character-collision equations `(12)`--`(13)`.

For Li-shaped dominant modes, future source-specific work can therefore separate two questions that should not be conflated. First, do actual arithmetic phase relations force a torsion affine component satisfying the finite catastrophic equations? If not, affine torsion relations themselves are harmless at the generic level and the remaining blocker is again Diophantine: whether the specific zeta phase vector lies in the codimension-at-least-one exponentially approximable set. Infinite-order affine constraints remain a genuinely different unresolved regime.