# PC-406 — shell-2 descendant Dirichlet sum is a Jordan-zeta ratio

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most direct infinite-level analytic resummation left open by PC-405. After conjugating the canonical shell-2 child maps to ordinary dilations, the complete descendant Dirichlet family has a universal Euler product. Polynomial Mellin moments give finite Euler corrections times `zeta(s+j)/zeta(s)`, and the full complex Mellin-character readout gives the same ratio with `j` replaced by a complex dilation character `z`. Moreover, the conjugated shell-2 measure is exactly the signed radial-flux measure of PC-179, so the only source-specific zeta factor in the two-variable transform is the already-classical one-shell Mellin carrier. Thus the natural infinite-level Dirichlet completion does not create a new analytic carrier: its nontrivial zeta divisors either pre-exist in the one-shell flux or appear only after scalarization and analytic continuation beyond the descendant operator series' native convergence domain.

This does **not** rule out every infinite-level or renormalized limit of the shell-2 refinement system. It closes the canonical conductor-Dirichlet resummation of all descendants, its operator-valued Euler product, its polynomial Mellin moments, and its full scalar Mellin-character diagonalization.

## 1. Start from the exact PC-405 dilation model

PC-405 associates to each shell `n>1` a finite signed shell-2 measure `mu_n` and proves the exact prime-child rule

\[
\mu_{pn}=\begin{cases}
T_p\mu_n,&p\mid n,\\
(T_p-I)\mu_n,&p\nmid n,
\end{cases}
\tag{1}
\]

where the pushforwards satisfy `T_aT_b=T_{ab}`. In the canonical coordinate

\[
\chi(t)=-\log(e^t-1),
\tag{2}
\]

PC-405 proves

\[
\chi(h_a(t))=\frac{\chi(t)}a.
\tag{3}
\]

Put

\[
\nu_n:=\chi_*\mu_n
\]

and let `S_a` denote pushforward under the ordinary dilation `x -> x/a` on `[0,\infty)`. Then (1) becomes

\[
\boxed{
\nu_{pn}=\begin{cases}
S_p\nu_n,&p\mid n,\\
(S_p-I)\nu_n,&p\nmid n.
\end{cases}}
\tag{4}
\]

with

\[
S_aS_b=S_{ab}.
\tag{5}
\]

The question left open here is genuinely infinite-level: what happens if one sums the entire multiplicative descendant tree instead of taking a finite list of descendants and a finite Chen packet?

## 2. Prime-power descendants have only two local factors

Fix the parent `n`. For `k>=1`, iterating (4) gives the exact local descendant operators

\[
B_{n,p^k}=\begin{cases}
S_{p^k},&p\mid n,\\
S_{p^k}-S_{p^{k-1}},&p\nmid n.
\end{cases}
\tag{6}
\]

The second line has one fresh-prime difference followed by `k-1` repeated-prime dilations. Because all `S_p` commute, if

\[
m=\prod_p p^{k_p},
\]

then

\[
\boxed{
\nu_{nm}=B_{n,m}\nu_n,
\qquad
B_{n,m}=\prod_p B_{n,p^{k_p}},
}
\tag{7}
\]

with the `k_p=0` factor interpreted as `I`.

This is already enough to form the canonical conductor-Dirichlet series without introducing any extra interaction law.

## 3. The operator-valued Dirichlet series has a universal Euler product

On finite signed measures with total-variation norm, every `S_p` has operator norm at most one. Hence for `sigma=Re(s)>1` the series

\[
\mathcal D_n(s):=\sum_{m\ge1}m^{-s}B_{n,m}
\tag{8}
\]

converges in operator norm and its Euler product can be computed prime by prime.

For `p|n`,

\[
\sum_{k\ge0}p^{-ks}B_{n,p^k}
=(I-p^{-s}S_p)^{-1}.
\tag{9}
\]

For a fresh prime `p\nmid n`,

\[
\begin{aligned}
I+\sum_{k\ge1}p^{-ks}(S_{p^k}-S_{p^{k-1}})
&=(1-p^{-s})(I-p^{-s}S_p)^{-1}.
\end{aligned}
\tag{10}
\]

Therefore

\[
\boxed{
\mathcal D_n(s)
=
\prod_{p\mid n}(I-p^{-s}S_p)^{-1}
\prod_{p\nmid n}(1-p^{-s})(I-p^{-s}S_p)^{-1}.
}
\tag{11}
\]

