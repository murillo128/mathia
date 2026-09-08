# PF-228 — flat-corridor dressing makes inverse-seam multiplicity weak-trace compatible

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + ARITHMETIC-COUNTING + POSITIVE/ROUTE-NARROWING`. PF-226 and PF-227 show that the canonical raw normalized pant crossing carries at least order `s_n^{-1}` channels above a fixed threshold, even after removing any fixed physical-frequency sector. PF-225 shows only that resolvent dressing caps every transmitted channel by `1/2`, leaving open whether this inverse-seam multiplicity is compatible with the weak-trace endpoint. An exact straight-corridor control gives a sharper calibration.

Replace one degenerating pant corridor by a shifted flat cylinder of width `s_n`, and normalize its two facing boundary components by the **symmetric** boundary-energy branches of centered seam strips of halfwidths `w_n,w_{n+1}`. For tangential frequency `\xi`, put

\[
\mu=\sqrt{1+\xi^2},\qquad z=\mu s_n,
\qquad t_i=\tanh(\mu w_i).
\]

The normalized exterior precision is an explicit positive `2\times2` matrix. If `D_{n,\xi}^{\rm cyl}=(I+K_{n,\xi}^{\rm cyl})^{-1}` and `x_{n,\xi}` is the absolute value of its off-diagonal entry, then

\[
\boxed{
 x_{n,\xi}
 =
 \frac{\sqrt{t_nt_{n+1}}}
 {\sinh z\,(1+t_nt_{n+1})+\cosh z\,(t_n+t_{n+1})}
 }
\]

and consequently

\[
\boxed{
 x_{n,\xi}
 \le
 \rho_n\frac{z}{\sinh z},
 \qquad
 \rho_n:=\frac{\sqrt{w_nw_{n+1}}}{s_n}.
 }
\]

Thus inversion does not merely saturate the raw crossing at order one in this matched control. On the whole inverse-seam band `z=O(1)`, it reduces the transmitted amplitude to order `w/s`; for `z\gg1` it adds exponential tangential-frequency decay. Under the canonical prime-flute scales,

\[
w_n\asymp P_n^{-1},\qquad
s_n\asymp\frac{g_n+g_{n+1}}{P_n},
\qquad
\delta_n:=\frac1{P_n}-\frac1{P_{n+1}},
\]

this gives the decisive weighted top scale

\[
\boxed{
\delta_n\rho_n\le \frac{C}{P_n^2}.
}
\]

That extra inverse-gap factor is enough at the distributional endpoint. Even if the straight control is pessimistically periodized with tangential length `\mathcal L_n=O(\log P_n)`, so that it has order `\mathcal L_n/s_n` rather than merely `s_n^{-1}` channels in the `z=O(1)` band, the orthogonal weighted model

\[
T_{\rm cyl}:=\bigoplus_n\delta_n X_n^{\rm cyl}
\]

satisfies

\[
\boxed{T_{\rm cyl}\in\mathcal S_{1,\infty}.}
\]

The proof uses only the exact mode formula above and the elementary Chebyshev bound already proved in PF-210. Hence the raw multiplicity discovered in PF-226/PF-227 is **not by itself a weak-`S_1` obstruction**. A local inverse that pays the natural ratio `w_n/s_n` already moves even a full `O(\mathcal L_n/s_n)` corridor population onto the prime-square singular scale required by threshold counting.

This is a matched-control theorem, **not** a theorem about the actual global cut flux `P[D,E_n]H`. The real pant is not a straight cylinder, its thickness varies, and the global Schur inverse can short through the rest of the flute. PF-228 therefore identifies a quantitative target rather than closing the endpoint: prove that the actual dressed one-seam transmission retains a comparable `w/s` amplitude gain plus physical-frequency decay, or exhibit the specific global mechanism that destroys it.

## Claim

For one edge suppress the index `n`. Let

\[
C_{s,\mathcal L}=[0,s]\times(\mathbb R/\mathcal L\mathbb Z)
\]

carry the flat metric and the positive shifted equation

\[
(-\partial_x^2-\partial_t^2+1)u=0.
\tag{1}
\]

For tangential Fourier frequency

\[
\xi_k=\frac{2\pi k}{\mathcal L},
\qquad
\mu_k=\sqrt{1+\xi_k^2},
\qquad
z_k=\mu_ks,
\tag{2}
\]

the two-boundary Dirichlet-to-Neumann matrix of the corridor is

\[
\Lambda_{E,k}
=
\mu_k
\begin{pmatrix}
\coth z_k&-\operatorname{csch}z_k\\
-\operatorname{csch}z_k&\coth z_k
\end{pmatrix}.
\tag{3}
\]

Now use, on the two adjacent modules, centered flat seam strips of halfwidths `w_1,w_2`. On the equal-value/symmetric branch of the two strip boundaries the exact shifted DtN eigenvalue is

\[
q_{i,k}=\mu_k\tanh(\mu_kw_i),
\qquad i=1,2.
\tag{4}
\]

Define the normalized corridor precision and its resolvent factor by

\[
K_k
=Q_k^{-1/2}\Lambda_{E,k}Q_k^{-1/2},
\qquad
Q_k=\operatorname{diag}(q_{1,k},q_{2,k}),
\qquad
D_k=(I+K_k)^{-1}.
\tag{5}
\]

Let

\[
x_k:=|(D_k)_{21}|.
\tag{6}
\]

Writing

\[
t_i=\tanh(\mu_kw_i),
\tag{7}
\]

direct inversion gives

\[
\boxed{
 x_k
 =
 \frac{\sqrt{t_1t_2}}
 {\sinh z_k(1+t_1t_2)+\cosh z_k(t_1+t_2)}.
}
\tag{8}
\]

In particular, with

\[
\rho:=\frac{\sqrt{w_1w_2}}s,
\tag{9}
\]

one has the uniform envelope

\[
\boxed{
0\le x_k
\le
\rho\frac{z_k}{\sinh z_k}.
}
\tag{10}
\]

If `w_i/s` stay in a fixed bounded range and `w_1/w_2` stays in a fixed compact subset of `(0,\infty)`, then for every fixed sufficiently small `z_0>0` there is also

\[
\boxed{
 x_k\ge c\rho
 \qquad(z_k\le z_0).
}
\tag{11}
\]

Thus the reference inverse still carries order `\mathcal L/s` modes at the natural corridor scale, but their amplitude is order `w/s`, not order one.

For the canonical prime-flute edge let

\[
P_n=p_{n-1},
\qquad
g_n=p_n-p_{n-1},
\qquad
G_n:=g_n+g_{n+1}.
\tag{12}
\]

Use any periodized straight control with

\[
\mathcal L_n\le C(1+\log P_n),
\tag{13}
\]

and canonical scale bounds

\[
w_n,w_{n+1}\le \frac C{P_n},
\qquad
s_n\ge c\frac{G_n}{P_n},
\qquad
\delta_n
=\frac{g_n}{P_nP_{n+1}}
\le C\frac{g_n}{P_n^2}.
\tag{14}
\]

Then

\[
\rho_n
:=\frac{\sqrt{w_nw_{n+1}}}{s_n}
\le \frac C{G_n},
\tag{15}
\]

so

\[
\boxed{
a_n:=\delta_n\rho_n
\le
C\frac{g_n}{P_n^2G_n}
\le\frac C{P_n^2}.
}
\tag{16}
\]

Let `X_n^{\rm cyl}` be the Fourier-diagonal operator with singular values `x_{n,k}` from (8), and place the edge blocks on mutually orthogonal source and target spaces. Then

\[
T_{\rm cyl}:=\bigoplus_n\delta_nX_n^{\rm cyl}
\tag{17}
\]

is compact and belongs to `\mathcal S_{1,\infty}`.

## 1. Exact inversion produces the `w/s` factor

Write

\[
a=\frac{\mu\coth z}{q_1},
\qquad
c=\frac{\mu\coth z}{q_2},
\qquad
b=\frac{\mu\operatorname{csch}z}{\sqrt{q_1q_2}}.
\tag{18}
\]

Then

\[
I+K
=
\begin{pmatrix}
1+a&-b\\
-b&1+c
\end{pmatrix}
\tag{19}
\]

and therefore

\[
x
=\frac{b}{(1+a)(1+c)-b^2}.
\tag{20}
\]

The hyperbolic identity

\[
\coth^2z-\operatorname{csch}^2z=1
\tag{21}
\]

gives

\[
ac-b^2=\frac{\mu^2}{q_1q_2}.
\tag{22}
\]

Substituting `q_i=\mu t_i` into (20), multiplying numerator and denominator by `q_1q_2`, and then multiplying by `\sinh z` gives exactly (8).

For the upper bound, discard all positive terms in the denominator of (8) except `\sinh z` and use `\tanh y\le y`:

\[
\begin{aligned}
x
&\le
\frac{\sqrt{t_1t_2}}{\sinh z}\\
&\le
\frac{\mu\sqrt{w_1w_2}}{\sinh z}\\
&=
\rho\frac{z}{\sinh z},
\end{aligned}
\tag{23}
\]

which is (10).

Equation (11) is equally elementary. On `z\le z_0`, boundedness of `w_i/s` makes `\mu w_i=(w_i/s)z` uniformly bounded, so `\tanh(\mu w_i)\asymp\mu w_i`. Also `\sinh z\asymp z` and `\cosh z\asymp1`. With comparable `w_1,w_2`, numerator and denominator in (8) are respectively comparable to `z\sqrt{w_1w_2}/s` and `z`, proving `x\asymp\rho` on the inverse-seam band.

This is the mechanism hidden by PF-225's universal `1/2` cap. In the straight control, the diagonal exterior energy and the raw crossing grow together. The inverse therefore charges their ratio, and that ratio is precisely the seam-normalizer width divided by the corridor width.

## 2. The mode count keeps the full inverse-seam population

The elementary function

\[
f(z)=\frac{z}{\sinh z}
\tag{24}
\]

is at most one and decays exponentially for large `z`. More concretely, for `z\ge1`,

\[
f(z)\le C e^{-z/2}.
\tag{25}
\]

Hence if `0<\lambda<C\rho`, equation (10) implies

\[
x_k>\lambda
\quad\Longrightarrow\quad
z_k
\le C\left(1+\log\frac{C\rho}{\lambda}\right).
\tag{26}
\]

Since

\[
z_k
=s\sqrt{1+(2\pi k/\mathcal L)^2}
\ge c\frac{s|k|}{\mathcal L},
\tag{27}
\]

we obtain

\[
\boxed{
N_{X^{\rm cyl}}(\lambda)
\le
C\frac{\mathcal L}{s}
\left(1+\log_+\frac{C\rho}{\lambda}\right).
}
\tag{28}
\]

The harmless additive constant in the number of Fourier modes is absorbed after the finite head. Equation (11) shows that, under the stated comparability assumptions, the scale `\mathcal L/s` is not an artifact of the upper bound: a fixed `z=O(1)` band genuinely contains that many order-`\rho` channels in the periodized reference.

For the PF-226 fixed-window witness rather than a full periodization, replace `\mathcal L` by a fixed tangential length. Then (28) has only order `s^{-1}` channels. PF-228 deliberately proves the weak endpoint for the larger periodized population, so the exact PF-226 witness multiplicity is cheaper than the counting model used below.

## 3. Reciprocal-prime weighting moves the block top scale to `P_n^{-2}`

Apply (28) to the weighted block `\delta_nX_n^{\rm cyl}`. If this block has a singular value above `\sigma`, then necessarily

\[
\sigma<C\delta_n\rho_n=C a_n.
\tag{29}
\]

By (16), every contributing edge satisfies

\[
P_n\le C\sigma^{-1/2}.
\tag{30}
\]

Moreover (13)--(14) and the elementary lower bound `G_n\ge4` give

\[
\frac{\mathcal L_n}{s_n}
\le
C\frac{P_n(1+\log P_n)}{G_n}
\le C P_n(1+\log P_n).
\tag{31}
\]

Therefore

\[
N_{\delta_nX_n^{\rm cyl}}(\sigma)
\le
CP_n(1+\log P_n)
\left(
1+\log_+\frac{Ca_n}{\sigma}
\right)
\mathbf 1_{\{P_n\le C\sigma^{-1/2}\}}.
\tag{32}
\]

Using again `a_n\le C/P_n^2`, the logarithm may be bounded by

\[
1+\log_+\frac{C}{\sigma P_n^2}.
\tag{33}
\]

This is the key distinction from PF-226's raw saturated-mass diagnostic. The multiplicity may grow essentially linearly in `P_n`, but the **largest weighted dressed singular value is already quadratic-decay scale** `P_n^{-2}`.

## 4. Prime threshold counting closes the reference model at weak `S_1`

Because the model edge blocks in (17) have mutually orthogonal sources and targets,

\[
N_{T_{\rm cyl}}(\sigma)
=
\sum_n N_{\delta_nX_n^{\rm cyl}}(\sigma).
\tag{34}
\]

Put

\[
X=C_0\sigma^{-1/2}
\tag{35}
\]

with `C_0` large enough to absorb (30). Equations (32)--(33) give

\[
N_{T_{\rm cyl}}(\sigma)
\le
C\sum_{p\le X}
p\log p
\left(1+\log\frac{CX}{p}\right)
\tag{36}
\]

after harmless finite-head and constant adjustments.

PF-210 already proves the elementary Chebyshev estimate

\[
\vartheta(Y):=\sum_{p\le Y}\log p\le CY.
\tag{37}
\]

In particular

\[
\sum_{p\le Y}p\log p
\le Y\vartheta(Y)
\le CY^2.
\tag{38}
\]

Split the primes in (36) into dyadic shells

\[
\frac{X}{2^{m+1}}<p\le\frac{X}{2^m}.
\tag{39}
\]

On the `m`th shell the logarithmic factor is `O(1+m)`, while (38) bounds the weighted prime sum by `CX^2/4^m`. Therefore

\[
\begin{aligned}
N_{T_{\rm cyl}}(\sigma)
&\le
CX^2\sum_{m\ge0}\frac{1+m}{4^m}\\
&\le CX^2\\
&\le \frac C\sigma.
\end{aligned}
\tag{40}
\]

Thus

\[
\boxed{
\sup_{\sigma>0}\sigma N_{T_{\rm cyl}}(\sigma)<\infty,
\qquad
T_{\rm cyl}\in\mathcal S_{1,\infty}.
}
\tag{41}
\]

Compactness follows independently: each Fourier block is compact by (10), and the weighted block norms satisfy

\[
\|\delta_nX_n^{\rm cyl}\|
\le a_n\le\frac C{P_n^2}\longrightarrow0.
\tag{42}
\]

No prime number theorem, average-gap asymptotic, or statistical hypothesis on consecutive gap ratios is needed.

## 5. Why this does not prove the actual PF cut flux estimate

The reference calculation is intentionally stronger than a heuristic but weaker than the desired geometric theorem.

First, the straight cylinder has exact tangential translation symmetry. The actual one-cusp pant has a varying Fermi thickness of order `s_n\cosh t` on the PF-226 corridor, and its global boundary identification is not Fourier diagonal. Equation (8) therefore cannot be transplanted mode by mode to the pant.

Second, `D_k` in (5) is the inverse of a **two-interface local reference precision**. The actual

\[
D=(I+K)^{-1}
\tag{43}
\]

is the global simultaneous Schur factor. PF-217 already shows that shorting through tangential boundary freedom can invalidate naive lower-energy deductions. PF-228 does not assume that global shorting preserves the local cylinder amplitude gain.

Third, the model uses the symmetric seam-normalizer branch because that is the low-cost branch underlying the PF-226 witness construction. It is not an upper bound for the complete two-boundary PF module operator. The theorem says that the **specific inverse-seam multiplicity exhibited by PF-226/PF-227 is compatible with weak trace after natural local inverse dressing**; it does not classify every boundary channel of the actual pant.

Finally, orthogonality in (17) is a control-model reassembly. The true PF-222 flux series uses nested prefix cuts and overlapping global resolvent factors. Equation (41) cannot be substituted for a proof that

\[
P[D,\Omega]H\in\mathcal S_{1,\infty}.
\tag{44}
\]

The actual theorem still has to control placement/reassembly.

## 6. Prior art and novelty audit

No novelty is claimed for the ingredients of the local calculation. Separation of variables on a flat strip gives the `\coth/\operatorname{csch}` two-boundary DtN matrix, and the symmetric centered-strip eigenvalue `\mu\tanh(\mu w)` is elementary. Block inversion and singular-value counting are standard.

The closest fixed-geometry DtN literature remains consistent with this calculation rather than supplying it as a black box. Hislop and Lutzer, *Spectral Asymptotics of the Dirichlet-To-Neumann Map on Multiply Connected Domains in R^d*, **Inverse Problems 17** (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`, isolate smoothing off-diagonal coupling between distinct boundary components on a fixed smooth domain. Girouard, Karpukhin, Levitin and Polterovich, *The Dirichlet-to-Neumann map, the boundary Laplacian, and Hörmander's rediscovered manuscript*, **Journal of Spectral Theory 12** (2022), 195--225, DOI `10.4171/JST/399`, place high-frequency DtN behavior relative to the boundary Laplacian. Neither result tracks the PF degenerating width ratio through the normalized inverse `(I+K)^{-1}`.

