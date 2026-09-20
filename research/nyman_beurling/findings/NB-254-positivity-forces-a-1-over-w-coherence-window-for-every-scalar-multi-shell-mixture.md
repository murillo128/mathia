# NB-254 — Positivity forces a `1/W` coherence window for every scalar multi-shell mixture

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + POSITIVE-MIXTURE-OBSTRUCTION + COHERENCE-WINDOW + MATCHED-CONTROL + NB-253-GENERALIZATION + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-253` closes the canonical equal-weight comb but deliberately leaves open nonuniform positive carrier geometries: perhaps one could spread positive shell mass over a mesoscopic span `W >> H` in a sufficiently irregular way that the Dirichlet coherence peak disappears while the Euler source normalization remains controlled.

For scalar positive mixtures this escape does not exist. Positivity alone forces the normalized carrier transform to remain order one throughout a vertical interval of width `Theta(1/W)` around the origin, independently of how irregular, sparse, continuous, or `J`-dependent the carrier distribution is. In the Ford regime this creates an effective coherent population

\[
J_W:=\frac RW,
\]

and the same matched-control construction as in `NB-231` and `NB-253` survives with `Theta(J_W)` points at horizontal depth

\[
X(1-\beta)=\log J_W+O(1).
\]

Relative to the original Ford coordinate

\[
d=X(1-\beta)-\log J,
\qquad J=R/H,
\]

the replacement critical layer is therefore

\[
\boxed{
d=-\log(W/H)+O(1).
}
\]

The equal spacing in `NB-253` was not responsible for the obstruction. **Every normalized positive scalar superposition whose carrier centers lie in a span `W` has a compulsory `1/W` coherence window.** Nonuniform positive geometry cannot realize the independent-carrier premise of `NB-251`.

This is a source-side method boundary, not a theorem about the actual zeros of `zeta`. Signed or complex carrier coefficients, or an `ell^2` family whose channels are kept separate until after projection, remain outside the argument.

## 1. General positive mixture at fixed component width

Retain the exact-Ford normalization used in `NB-230`--`NB-253`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

As in the conservative matched-control regime, assume

\[
J\le \log Q.
\tag{2}
\]

Fix

\[
0<a<b<1,
\qquad
0\le \phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\tag{3}
\]

and write

\[
F(z):=\int_0^1\phi(y)e^{iyz}\,dy,
\qquad
F(0)>0.
\tag{4}
\]

Let `W=W_J` satisfy

\[
\boxed{
\frac WH\to\infty,
\qquad
\frac WR\to0.
}
\tag{5}
\]

Thus

\[
J_W:=\frac RW\to\infty,
\qquad
J_W\le J.
\tag{6}
\]

Let `mu=mu_J` be an arbitrary probability measure supported in

\[
[-W/2,W/2].
\tag{7}
\]

No discreteness, spacing, regularity, or lower bound on individual masses is assumed. Define the positive scalar multi-shell source

\[
\boxed{
h_\mu(u)
:=
\int_{-W/2}^{W/2}
\frac1H
\phi\!\left(\frac{u-X-\xi}{H}\right)
\,d\mu(\xi).
}
\tag{8}
\]

Each component shell retains width `H`, while the convex support span is `W+O(H)`. Since `W/R -> 0` and `X/R=Y\asymp1`,

\[
\frac WX\to0,
\tag{9}
\]

so all component centers remain `X+o(X)`.

The total source mass is exactly fixed:

\[
\int_\mathbb R h_\mu(u)\,du
=
\int_0^1\phi(y)\,dy.
\tag{10}
\]

On

\[
\sigma_X=1+\frac rX,
\tag{11}
\]

the same prime-number-theorem/Stieltjes calculation used for the single shell and for `NB-253` is uniform for `|\xi|\le W/2=o(X)`. Consequently

\[
\sum_{n\ge2}\Lambda(n)h_\mu(\log n)n^{-\sigma_X}
\longrightarrow
 e^{-r}\int_0^1\phi(y)\,dy
>0.
\tag{12}
\]

Thus the mesoscopic carrier span is not being purchased by letting the positive Euler return grow or vanish.

## 2. Positivity forces an order-one Fourier peak of width `1/W`

The exact Mellin/Fourier carrier of (8) is

\[
\boxed{
L_\mu(v)
=
 e^{iXv}F(Hv)A_\mu(v),
}
\tag{13}
\]

where

\[
\boxed{
A_\mu(v)
:=
\int_{-W/2}^{W/2}e^{i\xi v}\,d\mu(\xi).
}
\tag{14}
\]

For real `u`, positivity gives an elementary pointwise lower bound. If

\[
|u|\le\frac{\pi}{3W},
\tag{15}
\]

then `|xi u|<=pi/6` throughout the support, and hence

\[
\begin{aligned}
\Re A_\mu(u)
&=
\int \cos(\xi u)\,d\mu(\xi)\\
&\ge
\cos(\pi/6)
=
\frac{\sqrt3}{2}.
\end{aligned}
\tag{16}
\]

This lower bound is completely independent of the geometry of `mu`. It applies equally to an irregular finite set of shells, a continuous distribution, or a singular positive measure.

The Ford residues evaluate the carrier at complex

\[
v=u+i\eta,
\qquad \eta>0.
\tag{17}
\]

The same positivity survives there. Indeed, whenever (15) holds,

\[
\begin{aligned}
\Re A_\mu(u+i\eta)
&=
\int e^{-\xi\eta}\cos(\xi u)\,d\mu(\xi)\\
&\ge
 e^{-W\eta/2}\cos(\pi/6).
\end{aligned}
\tag{18}
\]

Therefore a normalized positive carrier mixture cannot suppress its central response on any scale larger than a constant multiple of `1/W`. In particular, if `W eta=o(1)`, then

\[
\boxed{
\Re A_\mu(u+i\eta)\ge c_0>0
\qquad
\text{uniformly for } |u|\le \pi/(3W),
}
\tag{19}
\]

with an absolute constant `c_0` for all sufficiently large `J`.

Equation (19) is the general form of the Dirichlet-kernel peak found in `NB-253`. The peak there came from an explicit equal-weight polynomial; here it follows only from positivity and finite carrier diameter.

## 3. A matched Ford packet fits inside the compulsory coherence window

Fix an integer `q>=1` and a bounded depth parameter `d_*`. Set

\[
M_W:=\lfloor\delta J_W\rfloor,
\tag{20}
\]

where `delta>0` is a sufficiently small constant depending only on a fixed compact range for `Y` and on `q`.

Take the same abstract matched-control ordinates as before,

\[
\boxed{
\gamma_j-t_0
=
\frac{2\pi qj}{X},
\qquad
0\le j<M_W,
}
\tag{21}
\]

with common horizontal depth

\[
\boxed{
X(1-\beta_j)
=
\log J_W+d_*.
}
\tag{22}
\]

Put

\[
\eta_W
:=
\sigma_X-\beta_j
=
\frac{r+\log J_W+d_*}{X},
\tag{23}
\]

and

\[
v_j=(\gamma_j-t_0)+i\eta_W.
\tag{24}
\]

The large carrier phases align exactly:

\[
e^{iX(\gamma_j-t_0)}=1.
\tag{25}
\]

Moreover,

\[
|\gamma_j-t_0|
\le
\frac{2\pi q\delta J_W}{X}+o(1/W)
=
\frac{2\pi q\delta}{YW}+o(1/W).
\tag{26}
\]

Choose `delta` so that the right side is at most `pi/(3W)` uniformly over the allowed range of `Y`. Then every packet point lies inside the forced coherence window (19).

The complex displacement across the full carrier span is harmless:

\[
W\eta_W
=
\frac{W}{X}
\bigl(r+\log J_W+d_*\bigr)
=
\frac{r+\log J_W+d_*}{YJ_W}
\longrightarrow0.
\tag{27}
\]

Therefore (19) gives

\[
\Re A_\mu(v_j)\ge c_0>0
\tag{28}
\]

uniformly in `j<M_W` and uniformly over every allowed positive measure `mu`.

The original width-`H` shell profile is even flatter on this packet. From `W/H -> infinity`,

\[
|H(\gamma_j-t_0)|
\ll
\frac HW
=o(1),
\tag{29}
\]

while

\[
H\eta_W
=
\frac{H}{X}
\bigl(r+\log J_W+d_*\bigr)
=o(1).
\tag{30}
\]

Hence

\[
F(Hv_j)=F(0)+o(1)
\tag{31}
\]

uniformly. Since `F(0)>0` and `A_mu(v_j)` remains in a fixed right half-plane with uniformly bounded modulus, (28)--(31) imply, after decreasing `delta` if necessary,

\[
\Re\bigl(F(Hv_j)A_\mu(v_j)\bigr)
\ge c_1>0.
\tag{32}
\]

Finally,

\[
\begin{aligned}
e^{iXv_j}
&=
 e^{-X\eta_W}e^{iX(\gamma_j-t_0)}\\
&=
 e^{-r}e^{-X(1-\beta_j)}\\
&=
\frac{e^{-r-d_*}}{J_W}.
\end{aligned}
\tag{33}
\]

Combining (13), (32), and (33),

\[
\Re L_\mu(v_j)
\ge
\frac{c_2}{J_W}
\tag{34}
\]

for all packet points and all sufficiently large `J`. Since `M_W=Theta(J_W)`,

\[
\boxed{
\liminf_{J\to\infty}
\Re\sum_{j=0}^{M_W-1}L_\mu(v_j)
\ge c_2\delta>0.
}
\tag{35}
\]

Thus **every normalized positive scalar mixture supported on carrier span `W` admits the same order-one matched obstruction at the population scale `J_W=R/W`.** Irregular spacing cannot disperse it.

## 4. The Ford layer shifts by `log(W/H)`

The old Ford depth coordinate is

\[
d:=X(1-\beta)-\log J.
\tag{36}
\]

The forced coherence window has capacity

\[
J_W=\frac RW,
\tag{37}
\]

so its natural depth coordinate is

\[
d_W:=X(1-\beta)-\log J_W.
\tag{38}
\]

Since

\[
\frac{J}{J_W}=\frac WH,
\tag{39}
\]

we obtain exactly

\[
\boxed{
d_W=d+\log(W/H).
}
\tag{40}
\]

The packet (22) has `d_W=d_*`, hence

\[
\boxed{
d=-\log(W/H)+d_*.
}
\tag{41}
\]

The old `d=O(1)` packet is indeed weakened as the carrier span grows, but positivity forces a replacement layer closer to `Re(s)=1`. The mechanism is therefore scale-covariant for every positive scalar mixture, not only for the uniform comb.

## 5. Compatibility and adversarial audit

The packet in (21)--(22) is a matched compatibility control, not an assertion about the actual zeros of `zeta`. It remains within the same conservative input envelope audited in `NB-231` and `NB-253`. In particular,

\[
M_W=O(J_W)\le O(J)\le O(\log Q),
\tag{42}
\]

its vertical diameter is

\[
O(J_W/X)=O(1/W)=o(1),
\tag{43}
\]

and its Bellotti depth is

\[
R(1-\beta)
=
\frac1Y\bigl(\log J_W+O(1)\bigr)
=O(\log\log Q).
\tag{44}
\]

So none of the previously audited population, spacing, zero-free-region, or growing-density inputs excludes the control merely because `mu` has been made nonuniform.

The strongest possible failure mode is positivity itself. Equation (16) uses `d mu >= 0` in an essential way. With signed or complex coefficients, destructive interference can make the scalar array factor small near zero even though the algebraic normalization is fixed; the simple cosine lower bound then fails. Such designs must pay some other source-side cost if they are to be ruled out, and this finding does not supply that argument.

The result also does not cover vector-valued architectures that keep several shell currents separate through the Hardy projection and combine their energies only afterwards. The scalar source (8) linearly recombines all channels before the residual is tested. That distinction is exactly the independent-carrier opening left by `NB-251`.

Finally, the width `1/W` is a lower bound on a compulsory central coherence region, not a statement that every positive transform has no narrower secondary structure. Extra peaks or cancellations away from the origin are irrelevant to the control: one unavoidable central window already supports the replacement packet.

## 6. Representation audit

The inequality behind (19) is generic harmonic analysis: the Fourier transform of a probability measure supported in an interval cannot rotate substantially before the phase spread across that interval becomes order one. The proof is the elementary cosine estimate (16), so no new theorem about `zeta`, Nyman--Beurling, or Hardy spaces is being claimed.

What is specific to the present representation is the way that generic fact couples to the Ford scales:

\[
\text{carrier diameter }W
\quad\Longrightarrow\quad
\text{coherence width }1/W
\quad\Longrightarrow\quad
\text{capacity }J_W=R/W
\quad\Longrightarrow\quad
\text{critical depth }\log J_W.
\tag{45}
\]

Accordingly this is a **source-side method boundary for positive scalar multi-carrier constructions**. It does not establish an intrinsic obstruction to all Nyman--Beurling approximants, and it does not close the signed/complex or vector-valued routes.

## 7. Prior-art audit

A fresh search was made after the candidate survived the local calculation. The generic background is classical Fourier/characteristic-function theory: Fourier transforms of positive finite measures are positive-definite, and elementary support information forces continuity and an order-one neighborhood around the value at the origin. The precise lower bound used here is proved directly by (16)--(18), so no external theorem is load-bearing.

The search did not locate a prior Nyman--Beurling or zeta result identifying the Ford replacement scale `J_W=R/W` for arbitrary positive scalar multi-shell mixtures. This finding therefore records a local research-line method boundary rather than asserting novelty for the underlying Fourier fact. No new durable source is required in `SOURCES.md`.

## 8. Consequence for the live frontier

`NB-253` left three broad multi-carrier escapes: signed/complex scalar coefficients, an `ell^2` family kept separate until after projection, and nonuniform positive carrier geometries. The last of these is now closed in full generality under the source normalization above.

The next useful source-side audit should therefore not try another positive scalar placement of shells. **Any successful super-`H` construction must either introduce cancellation in the source coefficients or preserve multiple carrier channels as genuinely separate observables.** For the signed/complex route, the natural next question is whether suppressing the compulsory `1/W` peak forces a growing total-variation or Hardy-norm tariff that cancels the apparent bandwidth gain. For the vector route, the corresponding question is whether the Nyman admissibility/projection step can retain `ell^2` carrier energy without collapsing it back to one scalar Mellin current.
