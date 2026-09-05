# MC-071 — Signed inversion of the quadratic feedback kernel already carries both zeta and Dirichlet-L zero-free information

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the square-free quadratic comparator of `MC-066`--`MC-070`. Let `q` be an odd prime,

\[
\chi(n)=\left(\frac{n}{q}\right),
\qquad
f_\chi(n)=\mu(n)^2\chi(n),
\qquad
h_\chi=1*f_\chi,
\]

so that

\[
f_\chi=\mu*h_\chi.
\tag{1}
\]

`MC-070` closes the simplest positive-triangle feedback route by showing that the nonnegative kernel `h_chi` has too much power-weighted mass throughout every fixed conductor range `q<=X^A`, `A<2`, at every exponent bounded away from `1`.

There is a formally natural signed escape: invert the convolution before taking absolute values. Let

\[
k_\chi:=h_\chi^{-1}
\]

be the Dirichlet inverse. Then

\[
\boxed{\mu=f_\chi*k_\chi}
\tag{2}
\]

and, if

\[
F_\chi(X)=\sum_{n\le X}f_\chi(n),
\]

one has the exact finite recovery formula

\[
\boxed{
M(X)=\sum_{d\le X}k_\chi(d)F_\chi(X/d).
}
\tag{3}
\]

The inverse is genuinely signed, but its cancellation is not an independent cheap datum. Its Dirichlet series is

\[
\boxed{
K_\chi(s)
:=\sum_{n\ge1}\frac{k_\chi(n)}{n^s}
=
\frac{L(2s,\chi^2)}{\zeta(s)L(s,\chi)}
}
\qquad(\operatorname{Re}s>1).
\tag{4}
\]

For prime quadratic `chi`,

\[
L(2s,\chi^2)=\zeta(2s)(1-q^{-2s}),
\tag{5}
\]

which is holomorphic and zero-free throughout the open half-plane `Re(s)>1/2`. Consequently, for every fixed

\[
\frac12\le\alpha<1,
\]

a power bound

\[
\boxed{
\sum_{n\le x}k_\chi(n)=O(x^\alpha)
}
\tag{6}
\]

forces simultaneously

\[
\boxed{
\zeta(s)\ne0
\quad\text{and}\quad
L(s,\chi)\ne0
\qquad(\operatorname{Re}s>\alpha).
}
\tag{7}
\]

In particular, if for every `epsilon>0`

\[
\sum_{n\le x}k_\chi(n)
=O_\varepsilon(x^{1/2+\varepsilon}),
\tag{8}
\]

then RH holds for `zeta`, and the generalized Riemann hypothesis holds for this primitive quadratic Dirichlet `L`-function.

Thus replacing the failed positive estimate of `MC-070` by a black-box square-root cancellation theorem for the **inverse kernel itself** does not evade the zero-information burden: it asks for a statement at least as strong as RH and, for a fixed comparator, also the corresponding Dirichlet-L GRH.

At the same time, coefficientwise absolute inversion remains unusable below exponent `1`. For fixed `chi`,

\[
\boxed{
\sum_{n\ge1}\frac{|k_\chi(n)|}{n^\sigma}
<\infty
\quad\Longleftrightarrow\quad
\sigma>1.
}
\tag{9}
\]

Therefore the current signed-feedback frontier is narrower than merely "do not take the triangle inequality." A surviving proof must exploit **joint signed structure between** `k_chi(d)` **and** `F_chi(X/d)` (or an equivalent coupled recurrence), rather than first proving RH-scale cancellation for `k_chi` as a standalone sequence and then inserting it into `(3)`.

No improved bound for `M(X)` is claimed.

## 1. Exact local inverse

From `MC-066`, for every `a>=1`,

\[
h_\chi(p^a)=
\begin{cases}
0,&p\ne q,\ \chi(p)=-1,\\
2,&p\ne q,\ \chi(p)=+1,\\
1,&p=q.
\end{cases}
\tag{10}
\]

Write `z` for the local prime-power variable. At a split prime, `chi(p)=+1`,

\[
H_p(z)
=1+2z+2z^2+\cdots
=\frac{1+z}{1-z},
\]

so

\[
H_p(z)^{-1}
=\frac{1-z}{1+z}
=1+2\sum_{a\ge1}(-1)^a z^a.
\tag{11}
\]

At an inert prime, `chi(p)=-1`, one has `H_p(z)=1`. At the conductor prime,

\[
H_q(z)=\frac1{1-z},
\qquad
H_q(z)^{-1}=1-z.
\tag{12}
\]

Hence the inverse coefficients are exactly

