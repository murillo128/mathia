# RE-114 — actual finite-edge zero face realizes the adaptive mixed-race ray syndetically

**Status:** `DERIVED + FINITE-ZERO-EDGE + EXTREME-FACE-MERTENS-PROJECTION + ADAPTIVE-SELECTOR-COUPLING + UNIFORM-ALMOST-PERIODICITY + SYNDETIC-RAY-COMPATIBILITY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`.

Assume RH is false with finite zero edge

\[
\frac12<\Theta:=\sup_{\zeta(\rho)=0}\Re\rho<1,
\tag{1}
\]

and assume the edge is attained by at least one nontrivial zero. `RE-113` projects the ordinary Chebyshev source onto the actual edge-zero profile

\[
F_\Theta(u)
:=
\sum_{\Re\rho=\Theta}\frac{e^{i\Im(\rho)u}}{\rho},
\tag{2}
\]

with absolute and uniform convergence, and proves

\[
x-\vartheta(x)
=x^\Theta\bigl(F_\Theta(\log x)+o(1)\bigr).
\tag{3}
\]

The reciprocal Mertens coordinate selected in `RE-034` has a matching **actual edge-face projection**. With

\[
E(x):=
\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x,
\tag{4}
\]

define

\[
\boxed{
G_\Theta(u)
:=
\sum_{\Re\rho=\Theta}
\frac{e^{i\Im(\rho)u}}{1-\rho}.
}
\tag{5}
\]

Then

\[
\boxed{
E(x)
=\frac{x^{\Theta-1}}{\log x}
\bigl(G_\Theta(\log x)+o(1)\bigr).
}
\tag{6}
\]

For every fixed adaptive exponent

\[
1-\Theta<b<\frac12,
\tag{7}
\]

`RE-034` and `RE-113` therefore lock every unbounded adaptive witness sequence to **both** edge profiles at the same logarithmic phase. Writing `Y=log C` and

\[
\lambda_Y:=h(C)Y^{1-\Theta}\log Y,
\tag{8}
\]

one has

\[
\boxed{
F_\Theta(\log Y)=b\lambda_Y+o(1),
\qquad
G_\Theta(\log Y)=(1-b)\lambda_Y+o(1).
}
\tag{9}
\]

Equivalently, the edge residual

\[
K_{\Theta,b}(u)
:=bG_\Theta(u)-(1-b)F_\Theta(u)
\tag{10}
\]

satisfies `K_(Theta,b)(log Y)=o(1)` on adaptive witnesses.

The important adversarial outcome is that this stronger two-coordinate phase condition is **not** a spectral obstruction. There exist constants `eta>0` and `L<infinity`, depending only on the actual edge face and on `b`, such that every sufficiently late interval `[U,U+L]` contains a phase `u` for which

\[
\boxed{
K_{\Theta,b}(u)=0,
\qquad
F_\Theta(u)\ge\eta,
\qquad
G_\Theta(u)\ge\eta.
}
\tag{11}
\]

Thus the exact sign-correct adaptive mixed-race ray is **syndetic in logarithmic phase for the full actual edge face**, even when that face contains infinitely many zeros. No linear-independence hypothesis on their ordinates is used.

This closes the most immediate continuation suggested by `RE-113`: adding the reciprocal-Mertens edge phase does sharpen the selector dictionary, but the joint edge spectrum itself still supplies compatible order-one ray phases with bounded logarithmic gaps. Any contradiction must use the arithmetic placement of the CA selector relative to those windows, or information beyond the leading edge face.

## 1. Partial summation projects the Mertens product onto the same edge face

Put

\[
A(x):=\vartheta(x)-x,
\qquad
f(x):=\frac1{x\log x}.
\tag{12}
\]

Split the logarithmic Mertens product as

\[
\sum_{p\le x}-\log(1-p^{-1})
=
\sum_{p\le x}\frac1p+Q(x),
\tag{13}
\]

where

\[
Q(x):=
\sum_{p\le x}\sum_{k\ge2}\frac1{k p^k}.
\tag{14}
\]

The limit `Q(infinity)` exists and

\[
Q(\infty)-Q(x)=O(x^{-1}).
\tag{15}
\]

Using `sum_(p<=x) 1/p = integral_(2^-)^x f(t) d vartheta(t)`, integration by parts, and calibrating the constant by the ordinary Mertens theorem gives the exact tail identity

\[
E(x)
=f(x)A(x)
+\int_x^\infty A(t)f'(t)\,dt
+O(x^{-1}).
\tag{16}
\]

`RE-113` supplies a global remainder `r(x)->0` with

\[
A(x)
=-x^\Theta\bigl(F_\Theta(\log x)+r(x)\bigr),
\qquad
\sup_{t\ge x}|r(t)|\to0.
\tag{17}
\]

