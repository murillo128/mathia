# PC-163 — full one-hole Kron determinant has a prime-blind Bloch zero-mode logarithm

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `NEAR-MISS` + `DECISIVE-NEGATIVE` for using the **full** one-hole harmonic response left open by PC-162 as a new-prime spectral determinant. PC-162 classified the added Schur/Kron correction by itself and explicitly left open how that correction interacts with the prime-shell background. For the most canonical scalar joint observable, the pseudodeterminant of the complete Kron-reduced Laplacian, that interaction is still exactly controlled. It factors through the already-classified fixed-base Bloch pencil, and its only universal logarithmic finite-size term is `+log m`, produced by the simple translational zero mode at the two Bloch endpoints. The same formula holds for every coprime composite fiber size, so the logarithm is not a new-prime discriminator.

Fix `d>=2`, put

\[
r:=\varphi(d),
\qquad (m,d)=1,
\qquad m\ge2,
\]

and use the one-hole semi-primitive geometry of PC-158/PC-161/PC-162,

\[
S_{d,m}=\{x\bmod dm:(x,d)=1\},
\qquad
O_{d,m}=\{x\in S_{d,m}:m\mid x\},
\qquad
X_{d,m}=S_{d,m}\setminus O_{d,m}.
\tag{1}
\]

Thus `|S_{d,m}|=rm`, `|O_{d,m}|=r`, and `|X_{d,m}|=r(m-1)`. When `m=q` is prime and `q\nmid d`, the survivor is exactly the genuine primitive shell `U(dq)`.

Let

\[
M_{d,m}:=(dm)^{-2}L_{dm}[S_{d,m}]
\tag{2}
\]

be the normalized inverse-square chord Laplacian. With the vertices ordered as `X_{d,m}\sqcup O_{d,m}`, write

\[
M_{d,m}=
\begin{pmatrix}
A_{d,m}^{\rm hole}+\Delta_{d,m}&-B_{d,m}\\
-B_{d,m}^*&G_{d,m}
\end{pmatrix},
\tag{3}
\]

as in PC-162. The full zero-energy Kron response on the survivor is

\[
\boxed{
R_{d,m}
:=\operatorname{Kron}_{X_{d,m}}M_{d,m}
=A_{d,m}^{\rm hole}+\Delta_{d,m}
-B_{d,m}G_{d,m}^{-1}B_{d,m}^*.
}
\tag{4}
\]

PC-162 studied the added correction

\[
C_{d,m}:=\Delta_{d,m}-B_{d,m}G_{d,m}^{-1}B_{d,m}^*.
\]

The present finding studies the joint scalar response `det' R_{d,m}`, so the prime-shell background is retained rather than discarded.

## 1. Matrix-tree plus Schur complementation gives an exact determinant identity

For a connected weighted Laplacian `L` on `N` vertices, write `tau(L)` for its weighted spanning-tree enumerator. Kirchhoff's matrix-tree theorem gives

\[
\det' L=N\,\tau(L).
\tag{5}
\]

Delete any one survivor row and column from (3). Since `G_{d,m}` is positive definite, the ordinary block determinant formula gives

\[
\tau(M_{d,m})
=\det G_{d,m}\;\tau(R_{d,m}).
\tag{6}
\]

Indeed the Schur complement of `G_{d,m}` in that reduced matrix is exactly the same survivor cofactor of `R_{d,m}`. Combining (5) and (6), and using the vertex counts above, yields the exact identity

