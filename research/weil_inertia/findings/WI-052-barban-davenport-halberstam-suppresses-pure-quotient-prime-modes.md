# WI-052 — Barban--Davenport--Halberstam suppresses pure quotient prime modes

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It narrows the coefficient/localization obstruction isolated by WI-051. The explicit mean-zero quotient witness used there is a valid information-theoretic counterexample for arbitrary bounded functions, but the corresponding **pure residue-class quotient component of the actual centered von Mangoldt function is strongly suppressed on average over the prime moduli that dominate the Yang Mertens measure**, throughout every fixed power-separated interior of the source support. This follows from the classical Barban--Davenport--Halberstam variance theorem.

Accordingly, the remaining power-coefficient obstruction cannot be represented faithfully by an arbitrary `mod r` quotient mode on a positive-mass interior region. Any genuine leading Yang residual must instead survive in the nonzero aliasing/shift-frequency fibers inside those residue classes, concentrate toward the short-shift boundary, or come from the separately booked collision/analytic interface. This is a structural redirection, not a proof that the locked four-prime covariance is lower order.

## 1. The generic WI-051 witness and the prime-specific question

WI-051 localized the Yang first prime pair on the finite model

\[
G_m=\mathbf Z/(rL)\mathbf Z,
\qquad
G_k=\mathbf Z/L\mathbf Z,
\]

where the allowed shifts are multiples `rk`. Because `m -> m-rk` preserves the residue class of `m mod r`, any bounded function depending only on that quotient is perfectly coherent under every allowed shift. WI-051 used a centered quadratic phase on `Z/rZ` to produce an order-one localized correlation while its ordinary `U^2(G_m)` norm tends to zero like `r^{-1/4}`. Thus no coefficient-uniform localized estimate can follow from ordinary one-variable `U^2` information for arbitrary bounded functions.

For the actual centered von Mangoldt weight on a physical interval `I` of length `M`, define for prime `r`

\[
E_I(r,a)
:=
\sum_{\substack{n\in I\\n\equiv a\pmod r}}\Lambda(n)
-\frac{|I|}{\phi(r)}
\tag{1}
\]

when `(a,r)=1`, and define its normalized quotient energy

\[
\boxed{
\mathcal Q_I(r)
:=
\frac r{M^2}
\sum_{a\bmod r\atop(a,r)=1}|E_I(r,a)|^2.
}
\tag{2}
\]

If `f_r(a)=(r/M)E_I(r,a)`, then `(1/r) sum_a |f_r(a)|^2` is exactly (2), up to the omitted noncoprime residue. Thus (2) measures the `L^2` mass of the component that is constant on residue classes modulo `r`, in the normalization relevant to an order-one quotient witness. The residue `a=0` contains only the prime `r` and its powers and is negligible at macroscopic scale.

## 2. Classical BDH controls this quotient projection on average

Put

\[
\Psi(x;q,a)
=
\sum_{n\le x\atop n\equiv a\pmod q}\Lambda(n)
\]

and

\[
V(x,Q)
=
\sum_{q\le Q}\sum_{(a,q)=1}
\left|\Psi(x;q,a)-\frac{x}{\phi(q)}\right|^2.
\tag{3}
\]

The classical Barban--Davenport--Halberstam theory, in Hooley's all-`Q` refinement, gives for every fixed `A>0` and every `Q<=x`

\[
V(x,Q)
=
Qx\log Q+B_1Qx
+O(Q^{5/4}x^{3/4})
+O_A\!\left(\frac{x^2}{(\log x)^A}\right).
\tag{4}
\]

Only the consequence

\[
\boxed{
V(x,Q)
\ll_A
xQ\log(2x)
+Q^{5/4}x^{3/4}
+\frac{x^2}{(\log x)^A}
}
\tag{5}
\]

is used below. Hooley, *On the Barban--Davenport--Halberstam theorem. I*, J. reine angew. Math. 274/275 (1975), 206--223, is the load-bearing historical source. Harper's 2025 JLMS paper *Simple Barban--Davenport--Halberstam type asymptotics for general sequences* states this formula explicitly in its historical introduction and, importantly for this audit, distinguishes it from Gallagher's simpler upper bound whose stated range is only `x log^{-A}x <= Q <= x`.

For a translated interval `I=(u,v]` with `u,v\asymp M`, its discrepancy is the difference of two prefix discrepancies. The inequality `|A-B|^2<=2|A|^2+2|B|^2` therefore transfers (5), with an absolute constant change, to any fixed macroscopic block of length `asymp M` and location `O(M)`.

## 3. Actual primes dominate the Yang prime-power base measure

WI-033 uses

\[
\mu_\ell
=\frac1\ell
\sum_{p^a\le X}
\frac{\log p}{p^a}
\delta_{\log(p^a)/\ell},
\qquad
\ell=\log X.
\tag{6}
\]

The contribution of proper prime powers is absolutely negligible:

\[
\begin{aligned}
\frac1\ell
\sum_p\sum_{a\ge2}\frac{\log p}{p^a}
&\le
\frac1\ell
\sum_p\frac{\log p}{p(p-1)}\\
&=
\boxed{O(\ell^{-1})},
\end{aligned}
\tag{7}
\]