For thin-domain comparison, Bucur, Henrot and Michetti, *Asymptotic behaviour of the Steklov spectrum on dumbbell domains*, **Communications in Partial Differential Equations 46** (2021), 362--393, DOI `10.1080/03605302.2020.1840587`, shows that thin Steklov problems can develop lower-dimensional limiting scales. Their setting and spectral problem do not identify the PF symmetric seam-energy normalization, reciprocal-prime cut weights, or the weak-Schatten reassembly in (41).

A fresh structure-directed search for thin-strip/cylinder DtN transmission, off-diagonal DtN decay, and weak-Schatten reassembly did not locate a theorem whose hypotheses and conclusion contain the project-specific statement (41). The durable content claimed here is therefore narrow: **for the explicit PF-scaled straight-corridor control, local resolvent dressing converts the inverse-seam population from order-one raw amplitude to order `w/s`, and the resulting reciprocal-prime weighted block family is weak trace class by exact threshold counting.** No new general DtN theorem is claimed.

## 7. Falsification and boundary checks

1. Equation (8) is a statement about the exact flat control and the symmetric seam-normalizer branch. It must not be relabeled as the actual pant formula.
2. The `+1` shift is retained in `\mu=\sqrt{1+\xi^2}`. Dropping it changes the zero-mode algebra, although not the high-frequency scale.
3. The top weighted scale `P_n^{-2}` comes from **both** the reciprocal-prime jump and the local inverse ratio `w_n/s_n`. PF-225's universal `1/2` cap alone gives no such scale.
4. Equation (28) counts modes after fixing the singular threshold. Summing per-edge trace envelopes first discards the mechanism that proves (41).
5. The periodized `O(\mathcal L_n/s_n)` population is deliberately larger than PF-226's proved fixed-window `O(s_n^{-1})` witness family. This makes (41) a robust control calculation, not evidence that the actual pant has exactly that many channels.
6. No average prime-gap law is used. The only arithmetic inputs are the exact jump `\delta_n`, canonical scale bounds already persisted in the line, the trivial `g_n\le G_n`, and PF-210's Chebyshev estimate.
7. Strong trace class is not asserted for `T_{\rm cyl}`. The weak endpoint is obtained distributionally and may be strictly weaker.
8. No lower bound for the actual dressed flux follows from the raw PF-226/PF-227 channel count. Global Schur shorting can alter both singular vectors and amplitudes.
9. Nothing here proves the complete first relative resolvent is weak trace class, closes PF-183's short-collar splice or PF-204's unsmoothed route, proves wave-operator completeness, controls determinants/resonances, separates the prime flute from its shift clone, or implies RH.

