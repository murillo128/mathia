# PC-178 — raw resultant prime-axis form is nonclosable and Abel removal scalarizes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the prime-separable unbounded-domain escape left explicitly by PC-177. The exact Prime-Circle resultant symbol restricts on every fixed prime-valuation axis to the constant off-diagonal Toeplitz form. That form is semibounded but nonclosable on the natural finite-support shell domain: after its sharp scalar shift it is exactly the point-mass Toeplitz form classified by Yafaev. Moreover, the canonical Abel/valuation-length regularizations converge coefficientwise to the raw form while their self-adjoint operators converge in strong resolvent sense only to a scalar multiple of the identity. Thus the raw prime-axis interaction cannot be recovered by choosing a Friedrichs/Kato closure or by removing the intrinsic Abel damping one prime at a time. A surviving domain-sensitive mechanism must couple prime directions before closure, or derive additional non-Toeplitz domain/renormalization data from the geometry.

PC-177 showed that the exact common-anchor/resultant ratio symbol

\[
K(m,n)=\Lambda_\times(m/n)
\tag{1}
\]

is not bounded on the normalized `ell^2(N)` scale space, and deliberately left open the possibility that it could instead define an unbounded form with a separately geometry-derived self-adjoint domain. The first such repair to test is the one already forced by PC-177's prime-axis decomposition: close each valuation direction as an unbounded Toeplitz form before assembling the primes. That attempt fails at the form level.

## 1. Every prime axis is the constant off-diagonal Toeplitz form

Fix a prime `p` and the closed coordinate subspace

\[
\mathcal H_p
=
\overline{\operatorname{span}}\{e_{p^j}:j\ge0\}
\cong \ell^2(\mathbb N_0).
\tag{2}
\]

For two distinct points on this axis,

\[
\frac{p^i}{p^j}=p^{i-j},
\]

so the exact PC-177 symbol gives

\[
K(p^i,p^j)=\log p\quad(i\ne j),
\qquad
K(p^j,p^j)=0.
\tag{3}
\]

Hence on the natural finite-support domain `c_00(N_0)` the restricted quadratic form is

\[
\begin{aligned}
q_p[x]
&=(\log p)\sum_{i\ne j}\overline{x_i}x_j\\
&=(\log p)
\left(
\left|\sum_{j\ge0}x_j\right|^2
-\sum_{j\ge0}|x_j|^2
\right).
\end{aligned}
\tag{4}
\]

In particular

\[
q_p[x]\ge-(\log p)\|x\|_2^2,
\tag{5}
\]

so this individual prime-axis obstruction is not caused by lack of a lower bound. The sharp shifted form is

\[
\boxed{
q_p[x]+(\log p)\|x\|_2^2
=(\log p)
\left|\sum_{j\ge0}x_j\right|^2.
}
\tag{6}
\]

The right-hand side is boundary evaluation of the corresponding Hardy polynomial at `z=1`.

There is already a warning at the operator level. The formal matrix does not define an operator on the finite-support basis, since

\[
K_p e_0
=(\log p)\sum_{j\ge1}e_j
\notin\ell^2(\mathbb N_0).
\tag{7}
\]

Thus, exactly as in the general unbounded-Toeplitz setting, the finite-shell object that exists canonically is the quadratic form, not a symmetric operator on `c_00`.

## 2. The exact finite-shell form is not closable

For `N>=1` set

\[
u_N
=\frac1N\sum_{j=0}^{N-1}e_j.
\tag{8}
\]

Then

\[
\|u_N\|_2^2=\frac1N\longrightarrow0,
\qquad
\sum_j (u_N)_j=1.
\tag{9}
\]

If

\[
b_p[x]=q_p[x]+(\log p)\|x\|_2^2,
\tag{10}
\]

then (6) gives

\[
b_p[u_N]=\log p
\tag{11}
\]

for every `N`, while

\[
b_p[u_N-u_M]=0
\tag{12}
\]

for every `N,M`, because both vectors have coordinate sum `1`. Thus `u_N -> 0` in `ell^2`, the sequence is Cauchy in the form seminorm, but its form norm does not tend to zero. Therefore

