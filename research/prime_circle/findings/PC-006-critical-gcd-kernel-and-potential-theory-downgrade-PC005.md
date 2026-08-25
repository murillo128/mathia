# PC-006 — potential theory and the critical GCD kernel substantially downgrade PC-005 as an RH mechanism

**Status:** `DECISIVE-NEGATIVE` + `NOVELTY-CORRECTION` + `EXACT-DERIVED`

## Summary

PC-004/PC-005 found, on each prime-power ray, the exact kernel

\[
K^{(p)}_{ab}=(\log p)p^{-|a-b|/2}.
\]

The derivation from primitive-root polygons remains correct. However, a stronger novelty audit shows that the two structural ingredients previously viewed as potentially new are already parts of well-developed classical theories:

1. logarithmic mutual energy = minus log resultant, while the discriminant is the corresponding renormalized self-energy;
2. the half-density kernel \(p^{-|a-b|/2}\) is the prime-ray factor of the classical critical GCD kernel \(\gcd(m,n)/\sqrt{mn}\), whose Poisson-integral structure at \(\alpha=1/2\) has been studied explicitly.

Moreover, the natural unified logarithmic/Dirichlet energy does **not** produce the PC-005 diagonal \(\log p\) directly: its same-shell finite part is the discriminant energy itself. PC-005 obtains \(\log p\) only after applying an additional discrete scale derivative. Thus PC-005 currently splices two natural operations, rather than exhibiting one geometric positive quadratic form whose matrix is \(K^{(p)}\).

This substantially downgrades PC-005 as a candidate-new RH mechanism. The remaining gate is stricter: derive the scale derivative and global renormalization from one intrinsic operator/energy, rather than inserting a second operation after the mutual-energy construction.

## 1. Resultants and discriminants already belong to one classical potential theory

Gustafsson and Tkachev, *The Resultant on Compact Riemann Surfaces*, Commun. Math. Phys. 286 (2009), 313–358, prove in general that for divisor charge distributions \(\mu,\nu\),

\[
I(\mu,\nu)=-\log|\mathcal R(f,g)|,
\]

and that the discriminant is the exponential of the negative **renormalized self-energy**, with the point-charge diagonal singularities removed. They also express the mutual energy as a Dirichlet integral and develop determinant/Toeplitz representations.

Therefore the conceptual bridge

\[
\text{mutual shell chord energy}\leftrightarrow\text{resultant},
\qquad
\text{same-shell renormalized energy}\leftrightarrow\text{discriminant}
\]

is not new to the prime-circle construction; the cyclotomic shells are a distinguished specialization of a general potential-theoretic mechanism.

Reference:

- B. Gustafsson, V. G. Tkachev, *The Resultant on Compact Riemann Surfaces*, Commun. Math. Phys. **286** (2009), 313–358, DOI 10.1007/s00220-008-0622-2; arXiv:0710.2326. In particular §§5.1–5.2.

## 2. One exact Dirichlet Gram family contains both resultant and discriminant finite parts

Let

\[
F_n(z)=\log\Phi_n(z),\qquad F_n(0)=0,
\]

with the analytic branch in the unit disk. Since

\[
F_n(z)=-\sum_{k\ge1}\frac{c_n(k)}{k}z^k,
\]

where \(c_n(k)\) is the Ramanujan sum, define the radial regularization

\[
F_{n,r}(z)=F_n(rz),\qquad 0<r<1.
\]

For the analytic Dirichlet inner product,

\[
\langle f,g\rangle_{\mathcal D}
=\frac1\pi\int_{\mathbb D}f'(z)\overline{g'(z)}\,dA(z),
\]

we obtain exactly

\[
\boxed{
\langle F_{m,r},F_{n,r}\rangle_{\mathcal D}
=\sum_{k\ge1}\frac{c_m(k)c_n(k)}{k}r^{2k}.
}
\]

As \(r\uparrow1\), for \(m\ne n\) the finite limit is

\[
\boxed{
\langle F_{m,r},F_{n,r}\rangle_{\mathcal D}
\longrightarrow -\log|\operatorname{Res}(\Phi_m,\Phi_n)|
}
\]

(up to the sign convention for logarithmic potential), while for \(m=n\)

\[
\boxed{
\langle F_{n,r},F_{n,r}\rangle_{\mathcal D}
=-\varphi(n)\log(1-r^2)-\log|\operatorname{Disc}\Phi_n|+o(1).
}
\]

Thus a single positive regularized Gram family naturally supplies the off-diagonal resultants and the same-shell discriminant finite parts.

But crucially its diagonal finite part is **not** \(\log p\) on the ray \(n=p^a\). It is

