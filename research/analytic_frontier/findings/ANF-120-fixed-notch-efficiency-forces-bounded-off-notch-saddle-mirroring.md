# ANF-120 — fixed-notch efficiency forces bounded off-notch saddle mirroring

**Status:** `EXACT-DERIVED + FIXED-NOTCH + NEAR-EXTREMIZER + OFF-NOTCH-COMPANION + QUANTITATIVE-MISMATCH-TAX + BOUNDED-MASS-MIRRORING`. `ANF-119` classifies what a remainder must do to keep an interior-saddle packet indispensable: in the bounded source-mass branch it may still overpolarize the packet, while in the divergent branch it must mirror the packet's source profile. The bounded branch can be sharpened by using the fact that the central-notch observable has a finite efficiency relative to the Montgomery--Taylor source. High notch exposure leaves only a small source budget in any band on which the notch vanishes. Combining that budget with the localized polarization identity gives a two-sided corridor which quantitatively taxes any mismatch between packet mass and remainder defect.

Fix the Montgomery--Taylor source

\[
J_0:=J_{\rm MT},
\qquad
E_0(X):=\int_{-1}^{1}J_0(\alpha)|S_X(\alpha)|^2\,d\alpha,
\]

and one fixed central-notch weight `phi_eta` with

\[
0\le \phi_\eta\le J_0,
\qquad
E_\eta(X):=\int_{-1}^{1}\phi_\eta(\alpha)|S_X(\alpha)|^2\,d\alpha.
\]

Define its source efficiency

\[
\boxed{
\chi_\eta
:=
\operatorname*{ess\,sup}_{\alpha\in[-1,1]}
\frac{\phi_\eta(\alpha)}{J_0(\alpha)}
\in(0,1],
}
\tag{1}
\]

with the ratio interpreted as zero where `phi_eta=0`. Thus

\[
\phi_\eta\le \chi_\eta J_0
\quad\text{a.e.}
\tag{2}
\]

Let `W_n=P_n sqcup U_n` satisfy the bounded-mass setup of `ANF-119`. Put

\[
L_n:=L(W_n),
\qquad
\frac{E_0(W_n)}{L_n}=1+o(1),
\tag{3}
\]

assume `|P_n|=o(L_n)`, and define

\[
M_n:=\frac{E_0(P_n)}{L_n},
\qquad
X_n:=\frac{\Delta(U_n)}{L_n},
\tag{4}
\]

with

\[
0<\lambda\le M_n\le\Lambda,
\qquad
X_n=O(1).
\tag{5}
\]

Suppose there is a measurable symmetric spectral band `B_n` on which the fixed notch vanishes,

\[
\phi_\eta=0\quad\text{a.e. on }B_n,
\tag{6}
\]

and in which the packet is source-localized:

\[
E_{B_n^c}(P_n)=o(L_n),
\qquad
E_B(X):=\int_BJ_0(\alpha)|S_X(\alpha)|^2\,d\alpha.
\tag{7}
\]

Finally write

\[
h_n:=\frac{E_\eta(W_n)}{L_n},
\qquad
R_n:=\frac{E_{B_n}(W_n)}{L_n}.
\tag{8}
\]

Then the bounded off-notch companion obeys the exact asymptotic corridor

\[
\boxed{
\frac{(M_n-X_n)^2}{4M_n}+o(1)
\le
R_n
\le
1-\frac{h_n}{\chi_\eta}+o(1).
}
\tag{9}
\]

Equivalently,

\[
\boxed{
(M_n-X_n)^2
\le
4M_n\left(1-\frac{h_n}{\chi_\eta}\right)+o(1).
}
\tag{10}
\]

Thus high central-notch exposure directly constrains the amount of overpolarization available in an off-notch saddle band. In particular, if

\[
\frac{h_n}{\chi_\eta}\to1,
\tag{11}
\]

then

\[
\boxed{
R_n\to0,
\qquad
X_n-M_n\to0,
}
\tag{12}
\]

and the remainder mirrors the packet in the saddle band:

\[
\boxed{
\frac{E_{B_n}(U_n)}{E_{B_n}(P_n)}\to1,
\qquad
\frac{\mathcal C_{B_n}(P_n,U_n)}{E_{B_n}(P_n)}\to-1,
\qquad
\frac{E_{B_n}(W_n)}{E_{B_n}(P_n)}\to0.
}
\tag{13}
\]

This extends the profile-mirroring conclusion of `ANF-119` from the branch `M_n -> infinity` to the bounded branch whenever the global configuration approaches the maximum possible notch efficiency.

## 1. Localized Montgomery--Taylor polarization gives the lower wall

The affine bookkeeping in `ANF-119` remains valid because `|P_n|=o(L_n)`. In the notation above it gives