Let

\[
c:=1-\Theta>0
\tag{18}
\]

and introduce the forward exponentially stable filter

\[
J_\Theta(u)
:=
\int_0^\infty e^{-cs}F_\Theta(u+s)\,ds.
\tag{19}
\]

Since

\[
-f'(t)
=\frac1{t^2\log t}+\frac1{t^2(\log t)^2},
\tag{20}
\]

the change of variables `t=x e^s`, `u=log x`, gives

\[
\frac{\log x}{x^{\Theta-1}}
\int_x^\infty A(t)f'(t)\,dt
=
J_\Theta(u)+o(1).
\tag{21}
\]

Indeed the factor `log x/(log x+s)` differs from `1` by an exponentially integrable `O(s/log x)`, the second term in (20) contributes `O(1/log x)`, and the global remainder in (17) contributes `o(1)` uniformly over the whole tail. Equation (16) therefore becomes

\[
E(x)
=\frac{x^{\Theta-1}}{\log x}
\bigl(J_\Theta(\log x)-F_\Theta(\log x)+o(1)\bigr).
\tag{22}
\]

The reciprocal-ordinate summability already proved in `RE-112`--`RE-113` permits termwise evaluation of (19):

\[
J_\Theta(u)
=
\sum_{\Re\rho=\Theta}
\frac{e^{i\Im(\rho)u}}{\rho(1-\rho)}.
\tag{23}
\]

Since

\[
\frac1{\rho(1-\rho)}-\frac1\rho
=\frac1{1-\rho},
\tag{24}
\]

we obtain

\[
\boxed{G_\Theta=J_\Theta-F_\Theta,}
\tag{25}
\]

and (6) follows. Both edge series are absolutely and uniformly convergent because on the fixed edge `|rho|` and `|1-rho|` are comparable with `1+|Im rho|`, whose reciprocal sum is finite by the high-strip estimate already used in `RE-113`.

The coefficients `1/(1-rho)` are classical reciprocal-prime/Mertens explicit-formula coefficients; no novelty is claimed for them. The new point here is that the finite-edge summability already available in this line upgrades them to a **uniform actual-edge projection** compatible with the `RE-113` Chebyshev projection.

## 2. The adaptive selector locks the standard and reciprocal profiles simultaneously

For an adaptive `RE-034` witness, let `Z>Y` be its exact event parameter. Then

\[
\Phi(Z)=Y,
\qquad
Z/Y\to1,
\qquad
\log Z-\log Y\to0.
\tag{26}
\]

`RE-034` proves

\[
E(Z)=(1-b+o(1))h(C),
\tag{27}
\]

while `RE-113` proves

\[
F_\Theta(\log Y)=b\lambda_Y+o(1),
\qquad
\lambda_Y=O(1).
\tag{28}
\]

Applying (6) at `Z` and multiplying by `Z^(1-Theta) log Z` gives

\[
G_\Theta(\log Z)
=(1-b)h(C)Z^{1-\Theta}\log Z+o(1)
=(1-b)\lambda_Y+o(1).
\tag{29}
\]

Absolute uniform convergence makes `G_Theta` uniformly continuous. Equation (26) therefore lets us replace `log Z` by `log Y`, yielding the second relation in (9). Consequently every adaptive witness satisfies

\[
\boxed{K_{\Theta,b}(\log Y)=o(1).}
\tag{30}
\]

This is the exact edge-face version of the standard/reciprocal ray from `RE-034`. In the fixed-constant near-minimal regime isolated by `RE-113`, `lambda_Y asy 1`, so the selector would have to hit phases where both `F_Theta` and `G_Theta` have favorable order-one amplitude.

## 3. The full infinite edge face has a stable-filter ray identity

The stable filter (19) satisfies an exact first-order relation without differentiating the Fourier series. Writing

\[
J_\Theta(u)
=e^{cu}\int_u^\infty e^{-ct}F_\Theta(t)\,dt
\tag{31}
\]

and differentiating gives