## Consequences for the research line

PF-224 shows that reciprocal-prime weighting cannot pay for raw pant hopping. PF-225 shows that inversion saturates raw amplitude but leaves multiplicity open. PF-226/PF-227 then prove that the actual raw geometry supplies an inverse-seam population and that fixed high-pass truncation does not remove it. PF-228 now supplies the missing matched-control calibration: **inverse-seam multiplicity of that size is compatible with the desired weak endpoint once dressing pays the geometrically natural `w/s` factor.**

The next smooth-route theorem should therefore target a quantitative dressed estimate rather than another raw channel count. A natural sufficient shape is a bound of the form

\[
s_k\bigl(P[D,E_n]H\bigr)
\lesssim
\frac{w_n^{1/2}w_{n+1}^{1/2}}{s_n}
\,\Phi\!\left(\frac{s_n k}{\mathcal L_n}\right)
\tag{45}
\]

with an integrable/exponentially decaying profile `\Phi`, or any invariant substitute whose threshold count reproduces the prime-square block scale in (16). The exact profile in (45) is **not** established for the pant; it records the scale exposed by the control.

A negative continuation is equally precise. It must identify why the actual global shorted inverse fails to inherit the local `w/s` gain, or why nested-cut reassembly recreates enough coherent multiplicity to defeat the threshold count despite that gain. PF-226's raw `s_n^{-1}` population and PF-227's high--high persistence alone no longer distinguish those two outcomes.