\[
\boxed{
\frac{2\mathcal C_0(P_n,U_n)}{L_n}
=-(M_n+X_n)+o(1),
}
\tag{14}
\]

where

\[
\mathcal C_B(P,U)
:=
\operatorname{Re}\int_BJ_0(\alpha)S_P(\alpha)\overline{S_U(\alpha)}\,d\alpha.
\tag{15}
\]

Because `X_n=O(1)`, the source energy of `U_n` is `O(L_n)`. Equation (7) and Cauchy--Schwarz therefore imply

\[
\mathcal C_{B_n^c}(P_n,U_n)=o(L_n).
\tag{16}
\]

Hence the whole macroscopic anti-alignment in (14) occurs in the saddle band:

\[
\frac{2\mathcal C_{B_n}(P_n,U_n)}{L_n}
=-(M_n+X_n)+o(1),
\tag{17}
\]

while

\[
\frac{E_{B_n}(P_n)}{L_n}=M_n+o(1).
\tag{18}
\]

Put

\[
b_n:=\frac{E_{B_n}(U_n)}{L_n}.
\tag{19}
\]

Cauchy--Schwarz in `L^2(B_n,J_0 d alpha)` and the lower bound `M_n>=lambda` yield

\[
\boxed{
b_n
\ge
\frac{(M_n+X_n)^2}{4M_n}+o(1).}
\tag{20}
\]

On the other hand, expanding the residual source energy in `B_n` using (17)--(19),

\[
\begin{aligned}
R_n
&=M_n+b_n-(M_n+X_n)+o(1)\\
&=b_n-X_n+o(1).
\end{aligned}
\tag{21}
\]

Substitution of (20) gives

\[
\boxed{
R_n
\ge
\frac{(M_n-X_n)^2}{4M_n}+o(1).
}
\tag{22}
\]

This is the missing bounded-mass rigidity. The lower wall does not merely say that the remainder has substantial source energy in the packet band, as in `ANF-119`. It measures exactly how much **uncancelled** source must remain there if the remainder defect `X_n` fails to match the packet mass `M_n`.

## 2. Notch efficiency gives the upper wall

Equation (2) makes

\[
\chi_\eta J_0-\phi_\eta\ge0
\tag{23}
\]

pointwise in the spectral variable. Because the notch vanishes on `B_n`,

\[
\begin{aligned}
\chi_\eta\frac{E_0(W_n)}{L_n}-h_n
&=
\frac1{L_n}
\int_{-1}^{1}
(\chi_\eta J_0-\phi_\eta)|S_{W_n}|^2\\
&\ge
\chi_\eta R_n.
\end{aligned}
\tag{24}
\]

Using near-extremality (3),

\[
\boxed{
R_n
\le
1-\frac{h_n}{\chi_\eta}+o(1).
}
\tag{25}
\]

Combining (22) and (25) proves (9)--(10). The inequality has a simple interpretation: the normalized notch deficit

\[
1-h_n/\chi_\eta
\tag{26}
\]

is an upper budget for every source component living where the notch is identically zero. The off-notch companion constructed by polarization consumes at least `(M_n-X_n)^2/(4M_n)` of precisely that budget.

For the fixed triangle used in `ANF-099`, recall its fatal threshold

\[
B_\eta
=
\frac{C(\phi_\eta)}{C(J_0)}.
\tag{27}
\]

The elementary domination (2) already gives the global exposure ceiling

\[
\beta_\eta\le\chi_\eta.
\tag{28}
\]

If `chi_eta < B_eta`, the fixed-notch ray is therefore settled immediately by `ANF-099`. In the unresolved regime `B_eta<=chi_eta`, every fatal sequence containing a bounded-mass packet of the present type must instead satisfy

\[
\boxed{
\limsup_n
\frac{(M_n-X_n)^2}{4M_n}
\le
1-\frac{B_\eta}{\chi_\eta}.
}
\tag{29}
\]

Thus the only remaining room is quantified by a single fixed efficiency gap. If the fatal threshold lies close to the notch's pointwise source efficiency, the remainder defect must be correspondingly close to the packet source mass.

## 3. Efficiency saturation forces full bounded-mass profile mirroring

Assume now (11). Equation (25) gives `R_n -> 0`, while (22) and `M_n>=lambda` give

\[
X_n-M_n\to0.
\tag{30}
\]

Equation (21) then yields

\[
\frac{E_{B_n}(U_n)}{L_n}
=b_n
=M_n+o(1).
\tag{31}
\]

Together with (18),

\[
\frac{E_{B_n}(U_n)}{E_{B_n}(P_n)}\to1.
\tag{32}
\]

Similarly, (17) and (30) imply

\[
\frac{\mathcal C_{B_n}(P_n,U_n)}{E_{B_n}(P_n)}
\to-1.
\tag{33}
\]

