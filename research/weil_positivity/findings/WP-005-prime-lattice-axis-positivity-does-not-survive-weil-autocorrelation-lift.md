# WP-005 — Prime-Lattice axis positivity does not survive the Weil autocorrelation lift

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. WP-004 gives a canonical positive Prime-Lattice operator whose spectral measure is exactly the finite Weil coefficient measure `Lambda(n)/sqrt(n)` on prime powers. The present finding closes the most direct next step: converting that positive measure into the Weil quadratic form through autocorrelation necessarily turns the axis weights into **off-diagonal translations**, and the resulting finite-prime operator is indefinite as soon as one prime shift is visible. Moreover, adding only commuting same-space Fourier-multiplier corrections cannot turn this into an exact positive realization of the full Weil form. A successful Prime-Lattice route therefore needs a genuinely noncommuting, compressed, boundary, different-space, or singular global operation that produces the archimedean/polar sector together with the finite data.

## 1. Claim

WP-004 constructs on the Prime-Lattice exponent Hilbert space the positive operator

\[
T=e^{-A/2}QAN^{-1}Q\ge 0,
\]

with

\[
T e_n=\frac{\Lambda(n)}{\sqrt n}e_n.
\]

Equivalently, its positive spectral measure against the height operator `A` is

\[
\mu_{\rm axis}
=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\,\delta_{\log n}.
\tag{1}
\]

This is exactly the positive-location finite coefficient measure in the centered Riemann explicit formula. However, Weil positivity is not positivity of the measure (1). For a logarithmic test function `f`, set

\[
\widetilde f(x)=\overline{f(-x)},
\qquad
h=f*\widetilde f.
\]

The finite-prime part of the standard Weil quadratic functional is

\[
W_{\rm fin}(f)
=-2\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re} h(\log n),
\tag{2}
\]

with only the terms meeting the support of `h` present. If `\tau_a f(x)=f(x-a)`, then

\[
2\operatorname{Re}h(a)
=\langle f,(\tau_a+\tau_{-a})f\rangle.
\]

Thus the exact autocorrelation lift of (1) is not the positive diagonal operator `T`; it is the translation operator

\[
\boxed{
C_L
=\sum_{\substack{n=p^k\\ \log n<2L}}
\frac{\Lambda(n)}{\sqrt n}
\bigl(\tau_{\log n}+\tau_{-\log n}\bigr),
}
\tag{3}
\]

on tests supported in `[-L,L]`, and

\[
W_{\rm fin}(f)=-\langle f,C_Lf\rangle.
\tag{4}
\]

For every `L>(log 2)/2`, `C_L` is indefinite already on smooth compactly supported tests in `[-L,L]`. Therefore

\[
\boxed{
T\ge0
\quad\not\Longrightarrow\quad
W_{\rm fin}\ge0;
}
\tag{5}
\]

indeed, the **correct** map from Prime-Lattice axis weights to the Weil quadratic form is not positivity-preserving.

There is a second obstruction. All translations in (3) are functions of the same additive generator `D=-i d/dx`,

\[
\tau_a=e^{-iaD}.
\]

Hence adding an archimedean correction only as another same-space Fourier multiplier `m_\infty(D)` stays inside one abelian operator algebra. A recent direct no-go theorem of Shoeib--Torky proves that no fixed positive same-space assembly of translations and Fourier multipliers can equal the full zeta Weil form on the full test-function class: after Fourier transform such a Gram form has an absolutely continuous spectral measure, whereas positivity of the Weil form would force the atomic zero-sampling measure.

So the surviving target is stricter than WP-004 stated: the missing completion must not merely add the correct gamma/pole **formula**. It must introduce a structural operation that breaks the commuting multiplier template and makes global positivity a theorem of that larger object.

---

## 2. The exact autocorrelation lift

Let

\[
w_n=\frac{\Lambda(n)}{\sqrt n},
\qquad a_n=\log n,
\]

