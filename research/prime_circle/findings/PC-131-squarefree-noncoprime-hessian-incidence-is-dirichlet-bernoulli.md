# PC-131 — squarefree noncoprime Hessian incidence is fixed Dirichlet–Bernoulli data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `PRIOR-ART-REDIRECTION` + `NEGATIVE` for treating the linear multiplicative-character coordinates of a squarefree noncoprime PC-128 cross-shell inverse-square Hessian as a new arithmetic or RH-sensitive coefficient alphabet. This does not diagonalize the finite Hessian, classify its nonlinear eigenvalue/singular-value invariants, cover nonsquarefree noncoprime pairs, or address cross-level/infinite constructions or the global uniformization/monodromy branch of PC-017.

PC-129/PC-130 completely classify the coprime two-shell frontier: the edge multiset is the pointed product-shell profile and its CRT incidence becomes fixed `L(2,eta)` data after the two-sided multiplicative Fourier transform. The natural unresolved finite case is therefore a **noncoprime** pair of primitive shells, where the quotient map has nontrivial fibers and the clean CRT bijection of PC-130 fails.

For distinct squarefree `m,n`, that failure does not create a new linear harmonic package. In the multiplicative character bases of `U(m)` and `U(n)`, every matrix coefficient of the cross-shell inverse-square conductance block is either an explicit Gauss-factor multiple of one fixed generalized-Bernoulli value `L(-1,eta)`, with elementary local Euler factors, or a finite rational divisor sum in the principal conductor channel. Equivalently, after the standard functional equation in primitive parity-compatible channels, the same coefficients lie in the classical fixed-critical-value Dirichlet package already visible in PC-130.

The remaining finite difficulty is therefore nonlinear organization of these fixed coefficients, not a hidden new linear Fourier datum created by noncoprime shell incidence.

## 1. Cross-shell conductance as a restriction of the universal cyclic kernel

Let `m,n>1` be distinct squarefree integers with `(m,n)>1`, and put

\[
L=\operatorname{lcm}(m,n),\qquad
M=\frac{L}{m},\qquad
N=\frac{L}{n}.
\]

Write

\[
G_m=(\mathbb Z/m\mathbb Z)^\times,
\qquad
G_n=(\mathbb Z/n\mathbb Z)^\times.
\]

The primitive-shell vertices embedded in the common `L`-gon are

\[
\alpha_a=\zeta_L^{Ma},\qquad a\in G_m,
\]

and

\[
\beta_b=\zeta_L^{Nb},\qquad b\in G_n.
\]

The off-diagonal block of the PC-128 Hessian is

\[
\boxed{
C_{m,n}(a,b)
=\frac1{|\alpha_a-\beta_b|^2}
=\frac1{4\sin^2\!\bigl(\pi(Ma-Nb)/L\bigr)}.
}
\]

Since `m != n`, primitive roots of orders `m` and `n` cannot coincide, so `Ma-Nb` is never `0 mod L` on `G_m x G_n`.

Define the universal cyclic conductance profile

\[
c_L(u)=\frac1{4\sin^2(\pi u/L)},\qquad u\not\equiv0\pmod L,
\]

and set `c_L(0)=0` only for Fourier bookkeeping. Its discrete Fourier transform is the classical inverse-square polygon transform

\[
\boxed{
\widehat c_L(k)=d_L-\lambda_k,
\qquad
d_L=\frac{L^2-1}{12},
\qquad
\lambda_k=\frac{k(L-k)}2.
}
\]

Thus the noncoprime cross-shell problem is still a restriction of the same universal cyclic kernel used in PC-032/PC-044; all arithmetic lies in how the two reduced-residue sets sample it.

## 2. Two-sided character transform reduces to generalized Gauss transforms

For multiplicative characters `chi` of `G_m` and `psi` of `G_n`, use normalized bases

\[
e_\chi(a)=\frac{\chi(a)}{\sqrt{\varphi(m)}},
\qquad
f_\psi(b)=\frac{\psi(b)}{\sqrt{\varphi(n)}}.
\]

Put

\[
\mathcal M_{\chi,\psi}
:=\langle e_\chi,C_{m,n}f_\psi\rangle.
\]

