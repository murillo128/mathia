# ANF-126 — mesoscopic saddle chambers make subexponential growing mirrors excisable

**Status:** `EXACT-DERIVED + GROWING-PROFILE-EXCISION + MESOSCOPIC-SADDLE-CHAMBER + SUBEXPONENTIAL-UNSIGNED-BUDGET + DEGENERATE-COHERENT-SPAN-CLOSURE + EXTERNAL-COMPANION-GATE`. `ANF-123` shows that a low-budget `ANF-115` companion must bring its saddle toward the distinguished saddle, while `ANF-124`--`ANF-125` show that one or any fixed nondegenerate finite family of `A^{-1/2}`-coalescing profiles has a strict Gaussian coherence/projection gap. `ANF-125` deliberately leaves the singular limits in which phase-space points coalesce, coefficients grow, or the number of profiles tends to infinity. For the mirroring question, those singular coherent-state limits can be bypassed.

Take an arbitrary growing positive multiset of translated `ANF-115` packets whose saddles all remain in one shrinking macroscopic chamber around the distinguished saddle. If the **unsigned source budget is subexponential in `A`**, then one widening mesoscopic band captures the complete source norm of the entire aggregate before cancellation. Consequently, if the aggregate succeeds in cancelling itself on that band, its complete Montgomery--Taylor source norm is `o(1)` on the distinguished packet scale. Its fixed central-notch norm and its affine size are also negligible, so the whole aggregate is globally excisable from a near-extremizer.

Thus the tangent/Hermite and growing-span degeneracies left by `ANF-125` do not by themselves create an essential near-perfect mirror. They may realize increasingly delicate local cancellations, but **every successful subexponential mirror confined to the same macroscopic saddle chamber disappears as a whole**. A non-excisable completion must either recruit macroscopic saddle-band source from outside that chamber or pay an exponential unsigned source budget. The former is a genuinely external profile-coupling problem; for translated `ANF-115` packets separated from the chamber, `ANF-123` already quantifies the latter cost.

## 1. A uniform moderate-deviation band for all coalescing packet families

Use the exact `ANF-115` family indexed by an integer `n`. For a fixed `gamma_0>0`, put

\[
n_{0,A}=\lfloor\gamma_0A\rfloor,
\qquad
P_{0,A}:=P_{A,n_{0,A}},
\qquad
E_{0,A}:=E_0(P_{0,A}),
\qquad
 a_0:=a_{\gamma_0}.
\tag{1}
\]

For each `A`, let `J_A` be an arbitrary finite index set. For `j in J_A`, choose an integer `n_{j,A}>=1`, a real translation `tau_{j,A}`, and a positive integer multiplicity `w_{j,A}`. Write

\[
\gamma_{j,A}:=\frac{n_{j,A}}A,
\qquad
P_{j,A}:=P_{A,n_{j,A}}+\tau_{j,A},
\qquad
E_{j,A}:=E_0(P_{A,n_{j,A}}),
\tag{2}
\]

and form an aggregate containing the distinguished packet,

\[
T_A
:=
P_{0,A}\sqcup
\bigsqcup_{j\in J_A}w_{j,A}P_{j,A}.
\tag{3}
\]

Translations do not change individual source energies. Define the unsigned Hilbert budget

\[
\boxed{
\mathcal U_A
:=
1+
\sum_{j\in J_A}
 w_{j,A}
\sqrt{\frac{E_{j,A}}{E_{0,A}}}.
}
\tag{4}
\]

The square `mathcal U_A^2` is the analogue of the unsigned budget `mathfrak U_A` in `ANF-123`, normalized here to the distinguished packet rather than to the ambient affine scale.

Measure the largest saddle displacement in the natural Gaussian coordinate by

\[
\boxed{
 r_A
:=
\sqrt A\,
\max_{j\in J_A}
|a_{\gamma_{j,A}}-a_0|,
}
\tag{5}
\]

with `r_A=0` if `J_A` is empty. Assume

