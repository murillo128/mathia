# PC-406 — shell-2 descendant Dirichlet sum is a Jordan-zeta ratio

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most direct infinite-level analytic resummation left open by PC-405. After conjugating the canonical shell-2 child maps to ordinary dilations, every Mellin moment of the complete multiplicative descendant tree has an exact Dirichlet generating function equal to a finite Euler correction times `zeta(s+j)/zeta(s)`. Equivalently, the fresh-prime coefficients are the classical Dirichlet convolution `mu * id_{-j}` (a generalized Jordan-totient coefficient). Thus the natural infinite-level Dirichlet completion does not create a new analytic carrier: it reintroduces zeta through a standard Euler-product identity, and its nontrivial zeros/poles occur only after scalarization and analytic continuation beyond the operator series' native convergence half-plane.

This does **not** rule out every infinite-level or renormalized limit of the shell-2 refinement system. It closes the canonical conductor-Dirichlet resummation of all descendants, including its operator-valued Euler product and all polynomial Mellin moments.

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

## 5. The matched arbitrary-measure control survives the infinite sum

PC-405 already showed that the finite descendant architecture works for an arbitrary finite signed base measure when synthetic descendants are generated by the same `T_p` rules. The infinite-level series does not break that control.

Indeed, choose any finite signed measure `nu` for which the moment `M_j(nu)` exists and generate synthetic descendants using exactly the operators `B_{n,m}` of (7). Equations (8)--(18) are unchanged, with `M_j(nu_n)` replaced by `M_j(nu)`. In particular, the zeta ratio is **independent of the cyclotomic source measure**.

Thus neither the operator Euler product nor its moment symbol distinguishes the actual Prime-Circle shell from the matched nonarithmetic control. The arithmetic source contributes the base moment; the `zeta(s+j)/zeta(s)` carrier is forced by the universal dilation/difference semigroup and ordinary Dirichlet summation.

## 6. Why the zeta zeros here are not a new RH mechanism

There are three separate obstructions.

First, the operator series (8) is obtained canonically only in `Re(s)>1`. In that half-plane the denominator `zeta(s)` has no zeros, and for `j>=0` the numerator `zeta(s+j)` introduces no nontrivial zero phenomenon relevant to RH. The familiar nontrivial zeros appear only after the scalar identity (18) is meromorphically continued beyond the domain in which the operator Euler product was derived.

Second, the divisor in the continuation is exactly the classical one already visible in (17). A zero or pole of the continued scalar ratio is inherited from zeta; it is not produced as a spectrum, determinant, resonance, or positivity boundary of a new Prime-Circle operator.

Third, the moment order `j` merely translates the numerator to `zeta(s+j)`. No source-derived principle here singles out a half-density normalization, supplies the archimedean gamma factor, or creates an `s <-> 1-s` symmetry. Treating the continued ratio as the desired spectral object would therefore wrap the known zeta function around the descendant data rather than derive its critical-line geometry from the circle construction.

This is the same classicalization warning encountered in PC-055 and PC-378, but here it closes a distinct live regime: the infinite conductor sum of the shell-2 descendant measures left outside the finite theorem of PC-405.

## 7. Prior-art and novelty audit

The arithmetic identity is classical. For the Jordan totient,

\[
J_k(m)=m^k\prod_{p\mid m}(1-p^{-k})=(\mu*\operatorname{id}_k)(m),
\]

and the standard Dirichlet generating function is

\[
\sum_{m\ge1}\frac{J_k(m)}{m^s}
=\frac{\zeta(s-k)}{\zeta(s)}.
\tag{20}
\]

Equation (17) is the same identity with `k=-j`. PC-020 already records Jordan-totient data as classical Prime-Circle output in a different local-jet context. PC-055 classifies the corresponding zeta/Möbius thresholds for an infinite divisor transform, while PC-378 shows that an Euler-product completion of the Chebyshev refinement shifts is likewise just a classical zeta divisor multiplier. External checks against standard Dirichlet-series/Jordan-totient references and the Bost--Connes semigroup literature confirm that no historical novelty should be assigned to the zeta ratio or the dilation Euler-product mechanism.

The durable project-local delta is narrower: PC-405 explicitly left genuinely infinite-level or renormalized analytic limits outside its finite one-measure theorem. Equations (11) and (18) settle the most direct such continuation. Summing **all multiplicative descendants by conductor** still yields a universal one-measure dilation operator, and every canonical polynomial Mellin readout classicalizes to a Jordan/zeta ratio.

No novelty is claimed for the classical identity itself.

## 8. Falsification checks and surviving frontier

The derivation has exact local tests. For a fresh prime `p\nmid n`, (6) predicts

\[
M_j(\nu_{np})=(p^{-j}-1)M_j(\nu_n),
\tag{21}
\]

whereas for a repeated prime `p\mid n`,

\[
M_j(\nu_{np^k})=p^{-kj}M_j(\nu_n).
\tag{22}
\]

Any direct cyclotomic shell-2 computation violating either identity falsifies the reduction. Expanding the first few Euler factors in (18) gives an independent coefficient-by-coefficient check of (15).

The result does **not** cover an arbitrary nonlinear functional of the full descendant family, a source-derived interaction that couples two levels before separate pushforward reduction, angular/chord/old-new data joined to radial refinement, a non-functorial product law, or an infinite-level renormalization whose definition is not the ordinary conductor Dirichlet sum (8). Those remain legitimate only if they can be shown to introduce information not already determined by the one-base-measure dilation system.

## Consequence

The simplest infinite-level escape from PC-405 is closed. Passing from finitely many shell-2 descendants to the complete conductor-Dirichlet generating family does not generate a new zeta mechanism; it yields the classical generalized-Jordan identity `zeta(s+j)/zeta(s)` with only finite Euler corrections from primes already dividing the parent shell. A further Prime-Circle candidate must change the information law rather than merely sum the same descendant semigroup over all conductors.
