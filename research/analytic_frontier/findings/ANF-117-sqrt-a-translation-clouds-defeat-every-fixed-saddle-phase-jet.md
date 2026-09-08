# ANF-117 — sqrt-A translation clouds defeat every fixed saddle-phase jet

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SADDLE-GAUSSIAN-SCALING + SQRT-A-COHERENCE-THRESHOLD + PHASE-JET-HIERARCHY + FIXED-JET-NONCLOSURE + GLOBAL-NEAR-EXTREMIZER-CONTROL + FIXED-NOTCH-EXCISION`. `ANF-115` constructs exponentially source-unsaturated Montgomery--Taylor packets whose normalized source spectrum concentrates at a stable interior saddle `|alpha|=alpha_gamma<1`. `ANF-116` shows that every **fixed finite** family of real translates collapses at leading order to the single phasor sum evaluated at `alpha_gamma`; a zero phasor makes such a fixed cluster source-negligible.

That finite-cluster conclusion has a sharp mesoscopic boundary. The `ANF-115` saddle has spectral width `A^{-1/2}`. A root-of-unity translation cloud with `r_A` copies has an exact zero at the saddle, but its phase changes across the saddle window by order `r_A A^{-1/2}`. Consequently

\[
r_A=o(\sqrt A)
\quad\Longrightarrow\quad
\frac{E_0(T_A)}{E_A}\to0,
\]

whereas

\[
\frac{r_A}{\sqrt A}\to\rho>0
\quad\Longrightarrow\quad
\boxed{
\frac{E_0(T_A)}{E_A}
\longrightarrow
\frac{\rho^2}{\alpha_\gamma^2c_\gamma}>0,
}
\]

with

\[
c_\gamma:=-F_\gamma''(\alpha_\gamma)
=\frac{1+\pi^2\gamma^2}{2\gamma}.
\]

More strongly, for every fixed integer `s>=1` there is a positive physical translation multiset whose modulation polynomial has a zero of **exact order `s`** at both saddles, hence all saddle derivatives through order `s-1` vanish exactly, while its source energy remains a fixed positive fraction of `E_A`. These clouds remain sub-square-root in ambient population, retain the exponential source-capacity deficit of `ANF-115`, have only `O(A)` horizontal span, and remain exponentially invisible to every fixed notch lying strictly inside `alpha_gamma`.

Thus the aggregate-phase frontier cannot be closed by replacing the single phasor of `ANF-116` with any fixed finite saddle jet. The correct unresolved object is the full modulation profile on the mesoscopic coordinate

\[
u=\sqrt A\,(\alpha-\alpha_\gamma),
\]

or an equivalently strong physical invariant. The same root-of-unity recycling mechanism can cancel each fixed jet-level cloud inside an actual global near-extremizer, so finite-order phase bookkeeping is not merely incomplete in isolation; it is compatible with the affine-floor polarization constraints.

## 1. The ANF-115 saddle has a Gaussian `A^{-1/2}` local law

Retain the packet `P_A` of `ANF-115`, its source energy

\[
E_A:=E_0(P_A),
\]

and normalized source spectral measure

\[
d\nu_A(\alpha)
:=\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{E_A}\,d\alpha.
\tag{1}
\]

For fixed `gamma>0`, that finding identifies

\[
F_\gamma(\alpha)
=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2},
\qquad 0\le\alpha<1,
\tag{2}
\]

with unique maximizer

\[
\alpha_\gamma
=\frac2\pi\arctan\frac1{\pi\gamma},
\qquad
f_\gamma=F_\gamma(\alpha_\gamma).
\tag{3}
\]

Its curvature is

\[
F_\gamma''(\alpha)
=-\frac{\gamma\pi^2}{2}
\sec^2\frac{\pi\alpha}{2},
\]

so at the saddle

\[
\boxed{
c_\gamma:=-F_\gamma''(\alpha_\gamma)
=\frac{\gamma\pi^2}{2}+\frac1{2\gamma}
=\frac{1+\pi^2\gamma^2}{2\gamma}>0.}
\tag{4}
\]

The weak concentration `nu_A => (delta_{alpha_gamma}+delta_{-alpha_gamma})/2` from `ANF-115` can be sharpened locally without a new external input. On a fixed compact neighborhood of `alpha_gamma`, equations (6), (12), and (14) there give

\[
\log\!\left(
\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{m_A^2}
\right)
=A F_\gamma(\alpha)+b_A(\alpha),
\tag{5}
\]

where `b_A(alpha)-b_A(alpha_gamma)=o(1)` uniformly when `|alpha-alpha_gamma|=O(A^{-1/2})`. Indeed, the floor error `n_A-gamma A` is bounded, the ternary distinctness perturbations have total size `O(A^{-2})`, `J_0` is continuous and positive at the interior saddle, and the second exponential in the `cosh` factor is exponentially negligible there.

Taylor expansion gives, uniformly for bounded `u`,

\[
A\left[
F_\gamma\!\left(\alpha_\gamma+\frac{u}{\sqrt A}\right)
-f_\gamma
\right]
=-\frac{c_\gamma u^2}{2}+O\!\left(\frac{|u|^3}{\sqrt A}\right).
\tag{6}
\]

Strict concavity supplies a Gaussian majorant in a fixed saddle neighborhood, while the strict exponential gap away from the saddle and the endpoint estimate already proved in `ANF-115` control the complement. Hence, conditioning (1) on the positive saddle and putting

\[
U_A:=\sqrt A\,(\alpha-\alpha_\gamma),
\]

one obtains the local Laplace limit

\[
\boxed{
U_A\Longrightarrow
G_\gamma\sim N(0,c_\gamma^{-1}),
}
\tag{7}
\]

with convergence of every fixed polynomial moment. In particular

\[
\boxed{
\mathbb E G_\gamma^{2s}
=\frac{(2s-1)!!}{c_\gamma^s}
\qquad(s\ge1).
}
\tag{8}
\]

The negative saddle has the reflected identical law. Equation (7), rather than the point mass limit alone, is the scale needed to decide whether a growing translation aggregate is actually excisable.

## 2. A root-of-unity cloud has a sharp `sqrt A` coherence threshold

For an integer `r>=2`, define the positive translation polynomial

\[
p_r(\alpha)
:=\sum_{j=0}^{r-1}
\exp\!\left(-\frac{2\pi i\alpha j}{r\alpha_\gamma}\right).
\tag{9}
\]

It is realized by the physical multiset union of `r` translates

\[
T_{A,r}
:=\bigsqcup_{j=0}^{r-1}
\left(P_A+\frac{j}{r\alpha_\gamma}\right),
\qquad
S_{T_{A,r}}(\alpha)=p_r(\alpha)S_{P_A}(\alpha).
\tag{10}
\]

At the saddle the phases are all `r`th roots of unity, so

\[
\boxed{p_r(\alpha_\gamma)=p_r(-\alpha_\gamma)=0.}
\tag{11}
\]

For fixed `r`, the zero is simple. Differentiating the root sum gives

\[
\boxed{
|p_r'(\alpha_\gamma)|
=\frac{\pi}{\alpha_\gamma\sin(\pi/r)}.
}
\tag{12}
\]

Combining (7) with the first-order expansion of `p_r` therefore sharpens the qualitative `o(E_A)` conclusion of `ANF-116` to

\[
\boxed{
\frac{E_0(T_{A,r})}{E_A}
=\frac{\pi^2}
{\alpha_\gamma^2c_\gamma\sin^2(\pi/r)}\,
\frac1A
+o(A^{-1})
\qquad(r\ \text{fixed}).
}
\tag{13}
\]

The useful regime is when `r=r_A` grows. The exact geometric-series identity

\[
p_r(\alpha)
=\frac{1-e^{-2\pi i\alpha/\alpha_\gamma}}
       {1-e^{-2\pi i\alpha/(r\alpha_\gamma)}}
\tag{14}
\]

shows that, if `r_A/sqrt(A)->rho in (0,infinity)`, then uniformly for bounded `u`,

\[
\boxed{
p_{r_A}\!\left(
\alpha_\gamma+\frac{u}{\sqrt A}
\right)
\longrightarrow
\frac{\rho u}{\alpha_\gamma}.}
\tag{15}
\]

The same statement holds in modulus at the negative saddle. Since `|p_r|<=r=O(sqrt A)`, the exponential saddle gap dominates the polynomial prefactor outside the local window; (7)--(8) then give

\[
\boxed{
\frac{E_0(T_{A,r_A})}{E_A}
\longrightarrow
\frac{\rho^2}{\alpha_\gamma^2c_\gamma}.}
\tag{16}
\]

Conversely, the same local estimate yields

\[
r_A=o(\sqrt A)
\quad\Longrightarrow\quad
\frac{E_0(T_{A,r_A})}{E_A}\to0.
\tag{17}
\]

Thus `sqrt A` is the exact coherence scale at which an exact zero of the leading saddle phasor stops implying source excision. The issue is not failure of root-of-unity cancellation at the single frequency: (11) remains exact. The failure comes from resolving the `A^{-1/2}` spectral width around that frequency.

## 3. Every fixed finite saddle jet can vanish while macroscopic source survives

The one-zero example iterates inside the positive physical multiset class. Fix an integer `s>=1` and put `r_A=floor(rho sqrt(A))`. Define

\[
T_A^{(s)}
:=
\bigsqcup_{(j_1,\ldots,j_s)\in\{0,\ldots,r_A-1\}^s}
\left(
P_A+
\frac{j_1+\cdots+j_s}{r_A\alpha_\gamma}
\right).
\tag{18}
\]

Repeated shifts are retained with their positive multiplicities, which are admissible in the current physical multiset class. Its transform factorizes exactly as

\[
\boxed{
S_{T_A^{(s)}}(\alpha)
=p_{r_A}(\alpha)^sS_{P_A}(\alpha).
}
\tag{19}
\]

Because `p_{r_A}` has a simple zero at each saddle, `p_{r_A}^s` has exact order `s` there. Hence

\[
\boxed{
\frac{d^k}{d\alpha^k}
\bigl[p_{r_A}(\alpha)^s\bigr]_{\alpha=\pm\alpha_\gamma}
=0
\qquad(0\le k<s).
}
\tag{20}
\]

Nevertheless (15), (7), and (8) give the positive limit

\[
\boxed{
\frac{E_0(T_A^{(s)})}{E_A}
\longrightarrow
C_{s,\gamma}(\rho)
:=
\frac{\rho^{2s}(2s-1)!!}
     {\alpha_\gamma^{2s}c_\gamma^s}
>0.
}
\tag{21}
\]

The parameter `rho` can be chosen to realize any prescribed positive limiting source ratio. In particular one may normalize `C_{s,gamma}(rho)=1`.

These are still sparse interior-saddle packets in every ambient sense relevant to `ANF-113`--`ANF-116`. With `L_A=ceil(E_A)` and base cardinality `m_A`, `ANF-115` gives

\[
\frac1A\log\frac{E_A}{m_A}
\longrightarrow
\gamma\log2+f_\gamma>0.
\tag{22}
\]

Since `r_A^s=O(A^{s/2})`, equations (18) and (22) imply

\[
\boxed{
|T_A^{(s)}|
=r_A^s m_A
=o(\sqrt{L_A})
=o(L_A).
}
\tag{23}
\]

The additional translation range in (18) is less than `s/alpha_gamma`, so the horizontal span remains `O(A)`, and the maximum height remains exactly `A/(4pi)`. Moreover

\[
R_A^{(s)}
:=\frac{L_A}{|T_A^{(s)}|^2}
=\frac{L_A/m_A^2}{r_A^{2s}},
\]

so

\[
\frac1A\log R_A^{(s)}\to f_\gamma.
\tag{24}
\]

Thus multiplying the number of translates by any fixed power of `sqrt A` changes only logarithmic factors and preserves the same exponential source-capacity-deficit rate `1-f_gamma` found in `ANF-115`.

Equation (20) gives the decisive obstruction. For every fixed jet depth `J`, choose `s=J+1`. The aggregate modulation then has exactly the same zero jet

\[
(p,p',\ldots,p^{(J)})|_{\pm\alpha_\gamma}=0
\]

as a perfectly canceled profile, while (21) says it retains macroscopic Montgomery--Taylor source energy. Therefore **no criterion based only on vanishing of a fixed finite number of saddle derivatives can certify source excision**. The jet depth would have to grow with the scale, or be replaced by direct control of the complete `u=sqrt(A)(alpha-alpha_gamma)` profile.

## 4. Fixed jet-level source can itself be phase-recycled inside global near-extremizers

The obstruction is compatible with the global affine floor, not merely with an isolated packet. Normalize the source measure of `T_A^{(s)}` by

\[
d\mu_{s,A}(\alpha)
:=
\frac{J_0(\alpha)|S_{T_A^{(s)}}(\alpha)|^2}
     {E_0(T_A^{(s)})}\,d\alpha.
\tag{25}
\]

The local proof of (21) shows more than weak concentration: on the positive saddle, the scaled density is proportional to

\[
|u|^{2s}e^{-c_\gamma u^2/2}.
\]

In particular

\[
\mu_{s,A}\Longrightarrow
\frac12\delta_{\alpha_\gamma}
+\frac12\delta_{-\alpha_\gamma}.
\tag{26}
\]

Now set

\[
\tau_*:=\frac1{3\alpha_\gamma}
\]

and take three common translations

\[
T_A^{(s,0)}=T_A^{(s)},
\qquad
T_A^{(s,1)}=T_A^{(s)}+\tau_*,
\qquad
T_A^{(s,2)}=T_A^{(s)}+2\tau_*.
\tag{27}
\]

By (26), exactly as in the finite-cluster polarization step of `ANF-116`, every pair satisfies

\[
\boxed{
\frac{\mathcal C_0(T_A^{(s,i)},T_A^{(s,j)})}
     {E_0(T_A^{(s)})}
\longrightarrow-\frac12
\qquad(i\ne j).
}
\tag{28}
\]

Their aggregate modulation acquires the extra factor

\[
b(\alpha)
:=1+e^{-2\pi i\alpha\tau_*}
+e^{-4\pi i\alpha\tau_*},
\qquad
b(\pm\alpha_\gamma)=0.
\tag{29}
\]

Since this is a simple zero and the relevant spectral window has width `A^{-1/2}`, the same local Gaussian estimate gives

\[
\boxed{
E_0\!\left(
T_A^{(s,0)}\sqcup T_A^{(s,1)}\sqcup T_A^{(s,2)}
\right)
=O(E_A/A)
=o(E_A).
}
\tag{30}
\]

Thus the entire three-cloud aggregate is source-negligible even though each cloud separately has source norm `C_{s,gamma}(rho)E_A+o(E_A)` and vanishes through `s-1` saddle derivatives.

It can therefore be embedded into an actual near-extremizer by the same physical construction as `ANF-116`. Take a dilute simple-real core with `L_A` points and spacing tending to infinity, so its source energy is `L_A+o(L_A)`. The three clouds have total affine size

\[
6r_A^s m_A=o(L_A)
\]

by (22). A common real translation tending sufficiently far from the core makes their finitely many core cross terms `o(L_A)` by Riemann--Lebesgue. Equations (21), (28), and (30) then produce a global physical sequence `W_A` with

\[
\boxed{
\frac{E_0(W_A)}{L(W_A)}\to1,
}
\tag{31}
\]

containing three individually source-heavy `s`-jet clouds whose required negative polarization is recycled entirely among their siblings. As in `ANF-116`, the aggregate is excisable even though its components are not.

## 5. The phase-jet clouds remain invisible to a fixed interior notch

Let `0<eta<alpha_gamma` be fixed and retain the notch energy `E_eta`. `ANF-115` proves an exponential gap

\[
\frac{E_\eta(P_A)}{E_A}
=\exp\!\left(-c_{\eta,\gamma}A+o(A)\right)
\qquad(c_{\eta,\gamma}>0).
\tag{32}
\]

Since `|p_{r_A}(alpha)|<=r_A`, equation (19) gives

\[
E_\eta(T_A^{(s)})
\le r_A^{2s}E_\eta(P_A).
\]

The factor `r_A^{2s}=O(A^s)` is only polynomial, so (21) and (32) yield

\[
\boxed{
\frac{E_\eta(T_A^{(s)})}{E_A}\to0,
\qquad
\frac{E_\eta(T_A^{(s)})}{E_0(T_A^{(s)})}\to0.
}
\tag{33}
\]

For the stronger `ANF-115` chamber one may choose `gamma` so that `f_gamma<eta<alpha_gamma`; then these clouds simultaneously lie above the max-height notch-possibility threshold, remain exponentially source-unsaturated, carry macroscopic source energy, and still carry asymptotically no fixed-notch energy. Their outer phase-balanced triple is source-negligible by (30), hence notch-negligible as well.

Thus the construction does not produce a fatal sequence for `beta_eta`. It instead shows that arbitrarily deep but fixed saddle-phase cancellation can coexist with the exact compensator geometry already admitted by global near-extremality.

## 6. Adversarial checks and prior-art boundary

The `sqrt A` scale is not inserted heuristically. It is forced by the product of two exact scales: the `A^{-1/2}` Gaussian width from the curvature (4) and the order-`r` slope of the root cloud at its exact saddle zero. Equation (14) verifies the crossover directly and avoids assuming that a fixed-`r` Taylor expansion remains uniform when `r` grows.

The construction uses positive multiplicities in (18); no signed coefficient is introduced. Repeated translation sums are therefore physical multisets under the current Montgomery--Taylor model. This finding does **not** claim an analogous all-distinct realization of the higher-order clouds. Any future rigidity theorem that genuinely uses distinctness or simplicity would require a separate control. The base packet itself remains the distinct `ANF-115` packet.

No uncontrolled saddle tail is hidden in (21). The translation factor has at most polynomial size `r_A^s=O(A^{s/2})`, whereas `ANF-115` supplies a fixed exponential gap away from `+-alpha_gamma`. Inside a fixed saddle neighborhood, strict concavity gives an integrable Gaussian majorant after `sqrt A` rescaling, so the polynomial moments in (8) are uniformly integrable.

The general ingredients are classical: finite root-of-unity sums are Dirichlet-kernel/geometric-series objects, their exact cancellation is elementary cyclotomic structure, and the Gaussian local law is ordinary Laplace asymptotics at a nondegenerate maximum. The existing `SOURCES.md` already anchors the Montgomery--Taylor pair-correlation extremal setting through Carneiro--Chandee--Littmann--Milinovich. A targeted search of Dirichlet-kernel/root-of-unity concentration and saddle-point literature did not locate the specific combination of the `ANF-115` interior saddle, the `sqrt A` growing positive translation cloud, fixed-order jet cancellation, and affine near-extremizer embedding. No external theorem is load-bearing here, so `SOURCES.md` does not change. This is a boundary assessment rather than a blanket novelty claim.

## 7. Research consequence

`ANF-116` reduced every fixed finite same-saddle translation cluster to one complex phasor. `ANF-117` identifies exactly why that reduction cannot be iterated naively: the cluster cardinality can grow until it resolves the packet's own Gaussian saddle width. At `r~sqrt A`, a phasor that is **exactly zero at the saddle** still leaves order-one source energy.

Replacing the phasor by finitely many derivatives does not repair the problem. For every fixed jet depth there is a sub-square-root, exponentially capacity-deficient physical cloud with that entire jet exactly zero and with macroscopic source norm; three translated copies can then recycle that norm into an excisable aggregate inside an actual near-extremizer. The obstruction therefore moves from finite-dimensional saddle-phase bookkeeping to a genuinely mesoscopic object.

A useful next closure must control the limiting modulation profile on the full `u=sqrt(A)(alpha-alpha_gamma)` window, impose a physical realizability constraint strong enough to prevent the root-cloud profiles above, or derive an independent arithmetic/zero-geometric input that couples this mesoscopic source profile to fixed-notch exposure. Any argument that observes only a fixed finite phase jet can now be falsified by the explicit family (18).