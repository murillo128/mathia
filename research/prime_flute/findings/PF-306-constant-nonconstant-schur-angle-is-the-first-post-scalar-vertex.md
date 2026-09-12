# PF-306 — constant–nonconstant Schur angle is the first post-scalar conversion vertex

**Status:** `EXACT-DERIVED + CLASSICAL-SCHUR-COMPLEMENT + ROUTE-LOCALIZING`.

PF-303--PF-305 show that the finite constant-mode pant chain has a canonical killing normalization in which its complete scalar Green reservoir is a positive contraction and is neutral for symmetric operator ideals. The remaining question is therefore not another scalar Green estimate: it is where the **actual nonconstant boundary response first leaves that scalar chain**.

There is an exact answer at the level of every finite positive boundary-response section. Split the retained boundary variables into the global cuff-constant sector `\mathcal C_N` and its retained nonconstant complement `\mathcal Q_N`. Before the nonconstant modes are eliminated, the constant/constant compression is precisely the PF-303 scalar operator

\[
H_N=L_{c,N}+D_N>0.
\]

Thus the full positive response form has block matrix

\[
\mathcal A_N=
\begin{pmatrix}
H_N & B_N\\
B_N^* & J_N
\end{pmatrix}>0,
\]

where `B_N` is the first constant-to-nonconstant conversion operator and `J_N>0` is the nonconstant block. Normalize that conversion by the intrinsic energies on both sides:

\[
\boxed{K_N:=H_N^{-1/2}B_NJ_N^{-1/2}.}
\]

Then `\|K_N\|<1` for every finite strictly positive section, and shorting the nonconstant variables replaces the scalar chain by

\[
\boxed{
H_N^{\mathrm{eff}}
=H_N-B_NJ_N^{-1}B_N^*
=H_N^{1/2}(I-K_NK_N^*)H_N^{1/2}.
}
\]

Consequently the constant block of the **full** Green operator is

\[
\boxed{
[\mathcal A_N^{-1}]_{\mathcal C_N\mathcal C_N}
=H_N^{-1/2}(I-K_NK_N^*)^{-1}H_N^{-1/2}.
}
\]

This identifies the first operator omitted by the PF-303--PF-305 scalar model. If `B_N=0`, the scalar Green operator `G_N=H_N^{-1}` is exact on constants. If `B_N\neq0`, the first correction is not another return-depth factor but the **constant–nonconstant Schur-angle resolvent** `(I-K_NK_N^*)^{-1}`.

The same operator has an exact variational meaning. For `x\in\mathcal C_N`, the fraction of the raw constant compression energy erased by optimally relaxing the nonconstant modes is

\[
\delta_N(x)
:=1-
\frac{
\inf_{y\in\mathcal Q_N}
\langle (x,y),\mathcal A_N(x,y)\rangle
}{\langle x,H_Nx\rangle}
=
\frac{\|K_N^*H_N^{1/2}x\|^2}{\|H_N^{1/2}x\|^2}.
\]

Hence

\[
\boxed{
\sup_{x\neq0}\delta_N(x)=\|K_N\|^2.
}
\]

So `\|K_N\|^2` is exactly the worst assembled constant-energy fraction that can be screened by the retained nonconstant sector. This is the global version of the local low/high shorting deficit isolated in PF-290, now placed directly at the boundary between the PF-303 scalar chain and the full response.

## Claim

Let `\mathcal A_N` be any finite-dimensional strictly positive Galerkin section of the exact shifted/positive assembled boundary-response form for a finite prime-flute pant chain, chosen so that all cuff-constant modes are retained. Decompose its boundary space orthogonally as

\[
\mathcal C_N\oplus\mathcal Q_N,
\]

where `\mathcal C_N` is the global cuff-constant sector and `\mathcal Q_N` contains the retained nonconstant modes. By the constant compression assembled in PF-298 and PF-303,

\[
P_{\mathcal C_N}\mathcal A_N|_{\mathcal C_N}
=H_N=L_{c,N}+D_N>0.
\tag{1}
\]

Write

\[
\mathcal A_N=
\begin{pmatrix}
H_N & B_N\\
B_N^* & J_N
\end{pmatrix},
\qquad J_N>0,
\tag{2}
\]

and define

\[
K_N:=H_N^{-1/2}B_NJ_N^{-1/2}.
\tag{3}
\]

Then:

1. `I-K_NK_N^*>0`, so
   \[
   \boxed{\|K_N\|<1.}
   \tag{4}
   \]
2. eliminating `\mathcal Q_N` gives the exact shorted constant form
   \[
   \boxed{
   H_N^{\mathrm{eff}}
   :=H_N-B_NJ_N^{-1}B_N^*
   =H_N^{1/2}(I-K_NK_N^*)H_N^{1/2}.
   }
   \tag{5}
   \]
3. the constant/constant block of the inverse is
   \[
   \boxed{
   [\mathcal A_N^{-1}]_{\mathcal C_N\mathcal C_N}
   =H_N^{-1/2}(I-K_NK_N^*)^{-1}H_N^{-1/2}.
   }
   \tag{6}
   \]
