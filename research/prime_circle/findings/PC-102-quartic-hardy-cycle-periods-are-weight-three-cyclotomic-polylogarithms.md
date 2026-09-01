# PC-102 — quartic Hardy cycle periods reduce to weight-three cyclotomic polylogarithms

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the first even Hardy cycle left open by PC-101. For every cyclically separated quartic root word, the ordinary Hardy trace reduces exactly to a finite `Q(mu_N)`-linear combination of weight-three cyclotomic hyperlogarithm / multiple-polylogarithm values, with `N` any common cyclotomic level of the four roots. Hence the quartic critical cone retains information beyond pairwise resultants, but it does **not** define a new period class outside classical cyclotomic multiple-polylogarithm technology.

This closes the `k=4` period-class boundary left explicit by PC-100 and PC-101. It does **not** prove the same reduction for all cycle lengths `k>=5`, repeated-shell words that fail cyclic root separation, infinite-shell Hardy generating constructions, or global uniformization/monodromy.

## 1. Start from the exact quartic Hardy cube period

For roots of unity `a,b,c,d` satisfying the cyclic separation conditions

\[
ab\ne1,\qquad bc\ne1,\qquad cd\ne1,\qquad da\ne1,
\]

write

\[
\mathcal P_4(a,b,c,d)
=\operatorname{Tr}(\mathcal H_a\mathcal H_b\mathcal H_c\mathcal H_d).
\]

PC-082 and PC-086 give the ordinary boundary trace as the absolutely regular cube integral

\[
\boxed{
\mathcal P_4(a,b,c,d)
=abcd\int_{[0,1]^4}
\frac{dx_1\,dx_2\,dx_3\,dx_4}
{(1-abx_1x_2)(1-bcx_2x_3)(1-cdx_3x_4)(1-dax_4x_1)}.
}
\]

The four adjacent products are nontrivial roots of unity, so none of the four denominators vanishes on the real cube. No new regularization is being introduced here.

For complex `U,V` on the radial branch define

\[
D(U,V)
:=\int_0^1\frac{ds}{(1-Us)(1-Vs)}
=\frac{\Log(1-V)-\Log(1-U)}{U-V},
\]

with the diagonal value understood by continuity. Integrating the opposite variables `x_1` and `x_3` gives the exact two-dimensional reduction

\[
\boxed{
\mathcal P_4(a,b,c,d)
=abcd\int_0^1\!\int_0^1
D(da\,y,ab\,x)\,D(bc\,x,cd\,y)\,dx\,dy.
}
\]

Thus the first even critical cone can already be studied in two variables without rearranging its conditionally convergent lattice presentation.

## 2. Splitting the square along its diagonal gives one universal cubic building block

Introduce

\[
S(X,Y)
:=\int_0^1\frac{\Log(1-Xx)\Log(1-Yx)}{x}\,dx
=\sum_{m,n\ge1}\frac{X^mY^n}{mn(m+n)}
\]

where the series identity is first read in the open unit bidisk and continued on the same radial branches. This is the colored Tornheim building block of total weight three.

Split the `(x,y)` square into `y=xt`, `0<=x,t<=1`, and the transposed triangle. Put

\[
w=\frac db
\]

and

\[
\boxed{
\begin{aligned}
J_{a,b,c,d}(t)
={}&S(ad\,t,cd\,t)-S(ad\,t,bc)\\
&-S(ab,cd\,t)+S(ab,bc).
\end{aligned}
}
\]

A direct substitution into the two `D` factors gives the first triangular contribution

\[
\boxed{
R(a,b,c,d)
=\frac db\int_0^1
\frac{J_{a,b,c,d}(t)}{(1-(d/b)t)^2}\,dt.
}
\]

The other triangle is the same expression with the two opposite labels interchanged, hence

\[
\boxed{
\mathcal P_4(a,b,c,d)
=R(a,b,c,d)+R(a,d,c,b).
}
\]

This identity is exact. It is also the analytic counterpart of PC-101's even-cycle incidence fiber: the rank-one loss in the denominator-index map becomes a single remaining projective parameter `t`.

## 3. The apparent extra integration does not raise the transcendental weight

Since

\[
\frac{d}{dt}\frac1{1-wt}=\frac{w}{(1-wt)^2},
\]

integration by parts gives

