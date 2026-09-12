# PF-301 — arbitrary bounded pant killing is an exact intrinsic attenuation density

**Status:** `EXACT-DERIVED + OSCILLATION-ROBUST-QUADRATURE + RETURN-ACCUMULATION-REDUCTION + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-300-prime-seam-weights-realize-logarithmic-quadrature|PF-300]] converts losses of the special form

\[
s_n\phi(F(p_n))
\]

into an ordinary integral when `\phi` is nonnegative and monotone. Its explicit remaining boundary is that an actual pant coefficient may oscillate with the prime geometry and need not be a monotone function of `F(p_n)`. For the scalar PF-298 pant transmission, that monotonicity restriction is unnecessary.

Put

\[
t_n:=F(p_n),\qquad h_n:=t_n-t_{n-1},\qquad
s_n:=\frac{h_n+h_{n+1}}2,
\qquad
F(x)=\log\cot\frac{\pi}{x}.
\]

For one direction through the `n`th pant, write

\[
r_n:=\frac{\kappa_n}{c_n},
\qquad
\theta_n:=\frac{c_n}{c_n+\kappa_n}=\frac1{1+r_n}.
\]

PF-298 proves `0\le r_n\le C s_n`. Hence

\[
b_n:=\frac{r_n}{s_n}
\]

is an arbitrary **bounded nonnegative coefficient sequence**; no smoothness, monotonicity, or independence from the prime gaps is available or needed.

Let `\psi_n` be the triangular hat on the exact intrinsic mesh, equal to one at `t_n`, zero at `t_{n-1},t_{n+1}`, and affine on the two adjacent mesh intervals. Then

\[
\boxed{\int \psi_n(t)\,dt=s_n.}
\]

Therefore the locally finite piecewise-linear field

\[
\boxed{
B_N(t):=\sum_{n\ge N} b_n\psi_n(t)
}
\]

satisfies the exact identity

\[
\boxed{
\int_{t_{N-1}}^\infty B_N(t)\,dt
=\sum_{n\ge N}s_nb_n
=\sum_{n\ge N}r_n.
}
\]

This is not an asymptotic Riemann-sum comparison: it is an exact finite-element identity for **every** nonnegative coefficient sequence. Consequently

\[
\boxed{
\prod_{n\ge N}\theta_n>0
\iff
B_N\in L^1(t_{N-1},\infty),
}
\]

while divergence of the intrinsic attenuation mass forces the scalar transmission product to vanish.

The PF-298 bound and PF-299's `\sum s_n^2<\infty` give more. Since `r_n=O(s_n)`, one has `\sum r_n^2<\infty`, and therefore

\[
\boxed{
\prod_{n=N}^M\theta_n
=C_N\exp\!\left(-\int_{t_{N-1}}^{t_M}B_N(t)\,dt\right)(1+o(1))
}
\]

for one finite constant `C_N>0`. Thus the complete directional scalar attenuation, including arbitrary prime-correlated oscillation of the relative killing, is represented up to one finite multiplicative renormalization by the ordinary integral of a bounded piecewise-linear density in the exact coordinate `t=F(p)`.

This removes PF-300's monotonicity caveat at the accumulation stage. It does **not** calculate the density `b_n`, prove that its integral is finite or infinite, or identify the scalar compression with the complete physical `P/H` return problem. The live local question is now sharper: determine the intrinsic-mass behavior of the actual bounded density `b_n=\kappa_n/(c_ns_n)` (or enough block/integral control on it), then return to the full `P/H` reassembly.

## Claim

Let `t_n,h_n,s_n` be as above and assume only

\[
h_n>0,\qquad h_n\to0,
\qquad
s_n=\frac{h_n+h_{n+1}}2.
\tag{1}
\]

For each `n`, define the standard hat function

\[
\psi_n(t)=
\begin{cases}
\dfrac{t-t_{n-1}}{h_n},&t_{n-1}\le t\le t_n,\\[1.2ex]
\dfrac{t_{n+1}-t}{h_{n+1}},&t_n\le t\le t_{n+1},\\[1.2ex]
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]

Then:

1. For every `n`,
   \[
   \boxed{\int\psi_n=s_n.}
   \tag{3}
   \]
2. For every nonnegative sequence `(b_n)_{n\ge N}`, the locally finite function
   \[
   B_N(t):=\sum_{n\ge N}b_n\psi_n(t)
   \tag{4}
   \]
   obeys, with both sides allowed to be `+\infty`,
   \[
   \boxed{
   \int_{t_{N-1}}^\infty B_N(t)\,dt
   =\sum_{n\ge N}s_nb_n.
   }
   \tag{5}
   \]
3. For finite `M\ge N`,
   \[
   \boxed{
   \sum_{n=N}^M s_nb_n
   =\int_{t_{N-1}}^{t_M}B_N(t)\,dt
   +\frac{h_{M+1}}2b_M.
   }
   \tag{6}
   \]
   In particular, if `b_n` is bounded, the endpoint correction in (6) tends to zero.
4. Suppose `r_n=s_nb_n\ge0`, `\theta_n=(1+r_n)^{-1}`, and `b_n` is bounded. If additionally `\sum s_n^2<\infty`, then
   \[
   \boxed{
   \prod_{n\ge N}\theta_n>0
   \iff
   \int_{t_{N-1}}^\infty B_N(t)\,dt<\infty.
   }
   \tag{7}
   \]
   Moreover there is a finite `C_N>0` such that
   \[
   \boxed{
   \prod_{n=N}^M\theta_n
   =C_N
   \exp\!\left(-\int_{t_{N-1}}^{t_M}B_N(t)\,dt\right)
   (1+o(1)).
   }
   \tag{8}
   \]
5. If instead one uses the exact loss
   \[
   \varepsilon_n:=1-\theta_n=\frac{r_n}{1+r_n}
   \tag{9}
   \]
   and its density `a_n:=\varepsilon_n/s_n`, then
   \[
   \boxed{
   \sum_n s_n|b_n-a_n|
   =\sum_n\frac{r_n^2}{1+r_n}<\infty.
   }
   \tag{10}
   \]
   Hence the raw relative-killing density `b_n=r_n/s_n` and the exact-loss density `a_n=\varepsilon_n/s_n` have the same finite/infinite intrinsic attenuation mass.

For PF-298, statements (7)--(10) apply separately to the left-to-right choice `\kappa_n=\kappa_{n,R}` and the right-to-left choice `\kappa_n=\kappa_{n,L}`.

## 1. The seam weight is exactly the area of one intrinsic hat

Equation (3) is immediate from two triangle areas:

\[
\int_{t_{n-1}}^{t_n}\psi_n(t)\,dt=\frac{h_n}{2},
\qquad
\int_{t_n}^{t_{n+1}}\psi_n(t)\,dt=\frac{h_{n+1}}2.
\tag{11}
\]

Thus

\[
\int\psi_n
=\frac{h_n+h_{n+1}}2
=s_n.
\tag{12}
\]

Because the hats have locally finite overlap and every term is nonnegative, Tonelli's theorem gives

\[
\int B_N
=\sum_{n\ge N}b_n\int\psi_n
=\sum_{n\ge N}s_nb_n,
\tag{13}
\]

which proves (5) even when the common value is infinite.

On every interior cell `[t_n,t_{n+1}]`, equation (4) is simply the affine interpolation

\[
B_N(t)
=b_n\frac{t_{n+1}-t}{h_{n+1}}
+b_{n+1}\frac{t-t_n}{h_{n+1}}.
\tag{14}
\]

So the construction does not smooth away or statistically average oscillation in `(b_n)`: it retains the exact adjacent values on the exact prime mesh.

For the finite-interval identity, all hats with `N\le n\le M-1` contribute their complete areas before `t_M`, while `\psi_M` contributes only its left triangle. Hence

\[
\int_{t_{N-1}}^{t_M}B_N
=\sum_{n=N}^{M-1}s_nb_n+\frac{h_M}{2}b_M.
\tag{15}
\]

Subtracting this from the finite sum and using `s_M=(h_M+h_{M+1})/2` proves (6).

PF-300 needed monotonicity because it compared sampled values `\phi(t_n)` to the integral of a **pre-existing function** `\phi`. Here the coefficient sequence itself defines the canonical piecewise-linear field. The symmetric seam weight is exactly the mass-lumped area of its hat basis, so no regularity assumption remains.

## 2. Infinite transmission is exactly an `L^1` question in the intrinsic coordinate

Let

\[
r_n=s_nb_n,\qquad \theta_n=(1+r_n)^{-1}.
\tag{16}
\]

Then

\[
\prod_{n=N}^M\theta_n
=\exp\!\left(-\sum_{n=N}^M\log(1+r_n)\right).
\tag{17}
\]

If `b_n` is bounded and `s_n\to0`, then `r_n\to0`. For nonnegative `r_n\to0`, the elementary comparison

\[
\frac12r_n\le\log(1+r_n)\le r_n
\tag{18}
\]

holds after a finite head. Thus the infinite product has a positive limit exactly when `\sum r_n<\infty`. Equation (5) converts that criterion exactly into (7).

No distribution statement about the primes enters this equivalence. An arbitrarily oscillatory `b_n` may correlate with large or small prime gaps in any way; the exact seam weights already carry the irregular mesh.

## 3. PF-299 upgrades the criterion to a sharp attenuation asymptotic

PF-299 proves

\[
\sum_ns_n^2<\infty.
\tag{19}
\]

PF-298 gives `b_n\le C`, so

\[
\sum_nr_n^2
=\sum_ns_n^2b_n^2
<\infty.
\tag{20}
\]

The Taylor remainder is therefore globally summable:

\[
D_N
:=\sum_{n\ge N}\bigl(r_n-\log(1+r_n)\bigr)
<\infty,
\tag{21}
\]

because `0\le r-\log(1+r)\le Cr^2` on a sufficiently small tail. Combining (17), (21), and (6) gives

\[
\begin{aligned}
\log\prod_{n=N}^M\theta_n
&=-\sum_{n=N}^Mr_n
 +\sum_{n=N}^M\bigl(r_n-\log(1+r_n)\bigr)\\
&=-\int_{t_{N-1}}^{t_M}B_N(t)\,dt
 -\frac{h_{M+1}}2b_M
 +D_N+o(1).
\end{aligned}
\tag{22}
\]

Boundedness of `b_M` and `h_{M+1}\to0` remove the endpoint term. Exponentiating proves (8) with

\[
C_N=e^{D_N}>0.
\tag{23}
\]

Thus even when the attenuation density never approaches a pointwise limit, the scalar product has a canonical continuous exponent in the intrinsic coordinate.

## 4. Raw relative killing and exact loss differ only by finite intrinsic mass

For the actual PF-298 transfer,

\[
\varepsilon_n
=1-\frac1{1+r_n}
=\frac{r_n}{1+r_n}.
\tag{24}
\]

With `a_n=\varepsilon_n/s_n` and `b_n=r_n/s_n`,

\[
s_n(b_n-a_n)
=r_n-\frac{r_n}{1+r_n}
=\frac{r_n^2}{1+r_n}.
\tag{25}
\]

Equation (20) proves (10). Therefore a local geometric calculation may work with the simpler ratio

\[
\boxed{
\frac{\kappa_n}{c_n}=s_nb_n
}
\tag{26}
\]

without separately tracking the denominator in `\varepsilon_n=\kappa_n/(c_n+\kappa_n)`: at the global accumulation level the two densities differ by an `L^1` correction and have the same survival/extinction classification.

This is useful precisely at PF-299/PF-300's critical endpoint, where an `o(s_n)` statement is not enough. The missing information is the **total intrinsic mass** of the bounded coefficient field `b_n`, not whether it admits a monotone pointwise envelope of a particular power-law form.

## 5. Consequence for the current source/escape frontier

PF-298 leaves the directional ratios

\[
\frac{\kappa_{n,R}}{c_n},
\qquad
\frac{\kappa_{n,L}}{c_n}
\tag{27}
\]

at `O(s_n)`. PF-300 showed how to settle their products if the normalized coefficient is a monotone function of `F(p_n)`. Equations (5)--(10) show that this extra shape hypothesis is unnecessary.

For either direction define

\[
\boxed{
b_{n,\pm}:=\frac{\kappa_{n,\pm}}{c_ns_n}.}
\tag{28}
\]

PF-298 already gives a uniform upper bound on these nonnegative densities. A future pant calculation may therefore target any information strong enough to decide

\[
\boxed{
\int B_{\pm}(t)\,dt<\infty
\quad\text{or}\quad
\int B_{\pm}(t)\,dt=\infty,
}
\tag{29}
\]

including block averages, sparse-support estimates, lower-density statements, or an explicit oscillatory asymptotic. It no longer needs to force `b_{n,\pm}` into a monotone model solely so PF-300's integral test can be used.

This does not remove the harder gate emphasized by MI-008 and `CLUE-source-weighted-return-potential-controls-mixed-response`: the constant compression is not known to be an invariant reduction of the complete physical `P/H` return/reassembly. The result only makes the scalar source/escape subproblem exact and oscillation-robust.

## 6. Prior art and novelty audit

No novelty is claimed for triangular finite-element hat functions, piecewise-linear interpolation, the trapezoidal-rule identity behind (3), Tonelli's theorem, or the classical reduction of a positive infinite product to convergence of the logarithmic series. A structure-directed external check likewise places the product criterion in standard elementary infinite-product theory; no new general analysis theorem is claimed.

PF-300 already identified the symmetric seam weight as the average of adjacent Riemann weights. The new Mathia-specific point is narrower: **that same weight is exactly the area of the intrinsic hat basis**, so PF-298's actual bounded but potentially prime-correlated relative-killing coefficients admit an exact continuous attenuation field with no monotonicity assumption. Together with PF-299's square summability, this also gives the multiplicative asymptotic (8). No new external dependency is needed, so `SOURCES.md` is unchanged.

## 7. Boundaries and falsification

1. **Scalar constant compression only.** The products above are directional PF-298 constant-mode products. They are not the complete `P/H` mixed return operator.
2. **Reduction, not a value for the density.** The theorem does not prove whether `B_{\pm}` has finite or infinite integral. That still requires new geometry/operator control of `\kappa_{n,\pm}/c_n`.
3. **Boundedness is load-bearing only for the sharp product asymptotic.** The exact identity (5) holds for every nonnegative sequence, bounded or not. PF-298's `O(s_n)` bound and PF-299's `\ell^2` theorem are what make the logarithmic correction in (21) summable.
4. **No averaging of prime gaps.** `B_N` interpolates the actual coefficients on the actual `t_n=F(p_n)` mesh. Oscillation correlated with the prime gaps is retained rather than replaced by an average gap law.
5. **Directionality remains.** `\kappa_{n,L}` and `\kappa_{n,R}` may have different density fields. No symmetry between them is asserted.
6. **Finite heads do not matter.** All product and integrability conclusions are tail statements.
7. **No weak-trace or RH conclusion.** The finding sharpens one scalar accumulation gate only; it proves no compactness, weak ideal estimate, zeta-zero correspondence, critical-line statement, or RH consequence.

A refutation would have to break the exact seam identity `s_n=(h_n+h_{n+1})/2`, the hat-area computation (11)--(12), PF-298's bounded relative-killing ratio, PF-299's `\ell^2` seam result, or the elementary positive-product expansion. The unresolved mathematics is now isolated in the actual intrinsic attenuation density and, beyond the scalar compression, the complete `P/H` return/reassembly.

## Consequence for the research line

PF-299 identifies the linear seam endpoint; PF-300 calibrates monotone logarithmic suppressions. PF-301 removes the remaining monotonicity assumption at the accumulation stage. **Any bounded nonnegative relative-killing field, however irregularly correlated with the prime gaps, has an exact piecewise-linear attenuation density in `t=F(p)`.** The scalar survival question is precisely whether that density has finite total intrinsic mass.

The next useful local pant result should therefore estimate the actual fields `b_{n,L},b_{n,R}` in an integrated or block-averaged sense. Pointwise monotone asymptotics remain sufficient but are no longer necessary. After that scalar question is settled, the line must still return to the harder complete `P/H` source/escape and extension-mass gate.