4. for every nonzero `x\in\mathcal C_N`, if
   \[
   \delta_N(x):=
   1-
   \frac{
   \inf_y\langle(x,y),\mathcal A_N(x,y)\rangle
   }{\langle x,H_Nx\rangle},
   \tag{7}
   \]
   then
   \[
   \boxed{
   \delta_N(x)
   =\frac{\|K_N^*H_N^{1/2}x\|^2}
   {\|H_N^{1/2}x\|^2},
   \qquad
   \sup_{x\neq0}\delta_N(x)=\|K_N\|^2.
   }
   \tag{8}
   \]
5. with the PF-303 killing matrix `D_N`, put
   \[
   X_N:=H_N^{-1/2}D_N^{1/2},
   \qquad
   S_N:=D_N^{1/2}H_N^{-1}D_N^{1/2}=X_N^*X_N.
   \tag{9}
   \]
   The killing-normalized full constant Green block is
   \[
   \widetilde S_N
   :=D_N^{1/2}[\mathcal A_N^{-1}]_{\mathcal C_N\mathcal C_N}D_N^{1/2}
   =X_N^*(I-K_NK_N^*)^{-1}X_N,
   \tag{10}
   \]
   and obeys the exact Loewner bounds
   \[
   \boxed{
   S_N\le\widetilde S_N
   \le\frac{1}{1-\|K_N\|^2}\,S_N.
   }
   \tag{11}
   \]
6. the constant/nonconstant block of the full inverse is
   \[
   \boxed{
   [\mathcal A_N^{-1}]_{\mathcal C_N\mathcal Q_N}
   =-H_N^{-1/2}
   (I-K_NK_N^*)^{-1}
   K_NJ_N^{-1/2}.
   }
   \tag{12}
   \]

Equations (10)--(12) isolate three different currencies that should not be conflated: the already-controlled killing-normalized scalar reservoir `X_N`, the normalized conversion angle `K_N`, and the nonconstant energy normalization `J_N^{-1/2}`.

## 1. Positivity forces a strict finite-section angle

Since `\mathcal A_N>0` and `J_N>0`, its Schur complement in the nonconstant block is strictly positive:

\[
H_N-B_NJ_N^{-1}B_N^*>0.
\tag{13}
\]

Using (3),

\[
B_NJ_N^{-1}B_N^*
=H_N^{1/2}K_NK_N^*H_N^{1/2},
\tag{14}
\]

so (13) is equivalent to

\[
I-K_NK_N^*>0.
\tag{15}
\]

In finite dimension this gives `\|K_N\|<1`, proving (4), and (5) follows directly. Inverting (5) gives (6).

The inequality is deliberately only a finite-section statement. Nothing here supplies a depth-uniform gap `\|K_N\|\le1-\varepsilon`. The possibility `\|K_N\|\to1` is exactly the new live obstruction.

## 2. The Schur angle is the exact assembled screening fraction

For fixed `x`, complete the square in the nonconstant variable:

\[
\begin{aligned}
\langle(x,y),\mathcal A_N(x,y)\rangle
&=\langle x,H_Nx\rangle
+2\operatorname{Re}\langle B_N^*x,y\rangle
+\langle y,J_Ny\rangle\\
&=\langle x,(H_N-B_NJ_N^{-1}B_N^*)x\rangle
+\|J_N^{1/2}(y+J_N^{-1}B_N^*x)\|^2.
\end{aligned}
\tag{16}
\]

The minimizer is `y_*=-J_N^{-1}B_N^*x`, and therefore

\[
\langle x,H_Nx\rangle
-\inf_y\langle(x,y),\mathcal A_N(x,y)\rangle
=\langle x,B_NJ_N^{-1}B_N^*x\rangle.
\tag{17}
\]

But

\[
J_N^{-1/2}B_N^*x
=K_N^*H_N^{1/2}x,
\tag{18}
\]

which gives (8). Thus `\|K_N\|^2` is not merely a convenient block norm: it is the exact worst normalized loss of constant compression energy caused by optimal nonconstant relaxation.

This sharpens the qualitative warning of PF-217 and PF-279. Those results show that tangential/nonconstant reservoirs can erase a raw local floor after shorting. Equation (8) identifies the dimensionless assembled quantity that measures precisely how much of the current scalar chain can be erased.

## 3. Killing normalization exposes the only possible scalar backreaction factor

PF-305 proves

\[
0<S_N\le I,
\qquad
\|S_N\|=1.
\tag{19}
\]

Using (6) and (9) gives (10). Since

\[
I\le(I-K_NK_N^*)^{-1}
\le\frac{1}{1-\|K_N\|^2}I,
\tag{20}
\]

conjugation by `X_N` gives (11).

Therefore a uniform angle gap

\[
\sup_N\|K_N\|\le\kappa<1
\tag{21}
\]

would make the effect of nonconstant shorting on the killing-normalized constant Green block uniformly harmless up to the fixed factor `(1-\kappa^2)^{-1}`. In that regime the PF-305 conclusion is robust: depth in the scalar Green reservoir still cannot create an uncontrolled operator-ideal loss by itself.

