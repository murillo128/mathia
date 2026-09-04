# MC-061 — A single weighted quadratic Möbius fit forces twisted-Möbius uniformity blow-up

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CONTROL`, `CLASSICAL-IDENTITY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

Fix `X>=2`. Let `q>X` be an odd prime and let

\[
\chi(n)=\left(\frac{n}{q}\right)
\]

be its primitive quadratic character. As in `MC-060`, measure weighted agreement with the Möbius prime sign by

\[
A_X(\chi)
:=
\sum_{p\le X}\frac{|1+\chi(p)|}{p-1}.
\tag{1}
\]

Suppose that for some fixed `eta in (0,1]`,

\[
\boxed{A_X(\chi)\le 1-\eta.}
\tag{2}
\]

Write `lambda(n)=(-1)^{Omega(n)}` for the Liouville function and define

\[
G_\chi(X)
:=
\sum_{n\le X}\lambda(n)\chi(n),
\qquad
T_\chi(y)
:=
\sum_{n\le y}\mu(n)\chi(n).
\tag{3}
\]

Then the approximate quadratic Möbius fit is automatically a linearly biased Liouville-character product:

\[
\boxed{G_\chi(X)\ge \eta X.}
\tag{4}
\]

Moreover the classical square-divisor relation between Liouville and Möbius gives the exact finite-scale identity

\[
\boxed{
G_\chi(X)
=
\sum_{d\le\sqrt X}
T_\chi\!\left(\frac{X}{d^2}\right).
}
\tag{5}
\]

Consequently, for `0<=alpha<1`, put

\[
C_{\chi,X}(\alpha)
:=
\sup_{1\le y\le X}
\frac{|T_\chi(y)|}{y^\alpha}.
\tag{6}
\]

If

\[
H_N^{(s)}:=\sum_{d\le N}d^{-s},
\]

then `(4)` and `(5)` force the quantitative uniformity lower bound

\[
\boxed{
C_{\chi,X}(\alpha)
\ge
\frac{\eta X^{1-\alpha}}
{H_{\lfloor\sqrt X\rfloor}^{(2\alpha)}}.
}
\tag{7}
\]

In particular,

\[
\boxed{
C_{\chi,X}(\alpha)
\gg_{\alpha}
\begin{cases}
\eta\sqrt X,&0\le\alpha<1/2,\\[2mm]
\eta\sqrt X/\log X,&\alpha=1/2,\\[2mm]
\eta X^{1-\alpha},&1/2<\alpha<1.
\end{cases}
}
\tag{8}
\]

Thus the one-certificate quadratic escape left open by `MC-060` cannot be completed by attaching to the selected character a family-uniform power-saving theorem for its twisted Möbius sums. If a moving quadratic character remains within a fixed generator-weighted neighborhood `(2)` of the Möbius prime law at scale `X`, then **every** estimate

\[
|T_\chi(y)|\le C_X y^\alpha
\qquad(1\le y\le X)
\tag{9}
\]

with fixed `alpha<1` must pay a polynomially growing constant `C_X` of at least the size in `(8)`.

This does not rule out the existence of one isolated approximate quadratic certificate and does not bound `M(X)`. It closes a narrower bootstrap: twisted-Möbius cancellation for the same moving character cannot provide a scale-uniform sublinear certificate while the character remains sufficiently close to the Möbius prime signs.

## 1. The Möbius prime fit makes `lambda chi` principal-like on the whole prefix

Set

\[
g(n)=\lambda(n)\chi(n).
\tag{10}
\]

Because `q>X`, every integer `n<=X` is coprime to `q`, so `chi(n)` has modulus one. Since `chi` is quadratic and `lambda` takes values `+-1`,

\[
g(n)\in\{-1,+1\}
\qquad(n\le X).
\]

At every observed prime,

\[
g(p)=-\chi(p),
\]

and therefore

\[
|1-g(p)|=|1+\chi(p)|.
\tag{11}
\]

For any factorization `n=prod_p p^{v_p(n)}`, complete multiplicativity and repeated use of

\[
|1-zw|\le |1-z|+|1-w|
\qquad(|z|=|w|=1)
\]

give

\[
|1-g(n)|
\le
\sum_p v_p(n)|1-g(p)|.
\tag{12}
\]

Summing over `n<=X` and counting prime-generator occurrences exactly as in `MC-059` and `MC-060`,

\[
\begin{aligned}
\sum_{n\le X}|1-g(n)|
&\le
\sum_{p\le X}|1-g(p)|
\sum_{j\ge1}\left\lfloor\frac{X}{p^j}\right\rfloor\\
&\le
X\sum_{p\le X}\frac{|1+\chi(p)|}{p-1}\\
&=XA_X(\chi).
\end{aligned}
\tag{13}
\]

