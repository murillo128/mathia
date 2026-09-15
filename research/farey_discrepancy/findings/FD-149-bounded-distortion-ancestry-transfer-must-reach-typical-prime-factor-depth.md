# FD-149 — Bounded-distortion ancestry transfer must reach typical prime-factor depth

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** multiscale ancestry obstruction / quantitative nonlocality threshold
- **Depends on:** FD-148

## Claim

FD-148 shows that one-step finite-seed ancestry cannot have uniformly positive anchored expansion while its endpoint marginals remain a bounded-distortion version of the uniform squarefree coefficient measure. A natural escape is to replace one-step ancestry by a nonlocal relation that may jump several prime-adjunction generations at once. The depth needed for that escape is itself forced by the arithmetic geometry.

Let

\[
V_T=\{n\le T:\mu^2(n)=1\},
\qquad
\nu_T(n)=|V_T|^{-1},
\tag{1}
\]

and let `D` be a fixed finite divisor-closed subset of the squarefree integers containing `1`. Put

\[
r_D:=\max_{d\in D}\omega(d).
\tag{2}
\]

For an integer depth `L>=1`, define the positive `L`-step ancestry relation

\[
E_T^{(\le L)}
:=
\{(n,m)\in V_T^2:n\mid m,\ 1\le \omega(m/n)\le L\},
\tag{3}
\]

and the descendants reachable from the anchor within `L` prime adjunctions,

\[
R_{D,L}(T)
:=
\{m\in V_T\setminus D:\exists d\in D,\ d\mid m,\ \omega(m/d)\le L\}.
\tag{4}
\]

Let `eta_T` be any probability measure on `E_T^(<=L)` and write its child marginal as

\[
\eta_T^+(m)
:=
\sum_{n:(n,m)\in E_T^{(\le L)}}\eta_T(n,m).
\tag{5}
\]

Define the corresponding anchored Cheeger constant

\[
h_{D,T}^{(\le L)}
:=
\inf_{\varnothing\ne A\subseteq V_T\setminus D}
\frac{\eta_T(\partial A)}{\nu_T(A)}.
\tag{6}
\]

If the child marginal is `K_T`-dominated by the coefficient measure on the reachable anchor descendants,

\[
\eta_T^+(m)\le K_T\nu_T(m)
\qquad(m\in R_{D,L}(T)),
\tag{7}
\]

then the complement cut gives the exact structural bound

\[
\boxed{
h_{D,T}^{(\le L)}
\le
\frac{K_T\nu_T(R_{D,L}(T))}{1-\nu_T(D)}.
}
\tag{8}
\]

The arithmetic content is the size of `R_{D,L}(T)`.

For every **fixed** depth `L`, Landau's fixed-rank almost-prime law yields

\[
\boxed{
\nu_T(R_{D,L}(T))
\ll_{D,L}
\frac{(\log\log T)^{r_D+L-1}}{\log T},
}
\tag{9}
\]

with the convention that the right side is replaced by `O_D(1/T)` when `r_D+L=0`. Hence

\[
\boxed{
h_{D,T}^{(\le L)}
\ll_{D,L}
K_T\frac{(\log\log T)^{r_D+L-1}}{\log T}.
}
\tag{10}
\]

Thus **no fixed-depth positive ancestry transfer with `K_T=O(1)` can have uniformly positive finite-seed anchored expansion**. More quantitatively, positive expansion at fixed depth forces

\[
K_T
\gg_{c,D,L}
\frac{\log T}{(\log\log T)^{r_D+L-1}}.
\tag{11}
\]

The variable-depth threshold is sharper. Let

\[
\lambda_T:=\log\log T.
\tag{12}
\]

Assume `K_T<=K` for a fixed `K<infinity` and

\[
\liminf_{T\to\infty} h_{D,T}^{(\le L_T)}\ge c>0.
\tag{13}
\]

If `0<c/K<1`, then squarefree Erdos--Kac forces

\[
\boxed{
\liminf_{T\to\infty}
\frac{r_D+L_T-\lambda_T}{\sqrt{\lambda_T}}
\ge
\Phi^{-1}(c/K),
}
\tag{14}
\]

where `Phi` is the standard normal distribution function. In particular

\[
\boxed{
L_T
\ge
\log\log T-O_{c,K,D}(\sqrt{\log\log T}).
}
\tag{15}
\]

Consequently, for every fixed `delta>0`,

\[
L_T\le(1-\delta)\log\log T
\quad\Longrightarrow\quad
h_{D,T}^{(\le L_T)}\to0
\qquad(K_T=O(1)).
\tag{16}
\]

