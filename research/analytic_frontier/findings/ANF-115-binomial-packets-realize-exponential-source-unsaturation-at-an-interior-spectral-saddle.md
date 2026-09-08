# ANF-115 — binomial packets realize exponential source-unsaturation at an interior spectral saddle

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + DISTINCT-PACKET-CONTROL + INTERIOR-SPECTRAL-SADDLE + EXPONENTIAL-SOURCE-UNSATURATION + NOTCH-HEIGHT-NONSUFFICIENCY`. `ANF-113` shows that a sub-square-root source-heavy packet can evade the endpoint height cascade only if it becomes exponentially unsaturated relative to the universal max-height capacity `e^A/(R A^2)`, where `A=4 pi H`. That surviving chamber is not an artifact of the crude pointwise estimate. There are explicit finite **distinct** conjugation-invariant packets with only `O(A)` horizontal span whose Montgomery--Taylor source mass is exponentially concentrated at a prescribed interior spectral saddle `|alpha|=alpha_gamma<1`. After normalizing the ambient affine scale so that the packet is source-heavy, these examples satisfy

\[
\frac{A}{\log R}\longrightarrow \frac1{f_\gamma}>1,
\qquad
\frac{D}{A}\longrightarrow1-f_\gamma>0,
\]

with `D=log_+(e^A/(RMA^2))`, while every shrinking endpoint band carries `o(E_0(P))`. Hence the source-capacity-deficit escape in `ANF-113` is kinematically realizable inside the current physical multiset class and cannot be closed from cardinality, maximal height, distinctness, or logarithmic horizontal span alone.

The same packets sharpen the interpretation of the direct-notch height threshold in `ANF-107`. For every fixed `0<eta<1` one can choose the packet so that

\[
f_\gamma<\eta<\alpha_\gamma.
\]

Then its max height lies **strictly above** the leading `ANF-107` notch-visibility threshold,

\[
4\pi\eta H-\log R\asymp (\eta-f_\gamma)A\to+\infty,
\]

but its actual fixed-notch mass still satisfies `E_eta(P)/L -> 0` exponentially. Thus the `1/eta` max-height barrier is a necessary possibility threshold, not a sufficiency principle. Horizontal organization can move the realized source energy away from both `|alpha|=1` and the central notch even when the raw height is large enough to support either.

## 1. A distinct physical packet with an exact product structure

Retain the Montgomery--Taylor source notation

\[
E_0(P)=\int_{-1}^{1}J_0(\alpha)|S_P(\alpha)|^2\,d\alpha,
\qquad
S_P(\alpha)=\sum_{z\in P}e^{-2\pi i\alpha z},
\]

where `J_0=J_MT`. From `ANF-087`, `J_0=g*g` with

\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(2^{-1/2})}
\mathbf 1_{[-1/2,1/2]}(u).
\]

In particular `J_0` is continuous, even, nonnegative, and strictly positive on `(-1,1)` because `g` is strictly positive on the interior of its support.

Fix `gamma>0` and let `A->infinity`. Put

\[
H_A:=\frac{A}{4\pi},
\qquad
n_A:=\lfloor\gamma A\rfloor,
\qquad
\varepsilon_A:=A^{-2},
\]

and choose positive horizontal increments

\[
t_{k,A}:=\frac12+\varepsilon_A3^{-k},
\qquad 1\le k\le n_A.
\tag{1}
\]

For every subset `S subset {1,...,n_A}`, define

\[
x_S:=\sum_{k\in S}t_{k,A}.
\]

The `2^{n_A}` numbers `x_S` are distinct. If two subsets have different cardinalities, their half-integer parts differ by at least `1/2` while the total perturbation is less than `varepsilon_A/2`. If they have the same cardinality, the first differing ternary digit cannot be cancelled by all later digits because

\[
3^{-k}>\sum_{j>k}3^{-j}.
\]

Now take the conjugation-invariant packet

\[
P_A:=\{x_S+iH_A,\ x_S-iH_A:S\subset\{1,\ldots,n_A\}\}.
\tag{2}
\]

It has no repeated sites and

\[
m_A:=|P_A|=2^{n_A+1},
\qquad
D_x(P_A)=\sum_{k=1}^{n_A}t_{k,A}
=\frac{n_A}{2}+O(A^{-2}).
\tag{3}
\]

Thus the horizontal span is only `O(A)` despite exponential cardinality.

The subset-product identity gives

\[
Q_A(\alpha)
:=\sum_Se^{-2\pi i\alpha x_S}
=\prod_{k=1}^{n_A}\left(1+e^{-2\pi i\alpha t_{k,A}}\right),
\tag{4}
\]

and conjugation in height gives the exact factorization

\[
S_{P_A}(\alpha)
=2\cosh\!\left(\frac{A\alpha}{2}\right)Q_A(\alpha).
\tag{5}
\]

Since `m_A^2=4^{n_A+1}`,

\[
\boxed{
|S_{P_A}(\alpha)|^2
=m_A^2\cosh^2\!\left(\frac{A\alpha}{2}\right)
\prod_{k=1}^{n_A}\cos^2(\pi\alpha t_{k,A}).
}
\tag{6}
\]

If the tiny ternary perturbations are suppressed, (4) becomes the elementary binomial polynomial `(1+e^{-pi i alpha})^n`; the perturbation serves only to make all physical sites distinct while preserving the same exponential asymptotics.

## 2. The source norm concentrates at one interior spectral saddle

Define for `0<=alpha<1`

\[
F_\gamma(\alpha)
:=\alpha+2\gamma\log\cos\frac{\pi\alpha}{2}.
\tag{7}
\]

Its derivative and second derivative are

\[
F_\gamma'(\alpha)
=1-\gamma\pi\tan\frac{\pi\alpha}{2},
\qquad
F_\gamma''(\alpha)
=-\frac{\gamma\pi^2}{2}
\sec^2\frac{\pi\alpha}{2}<0.
\tag{8}
\]

Hence `F_gamma` is strictly concave and has the unique maximizer

\[
\boxed{
\alpha_\gamma
=\frac2\pi\arctan\frac1{\pi\gamma}
\in(0,1).
}
\tag{9}
\]

Write

\[
f_\gamma:=F_\gamma(\alpha_\gamma).
\tag{10}
\]

Because `F_gamma(0)=0` and `F_gamma'(0)=1`, while `log cos(pi alpha/2)<0` for `alpha>0`,

