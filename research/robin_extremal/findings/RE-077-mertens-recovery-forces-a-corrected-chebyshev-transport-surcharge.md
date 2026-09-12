# RE-077 — Mertens recovery forces a corrected-Chebyshev transport surcharge

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GLOBAL-FAN-SPAN-COERCIVITY + RECIPROCAL-RESET-SURCHARGE + TWO-SOURCE-SPLICE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-075` identifies the only genuine positive reset currency for the logarithmic Mertens source: new first-layer support births. `RE-076` identifies a different coordinate that no fan packet can reset,

\[
\widehat H(C,b)
:=Z_b(C)-\vartheta(Z_b(C))+\delta_\vartheta(Z_b(C))
=Z_b(C)-\log\operatorname{rad}(C).
\]

The two statements can be spliced quantitatively. The support births needed to recover reciprocal-Mertens error create physical CA span, and the same positive-amplitude fan geometry forces a definite increase of `\widehat H` across that span. Thus **Mertens recovery is not merely unable to reset the corrected Chebyshev coordinate; it must pay an additional corrected-Chebyshev transport bill.**

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\]

and work on a sufficiently late common positive CA block from `RE-040`. There is a constant `c_J>0`, independent of the block and of the exposed states, such that for any two ordered points of the rightmost threshold fan with physical state scales

\[
Y_0<Y_1
\]

one has the **global span-coercivity law**

\[
\boxed{
\widehat H_1-\widehat H_0
\ge
c_J\int_{Y_0}^{Y_1}t^{-b_1}\log t\,dt.
}
\tag{1}
\]

This remains valid across arbitrary mixtures of first-layer and higher-layer packets, arbitrary packet cardinality, fringe changes, and intervening open threshold cells. Higher-layer event mass only strengthens the inequality.

Now let a matched `0\to0` first-layer run of the type in `RE-072` terminate at physical scale `W`, with selector `Z_R\sim W`, threshold width `w`, and reciprocal-Mertens descent

\[
B:=E_\ell(Z_L)-E_\ell(Z_R)>0.
\]

`RE-072` gives

\[
B\gg_J W^{-b_1}w.
\tag{2}
\]

Suppose a later point of the same oriented fan recovers a fixed fraction `\lambda\in(0,1]` of that descent:

\[
E_\ell(Z_*)-E_\ell(Z_R)\ge\lambda B.
\tag{3}
\]

Whenever

\[
W^{1-b_1}w\longrightarrow\infty,
\tag{4}
\]

`RE-075` forces at least

\[
F_*\gg_{J,\lambda}W^{1-b_1}w
\tag{5}
\]

new first-layer support births and therefore physical span

\[
Y_*-W
\gg_{J,\lambda}
W^{1-b_1}w\log W.
\tag{6}
\]

Combining (1) and (6) yields the new reset surcharge

\[
\boxed{
\widehat H_*-\widehat H_R
\gg_{J,\lambda}
W^{1-2b_1}w(\log W)^2.
}
\tag{7}
\]

Because `b_1<1/2`, a reset of a matched run whose threshold width is bounded below by a positive constant carries a polynomially divergent corrected-Chebyshev bill. More generally, (7) records the exact width dependence when `w` shrinks with the block.

The significance is architectural rather than a proof of RH. `RE-073` showed that a matched first-layer run itself pays a joint Chebyshev-Mertens cost. `RE-075` showed that later reciprocal recovery requires many new support primes. `RE-077` now shows that those very support births cannot be used as a cheap reset mechanism: the physical span they purchase forces additional monotone growth in the global corrected Chebyshev coordinate. A false-RH fan can still survive this bill because the exponent `1-2b_1` is below the natural off-critical prime-error exponent `\Theta`; what has disappeared is the possibility of treating reciprocal recovery and corrected standard-prime growth as independent escape channels.

## 1. Every exposed fan switch pays corrected-Chebyshev cost per unit physical span

Consider two consecutive exposed fan states `C_-<C_+` tied at a breakpoint `b\in J`. Put

\[
Y_\pm:=\log C_\pm.
\]

At the tie their adaptive amplitudes agree:

\[
A_b(C_-)=A_b(C_+)=c>0.
\tag{8}
\]

`RE-040` gives one block-independent positive amplitude floor. On every sufficiently late common block, every blockwise maximizer satisfies

\[
c\ge c_0>0.
\tag{9}
\]

Along the common-amplitude interpolation between the two tied states, `RE-076` uses

\[
a_c(t):=\frac{ct^{-b}}{1+ct^{-b}}
\tag{10}
\]

and proves

\[
\widehat H_+-\widehat H_-
=
P_{\ge2}(-,+)
+b(1-b)
\int_{Y_-}^{Y_+}a_c(t)\log t\,dt\,(1+o_J(1)),
\tag{11}
\]

where `P_{\ge2}(-,+)\ge0` is exactly the logarithmic mass of the higher-layer event occurrences in the complete physical packet.

The uniform small-height regime of `RE-040` implies, at the lower endpoint,

\[
ct^{-b}\le cY_-^{-b}=e^{h(C_-)}-1=o(1/\log Y_-)
\]

for every `t\ge Y_-`. Hence, uniformly on the tied segment and for all sufficiently late blocks,

\[
a_c(t)
\ge \frac{c_0}{2}t^{-b}
\ge \frac{c_0}{2}t^{-b_1}.
\tag{12}
\]

Also `b(1-b)` has a positive lower bound on the fixed compact interval `J`, and the uniform relative error in (11) is eventually smaller than `1/2`. Therefore

\[
\boxed{
\widehat H_+-\widehat H_-
\ge
c_J\int_{Y_-}^{Y_+}t^{-b_1}\log t\,dt
+P_{\ge2}(-,+)
}
\tag{13}
\]

for a constant `c_J>0` depending only on the fixed fan interval and the common amplitude floor.

Now sum (13) over consecutive exposed switches between two ordered fan points. The physical switch intervals tile the interval from `Y_0` to `Y_1`. Open threshold cells do not change the physical state scale but, by `RE-076`, increase `\widehat H`; every higher-layer mass is nonnegative. Dropping these extra positive terms gives (1).

Thus the corrected Chebyshev Lyapunov coordinate is not merely monotone. On the false-RH positive fan it is **coercive in physical CA distance** with density `\gg_J Y^{-b_1}\log Y`.

## 2. Reciprocal recovery buys physical span through first-layer support births

Start at the terminal state of a matched `0\to0` first-layer run. Its endpoint is fringe-free, so the first-layer support accounting of `RE-075` has no delayed prime at the starting selector.

For any later selected endpoint, let

\[
R:=\bigl(E_\ell(Z_*)-E_\ell(Z_R)\bigr)_+.
\tag{14}
\]

If `F_*` new first-layer supports have entered, `RE-075` gives

\[
R\le\frac{F_*+1}{Z_R-1}.
\tag{15}
\]

Hence

\[
F_*+1\ge R(Z_R-1).
\tag{16}
\]

Every such new support birth after the fringe-free endpoint has prime label `p>Z_R`, and each event contributes `\log p` to the physical coordinate `Y=\log C`. Therefore

\[
Y_*-W
\ge F_*\log Z_R.
\tag{17}
\]

Equations (16)--(17) are the reciprocal-source reset bill. They use the exact endpoint prime-set conservation of `RE-075`; higher-layer events cannot substitute for the missing first-layer support births.

For the fixed-fraction recovery (3), (2), `Z_R/W\to1`, and the divergence assumption (4) imply

\[
R(Z_R-1)
\ge \lambda B(Z_R-1)
\gg_{J,\lambda}W^{1-b_1}w
\longrightarrow\infty.
\tag{18}
\]

The additive `1` in (16) is therefore negligible, and (17) gives (5)--(6).

## 3. The bought span has an unavoidable second-source surcharge

Choose a constant `c_1>0` such that (6) gives

\[
Y_*-W\ge L_W,
\qquad
L_W:=c_1W^{1-b_1}w\log W.
\tag{19}
\]

Because the whole fan lies over the fixed compact threshold interval,

\[
0<w\le b_1-b_0.
\]

Since `b_1>0`,

\[
\frac{L_W}{W}
=O_J(W^{-b_1}\log W)
\longrightarrow0.
\tag{20}
\]

Thus `[W,W+L_W]` is a short relative physical interval even though it contains a polynomially large number of support births. On that interval

\[
t^{-b_1}\asymp W^{-b_1},
\qquad
\log t\asymp\log W.
\tag{21}
\]

Apply the global span law (1) and use only the first guaranteed portion `L_W` of the actual reset span:

\[
\begin{aligned}
\widehat H_*-\widehat H_R
&\ge c_J\int_W^{Y_*}t^{-b_1}\log t\,dt\\
&\ge c_J\int_W^{W+L_W}t^{-b_1}\log t\,dt\\
&\gg_{J,\lambda}W^{-b_1}\log W\,L_W\\
&\gg_{J,\lambda}W^{1-2b_1}w(\log W)^2.
\end{aligned}
\tag{22}
\]

This proves (7).

The two ledgers therefore interact in one direction:

\[
\text{Mertens recovery}
\Longrightarrow
\text{new first-layer supports}
\Longrightarrow
\text{physical CA span}
\Longrightarrow
\text{additional corrected-Chebyshev growth}.
\tag{23}
\]

The chain does not require bounded packets, a bound on the number of intermediate fan transitions, a fixed higher-layer profile, or a restriction on Egyptian/deep-layer architectures. Those mechanisms may coexist with the reset, but they cannot lower the bill because their contribution to `\widehat H` is nonnegative.

## 4. Stress tests and limits of the conclusion

The fringe-free starting condition matters only to keep the support-birth bill clean. A selected endpoint can contain at most one ordinary prime whose first-layer event has not yet fired. Starting immediately after a matched `0\to0` run removes that exceptional atom exactly. A more general starting point would carry an `O(1)` support correction and does not alter the asymptotic mechanism, but (15)--(17) are deliberately applied in the configuration already certified by `RE-075`.

The divergence assumption (4) is also explicit. Without it, (16) may force only `O(1)` support births, so one cannot absorb the additive endpoint correction into a polynomial span. This is the same boundary already present in `RE-075`, not a new hidden hypothesis.

There is no contradiction with the expected false-RH source scale. For fixed positive `w`, the reset surcharge has size

\[
W^{1-2b_1}(\log W)^2,
\]

while `b_1>1-\Theta` gives

\[
1-2b_1<2\Theta-1<\Theta.
\tag{24}
\]

Thus an off-critical Chebyshev error of order `W^{\Theta+o(1)}` can still absorb the forced increase. The result rules out a cancellation architecture; it does not supply the missing prime-source upper-capacity theorem.

Nor is monotonicity or integrality by itself sufficient. An abstract ordered event staircase with a positive amplitude floor can be designed to reproduce a span-coercive potential. The specifically arithmetic input in the splice is the first-layer support conservation of `RE-075`: **positive reciprocal recovery is forced to buy actual new prime supports**, and those supports necessarily move the genuine CA physical coordinate.

## 5. Prior-art boundary and next theorem

A directed current search checked the closest Robin/CA source combinations. Frank Vega's May 2026 preprint *An Explicit Window for Hypothetical Colossally Abundant Counterexamples to Robin's Criterion* combines CA structure with explicit Chebyshev and Mertens-product estimates to confine hypothetical counterexamples near their primorial. Mantovanelli's August 2026 prime-layer workload develops event sweeps and packet conservation, and Zimov's 2025 work studies consecutive-CA Robin-ratio changes. None of those sources, in the material located, states the adaptive implication (23) or the quantitative surcharge (7). No claim of external priority is made. The proof above uses no external theorem beyond the sources already anchored in `SOURCES.md`, so the source ledger requires no update.

The live frontier is now sharper than after `RE-076`. The reciprocal reset mechanism and the corrected Chebyshev Lyapunov coordinate are no longer separate constraints: **every substantial Mertens reset necessarily drives the monotone standard-source coordinate farther in the expensive direction.** What remains is to cap that accumulated corrected-Chebyshev growth using the genuine prime source on the same positive blocks, or to show that repeated reset cycles force a total source excursion exceeding the available off-critical envelope.