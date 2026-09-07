# WP-187 — Hardy compression splits the Gamma phase into positive Hankel defects, but its oriented commutator is indefinite

**Status:** `EXACT-DERIVED + TOEPLITZ-HANKEL-COMPRESSION + POSITIVE-DEFECT-SPLITTING + FINITE-WINDOW-INDEFINITENESS + CRITICAL-ROUGHNESS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-WEIL-POSITIVITY`.

`WP-186` leaves Toeplitz/Hankel compression as one of the genuinely nonlocal boundary mechanisms that might retain the signed motion of the exact Gamma phase after pointwise Gram positivity has erased it. The canonical Hardy compression can now be audited exactly.

Let

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})},
\qquad |R_\infty(t)|=1,
\tag{1}
\]

and transport its boundary values to the circle by the Cayley coordinate

\[
t=\tan(x/2),\qquad -\pi<x<\pi.
\tag{2}
\]

Write

\[
\phi_\infty(e^{ix})=R_\infty(\tan(x/2)).
\tag{3}
\]

On `H^2(T)`, let `P_+` be the Hardy projection, `P_-=I-P_+`, and define

\[
T_\phi=P_+M_\phi|_{H^2},
\qquad
H_\phi=P_-M_\phi|_{H^2}.
\tag{4}
\]

For **every** unimodular boundary symbol `phi`, not just the Gamma phase, the compression of the unitary multiplier has two canonical positive defect forms,

\[
\boxed{
D_{\rm in}(\phi):=I-T_\phi^*T_\phi=H_\phi^*H_\phi\succeq0,
}
\tag{5}
\]

and

\[
\boxed{
D_{\rm out}(\phi):=I-T_\phi T_\phi^*=H_{\bar\phi}^*H_{\bar\phi}\succeq0.
}
\tag{6}
\]

This gives a genuine nonlocal positive boundary geometry for `R_infty`: it measures the energy leaked across the Hardy polarization by the exact scattering multiplier. But the orientation-sensitive object is not either positivity theorem. It is their **difference**,

\[
\boxed{
[T_\phi^*,T_\phi]
=D_{\rm out}(\phi)-D_{\rm in}(\phi).
}
\tag{7}
\]

Complex conjugation reverses the phase and exchanges the two positive defects. Thus the signed orientation appears only after choosing an order and subtracting two positive energies.

For the Gamma phase this distinction is decisive. Every ordinary smooth finite-window localization of the phase has winding number zero; its Toeplitz self-commutator is trace class with trace zero but is nonzero, hence has **both positive and negative spectrum**. At the untruncated critical phase, the Cayley boundary symbol oscillates infinitely fast at the compactification point and fails the critical `H^{1/2}` regularity needed for both Hankel leakage energies to have finite trace. Therefore the obvious attempt to obtain the signed archimedean Weil response as a positive Toeplitz self-commutator fails in both regimes:

- smooth finite-window regularization makes the oriented commutator finite but indefinite;
- the exact full Gamma boundary makes the canonical positive-trace splitting singular, with at least one leakage energy of infinite trace.

The route is not completely dead: an individual Hankel defect is a canonical PSD operator and may still be useful if a separate source-forced finite--archimedean bridge identifies the **global Weil form itself** with such a defect or with a larger coercive object. What is closed is the direct claim that Hardy compression converts the signed Gamma phase velocity into positivity merely by taking the Toeplitz self-commutator or by subtracting its canonical positive leakage forms.

## 1. Exact positive-defect identities

For `f in H^2`, unimodularity gives

\[
\|M_\phi f\|_2^2=\|f\|_2^2.
\tag{8}
\]

Decompose `M_phi f` across the Hardy polarization:

\[
M_\phi f=P_+M_\phi f+P_-M_\phi f
=T_\phi f+H_\phi f.
\tag{9}
\]

Orthogonality of the two summands yields

\[
\|f\|_2^2
=\|T_\phi f\|_2^2+\|H_\phi f\|_2^2,
\tag{10}
\]

which is exactly (5).

Apply the same calculation to `bar phi` and use `T_phi^*=T_{bar phi}`. Then

\[
I-T_\phi T_\phi^*
=I-T_{\bar\phi}^*T_{\bar\phi}
=H_{\bar\phi}^*H_{\bar\phi},
\tag{11}
\]

proving (6). Subtraction gives (7).