for prime powers `n=p^k`. If `supp(f) subset [-L,L]`, then

\[
\operatorname{supp}(h)\subset[-2L,2L],
\]

so only finitely many prime powers with `a_n<2L` contribute to (2). No regularization is involved.

With the standard complex `L^2` inner product,

\[
h(a)+h(-a)
=2\operatorname{Re}h(a)
=\langle f,(\tau_a+\tau_{-a})f\rangle.
\]

Substituting this into the finite explicit-formula term gives (3)-(4). Thus there are two different operators attached to the same coefficients:

```text
Prime-Lattice coefficient operator:
    T e_n = w_n e_n                         positive, diagonal

Weil autocorrelation operator:
    C_L = sum_n w_n (tau_{a_n}+tau_{-a_n})  off-diagonal translations
```

The passage from the first line to the second is forced by the autocorrelation `h=f*tilde(f)`. Replacing `h(a_n)` by `|f(a_n)|^2` or by a diagonal norm of `T^(1/2)` would preserve positivity but would **change the Weil functional**.

This identifies exactly where the positivity of WP-004 is lost: not in the Mangoldt weights, but in the required correlation geometry.

## 3. Exact indefiniteness of every nontrivial finite prime comb

Fourier transform diagonalizes (3). Its multiplier is the finite trigonometric polynomial

\[
P_L(t)
=2\sum_{\substack{n=p^k\\ \log n<2L}}
\frac{\Lambda(n)}{\sqrt n}\cos(t\log n).
\tag{6}
\]

It has no zero-frequency term. Its Bohr mean is therefore zero, while

\[
P_L(0)
=2\sum_{\log n<2L}w_n>0
\]

whenever at least one prime power occurs. A nonzero continuous trigonometric polynomial with mean zero cannot be nonnegative everywhere. Hence `P_L` assumes both signs and `C_L` is indefinite on `L^2(R)`.

The support restriction does not rescue positivity. Fix any contributing shift `a=a_n<2L`. Because the finite set of other shifts is discrete, choose a nonzero smooth bump `u` with sufficiently small support and place two disjoint translates `u_-` and `u_+` inside `[-L,L]` with centers separated by exactly `a`, narrow enough that none of the other prime-power shifts couples the two bumps. Then

\[
f_+=u_-+u_+,
\qquad
f_-=u_--u_+,
\]

have opposite correlations at `a` and zero correlations at every other active nonzero shift. Consequently

\[
\langle f_+,C_Lf_+\rangle
=-\langle f_-,C_Lf_-\rangle
\ne0.
\]

Therefore `C_L` and `-C_L` are both indefinite on the actual compact-support seed space as soon as

\[
L>\frac{\log2}{2}.
\tag{7}
\]

This is the global Prime-Lattice analogue of the zero-diagonal obstruction in WP-001, but it is not the same statement. WP-001 ruled out an independently positive **single-prime Prime-Circle ray block**. Here all exact Prime-Lattice finite weights are first aggregated successfully into a positive measure, and the obstruction appears only when one performs the unavoidable **Weil autocorrelation lift** from that measure to a quadratic form.

## 4. Why a commuting archimedean multiplier is still not enough

Let `D=-i d/dx`. Since

\[
\tau_a=e^{-iaD},
\]

(3) belongs to the abelian von Neumann algebra generated by `D`. Any correction of the form

\[
m_\infty(D)
\]

for a real measurable symbol remains in the same algebra. After Fourier transform, the whole same-space operator is multiplication by one scalar symbol

\[
m(t)=m_\infty(t)-P_L(t)
\]

(or the corresponding cutoff-free limit when that is meaningful).

If such an operator supplied positivity by an ordinary Gram theorem, its form would be

\[
q_m(f)=\int_{\mathbb R}m(t)|\widehat f(t)|^2\,dt,
\qquad m(t)\ge0,
\tag{8}
\]

