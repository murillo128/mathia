# WP-139 — Minimal new-prime puncture singular finite part is bounded and prime-blind

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIME-CIRCLE + SINGULAR-PSEUDODETERMINANT + MATCHED-COMPOSITE-CONTROL + PRIOR-ART-CLASSICALIZATION` for the zero-shift finite part of the `PC-158` one-hole positive spectral shift at the minimal coarse modulus `d=2`.

`WP-138` proves that every fixed regular monotone spectral response of the positive new-prime puncture defect is uniformly too small to supply the missing `log q` factor, but deliberately leaves one singular escape open. For the shifted logarithm

\[
Q_\lambda(d,m)
=
\log(I+M_{d,m}/\lambda)
-
\log(I+\widehat A_{d,m}/\lambda)
\succeq0,
\]

its trace has the zero-shift asymptotic

\[
\operatorname{Tr}Q_\lambda(d,m)
=
\varphi(d)\log\frac1\lambda
+
\log\frac{\det' M_{d,m}}{\det' A_{d,m}^{\rm hole}}
+o(1),
\]

and `WP-138` does not classify the finite pseudodeterminant ratio.

At the minimal base `d=2`, that finite part is exactly computable. For every odd `m>=3`, including every new odd prime and the matched composite one-hole controls of `PC-158`,

\[
\boxed{
\frac{\det' M_{2,m}}
{\det' A_{2,m}^{\rm hole}}
=
\frac{m-1}{16m}.
}
\tag{1}
\]

Hence

\[
\boxed{
\operatorname{Tr}Q_\lambda(2,m)
=
\log\frac1\lambda
+
\log\frac{m-1}{16m}
+o(1)
}
\qquad(\lambda\downarrow0),
\tag{2}
\]

and the renormalized finite part is

\[
\boxed{
F_m
:=
\log\frac{\det' M_{2,m}}
{\det' A_{2,m}^{\rm hole}}
=
-\log16+\log\left(1-\frac1m\right).
}
\tag{3}
\]

It is negative, uniformly bounded, and converges to `-log 16`. It therefore does not hide the missing `+log m` scale behind the universal zero-mode divergence. After the critical half-weight it remains only `O(m^{-1/2})`, not `(log m)/sqrt(m)`.

The formula is also exactly prime-blind: it holds for every odd composite `m` under the same one-hole geometry. Thus the singular finite part left open by `WP-138` does not rescue the minimal new-prime puncture route. Any logarithm obtained instead by making `lambda` depend on `m` comes from the universal extra zero mode and requires an independently forced refinement-dependent regularization; it is not contained in the canonical fixed-cutoff finite part classified here.

## 1. At `d=2`, the PC-158 ambient fiber is a regular `m`-gon

Since `phi(2)=1`, the semi-primitive ambient set `S_{2,m}` is one complete cyclic `m`-fiber. After a cyclic relabeling, the unnormalized inverse-square chord Laplacian is the weighted complete-graph Laplacian

\[
(L_m f)_i
=
\sum_{j\ne i}
\frac{f_i-f_j}{4\sin^2\!\bigl(\pi(i-j)/m\bigr)},
\qquad
0\le i,j<m.
\tag{4}
\]

Deleting the single old point `0` gives the one-hole induced Laplacian `B_m` on `1,...,m-1`. The normalized operators in the `PC-158` convention are

\[
M_{2,m}=\frac1{(2m)^2}L_m,
\qquad
A_{2,m}^{\rm hole}=\frac1{(2m)^2}B_m.
\tag{5}
\]

For a new prime `m=q`, the survivor is exactly `U(2q)`. For odd composite `m`, it is the matched one-hole control rather than the full primitive shell.

The circulant Fourier modes diagonalize `L_m`. The classical finite cosecant identity

\[
\sum_{s=1}^{m-1}
\frac{1-\cos(2\pi ks/m)}{4\sin^2(\pi s/m)}
=
\frac{k(m-k)}2
\]

gives

\[
\operatorname{Spec}(L_m)
=
\left\{
\frac{k(m-k)}2:0\le k<m
\right\}.
\tag{6}
\]

Therefore

\[
\boxed{
\det' L_m
=
\prod_{k=1}^{m-1}\frac{k(m-k)}2
=
\frac{((m-1)!)^2}{2^{m-1}}.
}
\tag{7}
\]

The nontrivial step is the one-hole pseudodeterminant `det' B_m`.

