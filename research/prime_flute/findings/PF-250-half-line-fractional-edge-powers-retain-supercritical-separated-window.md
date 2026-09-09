# PF-250 — half-line fractional edge powers retain a supercritical separated window

**Status:** `LITERATURE+DERIVED + SHARP-FREE-FRACTIONAL-THRESHOLD + FULL-OUTPUT-CALIBRATION + POSITIVE/ROUTE-NARROWING`.

PF-248 and PF-249 treat the square-root edge law of PF-247's constant half-line Jacobi limit. They show that the Dirichlet image cancels the bilateral `n^{-2}` tail in every fixed output row and that positive separation preserves the resulting full-output threshold `R<5/2`. The accepted clue `CLUE-critical-jacobi-square-root-decay-window.md`, however, still contains an older bilateral calibration suggesting that a general edge law `lambda^sigma` would need `sigma>1/4` merely to leave a strict `R>1` window.

That criterion is not the correct half-line calibration. For every noninteger fractional exponent

\[
0<\sigma<1,
\]

the spectral fractional power of the constant Dirichlet half-line Jacobi operator has the same image cancellation. Its fixed-row tail gains one full power relative to the bilateral kernel, and after any fixed positive output separation the sharp weighted full-output threshold is

\[
\boxed{
R<\frac32+2\sigma.
}
\]

Thus even a quarter-root edge law `sigma=1/4` leaves the genuine free separated window

\[
\boxed{1<R<2.}
\]

The square-root case `sigma=1/2` recovers PF-249's `R<5/2` exactly. Consequently, **a small positive fractional edge exponent is not by itself a free-model obstruction to PF-243**. The live difficulty is pushed back to the actual scalar factor and, especially, to whether PF-247's first-moment-critical variable parity chains preserve the half-line cancellation strongly enough.

This is not a theorem about the actual Prime Flute seam. The exact half-line fractional kernel is classical prior art; the project-specific contribution here is the sharp separated weighted threshold and its use to remove the obsolete `sigma>1/4` free-model kill criterion.

## Claim

On `ell^2(N_0)` let

\[
(J_0u)_j=-\frac14u_{j-1}+\frac12u_j-\frac14u_{j+1},
\qquad u_{-1}=0,
\]

and define

\[
S_\sigma=J_0^\sigma,
\qquad
Ne_n=(n+1)e_n,
\qquad
E_d=e^{-dN},
\qquad d>0.
\]

For every `0<sigma<1` and `R>=0`:

1. the matrix kernel of `S_sigma` is
   \[
   \boxed{
   (S_\sigma)_{mn}
   =c^{(\sigma)}_{|m-n|}-c^{(\sigma)}_{m+n+2},
   }
   \tag{1}
   \]
   where
   \[
   \boxed{
   c^{(\sigma)}_k
   =\frac{(-1)^k\Gamma(2\sigma+1)}
   {4^\sigma\Gamma(\sigma-k+1)\Gamma(\sigma+k+1)};
   }
   \tag{2}
   \]
2. for each fixed `m`, as `n->infinity`,
   \[
   \boxed{
   (S_\sigma)_{mn}
   =-2C_\sigma(2\sigma+1)(m+1)n^{-2\sigma-2}
   +O_m(n^{-2\sigma-3}),
   }
   \tag{3}
   \]
   with
   \[
   C_\sigma
   =\frac{\Gamma(2\sigma+1)\sin(\pi\sigma)}
   {\pi4^\sigma}>0;
   \tag{4}
   \]
3. the separated weighted operator satisfies the sharp equivalence
   \[
   \boxed{
   E_dS_\sigma N^R\in\mathcal S_2
   \quad\Longleftrightarrow\quad
   R<\frac32+2\sigma;
   }
   \tag{5}
   \]
4. for `R>=3/2+2sigma`, `E_dS_sigma N^R` has no bounded extension;
5. the same threshold holds for the adjoint orientation `N^RS_sigma E_d`.

The theorem is deliberately restricted to `0<sigma<1`. At the integer endpoint `sigma=1`, `J_0` is tridiagonal and the algebraic tail disappears rather than continuing the noninteger formula.

## 1. Spectral half-line powers are Toeplitz minus an image term

The discrete sine transform diagonalizes `J_0` with multiplier

\[
\lambda(t)=\frac12-\frac12\cos t=\sin^2\frac t2,
\qquad 0<t<\pi.
\tag{6}
\]

Hence `S_sigma` has multiplier `sin^{2sigma}(t/2)`. Put

