# ANF-107 — sparse tails have distinct Montgomery–Taylor source and central-notch visibility scales

**Status:** `EXACT-DERIVED + SPARSE-TAIL-SPECTRAL-SEPARATION + MATCHED-ENDPOINT-BARRIERS + NOTCH-COMPLEMENT-ANTI-ALIGNMENT + FIXED-RAY-NARROWING`. `ANF-103` shows that a sub-square-root tail can remain visible in the Montgomery--Taylor source norm only after crossing the endpoint scale `4πH >= log(L/m^2)+2 log log(L/m^2)+O(1)`. For the fixed triangular notch of `ANF-099`, that is **not yet enough to make the same tail visible to the decisive notch observable**. The notch closes linearly at the inner endpoints `±eta`, so the identical endpoint calculation occurs with bandwidth `eta` instead of `1`. A tail carrying a macroscopic fraction of the fixed-notch energy must satisfy the strictly stronger necessary condition

\[
\boxed{
4\pi\eta H
\ge
\log\frac{L}{m^2}
+2\log\log\frac{L}{m^2}
+O_\eta(1).
}
\tag{1}
\]

For every fixed `0<eta<1`, the leading height coefficient is therefore larger by the factor `1/eta` than the source-visibility coefficient in `ANF-103`. This creates a genuine asymptotic **intermediate chamber**: a sparse high tail may already be source-heavy, and hence essential to global Montgomery--Taylor near-extremality through the cancellation mechanism of `ANF-104`, while still contributing `o(L)` to the central notch.

Inside that chamber the tail has an even sharper interpretation. In a globally near-extremal configuration, if the tail is source-heavy but notch-negligible, then deleting it preserves the normalized notch exposure, while its required macroscopic negative source interaction moves entirely into the positive complementary form `J_0-phi_eta`. Thus such a tail cannot be the direct carrier of the dangerous `beta_eta` exposure of `ANF-099`; it can only act as a **notch-invisible source compensator** for the retained core. The surviving high-tail obstruction is consequently narrower than “source-heavy”: either the tail reaches the stronger notch-visibility height (1), or it must catalyze a macroscopic cancellation in the notch-complement channel without carrying the notch observable itself.

## 1. The triangular notch has its own linear endpoint zero

Retain the fixed-ray notation of `ANF-099`,

\[
J_0:=J_{\rm MT},
\qquad
\phi_\eta(\alpha)
=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad 0<\eta<1,
\tag{2}
\]

and write

\[
\|f\|_\eta^2
:=\int_{-\eta}^{\eta}\phi_\eta(\alpha)|f(\alpha)|^2\,d\alpha.
\tag{3}
\]

Let `B` be any finite conjugation-invariant multiset with

\[
m:=|B|,
\qquad
H:=\max_{z\in B}|\operatorname{Im}z|,
\qquad
S_B(\alpha):=\sum_{z\in B}e^{-2\pi i\alpha z}.
\tag{4}
\]

No separation, multiplicity restriction or horizontal geometry is assumed. For real `alpha`,

\[
|S_B(\alpha)|
\le m e^{2\pi|\alpha|H}.
\tag{5}
\]

Using the exact triangular profile rather than only its supremum gives

\[
\begin{aligned}
\|S_B\|_\eta^2
&\le
2b_\eta m^2
\int_0^\eta
\left(1-\frac{\alpha}{\eta}\right)e^{4\pi H\alpha}\,d\alpha\\
&=
\frac{2b_\eta m^2}{\eta}
\frac{e^{4\pi\eta H}-1-4\pi\eta H}{(4\pi H)^2}.
\end{aligned}
\tag{6}
\]

The continuous value at `H=0` is `b_eta eta m^2`, exactly as it should be. In particular, for every fixed `eta` and `H>=1`,

\[
\boxed{
\|S_B\|_\eta^2
\ll_\eta
m^2\frac{e^{4\pi\eta H}}{H^2}.
}
\tag{7}
\]

The factor `H^{-2}` is not a technical loss. It is the same endpoint mechanism as in `ANF-103`: the spectral weight vanishes linearly at the edge of its support. The only difference is that the central notch ends at `|alpha|=eta`, while the Montgomery--Taylor source ends at `|alpha|=1`.

## 2. Direct notch visibility costs `1/eta` times the source height

Let `W` be a larger physical configuration, put

\[
L:=L(W),
\qquad
R:=\frac{L}{m^2},
\tag{8}
\]

and assume `R->infinity` along a sequence, equivalently `m=o(sqrt L)`. Dividing (7) by `L` gives

\[
\boxed{
\frac{\|S_B\|_\eta^2}{L}
\ll_\eta
\frac1R\frac{e^{4\pi\eta H}}{H^2}.
}
\tag{9}
\]

Hence a tail with macroscopic fixed-notch mass,

\[
\limsup
\frac{\|S_B\|_\eta^2}{L}>0,
\tag{10}
\]

must satisfy, along a subsequence,

\[
\frac{e^{4\pi\eta H}}{H^2}\gg_\eta R.
\tag{11}
\]

