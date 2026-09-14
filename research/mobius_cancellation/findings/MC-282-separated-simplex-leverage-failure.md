# MC-282 — Separated simplex Legendre controls can have no blind pair while virtual leverage tends to zero

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-ARITHMETIC-CONTROL`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-281` reduced the surviving low-depth arithmetic-image route to the directional certificate

\[
\mathbf 1_Z\notin\operatorname{ran}(\mathbf A^*)
\qquad\text{or}\qquad
\Lambda:=\inf_{\mathbf A^*c=\mathbf1_Z}\|c\|_2^2>1.
\tag{1}
\]

Its decisive boundary was that any theorem proving `(1)` must exploit the tight prime shell rather than bare Legendre-symbol algebra. There is an exact separated-prime control showing that this warning is load-bearing even for the **specific empirical-Christoffel/leverage certificate**.

Fix an integer `d>=4` and put

\[
N=2^d-1.
\tag{2}
\]

Take `N` formal target columns indexed by the nonzero vectors

\[
z\in\mathbb F_2^d\setminus\{0\}.
\]

Choose `d` distinguished lower-prime rows and prescribe on those rows the binary column `z`; prescribe zero on every remaining lower-prime row. By the separated-prime realization theorem of `MC-252`, these columns are realized exactly by distinct genuine primes, all larger than the lower-prime cutoff and as far away as needed. Thus the construction is an exact Legendre-symbol matrix, but deliberately **not** a tight `(y,2y]` shell.

Now take target support `t=2` and the same one-extra-degree source depth used at the live frontier,

\[
m=t+1=3.
\tag{3}
\]

Every pair of distinct target columns has syndrome

\[
s=z+w\ne0.
\tag{4}
\]

Hence there is **no blind pair at all**. Nevertheless, for every `d>=5` the `MC-281` signed-synthesis problem is feasible with

\[
\boxed{
\Lambda_{3,d}^{\rm sep}
=
\frac{Z_3(d)}{(2^{d-1}-1)(2^d-Z_3(d))},
\qquad
Z_3(d)=\sum_{j=0}^3\binom dj.
}
\tag{5}
\]

In particular

\[
\Lambda_{3,5}^{\rm sep}
=
\frac{26}{15\cdot6}
=
\frac{13}{45}<1,
\tag{6}
\]

and

\[
\boxed{
\Lambda_{3,d}^{\rm sep}
\sim\frac{d^3}{3\,4^d}
\longrightarrow0.
}
\tag{7}
\]

Therefore the empirical Christoffel value satisfies

\[
\mathfrak C_{3,d}^{\rm sep}
=\frac1{\Lambda_{3,d}^{\rm sep}}>1
\qquad(d>=5),
\tag{8}
\]

so the sufficient certificate `\mathfrak C<1` fails increasingly badly even though the true blind count is exactly zero.

This gives a concrete matched control for the current frontier:

\[
\boxed{
\text{genuine Legendre arithmetic + no blind target + source depth }t+1
\not\Rightarrow
\text{favorable virtual leverage}.}
\tag{9}
\]

The missing ingredient is again quantitative prime localization. Bare reciprocity, primality, a feature surplus, and even exact absence of the target blind relation do not force the endpoint direction to separate or have synthesis cost above one.

No statement is made about the actual tight shell `(y,2y]`, no blind relation is constructed there, and no Möbius or RH consequence follows.

## 1. Use the classical simplex/Hamming matrix as the separated-prime sign pattern

Let the target columns be all nonzero vectors of `F_2^d`. On distinguished lower-prime rows `p_1,...,p_d`, prescribe

\[
\frac{1-(\frac{p_i}{r_z})}{2}=z_i,
\qquad 1\le i\le d,
\tag{10}
\]

and on every other lower-prime row prescribe

\[
\frac{1-(\frac p{r_z})}{2}=0.
\tag{11}
\]

The `d x (2^d-1)` active block whose columns are all nonzero binary `d`-vectors is the standard Hamming parity-check / simplex-generator configuration. Nothing new is claimed for that code.

`MC-252` proves that every finite prescribed binary Legendre matrix is realizable by distinct primes once the target primes are allowed to escape the tight shell. Applying that theorem to `(10)`--`(11)` produces genuine target primes `r_z` with exactly these sign columns.

For an unordered target pair `{r_z,r_w}`, multiplicativity of Legendre symbols gives the lower-prime syndrome

\[
z+w.
\tag{12}
\]