so its positive spectral measure is absolutely continuous with respect to Lebesgue measure.

Shoeib--Torky's 2026 Fourier-multiplier obstruction applies directly to this template. If (8) were exactly the zeta Weil form on `C_c^infinity(R)`, its positivity would imply RH by Weil--Bombieri. Under RH the same form is the discrete sampling form

\[
W_\zeta(f,f)
=\sum_\gamma m_\gamma|\widehat f(\gamma)|^2,
\tag{9}
\]

an atomic measure on the zero ordinates. An absolutely continuous measure cannot equal the nonzero atomic measure (9); a frequency-localizing sequence makes the contradiction exact. Thus

\[
\boxed{
\text{finite Prime-Lattice translations}
+
\text{commuting same-space archimedean multipliers}
\not\Rightarrow
\text{an exact positive Weil realization}.
}
\tag{10}
\]

This is a **prior-art redirect**, not a novelty claim for the general multiplier no-go. Its Mathia-specific consequence is that the most economical completion suggested by WP-004 is already in an excluded operator class.

The standard pole term also exposes the same boundary. In common normalizations the full compact-window Weil form contains a separate finite-rank/polar contribution in addition to the Fourier multiplier symbol. Such a term is not just another function of `D`. Therefore an exact global construction is expected to leave the commutative algebra anyway. Simply pasting the known pole term next to (8) would reproduce formula bookkeeping, not explain positivity; the research target is a geometry that **forces** the noncommuting/boundary piece and its sign.

## 5. Contemporary compact-window control

A useful matched control appeared independently in the current restricted-Weil literature. Chuk's August 2026 preprint writes, for tests supported in `[-L,L]`, the geometric-side symbol

\[
\Psi_L(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-\log\pi
-
\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n),
\tag{11}
\]

plus the polar term. The last summand is exactly `-P_L(t)` from (6), i.e. the autocorrelation lift of the WP-004 axis measure.

The same preprint gives a certified unconditional positivity result for the **assembled** Weil form on tests supported in `[-0.8,0.8]`. At that scale the prime comb is already nontrivial and, by the exact argument above, indefinite by itself. This is not used as proof of WP-005, but it is a strong control against the interpretation that the finite Prime-Lattice positivity should survive termwise: explicit finite-window positivity, where presently provable, is already a cancellation/dominance property of the **global archimedean + polar + prime** form.

The preprint also finds extremely small positive upper bounds for the window ground-state profile as `L` grows. That reinforces a practical novelty gate: proving positivity on one bounded window, or with a fixed cutoff, is not a substitute for a geometric mechanism uniform in the global limit.

## 6. Relation to WP-004 and WP-001

WP-004 remains correct and useful. It solved a problem the earlier branches did not:

\[
\text{canonical Mathia geometry}
\longrightarrow
\frac{\Lambda(n)}{\sqrt n}
\text{ on exactly the prime powers}.
\]

WP-005 says precisely what that success does **not** buy.

```text
WP-004:
    positive Prime-Lattice axis operator T
        -> exact finite Weil coefficient measure mu_axis

WP-005:
    Weil autocorrelation requirement
        -> replace diagonal samples by translations tau_log(n)
        -> finite prime operator C_L is indefinite
        -> commuting archimedean multiplier still lies in one abelian algebra
        -> same-space positive-multiplier realization is excluded by prior art
```

WP-001 and WP-005 therefore constrain two different levels:

- WP-001: a finite place cannot itself be an ordinary positive local Gram block with the exact Weil coefficients;
- WP-005: even a globally aggregated **positive coefficient measure** cannot transfer its positivity through the exact Weil autocorrelation operation, and a purely commuting multiplier completion remains structurally insufficient.

Together with the Beurling control in WP-004, this removes three increasingly strong shortcuts:

1. termwise local positivity;
2. positivity of the exact finite coefficient measure;
3. same-space commuting completion of that measure.

