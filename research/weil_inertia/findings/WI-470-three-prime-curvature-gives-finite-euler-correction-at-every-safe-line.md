# WI-470 — three-prime curvature gives finite Euler correction at every safe line

**Status:** EXACT-DERIVED + CLASSICAL-SMOOTHING-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the cumulative coefficient and its normalization; [WI-467](WI-467-far-right-euler-correction-is-an-absolutely-continuous-signed-measure.md), for the preceding one-angle sufficient regime. The separate arithmetic boundary is [WI-469](WI-469-gevrey-cutoffs-admit-the-full-first-euler-sampling-correction.md).

## Claim and mathematical delta

For **every fixed** `sigma>1` and `r>0`, the full coherent Euler response's
prime-axis coefficient is an absolutely continuous finite signed measure
on its scalar response interval. Every finite prime-power exhaustion
with vanishing omitted coefficient mass, using the original normalization,
converges to this measure in total variation. Consequently its cumulative
coefficients converge uniformly at every threshold, and WI-464's `L^1`
coefficient has a unique absolutely continuous representative.

This removes WI-467's far-right condition. Its summable prime-deletion
budget already worked for all `sigma>1`, but its uniform conditional
cosine geometry did not. Three sufficiently large comparable prime
coordinates supply a different uniform curvature certificate: at every
phase point at least one mixed second derivative stays nonzero,
independently of all other prime phases. Local one-dimensional smoothing
then gives the same square-root deletion bound.

This is a theorem about the candidate **coefficient**, not a first
arithmetic sampling theorem for indicators. Neither constants uniform
as `sigma downarrow 1` or `r downarrow 0`, nor a bound for the scaled
signed residual of actual zero sampling, is asserted. No RH conclusion
or stronger simple-critical proportion follows.

## Objects and the three anchor primes

Let `m` be product probability Haar measure on the prime torus. Set

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\Lambda(n)n^{-\sigma}/A,\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r}.
 \tag{1}
\]

Use Hilbert vectors with this Gram kernel, for example
`v_n(s)=sqrt(2r) exp(-r(log n-s)) 1_[0,log n](s)` in `L^2(0,infinity)`.
Thus `||v_n||<=1`. Define

\[
 V=\sum_{p,k\ge1}a_{p^k}e^{ik\theta_p}v_{p^k},\qquad
 Q=\|V\|^2,\qquad
 w_p=\sum_{k\ge1}a_{p^k}=\frac{\log p}{A(p^\sigma-1)}.
 \tag{2}
\]

The series is uniformly absolutely convergent, `sum_p w_p=1`, and
`0<=Q<=q_*:=Q(1)<=1`. For a finite set `F` of prime powers, let `Q_F`
retain just those vector terms, without rescaling. Write
`delta_F=sum_(n notin F) a_n`, so `||Q-Q_F||_infinity<=2 delta_F`.

The signed one-prime weight and its norm bound are

\[
 h_p(\theta)=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta),\qquad
 \int h_p=0,\qquad
 \|h_p\|_1\le b_p:=\frac{2\log p}{\sqrt p-1}.
 \tag{3}
\]

Choose a sufficiently large integer `P`. Three applications of the
classical Bertrand prime-interval theorem give distinct primes
`p_1,p_2,p_3` in `[P,8P]`. Put

\[
 g=\tfrac12 8^{-r},\qquad
 R_P=(1-P^{-\sigma})^{-2}-1.
\]

Choose `P` large enough that

\[
 P^{-2r}\le g,\qquad
 2[(1+R_P)^2-1]\le g/2.
 \tag{4}
\]

Both are possible at every fixed positive `r,sigma`. For the three
anchor primes, `G_r(p_i,p_j)>=g` when `i!=j`. These anchors depend on
the fixed source parameters, not on the phases, an omitted prime,
the panel, a threshold, or any hypothetical zero.

Condition on all non-anchor phases. In a panel containing the three
first-power terms, write

\[
 V_F=W_F+\sum_{i=1}^3X_{F,i}(\theta_i),\qquad
 X_{F,i}=\sum_{p_i^k\in F}a_{p_i^k}e^{ik\theta_i}v_{p_i^k}.
 \tag{5}
\]

The same notation permits the full series. The vector `W_F` is
independent of the anchor angles and has norm at most one. For `i!=j`,
all terms involving `W_F`, and all single-coordinate squares, disappear
under the mixed derivative. The exact expansion is therefore