because the final prime sum converges. Hence the two-base product measure assigns `o(1)` mass to pairs where either base is a proper prime power.

When both bases are primes, the common-underlying-prime exception is just `b_1=b_2`; its normalized product mass is

\[
\frac1{\ell^2}
\sum_{p\le X}\frac{(\log p)^2}{p^2}
=O(\ell^{-2}).
\tag{8}
\]

Thus, outside `o(1)` raw Mertens mass, the Yang reduced coefficients are distinct prime moduli

\[
r=b_1,
\qquad
q=b_2.
\tag{9}
\]

This exact reduction makes an all-moduli AP variance theorem relevant to the dominant source family: restricting the nonnegative BDH sum to these prime moduli loses no validity.

## 4. Mertens-weighted quotient energy is `o(1)` below a fixed power gap

Fix a dyadic prime-modulus range `R<r<=2R` and a physical prime block `I` of scale `M`. Weight (2) by the same normalized one-base Mertens measure as the Yang source:

\[
\begin{aligned}
W(R;M)
&:=
\frac1\ell
\sum_{\substack{R<r\le2R\\ r\ \text{prime}}}
\frac{\log r}{r}\,\mathcal Q_I(r)\\
&=
\frac1{\ell M^2}
\sum_{\substack{R<r\le2R\\ r\ \text{prime}}}
(\log r)
\sum_{(a,r)=1}|E_I(r,a)|^2.
\end{aligned}
\tag{10}
\]

All summands are nonnegative, so enlarge the prime-modulus sum to the full BDH sum over `q<=2R`. Equations (5) and (10) give

\[
\boxed{
W(R;M)
\ll_A
\frac{\log(2R)}\ell
\left[
\frac RM\log(2M)
+\left(\frac RM\right)^{5/4}
+\frac1{(\log M)^A}
\right].
}
\tag{11}
\]

For every fixed `epsilon>0`, uniformly when

\[
R\le M^{1-\varepsilon}
\tag{12}
\]

and `M` is a fixed positive power of `X`, summing (11) over the `O(ell)` dyadic ranges gives

\[
\boxed{
\frac1\ell
\sum_{\substack{r\le M^{1-\varepsilon}\\ r\ \text{prime}}}
\frac{\log r}{r}\,\mathcal Q_I(r)
=o(1).
}
\tag{13}
\]

The arbitrary logarithmic exponent in the last term of (5) absorbs the dyadic count, while the first two terms have a fixed power saving. Thus actual centered primes have asymptotically negligible **pure quotient projection energy**, in the exact Mertens base weighting, whenever the modulus is separated by a fixed power from the physical block length.

## 5. Every fixed Yang interior has that power separation

On the dominant coprime/prime family, WI-046 and WI-050 identify

\[
M_m\asymp\frac X{b_2},
\qquad
M_n\asymp\frac X{b_1},
\qquad
K\asymp\frac X{b_1b_2}.
\tag{14}
\]

Write

\[
b_1=X^\alpha,
\qquad
b_2=X^\beta.
\tag{15}
\]

The nontrivial off-diagonal source support lies in `alpha+beta<=1`, up to the boundary conventions audited in WI-046/WI-047. Fix `delta>0` and restrict to

\[
\alpha+\beta\le1-\delta.
\tag{16}
\]

At exponent level,

\[
1-\frac{\alpha}{1-\beta}
=
\frac{1-\alpha-\beta}{1-\beta}
\ge\delta,
\tag{17}
\]

and symmetrically for `beta/(1-alpha)`. The fixed multiplicative constants hidden in (14) can be absorbed by weakening the exponent margin. Thus, for all sufficiently large `X`, uniformly on (16),

\[
\boxed{
r\le M_m^{1-\delta/2},
\qquad
q\le M_n^{1-\delta/2},
}
\tag{18}
\]

and `M_m,M_n>=X^{\delta+o(1)}`.

Equation (13) therefore applies uniformly to the first base while the second base varies over (16), and vice versa. WI-033 gives total normalized one-base Mertens mass `1+o(1)`; integrating the uniform `o(1)` bound against the other nonnegative normalized base measure preserves `o(1)`. Hence

\[
\boxed{
\text{on every fixed interior }\alpha+\beta\le1-\delta,
\text{ the two-base Mertens-averaged pure quotient energy is }o(1)
\text{ on both prime legs.}
}
\tag{19}
\]

WI-033's weak convergence says that the discarded strip `1-delta<alpha+beta<=1` has raw two-base Mertens measure `O(delta)` as `delta->0`. Equation (19) does **not** turn that raw-mass fact into an energy bound; quotient energy could in principle concentrate as `K` becomes short. WI-046 separately proves that cells with only polylogarithmically many `k` shifts have `o(1)` raw Mertens mass, but neither fact is silently upgraded here to a full locked-covariance estimate.

## 6. What this removes from WI-051, and what survives

