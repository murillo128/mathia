# RE-157 — PNT-small insertion placement squares the terminal ambiguity scale

**Status:** `EXACT-DERIVED + MATCHED-GENERALIZED-SOURCE-OBSTRUCTION + COARSE-PNT-SMALL + SHRINKING-TERMINAL-LAYER-THRESHOLD + PRIOR-ART-BOUNDED`. `RE-156` shows that equal-cardinality **ordinary-prime relocation** in the terminal layer

\[
T_p(\epsilon)=[(1-\epsilon)U_A(p),U_A(p)]
\]

has order-one source capacity only down to the fourth-root scale

\[
\epsilon_*(p)
=\sqrt{\frac{\log U_A(p)}{\sqrt p\log p}}.
\]

That transition is not a consequence of coarse prime-number-theorem information alone. It contains an additional local-supply constraint: every relocation requires an ordinary prime to delete, so only `Theta(epsilon U/log U)` labels are available in a layer of relative width `epsilon`.

If instead one asks what can be determined from the same exact source below the terminal layer plus only a coarse PNT-sized control on the remaining source, generalized-prime **insertions** have no corresponding local deletion cap. Their placement can retain order-one leverage down to the squared scale

\[
\boxed{
\epsilon_{\mathrm{PNT}}(p)
:=
\frac{\log U_A(p)}{\sqrt p\log p}
=
\epsilon_*(p)^2.
}
\tag{1}
\]

For

\[
U:=U_A(p)
=
\exp\!\left(A(\log p)^{5/3}(\log\log p)^{1/3}\right),
\qquad A>A_0,
\tag{2}
\]

this is

\[
\boxed{
\epsilon_{\mathrm{PNT}}(p)
=
A\,p^{-1/2}(\log p)^{2/3}(\log\log p)^{1/3}.
}
\tag{3}
\]

More precisely, let `delta=delta_p -> 0`, put

\[
m_p:=\left\lfloor \delta_p\frac{U}{\log U}\right\rfloor,
\tag{4}
\]

and compare controls obtained from the ordinary prime source by adding exactly `m_p` distinct non-prime real labels inside `T_p(epsilon)`, with no changes below `(1-epsilon)U`. If one packet is placed within `o(epsilon U)` of the left endpoint and the other within `o(epsilon U)` of `U`, then their normalized Robin source coordinates satisfy

\[
\boxed{
|\mathcal A_p(Q_p^-)-\mathcal A_p(Q_p^+)|
=
\left(\frac12+o(1)\right)
\delta_p\,
\frac{\epsilon_p}{\epsilon_{\mathrm{PNT}}(p)}.
}
\tag{5}
\]

Consequently:

- if `epsilon_p/epsilon_PNT(p) -> infinity`, any prescribed fixed source separation can be produced with `delta_p -> 0`, hence with a perturbation invisible to coarse PNT asymptotics;
- if `epsilon_p=O(epsilon_PNT(p))`, every insertion family using `o(U/log U)` terminal labels has `o(1)` placement leverage.

Thus `epsilon_PNT` is the sharp lower envelope for **coarse-PNT-small insertion placement**. For a fixed perturbation intensity `delta`, the crossover is instead `epsilon asymp epsilon_PNT/delta`; equation (1) is the asymptotic threshold obtained when the allowed PNT perturbation itself must vanish.

In particular, at the `RE-156` fourth-root scale `epsilon=epsilon_*`, order-one ambiguity survives with only `delta_p asymp epsilon_*(p) -> 0`. Therefore the fourth-root transition of `RE-156` is a genuine ordinary-prime local-supply phenomenon, not a PNT-only identifiability threshold.

## 1. Exact terminal influence inherited from RE-154 and RE-156

Retain the `RE-153` normalized source coordinate

\[
\mathcal A_p(Q)
:=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t),
\tag{6}
\]

and the exact influence of one added label `q<U` from `RE-154`:

\[
\Lambda_p(q)
=
\frac{\sqrt p\log p}{Z_p}
\log q\,\bigl(h(q)-h(U)\bigr),
\qquad
Z_p=2+o(1).
\tag{7}
\]

Adding `q` changes `A_p` by `-Lambda_p(q)`. `RE-156` differentiates the exact expression and obtains, uniformly for `q` in a shrinking terminal layer,

