# NB-223 — Near-edge zero density gives a constant Euler gap within every log-epsilon of Ford scale

**Date:** 2026-09-19  
**Status:** `LITERATURE+DERIVED + ZETA-SPECIFIC + EXPLICIT-FORMULA + NEAR-ONE-ZERO-DENSITY + POSITIVE-EULER + CONSTANT-GAP + NEAR-FORD-SCALE + NB-212/NB-222-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-221` reduced every fixed-depth soft primitive route to the same moving-shell convolution with `P_0=-zeta'/zeta`, and `NB-222` proved that strip analyticity alone cannot improve its `exp(-X eta)` contour gain. The first useful escape therefore has to exploit structure of the actual zeta logarithmic derivative.

Bellotti's 2026 near-one zero-density theorem supplies such structure. Moving a compact smooth logarithmic shell globally across `P_0` turns the carrier into an absolutely weighted sum over zeta zeros. Bellotti bounds the population in every near-one layer of depth `K/R`, with `R=(log T)^(2/3)(log log T)^(1/3)`, by `exp(B(log log T)^alpha)K` whenever `K << (log log T)^alpha` and `alpha<1`. A finite layer decomposition then shows that **any fixed positive power of `log log |t|` in the carrier budget `X/R` beats the entire zero-residue sum**.

Consequently, for every fixed `epsilon>0` and `kappa>0`, a fixed smooth positive Euler shell has `o(1)` twisted barycenter uniformly up to

\[
\log |t|
\le
\kappa\frac{X^{3/2}}{(\log X)^{1/2+\epsilon}}.
\]

Thus the order-one positive-return gap of `NB-212` extends from its previous `(log X)^(-2)` corridor to every fixed logarithmic margin below the Ford denominator `(log X)^(-1/2)`. The exact endpoint `epsilon=0` remains open: Bellotti's moving density theorem stops at every fixed exponent `alpha<1`, while the final endpoint layer is of order `log log T`.

## 1. The smooth carrier is an explicit weighted zero sum

Fix `r>0`, `Delta>0`, and `phi in C_c^infinity((0,Delta))`. Put

\[
\sigma_X=1+\frac rX,
\qquad
h_X(u)=\phi(u-X),
\]

and

\[
S_X(t)
:=
\sum_{n\ge2}\Lambda(n)h_X(\log n)n^{-\sigma_X-it}.
\tag{1}
\]

With

\[
L_X(v)
:=
\int h_X(u)e^{ivu}\,du
=
e^{iXv}\Phi(v),
\qquad
\Phi(v)=\int_0^\Delta\phi(y)e^{ivy}\,dy,
\tag{2}
\]

Fourier inversion on `Re(s)>1` gives

