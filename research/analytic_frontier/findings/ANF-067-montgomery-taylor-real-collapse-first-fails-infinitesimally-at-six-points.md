# ANF-067 — Montgomery--Taylor real collapse first fails infinitesimally at six points

**Status:** `EXACT-DERIVED + COMPUTER-ASSISTED-INPUT + LARGER-CONFIGURATION-BOUNDARY + SIX-POINT-COMPLEX-REVERSAL + EXPLICIT-RATIONAL-WITNESS + NO-RH-CONSEQUENCE`.

`ANF-062`--`ANF-066` close the fixed Montgomery--Taylor five-point scalar geometry: the genuine two-pair defect is positive, has a sharp quadratic floor with positive higher height corrections, and its near-extremizers are completely classified. The local mind therefore asks for a transfer only when the source category genuinely changes. The change occurs immediately at the next cardinality. The one-conjugate-pair formula already derived in `ANF-037`, combined with the certified curvature minimum of `ANF-066`, shows that the Montgomery--Taylor profile itself has a strict **six-point complex-versus-real-collapse reversal at arbitrarily small positive height**.

Let

\[
F_{\rm MT}(z)=\widehat J_{\rm MT}(z),
\qquad
K(t)=\int_{-1}^{1}\alpha^2J_{\rm MT}(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\tag{1}
\]

and write

\[
K_0=K(0),\qquad k_*=\inf_{t\in\mathbb R}K(t).
\tag{2}
\]

For the four fixed distinct rational anchors

\[
T:=\left\{\frac{37}{50},\frac34,\frac{19}{25},\frac{77}{100}\right\}
=\{0.74,0.75,0.76,0.77\},
\tag{3}
\]

define the conjugation-invariant six-point multiset

\[
W_y:=\{iy,-iy\}\cup T,
\qquad y>0,
\tag{4}
\]

and its real-part collapse

\[
R(W_y):=\{0,0\}\cup T.
\tag{5}
\]

Then there exists `y_0>0` such that

\[
\boxed{
E_{F_{\rm MT}}(W_y)<E_{F_{\rm MT}}(R(W_y))
\qquad(0<y<y_0).
}
\tag{6}
\]

Moreover both multisets have cardinality six and exactly four simple real points. Hence (6) is a genuine new affine constraint relative to real collapse: it is not hidden by simple-point bookkeeping. It does **not** by itself prove that the Montgomery--Taylor affine certificate, or a narrow central-notch perturbation, fails at six points; it proves that the five-point real-collapse/coercivity mechanism cannot simply be propagated to the next cardinality.

## 1. The one-pair formula gives the complete small-height cardinality gate

`ANF-037` treats one conjugate pair together with `m` real anchors. With pair center at zero, put

\[
c_y(\alpha)=\cosh(2\pi\alpha y),
\qquad
p_y(\alpha)=J_{\rm MT}(\alpha)(c_y(\alpha)-1),
\tag{7}
\]

\[
L_y(t)=\int_{-1}^{1}p_y(\alpha)\cos(2\pi\alpha t)\,d\alpha,
\qquad
A_y=\int_{-1}^{1}J_{\rm MT}(\alpha)(c_y(\alpha)^2-1)\,d\alpha.
\tag{8}
\]

For distinct real anchors `t_1,...,t_m`, its exact structure-factor identity is

\[
E_F(\{iy,-iy,t_1,\ldots,t_m\})
-E_F(\{0,0,t_1,\ldots,t_m\})
=4\left(A_y+\sum_{j=1}^mL_y(t_j)\right).
\tag{9}
\]

Compact spectral support also gives the uniform small-height limits already proved there,

\[
\frac{A_y}{2\pi^2y^2}\longrightarrow2K_0,
\qquad
\frac{L_y(t)}{2\pi^2y^2}\longrightarrow K(t)
\quad\text{uniformly in }t.
\tag{10}
\]

Thus for any fixed finite anchor set,

\[
\boxed{
\frac{E_F(W_y)-E_F(R(W_y))}{8\pi^2y^2}
\longrightarrow
2K_0+\sum_jK(t_j).
}
\tag{11}
\]

If the anchors are allowed to approach a global minimizer of `K`, the sharp infinitesimal one-pair gate with `m` real anchors is therefore

\[
\boxed{2K_0+mk_*\ge0.}
\tag{12}
\]

This is the general cardinality version of the five-point curvature quantity `m_5=2K_0+3k_*` used throughout `ANF-037`--`ANF-066`.

For Montgomery--Taylor, the certified values place the curvature ratio strictly between the two adjacent thresholds. `ANF-064` gives

\[
2K_0+3k_*>0,
\tag{13}
\]

whereas the `ANF-059` upper bound

\[
K_0<0.1549985926411777
\tag{14}
\]

and the `ANF-066` certified global minimum

\[
k_*< -0.091274161151487458115
\tag{15}
\]

give

\[
\boxed{
2K_0+4k_*<-0.05509945932359.
}
\tag{16}
\]

Equivalently,

\[
-\frac23<\frac{k_*}{K_0}< -\frac12.
\tag{17}
\]

So the infinitesimal one-pair collapse gate changes sign **exactly between three and four real anchors**, i.e. between total cardinalities five and six. Every one-pair layer with `m>=4` admits the same kind of sufficiently-small-height reversal by placing its real anchors near a curvature minimizer.

## 2. Four fixed rational anchors already give a strict witness

The preceding argument can be made independent of coalescing-anchor limits. `ANF-066` certifies a unique positive minimizer

\[
\tau\in
[0.7588064485352071602166,
 0.7588064485352071602167]
\tag{18}
\]

with

\[
K(\tau)=k_*,\qquad K'(\tau)=0.
\tag{19}
\]

The Fourier representation gives the global derivative bound used in `ANF-066`,

\[
|K''(t)|
\le4\pi^2\int_{-1}^{1}\alpha^4J_{\rm MT}(\alpha)\,d\alpha
\le4\pi^2.
\tag{20}
\]

Taylor's theorem at `tau` therefore yields

\[
K(t)\le k_*+2\pi^2(t-\tau)^2
\qquad(t\in\mathbb R).
\tag{21}
\]

For the four rationals in (3), the certified interval (18) gives

\[
\sum_{t\in T}(t-\tau)^2
<0.000557957.
\tag{22}
\]

Combining (14)--(15), (21), and (22),

\[
\begin{aligned}
2K_0+\sum_{t\in T}K(t)
&<2(0.1549985926411777)
+4(-0.091274161151487458115)\\
&\qquad+2\pi^2(0.000557957)\\
&<-0.04408.
\end{aligned}
\tag{23}
\]

The limiting coefficient in (11) is therefore separated from zero by a substantial certified margin for this **fixed** rational horizontal geometry. By (10)--(11), there is a `y_0>0` such that the energy difference remains negative for every `0<y<y_0`, proving (6). No floating-point minimization or sampled sign test is used in this existence step; the numerical inputs are outward-certified bounds already canonical in `ANF-059` and `ANF-066`.

The witness is also robust horizontally. Equation (23) has more than `0.044` of curvature margin, so sufficiently small perturbations of the four anchors preserve the negative second variation. The six-point reversal is therefore an open local phenomenon, not an isolated arithmetic coincidence of the chosen rationals.

## 3. What changes after the completed five-point program

The important distinction is between **five-point positivity** and **larger-cardinality real-collapse dominance**. `ANF-062`--`ANF-066` show that the fixed Montgomery--Taylor two-pair five-point defect cannot become nonpositive and explain its sharp boundary geometry. Equation (6) does not contradict those results: it uses a different source category, one conjugate pair plus four independent real phase units, which first exists at cardinality six.

The phase-budget mechanism is transparent in the general formula. At height zero the conjugate pair contributes real amplitude `2`; moving it vertically changes that amplitude by order `y^2`. With three real anchors, the Montgomery--Taylor curvature minimum is not negative enough to defeat the positive self term because `2K_0+3k_*>0`. A fourth independent real phase unit crosses the exact curvature threshold, `2K_0+4k_*<0`. Thus the same curvature minimum that governs five-point near-extremizers becomes an actual descent direction as soon as one additional real anchor is available.

This also clarifies what should **not** be attempted next. Extending the five-point proof by stronger interval coverage, a sharper near-extremizer analysis, or another refinement of the same scalar coercive inequality cannot establish a general real-collapse theorem for larger multisets: the desired statement is already false for the base Montgomery--Taylor profile at six points. Any larger-configuration route must retain the full affine slack of the real collapse, exploit interactions among several vertical fibers, or introduce a genuinely richer ordered/matrix/higher-correlation carrier.

## 4. Affine-counting consequence and remaining gate

For the explicit witness (4)--(5),

\[
|W_y|=|R(W_y)|=6,
\qquad
s(W_y)=s(R(W_y))=4,
\tag{24}
\]

because the four rational anchors are distinct and nonzero, while the collapsed conjugate pair becomes a double point at zero. Consequently a universal affine inequality of the form

\[
s(Z)\ge A|Z|-tE_F(Z),\qquad t>0,
\tag{25}
\]

assigns a strictly larger right-hand side to `W_y` than to its real collapse whenever (6) holds. The six-point configuration is therefore a genuinely stronger deterministic test than the corresponding real multiset.

But the amount by which it is stronger is only `O(y^2)`, whereas the real multiset may have positive affine slack independent of `y`. Hence (6) is **not** itself a falsifier of the Montgomery--Taylor/Lamzouri certificate and is not yet a falsifier of the central-notch separator. The next decisive scalar question is quantitative: compare the six-point vertical descent against the exact affine margin of the collapsed six-point real configuration, and then against the finite-real gain and normalization slack of a narrow central-notch perturbation.

This distinction prevents an invalid leap from `energy decreases under vertical displacement` to `the universal counting inequality fails`. The durable conclusion here is narrower and still decisive: the completed five-point collapse/coercivity mechanism has a sharp cardinality boundary and cannot be the proof principle for the full universal complex-multiset problem.

## 5. Prior art and evidence boundary

A fresh audit checked the current Lamzouri Hilbert-space proof and the classical Carneiro--Chandee--Littmann--Milinovich Montgomery--Taylor extremal framework, together with the Fourier--Laplace positive-definite strip representation of Buescu--Paixão--Symeonides already recorded in `SOURCES.md`. Those sources provide the surrounding pair-correlation and positive-spectrum machinery, but the search did not locate a theorem giving this finite-cardinality real-collapse hierarchy or the six-point threshold (12)--(16). No publication-level novelty claim is made.

No new external theorem is load-bearing. The exact one-pair defect and uniform small-height expansion come from `ANF-037`; the fixed Montgomery--Taylor curvature transform and `K_0` enclosure come from `ANF-059`; and the unique minimizer, its certified value, and the global second-derivative bound come from `ANF-066`. Therefore `SOURCES.md` requires no change.

The computer-assisted evidence is confined to the already-canonical scalar curvature certificate. Equations (9)--(12), the rational-anchor Taylor argument, the simple-point comparison, and the cardinality interpretation are exact deductions. Ordinary numerical plots or optimization of `K` are unnecessary and would not support the claim.

## 6. Research consequence

The completed five-point program was not wasted by this reversal: it identifies the exact curvature minimum and supplies enough rigidity to make the first larger-cardinality failure almost algebraic. The frontier has now moved one level up. **Montgomery--Taylor is five-point stable but already infinitesimally non-collapse-dominant at six points.** The next useful question is no longer whether the scalar five-point defect can be made more coercive; it is whether the stronger six-point complex constraint actually consumes the affine margin of the Montgomery--Taylor or central-notch certificate, or whether that margin survives despite the energy reversal.

No statement here excludes every off-critical zero, improves a zero-density/proportion bound, or implies RH.