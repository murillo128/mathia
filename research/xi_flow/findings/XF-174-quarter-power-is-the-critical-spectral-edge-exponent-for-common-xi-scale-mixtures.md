---
type: theorem
research_line: xi_flow
finding_id: XF-174
status: canonical
---

# XF-174 — Quarter-power is the critical spectral-edge exponent for common Xi scale mixtures

**Evidence classification:** `EXACT-DERIVED + TWO-SIDED-SOURCE-EQUIVALENCE + ORDER-SHARP-STABILITY`. Inside the normalized positive even common Xi scale-mixture gauge, a subcritical family of source-visible Laplace edge observables is quantitatively equivalent to the XF-171 central Mellin deficit. The `1/4` weight used in XF-172 is exactly the critical exponent at which this equivalence fails and the logarithmic tail tax of XF-173 appears. No external theorem is load-bearing.

## Statement

Let `nu` be a finite positive even Borel measure on `R` satisfying

\[
\int_{\mathbb R}\cosh a\,d\nu(a)=1,
\tag{1}
\]

and let

\[
d_\nu
=\int_{\mathbb R}(\cosh a-1)\,d\nu(a)
\tag{2}
\]

be the XF-171 central Mellin deficit. Let the common-scale theta prekernel have positive Laplace measure

\[
\mu_\nu
=\int_{\mathbb R}e^a
\sum_{n\ge1}\delta_{\pi n^2e^{4a}}\,d\nu(a),
\tag{3}
\]

as in XF-169--XF-173.

For `alpha >= 0`, define the renormalized edge weight on `x>=1` by

\[
W_\alpha(x)
:=
\begin{cases}
\left(\dfrac{x^\alpha-1}{\alpha}\right)^2,&\alpha>0,\\[6pt]
(\log x)^2,&\alpha=0,
\end{cases}
\tag{4}
\]

and the source-visible subfundamental observable

\[
\boxed{
\mathcal E_{\nu,\alpha}
:=
\int_{(0,\pi)}
W_\alpha\!\left(\frac{\pi}{\lambda}\right)
\,d\mu_\nu(\lambda).
}
\tag{5}
\]

Then for every fixed

\[
\boxed{0\le\alpha<\frac14}
\tag{6}
\]

there exist finite constants

\[
0<c_\alpha\le C_\alpha<\infty
\tag{7}
\]

depending only on `alpha` such that every normalized positive even common-scale mixture obeys

\[
\boxed{
 c_\alpha d_\nu
 \le \mathcal E_{\nu,\alpha}
 \le C_\alpha d_\nu.
}
\tag{8}
\]

In particular `mathcal E_(nu,alpha)` is automatically finite under the original normalization `(1)`, with no extra logarithmic or exponential tail moment, and

\[
\boxed{
\mathcal E_{\nu,\alpha}=0
\iff d_\nu=0
\iff \nu=\delta_0.
}
\tag{9}
\]

Combining `(8)` with XF-171 gives a directly source-visible finite-height zero-resolution criterion. If

\[
\boxed{
\mathcal E_{\nu,\alpha}
<\frac{c_\alpha}{4T^2+2},
}
\tag{10}
\]

then the common-mixture Mellin multiplier `M_nu(s)` has no zero anywhere in

\[
0\le\operatorname{Re}s\le1,
\qquad
|\operatorname{Im}s|\le T.
\tag{11}
\]

The exponent `1/4` is a genuine threshold. At `alpha=1/4`, `mathcal E_(nu,1/4)=16 mathcal L_nu`, where `mathcal L_nu` is exactly the XF-172 leakage, and its shift kernel pays the XF-173 logarithmic tax. For every `alpha>1/4`, the tail surcharge is exponential relative to `d_nu`.

The parameter-free logarithmic choice

\[
\boxed{
\mathcal E_{\nu,0}
=\int_{(0,\pi)}
\log^2\!\left(\frac{\pi}{\lambda}\right)
\,d\mu_\nu(\lambda)
}
\tag{12}
\]