So FD-148's vague remaining escape through a "genuinely nonlocal" ancestry interface can be quantified: **bounded endpoint distortion requires genealogical reach all the way to the typical squarefree prime-factor depth, namely order `log log T`**. Any substantially shallower positive transfer must pay for the missing reach by a diverging child-marginal amplification.

## 1. The complement cut sees only descendants reachable from the anchor

Take

\[
A_T:=V_T\setminus D.
\tag{17}
\]

Because `D` is divisor-closed, an ancestry relation directed by divisibility cannot enter `D` from `A_T`. Thus every `E_T^(<=L)` edge crossing the complement cut starts in `D` and ends in `R_{D,L}(T)`. Therefore

\[
\eta_T(\partial A_T)
\le
\sum_{m\in R_{D,L}(T)}\eta_T^+(m).
\tag{18}
\]

Using (7),

\[
\eta_T(\partial A_T)
\le
K_T\nu_T(R_{D,L}(T)).
\tag{19}
\]

Since

\[
\nu_T(A_T)=1-\nu_T(D),
\tag{20}
\]

testing only this one cut in (6) proves (8).

This is the same endpoint mechanism isolated in FD-148, but there is now no one-step assumption. The only question is how much of the coefficient space can be reached from a fixed anchor after `L` prime adjunctions.

## 2. Fixed depth still occupies a vanishing coefficient fraction

If `m\in R_{D,L}(T)`, choose `d\in D` witnessing (4). Since both `d` and `m` are squarefree and `d|m`,

\[
\omega(m)
=
\omega(d)+\omega(m/d)
\le
r_D+L.
\tag{21}
\]

Hence

\[
R_{D,L}(T)
\subseteq
\{m\le T:\mu^2(m)=1,\ \omega(m)\le r_D+L\}.
\tag{22}
\]

For every fixed integer `j>=1`, Landau's squarefree fixed-rank asymptotic gives

\[
N_j(T)
:=
\#\{m\le T:\mu^2(m)=1,\ \omega(m)=j\}
\sim
\frac{T(\log\log T)^{j-1}}
{(j-1)!\log T}.
\tag{23}
\]

Summing (23) over the finitely many ranks `j<=r_D+L`, and using

\[
|V_T|=\frac{T}{\zeta(2)}+o(T),
\tag{24}
\]

proves (9). Substitution in (8), together with `nu_T(D)=O_D(1/T)`, gives (10).

The consequence is stronger than saying that the original one-step prime fan is sparse. Thickening that fan by **any fixed number of multiplicative generations** still leaves a zero-density subset of the coefficient space. Bounded child distortion therefore cannot turn finite-depth locality into constant anchored cut exposure.

## 3. Bounded distortion forces Erdos--Kac depth

Now let the depth vary with `T`. Equation (21) remains valid, so

\[
\nu_T(R_{D,L_T}(T))
\le
\nu_T\!\left(
\omega(m)\le r_D+L_T
\right).
\tag{25}
\]

The squarefree Erdos--Kac theorem says that under `nu_T`,

\[
Z_T(m)
:=
\frac{\omega(m)-\lambda_T}{\sqrt{\lambda_T}}
\Longrightarrow N(0,1).
\tag{26}
\]

On the other hand, (8) and (13), with `K_T<=K` and `nu_T(D)->0`, force

\[
\liminf_{T\to\infty}
\nu_T(R_{D,L_T}(T))
\ge
\frac cK.
\tag{27}
\]

Put

\[
z_T
:=
\frac{r_D+L_T-\lambda_T}{\sqrt{\lambda_T}}.
\tag{28}
\]

If some subsequence had

\[
z_T\le \Phi^{-1}(c/K)-\varepsilon
\tag{29}
\]

for a fixed `epsilon>0`, then (25)--(26) would give along that subsequence

\[
\limsup \nu_T(R_{D,L_T}(T))
\le
\Phi\!\left(\Phi^{-1}(c/K)-\varepsilon\right)
<
\frac cK,
\tag{30}
\]

contradicting (27). This proves (14), hence (15).

If `L_T<=(1-delta)lambda_T`, then `z_T->-infinity`. Tightness in (26) makes the right side of (25) tend to zero, and (8) gives (16).

The endpoint cases are consistent with the same picture. If `c/K>1`, (27) is impossible. If `c/K=1`, positive exposure at that maximal level would require the reachable coefficient mass to tend to one, and therefore necessarily `z_T->+infinity`; equivalently the depth must pass above the Erdos--Kac center by more than a bounded number of standard deviations.

