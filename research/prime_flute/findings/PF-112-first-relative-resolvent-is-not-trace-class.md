# PF-112 — a first relative resolvent cannot be trace class under the non-isometric shift-clone marking

**Status:** `LITERATURE+DERIVED + NEGATIVE/BOUNDARY`. This closes one operator-ideal escalation of the accepted all-composite shift-clone clue. The microlocal input is classical: on a two-dimensional manifold, a compactly supported classical pseudodifferential operator of order `-2` with nonzero principal symbol has singular values of order `j^-1`, hence lies at the weak trace-class threshold rather than in `S_1`. The project-specific consequence is that no smooth non-isometric marked identification of the exact prime flute with its `p_n -> p_n+1` composite clone can make the **first resolvent difference** trace class. Compactness, global `S_p` for `p>1`, higher resolvent powers, relative heat operators, and scattering remain separate questions.

## Claim

Let `X` be the underlying smooth surface of the exact prime flute, let `g` be its hyperbolic metric, and let `g_+` be the exact all-composite shift-clone metric of PF-106 transported to `X` by a smooth marked diffeomorphism `F` that sends the canonical pants/cuff classes to their mates. Use the standard density unitary to put the two Laplacians on one Hilbert space, and write

\[
P_0=\Delta_g,
\qquad
P_1=U_F^{-1}\Delta_{g_+}U_F
\]

on `L^2(X,dvol_g)`. For any `lambda>0`, set

\[
R_i(\lambda)=(P_i+\lambda)^{-1},
\qquad
A_\lambda=R_1(\lambda)-R_0(\lambda).
\]

Then

\[
\boxed{A_\lambda\notin \mathcal S_1.}
\tag{1}
\]

More generally, (1) holds for any smooth geometrically induced common-manifold identification for which the transported metrics are not identical. In particular it holds for the canonical marked prime/shift-clone comparison, because PF-107 proves that corresponding distinguished cuff lengths differ:

\[
\ell_n^+-\ell_n=\frac{2}{p_{n-1}}+o(p_{n-1}^{-1}),
\]

so the marked surfaces cannot be isometric.

The obstruction is **local** and therefore cannot be repaired by faster decay of the deformation at infinity. If `chi` is a compactly supported cutoff around any point where `g_+ != g`, then

\[
\boxed{
\chi A_\lambda\chi
\in \Psi^{-2}_{\mathrm{cl}},
\qquad
s_j(\chi A_\lambda\chi)
= c_\chi j^{-1}+o(j^{-1}),
\quad c_\chi>0.
}
\tag{2}
\]

Hence `chi A_lambda chi` is not trace class. Since multiplication by bounded cutoffs preserves every Schatten ideal, global trace-class membership of `A_lambda` would contradict (2).

## 1. Local principal symbol of the relative resolvent

Conjugating a Laplace-Beltrami operator by the density unitary changes lower-order terms but not its second-order principal symbol. Thus

\[
\sigma_2(P_i)(x,\xi)=q_i(x,\xi):=|\xi|_{g_i}^2,
\]

where `g_0=g` and `g_1=F^*g_+` after the common-manifold identification.

Local elliptic parametrices give

\[
R_i(\lambda)\in\Psi^{-2}_{\mathrm{cl}}
\]

microlocally on every relatively compact coordinate patch. The resolvent identity

\[
R_1-R_0
=R_1(P_0-P_1)R_0
\tag{3}
\]

shows directly that the relative resolvent is again of order `-2`. Its leading homogeneous symbol is

\[
\begin{aligned}
a_{-2}(x,\xi)
&=q_1(x,\xi)^{-1}
   \bigl(q_0(x,\xi)-q_1(x,\xi)\bigr)
   q_0(x,\xi)^{-1}\\
&=q_1(x,\xi)^{-1}-q_0(x,\xi)^{-1}.
\end{aligned}
\tag{4}
\]

The spectral parameter `lambda` enters only at lower homogeneous order and therefore does not affect (4).

If `g_0` and `g_1` differ at a point `x_0`, their cotangent quadratic forms differ there. Hence (4) is nonzero for some nonzero covector at `x_0`; by smoothness it is nonzero on an open conic set. Choose `chi` supported in a small coordinate patch meeting that set. Then `chi A_lambda chi` is a compactly supported classical operator of order `-2` with nonvanishing order-`-2` principal symbol.

