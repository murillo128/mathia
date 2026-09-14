# PC-286 — RH pushes boundary-log Li-grid collapse to near-square-root bandwidth

**Status:** `CONDITIONAL-DERIVED` + `CLASSICAL-RH-TRANSFER` + `DECISIVE-BOUNDARY` for the one-profile boundary-log spectral frontier left by PC-284/PC-285.

PC-284 proves a deterministic transport theorem for the complete normalized singular-spectrum law of the exact selector-subtracted boundary logarithm, and PC-285 inserts the strongest unconditional classical PNT remainder used by this line. The resulting unconditional window still stops far below the denominator-scale transition `B\asymp q^{1/2}`.

Assuming the Riemann hypothesis changes that boundary qualitatively. Schoenfeld's classical RH estimate

\[
\boxed{
|\pi(x)-\operatorname{Li}(x)|
\le \frac{1}{8\pi}\sqrt{x}\log x
\qquad (x\ge2657)
}
\tag{1}
\]

implies for the normalized prime source `\nu_q` and the denominator-`q` Li-grid control `\widetilde\lambda_q` of PC-277 that

\[
\boxed{
W_1(\nu_q,\widetilde\lambda_q)
\ll q^{-1/2}(\log q)^2+\frac1q.
}
\tag{2}
\]

Inserting (2) into the exact boundary-log finite-section estimate of PC-284 and optimizing the clipping scale gives the conditional bound

\[
\boxed{
\mathbb E\,W_1^{(\ell^\infty)}
\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
B^{1/3}q^{-1/6}(\log q)^2
+B^{1/3}q^{-2/3}
+\frac{(\log q)^2}{q},
}
\tag{3}
\]

where the expectation notation only records the coupling/averaging already used in PC-284; equivalently the left side is the Wasserstein distance between its two spectral laws. In particular, under RH,

\[
\boxed{
B=o\!\left(\frac{\sqrt q}{(\log q)^6}\right)
\quad\Longrightarrow\quad
W_1^{(\ell^\infty)}
\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)\to0.
}
\tag{4}
\]

Thus **RH itself forces the exact one-profile Prime-Circle boundary-log spectrum to become asymptotically indistinguishable from the non-prime Li-grid control almost all the way to the square-root bandwidth scale, up to a polylogarithmic gap**. A persistent order-one prime-versus-Li spectral separation along any sequence satisfying (4) would therefore contradict RH; collapse in this range does not conversely imply RH.

## 1. RH gives a polynomially small prime-to-Li source distance

Let

\[
E(x):=\pi(x)-\operatorname{Li}(x).
\]

Under RH, (1) gives `E(x)=O(sqrt(x) log x)`. For a bounded Lipschitz test `g` on the normalized source interval, Stieltjes integration by parts yields

\[
\sum_{p\le q}g(p/q)
-\int_2^q g(x/q)\,d\operatorname{Li}(x)
=
 g(1)E(q)
-\int_2^q E(x)\,d(g(x/q))
+O(\|g\|_\infty).
\tag{5}
\]

Since `|d(g(x/q))|<=Lip(g) dx/q` in the absolutely continuous approximation (or by the standard bounded-variation formulation),

\[
\frac1q\int_2^q |E(x)|\,dx
\ll \sqrt q\log q.
\tag{6}
\]

The endpoint term has the same order. Normalizing by `\pi(q)\asymp q/\log q`, and accounting for the difference between the normalizing masses `\pi(q)` and `\operatorname{Li}(q)`, therefore gives

\[
\left|
\int g\,d\nu_q-
\int g\,d\lambda_q
\right|
\ll
(\|g\|_\infty+\operatorname{Lip}(g))
q^{-1/2}(\log q)^2.
\tag{7}
\]

The nearest denominator-`q` projection from `\lambda_q` to `\widetilde\lambda_q` costs at most `1/q` in `W_1`, exactly as in PC-277. Kantorovich duality gives (2).

This is the only RH input. No explicit-formula oscillation, zero statistic, or Prime-Circle-specific estimate is inserted into the source comparison.

## 2. Transfer through the exact singular boundary profile

PC-284 proves for every `1/q<=\varepsilon<=1/4` that

\[
\begin{aligned}
W_1^{(\ell^\infty)}
\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll{}&
\sqrt\varepsilon\,(\log q)^{3/2}\\
&+\frac{B\log q}{\varepsilon}
W_1(\nu_q,\widetilde\lambda_q)
+\frac{(\log q)^2}{q}.
\end{aligned}
\tag{8}
\]

Put `L=log q`. Substitution of (2) gives

\[
W_1^{(\ell^\infty)}
\ll
\sqrt\varepsilon\,L^{3/2}
+\frac{Bq^{-1/2}L^3}{\varepsilon}
+\frac{BL}{q\varepsilon}
+\frac{L^2}{q}.
\tag{9}
\]

Balance the first two terms by taking

\[
\boxed{
\varepsilon_q
:=
B^{2/3}q^{-1/3}L.
}
\tag{10}
\]

