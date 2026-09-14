# PL-312 — The stretched Volterra defect has an explicit regular right inverse; endpoint cancellation is the only `C^1` outer solvability condition

**Evidence:** `EXACT-DERIVED + RANGE-COMPLETION + SOURCE-SELECTION-REFINEMENT`

**Status:** `EXACT-CONTINUOUS-RANGE + EXPLICIT-RIGHT-INVERSE + FINITE-s-MATCHING-STILL-OPEN`

## Question

`PL-311` proved a necessary endpoint compatibility for the limiting stretched Green operator

\[
(Tf)(r)=e^{-2r}f(r)+e^{-r}\int_0^r e^{-q}f(q)\,dq,
\qquad r>0:
\]

if `f` is endpoint-integrable, `h=(I-T)f` extends continuously to `r=0`, and the equation is solved in the ordinary outer scale, then necessarily `h(0)=0`. It deliberately stopped short of claiming that this condition is sufficient.

For regular outer corrections the range can in fact be characterized exactly. On `C([0,R])`, the only obstruction is first-order endpoint compatibility; in particular, for `C^1` forcing, the single scalar condition `h(0)=0` is both necessary and sufficient. The inverse is explicit. Thus the limiting outer Volterra problem contains no additional smooth solvability condition hidden behind `PL-311`: once the constant endpoint forcing is cancelled, the regular remainder can be solved directly. The unresolved information is therefore the finite-`s` matching law that produces that cancellation and selects the amplitude of the singular fixed profile.

## 1. Exact range theorem on continuous corrections

Fix `R>0` and write

\[
D(r)=1-e^{-2r}.
\tag{PL312-1}
\]

Define

\[
\mathcal Y_R
=
\left\{
 h\in C([0,R]):
 h(0)=0,
 \ \lim_{r\downarrow0}\frac{h(r)}r\text{ exists in }\mathbb R
\right\}.
\tag{PL312-2}
\]

Then

\[
\boxed{
\operatorname{Ran}\bigl((I-T):C([0,R])\to C([0,R])\bigr)
=\mathcal Y_R.
}
\tag{PL312-3}
\]

Moreover, `I-T` is injective on `C([0,R])`. If `h\in\mathcal Y_R`, its unique continuous preimage is

\[
\boxed{
(Rh)(r)
=
\frac{h(r)}{D(r)}
+
\frac{e^{-r}}{\sqrt{D(r)}}
\int_0^r
\frac{e^{-q}h(q)}{D(q)^{3/2}}\,dq,
\qquad r>0,
}
\tag{PL312-4}
\]

with endpoint value

\[
\boxed{
(Rh)(0)=\lim_{r\downarrow0}\frac{h(r)}r.
}
\tag{PL312-5}
\]

Consequently, if `h\in C^1([0,R])`, then

\[
\boxed{
(I-T)f=h\text{ has a unique }f\in C([0,R])
\iff h(0)=0,
}
\tag{PL312-6}
\]

and in that case

\[
f(0)=h'(0).
\tag{PL312-7}
\]

The theorem is a statement about the limiting outer operator only. It does not assert that the finite-`s` completed-Weil equation admits an expansion whose first correction lies in this class.

## 2. Derivation of the right inverse

Suppose first that

\[
(I-T)f=h.
\tag{PL312-8}
\]

Set

\[
V(r)=\int_0^r e^{-q}f(q)\,dq.
\tag{PL312-9}
\]

Then `V'=e^{-r}f`, and (PL312-8) becomes

\[
D(r)f(r)-e^{-r}V(r)=h(r).
\tag{PL312-10}
\]

Eliminating `f` gives

\[
V'(r)-\frac{V(r)}{e^{2r}-1}
=
\frac{e^{-r}h(r)}{D(r)}.
\tag{PL312-11}
\]

Since

\[
\frac{d}{dr}\log\sqrt{D(r)}
=
\frac{1}{e^{2r}-1},
\]

we recover the exact identity already underlying `PL-311`,

