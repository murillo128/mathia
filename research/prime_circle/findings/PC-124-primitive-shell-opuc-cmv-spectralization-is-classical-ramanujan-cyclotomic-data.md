# PC-124 — primitive-shell OPUC/CMV spectralization is classical Ramanujan–cyclotomic data

**Status:** `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`. The finite moment/Gram identities and the prime-level Verblunsky ladder are derived exactly below. Orthogonal polynomials on the unit circle (OPUC), finite CMV matrices, and the interpretation of Ramanujan sums as moments of the equal-mass measure on primitive roots are classical. In particular, Zhedanov (2022) studies precisely this primitive-root measure and gives explicit OPUC families for prime, twice-prime, and prime-power conductors. No theorem-level novelty is claimed for the OPUC/CMV framework.

PC-121--PC-123 studied Toeplitz finite sections built from the **boundary weight** `|Phi_n|^2` and coherent cross-shell polynomial amplitudes. A different natural spectralization starts one step earlier: place equal atomic mass on the primitive vertices themselves, use their Ramanujan moments to Gram--Schmidt the monomials, and represent multiplication by `z` as the canonical finite CMV unitary. This looks attractive because it keeps the complete primitive shell as a spectral measure and produces a genuine five-diagonal unitary operator rather than a scalar evaluation.

For Prime Circle, however, the construction is spectrally tautological. The CMV eigenvalues are exactly the primitive roots fed into the measure, its characteristic polynomial is exactly the cyclotomic polynomial `Phi_n`, the terminal moment determinant is only the classical cyclotomic discriminant, and for a prime conductor the entire Verblunsky sequence is an elementary rational ladder. Thus the canonical OPUC/CMV route does not create a new zeta-sensitive spectrum, functional equation, or critical line.

## 1. Canonical atomic measure of one primitive shell

Fix `n>1` and write

\[
P_n^*=\{\alpha_1,\ldots,\alpha_m\},
\qquad m=\varphi(n),
\]

for the primitive `n`-th roots. The most intrinsic probability measure carried by this shell is the equal-mass measure

\[
\boxed{
\mu_n=\frac1m\sum_{a\in(\mathbb Z/n\mathbb Z)^\times}\delta_{\zeta_n^a}.
}
\]

Its trigonometric moments are exactly normalized Ramanujan sums:

\[
\boxed{
\widehat\mu_n(k)
=\int_{\mathbb T}z^k\,d\mu_n(z)
=\frac{c_n(k)}{\varphi(n)}.
}
\]

This already locates the candidate on a classical arithmetic object: no auxiliary weight, interpolation, or spectral parameter has been introduced.

For `N>=1` define the monomial moment matrix

\[
G_{n,N}
=\left(\widehat\mu_n(j-k)\right)_{0\le j,k<N}
=\left(\frac{c_n(j-k)}m\right)_{0\le j,k<N}.
\]

Let `V_{n,N}` be the `m x N` evaluation matrix

\[
(V_{n,N})_{a,j}=\alpha_a^j,
\qquad 0\le j<N.
\]

Then directly

\[
\boxed{
G_{n,N}=\frac1m V_{n,N}^*V_{n,N}.
}
\]

So the entire OPUC input is simply the Vandermonde geometry of the primitive vertices.

## 2. Exact rank threshold and discriminant determinant

If `N<=m`, the columns of `V_{n,N}` are linearly independent: a nonzero polynomial of degree at most `N-1<m` cannot vanish at all `m` distinct primitive roots. Therefore

\[
G_{n,N}>0\qquad(1\le N\le m).
\]

For `N>m`, rank is at most `m`, hence

\[
\boxed{
\det G_{n,N}=0\qquad(N>\varphi(n)).
}
\]

At the last nonsingular size `N=m`, `V_{n,m}` is the square Vandermonde matrix on the primitive roots. Consequently

\[
\begin{aligned}
\det G_{n,m}
&=m^{-m}|\det V_{n,m}|^2\\
&=\boxed{\frac{|\operatorname{disc}\Phi_n|}{\varphi(n)^{\varphi(n)}}}.
\end{aligned}
\]

Using the classical cyclotomic discriminant formula,

\[
|\operatorname{disc}\Phi_n|
=\frac{n^{\varphi(n)}}{
\displaystyle\prod_{p\mid n}p^{\varphi(n)/(p-1)}},
\]

