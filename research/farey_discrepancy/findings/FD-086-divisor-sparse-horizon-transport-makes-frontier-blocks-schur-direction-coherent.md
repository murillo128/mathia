# FD-086 — divisor-sparse horizon transport makes frontier blocks Schur-direction coherent

**Status:** `EXACT-DERIVED + DIVISOR-SPARSE-HORIZON-TRANSPORT + JORDAN-VECTOR-COHERENCE + SCHUR-PROJECTIVE-COHERENCE + FRONTIER-ENERGY-BLOCKS + ADDITIVE-TRANSPORT`.

`FD-084` proves that every sufficiently late fixed-power future window contains a consecutive block of horizons of length `H^(Theta-delta)` on which the physical nonsquarefree occupation stays bounded below. `FD-085` then shows that the **set geometry** of those blocks cannot by itself produce the finite-entropy multiplicative chain required by the existing GCD-duality accumulation mechanism: even linear occupied blocks in every power window can be arranged so that all infinite integer-ratio chains have diverging transition ratios.

The physical Farey/Mertens object carries substantially more information than the occupied set. If one keeps the complete Jordan-coordinate vector instead of only its two scalar energies, moving the horizon from `M` to `M+h` changes a row `r` only when the interval `(M,M+h]` crosses a multiple of `r`. The exact quotient-shell source has increments of absolute value at most one, so this divisor incidence controls the full Hilbert displacement. The result is the additive transport inequality

\[
\boxed{
\|V_{M+h,D}-V_{M,D}\|_2^2
\ll_\gamma
h^2+h(M+h)^\gamma
\qquad(\gamma>0),
}
\tag{1}
\]

for a canonical zero-extended Jordan vector `V_(H,D)` whose squared norm is exactly the physical Schur energy `E_(H,D)`.

When (1) is applied to the near-frontier-energy seeds already extracted in `FD-084`, the whole occupied block lies in a **vanishing angular cap** in Jordan space. More precisely, if `H` is the seed used there and

\[
L_H:=\lfloor H^{\Theta-\delta}\rfloor,
\qquad 0<\delta<\Theta,
\tag{2}
\]

then uniformly for `0<=h<=L_H`,

\[
\boxed{
\frac{\|V_{H+h,D}-V_{H,D}\|_2^2}{E_{H,D}}
\ll
H^{-3\delta/2}+H^{-\Theta-\delta/4}
=o(1).
}
\tag{3}
\]

Consequently the normalized physical Jordan vectors, the normalized Schur equality direction, and the normalized transverse Schur defect all vary by `o(1)` across the entire block. This is a source-structural transport statement absent from the matched set control in `FD-085`: the good horizons are not merely consecutive; on each frontier-length block they carry asymptotically the **same full signed Jordan configuration**.

It still does not connect different blocks. A superexponentially placed sequence of coherent blocks is not excluded, and no new RH estimate follows. The live compatibility problem is therefore sharpened from finding multiplicative structure in the occupied set to transporting these coherent Jordan/Schur directions **between** separated blocks, or finding a multihorizon functional that can compose the already-coherent additive blocks directly.

## 1. The complete Jordan vector has an exact divisor-supported horizon increment

Retain the physical quotient-shell source from `FD-033` and `FD-046`,

\[
\mathcal H(k)
=\sum_{n\le k}c(n),
\qquad
c(n)=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\qquad
|c(n)|\le1,
\tag{4}
\]

with `mathcal H(0)=0`. Fix a Schur head `D>=1` and put

\[
w(r):=\frac{J_2(r)}{r^2}.
\tag{5}
\]

Embed every finite physical Jordan tail into the common Hilbert space

\[
\ell^2(\{r>D\})
\]

by zero extension and define

\[
\boxed{
V_{H,D}(r)
:=
\sqrt{w(r)}\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)
\qquad(r>D).
}
\tag{6}
\]

For `r>H` the floor is zero, so the coordinate vanishes automatically. By definition,

\[
\boxed{
\|V_{H,D}\|_2^2=E_{H,D}.
}
\tag{7}
\]

Likewise, if `P_ns` denotes the fixed coordinate projection onto nonsquarefree rows,

\[
\boxed{
\|P_{\rm ns}V_{H,D}\|_2^2=U_{H,D}.
}
\tag{8}
\]

Now let `N=M+h` with `h>=1` and define

\[
d_r
:=
\left\lfloor\frac Nr\right\rfloor
-
\left\lfloor\frac Mr\right\rfloor.
\tag{9}
\]