\[
 \partial_i\partial_j Q_F
 =2a_{p_i}a_{p_j}G_r(p_i,p_j)\cos(\theta_i-\theta_j)+E_{F,ij},
\]
\[
 |E_{F,ij}|
 \le 2a_{p_i}a_{p_j}[(1+R_P)^2-1]
 \le \tfrac g2 a_{p_i}a_{p_j}.
 \tag{6}
\]

Indeed the derivative mass of the higher powers relative to the first
one is at most
`sum_(k>=2) k p_i^(-(k-1)sigma)=(1-p_i^(-sigma))^-2-1<=R_P`.
Bounding each Gram entry by one proves (6), for every subset of the
higher powers as well as for the full series. No smallness of `W_F`
has been assumed.

For three angles there is always a pair with
`|cos(theta_i-theta_j)|>=1/2`: order their images on the circle of
length `pi`; one of the three gaps is at most `pi/3`. Thus (6) implies

\[
 \boxed{\max_{i<j}|\partial_i\partial_j Q_F|\ge c_0,
 \qquad c_0=\tfrac g2\min_{i<j}a_{p_i}a_{p_j}>0.}
 \tag{7}
\]

All conditional functions also have a common `C^3(T^3)` bound `B`
depending only on `sigma,r` and the selected anchors. To see this,
bound anchor-vector derivatives by the convergent series
`sum_(k>=1) k^j a_(p_i^k)`, `j<=3`, and apply the product rule to (5).
These bounds hold uniformly in the conditioned phases and panels,
including after deleting any non-anchor prime.

## Local curvature gives square-root stability in total variation

Here is the precise smoothing lemma being used. Let real functions
`f,g` on `T^3` satisfy `||f||_(C^3),||g||_(C^3)<=B`, and suppose
`max_(i<j)|partial_i partial_j f|>=c_0` everywhere. For every real
`C^1` weight `rho`,

\[
 \|f_\#(\rho m_3)-g_\#(\rho m_3)\|_{\rm TV}
 \le K_{B,c_0}\|\rho\|_{C^1}\|f-g\|_{C^1}^{1/2}.
 \tag{8}
\]

Use the maximum of the suprema of the Euclidean derivative-tensor
operator norms through the indicated order for `C^j`; in particular
`||d||_(C^1)` bounds `|D_v d|` for every unit direction `v`.
The total variation convention is the full mass of the variation
measure, equivalently the supremum over tests bounded in absolute
value by one. The pushforward under `f` is absolutely continuous.
The same conclusion holds for `g` if it satisfies the curvature
condition too. No positive-definite Hessian or nonzero Hessian
determinant is required.

To prove the lemma, use the finite set of unit directions
`e_i` and `(e_i+e_j)/sqrt(2)`. If a Hessian entry has magnitude at least
`c_0`, at least one of these directional second derivatives has
magnitude at least `c_0/2`, since

\[
 \partial_i\partial_j f
 =D_{(e_i+e_j)/\sqrt2}^{\,2}f
   -\tfrac12(\partial_i^2f+\partial_j^2f).
 \tag{9}
\]

The `C^3` bound allows a cover of the torus by a uniformly bounded
number of small Euclidean balls with a smooth subordinate partition
of unity. On each enlarged ball one selected direction `v` satisfies
`|D_v^2 f|>=c_0/4` with fixed sign. Ball radii, partition derivatives
and the number of balls can be chosen using only `B,c_0`; the selected
direction may depend on `f`. Each support lies inside a coordinate
chart. Slicing a ball parallel to `v` gives intervals on which
`D_v f` is strictly monotone. Uniformly in the transverse slice,

\[
 |\{|D_vf|\le h\}|\ll_{B,c_0}h,\qquad
 \int_{|D_vf|\ge h}|D_vf|^{-2}\,ds\ll_{B,c_0}h^{-1}.
 \tag{10}
\]

Let `d=g-f`, `delta=||d||_(C^1)`. Absorb a partition function into
`rho`, and take a smooth cutoff `chi` that vanishes for `|D_vf|<=h`
and equals one for `|D_vf|>=2h`. For a smooth test `phi` with
`||phi||_infinity<=1`, the omitted part of
`integral [phi(g)-phi(f)]rho` is `O(||rho||_(C^1)h)` by (10).
On the rest set `f_s=f+s d`, `0<=s<=1`. If `h>=2 delta`, then
`|D_v f_s|>=|D_v f|/2` wherever the cutoff is nonzero. Integration
by parts, with no boundary term because of the partition support,
gives

