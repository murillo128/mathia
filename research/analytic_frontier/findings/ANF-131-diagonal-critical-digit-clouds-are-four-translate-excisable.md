# ANF-131 — diagonal critical digit clouds are four-translate excisable

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + DIAGONAL-CRITICAL-ARITY + SUBEXPONENTIAL-COPY-BUDGET + TWO-ADJACENT-SOURCE-CELLS + FOUR-TRANSLATE-POSITIVE-ANNIHILATOR + FIXED-NOTCH-DARK + GLOBAL-EXCISION + CASCADE-GATE`. `ANF-129` constructs, for every sufficiently large fixed digit arity `q`, a critically tuned positive `q`-ary translation cloud whose original `ANF-115` saddle is evacuated while the complete Montgomery--Taylor source norm remains comparable to one packet. `ANF-130` then excises every fixed-`q` critical block after a finite positive outer annihilator, but deliberately leaves open a diagonal escape `q=q(A)->infinity`, because the regenerated maxima move toward the cancelled saddle and the number and conditioning of fixed-`q` critical chambers need not be uniform.

That diagonal escape does **not** survive at the `ANF-129` critical repetition density. If `q_A->infinity` and the number of critical digit levels is

\[
h_A:=\lfloor r_{q_A}A\rfloor,
\]

where `r_q` is the exact critical density of `ANF-129`, then on every nontrivial subsequence `h_A>=1` the entire digit cloud has subexponential copy budget, its source norm is still `Theta(E_A)`, and all source mass outside the two digit cells immediately adjacent to the cancelled saddle is negligible. Each adjacent cell has a unique exact source maximum and Gaussian width `O(A^{-1/2})`. A positive polynomial containing only two binary translation factors can be chosen to vanish at those two maxima. Its expansion uses exactly four translated copies of the complete cloud and reduces the total source norm to `o(E_A)` while preserving exponential fixed-notch darkness and negligible affine cardinality. Hence a diagonal critically tuned `ANF-129` block plus its same-orbit mirror is globally excisable.

The fixed-`q` and diagonal critical regimes are therefore both closed inside the same-profile translation orbit. Sending `q` to infinity does not convert the bounded-source critical architecture into an essential fatal component. The live positive-translation route must either move above critical density into a genuinely positive-rate cascade such as `ANF-128`, or introduce a profile-transverse component whose source landscape is not inherited from the critical block.

## 1. Critical diagonalization automatically makes the copy budget subexponential

Fix `gamma>0` and the `ANF-115` packet

\[
P_A=P_{A,\lfloor\gamma A\rfloor},
\qquad
E_A=E_0(P_A),
\qquad
a=a_\gamma,
\qquad
f=F_\gamma(a),
\qquad
c_\gamma=-F_\gamma''(a)>0.
\tag{1}
\]

For every sufficiently large integer `q`, retain the `ANF-129` notation

\[
D_q(x)=\sum_{v=0}^{q-1}e^{-2\pi i vx},
\qquad
d_q=\frac{q-1}{qa},
\qquad
K_q=d_q\frac{\pi q}{\sin(\pi/q)}.
\tag{2}
\]

The point `a` is a simple digit zero because

\[
ad_q=1-\frac1q,
\qquad
D_q(ad_q)=0.
\tag{3}
\]

Let `r_q` be the exact critical density from `ANF-129`, so that

\[
\Psi_q(\alpha)
:=F_\gamma(\alpha)-f
+2r_q\log|D_q(d_q\alpha)|
\tag{4}
\]

satisfies

\[
\sup_{0\le\alpha<1}\Psi_q(\alpha)=0,
\tag{5}
\]

and

\[
r_qK_q^2\longrightarrow\frac{e c_\gamma}{2},
\qquad
K_q\sim\frac{q^2}{a},
\qquad
\rho_q:=r_q\log q\sim
\frac{e c_\gamma a^2}{2}\frac{\log q}{q^4}.
\tag{6}
\]

Now let

\[
q=q_A\longrightarrow\infty,
\qquad
h_A:=\lfloor r_qA\rfloor.
\tag{7}
\]

If `h_A=0` along a subsequence, there is no nontrivial critical digit layer on that subsequence, so it supplies no diagonal escape. Restrict therefore to the nontrivial case

\[
h_A\ge1.
\tag{8}
\]

Equation (6) immediately forces

\[
r_qA\ge1
\quad\Longrightarrow\quad
q^4\ll_\gamma A,
\tag{9}
\]

and hence

\[
q=O_\gamma(A^{1/4}).
\tag{10}
\]

This elementary consequence is the key diagonal scale. The cloud can no longer carry a fixed positive exponential copy rate. Indeed, form the admissible positive multiset

\[
X_A
:=
\underset{v_1,\ldots,v_{h_A}\in\{0,\ldots,q-1\}}
{\bigsqcup}
\left(P_A+d_q\sum_{\ell=1}^{h_A}v_\ell\right).
\tag{11}
\]

Coincident translation sums in (11) are retained as positive multiplicities, which are allowed in the physical multiset class. Its exact modulation is

\[
S_{X_A}(\alpha)
=p_A(\alpha)S_{P_A}(\alpha),
\qquad
p_A(\alpha)=D_q(d_q\alpha)^{h_A},
\tag{12}
\]

and the number of translated packet copies, counted with multiplicity, is

\[
\mathcal U_A=q^{h_A}.
\tag{13}
\]

Because `h_A/A<=r_q`,

\[
\boxed{
\frac1A\log\mathcal U_A
=\frac{h_A}{A}\log q
\le\rho_q
\longrightarrow0.
}
\tag{14}
\]

Thus the diagonal critical construction is internally complicated but **subexponential on the ambient `A` scale**. This is exactly the regime in which a uniform finite-chamber description can again become decisive.

## 2. The floor cannot create a hidden source peak

Put

\[
s_A:=\frac{h_A}{A},
\qquad
\Phi_A(\alpha)
:=F_\gamma(\alpha)-f
+2s_A\log|D_q(d_q\alpha)|.
\tag{15}
\]

Although `s_A` differs from the ideal critical density `r_q`, the floor has a useful one-sided structure. If

\[
|D_q(d_q\alpha)|\ge1,
\]

then `s_A<=r_q` and therefore

\[
\Phi_A(\alpha)
\le\Psi_q(\alpha)
\le0.
\tag{16}
\]

If instead

\[
|D_q(d_q\alpha)|\le1,
\]

then the digit term in (15) is nonpositive, while the strict saddle property of `F_gamma` gives

\[
\Phi_A(\alpha)
\le F_\gamma(\alpha)-f
\le0.
\tag{17}
\]

Hence the exact floor satisfies the global exponential inequality

\[
\boxed{
\Phi_A(\alpha)\le0
\qquad(0\le\alpha<1).
}
\tag{18}
\]

There is also a matching point whose loss is only bounded. Let `alpha_q` be any global critical maximizer of `Psi_q`. The local scaling in `ANF-129` gives

\[
K_q|\alpha_q-a|\longrightarrow\sqrt e,
\qquad
|D_q(d_q\alpha_q)|\longrightarrow\sqrt e>1.
\tag{19}
\]

Writing `{x}` for fractional part and using `Psi_q(alpha_q)=0`,

\[
\begin{aligned}
A\Phi_A(\alpha_q)
&=
A\Psi_q(\alpha_q)
-2(r_qA-h_A)\log|D_q(d_q\alpha_q)|\\
&=-2\{r_qA\}\log|D_q(d_q\alpha_q)|
=O_\gamma(1).
\end{aligned}
\tag{20}
\]

Thus the floor neither creates positive exponential growth nor destroys the critical source completely.

The exact `ANF-115` density refines this exponential statement to a bounded source ratio. On a fixed neighborhood of `a`, that finding gives

\[
J_0(\alpha)|S_{P_A}(\alpha)|^2
=m_A^2\exp\!\left(AF_\gamma(\alpha)+B_A(\alpha)\right),
\tag{21}
\]

where `B_A` and its first two derivatives are uniformly bounded. The denominator satisfies the standard fixed-saddle comparison

\[
E_A\asymp_\gamma
m_A^2\frac{e^{Af}}{\sqrt A}.
\tag{22}
\]

It remains to prove that only a bounded number of numerator cells can live on that scale.

## 3. Every nonadjacent digit cell is negligible

The zeros of `D_q(d_q\alpha)` are separated by

\[
\frac1{qd_q}=\Theta_\gamma(q^{-1}).
\tag{23}
\]

Let `I_{A,-}` and `I_{A,+}` denote the two open digit cells having the root `alpha=a` as their common boundary. Every other digit cell in `[0,1]` lies at distance at least `c_\gamma/q` from `a`. Strict concavity of `F_gamma` therefore gives, uniformly on the union of all those nonadjacent cells,

\[
F_\gamma(\alpha)-f
\le-rac{c_1}{q^2}
\tag{24}
\]

for a fixed `c_1>0` and all large `q`, until one reaches a fixed neighborhood boundary; farther away there is a fixed negative gap. Since

\[
|D_q|\le q,
\qquad
2s_A\log q\le2\rho_q=O_\gamma\!\left(\frac{\log q}{q^4}\right),
\tag{25}
\]

we obtain

\[
\boxed{
\sup_{\alpha\notin I_{A,-}\cup I_{A,+}}
\Phi_A(\alpha)
\le-rac{c_2}{q^2}
}
\tag{26}
\]

apart from fixed regions where the stronger constant gap applies. By (9),

\[
\frac{A}{q^2}\gg_\gamma q^2\longrightarrow\infty.
\tag{27}
\]

There are only `O_\gamma(q)` digit cells in `[0,1]`. Combining (21), (26), the endpoint bounds already used in `ANF-115`, and (27) shows

\[
\boxed{
E_{([-1,1]\setminus(\pm I_{A,-}\cup\pm I_{A,+}))}(X_A)
=o(E_A).
}
\tag{28}
\]

The diagonal source therefore has an **at-most-two-cell positive-frequency skeleton**, regardless of how many fixed-`q` critical maxima existed before `q` began to move.

Inside either adjacent cell, the source logarithm is uniformly strongly concave. The elementary identity already used in `ANF-129` gives, between consecutive digit zeros,

\[
\frac{d^2}{dx^2}\log|D_q(x)|
=
\pi^2\csc^2(\pi x)
-
\pi^2q^2\csc^2(\pi qx)
\le0.
\tag{29}
\]

Together with `F_gamma''<0` and the bounded `B_A''`, the exact positive-frequency source log-density `H_A` of `X_A` satisfies

\[
\boxed{
H_A''(\alpha)\le-c_3A
\qquad
(\alpha\in I_{A,-}\cup I_{A,+})
}
\tag{30}
\]

for some fixed `c_3>0` and all large `A`. Since the density vanishes at the common digit root and at the other endpoint root of each cell, there is a unique exact maximizer

\[
\xi_{A,-}\in I_{A,-},
\qquad
\xi_{A,+}\in I_{A,+}.
\tag{31}
\]

The local scaling of `ANF-129` also remains uniform after the floor. If

\[
\vartheta_A:=\frac{h_A}{r_qA},
\]

then `h_A>=1` implies

\[
\frac12\le\vartheta_A\le1.
\tag{32}
\]

The rescaled floor landscape has limiting stationary points

\[
u^2=e\vartheta_A,
\]

and the bounded derivative `B_A'` produces only a lower-order displacement. Consequently

