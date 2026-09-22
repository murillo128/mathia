# PC-400 — shell-2 Hankel positivity is the radial-flux selector and the Jacobi spectrum is universal

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical single-shell Hankel/Jacobi spectralization as an independent RH mechanism. The boundary remains open for source-forced cross-shell or cross-level dynamics acting on the recovered coefficients rather than merely repackaging one shell measure.

PC-399 identifies the one-sided shell-2 Chen ladder with the compact moments of the signed measure

\[
\mu_n=(X_2)_*(dX_n),\qquad X_n(z)=\log\Phi_n(z),\qquad X_2(z)=\log(1+z),
\tag{1}
\]

on `[0,L]`, where `L=\log2`. Its surviving boundary explicitly included a possible **sign/coercivity form or spectral invariant** acting on the recovered information. The most canonical such construction is the Hankel moment form and, when positive, its associated self-adjoint Jacobi operator.

That branch can be classified exactly. The Hankel positivity hierarchy is not a new selector: it is precisely the prime-power sign theorem for the radial flux from PC-179 transported through the monotone shell-2 coordinate. On the positive branch, the canonical Jacobi operator has the same spectrum `[0,\log2]` for every prime power. Its recurrence coefficients retain the full shell measure, but that is another representation of the generic moment decoder already identified in PC-399, not a new spectral location principle.

## 1. The Chen ladder is a Hankel moment sequence

Write

\[
m_k(n):=k!\,J_{2^k,n}
=\int_0^L t^k\,d\mu_n(t),
\qquad k\ge0.
\tag{2}
\]

For each `N\ge0`, form the real Hankel matrix

\[
H_N(n)=\bigl(m_{i+j}(n)\bigr)_{0\le i,j\le N}.
\tag{3}
\]

For a real polynomial `p(t)=\sum_{j=0}^N a_jt^j`, its quadratic form is exactly

\[
\boxed{
a^T H_N(n)a
=\int_0^L p(t)^2\,d\mu_n(t).
}
\tag{4}
\]

Thus the standard moment-matrix positivity test is intrinsic here: no kernel, spectral parameter, or auxiliary Hilbert space has yet been chosen. The only input is the shell-2 Chen data already present in PC-399.

## 2. Positive definiteness is exactly the old prime-power radial-flux selector

PC-179 writes, with `z=e^{-x}`,

\[
\rho_n(x)
=-\frac{d}{dx}\log\Phi_n(e^{-x})
=zX_n'(z),
\tag{5}
\]

and proves the exact sign criterion

\[
\rho_n(x)>0\ \text{for every }x>0
\quad\Longleftrightarrow\quad
n\text{ is a prime power}.
\tag{6}
\]

Since `t=X_2(z)=\log(1+z)` is increasing and `z=e^t-1`, the pushed-forward measure has density

\[
d\mu_n(t)
=e^t X_n'(e^t-1)\,dt.
\tag{7}
\]

Hence for a prime power `n`, this density is strictly positive for every `0<t<L`. Every nonzero polynomial is nonzero on a set of positive Lebesgue measure, so (4) gives

\[
\boxed{
H_N(n)\succ0\quad\text{for every }N\ge0
\qquad(n\text{ a prime power}).
}
\tag{8}
\]

The converse is even sharper and does not require an approximation argument. If `n` is not a prime power, then the common-vertex identity gives

\[
m_0(n)=\mu_n([0,L])=\Lambda(n)=0.
\tag{9}
\]

PC-399 proves that `\mu_n\ne0`, so not all higher moments vanish. Let `r\ge1` be the least index with `m_r(n)\ne0`. In `H_r(n)` the `(0,0)` entry is zero while the `(0,r)` entry is `m_r(n)\ne0`. But every positive-semidefinite matrix `M` satisfies

\[
|M_{0r}|^2\le M_{00}M_{rr};
\tag{10}
\]

therefore a PSD matrix with `M_{00}=0` must have a zero first row and column. Consequently `H_r(n)` is not positive semidefinite.

Combining the two directions gives the exact equivalence

