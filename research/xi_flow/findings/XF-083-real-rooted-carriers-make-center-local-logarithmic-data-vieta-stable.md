# XF-083 — real-rooted carriers make center-local logarithmic data Vieta-stable

**Status:** `EXACT-DERIVED` + `POSITIVE/INTERFACE` + `REAL-DIVISOR-HARDY-STABILITY` + `ONE-CENTER-VIETA-RECOVERY`. XF-081 and XF-082 show that center-local function accuracy, even propagated by the exact periodic backward heat equation, does not identify the low Vieta state: exponentially invisible Chebyshev corrections can change or erase a growing Vieta prefix. The accepted one-center remote-mass clue gives a complementary obstruction: exact agreement of nearby real roots does not determine the XF-079 guarded selector because remote roots can retain order-one weighted mass.

There is nevertheless a sharp positive escape once the interface uses the **logarithmic derivative** and restricts the candidate periodic divisor to be real. For two degree-`N` periodic carriers whose roots are all real modulo the period, exponentially accurate agreement of their logarithmic derivatives on only the center half-period of one high line forces exponentially accurate agreement of every source-visible power sum, and hence of the XF-079 weighted selector and the corresponding low Vieta coordinates. No full-period observation, root matching, gap lower bound, or simplicity assumption is required.

Write the centered periodic carrier in the XF-067 variable

\[
G(\theta)
=C e^{-iN\theta/2}
\prod_{j=1}^{N}(e^{i\theta}-\nu_j),
\qquad |\nu_j|=1,
\tag{1}
\]

where real roots are equivalent to `|nu_j|=1`. For `y>0`, put

\[
r=e^{-y},
\qquad
P_m(G):=\sum_{j=1}^{N}\nu_j^{-m},
\tag{2}
\]

so `P_m` has exactly the sign convention of the XF-079 selector. If `G_1,G_2` are two such carriers of the same degree and

\[
\varepsilon
:=
\sup_{|x|\le\pi/2}
\left|
\partial_\theta\log G_1(x+iy)
-
\partial_\theta\log G_2(x+iy)
\right|,
\tag{3}
\]

then, whenever

\[
0<\varepsilon\le
\mathcal M:=\frac{2Nr}{1-r},
\tag{4}
\]

one has for every integer `m>=1`

\[
\boxed{
|P_m(G_1)-P_m(G_2)|
\le
\left(\frac{2}{r}\right)^m
\varepsilon^{1/6}\mathcal M^{5/6}.
}
\tag{5}
\]

The exponent `1/6` is an explicit nonoptimal constant coming from a half-circle harmonic-measure lower bound at radius `1/2`; the important point is that it is **independent of `N`, `m`, and the root geometry**.

At the Xi scaling

\[
N=2D,
\qquad
D=M=q^2=\Theta((\log T)^4),
\qquad
y=\Theta(D^{-1/2}),
\tag{6}
\]

the global factor in (5) is only polynomial:

\[
\mathcal M=O(D^{3/2}).
\tag{7}
\]

Therefore, if the local logarithmic-derivative mismatch is `epsilon<=e^{-cD}`, then for every `K=o(D)`