\[
\boxed{
K_q|\xi_{A,\pm}-a|=\sqrt{e\vartheta_A}+o(1),
}
\tag{33}
\]

on every side whose local branch is retained; in particular both exact cell maxima lie at distance

\[
|\xi_{A,\pm}-a|=\Theta_\gamma(q^{-2})
\tag{34}
\]

and each has natural width `O(A^{-1/2})`. One side may carry asymptotically less mass because the finite-`q` landscape is not exactly symmetric about the root; keeping both cells is deliberately robust against that asymmetry.

Equations (18), (20), (22), (28), and the strong-concavity bound (30) now give the two-sided source estimate

\[
\boxed{
0<c_\gamma
\le
\frac{E_0(X_A)}{E_A}
\le C_\gamma<\infty
}
\tag{35}
\]

along every nontrivial diagonal subsequence. The constants can be enlarged to cover the initial finite range of `q`; no convergence of the ratio is asserted or needed. The floor can leave bounded oscillation just as in fixed-`q` `ANF-129`.

## 4. Two binary factors annihilate the complete diagonal source

Define bounded positive translations

\[
\tau_{A,-}:=\frac1{2\xi_{A,-}},
\qquad
\tau_{A,+}:=\frac1{2\xi_{A,+}},
\tag{36}
\]

