# WI-471 — the full Euler response has no unrestricted smooth Wiener calculus

**Status:** LITERATURE+EXACT-DERIVED + CLASSICAL-FUNCTIONAL-CALCULUS-OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-469](WI-469-gevrey-cutoffs-admit-the-full-first-euler-sampling-correction.md), for the logarithmically weighted rational-coefficient sampling certificate and its Gevrey class; [WI-470](WI-470-three-prime-curvature-gives-finite-euler-correction-at-every-safe-line.md), for the separate finite signed scalar correction measure.

## Claim and mathematical boundary

Fix `sigma>1` and `r>0`. Let `Q` be the full, originally normalized coherent Euler response on the prime torus, and let `A(T^P)` be the Wiener algebra of absolutely summable rational-character coefficients. Then for every positive integer `d` there is a constant `c_d>0`, depending on the fixed source parameters and selected primes, such that

\[
 \boxed{\|e^{itQ}\|_{A(\mathbb T^{\mathcal P})}
       \ge c_d |t|^{d/2}\qquad(|t|\ge1).}
 \tag{1}
\]

In particular the norm grows faster than every fixed power of `|t|`. There exists a **fixed real four-periodic smooth function** `f`, with `0<=f<=1`, for which

\[
 \boxed{f(Q)\notin A(\mathbb T^{\mathcal P}).}
 \tag{2}
\]

For that same `f`, every finite prime-power panel `F` has `f(Q_F)` in WI-469's fourth-logarithmic-moment coefficient algebra, but along every exhaustion with omitted coefficient mass tending to zero,

\[
 \|f(Q_F)\|_A\longrightarrow\infty.
 \tag{3}
\]

Thus replacing WI-469's specified Gevrey class by *all* fixed smooth scalar tests cannot be accomplished by simply proving their absolute rational-coefficient summability. The obstruction already holds in the **unweighted** norm, before any arithmetic error or logarithmic weight is charged. This proves failure of the coefficient certificate. It does not decide whether the actual first zero-sampling formula holds for the test in (2).

WI-470 remains compatible with this obstruction: its finite scalar correction measure defines the candidate coefficient for every bounded Borel test, without supplying the source-side coefficient norm needed by WI-469. Neither theorem decides hard-threshold arithmetic transport or excludes any off-critical zero.

## Objects and a contractive finite-coordinate restriction

Let `m` denote probability Haar measure on the product of angle circles indexed by primes. Set

\[
 A_\sigma=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\frac{\Lambda(n)n^{-\sigma}}{A_\sigma},\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 c_{nm}=a_na_mG_r(n,m),\qquad
 Q(z)=\sum_{n,m\ge2}c_{nm}\chi_{n/m}(z),\qquad
 \chi_u(z)=\prod_p z_p^{\nu_p(u)}.
 \tag{4}
\]

Only prime powers have nonzero `a_n`, and `sum a_n=1`. For all integers `n,m>=2`,

\[
 G_r(n,m)=\left(\frac{\min(n,m)}{\max(n,m)}\right)^r
          [1-\min(n,m)^{-2r}]>0.
 \tag{5}
\]

Consequently `c_nm>=0`, the series is absolutely and uniformly convergent, and its Hilbert Gram representation gives `0<=Q<=Q(1)<=1`.

For a reduced rational `u=a/b>0`, define `H(u)=ab`. The two coefficient norms used here are

\[
 \|F\|_A=\sum_{u\in\mathbb Q_{>0}}|\widehat F(u)|,
 \qquad
 \|F\|_{[4]}=\sum_u|\widehat F(u)|(1+\log H(u))^4.
 \tag{6}
\]

Rational numbers index the finite-support integer exponent vectors, hence all characters of the prime torus. Equal rational characters in (4) are collected before taking either norm. Both are Banach algebra norms, and `||F||_infinity<=||F||_A<=||F||_[4]`. In particular `Q` and `e^(itQ)` belong to `A` for every fixed `t`; this is not a claim of infinite norm at any finite frequency.

Choose any `d` distinct primes `p_1,...,p_d`, and freeze every other prime coordinate at one. Write `R_d` for this restriction and

\[
 q_d(\theta)=R_dQ(\theta),\qquad \theta\in\mathbb T^d.
\]

For an absolutely summable character expansion, restriction groups together characters with the same selected exponent vector. The triangle inequality therefore gives

\[
 \|R_dF\|_{A(\mathbb T^d)}\le\|F\|_A,
 \qquad R_d(e^{itQ})=e^{itq_d}.
 \tag{7}
\]

This is evaluation of the complementary coordinates, **not** averaging over them and not a finite Euler truncation. It is legitimate even though the frozen fiber has zero product Haar measure: functions in `A` have continuous representatives with uniformly convergent character expansions.

