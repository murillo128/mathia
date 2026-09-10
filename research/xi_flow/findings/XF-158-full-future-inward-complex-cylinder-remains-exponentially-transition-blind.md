---
type: negative
research_line: xi_flow
finding_id: XF-158
status: canonical
---

# XF-158 — full-future inward complex cylinder remains exponentially transition-blind

**Confidence:** high for the canonical maximal-contact matched pair and every fixed inward depth `H>0`. The finite-`N` upper bound is an exact consequence of the XF-156 two-endpoint hyperbolic-cosine envelope after radial reflection, and the matching edge exponent follows by the same elementary binomial isolation used in XF-155.

## Statement

XF-154 proves that the initial inward continuation of the maximal-contact matched pair has no positive visibility threshold, while XF-156 classifies the complete future only in the outward direction. The missing inward full-future problem has a sharp answer: positive heat can expose the low-frequency edge of the packet, but that edge remains exponentially small. No fixed inward complex depth ever reaches a nonnegative visibility exponent.

Let `N>=8` be even, put

\[
n=N-2,
\]

and use the normalized inward continuation at

\[
z=\frac L2-d-ih,
\qquad
H=\frac{\pi h}{L}>0,
\qquad
D=\frac{\pi d}{L}\in\left[0,\frac\pi2\right].
\]

For the canonical maximal-contact matched pair define

\[
\mathcal A_N^-(u;H,D)
:=
\frac{|R_1(z,u)-R_{\lambda_\rho}(z,u)|}
{2(1-\lambda_\rho)},
\qquad u\ge0.
\]

Equivalently, replacing `H` by `-H` in the exact XF-155/XF-156 representation gives

\[
\mathcal A_N^-(u;H,D)
=
e^{-NH-N^2u/4}
\left|
2^{-n}\sum_{k=0}^{n}\binom nk
 e^{2\delta_k(-H+iD)+u\delta_k^2}
\right|,
\qquad
\delta_k=\frac n2-k.
\tag{1}
\]

Set

\[
M(H,D)
:=
\max\left\{
|\cosh(H+iD)|,\frac{e^H}{2}
\right\}.
\tag{2}
\]

Then for every `u>=0`,

\[
\boxed{
\mathcal A_N^-(u;H,D)
\le
2e^{-NH}M(H,D)^{N-2}e^{-(N-1)u}.
}
\tag{3}
\]

Consequently, for every fixed `H>0`, uniformly in `D in [0,pi/2]`,

\[
\boxed{
\lim_{N\to\infty}
\frac1N\log\sup_{u\ge0}\mathcal A_N^-(u;H,D)
=
\Gamma_-(H,D)
:=
\max\left\{
F_-(H,D),-\log2
\right\},
}
\tag{4}
\]

where the initial inward rate from XF-154 is

\[
F_-(H,D)
=
-H+\frac12\log\!\left(\cos^2D+\sinh^2H\right).
\tag{5}
\]

Both branches in `(4)` are strictly negative for every finite fixed `H>0`. Hence

\[
\boxed{
\Gamma_-(H,D)<0
\qquad
(H>0,\;0\le D\le\pi/2).
}
\tag{6}
\]

In particular, the complete future on every fixed inward circle remains exponentially transition-blind. Since

\[
|\cosh(H+iD)|\le\cosh H
\quad\text{and}\quad
\frac{e^H}{2}<\cosh H,
\]

`(3)` yields the stronger uniform cylinder estimate

\[
\boxed{
\sup_{\substack{u\ge0\\0\le D\le\pi/2}}
\mathcal A_N^-(u;H,D)
\le
\frac{2}{\cosh^2H}
\left(\frac{1+e^{-2H}}{2}\right)^N.
}
\tag{7}
\]

Under the periodic coordinate `w=-e^{-2\pi iz/L}`, inward depth `H` is the fixed interior radius

\[
|w|=e^{-2H}<1.
\]

Thus access to the entire real-angle circle at any fixed radius strictly inside the unit disk, through all positive heat times, still leaves this matched pair exponentially indistinguishable while its periodic transition times differ by the prescribed finite amount `rho`.

## Derivation

