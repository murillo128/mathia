# PC-107 — fixed-shell Hardy Fredholm zeros are too sparse for Riemann zero density

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` + `DECISIVE-BOUNDARY`. PC-075 isolates a canonical self-adjoint trace-class Hardy/Hankel remainder `T_n`, and PC-106 leaves the zero set of its fixed-conductor Fredholm determinant

\[
D_n(z):=\det(I-zT_n)
\]

as a genuinely open boundary after classifying all finite relative moments. The trace-class hypothesis itself closes the most direct version of that boundary. For every fixed conductor `n>1`, the reciprocal moduli of the nonzero zeros of `D_n` are absolutely summable, and its zero-counting function satisfies

\[
N_{D_n}(R)=o(R).
\]

By contrast, the Riemann--von Mangoldt formula gives `N_zeta(T) ~ (T/(2 pi)) log T` for the nontrivial Riemann zeros. Consequently no fixed-shell `D_n` can directly realize the Riemann-zero ordinate divisor under an asymptotically linear geometric normalization. The obstruction is not the reality of the Fredholm zeros but their **nuclear sparsity**.

This is a classical trace-ideal consequence specialized to the exact Prime-Circle Hardy remainder. No theorem-level novelty is claimed for Fredholm determinants, trace ideals, or the Riemann--von Mangoldt formula.

## 1. The Prime-Circle remainder is self-adjoint and trace class

PC-075 gives the exact residue decomposition

\[
W\Gamma_nW^*=-\frac1n C_n\otimes H+T_n,
\qquad T_n\in\mathcal S_1.
\]

Here `Gamma_n` is self-adjoint under the canonical Hardy basis identification, `C_n` is a finite real symmetric Ramanujan matrix, and `H` is the self-adjoint Hilbert matrix. Therefore

\[
\boxed{T_n=T_n^*\in\mathcal S_1.}
\]

Let the nonzero eigenvalues of `T_n`, repeated with multiplicity, be

\[
\lambda_{n,1},\lambda_{n,2},\ldots .
\]

Self-adjointness gives `lambda_{n,j} in R`, and trace class gives

\[
\boxed{
\sum_j |\lambda_{n,j}|=\|T_n\|_1<\infty.
}
\]

The argument below uses only these exact operator properties; none of the cyclotomic-period classification of PC-106 is needed.

## 2. The Fredholm zero divisor has absolutely summable reciprocals

For a trace-class operator the ordinary Fredholm determinant has the canonical eigenvalue product

\[
\boxed{
D_n(z)=\det(I-zT_n)
=\prod_j(1-z\lambda_{n,j}),
}
\]

with locally uniform convergence. Its nonzero zeros, with multiplicity, are therefore exactly

\[
z_{n,j}=\lambda_{n,j}^{-1}.
\]

Hence

\[
\boxed{
\sum_{D_n(z)=0}\frac{m(z)}{|z|}
=
\sum_j|\lambda_{n,j}|
=
\|T_n\|_1
<\infty.
}
\]

The standard trace-class determinant bound also gives

\[
\boxed{
|D_n(z)|\le \exp\!\bigl(|z|\,\|T_n\|_1\bigr).
}
\]

The reciprocal-summability statement is the stronger discriminator here. An order-one entire function can still have a much denser zero set; trace class forces this particular genus-zero zero divisor.

## 3. Trace class forces sublinear zero counting

Write

\[
a_j:=|\lambda_{n,j}|
\]

in nonincreasing order, omitting zero eigenvalues. Since `sum_j a_j<infinity`, the elementary summability lemma for a decreasing positive sequence gives

\[
\boxed{j a_j\longrightarrow0.}
\]

Indeed, for any `j`, the block from `floor(j/2)` to `j` contains on the order of `j` terms each at least `a_j`; the tail of the convergent series therefore forces `j a_j -> 0`.

Now let

\[
N_{D_n}(R):=
\#\{z:D_n(z)=0,\ |z|\le R\},
\]

counted with multiplicity. If `N=N_{D_n}(R)>0`, then `a_N>=1/R`, and therefore

\[
0\le \frac{N_{D_n}(R)}R\le N a_N.
\]

As `R -> infinity`, also `N -> infinity` unless `T_n` has finite rank; in the latter case the conclusion is stronger. Thus in all cases

\[
\boxed{
N_{D_n}(R)=o(R).
}
\]

So a fixed-shell Fredholm determinant has strictly sublinear spectral-zero density in its natural determinant variable.

## 4. Riemann zeros have the incompatible `T log T` density

Let `N_zeta(T)` count nontrivial zeros `rho=beta+i gamma` with `0<gamma<=T`, with multiplicity. The classical Riemann--von Mangoldt formula gives

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log T),
\]

and hence

\[
\boxed{
N_\zeta(T)\sim\frac{T}{2\pi}\log T.
}
\]

This is unconditional; no use of RH is made. In particular the Riemann ordinate divisor also fails the reciprocal-summability property. Partial summation gives

\[
\sum_{0<\gamma\le T}\frac{m(\gamma)}{\gamma}
=
\frac{N_\zeta(T)}T
+
\int^{T}\frac{N_\zeta(t)}{t^2}\,dt
=
\frac{(\log T)^2}{4\pi}+O(\log T),
\]

so

\[
\boxed{
\sum_{\gamma>0}\frac{m(\gamma)}{\gamma}=\infty.
}
\]

Therefore the zero divisor of `D_n` cannot equal the Riemann ordinate divisor under any asymptotically linear identification

\[
z=a\gamma+b+o(\gamma),\qquad a\ne0,
\]

or, more generally, under any eventual comparison `c_1 gamma <= |z| <= c_2 gamma` with fixed positive constants. Such a comparison preserves linear-vs-`T log T` counting scale and reciprocal divergence.

This is the relevant Hilbert--Pólya control. Merely observing that the zeros of `D_n` are real would be weak because RH itself predicts real ordinates; the decisive mismatch is the trace-class density law.

## 5. This closes the fixed-conductor zero-set escape left by PC-106

PC-106 proves that every finite moment `Tr(T_n^k)` and every individual Taylor coefficient of `D_n(z)` lies in a fixed-conductor cyclotomic hyperlogarithmic period algebra, but correctly leaves open the possibility that the **full infinite determinant** might still have a subtle zero set. The present argument attacks that remaining possibility at the operator-ideal level rather than coefficient by coefficient.

For every fixed `n`, the chain

\[
\boxed{
\text{Prime-Circle fixed shell}
\to T_n\in\mathcal S_1
\to \det(I-zT_n)
\to \text{direct Riemann-zero spectral divisor}
}
\]

is impossible in the determinant's intrinsic variable. No calculation of higher moments, no resummation of the already-classified Fredholm coefficients, and no hidden cyclotomic simplification can change `sum |lambda_j|<infinity` while the same `T_n` remains trace class.

This does **not** say that `D_n` has an elementary zero set. It says that, whatever those zeros are, their density is already in the wrong trace-ideal class for a direct Riemann-zero realization.

## 6. Sharp boundary: loss of trace class is necessary for Riemann-scale density

The obstruction identifies a useful analytic threshold rather than merely killing one determinant.

For a Hilbert--Schmidt operator `K in S_2`, the regularized determinant

\[
\det_2(I-zK)
\]

has the same reciprocal eigenvalue zero locations but only forces

\[
\sum_j|\lambda_j|^2<\infty,
\qquad
\sum_{\det_2(I-zK)=0}\frac{m(z)}{|z|^2}<\infty.
\]

Riemann--von Mangoldt is compatible with this weaker condition because

\[
\sum_{\gamma>0}\frac{m(\gamma)}{\gamma^2}<\infty.
\]

Thus the result does not rule out every regularized determinant architecture. It proves a precise necessary boundary for this Prime-Circle branch:

\[
\boxed{
\text{a Riemann-density determinant limit cannot remain a fixed trace-class remainder.}
}
\]

Any surviving Hardy mechanism must therefore involve a singular conductor/cross-level limit in which the relevant trace norm ceases to stay finite, a genuinely different operator ideal/regularized determinant, or another non-finite operation derived intrinsically from the geometry. These are necessary escape conditions, not evidence that such a mechanism exists.

The universal Hilbert channels of PC-075 are themselves non-trace-class and have continuous spectrum, so this statement does not repurpose them into a discrete RH spectrum. Likewise the nonlinear uniformization/monodromy branch of PC-017 is outside this Hardy trace-ideal argument.

## 7. Prior-art and novelty audit

The general analytic ingredients are classical. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, AMS (2005), Chapter 3, treats trace, determinants, Lidskii theory, and the trace-class Fredholm product. A current independent statement of the same standard determinant facts appears in E. Gallo, J. Zweck and Y. Latushkin, *Numerical Fredholm Determinants for Matrix-Valued Kernels on the Real Line*, *Integral Equations and Operator Theory* 98 (2026), Proposition 2.1: for trace-class `K`, the Fredholm determinant is entire, obeys `|det(I+zK)| <= exp(|z| ||K||_1)`, and equals the product over eigenvalues.

For the comparison divisor, the Riemann--von Mangoldt law is classical. R. R. Hall, *On the Zeros of the Riemann Zeta-Function*, *Journal of the London Mathematical Society* 59 (1999), 65--75, records the standard formula

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+S(T)+\frac78+E(T),
\]

with `S(T)=O(log T)` and `E(T)=O(1/T)`; NIST DLMF §25.10 gives the standard zero-distribution framework and cites Titchmarsh as the classical source.

Directed searches for trace-class Fredholm realizations of Riemann zeros find a broad operator-theoretic/Hilbert--Pólya literature, but they give no reason to assign novelty to the abstract sparsity argument: it is an immediate consequence of standard trace-ideal theory plus standard zeta-zero counting. The durable Prime-Circle content is narrower: PC-075 proves that the **specific geometry-forced remainder `T_n` is in `S_1`**, and PC-106 explicitly left its full fixed-shell Fredholm zero set open. Combining those persisted facts with the classical counting law closes that exact branch.

## 8. Falsification and remaining scope

The result would fail only if one of the following premises failed:

1. the PC-075 remainder `T_n` were not trace class or not the operator whose ordinary Fredholm determinant is being studied;
2. the zeros of `det(I-zT_n)` were not reciprocals of its nonzero eigenvalues with multiplicity;
3. a summable decreasing eigenvalue sequence could have reciprocal-zero counting comparable to `R log R`; or
4. the classical Riemann--von Mangoldt zero count were not the target divisor being compared.

Premises 2--4 are standard theorems/elementary consequences, and premise 1 is the exact persisted operator theorem of PC-075. The conclusion is deliberately limited to **fixed-conductor ordinary Fredholm determinants and direct/asymptotically linear zero identification**. It does not prohibit an intrinsically derived nonlinear change of spectral variable, an infinite-conductor limit with divergent trace norm, a `det_2`-type construction, or a different Prime-Circle mechanism outside the Hardy remainder. Any such repair must be derived from the canonical geometry rather than chosen to force the Riemann counting law.