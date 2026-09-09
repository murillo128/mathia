# ANF-137 — slack-spend ratios control historical zero pinching

**Status:** `EXACT-DERIVED + DEPTH-QUANTITATIVE-INVARIANT + POSITIVE-TRANSLATION-CASCADE + HISTORICAL-ZERO-SEPARATION + SLACK-SPEND-RATIO + LOCAL-CONDITIONING-BOUND + RESIDUAL-VANISHING-SPEND-GATE`. `ANF-136` isolates the remaining diagonal source-prefactor obstruction: a very low-density historical annihilator could, in principle, place a zero extremely close to a later source-carrying critical point even though chamber count, total copy rate, and floor error remain controlled. The pressure budget gives an exact quantitative restriction on that mechanism.

Write the stage-`d` limiting pressure as in `ANF-135`--`ANF-136`,

\[
G_d(\alpha)
=B_q(\alpha)
+2\sum_{k=1}^{d}\theta_k\log|Q_{k-1}(\alpha)|,
\qquad \sup G_d=0,
\tag{1}
\]

where

\[
Q_{k-1}(\alpha)
=\prod_{j=1}^{J_{k-1}}
\left(1+e^{-2\pi i\tau_{j,k-1}\alpha}\right),
\qquad
\tau_{j,k-1}=\frac1{2\xi_{j,k-1}},
\tag{2}
\]

and the copy-rate slack obeys

\[
\delta_k
=\delta_{k-1}-2\theta_kJ_{k-1}\log2.
\tag{3}
\]

Define the slack spent by layer `k` and the slack spent after it by

\[
s_k:=\delta_{k-1}-\delta_k
=2\theta_kJ_{k-1}\log2>0,
\qquad
T_{k,d}:=\delta_k-\delta_d
=\sum_{\ell=k+1}^{d}s_\ell,
\tag{4}
\]

and put

\[
\chi_{k,d}:=\frac{T_{k,d}}{s_k},
\qquad
\Omega_d
:=\max_{1\le k\le d}
J_{k-1}\bigl(1+\chi_{k,d}\bigr).
\tag{5}
\]

Then every current critical point `xi in K_d` satisfies, for every historical layer `k<=d`,

\[
\boxed{
|Q_{k-1}(\xi)|
\ge
\exp\!\left[-\frac{T_{k,d}}{2\theta_k}\right]
=2^{-J_{k-1}\chi_{k,d}}.
}
\tag{6}
\]

Consequently every individual binomial in that layer obeys

\[
\boxed{
\left|1+e^{-2\pi i\tau_{j,k-1}\xi}\right|
\ge
2^{1-J_{k-1}}
\exp\!\left[-\frac{T_{k,d}}{2\theta_k}\right]
=2\,2^{-J_{k-1}(1+\chi_{k,d})}.
}
\tag{7}
\]

Using the `ANF-134` lower bound `xi_{j,k-1}>=delta_{k-1}`, this becomes a direct zero-separation estimate:

\[
\boxed{
\operatorname{dist}\!\left(
\xi,
Z\!\left(1+e^{-2\pi i\tau_{j,k-1}\alpha}\right)
\right)
\ge
\frac{2\delta_{k-1}}{\pi}
2^{-J_{k-1}(1+\chi_{k,d})}.
}
\tag{8}
\]

The same budget controls local curvature. The entire stage-`k` binomial layer contributes at `xi`

\[
\boxed{
0\le
-2\theta_k\frac{d^2}{d\alpha^2}
\log|Q_{k-1}(\xi)|
\le
\frac{\pi^2s_k}{4\log2\,\delta_{k-1}^2}
4^{J_{k-1}(1+\chi_{k,d})}.
}
\tag{9}
\]

Hence, after summing all historical layers and using `sum_k s_k<=delta_0`, every current critical point satisfies

\[
\boxed{
-G_d''(\xi)
\le
C_q\left(1+\delta_d^{-2}4^{\Omega_d}\right).
}
\tag{10}
\]

The fixed seed digit factor is not an omitted singularity: at every current critical point its modulus is bounded below by a positive constant depending only on the fixed seed. Thus **historical zero pinching is governed by a single new quantity, the future-to-own slack-spend ratio**. The fresh layer itself is always safe: when `k=d`, `T_{d,d}=0`, and in fact every new critical point satisfies the strict inequality `|Q_{d-1}(xi)|>1`.