so even this apparently global Gram determinant is explicitly divisor/cyclotomic data already present in PC-005. It is not a new spectral invariant of the shell.

Equivalently, if `D_{n,N}=det G_{n,N}` and `Q_k^{(n)}` denotes the monic OPUC of degree `k`, then the usual Gram factorization gives

\[
D_{n,m}
=\prod_{k=0}^{m-1}\|Q_k^{(n)}\|_{L^2(\mu_n)}^2
=\prod_{j=0}^{m-2}(1-|\alpha_j^{(n)}|^2)^{m-1-j},
\]

where `alpha_j^(n)` are the Verblunsky coefficients. Hence the full product of their norm defects at the finite endpoint is exactly the normalized cyclotomic discriminant.

## 3. The terminal orthogonal polynomial is exactly `Phi_n`

The monic degree-`m` polynomial

\[
\Phi_n(z)=\prod_{a=1}^m(z-\alpha_a)
\]

vanishes on the entire support of `mu_n`. It is therefore orthogonal to every lower-degree polynomial and has zero `L^2(mu_n)` norm. Thus the finite OPUC chain terminates with

\[
\boxed{Q_m^{(n)}(z)=\Phi_n(z).}
\]

Because `Phi_n(0)=1` for `n>1`, the terminal Verblunsky parameter is

\[
\boxed{\alpha_{m-1}^{(n)}=-1.}
\]

Now consider multiplication by the coordinate,

\[
(M_zf)(z)=zf(z)
\qquad\text{on }L^2(\mu_n).
\]

In the delta basis at the primitive vertices this operator is literally

\[
M_z\simeq\operatorname{diag}(\alpha_1,\ldots,\alpha_m).
\]

After Gram--Schmidt of the standard Laurent basis, the same unitary is represented by the finite CMV matrix associated with the Verblunsky coefficients. Therefore, independently of CMV conventions,

\[
\boxed{
\operatorname{Spec}(\mathcal C_n)=P_n^*,
\qquad
\det(zI-\mathcal C_n)=\Phi_n(z).
}
\]

The spectral measure of the cyclic constant vector is exactly `mu_n`, whose moments are the normalized Ramanujan sums above. The canonical five-diagonal spectral operator has therefore not generated new eigenvalues: it is a unitary change of basis of the original primitive-root multiplication operator.

## 4. Prime conductors collapse to an elementary Verblunsky ladder

The prime case makes the obstruction especially transparent. Let `n=p` be prime and set `m=p-1`. For every nonzero integer `r` with `|r|<p`,

\[
c_p(r)=-1,
\]

so for `1<=N<=p-1`,

\[
\boxed{
G_{p,N}
=\frac{p}{p-1}I_N-\frac1{p-1}J_N.
}
\]

Its eigenvalues are `p/(p-1)` with multiplicity `N-1` and `(p-N)/(p-1)` once. Hence

\[
\boxed{
\det G_{p,N}
=\frac{p^{N-1}(p-N)}{(p-1)^N},
\qquad 1\le N\le p-1.
}
\]

At `N=p-1` this becomes

\[
\det G_{p,p-1}
=\frac{p^{p-2}}{(p-1)^{p-1}},
\]

which is exactly `|disc Phi_p|/(p-1)^{p-1}` because `|disc Phi_p|=p^{p-2}`.

The monic OPUC themselves are equally elementary. For `1<=k<=p-1`, put

\[
\boxed{
Q_k^{(p)}(z)
=z^k+\frac1{p-k}\sum_{j=0}^{k-1}z^j.
}
\]

For every `0<=r<k`, the normalized moment of `z^{k-r}` is `-1/(p-1)`, while

\[
\sum_{j=0}^{k-1}\int z^{j-r}\,d\mu_p
=1-\frac{k-1}{p-1}
=\frac{p-k}{p-1}.
\]

Therefore `Q_k^(p)` is orthogonal to `1,z,...,z^{k-1}`. Its constant term gives the exact Verblunsky sequence

\[
\boxed{
\alpha_{k-1}^{(p)}=-\frac1{p-k},
\qquad 1\le k\le p-1,
}
\]

or, equivalently,

\[
\boxed{
\alpha_j^{(p)}=-\frac1{p-1-j},
\qquad 0\le j\le p-2.
}
\]

The last value is `-1`, as required for a finite measure. The corresponding CMV `rho` parameters are simply