\[
-\Lambda_p'(q)
=
\left(\frac12+o(1)\right)
\frac{\sqrt p\log p}{U^2}.
\tag{8}
\]

Hence the full influence range across `T_p(epsilon)` is

\[
\boxed{
\Lambda_p((1-\epsilon)U)-\Lambda_p(U)
=
\left(\frac12+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}.
}
\tag{9}
\]

The important distinction from `RE-156` is that (9) itself does not contain a prime-density factor. That factor entered only when the number of usable source modifications was bounded by the ordinary primes available for deletion.

## 2. Same-cardinality insertion placement has a linear PNT budget

Let `Q_p^-` be obtained from the ordinary primes by adding `m_p` distinct non-prime real labels in an interval of width `o(epsilon U)` adjacent to `(1-epsilon)U`, and let `Q_p^+` add the same number of labels in an interval of width `o(epsilon U)` adjacent to `U`. The labels may be chosen distinct because a Beurling/generalized-prime control permits arbitrary increasing real labels greater than one; no ordinary-prime short-interval supply theorem is needed for the inserted points.

By additivity of (7), equal cardinality, and (9),

\[
\begin{aligned}
|\mathcal A_p(Q_p^-)-\mathcal A_p(Q_p^+)|
&=
\left(\frac12+o(1)\right)
 m_p\epsilon\frac{\sqrt p\log p}{U}\\
&=
\left(\frac12+o(1)\right)
\delta_p\epsilon
\frac{\sqrt p\log p}{\log U}.
\end{aligned}
\tag{10}
\]

Using (1), this is exactly (5):

\[
|\mathcal A_p(Q_p^-)-\mathcal A_p(Q_p^+)|
=
\left(\frac12+o(1)\right)
\delta_p\frac{\epsilon_p}{\epsilon_{\mathrm{PNT}}(p)}.
\tag{11}
\]

This gives a different capacity law from `RE-156`. Ordinary equal-cardinality relocation paid two factors of `epsilon`: one from the influence range and one from the number of ordinary primes available in the shrinking layer. Coarse-PNT insertion placement pays only the first factor; its cardinality budget can remain `o(U/log U)` independently of the layer width.

## 3. The controls are genuinely PNT-small

Each control differs from the ordinary source only after `(1-epsilon)U`, and at every `x`

\[
\boxed{
|\pi_Q(x)-\pi(x)|\le m_p
=\delta_p\frac{U}{\log U}+O(1)
=o\!\left(\frac{U}{\log U}\right).
}
\tag{12}
\]

Since every inserted label lies at `q=(1+o(1))U`, its logarithm is `log U+o(log U)`, so

\[
\boxed{
|\vartheta_Q(x)-\vartheta(x)|
\le
(1+o(1))m_p\log U
=(1+o(1))\delta_p U
=o(U).
}
\tag{13}
\]

Thus the perturbation is negligible at the selected PNT scale. For each fixed `p` the modification is finite, so eventual PNT asymptotics are also unchanged.

The two controls are even closer to one another after both packets have been passed. Their counting functions then agree exactly because the inserted cardinalities match. Their Chebyshev difference is only the difference between two sums of `m_p` logarithms whose arguments differ by a relative `O(epsilon)`, hence

\[
|\vartheta_{Q_p^-}(x)-\vartheta_{Q_p^+}(x)|
=O(m_p\epsilon)
=O\!\left(\delta_p\epsilon\frac{U}{\log U}\right)
\qquad(x\ge U).
\tag{14}
\]

Therefore the source separation in (11) is a placement effect inside the terminal layer, not a persistent discrepancy in total generalized-prime count.

## 4. Supercritical and subcritical regimes

Suppose first that

\[
\frac{\epsilon_p}{\epsilon_{\mathrm{PNT}}(p)}\longrightarrow\infty.
\tag{15}
\]

For any prescribed fixed `Delta>0`, choose

\[
\delta_p
=
(2\Delta+o(1))
\frac{\epsilon_{\mathrm{PNT}}(p)}{\epsilon_p}.
\tag{16}
\]

Then `delta_p -> 0`, while (11) gives

\[
|\mathcal A_p(Q_p^-)-\mathcal A_p(Q_p^+)|
\longrightarrow\Delta.
\tag{17}
\]