\[
\boxed{J_\Theta'(u)=cJ_\Theta(u)-F_\Theta(u).}
\tag{32}
\]

Using `G_Theta=J_Theta-F_Theta`, the adaptive ray residual becomes

\[
\begin{aligned}
K_{\Theta,b}(u)
&=bG_\Theta(u)-(1-b)F_\Theta(u)\\
&=bJ_\Theta(u)-F_\Theta(u)\\
&=J_\Theta'(u)+(b-c)J_\Theta(u).
\end{aligned}
\tag{33}
\]

Because `b>1-Theta=c`, put

\[
\mu:=b-c>0.
\tag{34}
\]

Then

\[
\boxed{
K_{\Theta,b}(u)
=e^{-\mu u}\frac d{du}
\left(e^{\mu u}J_\Theta(u)\right).
}
\tag{35}
\]

This is exactly the stable-filter mechanism that `RE-035` obtained for a **finite** rightmost zero packet, now for the actual complete edge face. The extension is possible because `RE-113` has removed the old nonuniform top-edge-tail escape: the edge Fourier series is absolutely convergent and the lower real-part contribution is already `o` of the edge scale.

## 4. Exact sign-correct ray phases are relatively dense

The functions `F_Theta`, `G_Theta`, `J_Theta`, and `K_(Theta,b)` are real uniformly almost periodic functions. This needs no external recurrence theorem as a load-bearing input. Their absolutely convergent Fourier series can be uniformly truncated; for each finite truncation the compact-torus argument of `RE-035` gives relatively dense simultaneous approximate periods, while the uniformly small tail transfers those periods to the full functions.

Since the edge is attained, `F_Theta` is nonzero. The multiplier in (23) never vanishes, so `J_Theta` is also nonzero. It has no zero-frequency term, hence its Bohr mean is zero. Therefore it takes both positive and negative values. Almost periodic recurrence of a negative value makes negative values relatively dense, so some positive connected component `(a,d)` of `J_Theta` is bounded.

On that component,

\[
e^{\mu u}J_\Theta(u)>0,
\qquad
J_\Theta(a)=J_\Theta(d)=0.
\tag{36}
\]

The derivative identity (35) implies that there are two interior points `u_-<u_+` for which

\[
K_{\Theta,b}(u_-)>0,
\qquad
K_{\Theta,b}(u_+)<0,
\tag{37}
\]

while `J_Theta` is bounded below by a fixed positive constant on the compact interval `[u_-,u_+]`.

Choose a simultaneous approximate period small enough to preserve both sign margins in (37) and half of that positive `J_Theta` margin. Such approximate periods are relatively dense. Hence every interval of some fixed length contains a translate of `[u_-,u_+]` on which `K_(Theta,b)` still has opposite endpoint signs and `J_Theta` remains uniformly positive. The intermediate value theorem supplies `u` in every such translated window with

\[
K_{\Theta,b}(u)=0,
\qquad
J_\Theta(u)\ge m>0.
\tag{38}
\]

At an exact ray zero, equations (10) and (25) solve to

\[
\boxed{
F_\Theta(u)=bJ_\Theta(u),
\qquad
G_\Theta(u)=(1-b)J_\Theta(u).
}
\tag{39}
\]

Thus both coordinates are positive and bounded below by a fixed `eta>0`. This proves (11).

The one-conjugate-pair control already saturates the mechanism: `J_Theta` is then a single sinusoid, and sign-correct exact-ray points recur periodically. The argument above shows that adding arbitrarily many actual edge zeros with absolutely summable coefficients does not restore coercivity; the finite packet obstruction of `RE-035` survives the full edge face.

## 5. Prior-art boundary and research consequence

The standard explicit-formula coefficients for reciprocal prime-counting and logarithmic Mertens-product errors are classical. Bhattacharya--Martin--Simpson, already anchored in `SOURCES.md`, give the modern joint standard/reciprocal normalization and explicit formulas on RH, while Lamzouri is prior art for the Mertens-product zero expansion and bias. Likewise, relative density of approximate periods for uniformly almost periodic functions is classical. None of those facts is claimed as new here.

The line-specific result is their combination with the off-critical finite-edge structure already established internally: `RE-113` supplies absolute high-strip summability and a uniform actual-edge projection under hypothetical finite-edge RH failure; partial summation transfers that projection to the Mertens coordinate; and the `RE-034` adaptive selector forces the two actual edge profiles onto one ray. Extending the `RE-035` finite-packet stable-filter control to this complete edge face then shows that the resulting two-coordinate condition is itself spectrally noncoercive.

No new external theorem is load-bearing, so `SOURCES.md` requires no new anchor.

The research frontier is therefore narrower than the one stated after `RE-113`. In the attained finite-edge branch, it is not enough to prove that Chebyshev and reciprocal-Mertens edge phases must align: **the actual edge spectrum has order-one sign-correct exact-ray alignments with bounded gaps in `log x` automatically.** A closing theorem must instead show that the arithmetic CA selector cannot repeatedly land in those syndetic compatibility windows, exploit a lower-order source coordinate at resolution finer than the leading edge face, or couple the recovery geometry to selector placement in a way that the edge almost-periodic model does not preserve.

If the edge is not attained, `RE-113` already excludes unbounded fixed-constant near-minimal recoveries; the present obstruction is specifically the complementary attained-edge branch.