Under the quantitative depth window of `ANF-136`,

\[
D(A)^2\log(D(A)+2)=o(\log A),
\tag{11}
\]

one already has `delta_{D(A)}=A^{-o(1)}` and `J_k=A^{o(1)}`. Therefore an additional condition

\[
\boxed{
\Omega_{D(A)}=o(A)
}
\tag{12}
\]

forces every current critical cell to stay `exp[-o(A)]` away from every historical zero and bounds its limiting-pressure Hessian by `exp[o(A)]`. In particular, this excludes a **fixed positive exponential source loss caused purely by local cell pinching**. Conversely, if such exponential pinching is to survive inside the controlled depth window, then some historical layer must have

\[
\frac{T_{k,D(A)}}{s_k}
\ge A^{1-o(1)},
\tag{13}
\]

because `J_{k-1}=A^{o(1)}`. Equivalently, the dangerous layer must spend an almost finite-`A`-quantum fraction of slack compared with the amount spent after it. This sharpens the qualitative residual mechanism in `ANF-136`: arbitrary historical zeros are not dangerous; only **vanishing-spend layers followed by much larger cumulative retuning** can become exponentially ill-conditioned.

## 1. Later retuning can compensate only its remaining slack budget

Fix `d>=1`, a current critical point

\[
\xi\in K_d,
\qquad
G_d(\xi)=0,
\tag{14}
\]

and a historical layer `1<=k<=d`. Split the current pressure at that layer:

\[
G_d(\xi)
=G_k(\xi)
+2\sum_{\ell=k+1}^{d}
\theta_\ell\log|Q_{\ell-1}(\xi)|.
\tag{15}
\]

Every later annihilator has coefficient mass `2^{J_{\ell-1}}`, hence pointwise

\[
\log|Q_{\ell-1}(\alpha)|
\le J_{\ell-1}\log2.
\tag{16}
\]

The maximum total pressure that all later layers can add is therefore exactly bounded by their total slack spend:

\[
2\sum_{\ell=k+1}^{d}
\theta_\ell\log|Q_{\ell-1}(\xi)|
\le
\sum_{\ell=k+1}^{d}s_\ell
=T_{k,d}.
\tag{17}
\]

Since the left side of (15) is zero,

\[
G_k(\xi)\ge-T_{k,d}.
\tag{18}
\]

But

\[
G_k(\xi)
=G_{k-1}(\xi)
+2\theta_k\log|Q_{k-1}(\xi)|,
\tag{19}
\]

and source criticality at stage `k-1` gives

\[
G_{k-1}(\xi)\le0.
\tag{20}
\]

Thus

\[
2\theta_k\log|Q_{k-1}(\xi)|
=G_k(\xi)-G_{k-1}(\xi)
\ge G_k(\xi)
\ge-T_{k,d},
\tag{21}
\]

which proves (6). Substituting

\[
\frac{T_{k,d}}{2\theta_k}
=J_{k-1}\log2\,rac{T_{k,d}}{s_k}
=J_{k-1}\log2\,\chi_{k,d}
\tag{22}
\]

gives the second form in (6).

This is an exact budget statement. It does not use a Taylor expansion, a chamber-count estimate, or any assumption that the historical density is bounded below. A zero can become extremely close to a later critical point only when its own layer is cheap enough that the remaining retuning budget can pay the logarithmic penalty.

## 2. Product control forces every binomial away from zero

Write

\[
B_{j,k-1}(\alpha)
:=1+e^{-2\pi i\tau_{j,k-1}\alpha}.
\tag{23}
\]

Every factor satisfies

\[
|B_{j,k-1}(\alpha)|\le2.
\tag{24}
\]

Since

\[
|Q_{k-1}(\xi)|
=\prod_{j=1}^{J_{k-1}}|B_{j,k-1}(\xi)|,
\tag{25}
\]

(6) and (24) imply for each individual factor

\[
|B_{j,k-1}(\xi)|
\ge
2^{1-J_{k-1}}|Q_{k-1}(\xi)|,
\tag{26}
\]

which is exactly (7).

The real zeros of `B_{j,k-1}` are the points `z` satisfying

\[
\tau_{j,k-1}z\in\mathbb Z+\frac12.
\tag{27}
\]