## The coherent point has full curvature in every finite dimension

For a prime power `n`, put

\[
 \alpha(n)=(\nu_{p_1}(n),\ldots,\nu_{p_d}(n)).
\]

The symmetry `c_nm=c_mn` makes the restricted function real, with

\[
 q_d(\theta)=\sum_{n,m}c_{nm}
       \cos((\alpha(n)-\alpha(m))\cdot\theta).
 \tag{8}
\]

This function is smooth to every order. For each selected prime and integer `j>=0`, the differentiated coefficient mass is bounded using
`sum_(k>=1) k^j a_(p_i^k)<infinity`; all unselected terms have zero angle derivative. Products of these convergent sums justify termwise differentiation of (8).

At the coherent point `theta=0`, the Hessian is the negative of a positive graph-energy matrix:

\[
 -D^2q_d(0)=\sum_{n,m}c_{nm}
       (\alpha(n)-\alpha(m))(\alpha(n)-\alpha(m))^{\!\top}.
 \tag{9}
\]

Choose a single prime `q` outside the selected finite set. The two ordered terms `(n,m)=(p_i,q),(q,p_i)` already contribute `2a_(p_i)a_q G_r(p_i,q) e_i e_i^top`. Every other term is positive semidefinite. Thus, for `v in R^d`,

\[
 v^\top[-D^2q_d(0)]v
 \ge 2a_q\sum_{i=1}^d a_{p_i}G_r(p_i,q)v_i^2>0
 \quad(v\ne0).
 \tag{10}
\]

No cancellation or estimate on the other primes is necessary. The anchored star in (10) removes every finite-coordinate null direction. Its constants can deteriorate arbitrarily with `d`, but are strictly positive at every fixed `d,sigma,r`.

The inverse function theorem applied to `grad q_d` at zero shows that `grad q_d(T^d)` contains an open set and therefore has positive `d`-dimensional measure. The gradient is Lipschitz because `q_d` is smooth on a compact torus.

## The classical oscillatory Wiener bound

Lebedev's Corollary 2 states that a real `C^(1,1)` phase `phi` on `T^d`, whose gradient image has positive measure, satisfies

\[
 \|e^{it\phi}\|_{A(\mathbb T^d)}\ge c_\phi |t|^{d/2}
 \tag{11}
\]

