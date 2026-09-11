# MI-017 — The first square-defect shell localizes its hard source coupling below quarter incidence

**Evidence level:** supported by the exact CRT intersection and incidence-tail bounds in MC-228--MC-229; no new Möbius cancellation estimate is claimed.

For `y=c\log X`, primorial `P`, shell primes `d in (y,2y]`, and

\[
\mathcal R_d=\{n\le X-P:(n,P)=1,\ n\equiv-P\pmod{d^2}\},
\]

the source-selected shell has real overlap structure: the same integer can feed many coordinates. MC-228 identifies the extreme full-shell common block and shows that estimating it separately has the target-power transition `c=1/4`.

MC-229 extends that calculation to every mesoscopic incidence level. Put

\[
r_y(n)=\#\{d:d^2\mid n+P\},
\qquad
E_{\ge\alpha}=\left\{n:r_y(n)\ge
\alpha\frac{\log X}{\log\log X}\right\}.
\]

Every `r`-fold intersection is one CRT progression with modulus `\prod_{d\in S}d^2`, and the number of possible shell subsets contributes only `X^{o(1)}`. Consequently, for fixed `0<\alpha<c`,

\[
|E_{\ge\alpha}|\le X^{1-2\alpha+o(1)},
\]

and the separately controlled weighted shell energy from this tail satisfies

\[
W_y^{\ge\alpha}\le X^{2-4\alpha+o(1)}.
\]

The diagonal target is `X^{1+o(1)}`, so the support-only transition is exactly

\[
\alpha=\frac14.
\]

Thus for every `c>1/4`, **all sufficiently high-incidence points are already harmless without using Möbius signs**. The full CRT common mode is only the top level of this tail. Any fixed-power excess must come from incidence

\[
r_y(n)<\left(\frac14+o(1)\right)\frac{\log X}{\log\log X},
\]

or from coherent interference among those lower/mesoscopic pieces.

This changes where “source-coupled cancellation” has to act. The difficult region is not the largest overlaps. It is the broad collection of partial intersections that are individually too dense for support bounds but remain coupled through the deterministic Möbius source. A useful decomposition must preserve signed cross-slice interference there; generic characterwise, fiberwise, or magnitude-only estimates can discard exactly that information.

**Boundary.** The quarter threshold calibrates the square-modulus shell and its quadratic weighted energy. It is not a bound for the full shell energy, does not say cancellation between high and low incidence is irrelevant, and changes if the divisor power, shell width, or energy weight changes.