Here the real sign-valued setting is even simpler than the complex phase setting. Since `g(n)=+-1`, every `1-g(n)` is nonnegative, so

\[
\begin{aligned}
G_\chi(X)
&=X-\sum_{n\le X}(1-g(n))\\
&=X-\sum_{n\le X}|1-g(n)|\\
&\ge X(1-A_X(\chi))\\
&\ge\eta X.
\end{aligned}
\tag{14}
\]

This proves `(4)`.

The transformation is intrinsic to the quadratic survivor. Squaring `chi` destroys the character and is therefore useless for Burgess (`MC-059`), but multiplying by Liouville removes the common target sign `-1` at the observed primes without making the resulting completely multiplicative function globally principal. The price is that `lambda chi` is no longer a Dirichlet character, so Burgess cannot be applied directly.

## 2. Quadraticity converts Liouville into a square convolution of twisted Möbius

The classical Liouville identity anchored by `MC-S9` is

\[
\lambda(n)
=
\sum_{d^2\mid n}
\mu\!\left(\frac{n}{d^2}\right).
\tag{15}
\]

Multiply `(15)` by `chi(n)` and write `n=d^2m`. If `n<=X`, then `d<q` because `q>X`, so quadraticity gives

\[
\chi(d^2)=1.
\tag{16}
\]

Hence

\[
\lambda(d^2m)\chi(d^2m)
=
\mu(m)\chi(m)
\]

inside the square-divisor expansion, and summing over `n<=X` yields

\[
\begin{aligned}
G_\chi(X)
&=
\sum_{d\le\sqrt X}
\sum_{m\le X/d^2}
\mu(m)\chi(m)\\
&=
\sum_{d\le\sqrt X}
T_\chi(X/d^2),
\end{aligned}
\]

which is `(5)`.

At the Dirichlet-series level the same classical identity is

\[
\sum_{n\ge1}\frac{\lambda(n)\chi(n)}{n^s}
=
\frac{L(2s,\chi^2)}{L(s,\chi)}
\qquad(\operatorname{Re}s>1).
\tag{17}
\]

For quadratic prime-conductor `chi`, `chi^2` is principal and

\[
L(2s,\chi^2)=\zeta(2s)(1-q^{-2s}).
\tag{18}
\]

Thus `(5)` is the finite coefficient-level form of a standard `L(2s,chi^2)/L(s,chi)` factorization. No analytic continuation or zero-free region is needed for the proof of the finite-scale obstruction.

## 3. Any sublinear twisted-Möbius exponent must carry a growing family constant

By definition of `(6)`, for every `d<=sqrt X`,

\[
\left|T_\chi(X/d^2)\right|
\le
C_{\chi,X}(\alpha)
X^\alpha d^{-2\alpha}.
\tag{19}
\]

Combining `(4)`, `(5)`, and the triangle inequality gives

\[
\eta X
\le
|G_\chi(X)|
\le
C_{\chi,X}(\alpha)X^\alpha
\sum_{d\le\sqrt X}d^{-2\alpha}.
\tag{20}
\]

This proves `(7)` exactly.

The three regimes in `(8)` are simply the classical asymptotics of generalized harmonic sums. If `alpha>1/2`,

\[
H_{\lfloor\sqrt X\rfloor}^{(2\alpha)}
\le\zeta(2\alpha),
\]

so

\[
C_{\chi,X}(\alpha)
\ge
\frac{\eta}{\zeta(2\alpha)}X^{1-\alpha}.
\tag{21}
\]

At the critical exponent `alpha=1/2`,

\[
H_{\lfloor\sqrt X\rfloor}^{(1)}
\ll\log X,
\]

which gives the middle line of `(8)`. For `alpha<1/2`,

\[
H_{\lfloor\sqrt X\rfloor}^{(2\alpha)}
\ll_\alpha X^{1/2-\alpha},
\]

so the exponent simplifies to `1/2` independently of `alpha`.

The exact inequality `(7)` is preferable to the case split whenever constants matter. It also shows that some reciprocal-square scale `y=X/d^2` must carry the corresponding large normalized twisted-Möbius sum; the obstruction is not an artifact of asking for control at every real scale independently.

## 4. Why this is a genuine uniformity obstruction rather than a new zero-free theorem

For one fixed character, a global estimate

\[
T_\chi(y)\ll y^\alpha
\qquad(y\to\infty)
\]

with `alpha<1` would analytically continue `1/L(s,chi)` into `Re(s)>alpha` by partial summation and hence exclude zeros of `L(s,chi)` there. That classical analytic burden is one reason twisted Möbius sums are hard.