\[
 \int[\phi(g)-\phi(f)]\rho\chi
 =-\int_0^1\int\phi(f_s)
       D_v\!\left(\frac{d\rho\chi}{D_vf_s}\right)\,ds.
 \tag{11}
\]

Derivatives of `d` or `rho` cost `O(delta||rho||_(C^1)/h)`.
A derivative of `chi` has the same bound because it is supported on
a set of slice length `O(h)`, and a derivative of the reciprocal
denominator has that bound by (10) and the uniform second-derivative
bound for `f_s`. Integrating the transverse variables and summing
the fixed cover gives
`O_(B,c_0)(||rho||_(C^1)[h+delta/h])`. Choose `h=sqrt(delta)` for
sufficiently small positive `delta`. The trivial variation bound
handles the other values. Smooth bounded tests determine the total
variation norm, proving (8).

For absolute continuity, on each slice `D_v f` has at most one zero.
Off that zero, the scalar change-of-variables formula applies on the
monotonicity intervals. A Lebesgue-null scalar set therefore has null
preimage on almost every slice. Fubini and the finite partition prove
the assertion, including signed smooth weights.

This proof retains `C^1` control of the map perturbation. Merely
combining a square-root translation modulus of image densities with
a weak distance estimate would generally lose the exponent needed
below.

## Summing all prime corrections

Let `S={p_1,p_2,p_3}` and let `Q^(-p)` delete the entire `p` block.
For `p notin S`, its removed vector is constant in the anchor angles.
With `D_1=sum_(i=1)^3 sum_(k>=1) k a_(p_i^k)`,

\[
 \|Q-Q^{(-p)}\|_{C^1(S)}\le 2(1+D_1)w_p.
 \tag{12}
\]

The same estimate holds for a panel, with its smaller removed mass.
Condition on the non-anchor angles and apply (8) with `rho=1`.
Multiplication by `h_p` then costs `||h_p||_1`. Since the deleted map
is independent of `theta_p`, its pushforward weighted by `h_p` is zero.
Consequently, for
`nu_p=Q_#(h_p m)` and `nu_(F,p)=(Q_F)_#(h_p m)`,

\[
 \boxed{\|\nu_p\|_{\rm TV},\ \|\nu_{F,p}\|_{\rm TV}
       \le K_{\sigma,r}b_p\sqrt{w_p}\quad(p\notin S).}
 \tag{13}
\]

Here the panel must contain the three first-power anchor terms; when
`p` is unused, `nu_(F,p)=0`. For `p in S`, the bound `b_p` suffices.
All these measures are absolutely continuous. For non-anchor `p`
this follows from the conditional unweighted lemma; for anchor `p`
use its smooth signed weight `rho=h_p` on `T^3`.

Exactly the convergence margin needed at every safe line is now
available:

\[
 \sum_p b_p\sqrt{w_p}<\infty,\qquad
 b_p\sqrt{w_p}\ll_\sigma
  (\log p)^{3/2}p^{-(\sigma+1)/2}.
 \tag{14}
\]

Comparison with all integers proves this because `sigma>1`. Thus

\[
 \nu=\sum_p\nu_p=k(x)\,dx,\qquad k\in L^1(\mathbb R),
 \tag{15}
\]

with absolute convergence in total variation. Its mass is zero and
its support is contained in `[0,q_*]`. This sums scalar pushforwards;
it does not construct the infinite signed torus density excluded by
WI-464.

## Exhaustion independence and the canonical cumulative coefficient

For any sequence of finite panels with `delta_F->0`, the three
first-power anchor terms are eventually present. Put

\[
 d_{F,1}=\sum_{i=1}^3\sum_{p_i^k\notin F}k a_{p_i^k},\qquad
 \eta_F=\|Q-Q_F\|_{C^1(S)}
       \le2(1+D_1)\delta_F+2d_{F,1}\longrightarrow0.
 \tag{16}
\]

The last convergence follows by first including any fixed finite
anchor-power prefix, then using its uniformly summable derivative
tail. It does not require nested panels.

For each fixed `p notin S`, (8), conditioning, and integration of
`|h_p|` give
`||nu_(F,p)-nu_p||_TV<=K b_p sqrt(eta_F)`. For `p in S` the weighted
lemma gives the corresponding bound with `||h_p||_(C^1)`. Hence for
every real `Y>=max S`,

