# RE-038 — false RH forces coherent multi-threshold adaptive selector fans

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + SAME-BLOCK-MULTI-THRESHOLD-SELECTION + MONOTONE-CONVEX-ENVELOPE + EVENT-CHAMBER-OCCUPATION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-034`--`RE-037` fix one exponent `b` with `1-Theta<b<1/2` and show that hypothetical RH failure forces an adaptive CA-selected sequence satisfying an increasingly rigid standard/reciprocal prime-race relation. The fixed-`b` formulation leaves open an important coherence question: the quantitative theorem of Robin is valid for every admissible `b`, but the previous reductions allowed the selected CA states for different exponents to live on unrelated counterexample blocks.

They need not be treated independently. Fix a compact interval

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2).
\tag{1}
\]

Under RH failure, infinitely many **single Robin-counterexample blocks** carry an adaptive selector for every `b in J` simultaneously. Inside each such block these selectors form a monotone step function of `b`, equivalently the exposed vertices of one finite convex envelope. Moreover, every CA state that carries a nontrivial interval of threshold exponents has an exact local `b`-capacity determined by its adjacent CA supporting-slope gap:

\[
\boxed{
|I(C)|
=
\frac{Y_C\,(\varepsilon_-(C)-\varepsilon_+(C))}
     {1-e^{-h(C)}}.
}
\tag{2}
\]

Here `Y_C=log C`, `h(C)=log G(C)-gamma>0`, and `epsilon_- > epsilon_+` are the supporting slopes of the two adjacent CA transitions. If `eta_-<eta_+` are the corresponding event coordinates, then along large selected states

\[
\boxed{
|I(C)|
=(1+o(1))
\frac{\eta_+(C)-\eta_-(C)}
     {h(C)Y_C\log Y_C}.
}
\tag{3}
\]

Thus a fixed compact interval of admissible Robin exponents must be covered, on each of infinitely many individual counterexample blocks, by a family of CA chambers whose normalized occupation obeys

\[
\boxed{
 b_1-b_0
\le
(1+o(1))
\sum_{C\in\mathcal S_J(\mathcal B)}
\frac{\eta_+(C)-\eta_-(C)}
     {h(C)Y_C\log Y_C}.
}
\tag{4}
\]

Equivalently, if `b_C` is any exponent in the actual selection cell of `C` and `D_{b_C}(C)=Z_{b_C}(C)-Y_C` is its adaptive CA defect, then

\[
\boxed{
 b_1-b_0
\le
(1+o(1))
\sum_{C\in\mathcal S_J(\mathcal B)}
 b_C\,
\frac{\eta_+(C)-\eta_-(C)}{D_{b_C}(C)}.
}
\tag{5}
\]

This is a genuinely stronger false-RH obligation than independent fixed-`b` sequences. The finite spectral controls of `RE-033`--`RE-037` realize the target geometry for each fixed exponent separately; they have not yet realized the **same-block ordered fan** together with the chamber-capacity constraint (4)--(5). Conversely, (4) is not itself a contradiction: a long block may contain enough selected states to cover `J`. The new target is to control the total normalized CA-chamber occupation rather than one selected point at a time.

## 1. One quantitative block at `b_0` is quantitative for every larger exponent in `J`

For a CA state `C` with positive Robin excess put

\[
Y_C:=\log C,
\qquad
h_C:=\log G(C)-\gamma>0,
\qquad
R_C:=e^{h_C}-1>0,
\tag{6}
\]

and retain the adaptive amplitude of `RE-034`,

\[
A_b(C):=Y_C^bR_C.
\tag{7}
\]

Robin's quantitative false-RH theorem gives a constant `c_0>0` and infinitely many CA states `N` such that

\[
A_{b_0}(N)\ge c_0.
\tag{8}
\]

As in `RE-034`, these witnesses occur in infinitely many finite CA counterexample blocks. Fix one such block `\mathcal B` and one witness `N in \mathcal B`. For every `b>=b_0`, the *same state* satisfies the exact identity

\[
A_b(N)
=Y_N^{b-b_0}A_{b_0}(N)
\ge c_0Y_N^{b-b_0}.
\tag{9}
\]

Consequently, if

\[
M_{\mathcal B}(b)
:=\max_{C\in\mathcal B}A_b(C),
\tag{10}
\]

then

\[
\boxed{
M_{\mathcal B}(b)
\ge c_0Y_N^{b-b_0}
\qquad(b\in J).
}
\tag{11}
\]

No diagonal extraction over `b` is needed. Every sufficiently late block selected at the single left endpoint `b_0` already supports the whole interval `J`. In particular, all subsequent statements below live on the **same finite CA block**.

This point is easy to miss because Robin's Proposition 1 is normally invoked one exponent at a time. The nesting in (9) is purely algebraic and uses the specific scale-invariant amplitude selected in `RE-034`.

## 2. The blockwise adaptive selector is an exact monotone convex-envelope selector

On a fixed positive counterexample block define

\[
x_C:=\log Y_C,
\qquad
y_C:=\log R_C.
\tag{12}
\]

Then

\[
\log A_b(C)=y_C+bx_C.
\tag{13}
\]

Hence

\[
\boxed{
m_{\mathcal B}(b)
:=\log M_{\mathcal B}(b)
=\max_{C\in\mathcal B}(y_C+bx_C).
}
\tag{14}
\]

This is the upper envelope of finitely many affine functions of `b`. It is therefore convex and piecewise affine. Let `C_{\mathcal B}(b)` denote the **rightmost** maximizer in (10), using exactly the tie convention of `RE-034`. Since larger CA states have larger `Y_C` and therefore larger slopes `x_C`, the standard one-line convex-envelope argument gives

\[
\boxed{
b'<b''
\Longrightarrow
Y_{C_{\mathcal B}(b')}
\le
Y_{C_{\mathcal B}(b'')}.
}
\tag{15}
\]

Indeed, if the lower exponent selected a state with larger `x` than the higher exponent, adding the two maximizing inequalities would give `(b''-b')(x_{\rm high}-x_{\rm low})>=0`, a contradiction. At a breakpoint the rightmost tie convention chooses the largest slope, so

\[
\boxed{
m'_{\mathcal B,+}(b)
=\log Y_{C_{\mathcal B}(b)}.
}
\tag{16}
\]

Thus the adaptive states are not an unrelated collection indexed by `b`: they are the exposed vertices of a single finite point set `(x_C,y_C)` viewed under a rotating supporting direction `(b,1)`. The selector can only move to the right along the CA ladder as `b` increases.

The breakpoints are finite. Away from them the maximizer is unique, so the local adaptive-tangency argument of `RE-034` applies with no tie ambiguity. Breakpoints themselves have zero `b`-measure and are irrelevant for the occupation inequality below; no regularity claim at a breakpoint is needed.

## 3. Every selected state has an exact threshold-exponent capacity

Fix a state `C` that is the unique blockwise maximizer on a nonempty open interval of exponents. Put

\[
Y:=Y_C,
\qquad h:=h_C,
\qquad a:=1-e^{-h}>0.
\tag{17}
\]

Let `epsilon_- > epsilon_+` be the exact supporting parameters of the adjacent CA transitions into and out of `C`. For the adaptive barrier used in `RE-034`, the tangent parameter `Z_b(C)` is defined exactly by

\[
\boxed{
g(Z_b)
=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.
}
\tag{18}
\]

The CA state `C` is selected by this tangent only when that slope lies in its open supporting chamber,

\[
\varepsilon_+
<g(Y)-\frac{ba}{Y}
<\varepsilon_-.
\tag{19}
\]

Solving (19) for `b` gives the exact local admissibility interval

\[
\boxed{
I(C)
=
\left(
\frac{Y(g(Y)-\varepsilon_-)}a,
\frac{Y(g(Y)-\varepsilon_+)}a
\right).
}
\tag{20}
\]

In particular,

\[
\boxed{
|I(C)|
=
\frac{Y(\varepsilon_- -\varepsilon_+)}a,
}
\tag{21}
\]

which is (2). The actual blockwise selection cell of `C` is a subinterval of `I(C)`: global amplitude maximality can shorten the cell, but it cannot enlarge the local CA chamber allowed by (19).

Let

\[
\eta_-:=g^{-1}(\varepsilon_-),
\qquad
\eta_+:=g^{-1}(\varepsilon_+),
\tag{22}
\]

so `eta_-<eta_+`. The full CA event set contains the first-layer events, whose coordinates track consecutive primes up to the bounded event-location correction already used in `RE-003` and `RE-034`. The prime number theorem therefore gives, uniformly in the large regime,

\[
\eta_+-\eta_-=o(Y)
\tag{23}
\]

for any chamber containing one of the selected tangencies. `RE-034` also proves for every sufficiently large positive CA state that

\[
h\log Y\to0,
\qquad
a\sim h,
\qquad
Z_b/Y\to1
\tag{24}
\]

uniformly when `b` stays in a fixed compact subinterval of `(0,1/2)`. By the mean-value theorem,

\[
\varepsilon_- -\varepsilon_+
=-g'(\xi)(\eta_+-\eta_-)
\tag{25}
\]

for some `xi in (eta_-,eta_+)`, and (23)--(24) imply `xi/Y->1`. Since

\[
-g'(Y)
=\frac{\log Y+1}{Y^2(\log Y)^2}
\sim\frac1{Y^2\log Y},
\tag{26}
\]

equation (21) becomes

\[
\boxed{
|I(C)|
=(1+o(1))
\frac{\eta_+-\eta_-}{hY\log Y},
}
\tag{27}
\]

which proves (3).

Finally, for any `b` in the actual selection cell of `C`, `RE-034` gives

\[
D_b(C):=Z_b(C)-Y
=(b+o(1))hY\log Y.
\tag{28}
\]

Combining (27)--(28), uniformly for `b in J`,

\[
\boxed{
|I(C)|
=(b+o(1))
\frac{\eta_+-\eta_-}{D_b(C)}.
}
\tag{29}
\]

This is the geometric meaning of the capacity: a state can carry a wide interval of threshold exponents only if its CA supporting chamber is wide compared with the adaptive defect scale forced by its Robin height.

## 4. False RH forces a same-block chamber-occupation inequality

Let `\mathcal S_J(\mathcal B)` be the finite set of CA states that are the unique maximizer of `A_b` on some nonempty open subinterval of `J`. Their actual selection cells are disjoint and cover `J` except for finitely many breakpoint exponents. Each cell is contained in the corresponding `I(C)`. Therefore

\[
\boxed{
 b_1-b_0
\le
\sum_{C\in\mathcal S_J(\mathcal B)}|I(C)|.
}
\tag{30}
\]

For the sequence of blocks furnished by (8)--(11), all selected states tend to infinity. The estimates in (23)--(27) are uniform once the left edge of the block tends to infinity, so (30) yields

\[
\boxed{
 b_1-b_0
\le
(1+o(1))
\sum_{C\in\mathcal S_J(\mathcal B)}
\frac{\eta_+(C)-\eta_-(C)}
     {h(C)Y_C\log Y_C}.
}
\tag{31}
\]

Choosing arbitrarily one `b_C` from each nonempty actual selection cell and using (29) gives the equivalent defect form

\[
\boxed{
 b_1-b_0
\le
(1+o(1))
\sum_{C\in\mathcal S_J(\mathcal B)}
 b_C\,
\frac{\eta_+(C)-\eta_-(C)}{D_{b_C}(C)}.
}
\tag{32}
\]

Equations (31)--(32) are an unconditional geometric consequence **inside the conditional false-RH scenario**. They do not assume a dominant zero, linear independence of ordinates, a finite spectral packet, a prime-gap conjecture, or a bounded counterexample-block stretch.

The inequality also makes the remaining escape explicit. Even if every individual adaptive state occupies only a tiny `b`-interval because its event chamber is narrow compared with `D_b`, a sufficiently long counterexample block could contain enough exposed states for the sum in (32) to cover `J`. Thus one-state spacing estimates do not close the argument. A useful continuation must control the **total occupation** of the exposed adaptive states, or independently bound how many such states a single counterexample block can contribute.

## 5. Relation to the prime-race normal form

For every fixed non-breakpoint `b in J`, the selected states on the same block sequence satisfy the `RE-037` translated nonlinear relation

\[
V(Z_b)
-
\sqrt{Z_b}\log Z_b\,
\Psi_{b,\log Z_b}
\left(
\frac{U(Z_b)}{\sqrt{Z_b}\log Z_b}
\right)
=
\sqrt2\,\frac{2b-1}{b}+o_b(1).
\tag{33}
\]

The new point is not a sharper version of (33). It is that, on each of infinitely many individual counterexample blocks, the points satisfying the family (33) are coupled by the monotone selector (15) and by the chamber budget (31). The fixed-`b` finite-packet controls of `RE-033`--`RE-037` show that no single member of this family is spectrally impossible. They do **not** yet show that a single arithmetic CA block can realize the whole ordered fan for a compact continuum of exponents while paying the required total event-chamber occupation.

This suggests a stricter falsification control for the next spectral or selector argument. Constructing, for every fixed `b`, an admissible continuous prime-race point on the translated nonlinear curve is no longer enough to model the full false-RH implication. A matched control must preserve the cross-`b` ordering and either reproduce (31) or explain why the CA chamber geometry is irrelevant to the proposed obstruction.

A particularly concrete sufficient target would be an unconditional estimate on the selected exposed states of the form

\[
\sum_{C\in\mathcal S_J(\mathcal B)}
\frac{\eta_+(C)-\eta_-(C)}
     {h(C)Y_C\log Y_C}
< b_1-b_0-o(1)
\tag{34}
\]

for all sufficiently late positive CA blocks. By (31), such an estimate would contradict the quantitative false-RH implication. Nothing close to (34) is proved here; it is recorded because it is now an exact, source-specific occupation target rather than a qualitative request for finer selector placement.

## 6. Stress tests, prior art, and evidence boundary

Several possible overstatements were checked. First, no uncountable diagonal argument is used: (9) transfers one `b_0` witness to every larger exponent in the same finite block before any maximizer is chosen. Second, monotonicity (15) is exact finite convex geometry and does not assume smooth motion of the CA state. The selector is a step function and may switch many times. Third, regular adaptive tangency is invoked only inside open unique-maximizer cells; the finitely many tie exponents are discarded in the measure argument. Fourth, (31) does not bound the number of selected states and therefore does not by itself contradict RH failure or exclude arbitrarily stretched counterexample blocks.

The external ingredients remain those already anchored in `SOURCES.md`: Robin supplies the quantitative false-RH excursions; Alaoglu--Erdos supplies CA supporting slopes; the PNT supplies only the coarse `o(Y)` first-layer mesh needed for (23); and Mantovanelli bounds the event-coordinate representation as nearby prior art. A targeted current search also checked recent Robin/CA work on explicit counterexample windows, consecutive-CA transitions, and convex-envelope formulations. Those sources treat fixed Robin thresholds, fixed extremal parameters, or different convex envelopes; no source located in the audit couples Robin's whole admissible exponent interval through the scale-invariant amplitude (7) and derives the same-block chamber-capacity law (21)/(31). No new load-bearing theorem is introduced, so `SOURCES.md` does not need expansion.

The novelty claim is therefore deliberately narrow. The convex-envelope fact by itself is elementary, and no novelty is claimed for maximizing affine functions. The line-specific delta is the splice of that envelope with `RE-034`'s adaptive Robin amplitude and exact CA tangent chamber, producing a **coherent multi-threshold false-RH obligation on each of infinitely many single counterexample blocks**.

This finding does not prove that the occupation sum in (31) is small, does not show that finite zero packets fail the multi-`b` test, and does not prove a bound on counterexample-block length. It changes the live problem from independent one-parameter selector hits to a coupled family: either the same block must contain enough exposed CA chambers to cover every `b in J`, or RH failure cannot realize the quantitative Robin excursions simultaneously across the admissible exponent interval.