\[
\boxed{b_p\text{ is not closable}.}
\tag{13}
\]

Adding or subtracting a bounded scalar form does not change closability, so

\[
\boxed{q_p\text{ is not closable}.}
\tag{14}
\]

This is exactly a classical Toeplitz obstruction rather than a new operator-theory phenomenon. After dividing (6) by `log p`, its Toeplitz coefficients are

\[
t_k=1\qquad(k\in\mathbb Z),
\tag{15}
\]

whose representing measure on the unit circle is the point mass `delta_1`. Yafaev's theorem says that a semibounded Toeplitz quadratic form on `ell^2(Z_+)` is closable if and only if its representing measure is absolutely continuous. His Example 2.1 is precisely the sequence (8) for `t_k=1` and exhibits the same failure.

Consequently the exact resultant prime axis has no Friedrichs/Kato self-adjoint realization obtained by closing its intrinsic finite-shell quadratic form. A bounded diagonal counterterm cannot repair this: (14) is invariant under every finite scalar shift.

## 3. Abel damping approaches the raw coefficients but not the raw operator

PC-177's valuation-length damping restricts on a fixed prime axis to the ordinary Abel factor. Put

\[
0<r<1,
\qquad
C_r=(r^{|i-j|})_{i,j\ge0}.
\tag{16}
\]

Then

\[
C_r
=I+\sum_{k\ge1}r^k(S^k+S^{*k}),
\tag{17}
\]

where `S` is the unilateral shift, and the damped prime-axis operator is

\[
H_{p,r}
=(\log p)(C_r-I).
\tag{18}
\]

For PC-177's parameter `sigma`, this is exactly `r=p^{-sigma}`. For every fixed finite-support vector,

\[
\lim_{r\uparrow1}
\langle x,H_{p,r}x\rangle
=q_p[x].
\tag{19}
\]

So Abel damping really does converge coefficientwise and pointwise on finite-shell forms to the raw resultant form.

However, its self-adjoint operator limit is completely different. The positive Toeplitz operator `C_r` has the exact inverse

\[
\boxed{
C_r^{-1}
=
\frac{(I-rS)(I-rS^*)}{1-r^2}.
}
\tag{20}
\]

Let `A_r=C_r^{-1}` and, for fixed `x in ell^2`, put

\[
y_r=(A_r+I)^{-1}x.
\tag{21}
\]

Taking the inner product of `(A_r+I)y_r=x` with `y_r` gives

\[
\frac{\|(I-rS^*)y_r\|^2}{1-r^2}
+\|y_r\|^2
=\operatorname{Re}\langle x,y_r\rangle.
\tag{22}
\]

The resolvent is contractive, so `y_r` is bounded. Equation (22) therefore forces

\[
\|(I-rS^*)y_r\|\longrightarrow0.
\tag{23}
\]

Every weak cluster point `y` then satisfies

\[
(I-S^*)y=0.
\tag{24}
\]

But the unilateral backward shift has no nonzero `ell^2` fixed vector, hence `y=0`. Thus `y_r` converges weakly to zero; using (22) once more,

\[
\|y_r\|^2
\le \operatorname{Re}\langle x,y_r\rangle
\longrightarrow0,
\tag{25}
\]

so in fact

\[
(A_r+I)^{-1}\xrightarrow[s]{}0.
\tag{26}
\]

Since for a positive invertible operator

\[
(C_r+I)^{-1}
=I-(C_r^{-1}+I)^{-1},
\tag{27}
\]

we obtain

\[
\boxed{
C_r\xrightarrow[\,r\uparrow1\,]{\mathrm{s.r.}}0.
}
\tag{28}
\]

Therefore

\[
\boxed{
H_{p,r}
\xrightarrow[\,r\uparrow1\,]{\mathrm{s.r.}}
-(\log p)I.
}
\tag{29}
\]

This is the decisive distinction. The finite-shell matrix coefficients in (19) retain the full constant off-diagonal prime-axis coupling, but the canonical self-adjoint Abel limit retains only a scalar. The singular positive component in (6) is pushed into an infinite-energy boundary mode rather than becoming a closed operator.

