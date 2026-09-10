# RE-034 — adaptive Robin threshold maxima force an exact standard prime-race ray

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-THRESHOLD-CA + SAME-PARAMETER-EXACT-RAY + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-027`--`RE-029` select hypothetical quantitative Robin witnesses against one fixed moving barrier `c_b x^{-b}`. That removes the block-stretch escape and forces an opposite-sign Chebyshev/Mertens cone, but the fixed barrier leaves an uncontrolled positive overshoot of the selected Robin height, so `RE-029` obtains only a lower bound for the reciprocal coordinate. The overshoot can be removed without adding an arithmetic hypothesis: **maximize the scale-invariant Robin excess itself inside each counterexample block, then use the attained excess as the tangent barrier.** The resulting same-parameter prime-race condition is an asymptotic ray, not merely a cone.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
1-\Theta<b<\frac12.
\tag{2}
\]

For a colossally abundant integer `C`, write

\[
Y:=\log C,
\qquad
h(C):=\log G(C)-\gamma,
\qquad
G(C)=\frac{\sigma(C)}{C\log\log C},
\tag{3}
\]

and define the adaptive amplitude

\[
\boxed{
A_b(C):=Y^b\bigl(e^{h(C)}-1\bigr).
}
\tag{4}
\]

Robin's quantitative false-RH theorem, already used in `RE-026`--`RE-029`, supplies a constant `c_b>0` and infinitely many CA witnesses with `A_b(C)>=c_b`. In each finite Robin-counterexample block containing such a witness, choose the **rightmost** CA state `C` maximizing `A_b` on that block, and put

\[
c:=A_b(C)\ge c_b.
\tag{5}
\]

Then an unbounded subsequence of these states is regular for the adaptive tangent. There is a unique real `Z>Y` such that

\[
\boxed{
\frac1{Z\log Z}
=
\frac1{Y\log Y}
-
\frac{bc}{Y(Y^b+c)},
}
\tag{6}
\]

and the ordinary CA event selector at `Z` chooses exactly `C`:

\[
\boxed{Y=\Phi(Z).}
\tag{7}
\]

Let

\[
D(Z):=Z-Y.
\tag{8}
\]

Because the adaptive choice makes

\[
h(C)=\log(1+cY^{-b}),
\tag{9}
\]

the tangent displacement is now tied to the **actual** Robin height:

\[
\boxed{
D(Z)=(b+o(1))h(C)\,Z\log Z.
}
\tag{10}
\]

At the same real parameters `Z`, use the standard errors from `RE-009` and `RE-029`,

\[
\mathcal E_{\vartheta}(Z)
:=\frac{\vartheta(Z)-Z}{\sqrt Z},
\tag{11}
\]

\[
E(Z):=
\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z,
\qquad
\mathcal E_{\pi_\ell}(Z):=E(Z)\sqrt Z\log Z.
\tag{12}
\]

Then the selected sequence satisfies

\[
\boxed{
\mathcal E_{\vartheta}(Z)
=-(b+o(1))h(C)\sqrt Z\log Z,
}
\tag{13}
\]

and, crucially,

\[
\boxed{
\mathcal E_{\pi_\ell}(Z)
=(1-b+o(1))h(C)\sqrt Z\log Z.
}
\tag{14}
\]

Hence both coordinates diverge in magnitude and their ratio is asymptotically fixed:

\[
\boxed{
\frac{\mathcal E_{\pi_\ell}(Z)}{-\mathcal E_{\vartheta}(Z)}
\longrightarrow\frac{1-b}{b}.
}
\tag{15}
\]

Equivalently,

\[
\boxed{
E(Z)
=\left(\frac{1-b}{b}+o(1)\right)
\frac{Z-\vartheta(Z)}{Z\log Z}.
}
\tag{16}
\]

Since `c>=c_b`, equations (9)--(10) also retain the quantitative size forced in `RE-027`:

\[
h(C)\ge(c_b+o(1))Z^{-b},
\tag{17}
\]

so

\[
-\mathcal E_{\vartheta}(Z),\ \mathcal E_{\pi_\ell}(Z)
\gg_b Z^{1/2-b}\log Z\to\infty.
\tag{18}
\]

Thus hypothetical RH failure forces infinitely many **adaptively threshold-selected CA parameters lying on one asymptotically exact opposite-sign standard prime-race ray**. The unknown fixed-barrier overshoot in `RE-029` is not intrinsic.

## 1. The adaptive amplitude has an interior CA maximizer in every quantitative block

Robin's Proposition 1 supplies infinitely many CA integers `N` with, for some fixed `c_b>0`,

\[
G(N)\ge e^\gamma(1+c_b(\log N)^{-b}).
\tag{19}
\]

Therefore `A_b(N)>=c_b`. As in `RE-027`, false RH also gives infinitely many CA values below `e^gamma`, so the positive CA values split into finite counterexample blocks and infinitely many quantitative witnesses cannot be trapped in finitely many of them.

Fix one block containing a quantitative witness and choose its rightmost maximizer `C` of (4). Put `c=A_b(C)`. For any CA state `D` in the block, with `X=log D`,

\[
A_b(D)\le c
\]

is exactly equivalent to

\[
h(D)\le\tau_{b,c}(X),
\qquad
\tau_{b,c}(x):=\log(1+cx^{-b}).
\tag{20}
\]

At `C` equality holds. At either immediate CA neighbor outside the block, `h<=0<tau_{b,c}`; inside the block the same inequality follows from maximality, and it is strict on the right because `C` was chosen rightmost. Hence `C` is a local CA maximum of

\[
\mathcal J_{b,c}(D)
:=h(D)-\tau_{b,c}(\log D),
\tag{21}
\]

with no overshoot at its maximum:

\[
\boxed{\mathcal J_{b,c}(C)=0.}
\tag{22}
\]

This is the only new variational choice. The parameter `c` is allowed to vary from block to block; the exponent `b` remains fixed.

## 2. Positive CA excess is small enough for the adaptive tangent to remain strictly concave

A possible obstruction is that the blockwise amplitude `c` need not be bounded. What matters for the local tangent geometry is only the dimensionless quantity `cY^{-b}=e^{h(C)}-1`.

Let `p=P^+(C)` be the largest prime divisor of a sufficiently large CA state with `h(C)>0`. CA exponent ordering gives `C` divisible by every prime at most `p`, hence

\[
Y\ge\vartheta(p).
\tag{23}
\]

Also

\[
\frac{\sigma(C)}C
\le\prod_{r\le p}(1-r^{-1})^{-1}.
\tag{24}
\]

The unconditional PNT remainder already anchored in `SOURCES.md`, together with partial summation, gives

\[
\sum_{r\le p}-\log(1-r^{-1})
=\gamma+\log\log p+o((\log p)^{-1}),
\tag{25}
\]

and

\[
\vartheta(p)=p+o\!\left(\frac p{\log p}\right).
\tag{26}
\]

Combining (23)--(26) with `h(C)>0` first forces `Y/p->1` and then

\[
\boxed{h(C)=o((\log Y)^{-1}).}
\tag{27}
\]

Indeed, if `Y` were multiplicatively farther from `p`, the `log log C` normalization would already consume more than the Mertens-product error available in (25).

Now put

\[
H_{b,c}(x):=\log\log x+\tau_{b,c}(x).
\tag{28}
\]

Direct differentiation gives

\[
\tau_{b,c}'(x)=-\frac{bc}{x(x^b+c)},
\qquad
\tau_{b,c}''(x)
=\frac{bc((b+1)x^b+c)}{x^2(x^b+c)^2}.
\tag{29}
\]

On an `O(log Y)` neighborhood of `Y`, equations (9) and (27) imply

\[
\frac{\tau_{b,c}''(x)}{|(\log\log x)''|}
=O\bigl(cY^{-b}\log Y\bigr)
=O\bigl((e^{h(C)}-1)\log Y\bigr)
=o(1).
\tag{30}
\]

Thus `H_{b,c}` is eventually strictly increasing and strictly concave throughout that neighborhood.

The needed `O(log Y)` CA-neighbor bound is unconditional. Alaoglu--Erdos show that a quotient of consecutive CA integers is a prime or a product of two distinct primes. The first-layer event of the next omitted prime lies within one unit of that prime (`RE-003`), while `p~Y` by the preceding paragraph. The same event-location argument as in `RE-003` therefore gives

\[
\log(C/A),\ \log(B/C)=O(\log Y)
\tag{31}
\]

for the adjacent CA states `A<C<B`. Self-tangency was not needed for this local jump estimate once `p~Y` is known.

Let `epsilon_-` and `epsilon_+` be the adjacent CA supporting slopes at `C`. The local maximum (21), strict concavity, and the rightmost tie-breaking give

\[
\boxed{
\varepsilon_+<H_{b,c}'(Y)<\varepsilon_-.
}
\tag{32}
\]

This proves regular adaptive tangency and therefore (6)--(7), exactly as the fixed-amplitude tangent argument in `RE-027`.

## 3. The tangent displacement is the actual Robin height times `b Z log Z`

Let

\[
g(x):=\frac1{x\log x}.
\tag{33}
\]

Using (9) in the derivative of the adaptive barrier gives the exact identity

\[
\boxed{
g(Y)-g(Z)=\frac{b(1-e^{-h(C)})}{Y}.}
\tag{34}
\]

By (27),

\[
\frac{g(Y)-g(Z)}{g(Y)}
=b(1-e^{-h(C)})\log Y=o(1),
\tag{35}
\]

so `Z/Y->1`. Since

\[
-g'(Y)=\frac{\log Y+1}{Y^2(\log Y)^2}
\sim\frac1{Y^2\log Y},
\tag{36}
\]

the mean-value theorem in (34), together with `1-e^{-h}=h(1+o(1))`, yields

\[
D(Z)=Z-Y=(b+o(1))h(C)Y\log Y,
\tag{37}
\]

which is (10). Equation (17) follows from `c>=c_b`, and then

\[
D(Z)\gg_b Z^{1-b}\log Z
\gg\sqrt{Z\log Z}.
\tag{38}
\]

The adaptive selector has therefore retained the super-square-root defect of `RE-027` while replacing the fixed coefficient `c_b` by the actually attained Robin height.

## 4. The event identity turns the same displacement into the Chebyshev coordinate

As in `RE-029`, first-layer event localization gives

\[
\Phi_1(Z)=\vartheta(Z)-\delta_\vartheta(Z),
\qquad
0\le\delta_\vartheta(Z)\le\log Z,
\tag{39}
\]

while the higher active layers satisfy the elementary estimate

\[
\Phi_{\ge2}(Z)=O(\sqrt{Z\log Z}).
\tag{40}
\]

Combining `Y=Phi(Z)` with (39)--(40),

\[
Z-\vartheta(Z)
=D(Z)+\Phi_{\ge2}(Z)-\delta_\vartheta(Z).
\tag{41}
\]

By (38), both correction terms are `o(D)`. Therefore

\[
\boxed{
Z-\vartheta(Z)=(b+o(1))h(C)Z\log Z,
}
\tag{42}
\]

which proves (13).

No prime-gap theorem is needed: as in `RE-029`, both the CA defect and the ordinary Chebyshev error are evaluated at the exact external event parameter `Z`.

## 5. The CA exponent tail is negligible at every adaptive false-RH threshold

To turn the reciprocal lower bound of `RE-029` into an equality, the finite exponent tail must be shown small relative to `h(C)`. At a regular CA state selected by event parameter `Z`, write

\[
C=\prod_{r}r^{a_r},
\qquad
T(C):=-\sum_{r\mid C}\log(1-r^{-(a_r+1)}).
\tag{43}
\]

Then, uniformly for such states,

\[
\boxed{T(C)=O(Z^{-1/2}).}
\tag{44}
\]

Here is an elementary proof from the exact CA layer thresholds. If `a_r=1`, the second layer is inactive. Since

\[
\lambda_{r,2}=\log\left(1+\frac1{r(r+1)}\right)\ge\frac1{4r^2},
\tag{45}
\]

inactivity of `lambda_{r,2}/log r` at `g(Z)` forces `r>\sqrt Z/3` for all sufficiently large `Z`. Hence

\[
\sum_{a_r=1}-\log(1-r^{-2})=O(Z^{-1/2}).
\tag{46}
\]

If `a_r>=2`, put `j=a_r+1>=3`. The next layer is inactive, and the exact increment from `RE-003` satisfies

\[
\lambda_{r,j}\ge\frac1{4r^j}.
\tag{47}
\]

Thus

\[
r^{-j}\ll\frac{\log r}{Z\log Z}.
\tag{48}
\]

At the same time the active second layer and the upper bound `lambda_{r,2}<=r^{-2}` imply

\[
r^2\log r<Z\log Z.
\tag{49}
\]

Summing (48) over the primes allowed by (49), and using Chebyshev's elementary `vartheta(u)=O(u)`, gives

\[
\sum_{a_r\ge2}-\log(1-r^{-(a_r+1)})
=O((Z\log Z)^{-1/2}).
\tag{50}
\]

Equations (46) and (50) prove (44). Since `b<1/2` and (17) holds,

\[
\boxed{T(C)=o(h(C)).}
\tag{51}
\]

This estimate is deterministic CA geometry; it is much weaker than controlling the prime-race source itself.

## 6. Exact Euler-product accounting forces the reciprocal coordinate onto the ray

The first-layer Euler product at event parameter `Z` differs from the ordinary product over primes `r<=Z` by at most one endpoint prime. Hence there is `delta_l(Z)>=0` with

\[
\delta_\ell(Z)=O(Z^{-1})
\tag{52}
\]

such that the exact factorization is

\[
\boxed{
h(C)
=E(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y}.}
\tag{53}
\]

The normalization displacement satisfies, by (37),

\[
\log\frac{\log Z}{\log Y}
=\int_Y^Z\frac{dt}{t\log t}
=(1+o(1))\frac{D(Z)}{Y\log Y}
=(b+o(1))h(C).
\tag{54}
\]

Equations (51)--(54) therefore give

\[
\boxed{E(Z)=(1-b+o(1))h(C),}
\tag{55}
\]

which is (14). Combining (42) and (55) proves (15)--(16).

This is the precise gain over `RE-029`. There the fixed amplitude `c_b` guaranteed only `h(C)>=tau_{b,c_b}(Y)`, so the Euler-product identity could only force `E(Z)` above the residual fraction `(1-b)c_bZ^{-b}`. Here the blockwise adaptive amplitude is defined by the attained height, making (53) an equality at the same scale and eliminating that one-sided slack.

## 7. Stress tests, prior art, and research consequence

The result remains conditional on hypothetical RH failure through Robin's quantitative theorem. It does not prove that arbitrary CA states lie on the ray, and the adaptively selected states need not be ordinary self-tangent maxima of `G`. The amplitude `c` varies between counterexample blocks and may be unbounded; equation (27) is exactly what makes this harmless for local tangent concavity.

The ray is a necessary condition, not a contradiction. `RE-030`--`RE-033` already show that finite explicit-formula packets have substantial freedom to realize opposite-sign configurations. A closing theorem must still use the arithmetic sampling imposed by the CA selector or genuinely nonuniform infinite spectral structure; merely replacing the cone by the ray does not by itself solve that problem.

There is important current neighboring prior art. Kalyabin's 25 March 2026 preprint `arXiv:2603.24548` gives an unconditional sharp relation between maximal Gronwall values at fixed greatest prime and a modified Mertens remainder, including the same deterministic `2sqrt(2)/(sqrt(p) log p)` scale familiar from the CA tax. This strongly bounds novelty claims for deterministic Mertens/Gronwall calibration and is now anchored in `SOURCES.md`. It does not use the blockwise adaptive CA tangent above or derive the false-RH same-parameter Chebyshev/Mertens ray (15).

The durable narrowing is therefore specific. Under false RH, a successful source-side exclusion may target not an arbitrary mixed-race excursion but the conjunction

\[
Y=\Phi(Z),
\qquad
h(C)>0,
\qquad
\frac{\mathcal E_{\pi_\ell}(Z)}{-\mathcal E_\vartheta(Z)}
\to\frac{1-b}{b},
\tag{56}
\]

with both coordinates diverging at least at the quantitative Robin scale. The next question is whether the CA threshold selector can hit this exact asymptotic ray infinitely often in the true, non-finitely-truncated prime spectrum.