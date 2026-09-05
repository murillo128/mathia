# MC-073 — Coupled comparator recovery is a universal Dirichlet-convolution gauge

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The exact signed recovery architecture used in `MC-066`--`MC-072` has a universal algebraic component that is independent of Möbius-specific arithmetic.

Let `a` be **any** arithmetic function with

\[
a(1)=1,
\]

let `\mathbf 1(n)=1`, and define

\[
h:=\mathbf 1*a,
\qquad
k:=h^{-1}
\]

under Dirichlet convolution. Since the Möbius function is the Dirichlet inverse of `\mathbf 1`, one has identically

\[
\boxed{
k=a^{-1}*\mu,}
\tag{1}
\]

and therefore

\[
\boxed{a*k=\mu.}
\tag{2}
\]

Writing

\[
A(x)=\sum_{n\le x}a(n),
\]

summing `(2)` through `X` gives the exact recovery formula

\[
\boxed{
M(X)=\sum_{d\le X}k(d)A(X/d).
}
\tag{3}
\]

No multiplicativity, character theory, zero-free region, or cancellation hypothesis is needed. Thus **the existence of a coupled comparator/inverse representation and the fact that its full signed sum recovers `M(X)` are universal Dirichlet-convolution identities, not arithmetic evidence.**

This has a direct matched-control consequence. If one randomizes or otherwise changes the comparator `a` and then recomputes its exact induced inverse kernel `k=(\mathbf 1*a)^{-1}`, the recovered coefficient sequence is still exactly `\mu` and the full finite sum `(3)` is still exactly `M(X)` for every sample. Any observed cancellation of the *complete* coupled recovery is therefore a degenerate control: its endpoint is algebraically fixed before the comparator is chosen.

For the quadratic square-free comparator of the current frontier,

\[
f_\chi(n)=\mu(n)^2\chi(n),
\]

the universal factorization simplifies further. Its Dirichlet inverse is exactly

\[
\boxed{f_\chi^{-1}=\lambda\chi,}
\tag{4}
\]

where `\lambda(n)=(-1)^{\Omega(n)}` is Liouville. Consequently the inverse kernel from `MC-071` is

\[
\boxed{k_\chi=\mu*(\lambda\chi),}
\tag{5}
\]

and the full coupled recovery is simply

\[
\boxed{
\mu
=f_\chi*k_\chi
=\mu*\bigl(f_\chi*(\lambda\chi)\bigr)
=\mu*\varepsilon.
}
\tag{6}
\]

Here `\varepsilon` is the Dirichlet-convolution identity. The `\chi`-dependent pair `f_\chi,\lambda\chi` cancels **exactly**, coefficient by coefficient, before any estimate is made.

This does **not** make the comparator program vacuous. `MC-066`--`MC-070` obtained genuine information by imposing independent bounds on one side of the factorization, and `MC-071`--`MC-072` identified zero-sensitive costs of other independent bounds. What `(1)`--`(6)` rule out is a vaguer residual strategy: merely appealing to "cancellation between the coupled factors" or to empirical cancellation across all reciprocal blocks cannot be the missing mechanism, because that total cancellation is present for every normalized comparator by construction.

A surviving coupled route must isolate a **proper, non-universal subfunctional**—for example a truncated range, selected reciprocal blocks, a bilinear form, or another weighted piece—and prove an arithmetic estimate for it together with a controlled complementary error. The estimate must use structure not forced by `a*a^{-1}=\varepsilon`.

No improved estimate for `M(X)` is claimed.

## 1. The group identity behind every comparator recovery

The arithmetic functions with nonzero value at `1` form an abelian group under Dirichlet convolution. In the normalized case `a(1)=1`, both `a` and `h=\mathbf 1*a` are invertible. Since

\[
\mathbf 1^{-1}=\mu,
\]

commutativity gives

\[
\begin{aligned}
k
&=(\mathbf 1*a)^{-1}\\
&=a^{-1}*\mathbf 1^{-1}\\
&=a^{-1}*\mu,
\end{aligned}
\]

which proves `(1)`. Convolving with `a` yields

\[
a*k=a*a^{-1}*\mu=\varepsilon*\mu=\mu,
\]

proving `(2)`.

