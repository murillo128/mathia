# AF-584 — Growing calibration degree has a sharp quadratic range cost

## Status

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · UNIFORM-DEGREE-RANGE-LAW · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

## Experiment and theorem

Consider the binary sources `0` and
\[
 f(x)=xe^{1-x},\qquad 0<x\le B,
\]
with one shared polynomial calibration of known degree at most `r` per input and arbitrary observation error bounded in absolute value. Competing labels may choose different polynomials. Write
\[
 E_r(B)=\inf_{p\in\Pi_r}\|f-p\|_{C[0,B]},\quad
 \varepsilon_r(B)=E_r(B)/2,\quad
 \Delta_r(B)=1-2E_r(B).
 \tag{1}
\]
The extension to zero preserves the norm. The whole-window unique-identification radius has supremum `epsilon_r(B)`, since two error balls meet when their combined radius reaches the distance between the two polynomial cosets. On the full ray only constant polynomials stay bounded against `f`, so the full-ray radius is `1/4`. Thus `Delta_r` measures the fraction of this margin lost by imposing the coordinate limit `B`.

[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]] proves the range order for each fixed degree but leaves the dependence on growing degree open. Here the constants are independent of degree.

**Theorem.** For every integer `r>=2` and `B>=16r^2`, put `mu=r^2/B`. Then
\[
 \boxed{\frac{\mu^2\log(1/\mu)}{20736}
 \le\Delta_r(B)\le 2\mu^2\log(1/\mu).}
 \tag{2}
\]
For every `B>=64` and `r^2/B>=1/16`,
\[
 \boxed{\Delta_r(B)\ge\frac{\log256}{2^{24}}>0.}
 \tag{3}
\]
The constants are deliberately nonoptimal. In particular, for arbitrary nonnegative integer degrees `r=r(B)` as `B->infinity`,
\[
 \boxed{\Delta_{r(B)}(B)\longrightarrow0
 \quad\Longleftrightarrow\quad r(B)^2/B\longrightarrow0.}
 \tag{4}
\]
If `R_r(delta)=inf{B>1: Delta_r(B)<=delta}`, then
\[
 \boxed{R_r(\delta)=\Theta\!\left(
 r^2\sqrt{\frac{\log(1/\delta)}{\delta}}\right),
 \qquad \delta\downarrow0,\quad r\ge2,}
 \tag{5}
\]
with absolute implied constants and a small-`delta` threshold independent of `r`. The degree may therefore grow arbitrarily along this limit. This gives the joint degree/range order, not a sharp leading coefficient or the limiting margin at `r^2/B` tending to a positive constant.

## The upper bound: choose the tail point at the degree-dependent scale

For completeness, the AF-583 interpolation/Markov argument gives, with
\[
 A_r=\frac{2r^2(r^2-1)}3,\qquad \kappa=A_r/B^2,
\]
the inequality
\[
 \Delta_r(B)\le e^{1-s}+\kappa(s-1),\qquad 1<s\le B.
 \tag{6}
\]
Indeed, for a best approximant `p` with error `E<=1/2`, one has `||p-1/2||<=1`. The second-derivative Markov inequality on `[0,B]` gives `||p''||<=2A_r/B^2`. Interpolating `p(1)` between `p(0)` and `p(s)` gives
\[
 p(1)\le(1-1/s)p(0)+p(s)/s+\kappa(s-1).
\]
Use `p(1)>=1-E`, `p(0)<=E`, and `p(s)<=E+se^{1-s}` to obtain (6).

If `mu<=1/16`, choose
\[
 s=1+\log(1/\kappa).
\]
Here `8/B^2<=kappa<1`, so `1<s<=B` for `B>=64`. Therefore
\[
 \Delta_r(B)\le\kappa\{1+\log(1/\kappa)\}.
 \tag{7}
\]
The function `u(1+log(1/u))` is increasing on `(0,1)`, and `kappa<=(2/3)mu^2`. Since `log(1/mu)>=log16>1+log(3/2)`, (7) is at most `2mu^2 log(1/mu)`. Optimizing the tail point removes the extraneous `log B` from AF-583's sufficient growing-degree condition, but by itself does not prove necessity.

## A polynomial witness for loss at every growing degree

The converse uses an explicit polynomial with a controlled positive part around the source peak and a bounded negative part over the entire remaining window.

**Lemma.** Let `n>=1` be an integer, let `B>=64n^2`, and set
\[
 k=n^2/B,\qquad t=\log(1/k),\qquad
 D(x)=1-T_n(1-2x/B),
\]
\[
 Q(x)=\left(\frac t x-1\right)D(x)^2,\qquad
 d=\frac{k^2\log(1/k)}{256}.
 \tag{8}
\]
At zero use the continuous extension `Q(0)=0`. Then `Q` is a polynomial of degree at most `2n`, and
\[
 0\le f(x)-Q(x)/64\le1-d\quad(0\le x\le B).
 \tag{9}
\]
Consequently the polynomial
\[
 p(x)=(1-d)/2+Q(x)/64
 \tag{10}
\]
has uniform error at most `(1-d)/2`, proving `Delta_(2n)(B)>=d`.