and the degree-two positive translation polynomial

\[
Q_A(\alpha)
:=
\left(1+e^{-2\pi i\tau_{A,-}\alpha}\right)
\left(1+e^{-2\pi i\tau_{A,+}\alpha}\right).
\tag{37}
\]

It vanishes at both signs of both exact maxima,

\[
Q_A(\pm\xi_{A,-})
=Q_A(\pm\xi_{A,+})=0,
\tag{38}
\]

and expands as

\[
Q_A(\alpha)
=
1
+e^{-2\pi i\tau_{A,-}\alpha}
+e^{-2\pi i\tau_{A,+}\alpha}
+e^{-2\pi i(\tau_{A,-}+\tau_{A,+})\alpha}.
\tag{39}
\]

Thus it is exactly the modulation of **four positive translated copies** of the whole cloud `X_A`, counted with multiplicity if any translated physical sites coincide. Let `Y_A` denote that four-copy outer cloud. Then

\[
S_{Y_A}(\alpha)=Q_A(\alpha)S_{X_A}(\alpha).
\tag{40}
\]

The translations in (36) stay in a fixed compact subset of `(0,infinity)` because `xi_{A,\pm}->a`. Hence near either cell maximum

\[
|Q_A(\alpha)|^2
\le C_\gamma|\alpha-\xi_{A,\pm}|^2,
\tag{41}
\]