Equivalently,

\[
\boxed{
\mathcal D_n(s)
=
\frac1{\zeta(s)}
\left[\prod_p(I-p^{-s}S_p)^{-1}\right]
\prod_{p\mid n}(1-p^{-s})^{-1},
\qquad \Re(s)>1.
}
\tag{12}
\]

The convergence statement is elementary: each fresh-prime factor differs from `I` by `O(p^{-sigma})` in operator norm, and `sum_p p^{-sigma}` converges for `sigma>1`; the finitely many primes dividing `n` cause no difficulty.

Equation (12) is already a warning sign. The infinite-level object is a universal dilation Euler product with a scalar Möbius factor, not a new interaction among cyclotomic shells.

## 4. Every polynomial Mellin moment is exactly `zeta(s+j)/zeta(s)`

For an integer `j>=0`, define the moment functional

\[
M_j(\nu):=\int_0^\infty x^j\,d\nu(x).
\tag{13}
\]

The shell-2 measures have all such moments, and dilation gives

\[
M_j(S_a\nu)=a^{-j}M_j(\nu).
\tag{14}
\]

Applying (14) to (6)--(7) yields the exact coefficient formula

\[
\boxed{
M_j(\nu_{nm})
=
m^{-j}
\prod_{\substack{p\mid m\\p\nmid n}}(1-p^j)
\,M_j(\nu_n).
}
\tag{15}
\]

In particular, when `(m,n)=1`, the multiplicative coefficient is

\[
m^{-j}\prod_{p\mid m}(1-p^j)
=(\mu * \operatorname{id}_{-j})(m),
\tag{16}
\]

the standard generalized Jordan-totient coefficient. Its Dirichlet series is classically

\[
\sum_{m\ge1}\frac{(\mu*\operatorname{id}_{-j})(m)}{m^s}
=
\frac{\zeta(s+j)}{\zeta(s)}.
\tag{17}
\]

Keeping the finitely many primes already present in `n` changes only their local factors. Thus for `Re(s)>1`,

\[
\boxed{
\sum_{m\ge1}\frac{M_j(\nu_{nm})}{m^s}
=
M_j(\nu_n)
\frac{\zeta(s+j)}{\zeta(s)}
\prod_{p\mid n}(1-p^{-s})^{-1}.
}
\tag{18}
\]

For `j=0`, the zeta ratio cancels identically and (18) reduces to the finite-prime Euler product

\[
M_0(\nu_n)\prod_{p\mid n}(1-p^{-s})^{-1}.
\tag{19}
\]

For `j>0`, the only new analytic factor is the shifted classical ratio in (18).

## 5. The full Mellin-character readout is the old radial-flux carrier times the same universal ratio

The shell-2 coordinate change can be identified exactly with the radial variable used in PC-179. PC-405 defines

\[
\mu_n=\tau_*(dX_n),
\qquad
\tau(r)=\log(1+r),
\qquad
X_n(r)=\log\Phi_n(r),
\]

and `chi(t)=-log(e^t-1)`. Since

\[
\chi(\tau(r))=-\log r,
\]

pushing `dX_n` through `chi\circ tau` and substituting `r=e^{-x}` gives, for every compactly supported continuous test function,

\[
\int f(x)\,d\nu_n(x)
=
\int_0^1 f(-\log r)\,dX_n(r)
=
\int_0^\infty f(x)\,\rho_n(x)\,dx,
\]

where `rho_n(x)=-d/dx log Phi_n(e^{-x})` is exactly the signed radial flux of PC-179. Hence

\[
\boxed{d\nu_n(x)=\rho_n(x)\,dx.}
\tag{20}
\]

This identifies two apparently different Prime-Circle carriers: the measure whose shell-2 moments drive PC-399--PC-406 and the radial-flux profile already Mellinized in PC-179 are the same object after the canonical refinement coordinate change.

For a complex dilation character `z`, put

\[
M_z(\nu):=\int_0^\infty x^z\,d\nu(x).
\]

Because `rho_n` is bounded at `0+` and decays exponentially at infinity, `M_z(\nu_n)` is holomorphic for `Re(z)>-1`. Substituting `s=z+1` into the exact PC-179 Mellin formula gives