For the nearest such zero, let

\[
r:=\operatorname{dist}(\xi,Z(B_{j,k-1})).
\]

Then `0<=pi tau r<=pi/2` and

\[
|B_{j,k-1}(\xi)|
=2\sin(\pi\tau_{j,k-1}r)
\le2\pi\tau_{j,k-1}r.
\tag{28}
\]

Hence

\[
r
\ge
\frac{|B_{j,k-1}(\xi)|}{2\pi\tau_{j,k-1}}
=\frac{\xi_{j,k-1}}\pi
|B_{j,k-1}(\xi)|.
\tag{29}
\]

`ANF-134` gives

\[
\xi_{j,k-1}\ge\delta_{k-1}.
\tag{30}
\]

Combining (7), (29), and (30) yields (8).

For the **fresh** layer, `k=d`, there is no later budget and (21) gives `|Q_{d-1}(xi)|>=1`. Equality cannot occur. If it did, (19) and `G_d(xi)=0` would force `G_{d-1}(xi)=0`, so `xi` would belong to the complete stage-`d-1` critical skeleton. But `Q_{d-1}` vanishes at every point of that skeleton, contradicting `|Q_{d-1}(xi)|=1`. Therefore

\[
\boxed{|Q_{d-1}(\xi)|>1.}
\tag{31}
\]

A newly created first-critical chamber can never be arbitrarily close to a zero of the annihilator that created it. Any severe pinching must have **historical lag**.

## 3. The same ratio bounds the weighted logarithmic curvature

On a zero-free cell,

\[
\frac{d^2}{d\alpha^2}
\log|B_{j,k-1}(\alpha)|
=-\pi^2\tau_{j,k-1}^2
\sec^2(\pi\tau_{j,k-1}\alpha).
\tag{32}
\]

Also

\[
|B_{j,k-1}(\xi)|
=2|\cos(\pi\tau_{j,k-1}\xi)|,
\]

so

\[
\sec^2(\pi\tau_{j,k-1}\xi)
=\frac4{|B_{j,k-1}(\xi)|^2}.
\tag{33}
\]

Using (7),

\[
\sec^2(\pi\tau_{j,k-1}\xi)
\le
4^{J_{k-1}(1+\chi_{k,d})}.
\tag{34}
\]

Meanwhile (30) gives

\[
\tau_{j,k-1}
=\frac1{2\xi_{j,k-1}}
\le\frac1{2\delta_{k-1}}.
\tag{35}
\]

Therefore

\[
\begin{aligned}
-2\theta_k(\log|Q_{k-1}|)''(\xi)
&=2\theta_k\pi^2
\sum_{j=1}^{J_{k-1}}
\tau_{j,k-1}^2
\sec^2(\pi\tau_{j,k-1}\xi)\\
&\le
\frac{\pi^2\theta_kJ_{k-1}}
{2\delta_{k-1}^2}
4^{J_{k-1}(1+\chi_{k,d})}\\
&=
\frac{\pi^2s_k}
{4\log2\,\delta_{k-1}^2}
4^{J_{k-1}(1+\chi_{k,d})},
\end{aligned}
\tag{36}
\]

which proves (9).

Summing (36), using `delta_{k-1}>=delta_d`, the definition of `Omega_d`, and

\[
\sum_{k=1}^{d}s_k
=\delta_0-\delta_d
\le\delta_0,
\tag{37}
\]

gives the historical-binomial part of (10) without an extra factor of `d`.

The base profile cannot create a new singularity at a current critical point. `ANF-134` gives

\[
0=G_d(\xi)\le F_\gamma(\xi)-\delta_d,
\]

hence

\[
F_\gamma(\xi)\ge\delta_d>0.
\tag{38}
\]

Since `F_gamma(alpha)->-infinity` as `alpha->1`, all such points remain in a fixed compact subset of `[0,1)`, and `F_gamma''` is uniformly bounded there.

The fixed digit factor is also uniformly separated from its zeros. Split

\[
G_d(\xi)
=B_q(\xi)
+2\sum_{k=1}^{d}\theta_k\log|Q_{k-1}(\xi)|.
\tag{39}
\]

The same coefficient-mass ceiling gives

\[
B_q(\xi)
\ge-(\delta_0-\delta_d).
\tag{40}
\]