Because the target primes are distinct, `z\ne w`, and over `F_2`

\[
z+w=0\iff z=w.
\]

Therefore no pair is blind.

For each fixed nonzero syndrome `s`, the number of unordered pairs satisfying

\[
z+w=s
\]

is exactly

\[
\boxed{
n_d=2^{d-1}-1.}
\tag{13}
\]

Indeed `z` can be any vector outside `{0,s}`, giving `2^d-2` ordered choices, and `{z,z+s}` is counted twice.

Thus the pair shell has `2^d-1` distinct nonblind sign patterns, each with the same multiplicity `n_d`.

## 2. The depth-three source constraints reduce exactly to low-weight Fourier moments

At source depth `m=3`, selecting lower-prime rows outside `p_1,...,p_d` changes no target sign because those rows were prescribed identically `+1`. Hence duplicate feature columns may occur, but they introduce no new synthesis equations.

The distinct equations are indexed exactly by

\[
L_3:=\{a\in\mathbb F_2^d:\operatorname{wt}(a)\le3\},
\qquad
|L_3|=Z_3(d).
\tag{14}
\]

Let `c_{z,w}` be signed synthesis weights on unordered target pairs, and aggregate them by syndrome:

\[
u_s
:=
\sum_{\{z,w\}:z+w=s}c_{z,w},
\qquad s\ne0.
\tag{15}
\]

Then `A^*c=1` is exactly

\[
\boxed{
\sum_{s\ne0}\nu_s(-1)^{a\cdot s}=1
\qquad(a\in L_3).
}
\tag{16}
\]

For fixed syndrome totals `nu_s`, the Euclidean norm is minimized by distributing the weight equally among the `n_d` pairs in that syndrome class. Cauchy--Schwarz gives

\[
\inf_{c\mapsto\nu}\|c\|_2^2
=
\frac1{n_d}
\sum_{s\ne0}|\nu_s|^2.
\tag{17}
\]

Therefore the leverage problem becomes an elementary minimum-energy Fourier extension on the punctured group `F_2^d\setminus{0}`.

## 3. Parseval solves the punctured Fourier extension exactly

Extend `nu` to all of `F_2^d` by setting

\[
\nu_0=0,
\tag{18}
\]

and use the unnormalized Walsh transform

\[
\widehat\nu(a)
=
\sum_{s\in\mathbb F_2^d}\nu_s(-1)^{a\cdot s}.
\tag{19}
\]

Constraint `(16)` says

\[
\widehat\nu(a)=1
\qquad(a\in L_3).
\tag{20}
\]

The puncture condition `(18)` is, by Fourier inversion at the origin,

\[
\sum_{a\in\mathbb F_2^d}\widehat\nu(a)=0.
\tag{21}
\]

Put

\[
L:=Z_3(d),
\qquad
H:=2^d-L.
\tag{22}
\]

For `d>=4`, `H>0`. Equations `(20)`--`(21)` force the `H` unconstrained Fourier coefficients to have total sum `-L`. Parseval gives

\[
\sum_s|\nu_s|^2
=2^{-d}\sum_a|\widehat\nu(a)|^2.
\tag{23}
\]

Among `H` numbers with fixed sum `-L`, the squared norm is minimized when they are all equal to `-L/H`. Therefore

\[
\begin{aligned}
\min\sum_s|\nu_s|^2
&=
2^{-d}\left(L+H\frac{L^2}{H^2}\right)\\
&=
2^{-d}L\left(1+\frac LH\right)\\
&=
\boxed{\frac LH}.
\end{aligned}
\tag{24}
\]

The minimum is attained explicitly by

\[
\widehat\nu(a)
=
\begin{cases}
1,&a\in L_3,\\
-L/H,&a\notin L_3.
\end{cases}
\tag{25}
\]

Combining `(17)`, `(22)`, and `(24)` proves `(5)` exactly.

No probabilistic independence, asymptotic random-matrix claim, or numerical optimization enters the result.

## 4. The leverage certificate fails although blindness is absent

For `d=4`, `(5)` gives

\[
\Lambda_{3,4}^{\rm sep}=\frac{15}{7}>1,
\]

so the leverage certificate still succeeds. At the next dimension,

\[
Z_3(5)=26,
\qquad
2^5-Z_3(5)=6,
\qquad
n_5=15,
\]

which gives `(6)`. Since

\[
Z_3(d)
=\frac{(d+1)(d^2-d+6)}6
\sim\frac{d^3}{6},
\tag{26}
\]

