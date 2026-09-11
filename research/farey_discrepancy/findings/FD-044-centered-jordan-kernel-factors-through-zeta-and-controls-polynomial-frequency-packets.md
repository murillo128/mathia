# FD-044 — centered Jordan kernel factors through `zeta(1+it)` and controls polynomial-width critical packets

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + CENTERED-JORDAN-KERNEL + EULER-PRODUCT + VINOGRADOV-KOROBOV + GROWING-CRITICAL-PACKETS + PHYSICAL-SOURCE-CONDITIONAL`.

`FD-042` proves universal nonsquarefree occupation for every fixed critical Mellin packet, and `FD-043` extends this to growing packets through the centered row kernel

\[
K_{R,D}(t)
=
\sum_{D<r\le R}
\frac{w(r)}r
\bigl(\mathbf 1_{\mu(r)=0}-\delta_{\rm ns}\bigr)
r^{it}.
\]

The generic density argument in `FD-043` gives the uniform bound
\(K_{R,D}(t)=O_D(\log(2+|t|))\), which is sharp enough for subpower frequency diameter but does not make a fixed packet with polynomially growing diameter asymptotically scalar at its natural critical energy scale.

The centered arithmetic weight has more structure than its summatory estimate reveals. Its Dirichlet series factors exactly as a Riemann-zeta factor times an Euler product whose pole-canceling bracket vanishes at `s=1`. On the line `Re(s)=1`, Kevin Ford's Vinogradov--Korobov bound therefore gives a `log^(2/3)` rather than `log` frequency cost for the **infinite** centered kernel. The finite truncation differs from that kernel by an explicit tail
\(O_\sigma((1+|t|)R^{\sigma-1})\).

Consequently, for every fixed `0<eta<1/2`, critical packets with frequency diameter

\[
\Omega_R\le R^{1/2-\eta}
\]

obey the sharpened occupation estimate

\[
\left|
\|P\|_{\rm ns,R,D}^2
-\delta_{\rm ns}\|P\|_{R,D}^2
\right|
\ll_{D,\eta}
m\bigl(1+\log^{2/3}(2+\Omega_R)\bigr)\|z\|_2^2.
\]

If their full critical norm has the natural conditioning
\(\|P\|_{R,D}^2\gg(\log R)\|z\|_2^2\), then every family with
\(m=o((\log R)^{1/3})\) has nonsquarefree occupation tending to
\(\delta_{\rm ns}\), even when \(\Omega_R\) is a fixed positive power of
`R` below the square-root threshold. This is strictly beyond the
`FD-043` logarithmic-kernel criterion, which for polynomial
\(\Omega_R\) does not even force a fixed packet's relative error to
vanish.

For the physical quotient-shell profile, a vanishing-occupation escape
must therefore use at least one of the following: a macroscopic
nonpacket remainder, packet dimension at least on the logarithmic
one-third scale, coefficient ill-conditioning that destroys the
natural critical norm, or frequency diameter reaching the square-root
truncation boundary. No inverse minimum-gap hypothesis appears.

## 1. Center the exact nonsquarefree row density

Retain

\[
w(r):=\frac{J_2(r)}{r^2}
=\prod_{p\mid r}(1-p^{-2})
\]

and put

\[
s(r):=\mu(r)^2w(r).
\]

Write

\[
a:=\frac1{\zeta(3)},\qquad
c_{\rm sf}:=
\prod_p(1-p^{-2}-p^{-3}+p^{-4}),
\]

so that `FD-038` gives

\[
\sum_{r\le x}w(r)=ax+O(1)
\]

and, for every fixed \(\sigma>1/2\),

\[
\sum_{r\le x}s(r)
=
c_{\rm sf}x+O_\sigma(x^\sigma).
\]

The universal nonsquarefree density is

\[
\delta_{\rm ns}
=
1-\frac{c_{\rm sf}}a
=
1-\zeta(3)c_{\rm sf}.
\]

Define the centered row coefficient

\[
\kappa(r)
:=
w(r)\bigl(\mathbf 1_{\mu(r)=0}-\delta_{\rm ns}\bigr)
=
(1-\delta_{\rm ns})w(r)-s(r).
\]

Its summatory function satisfies

\[
\boxed{
\sum_{r\le x}\kappa(r)=O_\sigma(x^\sigma)
\qquad(\sigma>1/2).
}
\]

This is exactly the density-pole cancellation used abstractly in
`FD-043`. The new point is to retain its Euler product instead of
discarding it after partial summation.

## 2. The centered Dirichlet series has an exact zeta factor

For `Re(s)>1`, the Jordan-weight Dirichlet series is

\[
\begin{aligned}
W(s)
&:=\sum_{r\ge1}\frac{w(r)}{r^s}\\
&=
\prod_p
\left(
1+(1-p^{-2})\frac{p^{-s}}{1-p^{-s}}
\right)\\
&=
\boxed{\frac{\zeta(s)}{\zeta(s+2)}}.
\end{aligned}
\]

The squarefree restriction is

\[
S(s)
:=
\sum_{r\ge1}\frac{s(r)}{r^s}
=
\prod_p\left(1+(1-p^{-2})p^{-s}\right).
\]

Factor one copy of `zeta(s)` and define

\[
A(s)
:=
\prod_p
(1-p^{-s})
\left(1+(1-p^{-2})p^{-s}\right).
\]

The local factor satisfies

\[
(1-p^{-s})
\left(1+(1-p^{-2})p^{-s}\right)
=
1-p^{-(s+2)}
-(1-p^{-2})p^{-2s}.
\]

Hence the product for `A(s)` converges absolutely and locally uniformly
throughout `Re(s)>1/2`. In particular,

\[
S(s)=\zeta(s)A(s)
\]

by analytic continuation from `Re(s)>1`, and

\[
A(1)=c_{\rm sf}.
\]

The centered Dirichlet series therefore has the exact factorization

\[
\boxed{
\mathfrak K(s)
:=
\sum_{r\ge1}\frac{\kappa(r)}{r^s}
=
\zeta(s)
\left[
\frac{1-\delta_{\rm ns}}{\zeta(s+2)}
-A(s)
\right].
}
\]

The bracket is analytic for `Re(s)>1/2`, and at `s=1`

\[
\frac{1-\delta_{\rm ns}}{\zeta(3)}
-A(1)
=
\frac{\zeta(3)c_{\rm sf}}{\zeta(3)}
-c_{\rm sf}
=0.
\]

Thus the pole of `zeta(s)` at `s=1` cancels exactly. This is the
Dirichlet-series version of the real-variable density cancellation,
but it preserves the oscillatory frequency information lost in the
summatory estimate.

Because the summatory function of `kappa` is
\(O_\sigma(x^\sigma)\) for every \(\sigma>1/2\), the series defining
\(\mathfrak K(s)\) itself converges and is analytic for `Re(s)>1/2`.
Hence the displayed Euler-product identity is an identity of the
actual centered Dirichlet series there, not merely a formal
meromorphic continuation.

## 3. Ford's zeta bound gives a two-scale finite-kernel estimate

On `Re(s)=1`, both

\[
\frac1{\zeta(s+2)}
\]

and `A(s)` are uniformly bounded. For the first term this follows from
the absolutely convergent Möbius series in `Re(s+2)=3`; for the second,
the local deviations from `1` are `O(p^-2)` uniformly on the line.

The cancellation at `s=1` also makes
\(\mathfrak K(1-it)\) bounded for bounded `t`. For `|t|>=3`, Ford's
Vinogradov--Korobov estimate

\[
|\zeta(\sigma+it)|
\le
76.2\,|t|^{4.45(1-\sigma)^{3/2}}
\log^{2/3}|t|
\qquad
\left(\frac12\le\sigma\le1\right)
\]

specializes at `sigma=1` to

\[
|\zeta(1+it)|\ll\log^{2/3}|t|.
\]

Therefore

\[
\boxed{
|\mathfrak K(1-it)|
\ll
\log^{2/3}(2+|t|).
}
\]

Now restore the finite Jordan row range and a fixed Schur head `D`:

\[
K_{R,D}(t)
:=
\sum_{D<r\le R}
\kappa(r)r^{-1+it}.
\]

Abel summation with
\(\sum_{r\le x}\kappa(r)=O_\sigma(x^\sigma)\) gives

\[
\sum_{r>R}\kappa(r)r^{-1+it}
=
O_\sigma\!\left(
(1+|t|)R^{\sigma-1}
\right).
\]

Removing the fixed first `D` terms costs only `O_D(1)`. Consequently,
for every fixed `D` and every fixed \(1/2<\sigma<1\),

\[
\boxed{
|K_{R,D}(t)|
\ll_{D,\sigma}
1+\log^{2/3}(2+|t|)
+(1+|t|)R^{\sigma-1}.
}
\]

Together with `FD-043`, one may take the minimum of this bound and the
globally uniform `O_D(log(2+|t|))` estimate. The new estimate matters
when the finite row horizon is already long enough for the centered
Dirichlet series to have settled.

Fix `0<eta<1/2` and choose
\(\sigma=1/2+\eta/2\). Uniformly for

\[
|t|\le R^{1/2-\eta},
\]

the tail is `O(R^(-eta/2))`, and hence

\[
\boxed{
\sup_{|t|\le R^{1/2-\eta}}
|K_{R,D}(t)|
\ll_{D,\eta}
1+\log^{2/3}(2+|t|).
}
\]

The square-root frequency threshold comes from truncation, not from a
singularity of the infinite Euler product.

## 4. Polynomial-width critical packets retain universal occupation

Let

\[
P(r)=\sum_{j=1}^m z_j r^{-i\gamma_j},
\qquad
\Omega:=\max_{j,k}|\gamma_j-\gamma_k|.
\]

Use the full and nonsquarefree critical row norms

\[
\|P\|_{R,D}^2
:=
\sum_{D<r\le R}
\frac{w(r)}r|P(r)|^2,
\]

\[
\|P\|_{\rm ns,R,D}^2
:=
\sum_{\substack{D<r\le R\\\mu(r)=0}}
\frac{w(r)}r|P(r)|^2.
\]

Expanding the quadratic form gives exactly

\[
\|P\|_{\rm ns,R,D}^2
-\delta_{\rm ns}\|P\|_{R,D}^2
=
\sum_{j,k}
z_j\overline{z_k}
K_{R,D}(\gamma_k-\gamma_j).
\]

If

\[
\Omega\le R^{1/2-\eta},
\]

the preceding kernel estimate and
\((\sum_j|z_j|)^2\le m\|z\|_2^2\) yield

\[
\boxed{
\left|
\|P\|_{\rm ns,R,D}^2
-\delta_{\rm ns}\|P\|_{R,D}^2
\right|
\ll_{D,\eta}
m
\bigl(
1+\log^{2/3}(2+\Omega)
\bigr)
\|z\|_2^2.
}
\]

No lower bound on the minimum frequency gap is used. Near-colliding
frequencies matter only insofar as they make the full packet norm small
relative to coefficient mass.

Suppose a packet family has the natural critical conditioning

\[
\|P_R\|_{R,D}^2
\ge
c(\log R)\|z_R\|_2^2
\]

with fixed `c>0`. Then

\[
\left|
\frac{\|P_R\|_{\rm ns,R,D}^2}
     {\|P_R\|_{R,D}^2}
-\delta_{\rm ns}
\right|
\ll_{D,\eta,c}
\frac{
m_R
\bigl(1+\log^{2/3}(2+\Omega_R)\bigr)
}{\log R}.
\]

In particular, if

\[
\Omega_R\le R^{1/2-\eta},
\qquad
m_R=o((\log R)^{1/3}),
\]

then

\[
\boxed{
\frac{\|P_R\|_{\rm ns,R,D}^2}
     {\|P_R\|_{R,D}^2}
\longrightarrow
\delta_{\rm ns}.
}
\]

For fixed `m`, this permits any frequency diameter
\(\Omega_R\le R^{1/2-\eta}\), including polynomially growing windows.
By contrast, the `FD-043` bound gives a relative error controlled by
`m log(2+Omega_R)/log R`; for polynomial `Omega_R` that does not tend
to zero even at fixed `m`. The zeta-factorization therefore enlarges
the rigorously controlled critical-packet regime rather than merely
changing a constant.

## 5. Consequence for the physical occupation frontier

As in `FD-043`, normalize the exact physical row profile by

\[
B_H(r)
:=
\sqrt{\frac rH}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right).
\]

Then

\[
\|B_H\|_{H,D}^2=\frac{E_{H,D}}H,
\qquad
\|B_H\|_{\rm ns,H,D}^2=\frac{U_{H,D}}H.
\]

Suppose along an unbounded sequence of horizons there are critical
packets `P_H` such that

\[
\|B_H-P_H\|_{H,D}
=
o(\|B_H\|_{H,D}),
\]

their frequency diameters satisfy, for one fixed `0<eta<1/2`,

\[
\Omega_H\le H^{1/2-\eta},
\]

their dimensions satisfy

\[
m_H=o((\log H)^{1/3}),
\]

and they retain natural coefficient conditioning,

\[
\|P_H\|_{H,D}^2
\gg
(\log H)\|z_H\|_2^2.
\]

The nonsquarefree norm is a coordinate restriction of the full
positive row norm, so the relative approximation also transfers to
the nonsquarefree quadratic form. Section 4 then gives

\[
\boxed{
\frac{U_{H,D}}{E_{H,D}}
\longrightarrow
\delta_{\rm ns}.
}
\]

Therefore any physical sequence with
\(U_{H,D}/E_{H,D}\to0\) must defeat at least one member of this
four-part approximation regime: relative packet approximation,
sub-square-root frequency diameter, logarithmic-one-third dimension,
or natural coefficient conditioning.

This sharpens the `FD-043` escape classification. In particular, a
fixed or slowly growing critical packet cannot evade occupation merely
by moving its frequencies out to a polynomial window. The remaining
spectral escape has to become genuinely more complex or reach the
finite-horizon square-root frequency scale where the tail of the
centered Dirichlet series is no longer uniformly negligible.

This still does **not** prove the physical occupation clue. Nothing
here establishes that the actual source admits such packet
approximations, nor that its effective frequency diameter stays below
the square-root threshold. Those are source-specific questions tied to
the zero expansion of `zeta(s+1)/zeta(s)` and its truncation.

## 6. Prior-art and falsification boundary

The Euler products above are elementary consequences of the classical
Jordan weight and the squarefree indicator; no novelty is claimed for
those products in isolation. A targeted search around squarefree
Jordan-totient Dirichlet series located standard Jordan and squarefree
Euler-product material but no theorem needed beyond the direct local
calculation above.

The only new external theorem used as a load-bearing analytic input is
Kevin Ford's 2002 Vinogradov--Korobov bound for `zeta(s)` in the
critical strip. Its `sigma=1` specialization is exactly what improves
the settled centered-kernel frequency cost from `log` to `log^(2/3)`.
The source is recorded in `SOURCES.md`.

The Mathia-specific contribution is the exact placement of that
classical zeta bound inside the centered nonsquarefree Jordan kernel
from `FD-038`--`FD-043`, including the finite-horizon tail and the
resulting polynomial-width packet criterion.

The finding is falsified if any of the following fails: the local
Euler factor for `W(s)`, the factorization `S(s)=zeta(s)A(s)`, the
identity `A(1)=c_sf` and resulting pole cancellation, the Abel tail
bound for `K_(R,D)`, or a direct finite evaluation of the quadratic
form in Section 4. The polynomial-frequency corollary also explicitly
depends on the stated packet conditioning; removing that hypothesis
would overclaim the result.
