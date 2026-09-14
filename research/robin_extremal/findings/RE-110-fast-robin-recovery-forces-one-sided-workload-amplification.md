# RE-110 — fast Robin recovery forces one-sided workload amplification

**Status:** `EXACT-DERIVED + EVENT-WORKLOAD + INTER-BLOCK-RECOVERY + SELECTION-CONDITIONED + PNT-ENVELOPE-SATURATION + FALSE-RH-CONSEQUENCE + MATCHED-CONTROL + PRIOR-ART-AUDITED`.

`RE-109` turns recovery from a positive Robin state into an exact quadrature defect for the full CA event staircase and then bounds every event/physical displacement by the unconditional PNT envelope `Y E(Y)`. This yields the recovery corridor

\[
V-Y\gg \frac{h(C)Y\log Y}{\mathcal E(Y)}.
\]

That estimate suppresses the actual **sign and size of the workload used by the recovery**. Retaining the positive part gives a sharper structural statement which does not itself use the PNT: recovery height is bounded by recovery length times the largest forward event-workload defect. For an adaptively selected false-RH witness, this forces a dichotomy: a sublinear recovery corridor can exist only if the event workload amplifies far beyond the selector defect that created the witness. If the `RE-109` corridor is close to its PNT lower scale, some crossed event must in fact saturate the one-sided PNT envelope up to constants.

Let `C<D` be colossally abundant states and write

\[
Y:=\log C,\qquad V:=\log D,\qquad L:=V-Y,
\]

\[
h(N):=\log G(N)-\gamma,
\qquad h(C)>0,\qquad h(D)\le0.
\tag{1}
\]

For every full CA event group crossed from `C` to `D`, let `eta_e` be its event coordinate, `m_e` its total logarithmic mass, and

\[
u_e:=\Phi(\eta_e^-).
\tag{2}
\]

The physical mass interval of that event is

\[
I_e=(u_e,u_e+m_e],
\tag{3}
\]

and the intervals `I_e` partition `(Y,V]`. Define the positive forward workload area and its maximal forward defect by

\[
\mathcal W_+(C,D)
:=
\sum_e\int_{I_e}(\eta_e-s)_+\,ds,
\tag{4}
\]

\[
M_+(C,D)
:=
\max_e (\eta_e-u_e)_+.
\tag{5}
\]

Then, as `Y->infinity`,

\[
\boxed{
\mathcal W_+(C,D)
\ge
(1+o(1))h(C)Y^2\log Y,
}
\tag{6}
\]

and therefore

\[
\boxed{
L\,M_+(C,D)
\ge
(1+o(1))h(C)Y^2\log Y.
}
\tag{7}
\]

This is a one-sided recovery budget: negative workload cannot help lower the Robin height, and a short corridor must compensate by developing a large positive event defect.

## 1. The recovery budget is an immediate signed consequence of the exact quadrature identity

Put

\[
g(x)=\frac1{x\log x}.
\tag{8}
\]

`RE-109` gives, exactly,

\[
h(C)-h(D)
=
\sum_e\int_{I_e}
\bigl(g(s)-g(\eta_e)\bigr)\,ds.
\tag{9}
\]

Because `g` is decreasing, an integrand can be positive only when `s<eta_e`. For such `s`, since `s>=Y`,

