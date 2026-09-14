# RE-120 — isolated finite zero edges determine every algebraic CA-height correction

**Status:** `EXACT-DERIVED + FINITE-ZERO-EDGE + SPECTRAL-GAP-CONDITIONAL + ALL-ORDERS-HEIGHT-EXPANSION + STABLE-FILTER-CLOSURE + REPRESENTATION-OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume RH is false with a finite attained zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\qquad c:=1-\Theta,
\tag{1}
\]

and impose the additional **horizontal isolation** hypothesis

\[
\boxed{
\exists\delta>0:\quad
\zeta(\rho)=0,\ \Re\rho<\Theta
\Longrightarrow
\Re\rho\le \Theta-\delta .
}
\tag{2}
\]

The hypothesis is not known and is not a consequence of `RE-113`--`RE-119`; its role is precisely to ask whether the first lower-order terms left open by `RE-119` can contain new CA arithmetic when the extreme zero face is spectrally isolated.

They do not. Let `C` range over sufficiently large regular CA states and put

\[
Y:=\log C,
\qquad
\nu:=\log Y,
\qquad
B_\Theta(C):=Y^c\nu\,(e^{h(C)}-1).
\tag{3}
\]

For the attained edge define

\[
J_0(u)
:=
\sum_{\Re\rho=\Theta}
\frac{e^{i\Im(\rho)u}}{\rho(1-\rho)}
=J(u)
\tag{4}
\]

as in `RE-114`--`RE-119`, and for `k>=1`

\[
\boxed{
J_k(u)
:=
\sum_{\Re\rho=\Theta}
\frac{e^{i\Im(\rho)u}}{(1-\rho)^{k+1}}.
}
\tag{5}
\]

Then for every fixed integer `K>=1`, uniformly over regular CA states,

\[
\boxed{
B_\Theta(C)
=
J_0(\nu)
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{\nu^k}J_k(\nu)
+
O_{\Theta,\delta,K}(\nu^{-K-1}).
}
\tag{6}
\]

In particular,

\[
\boxed{
B_\Theta(C)
=
J(\nu)-\frac{J_1(\nu)}{\nu}
+O(\nu^{-2}).
}
\tag{7}
\]

The `1/nu` term therefore exists under isolation, but it is **not a new source coordinate**. If

\[
(\mathcal L f)(u)
:=\int_0^\infty e^{-cs}f(u+s)\,ds,
\tag{8}
\]

then the stable-filter identities of `RE-114` give

\[
G=J'+\Theta J,
\qquad
\boxed{J_k=\mathcal L^k G\quad(k\ge1).}
\tag{9}
\]

Thus every coefficient in the entire fixed-order inverse-`nu` expansion is deterministically reconstructed from the same leading edge profile `J`. Combined with the exponentially fine regular-CA phase mesh of `RE-119`, this rules out **every finite algebraic order in `1/log log C`** as an independent arithmetic-placement mechanism in the isolated-edge branch.

The complementary non-isolated branch is now sharply localized: a subedge zero with `beta=Theta-Delta` enters the edge-normalized height with factor `e^{-Delta nu}`. Hence a contribution that can survive at order `nu^{-K}` must come from a shrinking spectral boundary layer of width

\[
\boxed{
\Theta-\beta
\lesssim
\frac{K\log\nu}{\nu},
}
\tag{10}
\]

up to the absolutely summable zero coefficients. If no fixed spectral gap exists, those near-edge zeros -- rather than discrete CA sampling -- are the first unresolved source capable of dominating the algebraic correction hierarchy.

## 1. Isolation upgrades the edge projection to power separation

Choose

\[
\max\!\left(\frac12,\Theta-\delta\right)<\sigma<\Theta.
\tag{11}
\]

By (2), the strip `Re rho>=sigma` contains only edge zeros. The same fixed-strip zero-density argument used in `RE-112`--`RE-113` gives

\[
\sum_{\Re\rho\ge\sigma}
\frac1{1+|\Im\rho|}<\infty.
\tag{12}
\]

Repeating the truncated Riemann--von Mangoldt separation from `RE-113`, but now retaining every zero in `Re rho>=sigma`, gives for some fixed exponent `A=A(sigma)`

\[
\vartheta(x)-x
=
-x^\Theta F(\log x)
+O_{\Theta,\delta}\!\left(x^\sigma(\log x)^A\right),
\tag{13}
\]

where

\[
F(u)=\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)u}}\rho .
\tag{14}
\]

The same statement holds for the full CA event staircase because the higher-layer contribution is
`O(x^(1/2)(log x)^(3/2))`, strictly below `x^sigma`:

\[
x-\Phi(x)
=
x^\Theta F(\log x)
+O_{\Theta,\delta}\!\left(x^\sigma(\log x)^A\right).
\tag{15}
\]

The exact logarithmic power in (13)--(15) is immaterial here. After edge normalization the remainder is

\[
x^{\sigma-\Theta}(\log x)^A
=e^{-(\Theta-\sigma)u}u^A,
\qquad u=\log x,
\tag{16}
\]

and is therefore smaller than `u^{-M}` for every fixed `M`.

This is the only point where the isolation hypothesis is load-bearing. Without (2), zeros with real parts approaching `Theta` from below need not obey any fixed exponential separation in `u`.

## 2. The reciprocal-Mertens term has an exact edge kernel

Retain the notation of `RE-114`,

\[
E(x)
:=
\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x,
\tag{17}
\]

and

\[
f(x):=\frac1{x\log x},
\qquad
A(x):=\vartheta(x)-x.
\tag{18}
\]

The exact partial-summation identity already proved there is

\[
E(x)
=f(x)A(x)+\int_x^\infty A(t)f'(t)\,dt+O(x^{-1}).
\tag{19}
\]

For one edge zero `rho=Theta+i gamma`, its contribution to `A(t)` is `-t^rho/rho`. Put `u=log x` and `a:=1-rho`, so `Re a=c>0`. Substituting this single term into (19), changing variables `t=xe^s`, and using

\[
-f'(t)=\frac1{t^2\log t}+\frac1{t^2(\log t)^2}
\tag{20}
\]

gives

\[
\begin{aligned}
E_\rho(x)
&=
\frac{x^{\rho-1}}\rho
\left[
-\frac1u
+
\int_0^\infty e^{-as}
\left(\frac1{u+s}+\frac1{(u+s)^2}\right)ds
\right].
\end{aligned}
\tag{21}
\]

The bracket simplifies exactly. Since

\[
\frac d{ds}\frac{e^{-as}}{u+s}
=-a\frac{e^{-as}}{u+s}
-\frac{e^{-as}}{(u+s)^2},
\tag{22}
\]

integration by parts yields

\[
\boxed{
E_\rho(x)
=
x^{\rho-1}
\int_0^\infty
\frac{e^{-(1-\rho)s}}{u+s}\,ds.
}
\tag{23}
\]

This identity is useful because it exposes the complete inverse-`u` hierarchy without losing the phase or inventing an independent remainder.

## 3. The Mertens kernel has a uniform all-orders expansion

For fixed `K`, expand

\[
\frac{u}{u+s}
=
\sum_{k=0}^{K}(-1)^k\frac{s^k}{u^k}
+R_K(s,u),
\tag{24}
\]

where

\[
R_K(s,u)
=(-1)^{K+1}
\frac{(s/u)^{K+1}}{1+s/u}.
\tag{25}
\]

The moments are exact:

\[
\int_0^\infty e^{-(1-\rho)s}s^k\,ds
=
\frac{k!}{(1-\rho)^{k+1}}.
\tag{26}
\]

The infinite edge face causes no uniformity problem. Integrating the remainder once by parts, using `Re(1-rho)=c`, gives

\[
\left|
\int_0^\infty e^{-(1-\rho)s}R_K(s,u)\,ds
\right|
\ll_{c,K}
\frac1{u^{K+1}(1+|\Im\rho|)}.
\tag{27}
\]

Equation (12) therefore makes the edge remainder absolutely summable. Summing (23)--(27) over the complete edge face gives

\[
\boxed{
x^c u E(x)
=
\sum_{k=0}^{K}
\frac{(-1)^k k!}{u^k}
\sum_{\Re\rho=\Theta}
\frac{e^{i\Im(\rho)u}}{(1-\rho)^{k+1}}
+O_K(u^{-K-1})
}
\tag{28}
\]

plus the exponentially small contribution (16), the `O(x^-1)` term in (19), and the ordinary prime-power correction already absorbed in the definition used by `RE-114`. The `k=0` inner sum is exactly `G(u)`.

Thus the reciprocal-Mertens coordinate itself has a Poincare expansion whose coefficients are successively filtered copies of the same edge spectrum.

## 4. The CA selector contributes only the leading `F` coordinate at algebraic orders

For a regular CA state, `RE-119` supplies an exact chamber parameter `Z` with

\[
Y=\Phi(Z).
\tag{29}
\]

Write `u=log Z`. Equations (15) and (29) give

\[
\delta_Z:=\frac{Z-Y}{Z}
=Z^{-c}F(u)
+O\!\left(Z^{\sigma-1}u^A\right).
\tag{30}
\]

Since `delta_Z=O(Z^-c)`,

\[
\log\frac{\log Z}{\log Y}
=
\frac{\delta_Z}{u}
+O\!\left(\frac{\delta_Z^2}{u}
+\frac{\delta_Z^2}{u^2}\right).
\tag{31}
\]

Consequently, for every fixed `M`,

\[
\boxed{
Z^c u\log\frac{\log Z}{\log Y}
=F(u)+O_M(u^{-M}).
}
\tag{32}
\]

The reason is structural: every correction beyond the term linear in `delta_Z` carries an extra factor `Z^-c=e^{-cu}`, while the non-edge source in (30) is exponentially separated by (16). Hence the selector geometry contributes no `1/u`, `1/u^2`, ... hierarchy at all.

The remaining exact height terms from `RE-119`,

\[
h(C)
=E(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y},
\tag{33}
\]

satisfy

\[
Z^c u\,\delta_\ell(Z)=O(Z^{c-1}u),
\qquad
Z^c u\,T(C)=O(Z^{c-1/2}u),
\tag{34}
\]

and are therefore also smaller than every fixed inverse power of `u`, because `c<1/2`.

Combining (28), (32), and (33)--(34) gives

\[
Z^c u\,h(C)
=
J(u)
+
\sum_{k=1}^{K}
\frac{(-1)^k k!}{u^k}J_k(u)
+O_K(u^{-K-1}).
\tag{35}
\]

## 5. Returning from the selector parameter to the actual CA phase

Equation (30) gives

\[
\log Z-\log Y=O(Z^{-c}),
\qquad
\frac YZ=1+O(Z^{-c}).
\tag{36}
\]

The edge series in (4)--(5) are uniformly convergent. Their derivatives are also uniformly controlled: for `J_0` this uses the high-strip reciprocal summability (12), while for `J_k`, `k>=1`, the coefficients have even stronger decay. Hence every fixed coefficient function in (35) is uniformly Lipschitz.

Replacing `u=log Z` by `nu=log Y`, and `Z^c u` by `Y^c nu`, therefore changes (35) by `O_M(nu^-M)` for every fixed `M`. Moreover `h(C)=O(Y^-c/nu)`, so

\[
Y^c\nu\left(e^{h(C)}-1-h(C)\right)
=O\!\left(\frac{Y^{-c}}\nu\right)
=O_M(\nu^{-M}).
\tag{37}
\]

This proves (6).

No assertion is made that the formal series in `K` converges as `K->infinity`. The factorial coefficients in (6) are exactly what one expects from a Poincare expansion. The result is only that **every fixed algebraic order is determined**.

## 6. Representation audit: no new coordinate appears at finite algebraic order

Let `mathcal L` be (8). On an edge mode `e^{i gamma u}`,

\[
\mathcal L e^{i\gamma u}
=
\frac{e^{i\gamma u}}{c-i\gamma}
=
\frac{e^{i\gamma u}}{1-\rho}.
\tag{38}
\]

`RE-114` gives

\[
J'=cJ-F,
\qquad
G=J-F=J'+\Theta J.
\tag{39}
\]

Since `G` has edge coefficient `(1-rho)^-1`, equations (38)--(39) yield

\[
\boxed{
J_k=\mathcal L^kG
=\mathcal L^k(J'+\Theta J).
}
\tag{40}
\]

Thus the vector

\[
(J_0,J_1,\ldots,J_K)
\tag{41}
\]

has no independent source coordinate beyond `J`: it is a deterministic stable-filter lift of `J`. Increasing the asymptotic order increases the ambient representation but not the primitive edge information.

This is the decisive kill test against the most immediate continuation of `RE-119`. Under edge isolation, computing the `1/nu` correction, the `1/nu^2` correction, or any other fixed inverse-phase correction cannot by itself reveal the missing arithmetic selector. The regular-CA mesh from `RE-119` is `o(nu^-A)` for every fixed `A`, so discretization is finer than every term retained in (6) as well.

## 7. Non-isolated edges leave a shrinking spectral boundary layer

The isolation hypothesis cannot simply be dropped from (6). Suppose instead that zeros with `beta<Theta` approach the edge. In the combined selector-plus-Mertens leading kernel, a zero `rho=beta+i gamma` carries the edge-normalized factor

\[
e^{-(\Theta-\beta)\nu}
\frac{e^{i\gamma\nu}}{\rho(1-\rho)}.
\tag{42}
\]

The coefficients `1/(rho(1-rho))` are absolutely summable over the zero set. Therefore, for any `A>0`, the total contribution from zeros satisfying

\[
\Theta-\beta\ge A\frac{\log\nu}{\nu}
\tag{43}
\]

is

\[
O(\nu^{-A}).
\tag{44}
\]

So an unresolved correction of size `nu^-K` can only be fed, at leading spectral order, by zeros in a horizontal layer whose width is `O_K((log nu)/nu)`. This is a source-side obstruction, not a CA-mesh obstruction.

Equation (44) is only a localization statement. It does not assert that such near-edge zeros exist, that their phases have a required sign, or that their combined coefficient is large enough to affect a Robin block maximum. Those are precisely the unresolved questions in the non-isolated branch.

## 8. Adversarial boundary and prior art

Several stronger readings are invalid.

The spectral-gap hypothesis (2) is additional and unproved. The finding does not show that a hypothetical off-critical zeta edge is isolated, and therefore does not upgrade `RE-119` unconditionally inside the finite-edge false-RH branch.

The all-orders statement is fixed-order only. It does not justify choosing `K=K(nu)`, summing the factorial Poincare series, or claiming an exponentially accurate transseries. Nor does it eliminate genuinely subedge information when the zero real parts accumulate at `Theta`.

The result concerns regular CA states, exactly as `RE-119`. It does not resolve the two-prime simultaneous-event problem, and no Four-Exponentials input is used. The higher CA layers and finite-exponent tax are harmless here only because `Theta>1/2`, making them exponentially small in the phase variable after edge normalization.

Zero-explicit formulas and inverse-log expansions for weighted prime sums are classical territory. Lamzouri's Mertens-product work and Bhattacharya--Martin--Simpson's joint weighted-prime error analysis already bound the novelty of the spectral ingredients, and the August 2026 preprint of Broadbent--Fiori--Kadiri--Ng--Wilk gives a recent exact Riemann--Guinand explicit formula for Mertens sums. No novelty is claimed for expanding the Mertens kernel itself.

The line-specific result is the splice with the **exact regular-CA selector** and the representation classification: once the finite extreme zero face is horizontally isolated, the selector contributes only `F` at algebraic phase orders, the reciprocal coordinate contributes the complete hierarchy (28), and every resulting coefficient is a stable-filter transform of the same `J`. The exponentially fine CA mesh then removes discrete placement at those orders as well.

No new external theorem is load-bearing: (19) and the fixed-strip summability are already established inside `RE-113`--`RE-114`, and the rest is the elementary kernel expansion above. `SOURCES.md` therefore requires no change.

The finite-edge frontier after `RE-120` splits cleanly. In the **isolated-edge branch**, no finite power of `1/log log C` can supply a new arithmetic selector coordinate; a contradiction must use exponentially smaller structure, a genuinely different source, or a non-algebraic effect. In the **non-isolated branch**, the first unresolved candidate is the shrinking near-edge zero layer (10), whose geometry was invisible in the edge-only `o(1)` statement of `RE-119`.