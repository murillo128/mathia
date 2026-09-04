# AF-110 — Infinitesimal trace clouds collapse to zero-free determinant exponentials

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-FREDHOLM-EXPANSION`, `ZERO-FREE-FACTOR-FIDELITY`, `SIGNED-SPECTRAL-ESCAPE`, `REGULARIZATION-LOSS`, `NO-NOVELTY-CLAIM`

## Claim

Let `H` be a complex Hilbert space and let `(A_i)` be a net of trace-class operators satisfying

\[
\sup_i \|A_i\|_1\le C<\infty,
\qquad
\|A_i\|\longrightarrow0,
\tag{1}
\]

where `\|\cdot\|` is the operator norm and `\|\cdot\|_1` the trace norm. Thus every individual spectral/singular scale collapses to zero while a bounded amount of total trace-class mass may remain distributed across more and more directions.

AF-108 and AF-109 showed that weak/operator assembly can preserve the trace-class category while losing trace, determinant, or singular-value geometry. In the stronger infinitesimal regime (1), the Fredholm determinant has an exact asymptotic classification.

### 1. Only the first trace moment survives in the ordinary determinant

For every fixed `R>0`, eventually `R\|A_i\|<1`, and on `|z|\le R`,

\[
\log\det(I+zA_i)
=
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}z^k\operatorname{Tr}(A_i^k).
\tag{2}
\]

For `k\ge2`,

\[
|\operatorname{Tr}(A_i^k)|
\le
\|A_i^k\|_1
\le
\|A_i\|^{k-1}\|A_i\|_1.
\tag{3}
\]

Hence

\[
\sup_{|z|\le R}
\left|
\log\det(I+zA_i)-z\operatorname{Tr}(A_i)
\right|
\le
\frac{C R^2\|A_i\|}{1-R\|A_i\|}
\longrightarrow0.
\tag{4}
\]

Therefore, if

\[
\operatorname{Tr}(A_i)\longrightarrow\tau\in\mathbb C,
\tag{5}
\]

then

\[
\boxed{
\det(I+zA_i)\longrightarrow e^{\tau z}
\quad\text{locally uniformly on }\mathbb C.
}
\tag{6}
\]

The limit is always zero-free. Under (1), every spectral moment of order at least two is forced below the compression scale; the ordinary Fredholm determinant retains at most the first-order trace channel.

### 2. Self-adjoint normal spectral mass can disappear completely

Let `(e_j)` be an orthonormal basis with rank-one projections `P_j=|e_j\rangle\langle e_j|`, and define

\[
A_n
=
\frac1{2n}\sum_{j=1}^{n}P_j
-
\frac1{2n}\sum_{j=n+1}^{2n}P_j.
\tag{7}
\]

Then `A_n` is finite-rank, self-adjoint and normal, with

\[
\|A_n\|=\frac1{2n}\to0,
\qquad
\|A_n\|_1=1,
\qquad
\operatorname{Tr}(A_n)=0.
\tag{8}
\]

Yet

\[
\det(I+zA_n)
=
\left(1-\frac{z^2}{4n^2}\right)^n
\longrightarrow1
=
\det(I+z\,0)
\tag{9}
\]

locally uniformly, while

\[
\|A_n-0\|_1=1
\tag{10}
\]

for every `n`.

Thus AF-109's nilpotent/non-normal control is not the only mechanism by which determinant data can miss trace-class mass. Even for **self-adjoint normal operators**, operator-norm convergence plus locally uniform convergence of the complete Fredholm-determinant function does not imply trace-norm fidelity. A balanced cloud of positive and negative eigenvalues can collapse to zero individually while retaining order-one total variation in the spectrum.

### 3. Positive escaped trace mass becomes a zero-free exponential

Define instead

\[
B_n=\frac1n\sum_{j=1}^{n}P_j.
\tag{11}
\]

Then

\[
B_n\ge0,
\qquad
\|B_n\|=\frac1n\to0,
\qquad
\|B_n\|_1=\operatorname{Tr}(B_n)=1,
\tag{12}
\]

but

\[
\det(I+zB_n)
=
\left(1+\frac zn\right)^n
\longrightarrow e^z.
\tag{13}
\]

The WOT/operator-norm limit is the zero operator, whose determinant is `1`, but the determinant functions converge to the nontrivial zero-free factor `e^z`. The unit of positive trace mass has escaped every fixed operator direction while surviving exactly as the first-order exponential allowed by (6).

The zeros of the finite determinants are at `-n`, with multiplicity `n`, and therefore leave every compact subset of the complex plane. Compression to the limiting zero divisor sees nothing of the escaped trace mass although value-level determinant convergence still remembers it through the zero-free factor.

### 4. The second regularized determinant erases this surviving channel by definition

For trace-class `A`, the second regularized Fredholm determinant satisfies

\[
\det_2(I+zA)
=
\det(I+zA)e^{-z\operatorname{Tr}(A)}.
\tag{14}
\]

Combining (4) and (14) gives, without assuming trace convergence,

\[
\boxed{
\det_2(I+zA_i)\longrightarrow1
\quad\text{locally uniformly on }\mathbb C.
}
\tag{15}
\]

Thus in the infinitesimal trace-cloud regime the ordinary determinant retains precisely one possible scalar channel, `\operatorname{Tr}(A_i)`, while `\det_2` removes that channel and all remaining higher-order terms vanish automatically.

This is not a defect of regularized determinants: subtracting the low-order trace terms is their purpose. It is an Arithmetic Fidelity warning. If the first trace moment carries provenance or arithmetic information, passing to a regularized determinant can destroy the **only** component that survives the preceding infinitesimal spectral compression.

## Derivation

### Fredholm logarithm and a uniform remainder bound

Fix `R>0`. Since `\|A_i\|\to0`, for all sufficiently large `i`,

\[
R\|A_i\|<1.
\tag{16}
\]

For such `i` and `|z|\le R`, the operator logarithm has the norm-convergent series

\[
\log(I+zA_i)
=
\sum_{k\ge1}\frac{(-1)^{k+1}}{k}z^kA_i^k.
\tag{17}
\]

Every term is trace class and the trace series is absolutely convergent because

\[
\sum_{k\ge1}\frac{|z|^k}{k}\|A_i^k\|_1
\le
\|A_i\|_1
\sum_{k\ge1}\frac{|z|^k\|A_i\|^{k-1}}{k}
<\infty.
\tag{18}
\]

The standard trace-log identity for the Fredholm determinant therefore gives (2), with the branch normalized by value zero at `z=0`.

For `k\ge2`, the ideal inequality

\[
\|A_i^k\|_1
\le
\|A_i\|^{k-1}\|A_i\|_1
\tag{19}
\]

proves (3). Dropping the harmless factors `1/k` yields

\[
\begin{aligned}
\sup_{|z|\le R}
\left|
\sum_{k\ge2}\frac{(-1)^{k+1}}{k}z^k\operatorname{Tr}(A_i^k)
\right|
&\le
C\sum_{k\ge2}R^k\|A_i\|^{k-1}\\
&=
\frac{CR^2\|A_i\|}{1-R\|A_i\|},
\end{aligned}
\tag{20}
\]

which tends to zero. This proves (4).

If (5) holds, then `z\operatorname{Tr}(A_i)\to\tau z` uniformly on every disk. Equation (4) gives locally uniform convergence of the logarithms to `\tau z`; exponentiation gives (6).

### The self-adjoint control isolates signed spectral escape

The nonzero eigenvalues of `A_n` in (7) are

\[
\underbrace{\frac1{2n},\ldots,\frac1{2n}}_{n\text{ times}},
\qquad
\underbrace{-\frac1{2n},\ldots,-\frac1{2n}}_{n\text{ times}}.
\tag{21}
\]

Hence its largest singular value is `1/(2n)`, the sum of singular values is one, and the signed eigenvalue sum is zero. Multiplying the `2n` scalar determinant factors gives (9).

For each fixed `R`,

\[
\sup_{|z|\le R}
\left|
\left(1-\frac{z^2}{4n^2}\right)^n-1
\right|
\to0,
\tag{22}
\]

which also follows directly from (6) with `\tau=0`. The example separates three levels:

\[
\boxed{
\text{operator-norm fidelity}
\quad+\quad
\text{full determinant-function fidelity}
\quad\not\Rightarrow\quad
\text{trace-norm fidelity}.
}
\tag{23}
\]

Unlike AF-109's rank-one nilpotent family, no nonnormal singular-vector geometry is available to blame: the hidden information is the total variation of a signed spectral cloud whose atoms all shrink below the operator-norm scale.

### The positive control identifies the residual channel

For `B_n`, every nonzero eigenvalue equals `1/n`, so (12) is immediate and

\[
\det(I+zB_n)
=\prod_{j=1}^n\left(1+\frac zn\right)
=\left(1+\frac zn\right)^n.
\tag{24}
\]

The elementary exponential limit gives (13). This realizes the general limit (6) with `\tau=1` and shows that the zero-free factor is not an arbitrary analytic decoration: it can be the exact residue of trace-class mass that is invisible in the limiting operator topology.

### Regularization removes the first-order term

From (2),

\[
\log\det_2(I+zA_i)
=
\log\det(I+zA_i)-z\operatorname{Tr}(A_i)
=
\sum_{k\ge2}\frac{(-1)^{k+1}}{k}z^k\operatorname{Tr}(A_i^k).
\tag{25}
\]

The right-hand side is exactly the remainder controlled by (20), so it converges locally uniformly to zero. Exponentiation proves (15).

## Exact controls and failure modes

### The uniform trace-norm budget is essential

Operator-norm collapse alone does not control the aggregate higher-order traces when rank and total variation are allowed to grow too quickly. The estimate (20) uses both ingredients of (1): `\|A_i\|\to0` kills each individual scale, while `\sup_i\|A_i\|_1<\infty` prevents an unbounded number of shrinking modes from carrying unbounded total mass.

The theorem therefore describes a specific compression regime, not arbitrary compact-operator convergence.

### Trace convergence is needed only to identify the ordinary determinant limit

Equation (4) holds without (5). If the traces do not converge, the determinant need not have one locally uniform limit. What is rigid is the residual degree of freedom: after the infinitesimal compression, the determinant differs from `e^{z\operatorname{Tr}(A_i)}` by a factor tending locally uniformly to one.

Thus the surviving ambiguity is one complex scalar per stage, not an uncontrolled entire function.

### Positivity prevents cancellation but not escape

The positive family `B_n` shows that positivity does not force trace mass to remain in the WOT/operator limit. This agrees with AF-108: positivity plus trace tightness is needed to upgrade WOT to trace norm. Here positivity instead makes the escaped amount visible as the coefficient of the exponential determinant factor.

The signed family `A_n` shows the complementary failure: trace can cancel exactly even while trace norm stays one, so ordinary determinant convergence may become completely blind to the escaped total variation.

### Self-adjointness and normality do not make determinant data complete

AF-109 showed maximal determinant blindness using nilpotent operators. Equation (9) closes the obvious normality escape: even when eigenvalues fully describe each operator up to unitary equivalence, the limiting determinant function can forget a nonvanishing amount of spectral total variation because the entire eigenvalue cloud contracts toward zero.

What is missing is therefore not always eigenvector information. It can be **uniform spectral-mass tightness at the scale relevant to the chosen observable**.

### Passing from determinant values to zeros loses the residual exponential exactly

The limit `e^{\tau z}` in (6) has empty zero divisor. Consequently a downstream object that retains only zeros cannot recover `\tau`. In the positive control, all polynomial zeros run to infinity while the determinant values retain a nontrivial `e^z` factor.

This gives a dynamic counterpart to AF-017: there, multiplication by a zero-free analytic factor changed arithmetic provenance while preserving a meromorphic divisor. Here a zero-free factor is **generated by the compression/assembly itself** from diffuse trace mass. A divisor-level argument must therefore prove that such a factor is either impossible or irrelevant; it cannot infer that from zero convergence alone.

### Regularization is a declared quotient, not a harmless normalization

Equation (14) quotients out the first trace moment. In problems where that moment is known a priori to be nonstructural, this may be exactly the correct canonicalization. But if the trace is one of the few quantities that survives the preceding compression, `\det_2` removes it by construction.

An arithmetic or spectral application must therefore justify the information semantics of regularization before treating the regularized determinant as equivalent evidence.

## Prior art and novelty assessment

The operator-theoretic ingredients are classical. **No theorem-level novelty is claimed.**

- Barry Simon, ***Trace Ideals and Their Applications***, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), DOI `10.1090/surv/120`. Role: standard source for trace ideals, Fredholm determinants, trace-log expansions, determinant continuity, and regularized determinants.
- Folkmar Bornemann, **“On the numerical evaluation of Fredholm determinants,”** *Mathematics of Computation* 79(270), 871–915 (2010), DOI `10.1090/S0025-5718-09-02280-7`. Role: modern authoritative treatment of Fredholm determinant definitions and trace-class approximation/continuity; useful background for distinguishing operator convergence from determinant convergence.
- Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev, and Dmitriy Zanin, **“The product formula for regularized Fredholm determinants,”** *Proceedings of the American Mathematical Society, Series B* 8 (2021), 42–51; arXiv:`2007.12834`. Role: modern source for the standard regularized Fredholm determinant framework, including the `\det_2` modification that removes the first trace term.

The estimate (4) and examples (7), (11) are elementary consequences of this classical machinery. The durable Arithmetic Fidelity content is their placement in the current compression hierarchy: **under bounded trace-class mass and vanishing operator scale, all determinant information above first order disappears; the surviving first-order trace becomes a zero-free exponential; signed cancellation can erase even that channel; and `\det_2` removes it deliberately.**

## Consequences for Arithmetic Fidelity

AF-108 through AF-110 now separate three different notions of spectral/operator survival.

A uniform Schatten budget can preserve membership in an operator ideal without preserving scalar observables. Exact Schatten-norm conservation upgrades weak assembly to full ideal-norm fidelity. But if the operator scale itself collapses while trace-class mass remains diffuse, the Fredholm determinant can compress the entire remaining cloud to one first-order scalar and the zero divisor can then erase that scalar completely.

For RH-oriented determinant or trace-formula constructions, this supplies a concrete audit order. Before interpreting a limiting determinant or its zeros, determine whether spectral mass is tight in the topology relevant to the operator, whether signed cancellation can hide total variation, which low-order trace moments survive the limit, and which of those moments are removed by the chosen regularization. A zero-free factor should be treated as a possible carrier of lost provenance until an independent theorem proves otherwise.

This also sharpens the line's general composition principle. Information loss can occur in successive, qualitatively different stages:

\[
\text{trace-class operator cloud}
\longrightarrow
\text{ordinary determinant}
\longrightarrow
\text{regularized determinant or zero divisor}.
\]

In the regime (1), the first arrow contracts the cloud to at most the trace exponential, and the second can erase that residual exactly. Once that channel has been removed, no later operation on the regularized determinant or divisor can reconstruct it without importing additional structure.