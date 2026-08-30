# PC-060 — exact radial divisor-Haar symbol vanishes a.e.; spectral mass becomes log-series atoms

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most natural infinite-operator continuation left open by PC-059. For the canonical exact radial Dirichlet kernel

\[
F_x(n)=-\log(1-x^n),\qquad 0<x<1,
\]

the finite divisor-Haar eigenvalue functions from PC-058 form a nonnegative martingale on the profinite valuation probability space identified in PC-059. That martingale converges to zero almost surely. The missing expectation does not disappear: the eigenvalue-weighted spectral measures converge to a singular atomic measure supported exactly on the ordinary positive integers, with atom

\[
\boxed{\nu_x(\{n\})=\frac{x^n}{n}.}
\]

After normalization by `-log(1-x)`, this is the classical logarithmic-series distribution. Thus the unrenormalized exact radial Gram family does **not** produce a nonzero infinite multiplication symbol on the profinite Haar spectral space; its energy escapes onto the countable arithmetic sector which has zero PC-059 vacuum measure.

## 1. Finite divisor-Haar symbols and their vacuum law

For a finite divisor box

\[
\mathcal D(N),\qquad N=\prod_p p^{A_p},
\]

let `S_{x,N}` be the normalized birth Gram matrix of PC-058 with scalar kernel `F_x`. PC-058 gives a common tensor divisor-Haar eigenbasis. For a local prime-power coordinate `p^A`, the eigenvalue functionals are

\[
\ell_{p,j}(f)=\frac{p f(p^j)-f(p^{j+1})}{p-1},
\qquad 0\le j<A,
\]

and

\[
\ell_{p,*}(f)=f(p^A).
\]

PC-059 computes the squared vacuum overlaps in the same basis:

\[
\mu_{p,A}(j)=\frac{p-1}{p^{j+1}},
\qquad
\mu_{p,A}(*)=p^{-A}.
\]

Write `Lambda_N(alpha)` for the eigenvalue of `S_{x,N}` at a joint Haar label `alpha`, and sample `alpha` with the vacuum law `mu_N`. PC-059 identifies the projective limit of these laws with

\[
\mu=\bigotimes_p\mu_p,
\qquad
\mu_p(j)=\frac{p-1}{p^{j+1}},
\]

the valuation pushforward of normalized Haar measure on the profinite integers.

## 2. Refinement makes the eigenvalue symbol a nonnegative martingale

The local weights and eigenvalue functionals satisfy an exact conditional-expectation identity. At the terminal state of a `p^A` coordinate, refinement to exponent `A+1` splits the old value `f(p^A)` into

\[
\lambda_A=\frac{p f(p^A)-f(p^{A+1})}{p-1}
\]

with conditional weight `(p-1)/p`, and the new terminal value `f(p^{A+1})` with conditional weight `1/p`. Hence

\[
\boxed{
\frac{p-1}{p}\lambda_A+\frac1p f(p^{A+1})=f(p^A).
}
\]

Adding a new prime is the same identity with `A=0`. Tensoring over coordinates shows that along any nested cofinal divisor-box filtration,