\[
\boxed{
\frac{d}{dr}
\left(\frac{V(r)}{\sqrt{D(r)}}\right)
=
\frac{e^{-r}h(r)}{D(r)^{3/2}}.
}
\tag{PL312-12}
\]

Now let `h\in\mathcal Y_R` and put

\[
L=\lim_{r\downarrow0}\frac{h(r)}r.
\tag{PL312-13}
\]

Because `D(r)=2r+O(r^2)`,

\[
\frac{e^{-r}h(r)}{D(r)^{3/2}}
=
\frac{L+o(1)}{2^{3/2}\sqrt r},
\qquad r\downarrow0.
\tag{PL312-14}
\]

The integrand is therefore locally integrable. Choosing the regular particular branch

\[
V_h(r)
=
\sqrt{D(r)}
\int_0^r
\frac{e^{-q}h(q)}{D(q)^{3/2}}\,dq
\tag{PL312-15}
\]

and using (PL312-10) yields exactly (PL312-4). Differentiating (PL312-15), or substituting (PL312-4) back into (PL312-10), proves

\[
(I-T)Rh=h
\qquad\text{on }(0,R].
\tag{PL312-16}
\]

## 3. Endpoint audit and necessity

The two terms in (PL312-4) each contribute half of the endpoint value. From

\[
h(r)=Lr+o(r),
\qquad
D(r)=2r+O(r^2),
\]

we have

\[
\frac{h(r)}{D(r)}\longrightarrow\frac L2.
\tag{PL312-17}
\]

Also (PL312-14) gives

\[
\int_0^r
\frac{e^{-q}h(q)}{D(q)^{3/2}}\,dq
=
\frac{L}{\sqrt2}\sqrt r+o(\sqrt r),
\tag{PL312-18}
\]

and hence

\[
\frac{e^{-r}}{\sqrt{D(r)}}
\int_0^r
\frac{e^{-q}h(q)}{D(q)^{3/2}}\,dq
\longrightarrow\frac L2.
\tag{PL312-19}
\]

Thus `Rh(r)->L`, proving continuity and (PL312-5).

Conversely, if `f\in C([0,R])` and `h=(I-T)f`, then

\[
V(r)=f(0)r+o(r),
\qquad
D(r)f(r)=2f(0)r+o(r).
\]

Equation (PL312-10) therefore gives

\[
\boxed{
 h(r)=f(0)r+o(r).
}
\tag{PL312-20}
\]

So `h\in\mathcal Y_R` and

\[
\lim_{r\downarrow0}\frac{h(r)}r=f(0).
\tag{PL312-21}
\]

This proves both directions of (PL312-3).

## 4. The amplitude mode is exactly the excluded singular homogeneous solution

The homogeneous equation `(I-T)f=0` gives from (PL312-12)

\[
V(r)=C\sqrt{D(r)}.
\tag{PL312-22}
\]

Since `f=e^rV'`,

\[
\boxed{
 f_C(r)
=C\frac{e^{-r}}{\sqrt{D(r)}}
=\frac{C}{\sqrt{e^{2r}-1}}.
}
\tag{PL312-23}
\]

This is exactly the fixed profile of `PL-310`. It is locally integrable but behaves as

\[
f_C(r)\sim\frac{C}{\sqrt{2r}}
\qquad(r\downarrow0),
\tag{PL312-24}
\]

so no nonzero homogeneous solution belongs to `C([0,R])`. This proves injectivity on continuous corrections and clarifies the decomposition on the larger endpoint-integrable class:

\[
\text{outer solution}
=
\text{regular particular correction}
+
C\,\frac{1}{\sqrt{e^{2r}-1}}.
\tag{PL312-25}
\]

The free coefficient in the second term is the same amplitude degree of freedom left by `PL-310`. The regular right inverse cannot determine it because fixing a continuous correction precisely gauges away that singular homogeneous mode.

## 5. Consequence for source selection

`PL-311` showed that a nonzero constant endpoint value in the first outer forcing produces the forbidden direction `e^{-r}` and therefore cannot be absorbed by an endpoint-integrable regular perturbation. The present calculation shows the complementary positive statement for smooth residual forcing.

