# PC-055 — infinite Möbius birth transform has Euler-product thresholds

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the natural weighted coefficient-Hilbert completion of the infinite Möbius birth/full-root change of basis left open by PC-027. In that completion the transform encounters two unconditional thresholds: at weight exponent `sigma=1/2` it first becomes defined on the coordinate vacuum, while bounded invertibility occurs only for `sigma>1`, the absolute Euler-product region. Neither threshold is a zeta-zero condition, and the critical value `1/2` is only square-summability of the Möbius column.

This does **not** rule out every conceivable renormalized infinite-dimensional determinant or non-diagonal completion. It rules out the most direct attempt to turn the finite determinant-one Möbius basis change of PC-027 into an RH mechanism merely by completing the scale-index coefficients in a standard weighted `l^2` / Hardy-Dirichlet space.

## 1. The infinite basis transform

PC-027 writes the primitive cyclotomic logarithmic fields as

\[
F_n=\sum_{d\mid n}\mu(n/d)V_d,
\qquad
V_d=\Log(1-z^d).
\]

On every finite divisor-closed set this is a lower-triangular determinant-one change of basis. The explicit caveat in PC-027 is that an infinite completion could behave differently if the corresponding Möbius operator ceased to be bounded or determinant-class.

The canonical sequence operator behind that caveat is

\[
\boxed{
(T_\mu x)(n)=\sum_{d\mid n}\mu(n/d)x(d).
}
\]

Its algebraic Dirichlet-convolution inverse is

\[
\boxed{
(T_1x)(n)=\sum_{d\mid n}x(d),
}
\]

because `mu * 1 = epsilon`.

For a real scale weight `sigma`, consider the diagonal coefficient completion

\[
\boxed{
\mathscr H_\sigma
=\left\{x=(x_n):
\|x\|_\sigma^2
=\sum_{n\ge1}|x_n|^2n^{-2\sigma}<\infty
\right\}.
}
\]

This is the natural shifted Hardy-Dirichlet completion: the unitary map

\[
J_\sigma x(s)
=\sum_{n\ge1}x_n n^{-\sigma}n^{-s}
\]

identifies `mathscr H_sigma` with the Hedenmalm-Lindqvist-Seip Hilbert space of Dirichlet series having square-summable coefficients.

## 2. Under the Dirichlet-series map, Möbius inversion is multiplication by shifted reciprocal zeta

Let

\[
y_n=x_n n^{-\sigma}.
\]

Then

\[
(T_\mu x)(n)n^{-\sigma}
=\sum_{dm=n}\mu(m)m^{-\sigma}y_d.
\]

Therefore Dirichlet multiplication gives, initially where the Euler products converge absolutely,

\[
\boxed{
J_\sigma T_\mu J_\sigma^{-1}
=M_{1/\zeta(s+\sigma)},
}
\]

and similarly

\[
\boxed{
J_\sigma T_1 J_\sigma^{-1}
=M_{\zeta(s+\sigma)}.
}
\]

This is the operator-level version of the Möbius factor already exposed in PC-015 and PC-027. The question is not whether zeta appears—it must—but whether the infinite Hilbert completion creates an additional critical boundedness or invertibility condition.

## 3. The first threshold is exactly `sigma=1/2`, but it is only square-summability

Apply the Möbius transform to the coordinate vacuum `e_1`. One gets

\[
T_\mu e_1=(\mu(n))_{n\ge1}.
\]

Hence

\[
\boxed{
\|T_\mu e_1\|_\sigma^2
=\sum_{n\ge1}\frac{\mu(n)^2}{n^{2\sigma}}.
}
\]

For `sigma>1/2`, the classical squarefree Euler product gives

\[
\boxed{
\sum_{n\ge1}\frac{\mu(n)^2}{n^{2\sigma}}
=\frac{\zeta(2\sigma)}{\zeta(4\sigma)}.
}
\]

At `sigma=1/2` the series `sum mu(n)^2/n` diverges, and it also diverges for every smaller `sigma`. Thus

\[
\boxed{
T_\mu e_1\in\mathscr H_\sigma
\iff \sigma>\frac12.
}
\]

The formal inverse has

\[
T_1e_1=(1,1,1,\ldots),
\qquad
\|T_1e_1\|_\sigma^2=\zeta(2\sigma),
\]

so it has the same membership threshold.

This is the first decisive diagnostic. The number `1/2` does appear naturally, but for the elementary reason

\[
\boxed{
\text{squarefree coefficient column}\in \ell^2(n^{-2\sigma})
\iff\sigma>1/2.
}
\]

No zero of zeta, functional equation, positivity theorem, or spectral localization is used. At the literal critical value the proposed infinite basis transform already fails to send the most basic coordinate vector into the Hilbert space.

## 4. Boundedness has a different threshold: `sigma>1`

For `sigma>1/2`, both Möbius and divisor-sum transforms are at least defined on every finitely supported input, so one can ask whether they extend boundedly to all of `mathscr H_sigma`.

Hedenmalm, Lindqvist and Seip identify the multiplier algebra of the square-coefficient Hardy space of Dirichlet series with the bounded Dirichlet-series functions on the right half-plane, equivalently with the corresponding bounded holomorphic multipliers under the Bohr lift to the infinite polydisk.

The Bohr symbols of the two operators are

\[
\boxed{
\mathcal B(T_\mu)(z)
=\prod_p(1-p^{-\sigma}z_p),
}
\]

and

\[
\boxed{
\mathcal B(T_1)(z)
=\prod_p(1-p^{-\sigma}z_p)^{-1}.
}
\]

