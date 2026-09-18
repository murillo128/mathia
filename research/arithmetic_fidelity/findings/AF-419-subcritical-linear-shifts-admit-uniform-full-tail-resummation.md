# AF-419 — Subcritical linear shifts admit uniform full-tail resummation

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `DERIVATIVE-SHIFT` · `UNIFORM-TAIL` · `SUBCRITICAL` · `SCHUR-PIERI` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-417--AF-418 with `R=n+1`, `x=c/n`,

\[
a=\frac{c^2}{4\pi^2}\ge0,
\]

and the normalized exceptional-`1` Cauchy--Binet sector

\[
S_n^{(s)}(a)
:=
\sum_{\ell(\lambda)\le n}
(-1)^{|\lambda|}
\left(\frac{a}{n^2}\right)^{|\lambda|}
 s_\lambda(1^n)^2
 R_{n,\lambda}^{(s)},
\tag{1}
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
\tag{2}
\]

Let `s_n` be any sequence of nonnegative integers satisfying

\[
\boxed{\limsup_{n\to\infty}\frac{s_n}{n}<2.}
\tag{3}
\]

Then for every finite `A`,

\[
\boxed{
\sup_{0\le a\le A}
\left|
S_n^{(s_n)}(a)
-
\exp\!\left(-a e^{s_n/n}\right)
\right|
\longrightarrow0.
}
\tag{4}
\]

In particular, if `s_n/n -> sigma<2`, then locally uniformly for `c` in compact subsets of `[0,\infty)`,

\[
\boxed{
S_n^{(s_n)}\!\left(\frac{c^2}{4\pi^2}\right)
\longrightarrow
\exp\!\left(-\frac{e^\sigma c^2}{4\pi^2}\right).
}
\tag{5}
\]

Thus the fixed-degree candidate from AF-417 is the actual complete signed exceptional-`1` limit throughout the entire subcritical regime. Together with AF-418, this makes `sigma=2` the sharp boundary for the available **absolute-uniform-integrability mechanism**: below it the full partition family is absolutely controlled, above it fixed-width full-height rectangles already destroy absolute control, and at the critical ratio absolute control can fail and a finer `n/log n` window survives.

The proof is not a refinement of the crude fixed-shift estimate from AF-415. It uses the **column structure of a partition** to separate ordinary shapes from columns whose height approaches the full determinant rank. The latter are precisely the shapes capable of turning the derivative factor into a power of `n`, and Pieri's rule shows that their Schur dimension cannot simultaneously grow without paying an exterior-power dimension factor.

## 1. Representation audit and the positive perturbation bound

Equation `(1)` is exactly the AF-417 normalization by the baseline term `E_n^{(s)}`. No gauge or sign convention is changed here. The signed factor remains `(-1)^{|\lambda|}`; absolute values are introduced only for the uniform-tail estimates below.

Put

\[
P_{n,\lambda}:=\prod_{i=1}^n\frac{k_i}{i}\ge1,
\qquad d=|\lambda|.
\tag{6}
\]

For real arguments above `1`, `\zeta` is decreasing, so

\[
0<\prod_i\frac{\zeta(2k_i)}{\zeta(2i)}\le1.
\tag{7}
\]

AF-415's elementary estimate gives

\[
\prod_i
\left(\frac{2k_i-1}{2i-1}\right)^2
\le 9^d.
\tag{8}
\]

Since `P_{n,\lambda}\ge1`, equation `(2)` therefore yields for every integer `s\ge0`

\[
\boxed{
0<R_{n,\lambda}^{(s)}
\le 9^d P_{n,\lambda}^{\,s}.
}
\tag{9}
\]

The replacement of `s-1` by `s` is only an upper bound by a positive factor; it is not used to infer any sign.

## 2. The derivative factor is a column-height product

Let

\[
h_m=\lambda'_m,
\qquad m\ge1,
\tag{10}
\]

be the column heights of `\lambda`. The hook-content formula gives the exact rank-growth identity

\[
P_{n,\lambda}
=
\frac{s_\lambda(1^{n+1})}{s_\lambda(1^n)}.
\tag{11}
\]

Taking the ratio box by box and telescoping down each column gives the more useful form

\[
\boxed{
P_{n,\lambda}
=
\prod_{m\ge1}
\frac{n+m}{n-h_m+m}
=
\prod_{m\ge1}
\left(1+\frac{h_m}{n-h_m+m}\right).
}
\tag{12}
\]

This identity exposes the geometry hidden by the excess degree `d` alone. A column with height bounded away from `n` contributes only `\exp(O(h_m/n))`; a nearly full-height column can contribute a power of `n` and is exactly the kind of shape isolated by AF-418.

Choose constants

\[
\limsup \frac{s_n}{n}<\beta<2,
\qquad
\frac{\beta}{2}<\eta<1.
\tag{13}
\]

For all sufficiently large `n`, `s_n/n\le\beta`.

## 3. Partitions without tall columns have a Cauchy majorant

First suppose every column satisfies

\[
h_m\le\eta n.
\tag{14}
\]

From `(12)` and `\log(1+u)\le u`,

