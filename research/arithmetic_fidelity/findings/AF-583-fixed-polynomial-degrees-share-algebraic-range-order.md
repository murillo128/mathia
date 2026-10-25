# AF-583 — Every fixed polynomial degree beyond affine shares the algebraic range order

## Status

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · RANGE-ORDER-CLASSIFICATION · QUANTITATIVE-PRIME-TRANSFER · NO-GENERAL-NOVELTY-CLAIM

## Claim and observation experiment

For the binary sources `0` and
\[
 f(x)=xe^{1-x},\qquad 0<x\le B,
\]
observe one source plus one shared, unrestricted-coefficient polynomial of known degree at most `r`, and an arbitrary error bounded by `epsilon` in absolute value. Competing source labels may use different polynomials. Set
\[
 E_r(B)=\inf_{p\in\Pi_r}\|f-p\|_{C[0,B]},\quad
 \varepsilon_r(B)=E_r(B)/2,\quad
 \Delta_r(B)=1-2E_r(B).
 \tag{1}
\]
The continuous extension at zero preserves the observation norm. The whole-window unique-identification radius is the supremum `epsilon_r(B)`: two translated error balls first meet at twice their radius. The full-ray radius is `1/4`, since only constant polynomials remain bounded against `f`, whose range has closure `[0,1]`. Thus `Delta_r` is the fraction of the full-ray margin lost by limiting the observation range.

[[research/arithmetic_fidelity/findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic|AF-582]] gives a sharp quadratic law but leaves higher degrees open. The rate question has a uniform answer without solving their alternation systems.

**Theorem.** Put
\[
 A_r=\frac{2r^2(r^2-1)}3.
\]
For every integer `r>=2`, every `B>1`, and every `1<t<=B`,
\[
 \boxed{\Delta_2(B)\le\Delta_r(B)
 \le e^{1-t}+\frac{A_r(t-1)}{B^2}.}
 \tag{2}
\]
In particular, taking `t=2 log B` for `B>=e` gives
\[
 \Delta_r(B)\le
 \frac{e+A_r(2\log B-1)}{B^2}.
 \tag{3}
\]
Together with AF-582,
\[
 \Delta_2(B)=\frac{1+2\log B}{B^2}
       +O\!\left(\frac{(\log B)^2}{B^3}\right),
 \tag{4}
\]
this proves, for **every fixed** `r>=2`,
\[
 \boxed{\Delta_r(B)=\Theta_r(\log B/B^2).}
 \tag{5}
\]
If
\[
 R_r(\delta)=\inf\{B>1:\Delta_r(B)\le\delta\},
\]
then
\[
 1\le\liminf_{\delta\downarrow0}
 \frac{R_r(\delta)}{\sqrt{\log(1/\delta)/\delta}}
 \le\limsup_{\delta\downarrow0}
 \frac{R_r(\delta)}{\sqrt{\log(1/\delta)/\delta}}
 \le\sqrt{A_r}.
 \tag{6}
\]
The constants in (2)--(3) are explicit bounds, **not sharp higher-degree asymptotic coefficients**. For `r=2`, AF-582 already supplies limit one in (6). The first transition from affine to quadratic changes the range order; no further fixed degree changes that order. Additional alternation contacts can still change its leading constant.

A concrete arithmetic transfer below proves a uniform normalized-profile error `O(1/log p)` for the registered prime-edit controls. Consequently (5)--(6), up to the stated degree-dependent bounds, hold for their simultaneous remote-prime/near-full-margin limit whenever `delta log p -> infinity`. This replaces an unquantified diagonal choice by a sufficient explicit scale relation.

## Why bounded curvature controls the entire fixed-degree hierarchy

Let `p` be a best approximant and `E=E_r(B)`. The constant `1/2` is admissible, so `E<=1/2`. Since `0<=f<=1`,
\[
 -E\le p(x)\le1+E,\qquad
 \|p-1/2\|_{[0,B]}\le E+1/2\le1.
 \tag{7}
\]
The classical second-derivative Markov inequality, rescaled from `[-1,1]`, gives
\[
 \|p''\|_{[0,B]}
 \le\frac{4}{B^2}T_r''(1)\|p-1/2\|_{[0,B]}
 \le\frac{4r^2(r^2-1)}{3B^2}
 =\frac{2A_r}{B^2}.
 \tag{8}
\]
Here `T_r` is the Chebyshev polynomial. Subtracting the constant in (7) does not change the second derivative.

