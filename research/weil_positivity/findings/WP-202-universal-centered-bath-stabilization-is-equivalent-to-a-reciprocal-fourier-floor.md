# WP-202 — Universal centered-bath stabilization is equivalent to a reciprocal Fourier floor

**Status:** `DERIVED + EXACT + HIGHER-ORDER-SPECTRAL-SHIFT + COMMUTING-INFINITE-DIMENSIONAL + CENTERED-DIAGONAL-BATH-CLASSIFICATION + NECESSARY-AND-SUFFICIENT + FULL-WEIL-AUTOCORRELATION-CONE + PHASE-SELECTION + MATCHED-NONARITHMETIC-CONTROL + DECISIVE-NARROWING + PRIOR-ART-AUDITED + NOT-A-WEIL-BRIDGE`.

`WP-199` showed that one rough centered diagonal bath can stabilize every fixed finite-dimensional monotone-positive payload, `WP-200` classified the complete power-law family, and `WP-201` showed that the same Schatten roughness can fail when the singular values are lacunary. The remaining gap is whether the reciprocal-scale Fourier lower envelope is merely a useful sufficient condition or the actual boundary of this direct-sum mechanism.

For centered diagonal baths it is the exact boundary.

Fix

\[
n=4k\ge 4,
\tag{1}
\]

and let

\[
H_0=0,
\qquad
V_0=\operatorname{diag}(a_1,a_2,\ldots)\ge0,
\qquad
0\ne V_0\in\mathcal S^n,
\tag{2}
\]

where zero entries may be discarded. Let

\[
F_0(\xi)
=
\widehat{\eta_{n,0,V_0}^{\rm ev}}(\xi)
\tag{3}
\]

be the even Fourier multiplier of its order-`n` higher-order spectral-shift density. Then the following are equivalent:

\[
\boxed{
\begin{array}{ll}
\text{(i)} & \text{For every finite-dimensional }H_f\ge0,\ V_f\ge0,\text{ there is a finite }M\ge1\\
& \text{such that }0^{\oplus M}\oplus H_f,\ V_0^{\oplus M}\oplus V_f
\text{ is positive on the full real Weil autocorrelation cone};\\[4pt]
\text{(ii)} & \displaystyle \liminf_{|\xi|\to\infty}|\xi|F_0(\xi)>0.
\end{array}
}
\tag{4}
\]

Thus the true resource in `WP-199`--`WP-201` is neither infinite dimension nor the Schatten strip by itself. It is a **uniform reciprocal-frequency positive floor**. If that floor is absent, a single fixed one-dimensional positive payload can always be chosen whose source phase finds infinitely many weak frequencies and defeats every finite bath multiplicity.

This is still a matched-control theorem, not a Weil bridge. Condition (ii) contains no arithmetic selector, Gamma term, pole term, or finite--archimedean incidence and can be satisfied by completely nonarithmetic baths.

## 1. Every nonzero centered diagonal bath has a strictly positive continuous multiplier

For one centered scalar channel of size `a>0`, `WP-198` gives

\[
F_a(\xi)
=
\frac1{(n-3)!\,\xi^2}
\int_0^a(1-\cos(t\xi))(a-t)^{n-3}\,dt
\qquad(\xi\ne0),
\tag{5}
\]

with

\[
F_a(0)=\frac{a^n}{n!}.
\tag{6}
\]

Every term in (5) is nonnegative and the integrand is not identically zero for `xi!=0`, so

\[
F_a(\xi)>0
\qquad(\xi\in\mathbb R).
\tag{7}
\]

Moreover

\[
0<F_a(\xi)\le \frac{a^n}{n!}.
\tag{8}
\]

Since `sum_j a_j^n<infinity`, the series

\[
F_0(\xi)=\sum_jF_{a_j}(\xi)
\tag{9}
\]

converges uniformly. Therefore

\[
\boxed{
F_0\in C(\mathbb R),
\qquad
F_0(\xi)>0\quad\text{for every }\xi\in\mathbb R.
}
\tag{10}
\]

