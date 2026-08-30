# WI-035 — the two-modulus major-arc geometry reduces to denominator contraction

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding closes a narrow but load-bearing audit question left open by WI-034: there is no intrinsically new `b`-dependent major-arc phenomenon in the Yang--Yang one-sided fourth-moment route. After an exact denominator contraction, the major-arc main term is the standard Siegel--Walfisz additive-character main term, and simultaneous small-denominator arcs obey the source's claimed `min(P b_1,P b_2,P^2 gcd(b_1,b_2))` denominator restriction by an elementary Diophantine argument. The phase-dilation step is likewise scale-covariant when the two prime sums are measured at their natural physical lengths.

This does **not** certify the one-sided fourth-moment theorem or change Mathia's current unconditional simple-critical proportion. The source still has to verify, cell by cell, that its smoothing collar supplies the explicit approximation-quality hypotheses below, and the welding/glue, minor-arc, dispersion-normalization and final remainder interfaces remain outside the established conclusion.

## 1. Source claim and scope

The pinned source is

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, `paper.tex`, subsection `Covered zone, middle band, bridge and aggregation`.

It writes

\[
S_i(\alpha)=\sum_{m\sim M_i}\Lambda(m)e(b_i m\alpha)
\]

and says that four archived lemmas discharge the two-modulus structure: a `b`-uniform major-arc law with reduced denominator

\[
q_i=\frac q{(q,b_i)},
\]

a classification of joint near-major points by

\[
q\le \min(P^2g,Pb_1,Pb_2),\qquad g=(b_1,b_2),
\]

a dilation transfer, and a smoothing-collar lemma. The public paper gives only a summary of those archived lemmas. WI-034 separately verified that, once this discharge has reduced the problem to ordinary long shifts, Matomäki--Radziwiłł--Tao supplies the required `L^2` averaged shifted-prime input.

The classical analytic input used below is only Siegel--Walfisz plus the standard major/minor-arc treatment of von Mangoldt exponential sums; see, for example, R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., Cambridge Tracts in Mathematics 125, Cambridge University Press, 1997. No novelty is claimed for those tools.

## 2. Exact denominator contraction

Let

\[
\alpha=\frac aq+\eta,\qquad (a,q)=1,
\]

and fix an integer dilation `b>=1`. Put

\[
g=(b,q),\qquad q_b=\frac qg,\qquad a_b=\frac{ab}{g}.
\tag{1}
\]

Then

\[
(a_b,q_b)=1
\tag{2}
\]

and, exactly,

\[
e\!\left(bn\frac aq\right)=e\!\left(n\frac{a_b}{q_b}\right).
\tag{3}
\]

Thus

\[
\boxed{
 b\alpha=\frac{a_b}{q_b}+b\eta
 \pmod 1,
 \qquad q_b=\frac q{(q,b)}.
}
\tag{4}
\]

The rational denominator seen by the dilated prime sum can only **decrease**. This is precisely the denominator `q_i=q/(q,b_i)` printed by the Yang--Yang source.

## 3. Siegel--Walfisz gives the `b`-uniform major-arc law once the reduced parameters are small

Let `I` be an interval contained in `[M,2M]`, and define

\[
S_b(\alpha;I)=\sum_{n\in I}\Lambda(n)e(bn\alpha),
\qquad
V_I(\xi)=\int_I e(\xi t)\,dt.
\tag{5}
\]

Fix constants `A,B>0`. Assume

\[
q_b\le (\log M)^A,
\qquad
|b\eta|M\le(\log M)^B.
\tag{6}
\]

Then Siegel--Walfisz in residue classes modulo `q_b`, followed by partial summation, gives

\[
\boxed{
S_b\!\left(\frac aq+\eta;I\right)
=
\frac{\mu(q_b)}{\varphi(q_b)}V_I(b\eta)
+O_{A,B}\!\left(M e^{-c_{A,B}\sqrt{\log M}}\right).
}
\tag{7}
\]

The error is uniform in the original `b` and `q`; they enter only through the reduced denominator and the phase-variation quantity in (6).

To see (7), decompose the sum by residue classes modulo `q_b`. For `(r,q_b)=1`, Siegel--Walfisz gives

\[
\sum_{\substack{n\le x\\n\equiv r\ (q_b)}}\Lambda(n)
=
\frac{x}{\varphi(q_b)}
+O_A\!\left(xe^{-c_A\sqrt{\log x}}\right)
\tag{8}
\]

