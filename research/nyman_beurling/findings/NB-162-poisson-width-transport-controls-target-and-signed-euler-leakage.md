# NB-162 — Poisson-width transport controls target gain and signed Euler leakage

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + SOURCE-SPECIFIC + TRANSPORT-SENSITIVE-EULER + BOUNDARY-SCALE + DECISIVE-METHOD-BOUNDARY

`NB-160` closes sign-separated growing samplers, while `NB-161` shows that genuine Jordan transport collapse kills a fixed-width Poisson target unless total-variation conditioning diverges. A remaining ambiguity is what happens when the exterior sampler itself approaches `Re s=1`: the Poisson width then shrinks, so an absolute transport length `ell_G -> 0` need not represent geometric collapse relative to the kernel. At the same time `NB-154` shows that the unsigned Euler-product remainder grows like `1/a_G` at horizontal gap `a_G`.

The two effects are governed by the same dimensionless quantity. For a zero-mass height sampler with total-variation conditioning `C_G` and mean Jordan transport length `ell_G`, define

\[
\boxed{
\Theta_G:=\frac{C_G\ell_G}{a_G}.
}
\]

Then `Theta_G` controls both (i) every Poisson target response, after normalizing by that target zero's own Poisson width, and (ii) the signed Euler-product response, after normalizing by the natural boundary scale `c_G/a_G`. In particular, **sub-Poisson Jordan transport `Theta_G=o(1)` cannot be used as a cheap prime-side cancellation mechanism: it suppresses the target at the same time.**

## Claim

Fix `A>0`. Let `0<a<=A`, and let `nu` be a finite real signed Borel measure on `R` with zero total mass and finite first moment. Write

\[
\nu=\nu^+-\nu^-,
\qquad
M:=\nu^+(\mathbb R)=\nu^-(\mathbb R),
\qquad
V:=\|\nu\|_{\rm TV}=2M,
\]

and let

\[
W_1:=\mathsf W_1(\nu^+,\nu^-),
\qquad
\ell:=\frac{W_1}{M}.
\]

Choose a positive reference mass `c>0`, put

\[
C:=\frac{V}{c},
\qquad
\Theta:=\frac{C\ell}{a},
\]

and for `x>0` define the Poisson response

\[
Q_\nu(x,\gamma)
:=
\int_{\mathbb R}
\frac{x}{x^2+(\gamma-t)^2}
\,d\nu(t).
\]

Then the following statements hold.

### 1. The same boundary-scale transport number controls every target Poisson response

For all `x>=a` and all `gamma in R`,

\[
\boxed{
|Q_\nu(x,\gamma)|
\le
\frac{9}{16\sqrt3}\,
\frac{c}{x}\,
\frac{C\ell}{x}
\le
\frac{9}{16\sqrt3}\,
\frac{c}{x}\,
\Theta.
}
\]

Consequently, if at any target point one asks for a fixed fraction of the natural Poisson peak scale,

\[
Q_\nu(x_*,\gamma_*)\ge q\frac{c}{x_*}
\qquad(q>0),
\]

then necessarily

\[
\boxed{
\frac{C\ell}{x_*}
\ge
\frac{16\sqrt3}{9}q,
\qquad
\Theta
\ge
\frac{16\sqrt3}{9}q.
}
\]

For the zeta sampler at exterior abscissa `1+a`, a nontrivial zero `rho=beta+i gamma` has

\[
x_\rho=1+a-\beta\ge a,
\]

so the bound applies uniformly to every actual zero without assuming that `beta` is close to `1`.

### 2. The signed Euler-product response obeys the same transport scale

Define

