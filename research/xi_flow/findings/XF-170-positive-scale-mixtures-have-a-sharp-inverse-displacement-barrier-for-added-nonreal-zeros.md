---
type: negative
research_line: xi_flow
finding_id: XF-170
status: canonical
---

# XF-170 — Positive scale mixtures have a sharp inverse-displacement barrier for added nonreal zeros

**Evidence classification:** `EXACT-DERIVED + SHARP-OBSTRUCTION`. The zero-free slab and its equality case follow from a direct one-sign integral argument for the cosine transform of a positive even compactly supported measure. No external theorem is load-bearing. The Xi-flow consequence uses only the exact scale-mixture/Fourier dictionary already established in XF-169.

## Statement

XF-169 showed, for one explicit three-atom Xi scale mixture, that a logarithmic square-lattice displacement `delta=4c` creates its first added nonreal zero at real height `T=pi/c=4pi/delta`. That inverse law is not an artifact of the chosen three-atom weights. It is the sharp universal lower barrier for the entire positive compact scale-mixture gauge.

Let `nu` be a finite positive even Borel measure on `R`, compactly supported and not concentrated at the origin. Put

\[
c_\nu:=\max\{|a|:a\in\operatorname{supp}\nu\}>0
\tag{1}
\]

and define its even entire cosine transform

\[
m_\nu(z):=\int_{\mathbb R}\cos(az)\,d\nu(a).
\tag{2}
\]

Then

\[
\boxed{
 m_\nu(z)\ne0
 \quad\text{whenever}\quad
 \operatorname{Im}z\ne0,
 \qquad
 |\operatorname{Re}z|<\frac{\pi}{c_\nu}.
}
\tag{3}
\]

Equivalently, every nonreal zero of `m_nu` satisfies

\[
\boxed{
 |\operatorname{Re}z|\,c_\nu\ge\pi.
}
\tag{4}
\]

The constant is sharp. Equality in `(4)` at a nonreal zero can occur only when

\[
\operatorname{supp}\nu\subset\{0,-c_\nu,c_\nu\}.
\tag{5}
\]

Conversely, for every `c>0` and every prescribed `y_0>0`, there is a positive even measure supported exactly on `{0,-c,c}`, normalized by

\[
\int\cosh a\,d\nu(a)=1,
\tag{6}
\]

whose cosine transform vanishes at

\[
z=\frac{\pi}{c}\pm i y_0.
\tag{7}
\]

The XF-167 family is the special case `y_0=1`.

Now place `(2)` back into the normalized Xi scale-mixture class of XF-169. Define

\[
\rho_\nu(u):=\int_{\mathbb R}\Phi(u+a)\,d\nu(a),
\qquad
\int\cosh a\,d\nu(a)=1,
\tag{8}
\]

so that `rho_nu` is a positive even Xi-source mixture preserving the standard real-axis Jacobi/Riemann normalization, and

\[
H_0^{(\nu)}(z)=m_\nu(z)H_0(z).
\tag{9}
\]

Translation by `a` moves the corresponding square-lattice copy by logarithmic scale `4a`. If

\[
\delta_{\rm shift}:=4c_\nu,
\tag{10}
\]

is the full logarithmic shift radius of the mixture, every **added nonreal multiplier zero** obeys the sharp resolution law

\[
\boxed{
\delta_{\rm shift}\,|\operatorname{Re}z|\ge4\pi.
}
\tag{11}
\]

Consequently the nonreal zero divisor of `H_0^(nu)` inside

\[
|\operatorname{Re}z|<\frac{4\pi}{\delta_{\rm shift}}
\tag{12}
\]

is exactly the nonreal zero divisor already inherited from `H_0`; a positive compact Xi scale mixture cannot create an additional nonreal zero below that height.

On the Mellin side, XF-169 gives

\[
M_\nu(s)=m_\nu(z),
\qquad
s=\frac12+\frac{iz}{2}.
\tag{13}
\]

Hence every zero of the gauge factor `M_nu` away from the critical line satisfies

\[
\boxed{
\delta_{\rm shift}\,|\operatorname{Im}s|\ge2\pi.
}
\tag{14}
\]

Thus the inverse-displacement/high-zero coupling left by XF-169 is exact throughout the positive compact scale-mixture class, not merely an example-based falsification scale.

## 1. Positivity forces a one-sign imaginary part

Write

\[
z=x+iy.
\tag{15}
\]

Because `nu` is even, `m_nu` is even in `z`, and because it is real on the real axis its zeros are also invariant under conjugation. It therefore suffices to consider `x>=0` and `y>0`.

For real `a,x,y`,

\[
\cos(a(x+iy))
=
\cos(ax)\cosh(ay)
-i\sin(ax)\sinh(ay).
\tag{16}
\]

Thus

\[
\operatorname{Im}m_\nu(x+iy)
=-\int_{\mathbb R}\sin(ax)\sinh(ay)\,d\nu(a).
\tag{17}
\]

The integrand in `(17)` is even in `a`, so