For a Dirichlet character `rho mod q`, extended by zero off `U(q)`, define its additive transform

\[
G_\rho^{(q)}(k)
:=\sum_{a\in U(q)}\rho(a)e^{2\pi i k a/q}.
\]

Substituting the cyclic Fourier expansion of `c_L` gives

\[
\mathcal M_{\chi,\psi}
=\frac1{L\sqrt{\varphi(m)\varphi(n)}}
\sum_{k=0}^{L-1}
(d_L-\lambda_k)
G_{\overline\chi}^{(m)}(k)
G_\psi^{(n)}(-k).
\]

The constant `d_L` term vanishes exactly. Indeed, finite Fourier orthogonality turns it into a weighted count of solutions of

\[
Ma\equiv Nb\pmod L,
\]

which would mean `alpha_a=beta_b`, impossible for distinct exact orders. Therefore

\[
\boxed{
\mathcal M_{\chi,\psi}
=-\frac1{L\sqrt{\varphi(m)\varphi(n)}}
\sum_{k=0}^{L-1}
\lambda_k
G_{\overline\chi}^{(m)}(k)
G_\psi^{(n)}(-k).
}
\]

This is the cross-modulus analogue of the additive/multiplicative compression formula in PC-044.

## 3. Squarefreeness gives Gauss × Ramanujan factorization

Let `chi` be induced by a primitive character `chi*` of conductor `f|m`, and let `psi` be induced by primitive `psi*` of conductor `h|n`. Because `m,n` are squarefree,

\[
q:=\frac mf,\qquad r:=\frac nh
\]

satisfy `(f,q)=(h,r)=1`. The standard generalized Gauss-transform formula used in PC-044 gives

\[
G_\rho^{(s)}(k)
=\rho^*(s/f_\rho)\,\tau_{f_\rho}(\rho^*)\,
\overline{\rho^*(k)}\,c_{s/f_\rho}(k).
\]

Applied to the two factors above, this yields

\[
G_{\overline\chi}^{(m)}(k)
G_\psi^{(n)}(-k)
=
K_{\chi,\psi}\,\eta(k)c_q(k)c_r(k),
\]

where

\[
\boxed{
K_{\chi,\psi}
=
\overline{\chi^*(q)}\,
\psi^*(r)\,
\overline{\psi^*(-1)}\,
\tau_f(\overline{\chi^*})\,
\tau_h(\psi^*)
}
\]

and, on modulus

\[
\ell=\operatorname{lcm}(f,h),
\]

we define

\[
\boxed{
\eta=\chi^*\overline{\psi^*}
}
\]

with the usual zero extension away from `U(ell)`.

Consequently

\[
\boxed{
\mathcal M_{\chi,\psi}
=-\frac{K_{\chi,\psi}}
{L\sqrt{\varphi(m)\varphi(n)}}
\sum_{k=0}^{L-1}
\lambda_k\eta(k)c_q(k)c_r(k).
}
\]

Everything left is a finite quadratic Ramanujan correlation.

## 4. Nonprincipal conductor channels are one fixed `L(-1,eta)` value

Because `q,r` are squarefree, separate their prime supports into

\[
\Delta:=\{p:p\mid q\text{ xor }p\mid r\},
\qquad
I:=\{p:p\mid q\text{ and }p\mid r\}.
\]

For `p in Delta`, one local factor is

\[
c_p(k)=-1+p\,\mathbf1_{p\mid k},
\]

while for `p in I`,

\[
c_p(k)^2=1+p(p-2)\mathbf1_{p\mid k}.
\]

Hence

\[
\boxed{
c_q(k)c_r(k)
=(-1)^{|\Delta|}
\sum_{d\mid\operatorname{rad}(qr)}A_d\mathbf1_{d\mid k},
}
\]

where `A_d` is multiplicative on the relevant squarefree divisors and

\[
A_p=
\begin{cases}
-p,&p\in\Delta,\\
p(p-2),&p\in I.
\end{cases}
\]

Assume now that `eta` is nonprincipal. If `(d,ell)>1`, then `eta(k)=0` on every term with `d|k`. If `(d,ell)=1`, then `L/d` is still a multiple of `ell`, and the generalized Bernoulli identity gives the exact quadratic sum