\[
\boxed{
 n\text{ is a prime power}
 \quad\Longleftrightarrow\quad
 H_N(n)\succ0\text{ for every }N\ge0.
}
\tag{11}
\]

For every non-prime-power shell there is therefore a **finite Hankel witness** to failure of positivity. No uniform bound on the first witness depth `r` is claimed here.

Equation (11) is useful structurally but not arithmetically new: it is exactly PC-179's sign/coercivity statement after the homeomorphic change of coordinate `t=\log(1+z)`. The infinite Hankel hierarchy has not produced a stronger support criterion than the radial flux already supplied.

## 3. The canonical self-adjoint Jacobi spectrum is independent of the prime power

For a prime power, `\mu_n` is a finite positive measure whose density in (7) is strictly positive throughout `(0,L)`. Its support is therefore all of

\[
\operatorname{supp}\mu_n=[0,L].
\tag{12}
\]

Consider multiplication by the coordinate in `L^2(\mu_n)`,

\[
(M_t f)(t)=t f(t).
\tag{13}
\]

It is a bounded self-adjoint operator. Because the support is compact, polynomials are dense in `L^2(\mu_n)`. Applying Gram--Schmidt to `1,t,t^2,\ldots` yields the orthonormal polynomial basis, in which (13) becomes the standard symmetric tridiagonal Jacobi operator associated with the moments (2).

The spectrum of a multiplication operator is the essential range of its multiplier. Since every open subinterval of `[0,L]` has positive `\mu_n`-measure,

\[
\boxed{
\sigma(M_t)=\sigma(J_n)=[0,\log2]
\qquad\text{for every prime power }n.
}
\tag{14}
\]

Thus the most canonical self-adjoint spectralization of the positive shell-2 moment form has **no arithmetic spectral-set motion at all** across prime powers. Prime-power arithmetic is carried by the cyclic spectral measure `\mu_n`, equivalently by the Jacobi recurrence coefficients, while the spectrum itself is the fixed interval imposed by the chosen shell-2 coordinate.

This distinction matters for RH-oriented interpretation. The Jacobi matrix is not producing a new distinguished set of spectral points whose location could encode zeta zeros. It is the standard operator representation of a compact positive measure already reconstructed by PC-399.

## 4. Exact control at shell 2: a scaled Hilbert matrix and shifted Legendre system

The reference shell itself makes the classicality explicit. For `n=2`, the coordinate equals the potential:

\[
t=X_2(z)=\log(1+z),\qquad d\mu_2=dt.
\tag{15}
\]

Hence

\[
\boxed{
m_k(2)=\int_0^L t^kdt=\frac{L^{k+1}}{k+1}.
}
\tag{16}
\]

The Hankel matrix is therefore

\[
H_N(2)=\left(\frac{L^{i+j+1}}{i+j+1}\right)_{0\le i,j\le N},
\tag{17}
\]

which is diagonally congruent to the classical Hilbert moment matrix. The orthogonal polynomials are simply shifted and rescaled Legendre polynomials on `[0,L]`, and their Jacobi operator again has spectrum `[0,L]`.

So the spectral construction already contains, at its canonical reference shell, one of the standard textbook compact moment systems. The other prime-power shells alter the positive weight but not the spectral interval.

## 5. Signed shells do not recover a new spectral set through the canonical positive repair

For a non-prime-power shell, `\mu_n` is a genuinely signed measure: it has zero total mass by (9), is nonzero by PC-399, and its density changes sign by PC-179. The ordinary positive-measure Hilbert-space Jacobi construction therefore does not apply directly to `\mu_n`.

A canonical way to force positivity is to pass to total variation `|\mu_n|`. This still does not create an arithmetic spectral set. The density in (7) is real-analytic on `(0,L)` and is not identically zero; its zeros are therefore isolated in the interior. Consequently

\[
\operatorname{supp}|\mu_n|=[0,L],
\tag{18}
\]

and multiplication by `t` in `L^2(|\mu_n|)` again has spectrum `[0,L]`.