### 1. Radial reflection gives the same two-endpoint envelope

XF-156 proves for `H>=0`, `D in [0,pi/2]`, and every real `y` that

\[
|\cosh(H+y+iD)|
\le
M(H,D)e^{|y|}.
\tag{8}
\]

The modulus is even in both the real and imaginary signs in the sense needed here:

\[
|\cosh(-H+y+iD)|
=
|\cosh(H-y-iD)|
=
|\cosh(H-y+iD)|.
\]

Applying `(8)` with `-y` therefore gives

\[
\boxed{
|\cosh(-H+y+iD)|
\le
M(H,D)e^{|y|}.
}
\tag{9}
\]

The Gaussian form equivalent to `(1)` is

\[
\mathcal A_N^-(u;H,D)
=
e^{-NH-N^2u/4}
\left|
\mathbb E\,
\cosh^n\!\left(
-H+iD+\sqrt{\frac u2}\,Z
\right)
\right|,
\tag{10}
\]

with `Z` standard Gaussian. Combining `(9)` with

\[
\mathbb E e^{t|Z|}\le2e^{t^2/2}
\]

at `t=n sqrt(u/2)` gives

\[
\mathcal A_N^-(u;H,D)
\le
2e^{-NH}M(H,D)^n
\exp\!\left[-\frac{N^2-n^2}{4}u\right].
\]

Since `(N^2-n^2)/4=N-1`, this is `(3)`. Taking the full-future supremum gives the exponential upper rate

\[
-H+\log M(H,D)
=
\max\left\{
-H+\log|\cosh(H+iD)|,
-\log2
\right\},
\tag{11}
\]

which is exactly the right-hand side of `(4)`.

### 2. The initial slice and the inward spectral edge both attain the envelope

At `u=0`, `(1)` gives exactly

\[
\mathcal A_N^-(0;H,D)
=
e^{-NH}|\cosh(H+iD)|^{N-2},
\tag{12}
\]

so the limiting rate is `F_-(H,D)`.

For the complementary edge witness, fix any constant `c>2` and take

\[
u_N=c\frac{\log N}{N}.
\tag{13}
\]

Now factor the `k=n` term from `(1)`, rather than the `k=0` outward edge used in XF-155. Its exact modulus is

\[
E_N^-(u,H)
=
\exp\!\left(
-2H-(N-2)\log2-(N-1)u
\right).
\tag{14}
\]

Writing `k=n-j`, the relative modulus of the `j`th neighboring term is

\[
\binom nj
\exp\!\left(-2jH-u\,j(n-j)\right).
\tag{15}
\]

This is the same tail expression that appears after factoring the outward `k=0` edge in XF-155. The identical split at `j=n/2`, using `j(n-j)>=jn/2` and `binom(n,j)<=n^j/j!`, shows that the sum of every non-edge modulus is `o(1)` relative to `(14)` when `(13)` holds. The estimate is independent of the phases and hence uniform in `D`. Therefore

\[
\boxed{
\mathcal A_N^-(u_N;H,D)
=(1+o(1))
\exp\!\left(
-2H-(N-2)\log2-(N-1)u_N
\right),
}
\tag{16}
\]

uniformly in `D`, and

\[
\lim_{N\to\infty}
\frac1N\log\mathcal A_N^-(u_N;H,D)
=-\log2.
\tag{17}
\]

The lower bounds `(12)` and `(17)` match the upper envelope `(11)`, proving `(4)`.

### 3. Neither inward branch can cross zero

For every `D in [0,pi/2]`,

\[
|\cosh(H+iD)|^2
=
\cos^2D+\sinh^2H
\le
\cosh^2H.
\]

Thus

\[
F_-(H,D)
\le
-H+\log\cosh H
=
\log\left(\frac{1+e^{-2H}}2\right)
<0
\tag{18}
\]

for every fixed `H>0`. The edge branch is the constant `-log 2<0`, proving `(6)`. Equation `(18)` inserted into `(3)` also gives the uniform full-cylinder estimate `(7)` directly.

The two negative branches have their own internal crossover. Since

