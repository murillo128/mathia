# ANF-116 — interior-saddle translation clusters collapse to one phasor and embed harmlessly in near-extremizers

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + INTERIOR-SADDLE-PHASE-REDUCTION + ROOT-OF-UNITY-RECYCLING + GLOBAL-NEAR-EXTREMIZER-EMBEDDING + FIXED-NOTCH-EXCISION`. `ANF-115` shows that exponentially source-unsaturated sub-square-root packets are genuinely realizable: a distinct conjugation-invariant packet can concentrate essentially all Montgomery--Taylor source mass at a stable interior spectral saddle `|alpha|=alpha_gamma<1` while retaining only logarithmic horizontal span. One possible response was to hope that the **global** near-extremizer condition would prevent such a packet from acquiring the macroscopic negative polarization required by the affine floor.

That response is false at component level. Real translations of an `ANF-115` packet act only by a Fourier phase, and the saddle concentration reduces every fixed finite translation cluster to a single phasor sum evaluated at `alpha_gamma`. In particular three nearby-disjoint translates whose limiting phases are the cubic roots of unity have pairwise source interaction

\[
\frac{\mathcal C_0(P_i,P_j)}{E_0(P_A)}\longrightarrow-\frac12
\qquad(i\ne j),
\]

while their **aggregate** source norm is `o(E_0(P_A))`. These three packets can be inserted, after a common horizontal translation, into an explicit physical Montgomery--Taylor near-extremizer built from a dilute simple-real core. Each packet individually remains source-heavy at ambient scale and retains the full exponential capacity deficit of `ANF-115`, yet all of the required macroscopic source cancellation can be supplied by the other two packets, with asymptotically negligible coupling to the core.

This does not create a fatal fixed-notch configuration. The phase-balanced triple is source-negligible as an aggregate and is therefore notch-negligible as well; deleting it preserves both near-extremality and fixed-notch exposure. The result instead sharpens the packet principle of `ANF-112`: **interior-saddle compensators must be analyzed after phase aggregation, not one component at a time.** Global near-extremality cannot forbid the `ANF-115` packet itself, because harmless phase crystals containing such packets occur inside genuine near-extremizing sequences.

## 1. Finite translation clusters reduce to one saddle phasor

Retain the `ANF-115` family. For fixed `gamma>0`, let

\[
P_A=\{x_S+iH_A,\ x_S-iH_A\},
\qquad
H_A=\frac{A}{4\pi},
\]

with cardinality `m_A`, source energy

\[
E_A:=E_0(P_A),
\]

and normalized source spectral measure

\[
d\nu_A(\alpha)
:=\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{E_A}\,d\alpha.
\tag{1}
\]

`ANF-115` proves

\[
\boxed{
\nu_A\Longrightarrow
\frac12\delta_{\alpha_\gamma}
+\frac12\delta_{-\alpha_\gamma},
}
\tag{2}
\]

where

\[
\alpha_\gamma
=\frac2\pi\arctan\frac1{\pi\gamma}
\in(0,1).
\tag{3}
\]

A real translation is exact phase modulation:

\[
S_{P_A+\tau}(\alpha)
=e^{-2\pi i\alpha\tau}S_{P_A}(\alpha).
\tag{4}
\]

Let `r` be fixed and choose real translations `tau_{j,A}->tau_j`, `1<=j<=r`. Put

\[
T_A:=\bigsqcup_{j=1}^r(P_A+\tau_{j,A}),
\qquad
p_A(\alpha):=
\sum_{j=1}^r e^{-2\pi i\alpha\tau_{j,A}}.
\tag{5}
\]

Whenever the copies are disjoint, `T_A` is again a finite conjugation-invariant physical multiset, and

\[
S_{T_A}(\alpha)=p_A(\alpha)S_{P_A}(\alpha).
\tag{6}
\]

Since `r` is fixed, `p_A` converges uniformly on `[-1,1]` to

\[
p(\alpha)=\sum_{j=1}^r e^{-2\pi i\alpha\tau_j}.
\]

Equations (1)--(2) therefore give the exact finite-cluster asymptotic

\[
\begin{aligned}
\frac{E_0(T_A)}{E_A}
&=\int |p_A(\alpha)|^2\,d\nu_A(\alpha)\\
&\longrightarrow
\frac{|p(\alpha_\gamma)|^2+|p(-\alpha_\gamma)|^2}{2}\\
&=\boxed{
\left|
\sum_{j=1}^r
 e^{-2\pi i\alpha_\gamma\tau_j}
\right|^2
}.
\end{aligned}
\tag{7}
\]

The last equality uses real translations, for which `p(-alpha_gamma)=overline{p(alpha_gamma)}`. Thus a potentially complicated finite union of exponentially large physical packets has, at leading Montgomery--Taylor source scale, only **one complex degree of freedom**: the vector sum of its translation phases at the interior saddle.

The corresponding pairwise polarization is just as simple. If

\[
\mathcal C_0(X,Y)
:=\operatorname{Re}\int J_0S_X\overline{S_Y},
\]

then (4) gives

\[
\frac{\mathcal C_0(P_A+\tau_{i,A},P_A+\tau_{j,A})}{E_A}
=
\int
\cos\!\bigl(2\pi\alpha(\tau_{j,A}-\tau_{i,A})\bigr)
\,d\nu_A(\alpha),
\]

hence

\[
\boxed{
\frac{\mathcal C_0(P_A+\tau_{i,A},P_A+\tau_{j,A})}{E_A}
\longrightarrow
\cos\!\bigl(2\pi\alpha_\gamma(\tau_j-\tau_i)\bigr).
}
\tag{8}
\]

In particular every target correlation in `[-1,1]` can be realized asymptotically by one relative translation. The relevant fact for the near-extremizer problem is that the affine-floor scale `-1/2` is not exceptional or difficult to reach: it is one ordinary phase angle.

## 2. Three cubic-root phases give pairwise minus-one-half interaction but negligible aggregate source

Set

\[
\tau_*:=\frac{1}{3\alpha_\gamma}.
\tag{9}
\]

We cannot simply assume that the three translates `P_A`, `P_A+tau_*`, `P_A+2tau_*` are disjoint for every finite `A`, because a translation could accidentally match one horizontal subset-sum difference. This is easily removed without changing the asymptotics. Let `X_A` be the finite set of horizontal centers of `P_A` and

\[
D_A:=X_A-X_A.
\]

The forbidden set

\[
D_A\cup\frac12D_A
\]

is finite. Hence one can choose

\[
\tau_A\to\tau_*
\tag{10}
\]

with `tau_A` outside that set. Then the three copies

\[
P_A^{(0)}:=P_A,
\qquad
P_A^{(1)}:=P_A+\tau_A,
\qquad
P_A^{(2)}:=P_A+2\tau_A
\tag{11}
\]

are pairwise disjoint and remain distinct physical packets. Their cardinality, maximal height, and internal horizontal span are unchanged up to an `O(1)` addition to the span.

At the saddle,

\[
e^{-2\pi i\alpha_\gamma\tau_*}=e^{-2\pi i/3},
\]

so the three limiting phases are the cubic roots of unity. Equation (8) gives, for every `i ne j`,

\[
\boxed{
\frac{\mathcal C_0(P_A^{(i)},P_A^{(j)})}{E_A}
\longrightarrow-\frac12.
}
\tag{12}
\]

Indeed differences of one step give `cos(2pi/3)=-1/2` and the two-step difference gives `cos(4pi/3)=-1/2`.

Let

\[
T_A:=P_A^{(0)}\sqcup P_A^{(1)}\sqcup P_A^{(2)}.
\tag{13}
\]

The phasor in (7) now vanishes:

\[
1+e^{-2\pi i/3}+e^{-4\pi i/3}=0.
\]

Consequently

\[
\boxed{
\frac{E_0(T_A)}{E_A}\to0.
}
\tag{14}
\]

The same conclusion follows directly by polarizing the three norms:

\[
E_0(T_A)
=3E_A+2\sum_{0\le i<j\le2}
\mathcal C_0(P_A^{(i)},P_A^{(j)}),
\]

and inserting (12). Equation (14) is fully compatible with the universal Montgomery--Taylor floor. The triple has affine size

\[
L(T_A)=2|T_A|=6m_A,
\]

whereas `ANF-115` has `E_A/m_A->infinity`; hence `6m_A=o(E_A)`. The aggregate is negligible only on the **ambient source-heavy scale**, not in violation of its own finite affine floor.

This is an explicit physical version of the recycling phenomenon that `ANF-111` identified abstractly. The difference is that here the recycling occurs inside the exact exponentially source-unsaturated interior-saddle chamber opened by `ANF-115`, and the pairwise interaction takes the canonical value `-1/2` rather than being an unspecified Hilbert-space control.

## 3. The phase-balanced triple embeds into an actual global near-extremizer

`ANF-115` normalized its packet against

\[
L_A:=\lceil E_A\rceil,
\qquad
R_A:=\frac{L_A}{m_A^2}\to\infty.
\tag{15}
\]

The finding deliberately did not claim that an arbitrary affine completion of one packet is globally near-extremal. The balanced triple removes that obstruction because its **aggregate** source norm is already negligible on the scale `L_A`.

Construct a simple-real dilute core with exactly `L_A` points. Choose any `d_A->infinity` and put

\[
C_A:=\{0,d_A,2d_A,\ldots,(L_A-1)d_A\}.
\tag{16}
\]

For a simple-real configuration the exact formula of `ANF-087` gives

\[
E_0(C_A)
=L_A+2\sum_{h=1}^{L_A-1}
(L_A-h)K(hd_A)^2,
\tag{17}
\]

where `K=widehat g` is the Montgomery--Taylor factor. Its explicit rational-trigonometric formula is continuous through its removable points and satisfies

\[
K(x)^2\le\frac{C_K}{1+x^2}
\qquad(x\in\mathbb R)
\tag{18}
\]

for some fixed constant `C_K`. Therefore

\[
0\le E_0(C_A)-L_A
\le
C L_A\sum_{h\ge1}\frac1{1+h^2d_A^2}
\ll\frac{L_A}{d_A^2},
\]

and hence

\[
\boxed{
E_0(C_A)=L_A+o(L_A).
}
\tag{19}
\]

To make the stronger component-level statement transparent, move the whole triple far from the real core by a common real translation `B_A`. A common translation does not change (12)--(14). For each fixed `A` and each `j`, the cross term

\[
\mathcal C_0(C_A,P_A^{(j)}+B)
\]

is the Fourier transform at `B` of an `L^1([-1,1])` function. Riemann--Lebesgue therefore lets us choose `B_A` so large that simultaneously

\[
\boxed{
|\mathcal C_0(C_A,P_A^{(j)}+B_A)|\le1,
\qquad j=0,1,2.
}
\tag{20}
\]

Put

\[
\widetilde T_A:=T_A+B_A,
\qquad
W_A:=C_A\sqcup\widetilde T_A.
\tag{21}
\]

The union is physical and conjugation-invariant. Since `R_A->infinity`,

\[
\frac{m_A}{L_A}\to0,
\]

and therefore

\[
L(W_A)=L_A+6m_A=L_A+o(L_A).
\tag{22}
\]

Equations (14), (19), and (20) give

\[
\begin{aligned}
E_0(W_A)
&=E_0(C_A)+E_0(\widetilde T_A)
+2\mathcal C_0(C_A,\widetilde T_A)\\
&=L_A+o(L_A).
\end{aligned}
\]

Thus

\[
\boxed{
\frac{E_0(W_A)}{L(W_A)}\to1.
}
\tag{23}
\]

So `W_A` is an explicit global Montgomery--Taylor near-extremizing sequence containing three copies of the `ANF-115` capacity-deficit packet.

Each individual copy remains macroscopic on the **ambient** source scale:

\[
\boxed{
\frac{E_0(P_A^{(j)}+B_A)}{L(W_A)}\to1,
\qquad j=0,1,2.
}
\tag{24}
\]

Its ambient sparsity ratio and capacity deficit are unchanged at leading order. Writing

\[
R_{j,A}:=\frac{L(W_A)}{m_A^2},
\qquad
M_{j,A}:=\frac{E_A}{L(W_A)},
\]

`ANF-115` and (22) give

\[
\frac{\log R_{j,A}}A\to f_\gamma,
\qquad
M_{j,A}\to1,
\]

and hence

\[
\boxed{
\frac1A
\log_+\!\left(
\frac{e^A}{R_{j,A}M_{j,A}A^2}
\right)
\to1-f_\gamma>0.
}
\tag{25}
\]

Thus exponential source-unsaturation occurs **inside actual global near-extremizers**, not merely in a locally normalized packet model.

Moreover, (12), (20), and (24) show that the core need not supply the packet's negative polarization. For example

\[
\boxed{
\frac{\mathcal C_0(P_A^{(0)}+B_A,
W_A\setminus(P_A^{(0)}+B_A))}{L(W_A)}
\to-1.
}
\tag{26}
\]

The two sibling packets supply `-1/2` each while the core contributes `o(1)`. The affine-floor conclusion that a source-heavy sublinear component must anti-align with its complement is therefore fully compatible with an interior-saddle capacity-deficit packet: the needed sign can be recycled entirely through finitely many phase-related siblings.

## 4. The same phase crystal is harmless for every fixed notch

Let `0<eta<1` be fixed and retain the admissible notch multiplier from the current ray,

\[
0\le\phi_\eta\le J_0,
\qquad
E_\eta(X)=\int\phi_\eta|S_X|^2.
\tag{27}
\]

Equation (14) immediately implies

\[
\boxed{
E_\eta(\widetilde T_A)
\le E_0(\widetilde T_A)
=o(L_A).
}
\tag{28}
\]

Since `E_eta(C_A)<=E_0(C_A)=O(L_A)`, Hilbert-space Cauchy--Schwarz gives

\[
|E_\eta(W_A)-E_\eta(C_A)|=o(L_A).
\]

Together with (22),

\[
\boxed{
h_\eta(W_A)-h_\eta(C_A)\to0.}
\tag{29}
\]

Thus the global embedding does not itself threaten the fixed-notch objective. The entire three-packet crystal is asymptotically excisable in exactly the packet sense of `ANF-112`.

There is nevertheless a sharper matched control inside the intermediate compensator chamber. `ANF-115` proves that for every fixed `eta` one may choose `gamma` with

\[
f_\gamma<\eta<\alpha_\gamma.
\tag{30}
\]

Then every **individual** translated packet satisfies

\[
\frac{E_\eta(P_A^{(j)})}{L(W_A)}\to0
\]

exponentially, while (24)--(25) say it is source-heavy and exponentially capacity-deficient. Consequently the pairwise notch cross terms are `o(L_A)` by Cauchy--Schwarz, whereas (12) gives

\[
\mathcal C_0(P_A^{(i)},P_A^{(j)})
=-\frac12L_A+o(L_A).
\]

Hence the macroscopic cancellation in this explicit global near-extremizer lives asymptotically in the notch-complement channel `J_0-phi_eta`, exactly where `ANF-107` says a notch-invisible source-heavy compensator must operate.

## 5. Adversarial checks and prior-art boundary

The conclusion does **not** use overlapping sites or hidden multiplicity. The ternary perturbation in `ANF-115` makes each packet distinct, and (10) avoids the finite difference set needed to keep the three translates pairwise disjoint. The later common translation `B_A` preserves all relative phases and cannot create real sites.

The aggregate collapse is also not an artifact of replacing a physical union by signed weights. Every coefficient in (6) arises from an actual positive-count translate of the same physical packet. The cancellation occurs only after Fourier phases are summed. The universal finite floor remains intact because the triple's own affine size is `o(E_A)`.

The real core is not assumed to be an exact finite equality configuration, which `ANF-087` rules out beyond two support sites. Its spacing `d_A->infinity` makes the positive off-diagonal real energy `o(L_A)`, which is exactly enough for near-extremality. No conjectural zero statistic or arithmetic input enters.

A targeted prior-art search across translation modulation, vanishing sums of roots of unity, Riesz-product concentration, and idempotent trigonometric-polynomial concentration found the expected mature general mechanisms. In particular, root-of-unity cancellation and the fact that translation becomes Fourier modulation are classical, and the concentration literature contains much richer trigonometric constructions than the elementary three-phase factor used here. No located result supplies the Mathia-specific combination of the `ANF-115` Montgomery--Taylor interior saddle, ambient affine normalization, component-level `-1/2` polarization, and explicit embedding into a global physical near-extremizer. No external theorem is load-bearing in the proof, so `SOURCES.md` does not change. This is a boundary assessment, not a blanket novelty claim.

The strongest possible overreading is explicitly false: (23) does **not** construct a fatal sequence for `beta_eta`, because (29) says the balanced packet cluster leaves fixed-notch exposure unchanged. Nor does the result show that every exponentially unsaturated packet in an arbitrary near-extremizer must belong to a finite translated crystal. It only provides a matched physical counterexample to any closure argument that tries to exclude an `ANF-115` packet from near-extremizers solely because the packet is source-heavy, interior-saddle localized, or requires macroscopic negative polarization.

## 6. Research consequence

The source-capacity-deficit frontier moves from **component existence** to **aggregate phase defect**. After `ANF-115`, one could still hope that global near-extremality itself would rule out the exponentially unsaturated packet. Equations (23)--(26) remove that route: the packet can occur at full ambient source scale inside a genuine near-extremizer, and its required anti-alignment can be supplied entirely by two phase-related siblings while the real core is asymptotically decoupled.

At the same time, equations (7) and (14) explain why this does not yet obstruct the fixed-notch program. A finite family of same-saddle translates is controlled at leading order by one complex phasor. If that phasor vanishes, the aggregate packet is source-negligible and should be excised as a whole; if it does not vanish, the aggregate retains macroscopic source mass and must itself satisfy the global polarization constraints of `ANF-112`--`ANF-113`.

The next useful theorem should therefore be formulated at **aggregate saddle-phase level**. A productive closure would show that every non-excisable interior-saddle packet aggregate in a fatal near-extremizer either develops a nonzero phase defect that cannot be cancelled by the unused physical remainder, is forced into a different saddle/height population that can be iterated, or loses the notch-exposure advantage needed to threaten `beta_eta`. Conversely, a genuine obstruction would require constructing a non-excisable phase aggregate whose global completion remains near-extremal while raising the fixed-notch exposure; isolated `ANF-115` packets and balanced finite phase crystals are no longer sufficient.