\[
\boxed{
k_\chi(p^a)=
\begin{cases}
2(-1)^a,&p\ne q,\ \chi(p)=+1,\\
0,&p\ne q,\ \chi(p)=-1,\\
-1,&p=q,\ a=1,\\
0,&p=q,\ a\ge2.
\end{cases}}
\tag{13}
\]

The convolution identity `(2)` follows immediately from `k_chi*h_chi=varepsilon` and `(1)`, and summing `(2)` through `X` gives `(3)`. These are finite coefficient identities; they use no analytic continuation or zero-free hypothesis.

## 2. The inverse factorizes into two Möbius-type zero-sensitive sequences

In `Re(s)>1`, `MC-066` gives

\[
\sum_{n\ge1}\frac{h_\chi(n)}{n^s}
=
\frac{\zeta(s)L(s,\chi)}{L(2s,\chi^2)}.
\tag{14}
\]

Taking the reciprocal proves `(4)`. The same identity can be read coefficientwise without any continuation. Define the square-supported function

\[
r_\chi(n)=
\begin{cases}
\chi^2(m),&n=m^2,\\
0,&\text{otherwise}.
\end{cases}
\tag{15}
\]

Then

\[
\sum_{n\ge1}\frac{r_\chi(n)}{n^s}=L(2s,\chi^2),
\]

while the classical Euler products give

\[
\frac1{\zeta(s)}
=\sum_{n\ge1}\frac{\mu(n)}{n^s},
\qquad
\frac1{L(s,\chi)}
=\sum_{n\ge1}\frac{\mu(n)\chi(n)}{n^s}
\qquad(\operatorname{Re}s>1).
\tag{16}
\]

Therefore

\[
\boxed{
k_\chi=\mu*(\mu\chi)*r_\chi.}
\tag{17}
\]

Equation `(17)` makes the analytic burden in the signed inverse transparent. The inverse is not a newly generated source of randomness: it contains simultaneously the reciprocal-zeta Möbius factor and the reciprocal-Dirichlet-L twisted Möbius factor, softened only by a square-supported factor whose Dirichlet series is zero-free to the right of the critical line.

## 3. Absolute inversion still has abscissa one

Equation `(13)` gives

\[
|k_\chi(p)|=2
\]

for every split prime `p` with `chi(p)=+1`. For a fixed nonprincipal quadratic character, standard prime distribution in arithmetic progressions gives a positive density of such primes. In particular,

\[
\sum_{\substack{p\\\chi(p)=+1}}\frac1p=\infty,
\tag{18}
\]

and more generally the corresponding prime sum diverges for every real exponent `sigma<=1`.

Thus the prime terms alone force divergence of the absolute series in `(9)` when `sigma<=1`. Conversely, `(13)` gives

\[
|k_\chi(n)|\le d(n),
\tag{19}
\]

so absolute convergence follows for every `sigma>1`. This proves `(9)`.

Consequently, if one knows only a comparator bound

\[
|F_\chi(y)|\le C y^\theta,
\]

then the coefficientwise use of `(3)` gives

\[
|M(X)|
\le
CX^\theta
\sum_{d\le X}\frac{|k_\chi(d)|}{d^\theta},
\tag{20}
\]

and no fixed exponent `theta<1` can close through an `X`-independent absolute inverse norm. The signed inverse is therefore a genuine structural escape from the **positive** feedback kernel, but not from the absolute-inversion obstruction already encountered elsewhere in this line.

## 4. Standalone power cancellation of the inverse forces two zero-free half-planes

Assume `(6)` for some `alpha>=1/2`. Partial summation gives a locally uniformly convergent holomorphic continuation of the Dirichlet series `K_chi(s)` to

\[
\operatorname{Re}s>\alpha.
\tag{21}
\]

On `Re(s)>1`, this holomorphic function agrees with the quotient `(4)` by absolute convergence. Uniqueness of meromorphic continuation therefore preserves `(4)` throughout `Re(s)>alpha` wherever the classical factors are defined.

For prime quadratic `chi`, equation `(5)` shows that its numerator has no zero in `Re(s)>1/2`: `zeta(2s)` is zero-free for `Re(2s)>1`, and `|q^{-2s}|<1` there. If either `zeta` or `L(s,chi)` had a zero `rho` with

\[
\operatorname{Re}\rho>\alpha,
\]

then the right-hand side of `(4)` would have a pole at `rho`, because its numerator is finite and nonzero there. This contradicts the holomorphy in `(21)`. Hence `(7)` follows.

