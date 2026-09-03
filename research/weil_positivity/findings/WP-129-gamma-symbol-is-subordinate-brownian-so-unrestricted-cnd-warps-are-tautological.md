# WP-129 — Gamma symbol is subordinate Brownian, so unrestricted CND warps are tautological

**Status:** `EXACT-DERIVED + GAMMA-COMPLETE-BERNSTEIN + SUBORDINATE-BROWNIAN + MATCHED-CONTROL + DECISIVE-CANONICALITY-NEGATIVE + PRIOR-ART-CLASSICALIZATION`.

`WP-117` identifies the Prime-Circle-selected Riemann Gamma variation

\[
H_\infty(t)=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\psi\!\left(\frac14\right)
\tag{1}
\]

as a genuine continuous conditionally negative-definite (CND) symbol. `WP-127` closes every Bernstein-subordinate Gamma heat filter with only polynomial high-frequency decay, and `WP-128` shows that positive power warps `H_\infty^\alpha` cross from Markov/CND to non-CND exactly when their heat cutoff becomes superpolynomial. `WP-128` deliberately leaves open a more subtle scalar warp that is mild at the Gamma origin but superlinear at large Gamma energy.

That logical escape is nonempty, but it exposes a stronger canonicality problem rather than a new Weil-positive mechanism. The exact digamma partial-fraction expansion shows that

\[
\boxed{H_\infty(t)=F(t^2)}
\tag{2}
\]

for an explicit **complete Bernstein function** `F`. Hence the Gamma jump process is itself a subordinate Brownian motion. Since `F` is strictly increasing from `[0,\infty)` onto `[0,\infty)`, one can de-subordinate it exactly:

\[
\boxed{F^{-1}(H_\infty(t))=t^2.}
\tag{3}
\]

The right side is the ordinary Brownian/Laplacian CND symbol, and its heat-dissipation multiplier `t^2 exp(-s t^2)` has Gaussian, hence superpolynomial, decay. More generally, for every `0<alpha<=2`,

\[
\Phi_\alpha(x):=[F^{-1}(x)]^{\alpha/2}
\tag{4}
\]

gives

\[
\boxed{\Phi_\alpha(H_\infty(t))=|t|^\alpha,}
\tag{5}
\]

the classical symmetric-stable CND symbols. Their heat-dissipation filters `|t|^alpha exp(-s |t|^alpha)` are superpolynomially decaying for every fixed `s>0`.

Thus **specific CND preservation does not force the polynomial-cutoff obstruction of `WP-127`/`WP-128` once arbitrary scalar warps are admitted**. The surviving scalar class is much larger than Bernstein subordination.

However, the same invertibility proves that this freedom is mathematically nonselective. Every continuous even target symbol `q` with `q(0)=0` can be written uniquely as a scalar warp of `H_\infty`:

\[
q(t)=\Phi_q(H_\infty(t)),
\qquad
\Phi_q(x):=q\!\left(\sqrt{F^{-1}(x)}\right).
\tag{6}
\]

In particular, every even CND symbol can be imported this way. Therefore the statement “find a scalar `Phi` such that `Phi(H_infty)` is CND and has a desired cutoff” has no remaining geometric content unless `Phi` is independently forced by Mathia before the target CND symbol or cutoff is chosen. The stable family (4) is a matched control showing the failure sharply: it restores a valid independent Markov sign theorem and escapes the known high-frequency obstruction, but it does so by **undoing the Gamma subordination and replacing the Gamma geometry by ordinary Euclidean/stable geometry**.

This finding does not rule out a scalar warp genuinely forced by Prime Circle, Prime Flute, Prime Lattice, a boundary construction, or a finite--archimedean coupling. It changes the proof obligation. CND of the final warped symbol is no longer evidence that the positivity came from the Gamma construction; the warp itself must carry an independent canonical derivation that survives matched non-arithmetic digamma controls. No global Weil form, finite-prime selector, polar term, or RH consequence is obtained here.

## 1. Exact partial fractions put the Gamma symbol in subordinate-Brownian form

For `a>0`, the classical digamma series (NIST DLMF §5.7(ii), Eq. 5.7.6) gives