uniformly for `q_b<=(log x)^A`. The non-coprime residue classes contain, as far as `Lambda` is concerned, only prime powers supported on primes dividing `q_b`, and contribute at most a polylogarithmic amount. Partial summation against `e(b eta t)` costs a factor `1+|b eta|M`, which is polylogarithmic by (6) and is absorbed by the exponential saving. Finally

\[
\sum_{\substack{r\bmod q_b\\(r,q_b)=1}}
e\!\left(\frac{a_b r}{q_b}\right)
=c_{q_b}(a_b)=\mu(q_b),
\tag{9}
\]

because `(a_b,q_b)=1`. Equations (8)--(9) give (7).

There is one normalization point that an audit of the Yang notation must retain. The standard main integral is `V_I(b_i eta)`, not literally `V_I(eta)`. The source writes `v_i(eta)` without defining `v_i` in the public text at that point. Its formula is correct if `v_i(eta)` denotes the naturally dilated integral `V_{I_i}(b_i eta)`; treating `v_i` as an undilated common function would be incorrect.

## 4. Exact simultaneous-major-arc denominator bound

The source's `P^2 g` restriction also follows from a short exact argument.

Let

\[
\gamma_i=b_i\alpha,
\qquad
\left|\gamma_i-\frac{a_i}{q_i}\right|\le\delta_i,
\qquad
(a_i,q_i)=1,
\qquad q_i\le P,
\tag{10}
\]

for `i=1,2`. Since `b_2 gamma_1=b_1 gamma_2` exactly,

\[
\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le b_2\delta_1+b_1\delta_2.
\tag{11}
\]

If the collar is narrow enough that

\[
\boxed{
 b_2\delta_1+b_1\delta_2<\frac1{q_1q_2},
}
\tag{12}
\]

then the rational number on the left of (11) must be zero: if nonzero, its denominator divides `q_1q_2`, so its absolute value is at least `1/(q_1q_2)`. Hence

\[
\frac{a_1}{b_1q_1}
=
\frac{a_2}{b_2q_2}
=:\frac cd
\tag{13}
\]

for a reduced common center `c/d`. Therefore

\[
d\mid b_1q_1,
\qquad
d\mid b_2q_2,
\tag{14}
\]

and immediately

\[
d\le Pb_1,
\qquad
d\le Pb_2.
\tag{15}
\]

Write `g=(b_1,b_2)`, `b_1=gr`, `b_2=gs` with `(r,s)=1`. From (14),

\[
d\le \gcd(b_1q_1,b_2q_2)
=g\,\gcd(rq_1,sq_2).
\tag{16}
\]

Prime by prime, `(r,s)=1` implies

\[
\gcd(rq_1,sq_2)\mid q_1q_2.
\tag{17}
\]

Thus

\[
\boxed{
 d\le \min(Pb_1,Pb_2,P^2g).
}
\tag{18}
\]

This is exactly the modulus shape quoted in the source. No distribution theorem for primes is involved in (18); the only analytic requirement is the collar/separation inequality (12).

The argument also explains why the apparently two-modulus major-arc family is finite after reduction: its essential arithmetic labels are the two reduced denominators `q_1,q_2<=P`, rather than the unreduced physical dilations `b_1,b_2`.

## 5. Dilation transfer is scale-covariant

Equation (4) already contains the phase transfer needed for a standard minor-arc estimate:

\[
\left|b\alpha-\frac{a_b}{q_b}\right|=b|\eta|.
\tag{19}
\]

If the dilated prime sum has length `M_b` and its natural physical scale is

\[
Z=bM_b,
\tag{20}
\]

then

\[
\boxed{
 (b|\eta|)M_b=|\eta|Z.
}
\tag{21}
\]

So the approximation-quality quantity that enters the usual Vaughan-type estimates is invariant under passing from the common phase to the dilated phase when the intervals are compared at fixed physical scale. This is exactly the geometry of the Yang locked pair: the two frequencies are `b_2 m` and `b_1 n`, while the corresponding windows are chosen so those physical ranges match.

Consequently, once a cell has verified its reduced denominator `q_b` and the common collar width, the standard one-variable exponential-sum estimate may be applied to `b alpha` directly. There is no additional multiplicative `b` loss hidden in the act of dilation itself.

## 6. What is now closed, and what is not

Together, (4), (7), (18), and (21) remove three plausible failure modes from the public summary of the Yang two-modulus discharge:

1. a dilation cannot create a larger rational denominator; the exact denominator is `q/(q,b)`;
2. simultaneous small reduced denominators necessarily coalesce onto a common rational center satisfying the advertised `min(Pb_1,Pb_2,P^2g)` bound once the collars are separated as in (12);
3. the phase error scales with the interval length so that `b` itself does not create a new minor-arc loss at matched physical scale.

This does **not** prove that every retained Yang cell satisfies the hypotheses required to invoke those statements. The remaining audit gates are explicit:

- verify from the source's actual smoothing/Gallagher collars that (12) holds uniformly and that every major-arc cell satisfies (6);
- isolate any top-scale edge on which `M_i` becomes too short for the stated Siegel--Walfisz regime, and show its normalized contribution is `o(1)` rather than infer this from finite-height measurements;
- verify the exact dispersion-swap normalization feeding `R(1)`;
- verify the welding-weight Abel summation and the claimed use of MRT Proposition 5.4 / Appendix A on the minor arcs;
- close the final zone/remainder ledger with rigorous, rather than trend-based, asymptotic bounds.

The four archived lemmas cited by the source are not part of the public reproduction tree as a standalone proof archive. The result here therefore replaces only their denominator/major-arc algebra by a self-contained argument; it does not treat an absent archive as evidence.

## 7. Relation to WI-003 and WI-034

WI-003 concerns a separate higher-moment truncation claim in which a global `ell_1` cutoff was used as though it reduced arithmetic moduli cellwise. Nothing above repairs that issue.

WI-034 verified a different interface: the published MRT almost-all-shifts theorem implies the hard-window `L^2` variance required by the one-sided route, and the structured multiplicity `nu(h)<=tau(h)` preserves arbitrary logarithmic saving. WI-035 now shows that the **rational-denominator geometry preceding that MRT layer is standard and internally consistent under explicit collar hypotheses**. The live uncertainty is therefore narrower: it lies in matching the source's actual collars/windows to those hypotheses and in the later glue/ledger interfaces, not in a mysterious two-modulus prime theorem.

## 8. Prior-art and novelty assessment

Literature/classical inputs:

- Siegel--Walfisz for `Lambda` in reduced residue classes with polylogarithmic modulus;
- Ramanujan's sum `c_q(a)=mu(q)` for `(a,q)=1`;
- partial summation for smooth additive twists;
- standard Vaughan/Hardy--Littlewood major/minor-arc estimates.

Source-specific inputs:

- the Yang--Yang definitions of the two dilated prime sums and the claimed four-lemma discharge;
- the matched physical-window geometry of the locked fourth-moment cells.

New exact deductions recorded here are the explicit audit reduction (4), the simultaneous-center lemma (12)--(18), and the scale-covariance statement (21), together with the identification of the precise hypotheses under which the source's `b`-uniform major-arc summary follows from classical one-variable theory. No priority claim is made for these elementary lemmas; their value is to remove an apparent arithmetic novelty from the remaining proof burden.

A bounded prior-art search found only standard circle-method formulations, consistent with this classification: the mechanism is classical after reduction rather than a new two-modulus theorem.

## 9. Decisive audit tests

Reject or narrow this finding if any of the following fails.

1. Recompute `(a_b,q_b)` in (1)--(4) prime by prime, including cases where `b` shares high prime powers with `q`.
2. Derive (7) directly from Siegel--Walfisz and verify that the total-variation factor from `e(b eta t)` is absorbed under (6).
3. Test the simultaneous-center proof at extreme gcd configurations, e.g. `b_1|b_2`, coprime `b_1,b_2`, and prime-power `q_i`; (17) must hold in every case.
4. In the Yang cell definitions, verify the actual arc widths imply the strict separation condition (12), not merely a numerically similar heuristic.
5. Verify the source's `v_i(eta)` convention includes the dilation `b_i eta`; otherwise its printed major-arc formula needs a normalization correction.
6. Keep smoothing/glue/final-ledger claims outside the conclusion until their own parameter inequalities are reconstructed.

## 10. Consequence for `weil_inertia`

The one-sided fourth-moment route remains a credible independent path past the current support-one theorem, but its remaining analytic uncertainty is now more sharply localized. There is no need to invent a new two-modulus prime-correlation theorem for the major arcs: **denominator contraction plus classical Siegel--Walfisz already supplies that layer once the collars are verified**. The next high-value audit target is therefore the smoothing-collar and welding/glue interface that turns these local major/minor-arc statements into the actual `R(1)` remainder bound.