If `(8)` holds, apply the same argument in every half-plane `Re(s)>1/2+epsilon`; there can be no zero of either denominator factor with real part strictly greater than `1/2`. The functional equations for `zeta` and for the primitive real character `chi` reflect nontrivial zeros across the critical line, so this is RH for `zeta` and GRH for `L(s,chi)`.

This is the same general analytic-nonmasking principle already isolated in `MC-008`, but applied here to the **inverse kernel of the current quadratic feedback architecture**. The important difference is structural: the numerator is now zero-free while the denominator contains two independent zero divisors, so inverse-kernel cancellation carries more, not less, analytic zero information than the original Mertens target.

## 5. Prior art and novelty boundary

No standalone novelty is claimed for the Euler products, Dirichlet inversion, `(16)`, or the partial-summation implication from power cancellation to a zero-free half-plane. The identity `1/L(s,chi)=sum mu(n)chi(n)n^{-s}` is classical Dirichlet-series theory; `MC-S15` supplies the surrounding standard Dirichlet-character and prime-distribution machinery used in `(18)`. A targeted search found the reciprocal-Dirichlet-L identity and standard uses of twisted Möbius cancellation under GRH, but no reason to reclassify these ingredients as new analytic-number-theory theorems.

The closest internal prior-art boundary is `MC-008`, which already proves that holomorphy of an auxiliary multiplicative Dirichlet series can retain RH information even when its absolute inverse is unusable. Venturini (`MC-S17`) is the broader literature anchor for the established principle that analytic continuation/nonvanishing properties of auxiliary multiplicative Dirichlet series can constrain zeta zeros. `MC-050` and `MC-054` separately show, in different comparator classes, that sufficiently strong fixed global proximity plus power cancellation can also force the corresponding zero-free problem.

The durable contribution here is therefore narrower and line-specific: it audits the **exact signed inverse left open by MC-070** and identifies its denominator as `zeta(s)L(s,chi)`. This converts the vague escape "use cancellation in the feedback instead of positivity" into a sharper boundary. Cancellation of the inverse kernel as a standalone sequence is itself zero-sensitive at both the Riemann and quadratic-Dirichlet levels; any genuinely cheaper escape must exploit cancellation in the coupled convolution `(3)` that is not reducible to a black-box bound for either factor alone.

## 6. Boundaries and falsification tests

The result does not rule out all signed uses of `(3)`.

- It does **not** say that a useful bilinear, recursive, oscillatory, or scale-coupled estimate for `sum k_chi(d)F_chi(X/d)` would imply GRH for `L(s,chi)` before yielding information on `M(X)`. The zero-free conclusion is attached specifically to a standalone power bound for the partial sums of `k_chi`.
- It does not exclude cancellation among the original feedback terms `h_chi(d)M(X/d)` without explicit inversion. Such an argument could use arithmetic dependence between `h_chi` and the Mertens values rather than an independent norm of `h_chi` or `k_chi`.
- The zero-free argument uses `alpha>=1/2` so that the numerator in `(4)` is known to be holomorphic and zero-free throughout the tested half-plane. No statement is made about pushing the same quotient through the pole of `zeta(2s)` at the boundary `s=1/2` or farther left.
- The exact abscissa-one assertion is for a fixed quadratic character. A character moving with `X` is a triangular-array problem and cannot be assigned one global Dirichlet-series abscissa in the same way.
- Equation `(20)` rules out only coefficientwise absolute recovery with a fixed inverse norm; it does not quantify the best finite-`X` signed operator norm.

The claim is falsified if any local coefficient in `(13)` is wrong, if the quotient `(4)` fails, if its numerator has a zero in `Re(s)>1/2`, if `(18)` fails for a fixed quadratic character, or if a holomorphic Dirichlet series satisfying `(6)` can retain a pole in `(4)` inside its domain. Each test reduces to explicit convolution algebra or classical analytic-number-theory facts.

## Consequence for the active frontier

`MC-070` closes the positive-kernel triangle contraction for the quadratic comparator throughout every conductor power range below `X^2`, producing a `7/8` floor for the Munsch-plus-positive-feedback package. The present finding closes the most immediate opposite extreme: **invert the kernel, prove square-root cancellation for that inverse independently, and transfer back**. The inverse already encodes `1/(zeta L_chi)`, so an RH-scale standalone estimate for it imports the Riemann target together with an additional Dirichlet-L zero-free target.

The remaining signed route is therefore genuinely relational. It must exploit the joint arithmetic of the two factors in `(3)`, or the signed recurrence in `MC-066`, in a way that does not first solve a zero-free problem for an auxiliary sequence. This is a stricter and more falsifiable next frontier than simply replacing positivity by an unspecified appeal to cancellation.