is therefore a particularly simple source-visible defect equivalent to `d_nu` on the full unbounded common-scale gauge.

## 1. Exact one-shift kernel

Only negative shifts place square-lattice atoms below `pi`. Write `a=-b`, `b>0`. The `n`th atom then lies at

\[
\lambda_{n,b}=\pi n^2e^{-4b}
\tag{13}
\]

with Laplace mass factor `e^-b`, and it lies below `pi` exactly when

\[
n<e^{2b}.
\tag{14}
\]

Define

\[
\boxed{
K_\alpha(b)
:=e^{-b}
\sum_{1\le n<e^{2b}}
W_\alpha\!\left(\frac{e^{4b}}{n^2}\right).
}
\tag{15}
\]

Tonelli and evenness give the exact representation

\[
\boxed{
\mathcal E_{\nu,\alpha}
=\int_{(0,\infty)}K_\alpha(b)\,d\nu(b).
}
\tag{16}
\]

On the same positive half-line the Mellin deficit is

\[
\boxed{
 d_\nu
 =\int_{(0,\infty)}D(b)\,d\nu(b),
 \qquad
 D(b):=2(\cosh b-1).
}
\tag{17}
\]

Thus the whole question is whether `K_alpha` and `D` are comparable uniformly in the shift `b`.

When

\[
0<b\le\frac12\log2,
\tag{18}
\]

only `n=1` contributes. For `alpha>0`,

\[
K_\alpha(b)
=e^{-b}
\left(\frac{e^{4\alpha b}-1}{\alpha}\right)^2,
\tag{19}
\]

while

\[
K_0(b)=16b^2e^{-b}.
\tag{20}
\]

Since

\[
D(b)=e^{-b}(e^b-1)^2,
\tag{21}
\]

we obtain the common small-shift limit

\[
\boxed{
\frac{K_\alpha(b)}{D(b)}\longrightarrow16,
\qquad b\downarrow0,
\quad \alpha\ge0.
}
\tag{22}
\]

The renormalization by `alpha^-2` in `(4)` was chosen precisely so that the fractional family has a nondegenerate logarithmic limit and the same local normalization.

## 2. Subcritical weights have exactly the normalization tail

For `alpha>0`, let

\[
N(b):=\lceil e^{2b}\rceil-1,
\qquad
H_N^{(p)}:=\sum_{n\le N}n^{-p}.
\tag{23}
\]

Expanding `(15)` gives the exact formula

\[
\boxed{
K_\alpha(b)
=\frac{e^{-b}}{\alpha^2}
\left[
 e^{8\alpha b}H_{N(b)}^{(4\alpha)}
 -2e^{4\alpha b}H_{N(b)}^{(2\alpha)}
 +N(b)
\right].
}
\tag{24}
\]

If `0<alpha<1/4`, elementary sum-integral comparison yields

\[
H_N^{(p)}
=\frac{N^{1-p}}{1-p}+O(1)
\qquad(0<p<1).
\tag{25}
\]

Since `N(b)=e^{2b}+O(1)`, substitution into `(24)` gives

\[
\boxed{
K_\alpha(b)
=
\frac{8}{(1-4\alpha)(1-2\alpha)}e^b
+o(e^b),
\qquad b\to\infty.
}
\tag{26}
\]

The coefficient comes from

\[
\frac1{\alpha^2}
\left(
\frac1{1-4\alpha}
-\frac2{1-2\alpha}
+1
\right)
=
\frac8{(1-4\alpha)(1-2\alpha)}.
\tag{27}
\]

For `alpha=0`, `(15)` becomes

\[
K_0(b)
=e^{-b}
\sum_{n<e^{2b}}
(4b-2\log n)^2.
\tag{28}
\]

Writing `N=e^(2b)`, the normalized sum is a Riemann sum for `4 log^2(1/x)` on `(0,1)`, whose integral is `8`. Equivalently, elementary monotone sum-integral comparison gives

\[
\boxed{
K_0(b)=8e^b(1+o(1)).
}
\tag{29}
\]

