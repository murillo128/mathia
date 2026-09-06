# ANF-066 — certified curvature convexity completes two-branch Montgomery--Taylor near-extremizer stability

**Status:** `COMPUTER-ASSISTED + EXACT-DERIVED + PROFILE-SPECIFIC + TWO-SIDED-STABILITY + NEAR-EXTREMIZER-CLASSIFICATION`. `ANF-064` proves the sharp Montgomery--Taylor five-point floor with a positive quartic remainder, while `ANF-065` shows that any near-extremizer must lose both its total height scale and the squared-height share of its smaller conjugate pair once the curvature minimum crosses the `ANF-059` threshold. The validated one-dimensional computation delegated in issue `#124` supplies exactly the missing scalar input: the curvature transform has only two global minimizers, they are nondegenerate, and in fact the whole low-curvature annulus is uniformly strictly convex. Combining that certificate with the exact height expansion closes the accepted near-extremizer clue with a two-sided stability theorem.

Let

\[
K(t):=K_{\rm MT}(t),\qquad K_0:=K(0),\qquad
k_*:=\inf_{t\in\mathbb R}K(t),
\tag{1}
\]

and retain

\[
\theta:=-\frac{K_0}{3},\qquad
\Delta:=\theta-k_*,\qquad
\varepsilon:=0.00082277.
\tag{2}
\]

The certificate below proves `Delta>0`. For a genuine two-pair geometry relabel so that `y_h>=y_l>0`, and put

\[
S:=y_h^2+y_l^2,\qquad
r:=\frac{y_l^2}{S}\in(0,1/2],\qquad
d:=t_h-t_l,
\tag{3}
\]

\[
c_*:=2\pi^2(2K_0+3k_*),\qquad
E:=\frac{H_{\rm MT}}{S}-c_*.
\tag{4}
\]

There is a unique `tau>0` such that the global minimizer set of `K` is exactly `{−tau,+tau}`. Define

\[
D^2:=\min_{\sigma,\eta\in\{-1,+1\}}
\left[(t_h-\sigma\tau)^2+(d-\eta\tau)^2\right].
\tag{5}
\]

Then, with

\[
E_0:=\min\{\pi^2\Delta,\,2\pi^4\varepsilon\}>0,
\tag{6}
\]

there are explicit profile-dependent constants `0<c_-<=c_+<infinity` such that every genuine configuration with `0<E<E_0` satisfies

\[
\boxed{
c_-\,(S+r+D^2)\le E\le c_+\,(S+r+D^2).
}
\tag{7}
\]

One valid choice is

\[
c_-:=\min\left\{2\pi^4\varepsilon,\,\pi^2\Delta,\,\frac{\pi^2}{20}\right\},
\tag{8}
\]

and

\[
\begin{aligned}
C_R&:=\cosh(4\pi)+\cosh(2\pi)-2-10\pi^2,\\
c_+&:=\max\left\{C_R,\,2\pi^2(K_0-k_*),\,8\pi^4\right\}.
\end{aligned}
\tag{9}
\]

Consequently every near-extremizing sequence has

\[
S=O(E),\qquad r=O(E),\qquad D=O(\sqrt E),
\tag{10}
\]

and the disappearing pair obeys

\[
\frac{y_l}{y_h}=O(\sqrt E).
\tag{11}
\]

Moreover the only horizontal boundary families are

\[
t_l\to0
\qquad\text{or}\qquad
t_l\to\pm2\tau,
\tag{12}
\]

and both families are actually approachable by genuine configurations. Thus the Montgomery--Taylor five-point scalar near-extremizer problem is now classified, not merely compactified.

## 1. The validated curvature certificate identifies the exact signed minimizers

The exact transform from `ANF-059` is

\[
G(t)=\frac{\cos(\pi t)-\lambda t\sin(\pi t)}{1-2\pi^2t^2},
\qquad
\lambda=\sqrt2\,\pi\cot(1/\sqrt2),
\tag{13}
\]

\[
K(t)=-\frac{(G(t)^2)''}{4\pi^2}.
\tag{14}
\]

Issue `#124` evaluated this closed form with outward-rounded Arb/FLINT arithmetic. On the entire positive `ANF-059` annulus it certifies the stronger uniform statement

\[
\boxed{K''(t)>\frac15\qquad(0.545\le t\le1.01).}
\tag{15}
\]

The rational cover inspected `717` boxes, produced `359` positive leaves and left `0` unresolved boxes. Every undecided box was reevaluated at 256 and 512 bits before subdivision; all successful leaves closed at 128 bits. The smallest lower endpoint over the complete cover was `0.20010977424681186676025390625`.

At the annulus endpoints the same validated evaluation gives