## 4. The `log log T` scale is not an artifact of the upper bound

For the minimal anchor `D={1}` the reachable set is exactly

\[
R_{\{1\},L}(T)
=
\{m\in V_T:\ 1\le\omega(m)\le L\}.
\tag{31}
\]

There is no loss in (22). Hence if

\[
L_T
=
\lambda_T+z\sqrt{\lambda_T}+o(\sqrt{\lambda_T})
\tag{32}
\]

for fixed real `z`, squarefree Erdos--Kac gives

\[
\boxed{
\nu_T(R_{\{1\},L_T}(T))
\longrightarrow
\Phi(z).
}
\tag{33}
\]

Thus the complement-cut obstruction itself has a genuine transition window of width `sqrt(log log T)` around depth `log log T`. A proof that only thickens the anchor by, say, two, ten, or even `o(log log T)` prime-adjunction layers remains on the sparse side of that transition.

This does **not** prove that depth near `log log T` is sufficient for a positive Cheeger constant. Other cuts may still be cheap. It proves that the fixed-anchor complement cut cannot stop a bounded-distortion construction merely because its depth has reached the typical prime-factor scale. So the threshold is sharp for the obstruction being isolated here, not a sufficiency theorem for the full transfer problem.

## 5. Matched controls and scope

The result depends on three restrictions, each of which has a concrete escape.

First, positivity is essential. A signed or oscillatory transfer can cancel across the complement cut and is not represented by a probability edge law. Such a construction would require a different coercivity mechanism.

Second, the anchor is fixed. If `D=D_T` grows so that its rank profile already reaches typical squarefree integers, the estimate through `r_D` no longer gives the same obstruction. But that is precisely a different strategy: it spends nonlocality in the anchor rather than in the transfer depth, and its relevance to the original Farey coefficient norm must be justified separately.

Third, bounded child distortion is essential. FD-148 already supplies the matched control: at depth one, a measure may put constant boundary mass on the prime fan by amplifying a coefficient set of mass `Theta(1/log T)` by a logarithmic factor. More generally (10) quantifies the price of keeping depth fixed. The theorem does not rule out such singular endpoint emphasis; it says that **bounded distortion and shallow reach cannot be kept simultaneously**.

For `D={1}`, (33) also gives a matched control on the depth estimate itself. Once the relation reaches `lambda_T+z sqrt(lambda_T)` generations, a fixed Gaussian fraction `Phi(z)` of the squarefree coefficient mass is genuinely accessible. Therefore no argument based only on cardinality of the reachable set can force a stronger depth requirement than the Erdos--Kac scale.

## 6. Prior-art and evidence boundary

The fixed-rank almost-prime asymptotic of Landau and the squarefree Erdos--Kac theorem are classical arithmetic inputs already anchored in `research/farey_discrepancy/SOURCES.md`: Wright is the fixed-rank source used in FD-131, and Li--Wang--Wang--Yi is the squarefree Erdos--Kac source used in FD-132. No new external dependency is introduced here.

The new line-specific statement is the splice of those rank laws with the endpoint-amplification obstruction of FD-148. It turns the qualitative phrase "use a genuinely nonlocal ancestry interface" into a quantitative trilemma:

\[
\boxed{
\text{positive fixed-seed exposure}
\Longrightarrow
\text{typical-rank depth}
\quad\text{or}\quad
\text{diverging endpoint amplification}
\quad\text{or}\quad
\text{a growing/nonlocal anchor}.
}
\tag{34}
\]

No abstract graph-theoretic novelty is claimed. The arithmetic content is that the squarefree coefficient geometry places the bounded-distortion transition at the typical multiplicative rank `omega(n)~log log T`.

## 7. Falsifiable next test

A proposed Farey-native positive multiscale transfer can now be screened before attempting a full coercivity proof. Compute its effective ancestry depth `L_T`, its anchor rank `r_D`, and the smallest child-marginal distortion `K_T` for which

\[
\eta_T^+(m)\le K_T\nu_T(m)
\tag{35}
\]

on the descendants carrying the anchor cut. If `D` is fixed, `K_T=O(1)`, and

\[
L_T\le(1-\delta)\log\log T
\tag{36}
\]

for some fixed `delta>0`, then the construction is dead on arrival: its anchored complement cut has vanishing exposure. If instead a source-native Farey or gcd-kernel weighting naturally reaches the Erdos--Kac depth while retaining bounded distortion, that would be the first local-to-nonlocal candidate not excluded by FD-147--FD-149 and should be tested against the remaining non-anchor cuts.