## 2. A cotangent-node generalized eigenproblem triangularizes exactly

Let the conductance from surviving vertex `j` to the deleted vertex be

\[
d_j
=
\frac1{4\sin^2(\pi j/m)},
\qquad
D_m=\operatorname{diag}(d_1,\ldots,d_{m-1}),
\tag{8}
\]

and form the positive semidefinite congruence

\[
H_m=D_m^{-1/2}B_mD_m^{-1/2}.
\tag{9}
\]

It is similar to `T_m=D_m^{-1}B_m`, so the two have the same eigenvalues. Put

\[
x_j=\cot\frac{\pi j}{m}.
\tag{10}
\]

The cotangent subtraction identity gives, for `i!=j`,

\[
\frac{w_{ij}}{d_i}
=
\frac{\sin^2(\pi i/m)}
{\sin^2(\pi(i-j)/m)}
=
\frac{1+x_j^2}{(x_i-x_j)^2}.
\tag{11}
\]

Consequently, if a vector is obtained by evaluating a polynomial `f` at the nodes `x_j`, then

\[
(T_mf)(x_i)
=
\sum_{j\ne i}
\frac{1+x_j^2}{(x_i-x_j)^2}
\bigl(f(x_i)-f(x_j)\bigr).
\tag{12}
\]

The `m-1` nodes are the roots of

\[
P_m(x)
=
\frac{(x+i)^m-(x-i)^m}{2i},
\tag{13}
\]

which obeys the exact differential equation

\[
(1+x^2)P_m''(x)
-2(m-1)xP_m'(x)
+m(m-1)P_m(x)
=0.
\tag{14}
\]

At a root `y=x_i`, the logarithmic-derivative identity and (14) yield