\[
F_-(H,D)\ge-\log2
\iff
e^{-2H}+2\cos(2D)\ge0,
\tag{19}
\]

one obtains:

- for `0<=D<=pi/4`, the initial branch dominates at every finite `H>0`;
- for `pi/4<D<pi/3`, the crossover occurs at
  \[
  H_c^-(D)
  =-\frac12\log\!\bigl(-2\cos(2D)\bigr),
  \tag{20}
  \]
  with the initial branch below that depth and the edge branch above it;
- for `pi/3<=D<=pi/2`, the edge branch `-log 2` dominates for every `H>0`.

This phase change affects only which exponentially small signal is largest. Unlike the outward crossover in XF-155/XF-156, it never creates a visibility transition.

## Consequences for the frontier

XF-154 established one-sidedness only at the initial slice: outward continuation crosses a finite threshold, while inward continuation does not. The present result shows that the asymmetry survives the **entire future**. Positive heat can spectrally isolate the inward low-frequency edge, but its best exponential rate is still `-log 2`; there is no inward analogue of the outward `2H-log 2` amplification branch.

This removes inward complex reach as a target-side escape for the canonical adversary. Even observing every real angle on a complete fixed interior circle is exponentially blind by `(7)`. Consequently, any subexponentially normalized linear or Lipschitz sensing scheme built only from that full inward cylinder inherits exponential ill-conditioning by the same norm argument used in XF-157, provided its total sensing/postprocessing gain is subexponential compared with the margin in `(7)`.

The asymmetry has a simple spectral interpretation. Outward continuation weights the highest-frequency edge strongly enough to produce the growing rate `2H-log 2`; inward continuation instead selects the opposite, lowest-frequency edge. The carrier factor cancels its radial gain at exponential order, leaving the fixed base-two rate `-log 2`. Going deeper inside the unit disk therefore cannot buy transition visibility for this packet.

The higher-value remaining interfaces are correspondingly narrower. On the target side, a successful complex observable must use outward reach, a genuinely nonlocal/nonlinear operation not reducible to this pointwise cylinder envelope, or exponential sensing gain. On the source side, the central unresolved question remains whether the actual Xi source can realize or approximate the maximal-contact direction at the transition scale.

## Falsification boundary

The theorem is specific to the canonical maximal-contact matched pair and to fixed inward depth `H>0` as `N->infinity`. It does not give a uniform exponent in joint regimes `H=H_N->0`; indeed at the antipodal point `D=0`, the exponent approaches zero as `H->0`. It also does not claim that all nonlinear functionals of interior values are bounded independently of their conditioning: an exponentially growing postprocessing gain can compensate exponential input blindness and must be charged explicitly.

The result is an observability obstruction, not a source theorem for Xi. It proves that this adversarial pair survives complete inward-circle/full-future raw observation at finite precision; it does not prove that Xi itself realizes the pair, nor does it constrain `Lambda` without an additional Xi-specific exclusion or source-faithfulness theorem.

## Prior-art audit

A directed audit covered the de Bruijn--Newman/holomorphic heat-flow literature, backward heat flow of high-degree trigonometric polynomials, and the Curie--Weiss/Lee--Yang complex-field representation already anchored in `SOURCES.md`. Recent high-degree polynomial heat-flow work likewise studies complex zero distributions rather than the directional conditioning of this matched transition packet. No audited result supplied the inward full-future max formula `(4)` or the fixed-radius cylinder bound `(7)`.

No external theorem is load-bearing. The proof uses the exact Mathia packet representation, the XF-156 elementary two-endpoint hyperbolic-cosine bound, the same elementary Gaussian moment estimate used there, and the XF-155 binomial edge-isolation argument reflected to the opposite spectral edge. `SOURCES.md` therefore requires no new entry.

## Next gate

The canonical maximal-contact target-side picture is now strongly one-sided: the outward half-plane has the exact two-branch visibility phase of XF-156, while every fixed inward circle remains exponentially blind through all future heat times. Further optimization of inward point traces is therefore closed for this adversary. The next high-value test remains source-side realizability of the maximal-contact direction by the actual Xi source; a secondary target-side route must change the observation class qualitatively rather than move farther inward.