**Proof.** The factor `D` vanishes at zero, so `D^2/x` is a polynomial: the apparent denominator in (8) does not enlarge the allowed nuisance class.

For `0<=x<=t`, write `theta=2 arcsin sqrt(x/B)`. Since `t<=log B<=B/2` and `k<=1/64`,
\[
 2\sqrt{x/B}\le\theta\le2\sqrt{2x/B},\qquad
 n\theta\le\sqrt{8kt}<1.
\]
Here `kt<=log64/64`. The elementary inequalities `1-cos u>=u^2/4` for `0<=u<=1` and `|sin(nv)|<=n|sin v|` give
\[
 kx\le D(x)\le2kx\quad(0\le x\le t).
 \tag{11}
\]
Hence
\[
 k^2x(t-x)\le Q(x)\le4k^2x(t-x),\quad 0\le x\le t.
 \tag{12}
\]
For `t<=x<=B`, `|T_n(1-2x/B)|<=1`, and the prefactor in (8) lies in `[-1,0]`; therefore
\[
 -4\le Q(x)\le0.
 \tag{13}
\]

Set `h=f-Q/64`. For `0<x<=t`,
\[
 \frac{Q(x)}{f(x)}\le4k^2(t-x)e^{x-1}
 \le4k^2e^{t-2}=4k/e^2<64.
 \tag{14}
\]
The maximum in the middle expression occurs at `x=t-1`. Thus `h>=0` there; (13) proves `h>=0` after `t`, and `h(0)=0`.

For the upper bound, partition the interval into three regions. Since `t>=log64>4`, on `[1/2,3/2]` equation (12) gives
\[
 Q(x)\ge k^2(t-3/2)/2\ge k^2t/4,
 \qquad h(x)\le1-k^2t/256=1-d.
 \tag{15}
\]
On `[0,t]` outside this peak neighborhood, `Q>=0` and
\[
 h\le f\le\max\{f(1/2),f(3/2)\}
 =\tfrac32e^{-1/2}<15/16<1-d.
 \tag{16}
\]
The last inequality uses `d<=log64/(256\cdot64^2)<1/16`. Finally, on `[t,B]`,
\[
 h(x)\le f(t)+1/16=e kt+1/16
 \le e\log64/64+1/16<1/2<1-d.
 \tag{17}
\]
This proves (9) over the whole window, including every oscillation of `T_n`, rather than only at selected contact points.

## Uniform lower bound, threshold, and range inversion

When `r>=2` and `mu<=1/16`, take `n=floor(r/2)`. Then `2n<=r` and
\[
 \mu/9\le k=n^2/B\le\mu/4\le1/64.
\]
The lemma and monotonicity in the approximation degree give
\[
 \Delta_r(B)\ge\frac{k^2\log(1/k)}{256}
 \ge\frac{\mu^2\log(1/\mu)}{81\cdot256},
\]
which proves the other half of (2).

For `B>=64` and `mu>=1/16`, take instead `n=floor(sqrt B/8)`. This satisfies `2n<=r` and `1/256<=k<=1/64`. The function `k^2 log(1/k)` is increasing on this interval; the lemma yields (3). For any fixed `eta>0`, (2)--(3) now give a positive lower bound on `Delta_r(B)` whenever `r^2/B>=eta`. This proves the necessary implication in (4). The sufficient implication follows from (2) on the subsequences with `r>=2`. For `r=0`, `Delta_0=0` when `B>1`; for `r=1`, the affine formula in [[research/arithmetic_fidelity/findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic|AF-582]] gives `Delta_1(B)->0`.

For (5), let `L=log(1/delta)` and evaluate (2) at
\[
 B=C r^2\sqrt{L/\delta},\qquad
 \mu=C^{-1}\sqrt{\delta/L}.
\]
Then
\[
 \mu^2\log(1/\mu)
 =\frac{\delta}{C^2}\left\{\frac12+
 \frac{\log L}{2L}+\frac{\log C}{L}\right\}.
 \tag{18}
\]
This expression and the condition `B>=16r^2` are uniform in all `r>=2`. For example, `C=1/300` makes the lower bound in (2) exceed `delta`, while `C=2` makes its upper bound smaller than `delta`, for all sufficiently small `delta` independently of `r`. The error `E_r(B)` is nondecreasing in `B`, so these two windows bracket `R_r(delta)` and prove (5). These constants are certificates of order, not asymptotic optimal constants.

Whole-window failure is also failure for every adaptive sampling scheme confined to that window. Conversely, for each finite `r`, classical alternation and divided-difference weights of total variation one give `r+2` fixed samples approaching the whole-window radius, as in AF-582. A zero node is approached through positive nodes. The count may grow with `r`; no precision or bit-cost bound is implied. All radii are suprema, with unique identification asserted only at strict noise allowances.