\[
\boxed{0<f_\gamma<\alpha_\gamma<1.}
\tag{11}
\]

The perturbation in (1) does not change this exponential landscape. On every compact subinterval of `[0,1)`, smoothness of `log cos(pi alpha t)` and

\[
\sum_{k=1}^{n_A}|t_{k,A}-1/2|=O(A^{-2})
\]

give uniformly

\[
\frac2A\sum_{k=1}^{n_A}
\log|\cos(\pi\alpha t_{k,A})|
=2\gamma\log\cos\frac{\pi\alpha}{2}+o(1).
\tag{12}
\]

No hidden maximum is created at `alpha=1`. If `r=1-alpha`, then for `alpha` near one,

\[
|\cos(\pi\alpha t_{k,A})|
\ll r+A^{-2}3^{-k}.
\tag{13}
\]

For `r>=A^{-1}`, (12) remains valid up to an `o(1)` error after restricting to a sufficiently small fixed endpoint neighborhood; for `r<A^{-1}`, (13) makes the product superpolynomially smaller than the interior saddle. Thus the unique exponential maximum of (6) remains `alpha_gamma`.

For `alpha>=0`,

\[
\frac14e^{A\alpha}
\le
\cosh^2\!\left(\frac{A\alpha}{2}\right)
\le e^{A\alpha}.
\tag{14}
\]

Combining (6), (12)--(14), continuity of `J_0`, and `J_0(alpha_gamma)>0` gives the elementary Laplace-principle limit

\[
\boxed{
\lim_{A\to\infty}
\frac1A\log\frac{E_0(P_A)}{m_A^2}
=f_\gamma.
}
\tag{15}
\]

No asymptotic integration theorem is needed for the exponential rate: strict concavity gives an exponential gap away from any fixed neighborhood of `alpha_gamma`, while a small interval around `alpha_gamma` supplies the matching lower bound.

More is true. Normalize the source spectral measure by

\[
d\nu_A(\alpha)
:=\frac{J_0(\alpha)|S_{P_A}(\alpha)|^2}{E_0(P_A)}\,d\alpha.
\tag{16}
\]

The same strict-gap argument, together with evenness, yields

\[
\boxed{
\nu_A\Longrightarrow
\frac12\delta_{\alpha_\gamma}
+\frac12\delta_{-\alpha_\gamma}.
}
\tag{17}
\]

Consequently every shrinking Montgomery--Taylor endpoint band is asymptotically empty for this packet:

\[
\boxed{
\delta_A\downarrow0
\quad\Longrightarrow\quad
\frac{E_{\rm edge,\delta_A}(P_A)}{E_0(P_A)}\to0.
}
\tag{18}
\]

This is the opposite geometry from the packet localization used in `ANF-112`--`ANF-113`: the source mass lives at a stable interior frequency, not in a layer approaching `|alpha|=1`.

## 3. The ANF-113 exponential capacity-deficit chamber is realized exactly