\[
\operatorname{Im}m_\nu(x+iy)
=-2\int_{(0,c_\nu]}
\sin(ax)\sinh(ay)\,d\nu(a).
\tag{18}
\]

If

\[
0<x<\frac{\pi}{c_\nu},
\tag{19}
\]

then for every `a` in `(0,c_nu]`,

\[
0<ax<\pi,
\qquad
\sin(ax)>0,
\qquad
\sinh(ay)>0.
\tag{20}
\]

Since `c_nu>0` and `c_nu` belongs to the support, the positive half-line carries nonzero `nu`-mass. Equation `(18)` is therefore strictly negative. In particular `m_nu(x+iy)` cannot vanish.

At `x=0` there is an even simpler obstruction:

\[
m_\nu(iy)
=\int_{\mathbb R}\cosh(ay)\,d\nu(a)>0.
\tag{21}
\]

Reflection in `x` and conjugation in `y` prove `(3)` and `(4)`.

The proof is deliberately elementary because it identifies the load-bearing hypotheses exactly: **positivity, evenness, and a finite shift radius**. No decay estimate for Xi, no zero statistics, and no Jacobi theorem enter the zero-free slab itself.

## 2. The boundary case forces a three-point support

Suppose `y>0` and

\[
m_\nu\!\left(\frac{\pi}{c_\nu}+iy\right)=0.
\tag{22}
\]

At the boundary `x=pi/c_nu`, the integrand in `(18)` is strictly positive for every

\[
0<a<c_\nu,
\tag{23}
\]

and vanishes only at `a=0` and `a=c_nu`. Since the imaginary part in `(22)` is zero and `nu` is positive,

\[
\nu((0,c_\nu))=0.
\tag{24}
\]

Evenness then forces `(5)`. Because `c_nu` is actually in the support, there is positive endpoint mass. Write

\[
\nu=w_0\delta_0+w(\delta_c+\delta_{-c}),
\qquad c=c_\nu,
\qquad w>0,
\qquad w_0\ge0.
\tag{25}
\]

Then

\[
m_\nu(z)=w_0+2w\cos(cz).
\tag{26}
\]

At `z=pi/c+iy`,

\[
\cos(\pi+icy)=-\cosh(cy),
\tag{27}
\]

so `(22)` is equivalent to

\[
\boxed{w_0=2w\cosh(cy).}
\tag{28}
\]

In particular a nonreal boundary zero requires both the central and endpoint masses.

Conversely fix any `c>0` and `y_0>0`. Choosing

\[
w=
\frac{1}{2(\cosh(cy_0)+\cosh c)},
\qquad
w_0=
\frac{\cosh(cy_0)}{\cosh(cy_0)+\cosh c}
\tag{29}
\]

makes `(28)` hold and also gives

\[
w_0+2w\cosh c=1,
\tag{30}
\]

which is exactly the Jacobi normalization `(6)`. This proves `(7)` and sharpness. At `y_0=1`, `(29)` reduces to

\[
w_0=\frac12,
\qquad
w=\frac{1}{4\cosh c},
\tag{31}
\]

which is precisely the XF-167/XF-169 stress family. Its equality in `(11)` is therefore extremal for the whole positive compact gauge, not just convenient algebra.

## 3. Translation to the Xi source and Mellin gauges

XF-169 classifies normalized positive compact Xi shift mixtures by evenness of `nu` together with `(6)`. In that class the theta prekernel is

\[
F_\nu(x)
=
\int e^aF_\Xi(e^{4a}x)\,d\nu(a),
\tag{32}
\]

so an atom at shift `a` generates a square-lattice copy

\[
\{\pi n^2e^{4a}:n\ge1\}.
\tag{33}
\]

The natural log-scale shift parameter carried by this representation is therefore `4a`, giving `(10)`.

The same shift measure appears at time zero as the exact Fourier multiplier `(2)`, yielding `(9)`. If `z` is nonreal and lies in the open slab `(12)`, `(3)` says `m_nu(z)` is nonzero. Multiplication by a nonvanishing analytic factor preserves the zero multiplicity of `H_0` there, which proves the nonreal-divisor statement after `(12)`.

Equation `(13)` transfers the geometry to the completed Mellin factor. If `z=x+iy`, then

\[
s=\frac{1-y}{2}+i\frac{x}{2}.
\tag{34}
\]

Thus `z` is nonreal exactly when the corresponding `s` is off the critical line, and `|Im s|=|x|/2`. Combining this with `(4)` and `delta_shift=4c_nu` gives `(14)`.

This is the quantitative source-stability statement that XF-168 and XF-169 were pointing toward, but only **inside the exact positive Xi scale-mixture gauge**. It says that bounded positive support contamination has a finite-height rigidity window whose width is precisely inverse to its logarithmic shift radius.

## 4. What this does and does not buy for the transition