The present result is different and purely finite-scale. It does not assume or prove any zero-free region for `L(s,chi)`. It says that if `chi=chi_X` itself moves with the observation scale so as to approximate the Möbius prime signs, then the constant in any putative twisted-Möbius power bound **already has to deteriorate polynomially before any asymptotic zero-free argument is invoked**.

This is exactly the failure mode that `MC-055` exposed for the square-free comparator `mu^2 chi_X`, but now on the natural reciprocal `L`-function object `mu chi_X`. The two obstructions are not the same calculation. `MC-055` lower-bounded a generic cancellation constant by exact coefficient agreement with `M(X)`; here approximate prime agreement first creates a linear `lambda chi` mean, and the classical square-divisor convolution then forces a quantitative blow-up in the normalized twisted-Möbius sums.

The result therefore supplies an explicit answer to one natural continuation of `MC-060`: replacing the missing quadratic Burgess step by a theorem for `sum mu(n)chi(n)` cannot be uniform enough to close the bootstrap while `(2)` holds.

## 5. Prior art and novelty boundary

The square-divisor identity `(15)` is classical and already anchored by `MC-S9`; its twisted form follows immediately because a Dirichlet character is completely multiplicative. The Dirichlet-series identity `(17)` is the corresponding standard Euler-product calculation.

Twisted Mertens sums

\[
M(x,\chi)=\sum_{n\le x}\mu(n)\chi(n)
\]

are established objects in analytic number theory. A targeted audit of that literature found, among other examples, Banks and Shparlinski, *Sums with the Möbius function twisted by characters with powerful moduli*, Transactions of the American Mathematical Society 373 (2020), 249–272, DOI `10.1090/tran/7914`, arXiv `1801.10276`. Their results concern special powerful moduli and use zero-free information for the relevant Dirichlet `L`-functions; they do **not** supply a bound in the prime-conductor moving regime of this finding. They are cited only to mark the twisted-Möbius/zero-free mechanism as established prior art.

The generator-to-prefix inequality `(13)` is the same elementary multiplicative telescoping mechanism already used in `MC-059` and `MC-060`. The new Mathia-specific content is the exact combination of that inequality with the quadratic `lambda`/`mu` square convolution to quantify the **single-certificate** uniformity cost left open by `MC-060`. No standalone novelty claim is made for the identities, twisted sums, or analytic machinery.

## 6. Boundaries and falsification tests

The conclusion is deliberately narrow.

- The modulus is an odd prime `q>X` and `chi` is quadratic. The condition `q>X` prevents character zeros inside the observed prefix and makes `chi(d^2)=1` in `(16)`.
- The defect must leave a fixed gap below one. If `A_X(chi)` approaches or exceeds one, `(14)` no longer guarantees a linear `lambda chi` mean.
- The theorem constrains the family constant in twisted-Möbius sums; it does not lower-bound the conductor `q`, does not rule out one isolated approximate quadratic certificate, and does not bound `M(X)`.
- The result does not say that the actual twisted-Möbius sum is large at `y=X`. The large normalized value may occur at one of the reciprocal-square scales `X/d^2` entering `(5)`.
- A theorem with explicit conductor dependence is not contradicted. Instead `(7)` supplies a necessary lower bound on whatever conductor-dependent constant that theorem produces for this specially selected family.
- Higher-order characters require a different square factor because `chi(d^2)` is then not identically one; those are already constrained directly by `MC-059`.
- The proof uses only triangle inequalities after `(5)`. A genuinely signed relation among the reciprocal-square scales could still contain additional information, but it cannot produce a uniform pointwise `y^alpha` bound for every scale without paying `(7)`.

The main claim is falsified if the generator occurrence bound in `(13)` fails, if the classical identity `(15)` is incorrect, if quadraticity does not imply `(16)` under `q>X`, or if `(20)` does not follow from the definition of `C_{chi,X}(alpha)`. Each step is exact and finite.

## Consequence for the active frontier

`MC-060` left one possible low-conductor approximate quadratic certificate at each scale because pairwise Burgess repulsion cannot constrain a singleton. `MC-061` shows that this survivor cannot be made useful merely by proving a sublinear twisted-Möbius exponent for each frozen certificate and ignoring how the implied constant changes with the selected character.

Under a fixed weighted agreement gap, the moving family necessarily contains twisted-Möbius sums whose normalized constants grow polynomially at **every fixed exponent below one**. The surviving question must therefore use information not reducible to a family-uniform bound on `sum mu(n)chi_X(n)`: for example, a multiscale constraint on how the single quadratic certificate evolves, a conductor-sensitive relation that does more than bound each twisted sum separately, or a signed coupling that survives the reciprocal-square aggregation in `(5)`.

This narrows the single-quadratic comparator frontier without claiming to close it.