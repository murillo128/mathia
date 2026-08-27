# PF-083 — canonical exact-vs-linearized relative period-two zeta converges and is zero-free

**Status:** `POSITIVE-RELATIVE-REGULARIZATION` + `DECISIVE-NEGATIVE` for the idea that the finite-scale Schwarzian correction of PF-082 can create new critical zeros through the canonical local period-two Selberg/Ruelle sector.

PF-075 proves that the canonical two-letter separator family already makes the absolute transfer trace diverge: infinitely many primitive period-two geodesics have lengths in a fixed positive compact interval.  PF-082 then shows that the exact prime-circle endpoint map

\[
V(p)=\pi\cot\frac{\pi}{p}
\]

is projectively asymptotic to the linear endpoint map `p`, with first fixed-pattern cross-ratio defect at order `p^-4`.

This suggests a geometrically forced relative comparison:

- the **exact flute sector**, built from the true endpoints `V(p_n)`;
- the **projective-tangent reference sector**, built from the linear endpoints `p_n` with exactly the same prime labels and symbolic words.

Unlike an arbitrary subtraction, this reference is the osculating projective geometry already used by the cusp-side tangent construction.

The main result here is that, for the canonical consecutive period-two separator family, the exact/reference **relative Ruelle and Selberg Euler products converge locally uniformly and are nonvanishing throughout `Re s > 0`**, even though the two absolute products separately fail.

That simultaneously gives the first genuinely canonical relative zeta-like cancellation in the prime-flute and shows that the PF-082 Schwarzian correction cannot itself supply critical-line zeros through this sector.

## 1. Exact and linearized consecutive separator lengths

Let four consecutive primes be

\[
p<q<r<t
\]

and define the linear cross-ratio

\[
\chi^0
=
\frac{(r-q)(t-p)}{(q-p)(t-r)}.
\]

The corresponding exact prime-circle cross-ratio is

\[
\chi^E
=
\frac{(V(r)-V(q))(V(t)-V(p))}
     {(V(q)-V(p))(V(t)-V(r))}.
\]

Their primitive separator lengths are

\[
L^0=4\operatorname{arsinh}\sqrt{\chi^0},
\qquad
L^E=4\operatorname{arsinh}\sqrt{\chi^E}.
\]

These are the same canonical two-letter geodesics used in PF-075, evaluated in the linearized and exact endpoint geometries respectively.

## 2. Uniform projective comparison needs no bounded-gap hypothesis

Different from the fixed-offset expansion of PF-082, convergence of the relative product only needs a coarse uniform estimate.

The exact derivative is

\[
V'(x)
=
\frac{\pi^2}{x^2}\csc^2\frac{\pi}{x}
=
\left(\frac{\pi/x}{\sin(\pi/x)}\right)^2.
\]

Hence, for `x` large,

\[
\log V'(x)=O(x^{-2}).
\]

For any `x<y`, the mean value theorem gives

\[
\frac{V(y)-V(x)}{y-x}=V'(\xi)
\]

for some `\xi\in(x,y)`.  If `x\ge p`, therefore

\[
\log\frac{V(y)-V(x)}{y-x}=O(p^{-2})
\]

uniformly, irrespective of the size of `y-x`.

Applying this to the four differences entering the cross-ratio gives

\[
\boxed{
\log\frac{\chi^E}{\chi^0}=O(p^{-2}).
}
\]

No prime-gap theorem beyond the ordering of the primes is used here.

PF-082 gives the sharper specialization for bounded offsets,

\[
\log\frac{\chi^E}{\chi^0}
=
-\frac{\pi^2}{3p^4}(r-p)(t-q)+O(p^{-5}),
\]

so the summable relative correction below contains the exact Schwarzian defect as its first fixed-pattern term.

## 3. Hyperbolic length is Lipschitz in log cross-ratio

Write

\[
F(u)=4\operatorname{arsinh}(e^{u/2}),
\qquad u=\log\chi.
\]

Then

\[
F'(u)
=
2\frac{e^{u/2}}{\sqrt{1+e^u}}
=
2\tanh\frac{L}{4},
\]

and hence

\[
0<F'(u)<2.
\]