Since `R->infinity`, (11) forces `H->infinity`. Writing `x=4 pi eta H` and inverting the elementary inequality `e^x/x^2 \gg R` yields

\[
\boxed{
4\pi\eta H
\ge
\log R+2\log\log R+O_\eta(1),
}
\tag{12}
\]

which is (1). Conversely, whenever

\[
4\pi\eta H
\le
\log R+2\log\log R-\omega(1),
\tag{13}
\]

formula (6) forces

\[
\boxed{
\frac{\|S_B\|_\eta^2}{L}\to0.
}
\tag{14}
\]

Compare (12) with the source-heavy necessity from `ANF-103`,

\[
4\pi H
\ge
\log R+2\log\log R+O(1).
\tag{15}
\]

Because `eta<1` is frozen before the amplitude is varied, the two thresholds are asymptotically separated by

\[
\frac{1-\eta}{4\pi\eta}\log R+O(\log\log R)
\tag{16}
\]

in physical height. In particular, a tail sitting at the minimal source-visible scale

\[
4\pi H
=
\log R+2\log\log R+O(1)
\tag{17}
\]

obeys the stronger quantitative decay

\[
\boxed{
\frac{\|S_B\|_\eta^2}{L}
\ll_\eta
R^{\eta-1}(\log R)^{2\eta-2}
\longrightarrow0.
}
\tag{18}
\]

Thus the matched log--log threshold of `ANF-095/103` is only the first stage. It makes a sparse tail visible to the full Montgomery--Taylor source, but for every proper central notch it still leaves that tail asymptotically invisible to the observable that controls the fixed-ray criterion.

## 3. Notch-negligibility removes every notch interaction with the tail

The previous section concerns the tail self-energy. In a globally near-extremal configuration it automatically controls the tail's **cross** contribution as well, without any horizontal gap assumption.

Let

\[
W=A\sqcup B
\tag{19}
\]

be a conjugation-invariant split complete on every real-part fiber, so

\[
L(W)=L(A)+L(B).
\tag{20}
\]

Assume

\[
e(W):=\frac{\|S_W\|_0^2}{L(W)}-1\to0,
\qquad
\frac{L(B)}{L(W)}\to0,
\qquad
\frac{\|S_B\|_\eta^2}{L(W)}\to0.
\tag{21}
\]

Because `0<=phi_eta<=J_0`,

\[
\frac{\|S_W\|_\eta^2}{L(W)}
=h_\eta(W)
\le1+e(W)=1+o(1).
\tag{22}
\]

Set `L=L(W)` and `b=||S_B||_eta/sqrt L=o(1)`. Since `S_A=S_W-S_B`,

\[
\frac{\|S_A\|_\eta}{\sqrt L}
\le\sqrt{1+e(W)}+b=1+o(1).
\tag{23}
\]

Therefore the notch cross term

\[
\mathcal C_\eta(A,B)
:=\operatorname{Re}
\int\phi_\eta S_A\overline{S_B}
\tag{24}
\]

satisfies

\[
\boxed{
\frac{|\mathcal C_\eta(A,B)|}{L}
\le
\left(\sqrt{1+e(W)}+b\right)b
\longrightarrow0.
}
\tag{25}
\]

More directly, expanding `S_A=S_W-S_B` gives

\[
\left|
\|S_A\|_\eta^2-
\|S_W\|_\eta^2
\right|
\le
2\|S_W\|_\eta\|S_B\|_\eta+
\|S_B\|_\eta^2=o(L).
\tag{26}
\]

Together with `L(A)/L(W)->1`, this proves

\[
\boxed{
h_\eta(A)-h_\eta(W)\to0.}
\tag{27}
\]

So a sparse tail below the stronger height threshold (12) cannot directly manufacture the dangerous near-extremizer exposure. Its self contribution, its cross contribution, and the change in normalized notch exposure all vanish together. This conclusion requires neither remote separation nor control of the Montgomery--Taylor norm of `B`.

## 4. A source-heavy but notch-negligible tail can only cancel in the complementary form

Now assume in addition that the sparse tail is genuinely source-heavy:

\[
\liminf
\frac{\|S_B\|_0^2}{L(W)}
\ge\lambda>0.
\tag{28}
\]

The exact source polarization from `ANF-104`, using the Montgomery--Taylor floor separately on `A` and `B`, gives

\[
\boxed{
\limsup
\frac{\mathcal C_0(A,B)}{L(W)}
\le-\frac\lambda2,
}
\tag{29}
\]

where

\[
\mathcal C_0(A,B)
:=\operatorname{Re}\int J_0S_A\overline{S_B}.
\tag{30}
\]

Define the positive notch-complement spectrum

\[
J_\eta^\perp:=J_0-\phi_\eta\ge0
\tag{31}
\]

and its cross term

\[
\mathcal C_\eta^\perp(A,B)
:=\operatorname{Re}\int
J_\eta^\perp S_A\overline{S_B}.
\tag{32}
\]

Linearity of the inner product gives

\[
\mathcal C_0
=\mathcal C_\eta+\mathcal C_\eta^\perp.
\tag{33}
\]

Combining (25) and (29) therefore yields