Equation `(3)` is then just the summatory form of `(2)`:

\[
\begin{aligned}
M(X)
&=\sum_{n\le X}\sum_{d\mid n}k(d)a(n/d)\\
&=\sum_{d\le X}k(d)
\sum_{m\le X/d}a(m).
\end{aligned}
\]

All statements are finite coefficient identities. They remain true for nonmultiplicative `a`; multiplicativity becomes relevant only when it supplies additional structure or estimates for the chosen factors.

Two extreme gauges make the nonuniqueness explicit.

- If `a=\mu`, then `h=\mathbf 1*\mu=\varepsilon`, so `k=\varepsilon` and `(3)` reduces to the original `M(X)=A(X)` with no distributed feedback at all.
- If `a=\varepsilon`, then `h=\mathbf 1`, so `k=\mu`, while `A(x)=1` for `x\ge1`; equation `(3)` becomes `M(X)=\sum_{d\le X}\mu(d)`.

Between these extremes there are infinitely many factorizations with very different-looking reciprocal-block geometries but exactly the same recovered Möbius sequence. Hence block shape, apparent cancellation, or spreading of the recovery is not intrinsic evidence unless the comparator itself is selected by an independently justified arithmetic theorem.

## 2. The square-free character inverse is twisted Liouville

For any Dirichlet character `\chi`, the square-free-supported function

\[
f_\chi=\mu^2\chi
\]

has local coefficients

\[
f_\chi(p)=\chi(p),
\qquad
f_\chi(p^j)=0\quad(j\ge2).
\]

Its local convolution generating factor is therefore

\[
1+\chi(p)z.
\]

The inverse local factor is

\[
\frac1{1+\chi(p)z}
=
\sum_{j\ge0}(-\chi(p))^jz^j.
\tag{7}
\]

But

\[
(\lambda\chi)(p^j)
=(-1)^j\chi(p)^j
=(-\chi(p))^j,
\]

including conductor primes, where `\chi(p)=0` makes every positive-power coefficient vanish. Thus `(7)` proves the coefficient identity `(4)` directly.

At the Dirichlet-series level this is the standard factorization already appearing in `MC-061`:

\[
\sum_{n\ge1}\frac{\lambda(n)\chi(n)}{n^s}
=
\frac{L(2s,\chi^2)}{L(s,\chi)},
\]

which is the reciprocal of

\[
\sum_{n\ge1}\frac{\mu(n)^2\chi(n)}{n^s}
=
\frac{L(s,\chi)}{L(2s,\chi^2)}
\]

in the common half-plane of absolute convergence. No continuation is required for the coefficient proof.

Equation `(5)` now follows immediately from `(1)`. It is equivalent to the more expanded factorization in `MC-071`,

\[
k_\chi=\mu*(\mu\chi)*r_\chi,
\]

because the classical square-divisor identity gives

\[
(\mu\chi)*r_\chi=\lambda\chi.
\]

The simplification matters conceptually: the current inverse kernel is `\mu` convolved with the **exact inverse of the chosen comparator**. The comparator-dependent signed pair is not a second independent source of randomness.

## 3. Reciprocal-block cancellation is universal at the full-sum level

Let

\[
K(x)=\sum_{n\le x}k(n).
\]

Grouping `(3)` by

\[
m=\left\lfloor\frac Xd\right\rfloor
\]

gives, for every normalized comparator `a`,

\[
\boxed{
M(X)
=
\sum_{m=1}^{X}
A(m)
\left(
K\!\left(\left\lfloor\frac Xm\right\rfloor\right)
-
K\!\left(\left\lfloor\frac X{m+1}\right\rfloor\right)
\right).
}
\tag{8}
\]

Thus the reciprocal-block formula of `MC-072` is not special to the quadratic comparator either. Its full block sum is a universal coordinate representation of the same convolution identity.

This creates a stringent control for the residual frontier. Suppose a family of comparators `a_\omega` is randomized, phase-twisted, changed with scale, or replaced by a matched non-arithmetic construction, and for each member one recomputes

\[
k_\omega=(\mathbf1*a_\omega)^{-1}.
\]