\[
K'(0.545)\in(-0.367355,-0.367354),
\qquad
K'(1.01)\in(0.256525,0.256526).
\tag{16}
\]

Since (15) makes `K'` strictly increasing, it has exactly one zero in the interval. Rational bisection followed by interval Newton isolates it in

\[
\boxed{
\tau\in
[0.7588064485352071602166,\,
 0.7588064485352071602167].
}
\tag{17}
\]

On this isolating interval,

\[
K(\tau)\in
(-0.091274161151487458117,
 -0.091274161151487458115),
\tag{18}
\]

and

\[
K''(\tau)\in
(1.6659855066870620284,
 1.6659855066870620286).
\tag{19}
\]

The rational witness `t=3/4` is also certified below the exterior threshold `-K_0/3`. Combining that fact with the `ANF-059` implication

\[
|t|\le0.545\ \text{or}\ |t|\ge1.01
\Longrightarrow K(t)>-\frac{K_0}{3},
\tag{20}
\]

strict convexity on the annulus, and evenness of `K`, proves

\[
\boxed{\operatorname*{argmin}_{\mathbb R}K=\{-\tau,+\tau\}.}
\tag{21}
\]

Using the upper endpoint for `K_0` from `ANF-059` and the upper endpoint for `k_*` in (18) gives the certified quantitative crossing

\[
\boxed{\Delta>0.0396079636044282.}
\tag{22}
\]

The integral implementation in issue `#124` agrees with the differentiated closed form to high precision at ordinary control points, but that agreement is not used as proof; the decisive statements (15)--(22) are the interval certificate.

## 2. The exact normalized excess separates curvature from higher height orders

Set

\[
g(t):=K(t)-k_*\ge0.
\tag{23}
\]

`ANF-065` reconstructs the `n=1` term of the exact `ANF-064` height expansion after normalizing by `S`:

\[
Q:=(1-r)g(t_h)+r g(t_l)+2g(d),
\tag{24}
\]

and the full normalized excess has the exact decomposition

\[
\boxed{E=2\pi^2Q+R,\qquad R\ge2\pi^4\varepsilon S.}
\tag{25}
\]

Every coefficient contributing to `R` is positive by `ANF-063`--`ANF-064`. In particular, `ANF-065` already gives the global linked lower bound

\[
\boxed{E\ge2\pi^2\Delta r+2\pi^4\varepsilon S.}
\tag{26}
\]

The new curvature certificate makes its previously conditional pair-disappearance term unconditional for the fixed Montgomery--Taylor profile.

There is also a simple uniform upper bound for the higher-order remainder. Normalize the height shape by `f_h^2+f_l^2=1` and write the common scale as `sqrt(S)`. For order `n>=2`, the original bracket in `ANF-064` is bounded in absolute value by

\[
(2c_n+1)M_n(0)\le4^n+1,
\qquad c_n=2^{2n-1},
\tag{27}
\]

because `J_MT>=0`, `|alpha|<=1`, `int J_MT=1`, `A_n<=1`, and `B_n<=c_nA_n`. Hence, whenever `S<=1`,

\[
0\le R
\le S\sum_{n=2}^{\infty}
\frac{(2\pi)^{2n}}{(2n)!}(4^n+1)
=C_RS.
\tag{28}
\]

This upper estimate is deliberately crude but completely uniform in all horizontal variables.

## 3. Small excess forces both high-weight arguments into the convex annulus

From (25) and `r<=1/2`,

\[
g(t_h)\le\frac{E}{\pi^2},
\qquad
g(d)\le\frac{E}{4\pi^2}.
\tag{29}
\]

Outside the signed annulus

\[
W:=(-1.01,-0.545)\cup(0.545,1.01),
\tag{30}
\]

`ANF-059` and (22) give `g(t)>Delta`. Therefore `E<pi^2 Delta` forces both `t_h` and `d` into `W`.

By evenness, (15) holds on both components of `W`. Since `K'(+-tau)=0`, integrating the curvature lower bound from the appropriate signed minimizer gives

\[
\boxed{
g(t)\ge\frac1{10}\operatorname{dist}(t,\{-\tau,+\tau\})^2
\qquad(t\in W).}
\tag{31}
\]

Using `1-r>=1/2` in (25) therefore yields

\[
E\ge
2\pi^4\varepsilon S
+\frac{\pi^2}{10}\operatorname{dist}(t_h,\{\pm\tau\})^2
+\frac{2\pi^2}{5}\operatorname{dist}(d,\{\pm\tau\})^2.
\tag{32}
\]

At the same time (26) gives the independent `r` control. Since a number dominating two lower bounds dominates their average, (26) and (32) imply