## 4. Why the two limits disagree

The discrepancy between (19) and (29) is not a paradox; it is exactly what nonclosability predicts. The shifted Abel symbol is the Poisson kernel

\[
P_r(e^{it})
=1+2\sum_{k\ge1}r^k\cos(kt),
\tag{30}
\]

and distributionally

\[
P_r\longrightarrow 2\pi\delta_0.
\tag{31}
\]

Thus the pointwise finite-shell limit remembers boundary evaluation at `z=1`. That boundary point mass is precisely the singular representing measure forbidden by the Toeplitz closability criterion. In the strong-resolvent limit the singular mode escapes instead of producing a finite self-adjoint Toeplitz degree of freedom.

This also shows why simply declaring the raw PC-177 symbol to be an unbounded Toeplitz operator is not an innocuous domain choice. The datum that distinguishes the raw prime-power coupling from the scalar `-(log p)I` is exactly the nonclosable boundary point mass.

## 5. Prior-art and novelty audit

The functional-analytic mechanism is classical. D. R. Yafaev, **On semibounded Toeplitz operators**, *Journal of Operator Theory* 77:1 (2017), 205–216, DOI `10.7900/jot.2016mar20.2095`, arXiv:1603.06229, proves that a semibounded Toeplitz form is closable exactly when its representing measure is absolutely continuous. Theorem 1.3 gives the criterion, and Example 2.1 treats `t_k=1` using exactly the averaging sequence (8). The Poisson/Abel matrices `C_r=(r^{|i-j|})` are likewise the classical positive Toeplitz/Kac–Murdock–Szegő family.

No historical novelty is claimed for either ingredient. The line-specific consequence is the identification forced by PC-177: **the exact cyclotomic-resultant prime-power interaction lands on Yafaev's nonclosable point-mass Toeplitz boundary on every prime valuation axis.** The natural valuation-length regularization used already in PC-177 is exactly its Abel regularization, and removing that regularization in the self-adjoint resolvent topology scalarizes the axis instead of recovering the raw coupling.

Targeted searches around semibounded/unbounded Toeplitz forms, point-mass symbols, boundary evaluation on Hardy space, Poisson-kernel Toeplitz matrices and Kac–Murdock–Szegő regularization found the ambient mechanism squarely inside this classical theory. No novelty claim rests on absence of a paper phrased in Prime-Circle language.

## 6. Exact boundary of the negative result

This finding closes the **prime-separable form-domain repair** of PC-177. It rules out:

- closing the raw constant-off-diagonal form independently on each valuation axis;
- obtaining a Friedrichs/Kato operator from the natural finite-support resultant form;
- repairing closability by any bounded scalar diagonal shift;
- interpreting removal of the canonical per-axis Abel damping as recovery of a nontrivial self-adjoint prime-axis interaction.

It does **not** prove that no self-adjoint realization of the entire formal multi-prime matrix can exist on some domain that couples distinct prime axes before closure. Such a domain would no longer be the independent Toeplitz-axis repair tested here. Nor does the result exclude vertexwise resultant Hessians, shell-dependent off-axis terms, nonlinear forms, cross-level operators, or a geometry-derived renormalization carrying extra data not present in the scalar ratio symbol.

The surviving domain-sensitive branch is therefore narrower than PC-177 left it: a successful construction must make the domain or renormalization itself genuinely nonseparable across prime directions, or derive additional operator data before the shell-normalized resultant graph has split into independent valuation axes.

## 7. Conclusion

The exact resultant ratio graph reaches a singular operator boundary, but the singularity does not by itself create a hidden RH spectrum. On each prime axis the raw finite-shell form is a classical nonclosable point-mass Toeplitz form, while its intrinsic Abel regularization has only the scalar strong-resolvent limit `-(log p)I`. Thus the most canonical local unbounded-domain completion of PC-177 loses, rather than preserves, the prime-power coupling. Any remaining critical/domain-sensitive Prime-Circle mechanism must occur before prime-axis separation or must introduce additional geometry-derived structure beyond this raw scalar resultant symbol.