\[
\log P_{n,\lambda}
\le
\sum_m\frac{h_m}{n-h_m+m}
\le
\frac{|\lambda|}{(1-\eta)n}.
\tag{15}
\]

Consequently `(9)` gives

\[
R_{n,\lambda}^{(s_n)}
\le
\left(9e^{\beta/(1-\eta)}\right)^{|\lambda|}.
\tag{16}
\]

Write

\[
C_{\beta,\eta}:=9e^{\beta/(1-\eta)}.
\tag{17}
\]

The positive Schur Cauchy identity then bounds the entire no-tall family by

\[
\sum_{\lambda}
\left(\frac{C_{\beta,\eta}a}{n^2}\right)^{|\lambda|}
 s_\lambda(1^n)^2
=
\left(1-\frac{C_{\beta,\eta}a}{n^2}\right)^{-n^2}
\tag{18}
\]

whenever the argument is below `1`. In particular, for `0\le a\le A` and large `n`, the right-hand side is bounded independently of `n`.

More strongly, the contribution of degrees `d>D` is bounded exactly as in AF-415 by

\[
\sum_{d>D}
\frac{(n^2)_d}{d!}
\left(\frac{C_{\beta,\eta}A}{n^2}\right)^d
\le
2^{-D}
\left(1-\frac{2C_{\beta,\eta}A}{n^2}\right)^{-n^2},
\tag{19}
\]

so the no-tall degree tail tends to zero as `D->infinity` uniformly in all sufficiently large `n` and uniformly on `a\in[0,A]`.

## 4. Tall columns are superexponentially suppressed below `sigma=2`

It remains to show that `(14)` did not discard a collective tail. Let `r\ge1` be the number of columns with

\[
h_m>\eta n.
\tag{20}
\]

Because column heights are nonincreasing, these are exactly `h_1,\ldots,h_r`. Delete those first `r` columns and call the remaining partition `\mu`; its column heights are `h_{r+1},h_{r+2},\ldots` and are all at most `\eta n`.

Repeated Pieri multiplication by elementary symmetric functions reconstructs `\lambda` from `\mu` by vertical strips of heights `h_r,h_{r-1},\ldots,h_1`. Since

\[
e_h(1^n)=\binom nh
\]

and every Schur specialization at `1^n` is nonnegative, Pieri's rule gives the exact dimension inequality

\[
\boxed{
 s_\lambda(1^n)
\le
s_\mu(1^n)
\prod_{m=1}^r\binom n{h_m}.
}
\tag{21}
\]

Split `(12)` into the first `r` columns and the residual columns. For the residual part, the same argument as `(15)` yields

\[
P_{\mathrm{res}}^{\,s_n}
\le
\exp\!\left(\frac{\beta}{1-\eta}|\mu|\right).
\tag{22}
\]

For every tall column,

\[
\frac{n+m}{n-h_m+m}
\le
\frac{n+m}{m}
\le n+1.
\tag{23}
\]

Combining `(9)`, `(21)`--`(23)`, and `a\le A`, the absolute weight of `\lambda` is at most a residual no-tall weight times

\[
\prod_{m=1}^r
\left[
\left(\frac{9A}{n^2}\right)^{h_m}
\binom n{h_m}^{\!2}
(n+1)^{s_n}
\right].
\tag{24}
\]

Define the maximum single-tall-column bracket

\[
\varepsilon_n(A)
:=
\max_{\eta n<h\le n}
\left(\frac{9A}{n^2}\right)^h
\binom nh^2
(n+1)^{s_n}.
\tag{25}
\]

For `A>0`, using `\binom nh\le2^n`, `h>\eta n`, and `s_n\le\beta n`,

\[
\log\varepsilon_n(A)
\le
-(2\eta-\beta)n\log n+O_A(n).
\tag{26}
\]

Because `2\eta-\beta>0`,

\[
\boxed{n\varepsilon_n(A)\longrightarrow0}
\tag{27}
\]

superexponentially. (`A=0` is trivial.)

For a fixed number `r` of tall columns there are at most `n^r` possible height sequences. The residual `\mu` sum is uniformly bounded by `(18)`. Therefore the absolute contribution of **all** partitions having at least one tall column is bounded by a constant times

\[
\sum_{r\ge1}(n\varepsilon_n(A))^r
=
\frac{n\varepsilon_n(A)}{1-n\varepsilon_n(A)}
\longrightarrow0,
\tag{28}
\]

uniformly for `a\in[0,A]`.

This is the shape-uniform estimate left open by AF-418. Nearly full-height columns are the only place where `(15)` can fail, and `(21)` couples exactly those columns to enough dimension/`n^{-2h}` cost to suppress them whenever the derivative-depth ratio stays strictly below `2`.

## 5. The finite head has the moving Cauchy parameter

It remains to identify the limit of the uniformly controlled head. Put

\[
\sigma_n=\frac{s_n}{n}.
\]

For every fixed partition `\lambda` of degree `d`, AF-417's calculation can be kept uniform for bounded `\sigma_n` rather than taking a limit first:

\[
\log P_{n,\lambda}
=\frac dn+O_\lambda(n^{-2}),
\tag{29}
\]

so

\[
P_{n,\lambda}^{\,s_n-1}
=e^{\sigma_n d}(1+o_\lambda(1)).
\tag{30}
\]

The zeta and odd-distance ratios tend to `1`, and the hook-content formula gives

\[
\frac{s_\lambda(1^n)}{n^d}
\longrightarrow\frac1{H_\lambda}.
\tag{31}
\]

Hence for each fixed `d`, uniformly for `a\in[0,A]`,

\[
\sum_{\lambda\vdash d}
(-1)^d
\left(\frac{a}{n^2}\right)^d
s_\lambda(1^n)^2R_{n,\lambda}^{(s_n)}
-
\frac{(-a e^{\sigma_n})^d}{d!}
\longrightarrow0,
\tag{32}
\]

using the classical identity

\[
\sum_{\lambda\vdash d}\frac1{H_\lambda^2}=\frac1{d!}.
\tag{33}
\]

For fixed `D`, all partitions of degree at most `D` satisfy `(14)` once `n` is large. Equations `(19)`, `(28)`, and `(32)` therefore permit `n->infinity` first and then `D->infinity`, proving `(4)`. Equation `(5)` follows immediately when `\sigma_n->\sigma<2`.

## 6. Arithmetic-fidelity interpretation

AF-417 showed that every bounded partition sees only the compressed derivative-depth coordinate `s_n/n`. AF-418 then demonstrated that growing partitions can retain more information and can destroy any naive all-shape domination. AF-419 identifies exactly how the missing shape information enters below the critical ratio: **column height is the sufficient geometric statistic for separating harmless bulk shapes from the boundary shapes that can amplify the derivative shift**.

The proof also illustrates a reusable fidelity pattern. A scalar complexity variable such as total degree `|\lambda|` is too compressed to control the transformation. Restoring one relational coordinate -- how that degree is distributed into column heights relative to the ambient rank -- exposes the dangerous fiber. Once that structure is retained, Pieri's rule supplies the missing compatibility between amplification and representation dimension, and the apparently unbounded family becomes uniformly controllable.

No rational-prime discriminator is used here, and no RH consequence follows. The value is an exact theorem about when an unbounded observation family can or cannot be replaced by its fixed-complexity limits.

## Prior-art and novelty audit

The hook-content formula, Pieri rule, Schur Cauchy identity, and interpretation of `s_\lambda(1^n)` as a `GL_n` representation dimension are classical; Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed. (1995), Chapter I, is a standard source. Okounkov's Schur-measure framework (*Infinite wedge and random partitions*, Selecta Mathematica 7 (2001), 57--81, arXiv:`math/9907127`) provides the established probability/partition setting for Cauchy-normalized Schur weights. Modern surveys of integrable probability likewise present Cauchy, branching, and Pieri identities as the standard algebraic structure behind Schur measures.

A targeted prior-art search also finds extensive asymptotic work on Schur functions with partition shapes and parameters growing with rank, so neither varying-shape Schur asymptotics nor the use of Pieri/branching bounds is claimed as new. No source located in that audit states the specific AF-417 Euler-log perturbation `(2)`, the subcritical tall-column decomposition `(20)`--`(28)`, or the moving-limit theorem `(4)`. The durable contribution is this exact specialization and the closure of the `sigma<2` uniform-tail gate, not the classical Schur technology used to prove it.

## Boundaries and falsification checks

- The theorem concerns only the exceptional-`1`, double-rank-two Cauchy--Binet sector normalized by `E_n^{(s_n)}`. AF-416's omitted-`1` and one-/zero-singular-block sectors are still uncontrolled for growing derivative shift.
- The strict inequality in `(3)` is essential to this proof. The tall-column suppression uses a choice `beta<2eta<2`; it degenerates at the critical ratio `2`, exactly where AF-418 exhibits non-negligible or divergent full-height rectangles.
- Equation `(4)` does not claim that `s_n/n` must converge. It compares the exact sector with the moving candidate `exp(-a e^{s_n/n})` whenever the ratios stay uniformly below `2` asymptotically.
- The theorem proves absolute uniform integrability below the threshold. It does not rule out a signed cancellation theorem at `sigma>=2`; AF-418 shows only that such a theorem cannot come from the same absolute-domination architecture.
- The constants `9`, `beta`, and `eta` are proof devices and carry no intrinsic transition. The intrinsic boundary comes from the ability of nearly full-height columns to contribute `n^{s_n}` against the `n^{-2h}` diagonal scaling.
- Nothing here proves all-order total positivity, a zeta-zero selector, a prime discriminator, or RH.

## Consequence for the research line

The subcritical branch of `CLUE-linear-derivative-shift-full-tail` is resolved: whenever `limsup s_n/n<2`, the complete exceptional-`1` sector has the fixed-degree Cauchy exponential as its actual locally uniform limit. The clue remains live only for the critical and supercritical regimes, where AF-418 proves that growing shapes defeat absolute domination and any survival of the candidate limit must arise from a genuinely signed global resummation or cancellation mechanism.