No Gamma-function identity, RH hypothesis, zeta zero, or regularization enters (5)--(7). These are the standard Hardy-space compression identities for a unitary multiplication operator. Their relevance here is that `WP-186` had isolated Toeplitz/Hankel compression as a plausible way to add **nonlocal orientation** to the boundary projector. Equations (5)--(7) show exactly where that orientation lives.

Under phase reversal,

\[
\phi\longmapsto\bar\phi,
\tag{12}
\]

we have

\[
D_{\rm in}(\bar\phi)=D_{\rm out}(\phi),
\qquad
D_{\rm out}(\bar\phi)=D_{\rm in}(\phi),
\tag{13}
\]

and hence

\[
[T_{\bar\phi}^*,T_{\bar\phi}]
=-[T_\phi^*,T_\phi].
\tag{14}
\]

So any symmetric positive readout built only from the unordered pair of leakage energies is reversal-even, while the canonical reversal-odd object is their signed difference. This is the Toeplitz/Hankel analogue of the pointwise phenomenon in `WP-186`, but it is stronger because the defects are genuinely nonlocal operators rather than pointwise Gram matrices.

## 2. The inner-function control shows when the difference really can be positive

The fact that (7) is a difference of PSD operators does **not** imply that it is always indefinite. There is an important matched control.

Let `B` be a finite Blaschke product of degree `m`. Then `B` is inner, multiplication by `B` preserves `H^2`, and therefore

\[
H_B=0,
\qquad
D_{\rm in}(B)=0.
\tag{15}
\]

`T_B` is an isometry, while

\[
D_{\rm out}(B)
=I-T_BT_B^*
\tag{16}
\]

is the orthogonal projection onto the model space

\[
K_B=H^2\ominus BH^2.
\tag{17}
\]

Thus

\[
\boxed{
[T_B^*,T_B]=P_{K_B}\succeq0,
\qquad
\operatorname{rank}P_{K_B}=m.
}
\tag{18}
\]

The trace equals the winding/degree `m`. This is a genuine positive oriented Toeplitz commutator, but its sign comes from the **analytic inner orientation**: one of the two leakage channels vanishes identically.

This is the correct control for the Gamma phase. The obstacle is not a general theorem saying that Toeplitz commutators cannot be positive. They can. The issue is whether the exact `R_infty` boundary phase belongs to a source-forced one-sided analytic/passive regime of this kind. `WP-170`, `WP-184`, and `WP-185` already show that its exact analytic continuation is not an ordinary passive inner or bounded-characteristic channel. The finite-window test below gives an independent boundary-only obstruction to manufacturing the missing orientation by a regular cutoff.

## 3. Every ordinary smooth finite-window Gamma phase has an indefinite self-commutator

Choose a real smooth cutoff `chi_T in C_c^infty(R)` with

\[
\chi_T(t)=1\quad(|t|\le T),
\qquad
\chi_T(t)=0\quad(|t|\ge 2T).
\tag{19}
\]

Take the continuous real phase branch `theta_infty` with `theta_infty(0)=0` and

\[
R_\infty(t)=e^{i\theta_\infty(t)}.
\tag{20}
\]

Define the finite-window phase

\[
\phi_T(e^{ix})
=
\exp\!\left(
 i\,\chi_T(\tan(x/2))\,
 \theta_\infty(\tan(x/2))
\right).
\tag{21}
\]

Because `chi_T` vanishes before the Cayley compactification point, `phi_T` is a smooth unimodular function on the entire circle and is identically `1` near that point. Therefore

\[
\operatorname{wind}(\phi_T)=0.
\tag{22}
\]

For a smooth symbol, both Hankel operators in (5)--(6) are Hilbert--Schmidt, so the self-commutator

\[
C_T:=[T_{\phi_T}^*,T_{\phi_T}]
\tag{23}
\]

is trace class. Writing

\[
\phi_T(e^{ix})=\sum_{n\in\mathbb Z}a_n e^{inx},
\tag{24}
\]

the elementary Hankel-matrix calculation gives

\[
\operatorname{Tr}D_{\rm in}(\phi_T)
=\sum_{n\ge1}n|a_{-n}|^2,
\qquad
\operatorname{Tr}D_{\rm out}(\phi_T)
=\sum_{n\ge1}n|a_n|^2.
\tag{25}
\]

Hence