The useful advance is a sharp finite-height statement. XF-169 showed that the explicit three-lattice control becomes invisible on fixed Mellin windows as `c->0` while its first added nonreal zero recedes like `1/c`. XF-170 proves that this inverse law is unavoidable for every positive compact normalized scale mixture: no redistribution of positive shift mass can beat the constant `4pi` in the `z` coordinate.

This prevents one misleading interpretation of the earlier counterexample. The high-zero escape of XF-167 is not caused by a badly chosen three-point mixture that could be redesigned to place nonreal defects at `o(1/c)` height. Positivity and compact shift support themselves forbid that. Any theorem controlling positive scale-mixture contamination through height `T` should therefore naturally resolve the dimensionless product

\[
\delta_{\rm shift}T.
\tag{35}
\]

Within this class, the onset `delta_shift T=4pi` is both necessary and sharp for **added nonreal multiplier zeros**.

The result still does not yield an upper bound on the de Bruijn--Newman constant. It controls only zeros contributed by the time-zero multiplier `m_nu`. It neither removes nonreal zeros already present in `H_0` nor determines how the product's zeros subsequently evolve under heat. Source identification at `delta_shift=0` remains exactly Xi and therefore returns to the original RH problem, as XF-168 emphasized.

Nor does the result say that the multiplier has no zeros at smaller real height. Real multiplier zeros can occur earlier. For example a normalized measure supported only at `+-c` has multiplier proportional to `cos(cz)`, whose first zeros are real at `|z|=pi/(2c)`. The `4pi` law is specifically a barrier for **new nonreal zero geometry**, the feature relevant to a positive transition obstruction.

## Prior-art and novelty audit

Zeros of Fourier/cosine transforms of positive compactly supported kernels and zeros of Laplace transforms of finite measures have a substantial classical literature, including Pólya-type real-zero criteria and general zero-localization questions. A targeted audit of that literature was used to check whether `(3)` was merely a named theorem being rediscovered. No external result is needed here: `(18)`--`(20)` prove the required slab directly and expose the exact equality mechanism.

Accordingly no general novelty claim is made for the abstract sign observation about cosine transforms. The durable Mathia-specific content is the sharp transfer through the XF-169 dictionary: the full positive compact Xi scale-mixture gauge obeys the exact resolution barrier `delta_shift |Re z| >= 4pi`, the XF-167 family saturates it, and the corresponding Mellin gauge cannot add an off-critical zero before `delta_shift |Im s|=2pi`. No newly located theorem is load-bearing, so `SOURCES.md` needs no update.

## Falsification boundary

Positivity is essential to `(18)`: signed or complex shift measures can cancel the one-sign imaginary part and are not covered. Compact support is also essential to the finite number `c_nu`; an unbounded positive shift law has no analogous conclusion from this argument alone. Evenness is load-bearing for the cosine multiplier and for the normalized Xi/Jacobi gauge. The theorem does not classify arbitrary perturbations of the individual atoms `pi n^2 e^{epsilon_n}` where the displacement varies with `n` independently of a common scale-mixture measure.

The parameter `delta_shift` in `(10)` is the logarithmic radius of the **generating Xi scale shifts**. It is not asserted to equal a Hausdorff distance from the union of the resulting atoms to the base square lattice, because different square indices can come close after rescaling. Any use of `(11)` outside the shift-mixture representation must first justify the corresponding dictionary.

Finally, `(12)` concerns the nonreal zero divisor only. Real multiplier zeros inside that slab, possible collisions with real Xi zeros, or positive-time heat evolution are separate questions. Any attempt to promote `(11)` directly to a bound on `Lambda` without a heat-dynamical bridge would exceed the result.

## Relation to prior findings

XF-167 constructed a positive, completely monotone, Jacobi-reflecting three-scale Xi source with a positive transition and explicit nonreal multiplier zeros. XF-168 showed that returning exactly to the single square lattice forces the Xi weights by Hamburger rigidity. XF-169 then classified the whole normalized Xi shift-mixture gauge and observed the exact `4pi/delta` displacement--height law for the XF-167 family.

XF-170 upgrades that last example into a sharp theorem for every positive compact member of the gauge. The source-stability picture is now quantitative at finite height: exact single-lattice support gives exact Hamburger identification, while a nonzero positive shift radius `delta_shift` cannot manufacture an added nonreal zero until height at least `4pi/delta_shift`, and this threshold cannot be improved.

## Consequence for `xi_flow`

The scale-mixture branch no longer needs further searches for a better positive measure that defeats the inverse-displacement scale: XF-170 proves that none exists. The live source-to-transition problem is therefore not to optimize the XF-167 mixture, but to leave this gauge in a mathematically meaningful way.

A genuinely stronger support-stability theorem must handle atomwise or mesoscopic deformations that are not common positive scale mixtures, or must combine the finite-height rigidity window with an independent Xi-specific heat/collision estimate. Conversely, a negative control that wants to beat the `delta_shift T` barrier must identify exactly which load-bearing hypothesis of XF-170 it gives up: positivity, compact common shift support, evenness, or the common scale-mixture representation.