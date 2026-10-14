# RE-259 — Zero density removes the apparent Guth–Maynard critical Robin-moment boundary

**Status:** LITERATURE+DERIVED + UNCONDITIONAL-ORDINARY-PRIME-CRITICAL-MOMENT-DECAY + EXTENDED-ROBIN-ANNULUS-LOCALIZATION + CLASSICAL-ANALYTIC-INPUT + ORDINARY-PRIME-REMOTE-TAIL-OPEN; independent adversarial review pending.

**Dependencies:** RE-021 (CA-selected endpoint), RE-022 (mixed Robin kernel and remote truncation), RE-252 (Guth–Maynard first-annulus bound), RE-253 (signed triangular prime moment); Ingham (1940) zero density and the Korobov–Vinogradov zeta zero-free region, both already referenced in this line's SOURCES.md.

RE-253's critical triangular moment is uncontrolled by Guth–Maynard's *stated* pointwise error estimate at its own balance horizon. This is an input-strength limitation, not an unresolved need for signed prime cancellation: the classical combination of polynomial-log zero density and a zeta zero-free strip is much stronger on the longer short intervals relevant here. The result is a new application to the Robin source integral, **not** a new theorem about primes or a proof of RH.

## 1. Classical quantitative short-interval input

Let

\[
L=\log x,\quad W(x)=\frac{L^{1/3}}{(\log L)^{1/3}},\quad
\psi(x)=\sum_{n\le x}\Lambda(n).
\]

For some absolute constant \(c>0\), all sufficiently large real \(x\), and uniformly for \(x^{18/25}\le y\le x^{4/5}\),

\[
\boxed{\psi(x+y)-\psi(x)=y+O(y e^{-cW(x)}),\qquad
\pi(x+y)-\pi(x)=\frac{y}{\log x}+O(y e^{-cW(x)}).}\tag{1}
\]

For an auditable derivation choose \(T=x^{3/10}\). The standard truncated explicit formula, allowing the ordinary harmless prime-power endpoint corrections, gives

\[
\psi(x+y)-\psi(x)-y
=-\sum_{|\Im\rho|\le T}\frac{(x+y)^\rho-x^\rho}{\rho}
+O(xT^{-1}\log^2(xT)+\log^2 x).
\tag{2}
\]

Each zero term has absolute value at most \(yx^{\beta-1}\), \(\beta=\Re\rho\). Ingham's *uniform* polynomial-log zero-density bound is

\[
N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}(\log T)^5
\quad(1/2\le\sigma\le1).
\tag{3}
\]

The Korobov–Vinogradov zero-free region ensures every zero of height at most \(T\) has

\[
\beta\le1-\eta,\quad
\eta=\frac{c_0}{(\log T)^{2/3}(\log\log T)^{1/3}}
\asymp L^{-2/3}(\log L)^{-1/3}.
\tag{4}
\]

Using \(N(1/2,T)\ll T\log T\) and integrating the zero-counting function by real part,

\[
\begin{aligned}
\sum_{|\Im\rho|\le T}x^{\beta-1}
&\ll x^{-1/2}T\log T+L\int_{1/2}^{1-\eta}x^{\sigma-1}N(\sigma,T)\,d\sigma\\
&\ll x^{-1/5}L+L(\log T)^5\int_{1/2}^{1-\eta}
\exp\!\left[-(1-\sigma)L\left(1-\frac{9/10}{2-\sigma}\right)\right]d\sigma\\
&\ll\exp(-c_1 W(x)),
\end{aligned}\tag{5}
\]

since \(1-(9/10)/(2-\sigma)\ge1/10\), \(\eta L\asymp W(x)\), and logarithmic powers are absorbed by lowering \(c_1>0\). The truncation error is \(O(x^{7/10}L^2)\), negligible compared to \(y e^{-c_2 W(x)}\) because \(y\ge x^{18/25}\) leaves the strict \(1/50\) power margin. This proves the \(\psi\) estimate in (1). Removing prime powers costs \(O(x^{1/2}L^2)\); replacing logarithmic prime weights by \(\log x\) costs \(O(y^2/x)\). Both are swallowed by the error in (1), uniformly up to \(y=x^{4/5}\). This is **all-start**, unconditional and not an almost-all estimate.

## 2. Exact triangular-moment consequence

Let \(p\) range over *all* ordinary primes, with \(L=\log p\), \(W=W(p)\), and use RE-253's definition

\[
D_p(H)=\int_0^H\left[\pi(p+y)-\pi(p)-\frac{y}{L}\right]dy.
\tag{6}
\]

Below \(y_0=p^{18/25}\), the trivial prime count gives \(\big|\pi(p+y)-\pi(p)-y/L\big|\ll y+1\). Above \(y_0\), (1) applies with \(x=p\). Thus uniformly for \(0\le H\le p^{4/5}\),

\[
\boxed{|D_p(H)|\ll p^{36/25}+H^2 e^{-cW}.}\tag{7}
\]

Fix \(0<\kappa<c/2\), set

\[
\boxed{H_\dagger(p)=\frac{p^{3/4}}{\sqrt{L}}\exp\bigl(\kappa W(p)\bigr).}\tag{8}
\]

