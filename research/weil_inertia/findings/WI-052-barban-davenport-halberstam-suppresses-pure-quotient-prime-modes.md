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

where the allowed shifts are multiples `rk`. Because `m -> m-rk` preserves the residue class of `m mod r`, any bounded function depending only on that quotient is perfectly coherent under every allowed shift. WI-051 used a centered quadratic phase on `Z/rZ` to produce

\[
\Lambda_{r,q,L}^{\rm loc}\asymp1
\]

while its ordinary `U^2(G_m)` norm tends to zero like `r^{-1/4}`. Thus no coefficient-uniform localized estimate can follow from ordinary one-variable `U^2` information for **arbitrary** bounded functions.

The prime-specific question is narrower. For the actual centered von Mangoldt weight on a physical interval `I` of length `M`, how large is its orthogonal projection onto functions that are constant on residue classes modulo the prime base `r`?

For prime `r`, define

\[
E_I(r,a)
:=
\sum_{\substack{n\in I\\n\equiv a\pmod r}}\Lambda(n)
-\frac{|I|}{\phi(r)}
\tag{1}
\]

for `(a,r)=1`, and define the normalized quotient energy

\[
\boxed{
\mathcal Q_I(r)
:=
\frac r{M^2}
\sum_{a\bmod r\atop(a,r)=1}|E_I(r,a)|^2.
}
\tag{2}
\]

Up to the harmless omission of the residue `a=0`, which contains only the prime `r` and its powers, (2) is exactly the squared `L^2` mass of the residue-class-constant component after normalizing the prime sum to mean scale `M/r`. An `O(1)` quotient witness of the WI-051 type would require `\mathcal Q_I(r)` to remain of order one on a non-negligible set of source moduli.

## 2. Classical BDH controls exactly this quotient projection on average

Write

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

The classical Barban--Davenport--Halberstam theory, sharpened by Hooley, gives for every fixed `A>0` and every `Q<=x`

\[
V(x,Q)
=
Qx\log Q+B_1Qx
+O(Q^{5/4}x^{3/4})
+O_A\!\left(\frac{x^2}{(\log x)^A}\right).
\tag{4}
\]

For the present use only the resulting upper bound matters:

\[
\boxed{
V(x,Q)
\ll_A
xQ\log(2x)
+Q^{5/4}x^{3/4}
+\frac{x^2}{(\log x)^A}.
}
\tag{5}
\]

The historical primary sources are Barban (1966), Davenport--Halberstam (1966), Gallagher (1967), Montgomery (1970), and Hooley's BDH series; Hooley, *On the Barban--Davenport--Halberstam theorem. I*, J. reine angew. Math. 274/275 (1975), 206--223, is the load-bearing all-`Q` asymptotic used here. Adam J. Harper's 2025 JLMS paper *Simple Barban--Davenport--Halberstam type asymptotics for general sequences* records (4) explicitly in its historical introduction and distinguishes it from Gallagher's simpler upper bound, whose printed range is only `x log^{-A}x <= Q <= x`.

The distinction matters: the Yang interior can have `r` far below `M/log^A M`, so the all-`Q` Hooley form, not a misquoted unrestricted Gallagher bound, is what makes the argument below rigorous.

For a translated interval `I=(u,v]` with `u,v\asymp M`, its discrepancy is the difference of two prefix discrepancies. Hence `|A-B|^2<=2|A|^2+2|B|^2` transfers (5), with only an absolute constant change, to any fixed macroscopic source block of length `asymp M` and location `O(M)`.

## 3. Prime bases, not higher prime powers, carry the Yang Mertens mass

WI-033 uses the normalized prime-power measure

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

The higher-prime-power part is in fact negligible by an elementary absolute estimate:

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

because the prime sum converges. Thus, in the two-base product measure, the set where either base is a proper prime power also has `o(1)` normalized mass.

Once both bases are primes, the common-underlying-prime exception is just the diagonal `b_1=b_2`. Its normalized product mass is

\[
\frac1{\ell^2}
\sum_{p\le X}\frac{(\log p)^2}{p^2}
=O(\ell^{-2}).
\tag{8}
\]

Consequently the asymptotically dominant Yang base family consists of **distinct prime moduli**

\[
r=b_1,
\qquad
q=b_2,
\tag{9}
\]