Because

\[
B_q(\alpha)
=F_\gamma(\alpha)-f_\gamma
+2r_q\log|D_q(d_q\alpha)|
\]

and `F_gamma-f_gamma<=0`,

\[
\boxed{
|D_q(d_q\xi)|
\ge
\exp\!\left[-\frac{\delta_0-\delta_d}{2r_q}\right]
\ge
\exp\!\left[-\frac{\delta_0}{2r_q}\right]
=:c_q>0.
}
\tag{41}
\]

The seed has fixed `q`, so (41) gives a fixed positive distance from every digit zero and a fixed curvature bound there. Combining these seed bounds with (36)--(37) proves (10).

## 4. A quantitative critical-cell radius

Let `I_d(xi)` be the zero-free cell of the complete stage-`d` limiting pressure containing a current critical point `xi`. The digit zeros are a fixed positive distance away by (41). Every binomial zero is controlled by (8). Since `delta_{k-1}>=delta_d` and every exponent in (8) is at most `Omega_d`, there is a fixed seed-dependent constant `c_q>0` such that

\[
\boxed{
\operatorname{dist}(\xi,\partial I_d(\xi))
\ge
c_q\,\delta_d\,2^{-\Omega_d}.
}
\tag{42}
\]

On the concentric half-cell, every historical binomial remains at least half as far from its nearest zero. The exact log-cos curvature formula then changes the bound (36) only by an absolute constant. Consequently the local curvature throughout that half-cell is bounded by

\[
\boxed{
\sup_{\alpha\in I_d^{1/2}(\xi)}
|G_d''(\alpha)|
\le
C_q\left(1+\delta_d^{-2}4^{\Omega_d}\right).
}
\tag{43}
\]

This is the local-conditioning estimate missing from the purely combinatorial argument of `ANF-136`, expressed in the one quantity that the previous slack recursions did not control.

For a diagonal depth `d=D(A)` satisfying (11), `ANF-135` gives

\[
\delta_d=A^{-o(1)}.
\tag{44}
\]

If also (12) holds, then (42)--(43) become

\[
\operatorname{dist}(\xi,\partial I_d(\xi))
=e^{-o(A)},
\qquad
\sup_{I_d^{1/2}(\xi)}|G_d''|
=e^{o(A)}.
\tag{45}
\]

Thus one may choose a neighborhood of the critical point with width

\[
w_A
\ge A^{-1/2}e^{-o(A)}
\tag{46}
\]

on which `A G_d` falls by only `O(1)`. At the limiting-pressure level the corresponding Laplace contribution loses at worst an `e^{-o(A)}` prefactor relative to a standard `A^{-1/2}` critical chamber. Together with the pointwise floor lower bound in `ANF-136`, this rules out a **fixed-rate loss `e^{-cA}` generated solely by zero-cell narrowing** whenever (12) holds.

This is intentionally weaker than

\[
E_0(X_A^{(D(A))})\asymp E_A.
\tag{47}
\]

A subexponential prefactor can still tend to zero, and (43) does not make the Hessian depth-uniformly `O(1)`. The result closes the possibility of an exponential local collapse under (12); it does not yet supply the bounded source constant required for a full arbitrary-depth cascade theorem.

## 5. What a genuine exponential pinch must look like

The depth window (11) gives from `ANF-136`

\[
J_k=A^{o(1)}
\qquad(k\le D(A)).
\tag{48}
\]

Suppose nevertheless that (12) fails at fixed positive exponential scale, so along a subsequence

\[
\Omega_{D(A)}\ge cA
\tag{49}
\]

for some `c>0`. Then for some layer `k<=D(A)`,

\[
J_{k-1}\left(1+\frac{T_{k,D(A)}}{s_k}\right)
\ge cA.
\tag{50}
\]

Because `J_{k-1}=A^{o(1)}`, the `1` is negligible and

\[
\boxed{
\frac{T_{k,D(A)}}{s_k}
\ge A^{1-o(1)}.
}
\tag{51}
\]

Equivalently,

\[
\boxed{
s_k
\le T_{k,D(A)}A^{-1+o(1)}
\le\delta_0A^{-1+o(1)}.}
\tag{52}
\]