\[
\boxed{
 r_A^2+\log(e+\mathcal U_A)=o(A).
}
\tag{6}
\]

In particular every packet saddle converges to `a_0` macroscopically, but the displacement may be much larger than one Gaussian width, and both the number of packet families and their multiplicities may grow arbitrarily subject to the unsigned budget.

There is a sequence `S_A->infinity` such that

\[
S_A^2=o(A),
\qquad
r_A=o(S_A),
\qquad
\log(e+\mathcal U_A)=o(S_A^2).
\tag{7}
\]

For example, with

\[
Q_A:=1+r_A^2+\log(e+\mathcal U_A),
\]

one may take `S_A^2=sqrt(AQ_A)` after harmless enlargement at finitely many scales. Define the two-sided mesoscopic saddle chamber

\[
\boxed{
B_A
:=
\left\{
\alpha\in[-1,1]:
\bigl||\alpha|-a_0\bigr|
\le\frac{S_A}{\sqrt A}
\right\}.
}
\tag{8}
\]

The exact packet exponent from `ANF-115` is

\[
F_\gamma(x)
=x+2\gamma\log\cos\frac{\pi x}{2},
\qquad
F_\gamma''(x)
=-\frac{\gamma\pi^2}{2}
\sec^2\frac{\pi x}{2}.
\tag{9}
\]

Because (6) forces all `gamma_{j,A}` into one compact neighborhood of `gamma_0`, strict concavity is uniform there. The exact product formula, including the `A^{-2}3^{-k}` distinctness perturbations, therefore gives constants `C,c>0` such that for every admitted packet and every `1<=Y<=c sqrt(A)`,

\[
\boxed{
\frac{
 E_{\{\,||\alpha|-a_{\gamma_{j,A}}|>Y/\sqrt A\,\}}
 (P_{A,n_{j,A}})
}{E_{j,A}}
\le
C e^{-cY^2}.
}
\tag{10}
\]

A direct proof is enough. In a fixed interior neighborhood of the saddle, the exact density is a uniformly bounded positive prefactor times `exp(A F_gamma(alpha))`; uniform strong concavity bounds it by a Gaussian, while integration on one `A^{-1/2}` neighborhood of the saddle gives the matching denominator. Outside that fixed neighborhood there is a uniform exponential gap, and the endpoint estimate from `ANF-115` is stronger still. No coalescing-saddle asymptotic theorem is needed.

Since `r_A=o(S_A)`, every point outside `B_A` is eventually at least `S_A/(2 sqrt A)` from the saddle of every constituent packet. Hence

\[
\boxed{
\frac{E_{B_A^c}(P_{j,A})}{E_{j,A}}
\le
C e^{-cS_A^2}
}
\tag{11}
\]

uniformly in `j`, with the same statement for the distinguished packet.

## 2. Summing norms before cancellation controls an arbitrary growing mirror

The useful order of operations is the same cancellation-safe principle that appeared in `ANF-118`: estimate the nonnegative Hilbert norms of the individual pieces before using any expansion of the cancelling exponential sum.

Minkowski in the restricted Montgomery--Taylor source space gives

\[
\begin{aligned}
\sqrt{E_{B_A^c}(T_A)}
&\le
\sqrt{E_{B_A^c}(P_{0,A})}
+
\sum_j w_{j,A}
\sqrt{E_{B_A^c}(P_{j,A})}\\
&\le
C e^{-cS_A^2/2}
\sqrt{E_{0,A}}\,\mathcal U_A.
\end{aligned}
\tag{12}
\]

Therefore

\[
\boxed{
\frac{E_{B_A^c}(T_A)}{E_{0,A}}
\le
C e^{-cS_A^2}\mathcal U_A^2
=o(1),
}
\tag{13}
\]

by (7). This estimate is independent of the number of profiles, their mutual separation on the Gaussian scale, the conditioning of their coherent-state Gram matrix, and the size of the coefficients after cancellation. All of that complexity is compressed into the unsigned budget `mathcal U_A`.