Therefore

\[
\boxed{
|L^E-L^0|
\le 2\left|\log\frac{\chi^E}{\chi^0}\right|
=O(p^{-2}).
}
\]

In particular,

\[
\sum_n |L_n^E-L_n^0|<\infty,
\]

since `\sum_p p^{-2}<\infty`.

This does **not** imply that either absolute Ruelle/Selberg product exists: PF-035/PF-075 remain valid.  It says only that the exact and projective-tangent sectors are asymptotically close enough for a relative comparison.

## 4. Relative Ruelle product converges on the whole right half-plane

For `Re s>0`, choose the analytic logarithm

\[
f_s(L)=\log(1-e^{-sL}),
\qquad L>0.
\]

Regarding `L` as a function of `u=\log\chi`,

\[
\frac{d}{du}f_s(L(u))
=
\frac{s}{e^{sL}-1}
\,2\tanh\frac{L}{4}.
\]

For `s` in any compact subset of `Re s>0`, this expression is uniformly bounded for all `L>0`:

- as `L\to0`, it tends to `1/2`;
- as `L\to\infty`, it decays exponentially.

Consequently

\[
\left|
\log\frac{1-e^{-sL^E_n}}{1-e^{-sL^0_n}}
\right|
\le
C_K
\left|\log\frac{\chi^E_n}{\chi^0_n}\right|
\le
C'_K p_n^{-2}.
\]

Thus

\[
\boxed{
\mathcal R_{\rm rel}^{(2)}(s)
:=
\prod_n
\frac{1-e^{-sL^E_n}}
     {1-e^{-sL^0_n}}
}
\]

converges locally uniformly on

\[
\boxed{\operatorname{Re}s>0.}
\]

Because the logarithmic series converges there, the product is holomorphic and nowhere zero:

\[
\boxed{
\mathcal R_{\rm rel}^{(2)}(s)\neq0
\qquad(\operatorname{Re}s>0).
}
\]

This is already enough to rule out the exact-circle Schwarzian correction as a source of critical-line zeros through the canonical local Ruelle sector.

## 5. The corresponding relative Selberg sector also converges

For one primitive length `L`, define its ordinary Selberg factor

\[
Z_L(s)=\prod_{k=0}^{\infty}(1-e^{-(s+k)L}).
\]

We compare `Z_{L^E_n}` and `Z_{L^0_n}`.

For `s` in a compact subset of `Re s>0`, differentiating with respect to `u=\log\chi` gives

\[
\left|\frac{d}{du}\log Z_{L(u)}(s)\right|
\le
C_K
\begin{cases}
L^{-1},&0<L\le1,\\
1,&L\ge1.
\end{cases}
\]

It remains to control how small a consecutive separator can be.  If

\[
X=q-p,\qquad Y=r-q,\qquad Z=t-r,
\]

then

\[
\chi^0
=
\frac{Y(X+Y+Z)}{XZ}
\ge
Y\left(\frac1X+\frac1Z\right).
\]

For all sufficiently large primes, `Y\ge2`.  Setting `M=\max(X,Z)`,

\[
\chi^0\ge\frac4M.
\]

Bertrand's postulate, iterated a fixed number of times, gives `M=O(p)`.  Hence

\[
\frac1{L^0}=O(p^{1/2})
\]

when `L^0` is small.  Since `\chi^E/\chi^0=e^{O(p^{-2})}`, the same bound holds for `L^E`.

Combining this with the projective estimate gives

\[
\left|
\log\frac{Z_{L^E_n}(s)}{Z_{L^0_n}(s)}
\right|
=
O_K(p_n^{-3/2}),
\]

which is summable.

Therefore

\[
\boxed{
\mathcal Z_{\rm rel}^{(2)}(s)
:=
\prod_n
\frac{Z_{L^E_n}(s)}{Z_{L^0_n}(s)}
}
\]

also converges locally uniformly and is nonzero on `Re s>0`.

Again, this is a **sector-relative** Selberg product, not a Selberg zeta for the entire infinite flute.

## 6. Fixed-pattern Schwarzian contribution inside the relative factor

For a bounded recurring pattern at scale `P`, PF-082 gives

