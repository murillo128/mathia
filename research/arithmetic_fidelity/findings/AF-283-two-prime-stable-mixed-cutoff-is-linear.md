# AF-283 — Stable two-prime mixed cutoff is linear in source breadth

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `JOINT-SAMPLING`, `FINITE-BREADTH`, `STABILITY`, `VANDERMONDE`, `NO-NOVELTY-CLAIM`

## Claim

AF-281 proves exact coefficient fidelity for the complete two-prime mixed channel and AF-282 shows that its finite-prefix phase labels have minimum pairwise spacing of order `1/N`. The remaining question is whether this inverse-breadth spacing forces a much worse coefficient-recovery budget.

For the known ordinary-Dirichlet prefix `1,...,N`, it does not. Let

\[
t_n=
\left(-\frac{\log n}{\log2},-\frac{\log n}{\log3}\right)
\pmod{\mathbb Z^2},
\qquad
z_n=e^{2\pi i t_n}\in\mathbb T^2,
\]

and for an integer `L>=2` retain the mixed moments

\[
y_\nu=\sum_{n=1}^N b_n z_n^\nu,
\qquad
\nu=(\nu_1,\nu_2)\in\{0,\ldots,L-1\}^2,
\]

where `b_n=a_n n^{-c}` are the weighted Dirichlet coefficients on a fixed vertical line `Re(s)=c`. Equivalently these are the samples

\[
F\!\left(c+i\left(\nu_1\frac{2\pi}{\log2}+\nu_2\frac{2\pi}{\log3}\right)\right).
\]

Then the coordinatewise mixed degree needed for **uniform coefficient stability** has the sharp order

\[
\boxed{L=\Theta(N).}
\]

More precisely:

1. if a decoder is Lipschitz from per-sample `\ell^\infty` error to coefficient `\ell^\infty` error on this known prefix, its inverse modulus obeys

\[
\boxed{
\kappa_\infty(N,L)
\ge
\frac{(N-1)\log2}{4\pi(L-1)};
}
\]

hence `L=o(N)` cannot give a breadth-uniform stable inverse;

2. taking the full square of mixed indices with

\[
\boxed{L=30N}
\]

gives a uniform stable inverse. If every retained mixed moment is perturbed by at most `epsilon`, least-squares recovery satisfies

\[
\boxed{
\|\widehat b-b\|_2<\frac{10}{9}\,\epsilon.
}
\]

The sufficiency statement is an arithmetic specialization of the explicit multivariate Vandermonde bound of Kunis--Nagel--Strotmann. Thus the finite-prefix instability left open by AF-282 is not hidden exponential conditioning in the required **mixed degree**: linear degree is both necessary and sufficient up to constants.

This does not make acquisition free. The dense square contains `L^2=Theta(N^2)` scalar samples. The theorem closes the degree/separation scale but leaves a genuine observation-complexity question: whether a substantially sparser set of mixed moments can retain a comparable uniform inverse on the arithmetic node family.

## Torus separation inherited from AF-282

Write the wrap-around distance on `T^2` as

\[
|t-t'|_{\mathbb T^2}
=
\min_{r\in\mathbb Z^2}\|t-t'+r\|_\infty
\]

and let

\[
q_N=
\min_{1\le m<n\le N}
|t_n-t_m|_{\mathbb T^2}.
\]

For one coordinate with wrap distance `x in [0,1/2]`, the corresponding chord is `2 sin(pi x)`, hence

\[
2\sin(\pi x)\le2\pi x.
\]

Therefore AF-282's chord lower bound implies

\[
q_N
\ge
\frac{\delta_N}{2\pi}
\ge
\frac{2}{\pi\,3^{1/4}\log6}\frac1N.
\]

Put

\[
c_0=
\frac{2}{\pi\,3^{1/4}\log6}
\approx0.269972856.
\]

Then

\[
\boxed{q_N\ge c_0/N.}
\]

The adjacent pair `N-1,N` also has phase displacement of order `1/N`; in particular its coordinatewise chord distance is bounded by

\[
d_{N-1,N}
\le
\frac{2\pi}{\log2}\frac1{N-1}.
\]

Thus both the necessary and sufficient stability estimates below operate at the same inverse-breadth separation scale.

## Linear mixed degree is necessary for uniform stability

Let `V_{N,L}` be the multivariate Vandermonde matrix

