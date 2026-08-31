# PC-082 — higher Hardy cyclic traces escape pairwise resultants into critical cyclotomic cone periods

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CANDIDATE-NEW-STRUCTURE` + `PRIOR-ART-REDIRECTION`. The cyclic-trace formulas and the exact control showing that higher mixed traces contain information beyond pairwise cyclotomic resultants are derived here. Rational/conical zeta values, cyclotomic multiple zeta values, and renormalized conical-zeta constructions are established neighboring theories. No theorem-level historical novelty is claimed for the surrounding cone-period technology, and no reduction of the critical Prime-Circle traces to known cyclotomic multiple zeta values is asserted.

PC-080 showed that for distinct primitive shells the first mixed Hardy trace is exactly the classical cyclotomic resultant,

\[
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log|\operatorname{Res}(\Phi_m,\Phi_n)|,
\qquad m\neq n,
\]

while PC-081 showed that every finite mixed algebraic word is trace class and therefore invisible to the joint essential spectrum. The surviving question is whether the **relative trace-class sector** contains anything beyond the pairwise resultant graph.

It does. For cyclically separated shell labels, every higher cyclic trace has an exact root-channel representation as a finite sum of cyclotomic periods on a rational cycle cone. At order three this becomes a triangle-cone Ramanujan sum. Moreover, an exact control shows that these higher traces do not collapse to the pairwise resultant values: `Tr(Gamma_2 Gamma_3)=0` but

\[
\boxed{
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)>0.
}
\]

Thus PC-080's resultant is only the first mixed trace, not a complete invariant of the trace-class Hardy interaction. The positive result is nevertheless bounded sharply by prior art: the resulting sums sit at the **critical, conditionally convergent boundary** of classical cyclotomic conical-zeta constructions. Fixed finite cyclic traces supply canonical arithmetic periods, but not yet an RH spectral parameter, functional equation, gamma factor, or critical-line mechanism.

## 1. Primitive-root Hilbert channels

Retain the PC-080 channel

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad j,k\ge0,
\qquad |\alpha|=1,
\]

so that

\[
\boxed{
\Gamma_n
=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
}
\]

For roots `alpha_1,...,alpha_k`, write cyclic indices `alpha_{k+1}=alpha_1` and assume

\[
\boxed{
\alpha_i\alpha_{i+1}\neq1
\quad\text{for every }i.
}
\]

This condition is automatic when the corresponding shell orders are cyclically adjacent and distinct, because `alpha_i alpha_{i+1}=1` would force the two roots to have the same exact order. Under this separation condition the product is trace class. More generally, for completed shell operators this already follows from PC-080 whenever the word contains an adjacent pair of distinct shell labels, because `S_1` is a two-sided ideal.

## 2. Exact cyclic root-channel trace as a cube period

Expanding the diagonal of a `k`-fold channel product gives formally

\[
\operatorname{Tr}(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k})
=
\sum_{j_1,\ldots,j_k\ge0}
\prod_{i=1}^k
\frac{\alpha_i^{j_i+j_{i+1}+1}}
{j_i+j_{i+1}+1},
\qquad j_{k+1}=j_1.
\]

Use the radial/Abel convention of PC-080. For `0<r<1`, put

\[
(\mathcal H_{\alpha,r})_{jk}
=\frac{(r\alpha)^{j+k+1}}{j+k+1}.
\]

Now all sums are absolute. Using

\[
\frac1{j_i+j_{i+1}+1}
=\int_0^1x_i^{j_i+j_{i+1}}\,dx_i
\]

and summing each `j_i` geometrically gives

\[
\operatorname{Tr}
(\mathcal H_{\alpha_1,r}\cdots\mathcal H_{\alpha_k,r})
=
 r^k\!\left(\prod_{i=1}^k\alpha_i\right)
\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-r^2\alpha_i\alpha_{i+1}x_ix_{i+1}}.
\]

Because every `alpha_i alpha_{i+1}` is a nontrivial root of unity, the limiting denominators stay nonzero on the compact cube. Dominated convergence therefore gives the scalar Abel limit of the displayed radial traces.

It remains to identify that scalar limit with the **ordinary trace of the boundary product**. Let

\[
R_r=\operatorname{diag}(1,r,r^2,\ldots).
\]

Then `R_r -> I` strongly, `||R_r|| <= 1`, and

\[
\mathcal H_{\alpha,r}=rR_r\mathcal H_\alpha R_r,
\]

so the radial channels converge strong-* and remain uniformly bounded. For a separated adjacent pair `gamma=alpha beta != 1`, use the PC-080 factorization of the pair through an integral operator on `L^2(0,1)` whose radial kernel is

\[
k_{\gamma,r}(x,y)=\frac1{1-\gamma r^2xy},
\qquad
k_\gamma(x,y)=\frac1{1-\gamma xy}.
\]

Separation keeps the denominators uniformly away from zero on `[0,1]^2`, hence `k_{gamma,r} -> k_gamma` in every `C^q` norm. For an integer `q>1`, the difference operator maps `L^2(0,1)` to `H^q(0,1)` with norm tending to zero, and the embedding `H^q(0,1) -> L^2(0,1)` is trace class. Therefore the separated radial pair converges in trace norm:

\[
\boxed{
\|\mathcal H_{\alpha,r}\mathcal H_{\beta,r}
-\mathcal H_\alpha\mathcal H_\beta\|_{\mathcal S_1}
\longrightarrow0.
}
\]

For a cyclically separated word choose one adjacent separated pair as a trace-class core and write `P_r=A_rT_rB_r`. The outer factors are uniformly bounded and converge strong-* to `A,B`, while `T_r -> T` in `S_1`. Finite-rank approximation of the fixed trace-class core gives

\[
\boxed{
\|A_rT_rB_r-ATB\|_{\mathcal S_1}\longrightarrow0.
}
\]

Consequently `Tr(P_r) -> Tr(P)`. Combining this trace-continuity bridge with the radial cube integral and dominated convergence proves the ordinary boundary-trace identity

\[
\boxed{
\mathcal P(\alpha_1,\ldots,\alpha_k)
:=
\operatorname{Tr}
(\mathcal H_{\alpha_1}\cdots\mathcal H_{\alpha_k})
=
\left(\prod_{i=1}^k\alpha_i\right)
\int_{[0,1]^k}
\prod_{i=1}^k
\frac{dx_1\cdots dx_k}
{1-\alpha_i\alpha_{i+1}x_ix_{i+1}}.
}
\]

The right-hand side is a finite cyclotomic period forced directly by the primitive-root geometry and the Hardy interior/exterior split. No external spectral parameter or weighting has been inserted.

For cyclically separated shell orders `n_1,...,n_k`, finite summation over primitive roots gives

\[
\boxed{
\operatorname{Tr}(\Gamma_{n_1}\cdots\Gamma_{n_k})
=(-1)^k
\sum_{\alpha_i\in P_{n_i}^*}
\mathcal P(\alpha_1,\ldots,\alpha_k).
}
\]

Thus the entire finite higher cyclic-trace family is reduced to an explicit finite set of root-of-unity cube periods.

## 3. Order two recovers PC-080 exactly

For `k=2`, put `delta=alpha beta !=1`. Then

\[
\mathcal P(\alpha,\beta)
=\delta
\int_0^1\int_0^1
\frac{dx\,dy}{(1-\delta xy)^2}.
\]

Integrating one variable gives

\[
\boxed{
\mathcal P(\alpha,\beta)
=-\operatorname{Log}(1-\alpha\beta),
}
\]

with the radial boundary branch. Summing complete primitive shells and taking the real trace is exactly the PC-080 identity

\[
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\]

The cycle-period formula is therefore a genuine extension of the same operator invariant rather than an unrelated construction.

## 4. Order three is a triangle-cone Ramanujan period

For three pairwise distinct shell orders `a,b,c`, the trace is

\[
\boxed{
\operatorname{Tr}(\Gamma_a\Gamma_b\Gamma_c)
=-
\sum_{i,j,k\ge0}^{\mathrm{Abel}}
\frac{
 c_a(i+j+1)c_b(j+k+1)c_c(k+i+1)
}
{(i+j+1)(j+k+1)(k+i+1)}.
}
\]

Make the linear change

\[
r=i+j+1,\qquad s=j+k+1,\qquad t=k+i+1.
\]

Its inverse is

\[
i=\frac{r+t-s-1}{2},\qquad
j=\frac{r+s-t-1}{2},\qquad
k=\frac{s+t-r-1}{2}.
\]

Hence nonnegative integer triples `(i,j,k)` correspond bijectively to positive integer triples `(r,s,t)` satisfying

\[
\boxed{
 r+s>t,\qquad s+t>r,\qquad t+r>s,\qquad r+s+t\equiv1\pmod2.
}
\]

Therefore

\[
\boxed{
\operatorname{Tr}(\Gamma_a\Gamma_b\Gamma_c)
=-
\sum_{\substack{r,s,t\ge1\\
 r+s>t,\ s+t>r,\ t+r>s\\
 r+s+t\ \mathrm{odd}}}^{\mathrm{Abel}}
\frac{c_a(r)c_b(s)c_c(t)}{rst}.
}
\]

The domain is the integral triangle cone, cut by one parity coset, and the coefficients are finite-order root-of-unity characters after expanding each Ramanujan sum. Thus the first genuinely higher mixed trace is a **cyclotomic conical period** intrinsic to Prime Circle.

The superscript `Abel` is essential. The corresponding absolute sum is critical rather than convergent: on a dyadic box where `r,s,t` are all comparable to `R`, there are `asymp R^3` admissible lattice points and the denominator is `asymp R^3`, so each dyadic scale contributes order one before character cancellation. The unweighted absolute series therefore diverges logarithmically. The operator trace supplies the radial boundary prescription canonically.

## 5. Exact control: higher mixed traces contain more than pairwise resultants

For `n=2`,

\[
c_2(m)=(-1)^m,
\qquad
(\Gamma_2)_{jk}=\frac{(-1)^{j+k}}{j+k+1}.
\]

Let `D=diag(1,-1,1,-1,...)`. Then

\[
\boxed{\Gamma_2=DHD,}
\]

where `H` is the positive Hilbert matrix. Hence `Gamma_2` is positive and injective. Injectivity follows from

\[
H_{jk}=\int_0^1x^{j+k}\,dx:
\]

if `Hx=0`, its quadratic form is the integral of the squared analytic generating function, forcing all coefficients of `x` to vanish.

On the other hand `Gamma_3` is a nonzero self-adjoint operator; for example its `(0,0)` entry is `-c_3(1)=1`. The pairwise resultant is trivial,

\[
|\operatorname{Res}(\Phi_2,\Phi_3)|=|\Phi_3(-1)|=1,
\]

so PC-080 gives

\[
\boxed{\operatorname{Tr}(\Gamma_2\Gamma_3)=0.}
\]

But `Gamma_3 Gamma_2` is trace class by PC-080, hence `Gamma_3 Gamma_2 Gamma_3` is trace class, and

\[
\boxed{
\Gamma_3\Gamma_2\Gamma_3
=(\Gamma_2^{1/2}\Gamma_3)^*
 (\Gamma_2^{1/2}\Gamma_3)
\ge0.
}
\]

It is nonzero: if `Gamma_2^{1/2} Gamma_3=0`, injectivity of `Gamma_2^{1/2}` would imply `Gamma_3=0`. A nonzero positive trace-class operator has strictly positive trace. Hence

\[
\boxed{
\operatorname{Tr}(\Gamma_3\Gamma_2\Gamma_3)
=\|\Gamma_2^{1/2}\Gamma_3\|_{\mathcal S_2}^2
>0.
}
\]

This proves, with no numerical input, that the higher relative sector is strictly richer than the pairwise resultant graph. This repeated-shell word is intentionally **not** covered term-by-term by the cyclic root-separation formula of Sections 2--4: the wrap-around `3 -> 3` can contain reciprocal root channels. Its role is only to prove that the complete trace-class shell algebra has higher information after the pairwise traces vanish.

## 6. Prior-art and novelty audit

The closest arithmetic neighborhood is the theory of rational/conical zeta values.

1. Tomohide Terasoma, *Rational convex cones and cyclotomic multiple zeta values* (2004), defines zeta values attached to rational cones, rational linear forms and finite-order characters and proves that the **absolutely convergent** cone values lie in the span of cyclotomic multiple zeta values. This is structurally very close to the triangle/cycle sums above.
2. Li Guo, Sylvie Paycha and Bin Zhang, *Conical zeta values and their double subdivision relations*, *Advances in Mathematics* 252 (2014), 343--381, develop conical zeta values as a geometric generalization of multiple zeta values and relate cone subdivisions to shuffle/quasi-shuffle-type relations.
3. Guo, Paycha and Zhang, *Renormalised conical zeta values* (2016), construct renormalized values at poles using an algebraic Birkhoff-factorization framework. This is direct novelty-warning territory for any claim that a critical cone sum becomes new merely because it needs regularization.

There is nevertheless an exact boundary that must not be blurred. Terasoma's cone-zeta definition and reduction theorem assume absolute convergence, whereas the natural Prime-Circle cycle sums above sit at critical homogeneity and are not absolutely convergent. The present operator construction selects a particular **radial/Abel boundary value**. No theorem cited above has been shown here to identify that operator-selected value with a specific published renormalized conical zeta value or to reduce it to a cyclotomic multiple zeta value.

Accordingly, the justified statement is not “PC-082 discovers new multiple-zeta periods.” It is

\[
\boxed{
\text{higher Hardy cyclic traces canonically land on the critical cyclotomic-cone boundary,}
}
\]

and pairwise resultants do not exhaust that boundary. Determining whether the Abel values are already contained in a standard cyclotomic conical/MZV regularization is a concrete novelty-audit problem, not an assumption.

## 7. RH relevance and obstruction boundary

This result reopens a narrow part of the Hardy branch that PC-080/PC-081 intentionally left alive. The trace-class sector really does retain multidimensional arithmetic information after the pairwise resultant collapses.

But fixed finite cyclic traces are still **static periods**. They provide no canonical free complex parameter `s`, no gamma factor, no `s <-> 1-s` symmetry, no positivity criterion equivalent to RH, and no compact-resolvent spectrum whose eigenvalues could represent zero ordinates. Merely packaging these periods into a determinant or an externally weighted generating function would fail the line's arbitrary-wrapper control.

Thus PC-082 is a positive information-carrier result, not an RH mechanism. A meaningful continuation must establish one of two things:

- **classicalization:** prove that the operator-selected Abel cycle periods coincide with an established cyclotomic conical/MZV regularization, sharply closing this finite-trace escape; or
- **intrinsic extension:** derive from Prime-Circle geometry itself a cross-level/infinite-shell deformation or relative determinant whose parameter and analytic structure are forced before spectral interpretation.

The old/new cotangent branch and the nonlinear uniformization/monodromy branch rooted in PC-017 remain separate.

## 8. Falsification surface

The finding has seven direct audit points.

1. The primitive-root decomposition `Gamma_n=-sum H_alpha` must have the PC-080 normalization.
2. For cyclically separated roots, the radial expansion and `k` geometric sums must yield exactly the product denominators `1-alpha_i alpha_{i+1} x_i x_{i+1}` and prefactor `prod alpha_i` in the `r -> 1` limit.
3. The separated adjacent radial pair must converge to its boundary product in `S_1`, and the strong-* outer factors must preserve that trace-norm convergence for the full cyclic word.
4. The `k=2` specialization must reduce to `-Log(1-alpha beta)` and hence to the PC-080 resultant after shell summation.
5. The map `(i,j,k) -> (r,s,t)` must be a bijection onto strict integer triangles with odd total parity.
6. The non-collapse control must satisfy simultaneously `Tr(Gamma_2 Gamma_3)=0`, positivity/injectivity of `Gamma_2`, and nonvanishing of `Gamma_3`, forcing `Tr(Gamma_3 Gamma_2 Gamma_3)>0`.
7. No Terasoma-type CMZV reduction may be invoked without first resolving the absolute-convergence failure or proving equivalence of the Hardy radial boundary prescription with an appropriate published regularization.

Failure of points 1--6 invalidates the exact structure. Point 7 is the novelty firewall preventing an unsupported classicalization or novelty claim.

## Research consequence

The finite Hardy/Hankel program has a sharper frontier than PC-081 alone implied:

\[
\boxed{
\text{essential cross-shell geometry is universal, but higher nuclear traces are genuinely richer than resultants.}
}
\]

For cyclically separated shells those traces are explicit critical cyclotomic cone periods. The next useful test is therefore not another finite essential-spectrum wrapper; it is to determine whether the canonical Abel regularization of these cycle-cone periods is already exhausted by cyclotomic conical-zeta/MZV theory, or whether Prime Circle forces a genuinely new cross-level analytic family before any RH interpretation is attempted.