For a twice differentiable function whose second derivative has absolute value at most `M`, linear interpolation between `0` and `t` yields
\[
 p(1)\le (1-1/t)p(0)+p(t)/t+\tfrac12M(t-1).
 \tag{9}
\]
For example, subtract the interpolating line: its remainder at one is `p''(xi)(1-t)/2`. This fixes both the sign and the factor in (9).

Now use
\[
 p(1)\ge1-E,\quad p(0)\le E,\quad
 p(t)\le E+te^{1-t}.
\]
Equations (8)--(9) give
\[
 1-2E\le e^{1-t}+A_r(t-1)/B^2,
\]
which is the upper bound in (2). The lower bound follows from `Pi_2 subset Pi_r`, hence `E_r<=E_2`. Taking `t=2 log B` proves (3), and (4) proves (5).

For (6), `R_r>=R_2` and AF-582 give the lower bound. At
`B=C sqrt(log(1/delta)/delta)`, (3) is at most
`(A_r/C^2+o(1)) delta`; every `C>sqrt(A_r)` therefore gives the upper bound. Monotonicity of `E_r(B)` in `B` justifies passage from a witness window to the minimum range.

The proof does not posit a particular higher-degree optimal polynomial or tail-contact pattern. It controls **every** admissible polynomial through the observed peak, the zero endpoint, a decaying-tail point, and its bounded curvature over the full window. More samples or adaptivity within that window cannot exceed the whole-window radius. Classical alternation and normalized divided-difference weights give `r+2` fixed probes approaching it; a zero node is replaced by a positive node tending to zero. These probe certificates and their total-variation-one noise bound are exactly those of AF-582, applied at the higher-degree alternation nodes.

Equation (3) also supplies the sufficient growing-degree regime
`r(B)^4 log B=o(B^2)` for `Delta_(r(B))(B)->0`. It is not asserted to be necessary or sharp in degree. Unknown unrestricted degree is a different experiment: on each fixed compact interval polynomial approximation makes the positive-noise quotient margin zero.

## Quantitative transfer from the actual prime-edit source

Use the exact registered limiting curves of
[[research/arithmetic_fidelity/findings/AF-559-all-pair-prime-edit-separation-has-uniform-sharp-critical-window|AF-559]]:
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_j(s)=j^{-s}-(j+1)^{-s},\quad Q_j=P-h_j,
\]
\[
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\qquad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
\]
Here `p<q` are odd rational primes labeling generalized-prime systems with one generator replaced by its successor integer. Put
\[
 L=\log p,\quad H=p^{-2}-q^{-2},\quad c=e^{B_1},\quad
 D_{p,q}=\sup_{a>0}(\Phi_q-\Phi_p)(a),
\]
where `B_1` is the reciprocal-prime Meissel--Mertens constant. Then
\[
 \boxed{D_{p,q}=\frac{H}{eL}\{1+O(L^{-1})\},\qquad
 \sup_{q>p}\sup_{z>0}\left|
 \frac{(\Phi_q-\Phi_p)(z/(cL))}{D_{p,q}}-ze^{1-z}
 \right|=O(L^{-1}).}
 \tag{10}
\]
All constants are independent of `q>p`. No restriction on `q/p` or lower bound on the relative gap is imposed. This is a quantitative refinement of AF-559's normalized convergence, derived from its exact source comparison rather than subtraction of individual asymptotic responses.

### Relative inverse displacement down to the singular endpoint