The same conclusion holds for any positive replacement equivalent to `|\mu_n|` with positive almost-everywhere density. This is **not** a no-go for arbitrary indefinite-metric, nonlinear, or source-forced signed-measure constructions; it only shows that the standard move from moments to a positive Jacobi spectral problem does not generate a new support geometry.

## 6. Prior art and novelty audit

Every abstract ingredient of the Hankel/Jacobi step is classical. The *Encyclopedia of Mathematics*, **Moment matrix**, records that for real moment sequences the quadratic form on polynomial squares is represented by the Hankel matrices and that positivity of those matrices is the classical moment-problem criterion: <https://encyclopediaofmath.org/wiki/Moment_matrix>. Its **Hankel matrix** entry also describes the connection from positive moment Hankel matrices to orthogonal polynomials and their three-term recurrences: <https://encyclopediaofmath.org/wiki/Hankel_matrix>.

The NIST *Digital Library of Mathematical Functions*, §18.2, gives the standard positive-measure orthogonality framework, the Jacobi-matrix form of the three-term recurrence, and the reconstruction of recurrence coefficients from Hankel determinants; see especially §§18.2(i), 18.2(iv), and 18.2(ix): <https://dlmf.nist.gov/18.2>. The general Jacobi-matrix/spectral-measure correspondence is standard OPRL spectral theory; a representative modern reference is Rowan Killip and Barry Simon, **Sum rules for Jacobi matrices and their applications to spectral theory**, *Annals of Mathematics* 158 (2003), 253--321, DOI `10.4007/annals.2003.158.253`.

Directed checks against moment problems, Hankel positivity, orthogonal-polynomial/Jacobi spectralization, and Jacobi spectral measures found no basis for treating this operator wrapper as a new arithmetic mechanism. The line-specific exact content is instead the combination of two already established Prime-Circle facts: PC-399 supplies the moment measure `\mu_n`, while PC-179 supplies its exact prime-power sign theorem. Their combination gives the finite Hankel witness in Section 2 and the universal spectral interval in Section 3.

No novelty is claimed for moment-matrix positivity, Favard/Jacobi theory, multiplication-operator spectralization, Hilbert matrices, or shifted Legendre polynomials.

## 7. Consequence and surviving boundary

The canonical route

\[
\text{shell-2 Chen moments}
\longrightarrow
\text{Hankel positivity}
\longrightarrow
\text{self-adjoint Jacobi operator}
\tag{19}
\]

therefore does not supply an independent bridge to the critical line. Its positivity content is the already-known prime-power radial-flux selector, and its operator spectrum is the fixed interval `[0,\log2]`. The recurrence coefficients can encode the complete shell measure, but that is precisely the generic information-complete behavior diagnosed in PC-399.

What remains open is narrower: a **source-forced relation among recurrence coefficients across shells or refinement levels**, a specific finite compression with arithmetic meaning not inherited from generic moment theory, a nonlinear/cross-shell operation, or an indefinite construction whose relevant invariant is not reducible to the signed measure itself. Such a mechanism would need an independent derivation from Prime-Circle geometry and a novelty audit against classical OPRL/moment theory; merely naming the Jacobi matrix or its coefficients is not enough.

## Audit / falsification tests

This finding fails if any of the following occurs:

1. the identity `m_k(n)=\int t^k d\mu_n` from PC-399 does not hold;
2. PC-179's exact criterion `\rho_n(x)>0` for all `x>0` iff `n` is a prime power is false;
3. a non-prime-power shell has all `m_k(n)=0`, contrary to compact moment determinacy and `\mu_n\ne0`;
4. a PSD matrix can have zero diagonal entry and a nonzero entry in the corresponding row;
5. for a prime power, the pushed-forward density in (7) fails to be positive on `(0,L)`;
6. multiplication by `t` on a positive measure with support `[0,L]` has spectrum different from `[0,L]`.

Items 1--6 are exact or standard functional analysis. The finding makes no claim of a uniform bound on the first non-PSD Hankel size for composite non-prime-powers, no claim that Jacobi recurrence coefficients are arithmetically featureless, and no no-go claim for genuinely cross-level or non-positive source-forced operators.