Finally,

\[
\frac{E_{B_n}(W_n)}{E_{B_n}(P_n)}
=
\frac{R_n}{M_n+o(1)}
\to0.
\tag{34}
\]

This is Hilbert-space profile mirroring, not merely equality of scalar energies: `S_U` has the same asymptotic norm as `S_P` inside the saddle band, their normalized inner product tends to `-1`, and their sum tends to zero relative to the packet norm. Equivalently,

\[
\frac{
\|\mathbf1_{B_n}(S_{P_n}+S_{U_n})\|_0^2
}{E_{B_n}(P_n)}
\to0.
\tag{35}
\]

For the interior-saddle clouds of `ANF-118`, take

\[
B_A
=
\left\{
\alpha:
\bigl||\alpha|-a_\gamma\bigr|
\le\frac{s_A}{\sqrt A}
\right\},
\qquad
s_A\to\infty
\tag{36}
\]

slowly. Whenever the central notch width satisfies `eta<a_gamma`, this band is eventually disjoint from the notch support, while `ANF-118` supplies the localization (7). Therefore (9)--(35) apply directly to every bounded Gram-mass cloud in that family.

A useful quantitative version follows without taking the efficiency limit. If, for some `delta in [0,1)`,

\[
h_n\ge\chi_\eta(1-\delta)+o(1),
\tag{37}
\]

then

\[
\boxed{
\limsup_n R_n\le\delta,
\qquad
\limsup_n\frac{(M_n-X_n)^2}{4M_n}\le\delta,
\qquad
\limsup_n
\frac{E_{B_n}(W_n)}{E_{B_n}(P_n)}
\le\frac\delta\lambda.
}
\tag{38}
\]

So profile mirroring is stable: it does not require exact saturation before imposing a quantitative constraint.

## 4. A two-band Hilbert model saturates the corridor

The new bound cannot be improved using only the Hilbert geometry, affine defect identity, and pointwise domination `phi_eta<=chi_eta J_0`. Consider an abstract two-dimensional source Hilbert space with orthonormal vectors `e_B,e_C`, where the notch is zero on `e_B` and acts with efficiency `chi` on `e_C`. Normalize `L=1` and set

\[
P=\sqrt M\,e_B,
\qquad
U_B=-\frac{M+X}{2\sqrt M}\,e_B.
\tag{39}
\]

Choose the orthogonal component `U_C` with

\[
\|U_C\|^2
=
1+X-\frac{(M+X)^2}{4M}
=
1-\frac{(M-X)^2}{4M},
\tag{40}
\]

whenever the right-hand side is nonnegative. Then

\[
\|P+U\|^2=1,
\qquad
\|U\|^2=1+X,
\qquad
\langle P,U\rangle=-\frac{M+X}{2},
\tag{41}
\]

so the near-extremal and polarization bookkeeping are exact. The residual off-notch energy is

\[
R
=
\frac{(M-X)^2}{4M},
\tag{42}
\]

while the notch exposure is

\[
h
=
\chi\left(1-rac{(M-X)^2}{4M}\right).
\tag{43}
\]

Both walls of (9) are therefore equalities. This adversarial control is important: a further improvement cannot come from another application of Cauchy--Schwarz or a more careful scalar energy split. It must exploit **physical realizability** of discrete exponential sums, additional spectral shape of `J_0` and `phi_eta`, or coupling between the off-notch saddle profile and the frequencies at which the notch approaches its maximal source efficiency.

## 5. Prior-art boundary and next gate

The broad compactness language surrounding this result is classical. Lions' concentration--compactness framework studies how minimizing sequences split or lose mass, and Gérard's profile decomposition makes almost-orthogonal profile splitting explicit in a Hilbert/Sobolev setting. Those results motivate the vocabulary of profiles and remainders, but neither is load-bearing here: (9) follows directly from the Mathia-specific Montgomery--Taylor affine polarization identity, the off-notch localization inherited from `ANF-118`--`ANF-119`, and the fixed-notch efficiency (1). No new external theorem is required for the proof, so this finding does not introduce a new `SOURCES.md` dependency.

The frontier after `ANF-119` is therefore narrower. A bounded interior-saddle packet cannot coexist with near-maximal notch exposure through arbitrary overpolarization. The available mismatch is paid exactly from the notch-efficiency deficit, and efficiency saturation forces the same spectral mirroring previously known only when the packet source mass diverges. The remaining physical question is whether a conjugation-invariant discrete configuration can simultaneously realize this off-notch mirror and concentrate enough of its surviving source energy near the spectral locations where `phi_eta/J_0` is most efficient. The saturated two-band model shows that this question is genuinely beyond abstract Hilbert bookkeeping.