The explicit quadratic witness in WI-051 is constant on each residue class modulo `r`. Equation (19) proves that actual centered primes cannot imitate an order-one amount of that **pure residue-class witness** over any fixed power-separated bulk region after the source Mertens averaging.

The exact localized Fourier formula of WI-051, however, contains full fibers

\[
A_r(t)
=
\sum_{a\equiv t\ ({\rm mod}\ L)}
\widehat f_1(-a)\widehat f_2(a),
\tag{20}
\]

and similarly for `q`. BDH controls the one-prime residue-class projection corresponding to the quotient/mean component. It does **not** control nonzero `t` fibers in (20), which encode shift-frequency information within residue classes and are coupled to the second prime pair in the locked four-form covariance.

Nothing here proves the density-normalized twin-prime estimate that WI-041 showed cannot be extracted from unweighted MRT `L^2`, nor the coefficient-uniform four-prime asymptotic missing in WI-039/WI-050. The durable redirection is

\[
\boxed{
\text{generic pure quotient witness}
\longrightarrow
\text{not source-faithful in the prime bulk},
}
\tag{21}
\]

while the live arithmetic target becomes

\[
\boxed{
\text{nonzero aliasing / within-residue pair-correlation fibers}
\text{ for power-sized prime moduli.}
}
\tag{22}
\]

A successful repair can therefore focus on prime-specific orthogonality of the locally centered von Mangoldt residual to those nonzero fibers rather than trying to prove an impossible arbitrary-function coefficient-uniform `U^2` inequality.

## 7. Prior-art and novelty audit

The BDH variance theorem and its refinements are classical. No novelty is claimed for (3)--(5), restriction of a nonnegative variance sum to prime moduli, dyadic decomposition, or the interpretation of arithmetic-progression variance as an `L^2` projection onto residue-class sigma-algebras.

Authoritative sources checked:

- M. B. Barban, **The “large sieve” method and its application to number theory**, Russian Math. Surveys 21:1 (1966), 49--103.
- H. Davenport and H. Halberstam, **Primes in arithmetic progressions**, Michigan Math. J. 13 (1966), 485--489; corrigendum 15 (1968), 505.
- P. X. Gallagher, **The large sieve**, Mathematika 14 (1967), 14--20. Gallagher's classical upper bound is not used outside its stated top-modulus range.
- H. L. Montgomery, **Primes in arithmetic progressions**, Michigan Math. J. 17 (1970), 33--39.
- C. Hooley, **On the Barban--Davenport--Halberstam theorem. I**, J. reine angew. Math. 274/275 (1975), 206--223. Role: the all-`Q` asymptotic (4).
- Adam J. Harper, **Simple Barban--Davenport--Halberstam type asymptotics for general sequences**, J. London Math. Soc. 112 (2025), e70293, DOI `10.1112/jlms.70293`. Role: recent authoritative statement of the classical formulas and their exact ranges, used to audit the Gallagher/Hooley distinction.

The line-specific deductions are (7)--(9), making actual distinct prime bases asymptotically dominant under the Yang prime-power Mertens measure, and (10)--(19), inserting classical AP variance into the exact quotient obstruction identified by WI-051. A targeted literature audit did not locate this Yang-specific combination. That absence is **not** used as a priority claim.

## 8. Decisive audit / falsification tests

Narrow or withdraw this finding if any of the following fails.

1. Verify that the all-`Q` Hooley formula (4) is available uniformly for every `Q<=x` with the stated arbitrary `x^2/log^A x` error; do not substitute Gallagher's narrower range.
2. Recompute (7) including all proper prime powers and verify convergence before division by `ell`.
3. Check the normalization in (2) and (10): the factor `r/M^2` is essential and the source base weight is `(1/ell)(log r)/r` on the prime-dominant family.
4. Verify that translated macroscopic source blocks follow from prefix BDH by subtraction without changing the power ranges.
5. Recheck the physical scales (14), the fixed-margin implication (18), and the uniform outer-base integration leading to (19).
6. Do not infer bounds for nonzero aliasing fibers (20), twin-prime residuals, or the full locked four-prime covariance from one-prime AP variance alone.
7. Do not use the `O(delta)` raw Mertens mass of the boundary strip as an energy bound without an additional uniform consumer estimate there.

## 9. Consequence for `weil_inertia`

WI-051 remains a valid no-go for arbitrary-function localized `U^2` control, but its strongest explicit quotient witness is arithmetically unrepresentative of the actual prime residual on every fixed power-separated bulk region. The coefficient wall is therefore sharpened from

\[
\text{“large-index quotient modes may survive”}
\]

to the more precise source-faithful question

\[
\boxed{
\text{can the post-local-main prime residual carry a leading }
\textbf{nonzero aliasing fiber}
\text{ when }r,q\text{ are power-sized?}
}
\]

That is the next efficient target for `CLUE-yang-locked-covariance-leading-scale`. A proof that those nonzero fibers also have negligible source-weighted mass would remove the main prime-specific escape left after WI-049--WI-052; a counterexample or lower bound showing coherent nonzero-fiber mass would identify the genuinely surviving arithmetic obstruction.