\[
\boxed{
\mathbb E_\mu[\Lambda_{N'}\mid\mathcal F_N]=\Lambda_N
\qquad(N\mid N').
}
\]

Because `S_{x,N}` is a Gram matrix, every `Lambda_N` is nonnegative. Its expectation is constant and equal to the vacuum quadratic form:

\[
\boxed{
\mathbb E_\mu\Lambda_N=F_x(1)=-\log(1-x).
}
\]

Thus `Lambda_N` is a nonnegative `L^1`-bounded martingale and has an almost-sure limit.

## 3. Along primorial refinement the almost-sure limit is zero

It is enough to use the squarefree primorial filtration. For each prime `p`, the first local split has label `*` with probability `1/p` and label `0` with probability `1-1/p`. These events are independent under `mu`, and

\[
\sum_p\frac1p=\infty.
\]

By the second Borel-Cantelli lemma, almost every valuation label has `*` at infinitely many primes.

At a primorial cutoff, let `S` be the set of star primes, let

\[
m=\prod_{p\in S}p,
\qquad
Q=\prod_{q\notin S}q,
\]

and let the products range over primes already exposed. Composing the local PC-058 functionals gives the exact eigenvalue

\[
\boxed{
\Lambda_{Q,S}(x)
=\frac{Q}{\varphi(Q)}
\sum_{d\mid Q}\frac{\mu(d)}d F_x(md).
}
\]

Suppose the current cutoff prime `p` is a new star. Then `m>=p`. Since `F_x(t)` is positive and decreasing in `t`, absolute values give

\[
0\le\Lambda_{Q,S}(x)
\le F_x(p)
\prod_{q\le p}\frac{q+1}{q-1}.
\]

The prime product is `O((log p)^2)`, while

\[
F_x(p)=-\log(1-x^p)=O(x^p).
\]

Therefore the eigenvalue tends to zero along the infinite subsequence of star cutoffs. The martingale already has an almost-sure limit, so that limit must be the subsequential limit:

\[
\boxed{
\Lambda_N\longrightarrow0
\quad\mu\text{-almost surely}.}
\]

In particular the martingale is not uniformly integrable, because its expectations remain `-log(1-x)>0`.

## 4. The lost expectation defines a singular arithmetic measure

Define the finite eigenvalue-weighted vacuum spectral measure by

\[
d\nu_{x,N}=\Lambda_N\,d\mu_N.
\]

The martingale identity makes these finite measures projectively consistent. They therefore define a finite measure `nu_x` on the limiting valuation space, with total mass

\[
\nu_x(\Omega)=-\log(1-x).
\]

The key local cancellation is exact:

\[
\boxed{
\mu_p(j)\ell_{p,j}(f)
=\frac{f(p^j)}{p^j}-\frac{f(p^{j+1})}{p^{j+1}}.
}
\]

For the terminal state the corresponding finite-box expression is simply `p^{-A}f(p^A)`. Thus the eigenvalue-weighted spectral measure is a tensor finite-difference transform of `F_x(n)/n`.

Fix an ordinary positive integer `n` and identify it with its finite-support valuation vector `(v_p(n))_p`. Shrinking cylinders onto that point and applying the displayed finite differences gives

\[
\nu_x(\{n\})
=\sum_{d\ge1}\mu(d)\frac{F_x(nd)}{nd}.
\]

The series is absolutely convergent for `0<x<1`. Expanding the logarithm,

\[
F_x(nd)=\sum_{k\ge1}\frac{x^{ndk}}k,
\]

and writing `r=dk` yields

\[
\begin{aligned}
\nu_x(\{n\})
&=\frac1n\sum_{r\ge1}\frac{x^{nr}}r
\sum_{d\mid r}\mu(d)\\
&=\boxed{\frac{x^n}{n}}.
\end{aligned}
\]

Since

\[
\sum_{n\ge1}\frac{x^n}{n}=-\log(1-x)=\nu_x(\Omega),
\]

these atoms account for **all** of the measure. Hence

\[
\boxed{
\nu_x=\sum_{n\ge1}\frac{x^n}{n}\,\delta_{(v_p(n))_p}.}
\]

PC-059 proves that the set of ordinary finite-support valuation vectors is countable and `mu`-null. Consequently

\[
\boxed{
\nu_x\perp\mu.}
\]

The finite symbols are absolutely continuous densities with respect to `mu_N`, but their projective-limit energy measure is singular with respect to the limiting vacuum law.

## 5. An explicit mass-escape spike

The all-zero primorial label already exhibits the mechanism. For `P#=prod_{p<=P}p`,

\[
\Lambda_{0,P}(x)
=\frac{P\#}{\varphi(P\#)}
\sum_{d\mid P\#}\frac{\mu(d)}d F_x(d).
\]

The infinite Mobius sum is exactly

\[
\boxed{
\sum_{d\ge1}\frac{\mu(d)}d[-\log(1-x^d)]=x,
}
\]

by the same divisor cancellation as above. Mertens' prime-product theorem therefore gives

\[
\Lambda_{0,P}(x)\sim e^\gamma x\log P.
\]

But the vacuum probability of that label is

\[
\mu_P(0)=\frac{\varphi(P\#)}{P\#}
\sim\frac{e^{-\gamma}}{\log P}.
\]

Their product tends to `x`, exactly the mass of the atom `n=1`. The pointwise symbol grows on an increasingly rare arithmetic cylinder while tending to zero on almost every profinite label. This is a concrete witness for the failure of uniform integrability; no spectral mass is mysteriously destroyed.

## 6. Prior-art and novelty audit

The ambient ingredients are classical and do not support a novelty claim.

- PC-059 already identifies `mu` as the standard independent prime-valuation law coming from Haar measure on `hat Z`; independent prime-divisibility models are standard probabilistic-number-theory/Kubilius territory.
- Nonnegative martingale convergence, failure of uniform integrability when expectation is lost, and the second Borel-Cantelli lemma are standard probability theory.
- The Mobius cancellation `sum_{d|r} mu(d)=1_{r=1}` is classical and is the only arithmetic inversion needed to identify the limiting atoms.
- After normalization, the atom law is

\[
\boxed{
\Pr_x(n)=\frac{x^n}{n[-\log(1-x)]},\qquad n\ge1,
}
\]

which is exactly the classical logarithmic-series distribution. Fisher, Corbet and Williams introduced this distribution in their 1943 work on species abundance: R. A. Fisher, A. S. Corbet and C. B. Williams, **The Relation Between the Number of Species and the Number of Individuals in a Random Sample of an Animal Population**, *Journal of Animal Ecology* 12:1 (1943), 42–58, DOI `10.2307/1411`.

No historical novelty is claimed for any of those ingredients. The durable project-specific consequence is their exact combination with PC-058/PC-059:

\[
\boxed{
\text{canonical radial divisor-Haar symbol}\to0\ \mu\text{-a.e.},
\qquad
\text{weighted spectral mass}\to\sum_{n\ge1}\frac{x^n}{n}\delta_n.
}
\]

This precisely resolves the nontrivial-infinite-symbol ambiguity left open in PC-059 for the exact radial Dirichlet Gram family.

## 7. Why this is a decisive negative for the canonical infinite-symbol route

PC-059 deliberately left open the possibility that, although the limiting joint Haar basis is classical, a specific infinite operator might survive as multiplication by a nontrivial function on `(Omega,mu)`. For the intrinsic exact radial family `F_x(n)=-log(1-x^n)`, the answer is now exact: **without additional renormalization, the only almost-everywhere multiplication-symbol limit is zero**.

The nonzero information survives only after changing measure to the singular atomic law `nu_x`, and that law is the classical logarithmic series. It contains no free complex spectral parameter, no gamma factor, no intrinsic `s<->1-s` symmetry, and no distinguished `Re(s)=1/2`. Letting `x->1^-` merely sends the total mass `-log(1-x)` to infinity and the normalized log-series mass outward; it does not generate the nontrivial zeros of zeta.

Therefore the route

\[
\boxed{
\text{exact radial prime-circle Gram}
\to
\text{PC-058 divisor-Haar diagonalization}
\to
\text{PC-059 profinite limit}
\to
\text{nontrivial unrenormalized infinite symbol}
\to
\text{RH}
}
\]

is closed.

## 8. Boundaries and falsification tests

This result does **not** rule out:

- a geometrically forced renormalization of the finite operators before the limit;
- a different intrinsic two-dimensional kernel outside the fixed divisor-Haar algebra;
- nonlinear or cross-level couplings taken before diagonalization;
- an independently derived archimedean/finite-adic self-duality;
- or the global primitive-root uniformization/accessory branch of PC-017.

A renormalization is not evidence by itself: unless its scale and operator meaning are forced by prime-circle geometry, it risks becoming the arbitrary spectral wrapper excluded by the research program.

The exact claim can be falsified at finite level in three independent ways:

1. verify the conditional-expectation identity under one prime/exponent refinement;
2. verify for any finite divisor box that `sum_alpha mu_N(alpha)Lambda_N(alpha)=F_x(1)` and all eigenvalues are nonnegative;
3. for a fixed integer valuation vector, expand the cylinder mass and check that its cofinal limit is `x^n/n`.

Any failure of one of these identities would invalidate the martingale/singular-measure conclusion. All three are algebraic consequences of the PC-058 eigenfunctionals and the exact logarithmic series for `F_x`.