\[
c^{(\sigma)}_k
=\frac1\pi\int_0^\pi
\sin^{2\sigma}\frac t2\cos(kt)\,dt.
\tag{7}
\]

The standard beta/gamma evaluation gives (2). Product-to-sum for the sine basis gives (1): the first term is the full-line Toeplitz coefficient, while the second is the Dirichlet image.

The exact same kernel, with the harmless factor corresponding to the normalization `J_0=(-\Delta_{\mathbb N})/4`, appears in the spectral fractional discrete half-line literature. In particular, Das--de la Fuente-Fernandez (2026), Appendix A, writes the half-line kernel as the difference of the two gamma-ratio terms. Thus (1)--(2) are not claimed as new fractional-Laplacian theory.

For `k>=1`, Euler reflection rewrites (2) as

\[
\boxed{
 c^{(\sigma)}_k
 =-C_\sigma
 \frac{\Gamma(k-\sigma)}{\Gamma(k+\sigma+1)}.
}
\tag{8}
\]

If

\[
r_\sigma(k):=
\frac{\Gamma(k-\sigma)}{\Gamma(k+\sigma+1)},
\]

then

\[
r_\sigma(k+1)
=\frac{k-\sigma}{k+\sigma+1}r_\sigma(k)
\]

and therefore

\[
\boxed{
 r_\sigma(k)-r_\sigma(k+1)
 =\frac{2\sigma+1}{k+\sigma+1}r_\sigma(k).
}
\tag{9}
\]

The gamma-ratio asymptotic

\[
r_\sigma(k)=k^{-2\sigma-1}(1+O(k^{-1}))
\tag{10}
\]

now makes the extra half-line power transparent.

## 2. The image term improves every noninteger fractional tail by one power

Fix `m` and take `n>m`. Equations (1) and (8) give

\[
(S_\sigma)_{mn}
=-C_\sigma\bigl[r_\sigma(n-m)-r_\sigma(n+m+2)\bigr].
\tag{11}
\]

The two arguments differ by `2m+2`. Expanding (10), or summing the exact first difference (9), yields

\[
r_\sigma(n-m)-r_\sigma(n+m+2)
=2(2\sigma+1)(m+1)n^{-2\sigma-2}
+O_m(n^{-2\sigma-3}),
\tag{12}
\]

which proves (3).

The bilateral coefficient alone has size `n^{-1-2sigma}`. The half-line image therefore improves every fixed row to

\[
 n^{-2-2\sigma}.
\]

This is the general mechanism behind PF-248's square-root `n^{-3}` cancellation; it is not special to `sigma=1/2`.

A fixed output row weighted on the input by `N^R` is square summable exactly when

\[
\sum_n n^{2R-4\sigma-4}<\infty,
\]

namely

\[
R<\frac32+2\sigma.
\tag{13}
\]

## 3. Positive separation preserves the same threshold in full output

For completeness, the fixed-row statement extends to the complete output space exactly as in PF-249.

For fixed `m`, define

\[
A_m(R)=\sum_{n\ge0}(n+1)^{2R}|(S_\sigma)_{mn}|^2.
\tag{14}
\]

On `n<2m+2`, `0<=J_0<=1` implies `||S_sigma||<=1`, so

\[
\sum_{n<2m+2}(n+1)^{2R}|(S_\sigma)_{mn}|^2
\le C_R(m+1)^{2R+1}.
\tag{15}
\]

On `n>=2m+2`, use (9) to telescope (11). Standard gamma-ratio bounds give

\[
r_\sigma(k)\le C_\sigma'(k+1)^{-2\sigma-1},
\]

hence

\[
\boxed{
|(S_\sigma)_{mn}|
\le C_\sigma''(m+1)(n+1)^{-2\sigma-2}.
}
\tag{16}
\]

Therefore the tail of (14) is finite when

\[
2R-4\sigma-4<-1,
\]

which is exactly (13). In that range `A_m(R)` grows at most polynomially in `m`. The fixed positive separation then absorbs the complete output sum:

\[
\begin{aligned}
\|E_dS_\sigma N^R\|_2^2
&=\sum_{m,n\ge0}
 e^{-2d(m+1)}(n+1)^{2R}|(S_\sigma)_{mn}|^2\\
&=\sum_{m\ge0}e^{-2d(m+1)}A_m(R)<\infty.
\end{aligned}
\tag{17}
\]

Conversely, (3) with `m=0` has a nonzero leading coefficient. If `R>=3/2+2sigma`, the zeroth output row of `E_dS_sigma N^R` is not in `ell^2`. A bounded operator would have every row in `ell^2` because its adjoint maps `e_0` into the Hilbert space. Thus no bounded extension exists at or above the threshold. This proves (5).