\[
\operatorname{Tr}C_T
=
\sum_{n\ge1}n\bigl(|a_n|^2-|a_{-n}|^2\bigr).
\tag{26}
\]

For smooth unimodular symbols, the classical Toeplitz/degree trace formula identifies (26) with the winding number. Thus (22) gives

\[
\boxed{\operatorname{Tr}C_T=0.}
\tag{27}
\]

For nontrivial `T`, `phi_T` is nonconstant. Brown--Halmos normality says that a normal scalar Toeplitz operator has symbol with essential range contained in an affine line. A nonconstant continuous unimodular `phi_T` has connected image containing a nontrivial arc of the unit circle, which is not contained in a line. Consequently

\[
C_T\ne0.
\tag{28}
\]

Now `C_T` is self-adjoint and trace class. If it were positive semidefinite, its trace would be strictly positive unless it vanished; if it were negative semidefinite, its trace would be strictly negative unless it vanished. Equations (27)--(28) therefore force

\[
\boxed{
C_T\text{ has both positive and negative spectrum.}
}
\tag{29}
\]

This is a decisive matched falsification of the most direct boundary proposal. Keeping any finite portion of the exact Gamma phase and returning smoothly to the trivial channel at infinity does not turn its orientation into a positive Toeplitz commutator. The signed response survives only as the difference of the two leakage energies in (7).

One could instead close the phase at infinity with an added integer winding. Then the trace in (27) would be that inserted integer. But the integer would come from the chosen closure, not from the finite Gamma window. Such a closure is exactly the kind of hand-picked global regularization excluded by the research mandate unless another Mathia structure forces it independently.

## 4. The exact Gamma phase is singular at the Hardy `H^{1/2}` trace threshold

The previous argument uses a smooth cutoff. The untruncated phase is more singular, and the singularity occurs precisely at the critical regularity controlling the sum of the two positive Hankel traces.

From `WP-186`,

\[
\theta_\infty'(t)
=\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right).
\tag{30}
\]

The standard digamma asymptotic gives, as `|t|->infinity`,

\[
\theta_\infty'(t)
=-\log\frac{|t|}{2\pi}+O(t^{-2}).
\tag{31}
\]

Approach the Cayley compactification point from the right-hand end of the interval by writing

\[
x=\pi-s,
\qquad
t=\cot(s/2),
\qquad s\downarrow0.
\tag{32}
\]

Let

\[
\Theta(s)=\theta_\infty(\cot(s/2)).
\tag{33}
\]

Since

\[
\frac{d}{ds}\cot(s/2)
=-\frac12\csc^2(s/2),
\tag{34}
\]

equations (31)--(34) imply

\[
\boxed{
\Theta'(s)
=
\frac{2\log(1/s)+O(1)}{s^2}
\qquad(s\downarrow0).
}
\tag{35}
\]

Thus the boundary phase has infinitely many oscillations accumulating at the single compactification point.

This already implies more than discontinuity. Put

\[
F(s)=e^{i\Theta(s)}.
\tag{36}
\]

For small `s`, define the local half-period

