# AF-335 — Even middle singularity is a one-real-dimensional fidelity defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `SELF-INVERSIVE`, `DIMENSION-TIGHT`, `MINIMAL-LIFT`, `STRUCTURAL-RECOVERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

For centered even-support unit-circle configurations, the middle self-inversive singularity loses **exactly one real degree of information** on a nonempty open singular patch, even though its image is cut out by one complex equation.

Let

\[
n=2m\ge4,
\qquad
Z=(z_1,\ldots,z_n)\in(S^1)^n,
\]

write

\[
s_k(Z)=\sum_{j=1}^n z_j^k,
\qquad
E(Z)=\prod_{j=1}^n z_j,
\]

and let `e_k(Z)` be the elementary symmetric functions. Define the centered source manifold

\[
\mathcal C_n=\{Z:s_1(Z)=e_1(Z)=0\}
\tag{1}
\]

on its noncollinear smooth locus, the low-harmonic compression

\[
H(Z)=(s_2(Z),\ldots,s_m(Z))\in\mathbb C^{m-1},
\tag{2}
\]

and the middle-singular source stratum

\[
\mathcal S_n=\{Z\in\mathcal C_n:e_m(Z)=0\}.
\tag{3}
\]

Then near every rotated regular `n`-gon:

\[
\boxed{\dim_{\mathbb R}\mathcal C_n=n-2,}
\tag{4}
\]

\[
\boxed{\dim_{\mathbb R}\mathcal S_n=n-3,}
\tag{5}
\]

while the singular harmonic image lies in the smooth complex hypersurface

\[
\mathcal Y_m
=
\{(s_2,\ldots,s_m):e_m(s_2,\ldots,s_m)=0\}
\subset\mathbb C^{m-1}
\tag{6}
\]

of real dimension

\[
\boxed{\dim_{\mathbb R}\mathcal Y_m=n-4.}
\tag{7}
\]

Moreover,

\[
\boxed{\operatorname{rank}_{\mathbb R}D(H|_{\mathcal S_n})=n-4}
\tag{8}
\]

at the regular polygon and hence on a nonempty open patch of `\mathcal S_n`. Therefore the low-harmonic compression has locally one-real-dimensional fibres there.

By contrast, the lifted representation

\[
\boxed{(H,E)}
\tag{9}
\]

recovers the complete unordered phase multiset globally on the centered source, including `\mathcal S_n`. Thus the product phase `E\in S^1` is not only sufficient on the middle-singular branch, as in AF-316: on this open singular patch it is **dimension-minimal as a continuous lift**. One real degree is genuinely missing.

The mechanism is structural. On the source, self-inversivity constrains the phase of the middle coefficient, so `e_m=0` costs only one real degree. After compression, the retained harmonic coordinates no longer carry the product phase that supplies that constraint, and the same condition appears as a full complex equation, costing two real output degrees. The one-degree mismatch is exactly the fidelity defect repaired by `E`.

For the eight-point frontier of AF-328--AF-334 this gives a second dimension ledger complementary to AF-334. The unitary target

\[
\{Z\in(S^1)^8:e_1(Z)=e_4(Z)=0\}
\tag{10}
\]

has local real dimension `5` at a regular octagon. A fixed rational-prime common-time orbit has real dimension `1`, so the source-plus-target dimensions fall short of the ambient eight-torus by two real dimensions. Already the centered unitary target `e_1=0` has dimension `6`, leaving a one-real-dimensional deficit for a real-time orbit. These are dimension counts only; they do not prove nonintersection.

No RH consequence is claimed.

## 1. The middle coefficient is intrinsically one-real-dimensional on the unitary source

For roots on the unit circle, the coefficient system is self-inversive:

\[
e_{n-k}=E\,\overline{e_k}.
\tag{11}
\]

At the fixed point `k=m=n/2`,

\[
\boxed{e_m=E\,\overline{e_m}.}
\tag{12}
\]

Locally choose a square root `\eta\in S^1` with

\[
\eta^2=E.
\]

Then

\[
r_m:=\eta^{-1}e_m
\tag{13}
\]

is real-valued. Indeed `(12)` gives

\[
\overline{r_m}
=\eta\,\overline{e_m}
=\eta^{-1}e_m
=r_m.
\]

Consequently the middle-singular condition on the unitary source is locally the single real equation

\[
r_m=0,
\tag{14}
\]

not two independent real equations. At a zero of `e_m`, differentiation of the phase factor contributes nothing, so

\[
D r_m=\eta^{-1}D e_m.
\tag{15}
\]

Thus `D e_m` has real rank at most one along the singular unitary stratum.

