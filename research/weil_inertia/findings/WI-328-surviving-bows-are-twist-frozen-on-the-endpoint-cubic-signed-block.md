# WI-328 — surviving bows are twist-frozen on the endpoint cubic signed block

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`.

WI-327 moves the endpoint cubic obstruction from raw prime positivity to a genuinely signed exceptional-set problem: for density-one source starts the exact coefficient

\[
f_X(n)=\Lambda(n)-\Lambda_X^\sharp(n),
\qquad
\Lambda_X^\sharp(n)=\frac{P(R)}{\varphi(P(R))}1_{(n,P(R))=1},
\qquad
R=\exp((\log X)^{1/10}),
\]

has only a small twisted residual on the coherent block `L=\lfloor X^{1/3}/8\rfloor`, but an actual distinguished bow could still select an exceptional start. A tempting de-exceptionalization is then to use the many neighboring zero ordinates inside the bow as many nearby twists and hope that an exceptional signed resonance at one height dephases across the bow.

That route fails on the exact endpoint cubic block throughout the entire count-saturating fixed-power range left alive by WI-202. For a fixed integer start `M\in[X,3X/2]`, define

\[
S_M(U)
:=
\sum_{j=1}^{L}
 f_X(M+j)
 e\!\left(
 \frac{U}{2\pi}\log\left(1+\frac jM\right)
 \right),
\qquad
L=\left\lfloor\frac{X^{1/3}}8\right\rfloor,
\tag{1}
\]

with `e(t)=e^{2\pi i t}`. Then for every pair of heights `U,V`,

\[
\boxed{
|S_M(U)-S_M(V)|
\le
|U-V|\,\frac{L^2}{M}\,
\bigl(\log(2X)+R\bigr)
}
\tag{2}
\]

for all sufficiently large `X`. Since `R=X^{o(1)}`, if `U,V` lie in one surviving count-saturating bow of vertical span

\[
H_{\rm bow}=\frac{T^{\vartheta+o(1)}}{\log T},
\qquad
0<\vartheta\le\vartheta_*:=\frac{3943}{12011},
\tag{3}
\]

at the endpoint source scale `T\asymp X^2`, then

\[
\boxed{
\sup_{|U-V|\le H_{\rm bow}}
\frac{|S_M(U)-S_M(V)|}{L}
\le
X^{2\vartheta-2/3+o(1)}
\le
X^{-364/36033+o(1)}
=o(1).
}
\tag{4}
\]

Thus the whole surviving bow is **twist-frozen** on this source block. If for some bow ordinate `U_0` one has a macroscopic exceptional value `|S_M(U_0)|\ge\eta L` with fixed `\eta>0`, then uniformly at every other ordinate `U` in the same bow,

\[
|S_M(U)|\ge(\eta-o(1))L.
\tag{5}
\]

Conversely, an `o(L)` value at one height stays `o(L)` throughout the bow. Merely sampling or averaging the neighboring bow ordinates therefore does not turn the WI-327 exceptional start into independent twist samples.

The scale comparison is sharp enough to identify where this particular escape could first become possible. A source block of length `J` acquires order-one phase variation across a bow only when

\[
H_{\rm bow}\frac{J}{X}\gtrsim1.
\tag{6}
\]

At the largest still-live exponent `\vartheta_*`, this requires, at power scale,

\[
\boxed{
J\gtrsim X^{1-2\vartheta_*+o(1)}
=X^{4125/12011+o(1)},
}
\tag{7}
\]

whereas the endpoint coherent block of WI-327 has length `X^{1/3}`. The exact exponent gap is

\[
\frac{4125}{12011}-\frac13
=
\boxed{\frac{364}{36033}}>0.
\tag{8}
\]

So a height-dephasing attack must leave the present cubic block and control a genuinely longer source interval, or use information other than bow-internal vertical variation.

## 1. Exact Lipschitz control in the height variable

For fixed `M,j`, put

\[
C_{M,j}(U)
:=
e\!\left(
\frac{U}{2\pi}
\log\left(1+\frac jM\right)
\right)
=
\exp\!\left(iU\log\left(1+\frac jM\right)\right).
\tag{9}
\]

The elementary inequality `|e^{ia}-e^{ib}|\le|a-b|` gives

\[
|C_{M,j}(U)-C_{M,j}(V)|
\le
|U-V|\log\left(1+\frac jM\right)
\le
|U-V|\frac jM
\le
|U-V|\frac LM.
\tag{10}
\]

Therefore

\[
|S_M(U)-S_M(V)|
\le
|U-V|\frac LM
\sum_{j=1}^{L}|f_X(M+j)|.
\tag{11}
\]

No Taylor approximation, zero-density theorem, or almost-all estimate enters this step.

## 2. The signed coefficient has a deterministic subpolynomial pointwise bound

The density-one `L^1` estimate used in WI-327 cannot be invoked at an exceptional start, so the present argument uses only a deterministic bound. For `M\in[X,3X/2]` and `j\le L`, one has `M+j<2X` for large `X`, hence

\[
0\le\Lambda(M+j)\le\log(2X).
\tag{12}
\]

For the structured term,

\[
\frac{P(R)}{\varphi(P(R))}
=
\prod_{p\le R}\frac{p}{p-1}
\le
\prod_{2\le n\le\lfloor R\rfloor}\frac{n}{n-1}
=
\lfloor R\rfloor
\le R.
\tag{13}
\]

Thus, at every start including the exceptional ones,

\[
\sum_{j=1}^{L}|f_X(M+j)|
\le
L\bigl(\log(2X)+R\bigr),
\tag{14}
\]

and (11) becomes the claimed exact inequality (2). Since

\[
R=\exp((\log X)^{1/10})=X^{o(1)},
\tag{15}
\]

the coefficient norm costs no fixed power of `X`.

This deterministic replacement is important. The twist-freezing statement is valid precisely on the WI-327 exceptional starts where its density-one prime estimates supply no information.

## 3. The whole live bow is shorter than the cubic twist-coherence window

WI-184 gives a fixed-power bow with `m_T=T^{\vartheta+o(1)}` selected labels and bounded positive unfolded spacing a vertical span

\[
H_{\rm bow}=\frac{T^{\vartheta+o(1)}}{\log T}.
\tag{16}
\]

WI-202 excludes count-saturating bows for every fixed `\vartheta>3943/12011` and leaves only

\[
0<\vartheta\le\vartheta_*:=\frac{3943}{12011}.
\tag{17}
\]

The strict comparison with the cubic threshold is exact:

\[
\frac13-\vartheta_*
=
\frac{12011-3\cdot3943}{3\cdot12011}
=
\boxed{\frac{182}{36033}}>0.
\tag{18}
\]

On the endpoint family used in WI-324--WI-327, `T\asymp X^2`. Hence

\[
H_{\rm bow}X^{-2/3+o(1)}
=
T^{\vartheta-1/3+o(1)}
\le
T^{-182/36033+o(1)}
\longrightarrow0.
\tag{19}
\]

Combining (2), (15), and (19) proves (4). Notice that the endpoint `\vartheta=3943/12011` is covered here even though WI-202's packing argument does not exclude it: the fixed exponent gap to `1/3` remains positive.

Equivalently, the natural height-coherence window of an `X^{1/3}` logarithmic block is `X^{2/3}=T^{1/3+o(1)}`, while every bow not already excluded by WI-202 has smaller vertical span by a fixed power. This is the precise scale separation missing from a generic appeal to nearby zero ordinates.

## 4. Minimum source length needed for bow-height dephasing

For a general fixed-start block `1\le j\le J=o(X)`, the same calculation gives phase diameter

\[
\sup_{|U-V|\le H_{\rm bow}}
|C_{M,j}(U)-C_{M,j}(V)|
\ll
H_{\rm bow}\frac JX.
\tag{20}
\]

Thus bow-internal height variation cannot even produce order-one bare carrier motion while `J=o(X/H_{\rm bow})`. At the largest surviving exponent,

\[
\frac{X}{H_{\rm bow}}
=
X^{1-2\vartheta_*+o(1)}
=
X^{4125/12011+o(1)},
\tag{21}
\]

up to logarithmic factors absorbed in `X^{o(1)}`. Since

\[
\frac{4125}{12011}=0.343434\ldots>\frac13,
\tag{22}
\]

the current cubic block lies strictly below the first power scale at which the live bow can dephase it.

Equation (21) is not a theorem that every longer block cancels. It is only a necessary scale for this particular height-variation mechanism to become nontrivial. A future attack at `J\gtrsim X^{4125/12011}` must separately control the logarithmic carrier and the exact signed arithmetic coefficients there.

## 5. Prior-art and internal novelty audit

The surrounding Riemann--Siegel exponential-sum technology is classical. Huxley--Kolesnik, *Exponential Sums and the Riemann Zeta Function III*, Proc. London Math. Soc. 62 (1991), 449--468, studies exponential sums near square-root Dirichlet length; its 1993 corrigendum withdraws one power-sum assertion but leaves the exponential-sum theorems stated there intact. Hiary, *Fast methods to compute the Riemann zeta function*, Ann. of Math. 174 (2011), 891--946, develops quadratic and cubic exponential-sum reductions at Riemann--Siegel scale. Those papers are background for the cubic source geometry only; no result from them is load-bearing for (2)--(8), which follow from elementary phase Lipschitz control plus the already audited Mathia bow scales.

A bounded fresh literature search did not locate a theorem asserting this specific cross-scale statement: the currently surviving Maynard--Pratt bow span is uniformly shorter than the twist-coherence window of the endpoint `X^{1/3}` signed source block. That negative search is not a priority claim.

The internal audit separates this obstruction from nearby findings. WI-190 shows that an almost-all prime theorem may hide the deterministic `B`-process alias locus; WI-204 shows that a global exceptional-measure budget can absorb one bow; WI-196 shows abstractly that positivity, bandwidth, and long twist averages cannot control one distinguished center. WI-324--WI-325 construct and snap the endpoint cubic carrier resonance, while WI-327 proves that the exact signed subtraction suppresses it on density-one starts. None of those statements says that **all zero ordinates inside one surviving bow remain asymptotically the same twist on the exceptional endpoint cubic block**. Equations (2)--(8) are the new route-closing bridge.

## 6. Evidence boundary and research consequence

This is an information barrier for one concrete de-exceptionalization strategy, not a construction of an actual zeta bow and not a proof that the true distinguished start is exceptional. It fixes the source start `M` and the endpoint cubic block while varying the height `U`. The full WI-195 Gallagher norm contains many multiplicative windows, shifts, and source starts; other pieces can vary on different scales. Nor does (4) prove the macroscopic signed cancellation required by the bow or rule it out pointwise.

The result does close the implication

\[
\boxed{
\text{many zero ordinates inside a surviving bow}
\; + \;
\text{one exceptional endpoint cubic source block}
\Longrightarrow
\text{automatic dephasing / independent twist samples}.
}
\tag{23}
\]

That implication is false: on the current block, the whole bow changes the signed sum by only `o(L)`.

Accordingly `CLUE-bow-distinguished-twist-offdiagonal-cancellation` remains open, but its de-exceptionalization burden is narrower. A successful next step must use genuinely pointwise arithmetic information at the distinguished source start, couple the exceptional-start set to additional bow/source structure, exploit cross-scale information, or move to source blocks of at least the dephasing power scale (7) and prove new control there. Averaging over the neighboring bow ordinates while retaining the same endpoint cubic block cannot do the job.

No unconditional simple-critical-zero proportion changes here, and no conclusion about the existence of off-critical zeta zeros or RH follows.