\[
V_{N,L}=
\bigl(z_n^\nu\bigr)_
{1\le n\le N,\;\nu\in\{0,\ldots,L-1\}^2}.
\]

The observation map is `b -> V_{N,L}^T b`.

Consider only the adjacent coefficient difference

\[
u=e_N-e_{N-1}.
\]

For unit complex numbers `u,v` and an integer `r>=0`,

\[
|u^r-v^r|\le r|u-v|.
\]

Hence for every retained multi-index `nu`,

\[
\begin{aligned}
|z_N^\nu-z_{N-1}^\nu|
&\le
\nu_1|z_{N,1}-z_{N-1,1}|
+\nu_2|z_{N,2}-z_{N-1,2}|\\
&\le
2(L-1)d_{N-1,N}\\
&\le
\frac{4\pi(L-1)}{(N-1)\log2}.
\end{aligned}
\]

But `||u||_infinity=1`. Therefore any exact decoder whose coefficient error is bounded by `kappa_infinity` times the maximum mixed-sample error must satisfy

\[
1
\le
\kappa_\infty(N,L)
\frac{4\pi(L-1)}{(N-1)\log2},
\]

which proves

\[
\kappa_\infty(N,L)
\ge
\frac{(N-1)\log2}{4\pi(L-1)}.
\]

The same ratio is obtained after scaling the two-point perturbation into any fixed weighted `ell^1` ball, so this is not an artifact of an unbounded source norm.

Consequently a family with `L=o(N)` has diverging worst-case inverse modulus even on the declared finite prefix. Exact injectivity at smaller mixed degree is therefore not enough for breadth-uniform coefficient recovery.

## Linear mixed degree is sufficient on the known prefix

Kunis, Nagel, and Strotmann study exactly the rectangular multivariate Vandermonde matrix with nodes `t_j in T^d`, exponents

\[
\nu\in\mathbb N^d,
\qquad
\|\nu\|_\infty<L,
\]

and wrap-around node separation `q`. Their Theorem 4.2 states that for `d>=2`, even `L`, and

\[
qL>4d,
\]

the smallest singular value satisfies

\[
\sigma_{\min}(V)>0.9L^{d/2}.
\]

Here `d=2`. From the arithmetic separation above,

\[
q_N(30N)
\ge30c_0
\approx8.09918568
>8=4d.
\]

Since `30N` is even, Theorem 4.2 applies with `L=30N` and gives

\[
\boxed{
\sigma_{\min}(V_{N,30N})>0.9(30N).
}
\]

The transpose observation matrix has the same singular values. Suppose the `L^2` observed moments are perturbed by a vector `eta` with

\[
\|\eta\|_\infty\le\epsilon.
\]

Then

\[
\|\eta\|_2\le L\epsilon.
\]

Least-squares/pseudoinverse recovery on the known support therefore gives

\[
\|\widehat b-b\|_2
\le
\frac{\|\eta\|_2}{\sigma_{\min}(V_{N,L})}
<
\frac{L\epsilon}{0.9L}
=
\frac{10}{9}\epsilon.
\]

Thus a fixed constant multiple of the arithmetic breadth gives a coefficient-recovery modulus independent of `N` when noise is measured per retained mixed sample.

Together with the adjacent-pair lower bound, this proves the claimed order-sharp law

\[
\boxed{
\text{uniform stable mixed degree}=\Theta(N).
}
\]

## Resource accounting

This result separates several bills that AF-281 and AF-282 had left distinct but unpriced jointly.

The **coordinatewise mixed degree** is now sharp up to constants: `Theta(N)` is necessary and sufficient for uniform recovery of the weighted coefficients on the known prefix. The associated mixed-time horizon is also `O(N)` because each retained time is a nonnegative combination `nu_1 h_2+nu_2 h_3` with `nu_j<L`.

The sufficient construction, however, uses the complete square of indices, hence

\[
L^2=\Theta(N^2)
\]

scalar measurements. Rank alone gives only the elementary lower bound of at least `N` scalar observations for arbitrary `N` coefficients. Nothing here closes the gap between `Omega(N)` and `O(N^2)` sample count, nor shows that the dense square is optimal for the arithmetic node set.