This is the source-side form of the information constraint. The phase of `e_m` is not free: it is tied to the unretained total product phase `E`.

## 2. The regular polygon shows that the one-real constraint is genuine

Let

\[
\omega=e^{2\pi i/n},
\qquad
z_j=\rho\omega^j,
\qquad j=0,\ldots,n-1,
\qquad |\rho|=1.
\tag{16}
\]

This is a rotated regular `n`-gon. Its root polynomial is `w^n-\rho^n`, so

\[
e_k=0
\qquad(1\le k\le n-1).
\tag{17}
\]

In particular it lies in `\mathcal S_n`.

Write an infinitesimal unit-circle deformation as

\[
z_j(\varepsilon)=z_j e^{i\varepsilon u_j},
\qquad u_j\in\mathbb R.
\tag{18}
\]

Then

\[
D s_k(u)
=ik\rho^k\sum_{j=0}^{n-1}\omega^{jk}u_j.
\tag{19}
\]

For `k=1`, the real and imaginary parts are the two independent first Fourier modes. Hence the centering map has real rank two at `(16)`, giving `(4)`.

For the middle coefficient, deleting one root from a configuration satisfying `(17)` gives recursively

\[
e_{m-1}(Z\setminus\{z_j\})=(-z_j)^{m-1}.
\]

Therefore

\[
D e_m(u)
=i(-1)^{m-1}\rho^m
\sum_{j=0}^{n-1}(-1)^j u_j.
\tag{20}
\]

The alternating Fourier mode in `(20)` is nonzero and independent of the two first-harmonic modes. Hence the centered condition plus middle singularity has real differential rank three at the regular polygon. This proves `(5)` by the implicit-function theorem.

The same calculation also exhibits why the middle equation is only one-real-dimensional on the source: the differential in `(20)` runs along one fixed real line in `\mathbb C`, exactly as `(15)` predicts.

## 3. Compression turns that one real source constraint into one complex output constraint

Newton's identities express `e_m` as a polynomial in the retained harmonics `s_2,\ldots,s_m` once `s_1=0`. In particular,

\[
m e_m
=(-1)^{m-1}s_m
+\text{a polynomial in }s_2,\ldots,s_{m-1}.
\tag{21}
\]

Therefore

\[
\frac{\partial e_m}{\partial s_m}
=\frac{(-1)^{m-1}}m\ne0.
\tag{22}
\]

So `(6)` is a smooth **complex** hypersurface of `\mathbb C^{m-1}`. Its real dimension is

\[
2(m-1)-2=2m-4=n-4,
\]

proving `(7)`.

At the regular polygon all retained harmonics through order `m` vanish. Equation `(19)` shows that the differentials for

\[
k=2,\ldots,m-1
\]

supply the independent real Fourier pairs of frequencies `2,...,m-1`, while the `k=m` differential is the single alternating mode. Restricting to `T\mathcal S_n` removes the first-harmonic pair and the alternating mode. Hence

\[
\operatorname{rank}_{\mathbb R}D(H|_{\mathcal S_n})
=2(m-2)=n-4,
\]

which is `(8)`.

Because `H(\mathcal S_n)\subset\mathcal Y_m`, this is the maximum possible rank. The nonzero rank minor persists on a neighborhood, so the constant-rank theorem gives locally one-dimensional fibres on a nonempty open singular patch.

At the regular polygon the missing fibre is visible without linearization: every common rotation of the polygon still has

\[
s_2=\cdots=s_m=0,
\tag{23}
\]

so an entire circle of source configurations collapses to the same low-harmonic output.

## 4. The product phase is a sharp one-real lift

AF-316 already gives the exact global recovery mechanism. The harmonics `H` determine

\[
e_2,\ldots,e_m
\]

by Newton's identities. If the product phase `E` is also retained, self-inversivity `(11)` determines

\[
e_{n-k}=E\overline{e_k}
\qquad(0\le k\le m),
\tag{24}
\]

including all coefficients above the middle. Thus `(H,E)` determines the monic root polynomial and hence the complete unordered multiset `Z`, even when `e_m=0`.

On the open singular patch from Section 3, `H` alone has one-dimensional local fibres. No continuous zero-dimensional mark can separate a connected local fibre, while the circle-valued `E` supplies exactly one real degree and restores exact recovery. Therefore the lift has the sharp local information size:

\[
\boxed{\text{middle-singular continuous fidelity defect}=1\text{ real degree}.}
\tag{25}
\]

This closes the minimality boundary deliberately left open in AF-316: the product phase need not be the unique possible lift, but one real degree is necessary on a genuine open part of the singular stratum, and `E` attains that lower bound.

## 5. Consequence for the eight-prime incidence frontier

