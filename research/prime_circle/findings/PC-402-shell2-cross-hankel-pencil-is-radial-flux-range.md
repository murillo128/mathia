# PC-402 — shell-2 cross-Hankel pencil is only the radial-flux range

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical source-forced generalized eigenvalue pencil obtained by pairing one shell's Chen/Hankel moment form with the intrinsic positive shell-2 reference form. This does not classify cross-shell pencils whose second form contains independent off-diagonal or cross-level Prime-Circle information.

PC-401 leaves open a natural loophole after the single-measure Jacobi/Krein spectralizations: instead of representing one signed shell measure alone, use **two source-forced forms** and ask for their generalized spectrum. The shell-2 Chen coordinate supplies a canonical positive reference without importing an external operator, so this is the first pencil to test.

The pencil can be classified exactly. Relative to shell 2, the target form is simply multiplication by the already-known radial-flux density. Its infinite generalized spectrum is the ordinary range of that scalar density, hence a single real interval. Finite Hankel pencils are Galerkin/Ritz compressions whose extremal generalized eigenvalues converge to the endpoints of the same interval. The prime-power/non-prime-power distinction is exactly the old sign theorem for the radial flux, not a new spectral localization mechanism.

## 1. Two intrinsic moment forms

Let

\[
X_n(z)=\log\Phi_n(z),\qquad t=X_2(z)=\log(1+z),\qquad L=\log2.
\]

By PC-399/PC-400, the shell-2 Chen moments are

\[
m_k(n)=k!J_{2^k,n}=\int_0^L t^k\,d\mu_n(t),
\]

with