Write `r_j(s)=Q_j^{-1}(P(s))`. AF-559 establishes, for `k=h_p-h_q`,
\[
 k(s)=s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv,
 \qquad
 r_q(s)-r_p(s)=\frac{k(r_q(s))}{-Q_p'(\xi)},
 \quad r_p(s)<\xi<r_q(s).
 \tag{11}
\]
Fix a sufficiently small `eta>0`. For `0<x<=eta`, its gap-relative integral comparison is
\[
 k(1+x)=He^{-Lx}\{1+O(x+p^{-1})\}.
 \tag{12}
\]
The crucial uniformity, even for neighboring edit positions, is
\[
 1\le\frac{p^{-2-x}-q^{-2-x}}{H e^{-Lx}}
 =\frac{1-e^{-(2+x)b}}{1-e^{-2b}}\le1+x/2,
 \qquad b=\log(q/p)>0.
 \tag{13}
\]

The prime-zeta boundary normal form is
\[
 P(1+x)=-\log x+(B_1-\gamma)+O(x),\qquad
 -P'(1+x)=x^{-1}+O(1).
 \tag{14}
\]
The remainder is analytic near zero; the derivative assertion is not obtained by differentiating an arbitrary big-O remainder. It follows, independently of RH, from the Euler-product/Möbius identity for `P`, separating `log zeta(s)` from the locally analytic sum over multiples `m>=2`.

The global inverse bound of
[[research/arithmetic_fidelity/findings/AF-555-remote-generator-perturbations-have-sharp-critical-curve-resolution|AF-555]], with generator displacement one, gives
\[
 d_j(x):=1+x-r_j(1+x)
 \le(1-\epsilon_j)^{-1}\frac{h_j(1+x)}{-P'(1+x)},
 \quad \epsilon_j=O(\log j/j^2).
\]
Since `h_j(1+x)<=C j^(-2)` on this fixed interval, (14) strengthens the absolute displacement estimate to
\[
 0<d_j(x)\le Cx/j^2.\tag{15}
\]
Thus every intermediate `xi` in (11) satisfies
`xi-1=x(1+O(p^(-2)))`, **uniformly even as x tends to zero**. Also `|h_p'(xi)|/[-P'(xi)]<=epsilon_p`. Hence
\[
 -Q_p'(\xi)=x^{-1}\{1+O(x+L/p^2)\}.
 \tag{16}
\]
Differentiating the positive integral in (11) bounds
`|(log k)'|<=log(q+1)+2` for `s>=1`. Applying (15) with `j=q`, not `j=p`, gives
\[
 k(r_q(1+x))/k(1+x)=1+O(x\log q/q^2).
\]
Together with (12) and (16), this proves the uniform local relative estimate
\[
 r_q(1+x)-r_p(1+x)
 =Hxe^{-Lx}\{1+O(x+p^{-1})\}.
 \tag{17}
\]

### The global profile rate and the coordinate change

For `u=Lx` and `0<x<=eta`, multiplying (17) by `L/H` shows that its difference from `u exp(-u)` is bounded by
\[
 C\left(\frac{u^2e^{-u}}L+\frac{ue^{-u}}p\right)=O(L^{-1}).
 \tag{18}
\]
For `x>=eta`, AF-559's positive-integral tail bound and its global inverse majorant give
\[
 0\le\frac{L}{H}(r_q(1+x)-r_p(1+x))
 \le C_\eta Lp^{-\eta}=O(L^{-1}).
 \tag{19}
\]
The constants remain uniform over all `q>p`: in the global numerator comparison AF-555 gives
`sup_s(s-r_q(s))=O((q^2 log q)^(-1))`, so the logarithmic derivative bound costs only `O(q^(-2))`. The global denominator perturbation is `O(L/p^2)`. The comparison profile `u exp(-u)` has the same negligible upper tail. Thus (18)--(19) prove a global error `O(1/L)` in the `u` coordinate, including the peak, which gives the first assertion of (10).

To retain the actual observation coordinate, define `a(x)` by
`E_1(a(x))=P(1+x)`. The boundary expansions give
\[
 ca(x)=x\{1+O(x)\}.
\]
For `v=ca(x)L`, shrink `eta` if necessary so that
`u/2<=v<=3u/2` and `|v-u|<=Cu^2/L` on the local interval. The derivative of `w exp(-w)` then gives
\[
 |ve^{-v}-ue^{-u}|
 \le C u^2(1+u)e^{-u/2}/L=O(L^{-1}).
 \tag{20}
\]
Outside that interval, monotonicity gives `v>=ca(eta)L`, so the profile is exponentially small. Dividing by the peak `1/e+O(1/L)` proves the second assertion of (10). Independent horizontal reparametrizations of the two sources are not allowed in this argument.

## Joint range and source limit

Let `epsilon_(r;p,q)(B)` be the binary whole-window radius for the two curves with one shared degree-`r` calibration per input, on
`0<a<=B/(c log p)`. Rescaling `a` and dividing the output difference by `D_(p,q)` preserve the polynomial subspace. The distance to a fixed subspace is 1-Lipschitz, so (10) yields
\[
 \left|\left(1-\frac{\varepsilon_{r;p,q}(B)}{D_{p,q}/4}\right)
                  -\Delta_r(B)\right|\le \frac C{\log p}.
 \tag{21}
\]
This holds uniformly in `q>p`, `B>0`, and the nonnegative integer degree `r`. The full-ray radius `D_(p,q)/4` is exact: the bounded positive source gap tends to zero at both ends, and all nonconstant polynomials are unbounded on the ray. TV-one alternation contrasts likewise transfer, so (21) is both an obstruction and a finite-probe achievability comparison, with the usual strict-noise/supremum boundary.

In particular, for fixed `r>=2`, `B->infinity`, and
\[
 B^2=o((\log p)\log B),\tag{22}
\]
the normalized prime-window loss is `Theta_r(log B/B^2)`, uniformly over all larger prime edit labels. Equivalently, let `delta=delta(p)->0` with
\[
 \delta\log p\longrightarrow\infty.\tag{23}
\]
The minimum **normalized** range `R_(r;p,q)(delta)` required to retain fraction `1-delta` of the actual full-ray radius obeys
\[
 R_{r;p,q}(\delta)=\Theta_r\!\left(
          \sqrt{\log(1/\delta)/\delta}\right),\tag{24}
\]
uniformly in `q>p`. To see this precisely, (21) sandwiches this range between `R_r(delta+C/L)` and `R_r(delta-C/L)` once `delta>C/L`. Equations (6) and (23) then apply. For `r=2`, the ratio to the displayed square-root expression tends to one. The physical range endpoint is this normalized range divided by `c log p`.

Conditions (22)--(23) are sufficient transport conditions; necessity is not claimed. The error `O(1/log p)` has not been proved sharp. In particular, failure of (23) is not a theorem that the prime-source quotient loses its range law. No joint growing-prime/finite-critical-index error is supplied: these are the exact limiting curves, formed first for each source.

## Prior art, validation and remaining boundary

The derivative bound is the classical Markov brothers inequality. Aleksei Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.1, equations (1.1)--(1.2), supplies its all-derivative form and Chebyshev constant. Linear-interpolation error and Chebyshev alternation are also classical; [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) records the latter. Sachdeva--Vishnoi, [*Faster Algorithms via Approximation Theory*](https://www.cs.yale.edu/homes/sachdeva/pubs/fast-algos-via-approx-theory.pdf), §§4--5, treats exponential approximation and degree/interval tradeoffs. Those general results are not discoveries here. Their usual approximation target and resource regime do not by themselves state this peaked-source fractional-margin law.

For the prime boundary, Fröberg's classical source is already anchored in `SOURCES.md`. Kawalec's [recent preprint](https://arxiv.org/html/2603.21535v1), equations (2)--(3), explicitly records the Möbius formula and analytic regular part. Only that classical local input is used; no conditional prime-counting error estimate or RH assumption from another part of the paper enters this proof. AF-555/559 supply the exact marked-source inverse identities and global majorants. The new local contribution is their endpoint-relative quantitative refinement (15)--(20), used to make the range transfer simultaneous rather than merely iterated.

A scratch-only standard-library check verified the sign and interval scaling in (8)--(9) exactly with rational arithmetic on rescaled Chebyshev polynomials of degrees 2 through 12, three windows and three interpolation lengths, with both signs (198 inequalities). Another 35 floating checks of (13) covered near-coincident through very large gap ratios. These are normalization checks, not proofs of the continuum estimates or computations of higher-degree minimax constants. The proof of (2) is the analytic interpolation/Markov argument; (4) rests on AF-582's independently reconstructed alternation certificate; the arithmetic rate rests on the positive gap integral and the uniform inverse estimates above.

The substantive delta is a complete fixed-degree **range-order** classification and a quantitative sufficient transfer regime for the existing prime-edit experiment. It does not determine higher-degree leading constants, optimal contact locations, optimal dependence on growing degree, a common multiway design, or computational bit complexity.

This law is already realized by the non-arithmetic binary profile. The arithmetic sources remain generalized-prime matched controls indexed by rational-prime edit locations; their absolute margins still vanish with the edit position. It neither certifies ordinary-prime provenance nor excludes off-critical zeros or proves RH.