\[
-\log|\operatorname{Disc}\Phi_{p^a}|.
\]

The PC-005 value

\[
\log p
\]

appears only after the separate operation

\[
\Delta_a\left[
\frac{\log|\operatorname{Disc}\Phi_{p^a}|}{\varphi(p^a)}
\right]
=\log p.
\]

So the positivity of the completed Poisson kernel is not yet the positivity of this canonical Dirichlet energy.

## 3. The same half-density kernel is already the critical GCD kernel

There is an even more direct route from the original regular polygons. Put

\[
V_n(z)=\log(1-z^n),
\qquad
V_{n,r}(z)=V_n(rz).
\]

Using

\[
V_{n,r}(z)=-\sum_{j\ge1}\frac{r^{nj}}{j}z^{nj},
\]

a direct coefficient calculation gives

\[
\boxed{
\langle V_{m,r},V_{n,r}\rangle_{\mathcal D}
=-\gcd(m,n)\log\!\left(1-r^{2\operatorname{lcm}(m,n)}\right).
}
\]

Hence

\[
\langle V_{m,r},V_{n,r}\rangle_{\mathcal D}
=-\gcd(m,n)\log(1-r^2)
-\gcd(m,n)\log\operatorname{lcm}(m,n)+o(1).
\]

After normalizing the leading boundary divergence by \(\sqrt{mn}\), its Gram kernel is

\[
\boxed{
C_{mn}=\frac{\gcd(m,n)}{\sqrt{mn}}.
}
\]

In valuation coordinates,

\[
\boxed{
C_{mn}
=\prod_p p^{-\frac12|v_p(m)-v_p(n)|}
=\exp\!\left[-\frac12\sum_p|v_p(m)-v_p(n)|\log p\right].
}
\]

Therefore on the prime-power ray \(m=p^a,n=p^b\),

\[
\boxed{
C_{p^a,p^b}=p^{-|a-b|/2}.
}
\]

The \(p^{-k/2}\) factor in PC-004/005 is thus not an isolated new half-density phenomenon: it is exactly the local factor of the global critical GCD kernel.

## 4. Prior art already studies the critical \(\alpha=1/2\) Poisson structure

Aistleitner, Berkes and Seip study

\[
\sum_{k,\ell}
\frac{\gcd(n_k,n_\ell)^{2\alpha}}
{(n_kn_\ell)^\alpha},
\qquad 0<\alpha\le1,
\]

identify these GCD sums with Poisson integrals on a polydisc, and explicitly treat the critical case \(\alpha=1/2\), including spectral estimates for the corresponding GCD matrices.

At \(\alpha=1/2\), their matrix entry is precisely

\[
\boxed{
\frac{\gcd(m,n)}{\sqrt{mn}}.
}
\]

Reference:

- C. Aistleitner, I. Berkes, K. Seip, *GCD sums from Poisson integrals and systems of dilated functions*, J. Eur. Math. Soc. **17** (2015), 1517–1546, DOI 10.4171/JEMS/537; arXiv:1210.0741.

Thus the Poisson/Toeplitz positivity and the critical exponent \(1/2\) attached to the prime-ray factors are already embedded in a substantial classical literature on GCD matrices.

## 5. What survives from PC-005

The exact cyclotomic specialization remains valid and potentially useful:

\[
\frac{\log|\operatorname{Res}(\Phi_{p^a},\Phi_{p^b})|}
{\sqrt{\varphi(p^a)\varphi(p^b)}}
=(\log p)p^{-|a-b|/2},
\qquad a\ne b,
\]

and

\[
\Delta_a\left[
\frac{\log|\operatorname{Disc}\Phi_{p^a}|}{\varphi(p^a)}
\right]
=\log p.
\]

No source was found in this audit writing **this exact cyclotomic splice** in the PC-005 form. But its strongest previous interpretation must be downgraded:

- the energy/resultant/discriminant organization is classical potential theory;
- the half-density Poisson kernel is the classical critical GCD kernel restricted to one valuation axis;
- the positive completed PC-005 matrix is not currently derived as the Gram matrix of one canonical prime-circle energy, because its diagonal uses a scale derivative not used off diagonal.

Accordingly PC-005 should not presently be treated as evidence for a new RH mechanism.

## 6. Stronger gate for future work

A genuinely substantive continuation must derive, from **one intrinsic global object**, all three operations:

1. mutual shell interaction;
2. same-shell renormalization / scale derivative;
3. the global/archimedean counterterm that removes the divergent \(\sum_p\log p\) diagonal.

If a single operator or variational principle produces these without importing the Weil explicit formula as input, that would survive the present negative result. Simply recognizing another Poisson/GCD kernel or another appearance of \(1/2\) will not.
