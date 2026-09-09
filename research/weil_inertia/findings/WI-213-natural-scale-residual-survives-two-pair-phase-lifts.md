# WI-213 — natural-scale residual survives every admissible phase lift of the two-pair screen

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + STRUCTURAL-RIGIDITY + LITERATURE-CONTEXT`.

WI-211 constructs two additional off-line functional-equation pairs that cancel an equal-depth arithmetic bow exactly at the two reciprocal harmonics available when `2<d<3`, and WI-212 shows that every fixed finite reciprocal packet can likewise be screened by only finitely many deep off-line pairs. The remaining test in `CLUE-two-harmonic-screen-continuum-residual` is whether the exact WI-211 screen also cancels the coherent peak *between* those samples once integer phase lifts are retained and the `1/M` frequency window is priced in the actual source variable.

It does not. Every admissible integer-lift family of the WI-211 two-pair screen with bounded normalized continuum energy has, after passage to a subsequence, the explicit natural-scale profile

\[
\boxed{
F_{h,\kappa,q}(u)
=2\cosh(2h)\frac{\sin(\pi u)}{\pi u}
+e^{2\pi i\kappa u}
\left[-2\cosh(2h)+\pi(3+4q)\cosh^2(h)u\right],
}
\tag{1}
\]

where `q` is an integer relative lift and `\kappa` is the limiting common lift divided by the bow length. At the cancelled harmonic,

\[
\boxed{
F'_{h,\kappa,q}(0)
=\pi(3+4q)\cosh^2(h)-4\pi i\kappa\cosh(2h),
}
\tag{2}
\]

so, because `|3+4q|>=1` for every integer `q`,

\[
\boxed{|F'_{h,\kappa,q}(0)|\ge\pi\cosh^2h>0.}
\tag{3}
\]

The central representatives in the clue are `(q,\kappa)=(0,0)` and have slope `3\pi\cosh^2h`. The best relative lift is `q=-1`, which reduces the leading slope by a factor `3` and the leading small-window energy coefficient by a factor `9`, but cannot make the residual vanish. Relative lifts growing with `M` have divergent normalized continuum energy and therefore do not supply a low-energy escape.

The same profile has an exact source dictionary. Put `L=\log T`, twist at the bow center, and set

\[
X=T^{2/d},\qquad
x_M(u)=T^{(2+u/M)/d}
=X\exp\!\left(\frac{uL}{dM}\right).
\tag{4}
\]

Then the synthetic bow-plus-screen function is exactly the `x^{1/2}`-normalized selected zero-residue integrand of the twisted explicit formula at `x=x_M(u)`, up to a common harmless sign/phase. A fixed `u`-window therefore has physical relative width

\[
\boxed{\Delta x/X\asymp L/(dM),}
\tag{5}
\]

which is precisely the bow/Gallagher scale isolated in WI-195 and WI-209. Integrating across a fixed short `u`-interval turns any nonzero profile (1) into selected residue energy of order `X^2L^3/(d^3M)`, while the raw-prime Gallagher diagonal at the matching short length is of order `X^2L^2/(d^2M)`. Hence the screened-bow residual remains `Omega(\log T)` superdiagonal in energy.

This is not an unconditional contradiction for zeta. The full explicit formula retains remote/complementary zeros and the structured source terms. WI-195 records that the needed diagonal-scale upper bound for the **full** source-fixed error in this Gallagher norm is not currently established. If such an upper bound were available, the complement would have to approximate the negative of the screened-bow residual to relative `O((\log T)^{-1/2})`, just as WI-209 derives for the unscreened bow. Thus the two-pair screen is ruled out as a continuum-flattening mechanism, but more general screen pairs and the full source complement remain open.

## 1. Central profile from the exact WI-211 root

Let `M` be odd and write

\[
D_M(t)=\frac{\sin(\pi Mt)}{\sin(\pi t)},
\qquad
B_M(t)=2\cosh(ht)D_M(t).
\tag{6}
\]

Use WI-211's exact parameters

\[
A_M=\frac12M\cosh h,
\qquad
C_M=\frac12M\cosh(2h),
\tag{7}
\]

with `y_M` the larger root of

\[
2y^2-(4A_M^2+1+C_M)y+2A_M^2=0,
\tag{8}
\]

and

\[
a_M=\operatorname{arcosh}\sqrt{y_M},
\qquad
\phi_M=\arccos\!\left(-\frac{A_M}{\sqrt{y_M}}\right).
\tag{9}
\]

WI-211 gives

\[
y_M=\frac12M^2\cosh^2h+\frac14M\cosh(2h)+O_h(1),
\tag{10}
\]

hence

\[
\frac{\cosh(2a_M)}{M^2}\to\cosh^2h,
\qquad
\phi_M\to\frac{3\pi}{4},
\qquad
a_M=\log M+O_h(1).
\tag{11}
\]

At `t=2+u/M`,

\[
\frac{D_M(2+u/M)}M
=\frac{\sin(\pi u)}{M\sin(\pi u/M)}
\longrightarrow\frac{\sin(\pi u)}{\pi u}
\tag{12}
\]

uniformly for `u` in compact intervals. The central screen is

\[
S_M(t)=4\cosh(a_Mt)\cos(\phi_Mt),
\tag{13}
\]

and the root identity gives exactly

\[
S_M(2)=-2M\cosh(2h).
\tag{14}
\]

Differentiating (13), the depth derivative is `O_h(M\log M)` at `t=2`, while the phase derivative is of order `M^2`; (11) gives

\[
\frac{S_M'(2)}{M^2}\to3\pi\cosh^2h.
\tag{15}
\]

On `t=2+u/M` with bounded `u`, the second derivative is `O_{h,u}(M^2\log^2M)`, so the Taylor remainder divided by `M` is `O_{h,u}(\log^2M/M)`. Combining (12)--(15), uniformly on compact `u`-intervals,

\[
\frac{B_M(2+u/M)+S_M(2+u/M)}M
\to
2\cosh(2h)\left(\frac{\sin(\pi u)}{\pi u}-1\right)
+3\pi\cosh^2h\,u.
\tag{16}
\]

This proves the clue's proposed central profile. On a symmetric interval the sinc-minus-one term is even and the linear term is odd, so

\[
\int_{-c}^{c}|F_{h,0,0}(u)|^2du
\ge6\pi^2c^3\cosh^4h.
\tag{17}
\]

## 2. Integer phase lifts cannot flatten the peak

Write general integer representatives of the two WI-211 phases as

\[
\theta_{+,M}=\phi_M+2\pi n_{+,M},
\qquad
\theta_{-,M}=-\phi_M+2\pi n_{-,M},
\tag{18}
\]

and

\[
S_M^{\rm lift}(t)
=2\cosh(a_Mt)
\left(e^{i\theta_{+,M}t}+e^{i\theta_{-,M}t}\right).
\tag{19}
\]

Every lift preserves the exact harmonic values at `t=1,2`. Put

\[
n_M=n_{-,M},\qquad q_M=n_{+,M}-n_{-,M}.
\tag{20}
\]

Then

\[
S_M^{\rm lift}(t)=e^{2\pi in_Mt}H_{M,q_M}(t),
\tag{21}
\]

where

\[
H_{M,q}(t)=2\cosh(a_Mt)
\left(e^{i(\phi_M+2\pi q)t}+e^{-i\phi_Mt}\right).
\tag{22}
\]

For every fixed integer `q`,

\[
H_{M,q}(2)=-2M\cosh(2h)
\tag{23}
\]

and direct differentiation with (11) gives

\[
\boxed{
\frac{H_{M,q}'(2)}{M^2}
\to\pi(3+4q)\cosh^2h.
}
\tag{24}
\]

If both lifted screen ordinates remain inside the centered `M`-cell bow, `n_M/M` is bounded (indeed in `[-1/2,1/2]+o(1)`). Along a subsequence with fixed `q_M=q` and `n_M/M\to\kappa`, the same Taylor estimate yields the profile (1).

A varying relative lift cannot lower the continuum energy. If `|q_M|/M` stays bounded away from zero along a subsequence, the relative factor `e^{2\pi iq_Mu/M}` is nontrivial on a positive-measure set while each individual screen term has normalized size `asymp M`; the normalized `L^2` energy diverges. If `q_M=o(M)` but `|q_M|\to\infty`, then for every fixed nonzero `u`, the relative phase displacement is `2\pi q_Mu/M=o(1)` but multiplied by the individual normalized screen amplitude `asymp M` it produces size `asymp |q_Mu|`; Fatou again gives divergent normalized `L^2` energy on any fixed nontrivial interval. Thus bounded normalized continuum energy forces `q_M=O(1)`, and the subsequential classification (1) is exhaustive for low-energy admissible lifts.

Differentiating (1) gives (2)--(3). Therefore no admissible low-energy phase lift makes the limiting profile identically zero. In particular, for small symmetric windows,

\[
\int_{-c}^{c}|F_{h,\kappa,q}(u)|^2du
=\frac23|F'_{h,\kappa,q}(0)|^2c^3+O_{h,\kappa,q}(c^4),
\tag{25}
\]

and the smallest possible leading slope occurs at `q=-1`, `\kappa=0`, with magnitude `\pi\cosh^2h`.

## 3. Exact source-coordinate dictionary

Use the WI-209--WI-211 unfolded bow normalization

\[
\frac{\gamma_jL}{2\pi}=x_0+dj,
\qquad
b_j=(\beta_j-\tfrac12)L=dh,
\tag{26}
\]

and twist at `U=2\pi x_0/L`. For `x=x_M(u)` from (4), define

\[
t=\frac{d\log x}{L}=2+\frac{u}{M}.
\tag{27}
\]

A selected bow zero and its same-ordinate functional-equation mirror contribute

\[
x^{\beta_j-1/2}e^{i(\gamma_j-U)\log x}
+x^{1/2-\beta_j}e^{i(\gamma_j-U)\log x}
=2\cosh(ht)e^{2\pi ijt}.
\tag{28}
\]

Likewise each added screen pair with integer phase lift `n` contributes exactly

\[
2\cosh(a_Mt)e^{i(\pm\phi_M+2\pi n)t}.
\tag{29}
\]

Thus `R_M(t)=B_M(t)+S_M^{lift}(t)` is exactly the selected zero-residue integrand after extracting the common `x^{-1/2}` factor and common explicit-formula sign.

Let `Q_M(s,\lambda)` be the selected residue in the twisted short interval with endpoints `x_M(s)` and `x_M(s+\lambda)`. The classical integrated zero term is

\[
Q_M(s,\lambda)
=-\int_{x_M(s)}^{x_M(s+\lambda)}x^{-1/2}R_M(t(x))\,dx.
\tag{30}
\]

Since

\[
\frac{dx_M(v)}{dv}=x_M(v)\frac{L}{dM},
\tag{31}
\]

profile convergence gives, uniformly for `s` in a fixed compact interval,

\[
\boxed{
\frac{Q_M(s,\lambda)}{X^{1/2}L/d}
\to-\int_s^{s+\lambda}F_{h,\kappa,q}(v)\,dv.
}
\tag{32}
\]

Because `F` is continuous and nonzero by (3),

\[
\lambda^{-1}\int_s^{s+\lambda}F(v)\,dv\to F(s)
\tag{33}
\]

uniformly on compact `s`-intervals as `\lambda\downarrow0`. Hence, for every lifted limit (1), fixed `c>0` may be chosen and then a sufficiently small fixed `\lambda>0` chosen so that

\[
J_{h,\kappa,q}(c,\lambda)
:=\int_{-c}^{c-\lambda}
\left|\int_s^{s+\lambda}F_{h,\kappa,q}(v)\,dv\right|^2ds>0.
\tag{34}
\]

The physical short length is

\[
K\sim\lambda\frac{XL}{dM}.
\tag{35}
\]

Integrating (32) over the corresponding starting-point slab and using `dx_M/ds\sim XL/(dM)` gives

\[
\boxed{
\int |Q_M(x)|^2dx
=\left(J_{h,\kappa,q}(c,\lambda)+o(1)\right)
\frac{X^2L^3}{d^3M}.
}
\tag{36}
\]

The raw-prime Gallagher diagonal from WI-195/WI-209 is

\[
XK\log X
\sim\frac{2\lambda X^2L^2}{d^2M},
\qquad \log X=\frac{2L}{d}.
\tag{37}
\]

Therefore

\[
\boxed{
\frac{\int |Q_M(x)|^2dx}{XK\log X}
=\left(\frac{J_{h,\kappa,q}(c,\lambda)}{2\lambda d}+o(1)\right)L.
}
\tag{38}
\]

The natural continuum residual is thus not a free extra Fourier channel: it is a concrete physical short-interval observable at exactly the Gallagher scale, and the selected screened-bow residue is logarithmically superdiagonal there.

## 4. Evidence boundary and source bottleneck

Equation (38) concerns only the deliberately selected bow plus its WI-211 two-pair screen. The full source-fixed explicit formula also contains all complementary nontrivial zeros, pole/trivial terms, contour remainder, and the structured prime-side subtraction used in the WI-195 bridge. Accordingly no lower bound for the selected vector alone is an unconditional lower bound for the full source error.

A theorem of the schematic strength

\[
\|E_{\rm src}\|_2^2\ll XK\log X
\tag{39}
\]

on this distinguished slab would, together with (38), force the complementary source vector to approximate `-Q_M` to relative `O(L^{-1/2})`. WI-195 shows that currently audited short-interval major-arc technology does not provide the required square-root-scale variance for the relevant `\Lambda-\Lambda^\sharp` source norm, even though its interval and Archimedean-twist ranges fit the bow. WI-209 derived the same near-opposite cancellation burden for the unscreened dense bow; the new point is that WI-211's exact sparse two-harmonic screen does not remove it.

This result does not rule out changing the two screen depths/phases away from WI-211's equal-depth construction, using more than two added off-line pairs, or arranging cancellation by remote/global zero populations. WI-212's finite-packet barrier therefore remains valid: finitely many discrete samples alone do not charge sparse screens. What is now excluded is the simplest and most dangerous escape suggested by WI-211, namely that its exact two-pair sample screen might remain low-energy throughout the natural coherent peak merely by choosing different integer phase representatives.

## 5. Prior-art and novelty audit

The ingredients are separated by provenance. The Dirichlet-kernel identity (12) and its local sinc limit are classical Fourier analysis. The integrated zero residue (30) is the classical explicit-formula identity already used in WI-205/WI-209. The short-interval `L^2`/Gallagher scale and its current arithmetic barrier were audited in WI-195; weighted Gallagher variants are classical prior art, including Coppola--Laporta (2015). Truncated trigonometric and indefinite moment interpolation have a broad classical/operator-theoretic literature, including Derkach--Hassi--de Snoo (2012), and provide context for WI-210--WI-212's finite-sample screening phenomena.

A fresh prior-art search around Dirichlet-kernel local limits, Gallagher short-interval mean squares, trigonometric moment interpolation, and indefinite moment completion did not locate a statement matching the specific lifted WI-211 profile (1)--(3) or the source-coordinate conversion (26)--(38). That absence is not used as a priority claim. The durable mathematical claim is only the exact derivation above from the already-audited WI-211 screen and classical identities.

## Research consequence

`CLUE-two-harmonic-screen-continuum-residual` is resolved in a narrowed form. Its central asymptotic is correct; optimizing integer phase lifts reduces the best leading small-window coefficient by a factor `9` but cannot erase it; and the `1/M` frequency width converts exactly to a physical `XL/M` Gallagher-scale slab whose selected residue remains `Omega(\log T)` superdiagonal in energy. The surviving bottleneck is therefore the source-level complement: either prove a diagonal-scale upper bound for the full source-fixed error on this distinguished slab, or construct a genuinely more general off-line screen whose continuum residue cancels there as well.