\[
\psi(z)=-\gamma+\sum_{n=0}^\infty\left(\frac1{n+1}-\frac1{n+z}\right).
\tag{7}
\]

Put `r_n=n+a`. For real `u`, subtract the value at `a` and take real parts:

\[
\begin{aligned}
h_a(u)
&:=\operatorname{Re}\psi(a+iu)-\psi(a)\\
&=\sum_{n=0}^\infty\left(\frac1{r_n}-\frac{r_n}{r_n^2+u^2}\right)\\
&=\boxed{\sum_{n=0}^\infty\frac{u^2}{r_n(r_n^2+u^2)}}.
\end{aligned}
\tag{8}
\]

Define, for `lambda>=0`,

\[
F_a(\lambda):=\sum_{n=0}^\infty\frac{\lambda}{r_n(r_n^2+\lambda)}.
\tag{9}
\]

Then `h_a(u)=F_a(u^2)`. Moreover (9) is already the standard complete-Bernstein/Stieltjes representation

\[
F_a(\lambda)=\int_{(0,\infty)}\frac{\lambda}{\lambda+r}\,\rho_a(dr),
\qquad
\rho_a:=\sum_{n=0}^\infty\frac1{r_n}\,\delta_{r_n^2},
\tag{10}
\]

because

\[
\int\frac{1}{1+r}\,\rho_a(dr)=\sum_{n=0}^\infty\frac1{r_n(1+r_n^2)}<\infty.
\tag{11}
\]

Hence `F_a` is a complete Bernstein function. In the standard probabilistic normalization, a Lévy exponent of the form `F_a(|xi|^2)` is exactly the exponent of Brownian motion subordinated by the subordinator with Laplace exponent `F_a`. This is classical complete-Bernstein/subordinate-Brownian theory; the branch-specific observation is that the exact digamma symbol selected in `WP-117` lies in this class with an elementary atomic Stieltjes measure.

For the Riemann normalization (1), `a=1/4` and `u=t/2`. Absorb the factor `1/4` into

\[
F(\lambda):=F_{1/4}(\lambda/4)
=\sum_{n=0}^\infty\frac{\lambda}{r_n(4r_n^2+\lambda)},
\qquad r_n=n+\frac14.
\tag{12}
\]

Then (2) follows exactly, and the Stieltjes measure is

\[
\rho=\sum_{n=0}^\infty\frac1{r_n}\,\delta_{4r_n^2}.
\tag{13}
\]

So `F` is complete Bernstein. This refines `WP-117`: the positive Gamma jump energy is not merely some symmetric Lévy form; it is a **subordinate Euclidean Dirichlet form**.

## 2. The Gamma dispersion is an invertible radial coordinate

Every term in (12) has positive derivative:

\[
\frac{d}{d\lambda}\frac{\lambda}{r_n(4r_n^2+\lambda)}
=\frac{4r_n}{(4r_n^2+\lambda)^2}>0.
\tag{14}
\]

Therefore `F` is strictly increasing. Also `F(0)=0`, while the ordinary digamma asymptotic used in `WP-117` gives

\[
F(\lambda)=H_\infty(\sqrt\lambda)
=\frac12\log\lambda-\log2-\psi\!\left(\frac14\right)+o(1)
\qquad(\lambda\to\infty).
\tag{15}
\]

Thus `F(lambda)->infinity`, and `F:[0,infinity)->[0,infinity)` is a continuous strictly increasing bijection. Consequently `F^{-1}` is globally well-defined and (3) is an identity, not an asymptotic construction.

The warp has exactly the endpoint behavior needed to evade the boundary left by `WP-128`. From its Taylor coefficient,

\[
H_\infty(t)=\frac{\zeta(3,1/4)}4t^2+O(t^4),
\tag{16}
\]

so

\[
F^{-1}(x)=\frac4{\zeta(3,1/4)}x+O(x^2)
\qquad(x\downarrow0).
\tag{17}
\]

At the other endpoint, inversion of (15) gives

\[
\boxed{F^{-1}(x)=4e^{2\psi(1/4)}e^{2x}(1+o(1))}
\qquad(x\to\infty).
\tag{18}
\]

