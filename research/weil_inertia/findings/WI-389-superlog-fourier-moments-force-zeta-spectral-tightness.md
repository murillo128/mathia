# WI-389 — Superlog Fourier moments force zeta-spectral tightness, while log-order moments do not

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-387 identified uniform zeta-frequency spectral tightness as the coefficient-independent compactness hypothesis that makes the fixed-width recurrence obstruction survive arbitrary endpoint-dependent profile changes. WI-388 then showed that a uniform negative archimedean budget does not imply that tightness: an `L^2` sideband mass of order `1/log R` can escape to frequency `R` at only `O(1)` archimedean cost and still carry `Omega(1)` mass on a suitable packet of zeta ordinates.

There is an exact scalar-moment boundary behind those two results.

Fix `L>0`. For any

\[
g\in L^2(\mathbb R),\qquad
\operatorname{supp}g\subset[-L/2,L/2],
\tag{1}
\]

write

\[
F_g(\xi)=\int_{\mathbb R}g(s)e^{i\xi s}\,ds.
\tag{2}
\]

Let the nontrivial zeta zeros be written `rho=beta+i gamma`, counted with multiplicity, and let the sampling measure on ordinates be

\[
\mu_\zeta=\sum_\rho \delta_\gamma.
\tag{3}
\]

Then there are constants `C_L` and, for every `M>0`, `C_{L,M}` such that for all `T>=2`,

\[
\boxed{
\sum_{|\gamma|>T}|F_g(\gamma)|^2
\le
C_L\int_{|\xi|>T/2}
\log(2+|\xi|)|F_g(\xi)|^2\,d\xi
+
C_{L,M}T^{-M}\|F_g\|_2^2.
}
\tag{4}
\]

The sum in (4) counts zero multiplicity. The estimate itself is unconditional; it uses only fixed exponential type and the classical Riemann--von Mangoldt local zero count.

Consequently, for a normalized fixed-width family `g_k`,

\[
\lim_{T\to\infty}
\sup_k
\int_{|\xi|>T}
\log(2+|\xi|)|F_{g_k}(\xi)|^2\,d\xi=0
\tag{5}
\]

implies

\[
\boxed{
\lim_{T\to\infty}
\sup_k
\sum_{|\gamma|>T}|F_{g_k}(\gamma)|^2=0.
}
\tag{6}
\]

Under RH, (6) is exactly the zeta-spectral tightness hypothesis used in WI-387. Hence the **unperforated** fixed-width recurrence theorem of WI-387 applies to every family satisfying (5): arbitrary endpoint-dependent changes of profile still cannot open a uniform positive Weil spectral floor.

A convenient sufficient condition is any uniformly bounded Fourier moment whose weight grows strictly faster than logarithmically. If `w:[0,infinity)->(0,infinity)` satisfies

\[
\eta_w(T)
:=
\sup_{r\ge T}
\frac{\log(2+r)}{w(r)}
\longrightarrow0,
\tag{7}
\]

and

\[
\sup_k
\int_{\mathbb R}w(|\xi|)|F_{g_k}(\xi)|^2\,d\xi<\infty,
\tag{8}
\]

then (5)--(6) follow. In particular a uniform `(log(2+|xi|))^(1+delta)` moment for any fixed `delta>0` suffices. So does a uniform `H^s` bound for **any** `s>0`; the `H^1` hypothesis in WI-387 is much stronger than necessary for the spectral-tightness half of that theorem.

The growth threshold is sharp inside this natural class of one-weight scalar moment hypotheses. The WI-388 sideband family can be chosen so that

\[
\sup_R
\int_{\mathbb R}
\log(2+|\xi|)|F_{g_R}(\xi)|^2\,d\xi<\infty,
\tag{9}
\]

while its zeta-sampled tails are not uniformly tight. More generally the same countermodel has uniformly bounded `w`-moment for every `w(r)=O(log(2+r))`. Thus no implication of the form

\[
\sup_k\int w(|\xi|)|F_{g_k}(\xi)|^2<\infty
\quad\Longrightarrow\quad
\text{uniform zeta-spectral tightness}
\tag{10}
\]

