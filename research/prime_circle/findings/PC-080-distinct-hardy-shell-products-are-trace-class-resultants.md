# PC-080 — distinct Hardy shell products are trace class and their first mixed trace is the cyclotomic resultant

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The trace-class separation and exact Prime-Circle trace identity below are derived here. The cyclotomic resultant formula and the general multichannel/localization principle for Hankel operators with disjoint singularities are classical. No theorem-level historical novelty is claimed.

PC-075 introduced the canonical Hardy interior/exterior operator

\[
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1},\qquad j,k\ge0,
\]

and PC-079 showed that refinement of the whole family is a commuting Möbius calculus of Hilbert-channel dilations. A remaining natural escape is **cross-shell spectral interference**: perhaps two different primitive birth shells interact nontrivially when their noncompact Hardy operators are multiplied before any scalar compression.

For the first pairwise test there is an exact answer. If `m != n`, then

\[
\boxed{\Gamma_m\Gamma_n\in\mathcal S_1}
\]

and in fact

\[
\boxed{
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|.
}
\]

Thus distinct exact-order shells have **no noncompact pairwise interference at all**: their products vanish in the Calkin algebra. The first nuclear invariant of the surviving interaction is exactly minus the classical logarithmic shell energy of PC-002. For `1<m<n`, Apostol's cyclotomic resultant theorem gives

\[
\boxed{
\operatorname{Tr}(\Gamma_m\Gamma_n)
=
\begin{cases}
-\varphi(m)\log p,& n/m=p^a\text{ for a prime }p,\\
0,&\text{otherwise.}
\end{cases}}
\]

With the natural base-shell convention `\Phi_1(z)=z-1` and `\Gamma_1=-H`, the same formula includes

\[
\boxed{\operatorname{Tr}(\Gamma_1\Gamma_n)=-\Lambda(n),}
\]

so the common-anchor von Mangoldt identity PC-001 and the pairwise resultant graph PC-002 become the same mixed-Hardy trace law.

## 1. Primitive-root decomposition into oscillatory Hilbert channels

For `alpha` on the unit circle define

\[
(\mathcal H_\alpha)_{jk}
=\frac{\alpha^{j+k+1}}{j+k+1},
\qquad j,k\ge0.
\]

If `H=(j+k+1)^{-1}` is the Hilbert matrix and

\[
D_\alpha e_j=\alpha^j e_j,
\]

then

\[
\boxed{\mathcal H_\alpha=\alpha D_\alpha H D_\alpha.}
\]

The Ramanujan expansion

\[
c_n(r)=\sum_{\alpha\in P_n^*}\alpha^r
\]

therefore gives the exact finite channel decomposition

\[
\boxed{
\Gamma_n=-\sum_{\alpha\in P_n^*}\mathcal H_\alpha.
}
\]

This is the primitive-root version of the multichannel Hilbert structure already identified in PC-075.

## 2. Different primitive shells have trace-class cross products

Take `alpha in P_m^*` and `beta in P_n^*`, with `m != n`. Then

\[
\alpha\beta\neq1,
\]

because `alpha beta=1` would imply `beta=alpha^{-1}`, hence `alpha` and `beta` would have the same exact order.

Put `gamma=alpha beta`. From the factorization above,

\[
\mathcal H_\alpha\mathcal H_\beta
=\alpha\beta\,D_\alpha H D_\gamma H D_\beta.
\]

To classify the middle factor, define the bounded map

\[
B:\ell^2(\mathbb Z_{\ge0})\to L^2(0,1),
\qquad Be_j(x)=x^j.
\]

Since `B^*B=H`,

\[
H D_\gamma H=B^*K_\gamma B,
\qquad
K_\gamma:=B D_\gamma B^*.
\]

For almost every `x,y in [0,1]`, the integral kernel of `K_gamma` is

\[
K_\gamma(x,y)
=\sum_{r\ge0}(\gamma xy)^r
=\frac1{1-\gamma xy}.
\]

Because `gamma != 1`, the denominator never vanishes on the compact square `[0,1]^2`; the kernel extends to a `C^infty` function there. A smooth-kernel integral operator on a compact one-dimensional domain is trace class (indeed its singular values decay faster than any fixed power, for example by repeated integration by parts in a smooth Fourier/eigenfunction basis). Hence

\[
K_\gamma\in\mathcal S_1,
\qquad
H D_\gamma H\in\mathcal S_1,
\qquad
\mathcal H_\alpha\mathcal H_\beta\in\mathcal S_1.
\]

There are only `phi(m)phi(n)` root pairs, so

\[
\boxed{\Gamma_m\Gamma_n\in\mathcal S_1\qquad(m\neq n).}
\]

The distinct-shell hypothesis is sharp. For `m=n`, the primitive set is closed under inversion, so reciprocal pairs `beta=alpha^{-1}` give `gamma=1`; the smooth-kernel argument fails exactly at the Hilbert singularity. Consistently, PC-075 gives nonzero absolutely continuous spectrum for `Gamma_n`, so `Gamma_n^2` is not trace class.

