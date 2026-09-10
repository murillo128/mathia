---
type: theorem
research_line: xi_flow
finding_id: XF-171
status: canonical
---

# XF-171 — Central Mellin deficit gives order-sharp critical-strip zero resolution without compact support

**Evidence classification:** `EXACT-DERIVED + ORDER-SHARP-STABILITY`. The critical-strip estimate follows from a pointwise integral remainder for the cosine function and positivity of the normalized Xi scale-mixture measure. No external theorem is load-bearing. The XF-167 family shows that the resulting inverse-square-root height scale cannot be improved in order.

## Statement

XF-170 proved a sharp `delta_shift |Re z| >= 4 pi` barrier for positive **compactly supported** Xi scale mixtures, where `delta_shift` is the hard logarithmic shift radius. The compact-support hypothesis leaves open a softer question: can one obtain finite-height zero resolution from an intrinsic scalar defect even when arbitrarily remote shifts are allowed with very small mass?

Let `nu` be a finite positive even Borel measure on `R`, not assumed compactly supported, satisfying the normalized Xi/Jacobi moment

\[
\int_{\mathbb R}\cosh a\,d\nu(a)=1.
\tag{1}
\]

On the closed strip `|Im z| <= 1` define

\[
m_\nu(z):=\int_{\mathbb R}\cos(az)\,d\nu(a),
\tag{2}
\]

and define the **central Mellin deficit**

\[
\boxed{
 d_\nu:=1-m_\nu(0)
 =1-\nu(\mathbb R)
 =\int_{\mathbb R}(\cosh a-1)\,d\nu(a).
}
\tag{3}
\]

Then `0 <= d_nu < 1`, with `d_nu=0` if and only if `nu=delta_0`, and for every `z` with `|Im z| <= 1`,

\[
\boxed{
 |m_\nu(z)-m_\nu(0)|
 \le |z|^2 d_\nu.
}
\tag{4}
\]

Consequently every zero of `m_nu` in that strip obeys

\[
\boxed{
 |z|^2 d_\nu\ge 1-d_\nu.
}
\tag{5}
\]

Equivalently, the multiplier is zero-free in

\[
\boxed{
 |\operatorname{Im}z|\le1,
 \qquad
 |z|<\sqrt{\frac{1-d_\nu}{d_\nu}}.
}
\tag{6}
\]

The same quantity is intrinsic on the Mellin side. With the XF-169 coordinate

\[
M_\nu(s):=\int e^{(1-2s)a}\,d\nu(a),
\qquad
s=\frac12+\frac{iz}{2},
\tag{7}
\]

we have

\[
\boxed{
 d_\nu=1-M_\nu(1/2)
}
\tag{8}
\]

and throughout the critical strip `0 <= Re s <= 1`,

\[
\boxed{
 |M_\nu(s)-M_\nu(1/2)|
 \le 4|s-1/2|^2d_\nu.
}
\tag{9}
\]

Thus a multiplier zero `s=sigma+iT` in the critical strip must satisfy

\[
\boxed{
 4T^2+(1-2\sigma)^2
 \ge \frac{1-d_\nu}{d_\nu}.
}
\tag{10}
\]

In particular, there are no multiplier zeros anywhere in `0 <= Re s <= 1`, `|Im s| <= T` whenever

\[
\boxed{
 d_\nu<\frac{1}{4T^2+2}.
}
\tag{11}
\]

This replaces the hard support radius of XF-170 by a scalar central defect and remains valid for unbounded positive shift laws. The height scale `T ~ d_nu^{-1/2}` is optimal in order.

## 1. The pointwise strip inequality

Fix `z=x+iy` with `|y|<=1`. For `A>=0`, Taylor's formula with integral remainder gives

\[
\cos(Az)-1
=-z^2\int_0^A(A-r)\cos(rz)\,dr.
\tag{12}
\]

For real `r,x,y`,

\[
|\cos(r(x+iy))|^2
=\cos^2(rx)+\sinh^2(ry)
\le \cosh^2 r,
\tag{13}
\]

because `|y|<=1`. Hence

\[
|\cos(Az)-1|
\le |z|^2\int_0^A(A-r)\cosh r\,dr
=|z|^2(\cosh A-1).
\tag{14}
\]

Since cosine and hyperbolic cosine are even in `A`, `(14)` holds for every real `a`:

\[
\boxed{
|\cos(az)-1|
\le |z|^2(\cosh a-1),
\qquad |\operatorname{Im}z|\le1.
}
\tag{15}
\]