Because

\[
D(b)=e^b(1+o(1)),
\tag{30}
\]

we therefore have

\[
\boxed{
\frac{K_\alpha(b)}{D(b)}
\longrightarrow
\begin{cases}
\dfrac8{(1-4\alpha)(1-2\alpha)},&0<\alpha<1/4,\\[8pt]
8,&\alpha=0,
\end{cases}
\qquad b\to\infty.
}
\tag{31}
\]

No extra factor `b` survives. The observable sees remote scale contamination with exactly the `e^b` order already forced by the Jacobi normalization.

## 3. Global two-sided equivalence

At a threshold `e^(2b)=m` where a new lattice atom enters `(15)`, that new term has argument `e^(4b)/m^2=1`, and `W_alpha(1)=0`. Hence `K_alpha(b)` is continuous for `b>0` despite the changing number of summands. It is strictly positive for every `b>0` because the `n=1` contribution is positive.

Therefore

\[
R_\alpha(b):=\frac{K_\alpha(b)}{D(b)}
\tag{32}
\]

is positive and continuous on `(0,infinity)`. Equations `(22)` and `(31)` extend it continuously to both endpoints `b=0` and `b=infinity`, with finite positive limits. Compactness after this two-end compactification gives

\[
0<c_\alpha
:=\inf_{b>0}R_\alpha(b)
\le
\sup_{b>0}R_\alpha(b)
=:C_\alpha
<\infty.
\tag{33}
\]

Multiplying `(33)` by `D(b)dnu(b)` and integrating proves `(8)`. In particular, normalization `(1)` implies `d_nu<1` and therefore automatically

\[
\mathcal E_{\nu,\alpha}<\infty
\qquad(0\le\alpha<1/4),
\tag{34}
\]

without any additional tail hypothesis.

The lower bound in `(8)` and XF-171 immediately prove `(9)` and `(10)`--`(11)`. Thus the open alternative left by XF-173 has a positive answer: a regularized source-visible spectral observable can recover the intrinsic central Mellin topology without paying the `b e^b` tax.

## 4. The quarter-power phase transition

At the endpoint `alpha=1/4`, `(4)` gives

\[
W_{1/4}(x)=16(x^{1/4}-1)^2,
\tag{35}
\]

so

\[
\boxed{
\mathcal E_{\nu,1/4}=16\mathcal L_\nu,
}
\tag{36}
\]

with `mathcal L_nu` exactly the XF-172 observable. XF-173 therefore becomes the endpoint asymptotic

\[
\boxed{
\frac{K_{1/4}(b)}{D(b)}
=32b+O(1).
}
\tag{37}
\]

The logarithmic tail tax is not an accidental choice of normalization: it is the critical harmonic divergence of `H_N^(4 alpha)` when `4 alpha=1`.

For `alpha>1/4`, the first generalized harmonic sum in `(24)` converges to the positive finite constant `zeta(4alpha)`, and it dominates the other two terms. Hence

\[
\boxed{
K_\alpha(b)
\sim
\frac{\zeta(4\alpha)}{\alpha^2}
 e^{(8\alpha-1)b},
}
\tag{38}
\]

and therefore

\[
\boxed{
\frac{K_\alpha(b)}{D(b)}
\sim
\frac{\zeta(4\alpha)}{\alpha^2}
 e^{(8\alpha-2)b}.
}
\tag{39}
\]

So the three regimes are sharp and qualitatively distinct:

\[
\boxed{
\begin{array}{c|c}
0\le\alpha<1/4 & K_\alpha(b)\asymp e^b \\ 
\alpha=1/4 & K_\alpha(b)\asymp b e^b \\ 
\alpha>1/4 & K_\alpha(b)/e^b\text{ grows exponentially.}
\end{array}
}
\tag{40}
\]

This identifies `1/4` as the exact spectral-edge integrability threshold for the normalized common-scale gauge.

## 5. Stress test: finite-height scale remains order-sharp

Take the XF-167/XF-171 three-atom family

