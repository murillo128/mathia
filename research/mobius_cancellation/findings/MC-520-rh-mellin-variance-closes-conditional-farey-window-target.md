# MC-520 — RH already supplies the polynomial-window Möbius variance needed by the conditional Farey branch

**Status:** `LITERATURE+DERIVED`, `CONDITIONAL-ON-RH`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`.

## Claim and scope

Assume RH. For every fixed \(\varepsilon>0\), uniformly for real \(X\ge2\) and \(1\le H\le X\),

\[
\boxed{
\int_X^{2X}|M(x+H)-M(x)|^2\,dx
\ll_\varepsilon X^{1+\varepsilon}H.
}
\tag{1}
\]

For integer \(X,H\), the integral equals the discrete sliding moment

\[
J_\mu(X,H)=\sum_{X\le y<2X}|M(y+H)-M(y)|^2.
\tag{2}
\]

The statement is a classical conditional consequence of the reciprocal-zeta bound to the right of the critical line, Mellin Plancherel, and the Saffari–Vaughan conversion between multiplicative and additive windows. A complete derivation is given below. No new unconditional cancellation theorem, variance asymptotic, or RH mechanism is claimed.

The material consequence concerns the local clue `CLUE-farey-selected-sliding-mertens-variance`. Its explicitly authorized source packet, FD-311 and FD-312, records at balanced depth the lower bound

\[
J_\mu(X,N)\ge XN^{1/2+3c-o(1)},
\qquad c=1-\log_2(3/2),
\tag{3}
\]

and, under RH, the localization

\[
N=X^{\beta+o(1)},\qquad
\frac12\le\beta\le\frac1{1+2c}.
\tag{4}
\]

Equation (1) contradicts (3) uniformly throughout (4). Thus **the RH-conditional balanced near-capacity branch described in that packet is already excluded by classical analytic input**, even though the separate-endpoint strategy of FD-312 cannot exclude it. An additional unconditional source estimate remains a different, unresolved task. RH is used to obtain (1), not merely to localize the shell.

## 1. The analytic input is explicit

Two standard consequences of RH will be used, with constants depending on their fixed positive parameters:

\[
M(x)\ll_\alpha x^{1/2+\alpha},
\qquad
\frac1{\zeta(\sigma+it)}
\ll_{\sigma,a}(1+|t|)^a
\quad(\sigma>1/2,\ a>0).
\tag{5}
\]

The second bound is the Littlewood–Titchmarsh estimate, recorded explicitly as equation (52) in Flajolet–Vepstas, with reference to Titchmarsh, equation (14.2.6). Neither estimate is an unconditional input. The first ensures convergence of the physical Mellin transform; the second controls its high frequencies. No estimate for \(1/\zeta'(\rho)\), simplicity, or pair correlation of zeros is needed.

Fix \(1/2<\sigma<1\) and define

\[
f_\sigma(u)=e^{-\sigma u}M(e^u),\qquad u\in\mathbb R,
\]

where \(M(x)=0\) for \(0<x<1\). The first part of (5), with \(0<\alpha<\sigma-1/2\), gives \(f_\sigma\in L^1\cap L^2(\mathbb R)\). With Fourier convention \(\widehat f(t)=\int f(u)e^{-itu}\,du\), partial summation and analytic continuation give

\[
\widehat f_\sigma(t)
=\int_0^\infty M(x)x^{-\sigma-it}\frac{dx}{x}
=\frac1{(\sigma+it)\zeta(\sigma+it)}.
\tag{6}
\]

The integral is absolutely convergent and holomorphic for \(\Re s>1/2\), by choosing \(\alpha\) locally smaller than \(\Re s-1/2\). The identity first holds for \(\Re s>1\) and extends into this half-plane under RH. Thus (6) does not interchange a non-absolutely-convergent Möbius series with an integral.

## 2. Keep the difference inside the Mellin multiplier

Put \(b=\log(1+\delta)\), where \(0<\delta\le3\). Then

\[
e^{-\sigma u}\bigl(M((1+\delta)e^u)-M(e^u)\bigr)
=e^{\sigma b}f_\sigma(u+b)-f_\sigma(u).
\]

Plancherel and (6) give the exact identity

\[
\begin{aligned}
&\int_0^\infty
 |M((1+\delta)x)-M(x)|^2x^{-2\sigma-1}\,dx\\
&\qquad=\frac1{2\pi}\int_{\mathbb R}
 \left|\frac{(1+\delta)^{\sigma+it}-1}
 {(\sigma+it)\zeta(\sigma+it)}\right|^2dt.
\end{aligned}
\tag{7}
\]

For this bounded \(\delta\) range,

\[
\left|\frac{(1+\delta)^{\sigma+it}-1}{\sigma+it}\right|
\ll_\sigma \min\{\delta,(1+|t|)^{-1}\}.
\tag{8}
\]

The first bound follows from \(\int_1^{1+\delta}v^{\sigma+it-1}\,dv\), and the second from the bounded numerator. For fixed \(0<a<1/2\), (5), (7), and splitting the frequency integral at \(\delta^{-1}\) imply

\[
\int_0^\infty
 |M((1+\delta)x)-M(x)|^2x^{-2\sigma-1}\,dx
\ll_{\sigma,a}\delta^{1-2a}.
\tag{9}
\]

Indeed, for \(\delta\le1\), the two contributions are bounded by
\(\delta^2\int_0^{1/\delta}(1+t)^{2a}dt\) and
\(\int_{1/\delta}^{\infty}t^{-2+2a}dt\), both of order \(\delta^{1-2a}\). For \(1\le\delta\le3\) the same assertion follows with a larger constant. Restricting the positive physical integral to \([X,3X]\) yields

\[
\int_X^{3X}|M((1+\delta)x)-M(x)|^2dx
\ll_{\sigma,a} X^{2\sigma+1}\delta^{1-2a}.
\tag{10}
\]

The factor \(\delta\) at low frequency is the gain that separate bounds for the two endpoints discard.

## 3. Fixed additive windows incur no power loss

The Saffari–Vaughan averaging inequality states, for locally square-integrable \(F\) and \(0<H\le X\),

\[
\int_X^{2X}|F(x+H)-F(x)|^2dx
\ll\sup_{H/(3X)\le\delta\le3H/X}
\int_X^{3X}|F((1+\delta)x)-F(x)|^2dx.
\tag{11}
\]

For completeness, average
\(|F(x+H)-F(x)|^2\le2|F(x+v)-F(x)|^2+2|F(x+v)-F(x+H)|^2\)
over \(2H\le v\le3H\). Translating the second term, both resulting integrals are bounded by a constant times

\[
\int_X^{3X}\int_H^{3H}|F(x+v)-F(x)|^2\,dv\,dx.
\]

Set \(v=\delta x\). The Jacobian is at most \(3X\), and the enclosing \(\delta\)-interval has length \(O(H/X)\). Dividing by the original averaging length \(H\) proves (11). All arguments of \(F\) are in a bounded interval, so local square integrability suffices; alternatively one can truncate \(F\) outside \([0,12X]\). This is the inequality reproduced as Lemma 10 of Gorodetsky–Matomäki–Radziwiłł–Rodgers.

Apply (11) to \(F=M\), then use (10) uniformly in \(\delta\asymp H/X\):

\[
\int_X^{2X}|M(x+H)-M(x)|^2dx
\ll_{\sigma,a}X^{2\sigma+2a}H^{1-2a}.
\tag{12}
\]

For \(0<\varepsilon<1\), choose \(\sigma=1/2+\varepsilon/4\) and \(a=\varepsilon/4\). Since \(H\ge1\), (12) proves (1). Larger \(\varepsilon\) follow from any smaller one. The constants are independent of \(X,H\) and of a source-selected shell.

When \(X,H\) are integers, \(M(x+H)-M(x)\) is constant on every \([y,y+1)\), apart from immaterial endpoints. This proves (2) exactly, without an exceptional-start or discretization error.

## 4. Consequence for the authorized Farey window

In (4), \(X\le N^{2+o(1)}\). Hence (1) gives

\[
J_\mu(X,N)\ll_\varepsilon XN^{1+2\varepsilon+o(1)}.
\tag{13}
\]

The lower exponent from (3) exceeds \(1\) by

\[
d:=3c-\frac12=0.7451124978\ldots>0.
\]

Choose any fixed \(0<\varepsilon<d/2\). Equations (3) and (13) then conflict by a fixed power, uniformly over the permitted shells. Equivalently, (13) supplies the saving \(\eta=1-2\varepsilon\), which exceeds the required \(3/2-3c=0.2548875021\ldots\). For example \(\varepsilon=1/8\) supplies \(\eta=3/4\) with ample strict slack.

The upper bound holds on every dyadic start window, so choosing the window through the Farey construction creates no exceptional-set problem. The near-capacity-to-lower-bound implication (3) and the RH localization (4) are used exactly as stated in the authorized FD-311/312 packet; their upstream dependencies were not independently re-audited here. No other Farey source is needed for the Möbius estimate (1).

This leaves FD-312's endpoint no-go intact: it restricts a particular proof operation. It does not show that RH cannot provide the needed difference variance. Likewise MC-176 and MC-177 seek arithmetic input that could produce cancellation without assuming RH; (1) cannot serve that purpose without circularity.

## 5. Prior art and the corrected research boundary

The ingredients of (1) are classical, and their composition carries no novelty claim. The reciprocal-zeta estimate is anchored in Titchmarsh, *The Theory of the Riemann Zeta-Function*, second edition (1986), equation (14.2.6), also explicitly displayed in [Flajolet–Vepstas, equation (52)](https://algo.inria.fr/flajolet/Publications/FlVe06.pdf). The fixed-window conversion is [Saffari–Vaughan (1977)](https://doi.org/10.5802/aif.649), in the precise form and proof reproduced by [Gorodetsky–Matomäki–Radziwiłł–Rodgers, Lemma 10](https://doi.org/10.1007/s00039-021-00557-5).

There is also a directly relevant literature correction. [Chinis, *On the Liouville Function in Short Intervals*, arXiv:2007.06788v2, pp. 1–2](https://arxiv.org/pdf/2007.06788v2), reports Gao's unpublished RH estimate \(XH(\log X)^A\), and its footnote says the original statement was for Möbius. This is stronger than the qualitative \(o(XH^2)\) report quoted in FD-312. Gao's unpublished proof is not treated here as independently verified evidence: (1), which is already sufficient at polynomial lengths, has the explicit proof above from established analytic input.

MC-178 correctly prices Chinis's *particular* large-prime-factor theorem and its block extension. That method limitation must not be promoted to a limitation on every RH-conditional method. The \(X^\varepsilon\) loss in (1) is harmless for the current fixed polynomial windows, while it is very different from Chinis's logarithmic loss for subpolynomial windows.

The durable change is therefore to the research question: the conditional branch needs no new polynomial-window variance theorem. The genuinely additional target is an unconditional or explicitly weaker-hypothesis source estimate, with its own justified window range. This result neither supplies that estimate nor refutes its possibility.

## Audit boundaries

- RH is load-bearing twice: in the convergence/continuation behind (6) and in the frequency bound (5). Removing its label invalidates the derivation.
- \(\sigma>1/2\) and \(a>0\) are fixed before \(X,H\) vary. No uniform limit \(\sigma\downarrow1/2\) is taken, and no logarithmic-loss or asymptotic variance formula follows.
- The high-frequency tail in (9) converges because \(a<1/2\); keeping the difference before squaring is essential.
- The all-plus square-free control has Dirichlet series \(\zeta(s)/\zeta(2s)\) with a pole at \(1\), so it fails the analytic hypotheses and is not falsely assigned diagonal variance. Liouville, by contrast, has \(\zeta(2s)/\zeta(s)\) and satisfies the same conditional argument on each fixed \(\sigma>1/2\); the mechanism is not Möbius-specific beyond its Dirichlet-series input.
- No numerical experiment, formal verification, general discovery claim, or unconditional exclusion of the Farey branch is asserted.