So an exponentially ill-conditioned historical zero cannot come from a layer that spent an ordinary fraction of the remaining copy-rate budget. It must come from a layer whose own slack decrement is essentially at, or below, the finite-`A` `1/A` scale up to subpolynomial factors, followed by substantially more retuning.

This is exactly the regime in which ideal limiting densities and physical repetition counts begin to interact most delicately. A layer with

\[
\theta_k
=\frac{s_k}{2J_{k-1}\log2}
\]

may have only subpolynomially many physical repetitions `floor(theta_k A)` even though its logarithmic zero can still be felt by a later ideal maximizer. The next gate is therefore no longer an unrestricted historical-zero problem. It is a **vanishing-spend/finite-quantization problem**: determine whether first-critical retuning can actually create the ratio (51), and if it can, whether flooring such a layer destroys, preserves, or regularizes the putative exponential pinch.

## 6. Adversarial controls and exact scope

Several tempting stronger conclusions are false or not proved here.

First, the coefficient-mass bound cannot give a depth-uniform positive separation from every historical zero without controlling `chi_{k,d}`. If `s_k` is arbitrarily small while `T_{k,d}` stays macroscopic, (6)--(8) legitimately allow exponentially or superexponentially small distances. The result therefore does not erase the obstruction identified by `ANF-136`; it identifies exactly what budget geometry is required for that obstruction to occur.

Second, the fresh-layer estimate does not propagate automatically to later generations. Equation (31) says a chamber regenerated at stage `k` is separated from the zeros introduced at that same stage. Future retuning can move later critical points back toward those zeros, and the amount of allowed movement is measured precisely by `T_{k,d}/s_k`.

Third, (10) is a weighted curvature bound for the limiting pressure. It is not an unweighted trigonometric-polynomial degree estimate, and no claim is made that every positive trigonometric product with the same number of factors obeys it. The affine slack identity (3) and the stagewise source-critical inequalities are load-bearing.

Fourth, (45)--(46) protect only exponential scale. They are compatible with Hessians and inverse cell widths tending to infinity subexponentially, so they do not prove the bounded source ratio (47). A proof of (47) still needs stronger control, compensation among many chambers, or a direct finite-`A` source argument.

Finally, no genericity or noncoincidence of historical zeros is required. Several binomials may share a zero. Equations (6)--(9) work factor by factor because each individual modulus is at most `2`; coincident zeros only make `Q` smaller and therefore make the pressure-budget restriction stronger.

## 7. Prior-art boundary

The local analytic ingredients are classical: finite Riesz products and positive trigonometric products organize products of cosine-type factors; the identity

\[
(\log|\cos x|)''=-\sec^2x
\]

is elementary; and converting a local Hessian bound into a Laplace-width estimate is standard one-dimensional steepest-descent/Laplace analysis. A directed audit against classical Riesz-product constructions (including the standard Bary/Zygmund framework summarized in the *Encyclopedia of Mathematics* entry on Riesz products), extremal nonnegative trigonometric polynomials, zero-count arguments, and Laplace asymptotics did not identify a theorem matching (6)--(10).

The additional structure here is not a new theorem about arbitrary trigonometric polynomials. It is the exact conversion of the Mathia cascade's **affine copy-rate slack accounting** into a historical zero-separation and curvature law, with the future-to-own spend ratio `chi_{k,d}` as the conditioning parameter. No external theorem is load-bearing for the proof, so `SOURCES.md` is unchanged.

## 8. Consequence for the analytic-frontier program

`ANF-134` showed that total slack protects the notch and translation span. `ANF-135` bounded how fast that slack can collapse. `ANF-136` showed that the number of cells and floor-rate error remain subexponential at useful diagonal depths. The remaining local obstruction can now be stated much more narrowly:

\[
\boxed{
\text{exponential historical pinching}
\Longrightarrow
\text{a layer with }T_{k,d}/s_k\ge A^{1-o(1)}.
}
\tag{53}
\]

Therefore the next decisive test should target the **retuning spend sequence itself**, not generic cell geometry: either prove that first-critical retuning prevents ratios of the form (51), which would eliminate fixed-rate local collapse, or construct a genuine cascade in which an almost-quantized low-spend layer is later driven exponentially close to one of its zeros. The finite-`A` flooring behavior of precisely that regime is now the natural place to look for the remaining obstruction or the missing compactness mechanism.
