# MC-408 — The signed Möbius--PNT-error correlation is an RH-scale criterion, not an easier auxiliary observable

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `RH-EQUIVALENT-BOUNDARY` · `CLASSICAL-TRANSFORMS` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM`.

## Claim

Let

\[
E(y):=\psi(y)-y,
\qquad
C(x):=\sum_{a\le x}\mu(a)E(x/a).
\tag{1}
\]

`MC-407` showed that `C(x)` is the exact signed remainder left after separating the deterministic PNT main term from the Möbius--Mangoldt quotient convolution. The remaining question was whether a new signed theorem for `(1)` could be an intermediate route toward Mertens cancellation.

At the square-root target, it is not an easier intermediate statement. For every `epsilon>0`,

\[
\boxed{
C(x)=O_\varepsilon\!\left(x^{1/2+\varepsilon}\right)
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{2}
\]

The reason is sharper than the finite identity in `MC-407`. For `Re(s)>1`, the Mellin transform of `C` is

\[
\boxed{
\int_1^\infty C(x)x^{-s-1}\,dx
=
-\frac{\zeta'(s)}{s\zeta(s)^2}
-\frac{1}{(s-1)\zeta(s)}.
}
\tag{3}
\]

If `rho` is a nontrivial zero of `zeta` of multiplicity `m`, then the first term in `(3)` has a pole of order `m+1` at `rho`, while the second has order only `m`. Hence the highest-order pole cannot cancel. A bound of the form on the left of `(2)` makes the Mellin integral holomorphic throughout `Re(s)>1/2`, excluding every zero there and therefore implying RH.

Conversely RH gives the standard Mertens bound `M(x)=O_epsilon(x^(1/2+epsilon))`. Combining that with the exact identity already present in `MC-407`,

\[
C(x)
=-\sum_{n\le x}\mu(n)\log n
-x\sum_{n\le x}\frac{\mu(n)}n,
\tag{4}
\]

and partial summation gives the reverse implication in `(2)`.

There is also a finite-prefix information statement. If `C_N:=C(N)` and

\[
m_N:=\sum_{n\le N}\frac{\mu(n)}n,
\]

then

\[
C_N-C_{N-1}
=-m_{N-1}-(1+\log N)\mu(N).
\tag{5}
\]

Thus the finite vector `(C_1,...,C_N)` determines `(mu(1),...,mu(N))` recursively. The correlation `(1)` is not a compression of Möbius data; it is a lower-triangular re-encoding with nonzero diagonal. This exact invertibility does **not** make norm bounds equivalent automatically, but it reinforces the frontier diagnosis: merely naming `(1)` as a joint prime-error observable has not supplied independent information.

The useful residual question is therefore methodological, not representational. A proof of a strong bound for `(1)` could still solve RH, but it must introduce an estimate not already equivalent to controlling `M`. The prime-error factor `E(x/a)` by itself does not create a cheaper target.

## 1. Mellin transform

For `sigma=Re(s)>1`, absolute convergence permits interchanging sum and integral in `(1)`. With `x=au`,

\[
\begin{aligned}
\int_1^\infty C(x)x^{-s-1}\,dx
&=\sum_{a\ge1}\mu(a)
  \int_a^\infty E(x/a)x^{-s-1}\,dx\\
&=\left(\sum_{a\ge1}\frac{\mu(a)}{a^s}\right)
  \int_1^\infty E(u)u^{-s-1}\,du.
\end{aligned}
\tag{6}
\]

The first factor is `1/zeta(s)`. For the second, using

\[
\psi(u)=\sum_{n\le u}\Lambda(n),
\]

again by absolute convergence,

\[
\int_1^\infty \psi(u)u^{-s-1}\,du
=\frac1s\sum_{n\ge1}\frac{\Lambda(n)}{n^s}
=-\frac1s\frac{\zeta'(s)}{\zeta(s)}.
\tag{7}
\]

Also

\[
\int_1^\infty u\,u^{-s-1}\,du=\frac1{s-1}.
\tag{8}
\]

Substituting `(7)` and `(8)` into `(6)` proves `(3)`.

No contour shift, zero-free region, Perron inversion or RH input is used to derive `(3)`; it is an identity in the half-plane of absolute convergence followed by the standard meromorphic continuation of its closed form.

## 2. A zero forces a nonremovable pole

Suppose `zeta` has a zero `rho` of multiplicity `m>=1`. Write locally

\[
\zeta(s)=(s-\rho)^m h(s),
\qquad h(\rho)\ne0.
\]

Then

\[
\frac{\zeta'(s)}{\zeta(s)^2}
=\frac{m}{h(\rho)}(s-\rho)^{-m-1}
+O\bigl((s-\rho)^{-m}\bigr).
\tag{9}
\]

Because every nontrivial zero has `rho!=0,1`, the coefficient of the order-`m+1` term in the first summand of `(3)` is nonzero. The second summand of `(3)` contains only `1/zeta(s)` and therefore has pole order `m`. It cannot cancel `(9)`.

Hence every nontrivial zero of `zeta` is a genuine singularity of the meromorphic continuation of the Mellin transform in `(3)`, with pole order one larger than its multiplicity as a zeta zero.

## 3. The square-root bound implies RH

Assume that for every `epsilon>0`,

\[
C(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{10}
\]

Fix any `s` with `Re(s)>1/2`. Choose `epsilon` with

\[
0<\varepsilon<\Re(s)-1/2.
\]

Then the Mellin integral

\[
\int_1^\infty C(x)x^{-s-1}\,dx
\]

converges absolutely and locally uniformly near `s`, so it defines a holomorphic function throughout `Re(s)>1/2`. On `Re(s)>1` it equals `(3)`, hence it is a holomorphic continuation of that expression into the entire half-plane.

Section 2 shows that `(3)` would have a nonremovable pole at any zeta zero with real part greater than `1/2`. Therefore no such zero exists. The functional equation gives the usual symmetry of nontrivial zeros about `Re(s)=1/2`, so all nontrivial zeros lie on the critical line: RH follows.

## 4. RH implies the square-root bound

Under RH, the standard Mertens criterion gives, for every `eta>0`,

\[
M(x)=O_\eta(x^{1/2+\eta}).
\tag{11}
\]

Let

\[
L(x):=\sum_{n\le x}\mu(n)\log n,
\qquad
m(x):=\sum_{n\le x}\frac{\mu(n)}n.
\]

Partial summation gives

\[
L(x)=M(x)\log x-\int_1^x\frac{M(t)}t\,dt.
\tag{12}
\]

Thus `(11)` implies

\[
L(x)=O_\eta(x^{1/2+2\eta})
\tag{13}
\]

after absorbing the logarithm into an arbitrarily small power.

The prime number theorem gives `sum_(n>=1) mu(n)/n=0`. Together with partial summation and `(11)`,

\[
m(x)
=\frac{M(x)}x-\int_x^\infty\frac{M(t)}{t^2}\,dt
=O_\eta(x^{-1/2+\eta}).
\tag{14}
\]

Using `(4)`, equations `(13)` and `(14)` yield

\[
C(x)=O_\eta(x^{1/2+2\eta}).
\]

Renaming `2 eta` as `epsilon` proves the reverse implication in `(2)`.

## 5. Finite-prefix transform is triangular and invertible

Equation `(4)` can be written for integer `N` as

\[
C_N
=-\sum_{n\le N}\mu(n)\log n-Nm_N.
\tag{15}
\]

Subtract the same identity at `N-1`. Since

\[
m_N=m_{N-1}+\frac{\mu(N)}N,
\]

one obtains exactly `(5)`:

\[
C_N-C_{N-1}
=-m_{N-1}-(1+\log N)\mu(N).
\]

Starting from `m_0=0`, this gives the recursion

\[
\mu(N)
=-\frac{C_N-C_{N-1}+m_{N-1}}{1+\log N},
\tag{16}
\]

and then `m_N` is updated from the recovered `mu(N)`. Thus every finite prefix of the correlation sequence contains exactly enough information to reconstruct the corresponding finite Möbius prefix.

This is an information statement, not a stable-norm estimate. The inversion uses discrete differences of `C_N`; a small pointwise upper bound for `C_N` does not automatically give a comparably small bound for `M(N)`. What `(16)` rules out is only the interpretation that the prime-error correlation creates an additional independent data stream at the finite-object level.

## 6. Prior art and novelty boundary

Every ingredient used above is classical: Möbius inversion, `1/zeta(s)=sum mu(n)n^{-s}` for `Re(s)>1`, `sum Lambda(n)n^{-s}=-zeta'(s)/zeta(s)`, Mellin/partial summation, the prime number theorem, the standard RH-equivalent Mertens bound, and the zero symmetry from the functional equation.