\[
\boxed{
M_z(\nu_n)
=-\Gamma(z+1)\zeta(z+1)n^{-z}
\prod_{p\mid n}(1-p^z),
\qquad \Re(z)>-1,
}
\tag{21}
\]

with removable cancellations interpreted by limits, in particular at `z=0`. Dilation is diagonal on these characters,

\[
M_z(S_a\nu)=a^{-z}M_z(\nu),
\]

so (6)--(7) immediately sharpen (15) to

\[
\boxed{
M_z(\nu_{nm})
=
m^{-z}
\prod_{\substack{p\mid m\\p\nmid n}}(1-p^z)
\,M_z(\nu_n).
}
\tag{22}
\]

Now form the genuine two-variable Mellin--conductor transform

\[
\mathcal Z_n(s,z)
:=
\sum_{m\ge1}\frac{M_z(\nu_{nm})}{m^s}.
\tag{23}
\]

The local Euler factors converge absolutely in the natural domain

\[
\Re(z)>-1,
\qquad
\Re(s)>1,
\qquad
\Re(s+z)>1.
\]

For `p\nmid n` the local factor is

\[
1+\sum_{k\ge1}p^{-k(s+z)}(1-p^z)
=
\frac{1-p^{-s}}{1-p^{-(s+z)}},
\]

while for `p\mid n` it is `(1-p^{-(s+z)})^{-1}`. Therefore

\[
\boxed{
\mathcal Z_n(s,z)
=
M_z(\nu_n)
\frac{\zeta(s+z)}{\zeta(s)}
\prod_{p\mid n}(1-p^{-s})^{-1}.
}
\tag{24}
\]

Combining (21) and (24) gives the complete scalar factorization

\[
\boxed{
\mathcal Z_n(s,z)
=
-\Gamma(z+1)\zeta(z+1)
\frac{\zeta(s+z)}{\zeta(s)}
 n^{-z}
\prod_{p\mid n}\frac{1-p^z}{1-p^{-s}}.
}
\tag{25}
\]

Thus passing from integer moments to the full complex Mellin spectrum does not expose a hidden interaction. It separates even more cleanly: the cyclotomic source contributes the one-shell PC-179 factor, while the entire descendant tree contributes the universal Jordan/zeta ratio already present in PC-406. For the smooth exponentially decaying profiles here, Mellin characters are the natural scalar diagonalization of dilation, so this closes the obvious noninteger-Mellin escape rather than merely checking more polynomial moments.

## 6. The matched arbitrary-measure control survives the full Mellin sum

PC-405 already showed that the finite descendant architecture works for an arbitrary finite signed base measure when synthetic descendants are generated by the same `T_p` rules. The infinite-level series does not break that control.

Choose any finite signed measure `nu` for which `M_z(nu)` exists in a common vertical strip and generate synthetic descendants using exactly the operators `B_{n,m}` of (7). The derivation of (22)--(24) is unchanged, with `M_z(nu_n)` replaced by `M_z(nu)`. In particular, the factor

\[
\frac{\zeta(s+z)}{\zeta(s)}
\prod_{p\mid n}(1-p^{-s})^{-1}
\]

is **independent of the cyclotomic source measure**.

Thus neither the operator Euler product nor its full Mellin symbol distinguishes the actual Prime-Circle shell from the matched nonarithmetic control. The arithmetic source contributes only its base Mellin transform; for the genuine cyclotomic source that transform is already exactly the classical PC-179 factor (21).

## 7. Why the zeta zeros here are not a new RH mechanism

There are four separate obstructions.

First, the operator series (8) is obtained canonically only in `Re(s)>1`. The full scalar Euler product (24) additionally has the natural absolute-convergence condition `Re(s+z)>1`. In that joint domain both descendant factors `zeta(s)` and `zeta(s+z)` are zero-free. The only nontrivial zeta zeros accessible without continuing the descendant variables are those of the base factor `zeta(z+1)` in (21), and those are exactly the one-shell zeros already classicalized in PC-179.

Second, after meromorphic continuation the two-variable divisor consists only of inherited zeta hyperplanes `z+1=rho`, `s+z=rho`, and `s=rho`, together with elementary gamma and finite Euler factors. No new nonlinear zero condition, spectral determinant, positivity boundary, or resonance equation is generated by coupling the shell to its descendants.

Third, even the tempting functional-equation pairing is not source-forced. Pairing `zeta(z+1)` with its reflected argument would require