The number of inserted labels tends to infinity because `U_A(p)` is super-polynomially large relative to all the displayed inverse powers of `p`, so the packets can be chosen with the required endpoint concentration while remaining distinct.

Conversely, suppose two controls use `m_1,m_2=o(U/log U)` insertions in the terminal layer. By (9), every individual inserted label has influence between zero and

\[
\left(\frac12+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}.
\tag{18}
\]

Hence, whenever `epsilon=O(epsilon_PNT)`,

\[
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\le
(m_1+m_2)
\left(\frac12+o(1)\right)
\epsilon\frac{\sqrt p\log p}{U}
=o\!\left(\frac{\epsilon}{\epsilon_{\mathrm{PNT}}}\right)
=o(1).
\tag{19}
\]

This proves the claimed sharp lower envelope for insertion placement under the vanishing coarse-PNT budget. It does not say that all generalized-source perturbations are subcritical below `epsilon_PNT`; signed nonlocal compensations, changes outside the terminal layer, or constraints not expressible as insertion placement are outside the theorem.

## 5. Relation to the fourth-root transition

`RE-156` defines

\[
\epsilon_*(p)
=
\sqrt{\epsilon_{\mathrm{PNT}}(p)}.
\tag{20}
\]

At `epsilon=epsilon_*`, equations (11) and (20) give

\[
|\mathcal A_p(Q_p^-)-\mathcal A_p(Q_p^+)|
=
\left(\frac12+o(1)\right)
\frac{\delta_p}{\epsilon_*(p)}.
\tag{21}
\]

Thus choosing `delta_p asymp epsilon_*(p)` already produces order-one separation while `delta_p -> 0`. The ordinary-prime relocation class of `RE-156` is simultaneously at its maximal order-one capacity there because it must source deletions from only `Theta(epsilon_* U/log U)` ordinary primes.

The comparison isolates the source of the exponent change:

\[
\boxed{
\text{ordinary relocation: }
\epsilon^2\frac{\sqrt p\log p}{\log U},
\qquad
\text{PNT-small insertion placement: }
\delta\epsilon\frac{\sqrt p\log p}{\log U}.
}
\tag{22}
\]

The first law couples terminal width to **local ordinary-prime supply**; the second couples it only to the global perturbation intensity permitted by coarse PNT information. Therefore any argument that tries to turn propagation through the `RE-156` terminal layer into a positive Robin theorem must use more than `pi(x)~x/log x`, `theta(x)~x`, or a qualitatively vanishing PNT error. It needs a genuinely local terminal mass constraint, ordinary-prime/CA coupling, or a sharper signed source identity capable of distinguishing these matched controls.

## 6. Scope and prior-art boundary

This is a matched generalized-source obstruction, not a construction of an ordinary-prime counterexample to Robin and not a statement that the actual prime source admits arbitrary terminal insertions. It also does not address the observation-coordinate zero geometry. Its role is information-theoretic: it identifies what **cannot** be inferred from exact pre-terminal source agreement plus coarse PNT control alone.

Beurling generalized-prime systems and small perturbations of generalized-prime sequences are classical background, and the current `SOURCES.md` already contains the load-bearing PNT material used elsewhere in this line. A targeted audit of Beurling-prime perturbations, generalized PNT results, Robin/colossally-abundant formulations, and combinations of those topics did not locate the Robin-kernel placement law (11), the squared scale (1), or the comparison (22). No new external theorem is used in the proof, so no `SOURCES.md` update is required.

## Research consequence

`RE-156` found a fourth-root boundary for one very natural prime-only matched-control architecture. `RE-157` shows that this boundary should not be interpreted as the point where **PNT information** starts determining the terminal Robin source. Coarse PNT leaves enough generalized-source freedom to maintain order-one ambiguity all the way down to the parametrically smaller scale

\[
\epsilon_{\mathrm{PNT}}
=
\epsilon_*^2
\asymp
p^{-1/2}(\log p)^{2/3}(\log\log p)^{1/3}.
\]

Above that scale, source non-identifiability can coexist with a perturbation intensity tending to zero; at and below that scale, vanishing-budget insertion placement itself becomes subcritical. The remaining positive route must therefore supply local arithmetic rigidity that is absent from the PNT envelope, rather than merely sharpen the global prime-density approximation.