Now suppose the aggregate realizes the local mirror condition

\[
\boxed{
E_{B_A}(T_A)=o(E_{0,A}).
}
\tag{14}
\]

Combining (13) and (14) gives the global conclusion

\[
\boxed{
E_0(T_A)=o(E_{0,A}).
}
\tag{15}
\]

This is the main excision implication. A growing or degenerating coherent-state span may indeed drive its mesoscopic saddle norm to zero, but under (6) there is no hidden source reservoir elsewhere in the spectrum capable of keeping that mirror aggregate essential.

Fix any central notch width `0<eta<a_0`. Because `S_A/sqrt A->0`, the support `|alpha|<=eta` is eventually contained in `B_A^c`. Since `0<=phi_eta<=J_0`, (13) immediately yields

\[
\boxed{
E_\eta(T_A)
\le E_{B_A^c}(T_A)
=o(E_{0,A}).
}
\tag{16}
\]

Thus successful cancellation in the common saddle chamber destroys both the complete source norm and the fixed-notch observable. This is stronger than a Gaussian Gram statement: it remains valid after the finite-dimensional Gram matrix becomes singular and after the number of coherent states tends to infinity.

## 3. The cancelled aggregate has negligible affine size and is globally excisable

The source-energy asymptotic also makes the physical size of `T_A` negligible. Write

\[
m_{j,A}:=|P_{A,n_{j,A}}|=2^{n_{j,A}+1}.
\]

Uniformly for `gamma_{j,A}` near `gamma_0`, the lower half of the same Laplace estimate gives

\[
E_{j,A}
\ge
cA^{-1/2}m_{j,A}^2e^{f_*A}
\tag{17}
\]

for some fixed `f_*>0`. Hence

\[
m_{j,A}
\le
CA^{1/4}e^{-f_*A/2}\sqrt{E_{j,A}}.
\tag{18}
\]

Summing before cancellation once more,

\[
\boxed{
|T_A|
\le
CA^{1/4}e^{-f_*A/2}
\sqrt{E_{0,A}}\,\mathcal U_A.
}
\tag{19}
\]

Because `log mathcal U_A=o(A)`, this is exponentially smaller than the ambient affine scale whenever the distinguished packet has bounded macroscopic source mass.

Precisely, let a global physical configuration split as

\[
W_A=T_A\sqcup R_A,
\qquad
\frac{E_0(W_A)}{L_A}=1+o(1),
\qquad
0<\lambda\le\frac{E_{0,A}}{L_A}\le\Lambda<\infty.
\tag{20}
\]

If (14) holds, then (15), (16), (19), and (20) give

\[
E_0(T_A)=o(L_A),
\qquad
E_\eta(T_A)=o(L_A),
\qquad
|T_A|=o(L_A).
\tag{21}
\]

Every point of every packet in `T_A` has nonzero imaginary part, so deleting `T_A` changes the affine denominator by exactly `2|T_A|`. The Hilbert triangle inequality gives

\[
\bigl|
\sqrt{E_0(R_A)}-\sqrt{E_0(W_A)}
\bigr|
\le
\sqrt{E_0(T_A)}=o(\sqrt{L_A}),
\tag{22}
\]

and the analogous estimate holds for the notch norm. Consequently

\[
\boxed{
\frac{E_0(R_A)}{L(R_A)}\to1,
\qquad
\frac{E_\eta(R_A)-E_\eta(W_A)}{L_A}\to0.
}
\tag{23}
\]

Thus `T_A` is globally excisable in exactly the sense relevant to the near-extremizer envelope of `ANF-099`.

There is also a useful decomposition corollary. Suppose a candidate high-efficiency configuration is written as

\[
W_A=T_A\sqcup D_A
\]

and the global source residual in `B_A` tends to zero on the distinguished scale. If

\[
E_{B_A}(D_A)=o(E_{0,A}),
\tag{24}
\]