\[
\sum_{j\ne i}\frac1{y-x_j}
=
\frac{P_m''(y)}{2P_m'(y)}
=
\frac{(m-1)y}{1+y^2}.
\tag{15}
\]

Now let `f` have degree `ell<=m-2`, and for fixed `y` define

\[
q_y(x)=\frac{f(x)-f(y)}{x-y},
\qquad
h_y(x)=(1+x^2)q_y(x),
\qquad
r_y(x)=\frac{h_y(x)-h_y(y)}{x-y}.
\tag{16}
\]

Using

\[
\frac{h_y(x_j)}{y-x_j}
=
\frac{h_y(y)}{y-x_j}-r_y(x_j),
\]

and (15), equation (12) becomes

\[
\boxed{
(T_mf)(y)
=
(m-1)y f'(y)
-
\sum_{j=1}^{m-1}r_y(x_j)
+
h_y'(y).
}
\tag{17}
\]

This expression is a polynomial in `y` of degree at most `ell`. For the monic test polynomial `f(x)=x^ell`, its degree-`ell` coefficients are explicit. The first term contributes `(m-1)ell`; the root sum contributes the same `(m-1)ell` with the opposite sign; and

\[
h_y'(y)
=
2y f'(y)
+
\frac{1+y^2}{2}f''(y)
\]

has leading coefficient

\[
2\ell+\frac{\ell(\ell-1)}2
=
\frac{\ell(\ell+3)}2.
\tag{18}
\]

Thus `T_m` preserves the polynomial-degree filtration and is triangular in the monomial basis with diagonal

\[
\boxed{
\eta_\ell
=
\frac{\ell(\ell+3)}2,
\qquad
0\le\ell\le m-2.
}
\tag{19}
\]

Evaluation of polynomials of degree at most `m-2` at the `m-1` distinct nodes is an isomorphism, so (19) is the complete spectrum of both `T_m` and `H_m`. In particular,

\[
\boxed{
\det' H_m
=
\prod_{\ell=1}^{m-2}\frac{\ell(\ell+3)}2
=
\frac{(m-2)!(m+1)!}{6\,2^{m-2}}.
}
\tag{20}
\]

This generalized spectrum is the exact finite certificate needed for the hole determinant; no asymptotic spectral approximation enters.

## 3. Matrix-tree conversion gives the exact one-hole pseudodeterminant

The graph underlying `B_m` is connected. If `tau(B_m)` is its weighted spanning-tree sum, the matrix-tree theorem gives

\[
\operatorname{adj}(B_m)
=
\tau(B_m)\mathbf1\mathbf1^*,
\qquad
\det' B_m=(m-1)\tau(B_m).
\tag{21}
\]

Let

\[
v=D_m^{1/2}\mathbf1.
\]

Since `H_m=D_m^{-1/2}B_mD_m^{-1/2}`, transforming the adjugate gives

\[
\operatorname{adj}(H_m)
=
\det(D_m)^{-1}\tau(B_m)vv^*.
\tag{22}
\]

On the other hand, `H_m` has one-dimensional kernel spanned by `v`, so its spectral adjugate is

\[
\operatorname{adj}(H_m)
=
\frac{\det'H_m}{v^*v}vv^*.
\tag{23}
\]

Comparing (22)--(23),

\[
\boxed{
\tau(B_m)
=
\frac{\det D_m\,\det'H_m}
{\sum_{j=1}^{m-1}d_j}.
}
\tag{24}
\]

The standard sine product and cosecant-square sum are

\[
\prod_{j=1}^{m-1}\sin\frac{\pi j}{m}
=
\frac{m}{2^{m-1}},
\qquad
\sum_{j=1}^{m-1}\csc^2\frac{\pi j}{m}
=
\frac{m^2-1}{3}.
\tag{25}
\]

Hence

\[
\det D_m=\frac1{m^2},
\qquad
\sum_{j=1}^{m-1}d_j=\frac{m^2-1}{12}.
\tag{26}
\]

Substituting (20) and (26) into (24) yields

\[
\tau(B_m)
=
\frac{2^{3-m}((m-2)!)^2}{m},
\tag{27}
\]

and therefore

\[
\boxed{
\det' B_m
=
\frac{2^{3-m}(m-1)!(m-2)!}{m}.
}
\tag{28}
\]

Combining (7) and (28), the unnormalized pseudodeterminant ratio collapses to

\[
\boxed{
\frac{\det'L_m}{\det'B_m}
=
\frac{m(m-1)}4.
}
\tag{29}
\]

## 4. Normalization cancels the apparent logarithmic growth

The normalization in (5) matters because the ambient and one-hole Laplacians have different numbers of nonzero eigenvalues. `L_m` has `m-1` nonzero eigenvalues, whereas `B_m` has `m-2`. Therefore

\[
\frac{\det'M_{2,m}}{\det'A_{2,m}^{\rm hole}}
=
\frac1{(2m)^2}
\frac{\det'L_m}{\det'B_m}.
\tag{30}
\]

Using (29),

\[
\frac{\det'M_{2,m}}{\det'A_{2,m}^{\rm hole}}
=
\frac1{4m^2}\frac{m(m-1)}4
=
\frac{m-1}{16m},
\]

which proves (1).

This cancellation is the decisive point. Before the intrinsic `N^{-2}` normalization, the pseudodeterminant ratio contains `m(m-1)` and its logarithm grows like `2 log m`. But that growth is exactly the scale dimension contributed by the one extra nonzero ambient mode. The normalized Prime-Circle operator removes it, leaving only the bounded factor `(m-1)/(16m)`.

For the padded one-hole operator `widehat A_{2,m}=A_{2,m}^{hole}\oplus0`, the nullities are

\[
\dim\ker M_{2,m}=1,
\qquad
\dim\ker\widehat A_{2,m}=2.
\tag{31}
\]

Thus

\[
\begin{aligned}
\operatorname{Tr}Q_\lambda(2,m)
&=
\log\frac{\det(\lambda I+M_{2,m})}
{\det(\lambda I+\widehat A_{2,m})}\\
&=
\log\frac1\lambda
+
\log\frac{m-1}{16m}
+o(1),
\end{aligned}
\tag{32}
\]

which is (2). The first term is the universal nullity defect already identified abstractly in `WP-138`; the second is the complete canonical finite part.

At the critical root-cover normalization,

\[
\frac{F_m}{\sqrt m}
=
O(m^{-1/2}),
\tag{33}
\]

whereas the desired first-power finite Weil coefficient at a prime is

\[
\frac{\Lambda(q)}{\sqrt q}
=
\frac{\log q}{\sqrt q}.
\tag{34}
\]

Hence the singular finite part is asymptotically smaller by a factor of order `1/log q`, just like the regular responses ruled out in `WP-138`.

## 5. Matched composite control and scope boundary

No step of (4)--(33) uses primality of `m`. The determinant identity itself holds for the regular `m`-gon family generally; the `PC-158` matched-control interpretation requires `(m,2)=1`, hence odd `m`.

For prime `m=q`, deleting the one old section gives the genuine primitive shell `U(2q)`. For odd composite `m`, exactly the same deletion gives the matched one-hole control. Equation (3) therefore has a smooth composite continuation and cannot itself distinguish a new prime from a composite refinement.

This result closes the most immediate singular escape left by `WP-138` at the minimal conductor:

\[
\boxed{
\text{PC-158 positive one-hole shift}
\to
\text{zero-shift log-det finite part}
\to
\text{critical normalization}
\not\to
\frac{\log q}{\sqrt q}.
}
\tag{35}
\]

It also rules out interpreting the minimal one-hole finite part as a conductor-uniform local mechanism that should work at every coarse base, because any such mechanism would have to survive `d=2`.

Several stronger escapes remain outside the theorem. For `d>2`, cross-fiber geometry can alter the finite pseudodeterminant ratio and is not classified here. A true composite primitive shell is a multi-hole object and may carry arithmetic information absent from the matched one-hole control. An independently forced `m`-dependent singular regulator could turn the universal `log(1/lambda)` term into a logarithmic refinement scale, but then the logarithm comes from the extra zero mode, is present in the composite control as well, and requires a separate geometric theorem fixing the regulator before the arithmetic target is identified. Nonseparable finite--archimedean coupling before scalarization is also untouched.

Most importantly, subtracting the positive shifted response's universal divergence to form `F_m` does **not** inherit the Loewner positivity of `Q_lambda`. The finite part in (3) is in fact negative. Thus even if its scale had matched, a new sign theorem would still have been necessary.

## 6. Prior-art and novelty audit

The ingredients of the proof are classical: Fourier diagonalization of circulant inverse-square chord Laplacians, finite cosecant identities, the cotangent-root/Stieltjes polynomial method, and the weighted matrix-tree theorem. The generalized eigenvalue calculation (19) is an elementary finite-dimensional consequence of those identities.

A targeted audit against inverse-square/cosecant matrices, Calogero--Sutherland finite spectra, cotangent-node interpolation matrices, principal minors, and weighted spanning-tree formulas did not locate the exact normalized `PC-158` one-hole ratio (1). That absence is not evidence of historical priority, and no new general spectral or matrix-tree theorem is claimed.

The durable branch-specific content is the specialization to the exact Mathia object left open by `WP-138`: once the intrinsic Prime-Circle normalization is included, the apparent logarithmic pseudodeterminant growth cancels and the singular finite part becomes bounded and prime-blind.

## 7. Consequence for the Weil-positivity search

`PC-158` supplied a rare Mathia-native object with an independent positive theorem and the correct geometric operation for a new prime: deleting the old section produces a positive spectral shift. `WP-138` showed that every regular fixed spectral readout of that positivity is too small. The present exact calculation shows that, at the minimal base, the canonical singular zero-shift finite part is too small as well.

So neither the regular nor the canonical finite-part logarithmic calculus of the one-hole defect produces the critical local `log q` scale. The only logarithm visible in the raw singular shifted response is the regulator divergence associated with one extra zero mode. Turning that universal divergence into arithmetic scale would require additional intrinsic structure and would still need to survive the composite control, produce the archimedean and polar/global terms, and furnish a sign theorem independent of RH or inserted zero data.

### Internal evidence

- [WP-138](WP-138-new-prime-puncture-regular-positive-spectral-responses-cannot-supply-critical-logarithmic-local-scale.md)
- [WP-073](WP-073-pointed-dirichlet-root-cover-isometry-forces-critical-half-weight.md)
- [PC-158](../../prime_circle/findings/PC-158-new-prime-puncture-is-a-prime-blind-positive-spectral-shift.md)