\[
\boxed{
S_X(t)
=
\frac1{2\pi}\int_{\mathbb R}
L_X(v)
\left(-\frac{\zeta'}{\zeta}\right)
(\sigma_X+i(t+v))\,dv.
}
\tag{3}
\]

This is the unwindowed leading carrier isolated in `NB-221`. Since `Phi` is Schwartz, shift the whole `v`-line upward to `Im(v)=sigma_X+1`; the zeta argument on the new line has real part `-1`. The functional equation gives

\[
\frac{\zeta'}{\zeta}(-1+i\tau)
\ll\log(3+|\tau|),
\]

while the shell carrier contributes `exp(-X(sigma_X+1))`, so the new horizontal integral is exponentially small in `X` in the coupled ranges below.

The zeta pole at `1` is crossed at horizontal coordinate `-t`; its residue is `O_A(|t|^(-A))` for every `A`, because `Phi` is Schwartz. The first trivial zero at `-2` is not crossed. A nontrivial zero `rho=beta+i gamma`, counted with its true multiplicity, is crossed at

\[
v_\rho=(\gamma-t)+i(\sigma_X-\beta).
\]

Repeated integration by parts in the fixed profile gives, for every fixed `A`,

\[
|L_X(v_\rho)|
\ll_A
 e^{-X(\sigma_X-\beta)}
(1+|\gamma-t|)^{-A}.
\]

Since `X(sigma_X-beta)=r+X(1-beta)`, the residue theorem yields

\[
\boxed{
|S_X(t)|
\ll_A
\sum_\rho m(\rho)e^{-X(1-\beta)}
(1+|\gamma-t|)^{-A}
+O_A(|t|^{-A})
+O(e^{-cX}(1+\log |t|)).
}
\tag{4}
\]

The same estimate holds for negative `t` by conjugation. Equation (4) is the arithmetic information absent from the matched `H^infinity` class of `NB-222`: the actual carrier is controlled by a discrete zero spectrum, not by an arbitrary bounded analytic function.

## 2. A finite Bellotti layering kills the near-one residues

Write

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR.
\tag{5}
\]

Bellotti's Theorem 1.1 says that for fixed `alpha<1`, if

\[
K(T)\ll(\log\log T)^\alpha
\]

and

\[
\sigma\ge
1-\frac{K(T)}{(\log T)^{2/3}(\log\log T)^{1/3}},
\]

then

\[
N(\sigma,T)
\ll
\exp\!\bigl(B(\log\log T)^\alpha\bigr)K(T).
\tag{6}
\]

Her Theorem 1.2 also gives `N(sigma,T)=O_A(1)` in every fixed-width layer `sigma >= 1-A/R` with fixed `A>A_0`, where `A_0` is the Vinogradov--Korobov zero-free constant.

Assume now that for some fixed `d>0`

\[
\boxed{Y\ge L^d.}
\tag{7}
\]

It suffices to take `0<d<1`, since a stronger hypothesis implies one with a smaller positive exponent. Ordinary explicit zero counting, already anchored through Bellotti--Wong--Fiori, gives

\[
N(U+1)-N(U)=O(\log(3+U)).
\tag{8}
\]

Hence for `A>3`, the vertically weighted number of zeros around height `t` is `O(Q)`, and zeros with `|gamma-t|` comparable with `|t|` are negligible in (4). We may therefore bound the delicate part using Bellotti with height `2|t|`, which changes `Q,L,R` only by `1+o(1)` factors.

The zero-free region first excludes `1-beta<c_0/R`. Bellotti's fixed-width theorem then leaves only `O(1)` zeros with

\[
1-\beta\le\frac{A_1}{R}
\]

for any fixed `A_1>A_0`; their total residue mass is `O(exp(-c_0Y))=o(1)`.

For the rest choose a finite partition

\[
0=u_0<u_1<\cdots<u_J=1-\frac d2
\tag{9}
\]

whose gaps are all less than `d/4`. Consider the layer

\[
\frac{L^{u_{j-1}}}{R}
\lesssim 1-\beta
<\frac{L^{u_j}}{R},
\tag{10}
\]

with the fixed initial constant absorbed into the first layer. Each zero in it has weight at most

\[
\exp(-Y L^{u_{j-1}})
\le
\exp(-L^{d+u_{j-1}}).
\tag{11}
\]

At the upper edge apply (6) with the fixed exponent

\[
\alpha_j=u_j+\frac d4<1.
\]

The layer population is at most

\[
L^{u_j}\exp(B_jL^{\alpha_j}).
\tag{12}
\]

Because `u_j-u_(j-1)<d/4`,

\[
\alpha_j
< u_{j-1}+\frac d2
< u_{j-1}+d,
\]

so the decay in (11) dominates (12). Each of the finitely many layers contributes `o(1)`.

Finally, zeros deeper than `L^(u_J)/R` have total contribution at most

\[
O(Q)\exp(-Y L^{u_J})
\le
\exp\!\left(L-L^{1+d/2}\right)
=o(1),
\tag{13}
\]

using (8). Substitution into (4) proves the intrinsic carrier theorem

\[
\boxed{
\frac{X}{Q^{2/3}(\log Q)^{1/3}}
\ge (\log Q)^d
\quad\Longrightarrow\quad
S_X(t)=o(1)
}
\tag{14}
\]

for every fixed `d>0` in the coupled high-ordinate limit.

## 3. This reaches every `log^epsilon` margin below Ford height

Fix `epsilon>0` and `kappa>0`, and suppose

\[
Q
\le
\kappa\frac{X^{3/2}}{(\log X)^{1/2+\epsilon}}.
\tag{15}
\]

Then

\[
\frac XR
\ge
c_\kappa
\frac{(\log X)^{1/3+2\epsilon/3}}
{(\log Q)^{1/3}}.
\]

Since (15) implies `log Q <= (3/2+o(1))log X`, we get

\[
\frac XR
\ge
c_{\kappa,\epsilon}(\log Q)^{2\epsilon/3}.
\tag{16}
\]

For large `Q`, this dominates `(log Q)^(epsilon/2)`, so (14) gives

\[
\boxed{
S_X(t)=o(1)
\quad\text{uniformly for}\quad
\log(10+|t|)
\le
\kappa\frac{X^{3/2}}{(\log X)^{1/2+\epsilon}},
}
\tag{17}
\]

apart from bounded ordinates, which are handled directly by the fixed Fourier transform and the prime number theorem.

This is exactly where the arithmetic zero-density input improves `NB-221`. The pointwise contour estimate there was

\[
Q^2\exp(-cX/R),
\]

so it needed `X/R` of order `log Q`, producing the `(log X)^2` denominator of `NB-212`. The residue decomposition replaces that polynomial pointwise tariff by finitely many sublogarithmic zero populations and therefore needs only **some positive power** of `log Q`.

At the formal Ford scale

\[
Q\asymp\frac{X^{3/2}}{(\log X)^{1/2}},
\tag{18}
\]

we have only `X/R=Theta(1)`. The proof then fails for a structural reason: Bellotti permits `K(T)` up to every fixed power `(log log T)^alpha`, `alpha<1`, but the untreated tail still has generic local mass `Q=e^L`. An `exp(-O(L^alpha))` horizontal weight cannot beat that final `e^L` cost. Thus (17) is deliberately **not** an endpoint theorem.

## 4. Positive Euler returns inherit an order-one gap

Take `phi>=0`, nonzero. The prime number theorem gives

\[
S_X(0)
\longrightarrow
m_\phi
:=e^{-r}\int_0^\Delta\phi(y)\,dy
>0.
\tag{19}
\]

For every fixed nonzero bounded `t`, the same argument gives

\[
S_X(t)
=
e^{-itX}e^{-r}
\int_0^\Delta\phi(y)e^{-ity}\,dy+o(1),
\tag{20}
\]

whose modulus is uniformly smaller than `m_phi` on every compact set `1<=|t|<=T_0`. For ordinates tending to infinity in (15), (17) is stronger: `S_X(t)=o(1)`.

The positive-return defect used in `NB-194`--`NB-212` satisfies the elementary implication that a small defect forces `Re S_X(t)` close to `S_X(0)`. Combining that implication with (17)--(20) yields a constant `eta_phi>0` such that for all sufficiently large `X`,

\[
\boxed{
\mathcal A_X(t)\ge\eta_\phi
\qquad
\left(
1\le |t|
\le
\exp\!\left[
\kappa\frac{X^{3/2}}{(\log X)^{1/2+\epsilon}}
\right]
\right).
}
\tag{21}
\]

Therefore the constant-gap result of `NB-212` reaches every fixed `log^epsilon` margin below the Ford height. `NB-205` still reaches the exact Ford scale, but only with a vanishing `1/X`-scale discrepancy gap. The two mechanisms now meet much more tightly.

This remains a source-side theorem. It does not imply a quantitative Nyman--Beurling distance bound, and it does not prove that every good Nyman approximant must realize this Euler return observable.

## 5. Adversarial checks and prior-art boundary

The global contour deliberately crosses the nontrivial zeros; it does not assume a fictitious global zero-free strip. Smoothness supplies the factor `(1+|gamma-t|)^(-A)`, and explicit local zero counting controls the remote residue tail. Multiplicity is harmless because both the residue sum and `N(sigma,T)` count true multiplicity. The pole at `1` occurs at horizontal coordinate `-t`, where the shell transform is rapidly decaying, and the shift stops before the first trivial zero at `-2`.

No pointwise `Q^2` bound for `P_0` is used in the main term. Pointwise control is used only on the fixed top line `Re(s)=-1`, after the carrier has already paid an exponential `e^{-cX}` factor. The improvement over `NB-221` therefore comes from the actual zeta zero spectrum rather than from repackaging the same strip estimate.

The load-bearing modern input is Chiara Bellotti, *A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem*, Bull. London Math. Soc. 58 (2026), e70442, DOI `10.1112/blms.70442`, arXiv:2508.02041. Theorem 1.1 supplies (6), and Theorem 1.2 controls the fixed layer adjacent to the Vinogradov--Korobov edge. The paper is already anchored in `SOURCES.md`, so no new source dependency is needed. The explicit-formula contour itself is classical; no novelty is claimed for that mechanism.

A targeted audit did not locate the specific combination of Bellotti's moving near-one density estimate with a Nyman-line moving smooth Euler shell. The line-local delta is the finite horizontal-layer optimization proving (14), its inversion to the near-Ford corridor (17), and the resulting order-one positive-return gap (21).

The representation audit separates the generic and arithmetic pieces. Smooth compact logarithmic support generically supplies the vertical Schwartz weight and the factor `e^{-X(1-beta)}`. The decisive fact that only sublogarithmically many singularities can occupy each layer `1-beta~K/R` is zeta-specific. Replacing the zeta zeros by an arbitrary meromorphic spectrum satisfying only the strip envelope of `NB-222` restores its matched extremizer and destroys the improvement.

## Route consequence

`NB-222` established a genuine analytic ceiling; `NB-223` supplies the first direct arithmetic escape on that exact carrier. The positive Euler branch now has an order-one obstruction throughout every fixed `log^epsilon` sub-Ford margin.

The next source-side target is correspondingly precise. At the exact Ford scale `X/R=Theta(1)`, one must either control the final near-one layers at depth comparable with `log log t` or exploit cancellation among their residue phases instead of only their count. For the signed/complex route, (4) points to the same object without absolute values: a phase-sensitive weighted zero sum. Either step would use information strictly beyond the finite-layer density input proved here.