\[
 \|\nu_F-\nu\|_{\rm TV}
 \le K_{\sigma,r}\left[
  \sqrt{\eta_F}\left(\sum_{p\in S}\|h_p\|_{C^1}
          +\sum_{\substack{p\le Y\\p\notin S}}b_p\right)
       +2\sum_{p>Y}b_p\sqrt{w_p}\right],
 \tag{17}
\]

where `nu_F=sum_(p in P(F)) nu_(F,p)` is the original finite-panel
coefficient. Choose `Y` by (14), then send `delta_F` to zero. This
proves total-variation convergence. In particular,

\[
 C_*(t)=\int_{-\infty}^t k(x)\,dx,\qquad
 \sup_{t\in\mathbb R}|C_F(t)-C_*(t)|\longrightarrow0.
 \tag{18}
\]

`C_*` belongs to `W^(1,1)(R)` and vanishes off `[0,q_*]`. WI-464's
`L^1` limit therefore equals `C_*` almost everywhere; continuity
makes this representative unique. The original coefficient on
Lipschitz tests is preserved:

\[
 \mathcal L(f)=\int f(x)k(x)\,dx
             =-\int f'(x)C_*(x)\,dx.
 \tag{19}
\]

It now extends to bounded Borel tests by integration against `k`.
Equation (19) is only coefficient identification; it does not extend
WI-469's arithmetic test class.

## Prior art, falsification controls and remaining boundary

For the only prime-location input, see P. Erdős, *Beweis eines Satzes
von Tschebyschef*, **Acta Litt. Sci. Szeged 5** (1932), 194–198,
[original proof](https://combinatorica.hu/~p_erdos/1932-01.pdf).
Successive dyadic intervals suffice; no short-interval prime estimate
or quantitative dependence of a zeta zero is involved.

Fractional regularity and total-variation stability of nonlinear image
laws are classical. Youri Davydov, *On distance in total variation
between image measures*, **Statistics & Probability Letters 129**
(2017), 393–400, [Theorem 1](https://arxiv.org/pdf/1611.03009), turns
translation moduli into weak-to-variation estimates and discusses
trigonometric polynomials. V. I. Bogachev, E. D. Kosov and G. I. Zelenov,
*Fractional smoothness of distributions of polynomials and a fractional
analog of the Hardy–Landau–Littlewood inequality*, **Trans. AMS 370**
(2018), 4401–4432, [§§5–6](https://arxiv.org/pdf/1602.05207), give
neighboring Gaussian-polynomial regularity and stability results.
Neither theorem is invoked with unverified hypotheses here: the
weighted local curvature estimate (8) is proved directly.

Yasutaka Ihara, *On “M-Functions” Closely Related to the Distribution
of L'/L-Values*, **Publ. RIMS 44** (2008), 893–954,
[publisher source](https://ems.press/journals/prims/articles/2161),
provides established Euler-model value-distribution context. The object
here is a Hilbert-response square with a signed prime-axis correction,
not the complex logarithmic-derivative value alone. No general
probability theorem or literature priority is claimed. The new local
conclusion is the all-safe-line extension obtained from (6)–(7).

The following controls are essential:

- A nonzero Hessian entry is enough; assuming a nonsingular or positive
  Hessian would be unjustified. Conditional critical points and
  singular response densities are allowed in (8).
- Two phases can have their sole mixed cosine vanish. Three phases
  cannot make all three leading mixed cosines small simultaneously.
  The higher-power errors are paid relative to their own pair's
  `a_(p_i)a_(p_j)`; a bound relative to the total response would not
  establish (7).
- All uncontrolled other-prime contributions are killed by the mixed
  derivative. Their size need not be smaller than any anchor term.
  Deleting an anchor is not covered by (13), and is handled as one of
  three finite exceptions.
- For very small `sigma-1` or extreme `r`, the anchors and smoothing
  constants can be very expensive. Fixed-parameter finiteness supplies
  no uniform pole-limit, moving-width or normalized far-right bound.
- Prime-only and diagonal controls retain their zero correction by
  common-rotation invariance and constancy respectively. Curvature
  does not manufacture prime-power bias or a sign for it.
- Uniform convergence in (18) is over **panel removal**, not over
  zero-sampling height. Finite scalar variation does not bound the
  scaled signed residual at an indicator boundary. WI-463's Fourier
  bracket obstruction and WI-469's fixed-test limitation survive.

The bounded investigation closes at finite scalar variation throughout
the absolute-convergence region. The proof uses no computation of zeta
zeros, numerical quadrature, Lean verification, or independent review.
No separate bounded formalization handoff with an identified material
verification or fertility advantage is selected here.