then the reverse triangle inequality implies (14), so the whole growing coalescing aggregate `T_A` is excisable. Therefore a **non-excisable** completion must leave an external component `D_A` carrying macroscopic source norm in the same saddle chamber. The singular internal coherent-state geometry is not enough.

## 4. This closes the tangent/Hermite escape but not external cancellation

The result changes the boundary left explicitly open by `ANF-125`. If finitely many phase-space points remain nondegenerate, `ANF-125` already says that the mirror cannot become perfect. If points coalesce, coefficients grow, or the number of profiles grows, difference quotients can indeed generate Hermite-type tangent states and the finite Gram matrix may become singular. `ANF-126` says that none of those singular limits needs to be classified in order to decide **successful internal mirroring**: whenever they make (14) true with subexponential unsigned budget, (15)--(23) delete the entire construction.

This includes fixed `A^{-1/2}` coalescing families, finer-than-`A^{-1/2}` degeneracies, polynomially or subexponentially many packet components, and moderate saddle displacements satisfying `r_A=o(sqrt A)`. It also strictly enlarges the growth envelope of the same-family excision in `ANF-122`: the present argument permits `log mathcal U_A=o(A)` and varying packet parameters, because it uses a widening common chamber rather than a fixed-saddle Gaussian approximation to the complete modulation.

The assumptions have sharp qualitative boundaries. If `r_A^2=Theta(A)`, some packet saddle stays a fixed macroscopic distance from `a_0`, so no shrinking common band can contain all constituent source norms. If `log mathcal U_A=Theta(A)`, exponentially small tails can be amplified back to order one; the exact exponential translation clouds already seen in `ANF-118` and the wrong-saddle budget law of `ANF-123` show that this is a real mechanism, not a proof artifact. Finally, if an external component has macroscopic energy in `B_A`, it may cancel `T_A` without making `T_A` itself small; that is precisely the external profile-coupling problem retained by (24).

For external components that are themselves translated `ANF-115` packets with saddles separated from the chamber, `ANF-123` supplies the next step: making macroscopic energy available in the chamber requires an exponential unsigned source reservoir. Hence, within the packetized model, a fatal non-excisable completion is pushed toward a **cancellation cascade across macroscopic saddle chambers with exponential hidden budget**, rather than toward ever more delicate finite or growing coherent-state algebra near one saddle.

## 5. Prior-art boundary and research consequence

The analytical ingredients behind (10) are classical. Uniform Laplace/steepest-descent estimates for parameter-dependent nondegenerate saddles are standard; NIST DLMF §§2.3--2.4 records the relevant uniform-asymptotic discipline, including the need to change approximations when saddles or endpoints coalesce. Gaussian coherent states, their Fock-space realization, and Hermite/polyanalytic tangent structures are likewise classical neighboring language, as already audited in `ANF-125`. A targeted search found no theorem whose content is the Mathia-specific implication (13)--(23): the new step is to combine the exact `ANF-115` physical large-deviation landscape with the unsigned packet budget, Montgomery--Taylor source norm, and affine excision bookkeeping. No external theorem is load-bearing, so `SOURCES.md` does not change.

Two controls are important. The two-copy same-saddle mirror in `ANF-122` has bounded `mathcal U_A` and satisfies the present implication, recovering its excision without using the exact Gaussian Gram constant. At the opposite boundary, exponentially many positive translations can modify the macroscopic source rate and move the saddle, so replacing `log mathcal U_A=o(A)` by an unrestricted growth hypothesis is false.

The live completion problem is therefore narrower than the final paragraph of `ANF-125` suggested. Computing every tangent/Hermite Gram law is optional for classification of the local coherent geometry, but it is **not required to rule out an essential internally mirrored packet cluster**. What remains structurally relevant is external coupling: can a globally near-extremal physical configuration sustain macroscopic cancellation between different saddle chambers, or between an interior-saddle packet chamber and a qualitatively different source profile, without paying an exponential hidden source budget or exposing a removable subconfiguration? That is the next gate capable of changing the fixed-notch near-extremizer envelope.