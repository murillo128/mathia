# AF-418 — Full-height rectangles expose a sigma=2 absolute-tail transition

## Status

`EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `DERIVATIVE-SHIFT` · `GROWING-PARTITION` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-417 with `R=n+1`, `x=c/n`,

\[
a=\frac{c^2}{4\pi^2}>0,
\]

and the exceptional-`1` normalized Cauchy--Binet terms

\[
\frac{T_{n,\lambda}^{(s)}(c/n)}{E_n^{(s)}(c/n)}
=
(-1)^{|\lambda|}
\left(\frac{a}{n^2}\right)^{|\lambda|}
 s_\lambda(1^n)^2
 R_{n,\lambda}^{(s)},
\]

where

\[
R_{n,\lambda}^{(s)}
=
\prod_{i=1}^{n}
\left(\frac{k_i}{i}\right)^{s-1}
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2,
\qquad
k_i=i+\lambda_{n+1-i}.
\tag{1}
\]

For every fixed integer `r>=1`, take the growing rectangular partition

\[
\lambda^{(n,r)}=(r^n).
\]

Then `|\lambda^{(n,r)}|=rn`, `s_{(r^n)}(1^n)=1`, and `k_i=i+r`. Its normalized term is therefore exactly

\[
\boxed{
\begin{aligned}
C_{n,r}^{(s)}(a)
&:=
\left|
\frac{T_{n,(r^n)}^{(s)}(c/n)}{E_n^{(s)}(c/n)}
\right|\\
&=
\left(\frac{a}{n^2}\right)^{rn}
\binom{n+r}{r}^{s-1}
\frac{\prod_{j=n+1}^{n+r}\zeta(2j)}{\prod_{j=1}^{r}\zeta(2j)}
\left[
\frac{\prod_{j=n+1}^{n+r}(2j-1)}{\prod_{j=1}^{r}(2j-1)}
\right]^2.
\end{aligned}
}
\tag{2}
\]

If `s_n/n -> sigma` with finite `sigma`, then for fixed `r`

\[
\frac1n\log C_{n,r}^{(s_n)}(a)
=
r\left(\frac{s_n}{n}-2\right)\log n
+r\log a
-\frac{s_n}{n}\log(r!)
+o(1).
\tag{3}
\]

Consequently:

- if `sigma<2`, every fixed-width full-height rectangle `(r^n)` is superexponentially negligible;
- if `sigma>2`, every such rectangle has `C_{n,r}^{(s_n)}(a) -> infinity` superexponentially for every fixed `a>0`;
- at `sigma=2`, the ratio `s_n/n` is no longer sufficient to describe these growing partitions. If

\[
\tau_n:=\left(\frac{s_n}{n}-2\right)\log n\longrightarrow\tau\in\mathbb R,
\tag{4}
\]

then

\[
\boxed{
\left(C_{n,r}^{(s_n)}(a)\right)^{1/n}
\longrightarrow
\frac{e^{r\tau}a^r}{(r!)^2}.
}
\tag{5}
\]

In particular, for the exact critical sequence `s_n=2n`, the single column `\lambda=(1^n)` has exponentially growing normalized magnitude whenever `a>1`, equivalently `c>2\pi`.

Therefore the complete exceptional-`1` partition family is **not uniformly absolutely controlled by the AF-415 mechanism** once `sigma>2`; at `sigma=2` absolute control already fails on part of the `c`-axis and depends on the finer window `(4)`. Any proof of the signed full-tail limit proposed after AF-417 in those regimes must exploit cancellations between growing partition sectors. Fixed-degree convergence and absolute Schur domination cannot establish it.

This finding does **not** prove that the signed complete partition sum fails to converge to `exp(-e^sigma a)`. Large alternating contributions may in principle cancel. It proves the sharper obstruction actually forced by the growing family: the full tail retains asymptotic information that is invisible to every fixed partition and destroys the available absolute-dominated-convergence route.

## 1. Exact rectangular term

For `\lambda=(r^n)`, every shifted index is

\[
k_i=i+r.
\]

The Schur specialization is

\[
s_{(r^n)}(1^n)=1,
\tag{6}
\]

because `(r^n)` is the `r`-th determinant power for `GL_n`; equivalently `(6)` follows immediately from the hook-content formula.

The derivative-shift factor telescopes to

\[
\prod_{i=1}^n\frac{k_i}{i}
=
\prod_{i=1}^n\frac{i+r}{i}
=
\binom{n+r}{r}.
\tag{7}
\]

The zeta and odd-distance factors telescope in blocks:

\[
\prod_{i=1}^n\frac{\zeta(2i+2r)}{\zeta(2i)}
=
\frac{\prod_{j=n+1}^{n+r}\zeta(2j)}
{\prod_{j=1}^{r}\zeta(2j)},
\tag{8}
\]

and

\[
\prod_{i=1}^n\frac{2i+2r-1}{2i-1}
=
\frac{\prod_{j=n+1}^{n+r}(2j-1)}
{\prod_{j=1}^{r}(2j-1)}.
\tag{9}
\]

Substitution of `(6)`--`(9)` into `(1)` gives `(2)` exactly. The sign of the original term is `(-1)^{rn}`; `(2)` records its magnitude because the present obstruction concerns absolute tail control.

## 2. The large-order exponent

For fixed `r`,

\[
\log\binom{n+r}{r}
=r\log n-\log(r!)+O_r(n^{-1}),
\tag{10}
\]

while

\[
\log\frac{\prod_{j=n+1}^{n+r}\zeta(2j)}
{\prod_{j=1}^{r}\zeta(2j)}
=O_r(1),
\tag{11}
\]

and

\[
2\log
\frac{\prod_{j=n+1}^{n+r}(2j-1)}
{\prod_{j=1}^{r}(2j-1)}
=2r\log n+O_r(1).
\tag{12}
\]

Insert `(10)`--`(12)` into the logarithm of `(2)`. Since `s_n=O(n)` whenever `s_n/n` has a finite limit,

\[
\log C_{n,r}^{(s_n)}(a)
=
 rn\log a
-2rn\log n
+(s_n-1)\bigl(r\log n-\log(r!)+O_r(n^{-1})\bigr)
+2r\log n+O_r(1).
\tag{13}
\]

After division by `n`, the polynomial factors disappear and `(3)` follows.

If `sigma<2` or `sigma>2`, the first term on the right of `(3)` tends respectively to `-infinity` or `+infinity`, dominating the bounded remaining terms. This proves the subcritical/supercritical statements.

When `sigma=2`, however, the apparently lower-order error in `s_n/n` is multiplied by `log n`. Writing it as `tau_n` gives

\[
\frac1n\log C_{n,r}^{(s_n)}(a)
=
r\tau_n+r\log a-2\log(r!)+o(1),
\]

which proves `(5)`.

The critical window in derivative depth is therefore

\[
s_n=2n+\Theta\!\left(\frac{n}{\log n}\right),
\tag{14}
\]

not merely the coarse condition `s_n/n -> 2`.

## 3. Why this blocks AF-415-style domination

AF-415 succeeded for fixed derivative shift because its exact perturbation admitted an `n`-independent exponential-in-degree bound. Combined with the positive Schur Cauchy identity, that supplied a uniform absolute tail and justified exchanging the large-`n` limit with the complete partition sum.

No analogous uniform absolute bound can hold over the full `s_n/n -> sigma` family for `sigma>2`. The absolute normalized partition sum is at least `C_{n,1}^{(s_n)}(a)`, and `(3)` makes that lower bound diverge for every `a>0`. At `sigma=2`, choose `s_n=2n`; then `(5)` with `r=1` gives

\[
\left(C_{n,1}^{(2n)}(a)\right)^{1/n}\to a,
\]

so the same absolute sum diverges exponentially whenever `a>1`.

This is a no-go result for the **available proof architecture**, not yet for the signed limit itself. The alternating factor `(-1)^{|\lambda|}` leaves open the possibility of cancellations among partitions whose size grows with `n`. Such a cancellation theorem would have to be genuinely global; no fixed-degree argument can see the rectangular terms above.

## 4. Arithmetic-fidelity interpretation

AF-417 showed that every fixed partition sees only the coarse ratio `sigma=s_n/n`: a degree-`d` sector is renormalized by `e^{sigma d}`. AF-418 shows that this compressed parameter ceases to be sufficient when the observation class is enlarged to partitions whose complexity grows with determinant order.

The full-height rectangles retain a second scale. Away from `sigma=2` they distinguish the sign of `sigma-2` through a `n log n` exponent; at the critical value they retain the finer variable `tau_n=((s_n/n)-2)log n`. Thus the operation "take every fixed partition limit" forgets information that is still visible to the complete partition tail.

This is a direct instance of the line's mandate: a property that appears stable under every bounded-complexity probe need not survive passage to an unbounded family. Here the missing information is not arithmetic-prime data, and no RH consequence follows, but the mechanism is exact and directly constrains the live large-order determinant route.

## Prior-art and novelty audit

The hook-content formula, the specialization `s_\lambda(1^n)` as a `GL_n` representation dimension, and Schur/Cauchy partition technology are classical; Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed. (1995), Chapter I, and Okounkov, *Infinite wedge and random partitions*, Selecta Mathematica 7 (2001), 57--81, provide the standard background already used in AF-415 and AF-417. A targeted search also confirms the standard hook-content specialization and the established Schur-measure setting for partition sums.

No novelty is claimed for those ingredients, for determinant-power representations, or for elementary fixed-`r` asymptotics of binomial coefficients. The durable Mathia result is the exact specialization of AF-417 to a partition family whose shape grows with `n`, which exposes the `sigma=2` absolute-tail transition and the finer `n/log n` critical window that fixed-degree analysis cannot detect.

## Boundaries and falsification checks

- The theorem is about individual growing rectangular sectors and the resulting **absolute-tail obstruction**. It does not prove divergence, nonconvergence, or a different limit for the signed complete partition sum.
- `r` is fixed while `n -> infinity`. Rectangles whose width also grows with `n` may introduce additional scales; they are not needed for the obstruction above.
- For `sigma<2`, `(r^n)` is negligible for every fixed `r`, but this does not by itself provide a uniform majorant over all partition shapes. Subcritical full-tail resummation remains open.
- At `sigma=2`, specifying only `s_n/n -> 2` is insufficient. Formula `(5)` requires the refined limit `(4)`; if `tau_n` has no limit, the rectangular term can exhibit corresponding subsequential behavior.
- The threshold `a=1` for `s_n=2n`, `r=1` is a threshold for that single normalized sector, not a claimed singularity of the full determinant.
- Nothing here establishes a prime discriminator, zeta-zero selection mechanism, total positivity, or RH.

## Consequence for the research line

The growing-shift full-tail question from AF-417 must be split by regime. For `sigma<2`, an absolute-tail proof remains plausible but requires a genuinely shape-uniform estimate. For `sigma>2`, AF-415-style dominated convergence is impossible because full-height rectangular sectors already diverge in absolute value. At `sigma=2`, the complete tail sees the additional critical variable `(s_n/n-2)log n`, so any claimed limit depending only on `sigma` would require nontrivial cancellation of sequence-dependent exponentially large sectors.

The next decisive test is therefore no longer one generic uniform majorant for all finite `sigma`: prove subcritical absolute resummation for `sigma<2`, or identify the global signed cancellation/resummation mechanism required at and above the critical derivative-depth ratio.