## Concrete transfer to the registered prime-edit controls

Use the same source coordinate and exact limiting curves as AF-583:
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 Q_j(s)=P(s)-j^{-s}+(j+1)^{-s},\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),
\]
\[
 E_1(a)=\int_a^\infty e^{-u}\,du/u,
 \quad D_{p,q}=\sup_{a>0}(\Phi_q-\Phi_p)(a),\quad c=e^{B_1},
\]
where `p<q` are odd rational-prime edit locations and `B_1` is the reciprocal-prime Meissel--Mertens constant. Let
\[
 g_{p,q}(x)=\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}}.
\]
AF-583, equation (10), proves
\[
 \sup_{q>p}\|g_{p,q}-f\|_{(0,\infty)}\le C_0/\log p
 \tag{19}
\]
for sufficiently large `p`, uniformly in the larger prime label. This is a canonical local input, not a new prime asymptotic proved here.

Denote the binary radius on `0<a<=B/(c log p)` by `epsilon_(r;p,q)(B)`, and set
\[
 \Delta_{r;p,q}(B)=1-
 \frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}.
\]
The denominator is the exact full-ray radius for every finite `r`. Coordinate dilation preserves `Pi_r`; distance to a fixed subspace is 1-Lipschitz. Thus
\[
 |\Delta_{r;p,q}(B)-\Delta_r(B)|\le2C_0/\log p,
 \tag{20}
\]
uniformly in `r`, `B`, and `q>p`. There is no degree-dependent amplification of this uniform source error.

Consequently, as `p->infinity`, `B(p)->infinity`, and with any supplied finite integer degree `r(p)` and any `q(p)>p`,
\[
 \Delta_{r(p);p,q(p)}(B(p))\to0
 \quad\Longleftrightarrow\quad r(p)^2/B(p)\to0.
 \tag{21}
\]
For the more quantitative target `delta->0`, assume `delta log p->infinity`. Equation (20) sandwiches the minimum normalized prime range between the profile ranges at `delta+2C_0/log p` and `delta-2C_0/log p`. Equation (5) then gives
\[
 R_{r;p,q}(\delta)=\Theta\!\left(
 r^2\sqrt{\frac{\log(1/\delta)}{\delta}}\right),\qquad r\ge2,
 \tag{22}
\]
with constants uniform also in the growing known degree and larger prime label. The physical range is this quantity divided by `c log p`. The condition `delta log p->infinity` is sufficient for relative-error transfer; it is not asserted necessary. Unlike (22), the qualitative equivalence (21) only needs the absolute profile error to vanish.

## Prior art, checks, and evidence boundary

The Markov brothers inequality and Chebyshev trigonometric representation are classical: Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.1, and [NIST DLMF (18.5.1)](https://dlmf.nist.gov/18.5.E1), provide the precise inputs. [DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) supplies alternation. None is claimed as new.

Sachdeva--Vishnoi, [*Faster Algorithms via Approximation Theory*](https://www.cs.yale.edu/homes/sachdeva/pubs/fast-algos-via-approx-theory.pdf), §§4--5, and Aggarwal--Alman, [*Optimal-Degree Polynomial Approximations for Exponentials and Gaussian Kernel Density Estimation*](https://doi.org/10.4230/LIPIcs.CCC.2022.22), Theorem 2, establish neighboring degree/interval approximation laws for the exponential. In particular the square-root interval scale is established approximation theory, not a newly discovered general resolution principle. Here the target is the *deficit from half-range best error* for the peaked function `x exp(1-x)`, including its logarithmic small-deficit order. The explicit witness (8)--(17) and the optimized Markov bound prove that statement directly; it is not inferred from an exponential approximation theorem with a different target/error regime. No general priority claim is made for this specialization.

A scratch-only standard-library check used 70-digit decimal arithmetic on 24 `(n,B)` families with `n` in `{1,2,3,5,10,40}` and `B/n^2` in `{64,100,1000,10^6}`. Across 14,754 points, including the peak, moving tail boundary, near-boundary points and Chebyshev extremal locations, it checked (11)--(13), (9), and the approximant error. A separate exact rational recurrence checked the zero divisibility, degree, and derivative `D'(0)=2n^2/B` for 24 polynomials with degrees 1 through 12. All checks passed. Sampling is a normalization check, not a continuum proof or a computed minimax value; the global certificate is (11)--(17).

The result closes the growing-degree range-order question left by AF-583. It does not determine higher-degree leading constants, the positive-`mu` limiting curve, the high-degree small-error approximation regime, or a common optimal multiway design. Known degree, a shared calibration, the common coordinate, and absolute bounded noise are essential parts of the experiment. Unknown unrestricted degree or independently recalibrated readings are different models.

The non-arithmetic binary source already realizes the obstruction. The arithmetic instantiation consists of generalized-prime matched controls indexed by rational-prime edit locations; their absolute full-ray margins still vanish remotely. No ordinary-prime provenance discriminator, zero exclusion, or RH consequence follows.