while

\[
(2^{d-1}-1)(2^d-Z_3(d))
\sim2^{2d-1},
\tag{27}
\]

we obtain `(7)`.

The failure is not caused by a hidden blind row: `(12)` proves that none exists. It is caused by a signed low-degree cubature effect. The virtual endpoint can be synthesized from the nonblind pair rows with increasingly small `l2` mass because the low-depth moment constraints occupy only `Z_3(d)` Fourier directions while the punctured syndrome group has `2^d-1` points, and every syndrome is realized many times by target pairs.

This is exactly the distinction that `MC-281` left open: `Lambda<=1` is only failure of a sufficient certificate, not evidence of blindness.

## 5. Why this is a relevant arithmetic control rather than an abstract matrix trick

The construction uses two classical ingredients whose roles should remain separate.

First, the active binary block is the standard simplex/Hamming configuration. The binary simplex code has length `2^d-1`, dimension `d`, and a generator matrix with one column for each nonzero vector of `F_2^d`; see F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes* (North-Holland, 1977), and the modern Error Correction Zoo entry for the `[2^d-1,d,2^{d-1}]` simplex code. No novelty is claimed for this code or for its relation to the Hamming code.

Second, `MC-252` already audited the prescribed-Legendre realization against quadratic reciprocity, CRT, Dirichlet's theorem, and Hanson--Vaughan--Zhang, *The Least Number with Prescribed Legendre Symbols*, arXiv `1605.05584`. Hence `(10)`--`(11)` can be realized by actual primes; this is not merely a generic binary control.

The Fourier minimization `(20)`--`(25)` is standard finite-group Parseval plus orthogonal projection. Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014), is a standard reference for Walsh--Fourier normalization and Parseval. No novelty is claimed for that Hilbert-space calculation.

A targeted literature search through 14 September 2026 found the standard simplex/Hamming and Boolean-Fourier ingredients, but no source was used to claim this exact separated-prime empirical-Christoffel specialization. The durable content is the matched-control consequence for the `MC-281` certificate, not a novelty claim about coding theory or Fourier projection.

## Boundaries and falsification tests

- **Separated targets are essential.** `MC-252` may place the realizing primes arbitrarily far above the lower-prime cutoff. Nothing here realizes the same simplex matrix with all target primes in `(y,2y]`.
- **The control uses `t=2`.** It tests the same `m=t+1` representation rule in the first nontrivial pair shell; it does not assert failure of leverage at the live growing support `t~(log log y)/log 2`.
- **Padding rows is intentional.** Lower-prime rows outside the distinguished `d` are prescribed identically `+1`. They create duplicate feature equations but no new Fourier directions. A theorem using quantitative tight-shell distribution may forbid such a low-rank pattern; that is exactly the missing arithmetic input.
- **No contradiction with MC-281.** `MC-281` states only that `Lambda>1` or row-span separation is sufficient for blind exclusion. It explicitly allows blind-free configurations with `Lambda<=1`.
- **No contradiction with the tight-shell support floor.** `MC-242` uses the conductor primes all lying near `y`; the separated-prime realization removes that hypothesis and is not subject to its support bound.
- **Euclidean normalization is exact.** The factor `n_d^{-1}` in `(17)` is required because `MC-281` assigns one synthesis coordinate to each target pair, not one coordinate to each distinct syndrome.
- **Complex weights do not improve the minimum.** Cauchy--Schwarz and Parseval apply identically; the real minimizer `(25)` already attains `(24)`.

A direct falsification would be a blind pair in `(10)`--`(12)`, or a synthesis vector of squared norm below `(5)`. Distinct nonzero columns exclude the first, and the Parseval minimization proves the second impossible.

## Consequence for the research line

The current directional-leverage frontier is now sharply stress-tested. Even after requiring genuine Legendre symbols and even when the target blind relation is actually absent, the virtual endpoint can lie in the low-depth row span with synthesis norm far below one once tight prime localization is discarded.

Therefore a successful theorem for the live `MC-281` criterion cannot be justified by **Legendre provenance, reciprocity, feature surplus, no-blindness, or generic low-degree moment geometry alone**. It must use a property that the separated simplex realization cannot preserve: most naturally the simultaneous constraint that every target prime lies in the same moving shell `(y,2y]`, or another quantitative source/target coupling of comparable strength.

That narrows the next proof target from generic leverage theory to a genuinely localized arithmetic statement about the actual shell matrix.