\[
0<g(s)-g(\eta_e)
=
\int_s^{\eta_e}(-g'(t))\,dt
\le
(-g'(Y))(\eta_e-s),
\tag{10}
\]

where

\[
-g'(Y)
=
\frac{\log Y+1}{Y^2(\log Y)^2}
=
\frac{1+o(1)}{Y^2\log Y}.
\tag{11}
\]

Discarding every nonpositive contribution in (9) and using `h(C)-h(D)>=h(C)` gives

\[
h(C)
\le
(-g'(Y))\mathcal W_+(C,D),
\tag{12}
\]

which proves (6). For `s in I_e`,

\[
(\eta_e-s)_+
\le
(\eta_e-u_e)_+
\le M_+(C,D).
\tag{13}
\]

Since the total length of the intervals `I_e` is `L`,

\[
\mathcal W_+(C,D)\le L M_+(C,D),
\tag{14}
\]

and (7) follows.

No PNT estimate enters (6)--(7). Ties cause no difficulty: all atoms at one event coordinate may be grouped into one mass `m_e`, or equivalently the corresponding physical interval may be subdivided without changing the argument.

## 2. Adaptive selection fixes the initial workload scale

Now let `C=C_b` be one of the regular adaptive-amplitude maximizers from `RE-034`, with

\[
1-\Theta<b<\frac12,
\tag{15}
\]

and let `Z>Y` be its selector coordinate. Then

\[
\Phi(Z)=Y
\tag{16}
\]

and the selector defect

\[
d_0:=Z-Y
\tag{17}
\]

satisfies

\[
\boxed{
d_0=(b+o(1))h(C)Y\log Y.
}
\tag{18}
\]

Combining (6)--(7) with (18) gives the selection-conditioned forms

\[
\boxed{
\mathcal W_+(C,D)
\ge
\left(\frac1b+o(1)\right)Yd_0,
}
\tag{19}
\]

\[
\boxed{
L M_+(C,D)
\ge
\left(\frac1b+o(1)\right)Yd_0.
}
\tag{20}
\]

Hence

\[
\boxed{
\frac{M_+(C,D)}{d_0}
\ge
\left(\frac1b+o(1)\right)\frac YL.
}
\tag{21}
\]

The first event after the regular selector chamber already has forward defect larger than `d_0`, because its left physical coordinate is `Y` and its event coordinate lies to the right of `Z`. Equation (21) says much more when the recovery is fast: if

\[
L=o(Y),
\tag{22}
\]

then the maximal forward workload encountered before the Robin height becomes nonpositive must exceed the selector defect by an unbounded factor.

Thus endpoint selection is not merely compatible with the `RE-109` corridor. It fixes a small initial workload scale and forces any genuinely sublinear recovery to **amplify that workload after leaving the selected state**.

## 3. Near-minimal recovery forces one-sided saturation of the PNT envelope

Recall the event-sweep PNT estimate from `RE-109`,

\[
\Phi(x)
=
x+O\bigl(x\mathcal E(x)\bigr),
\qquad
\mathcal E(x)
=
\exp\!\left[-a(\log x)^{3/5}(\log\log x)^{-1/5}\right]
\tag{23}
\]

for some `a>0`.

Suppose the recovery corridor is sublinear, `L=o(Y)`. For a crossed event with positive forward defect, `u_e in [Y,V]=Y+o(Y)`. Equation (23), with the harmless left-limit jump absorbed into the error, then forces `eta_e~Y` and

\[
M_+(C,D)\ll Y\mathcal E(Y).
\tag{24}
\]

Substituting (24) into (7) recovers the `RE-109` lower bound

\[
L
\gg
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
\tag{25}
\]

The new information is the converse interpretation. Define, on a sublinear recovery corridor,

\[
\mathfrak R(C,D)
:=
\frac{L\mathcal E(Y)}{h(C)Y\log Y},
\qquad
\mathfrak S(C,D)
:=
\frac{M_+(C,D)}{Y\mathcal E(Y)}.
\tag{26}
\]

Then (7) gives

\[
\boxed{
\mathfrak R(C,D)\,\mathfrak S(C,D)\gg1,
}
\tag{27}
\]

while (24) gives `mathfrak S<<1`. Therefore `RE-109` is exactly the consequence obtained after forgetting the actual selected source phase and replacing `mathfrak S` by its unconditional supremum bound.

More importantly, if a recovery occurs within a fixed multiple of the natural `RE-109` scale,

\[
L
\ll
\frac{h(C)Y\log Y}{\mathcal E(Y)},
\tag{28}
\]

then

\[
\boxed{
M_+(C,D)\asymp Y\mathcal E(Y).
}
\tag{29}
\]

So a near-minimal recovery is possible only if at least one crossed event reaches a **positive full-event discrepancy of the same order as the complete unconditional PNT envelope**.

Conversely, any theorem on the CA-selected recovery intervals proving merely

\[
M_+(C,D)=o\bigl(Y\mathcal E(Y)\bigr)
\tag{30}
\]

would already force

\[
\mathfrak R(C,D)\to\infty,
\tag{31}
\]

and hence a strictly stronger inter-block separation than `RE-109`, without improving the global PNT error term at all. This is a concrete selection-conditioned source target.

## 4. The bound is sharp for the information currently retained

The product law (7) cannot be improved from endpoint selection plus a sup-norm discrepancy envelope alone. In a relaxed monotone event staircase, prescribe the selected starting defect `d_0` from (18), then allow the forward discrepancy to rise to a value `M` within the permitted envelope and keep it approximately constant across physical mass `L`. Using arbitrarily fine positive event masses, the recovery quadrature becomes

\[
\sum_e\int_{I_e}
\bigl(g(s)-g(\eta_e)\bigr)ds
=
(1+o(1))\frac{LM}{Y^2\log Y}
\tag{32}
\]

whenever `L,M=o(Y)`. Choosing

\[
LM\asymp h(C)Y^2\log Y
\tag{33}
\]

therefore realizes the recovery scale of (7). If `M asy Y E(Y)`, the construction also reproduces the `RE-109` corridor scale.

This control is deliberately a relaxed event staircase, not a claim that the ordinary primes or the CA event set realize such an excursion. Its role is adversarial: the initial adaptive selector relation and the global PNT envelope do not by themselves prevent the required amplification. Any further gain has to use arithmetic information about the **phase of the actual event discrepancy on the selected recovery interval**, not just its endpoint value or global supremum norm.

## 5. Prior-art boundary and research consequence

Mantovanelli's 2026 prime-layer workload preprint is the closest direct prior art. Its organizing packet identity already represents changes of the Robin quotient by integrating the exact CA workload against the Robin kernel. This finding does **not** claim novelty for that workload or for the packet identity. The line-specific step is to apply the positive part of the `RE-109` physical/event quadrature to a recovery from the quantitative adaptive witnesses of `RE-034`, producing the length-times-forward-defect budget (7), the selector-amplification law (21), and the envelope-saturation criterion (29).

The current Bhattacharya--Martin--Simpson work on correlations of weighted prime-counting errors is also an important boundary: it shows that standard and reciprocal prime errors carry strong joint information, and `RE-009` already records why global one-sided control of the corresponding mixed coordinate is RH-strength. It does not impose the one-sided full-event workload condition (30) on CA-selected recovery corridors.

No new external theorem is load-bearing here: the event-workload framework, Robin quantitative witnesses, and unconditional PNT envelope are already anchored in `SOURCES.md`.

The frontier after `RE-109` can therefore be stated more sharply. A fast inter-block recovery must not merely use a large generic PNT error; it must **build a positive full-event workload from the adaptive selector scale up to the PNT envelope during the recovery itself**. Excluding that selected one-sided saturation, even by an `o(1)` factor, would immediately strengthen the recurrence spacing. Proving such a selected-source anti-saturation statement is now a strictly more targeted goal than sharpening the unconditional PNT remainder.