\[
\rho_j
=\sqrt{1-\frac1{(p-1-j)^2}}.
\]

Thus even at a prime birth level, where every non-anchor vertex is new, the canonical CMV operator has an entirely elementary coefficient ladder. There is no hidden prime-specific internal spectrum waiting to be extracted: its eigenvalues remain the primitive `p`-th roots and its recursion coefficients are explicit rational functions of `p`.

For example, at `p=5`,

\[
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(-\frac14,-\frac13,-\frac12,-1\right),
\]

and the terminal polynomial is

\[
Q_4^{(5)}(z)=z^4+z^3+z^2+z+1=\Phi_5(z).
\]

## 5. Matched non-arithmetic control: CMV returns its input support generically

Nothing in the spectral tautology uses cyclotomy. Let

\[
S=\{\beta_1,\ldots,\beta_m\}\subset\mathbb T
\]

be any `m` distinct unit-circle points and put equal mass on them. The same construction gives

\[
M_z\simeq\operatorname{diag}(\beta_1,\ldots,\beta_m)
\]

and therefore the finite CMV representation has characteristic polynomial

\[
\prod_{j=1}^m(z-\beta_j).
\]

So the passage

\[
\text{finite point set}
\to\text{atomic moment measure}
\to\text{OPUC/CMV operator}
\]

is generically a change of coordinates that returns the original support as spectrum. Prime Circle contributes special moment identities -- Ramanujan sums -- and the special support polynomial `Phi_n`, but the spectralization mechanism itself is not arithmetic.

This matched control is important because it distinguishes two statements:

1. the primitive shell certainly contains arithmetic information;
2. representing that already-known shell as a finite CMV spectrum does **not** create an additional arithmetic carrier.

The second statement is the obstruction relevant to an RH mechanism.

## 6. Direct prior-art collision

The closest literature is not merely adjacent OPUC theory; it contains the same primitive-root moment construction.

1. **Alexei Zhedanov, _Ramanujan's trigonometric sums and orthogonal polynomials on the unit circle_, The Ramanujan Journal 59 (2022), 993--1006, DOI `10.1007/s11139-022-00576-2`.** Zhedanov interprets `c_q(k)` as trigonometric moments of the equal-mass finite measure supported on primitive `q`-th roots of unity, constructs the corresponding unit-circle orthogonal polynomials, and gives explicit formulas for `q=p`, `q=2p`, and `q=p^k`. This is a direct prior-art collision with the proposed primitive-shell OPUC route, not merely a broad analogy.
2. **M. J. Cantero, L. Moral and L. Velazquez, _Five-diagonal matrices and zeros of orthogonal polynomials on the unit circle_, Linear Algebra and its Applications 362 (2003), 29--56, DOI `10.1016/S0024-3795(02)00457-3`.** This is the foundational CMV representation: monic OPUC arise as characteristic polynomials of canonical five-diagonal unitary matrices determined by Schur/Verblunsky parameters.
3. Barry Simon's two-volume _Orthogonal Polynomials on the Unit Circle_ (AMS Colloquium Publications 54, 2005) is the standard monograph-level framework for the moment, Verblunsky, and CMV correspondence.

The exact formulas in Sections 1--4 are elementary specializations of that classical framework to the Prime-Circle shell. The useful project-specific contribution is therefore a **negative classification**: this natural operator packaging is already known and cannot count as a new bridge merely because it turns the shell into a five-diagonal matrix.

## 7. Why no Riemann-zero divisor appears

The tempting chain is

\[
\text{primitive roots}
\to\text{Ramanujan moments}
\to\text{OPUC/CMV operator}
\to\text{spectral determinant}
\to\text{RH}.
\]

The exact chain is instead

\[
\boxed{
P_n^*
\to \mu_n
\to \mathcal C_n
\to \det(zI-\mathcal C_n)=\Phi_n(z).
}
\]

All eigenvalues are roots of unity on the unit circle. The only terminal Gram determinant is the classical cyclotomic discriminant. At prime level the recursion coefficients are the rational ladder above. No free complex spectral variable `s`, gamma factor, `s<->1-s` symmetry, or distinguished line `Re(s)=1/2` is forced by the construction.