## 4. Consequence for the PF-243 exponent budget

The half-line correction changes the generic fractional-edge budget qualitatively.

For a free spectral factor whose first nonconstant edge term is `lambda^sigma` with `0<sigma<1`, the relevant separated calibration is

\[
\boxed{
1<R<\frac32+2\sigma,
}
\tag{18}
\]

not the older bilateral fixed-row interval `R<1/2+2sigma`.

Two cases matter immediately:

\[
\sigma=\frac12
\quad\Longrightarrow\quad
R<\frac52,
\]

recovering PF-249, while

\[
\boxed{
\sigma=\frac14
\quad\Longrightarrow\quad
R<2.
}
\tag{19}
\]

Thus identifying an actual normalized Robin factor with quarter-root-type edge behavior would **not** by itself close PF-243. Even substantially weaker positive fractional regularity still leaves a free half-line interval above `R=1`.

The decisive issue is now more structural: does the specific `O(j^{-2})` PF-247 variable Jacobi tail preserve the image-type cancellation or an equivalent weighted estimate after the actual seam-normalized source map is inserted? PF-248 already warns that first-moment free-Jost transfer is unavailable, so (18) must not be transferred to the actual chain by analogy.

## 5. Prior-art and novelty audit

The half-line fractional kernel is classical/recently explicit prior art, not a new general theorem here.

- U. Das and R. de la Fuente-Fernandez, *An optimal fractional Hardy inequality on the discrete half-line*, Calculus of Variations and Partial Differential Equations 65 (2026), article 46, DOI `10.1007/s00526-025-03217-w`, arXiv:2507.06716. Their Section 2 and Appendix A use the spectral powers `(-Delta_N)^sigma` and record the gamma-ratio half-line kernel. Our `J_0` is simply `(-Delta_N)/4`.
- O. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea, J. L. Varona, *Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications*, Advances in Mathematics 330 (2018), 688--738, DOI `10.1016/j.aim.2018.03.023`, arXiv:1608.08913, provides the classical full-line fractional-discrete kernel scale used already in PF-248.
- F. Stampach and J. Waclawek, *Optimal fractional discrete Hardy inequalities on the half-line*, arXiv:2608.26936 (2026), studies a **Toeplitz compression** realization of the full-line fractional operator. That is not the spectral Dirichlet half-line power used in PF-248--PF-250; the distinction matters precisely because the spectral half-line image term is the source of the extra decay here.

The new Mathia content is therefore narrow: equations (5), (18), and (19) are the weighted positive-separation consequence needed by the PF-243 route. They correct the research program's previous bilateral exponent budget without claiming novelty for fractional discrete Laplacians themselves.

## 6. Falsification and boundary checks

1. **Square-root recovery.** At `sigma=1/2`, (2) reduces to PF-248's `c_k=-2/[pi(4k^2-1)]`, (3) becomes `-2(m+1)/(pi n^3)+O_m(n^-4)`, and (5) gives exactly PF-249's `R<5/2` threshold.
2. **Quarter-root check.** At `sigma=1/4`, (3) has nonzero `n^{-5/2}` fixed-row tail, so the sharp weighted threshold is `R<2`; the endpoint `R=2` diverges logarithmically in the squared row.
3. **Integer endpoint is exceptional.** Do not take `sigma->1` in (3) as a statement about `sigma=1`: `sin(pi sigma)` kills the long-range coefficient and `J_0` itself is local.
4. **Zero exponent is exceptional.** For every fixed `sigma>0` the algebraic tail is present, although its amplitude tends to zero as `sigma->0+`; at `sigma=0` the operator is the identity and has no off-diagonal tail.
5. **Spectral versus Toeplitz half-line fractionalization.** Replacing the spectral Dirichlet power by compression of the bilateral fractional operator removes the image structure and changes the kernel. Such a substitution would invalidate the PF-243 calibration.
6. **No variable-chain transfer.** Nothing here proves that PF-247's `O(j^-2)` variable chains retain (3), (16), or any `R>1` bound. That remains the main fixed-axis gate.
7. **No actual Robin identification.** The scalar/noncommutative factor appearing in the complete-lift seam-normalized Poisson map has still not been identified. The result says only that a positive fractional edge exponent, including `1/4`, is not a free half-line obstruction once that factor is known.
8. **Later geometry remains open.** `T_a`, the width-dependent hypercycle/axis coordinate defect, Hardy ends, physical `P/H` recoupling, finite-pant completion, neighboring-cell extension, global weak-`S_1` reassembly, and every RH-level bridge are untouched.