\[
\boxed{
\max_{1\le m\le K}
|P_m(G_1)-P_m(G_2)|
\le e^{-c'D}
}
\tag{8}
\]

for some `c'>0`. In particular the full XF-070--XF-071 source-visible range

\[
K=O(q\log\log T)
=O(D^{1/2}\log\log T)
=o(D)
\tag{9}
\]

is exponentially stable. Substituting (8) into the exact sideband identity of XF-079 shows that the difference of the two one-center selectors is exponentially small in the entire guarded `X(B)` resource. If in addition `K log D=o(D)`, Newton's identities and the unit-circle bounds `|P_m|<=N`, `|E_j|<=\binom Nj` imply exponentially small differences of both low Vieta edges as well.

This identifies what the Chebyshev nullspace of XF-081--XF-082 was missing: those repaired carriers are allowed to leave the unit-circle divisor class. Inside the real-divisor class, the logarithmic derivative is a bounded one-sided Hardy function on every inner circle, and a center arc already controls its low Taylor coefficients with only `exp(O(m))` loss. Since the guarded mode count is `o(D)` while the Gaussian/Appell source accuracy is `exp(-Theta(D))` or better, that continuation loss is asymptotically harmless.

The result does **not** yet construct a real-rooted periodic carrier matching the Xi Gaussian quotient, and it does not apply through a genuinely complex-root interval. It instead converts the current dictionary problem from a nonidentifiability problem into an **existence/root-faithfulness problem** on real-rooted slices: if two admissible real-divisor candidates fit the same center-local Xi logarithmic data at the available exponential accuracy, they necessarily induce the same guarded Vieta state up to an exponentially small error.

## 1. The logarithmic derivative is a one-sided power-sum generating function

From (1), with `w=e^{i theta}`, differentiate logarithmically:

\[
\partial_\theta\log G
=-\frac{iN}{2}
+i w\sum_{j=1}^{N}\frac1{w-\nu_j}.
\tag{10}
\]

For `|w|<1=|nu_j|`, expand each resolvent absolutely:

\[
\frac{w}{w-\nu_j}
=-\sum_{m\ge1}w^m\nu_j^{-m}.
\tag{11}
\]

Hence the centered logarithmic derivative

\[
U_G(w)
:=
\partial_\theta\log G+\frac{iN}{2}
\tag{12}
\]

has the exact Hardy expansion

\[
\boxed{
U_G(w)
=-i\sum_{m\ge1}P_m(G)w^m,
\qquad |w|<1.
}
\tag{13}
\]

This is the finite periodic analogue of the one-sided horizontal logarithmic-derivative field in XF-051, but here the coefficients are exactly the finite XF-079 selector power sums.

Reality of the divisor supplies a geometry-independent global bound. On `|w|=r<1`,

\[
\left|\frac{w}{w-\nu_j}\right|
\le\frac{r}{1-r},
\tag{14}
\]

so

\[
\|U_G\|_{L^\infty(|w|=r)}
\le\frac{Nr}{1-r}.
\tag{15}
\]

For the difference

\[
F(w):=U_{G_1}(w)-U_{G_2}(w),
\tag{16}
\]

we therefore have

\[
\boxed{
\|F\|_{L^\infty(|w|=r)}
\le\mathcal M=\frac{2Nr}{1-r}.
}
\tag{17}
\]

No gap envelope is used. Multiple roots on the unit circle do not change either (13) or (17).

## 2. A center half-arc controls the whole inner half-disk

Scale the disk by defining

\[
H(\zeta):=F(r\zeta),
\qquad |\zeta|<1.
\tag{18}
\]

On the boundary circle, (17) gives `|H|<=mathcal M` everywhere, while (3) gives `|H|<=epsilon` on the half-circle

\[
\Gamma:=\{e^{ix}: |x|\le\pi/2\}.
\tag{19}
\]

Apply the elementary two-constants argument to the subharmonic function `log|H|`. For `|zeta|<=1/2`, the Poisson kernel obeys

\[
P_\zeta(e^{it})
\ge
\frac{1-|\zeta|}{1+|\zeta|}
\ge\frac13.
\tag{20}
\]

Since `Gamma` has half the boundary measure, its harmonic measure at every such point is at least

\[
\omega(\zeta,\Gamma,\mathbb D)
\ge\frac16.
\tag{21}
\]

Therefore, for `epsilon<=mathcal M`, the maximum principle for `log|H|` gives

\[
\boxed{
\sup_{|\zeta|\le1/2}|H(\zeta)|
\le
\varepsilon^{1/6}\mathcal M^{5/6}.
}
\tag{22}
\]

This is deliberately a crude explicit version of the classical harmonic-measure/two-constants principle. Sharper harmonic measure would improve `1/6`, but no sharper constant is needed at the Xi scales.

Now write

\[
F(w)
=-i\sum_{m\ge1}
\bigl(P_m(G_1)-P_m(G_2)\bigr)w^m.
\tag{23}
\]

Cauchy's coefficient bound on `|w|=r/2`, together with (22), yields exactly

\[
|P_m(G_1)-P_m(G_2)|
\le
(r/2)^{-m}
\varepsilon^{1/6}\mathcal M^{5/6},
\tag{24}
\]

which is (5).

Thus the continuation cost from a center half-arc to the low Taylor coefficients is only the explicit factor `(2/r)^m`; it depends on the requested coefficient index, not on the full carrier degree.

## 3. The Xi source-visible band lies far below the continuation barrier

On the XF-073 moving high line,

\[
\theta=\frac{2\pi z}{L},
\qquad
\operatorname{Im}z=h(t)A\log T,
\qquad
L=(\log T)^3,
\tag{25}
\]

so for every fixed heat interval

\[
y=\operatorname{Im}\theta
=\Theta((\log T)^{-2})
=\Theta(D^{-1/2}).
\tag{26}
\]

Consequently

\[
1-r
=1-e^{-y}
\asymp y
\asymp D^{-1/2},
\tag{27}
\]

and (7) follows from `N=2D`.

Suppose now that

\[
\varepsilon_D\le e^{-cD}.
\tag{28}
\]

For `m<=K`, taking logarithms in (5) gives

\[
\log|\Delta P_m|
\le
-\frac c6D
+m(\log2+y)
+O(\log D).
\tag{29}
\]

Thus every `K=o(D)` leaves a fixed exponential margin, proving (8). The actual guarded source range (9) is much smaller than this threshold.

This scale comparison is favorable by a large margin. XF-073's relative source error is in fact

\[
\exp(-\Theta((\log T)^{9/2})),
\tag{30}
\]

while XF-078's finite center approximation has error

\[
\exp(-\Theta(D))
=
\exp(-\Theta((\log T)^4)).
\tag{31}
\]

Either scale is strong enough for (29). The harmonic-continuation loss through the entire guarded band is only

\[
\exp(O(q\log\log T))
=
\exp(o(D)).
\tag{32}
\]

Therefore the one-center high-line logarithmic data has ample precision to distinguish real-divisor candidates at every mode currently consumed downstream.

## 4. The XF-079 guarded selector becomes unique inside the real-divisor class

Let `B` be a union of the source-visible disjoint sidebands from XF-079, contained in indices `1<=k<=K`. Its exact one-center norm is

\[
\|\mathcal S_{r_0}\|_{X(B)}^2
=
\frac1{4D^2}
\sum_{k=1}^{K}|P_k|^2
\int_{U_{k,B}}
(\pi k+u)^4|\chi(u)|^2\,du.
\tag{33}
\]

Applying (8) to the difference of two real-divisor candidates and using the fixed compact support of `chi` gives

\[
\begin{aligned}
\|\mathcal S_{r_0}^{(1)}-
\mathcal S_{r_0}^{(2)}\|_{X(B)}^2
&\le
C_\chi D^{-2}
\sum_{k\le K}k^4|\Delta P_k|^2\\
&\le
C_\chi\frac{K^5}{D^2}e^{-2c'D}
=e^{-c''D}.
\end{aligned}
\tag{34}
\]

Thus the accepted remote-mass control and the XF-081--XF-082 Chebyshev controls cannot survive **simultaneously** with exponentially accurate local logarithmic data and a real periodic divisor. They remain valid counterexamples to weaker interfaces, but not to this strengthened admissible class.

Equation (34) is exactly matched to the destination norm rather than merely showing coefficientwise uniqueness. It also needs only one center, consistently with XF-079.

## 5. Low Vieta coordinates are stable with the same exponential margin

For a real divisor, positive and negative root power sums are conjugate. Hence (8) controls the positive-frequency sums used by the XF-067 Newton map as well. Let `E_k^{(a)}` be the normalized elementary symmetric coordinates of the two carriers. Newton's identity gives

\[
kE_k
=\sum_{m=1}^{k}(-1)^{m-1}E_{k-m}P_m.
\tag{35}
\]

Unit-circle roots imply the crude uniform bounds

\[
|P_m|\le N,
\qquad
|E_j|\le\binom Nj\le N^j.
\tag{36}
\]

If

\[
\delta_K:=
\max_{1\le m\le K}|\Delta P_m|,
\tag{37}
\]

then subtracting (35) for the two carriers and inducting on `k` yields the simple bound

\[
\boxed{
|\Delta E_k|
\le
\delta_K(2N)^k,
\qquad 1\le k\le K.
}
\tag{38}
\]

Indeed, after multiplying the inductive bounds by `|P_m|<=N`, the sum of the earlier `Delta E` terms is dominated by the last geometric scale, while the inhomogeneous terms use `|E_{k-m}|<=N^{k-m}`.

Combining (8) and (38), if

\[
K\log D=o(D),
\tag{39}
\]

then

\[
\boxed{
\max_{1\le k\le K}
|E_k^{(1)}-E_k^{(2)}|
\le e^{-c'''D}.
}
\tag{40}
\]

The actual source-visible `K=O(q log log T)` satisfies (39). Self-inversive symmetry transfers the same conclusion to the opposite Vieta edge. Hence real-divisor logarithmic data stabilizes both the power-sum selector resource and the Vieta coordinates consumed by the periodic heat transport.

## 6. Stress tests: why the previous counterexamples do not contradict the theorem

The first stress test is XF-081--XF-082. Their Chebyshev repair makes a center-locally invisible change while forcing `P_1,...,P_K` to vanish. If both the original and repaired carriers had unit-circle divisors and exponentially close logarithmic derivatives on the center high-line arc, (5) would force their `P_1` difference to be exponentially small. XF-080/XF-082 instead give a `Theta(D)` difference. Therefore at least one of the required unit-circle/logarithmic-data hypotheses must fail; the construction already leaves real-rootedness uncontrolled, exactly as its evidence boundary states.

The second stress test is the accepted remote-wave clue. There the two configurations are genuinely real and have a selected discrepancy

\[
|\Delta P_k|\asymp k,
\qquad
k=D^{1/3}.
\tag{41}
\]

Rearranging (5) shows that their center high-line logarithmic derivatives must satisfy

\[
\varepsilon
\ge
|\Delta P_k|^6
\left(\frac r2\right)^{6k}
\mathcal M^{-5}
=
\exp(-O(D^{1/3})),
\tag{42}
\]

up to polynomial factors at `y=Theta(D^{-1/2})`. Thus exact local root agreement does not make the analytic high-line signature exponentially invisible. The remote packet is invisible to a local **root list**, but not to sufficiently accurate local logarithmic data. This is precisely why the Gaussian/Appell analytic comparison remains potentially stronger than root matching.

Third, no contradiction with analytic continuation is hidden in the estimate. Equation (5) is a quantitative stability theorem with an exponentially bad-in-`m` continuation factor; it does not claim uniformly well-conditioned recovery of modes comparable to the full degree `D`. If `m=Theta(D)`, the factor `2^m` competes directly with the `e^{-cD}` source margin and the theorem may become useless. The current Xi guarded band stays parametrically below that barrier.

## 7. Prior-art and novelty boundary

The ingredients are classical. The identity (13) is the ordinary logarithmic-derivative generating function for power sums of unit-circle roots. The passage from a boundary arc bound to the inner disk is the classical harmonic-measure/two-constants principle, and Cauchy's estimate then recovers Taylor coefficients. Contemporary approximation theory studies logarithmic derivatives of polynomials whose zeros lie on the unit circle; in particular M. A. Komarov, *A Newman type bound for L_p[-1,1]-means of the logarithmic derivative of polynomials having all zeros on the unit circle*, Constructive Approximation 58 (2023), 551--563, DOI `10.1007/s00365-023-09622-8`, and *Estimates for Approximation of Functions from Hardy Spaces H^p(D) by Logarithmic Derivatives of Polynomials, Whose Zeros Lie on the Unit Circle*, Lobachevskii Journal of Mathematics 47:2 (2026), 575--585, DOI `10.1134/S1995080225615024`, provide neighboring norm/approximation context. A targeted search found no source stating the Xi-scale half-arc-to-guarded-Vieta recovery (5)--(40).

No external theorem is load-bearing: (20)--(22) are proved directly from the Poisson kernel and the maximum principle, while (13), (24), and the Newton step are elementary. The line-specific delta is the scale match

\[
\boxed{
\text{real periodic divisor}
+
\text{one-center high-line log-derivative accuracy }e^{-cD}
\Longrightarrow
\text{guarded Vieta/selector accuracy }e^{-c'D}
}
\tag{43}
\]

for all `k` in the actual Xi source-visible band.

## 8. Consequence for the current `xi_flow` frontier

XF-081 and XF-082 showed that neither static local function accuracy nor exact free-heat compatibility can choose a Vieta state. XF-083 shows that this nonidentifiability is **not intrinsic to center-local observation**. It disappears if the candidate class retains a real global divisor and the interface compares logarithmic derivatives rather than only absolute function values.

This leaves a substantially sharper positive gate. On a real-rooted slice, it is enough to construct one degree-`N` periodic, real-divisor carrier whose center high-line logarithmic derivative matches the actual Xi/Gaussian-Appell logarithmic data at `e^{-cD}` accuracy; uniqueness of the entire guarded source state then follows automatically from (5)--(40). The accepted remote-mass clue is automatically passed by such a carrier because (34) controls the same `X(B)` norm.

The unresolved existence problem is still serious. Gaussian periodization itself creates auxiliary complex seam zeros, XF-076 rules out a nonconstant globally exact finite-band Gaussian quotient, and XF-082 does not provide real roots for its repaired carrier. Moreover, below a hypothetical positive transition time the Xi divisor may genuinely be complex, so the unit-circle Hardy bound (17) is not available there. The finding therefore supplies no upper bound on `Lambda` and no RH implication by itself.

What changes is the object/dictionary target: **do not try to canonically normalize an arbitrary center-local Fourier surrogate. Seek a root-faithful real-divisor logarithmic-derivative approximant on the real-rooted side of the transition.** If such an approximant exists at the already available Gaussian accuracy, the Vieta conditioning and remote-selector ambiguity are no longer independent obstacles; the remaining hard question is existence and how to connect that real-rooted-side state across the transition geometry.