\[
E\ge
2\pi^4\varepsilon S
+\pi^2\Delta r
+\frac{\pi^2}{20}\operatorname{dist}(t_h,\{\pm\tau\})^2
+\frac{\pi^2}{5}\operatorname{dist}(d,\{\pm\tau\})^2.
\tag{33}
\]

This proves the lower half of (7) with (8).

## 4. A uniform Taylor bound gives the reverse inequality

The Fourier representation gives globally

\[
|K''(t)|
\le4\pi^2\int_{-1}^{1}\alpha^4J_{\rm MT}(\alpha)\,d\alpha
\le4\pi^2.
\tag{34}
\]

Taylor's theorem at either exact minimizer therefore yields

\[
0\le g(t)
\le2\pi^2\operatorname{dist}(t,\{-\tau,+\tau\})^2.
\tag{35}
\]

Also `K(t)<=K_0` pointwise, so

\[
g(t_l)\le K_0-k_*.
\tag{36}
\]

Substitution into (24) gives

\[
2\pi^2Q
\le
4\pi^4\operatorname{dist}(t_h,\{\pm\tau\})^2
+2\pi^2(K_0-k_*)r
+8\pi^4\operatorname{dist}(d,\{\pm\tau\})^2.
\tag{37}
\]

If `E<E_0`, equation (26) implies `S<1`, so (28) applies. Combining (28) and (37) proves the upper half of (7) with the explicit choice (9). No local analytic expansion in the horizontal variables is required for the upper estimate.

## 5. Exactly two boundary families remain, and both are realized

Because the minimization in (5) separates in the two horizontal variables, (7) implies that every sequence with `E->0` admits signs `sigma,eta` for which

\[
t_h-\sigma\tau=O(\sqrt E),
\qquad
d-\eta\tau=O(\sqrt E).
\tag{38}
\]

Since `t_l=t_h-d`,

\[
t_l-(\sigma-\eta)\tau=O(\sqrt E).
\tag{39}
\]

If `sigma=eta`, the limit is `t_l=0`; if `sigma=-eta`, it is `t_l=+-2tau`. There is no third branch.

Both types occur as genuine near-extremizing families. Fix any signs and set exactly

\[
t_h=\sigma\tau,\qquad d=\eta\tau,
\qquad t_l=(\sigma-\eta)\tau,
\tag{40}
\]

while taking any positive `S->0` and `r->0` with `r<=1/2`. The uniform upper estimate gives `E=O(S+r)`, hence `E->0`. Thus neither the `0` branch nor the `+-2tau` branch is an artifact of subsequence extraction.

The exponents in (10) are also the natural sharp ones for this local law. Along an exact horizontal branch with `r=o(S)`, (7) gives `E=Theta(S)`; with `S=o(r)`, it gives `E=Theta(r)`. If instead `S,r=o(delta^2)` and one high-weight horizontal argument is displaced by `delta`, then `E=Theta(delta^2)`. Hence linear control of the squared-height variables and square-root control of horizontal displacement cannot be improved in exponent within this five-point profile.

## 6. Prior art and evidence boundary

A fresh literature check covered the classical Carneiro--Chandee--Littmann--Milinovich Hilbert-space extremal theorem, the current Lamzouri pair-correlation/Hilbert-space proof dated 2 September 2026, and the semidefinite pair-correlation enlargement of Chirre--Goncalves--de Laat. Those works control pair-correlation extremal constants or enlarge the admissible test-function class; none supplies a classification of the global minimizers of the exact curvature transform (14), a disappearing-pair estimate tied to the additive relation `d=t_h-t_l`, or a two-branch near-extremizer stability theorem of the form (7). All of those literature anchors are already present in `SOURCES.md`, and no external theorem is load-bearing for the proof above, so no source-file change is required.

The theorem is computer-assisted only at the scalar curvature gate: (15)--(22) depend on the validated Arb/FLINT certificate returned by issue `#124`. The passage from that certificate to the two-sided law (7), including the remainder upper bound, the additive pair-disappearance splice, and the branch classification, is exact analytic derivation from canonical local findings. Ordinary floating-point optimization of `K` would not justify the result.

This finding remains confined to the fixed Montgomery--Taylor **five-point** two-pair defect. It does not transfer the stability law to another spectrum or to larger conjugation-invariant multisets, does not strengthen the pair-correlation theorem itself, and does not imply RH. Its durable consequence for `analytic_frontier` is instead a closure statement: positivity, sharp radial coercivity, and now the complete scalar near-extremizer geometry are all settled at cardinality five. Any further progress must change the information carrier, the source category, or the configuration size rather than refine this same scalar five-point problem.