\[
\boxed{
\det'R_{d,m}
=\frac{m-1}{m}
\frac{\det'M_{d,m}}{\det G_{d,m}}.
}
\tag{7}
\]

Thus the full nonlocal Kron pseudodeterminant is not an independent spectral object. It is the ambient semi-primitive tree determinant divided by a fixed-size old-section Dirichlet determinant.

This identity is already enough to localize the possible source of any new arithmetic: either it must occur in the complete-fiber ambient determinant or in the `r\times r` old block. Both pieces can be classified.

## 2. The ambient determinant is a product of one fixed Bloch polynomial

PC-156 gives the exact complete-fiber Bloch decomposition, and PC-159/PC-160 extend the same pencil to arbitrary coarse root subsets. For the coarse primitive set `U(d)`, define

\[
\mathcal P_d(t)
=\frac1{d^2}
\left(
L_d^{\rm int}+\frac t2 C_d-\frac{t^2}{2}I
\right),
\qquad
D_d(t):=\det\mathcal P_d(t).
\tag{8}
\]

Then

\[
M_{d,m}
\simeq
\bigoplus_{k=0}^{m-1}
\mathcal P_d(k/m).
\tag{9}
\]

The `k=0` block has exactly one zero mode and all `k=1,...,m-1` blocks are positive definite. Hence

\[
\boxed{
\det'M_{d,m}
=\det'\mathcal P_d(0)
\prod_{k=1}^{m-1}D_d(k/m).
}
\tag{10}
\]

Equations (7) and (10) reduce the full one-hole Kron determinant to one fixed finite-dimensional Bloch determinant sampled on the ordinary cyclic grid.

## 3. Hyperbolicity forces an exact positive quadratic factorization

PC-159 proves

\[
D_d(t)=D_d(1-t),
\tag{11}
\]

and PC-160 proves that every zero of `D_d` is real and belongs to

\[
(-\infty,0]\cup[1,\infty).
\tag{12}
\]

The endpoint zero at `t=0` is simple. The base inverse-square Laplacian is connected, so its zero mode is the constant vector. On that vector the cotangent part has zero quadratic average by pair antisymmetry while `J_d` contributes positively; explicitly, for `\mathbf1\in\mathbb C^r`,

\[
\frac{\langle\mathbf1,C_d\mathbf1\rangle}
{\|\mathbf1\|^2}=r.
\tag{13}
\]

Therefore the zero eigenvalue of `\mathcal P_d(0)` leaves zero with positive first derivative `r/(2d^2)`. By (11), `t=1` is also a simple zero.

Since `D_d` is a degree-`2r` polynomial invariant under `t\mapsto1-t`, it is a degree-`r` polynomial in

\[
u=t(1-t).
\]

The leading coefficient follows from the `-t^2I/(2d^2)` term in (8). Consequently there exist fixed numbers

\[
\rho_{d,1},\ldots,\rho_{d,r-1}>0
\]

depending only on the base `d` such that

\[
\boxed{
D_d(t)
=\frac1{(2d^2)^r}
\,u\prod_{j=1}^{r-1}(u+\rho_{d,j}).
}
\tag{14}
\]

No Riemann-like complex zero set is hidden in this scalar Bloch determinant: all nontrivial factors are positive on `0<t<1`, and their paired polynomial zeros are real and outside the Bloch interval.

## 4. The complete finite-size determinant is an explicit Gamma product

Write

\[
\rho_{d,j}=A_{d,j}(1+A_{d,j}),
\qquad A_{d,j}>0,
\tag{15}
\]

and set `A_{d,0}=0`. For `t=k/m`,

\[
t(1-t)+\rho_{d,j}
=\left(\frac{k}{m}+A_{d,j}\right)
\left(1+A_{d,j}-\frac{k}{m}\right).
\tag{16}
\]

Taking the product over the complete Bloch grid and using the elementary Gamma product gives

\[
\boxed{
\prod_{k=1}^{m-1}D_d(k/m)
=
(2d^2)^{-r(m-1)}
 m^{-2r(m-1)}
\prod_{j=0}^{r-1}
\left[
\frac{\Gamma(m(1+A_{d,j}))}
{\Gamma(1+mA_{d,j})}
\right]^2.
}
\tag{17}
\]

Combining (7), (10), and (17) yields the exact full one-hole Kron formula

\[
\boxed{
\begin{aligned}
\det'R_{d,m}
={}&\frac{m-1}{m}
\frac{\det'\mathcal P_d(0)}{\det G_{d,m}}
(2d^2)^{-r(m-1)}m^{-2r(m-1)}\\
&\times
\prod_{j=0}^{r-1}
\left[
\frac{\Gamma(m(1+A_{d,j}))}
{\Gamma(1+mA_{d,j})}
\right]^2.
\end{aligned}
}
\tag{18}
\]

The Gamma functions in (18) are not an imported analytic continuation. They are merely the closed form of a finite product over the cyclic Bloch grid. Their slopes `A_{d,j}` are the fixed real roots of the base Bloch polynomial; they do not encode zeta zeros or a new prime-specific archimedean factor.

## 5. The old block contributes no hidden logarithmic or prime-specific scale

PC-162 proves that `G_{d,m}` converges to a positive diagonal matrix. The convergence can be sharpened directly. Index the old point by `b\in U(d)`, so its circle coordinate is `mb`. With

\[
s_a
=\frac{\deg_d(a)}{d^2}+\frac1{12d^2}
\tag{19}
\]

as in PC-162, the cosecant-square distribution identity gives exactly

\[
G_{d,m}(b,b)
=s_{mb}-\frac1{12d^2m^2},
\tag{20}
\]

while for `b\ne c`,

\[
G_{d,m}(b,c)
=-\frac1{4d^2m^2
\sin^2(\pi(b-c)/d)}.
\tag{21}
\]

Multiplication by `m` permutes `U(d)`, so

\[
\boxed{
\det G_{d,m}
=\prod_{a\in U(d)}s_a+O_d(m^{-2}),
}
\tag{22}
\]

with a strictly positive limiting constant. The old block therefore cannot cancel or create a `log m` term. Its residual dependence on `m mod d` is a fixed-size `O_d(m^{-2})` correction.

## 6. A universal `+log m` appears, but it is only the Bloch zero-mode anomaly

Define the fixed-base logarithmic Bloch integral

\[
\mathfrak m_d
:=\int_0^1\log D_d(t)\,dt.
\tag{23}
\]

The integral is finite because the endpoint zeros are simple. Applying Stirling's formula to (17) gives

\[
\boxed{
\log\det'R_{d,m}
=m\mathfrak m_d+\log m+C_d+o(1)
\qquad(m\to\infty,(m,d)=1),
}
\tag{24}
\]

for a constant `C_d` depending only on the base geometry.

The coefficient of `log m` is exactly one for every base `d`. Its source is transparent from (14). The factor `u=t(1-t)` gives

\[
\prod_{k=1}^{m-1}\frac{k}{m}\left(1-\frac{k}{m}\right)
=\frac{\Gamma(m)^2}{m^{2(m-1)}},
\tag{25}
\]

and therefore

\[
2\log\Gamma(m)-2(m-1)\log m
=-2m+\log m+\log(2\pi)+o(1).
\tag{26}
\]

Every factor `u+\rho_{d,j}` with `\rho_{d,j}>0` has no endpoint zero and contributes only an extensive `m` term plus an `O_d(1)` constant. Thus the entire `+log m` in (24) comes from the single translational zero mode paired at Bloch times `0` and `1`.

This is a sharp near-miss against the von Mangoldt scale. For a genuinely new prime `q`, the survivor is `U(dq)` and (24) contains `+log q`. But **exactly the same coefficient occurs for every coprime composite `m` in the matched one-hole control**. Nothing in the derivation knows that `m` is prime. The logarithm is the finite-size correction of a cyclic zero mode, not the arithmetic support condition `\Lambda(m)`.

There is a second normalization warning. If the whole energy is rescaled by a positive factor `c_m`, then

\[
\det'(c_mR_{d,m})
=c_m^{r(m-1)-1}\det'R_{d,m}.
\tag{27}
\]

Hence a size-dependent change of energy units changes the determinant asymptotics extensively. The clean coefficient in (24) belongs to the already-chosen `(dm)^{-2}` Prime-Circle normalization; positivity alone does not select it.

## 7. Minimal exact audit: `d=2`

For `d=2`, `r=1` and the Bloch pencil is scalar,

\[
D_2(t)=\frac{t(1-t)}8.
\tag{28}
\]

The old block is also scalar,

\[
G_{2,m}=\frac{m^2-1}{48m^2}.
\tag{29}
\]

Equation (18) becomes

\[
\boxed{
\det'R_{2,m}
=\frac{48m}{m+1}
\frac{\Gamma(m)^2}
{8^{m-1}m^{2m-2}}.
}
\tag{30}
\]

This formula agrees directly with finite Schur complementation of the normalized regular `m`-gon for odd `m`. Its asymptotic is

\[
\log\det'R_{2,m}
=-(2+\log8)m+\log m+O(1),
\tag{31}
\]

already exhibiting the same universal logarithm with no primality input.

## 8. Prior-art and novelty audit

The general mechanisms are classical. Dörfler--Bullo, already anchored in `SOURCES.md`, treat Kron reduction as graph-Laplacian Schur complementation. Kirchhoff's matrix-tree theorem and the Schur-complement determinant identity give (5)--(7). Finite cyclic Fourier/Bloch determinant products and their relation to spanning-tree growth are likewise classical in the theory of cyclic graph covers; nearby examples include Y. S. Kwon, A. D. Mednykh and I. A. Mednykh, *On complexity of cyclic coverings of graphs* (arXiv:1811.03801), and Riccardo Pengo and Daniel Vallières, *Spanning Trees in Z-Covers of a finite Graph and Mahler Measures*, J. Aust. Math. Soc. 118 (2025), 108--144, DOI `10.1017/S1446788724000144`. Those works organize cyclic-cover tree growth through Laplacian/voltage polynomials and Mahler-measure-type quantities.

The present weighted family is not literally a fixed-edge-weight graph cover because the chord weights change with `m`; the exact PC-156 Bloch identity is what makes (10) available here. The Gamma reduction (17) then uses the extra Prime-Circle fact, established by PC-159/PC-160, that the fixed determinant is a reflection-symmetric hyperbolic polynomial in `t(1-t)`. Directed searches across Kron/tree determinant identities, cyclic-cover spanning-tree asymptotics, Bloch determinant products, Mahler measures, and Gamma products did not locate this exact Prime-Circle formula. That absence is not evidence of historical priority, and no new general theorem about graph covers, matrix-tree identities, Gamma products, or Mahler measure is claimed.

The durable contribution is the line-specific classification: even after keeping the prime-shell background and the nonlocal Kron correction **jointly**, the canonical one-hole pseudodeterminant is a fixed-base Bloch product. Its apparently arithmetic `+log m` term is universal cyclic zero-mode structure and survives unchanged on matched composite controls.

## 9. Boundary and falsification surface

This finding closes the scalar **full one-hole Kron pseudodeterminant** route at fixed base `d`. It does not classify the complete spectrum of `R_{d,m}`, energy-dependent Feshbach/scattering determinants, simultaneous growth of `d` and `m`, true multi-hole primitive refinement for composite added conductors, growing-support nonlinear cross-level observables, or the global uniformization/monodromy branch.

The result is exactly falsifiable. A violation of (7) would contradict Kirchhoff plus the Schur determinant formula. A Bloch sample violating (10) would contradict PC-156. A zero of `D_d` not represented by (14) would contradict the PC-159 reflection together with the PC-160 hyperbolicity and endpoint simplicity. A finite `m` violating (17) would contradict the elementary Gamma product. Finally, a coprime sequence for which `det G_{d,m}` fails (22) would contradict the exact cosecant-square fiber sums (20)--(21). Under the stated fixed-base hypotheses, the canonical joint one-hole tree determinant therefore supplies no new prime-specific RH mechanism.