whenever the exponential belongs to that algebra. See *Estimates in Beurling–Helson type theorems. Multidimensional case*, author preprint, [Corollary 2, p. 6](https://arxiv.org/pdf/1201.0403). Here membership holds for every real `t`, since `q_d` is smooth (or by (7)). Equations (9)–(10) verify the nondegeneracy hypothesis; compact smoothness verifies the Lipschitz hypothesis. Combining (11) with (7) proves (1).

For any real `K>=0`, first fix an integer `d>2K`. The constant in (1) is then fixed as `|t|` grows, so

\[
 |t|^{-K}\|e^{itQ}\|_A\longrightarrow\infty.
 \tag{12}
\]

There is no exchange of a growing dimension with the frequency limit. No uniform-in-`d` stationary-phase constant is asserted. This result also does not identify a stretched-exponential lower rate or prove sharpness of WI-469's Gevrey order.

## Why some fixed smooth test must fail absolute summability

Suppose, to the contrary, that `f(Q)` belongs to `A` for every complex smooth function on the scalar circle `R/4Z`. Composition would define a linear map

\[
 C_Q:C^\infty(\mathbb R/4\mathbb Z)\longrightarrow A,
 \qquad C_Q f=f(Q).
 \tag{13}
\]

Its graph is closed. Indeed, if `f_j->f` in the smooth Fréchet topology and `f_j(Q)->F` in `A`, both convergences imply uniform convergence of the composed functions, so `F=f(Q)`. The Fréchet closed-graph theorem then makes (13) continuous. Since its target is normed, continuity provides a finite integer `K` and a constant `C` such that

\[
 \|f(Q)\|_A\le C\max_{0\le j\le K}\|f^{(j)}\|_\infty.
 \tag{14}
\]

Take `f_l(x)=exp(i pi l x/2)`, `l in Z`. The right side of (14) is `O((1+|l|)^K)`, whereas (12) on the frequency sequence `t=pi l/2` contradicts that bound. This proves existence of a fixed smooth test outside `A`.

If a complex test fails, at least one of its real or imaginary parts fails, since `A` is a complex vector space. A real failing test is bounded and nonconstant. Shifting and multiplying it by a nonzero real constant normalizes its range into `[0,1]` without restoring membership in `A`. This proves the real, bounded assertion (2). Existence is proved by functional analysis; no explicit formula for this smooth test, monotonicity, or exact cutoff plateaus is claimed.

The argument is the usual link between smooth functional calculus and polynomial growth of an exponential group, applied to this one fixed source element. It does not assert that scalar smoothness is inadequate for evaluating `f(Q)` as a continuous function; only absolute Fourier summability fails.

## Every finite panel works, but its certificate can diverge

Let `F` be a finite set of prime powers, define `Q_F` by restricting both indices in (4) to `F` with the same `A_sigma`, and put `delta_F=sum_(n notin F) a_n`. The Gram representation gives

\[
 \|Q-Q_F\|_\infty\le2\delta_F.
 \tag{15}
\]

A finite panel depends on finitely many prime angles, say `d_F` of them. For every fixed smooth `f`, the function `f(Q_F)` is smooth on that finite torus. Its Fourier coefficients decrease faster than every polynomial in the exponent vector `k`. For those primes,
`log H(chi_k)<=C_F |k|_1`; choosing decay order greater than `d_F+4` proves `||f(Q_F)||_[4]<infinity`.

Now take the failing test from (2) and any sequence of finite panels with `delta_F->0`, nested or otherwise. Equation (15) implies uniform convergence `f(Q_F)->f(Q)`, hence convergence of each rational-character Fourier coefficient. If a subsequence had uniformly bounded `A` norms, Fatou's lemma for the countable coefficient sum would imply

\[
 \sum_u|\widehat{f(Q)}(u)|
 \le\liminf_F\sum_u|\widehat{f(Q_F)}(u)|<\infty.
 \tag{16}
\]

Absolute summability of these coefficients would put the continuous function `f(Q)` in `A`: its uniformly convergent Fourier series has the same coefficients, and uniqueness on the compact prime torus identifies the functions. This contradicts (2). More directly, arbitrarily large finite partial sums on the left of (16) force all sufficiently late panel norms to exceed any prescribed bound. Thus the norms tend to infinity, proving (3), and the stronger `[4]` norms diverge as well.

## Prior art, controls, and consequence for the line

Vladimir Lebedev, *Estimates in Beurling–Helson Type Theorems: Multidimensional Case*, **Mathematical Notes 90** (2011), 373–384, [author preprint](https://arxiv.org/abs/1201.0403), supplies the finite-dimensional lower bound. The paper also attributes the smooth nonzero-Hessian case to earlier work of Hedstrom. No new general oscillatory-norm theorem is claimed.

Mats Andersson, Håkan Samuelsson and Sebastian Sandberg, *Operators with smooth functional calculi*, **Journal d'Analyse Mathématique 98** (2006), 221–248, [§2.2](https://arxiv.org/pdf/math/0503256), records the classical equivalence between smooth calculus and polynomial exponential growth for bounded real-spectrum operators. The closed-graph proof above gives the precise implication needed here without importing an operator resolvent hypothesis.

The substantive specialization is (9)–(10) for the actual full Euler response, followed by finite-coordinate contraction and the infinite-panel obstruction. Local searches against the existing Euler findings did not identify this coefficient-calculus boundary; search absence is not a priority claim.

The controls delimit the result:

- At every fixed finite number of prime coordinates, arbitrary smooth composition has absolutely summable coefficients. The obstruction uses the one full response having nondegenerate restrictions in **all** finite dimensions, not failure of a finite-dimensional smooth theorem.
- The same anchored-star Hessian argument works after deleting higher prime powers, as long as infinitely many prime tones retain positive coefficients. That prime-only control has zero prime-axis sampling correction by common-rotation invariance. Hence Wiener-norm growth does not itself certify arithmetic bias or detect off-line zeros.
- A diagonal-only response is constant and has exponential Wiener norm one. The off-diagonal positivity in (5) and retained infinite prime coordinates are load-bearing.
- `r=0` gives a zero Gram kernel and is excluded. Limits `r->0`, `sigma->1`, or `sigma->infinity` are not uniform conclusions of (1).
- WI-469's class `1<s<sigma` still works. This argument neither makes that endpoint sharp nor refutes arithmetic transport for every smooth test outside the coefficient algebra. Cancellation or a different norm could support such a theorem.
- WI-470's finite signed scalar coefficient and its bounded-Borel extension remain valid. Scalar image-measure regularity and absolute source Fourier summability are different properties; one does not supply the other.

The bounded question closes with an exact obstruction to unrestricted smooth composition in the present certificate. A continuation toward threshold sampling requires different arithmetic remainder control, not a claim that ordinary smoothness alone pays every infinite-prime coefficient cost. This proof uses checked primary-source hypotheses and an explicit Hessian calculation; no numerical zero experiment, formal proof, or independent adversarial certification is claimed. No separate bounded formalization target with a material verification or fertility advantage is selected from this classical argument.