If `sigma<=1`, evaluate finite-coordinate restrictions with `z_p=-r` for the Möbius symbol and `z_p=r` for its inverse, where `0<r<1`. Their suprema dominate

\[
\prod_{p\le P}(1+r p^{-\sigma})
\]

and

\[
\prod_{p\le P}(1-r p^{-\sigma})^{-1}.
\]

Because `sum_p p^{-\sigma}` diverges for every `sigma<=1`, these products become arbitrarily large as `P` grows. Therefore

\[
\boxed{
\frac12<\sigma\le1
\quad\Longrightarrow\quad
T_\mu\text{ and }T_1\text{ are unbounded on }\mathscr H_\sigma.
}
\]

For `sigma>1` the Euler products converge absolutely and uniformly on the infinite polydisk, so both operators are bounded. In fact the multiplier norms are exact:

\[
\boxed{
\|T_\mu\|
=\prod_p(1+p^{-\sigma})
=\frac{\zeta(\sigma)}{\zeta(2\sigma)},
}
\]

and

\[
\boxed{
\|T_1\|
=\prod_p(1-p^{-\sigma})^{-1}
=\zeta(\sigma).
}
\]

The first equality is attained in the supremum limit by sending finitely many Bohr coordinates toward `-1`; the second by sending them toward `+1`.

Consequently

\[
\boxed{
T_\mu:\mathscr H_\sigma\to\mathscr H_\sigma
\text{ is boundedly invertible}
\iff \sigma>1.
}
\]

Thus the infinite determinant-one finite-dimensional change of basis does develop an operator anomaly, but its bounded-invertibility boundary is exactly the ordinary absolute Euler-product line, not the critical line.

## 5. Why this does not yield an RH criterion

The two thresholds have completely different and unconditional origins:

\[
\boxed{
\sigma=\frac12
\quad\leftrightarrow\quad
\text{coefficient square-summability},
}
\]

while

\[
\boxed{
\sigma=1
\quad\leftrightarrow\quad
\text{bounded Euler-product multiplier / bounded inverse}.
}
\]

In particular, shifting reciprocal zeta so that the geometric-looking value `sigma=1/2` places its zeros relative to the HLS right half-plane does not help. At `sigma=1/2`, the coefficient sequence of the multiplier is not even an element of the underlying Hardy-Dirichlet Hilbert space. For `1/2<sigma<=1`, the coefficient vector exists but the multiplier is still unbounded for the elementary prime-product reason above, independently of any unresolved zero-free region.

So the natural sequence completion cannot turn

\[
\text{finite Möbius basis change}
\to
\text{unbounded infinite operator}
\to
\text{RH}
\]

into a new mechanism. To obtain a critical-line operator one would have to add a renormalization, change the inner product, or choose a more elaborate domain precisely where the canonical completion fails. Such extra structure would need an independent geometric derivation; it cannot be credited to the finite prime-circle Möbius basis relation itself.

## 6. Prior-art and novelty audit

The functional-analytic framework is classical. Håkan Hedenmalm, Peter Lindqvist and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in `L^2(0,1)`**, *Duke Mathematical Journal* **86**:1 (1997), 1–37, DOI `10.1215/S0012-7094-97-08601-4`, introduce the square-coefficient Hilbert space of Dirichlet series, its infinite-polydisk/character-space model, and prove in Theorem 3.1 that its multiplier algebra is the corresponding `H^infinity` algebra on the right half-plane. Modern multiplier work continues to use this identification.

The arithmetic ingredients are also classical: `mu * 1 = epsilon`, `sum mu(n)n^{-s}=1/zeta(s)`, `sum mu(n)^2n^{-s}=zeta(s)/zeta(2s)`, and the Euler products for `zeta` and reciprocal zeta. PC-015 already establishes that reciprocal zeta in the scale transform is Möbius inversion rather than new spectral data.

No historical novelty is claimed for any of these facts. The durable prime-circle contribution is the **closure of the explicit infinite-dimensional caveat in PC-027 for the standard weighted coefficient completion**: the only canonical operator thresholds are the unconditional `1/2` square-summability boundary and the unconditional `1` bounded-multiplier boundary.

## 7. Boundaries and falsification tests

The result is deliberately limited to the diagonal scale-index Hilbert family `mathscr H_sigma`. It does not rule out:

- a non-diagonal inner product derived from genuinely two-dimensional correlations of the fields `U_n(z)`;
- a renormalized determinant for an unbounded operator with a separately justified domain;
- nonlinear or nonseparable cross-level couplings;
- an operator whose scale variable is created by the geometry rather than attached as a Dirichlet weight;
- the global uniformization/monodromy branch of PC-017.

It does rule out claiming that the **mere loss of boundedness of the infinite Möbius basis transform in the standard Hardy-Dirichlet completion** is an RH signal.

The classification has direct audit tests:

1. apply `T_mu` and `T_1` to `e_1` and verify the two weighted square norms;
2. conjugate by `J_sigma` and check that the coefficient convolutions have symbols `1/zeta(s+sigma)` and `zeta(s+sigma)`;
3. use finite sets of Bohr prime coordinates to force the multiplier norms to diverge for `sigma<=1`;
4. for `sigma>1`, bound the Euler products absolutely and recover the exact norms `zeta(sigma)/zeta(2sigma)` and `zeta(sigma)`;
5. verify that no step invokes the location of nontrivial zeta zeros.

A counterexample to one of those norm thresholds would invalidate the finding. A different completion can evade it only by explicitly breaking the diagonal weighted-`l^2` hypothesis and supplying a separate reason that the replacement structure is intrinsic to prime-circle geometry.