This compact-frequency positivity is important: once the high-frequency ratio is controlled, no additional obstruction can hide on a bounded interval.

## 2. The reciprocal floor is sufficient

Let `(H_f,V_f)` be an arbitrary finite-dimensional self-adjoint pair with

\[
H_f\ge0,
\qquad
V_f\ge0.
\tag{11}
\]

No commutativity assumption is imposed. Write

\[
G_f(\xi)=\widehat{\eta_f^{\rm ev}}(\xi).
\tag{12}
\]

The finite-dimensional source-jump formula used in `WP-197` and `WP-199` gives

\[
G_f(\xi)
=
-\frac1\xi
\sum_{\lambda\in\sigma(H_f)}
J_\lambda\sin(\lambda\xi)
+o(|\xi|^{-1}),
\qquad
J_\lambda\ge0,
\tag{13}
\]

and hence constants `C_f,R_f>0` with

\[
|G_f(\xi)|\le\frac{C_f}{|\xi|}
\qquad(|\xi|\ge R_f).
\tag{14}
\]

Assume condition (ii) in (4). Then there are `c,R>0` such that

\[
F_0(\xi)\ge\frac c{|\xi|}
\qquad(|\xi|\ge R).
\tag{15}
\]

Combining (14)--(15) bounds `|G_f|/F_0` at high frequency. On the compact interval `[-max(R,R_f),max(R,R_f)]`, continuity and (10) give a strictly positive minimum for `F_0`, while `G_f` is bounded. Thus

\[
K_f
:=
\sup_{\xi\in\mathbb R}
\frac{|G_f(\xi)|}{F_0(\xi)}
<\infty.
\tag{16}
\]

Choose an integer

\[
M>K_f.
\tag{17}
\]

Direct-sum additivity gives the completed multiplier

\[
\widetilde F_M(\xi)=MF_0(\xi)+G_f(\xi)>0
\qquad(\xi\in\mathbb R).
\tag{18}
\]

The exact order-`4k` criterion of `WP-193` then gives strict positivity of the Taylor remainder on every nonzero real compactly supported smooth autocorrelation. This proves `(ii) => (i)`.

The proof shows that the `1/|xi|` scale is not an artifact of the power-law estimates in `WP-200`: it is forced by the universal high-frequency defect class of finite positive payloads.

## 3. A phase-selection lemma turns arbitrary Fourier valleys into one fixed source

For necessity, suppose

\[
\liminf_{\xi\to+\infty}\xi F_0(\xi)=0.
\tag{19}
\]

Choose a sequence

\[
\xi_m\to\infty,
\qquad
\xi_mF_0(\xi_m)\to0.
\tag{20}
\]

Unlike `WP-201`, do **not** arrange these valley frequencies to match a preselected scalar source. Instead select one source location after the valley sequence is known.

For each `m`, define

\[
E_m
=
\{h\in[1,2]:\sin(h\xi_m)>1/2\}.
\tag{21}
\]

The set where `sin x>1/2` occupies exactly one third of every full `2pi` period. Under `x=h xi_m`, the interval `h in [1,2]` becomes an interval of length `xi_m`, so elementary periodic counting gives

\[
|E_m|=\frac13+O(\xi_m^{-1}).
\tag{22}
\]

In particular, `|E_m|>=1/4` for all sufficiently large `m`. Since

\[
\left|\bigcup_{m\ge N}E_m\right|
\ge
\sup_{m\ge N}|E_m|,
\tag{23}
\]

continuity of Lebesgue measure from above gives

\[
\left|\limsup_{m\to\infty}E_m\right|
=
\lim_{N\to\infty}
\left|\bigcup_{m\ge N}E_m\right|
\ge\frac14.
\tag{24}
\]

Hence there exists one fixed

\[
h\in[1,2]
\tag{25}
\]

and an infinite subsequence, still denoted `xi_m`, such that

\[
\sin(h\xi_m)>\frac12
\tag{26}
\]