\[
\mathcal E_a(\nu)
:=
\int_{\mathbb R}
\frac{\zeta'}{\zeta}(1+a+it)
\,d\nu(t).
\]

Absolute convergence of the Euler product on `Re s>1` and optimal transport give the exact estimate

\[
\boxed{
|\mathcal E_a(\nu)|
\le
W_1
\left(\frac{\zeta'}{\zeta}\right)'(1+a).
}
\]

Since

\[
\left(\frac{\zeta'}{\zeta}\right)'(1+a)
=\frac1{a^2}+O_A(1)
\]

as `a -> 0+`, there is a finite constant `B_A` such that

\[
\boxed{
|\mathcal E_a(\nu)|
\le
\frac{B_A}{2}
\frac{c}{a}\Theta.
}
\]

The usual total-variation estimate from `NB-154` remains available as

\[
|\mathcal E_a(\nu)|
\le
V\left(-\frac{\zeta'}{\zeta}(1+a)\right)
\le
A_A\frac{c}{a}C
\]

for a finite `A_A=A_A(A)`. Hence the useful interpolation is

\[
\boxed{
|\mathcal E_a(\nu)|
\le
\frac{c}{a}
\min\left\{A_A C,\frac{B_A}{2}\Theta\right\}.
}
\]

Thus when the Jordan signs are close in transport, the prime-side remainder is much smaller than the unsigned `V/a` majorant, but exactly the same small transport parameter also suppresses target visibility.

### 3. The logarithmic Gamma moment is cheaper still at high ordinate

If the sampler is supported on `[H,\infty)` with `H>0`, zero total mass and the same coupling argument give

\[
\boxed{
\left|
\int \log(t/G)\,d\nu(t)
\right|
\le
\frac{W_1}{H}
=
\frac{cC\ell}{2H}.
}
\]

This is the signed logarithmic-height moment isolated in `NB-157`. Therefore fine Jordan transport automatically controls the macroscopic Gamma moment; exact three-height balancing is not required for this particular regime. If `H` is polynomially high while `a<=A`, this contribution is negligible compared with the boundary Euler scale `c/a` whenever `C` stays bounded.

## Derivation

### Poisson response

For fixed `x>0` and `gamma`, let

\[
K_{x,\gamma}(t)
:=
\frac{x}{x^2+(\gamma-t)^2}.
\]

As computed in `NB-161`,

\[
\operatorname{Lip}(K_{x,\gamma})
=
\frac{9}{8\sqrt3\,x^2}.
\]

For any coupling `pi in Pi(nu^+,nu^-)`,

\[
Q_\nu(x,\gamma)
=
\int
\bigl(K_{x,\gamma}(s)-K_{x,\gamma}(t)\bigr)
\,d\pi(s,t),
\]

so

\[
|Q_\nu(x,\gamma)|
\le
\frac{9}{8\sqrt3\,x^2}W_1.
\]

Because `W_1=M ell=(V/2)ell=(cC/2)ell`, this becomes

\[
|Q_\nu(x,\gamma)|
\le
\frac{9}{16\sqrt3}
\frac{c}{x}\frac{C\ell}{x}.
\]

Finally `x>=a` implies `C ell/x <= C ell/a=Theta`, proving the first part.

### Euler response

For `Re s>1`,

\[
\frac{\zeta'}{\zeta}(s)
=-\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
\]

absolutely. Therefore finite total variation permits termwise integration:

\[
\mathcal E_a(\nu)
=-\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+a}}
\widehat\nu(\log n),
\qquad
\widehat\nu(u):=\int e^{-iut}\,d\nu(t).
\]

For any transport coupling `pi`, zero total mass gives

\[
\widehat\nu(u)
=
\int
\bigl(e^{-ius}-e^{-iut}\bigr)
\,d\pi(s,t).
\]

Since `t -> e^{-iut}` is `|u|`-Lipschitz,

\[
|\widehat\nu(u)|
\le
|u|\int|s-t|\,d\pi(s,t).
\]

Taking the optimal coupling yields

\[
|\widehat\nu(u)|\le |u|W_1.
\]

Substitution into the Euler series gives

\[
\begin{aligned}
|\mathcal E_a(\nu)|
&\le
W_1
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+a}}\\
&=
W_1
\left(\frac{\zeta'}{\zeta}\right)'(1+a).
\end{aligned}
\]

The Laurent expansion at the simple pole of `zeta` gives

\[
-\frac{\zeta'}{\zeta}(1+a)=\frac1a+O(1),
\qquad
\left(\frac{\zeta'}{\zeta}\right)'(1+a)=\frac1{a^2}+O(1).
\]

Hence

\[
A_A:=\sup_{0<a\le A}
a\left(-\frac{\zeta'}{\zeta}(1+a)\right)<\infty,
\]

and

\[
B_A:=\sup_{0<a\le A}
a^2\left(\frac{\zeta'}{\zeta}\right)'(1+a)<\infty.
\]

The transport-sensitive and total-variation estimates then give the displayed interpolation.

### Log-height moment

Assume `supp nu subset [H,\infty)`. For any coupling `pi`,

\[
\int \log(t/G)\,d\nu(t)
=
\int
\log(s/t)
\,d\pi(s,t).
\]

The function `log t` is `1/H`-Lipschitz on `[H,\infty)`, so

\[
\left|
\int \log(t/G)\,d\nu(t)
\right|
\le
\frac1H
\int|s-t|\,d\pi(s,t).
\]

Minimizing over couplings proves the third estimate.

## What this changes after NB-154 and NB-161

`NB-154` identified `C/a` as the relevant conditioning cost when one throws away all prime-side sign cancellation. `NB-161` identified `C ell` as the fixed-width cost of making the Jordan signs approach one another. The present result shows how those two currencies combine near `Re s=1`:

\[
\boxed{
\Theta=\frac{C\ell}{a}
}
\]

is the scale-invariant transport parameter for boundary approach.

This corrects a possible over-reading of `NB-161`. If `a_G -> 0`, absolute transport collapse `ell_G -> 0` is not by itself fatal: the Poisson kernel is narrowing simultaneously. What is fatal is **sub-Poisson collapse**, `C_G ell_G/a_G -> 0`. In that regime every zero sees vanishing normalized target response, while the signed Euler contribution is also `o(c_G/a_G)`. The sampler has indeed bought excellent prime-side cancellation, but only by becoming equally invisible to the target.

Conversely, if a bounded-conditioning construction keeps a fixed fraction of natural Poisson target gain, it must retain Jordan transport of at least one Poisson width:

\[
C_G=O(1),
\qquad
Q_G\gtrsim c_G/x_G
\quad\Longrightarrow\quad
\ell_G\gtrsim x_G\ge a_G.
\]

So approaching the one-line does not open a free regime in which the two Jordan signs can be collapsed much more finely than the kernel width while still exploiting the `1/a_G` arithmetic amplification.

## Remaining geometric regime

This does not close the fixed-width interlaced geometry left by `NB-160` and `NB-161`. In particular, the theorem is compatible with

\[
\Theta_G\asymp1,
\qquad
\ell_G\asymp a_G/C_G,
\]

where target response and signed Euler leakage are both of their natural boundary scale. Nor does it prove that an interlaced sampler with `Theta_G=Theta(1)` must export an `Omega(log G)` adverse zero reservoir. That still requires information about how the signed Poisson profile interacts with the actual local zero set, rather than only Lipschitz/transport control.

The next sharp regime is therefore narrower than after `NB-161`: **one-Poisson-width interlacing**. A genuinely new construction must keep `Theta_G` bounded below while arranging enough local sign overlap to defeat `NB-160`'s separated-reservoir mechanism, and it must exploit more than the generic transport cancellation above if the prime side is to become smaller than its target response.

## Prior-art and novelty audit

The transport step is classical in mechanism. Kantorovich--Rubinstein duality controls integration against Lipschitz test functions by `W_1`; D. A. Edwards, *On the Kantorovich--Rubinstein theorem*, Expositiones Mathematicae 29 (2011), 387--398, is a standard expository reference. The Fourier inequality `|hat nu(u)| <= |u| W_1` is an immediate application to the Lipschitz test `e^{-iut}`. The Euler-product identity for `zeta'/zeta` on `Re s>1` and its Laurent behavior at `1` are classical and already part of this line's analytic toolkit.

A fresh search for combinations of Wasserstein/Kantorovich transport, Poisson sampling, and the logarithmic derivative of the Riemann zeta function found the expected general optimal-transport literature but no source giving the line-specific coupling above: the same Jordan transport number simultaneously controlling a Nyman-side exterior Poisson target and the signed Euler leakage. No novelty is claimed for Kantorovich--Rubinstein duality, the Fourier bound, or the Euler series separately. Because every load-bearing step is derived here from classical identities already used in the line, `SOURCES.md` needs no new anchor.

## Source map

- `NB-154`: boundary approach and the unsigned `V/a` Euler-product cost.
- `NB-157`: the signed logarithmic Gamma moment.
- `NB-160`: adverse-zero reservoir for Jordan supports separated by sufficiently many Poisson widths.
- `NB-161`: optimal Jordan transport as the correct currency for collapsing/interlaced signed Poisson geometry.

## Consequence for the line

Boundary approach and sign collapse are not independent escape currencies. **For a zero-mass height sampler at exterior gap `a_G`, the dimensionless quantity `Theta_G=C_G ell_G/a_G` upper-controls every Poisson response relative to its natural kernel height and also the signed Euler-product response relative to `c_G/a_G`. If `Theta_G=o(1)`, both disappear together.** The only bounded-cost transport geometry still capable of carrying a useful target is therefore transport on at least the Poisson-width scale; whether such one-width interlacing can cancel the routine actual-zero background remains the decisive geometric question.