\[
\delta(s)=\frac{\pi}{\Theta'(s)}.
\tag{37}
\]

Equation (35) gives

\[
\delta(s)
\asymp\frac{s^2}{\log(1/s)},
\qquad
\frac{\delta(s)}s\longrightarrow0.
\tag{38}
\]

Differentiating the asymptotic also shows that the relative change of `Theta'` across an interval of length `O(delta(s))` tends to zero. Hence for all sufficiently small `s` there is a fixed `epsilon>0` such that, for

\[
r\in
[s+(1-\epsilon)\delta(s),\,
 s+(1+\epsilon)\delta(s)],
\tag{39}
\]

the phase difference `Theta(r)-Theta(s)` stays in a compact subinterval around `pi`. In particular there is a fixed `c>0` with

\[
|F(r)-F(s)|^2\ge c
\tag{40}
\]

throughout (39).

The critical fractional Sobolev seminorm therefore obeys the lower bound

\[
\begin{aligned}
[F]_{H^{1/2}}^2
&\gtrsim
\int_0^{s_0}
\int_{s+(1-\epsilon)\delta(s)}^{s+(1+\epsilon)\delta(s)}
\frac{|F(r)-F(s)|^2}{|r-s|^2}\,dr\,ds\\
&\gtrsim
\int_0^{s_0}\frac{ds}{\delta(s)}\\
&\asymp
\int_0^{s_0}\frac{\log(1/s)}{s^2}\,ds
=\infty.
\end{aligned}
\tag{41}
\]

Thus the exact Cayley boundary symbol satisfies

\[
\boxed{
\phi_\infty\notin H^{1/2}(\mathbb T).
}
\tag{42}
\]

This conclusion can be translated directly back to the two positive Hankel defects without invoking a general Schatten theorem. If

\[
\phi_\infty(e^{ix})
=\sum_{n\in\mathbb Z}a_ne^{inx},
\tag{43}
\]

then the Hankel matrix entries give

\[
\|H_{\phi_\infty}\|_{S_2}^2
=\sum_{n\ge1}n|a_{-n}|^2,
\qquad
\|H_{\bar\phi_\infty}\|_{S_2}^2
=\sum_{n\ge1}n|a_n|^2.
\tag{44}
\]

Adding them yields the `H^{1/2}` Fourier energy. Equation (42) therefore forces

\[
\boxed{
\operatorname{Tr}D_{\rm in}(\phi_\infty)
+
\operatorname{Tr}D_{\rm out}(\phi_\infty)
=\infty,
}
\tag{45}
\]

where at least one of the two positive traces is infinite.

Equation (45) is deliberately weaker than saying that both defects fail to be trace class, or that their difference cannot belong to a smaller operator ideal; neither stronger statement follows from the calculation above. What it does rule out is the naive full-phase version of (26) as a difference of **two finite canonical positive energies**. Any attempt to recover an oriented finite trace from the exact Gamma phase must introduce a singular cancellation, relative trace, Dixmier/Witten-type index, changing domain, or another renormalized operator framework. Such a framework is additional mathematics and must carry its own canonicity and sign theorem.

## 5. Why this does not yet yield a positive archimedean Weil form

The Toeplitz construction is more informative than the pointwise projector of `WP-186`. `D_in` and `D_out` are nonlocal, depend on the Hardy polarization, and can distinguish phases that have identical pointwise projector spectra. In particular it would be incorrect to say that Hankel leakage simply squares away all phase information.

What fails is narrower and more consequential for the branch mandate.

First, the positivity in (5)--(6) is universal compression geometry. Every unimodular symbol has both PSD defect forms. The theorem `D_in,D_out >=0` does not by itself distinguish the Gamma phase from an arbitrary phase.

Second, the canonical reversal-odd response is (7), a signed difference. The finite-window control proves that the exact Gamma motion does not make this difference semidefinite: once the phase is localized without inserting topological winding by hand, the self-commutator is necessarily indefinite.

Third, the untruncated phase does not repair that defect by a straightforward limit. It sits outside the finite two-sided Hankel-energy class (45). A singular limiting/index construction may still exist, but then the sign must be established in that singular category rather than inherited from finite positive traces.

Finally, this remains an archimedean boundary construction. Nothing in (5)--(45) produces Mangoldt support, mixed-prime incidence, the critical `p^{-1/2}` finite coefficient, or the polar terms. Even a successful one-sided Gamma Hankel energy would meet the research mandate only after the **same source geometry** couples that boundary defect to the finite arithmetic sector and proves positivity of the completed object independently of RH.

## 6. Prior art and novelty audit

The operator theory in this finding is classical.

- Arlen Brown and P. R. Halmos, *Algebraic Properties of Toeplitz Operators*, Journal für die reine und angewandte Mathematik 213 (1964), 89--102, DOI `10.1515/crll.1964.213.89`, is the classical Hardy-space Toeplitz reference, including the algebraic product/normality structure used in the finite-window test.
- Jani A. Virtanen, *On the Product Formula for Toeplitz and Related Operators*, in *Toeplitz Operators and Random Matrices*, Operator Theory: Advances and Applications 289 (2022), 605--616, DOI `10.1007/978-3-031-13851-5_26`, revisits the standard Toeplitz/Hankel product identities used in (5)--(7).
- Vladimir V. Peller, *Besov spaces in operator theory*, Russian Mathematical Surveys 79 (2024), no. 1, 1--52, DOI `10.4213/RM10140E`, surveys the classical characterization of Schatten-class Hankel operators by Besov regularity. The `S_2/H^{1/2}` boundary used here is also visible directly from the elementary Fourier matrix sums (44).
- Masaki Izumi, *A generalized winding number formula for the Witten index of a Toeplitz operator*, Journal of Spectral Theory 16 (2026), no. 1, 271--297, DOI `10.4171/JST/593`, is a current reference showing that generalized winding and trace formulae for singular Toeplitz settings are an active but already classical operator-index direction. It is a prior-art warning for any future attempt to relabel a renormalized Toeplitz/Witten index as Mathia-native Weil positivity.

No novelty is claimed for Toeplitz defects, Hankel operators, the winding trace formula, Brown--Halmos normality, or the `H^{1/2}`/Hilbert--Schmidt boundary.

The Mathia-specific delta is their application to the **exact `WP-169` Gamma scattering phase** and the combination of two tests that were not previously persisted in this line:

1. every source-preserving smooth finite-window localization has zero winding and therefore a nonzero **indefinite** Toeplitz self-commutator;
2. the exact untruncated Gamma phase has the asymptotic oscillation (35), which puts its Cayley boundary outside `H^{1/2}` and makes at least one canonical positive Hankel trace infinite.

Together these facts sharply delimit the Toeplitz/Hankel escape explicitly left open by `WP-186` without claiming a new theorem of operator theory.

## Consequence for the research line

Hardy compression does create a real positive object from the exact Gamma phase:

\[
R_\infty
\longmapsto
\bigl(D_{\rm in}(R_\infty),D_{\rm out}(R_\infty)\bigr),
\qquad
D_{\rm in},D_{\rm out}\succeq0.
\tag{46}
\]

But the orientation needed to distinguish the signed Gamma motion is

\[
D_{\rm out}-D_{\rm in},
\tag{47}
\]

not positivity of either defect. The inner-function matched control shows that (47) can be positive when analytic causality kills one leakage channel; the Gamma phase fails the corresponding ordinary passive/regular regime. Smooth finite-window Gamma phases make (47) rigorously indefinite, while the exact critical phase makes the two-positive-trace decomposition singular.

Therefore the direct boundary proposal

\[
\text{Gamma scattering phase}
\to
\text{Hardy compression}
\to
\text{positive Toeplitz self-commutator}
\to
\text{Weil sign}
\tag{48}
\]

is closed.

The surviving version is substantially narrower: a future mechanism may use **one** of the positive Hankel defects, a singular relative index, or a larger matrix/noncommutative compression, but only if Mathia independently forces the polarization/renormalization and couples it before scalarization to the finite-prime and polar sectors. The next useful test is therefore not another boundary-only positivity identity; it is whether a source-forced finite--archimedean coupling can enter the Hardy leakage operator itself so that the completed object has a coercive sign theorem before any signed defect subtraction.

## Dependencies

- `research/weil_positivity/findings/WP-169-pointed-nyman-relative-phase-is-exact-archimedean-scattering.md`
- `research/weil_positivity/findings/WP-170-archimedean-phase-is-not-a-passive-inner-boundary-response.md`
- `research/weil_positivity/findings/WP-184-gamma-phase-is-outside-bounded-characteristic-and-bounded-type-mobius-repairs-degenerate.md`
- `research/weil_positivity/findings/WP-185-gamma-phase-cannot-be-projective-coordinate-of-bounded-analytic-completion.md`
- `research/weil_positivity/findings/WP-186-boundary-gamma-phase-has-universal-positive-projector-lift-but-weil-density-is-indefinite.md`

## Bottom line

The Toeplitz/Hankel route left open by `WP-186` produces a canonical nonlocal positive geometry, but not the desired sign theorem. A unimodular boundary phase always yields two PSD Hardy leakage defects. Their difference is the oriented Toeplitz self-commutator. For every ordinary smooth finite-window localization of the exact Gamma phase, that commutator is nonzero, trace class, trace zero, and therefore indefinite. For the untruncated Gamma phase, the Cayley boundary oscillates at rate `~log(1/s)/s^2`, fails `H^{1/2}`, and forces at least one of the two positive leakage traces to diverge. The only clean positive control is the genuinely inner case, where one leakage vanishes and the commutator becomes the positive model-space projection.

So Hardy compression does not turn the exact Gamma phase velocity into Weil positivity for free. Any surviving use of this boundary mechanism must add a source-forced singular/global coupling with its own independent coercivity theorem, and that same object must still generate the finite-prime and polar parts of the global explicit formula.