A targeted literature/web search on 20 September 2026 for the exact kernel `sum mu(a)(psi(x/a)-x/a)`, its Mellin transform and the `zeta'/zeta^2` expression found standard sources for the component identities and the classical Mertens/RH criterion, but no reliable basis for claiming the packaged criterion `(2)` as a new theorem. No novelty claim is made. The durable result is the line-local obstruction: the specific signed correlation left open by `MC-407` is itself an RH-scale criterion and its transform has *higher*, not lower, pole order at zeta zeros.

This changes how that branch should be evaluated. A future proof of `(10)` would of course be decisive, but the quantity should not be treated as an easier auxiliary statistic merely because it visibly mixes Möbius and prime-counting error.

## Boundaries and falsification tests

- **The criterion is at the `O_epsilon(x^(1/2+epsilon))` scale.** No claim is made here that every weaker quantitative bound for `C` is exactly equivalent to the corresponding bound for `M`.
- **Finite invertibility is not norm equivalence.** Equation `(16)` reconstructs `mu` exactly but differentiation can amplify errors; it does not turn an arbitrary pointwise estimate for `C` into the same exponent for `M`.
- **A new proof method is not ruled out.** An independently proved cancellation theorem for `C` may still solve RH. The obstruction is only to treating `C` as a pre-existing easier source of information.
- **No factorwise estimate suffices automatically.** `MC-407` already showed that taking absolute values after a pointwise bound on `E` gives only linear scale. This finding adds that the fully signed square-root target is itself RH-equivalent.
- **Multiplicity is handled.** A zeta zero of multiplicity `m` creates an order-`m+1` pole in the first term of `(3)`, so the lower-order `1/zeta` term cannot remove it.

## Consequence for the research line

The first exit left after `MC-407` is now classified more sharply. The scalar signed convolution

\[
\sum_{a\le x}\mu(a)E(x/a)
\]

contains no independent finite-prefix information and, at the only endpoint strong enough to reach the critical line directly, satisfies an RH-equivalent bound. Therefore continuing this branch by searching for generic pointwise estimates, transform changes, or a claim that the prime-error factor itself is an extra observable is unlikely to reduce the problem.

A productive continuation must instead identify a theorem whose **proof input** is genuinely additional before scalarization—for example a retained congruence/phase/translation variable inside the quotient fibers, a nonseparable bilinear structure, or another arithmetic relation that yields the signed bound without already assuming an RH-strength Mertens estimate. This shifts the live frontier back toward the retained-variable branch of the accepted source-frame clue.