can hold for all fixed-width families when `w=O(log)`. Within scalar moment-growth controls, the dividing line is therefore:

- **superlogarithmic growth:** sufficient for tightness;
- **logarithmic growth or less:** insufficient in general.

This is a structural route-pruning result. It does not prove RH or improve the simple-critical-zero proportion. It says that any fixed-width adaptive-profile attempt to evade WI-387 through high-frequency escape must spend at least the logarithmic spectral resource already realized by WI-388; merely replacing bounded `H^1` by a softer but still superlogarithmic scalar moment cannot help.

There is one important boundary. WI-387 used the `H^1` hypothesis not only to prove spectral tightness but also to make the source-slot perforation transfer uniform over the whole adaptive family. The present superlogarithmic Fourier condition replaces `H^1` only in the **spectral recurrence** step. By itself it does not prove that exact source perforation is uniformly negligible. A source-exact no-go theorem under this weaker condition still needs an independent uniform source-transfer estimate. WI-388 shows only diagonal compatibility with exact source slots, not such a uniform estimate.

## 1. Fixed support gives a Schwartz reproducing kernel

Choose

\[
\theta\in C_c^\infty(\mathbb R),
\qquad
\theta(s)=1
\quad (|s|\le L/2).
\tag{11}
\]

Since `g=theta g`, Fourier transformation gives

\[
F_g=K*F_g,
\tag{12}
\]

where `K` is a fixed Schwartz function depending only on `L` and on the Fourier convention. Its normalization is immaterial below.

Cauchy--Schwarz with the measure `|K(xi-y)|dy` gives

\[
|F_g(x)|^2
\le
\|K\|_1
\int_{\mathbb R}|K(x-y)|\,|F_g(y)|^2\,dy.
\tag{13}
\]

This is the only Paley--Wiener input needed. No zero spacing, RH, or zeta-specific Fourier identity enters here.

## 2. Riemann--von Mangoldt turns ordinate sampling into a logarithmic weight

The classical Riemann--von Mangoldt formula implies the unit-interval bound

\[
\mu_\zeta([n,n+1])\ll\log(2+|n|).
\tag{14}
\]

For `T>=2`, put

\[
Q_T(y)
=
\sum_{|\gamma|>T}|K(\gamma-y)|.
\tag{15}
\]

Because `K` is Schwartz, grouping the ordinates into unit intervals and using (14) yields

\[
Q_T(y)\le Q_0(y)
\ll_L \log(2+|y|).
\tag{16}
\]

There is also rapid off-diagonal decay. If `|y|<=T/2`, every sampled ordinate in (15) is at distance at least `T/2` from `y`. Taking an arbitrarily high Schwartz decay power and summing the unit-interval majorants gives, for every `M>0`,

\[
\boxed{
Q_T(y)\ll_{L,M}T^{-M}
\qquad(|y|\le T/2).
}
\tag{17}
\]

Summing (13) over `|gamma|>T`, applying Tonelli, and splitting the `y`-integral at `T/2` now gives

\[
\begin{aligned}
\sum_{|\gamma|>T}|F_g(\gamma)|^2
&\le
\|K\|_1
\int |F_g(y)|^2Q_T(y)\,dy\\
&\le
C_L\int_{|y|>T/2}\log(2+|y|)|F_g(y)|^2\,dy
+
C_{L,M}T^{-M}\|F_g\|_2^2,
\end{aligned}
\tag{18}
\]

which is (4).

The logarithm in (18) has a transparent origin: it is exactly the local sampling intensity of zeta ordinates. The proof is a weighted Plancherel--Polya/Carleson-embedding argument specialized to a sampling measure whose mass in a unit interval grows like `log |gamma|`.

## 3. Uniform logarithmic integrability is the intrinsic recurrence-side compactness

Suppose `\|g_k\|_2=1` and (5) holds. By Plancherel the last term in (18) is uniformly `O(T^{-M})`, while the first tends uniformly to zero after replacing `T` by `T/2`. This proves (6).

Under RH, every nontrivial zero is `1/2+i gamma`, so the nonnegative spectral representation used in WI-387 is

