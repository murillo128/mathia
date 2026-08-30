# WI-038 — the covered-zone Gallagher collar is automatic at the MRT scale

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. Under the public Yang--Yang collar convention and the same covered-zone hypothesis needed to invoke Matomäki--Radziwiłł--Tao (MRT), the Diophantine separation hypothesis left conditional in WI-035 is automatic. The apparently dangerous dilation factors cancel against the matched physical lengths of the two locked prime sums. The same calculation also supplies the polylogarithmic phase-variation condition required by the reduced-denominator Siegel--Walfisz major-arc law.

This does **not** establish the one-sided fourth-moment theorem or change Mathia's current unconditional simple-critical proportion. It applies only where both prime-sum lengths lie in the MRT-covered range. The uncovered/low zone, welding/Abel glue, dispersion normalization, and final asymptotic remainder remain independent gates.

## 1. Source boundary

The pinned source is `JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`. In `paper.tex`, the subsection `Covered zone, middle band, bridge and aggregation` uses locked dilated sums

\[
S_i(\alpha)=\sum_{m\sim M_i}\Lambda(m)e(b_i m\alpha)
\]

and invokes MRT only when

\[
M_i\ge X^{8/33+\varepsilon}.
\tag{1}
\]

The public reproduction code uses `arc_quality(gam,P,wid)` with `wid_i=P/Y_i`, so a major-arc approximation has the normalization

\[
\boxed{
\left|\gamma_i-\frac{a_i}{q_i}\right|
\le \frac{P}{q_iY_i},
\qquad q_i\le P.
}
\tag{2}
\]

Here `P=(log X)^B` in the analytic argument and the physical span is

\[
Y_i=b_iM_i.
\tag{3}
\]

The locked cells compare the two sums at the same physical product scale, so after dyadic localization

\[
C^{-1}Y_1\le Y_2\le CY_1
\tag{4}
\]

for an absolute constant `C` (and at the locked center one has `Y_1=Y_2`).

No novelty is claimed for Gallagher smoothing, rational separation, Siegel--Walfisz, or MRT. The deduction here is the parameter compatibility specific to the public Yang--Yang construction.

## 2. Matched physical scale forces simultaneous rational coalescence

Set

\[
\gamma_1=b_1\alpha,
\qquad
\gamma_2=b_2\alpha.
\tag{5}
\]

Suppose both phases satisfy (2). Since `b_2 gamma_1=b_1 gamma_2` exactly,

\[
\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
\frac{Pb_2}{q_1Y_1}+
\frac{Pb_1}{q_2Y_2}.
\tag{6}
\]

Multiplying by `q_1q_2` and using `q_i<=P` gives

\[
q_1q_2\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
P^2\left(\frac{b_2}{Y_1}+\frac{b_1}{Y_2}\right).
\tag{7}
\]

The physical-scale relation eliminates the large dilations. From (3)--(4),

\[
\frac{b_2}{Y_1}
=\frac{Y_2}{Y_1}\frac1{M_2}
\le \frac{C}{M_2},
\qquad
\frac{b_1}{Y_2}
=\frac{Y_1}{Y_2}\frac1{M_1}
\le \frac{C}{M_1}.
\tag{8}
\]

Hence on the covered zone,

\[
\boxed{
q_1q_2\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
CP^2\left(\frac1{M_1}+\frac1{M_2}\right)
=o(1).
}
\tag{9}
\]

For sufficiently large `X` the right side is below `1`. If the rational number in (9) were nonzero, its absolute value would be at least `1/(q_1q_2)`. Therefore

\[
\boxed{
\frac{b_2a_1}{q_1}=\frac{b_1a_2}{q_2}.
}
\tag{10}
\]

This is exactly the rational-separation conclusion that WI-035 had obtained only under an explicit collar hypothesis. Thus that extra hypothesis is not an additional arithmetic input on the MRT-covered zone.

## 3. The phase-variation condition is automatic as well

Let

\[
\eta_i=\gamma_i-a_i/q_i.
\]