The strip width is not decorative. It is exactly the width controlled by the normalization `(1)`; beyond `|Im z|=1`, an unbounded `nu` need not possess the larger exponential moment required even to define the same estimate.

## 2. Positivity turns the normalization defect into a zero-free radius

Integrating `(15)` against the positive measure `nu` and using `(3)` yields

\[
\begin{aligned}
|m_\nu(z)-m_\nu(0)|
&\le \int |\cos(az)-1|\,d\nu(a)\\
&\le |z|^2\int(\cosh a-1)\,d\nu(a)\\
&=|z|^2d_\nu,
\end{aligned}
\tag{16}
\]

which is `(4)`. If `m_nu(z)=0`, then `m_nu(0)=nu(R)=1-d_nu>0`, so

\[
1-d_\nu
=|m_\nu(0)-m_\nu(z)|
\le |z|^2d_\nu,
\tag{17}
\]

proving `(5)` and `(6)`.

Equation `(3)` also shows why this is a genuine source defect rather than another tail gauge. Because `cosh a-1` is nonnegative and vanishes only at `a=0`,

\[
d_\nu=0
\iff \operatorname{supp}\nu\subset\{0\}
\iff \nu=\delta_0,
\tag{18}
\]

where the last equality uses `(1)`. Thus the defect detects any nontrivial positive scale mixing, including arbitrarily small amounts of mass at arbitrarily remote shifts.

There is also a useful probabilistic interpretation on the critical-strip boundary. Evenness and `(1)` imply

\[
\int e^{-a}\,d\nu(a)=1.
\tag{19}
\]

Hence `dP(a)=e^{-a}dnu(a)` is a probability measure. If `A` has law `P`, then

\[
\boxed{
 d_\nu=\frac12\mathbb E_P[(e^A-1)^2].
}
\tag{20}
\]

Indeed the right side equals one half of `int (e^a-2+e^{-a}) dnu(a)`. Thus `d_nu` is exactly an `L^2` multiplicative-scale displacement on the exponentially tilted shift law, not merely a formal central value.

## 3. Mellin translation and finite-height resolution

On `0<=Re s<=1`, the integral in `(7)` is absolutely convergent because

\[
|e^{(1-2s)a}|
\le e^{|a|}
\le 2\cosh a,
\tag{21}
\]

and `(1)` is finite. The XF-169 identity

\[
M_\nu\!\left(\frac12+\frac{iz}{2}\right)=m_\nu(z)
\tag{22}
\]

therefore extends to this noncompact positive class on the whole closed critical strip. Substituting `z=-2i(s-1/2)` into `(4)` proves `(9)`.

If `M_nu(s)=0`, then `(5)` becomes

\[
4|s-1/2|^2d_\nu\ge1-d_\nu.
\tag{23}
\]

Writing `s=sigma+iT` gives `(10)`. Since `|1-2sigma|<=1` in the critical strip, every point with `|T|<=T_0` satisfies

\[
4|s-1/2|^2\le4T_0^2+1.
\tag{24}
\]

Condition `(11)` makes the right side of `(24)` strictly smaller than `(1-d_nu)/d_nu`, proving the uniform finite-height zero-free statement.

For the associated positive Xi source mixture

\[
\rho_\nu(u)=\int\Phi(u+a)\,d\nu(a),
\tag{25}
\]

the time-zero Fourier factorization from XF-169 remains valid on `|Im z|<=1` by absolute Fubini under `(1)`:

\[
H_0^{(\nu)}(z)=m_\nu(z)H_0(z).
\tag{26}
\]

Therefore `(6)` is also a zero-divisor stability statement: inside that critical-strip disk, the perturbed source adds no multiplier zeros and preserves the zero multiplicities inherited from `H_0`.

## 4. Stress test: XF-167 makes the square-root scale unavoidable

The normalized three-point family from XF-167/XF-169 is

\[
\nu_c
=\frac12\delta_0+
\frac{1}{4\cosh c}(\delta_c+\delta_{-c}),
\qquad c>0.
\tag{27}
\]

Its central deficit is

\[
\boxed{
 d_c
=1-\nu_c(\mathbb R)
=\frac{1-\operatorname{sech}c}{2}
=\frac{c^2}{4}+O(c^4).
}
\tag{28}
\]

Its first added nonreal time-zero zeros occur at

\[
z=\frac{\pi}{c}\pm i,
\tag{29}
\]

and its corresponding off-critical Mellin zeros occur at