The noncompactness and infinite type of the ambient flute play no role in this step. After localization the operator may be embedded in a closed auxiliary surface, and the difference between the localized resolvent and its local parametrix is smoothing. The critical singular-value asymptotics are therefore the standard compactly supported pseudodifferential ones.

## 2. Dimension two is exactly the trace-class borderline

The Birman--Solomyak singular-value Weyl law for a compactly supported classical pseudodifferential operator `B` of negative order `-m` in dimension `d` gives

\[
s_j(B)\sim C(B)j^{-m/d}
\]

when the principal symbol is nonzero, with `C(B)>0` determined by the corresponding phase-space integral. For the localized relative resolvent here,

\[
m=d=2,
\]

and therefore

\[
\boxed{s_j(\chi A_\lambda\chi)\sim c_\chi j^{-1}.}
\tag{5}
\]

This is the critical weak-trace-class behavior familiar from Connes' trace theorem for order `-d` classical pseudodifferential operators. Equation (5) immediately implies

\[
\sum_j s_j(\chi A_\lambda\chi)=\infty,
\]

so the localized operator is not in `S_1`.

Now suppose, for contradiction, that the global relative resolvent `A_lambda` were trace class. Since multiplication by `chi` is bounded on `L^2`, the ideal property would imply

\[
\chi A_\lambda\chi\in\mathcal S_1,
\]

contradicting (5). This proves (1).

The argument is deliberately stronger than a tail estimate: **one non-isometric open patch is enough**. No amount of `ell^1` decay of endpoint, collar, area, or pant-local distortions can turn the first relative resolvent into a trace-class operator under a smooth geometric identification.

## 3. Why the prime/shift-clone marking is genuinely non-isometric

PF-106--PF-111 show that the exact shift clone is extremely close to the prime flute in several tail senses, but PF-107 also gives a direct marked obstruction to isometry. The canonical distinguished cuff class `gamma_n` has

\[
L_g(\gamma_n)=\ell_n,
\qquad
L_{g_+}(F_*\gamma_n)=\ell_n^+,
\]

with `ell_n^+ != ell_n` for all sufficiently large `n` and the explicit asymptotic above. A marked isometry would preserve every such length, so no diffeomorphism in the canonical marked class can pull `g_+` back to `g` identically.

Consequently there is at least one open set where the two transported metric tensors differ, and the microlocal obstruction of Sections 1--2 applies. The conclusion does not depend on whether the surviving global direct pants/collar gluing program eventually proves that the metrics are strongly equivalent at infinity.

## 4. What this closes in the accepted operator clue

The accepted clue `CLUE-affine-composite-clone-relative-operator-class.md` separates several operator gates. PF-112 closes one of them before the difficult infinite-end analysis is even reached:

\[
\boxed{
R_1(\lambda)-R_0(\lambda)\in\mathcal S_1
\quad\text{is impossible for the non-isometric metric comparison.}
}
\tag{6}
\]

Therefore an ordinary Fredholm-determinant or spectral-shift construction whose prerequisite is **trace class of the first resolvent difference** cannot be the surviving prime-sensitive object for this clone comparison. This is a generic two-dimensional microlocal obstruction, not an arithmetic effect.

The result is compatible with a positive answer to the weaker Georgescu--Golénia-style question of **compact** relative resolvent. An order-`-2` localized operator in dimension two is compact; the unresolved issue is whether the deformation at infinity preserves compactness globally. Likewise, the local pseudodifferential threshold allows `S_p` for every `p>1`; global membership in such ideals still depends on the infinite tail.

## 5. Higher resolvent powers and heat remain open operator gates

PF-112 must not be overextended. For an integer `m>=2`, the leading symbol of

\[
R_1(\lambda)^m-R_0(\lambda)^m
\]

has order `-2m`. In dimension two this lies strictly below the critical order `-2`, so the **local** trace-class obstruction disappears. Similarly, for each fixed positive time, localized heat operators are smoothing.

Thus the correct hierarchy after PF-112 is