\[
\boxed{
R(a,b,c,d)
=
\left[\frac{J_{a,b,c,d}(t)}{1-wt}\right]_{0}^{1}
-
\int_0^1\frac{J'_{a,b,c,d}(t)}{1-wt}\,dt.
}
\]

The key point is that `J` has weight three whereas `J'` has weight two. The double pole forced by the even-cycle fiber is therefore removed by one derivative before the final `dlog` integration. The quartic trace stays at weight three rather than acquiring weight four.

If `b=d`, the displayed boundary quotient has an apparent `0/0` at `t=1`, but this is removable. In that case both logarithmic differences that produced `J` vanish linearly as `t->1`, so

\[
J(t)=O((1-t)^2),
\qquad
\frac{J(t)}{1-t}\longrightarrow0,
\]

and `J'(t)/(1-t)` remains integrable. Other coincident cyclotomic letters below are handled by the same confluent-limit convention. The original two-dimensional integral supplies the canonical regular value, so no singular branch is created by the reduction.

## 4. Every term is a cyclotomic hyperlogarithm of weight three

Use the standard hyperlogarithm notation

\[
G(q_1,\ldots,q_r;z)
=\int_0^z\frac{du}{u-q_1}G(q_2,\ldots,q_r;u),
\qquad G(;z)=1.
\]

First, for fixed `X,Y`, the shuffle product gives

\[
\boxed{
S(X,Y)
=G(0,X^{-1},Y^{-1};1)
 +G(0,Y^{-1},X^{-1};1).
}
\]

Thus every constant `S` in the boundary term is already a weight-three multiple-polylogarithm value.

Second, if both arguments scale with `t`, then

\[
S(At,Bt)
=\int_0^t
\frac{\Log(1-Au)\Log(1-Bu)}u\,du,
\]

which is a weight-three hyperlogarithm in `t` with letters among `0,A^{-1},B^{-1}`.

The only less immediate case is a mixed term such as `S(At,B)`. Differentiating under the integral gives

\[
\frac{d}{dt}S(At,B)
=-A\int_0^1\frac{\Log(1-Bx)}{1-Atx}\,dx.
\]

Writing `C=At`, the inner integral has the exact dilogarithmic primitive

\[
\boxed{
\begin{aligned}
\int_0^1\frac{\Log(1-Bx)}{1-Cx}\,dx
=\frac1C\Bigg[&
\operatorname{Li}_2\!\left(\frac C{C-B}\right)\\
&-\Log(1-B)\Log\!\left(\frac{B(1-C)}{B-C}\right)\\
&-\operatorname{Li}_2\!\left(\frac{C(B-1)}{B-C}\right)
\Bigg].
\end{aligned}
}
\]

It is enough to inspect the rational arguments: their zeros, poles, and inverse images of `1` occur only at

\[
C\in\{0,B,1,\infty\},
\]

so as functions of `t` the singular alphabet is contained in

\[
\{0,B/A,1/A,\infty\}.
\]

For the present `A,B`, all nonzero finite letters are products or ratios of `a,b,c,d`, hence roots of unity. Therefore each mixed derivative is a weight-two cyclotomic hyperlogarithmic differential. The last factor

\[
\frac{dt}{1-wt}
\]

adds only the cyclotomic letter `w^{-1}=b/d`. Consequently the final integral has weight three.

Let

\[
N=\operatorname{lcm}
(\operatorname{ord}(a),\operatorname{ord}(b),
 \operatorname{ord}(c),\operatorname{ord}(d)).
\]

All letters belong to `mu_N`, and algebraic prefactors such as `(1-w)^{-1}` lie in `Q(mu_N)`. We therefore obtain the exact period classification

\[
\boxed{
\mathcal P_4(a,b,c,d)
\in \mathbb Q(\mu_N)\cdot \operatorname{MPV}_3(N),
}
\]

where `MPV_3(N)` denotes the `Q`-span of weight-three multiple-polylogarithm values with cyclotomic letters of level dividing `N`. Coincident letters are understood by the finite confluent limits inherited from the regular cube integral.

## 5. Primitive-shell traces inherit the same classicalization

Let `n_1,n_2,n_3,n_4>1` be cyclically adjacent distinct shell orders. Rootwise cyclic separation is automatic: if `alpha_i alpha_{i+1}=1`, then the two roots have the same exact order. Since

\[
\Gamma_n=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha,
\]

the four minus signs cancel and

\[
\boxed{
\operatorname{Tr}
(\Gamma_{n_1}\Gamma_{n_2}\Gamma_{n_3}\Gamma_{n_4})
=
\sum_{\alpha_i\in P_{n_i}^*}
\mathcal P_4(\alpha_1,\alpha_2,\alpha_3,\alpha_4).
}
\]

Hence the completed quartic shell trace lies in the finite sum of the same weight-three cyclotomic period spaces at level dividing `lcm(n_1,n_2,n_3,n_4)`.

This does not say the quartic trace is determined by pairwise resultants. PC-082 already established that the higher trace-class Hardy sector carries information beyond pairwise mixed traces. The statement here is about the **period class** of the first even cyclic trace.

## 6. Matched controls and stress tests

Several checks sharply delimit the claim.

1. **Direct integral control.** Integrating `x_1,x_3` in the PC-082 cube must reproduce the two-`D` square integral. Any extra factor or sign would falsify the reduction.
2. **Triangular control.** On `y=xt`, the Jacobian and two divided logarithmic differences must give exactly `(d/b) J(t)/(1-(d/b)t)^2`; the transposed triangle must equal `R(a,d,c,b)`.
3. **Confluent control.** At `b=d`, `J(t)/(1-t)` must have a finite endpoint limit and `J'(t)/(1-t)` must remain integrable. A genuine pole would invalidate the integration-by-parts step.
4. **Hyperlog alphabet control.** For every mixed `S(At,B)`, the only possible finite singular letters in `t` are `0`, `B/A`, and `1/A`. A non-cyclotomic letter would refute the stated period class.
5. **Arbitrary-phase control.** The same two-dimensional and triangular reductions hold for generic unit phases satisfying adjacent separation. What is special to Prime Circle is that the resulting alphabet is cyclotomic; the hyperlogarithmic reduction itself is not prime-specific.
6. **Numerical controls.** Direct four-index radial sums, the two-dimensional integral, and the two triangular formulas agree at generic damped and boundary test points to high precision. These checks support signs and normalizations only; the evidence is the exact derivation above.

## 7. Prior-art and novelty audit

The reduction lands in established period technology rather than a new transcendental class.

- A. B. Goncharov, **Multiple polylogarithms, cyclotomy and modular complexes**, *Mathematical Research Letters* 5 (1998), 497–516, DOI `10.4310/MRL.1998.v5.n4.a7`, develops the iterated-integral continuation and the special-value theory of multiple polylogarithms at roots of unity.
- Jianqiang Zhao, **A Note on Colored Tornheim's Double Series**, *Integers* 10:6 (2010), 879–882, DOI `10.1515/integ.2010.059`, gives an explicit reduction of colored double Tornheim series to double polylogarithm values at roots of unity. The function `S(X,Y)` above is precisely the weight-three `p=q=r=1` colored double-Tornheim building block.
- Erik Panzer, **Algorithms for the symbolic integration of hyperlogarithms with applications to Feynman integrals**, *Computer Physics Communications* 188 (2015), 148–166, DOI `10.1016/j.cpc.2014.10.019`, supplies the standard closure framework for integrating rational functions times hyperlogarithms and for tracking the singular alphabet.
- Terasoma and Guo--Paycha--Zhang, already recorded for PC-082, remain the broader conical-zeta boundary. Their general results did not by themselves identify the critical Hardy-selected quartic boundary value; the explicit reduction above removes that gap specifically for `k=4`.

No historical novelty is claimed for hyperlogarithmic integration, colored Tornheim reductions, or cyclotomic multiple polylogarithms. The Prime-Circle-specific durable content is the exact reduction of the PC-101 quartic Hardy invariant and the resulting closure of its previously open period-class boundary.

## 8. Consequence for the RH program

The first even higher Hardy cycle now follows the exact chain

\[
\boxed{
\text{quartic Prime-Circle Hardy trace}
\longrightarrow
\text{PC-101 critical even-cycle fiber}
\longrightarrow
\text{two triangular hyperlog integrals}
\longrightarrow
\text{weight-3 cyclotomic MPVs}.
}
\]

Thus the quartic trace can carry relational information not visible in pairwise resultants while still remaining a **static classical cyclotomic period**. It supplies no geometry-forced free complex spectral parameter, gamma factor, `s\leftrightarrow1-s` symmetry, positivity criterion, or Riemann-zero divisor. Treating `k=4` by itself as a new RH mechanism is therefore not justified.

The surviving Hardy-period question is narrower: determine whether `k>=5` cyclic traces admit analogous finite hyperlogarithmic reductions, whether repeated-shell words outside cyclic root separation force a different analytic class, or whether an intrinsically generated infinite-shell/global Hardy organization introduces genuinely new functional rather than static-period structure. Those questions remain outside the present theorem.