\[
\nu_c
=\frac12\delta_0+
\frac{1}{4\cosh c}(\delta_c+\delta_{-c}),
\qquad c>0.
\tag{41}
\]

For sufficiently small `c`, only the negatively shifted `n=1` atom lies below `pi`, so equations `(19)`--`(22)` give

\[
\boxed{
\frac{\mathcal E_{\nu_c,\alpha}}{d_c}
\longrightarrow16
\qquad(c\downarrow0)
}
\tag{42}
\]

for every fixed `0<=alpha<1/4`. XF-171 gives

\[
d_cT_c^2\longrightarrow\frac{\pi^2}{16},
\qquad
T_c=\frac{\pi}{2c},
\tag{43}
\]

so

\[
\boxed{
\mathcal E_{\nu_c,\alpha}T_c^2
\longrightarrow\pi^2.
}
\tag{44}
\]

Thus replacing `d_nu` by the source-visible subcritical edge observable preserves the order-sharp inverse-square-root height scale. The result does not merely prove finiteness; it preserves the correct perturbative resolution law.

## Prior-art and novelty audit

The mandatory audit checked classical Jacobi-theta/Mellin/Laplace representations, positive Laplace-measure background, and generalized soft-lattice theta constructions. Those sources supply the surrounding transform language but not the kernel comparison above. No located result states the `alpha=1/4` edge phase transition for the normalized Xi common-scale mixture, nor the two-sided equivalence `(8)` used here.

No external theorem is load-bearing. Equations `(24)`--`(31)` use only the already-persisted XF-169 Laplace mixture formula and elementary sum-integral asymptotics; the global equivalence is then a positivity/continuity argument. `SOURCES.md` therefore requires no new anchor.

## Falsification boundary

Positivity, evenness, and the common-scale representation remain load-bearing. They permit the one-sided kernel formula `(16)` and identify the positive-half normalization kernel with `D(b)`. Signed mixtures, asymmetric shifts, or atomwise displacement of `pi n^2` do not satisfy this reduction.

The theorem controls zeros added by the common-mixture multiplier. It does not constrain zeros inherited from the Xi factor, does not prove RH or `Lambda=0`, and does not yet supply an atomwise/mesoscopic stability modulus once different square-lattice atoms move by different amounts.

The constants `c_alpha,C_alpha` are asserted to exist and are source-independent, but are not optimized. XF-171's zero-free constant is also not claimed sharp. The order `T~mathcal E^(-1/2)` is the robust statement, with `(44)` showing that no parametrically stronger power follows from this defect alone.

## Relation to prior findings

XF-171 found the intrinsic unbounded-support zero-resolution modulus `d_nu`. XF-172 made it source-visible using the quarter-power edge weight but only in the one-sided direction `d_nu<=mathcal L_nu`. XF-173 then showed why the reverse direction fails: at exactly that weight, summing the crossed square-lattice atoms produces one extra logarithmic shift moment.

XF-174 identifies that failure as a critical-exponent phenomenon rather than a generic obstruction. Lower the edge singularity below the quarter-power threshold, or use the logarithmic endpoint `(12)`, and the source-visible defect becomes globally equivalent to `d_nu` on the entire normalized unbounded common-scale gauge.

## Consequence for `xi_flow`

The common positive scale-mixture metric problem is now quantitatively closed at finite height: there is a source-visible Laplace observable with exactly the same tail topology and the same order-sharp zero-resolution scale as the intrinsic Mellin defect, without a compact-support or uniform-integrability supplement. The quarter-power observable of XF-172 remains useful when its stronger tail control is available, but it is no longer the right default topology for unbounded mixtures.

The next genuinely different source-side gate should therefore leave common global scale mixing and treat **atomwise or mesoscopic deformation of the individual square-lattice atoms `pi n^2`**. There the one-variable shift kernel disappears, and the missing theorem is a local spectral budget that converts approximate square-lattice placement/weights into finite-height control of the corresponding Mellin or Fourier zero geometry.