Turn the packet into the source-heavy normalization used by `ANF-113`. Let

\[
L_A:=\lceil E_0(P_A)\rceil,
\qquad
M_A:=\frac{E_0(P_A)}{L_A},
\qquad
R_A:=\frac{L_A}{m_A^2}.
\tag{19}
\]

Then `M_A->1`. Equation (15) gives

\[
\boxed{
\frac{\log R_A}{A}\to f_\gamma>0,
\qquad
R_A\to\infty,
}
\tag{20}
\]

so `m_A=o(sqrt(L_A))`. The max-height ratio is therefore

\[
\boxed{
\frac{4\pi H_A}{\log R_A}
=\frac{A}{\log R_A}
\longrightarrow\kappa_\gamma:=\frac1{f_\gamma}>1.
}
\tag{21}
\]

The logarithmic source-capacity deficit from `ANF-113` satisfies

\[
\begin{aligned}
D_A
&:=\log_+\!\left(
\frac{e^A}{R_AM_AA^2}
\right)\\
&=(1-f_\gamma)A+o(A),
\end{aligned}
\]

hence

\[
\boxed{
\frac{D_A}{A}\to1-f_\gamma>0.
}
\tag{22}
\]

Thus the sufficient cascade condition `D_A=o(A)` fails by a fixed exponential rate, while the packet remains source-heavy (`M_A->1`) and sub-square-root. Equations (18) and (22) show that this failure has real spectral content: the missing max-height capacity has been used to move the source norm to `|alpha|=alpha_gamma`, not merely lost through a slack estimate.

The normalization `L_A` is compatible with the physical affine bookkeeping. Since `L_A/m_A->infinity`, for large `A` one may adjoin `L_A-2m_A` distinct real simple sites to `P_A` and obtain a finite conjugation-invariant multiset whose affine size is exactly `L_A`. No assertion is made that this arbitrary completion is globally near-extremal; the point is that the packet scale required in (19) is a genuine physical scale rather than an impossible formal normalization.

The family spans every multiplicative supercritical ratio. As `gamma downarrow0`, `f_gamma->1`; as `gamma->infinity`, `f_gamma->0`; and `f_gamma` is strictly decreasing because increasing `gamma` strictly decreases `F_gamma(alpha)` at every `alpha>0`. Hence for every `kappa>1` there is a `gamma` with

\[
\kappa_\gamma=\kappa.
\tag{23}
\]

So exponential source-unsaturation is not confined to one exceptional height ratio: packet controls exist throughout the entire multiplicatively supercritical range.

## 4. Crossing the max-height notch barrier still need not create notch mass

Let `0<eta<1` be fixed and retain the triangular notch

\[
\phi_\eta(\alpha)
=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad
E_\eta(P)=\int\phi_\eta|S_P|^2.
\]

If `eta<alpha_gamma`, strict concavity shows that the largest exponent available inside the notch is `F_gamma(eta)<f_gamma`; the linear zero of `phi_eta` at `eta` affects only a subexponential factor. Thus

\[
\boxed{
\lim_{A\to\infty}
\frac1A\log\frac{E_\eta(P_A)}{E_0(P_A)}
=F_\gamma(\eta)-f_\gamma<0.
}
\tag{24}
\]

In particular

\[
\boxed{
\frac{E_\eta(P_A)}{L_A}\to0.
}
\tag{25}
\]

The spectral limit (17) gives the complementary side. If `eta>alpha_gamma`, the bounded continuous multiplier `phi_eta/J_0` is positive at the two saddle points, so

\[
\boxed{
\frac{E_\eta(P_A)}{E_0(P_A)}
\to
\frac{\phi_\eta(\alpha_\gamma)}{J_0(\alpha_\gamma)}>0.
}
\tag{26}
\]

At `eta=alpha_gamma` the same ratio tends to zero because `phi_eta(alpha_gamma)=0`. Thus for this explicit family the actual direct-notch transition occurs at the **interior source saddle** `alpha_gamma`, not at a condition on maximal height alone.

This produces a matched falsifier for an overstrong reading of `ANF-107`. Given any fixed `0<eta<1`, define

\[
\gamma_0:=\frac{1}{\pi\tan(\pi\eta/2)},
\]

so `alpha_(gamma_0)=eta`. Since `f_(gamma_0)<eta`, continuity allows a slightly smaller `gamma` for which

\[
\boxed{f_\gamma<\eta<\alpha_\gamma.}
\tag{27}
\]

For that choice, (20) gives

\[
\eta A-\log R_A
=(\eta-f_\gamma)A+o(A)\to+\infty.
\tag{28}
\]