This integer has the exact divisibility interpretation

\[
\boxed{
d_r=\#\{n:M<n\le N,\ r\mid n\}.}
\tag{10}
\]

In particular, if `d_r=0` then the `r`th Jordan coordinate is literally unchanged. More generally, (4) gives

\[
\left|
\mathcal H\!\left(\left\lfloor\frac Nr\right\rfloor\right)
-
\mathcal H\!\left(\left\lfloor\frac Mr\right\rfloor\right)
\right|
\le d_r.
\tag{11}
\]

Since `0<w(r)<=1`, equations (6) and (11) imply the exact Hilbert majorization

\[
\boxed{
\|V_{N,D}-V_{M,D}\|_2^2
\le
\sum_{r>D}d_r^2.
}
\tag{12}
\]

The support statement is also exact up to possible source cancellation:

\[
\boxed{
\operatorname{supp}(V_{N,D}-V_{M,D})
\subseteq
\bigcup_{M<n\le N}\{r>D:r\mid n\}.
}
\tag{13}
\]

Thus additive horizon motion is not a generic perturbation of all Jordan rows. It is carried by the divisor incidence of the physical integers crossed by the horizon.

## 2. The divisor incidence has quadratic displacement cost

Split the sum in (12) at `r=h`. For `r<=h`,

\[
d_r
\le
\frac hr+1
\le
\frac{2h}{r},
\tag{14}
\]

so

\[
\sum_{r\le h}d_r^2
\le
4h^2\sum_{r\ge1}\frac1{r^2}
\ll h^2.
\tag{15}
\]

For `r>h`, the interval `(M,M+h]` contains at most one multiple of `r`, hence

\[
d_r\in\{0,1\}.
\tag{16}
\]

Using (10),

\[
\sum_{r>h}d_r^2
=
\sum_{r>h}d_r
\le
\sum_{M<n\le N}\tau(n).
\tag{17}
\]

The standard divisor bound `tau(n)<<_gamma n^gamma`, valid for every fixed `gamma>0` and already used in `FD-084`, gives

\[
\sum_{M<n\le N}\tau(n)
\ll_\gamma hN^\gamma.
\tag{18}
\]

Combining (12), (15), and (18) proves (1):

\[
\boxed{
\|V_{M+h,D}-V_{M,D}\|_2^2
\ll_\gamma
h^2+h(M+h)^\gamma.
}
\tag{19}
\]

The estimate is uniform in the common fixed head `D`; deleting the first `D` coordinates only decreases the left side. It uses no cancellation theorem for the Mertens function. The load-bearing physical input is the exact quotient-shell sampling together with the bounded coefficient law `|c(n)|<=1`.

Equation (19) is stronger than the scalar increment estimate used in `FD-084`. There only `E_(H,D)` and `U_(H,D)` were transported. Here the complete signed Jordan vector is transported, so every fixed row filter, correlation, and Schur projection can be compared across nearby horizons before any scalarization.

## 3. Near-frontier-energy blocks collapse to one asymptotic Jordan direction

`FD-084` extracts, inside the relevant good annulus, a seed `H` satisfying

\[
\nu_{H,D}>\eta_1,
\qquad
E_{H,D}>H^{2\Theta-\delta/2},
\tag{20}
\]

and then proves that the entire interval

\[
[H,H+L_H],
\qquad
L_H=\lfloor H^{\Theta-\delta}\rfloor,
\tag{21}
\]

remains occupied at the weaker fixed threshold `eta<eta_1`. Since `Theta<=1` and `delta>0`, one has `L_H=o(H)`.

Apply (19) with `M=H`, `h<=L_H`, and choose

\[
\gamma:=\frac\delta4.
\tag{22}
\]

Uniformly for the whole block,

\[
\|V_{H+h,D}-V_{H,D}\|_2^2
\ll
H^{2\Theta-2\delta}
+H^{\Theta-3\delta/4}.
\tag{23}
\]

Divide by the seed energy in (20). This gives exactly (3):

\[
\boxed{
\sup_{0\le h\le L_H}
\frac{\|V_{H+h,D}-V_{H,D}\|_2^2}{E_{H,D}}
\ll
H^{-3\delta/2}
+H^{-\Theta-\delta/4}
\longrightarrow0.
}
\tag{24}
\]

Let

\[
\widehat V_{H,D}:=
\frac{V_{H,D}}{\|V_{H,D}\|_2}.
\tag{25}
\]

The reverse triangle inequality and (24) first give

\[
\boxed{
\sup_{0\le h\le L_H}
\left|
\sqrt{\frac{E_{H+h,D}}{E_{H,D}}}-1
\right|
\longrightarrow0,
}
\tag{26}
\]

and then the standard normalization estimate yields

\[
\boxed{
\sup_{0\le h\le L_H}
\|\widehat V_{H+h,D}-\widehat V_{H,D}\|_2
\longrightarrow0.
}
\tag{27}
\]

Hence for any two displacements `h_1,h_2` in the same block,

\[
\boxed{
\left\langle
\widehat V_{H+h_1,D},
\widehat V_{H+h_2,D}
\right\rangle
\longrightarrow1
}
\tag{28}
\]

uniformly. The whole block therefore carries one asymptotic signed Jordan direction, not merely comparable scalar energy.

There is an immediate simultaneous consequence for every fixed orthogonal coordinate projection `P` on the common Jordan space. Equation (27) gives

\[
\boxed{
\sup_{0\le h\le L_H}
\left|
\|P\widehat V_{H+h,D}\|_2^2
-
\|P\widehat V_{H,D}\|_2^2
\right|
\longrightarrow0.
}
\tag{29}
\]

The nonsquarefree projector in (8) is only one example. Squarefree rows, fixed residue classes, finite square sieves, or any other horizon-independent row mask are all transported at once. This is information that cannot be recovered from the scalar occupation set `\{H:nu_(H,D)>eta\}`.

## 4. The full Schur projective defect is coherent on the same block

The distinguished equality direction of `FD-032`--`FD-034` is equally simple in the common Jordan coordinates. Define

\[
G_{H,D}(r)
:=
-\frac{\mu(r)}{\sqrt{J_2(r)}}
\mathbf 1_{D<r\le H}.
\tag{30}
\]

Then

\[
\|G_{H,D}\|_2^2
=
\Delta_{H,D}=C_H-C_D,
\tag{31}
\]

and the squared transverse Schur residual is

\[
\boxed{
\rho_{H,D}^2
=
\operatorname{dist}\!\left(
V_{H,D},\operatorname{span}(G_{H,D})
\right)^2.
}
\tag{32}
\]

For fixed `D`, `Delta_(H,D)` tends to the positive constant `zeta(2)-C_D`. Moreover `J_2(r)>=r^2/zeta(2)`, so for `0<=h<=L_H`,

\[
\begin{aligned}
\|G_{H+h,D}-G_{H,D}\|_2^2
&=
\sum_{H<r\le H+h}\frac{\mu(r)^2}{J_2(r)}\\
&\le
\zeta(2)\sum_{H<r\le H+h}\frac1{r^2}\\
&\ll \frac{h}{H^2}
=o(1).
\end{aligned}
\tag{33}
\]

Thus the **normalized equality ray itself** changes by `o(1)` uniformly across the block. Let `P_H` denote orthogonal projection onto `span(G_(H,D))`. Equations (31)--(33) imply

\[
\sup_{0\le h\le L_H}\|P_{H+h}-P_H\|_{\rm op}
\longrightarrow0.
\tag{34}
\]

The normalized projective defect is

\[
\varepsilon_{H,D}
=
\frac{\rho_{H,D}^2}{E_{H,D}}
=
\|(I-P_H)\widehat V_{H,D}\|_2^2.
\tag{35}
\]

Combining (27) and (34) therefore gives the block transport law

\[
\boxed{
\sup_{0\le h\le L_H}
|\varepsilon_{H+h,D}-\varepsilon_{H,D}|
\longrightarrow0.
}
\tag{36}
\]

Because the seed is already nonsquarefree-occupied, `epsilon_(H,D)>=nu_(H,D)>eta_1`. Hence the normalized transverse vectors

\[
R_{H,D}
:=(I-P_H)\widehat V_{H,D}
\tag{37}
\]

have norms uniformly bounded away from zero on the seed sequence. Equations (27) and (34) then also imply

\[
\boxed{
\sup_{0\le h\le L_H}
\left\|
\frac{R_{H+h,D}}{\|R_{H+h,D}\|_2}
-
\frac{R_{H,D}}{\|R_{H,D}\|_2}
\right\|_2
\longrightarrow0.
}
\tag{38}
\]

So the transverse Schur loss is not merely positive throughout the block: its **direction** is asymptotically common. Any future multihorizon functional capable of summing these transverse vectors would therefore encounter coherent rather than adversarially rotating defects inside each physical block.

Equation (38) is deliberately not converted into such a functional here. The present GCD-duality accumulation theorems compare special multiplicatively compatible horizons; they do not identify the sum of the additive residual vectors above with a Franel quantity at one larger horizon.

## 5. What this adds after the `FD-085` matched control

The synthetic set in `FD-085` matches stronger versions of the current **locations** of good horizons: full counting exponent in every fixed-power window and even linear consecutive blocks. It carries no analogue of the vector `V_(H,D)`, the exact support law (13), or the angular collapse (27). Therefore it does not test, and cannot refute, the additive transport theorem above.

This closes one narrower gap left explicitly by `FD-084` and `FD-085`. Within a physical occupied block there is no hidden freedom to rotate the Jordan energy among unrelated row patterns from one horizon to the next. Up to a vanishing relative error, the complete physical state, the equality ray, and the transverse defect are frozen over the full frontier-length interval `H^(Theta-delta)`.

The remaining obstruction is now **inter-block transport**. The theorem does not prevent the block seeds themselves from occurring on a superexponential schedule, and it does not show that two separated coherent caps have compatible directions after any fixed integer dilation. `FD-034` still gives the exact lower-horizon copy on square-divisor rows, but `FD-071` shows that destination energy can dilute such a copied packet. Combining that dilation copy with (27)--(38) may be useful, but a bound controlling the destination denominator or a new multihorizon functional is still required.

A natural next statement to test is therefore not another abundance theorem. It is whether the exact dilation embedding from `FD-034`, applied to one coherent block, forces a non-negligible overlap with the coherent direction of a later physical block before the destination energy can rotate or dilute it. Failure would need an explicit source-like control carrying both the divisor-supported additive transport (19) and the superexponential inter-block escape.

## 6. Falsification and scope boundary

The exact inequality (19) is a theorem about a **common fixed head**. If the Schur head changes with the horizon, rows are inserted or deleted at the head and an additional comparison is required. The `FD-084` corollary is fixed-head for the same reason.

The small relative displacement in (24) depends on near-frontier seed energy. A generic horizon with much smaller `E_(H,D)` need not have a stable normalized direction even though the absolute bound (19) still holds. Likewise, the transport scale is genuinely additive and sublinear. Nothing here claims coherence for `h` comparable with `H`.

The proof uses only the quotient-shell floor sampling and `|c(n)|<=1`. It therefore does **not** yet exploit the full Möbius sign law. A synthetic one-Lipschitz quotient-shell profile that also realizes comparable near-frontier seeds would satisfy the same Hilbert transport estimate. This is stronger than the set-theoretic control of `FD-085` but weaker than a theorem that distinguishes the true arithmetic source from every bounded-increment control. If such a synthetic profile can also realize superexponentially separated coherent blocks while satisfying the existing annular constraints, that would identify the next missing arithmetic input rather than contradict this finding.

No claim is made that (36) improves the pointwise lower bound of `FD-036`, that coherent residual vectors automatically add to a stronger scalar Franel estimate, or that the present theorem changes the zeta-zero exponent. Its contribution is a precise source-structural transport law and a reduction of the compatibility frontier.

## 7. Prior-art boundary

The literature audit covered the classical and recent Farey/Mertens discrepancy material already anchored in `SOURCES.md`, the Smith/GCD-matrix factorization underlying the Jordan coordinates, and floor-quotient structures around Mertens matrices. In particular, García's 2025 Farey rank/local-discrepancy formulas provide neighboring Mertens/Farey identities; Jean-Paul Cardinal's *Symmetric matrices related to the Mertens function* (arXiv:`0811.3701`) studies a different matrix route to Mertens norm bounds; and Lagarias--Richman's *The floor quotient partial order* (Advances in Applied Mathematics **153** (2024), arXiv:`2212.11689`) studies the internal order structure generated by values `floor(n/k)`.

No located source states the present combination: the divisor-incidence Hilbert displacement (19) for the physical Jordan vector, its relative collapse on zero-frontier-energy blocks, or the resulting coherence of the Schur projective defect direction. This absence is not treated as a priority claim. The proof above is elementary once the Mathia-specific Jordan representation and source coefficient law have been established.

No new external theorem is load-bearing: the only generic estimate used beyond canonical line identities is the standard divisor bound already used in `FD-084`. Accordingly no new durable dependency is added to `SOURCES.md`.