\[
\mathcal W[f_k^0]
=
4\sum_\gamma
|F_{g_k}(\gamma)|^2
\sin^2\!\left(\frac{\gamma A_k}{2}\right),
\tag{19}
\]

with multiplicity included. WI-387's coefficient-independent recurrence argument needs only a finite low-frequency head plus a uniformly negligible high-frequency tail. Equation (6) supplies exactly that tail condition. Therefore (5), not an `H^1` bound itself, is enough for the spectral recurrence part of WI-387.

This sharpens the meaning of "spectrally tight" in that finding. A fixed-width family need not have any pointwise `1/|gamma|` Fourier decay. It is enough that its continuous Fourier energy be uniformly integrable against the local zeta sampling density `log(2+|xi|)`.

## 4. Every superlogarithmic moment closes the tail

Assume (7)--(8), with the common bound in (8) denoted by `C_w`. Then

\[
\int_{|\xi|>T}
\log(2+|\xi|)|F_{g_k}(\xi)|^2\,d\xi
\le
\eta_w(T)
\int w(|\xi|)|F_{g_k}(\xi)|^2\,d\xi
\le
C_w\eta_w(T).
\tag{20}
\]

Taking the supremum over `k` proves (5). For example

\[
w(r)=\log^{1+\delta}(2+r),
\qquad\delta>0,
\tag{21}
\]

works. Polynomial Sobolev weights `(1+r^2)^s` dominate every logarithm, so any uniform positive Sobolev regularity `H^s`, however small `s>0`, also works.

This is substantially weaker than the direct WI-387 estimate

\[
|F_{g_k}(\gamma)|\ll |\gamma|^{-1}
\tag{22}
\]

coming from uniform `H^1`. The price is that (20) is an integrated compactness statement rather than pointwise decay.

## 5. WI-388 saturates the logarithmic moment scale

It remains to show that the logarithm in this route is not a proof artifact that can simply be replaced by a bounded logarithmic moment.

Use the WI-388 construction

\[
g_R
=
\sqrt{1-\varepsilon_R}\,\phi
+
\sqrt{\varepsilon_R}\,\nu_R,
\qquad
\varepsilon_R=\frac c{\log R},
\tag{23}
\]

where `phi` is a fixed smooth compactly supported base profile and `nu_R` is the normalized orthogonalized modulation of `phi(s)cos(Rs)`. Let `Phi` and `U_R` be their Fourier transforms. Since `Phi` is Schwartz, translation of the two sidebands gives

\[
\int
\log(2+|\xi|)|U_R(\xi)|^2\,d\xi
\ll_{\phi,L}1+\log R.
\tag{24}
\]

Indeed, after shifting `xi=eta+/-R`, use

\[
\log(2+|\eta\pm R|)
\ll
1+\log(2+R)+\log(2+|\eta|),
\tag{25}
\]

and the rapid decay of `Phi`; the vanishing orthogonalization coefficient in WI-388 changes only the constant.

From `|a+b|^2<=2|a|^2+2|b|^2`, (23)--(24) give

\[
\int
\log(2+|\xi|)|F_{g_R}(\xi)|^2\,d\xi
\ll
1+\varepsilon_R\log R
\ll1.
\tag{26}
\]

Yet WI-388 constructs `R_j->infinity` for which a fixed-width packet near `R_j` carries

\[
\sum_{\gamma\in[R_j-\delta,R_j+\delta]}
|F_{g_{R_j}}(\gamma)|^2
\ge\kappa>0.
\tag{27}
\]

Thus (26) does not imply uniform integrability of the logarithmic moment tails, and it does not imply zeta-spectral tightness. The distinction is exactly the familiar one between boundedness in an `L^1`-type weighted quantity and uniform integrability of that quantity.

If `w(r)=O(log(2+r))`, (26) immediately yields a uniform bound for the `w`-moment as well. Hence every scalar moment-growth criterion at or below logarithmic order admits the same counterexample.

The result is sharp only in this stated sense. It does **not** say that every non-tight family must have a divergent logarithmic moment, nor that superlogarithmic growth is necessary for all possible compactness conditions. Direct zeta-sampled conditions, endpoint-dependent arithmetic restrictions, nonlinear constraints, or profile classes with additional structure can behave differently.