## 7. Prior art and novelty assessment

No novelty is claimed for the classical Weil autocorrelation form, for translation/Fourier diagonalization, or for the general same-space multiplier obstruction.

- Weil and Bombieri supply the explicit quadratic functional and its RH-equivalent positivity criterion.
- Connes--Consani's archimedean work already uses **compression** rather than a bare multiplier as the source of positivity, so it lies outside the excluded naive template in exactly the relevant way.
- Shoeib--Torky give a direct 2026 no-go theorem for fixed same-space assemblies of translations and Fourier multipliers, using the absolutely-continuous-versus-atomic spectral-measure mismatch. Their theorem is very close prior art and prevents any novelty claim for the general operator obstruction.
- Chuk's 2026 compact-window preprint independently displays the same finite Mangoldt cosine comb inside the full Weil symbol and provides a current control where the assembled form is positive while the finite comb alone is indefinite.

The durable Mathia result is the **identification of the natural WP-004 continuation with this excluded class**. The positivity in `T` is positivity of a coefficient operator on exponent space; the Weil test-function geometry forces those coefficients into translations, where the sign theorem disappears. This tells the research line exactly which extra structure must be genuinely new rather than another reformulation of the axis weights.

## 8. Boundary conditions and surviving escapes

WP-005 does **not** rule out Prime Lattice as finite boundary data for a successful global construction. It rules out a direct positivity transfer and the fixed same-space commuting-multiplier completion.

A surviving construction may escape by changing a substantive hypothesis, for example through:

- a canonical compression or quotient that does not commute with `D`;
- a boundary-value/scattering problem whose Dirichlet-to-Neumann or relative operator couples finite and archimedean sectors;
- a cohomological/intersection pairing on a different space;
- a finite-rank/polar component forced by the same geometry rather than appended from the explicit formula;
- a change of base measure or rigged Hilbert space;
- a genuinely singular concentration limit whose atomic output is proved, not assumed;
- a noncommutative or semilocal/adelic coupling in which the Prime-Lattice operator is only one boundary block.

These are escape routes, not evidence that such a Mathia construction exists.

The finding also does not say that every positive Fourier multiplier is useless. Such operators can prove restricted inequalities. What is excluded is claiming that positivity of a fixed same-space multiplier **is itself** the exact global Weil positivity mechanism.

## 9. Audit / falsification test

The exact Mathia portion can be checked without zero data:

1. start from WP-004 and verify the measure (1);
2. insert `h=f*tilde(f)` into the finite explicit-formula term;
3. verify `h(a)+h(-a)=<f,(tau_a+tau_-a)f>` and hence (3)-(4);
4. Fourier transform (3) to obtain the cosine comb (6);
5. use zero Bohr mean plus `P_L(0)>0`, or the two-bump construction, to prove indefiniteness whenever a prime shift is active.

The prior-art portion is falsified only if the quoted same-space multiplier theorem does not apply to the claimed class or if an equality between the positive multiplier form and the full Weil form avoids the absolutely-continuous/atomic measure mismatch without changing Hilbert space, base measure, compression, boundary conditions, or limiting regime.

A future Mathia construction **escapes** WP-005, rather than falsifies it, if it derives a principled noncommuting/global operation and proves that operation positive independently of RH while retaining the WP-004 finite boundary data.

## Consequence for the research line

The next target can now be stated more sharply than after WP-004:

\[
\boxed{
\text{Do not search for another positive diagonal realization of the Mangoldt weights.}
}
\]

Prime Lattice already has that. The required object must explain the transition

```text
positive axis measure
    -> indefinite arithmetic translations
    -> archimedean + polar coupling
    -> one globally positive form
```

with the **last two arrows forced by a noncommuting/global geometric theorem**, not by inserting the known explicit formula. Compression, boundary response, relative scattering, or cohomological/intersection structure remain plausible precisely because they cross the operator-class boundary identified here.