Then `(8)` equals the same deterministic `M(X)` for every `\omega`. The variance of the **complete recovered output across that ensemble is exactly zero**, regardless of how different the individual block terms look.

Therefore numerical evidence that different comparators display large internal block cancellation before landing on the same small or large `M(X)` cannot validate the arithmetic mechanism. That landing is hard-wired by inversion. A meaningful matched control must instead test an observable not fixed by `(2)`, such as a bounded subset of blocks, a truncation whose complement is independently estimated, or a norm/covariance predicted to be small only for the arithmetic comparator.

Freezing `k` while changing `a`, or changing only one factor, can produce a nondegenerate control, but it is then testing a different mathematical object rather than the exact comparator/inverse architecture.

## 4. Prior art and novelty boundary

The algebra is classical. NIST DLMF §27.5, *Inversion Formulas*, explicitly records Dirichlet convolution and states that number-theoretic functions with nonzero value at `1` form an abelian group under Dirichlet multiplication, citing Apostol's *Introduction to Analytic Number Theory*, Chapter 2. The same section records Möbius inversion as the identity `\mathbf1*\mu=\varepsilon`.

`MC-S9` anchors the classical Liouville square-divisor identity, and `MC-061` already records the twisted Liouville Dirichlet series `L(2s,chi^2)/L(s,chi)`. `MC-071` records the reciprocal kernel quotient `L(2s,chi^2)/(zeta(s)L(s,chi))`. Equations `(4)`--`(6)` are the coefficient-level compression of those already-established facts.

A targeted prior-art audit found no reason to treat `(1)`--`(8)` as a new theorem of analytic number theory. They are standard convolution-group identities and immediate specializations. The durable Mathia contribution is the **control interpretation at the current frontier**: the complete signed coupling left open after `MC-072` is algebraically gauge-degenerate, so full-sum cancellation across comparator choices cannot itself provide evidence or a new mechanism.

## 5. Boundaries and falsification tests

The obstruction is deliberately about the **complete exact coupling**, not every possible use of a comparator.

- It does not rule out `MC-066`-style feedback inequalities, because those introduce nontrivial estimates on `A` or on a proper kernel functional before the universal identity is completed.
- It does not rule out cancellation between a selected subset of reciprocal blocks and its complement. It says that the *total* cross-block cancellation is predetermined and therefore cannot be the evidential object.
- It does not rule out a truncation with a provably small remainder, a bilinear estimate, a scale-coupled contraction, or another proper functional that uses special arithmetic structure.
- It does not assert that all comparator choices are equally useful analytically. Different gauges can expose radically different theorem surfaces even though their exact recombination is invariant.
- The random-control degeneracy applies only when the exact inverse is recomputed with each randomized comparator. Randomizing one factor while holding the other fixed is nondegenerate but no longer preserves the exact factorization.
- The identity `(4)` uses `f_\chi=\mu^2\chi`; a different prime-power rule has a different Dirichlet inverse even though the universal statement `(1)`--`(3)` still holds.

The claim is falsified if normalized arithmetic functions fail to form a Dirichlet-convolution group, if `(\mathbf1*a)^{-1}` is not `a^{-1}*\mu`, if summing `a*k=\mu` does not give `(3)`, or if the local inverse of `1+\chi(p)z` is not the `\lambda\chi` prime-power series. Each point is an exact finite algebraic check.

## Consequence for the active frontier

After `MC-070`, positive triangle feedback is quantitatively blocked for the current quadratic package. `MC-071` shows that standalone cancellation of the signed inverse already carries zeta and Dirichlet-`L` zero-free information, and `MC-072` shows that independently controlling its first reciprocal annulus has the same burden.

The residual phrase **"exploit cancellation between reciprocal blocks" now needs one further qualification**: cancellation of the complete set of blocks is universal and algebraically forced for every comparator/inverse pair. It cannot be the missing datum by itself.

A productive continuation must name a proper coupled statistic whose smallness is *not* invariant under arbitrary Dirichlet-convolution gauge changes, prove that the quadratic or another arithmetic comparator controls that statistic by information genuinely cheaper than the Mertens target, and bound the complementary part without restoring the zero-hard inverse estimate. This converts the remaining signed route from a generic appeal to coupling into a falsifiable requirement for a non-universal partial coupling.