The stable object recovered above is `b_n=a_n n^{-c}`. If the downstream norm instead measures the unweighted coefficients `a_n`, converting the uniform bound back to that norm can cost as much as `N^c` on the prefix. That weighting bill is separate from Vandermonde conditioning and must be stated explicitly in any downstream application.

Finally, known support is a real resource. The theorem assumes the candidate frequencies are exactly `log1,...,logN`. Unknown-support super-resolution, unbounded Dirichlet sources, and support selection are different inverse problems.

## Prior art and novelty assessment

No Vandermonde, super-resolution, or sampling novelty is claimed.

Stefan Kunis, Dominik Nagel, and Anna Strotmann, **“Multivariate Vandermonde matrices with separated nodes on the unit circle are stable,”** *Applied and Computational Harmonic Analysis* 58 (2022), 50--59, DOI `10.1016/j.acha.2022.01.001`, prove the explicit multivariate smallest-singular-value estimate used above. Their result is already formulated in the same torus wrap metric and rectangular mixed-monomial basis required here.

Stefan Kunis, Thomas Peter, Tim Roemer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31--47, DOI `10.1016/j.laa.2015.10.023`, gives broader prior art for stable multivariate recovery from moments under support-size and separation conditions.

Ankur Moitra, **“Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices,”** *Proceedings of STOC 2015*, 821--830, DOI `10.1145/2746539.2746561`, gives the sharp univariate separation-versus-cutoff picture and is useful context for why a cutoff proportional to inverse node separation is the natural scale.

The retained result is the arithmetic specialization obtained by combining AF-282's explicit two-prime phase separation with the classical multivariate stability theorem, plus the elementary adjacent-integer lower bound. Its value for Arithmetic Fidelity is the resulting exact resource law, not a claim that the underlying harmonic-analysis theorem is new.

## Boundaries and failure modes

- The source support is known a priori to be `1,...,N`; this is not an unknown-frequency theorem.
- The recovery guarantee concerns weighted coefficients `b_n=a_n n^{-c}` on the chosen line `Re(s)=c`.
- The noise model is uniform absolute error per retained mixed moment. Correlated, relative, stochastic, or time-dependent noise requires a separate norm calculation.
- `L=30N` is an explicit convenient sufficient constant, not a sharp constant. It comes from combining AF-282's nonsharp separation constant with the explicit `qL>8` theorem.
- The lower bound proves that `o(N)` coordinatewise mixed degree cannot have a uniform inverse modulus. It does not prove that every `Theta(N)` index pattern is stable.
- The dense square uses `Theta(N^2)` samples. No sample-count optimality is claimed.
- Exact timing of the mixed samples is assumed. A finite-precision timing channel introduces a further phase error that must be propagated separately.
- AF-281's unrestricted infinite-source obstruction remains untouched: fixed finite mixed degree cannot recover an unbounded weighted `ell^1` Dirichlet source uniformly.
- No analytic continuation, zero-location statement, functional equation, or RH consequence follows from this finite-prefix stability theorem alone.

## Decisive audit test

When a finite-prefix mixed-cadence proposal claims that the exact two-prime coupling of AF-281 is unusable because coefficient inversion necessarily becomes super-polynomially ill-conditioned as the prefix grows, separate the resource being asserted.

For the full mixed square on `1,...,N`, `o(N)` coordinatewise degree cannot have a breadth-uniform inverse modulus, while degree `30N` already gives a uniform `ell^2` coefficient bound under per-sample absolute noise. Any stronger obstruction must therefore come from sample-count restrictions, a sparser admissible acquisition geometry, timing precision, source weights, unknown support, the downstream target metric, or another source-category constraint rather than from pairwise phase separation itself.

## Consequence for the research line

The finite-prefix mixed-degree question left by AF-282 is now closed at order level: exact coupling plus arithmetic phase separation supports a uniformly stable inverse once mixed degree grows linearly with breadth, and linear growth is necessary.

The next live acquisition question should therefore stop conflating degree with observation count. Determine whether the arithmetic node set admits a **sparse mixed-moment family** with near-linear sample count and a comparable uniform inverse, or prove a lower bound showing that stable acquisition intrinsically needs substantially more than `N` scalar mixed moments under the admissible timing geometry. A second legitimate branch is target-sensitive compression: if an RH-relevant downstream functional needs less than the full coefficient vector, quantify its smaller witness budget directly rather than paying for complete source reconstruction.