Using (2) and `Y_i=b_iM_i`,

\[
\boxed{
|\eta_i|M_i
\le \frac{P}{q_ib_i}
\le P.
}
\tag{11}
\]

For `P=(log X)^B`, partial summation therefore pays only a polylogarithmic phase-variation cost. This is the hypothesis used in WI-035 to derive, after denominator contraction,

\[
S_i(\alpha)
=
\frac{\mu(q_i')}{\varphi(q_i')}V_i(\eta_i)
+O\!\left(M_i e^{-c\sqrt{\log M_i}}\right),
\qquad
q_i'=\frac{q_i}{(q_i,b_i)}.
\tag{12}
\]

Large `b_i` again create no extra loss because the Gallagher width was normalized by the physical length before rational classification.

## 4. Consequence for simultaneous major arcs

Once (10) holds, the denominator-contraction argument of WI-035 applies without a separate collar assumption. If `g=(b_1,b_2)` and `d` is the reduced common rational center, then

\[
d\mid b_1q_1,
\qquad d\mid b_2q_2,
\]

and therefore

\[
\boxed{
d\le \min(Pb_1,Pb_2,P^2g).}
\tag{13}
\]

Thus on the covered zone the chain

\[
\text{Gallagher collar}
\to
\text{rational coalescence}
\to
\text{denominator contraction}
\to
\text{ordinary Siegel--Walfisz major arc}
\]

is supplied by the public parameters rather than by a separate two-modulus arithmetic theorem.

## 5. Boundary conditions and remaining gates

The conclusion deliberately excludes:

- **Uncovered / low zone:** if either `M_i` lies below the MRT threshold (1), the power saving in (9) is no longer available from this argument.
- **Welding/glue:** exact main-term factorization, Abel summation against the welding weight, and the minor-arc weighted estimate remain separate obligations. WI-037 shows in particular that divisor-boundedness alone does not supply that weighted MRT bridge.
- **Dispersion and consumer normalization:** the conversion from the prime-correlation variance to the `R(1)` remainder still needs an end-to-end audit.
- **Finite deterministic remainder:** WI-030/WI-031 settle important continuum/tail pieces, not the entire finite zone ledger.
- **Higher-moment tower:** nothing here repairs WI-003's separate truncation defect.

The exact falsification tests are: verify that the analytic collar really has normalization (2); verify that `Y_1/Y_2` stays within fixed constants on every locked covered cell; and verify that every cell called covered has **both** prime-sum lengths satisfying (1). Any failure requires narrowing this finding.

## 6. Prior-art and novelty assessment

Classical/literature-backed inputs are Gallagher-type smoothing at physical width `1/Y`, elementary separation of distinct rationals, Siegel--Walfisz with partial summation, and MRT's shifted-prime theorem in the `8/33+epsilon` range. Source-backed inputs are the Yang--Yang locked dilated sums, the public `P/Y_i` collar, and the covered-zone scale condition. WI-035 supplies the denominator-contraction lemma conditional on rational coalescence.

The additional exact deduction recorded here is

\[
\boxed{
P^2\left(\frac{b_2}{Y_1}+\frac{b_1}{Y_2}\right)
\asymp
P^2\left(\frac1{M_1}+\frac1{M_2}\right)=o(1),
}
\]

which identifies the smoothing-collar compatibility as a consequence of already-present physical-scale hypotheses. No priority claim is made from the absence of a matching formulation in the bounded prior-art search.

## 7. Consequence for `weil_inertia`

The one-sided fourth-moment audit no longer needs a separate covered-zone Diophantine collar lemma. WI-034 supplies the structured `L^2` aggregation, WI-035 supplies denominator contraction, and this finding closes the public collar/phase compatibility on the same zone where MRT is available. The high-value unresolved interface is now the **uncovered/low-zone plus welding/remainder ledger**, with WI-037 showing that the welding minor-arc step cannot be justified by divisor-boundedness alone. WI-028 remains the quantitative benchmark: the final remainder need only beat the much coarser threshold stored there to improve the current unconditional theorem.