Suppose a justified finite-`s` expansion were to produce, after separating the leading amplitude mode, a total first-order outer forcing `h_tot\in C^1([0,R])`. Then regular outer solvability is equivalent to the single scalar condition

\[
\boxed{h_{\rm tot}(0)=0.}
\tag{PL312-26}
\]

Once that cancellation holds, the correction is not another mystery: it is uniquely

\[
f_1=R h_{\rm tot}
\tag{PL312-27}
\]

in the continuous gauge, with `f_1(0)=h_tot'(0)`.

This narrows the source-selection frontier. The `r=O(s)` matching corner identified in `PL-311`, or an equivalent finite-`s` kernel correction, does not need to satisfy an unknown family of smooth outer Fredholm conditions. At the level of the limiting `C^1` outer problem it needs to provide one scalar endpoint cancellation. The remaining singular homogeneous amplitude is then free until the global/matched problem fixes it.

The statement is conditional only at this last interpretive step: the existence, order, and uniformity of the finite-`s` expansion are still open.

## 6. Adversarial and novelty audit

The calculation was checked against the two most dangerous failure modes from `PL-310`--`PL-311`.

First, no false uniqueness is asserted on the endpoint-integrable class. The nonzero kernel (PL312-23) belongs locally to `L^1` and is exactly the amplitude mode. Uniqueness holds only after restricting the correction itself to `C([0,R])`, where that mode is excluded.

Second, `h(0)=0` is not claimed sufficient for arbitrary merely continuous forcing. The exact continuous range is (PL312-2): a finite first-order endpoint ratio is also required. The simpler scalar criterion (PL312-6) is stated only for `C^1` forcing, where that ratio is automatically `h'(0)`.

Local duplicate checks against the current `prime_lattice` finding set found no previous exact right inverse (PL312-4), continuous-range characterization (PL312-3), or proof that the `PL-311` compatibility is sufficient on `C^1` forcing. `PL-311` explicitly recorded only necessity and made no surjectivity claim. The integrating-factor inversion is elementary first-order Volterra/ODE calculus, so no broad novelty is claimed for the method itself; the durable contribution is the exact completion of the line-local limiting range problem and its consequence for where completed-Weil source selection can still occur.

No external literature claim is load-bearing here, so this finding adds no source-ledger entry.

## Limits

Nothing in this result proves a matched asymptotic expansion for the finite-`s` Green operator. In particular, it does not estimate `T_s-T` on the overlap `r=O(s)`, identify the actual completed-Weil endpoint forcing, prove that its cancellation determines the leading amplitude, or show that the resulting scalar has a rational-prime-specific sign.

The exact theorem concerns the limiting outer operator and regular corrections. More singular forcing or corrections can occupy larger range classes; for example, the endpoint-integrable class is deliberately broader than `C([0,R])` and can admit behavior excluded by (PL312-2). Such singular corrections would signal breakdown of the regular outer expansion rather than contradict the theorem.

No RH consequence follows from the right inverse itself. It removes an analytic ambiguity: **after the constant endpoint mismatch is cancelled, there is no further `C^1` outer solvability obstruction in the limiting Volterra equation.** The next load-bearing theorem must therefore come from finite-`s` overlap/matching and source structure, not from another regular inversion of `I-T`.

## Verdict

**Exact range completion / positive localization of the remaining gate.** The stretched Volterra defect has an explicit regular right inverse. On continuous outer corrections its range is exactly the functions vanishing to first order with a finite endpoint slope, and for `C^1` forcing the `PL-311` condition `h(0)=0` is necessary and sufficient. The only homogeneous degree of freedom is the singular `PL-310` profile itself.

This makes the small-order source-selection problem more precise: a legitimate matched expansion must determine the scalar endpoint cancellation and the amplitude of the singular profile. The fixed-`r` outer Volterra equation contributes no additional smooth compatibility condition once that endpoint cancellation is supplied.