```text
first resolvent difference
    -> locally critical order -2
    -> weak-S1 / S_p (p>1) scale
    -> never S1 when the metrics differ

higher resolvent powers or heat differences
    -> locally trace-class-compatible
    -> global tail summability still has to be proved

compact first resolvent difference
    -> not blocked microlocally
    -> remains the first global operator gate in the accepted clue
```

A relative determinant built from heat subtraction, higher resolvent powers, or another renormalized construction is therefore **not** ruled out by this finding. Its existence and arithmetic content would require separate hypotheses and, in view of PF-099--PF-111, an adversarial comparison against the all-composite clone.

## 6. Relevance to the RH search

The shift clone was introduced as a strong adversarial background because it carries no prime labels while matching the exact prime-flute tail extremely closely. A tempting next step was to hope that this closeness might place the full relative Laplacian directly in a trace-class perturbation regime and thereby produce a canonical Fredholm determinant whose zeros could be inspected.

PF-112 shows that this particular route is structurally mismatched to two-dimensional metric perturbations. The obstruction is present for **any** nontrivial smooth change of principal metric symbol, even on one compact patch. Therefore trace-class first-resolvent behavior cannot be interpreted as a delicate detector of prime-gap organization: it is unavailable before the arithmetic tail is considered at all.

The surviving question is narrower and cleaner. One may still ask whether the prime/clone metrics have compact relative resolvent, whether the global difference lies in some `S_p`, `p>1`, whether a higher-power/heat relative trace can be defined, and whether any resulting relative spectral shift or scattering quantity retains information not erased by the composite controls. Those are genuinely global questions; (6) prevents conflating them with first-resolvent trace class.

## 7. Prior art and novelty audit

No novelty is claimed for the microlocal theorem. The relevant classical sources are:

- M. Sh. Birman and M. Z. Solomyak, *Asymptotic behavior of the spectrum of pseudodifferential operators with anisotropically homogeneous symbols*, Vestnik Leningrad Univ. 13(3) (1977), 13--21; English translation, Vestnik Leningr. Univ. Math. 10 (1982), 237--247. This is a standard source for the negative-order pseudodifferential Weyl/singular-value asymptotics used in (5).
- M. Sh. Birman and M. Z. Solomyak, *Estimates for the singular numbers of integral operators*, Russian Math. Surveys 32:1 (1977), 15--89, DOI `10.1070/RM1977v032n01ABEH001592`, for the surrounding singular-number ideal theory.
- N. Kalton, S. Lord, D. Potapov, F. Sukochev, *Traces of compact operators and the noncommutative residue*, Advances in Mathematics 235 (2013), 1--55, DOI `10.1016/j.aim.2012.11.007`, for the critical order `-d` weak-trace-class / Connes-trace context.

The local pseudodifferential fact is therefore classical and substantially stronger prior art than any project-specific summability calculation. Directed searches did not locate the prime/cotangent shift-clone specialization, but that is not the novelty claim. The durable Mathia contribution is the **programmatic consequence**:

\[
\boxed{
\text{exact all-composite shift clone}
+
\text{non-isometric marked metric change}
+
\dim X=2
\Longrightarrow
\text{first relative resolvent cannot be }S_1.
}
\]

This redirects the accepted clue away from a first-resolvent trace-class determinant while leaving its compactness and higher relative-trace questions intact.

## 8. Audit / falsification core

The reusable audit is finite and independent of prime statistics:

1. place the two Laplacians on one `L^2` space by the marked diffeomorphism and density unitary;
2. verify that their order-two principal symbols are the inverse metric quadratic forms `q_0` and `q_1`;
3. use the local resolvent parametrix or (3) to obtain the order-`-2` symbol (4);
4. use PF-107 only to certify that the canonical marked metrics are not identical;
5. choose a compact cutoff where (4) is nonzero;
6. apply the classical negative-order singular-value Weyl law to obtain `s_j ~ c/j` with `c>0` in dimension two;
7. invoke the two-sided ideal property of `S_1` to rule out global trace-class membership.

A refutation would need to show that the common-manifold identification makes the two principal metric symbols identical everywhere, that the localized resolvent difference has lower order than (4), or that the cited critical singular-value asymptotics do not apply to the compactly supported localization. None of the endpoint/collar summability results can by themselves affect this local principal-symbol calculation.