\[
\delta L
:=L^E-L^0
=
-\frac{2\pi^2}{3P^4}
(X+Y)(Y+Z)
\tanh\frac{L^0}{4}
+O(P^{-5}).
\]

Hence the corresponding Ruelle logarithm has the explicit first correction

\[
\boxed{
\delta\log(1-e^{-sL})
=
-\frac{2\pi^2s}{3P^4}
\frac{(X+Y)(Y+Z)\tanh(L^0/4)}{e^{sL^0}-1}
+O(P^{-5}).
}
\]

Thus the relative product really does globalize the first projective defect of the exact prime-circle geometry.  But it globalizes it into an **absolutely convergent holomorphic correction**, not into a new divisor.

This is the important negative conclusion.

## 7. What this does and does not rescue from PF-075

PF-075 remains a decisive obstruction to an absolute nuclear transfer operator: its second flat trace contains infinitely many positive contributions of order one.

PF-083 shows that the obstruction is *relative-cancellable* against the canonical projective-tangent reference for this local period-two family:

\[
\boxed{
\text{absolute period-two zeta sector: divergent},
\qquad
\text{exact/reference relative sector: convergent}.
}
\]

This is the first geometrically forced relative cancellation found in the global zeta direction.

However, it does **not** yet construct

\[
\det_{\rm rel}(\Delta_{X_{\rm exact}},\Delta_{X_{\rm lin}})
\]

or a full relative Selberg/Ruelle zeta over every primitive word.  Nonlocal words proliferate, and trace-class resolvent comparability of the two infinite-type Laplacians has not been proved.

That is the next real gate.  Merely multiplying the local factor above by hand over other selected orbit families would again risk becoming an arbitrary generating function.

## 8. Novelty / prior-art audit

Known theory already provides relative determinants and relative zeta functions for suitable pairs of noncompact elliptic operators when heat/resolvent differences are trace class.  Müller develops the abstract relative zeta/determinant formalism; Borthwick--Judge--Perry construct relative determinants for hyperbolic-near-infinity surfaces under controlled perturbations; Aldana treats conformal perturbations on finite-area cusp surfaces.

Those results do not directly cover the present surface: the prime-flute is infinite type, has infinitely many cusps, systole zero, and a non-discrete primitive length spectrum.  Nor do they identify the exact prime-circle endpoint map with its projective tangent as a reference pair.

No targeted search found the specific construction

\[
\boxed{
\pi\cot(\pi/p_n)\text{ flute}
\;/\;
p_n\text{ projective-tangent flute}
\longrightarrow
\text{relative period-two Selberg/Ruelle product}.
}
\]

Novelty is **not** claimed for relative determinant theory, Euler-product ratios, or Schwarzian distortion separately.

The narrow candidate content is the canonical reference geometry plus the summability theorem above.

## 9. Decisive interpretation

PF-082 raised the possibility that the first exact projective defect, of order `P^-4` for bounded patterns, might propagate into a new zeta-like spectral divisor.

For the most canonical local orbit sector, PF-083 rules that out:

\[
\boxed{
\text{exact-circle finite-scale defect}
\longrightarrow
\text{nonzero holomorphic relative factor on }\operatorname{Re}s>0.
}
\]

So the Schwarzian correction survives globally only as a finite multiplicative renormalization in this sector.  It cannot create Riemann-critical-line zeros there.

If a genuinely new global determinant exists, it must come from **interaction among nonlocal primitive words or from a relative Laplacian/scattering construction stronger than this locally factorized cancellation**.

## Lean / symbolic candidates

1. Prove `V'(x)=((pi/x)/sin(pi/x))^2` and `log V'(x)=O(x^-2)`.
2. Prove the mean-value cross-ratio bound `|log(chiE/chi0)| <= C/p^2` for four ordered arguments at least `p`.
3. Prove `0 < d/d(log chi) [4 asinh(sqrt chi)] < 2`.
4. Formalize local uniform convergence of the relative Ruelle logarithmic series from `sum p^-2 < infinity`.
5. Keep the relative Selberg factor for a later analytic formalization because it requires uniform estimates on the `q`-Pochhammer derivative as `L -> 0`.