## 6. Prior art and novelty audit

The sampling ingredients are classical. Plancherel--Polya inequalities and their extensions control samples of entire functions of exponential type; a convenient modern reference is G. R. Grozev and Q. I. Rahman, *Entire Functions of Exponential Type Belonging to L^p(R)*, J. London Math. Soc. 50 (1994), 121--138, DOI `10.1112/jlms/50.1.121`. Donoho--Logan's *Signal Recovery and the Large Sieve*, SIAM J. Appl. Math., DOI `10.1137/0152031`, is neighboring large-sieve prior art for controlling concentration of bandlimited functions by sampling-density geometry. Burnol's *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, J. Theorie des Nombres de Bordeaux 16 (2004), 65--94, DOI `10.5802/jtnb.434`, is direct prior art for Hilbert-space/Fourier systems built from the zeta zeros. The Riemann--von Mangoldt local-count input is classical and is already anchored in this line by Hasanalizade--Shen--Wong's explicit zero-counting work.

The logarithmic carrier scale in WI-388 is also consonant with the logarithmic-Laplacian literature: H. Chen and T. Weth, *The Dirichlet problem for the logarithmic Laplacian*, Comm. PDE 44 (2019), 1100--1139, DOI `10.1080/03605302.2019.1611851`, studies the operator with logarithmic Fourier symbol. That paper is contextual rather than load-bearing here; WI-388 proves its needed `O(log R)` carrier estimate directly.

A targeted audit around Plancherel--Polya sampling, large-sieve inequalities for bandlimited functions, zeta-zero Hilbert systems, and weighted Paley--Wiener statements found the classical mechanisms above but no source stating the exact tail estimate (4) for zeta ordinates or the log-versus-superlog scalar-moment boundary obtained by combining it with the WI-388 sideband. This negative search is **not** used as a priority claim. The Mathia contribution is the specialization of the elementary sampling argument to the logarithmically dense zeta-ordinate measure, the uniform-tail formulation needed by WI-387, and the matching WI-388 counterexample at logarithmic moment growth.

## Evidence boundary

- **Classical / literature-backed:** fixed-support Paley--Wiener reproduction; Schwartz convolution bounds; Plancherel; Riemann--von Mangoldt and the resulting `O(log T)` unit-interval zero count; classical exponential-type sampling context.
- **Exact deduction here:** the weighted zeta-ordinate tail inequality (4); continuous logarithmic-tail integrability implying WI-387 spectral tightness; the superlogarithmic moment criterion (7)--(8); extension of the recurrence-side no-go from uniform `H^1` to every uniform `H^s`, `s>0`; and the exact scalar moment-growth boundary obtained from WI-388.
- **Inherited local evidence:** WI-387's coefficient-independent RH recurrence theorem and WI-388's dilute sideband construction with non-tight zeta-sampled mass.
- **Conditional interface:** only the step interpreting (6) inside WI-387's nonnegative Weil spectral formula is under RH. The sampling inequality (4) itself is unconditional.
- **Not claimed:** uniform source-perforation control under a bare superlogarithmic moment; a new simple-critical-zero proportion; a positive Weil gap; a contradiction to RH; or necessity of superlogarithmic growth for arbitrary non-scalar compactness hypotheses.

## Consequence for the live route

The fixed-width adaptive-profile program now has a sharp scalar compactness fork. If the family retains any uniform frequency moment that grows faster than `log |xi|`, WI-387 recurrence returns and the spectral floor collapses to zero under RH. If it escapes through the WI-388 mechanism, bounded log-order energy is compatible with persistent zeta-sampled mass at arbitrarily high frequency. Therefore the next viable argument cannot be "negative gamma energy plus a slightly stronger scalar regularity should imply compactness" unless that regularity crosses the superlog threshold. A genuinely new step must instead control the endpoint phases on the escaped high-frequency packet, derive direct arithmetic restrictions on that packet, or establish source-exact transfer for a stronger non-scalar compactness mechanism.