\[
\boxed{
\limsup
\frac{\mathcal C_\eta^\perp(A,B)}{L(W)}
\le-\frac\lambda2.
}
\tag{34}
\]

This is the key structural consequence of the two visibility scales. A source-heavy tail in the intermediate chamber is not removable in the source norm: it may be essential for cancelling the positive Montgomery--Taylor excess of the core. But it is invisible to the fixed notch, and the macroscopic anti-alignment required by global near-extremality is forced into `J_0-phi_eta`. The tail is therefore a **source compensator rather than a notch carrier**.

Equation (27) must not be overread. It does not imply that `A` is itself a Montgomery--Taylor near-extremizer. Indeed (28)--(29) are precisely the mechanism by which deleting `B` can expose a macroscopic source excess of `A`. What has been separated is the role of the tail: it can lower the source energy of the union while leaving the decisive central-notch observable asymptotically unchanged.

## 5. The sparse high-tail branch now has three distinct chambers

For `R=L/m^2->infinity`, the max-height screening can be organized without any horizontal assumptions.

Below the source threshold of `ANF-103`,

\[
4\pi H
\le
\log R+2\log\log R-\omega(1),
\tag{35}
\]

the tail is source-negligible and `ANF-103` trims it completely whenever a suitable core exists.

Between the source and notch thresholds, namely in any asymptotic region compatible with

\[
4\pi H
\gtrsim
\log R+2\log\log R
\tag{36}
\]

but

\[
4\pi\eta H
\le
\log R+2\log\log R-\omega(1),
\tag{37}
\]

the tail may be source-heavy but is necessarily notch-negligible. If it actually is source-heavy inside a global near-extremizer, (27) and (34) force the notch-invisible compensator mechanism.

Only after

\[
4\pi\eta H
\ge
\log R+2\log\log R+O_\eta(1)
\tag{38}
\]

can the tail itself carry a macroscopic fraction of the fixed-notch observable. Thus a fatal sparse-tail candidate for `beta_eta` has two genuinely different options: cross the stronger direct notch-visibility barrier, or remain below it and use a notch-complement source cancellation to make an exposed core globally near-extremal.

For the calibration of `ANF-095`, where `L\asymp n^3`, `m\asymp n`, and hence `R\asymp n`, the two thresholds become

\[
4\pi H_{\rm source}
\ge
\log n+2\log\log n+O(1),
\tag{39}
\]

versus

\[
\boxed{
4\pi H_{\rm notch}
\ge
\frac1\eta
\left(\log n+2\log\log n\right)
+O_\eta(1).
}
\tag{40}
\]

The earlier critical surgery therefore becomes source-visible parametrically before it can be directly visible to any frozen proper central notch.

## 6. Prior-art boundary, stress tests, and remaining frontier

A targeted literature search was made across the current Montgomery--Taylor/pair-correlation sources and the classical bandlimited-concentration/Paley--Wiener neighborhood. General spectral concentration and uncertainty principles study how arbitrary bandlimited functions distribute `L^2` mass between sets, but no located theorem gives the present line-specific comparison between **vertical Fourier--Laplace amplification at two nested compact spectral endpoints** for physical conjugation-invariant exponential sums, nor the near-extremal notch-complement polarization (34). No external theorem is load-bearing: (6) is an elementary exact integral, (12) is its inversion, and (25)--(34) are Hilbert-space polarization combined with the already-canonical Montgomery--Taylor floor. `SOURCES.md` therefore remains unchanged.

Several boundaries are essential. The notch width `eta` is fixed with `eta<1`; if `eta` is allowed to approach one with the scale, the separation in (16) can disappear. The max-height condition is only a necessary screening statistic: one extremely high point can make `H` large without making either source or notch energy macroscopic, so crossing (12) is not sufficient. The sub-square-root hypothesis enters only when comparing with the `ANF-103` source threshold through `R->infinity`; the notch estimate (6) itself is finite and unconditional. The decomposition in Sections 3--4 is complete on real-part fibers so that the affine denominator remains additive. Finally, `J_0-phi_eta` is a positive **complementary weight**, not literally a support-disjoint outer band; equation (34) asserts cancellation invisible to the notch quadratic form, not pointwise localization of that cancellation at `|alpha|>eta`.

The fixed-ray frontier after `ANF-103`--`ANF-107` is therefore more specific. Bounded-height bulk is localized to finite physical boxes by `ANF-106`. A sub-square-root high tail below the source threshold is removable. A tail in the newly isolated intermediate chamber cannot itself carry the dangerous notch exposure and can survive only as a macroscopic compensator in the notch-complement source form. Direct sparse-tail notch carriage requires the stronger `1/eta` height scale (38). The next decisive test is accordingly two-pronged: either rule out the notch-complement compensator mechanism for a high-exposure core, or construct a physical near-extremizing sequence that crosses (38) and still reaches the `B_eta` exposure threshold of `ANF-099`.

This does not prove `beta_eta<B_eta`, certify an improved simple-critical-zero proportion, or establish RH. It removes the identification of “source-heavy” with “notch-dangerous” and isolates the extra vertical scale and cancellation channel that any remaining sparse-tail obstruction must pay.