## 3. The trace of one separated root channel is a logarithmic chord interaction

For `gamma=alpha beta != 1`, the diagonal of the trace-class product is

\[
(\mathcal H_\alpha\mathcal H_\beta)_{jj}
=
\sum_{k\ge0}
\frac{\gamma^{j+k+1}}{(j+k+1)^2}.
\]

Set

\[
d_j=\sum_{r\ge j+1}\frac{\gamma^r}{r^2}.
\]

Since the partial sums of `gamma^r` are bounded when `gamma != 1`, summation by parts gives `d_j=O(j^{-2})`; hence the diagonal series is absolutely summable. For the first `N` diagonal terms,

\[
\sum_{j=0}^{N-1}d_j
=
\sum_{r=1}^{N}\frac{\gamma^r}{r}
+N\sum_{r>N}\frac{\gamma^r}{r^2}.
\]

The second term is `O(N^{-1})`, while the first converges by Dirichlet to the boundary value of the logarithmic series. Therefore

\[
\boxed{
\operatorname{Tr}(\mathcal H_\alpha\mathcal H_\beta)
=-\operatorname{Log}(1-\alpha\beta),
}
\]

with the logarithm understood as the radial boundary value from the unit disk. No branch choice survives after summing complete primitive shells: `Gamma_m Gamma_n` has real trace because `Gamma_m` and `Gamma_n` are self-adjoint and trace cyclicity gives

\[
\overline{\operatorname{Tr}(\Gamma_m\Gamma_n)}
=\operatorname{Tr}(\Gamma_n\Gamma_m)
=\operatorname{Tr}(\Gamma_m\Gamma_n).
\]

Thus taking real parts gives

\[
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\sum_{\alpha\in P_m^*}
\sum_{\beta\in P_n^*}
\log|1-\alpha\beta|.
\]

## 4. The full operator trace is exactly minus the shell resultant

The primitive set `P_m^*` is invariant under inversion. Since `|alpha|=1`,

\[
|1-\alpha\beta|
=|\alpha^{-1}-\beta|.
\]

Therefore

\[
\begin{aligned}
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}|1-\alpha\beta|
&=
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}|\alpha-\beta|\\
&=
\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|.
\end{aligned}
\]

Consequently

\[
\boxed{
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|.
}
\]

PC-002 defined the intrinsic pairwise primitive-shell logarithmic energy

\[
I_{m,n}=\log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|.
\]

Hence the new operator identity is simply

\[
\boxed{
\operatorname{Tr}(\Gamma_m\Gamma_n)=-I_{m,n}.
}
\]

The genuinely nonlocal Hardy product therefore reproduces, at first mixed trace order, exactly the original two-dimensional chord/resultant interaction and nothing beyond it.

## 5. Apostol support: only prime-power scale jumps survive

For `1<m<n`, Apostol's classical theorem gives

\[
\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|
=
\begin{cases}
p^{\varphi(m)},&n/m=p^a,\\
1,&\text{otherwise.}
\end{cases}
\]

Therefore

\[
\boxed{
\operatorname{Tr}(\Gamma_m\Gamma_n)
=
\begin{cases}
-\varphi(m)\Lambda(n/m),&m\mid n,\\
0,&\text{otherwise,}
\end{cases}}
\]

where the first line is nonzero only when `n/m` is a prime power. The symmetric statement for arbitrary distinct `m,n` is best kept in resultant form.

At the base shell,

\[
|\operatorname{Res}(\Phi_1,\Phi_n)|
=|\Phi_n(1)|,
\]

so PC-001 immediately becomes

\[
\operatorname{Tr}(\Gamma_1\Gamma_n)
=-\log\Phi_n(1)
=-\Lambda(n).
\]

Thus the common anchored vertex and the pairwise primitive-shell resultant are not separate mechanisms at this operator level: both are instances of the same mixed Hardy trace.

## 6. Calkin-level consequence: exact-order Hardy channels do not interfere noncompactly

Let `pi` denote the quotient map to the Calkin algebra. Since every distinct-shell product is trace class,

\[
\boxed{
\pi(\Gamma_m)\pi(\Gamma_n)=0
\qquad(m\neq n).
}
\]

The opposite product is trace class as well, so distinct primitive shells commute modulo trace class and in fact annihilate one another modulo compact operators. Their noncompact Hilbert channels are therefore localized independently; any interaction between different exact orders lives entirely below the essential-spectrum level.

This is exactly the qualitative behavior expected from classical multichannel Hankel theory. Pushnitski and Yafaev's piecewise-continuous-symbol scattering theory separates contributions from disjoint symbol singularities and explicitly uses compact cross-products between different model channels; the same paper notes the earlier trace-class cross-channel condition in Howland's self-adjoint Hankel-matrix work. The Prime-Circle derivation above is stronger only in its special arithmetic form: the cross product is explicitly trace class and its trace can be evaluated as a cyclotomic resultant.

