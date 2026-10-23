# MI-101 — Smooth deconvolution reaches sharp Mertens recovery through zero exclusion

**Evidence level:** supported conditional synthesis of [MC-521](../../findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss.md), with the direct endpoint comparison in [MC-177](../../findings/MC-177-gallagher-diagonal-energy-direct-mertens-power.md) and the RH converse in [MC-520](../../findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md). The variance input is not proved unconditionally; no novelty or formal verification is claimed.

Let `M(t)=sum_(n<=t) mu(n)`. Fix `0<theta<1`, `0<eta<=1`, `H=X^theta`, and `alpha=1-theta eta/2`. Suppose that for every `epsilon>0`, uniformly for all sufficiently large real `X`, the complete, uncentered moment satisfies

`J(X,H)=int_X^(2X) |M(y+H)-M(y)|^2 dy <<_epsilon X^(1+epsilon)H^(2-eta)`.

Then `zeta(s)` has no zeros in `Re(s)>alpha`, and the classical reciprocal-zeta bridge gives `M(x)<<_epsilon x^(alpha+epsilon)` for every `epsilon>0`. For the multiplicative-window input below, MC-177's direct recovery of sharp endpoints gives only the Mertens exponent `max(alpha,theta)`. The stronger conclusion first excludes zeros using smooth tests, then recovers the sharp sum using the specific analytic structure of zeta.

For bounded coefficients `|a_n|<=1`, `n>=1`, and any fixed `w in C_c^infty((1,2);C)`, put `A_w(X)=sum_n a_n w(n/X)` and `h=H/X`. The box average

`B_h v(z)=h^(-1) int_0^h v(z-u) du`

gives an exact averaging identity: if `S(y)=sum_(y<n<=y+H) a_n`, then `H^(-1) int_R S(y)v(y/X)dy=sum_n a_n B_h v(n/X)`. For a positive integer `K`, correct the known weight by the finite polynomial

`v_h=sum_(j=0)^(K-1)(I-B_h)^j w`, so `B_h v_h=w-(I-B_h)^K w`.

For fixed `K`, its support stays inside `(1,2)` eventually, its `L^2` norm is bounded independently of `h`, and the residual has sup norm at most `h^K ||w^(K)||_infinity`. Hence

`|A_w(X)| <<_(K,w) (sqrt(X)/H) ||S||_(L^2[X,2X]) + X(H/X)^K`.

Choose `K(1-theta)>theta eta/2` before varying `X`. The two terms are then `O(X^(alpha+epsilon))` and `o(X^alpha)`. Using only the uncorrected weight would leave `O(H)`; finite correction removes that error without inverting the box filter on arbitrary data. For multiplicative windows, replacing `B_h` by `C_b v(z)=b^(-1) int_0^b v(ze^(-u))du`, `b=H/X`, gives the same conclusion from `int_X^(2X)|M(e^b y)-M(y)|^2 dy/y <<_epsilon X^epsilon H^(2-eta)`.

With `a_n=mu(n)`, the smooth-sum bound makes `F_w(s)=int_0^infty A_w(X)X^(-s-1)dX` holomorphic on `Re(s)>alpha`. Initially for `Re(s)>1`, `F_w(s)=w_hat(s)/zeta(s)`, where `w_hat(s)=int_1^2 w(u)u^(s-1)du`. Continue the identity `(s-1)zeta(s)F_w(s)=(s-1)w_hat(s)`. A single weight could mask a zero. The whole test family cannot: for a putative zero `rho=beta+i gamma`, take `w(u)=psi(u)u^(-i gamma)` with nonzero nonnegative `psi in C_c^infty((1,2))`; then `w_hat(rho)>0`. Constants may depend on this fixed zero, so this test step alone gives no reciprocal-zeta bound uniform at growing height.

The extra step in MC-521, Section 4, uses polynomial vertical growth of zeta and its bounded Euler-product logarithm to the right of `1`. Inside a fixed zero-free half-plane, Borel--Caratheodory followed by three-circles gives `|log zeta(sigma+it)|<< (log |t|)^q`, with some fixed `q<1`, on every fixed interior strip. Consequently `1/zeta(sigma+it)<<_nu(1+|t|)^nu` for each `nu>0` and fixed `sigma>=sigma_0>alpha`. Truncated Perron, shifted to `sigma_0`, then gives

`M(x)<< x^sigma_0 T^nu + x^2 T^(nu-1) + x^2/T`.

Taking `T=x^3` and `sigma_0+3nu<alpha+epsilon` recovers the sharp Mertens exponent. No uniform limit `sigma_0` down to `alpha`, endpoint `O(x^alpha)` bound, or general sharp inversion theorem for arbitrary bounded coefficients follows. For Möbius, nonvanishing and the epsilon-loss Mertens conclusion are equivalent; the fixed-window variance premise is only proved sufficient, not equivalent to them.

The improvement over the direct endpoint exponent is strict exactly when `theta>2/(2+eta)`. It does not cover `theta=1` or remove MC-177's Gaussian-removal cost when its input is a weighted Gallagher energy rather than the unweighted moment above. Bounded multiplicative controls `a_n=n^(alpha-1)` and `a_n=mu(n)^2 n^(alpha-1)` meet the same variance ceiling but have a Dirichlet-series pole at `alpha`; generic continuation cannot cross that boundary. These controls do not match Möbius prime signs.

The scale quantifier is decisive. A source-selected shell, an uncontrolled exceptional-start contribution, or centering by an uncontrolled local mean cannot supply the hypothesis. Diagonal bounds (`eta=1`) at every sufficiently large scale for each of a sequence of fixed `theta_j` tending to `1` imply RH; [MI-100](MI-100-mellin-differences-retain-the-rh-short-window-variance-gain.md) supplies the converse under RH. No uniformity in `j` is required. This calibrates the strength of the variance family without supplying its arithmetic proof.