with a constant independent of `A`; if the two maxima approach each other on the same Gaussian scale, the second zero only strengthens the estimate. From (30),

\[
H_A(\alpha)
\le H_A(\xi_{A,\pm})
-\frac{c_3A}{2}|\alpha-\xi_{A,\pm}|^2.
\tag{42}
\]

Integrating (41)--(42) on the two adjacent cells, using the bounded source ratio (35), and charging all remaining cells by (28), gives

\[
\boxed{
\frac{E_0(Y_A)}{E_A}
=O_\gamma(A^{-1})+o(1)
=o(1).
}
\tag{43}
\]

Write

\[
Y_A=X_A\sqcup U_A,
\tag{44}
\]

where `U_A` is the union of the three nonconstant translation terms in (39). Equation (35) and (43) imply

\[
\|S_{X_A}+S_{U_A}\|_0=o(\sqrt{E_A}),
\qquad
\|S_{X_A}\|_0\asymp\sqrt{E_A}.
\tag{45}
\]

The reverse triangle inequality and expansion of the source norm therefore yield

\[
\boxed{
E_0(U_A)=E_0(X_A)+o(E_A),
\qquad
\mathcal C_0(X_A,U_A)
=-E_0(X_A)+o(E_A).
}
\tag{46}
\]

The diagonal critical cloud consequently admits an explicit **complete-source physical mirror**, not merely cancellation in a chosen saddle window. As in `ANF-122` and fixed-`q` `ANF-130`, the price of realizing that mirror is that the aggregate mirror block itself becomes source-negligible and hence excisable.

## 5. Fixed-notch darkness and affine negligibility survive the diagonal

Fix a central notch width

\[
0<\eta<a.
\tag{47}
\]

The base saddle has a fixed positive gap

\[
\Delta_\eta
:=f-\sup_{0\le\alpha\le\eta}F_\gamma(\alpha)>0.
\tag{48}
\]

Using `|D_q|<=q` and (14), uniformly on the notch,

\[
\Phi_A(\alpha)
\le-\Delta_\eta+2\rho_q
\le-\frac{\Delta_\eta}{2}
\tag{49}
\]

for all sufficiently large `A`. The exact packet prefactors are subexponential there, so

\[
\boxed{
E_\eta(X_A)
\le e^{-c_{\gamma,\eta}A}E_A.
}
\tag{50}
\]

Because `|Q_A|<=4`, the same is true for the annihilated four-copy block:

\[
\boxed{
E_\eta(Y_A)=o(E_A).
}
\tag{51}
\]

Affine cardinality is even cheaper. From `ANF-115`,

\[
m_A=|P_A|=\exp((\gamma\log2+o(1))A),
\qquad
E_A=\exp((2\gamma\log2+f+o(1))A).
\tag{52}
\]

Together with (14),

\[
\frac1A\log\frac{|X_A|}{E_A}
\le
-\gamma\log2-f+o(1)<0.
\tag{53}
\]

Multiplying by four copies does not change the exponent, so

\[
\boxed{|Y_A|=o(E_A).}
\tag{54}
\]

Suppose now that a Montgomery--Taylor near-extremizing family contains this diagonal mirror block at macroscopic packet scale,

\[
W_A=Y_A\sqcup R_A,
\qquad
\frac{E_0(W_A)}{L_A}=1+o(1),
\qquad
0<\lambda\le\frac{E_A}{L_A}\le\Lambda.
\tag{55}
\]

