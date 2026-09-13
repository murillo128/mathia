# PC-283 — selector-subtracted log remainder is a digamma Green kernel

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-BOUNDARY` for the renormalized single-profile branch left open by PC-282.

PC-282 showed that the radial logarithmic profile

\[
f_\rho(t):=\log|1-\rho\zeta_q^t|,
\qquad 0<\rho<1,
\]

has a diverging collision-selector component when sampled through the finite-section mismatch `ph+rk mod q`. It left open whether the finite remainder after removing that selector might carry a genuinely new boundary symbol. The remainder can in fact be classified exactly. There is a canonical anchor-local renormalization whose full cyclic convolution is a strictly negative digamma multiplier on every nonconstant Fourier mode, and whose large-`q` low-mode limit is the classical logarithmic Green kernel, equivalently `-|D|^{-1}/2` on the mean-zero circle.

The conclusion is therefore a boundary result rather than an RH mechanism: after the forced collision singularity is removed, the **full-domain symbol is classical harmonic data**. What remains genuinely open in the PC-280/282 frontier is the arithmetic information carried by source-dependent two-sided finite-section placement or by a simultaneous critical scaling of `(q,B,rho)`, not a new scalar boundary multiplier.

## 1. The unique anchor-local zero-mean counterterm

The derivation does not require primality, so let `q>=2` and `zeta_q=e^{2 pi i/q}`. Use the unnormalized discrete Fourier transform

\[
\widehat f(j)=\sum_{t\bmod q}f(t)e^{-2\pi ijt/q}.
\]

The root-of-unity product gives the exact zero mode

\[
\sum_{t\bmod q} f_\rho(t)
=\log\left|\prod_{t=0}^{q-1}(1-\rho\zeta_q^t)\right|
=\log(1-\rho^q).
\]

Hence the unique counterterm supported only at the collision/anchor class `t=0` that makes the cyclic profile mean zero is

\[
\boxed{
 k_{q,\rho}(t)
 :=f_\rho(t)-\log(1-\rho^q)\,\mathbf 1_{t=0}.
}
\]

It satisfies

\[
\boxed{\widehat k_{q,\rho}(0)=0.}
\]

This normalization is intrinsic to the same anchor singled out by the prime-circle construction; no values away from the anchor are altered.

Write the PC-282 singular scale as

\[
a_\rho=-\log(1-\rho).
\]

Since

\[
-\log(1-\rho^q)
=a_\rho-\log(1+\rho+\cdots+\rho^{q-1}),
\]

the present counterterm is exactly the PC-282 leading selector subtraction together with a forced finite correction. As `rho -> 1^-`, that correction tends to `-log q`.

## 2. Every nonconstant Fourier multiplier is strictly negative

For `1<=j<=q-1`, put

\[
\alpha=\frac jq,
\qquad
x=\rho^q.
\]

The absolutely convergent expansion

\[
\log|1-\rho e^{i\theta}|
=-\sum_{n\ge1}\frac{\rho^n}{n}\cos(n\theta)
\]

and the root-of-unity filter give

\[
\widehat f_\rho(j)
=-\frac q2\left(
\sum_{m\ge0}\frac{\rho^{mq+j}}{mq+j}
+
\sum_{m\ge0}\frac{\rho^{mq+q-j}}{mq+q-j}
\right).
\]

After adding the zero-mean counterterm and writing everything in `(x,alpha)`, this becomes

\[
\widehat k_{q,\rho}(j)
=
\sum_{m\ge1}\frac{x^m}{m}
-\frac12\sum_{m\ge0}
\left(
\frac{x^{m+\alpha}}{m+\alpha}
+
\frac{x^{m+1-\alpha}}{m+1-\alpha}
\right).
\]

Termwise integration yields the particularly transparent exact form

\[
\boxed{
\widehat k_{q,\rho}(j)
=
\int_0^x
\frac{
1-\tfrac12\bigl(t^{\alpha-1}+t^{-\alpha}\bigr)
}{1-t}\,dt.
}
\]

For `0<t<1` and `0<alpha<1`, both `t^{alpha-1}` and `t^{-alpha}` are strictly greater than `1`. Therefore the integrand is strictly negative, and

\[
\boxed{
\widehat k_{q,\rho}(j)<0
\qquad(1\le j\le q-1).
}
\]

Consequently the full cyclic convolution matrix

\[
C_{q,\rho}(u,v)=k_{q,\rho}(u-v)
\]

is negative semidefinite with one-dimensional kernel equal to the constant mode. Equivalently,

\[
\boxed{-C_{q,\rho}\succeq0,\qquad
\ker C_{q,\rho}=\operatorname{span}\{\mathbf 1\}.}
\]

Thus positivity does arise canonically in this renormalized logarithmic branch, but it is already forced by the elementary harmonic kernel and does not by itself introduce arithmetic spectral data.

## 3. Boundary limit: exact finite digamma spectrum

Because `q` is fixed, entrywise convergence is also operator-norm convergence. At `rho -> 1^-`,

\[
k_{q,\rho}(t)\longrightarrow k_q(t),
\]

where

\[
\boxed{
 k_q(0)=-\log q,
\qquad
 k_q(t)=\log|1-\zeta_q^t|
       =\log\left(2\sin\frac{\pi t}{q}\right)
\quad(t\ne0).
}
\]

The value at the anchor is exactly the finite part required by the root-of-unity product

\[
\prod_{t=1}^{q-1}|1-\zeta_q^t|=q,
\]

so `sum_t k_q(t)=0`.

Taking `x -> 1^-` in the integral formula and using the classical digamma identity

\[
\psi(z)+\gamma
=
\int_0^1\frac{1-t^{z-1}}{1-t}\,dt
\qquad(\Re z>0)
\]

gives the exact nonzero Fourier multipliers

\[
\boxed{
\widehat k_q(j)
=
\gamma+rac12\left[
\psi\left(\frac jq\right)
+
\psi\left(1-\frac jq\right)
\right]
<0,
\qquad 1\le j\le q-1.
}
\]

Together with `\widehat k_q(0)=0`, this completely diagonalizes the boundary-renormalized full cyclic operator. The same formula is equivalent to the classical finite Fourier/Gauss-digamma transform of the log-sine kernel.

The sign is not a numerical observation. The integral representation above proves it pointwise for every `q`, every nonconstant mode, and every `0<rho<=1` after taking the boundary limit where appropriate.

## 4. Large-`q` low modes are the classical circle Green multiplier

Fix a nonzero integer Fourier mode `m`. For `q>|m|`, identify it with `j=m mod q`. The standard small-argument expansion

\[
\psi(x)=-\gamma-\frac1x+O(x)
\qquad(x\to0^+)
\]

and the symmetry `j <-> q-j` imply

\[
\boxed{
\frac1q\widehat k_q(m\bmod q)
\longrightarrow
-\frac1{2|m|}.
}
\]

These are exactly the nonzero Fourier coefficients of the mean-zero logarithmic circle kernel

\[
\log|1-e^{i\theta}|
=\log\left(2\left|\sin\frac\theta2\right|\right)
=-\sum_{m\ge1}\frac{\cos(m\theta)}m.
\]

Accordingly, on fixed low Fourier modes,

\[
-\frac{2}{q}C_{q}
\longrightarrow |D|^{-1}
\]

on the mean-zero circle. This is the standard logarithmic single-layer/Green kernel behavior, not a new Riemann-zero operator.

No operator-norm limit across the growing spaces is asserted here; the statement is the exact finite multiplier formula plus fixed-mode convergence.

## 5. What happens to the PC-280/282 finite section

For source units `p,r mod q` and a window `H_B`, PC-282 studies

\[
L^{\rho}_{p,r;B}(h,k)
=f_\rho(ph+rk).
\]

Let

\[
Z_{p,r;B}(h,k)=\mathbf 1_{ph+rk\equiv0\pmod q}.
\]

The canonical renormalized finite section is therefore

\[
\boxed{
K^{\rho}_{p,r;B}
=L^{\rho}_{p,r;B}
-\log(1-\rho^q)Z_{p,r;B}.
}
\]

Using PC-282's decomposition `L^rho=-a_rho Z+R^rho`, this can equally be written

\[
K^{\rho}_{p,r;B}
=R^{\rho}_{p,r;B}
-\log(1+\rho+\cdots+\rho^{q-1})Z_{p,r;B},
\]

and hence

\[
\boxed{
K^{\rho}_{p,r;B}
\longrightarrow
K^{\partial}_{p,r;B}
=R^{\partial}_{p,r;B}-(\log q)Z_{p,r;B}.
}
\]

By PC-280 this is still exactly a two-sided finite section of one cyclic convolution:

\[
K^{\rho}_{p,r;B}
=E_{pH_B}C_{q,\rho}E_{rH_B}^{*}.
\]

Therefore the **underlying full-domain multiplier has now been completely classicalized**. For `p=r`, the finite compression inherits negative semidefiniteness. For `p != r`, however, the two row/column placements differ, and positivity of the full convolution does not classify the singular values of the mismatch finite section. That source-dependent placement is precisely the part PC-280 identified as potentially nontrivial.

## 6. Prior-art and novelty audit

The ingredients are classical.

- The Fourier expansion of `log|1-rho e^{i theta}|` is the standard harmonic expansion of the two-dimensional logarithmic potential.
- The root-of-unity filter and the product `prod_{t=1}^{q-1}|1-zeta_q^t|=q` are elementary cyclotomic identities.
- The boundary multiplier is the Gauss/digamma finite Fourier transform of the log-sine kernel. The digamma integral used above is standard; see NIST DLMF §5.9(ii), especially Eq. 5.9.16.
- The continuum multiplier `-1/(2|m|)` is the classical Fourier diagonalization of the logarithmic single-layer kernel on the circle.

Directed searches around finite log-sine transforms, Gauss's digamma theorem, logarithmic potential operators on the circle, and conditionally definite cyclic kernels found these ingredients squarely in classical harmonic/special-function territory. No novelty is claimed for the transform, the sign, or the Green-kernel interpretation.

The project-local delta is the exact placement of this classical object at the PC-282 boundary: the unique anchor-local mean-zero counterterm is `-log(1-rho^q)`, its finite boundary correction is `-log q`, and after that subtraction there is no unexplained full-torus spectral symbol left to attribute to prime-circle geometry.

An apparent resemblance of

\[
\psi(j/q)+\psi(1-j/q)
\]

to a functional-equation reflection is a false positive for the RH target. The symmetry is only the even circle mode `j <-> q-j`; there is no free complex spectral variable `s`, no intrinsic `s <-> 1-s` continuation, no completed zeta gamma factor, and no zero divisor encoding the nontrivial zeros.

## 7. Consequence and surviving boundary

This closes the simplest interpretation of PC-282's **renormalized single-profile boundary remainder** as a new operator symbol:

\[
\text{radial log profile}
\to
\text{collision subtraction}
\to
\text{boundary remainder}
\to
\text{new full-domain RH spectrum}
\]

fails. The exact remainder is a discrete log-sine/digamma Green kernel and converges modewise to the classical inverse-`|D|` kernel.

It does **not** close the whole finite-section program. Two possibilities remain outside this result and should not be conflated with the classicalized symbol:

1. the arithmetic dependence of the two-sided source placements `E_{pH_B}` and `E_{rH_B}` acting on this fixed multiplier, especially in a critical growing-window regime not covered by PC-281; and
2. simultaneous scaling of `(q,B,rho)` where the selector and regular remainder remain comparable rather than one asymptotically dominating the other.

Any future claim from this branch must therefore survive a matched rational/source control at the **finite-section placement or coupled-scaling level**. Repackaging the boundary digamma multiplier, its positivity, or its `|D|^{-1}` limit is not additional RH progress.