for every member of that subsequence.

This elementary lemma is the missing converse mechanism. Arbitrarily deep reciprocal-scale valleys cannot hide from **all** positive source phases; one fixed source phase sees infinitely many of them.

## 4. One scalar positive payload defeats every finite multiplicity when the floor fails

Use the fixed scalar pair selected above:

\[
H_f=h,
\qquad
V_f=1.
\tag{27}
\]

Its order-`n` spectral-shift density is

\[
q_h(x)
=
\frac{(h+1-x)^{n-1}}{(n-1)!}
\mathbf1_{[h,h+1]}(x).
\tag{28}
\]

Set

\[
J=\frac1{(n-1)!}.
\tag{29}
\]

Integration by parts gives its even Fourier multiplier directly:

\[
\begin{aligned}
G_h(\xi)
&=\int_h^{h+1}q_h(x)\cos(\xi x)\,dx\\
&=-\frac{J\sin(h\xi)}{\xi}
-\frac1\xi\int_h^{h+1}q_h'(x)\sin(\xi x)\,dx.
\end{aligned}
\tag{30}
\]

Because `q_h' in L^1`, the Riemann--Lebesgue lemma yields

\[
G_h(\xi)
=
-\frac{J\sin(h\xi)}{\xi}
+o(|\xi|^{-1}).
\tag{31}
\]

Along the subsequence from (26),

\[
\limsup_{m\to\infty}
\xi_mG_h(\xi_m)
\le -\frac J2<0.
\tag{32}
\]

Now fix **any** finite bath multiplicity `M`. Equations (20) and (32) imply

\[
\limsup_{m\to\infty}
\xi_m\bigl(MF_0(\xi_m)+G_h(\xi_m)\bigr)
\le -\frac J2<0.
\tag{33}
\]

Thus the completed multiplier is negative at infinitely many frequencies. By `WP-193`, the corresponding order-`4k` Taylor remainder is negative on some real compactly supported smooth autocorrelation. Since the same fixed scalar pair (27) defeats every finite `M`, property (i) fails.

This proves `(i) => (ii)` by contraposition and establishes the equivalence (4).

## 5. The criterion unifies the finite, power-law, and lacunary regimes

The equivalence turns the preceding examples into instances of one exact classification.

For a **finite** centered bath, each scalar summand in (5) is `O(|xi|^{-2})`, so

\[
|\xi|F_0(\xi)\longrightarrow0.
\tag{34}
\]

Hence no finite centered reservoir can universally stabilize all finite positive payloads. This is consistent with the finite positive-source obstruction of `WP-197`.

For the rough **power-law** baths of `WP-200`, the lower-bound calculation gives

\[
F_0(\xi)\gtrsim |\xi|^{-\beta},
\qquad
0<\beta\le1,
\tag{35}
\]

throughout the exact stabilizing strip. Therefore (ii) holds, recovering their universal stabilization without any power-law-specific converse argument.

For the **lacunary** bath of `WP-201`,

\[
\liminf_{\xi\to\infty}\xi F_0(\xi)=0,
\tag{36}
\]

so universal stabilization fails automatically. `WP-201` arranged its valleys at the phase of the predetermined payload `H_f=V_f=1`; the present phase-selection lemma shows that such alignment is unnecessary for the general classification.

The distinction exposed by `WP-201` is therefore exact:

\[
\boxed{
\text{universal finite-payload stabilization}
\quad\Longleftrightarrow\quad
\text{uniform reciprocal-frequency floor}.
}
\tag{37}
\]

Schatten membership constrains total spectral-shift mass, while (37) constrains how that mass remains visible across frequency scales. They are different pieces of information.

## 6. Aggressive falsification and exact scope

**Does necessity tune the payload separately at every weak frequency?** No. The phase-selection lemma chooses one `h` once. The same scalar positive pair `(h,1)` defeats every fixed finite multiplicity along an infinite subsequence.