Then (43), (51), (54), the Hilbert triangle inequality, and the same deletion bookkeeping as `ANF-130` give

\[
\boxed{
\frac{E_0(R_A)}{L(R_A)}\to1,
\qquad
\frac{E_\eta(R_A)-E_\eta(W_A)}{L_A}\to0.
}
\tag{56}
\]

Thus the complete diagonal same-orbit mirror is irrelevant to the fixed-notch exposure envelope `beta_eta` of `ANF-099`.

## 6. Adversarial controls and exact scope

The main possible escape was the coalescence of the regenerated maxima as `q->infinity`. Equation (34) shows that their displacement from the old saddle is `Theta(q^{-2})`. At the fastest nontrivial diagonal scale `q asymp A^{1/4}`, this is exactly the natural Gaussian width `A^{-1/2}`; the two cells can therefore become mesoscopically inseparable. The proof does not require them to remain separated by many Gaussian widths. It annihilates the unique exact maximum in **each** adjacent digit cell, and the two translation parameters remain bounded even when the zeros coalesce.

The floor is another genuine issue. One cannot simply replace `h_A` by `r_qA` in a diagonal argument because when `r_qA=O(1)` the relative floor error is order one. Equations (16)--(20) avoid that mistake: the floor has the correct monotonic sign on `|D_q|>=1`, while on `|D_q|<=1` the base saddle alone prevents growth. The nontriviality assumption `h_A>=1` also gives the uniform ratio `1/2<=h_A/(r_qA)<=1`, which is why the local critical scale remains `Theta(q^{-2})`.

The proof intentionally uses the unperturbed digit spacing and allows positive multiplicities. This is already inside the finite conjugation-invariant multiset class and makes the global floor inequality (18) exact. The `O(A^{-4})` distinctness perturbations used in `ANF-129` are a stronger cosmetic realization, not an admissibility requirement here. On the dominant cells their root displacement is negligible relative to `q^{-2}` because (10) gives `q^{-2}>=cA^{-1/2}`, and the summed logarithmic perturbation is `o(1)`; hence the local two-cell and four-annihilator picture is stable if distinct translated packet copies are additionally desired. No distinctness claim is needed for the theorem above.

Most importantly, this does **not** collapse `ANF-128`. There the repetition depth is

\[
h_A\sim\frac{\rho A}{\log q_A}
\]

with a fixed positive copy-rate `rho`, rather than the critical depth `r_qA=Theta(A/q^4)`. Its regenerated chamber can therefore carry `exp(cA)` excess source. A fixed pair of binary zeros buys only Gaussian polynomial suppression and cannot excise such an exponentially oversized reservoir. `ANF-131` closes the diagonal **critical bounded-source** route, not the positive-rate moving-arity cascade.

Nor does the result address a profile-transverse companion. The four-copy annihilator exploits the exact translation factorization of the complete diagonal block. Another vertical profile, another base saddle family, or a component whose notch/source landscape is not a scalar modulation of `X_A` remains outside the theorem.

## 7. Prior-art boundary and remaining gate

Parameter-dependent Laplace asymptotics with moving or coalescing stationary points are classical. Bleistein's 1966 work on uniform asymptotic expansions near moving singular/stationary geometry, later uniform Laplace treatments for coalescing saddles, and the Chester--Friedman--Ursell steepest-descent framework are natural neighboring references. Dirichlet kernels, geometric sums, and positive products of translation factors are likewise classical harmonic-analysis objects.

None of that literature is load-bearing for the Mathia statement. The proof here needs only the exact `ANF-129` critical relation, the elementary sign split in (16)--(17), strict concavity of the `ANF-115` saddle, the exact logarithmic concavity identity (29), and the explicit four-term positive expansion (39). The new content is the uniform coupling of these facts to Montgomery--Taylor source mass, the `q^4\ll A` diagonal scale, complete-source mirroring, fixed-notch darkness, and affine excision. No new durable dependency is therefore required in `research/analytic_frontier/SOURCES.md`.

Together, `ANF-130` and `ANF-131` close both ways of keeping the `ANF-129` architecture at its bounded-source critical density: bounded `q` is finitely annihilable by `ANF-130`, while unbounded diagonal `q` collapses to the two adjacent cells and the four-copy annihilator above. The same-profile route that remains is genuinely supercritical: a second positive exponential layer, a moving-arity positive-rate cascade, or a different physical profile. No clue disposition changes are justified by this result.