Taking a Cayley transform of the unitary only maps the same finite rational-angle spectrum to an explicitly transformed finite real spectrum. Taking direct sums over conductors merely rebuilds the exact-order roots-of-unity tower already classicalized by PC-010 and the later solenoidal/refinement findings. To obtain compactness, a trace, or a Dirichlet series from such a direct sum one must choose a conductor-dependent weight; that additional scale is not supplied by the single-shell CMV correspondence and falls back into the already-audited issue of externally imposed spectral wrappers.

Likewise, Dirichlet-transforming the Ramanujan moments across `n` recovers the standard reciprocal-zeta factors already identified in PC-015. The appearance of zeta after that transform would come from the external conductor summation, not from the finite CMV spectrum.

## 8. Relation to PC-121--PC-123

This result is not a restatement of the recent Toeplitz no-go chain.

- PC-121 uses the absolutely continuous Haar weight `|Phi_n(e^{it})|^2` and studies Toeplitz compressions of multiplication by that weight.
- PC-122 and PC-123 use coherent vectors of cyclotomic polynomial amplitudes and classify the resulting block determinant and pseudodeterminant.
- PC-124 instead uses the **atomic primitive-shell measure itself**. Its Toeplitz moment matrix contains normalized Ramanujan sums, and its canonical spectral representation is CMV.

The collapse is correspondingly different: PC-121 is finite-period quasipolynomiality, PC-122/123 are polynomial-Gram rank/syzygy collapse, whereas PC-124 is a finite spectral-measure tautology plus a direct literature collision. Together they close several distinct canonical ways of turning one or finitely many primitive shells into Toeplitz/Hardy/CMV spectral determinants without adding cross-level structure.

## 9. Boundary of the obstruction

PC-124 rules out treating the following as a new RH mechanism by itself:

- the equal atomic probability measure on one primitive shell;
- its Ramanujan moment Toeplitz matrices;
- the OPUC/Verblunsky recursion generated by those moments;
- the finite CMV representation of multiplication by `z`;
- the characteristic polynomial or ordinary finite spectral determinant of that CMV matrix;
- direct claims of new arithmetic from the fact that a five-diagonal unitary has been produced.

It does **not** rule out:

- a cross-level operator that couples different primitive-shell measures **before** they are separately diagonalized;
- a nonuniform weight on primitive vertices if that weight is independently forced by Prime-Circle geometry rather than chosen to engineer a spectrum;
- matrix-valued or old/new couplings retaining extensive relational data such as the cotangent sector surviving after PC-047;
- genuinely nonlinear shell interactions outside the finite canonical cotangent-network class already closed through PC-097;
- the nonlinear uniformization/monodromy direction rooted in PC-017.

Those would be different mathematical objects. The no-go is specifically against the canonical single-shell OPUC/CMV spectralization and its immediate direct-sum packaging.

## 10. Exact audit surface

The conclusion can be falsified at five concrete points.

1. **Moment identity:** verify directly that the `k`-th moment of the equal primitive-root measure is `c_n(k)/phi(n)`.
2. **Vandermonde Gram factorization:** check `G_{n,N}=m^{-1}V^*V`, positivity through `N=m`, and rank loss for `N>m`.
3. **Endpoint determinant:** at `N=m`, compute the square Vandermonde determinant and verify `det G=|disc Phi_n|/m^m`.
4. **CMV spectrum:** represent multiplication by `z` in the atomic basis and in the Gram--Schmidt/CMV basis; the two matrices must be unitarily equivalent and have characteristic polynomial `Phi_n`.
5. **Prime ladder:** for prime `p`, substitute the constant off-diagonal Ramanujan moment `-1/(p-1)` and verify both
   \[
   \det G_{p,N}=\frac{p^{N-1}(p-N)}{(p-1)^N}
   \]
   and
   \[
   \alpha_j^{(p)}=-\frac1{p-1-j}.
   \]

All five are finite exact calculations. If they hold, the canonical primitive-shell CMV operator contains no spectral information beyond the shell it represents.

## Research consequence

The natural atomic spectralization of the primitive/new-vertex layer is now classified:

\[
\boxed{
\text{primitive shell}
\to\text{Ramanujan moment measure}
\to\text{OPUC/CMV}
\to\text{the same cyclotomic support and discriminant}.
}
\]

This branch should not be pursued further as a single-shell Hilbert--Polya-style mechanism. A viable operator continuation must make new relational information appear **before** the primitive shell is reduced to its scalar spectral measure -- for example by cross-level, old/new, or genuinely nonlinear coupling -- rather than re-encoding the already-known primitive roots in a canonical unitary basis.