Thus the exact de-subordination warp is linear at zero but exponentially superlinear at infinity. It is not a Bernstein function: Bernstein functions are increasing and concave and hence grow at most linearly. There is therefore no conflict with `WP-127`; (3) is not further Bochner subordination of the Gamma process but reversal of the existing subordination for this specific symbol.

## 3. Stable Markov controls cross the superpolynomial cutoff boundary

For every `0<alpha<=2`, the classical Schoenberg/Lévy theorem says that `q_alpha(t)=|t|^alpha` is CND on `R`. Equation (5) therefore gives a whole family of symbol-specific Gamma warps whose final generators are Markov-positive. For every fixed `s>0` and every `N>0`,

\[
|t|^N |t|^\alpha e^{-s|t|^\alpha}\longrightarrow0
\qquad(|t|\to\infty).
\tag{19}
\]

These multipliers lie outside the polynomial-lower-tail hypothesis of `WP-126`. They also vanish at `t=0`, so they do not trigger the nondegenerate low-frequency hypotheses of `WP-113`/`WP-114`.

This is a genuine matched control on those obstruction theorems. They did not prove that a Markov-positive superpolynomial filter is impossible. They proved that the **intrinsic Gamma Markov functional calculi investigated there** do not supply one. The present stable family shows that a specifically tailored CND warp can.

For completeness, (17)--(18) give

\[
\Phi_\alpha(x)\sim\left(\frac4{\zeta(3,1/4)}\right)^{\alpha/2}x^{\alpha/2}
\qquad(x\downarrow0)
\tag{20}
\]

and

\[
\Phi_\alpha(x)\sim2^\alpha e^{\alpha\psi(1/4)}e^{\alpha x}
\qquad(x\to\infty).
\tag{21}
\]

None of these warps is Bernstein globally, despite the fact that the **specific compositions** (5) are CND. This sharply separates universal CND-preserving functional calculus from symbol-specific reparameterization.

The `alpha=2` case is especially transparent: `H_infty` is first mapped by `F^{-1}` to `t^2`, and the independent sign theorem at the end is simply the standard Euclidean Dirichlet/Brownian theorem.

## 4. Unrestricted scalar warp search is universal

The stable family is not an isolated trick. Since (2) makes `H_\infty(t)=F(t^2)` a one-to-one coordinate on `|t|`, let `q:R->R` be any continuous even function with `q(0)=0`. Define

\[
\boxed{\Phi_q(x):=q\!\left(\sqrt{F^{-1}(x)}\right).}
\tag{22}
\]

Then for every real `t`,

\[
\boxed{\Phi_q(H_\infty(t))=q(t).}
\tag{23}
\]

In particular, if `q` is even CND, then `Phi_q o H_infty` is CND, but that implication is tautological because the composition equals the chosen `q` identically.

This gives a decisive canonicality test for the remaining scalar route. If admissible warps may depend arbitrarily on the inverse Gamma dispersion, then **every desired even CND geometry can be presented as a “Gamma warp.”** CND, heat-semigroup positivity, stable-process provenance, or a desired high-frequency cutoff of the final symbol can therefore no longer distinguish a Mathia-derived mechanism from an imported positive kernel.

The same argument applies to every `a>0` in (8)--(10): each `F_a` is strictly increasing and unbounded, so every digamma member `h_a` can be de-subordinated and reparameterized to the same Brownian/stable controls. This is a strong matched non-arithmetic test. The reparameterization freedom is not special to the Prime-Circle-selected Riemann value `a=1/4`.

## 5. Aggressive falsification of the apparent positive escape

**The Gamma term has been replaced, not explained.** The Weil archimedean structure singled out by Prime Circle is `H_infty`. After applying `F^{-1}`, the sign theorem belongs to `t^2` or `|t|^alpha`, a universal Euclidean/stable symbol. Nothing here says that positivity of the new symbol yields positivity of the original Gamma contribution or of the assembled Weil functional.