Hence the packet lies not merely at but a linear distance **above** the leading max-height notch-visibility threshold `eta A ~= log R` (and therefore above its `2 log log R` correction), yet (24)--(25) say its actual notch mass is exponentially negligible. The height barrier in `ANF-107` is correctly necessary for a sparse packet to *be capable* of carrying notch mass; it cannot be reversed into a sufficiency statement.

## 5. Matched controls show that horizontal organization carries the missing exponent

The max-height capacity in `ANF-113` is also sharp at exponential scale. With the same cardinality `m_A` and height `H_A`, place the conjugate pairs coherently at one horizontal phase. Then

\[
|S_{\rm coh}(\alpha)|^2
=m_A^2\cosh^2\!\left(\frac{A\alpha}{2}\right),
\]

and the linear endpoint zero of `J_0` gives

\[
\lim_{A\to\infty}
\frac1A\log\frac{E_0(P_A^{\rm coh})}{m_A^2}=1.
\tag{29}
\]

Comparing (15) and (29),

\[
\boxed{
\frac1A\log
\frac{E_0(P_A)}{E_0(P_A^{\rm coh})}
\to-(1-f_\gamma).
}
\tag{30}
\]

Thus two packets with the same cardinality and maximal vertical height differ in realized source capacity by the exact exponential rate appearing in (22). The source-unsaturated chamber is therefore a **horizontal phase-organization phenomenon**. It is invisible to any control that retains only `m` and `H`.

The distinct construction (1)--(6) also rules out a second shortcut. Exponential unsaturation does not require repeated sites: all `2^{n_A}` horizontal centers are different. Nor does it require a large raw horizontal span: by (3) and (20),

\[
\boxed{
\frac{D_x(P_A)}{\log R_A}
\to\frac{\gamma}{2f_\gamma}<\infty.
}
\tag{31}
\]

The mechanism is dense finite-span interference produced by the product structure. A future theorem may of course use stronger information about local occupancy, additive structure, or coupling to the near-extremal remainder; but distinctness plus a logarithmic span bound does not eliminate the packet.

## 6. Prior-art boundary, adversarial checks, and exact scope

The factorization in (4) is the elementary finite product behind a binomial characteristic polynomial, and the exponential localization argument is a one-dimensional Laplace principle. A targeted prior-art search across trigonometric-polynomial concentration, idempotent concentration, Riesz-product/positive-definite constructions, and standard Laplace asymptotics found mature general concentration mechanisms but no result that identifies this Montgomery--Taylor Fourier--Laplace saddle, the `ANF-113` normalized capacity deficit, or the fixed-notch consequence (27)--(28). No external theorem is load-bearing: equations (4)--(6) are exact finite identities and the asymptotic claims follow from strict concavity plus elementary exponential upper/lower bounds. `SOURCES.md` therefore does not change. This search outcome is not a global novelty claim.

The packet uses heights `H_A->infinity`; it says nothing against the bounded-height localization theorem of `ANF-106`. Although the packet is distinct, its horizontal occupancy becomes enormous, so no separation assumption is present. The packet itself is also **not** a Montgomery--Taylor near-extremizer relative to its own affine size: its source norm is exponentially larger than `L(P_A)`. The normalization `L_A` models its role as a sparse source-heavy component inside a much larger candidate near-extremizer. This finding does not construct the complementary core whose negative polarization would be required by `ANF-112`, and therefore does not construct a fatal sequence for `beta_eta`.

That boundary is decisive. The result falsifies a packet-local route to closing `ANF-113`: no theorem based only on sub-square-root cardinality, maximal height, distinctness, or logarithmic horizontal span can force capacity saturation or endpoint localization. It does **not** falsify a theorem using the global near-extremizer condition, the forced packet--remainder anti-alignment, a complex analogue of `ANF-114`, or arithmetic information beyond the universal physical multiset class.

## 7. Research consequence

The live source-capacity-deficit problem changes form. Exponential unsaturation is no longer merely the logical complement of the sufficient condition in `ANF-113`; it has an explicit physical packet model. In that model the source energy migrates to an interior saddle `alpha_gamma`, and the same horizontal product structure can keep a packet notch-negligible even after its maximal height has crossed the direct `ANF-107` threshold.

Therefore the next useful rigidity statement must see **global coupling or horizontal phase structure**, not just vertical capacity. A successful closure can proceed by showing that an interior-saddle packet like (2) cannot acquire the macroscopic negative polarization with the unused remainder required by global Montgomery--Taylor near-extremality, by proving that such dense product interference is incompatible with the source-generated physical geometry of a near-extremizer, or by finding a complex/conjugate effective modulus that controls these phase-organized packets. Conversely, constructing a near-extremal completion of this packet with fixed-notch exposure at or above `B_eta` would turn the present local control into an actual obstruction to the frozen-notch route.