Take `n=8`, `m=4`. Near a regular octagon,

\[
\dim_{\mathbb R}\{Z\in(S^1)^8:e_1=e_4=0\}=5.
\tag{26}
\]

After quotienting the locally free common-rotation action, the corresponding singular shape space has dimension `4`. This is larger than the three-real-dimensional antipodal-extension subfamily used in AF-318, so that family is a substantial exact source of singular points but does not exhaust the local singular geometry.

The dimension count also separates the complex-time and real-time incidence currencies appearing in AF-334. In the complex torus, `W_1=V(e_1)` has complex dimension `7` and the complex prime-log line has complex dimension `1`, exactly the threshold at which Gallinaro's exponential-algebraic-closedness theorem can force an intersection. On the unitary slice, however,

\[
\dim_{\mathbb R}(W_1\cap(S^1)^8)=6,
\]

so a one-real-dimensional common-time orbit is already one real dimension below generic intersection count. Adding `e_4=0` reduces the unitary target dimension only from `6` to `5`, because the middle coefficient is self-inversive; the resulting real-time incidence is two real dimensions below generic count.

This does not imply that the prime orbit misses either target. It identifies a precise fidelity distinction: **complex solvability, unitary solvability, and low-harmonic recoverability pay different dimension costs even for the same algebraic equations.** Any attempt to transport AF-334's complex EAC existence back to an imaginary-axis statement must supply the missing real-time structure rather than rely on the complex dimension threshold alone.

## Prior art and novelty assessment

The coefficient symmetry and ambient coefficient-space geometry are classical.

- Kathleen L. Petersen and Christopher D. Sinclair, **“Conjugate Reciprocal Polynomials with All Roots on the Unit Circle,”** *Canadian Journal of Mathematics* 60(5) (2008), 1149--1167, DOI `10.4153/CJM-2008-050-8`, studies the geometry and topology of the coefficient space of monic conjugate-reciprocal polynomials with all roots on the unit circle.
- Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, LMS Lecture Note Series 352, Cambridge University Press (2010), pp. 312--321, DOI `10.1017/CBO9780511721274.020`, is direct prior art for the self-inversive relation `(11)`.
- Newton identities and the conversion between power sums and elementary symmetric coefficients are classical; I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), is standard background.

A targeted literature search located the established self-inversive coefficient-space theory but no reason to present the local rank calculation `(19)`--`(25)` as a new general theorem. No broad novelty is claimed. The durable Arithmetic Fidelity contribution is the exact composition of these classical facts with the line's compression question: the even middle-singular source loses one real dimension, its harmonic image loses two, and the resulting one-real mismatch is precisely repaired by the product-phase mark.

## Boundaries and failure modes

- The exact dimension and rank claims are local near the regular polygon and on the resulting nonempty open singular patch. Singular components elsewhere may have lower differential rank or different fibre geometry.
- The theorem concerns ordered configurations for the differential calculation. Passing to unordered configurations is a finite quotient on the distinct-root patch and does not change local dimension.
- `E` is proved dimension-minimal as a **continuous one-real-dimensional lift** on the stated patch. No uniqueness claim is made; another circle-valued or real-valued mark may repair the same defect.
- The low-harmonic compression recovers an unordered phase multiset, not prime labels, the rational primes themselves, or the common time.
- Dimension deficit is not a nonintersection theorem. A one-dimensional curve can meet a higher-codimension target at isolated points. Equations `(26)` and the real-time deficit therefore do not settle AF-328.
- The real/complex comparison does not weaken AF-334's theorem: Gallinaro supplies complex-time intersections for `e_1=0`. It only explains why that result carries no automatic imaginary-axis intersection.
- No uniform conditioning follows from the exact one-degree count. AF-321--AF-327 separately show that exact recoverability and stable recovery have different quantitative requirements.
- No statement about Riemann zeros, the critical line, zero density, or RH follows.

## Consequence for the research line

The middle-singular branch now has an exact information budget. For every even support, the self-inversive fixed coefficient makes `e_m=0` a one-real source constraint, but forgetting the product phase makes it a two-real output constraint. The resulting one-dimensional fidelity defect is not an artifact of the eight-point example: it occurs already at the regular `2m`-gon and persists on an open singular patch.

For the current eight-prime problem this removes another ambiguity about what the singularity means. The lost information is locally neither an unspecified high-dimensional pathology nor a purely algebraic two-complex-real collapse: it is exactly one real phase degree, and `E` is a sharp lift for post-incidence recovery. The unresolved arithmetic content remains the harder first-incidence question identified by AF-328--AF-334: whether the one-real prime-time source can hit the five-real-dimensional unitary singular target at all.