\[
\boxed{
\sum_{\substack{0\le k<L\\ d\mid k}}
\lambda_k\eta(k)
=dL\,\eta(d)L(-1,\eta).
}
\]

Substituting and resumming multiplicatively therefore gives

\[
\boxed{
\begin{aligned}
&\sum_{k=0}^{L-1}
\lambda_k\eta(k)c_q(k)c_r(k)\\
&\quad=
(-1)^{|\Delta|}L\,L(-1,\eta)
\prod_{\substack{p\in\Delta\\p\nmid\ell}}
\left(1-p^2\eta(p)\right)
\prod_{\substack{p\in I\\p\nmid\ell}}
\left(1+p^2(p-2)\eta(p)\right).
\end{aligned}
}
\]

Thus every nonprincipal coefficient is

\[
\boxed{
\begin{aligned}
\mathcal M_{\chi,\psi}
&=
\frac{(-1)^{|\Delta|+1}K_{\chi,\psi}}
{\sqrt{\varphi(m)\varphi(n)}}
L(-1,\eta)\\
&\qquad\times
\prod_{\substack{p\in\Delta\\p\nmid\ell}}
\left(1-p^2\eta(p)\right)
\prod_{\substack{p\in I\\p\nmid\ell}}
\left(1+p^2(p-2)\eta(p)\right).
\end{aligned}
}
\]

There is no free complex spectral variable: the only analytic datum is the fixed generalized-Bernoulli special value `L(-1,eta)`, multiplied by Gauss sums and elementary local factors.

Parity zeros are automatic. If `eta(-1)=-1`, then `L(-1,eta)=0`, matching the reflection selection rules already seen elsewhere in the Prime-Circle chord/cotangent branches.

## 5. Principal conductor channels are finite rational divisor sums

The only case not covered by the preceding formula is when `eta` is principal. Then `chi*` and `psi*` have the same primitive ancestor; writing its common conductor as `ell`,

\[
\eta(k)=\mathbf1_{(k,\ell)=1}.
\]

No new special function appears. Expand both the Ramanujan product as above and the coprimality indicator by Möbius inversion:

\[
\mathbf1_{(k,\ell)=1}
=\sum_{e\mid\ell}\mu(e)\mathbf1_{e\mid k}.
\]

For every `a|L`, the universal quadratic sum is elementary:

\[
\boxed{
T_a(L)
:=\sum_{\substack{0\le k<L\\a\mid k}}\lambda_k
=\frac{L(L^2-a^2)}{12a}.
}
\]

Therefore the remaining correlation is exactly

\[
\boxed{
\sum_{k=0}^{L-1}\lambda_k\eta(k)c_q(k)c_r(k)
=
(-1)^{|\Delta|}
\sum_{d\mid\operatorname{rad}(qr)}A_d
\sum_{e\mid\ell}\mu(e)
T_{\operatorname{lcm}(d,e)}(L).
}
\]

This is a finite rational divisor expression. Hence the principal-conductor channels are even more elementary than the nonprincipal ones: they contain no `L`-value beyond the Bernoulli/zeta values already implicit in the quadratic polynomial sum.

Together, Sections 4 and 5 classify **every** linear multiplicative-character coefficient of `C_{m,n}` for distinct squarefree noncoprime `m,n`.

## 6. Exact audits

Two small noncoprime examples exercise both branches.

For `(m,n)=(6,15)` and principal characters on both endpoint groups, direct evaluation gives

\[
\boxed{\mathcal M_{1,1}=15.}
\]

Here `q=6`, `r=15`, `ell=1`; the principal divisor formula gives the same value exactly.

For `(m,n)=(10,15)`, let `chi` be the character modulo `10` induced by the quadratic character `chi_5` modulo `5`, and let `psi` be principal modulo `15`. Then `eta=chi_5`, `|Delta|=3`,

\[
L(-1,\chi_5)=-\frac25,
\qquad
\tau_5(\chi_5)=\sqrt5,
\]

and the local product is

\[
(1-2^2\chi_5(2))(1-3^2\chi_5(3))=50.
\]

The formula gives

\[
\boxed{
\mathcal M_{\chi,1}=\frac{5\sqrt{10}}2,
}
\]