Conversely, if `\|K_N\|\to1`, the Schur-angle resolvent can become arbitrarily large. Then the scalar estimate `0<S_N\le I` cannot control the full constant response. This is the first exact operator at which the scalar factorization can fail.

That converse must not be overread. Near-unit `\|K_N\|` does **not** by itself imply a large physical `P/H` response. The almost-screened directions may be invisible to the actual source and reassembly maps. A source-adapted estimate on the range actually used by the physical response may be enough even when the full operator norm tends to one.

## 4. The mixed Green block factors through the same angle

The standard block inverse formula and (3) give

\[
[\mathcal A_N^{-1}]_{\mathcal C_N\mathcal Q_N}
=-(H_N-B_NJ_N^{-1}B_N^*)^{-1}B_NJ_N^{-1},
\tag{22}
\]

hence (12). The full mixed response therefore separates into:

- a constant energy normalization `H_N^{-1/2}`;
- the angle resolvent `(I-K_NK_N^*)^{-1}`;
- the normalized conversion `K_N`;
- a nonconstant energy normalization `J_N^{-1/2}`.

This is the concrete specialization of the generic normalized cross-form algebra in PF-281/PF-282 to the **actual constant versus nonconstant split sitting immediately above PF-303--PF-305**. It does not yet derive the final physical source/reassembly vertices, but it tells that derivation exactly which new operator has to be estimated once the scalar chain is embedded back into the full boundary response.

## 5. Prior art and novelty audit

The Schur-complement and shorted-operator algebra used here is classical. Anderson and Trapp, *Shorted Operators. II*, SIAM Journal on Applied Mathematics 28(1), 60--71 (1975), DOI `10.1137/0128007`, develops shorting for positive operators and its network interpretation. Li and Mathias, *Extremal Characterizations of the Schur Complement and Resulting Inequalities*, SIAM Review 42(2), 233--246 (2000), DOI `10.1137/S0036144599337290`, gives variational characterizations and inequalities for positive Schur complements. No novelty is claimed for (5)--(8), block inversion, or the normalized-angle criterion itself.

The Mathia-specific contribution is placement, not abstract operator theory. PF-217 already warned that nonconstant boundary screening can erase raw pant mass; PF-281/PF-282 already supplied generic normalized cross-form algebra; PF-290 identifies a local low/high shorting deficit. What had remained unresolved after PF-303--PF-305 was **where that algebra enters the current assembled scalar chain**. Equations (5), (10), and (12) identify the first missing conversion vertex exactly: the normalized constant-to-nonconstant block `K_N` of the assembled full response.

A structure-directed literature audit found the expected classical Schur-complement/shorted-operator framework and no basis for a theorem-level novelty claim. The new value here is that the current Prime Flute frontier is reduced from the vague alternative “perhaps the physical response does not factor through the scalar chain” to a precise finite-section object and a decisive estimate.

## 6. Boundaries and failure modes

This finding establishes no compactness, weak-Schatten estimate, localization theorem, or RH consequence by itself.

The strict inequality `\|K_N\|<1` uses a finite strictly positive section. An infinite-dimensional or infinite-depth limit may have only `\|K\|\le1`; passing to that limit requires the appropriate closed-form/domain control and cannot be inferred from finite matrices alone.

The result also does not prove a uniform gap in (21). `\|K_N\|\to1` is compatible with every finite section being strictly positive. Determining whether Prime Flute geometry forces or excludes such near-saturation is a new geometric/operator question.

Operator-norm saturation may be physically irrelevant if the near-unit singular directions are not reached by the actual `P/H` source map. Conversely, a modest global norm can still be insufficient if the required target is a sharper weak/Schatten counting estimate. The eventual test should therefore be source- and target-adapted whenever possible.

Finally, `K_N` is only the **first** conversion vertex beyond the scalar chain. The actual physical response may contain further nonconstant propagation, reassembly, and extension-mass factors. Nothing here licenses replacing the full response by `(I-K_NK_N^*)^{-1}` alone.

## 7. Decisive next test

The next calculation is now sharply specified. Starting from the exact neighboring-pant full boundary kernels, derive the assembled blocks `B_N` and `J_N` in the same energy normalization that produces `H_N`, and test the normalized conversion

\[
K_N=H_N^{-1/2}B_NJ_N^{-1/2}.
\]

A depth-uniform bound `\|K_N\|\le1-\varepsilon` would show that nonconstant shorting cannot undo the PF-305 killing-normalized scalar control by more than a fixed factor. A sequence of normalized constant inputs with `\delta_N(x_N)\to1` would prove near-total screening and exhibit the exact failure mode instead.

For the physical `P/H` target, the stronger and potentially cheaper question is source-adapted: estimate `(I-K_NK_N^*)^{-1/2}X_N` only on the actual source range and its corresponding reassembly range. This avoids demanding a uniform global angle gap when the near-singular directions are physically inaccessible.

Thus the live gate has moved from **scalar return depth** to **constant–nonconstant conversion geometry**. Any subsequent claim that the scalar chain controls the full response must now pay for that conversion explicitly.