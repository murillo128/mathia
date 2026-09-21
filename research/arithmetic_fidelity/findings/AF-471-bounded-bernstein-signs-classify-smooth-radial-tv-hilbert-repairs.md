# AF-471 — Bounded Bernstein signs classify smooth radial TV Hilbert repairs

- **Date:** 2026-09-21
- **Status:** proved
- **Research line:** `arithmetic_fidelity`
- **Kind:** metric transform / total variation / conditional negative type / bounded Bernstein class / histogram intersection / Hilbert repair
- **Depends on:** AF-466, AF-470
- **Classification:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + LINE-SPECIFIC-CLASSIFICATION + NO-NOVELTY-CLAIM`

## Claim

Let `A` be an infinite discrete alphabet and let `Delta(A)` be its finitely supported probability simplex with

\[
d(\mu,\nu)=\|\mu-\nu\|_1\in[0,2].
\]

Let

\[
g:[0,2]\to[0,\infty),\qquad g(0)=0,
\]

be continuous on `[0,2]` and smooth on `(0,2)`. Then the following are equivalent.

1. For every finite family in `Delta(A)`, the kernel
   \[
   K_g(\mu,\nu)=g(d(\mu,\nu))
   \]
   is conditionally negative definite, equivalently it is a squared Hilbert distance on every finite subset.

2. `g` obeys the bounded Bernstein sign hierarchy
   \[
   \boxed{
   (-1)^{k-1}g^{(k)}(t)\ge0
   \qquad(k\ge1,\ 0<t<2).
   }
   \tag{1}
   \]

3. There is a summable sequence `a_n>=0`, `n>=1`, with
   \[
   \sum_{n\ge1}a_n=g(2),
   \]
   such that for every `0<=t<=2`,
   \[
   \boxed{
   g(t)=\sum_{n\ge1}a_n
   \left[1-\left(1-\frac t2\right)^n\right].
   }
   \tag{2}
   \]

Thus the sufficiency question left open by AF-470 is closed for the natural continuous/smooth radial class. On the bounded probability simplex, exact scalar Hilbert repair does **not** require `g` to extend to a Bernstein function on `[0,infinity)`. The exact smooth class is instead the bounded-interval Bernstein class `(1)`, equivalently the nonnegative overlap-power mixture `(2)`.

Moreover, `(2)` gives an explicit Hilbert embedding, not merely a conditional-negative-type certificate.

## Overlap turns TV into an inner-product coordinate

Use the AF-466 subgraph embedding

\[
\Phi(\mu)(a,s)=\mathbf 1_{[0,\mu(a)]}(s)
\]

in

\[
H_0=L^2(A\times[0,1],\#\otimes ds).
\]

Every `Phi(mu)` is a unit vector, and

\[
\begin{aligned}
S(\mu,\nu)
&=\langle\Phi(\mu),\Phi(\nu)\rangle\\
&=\sum_{a\in A}\min\{\mu(a),\nu(a)\}\\
&=1-\frac12\|\mu-\nu\|_1.
\end{aligned}
\tag{3}
\]

Hence the normalized histogram-intersection kernel `S` is positive definite, takes values in `[0,1]`, has diagonal `1`, and satisfies

\[
d(\mu,\nu)=2(1-S(\mu,\nu)).
\tag{4}
\]

This bounded overlap coordinate is the structure that makes local complete alternation sufficient even when no global Bernstein extension exists.

## From bounded Bernstein signs to nonnegative overlap powers

Assume `(1)` and define

\[
F(u)=g(2)-g(2-2u),\qquad 0\le u\le1.
\tag{5}
\]

For `0<u<1`,

\[
F^{(k)}(u)
=2^k(-1)^{k-1}g^{(k)}(2-2u)
\ge0.
\tag{6}
\]

Thus `F` is absolutely monotone on `(0,1)`. Bernstein's classical analyticity theorem for absolutely monotone functions gives a power series on the unit interval,

\[
F(u)=\sum_{n\ge0}a_nu^n,
\qquad a_n\ge0,
\qquad 0\le u<1.
\tag{7}
\]

Continuity at `u=0` gives `a_0=F(0)=0`. Because the coefficients are nonnegative, monotone convergence as `u\uparrow1`, together with continuity of `g` at zero, gives

\[
\sum_{n\ge1}a_n
=F(1)
=g(2)-g(0)
=g(2).
\tag{8}
\]

Substituting `u=1-t/2` into `(5)`--`(8)` yields exactly `(2)` on the closed interval.

This step is deliberately local. It uses absolute monotonicity on a bounded interval and does not infer a Levy--Khintchine representation on the positive half-line.

## Explicit Hilbert realization

For every `n>=1`, the tensor-power map

\[
\Phi_n(\mu)=\Phi(\mu)^{\otimes n}
\]

is again unit norm and satisfies

\[
\langle\Phi_n(\mu),\Phi_n(\nu)\rangle
=S(\mu,\nu)^n.
\tag{9}
\]

Define the Hilbert direct-sum map

\[
\Psi_g(\mu)
=\bigoplus_{n\ge1}
\sqrt{\frac{a_n}{2}}\,\Phi_n(\mu).
\tag{10}
\]

The series is well defined because `sum a_n=g(2)<infinity`. Using `(9)`,

\[
\begin{aligned}
\|\Psi_g(\mu)-\Psi_g(\nu)\|^2
&=\sum_{n\ge1}a_n\bigl(1-S(\mu,\nu)^n\bigr)\\
&=g\!\left(2(1-S(\mu,\nu))\right)\\
&=g(d(\mu,\nu)).
\end{aligned}
\tag{11}
\]

So every bounded-Bernstein profile in `(1)` is an exact squared-Hilbert transform of TV on the whole probability simplex.

Equivalently, the positive-definite complement

\[
g(2)-g(d(\mu,\nu))
=\sum_{n\ge1}a_nS(\mu,\nu)^n
\tag{12}
\]

is a nonnegative power mixture of the histogram-intersection kernel. The sufficiency mechanism is therefore an ordinary positive-kernel construction after the TV compression is rewritten in its retained overlap coordinate.

## Necessity

AF-470 proves, without continuity, that exact conditional negative definiteness of `g(d)` on the unrestricted simplex forces

\[
(-1)^{k-1}
\Delta_{\epsilon_1}\cdots\Delta_{\epsilon_k}g(x)\ge0
\]

whenever `x+sum epsilon_i<=2`. Under the present smoothness hypothesis, divide by the increments and let them tend to zero. This gives `(1)` for every order and every interior point.

Combining AF-470 with the sufficiency argument above proves the claimed equivalence in the continuous/smooth class.

## The bounded class is strictly larger than global Bernstein restrictions

Consider

\[
g_*(t)=t-\frac{t^2}{4}+\frac{t^3}{24},
\qquad 0\le t\le2.
\tag{13}
\]

Then

\[
g_*'(t)=1-\frac t2+\frac{t^2}{8}>0,
\qquad
g_*''(t)=\frac{t-2}{4}\le0,
\qquad
g_*'''(t)=\frac14>0,
\tag{14}
\]

and all higher derivatives vanish. Hence `g_*` satisfies `(1)` on `[0,2]`.

Its overlap transform is especially simple:

\[
g_*(2)-g_*(2-2u)
=u+\frac{u^3}{3}.
\tag{15}
\]

Therefore

\[
\boxed{
g_*(d)=
\left[1-S\right]
+\frac13\left[1-S^3\right],
}
\tag{16}
\]

and `(10)` uses only the first and third tensor powers.

But `g_*` cannot be the restriction of any Bernstein function on `[0,infinity)`. A global Bernstein function is real analytic on `(0,infinity)` through the Bernstein--Widder/Laplace representation of its completely monotone derivative. Agreement with the polynomial `(13)` on the open interval `(0,2)` would force agreement everywhere by analytic continuation, while

\[
g_*''(t)=\frac{t-2}{4}>0
\qquad(t>2),
\]

contradicting the concavity of every Bernstein function.

Thus the compact TV diameter creates genuine extra exact-Hilbert transforms that the global Manhattan/Bernstein classification does not allow.

## Prior-art audit

The ingredients are classical and no theorem-level novelty is claimed for absolute monotonicity, positive-definite power series, histogram-intersection kernels, tensor-power kernels, or Schoenberg theory.

- S. N. Bernstein, **“Sur les fonctions absolument monotones,”** *Acta Mathematica* 52 (1928/29), 1--66, DOI `10.1007/BF02592679`. Bernstein's little theorem supplies analyticity and nonnegative Taylor coefficients for absolutely monotone functions on a bounded interval.
- I. J. Schoenberg, **“Positive Definite Functions on Spheres,”** *Duke Mathematical Journal* 9 (1942), 96--108, DOI `10.1215/S0012-7094-42-00908-6`. Schoenberg's Hilbert-sphere theory is the classical source behind nonnegative power expansions of inner-product kernels.
- Josh Alman, Timothy Chu, Gary Miller, Shyam Narayanan, Mark Sellke and Zhao Song, **“Metric Transforms and Low Rank Matrices via Representation Theory of the Real Hyperrectangle,”** arXiv:`2011.11503`. Their global Manhattan-transform classification identifies Bernstein functions as the exact whole-half-line class for transforming Manhattan distances to squared Euclidean distances.
- Chunsheng Ma, **“Vector Random Fields on the Probability Simplex with Metric-Dependent Covariance Matrix Functions,”** *Journal of Theoretical Probability* 36 (2023), 1922--1938, DOI `10.1007/s10959-022-01217-6`. This is adjacent probability-simplex prior art on metric-dependent positive/negative definite kernels.

A targeted search did not locate the exact equivalence `(1)`--`(2)` stated for `l1` total variation on the unrestricted probability simplex or the explicit observation that the bounded simplex admits smooth exact transforms such as `(13)` that cannot extend to global Bernstein functions. This absence is not treated as a novelty proof. The result is best classified as a line-specific synthesis of classical Bernstein analyticity, the histogram-intersection Gram representation, Schoenberg power kernels, and AF-470's necessity theorem.

## Boundaries

1. **Smoothness is used only for the present exact equivalence.** AF-470's finite-difference necessity is stronger and requires no continuity. AF-471 does not classify possible endpoint-discontinuous or otherwise nonsmooth completely alternating profiles.

2. **Infinite alphabet breadth is needed only for necessity.** The construction `(10)` proves sufficiency on every finite or countable alphabet. The converse uses AF-470's unlimited private-atom geometry and therefore belongs to the unrestricted simplex.

3. **This is scalar and radial.** Non-radial, marked, anisotropic or provenance-bearing Hilbert representations are outside the classification.

4. **This is exact squared-Hilbert geometry, not bounded distortion.** Approximate embeddings and two-sided distortion remain governed by AF-468-type metric constraints rather than `(2)` alone.

5. **The compact diameter is load-bearing.** The coefficient representation is in powers of `1-t/2`. It is not a Levy--Khintchine representation in the distance variable and need not survive if the source metric is unbounded.

6. **No arithmetic discriminator is created.** The theorem works for arbitrary labels. It identifies the complete smooth scalar-radial transport class for unrestricted probability-law TV geometry; rational-prime specificity must still come from source restrictions or downstream marked structure.

## Consequence for Arithmetic Fidelity

The smooth exact scalar-radial branch is now closed at the representation level. AF-470 gave the full bounded-interval sign obstruction; AF-471 shows that those signs are also sufficient and identifies the exact retained carrier: nonnegative tensor powers of the histogram-intersection overlap.

This changes the next question. There is no remaining need to search for a mysterious scalar radial Hilbert transform between the square root and global Bernstein functional calculus. On the unrestricted probability simplex, the smooth exact class is already explicit. Any arithmetic gain must now come from one of three places: prove that the arithmetic source occupies a much thinner family than the unrestricted mixture simplex; use a non-radial/marked carrier that preserves provenance absent from scalar TV; or prove that a downstream arithmetic operation consumes one of the overlap-power representations without collapsing the discriminator again.