**Does the argument rely on commutativity of the arbitrary finite payload?** Sufficiency does not. Equation (13) is the finite-dimensional source-jump result already used in `WP-199` for arbitrary `H_f>=0`, `V_f>=0`, including noncommuting pairs. Necessity needs only one scalar commuting payload because a single counterexample is enough to refute universality.

**Could bounded-frequency zeros invalidate the ratio argument?** No. A nonzero centered diagonal bath has `F_0(xi)>0` at every real frequency by (10). Compact intervals therefore have a positive minimum.

**Is `liminf |xi|F_0>0` claimed to classify every infinite positive completion?** No. It classifies the specific but broad category of nonzero centered diagonal `S^n` baths used as orthogonal direct-sum reservoirs. Coupled, noncentered, noncommuting, resolvent-comparable, or other genuinely different infinite completions require their own trace and order theorems.

**Does pointwise positivity of the higher-order spectral-shift density imply this criterion?** No. Recent work of Chandan Pradhan and Anna Skripka, *Positivity of spectral shift functions and infinite-dimensional BMV conjecture* (arXiv:2512.05587, 2025), proves nonnegativity of all even-order higher-order spectral-shift functions in the Schatten setting. That is a different order: the Weil autocorrelation cone at order `4k` tests nonnegativity of the **Fourier transform of the even density**, equivalently positive-definiteness of that density, not merely its pointwise sign. `WP-201` already supplies a positive density/multiplier reservoir with insufficient uniform floor after an off-zero payload is added.

**Does (37) identify an arithmetic mechanism?** No. The criterion is source-blind. A bath may satisfy it because an arbitrary nonarithmetic singular-value distribution is thick enough across reciprocal scales. Conversely, failure only shows that this appendable-reservoir mechanism cannot dominate every finite payload.

## 7. Prior art and novelty boundary

Higher-order spectral-shift functions for `S^n` perturbations are classical operator-theoretic infrastructure. Denis Potapov, Anna Skripka, and Fedor Sukochev, *Spectral shift function of higher order*, Inventiones Mathematicae **193** (2013), 501--538, DOI `10.1007/s00222-012-0431-2`, establishes existence and `L^1` control of the order-`n` density. Pradhan--Skripka's 2025 preprint strengthens the positivity side by proving the pointwise sign of all even-order densities. Neither result supplies Fourier positive-definiteness on the Weil autocorrelation cone.

The remaining ingredients in the converse are elementary harmonic analysis: the Riemann--Lebesgue lemma and the positive-measure phase-selection argument (21)--(26). A targeted audit for higher-order spectral-shift Fourier positivity, positive-definiteness, autocorrelation-cone positivity, and universal direct-sum stabilization found the standard spectral-shift existence/sign theory and broader relative/resolvent-comparable trace formulas, but no directly matching necessary-and-sufficient stabilization theorem. No broad external novelty claim is inferred from that absence.

The durable Mathia delta is the exact internal classification (4): within the centered diagonal direct-sum category, the reciprocal Fourier floor is not merely sufficient but necessary for universal finite-payload sign manufacture.

## 8. Consequence for `weil_positivity`

This closes the adjustable centered-bath route more sharply. If a proposed `4k` completion appends an independent centered diagonal reservoir and its multiplier satisfies (ii), then full Weil-cone positivity can be manufactured around **any** finite positive payload and therefore does not select the arithmetic source. If (ii) fails, some fixed scalar positive payload defeats every finite reservoir multiplicity.

Accordingly, changing the Schatten exponent, choosing a smoother or rougher diagonal tail, or redistributing diagonal singular values cannot by itself turn this mechanism into an explanatory Weil geometry. A surviving construction must make the reservoir and its scale distribution **source-forced**, or leave the orthogonal centered-diagonal category through genuine finite--infinite coupling, mixed-prime incidence, archimedean interaction, or another global order operation. It must then derive the Mangoldt, Gamma, and polar/global pieces before the sign theorem rather than using an independent Fourier floor to overwhelm whatever finite block is supplied.