## 7. Prior-art and novelty audit

The surrounding mechanism is classical on both sides.

1. Apostol's cyclotomic resultant theorem is already the source anchor for PC-002. It completely classifies the arithmetic value of the final trace.
2. The decomposition of periodic `1/r` Hankel coefficients into finitely many oscillatory Hilbert channels is within the Hilbert/Hankel framework already audited in PC-075.
3. Pushnitski--Yafaev's multichannel theory for Hankel operators with separated symbol singularities supplies the main operator-theoretic novelty warning: separated singular channels are expected to decouple at the compact/trace-class level rather than generate a new shared absolutely continuous spectrum.
4. Directed searches for Ramanujan-sum Hankel cross traces, cyclotomic-resultant Hankel traces, and products of oscillatory Hilbert channels found the surrounding Ramanujan/cyclotomic and Hankel-localization theories, but not an authoritative source stating this exact `Tr(Gamma_m Gamma_n)` specialization. Absence of that wording is not treated as evidence of historical novelty.

The durable contribution is an **internal bridge/classification**: a natural nonlocal cross-shell operator invariant that survives the linear no-go results does not generate new RH data; it maps exactly back to the classical shell resultant already present at the beginning of Prime Circle.

## 8. What this rules out, and what remains open

This closes two specific escape routes from PC-075/PC-079:

\[
\text{distinct primitive Hardy shells}
\to
\text{noncompact pairwise spectral interference}
\to
\text{new RH channel}
\]

is impossible because the cross product is trace class, and

\[
\text{pairwise Hardy product}
\to
\operatorname{Tr}
\to
\text{new arithmetic invariant}
\]

collapses exactly to the classical resultant graph of PC-002.

It does **not** show that the full trace-class product `Gamma_m Gamma_n` is determined by its trace. In particular it leaves open:

- singular values, trace norm, Fredholm determinants, or other relative invariants of `Gamma_m Gamma_n`;
- trace-class commutators beyond the trivial identity `Tr[Gamma_m,Gamma_n]=0`;
- higher cyclic interactions such as `Tr(Gamma_a Gamma_b Gamma_c)`, where three or more shell singularity patterns can interact;
- block operators that retain several shell labels simultaneously instead of multiplying them down to one operator;
- the squarefree mixed-prime higher relative data of `T_rho` left open by PC-077--PC-079;
- shell-dependent nonlinear constructions, the old/new cotangent branch, and the global uniformization/monodromy branch rooted in PC-017.

The result therefore redirects rather than terminates cross-level Hardy research: **pairwise essential-spectrum mixing and the first mixed trace are exhausted; any residual information must be genuinely higher relative data.**

## 9. Falsification surface and controls

The result has five direct failure points.

1. The Ramanujan root expansion must give `Gamma_n=-sum_{alpha in P_n^*} H_alpha` with the stated normalization.
2. For roots of different exact orders, `alpha beta` must never equal `1`; otherwise a non-trace-class Hilbert channel survives.
3. For `gamma != 1`, the kernel `(1-gamma xy)^{-1}` must be smooth on `[0,1]^2`, implying `H D_gamma H` and hence `H_alpha H_beta` are trace class.
4. The diagonal trace must equal `-Log(1-alpha beta)`; the `N`-term triangular remainder above must tend to zero.
5. Inversion invariance of the primitive root set must identify the absolute product `prod |1-alpha beta|` with the cyclotomic resultant.

Exact arithmetic controls are immediate:

\[
\begin{aligned}
\operatorname{Tr}(\Gamma_1\Gamma_9)&=-\log3,\\
\operatorname{Tr}(\Gamma_3\Gamma_6)&=-2\log2=-\log4,\\
\operatorname{Tr}(\Gamma_3\Gamma_5)&=0,\\
\operatorname{Tr}(\Gamma_4\Gamma_{12})&=-2\log3.
\end{aligned}
\]

Direct truncations of the conditionally convergent Ramanujan series `sum_{r>=1} c_m(r)c_n(r)/r` approach these values for the same controls. By contrast, the same-shell control `Gamma_n^2` is not trace class, matching the exact failure of the `gamma != 1` separation condition.

## Research consequence

The first genuinely mixed nonlinear operation on **distinct primitive Hardy shells** has a sharp classification:

\[
\boxed{
\Gamma_m\Gamma_n\in\mathcal S_1,
\qquad
\operatorname{Tr}(\Gamma_m\Gamma_n)
=-\log|\operatorname{Res}(\Phi_m,\Phi_n)|
\quad(m\neq n).
}
\]

So the noncompact Hardy channels of different exact orders decouple completely, while their first residual nuclear coupling is precisely the old prime-power resultant interaction. A meaningful continuation of this branch must move beyond pairwise essential-spectrum mixing and first traces to **higher trace-class invariants, multi-shell cyclic interactions, or simultaneous block structure**.