**The warp is target-reconstructible from any desired symbol.** Equation (22) means that choosing `F^{-1}` because it gives Brownian motion is mathematically equivalent to choosing Brownian motion first and solving for the scalar reparameterization. That fails the branch's anti-hand-picking control unless some independent Mathia construction produces `F^{-1}` or the target Euclidean/stable generator before its useful cutoff/sign behavior is consulted.

**The finite places and global counterterms are absent.** No Mangoldt selector, mixed-prime completion, polar term, or finite--archimedean coupling is produced. The stable filter merely falls outside the hypotheses of `WP-126`; it is not proved to have finite cylindrical energy on the surviving correlated completions, much less to reproduce the explicit formula.

**The result does not contradict the previous no-go theorems.** `WP-127` assumes Bernstein subordination of `H_infty`, while `F^{-1}` is not Bernstein. `WP-128` treats the special power family `H_infty^alpha`, whereas (4) is an inverse-dispersion warp. `WP-126` explicitly leaves superpolynomial multipliers outside its theorem. The present calculation fills that logical gap with a matched control rather than invalidating those findings.

**A legitimate possibility remains, but its burden is higher.** If Prime Circle or another Mathia structure independently produces the Euclidean Laplacian, a stable generator, or an inverse-subordination operation and then forces its coupling to the finite arithmetic sector, that would be additional structure rather than the tautological construction (22). Such a mechanism must be derived without using the desired CND target, cutoff, or Weil coefficients to define the warp.

## 6. Prior-art and novelty audit

The ingredients are classical and no theorem-level historical novelty is claimed.

- NIST DLMF §5.7(ii), Eq. 5.7.6 (`https://dlmf.nist.gov/5.7.E6`) supplies the digamma partial-fraction series from which (8) follows immediately.
- René L. Schilling, Renming Song, and Zoran Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), is the standard reference for the complete-Bernstein representation and Bochner-subordination machinery used in (10).
- Mateusz Kwaśnicki, *Spectral analysis of subordinate Brownian motions on the half-line*, Studia Mathematica 206 (2011), 211--271, DOI `10.4064/sm206-3-2`, uses the standard class of Lévy exponents `psi(xi^2)` with `psi` complete Bernstein and provides a direct neighboring probabilistic comparison.
- The fact that `|t|^alpha` is CND for `0<alpha<=2` is the classical symmetric-stable/Schoenberg example already covered by standard Lévy--Khintchine theory.

A bounded structural search for the exact special-function statement `Re psi(a+iu)-psi(a)=F_a(u^2)` framed as a complete-Bernstein subordinate-Brownian exponent did not expose a direct theorem needed here. That absence is not treated as historical novelty: once DLMF 5.7.6 is written in the form (8), the complete-Bernstein representation (10) is immediate.

The Mathia-specific content is therefore the **research-boundary consequence**: the precise Gamma symbol already selected by `WP-117` is invertibly subordinate Brownian, so arbitrary symbol-specific CND warping is universal and cannot itself count as an intrinsic geometric explanation of Weil positivity.

## 7. Consequence for the Weil-positivity search

`WP-127` proves that universal sign-preserving **Bernstein subordination** of the Gamma generator cannot sharpen its logarithmic high-frequency growth enough. `WP-128` proves that the obvious **positive power warps** cross the CND boundary exactly when their cutoff becomes superpolynomial. The present finding shows that **arbitrary symbol-specific CND warps do exist**, even with Gaussian or stable superpolynomial heat cutoffs, but that allowing them makes the search tautological because `H_infty` is an invertible radial coordinate.

Accordingly, a future scalar warp is research-relevant only if its definition is independently forced by Mathia and survives the generic `a>0` digamma control. Merely exhibiting `Phi(H_infty)` as CND with a rapidly decaying positive heat filter is no longer sufficient evidence of a Gamma-native mechanism.

The substantive global frontier remains the one identified by the line mandate: a nonseparable finite--archimedean geometry, boundary/intersection/cohomological form, or other canonical construction whose **own** positivity theorem simultaneously retains the arithmetic prime structure, the Riemann archimedean/global counterterms, and the exact Weil local-to-global decomposition. The de-subordination control shows why additional geometric structure, rather than more unconstrained scalar functional calculus, is required.