which agrees with direct summation of the `4 x 8` conductance matrix.

These examples are checks only; the derivation is exact for all distinct squarefree noncoprime `m,n`.

## 7. Relation to PC-044, PC-125 and PC-130

This result deliberately avoids manufacturing a duplicate from an apparently new noncoprime quotient distribution.

PC-125 already classifies the **complete ratio multiset** `beta/alpha` for arbitrary shell indices as a finite cyclotomic divisor, with exact multiplicities given by Ramanujan triple correlations. Since

\[
|\alpha-\beta|^{-2}=|1-\alpha\beta^{-1}|^{-2},
\]

the raw noncoprime edge-value multiset is already a direct corollary of PC-125. It is not a new finding.

PC-130 goes further in the coprime case because CRT makes the endpoint incidence itself a bijective reshape of one pointed product-shell profile. The present calculation addresses precisely what fails when that bijection is unavailable: for squarefree noncoprime shells, the **full rectangular incidence matrix** still has no new linear character alphabet. Its coefficients reduce to Gauss/Ramanujan factors and fixed `L(-1)`/Bernoulli data.

PC-044 obtains a closely related Bernoulli coupling for the squarefree **single-level primitive compression** of the full chord Laplacian. PC-131 is the cross-shell counterpart: two different reduced-residue groups, two different conductors, and the rectangular PC-128 Hessian block. The shared derivation is evidence of classicalization, not an independent new `L`-mechanism.

## 8. Prior art and novelty audit

No theorem-level historical novelty is claimed.

- The finite trigonometric-character-sum framework is classical. Beck–Halloran, already anchored in `research/prime_circle/SOURCES.md`, derives broad families of such identities by discrete Fourier analysis.
- Gao–Guo, also already anchored there, treats trigonometric matrices and determinants through Dirichlet `L`-values, Gauss sums, and spectral decomposition for arbitrary positive moduli. This is a particularly strong novelty warning against interpreting the fixed special values above as a new spectral bridge.
- Ramanujan sums, induced-character Gauss transforms, generalized Bernoulli identities, and finite cyclic Fourier diagonalization are all standard ingredients. PC-044 already combines the same ingredients for the squarefree single-level compression.
- PC-125 independently prevents a false novelty claim at the edge-multiset level: arbitrary shell-ratio multiplicities are already finite Ramanujan/cyclotomic data before the Hessian incidence is studied.

Directed searches around cosecant-squared character matrices, noncoprime moduli, finite trigonometric character sums, and Dirichlet-`L` spectral decompositions found the established Beck–Halloran and Gao–Guo neighborhoods, not an exact published statement of this particular two-modulus PC-128 rectangular formula. That absence is **not** a priority claim. The durable contribution is the Prime-Circle scope classification: the first noncoprime squarefree incidence frontier left by PC-130 remains inside fixed classical Dirichlet–Bernoulli coefficient data.

## 9. Research consequence and boundary

For distinct squarefree noncoprime shell indices,

\[
\boxed{
\text{noncoprime PC-128 Hessian incidence}
\xrightarrow{\text{two-sided multiplicative Fourier}}
\text{Gauss/Ramanujan factors}\times L(-1,\eta)
\text{ or rational divisor data}.
}
\]

So noncoprimality does not by itself supply a new linear harmonic carrier, a complex spectral parameter, a functional equation, a gamma factor, or a critical-line selector. At the coefficient level it is another finite classical special-value package.

The obstruction is intentionally limited. It does **not** prove that singular values, eigenvalues, determinants after nontrivial cross-shell coupling, or other nonlinear matrix functions are elementary; those can mix many fixed coefficients. It also does not cover repeated prime powers, where the squarefree Gauss × Ramanujan factorization must be replaced by the full imprimitive local theory, nor does it address a coherent cross-level/infinite operator, an intrinsically forced renormalization, or PC-017's nonlinear uniformization/monodromy defect.

The practical boundary after PC-130 is therefore narrower: **a finite squarefree noncoprime Hessian cannot claim novelty from its raw incidence or any linear multiplicative-character coordinate.** Any surviving use must exploit controlled nonlinear organization, genuinely nonsquarefree local depth, cross-level/infinite structure, or a different nonlinear geometric mechanism.