up to `o(1)` raw Mertens mass. This makes the prime-modulus restriction in the next section source-faithful rather than a sparse exceptional subfamily.

## 4. Mertens-weighted quotient energy is `o(1)` in every power-separated interior

Fix a dyadic prime-modulus range

\[
R<r\le2R
\]

and a physical prime block `I` of scale `M`. Weight (2) by the same normalized one-base Mertens measure as the Yang source. Then

\[
\begin{aligned}
W(R;M)
&:=
\frac1\ell
\sum_{R<r\le2R\atop r\ {m prime}}
\frac{\log r}{r}\,\mathcal Q_I(r)\\
&=
\frac1{\ell M^2}
\sum_{R<r\le2R\atop r\ {m prime}}
(\log r)
\sum_{(a,r)=1}|E_I(r,a)|^2.
\end{aligned}
\tag{10}
\]

All summands are nonnegative, so the prime-modulus sum may be enlarged to the full BDH sum over `q<=2R`. Equations (5) and (10) give

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

In particular, for every fixed `epsilon>0`, uniformly when

\[
R\le M^{1-\varepsilon}
\tag{12}
\]

and `M` is a fixed positive power of `X`, summing (11) over the `O(ell)` dyadic ranges gives

\[
\boxed{
\frac1\ell
\sum_{r\le M^{1-\varepsilon}\atop r\ {m prime}}
\frac{\log r}{r}\,\mathcal Q_I(r)
=o(1).
}
\tag{13}
\]

The arbitrary logarithmic exponent in the last term of (5) absorbs the dyadic count; the first two terms have a fixed power saving.

Thus the actual centered prime weight has asymptotically negligible **pure quotient projection energy**, in the exact Mertens base weighting, whenever the modulus is separated by a fixed power from the physical block length.

## 5. The Yang source interior satisfies the BDH power separation

On the asymptotically dominant coprime/prime family, WI-046 and WI-050 identify the physical scales

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

The nontrivial off-diagonal source support lies in

\[
\alpha+\beta\le1
\tag{16}
\]

up to the boundary conventions already audited in WI-046/WI-047. Fix any `delta>0` and restrict to the fixed power-separated interior

\[
\alpha+\beta\le1-\delta.
\tag{17}
\]

Then

\[
r=X^\alpha
\le
M_m^{1-\delta},
\qquad
q=X^\beta
\le
M_n^{1-\delta},
\tag{18}
\]

because

\[
1-\frac{\alpha}{1-\beta}
=\frac{1-\alpha-\beta}{1-\beta}\ge\delta
\]

and symmetrically for the other pair. Also `M_m,M_n>=X^delta`, so the uniformity condition after (12) is automatic.

Applying (13) to both legs therefore shows:

\[
\boxed{
\text{on every fixed interior }\alpha+\beta\le1-\delta,
\text{ the Mertens-averaged pure }\bmod r,\bmod q
\text{ quotient energy is }o(1).
}
\tag{19}
\]

WI-033's quantitative weak convergence says that the discarded strip `1-delta<alpha+beta<=1` has raw two-base Mertens measure `O(delta)` as `delta->0`. Equation (19) does **not** by itself control quotient energy on that strip; energy could in principle concentrate as `K` becomes short. WI-046 separately proves that cells with only polylogarithmically many `k` shifts have `o(1)` raw Mertens mass, but neither statement is silently upgraded here to a full weighted covariance estimate.

## 6. What this removes from WI-051, and what survives

The quadratic quotient witness in WI-051 is constant on each residue class modulo `r`; all of its Fourier mass lies in the quotient fibers that are fixed by the sublattice motion. Equation (19) proves that **actual centered primes cannot imitate an order-one amount of that pure residue-class witness on a positive-mass fixed interior of the Yang continuum** after the source's Mertens averaging over prime bases.

This materially narrows the obstruction, but it does not remove it. The exact localized Fourier formula of WI-051 has fibers

\[
A_r(t)
=
\sum_{a\equiv t\ ({\rm mod}\ L)}
\widehat f_1(-a)\widehat f_2(a),
\tag{20}
\]

and similarly for `q`. BDH controls the one-prime residue-class projection corresponding to the pure quotient/mean component. It does **not** control the nonzero `t` fibers in (20), which encode shift-frequency information **within** residue classes and are coupled to the second prime pair in the locked four-form covariance.