For every sequence in (4), `\varepsilon_q\to0`, while `\varepsilon_q\ge1/q` for all sufficiently large `q`; also `2B+1<=q`, so all hypotheses of PC-284 remain valid. The balanced terms are

\[
\sqrt{\varepsilon_q}\,L^{3/2}
=
\frac{Bq^{-1/2}L^3}{\varepsilon_q}
=
B^{1/3}q^{-1/6}L^2,
\tag{11}
\]

and the denominator-mesh term becomes

\[
\frac{BL}{q\varepsilon_q}
=
B^{1/3}q^{-2/3}.
\tag{12}
\]

Equations (9)--(12) prove (3). The leading term tends to zero precisely under

\[
B^{1/3}q^{-1/6}L^2=o(1),
\]

which is equivalent to (4).

The logarithmic sixth power is therefore not a proposed arithmetic exponent. It is the deterministic loss from combining the PC-284 microscopic clipping error with the RH source-transport scale. A sharper treatment of the exceptional phase set could change that power without changing the main conclusion that RH moves the classicalization boundary from subexponential bandwidth to a polynomially near-square-root scale.

## 3. Relation to the exact denominator transition

PC-277 records the universal denominator-`q` resonance fact that once `(B+1)^2>q`, the normalized scalar near-resonance statistic collapses for every denominator-`q` source, prime or not. PC-284 concerns a richer finite-section singular spectrum and does not assert the same exact scalar collapse, so (4) should not be identified with an exact resonance theorem for the boundary-log matrix.

What (4) does show is that the unresolved one-profile boundary-log window is conditionally squeezed to within polylogarithmic distance of the natural rational-microscopic square-root scale. The previous unconditional PC-285 frontier

\[
\log B=o\!\left(
(\log q)^{3/5}(\log\log q)^{-1/5}
\right)
\]

is exponentially smaller than the RH-conditional range (4).

This distinction matters for interpretation. If a numerical or asymptotic prime-only effect appears at, say, `B=q^{1/3}` in this one-profile spectrum, it is not evidence in favor of RH: **provided the persisted deterministic estimates are correct, an order-one separation from the matched Li-grid law at that scale would be evidence against RH.** Under RH the source is already too close to its classical non-prime control for PC-284's full normalized spectral law to retain such a separation.

## 4. Prior-art and novelty audit

The analytic-number-theory input is classical. Lowell Schoenfeld, *Sharper Bounds for the Chebyshev Functions θ(x) and ψ(x). II*, **Mathematics of Computation** 30 (1976), 337–360, gives the explicit RH estimate (1); it is the effective form of the classical von-Koch implication `RH => pi(x)-Li(x)=O(sqrt(x) log x)`. Modern refinements of RH-conditional prime-counting bounds do not change the polynomial `q^{-1/2}` source scale needed here.

Targeted searches against RH prime-counting transport, Wasserstein formulations for prime distributions, singular-value asymptotics of finite Toeplitz sections, and logarithmic/cyclotomic kernels found the expected classical ingredients but no prior result with this particular Prime-Circle finite-section statement. Wasserstein methods do occur in contemporary prime-race work, and singular-value laws for Toeplitz finite sections are classical operator theory; neither supplies an independent prime-circle mechanism here.

Accordingly, **no new RH theorem is claimed**. Equation (1) is classical, (2) is its elementary bounded-Lipschitz transport consequence, and (8) is already PC-284. The project-local mathematical delta is the optimized composition (3)--(4): it identifies what RH would force on the exact roots-of-unity boundary-log spectral experiment and moves the conditional no-go frontier to `B=o(sqrt(q)/(log q)^6)`.

No new `SOURCES.md` entry is required for the line's logic because the load-bearing external theorem is cited explicitly here and the remaining operator/transport ingredients are already sourced by PC-277/PC-280/PC-281/PC-284.

## 5. Falsification and surviving frontier

This finding is deliberately one-way. It proves

\[
\mathrm{RH}
\Longrightarrow
\text{Li-grid reproduction of the PC-284 spectral law in the range (4)}.
\tag{13}
\]

It does **not** prove that Li-grid reproduction implies RH, nor that a single finite discrepancy falsifies RH. A contradiction requires an asymptotic order-one lower bound along a sequence satisfying (4), after preserving the exact PC-284 normalization and matched Li-grid control.

The live one-profile boundary-log frontier is therefore the remaining polylogarithmic gap between (4) and genuinely denominator-microscopic bandwidth, together with any deliberately magnified prime-minus-Li residual. The latter is especially delicate: under RH its natural size is already governed by the classical explicit-formula remainder, so a successful continuation must show that the Prime-Circle geometry contributes a nontrivial transform, positivity, topology, or operator constraint rather than merely magnifying `\pi-\operatorname{Li}`.

Cross-level, multi-source, directional, noncommuting, or otherwise enriched observables remain outside (13), as do mechanisms that retain more than the ordered normalized singular-value vector of one boundary-log finite section. Those remain legitimate places for an intrinsically geometric RH bridge; the single-profile spectral law studied here is conditionally classical almost up to the square-root rational scale.