\[
s=0\mp i\frac{\pi}{2c},
\qquad
s=1\mp i\frac{\pi}{2c}.
\tag{30}
\]

Thus, if `T_c=pi/(2c)`,

\[
\boxed{
 d_cT_c^2\longrightarrow\frac{\pi^2}{16}.
}
\tag{31}
\]

So a theorem based only on `d_nu` cannot replace the scale `T=O(d_nu^{-1/2})` by any parametrically larger power of `1/d_nu`: the explicit positive normalized Xi mixture already develops off-critical multiplier zeros at that order. The constant in `(11)` is not claimed sharp; the **inverse-square-root exponent is**.

This stress test also separates XF-171 from XF-170. XF-170 is stronger when a hard support radius is known and gives the sharp constant `4pi` in the displacement-height product, but it says nothing for unbounded shift support. XF-171 sacrifices that sharp support constant in exchange for a soft, intrinsic defect that still controls arbitrarily remote low-mass contamination.

## Prior-art and novelty audit

Lower bounds for the first real zero of characteristic functions in terms of moments are classical. In particular, Shunlong Luo and Zhengmin Zhang, *Estimating the first zero of a characteristic function*, C. R. Math. 338 (2004), 203--206, DOI `10.1016/j.crma.2003.11.028`, gives general moment-based lower bounds for characteristic-function zeros. That literature is the nearest prior-art class located in the audit.

No theorem from that literature is used in the proof. The bound `(15)` is derived directly and works on a **complex strip** with the Jacobi normalization defect `int(cosh a-1)dnu`, not an ordinary real-axis moment of a probability law. The durable `xi_flow` contribution is the transfer through the XF-169 scale-mixture/Mellin dictionary: the scalar `1-M_nu(1/2)` gives a compact-support-free finite-height zero-resolution modulus, and XF-167 proves its `T ~ d_nu^{-1/2}` order is unavoidable. Because the external paper is prior-art calibration rather than a load-bearing dependency, `SOURCES.md` is unchanged.

## Falsification boundary

Positivity is load-bearing in `(16)` and `(18)`. A signed or complex shift measure can preserve the normalization while cancelling the defect integral and is not covered. Evenness is load-bearing for the normalized Xi scale-mixture dictionary and for the identification of `(1)` with both endpoint exponential moments.

The theorem controls only the strip `|Im z|<=1`, equivalently the Mellin critical strip. A larger strip requires correspondingly stronger exponential moments of `nu`; `(1)` alone cannot provide them for an unbounded shift law. The result also concerns zeros introduced by the common scale-mixture multiplier. It does not control nonreal zeros already present in `H_0`, atomwise perturbations `pi n^2 e^{epsilon_n}` with `n`-dependent displacements, or the later heat evolution of the product.

Finally, `d_nu` is not a substitute for exact square-lattice identification. At `d_nu=0` one recovers `nu=delta_0` inside this gauge, hence exactly Xi, but proving the zero statement for the inherited factor is again RH. The theorem is a stability modulus for **added scale-mixture zero geometry**, not a proof of `Lambda=0`.

## Relation to prior findings

XF-168 showed that exact support on the single Xi square lattice forces the theta weights. XF-169 classified the positive normalized common scale-mixture freedom, and XF-170 proved the sharp inverse-hard-support barrier for added nonreal multiplier zeros. XF-171 supplies the complementary soft theorem: hard support can be discarded entirely if one measures the central Mellin deficit `d_nu=1-M_nu(1/2)`.

The two moduli answer different perturbative questions. `delta_shift T` is the correct sharp parameter for compactly supported common shifts; `d_nu T^2` is an intrinsic finite-height parameter that survives unbounded support and is order-sharp. Neither by itself crosses from source identification to the de Bruijn--Newman transition of the inherited Xi factor.

## Consequence for `xi_flow`

Within the positive normalized common scale-mixture gauge, finite-height source resolution now has both a hard and a soft quantitative form. A reconstruction theorem that controls only central Mellin error can still exclude added off-critical multiplier zeros through height `T` if it proves

\[
d_\nu=o(T^{-2}).
\tag{32}
\]

That is a concrete resolution target, rather than the qualitative demand that a source be "close to Xi". The next source-side gate should either derive such a height-dependent defect from an approximate single-square-lattice law, or leave the common-mixture gauge and treat genuinely atomwise/mesoscopic support deformations. A further qualitative classifier inside the same positive scale-mixture class would not advance the transition problem.