\[
s+z=1-(z+1)=-z,
\qquad\text{hence}\qquad s=-2z.
\]

But this diagonal has **no intersection with the native domain** `Re(z)>-1`, `Re(s)>1`, `Re(s+z)>1`: the last condition would require `Re(z)<-1`. The relation can only be imposed after analytic continuation as an external constraint between two independent transform variables. It therefore inserts the classical functional equation geometry rather than deriving it from Prime Circle.

Fourth, no source-derived principle in the descendant semigroup singles out a half-density normalization or creates an intrinsic `s <-> 1-s` involution. Treating the continued factors in (25) as the desired spectral object would wrap known zeta functions around the shell data rather than explain their critical-line geometry.

This is the same classicalization warning encountered in PC-055 and PC-378, but here it closes a distinct live regime: the infinite conductor sum of the shell-2 descendant measures left outside the finite theorem of PC-405, including its full scalar dilation spectrum rather than only integer moments.

## 8. Prior-art and novelty audit

The arithmetic identity is classical. For the Jordan totient,

\[
J_k(m)=m^k\prod_{p\mid m}(1-p^{-k})=(\mu*\operatorname{id}_k)(m),
\]

and the standard Dirichlet generating function is

\[
\sum_{m\ge1}\frac{J_k(m)}{m^s}
=\frac{\zeta(s-k)}{\zeta(s)}.
\tag{26}
\]

Equation (17) is the same identity with `k=-j`, and equations (22)--(24) are its elementary complex-parameter Euler-product continuation in the domain of absolute convergence. Likewise, using Mellin characters to diagonalize ordinary dilation is classical harmonic analysis on the multiplicative half-line. PC-020 already records Jordan-totient data as classical Prime-Circle output in a different local-jet context. PC-055 classifies the corresponding zeta/Moebius thresholds for an infinite divisor transform, while PC-378 shows that an Euler-product completion of the Chebyshev refinement shifts is likewise just a classical zeta divisor multiplier. Most importantly, PC-179 already proves the one-shell factor (21). External checks against standard Jordan-totient/Dirichlet-series references and standard Mellin-dilation theory therefore leave no plausible historical novelty claim for any factor in (25).

The durable project-local delta is structural rather than a new number-theory identity. PC-405's shell-2 measure, after its own canonical dilation conjugacy, is **exactly** the PC-179 radial-flux measure, and the full two-variable transform factors into that old one-shell carrier times the universal PC-406 descendant multiplier. This identifies and closes what otherwise looks like a separate complex-Mellin/refinement route.

No novelty is claimed for the classical factors themselves.

## 9. Falsification checks and surviving frontier

The derivation has exact local tests. For a fresh prime `p\nmid n`, (22) predicts

\[
M_z(\nu_{np})=(p^{-z}-1)M_z(\nu_n),
\tag{27}
\]

whereas for a repeated prime `p\mid n`,

\[
M_z(\nu_{np^k})=p^{-kz}M_z(\nu_n).
\tag{28}
\]

The `z=j` specializations reproduce the previous polynomial identities exactly. Independently, direct substitution of `chi(tau(r))=-log r` must reproduce the PC-179 radial density (20); failure of that pushforward identity would invalidate the strengthened conclusion. Expanding the first few Euler factors in (24) gives a coefficient-by-coefficient check of (22).

The result does **not** cover an arbitrary nonlinear functional of the full descendant family, a source-derived interaction that couples two levels before separate pushforward reduction, angular/chord/old-new data joined to radial refinement, a non-functorial product law, or an infinite-level renormalization whose definition is not the ordinary conductor Dirichlet sum (8). Those remain legitimate only if they can be shown to introduce information not already determined by the one-base-measure dilation system.

## Consequence

The simplest infinite-level escape from PC-405 is closed more strongly than the polynomial-moment calculation alone showed. Passing from finitely many shell-2 descendants to the complete conductor-Dirichlet generating family does not generate a new zeta mechanism, and allowing the full complex Mellin spectrum does not repair it: the two-variable transform is exactly the old PC-179 radial-flux Mellin factor times the classical generalized-Jordan ratio `zeta(s+z)/zeta(s)`, with only finite Euler corrections from primes already dividing the parent shell. A further Prime-Circle candidate must change the information law rather than merely respectralize or sum the same descendant dilation semigroup.