\[
d\mu_n(t)=w_n(t)\,dt,
\qquad
\boxed{w_n(t)=e^tX_n'(e^t-1).}
\tag{1}
\]

For the reference shell itself, `X_2(z)=log(1+z)=t`, so

\[
d\mu_2(t)=dt.
\tag{2}
\]

Thus Prime Circle supplies, without choosing an auxiliary measure, the pair of bilinear forms on real polynomials

\[
B_n(p,q)=\int_0^L p(t)q(t)w_n(t)\,dt,
\qquad
B_2(p,q)=\int_0^L p(t)q(t)\,dt.
\tag{3}
\]

The finite moment matrices in the monomial basis are

\[
H_N(n)=\left(m_{i+j}(n)\right)_{0\le i,j\le N},
\qquad
H_N(2)=\left(\frac{L^{i+j+1}}{i+j+1}\right)_{0\le i,j\le N}.
\tag{4}
\]

`H_N(2)` is positive definite for every `N`, so the generalized eigenvalue problem

\[
H_N(n)v=\lambda H_N(2)v
\tag{5}
\]

is canonical and real even when `mu_n` is signed.

## 2. The infinite relative operator is multiplication by the old flux density

Complete the polynomial space in the `B_2` norm. This gives

\[
\mathcal H=L^2([0,L],dt).
\]

Since `Phi_n` has no zero on `[0,1]`, the function `w_n` in (1) is real analytic on a neighborhood of `[0,L]`, hence bounded. The Riesz representative of `B_n` relative to `B_2` is therefore exactly

\[
\boxed{A_n=M_{w_n},\qquad (A_nf)(t)=w_n(t)f(t).}
\tag{6}
\]

Indeed,

\[
B_n(f,g)=\langle M_{w_n}f,g\rangle_{L^2(dt)}.
\tag{7}
\]

Because Lebesgue measure has full support and `w_n` is continuous,

\[
\boxed{
\sigma(A_n)
=\operatorname{essran}(w_n)
=w_n([0,L])
=[a_n,b_n],
}
\tag{8}
\]

where

\[
a_n=\min_{0\le t\le L}w_n(t),
\qquad
b_n=\max_{0\le t\le L}w_n(t).
\tag{9}
\]

Thus the entire generalized spectral set of this two-form construction contains only the two extrema of one scalar shell profile. The passage from one form to a pencil has not created a new nonlocal carrier.

## 3. The sign of the generalized spectrum is exactly PC-179's prime-power selector

The density (1) is a positive reparametrization of the radial flux from PC-179. Put

\[
z=e^t-1\in(0,1],\qquad x=-\log z.
\]

PC-179 defines

\[
\rho_n(x)=zX_n'(z).
\]

Hence for `0<t\le L`,

\[
\boxed{
w_n(t)=\frac{1+z}{z}\rho_n(-\log z).
}
\tag{10}
\]

The prefactor is positive. Therefore PC-179's exact criterion

\[
\rho_n(x)>0\ \text{for all }x>0
\iff n\text{ is a prime power}
\]

translates directly to the relative form.

If `n=p^a`, then `w_n(t)>0` on `(0,L]` and `w_n(t)\ge0` on the closed interval. Consequently

\[
\boxed{\sigma(A_{p^a})\subset[0,\infty).}
\tag{11}
\]

For `a>1`, `X_{p^a}'(0)=0`, so `0` is actually the lower endpoint; for prime `p`, `X_p'(0)=1` and the compact continuous density is strictly positive on all of `[0,L]`.

If `n` is not a prime power, then the common-anchor identity gives

\[
\int_0^L w_n(t)\,dt
=\mu_n([0,L])
=\Lambda(n)=0.
\tag{12}
\]

The density is continuous and not identically zero. Therefore it takes both signs, so

\[
\boxed{a_n<0<b_n.}
\tag{13}
\]

The generalized-spectrum sign test is thus precisely the radial-flux sign/coercivity theorem already present before the pencil was formed. It is not a stronger arithmetic selector.

## 4. Finite cross-Hankel pencils are Ritz approximations to the same multiplication operator

For a polynomial `p` of degree at most `N`, the generalized Rayleigh quotient of (5) is

\[
\mathcal R_n[p]
=
\frac{B_n(p,p)}{B_2(p,p)}
=
\frac{\int_0^L |p(t)|^2w_n(t)\,dt}
       {\int_0^L |p(t)|^2\,dt}.
\tag{14}
\]

It is an average of `w_n`, hence every finite generalized eigenvalue lies in

\[
[a_n,b_n].
\tag{15}
\]

Let `lambda_N^-` and `lambda_N^+` be the smallest and largest generalized eigenvalues. By the min-max characterization,

\[
\lambda_N^-
=\min_{0\ne p\in\mathcal P_N}\mathcal R_n[p],
\qquad
\lambda_N^+
=\max_{0\ne p\in\mathcal P_N}\mathcal R_n[p].
\tag{16}
\]

The polynomial spaces are nested, so `lambda_N^-` is nonincreasing and `lambda_N^+` is nondecreasing. Polynomials are dense in `L^2([0,L])`. Approximating an `L^2` bump supported where `w_n` is arbitrarily close to its minimum or maximum gives

\[
\boxed{
\lambda_N^-\downarrow a_n,
\qquad
\lambda_N^+\uparrow b_n.
}
\tag{17}
\]

Indeed, if `p_j -> f` in `L^2`, then `|p_j|^2 -> |f|^2` in `L^1`; boundedness of `w_n` passes the Rayleigh quotient to the limit. Thus increasing the Hankel depth does not reveal a hidden discrete arithmetic spectrum. It converges to the extremal values of the same multiplication symbol.

This is exactly the kind of generalized-eigenvalue moment hierarchy studied classically in moment/nonnegativity methods. Jean B. Lasserre, **A New Look at Nonnegativity on Closed Sets and Polynomial Optimization**, *SIAM Journal on Optimization* 21:3 (2011), 864–885, DOI `10.1137/100806990`, characterizes nonnegativity of a continuous `f` on compact support through moment matrices of `f dmu` and obtains convergent generalized-eigenvalue hierarchies for extrema. Carmen Escribano, Raquel Gonzalo and Emilio Torrano, **Smallest and largest generalized eigenvalues of large moment matrices and some applications**, arXiv:`2203.15453` (2022), explicitly study pairs of Borel-measure moment matrices through smallest/largest generalized eigenvalues and Rayleigh quotients. No novelty is claimed for this moment-pencil mechanism.

## 5. Matched controls erase the arithmetic interpretation of the spectral interval

The collapse is not specific to cyclotomic data. Let `v` be any real continuous, or real-analytic, non-arithmetic function on `[0,L]`. The pair

\[
\widetilde B_v(p,q)=\int_0^L p(t)q(t)v(t)\,dt,
\qquad
B_2(p,q)=\int_0^L p(t)q(t)\,dt
\tag{18}
\]

has relative operator `M_v` and generalized spectrum

\[
\sigma(M_v)=[\min v,\max v].
\tag{19}
\]

There are infinitely many such `v` with the same minimum and maximum as a given `w_n` but otherwise unrelated profiles. They produce the same generalized spectral set and the same endpoint limits (17). Therefore the spectrum of the canonical cross-Hankel pencil is much less informative than the signed cyclic measure retained in PC-401: it forgets almost the entire shell profile and remembers only its range.

The arithmetic specialization of (13) survives only because Prime Circle independently proves the sign/zero-mass theorem for `w_n`. The generalized eigenvalue wrapper does not add that arithmetic fact.

## 6. Prior-art and novelty audit

The abstract mechanism is classical multiplication-operator and moment-matrix theory. Lasserre's 2011 theorem is especially close: with a compactly supported reference measure `mu`, positivity of a continuous function `f` is detected by moment matrices of the signed measure `f dmu`, and the extremal-value hierarchy is formulated as generalized eigenvalue problems. The present pair is exactly that setup with `mu=dt` on `[0,log2]` and `f=w_n`.

Escribano--Gonzalo--Torrano provide neighboring matrix-theoretic prior art for comparing two measures through generalized moment eigenvalues and associated Rayleigh quotients. Standard spectral theory supplies the infinite-dimensional statement that multiplication by a continuous real function has spectrum equal to its range on a full-support compact measure space.

The Prime-Circle-specific derivation is exact but not a novel spectral mechanism: shell 2 makes the positive reference measure intrinsic, and equations (6)--(13) identify the resulting relative operator with the already-known cyclotomic radial-flux density. This closes a genuine line-local loophole left open by PC-401 while classicalizing the proposed escape.

## 7. Consequence and surviving boundary

The canonical route

\[
\text{shell-2 reference moments + target shell moments}
\longrightarrow
(H_N(n),H_N(2))
\longrightarrow
\text{generalized spectrum}
\]

therefore does **not** produce a new RH-relevant spectral localization. In the infinite limit it is just `M_{w_n}`; at finite depth it is a Ritz approximation to that multiplication operator; and its positivity transition is exactly PC-179's radial-flux prime-power criterion.

This result does not rule out every two-form construction. A surviving pencil must use genuinely additional Prime-Circle information not reducible to a density relative to one recovered shell measure: for example a source-forced off-diagonal cross-shell kernel, cross-level/refinement coupling before moment reduction, a second form not absolutely continuous with respect to the same scalar reference in a way that collapses to multiplication, or a nonlinear interaction. Merely pairing the target shell's Hankel moments with the canonical shell-2 Hilbert/Hankel matrix is exhausted.

## Audit / falsification tests

The claim fails if any of the following occurs:

1. the shell-2 measure is not Lebesgue measure `dt` in the coordinate `t=log(1+z)`;
2. the target measure does not have density (1);
3. the relative Riesz operator of (3) is not multiplication by `w_n`;
4. a continuous real multiplication operator on `L^2([0,L],dt)` has spectrum different from its range;
5. equation (10) fails, so the sign of `w_n` differs from the PC-179 radial flux;
6. a non-prime-power shell can have nonzero continuous `w_n` of zero integral without changing sign;
7. the generalized Rayleigh quotients (14) do not converge at their extrema to `min w_n` and `max w_n` under polynomial density.

Items 1--7 are exact consequences of PC-179/PC-399/PC-400, elementary measure/spectral theory, and the density of polynomials on a compact interval. The finding makes no claim about generalized pencils built from genuinely independent cross-shell or cross-level kernels.