In particular, nothing here proves the density-normalized twin-prime estimate that WI-041 showed cannot be extracted from unweighted MRT `L^2`, nor the coefficient-uniform four-prime asymptotic missing in WI-039/WI-050. The durable redirection is

\[
\boxed{
\text{generic quotient witness}
\quad\longrightarrow\quad
\text{not source-faithful in the bulk for actual primes;}
}
\tag{21}
\]

while the live target becomes

\[
\boxed{
\text{nonzero aliasing / within-residue pair-correlation fibers}
\text{ for power-sized prime moduli.}
}
\tag{22}
\]

A successful repair can therefore focus on prime-specific orthogonality of the locally centered von Mangoldt residual to those nonzero fibers rather than trying to prove an impossible arbitrary-function coefficient-uniform `U^2` inequality.

## 7. Prior-art and novelty audit

The BDH variance theorem and all of its historical refinements are classical. No novelty is claimed for (3)--(5), restriction of a nonnegative variance sum to prime moduli, dyadic decomposition, or the interpretation of arithmetic-progression variance as an `L^2` projection onto residue-class sigma-algebras.

Primary/authoritative prior art checked:

- M. B. Barban, **The “large sieve” method and its application to number theory**, Russian Math. Surveys 21:1 (1966), 49--103.
- H. Davenport and H. Halberstam, **Primes in arithmetic progressions**, Michigan Math. J. 13 (1966), 485--489; corrigendum 15 (1968), 505.
- P. X. Gallagher, **The large sieve**, Mathematika 14 (1967), 14--20. Gallagher's classical upper bound is sufficient near the top range but is not used outside its stated `x log^{-A}x <= Q` regime.
- H. L. Montgomery, **Primes in arithmetic progressions**, Michigan Math. J. 17 (1970), 33--39.
- C. Hooley, **On the Barban--Davenport--Halberstam theorem. I**, J. reine angew. Math. 274/275 (1975), 206--223. Role: the all-`Q` asymptotic (4), including the `x^2/log^A x` small-modulus error.
- Adam J. Harper, **Simple Barban--Davenport--Halberstam type asymptotics for general sequences**, J. London Math. Soc. 112 (2025), e70293, DOI `10.1112/jlms.70293`. Role: recent authoritative statement of the classical prime variance formulas and their exact ranges, used to audit the Gallagher/Hooley distinction.

The new line-specific deductions are (7)--(8), which make actual prime bases asymptotically dominant under the Yang prime-power Mertens measure, and (10)--(19), which insert the classical AP variance into the exact quotient obstruction identified by WI-051. A targeted literature audit did not locate this Yang-specific combination. That absence is **not** used as a priority claim.

## 8. Decisive audit / falsification tests

Narrow or withdraw this finding if any of the following fails.

1. Verify from the primary/authoritative BDH literature that (4) is available uniformly for every `Q<=x` with an arbitrary `x^2/log^A x` error; do not substitute Gallagher's narrower upper-bound range.
2. Recompute (7) including all prime powers `a>=2` and verify that the convergent bound is independent of `X` before division by `ell`.
3. Check the normalization in (2) and (10): the factor `r/M^2` is essential, and the source base weight is `(1/ell)(log r)/r` on the prime-dominant family.
4. Verify that translated macroscopic source blocks are obtained from prefix BDH by subtraction without changing the power ranges.
5. Recheck the source physical scales (14) and the implication (18) from every fixed interior (17).
6. Do not infer any bound for the nonzero aliasing fibers (20), twin-prime residuals, or the full locked four-prime covariance from one-prime AP variance alone.
7. Do not use the `O(delta)` raw Mertens mass of the boundary strip as an energy bound without an additional uniform consumer estimate there.

## 9. Consequence for `weil_inertia`

WI-051 remains a valid no-go for arbitrary-function localized `U^2` control, but its strongest explicit quotient witness is now known to be arithmetically unrepresentative of the actual prime residual on every fixed power-separated bulk region. The coefficient wall has therefore been sharpened from

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

That is the next efficient target for `CLUE-yang-locked-covariance-leading-scale`. A proof that those nonzero fibers also have negligible source-weighted mass would remove the main prime-specific escape left after WI-049--WI-051; a counterexample or lower bound showing coherent nonzero-fiber mass would identify the genuinely surviving arithmetic obstruction.