Then \(H_\dagger\le p^{4/5}\) eventually and

\[
\boxed{\sup_{0\le H\le H_\dagger}\frac{L}{p^{3/2}}|D_p(H)|
\ll Lp^{-3/50}+\exp(-(c-2\kappa)W)=O_M(L^{-M})\quad(\forall M>0).}\tag{9}
\]

RE-252–RE-253's Guth–Maynard balance horizon was

\[
H_\star(p)=\frac{p^{3/4}}{\sqrt L}\exp\bigl(\tfrac12 L^{1/4}\bigr).
\]

Because \(W/L^{1/4}=L^{1/12}/(\log L)^{1/3}\to\infty\), one has \(H_\star=o(H_\dagger)\). In particular,

\[
\boxed{D_p(H_\star)=o(p^{3/2}/L)}\tag{10}
\]

holds for **every unbounded ordinary-prime sequence**, without a CA selection hypothesis, via an absolute upper bound rather than a signed-cancellation theorem.

## 3. CA-selected Robin source and remaining tail

Let \(C\) be any sufficiently large regular self-tangent colossally abundant state, and let \(p\) be the last active first-layer prime. RE-021 supplies \(|\vartheta(p)-p|\ll p^{13/25}\), even for exceptional adjacent CA transitions. Define

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t},\qquad
k(t)=\frac{1}{t\log t},\qquad
I(t)=(\vartheta(t)-t)h'(t)-(h(t)-k(t)).
\]

RE-253's exact kernel expansion, with all endpoint and logarithmic weight terms retained, gives for \(1\le H\le p^{4/5}\)

\[
\sqrt p L\int_p^{p+H}I(t)dt
=-a_pD_p(H)+O\!\left(\frac{H(1+|\vartheta(p)-p|)}{p^{3/2}}
+\frac{L(H^3+H^2)}{p^{5/2}}\right),\quad
 a_p=-\sqrt p L^2h'(p)=\frac L{p^{3/2}}(1+O(L^{-1})).
\tag{11}
\]

The \(H<1\) case follows from the elementary kernel bound. At \(H\le H_\dagger=p^{3/4+o(1)}\), the remainders are respectively \(p^{-23/100+o(1)}\) and \(p^{-1/4+o(1)}\). With (9),

\[
\boxed{\sup_{0\le H\le H_\dagger}\left|\sqrt pL\int_p^{p+H}I(t)dt\right|
=O_M(L^{-M})\quad(\forall M>0).}\tag{12}
\]

The remote-tail cutoff of RE-022 is \(U_A(p)=\exp(A L^{5/3}(\log L)^{1/3})\), for a sufficiently large fixed \(A\). The exact CA tax from RE-021 and (12) now yield

\[
\boxed{\begin{aligned}
\sqrt pL(\log G(C)-\gamma)
&=\sqrt pL\int_{p+H_\dagger}^{U_A(p)}I(t)dt
 -2\sqrt2+\frac{\sqrt2(2+\log2)}L+O_A(L^{-2}).
\end{aligned}}\tag{13}
\]

Hence an infinite counterexample family still needs a positive normalized *remote* mixed-race excursion with lower limit \(2\sqrt2\). No result here estimates that remote integral, excludes ordinary-prime/CA-selected positive excursions, or proves Robin's inequality or RH.

## 4. Literature novelty and falsification boundaries

Analytic inputs are classical: A. E. Ingham, *On the estimation of N(sigma,T)*, QJM **os-11** (1940), 201–202, DOI 10.1093/qmath/os-11.1.201; the Korobov–Vinogradov zero-free region and the conventional truncated explicit formula. For a modern uniform-in-\(\sigma\) density formulation see S. Chourasiya and A. Simonič, *An explicit form of Ingham's zero density estimate*, arXiv:2507.15184v2 (2025). For this general short-interval mechanism see V. Starichkova, *A note on zero-density approaches for the difference between consecutive primes*, arXiv:2411.01845 (2024). The line's existing SOURCES.md already anchors both load-bearing density and zero-free inputs. **There is no claim of novelty for the analytic prime-number theorem itself.** The substantive line-local deduction is that RE-253's signed-moment frontier disappears when the stronger classical input is used at precisely the CA/Robin-sensitive scale.

Potential failure modes explicitly checked: the exponent must have a *uniform polynomial-log* density bound rather than an uncontrolled \(T^{o(1)}\) factor; the choice \(T=x^{3/10}\) gives the strict density margin \(1/10\), and \(y\ge x^{18/25}\) gives the strict explicit-formula truncation margin \(1/50\); the small-\(y\) \(p^{36/25}\) loss is retained; the CA endpoint error and cubic Taylor error both decay at \(H_\dagger\); the claimed comparison is asymptotic with unspecified positive constants. RE-254–RE-257 generalized-prime source controls obey only the *weaker* Guth–Maynard-scale envelope and need not inherit zeta zero-density/zero-free arithmetic: they do not refute (1). No independent adversarial review has been completed.

**Research consequence:** RE-253's apparently critical signed moment was an artifact of the weaker input. The remaining potentially RH-relevant problem begins beyond \(H_\dagger\), in the CA-selected signed mixed Mertens–Chebyshev tail.
