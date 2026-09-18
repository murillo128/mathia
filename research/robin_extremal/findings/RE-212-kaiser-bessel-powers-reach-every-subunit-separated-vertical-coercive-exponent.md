# RE-212 — Kaiser–Bessel powers reach every subunit separated vertical coercive exponent

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + WEIGHTED-PRIMITIVE-LOWER-BOUND + KAISER-BESSEL-WINDOW + ORDINARY-PRIME-SOURCE + SELECTOR-DEBT-SCALE + CHEBYSHEV-PREFIX-COERCIVITY + KV-BARRIER + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-211.

`RE-211` showed that the compact-positive test, not the sinc family, controls the obstruction constant. The normalized Blackman window raised the certified exponent from `0.5979019...` to `0.7415820...`, leaving open whether substantially larger rates are available.

They are. A one-parameter normalized continuous Kaiser–Bessel density gives rates tending to one. For every fixed `eta>0`, the same separated continuum argument can be run with a nonnegative test supported in `[-T,T]` and yields

\[
\boxed{
\log R\ge ((1-\eta)+o(1))HT.
}
\tag{1}
\]

The arithmetic pullback of `RE-209`--`RE-211` is unchanged. Hence a separated ordinary-prime `{0,1,2}` repair hiding a selector-scale local Euler packet from `|t|<=T_Q` while preserving every fixed Korobov--Vinogradov envelope cannot have

\[
T_Q=c\log Q
\qquad\text{with}\qquad
c>\frac1{2H}.
\tag{2}
\]

For the current corridor `H=log 8`, every

\[
\boxed{c>\frac1{2\log 8}=0.2404491734\ldots}
\tag{3}
\]

is excluded. Equality is not excluded by this argument. The constructive range from `RE-208`, `c<0.0289079...`, is unchanged, so the ratio between the current constructive and coercive constants falls to `12 log 2=8.317766...`.

## 1. A normalized Kaiser–Bessel probability density

Fix `beta>0` and define

\[
w_\beta(t):=
\frac{\beta}{2\sinh\beta}
I_0\!\left(\beta\sqrt{1-t^2}\right),
\qquad |t|\le1,
\tag{4}
\]

and `w_beta(t)=0` outside `[-1,1]`. Here `I_0` is the modified Bessel function of order zero. The density is nonnegative. The standard continuous Kaiser–Bessel transform identity, which also follows directly by expanding `I_0` and integrating termwise, is

\[
\int_{-1}^{1}
I_0\!\left(\beta\sqrt{1-t^2}\right)e^{-ixt}\,dt
=
\begin{cases}
\displaystyle
2\frac{\sinh\sqrt{\beta^2-x^2}}{\sqrt{\beta^2-x^2}},& |x|<\beta,\\[1.1em]
\displaystyle
2\frac{\sin\sqrt{x^2-\beta^2}}{\sqrt{x^2-\beta^2}},& |x|>\beta,
\end{cases}
\tag{5}
\]

with the transition value interpreted continuously. At `x=0`, (5) gives

\[
\int_{-1}^{1}I_0\!\left(\beta\sqrt{1-t^2}\right)dt
=\frac{2\sinh\beta}{\beta},
\tag{6}
\]

so (4) has total mass one.

Its normalized Fourier transform is therefore

\[
\Phi_\beta(x)=
\begin{cases}
\displaystyle
\frac{\beta}{\sinh\beta}
\frac{\sinh\sqrt{\beta^2-x^2}}{\sqrt{\beta^2-x^2}},& |x|<\beta,\\[1.1em]
\displaystyle
\frac{\beta}{\sinh\beta}
\frac{\sin\sqrt{x^2-\beta^2}}{\sqrt{x^2-\beta^2}},& |x|>\beta.
\end{cases}
\tag{7}
\]

Thus the whole oscillatory tail begins already at the exact transition `|x|=beta`, and the elementary bound `|sin y/y|<=1` gives

\[
\boxed{
\sup_{|x|\ge\beta}|\Phi_\beta(x)|
\le C_\beta:=\frac{\beta}{\sinh\beta}.
}
\tag{8}
\]

The corresponding convolution-power rate is

\[
\boxed{
\gamma_\beta
:=\frac{\log(1/C_\beta)}{\beta}
=\frac{\log(\sinh\beta/\beta)}{\beta}.
}
\tag{9}
\]

Since

\[
\log(\sinh\beta/\beta)
=\beta-\log(2\beta)+o(1),
\]

we have

\[
\boxed{\gamma_\beta\longrightarrow1\quad(\beta\to\infty).}
\tag{10}
\]

For every finite `beta`, `gamma_beta<1`; the result below uses a fixed sufficiently large `beta`, not a parameter growing with `Q`.

## 2. Positive convolution powers convert the transition drop into any subunit rate

Let `nu` be the finite real signed measure supported on `[H,infinity)` from the separated spectral-gap reduction and assume

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad 0\le\epsilon<1.
\tag{11}
\]

As before, set

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|.
\tag{12}
\]

Choose a fixed `beta` and

\[
n:=\left\lfloor\frac{HT}{\beta}\right\rfloor.
\tag{13}
\]

Scale (4) to `v_n(t)=(n/T)w_beta(nt/T)`, supported on `[-T/n,T/n]`, and let `W_n=v_n^{*n}`. Then `W_n` is a nonnegative probability density supported on `[-T,T]`, with transform

\[
\phi_n(L)=\Phi_\beta(LT/n)^n.
\tag{14}
\]

Since `n<=HT/beta`, every `L>=H` has `LT/n>=beta`, so (8) applies to the entire repair support. Pairing (11) against `W_n` gives

\[
\left|\int\phi_n(L)\,d\nu(L)\right|\ge1-\epsilon.
\tag{15}
\]

The endpoint jump of the zero-extended base density is not an obstruction. On `x>beta`, write `y=sqrt(x^2-beta^2)`. Then

\[
\Phi_\beta(x)=C_\beta\frac{\sin y}{y}.
\tag{16}
\]

Although the base transform itself has only an `O(1/x)` tail, its `n`-th power has integrable value and derivative once `n>1`. More directly, changing variables from `x` to `y` gives

\[
\int_\beta^\infty |\Phi_\beta(x)|^n\,dx
\ll_\beta C_\beta^n,
\qquad
\int_\beta^\infty |(\Phi_\beta(x)^n)'|\,dx
\ll_\beta nC_\beta^n.
\tag{17}
\]

Indeed `|sinc y|<=min(1,1/|y|)` and `sinc'` is locally bounded with `O(1/y)` tail; the change of variables cancels in the total-variation integral. Returning to `L` therefore yields

\[
\int_H^\infty (|\phi_n'(L)|+|\phi_n(L)|)\,dL
\ll_{\beta,H,T/n} nC_\beta^n,
\tag{18}
\]

where for fixed `beta` and fixed `H` the suppressed prefactor contributes only `e^{o(n)}`. Integrating `dnu=e^{-L}dG` by parts as in `RE-209` gives

\[
1-\epsilon
\le
R\int_H^\infty (|\phi_n'|+|\phi_n|)\,dL,
\tag{19}
\]

and hence

\[
\boxed{
\log R\ge (\gamma_\beta+o(1))HT.
}
\tag{20}
\]

Given any fixed `eta>0`, choose `beta=beta(eta)` once so that `gamma_beta>1-eta`, then let `T` grow. This proves (1). No uniformity in a choice `beta=beta(Q)` is asserted or needed.

## 3. Ordinary-prime pullback and the limiting KV ceiling

Use exactly the arithmetic setup of `RE-209`--`RE-211`: a selector-scale local packet of

\[
B_Q\asymp\frac{\sqrt Q}{\log Q}
\]

ordinary primes near `X_0=2Q`, followed only after logarithmic gap `H` by remote ordinary-prime edits with coefficients in `{-1,+1}`. Assume `T_Q=O(log Q)` and exact Euler discrepancy `o(d_Q)` uniformly on `|t|<=T_Q`, where

\[
d_Q=\frac1{\sqrt Q\log Q}.
\]

The normalization, exact prime-power error and signed-prefix identification are unchanged. Applying (20) with fixed `beta` gives

\[
\boxed{
\sup_{x\ge X_0e^H}
\frac{|\Delta\vartheta_Q(x)|}{x}
\ge
Q^{-1/2}
\exp\left((\gamma_\beta+o(1))HT_Q\right).
}
\tag{21}
\]

For each fixed `beta`, fidelity to every fixed KV envelope therefore requires

\[
\frac{\frac12\log Q-\gamma_\beta HT_Q}{V(Q)}
\longrightarrow+\infty.
\tag{22}
\]

Now suppose `T_Q=c log Q` with `c>1/(2H)`. Choose `eta>0` small enough that `(1-eta)Hc>1/2`, then fix `beta` with `gamma_beta>1-eta`. Equation (21) is then polynomially larger than every fixed KV envelope, a contradiction. Hence

\[
\boxed{
c>\frac1{2H}\quad\text{is impossible in the separated KV architecture}.}
\tag{23}
\]

At `H=log 8`, this is (3). The boundary `c=1/(2H)` remains open: every fixed `beta` leaves a positive linear margin in (22), so taking the supremal rate after the asymptotic limit does not justify excluding equality.

## 4. Representation audit and falsification checks

The invariant carried from `RE-209` is the positive compact spectral test and its weighted signed-prefix pullback. The sinc and Blackman constants were properties of convenient coordinates in the test family, not properties of the ordinary-prime source. The Kaiser–Bessel representation makes this explicit: its exact transition at `|x|=beta` trades a main-lobe width `beta` against a uniform tail `beta/sinh beta`, and that tradeoff approaches one exponential unit per unit transition width.

Three failure modes were checked. First, the Kaiser density does not vanish at the endpoints, so the zero extension has a jump; (16)--(18) show that convolution powers restore enough Fourier-tail integrability for the integration-by-parts argument. Second, `beta` must be fixed after choosing the target rate; allowing `beta` to grow with `Q` would require a new uniform argument and is not used. Third, (10) is only a lower-bound construction for the compact-support functional

\[
\Gamma(w)=\sup_{a>0}
\frac{-\log\sup_{|x|\ge a}|\widehat w(x)|}{a}.
\tag{24}
\]

It proves `sup_w Gamma(w)>=1` in the supremal sense, but it does **not** prove equality, attainment at one, or an upper bound preventing `Gamma(w)>1` for another window.

The Kaiser/Kaiser–Bessel window and the Bessel transform in (5) are classical harmonic-analysis and signal-processing objects. Broad prior-art search covered Kaiser window design and transforms, compact-support Fourier decay, and repo-local terminology. No collision was found with the source-specific use here: positive Kaiser convolution powers are inserted into the `RE-209` signed-prefix coercive argument and then pulled back to exact ordinary-prime Euler atoms and KV source fidelity. Since the only arithmetic external input remains the already anchored PNT/KV estimate and the transform identity is explicit, `SOURCES.md` gains no new load-bearing dependency.

## Research consequence

`RE-211` left the obstruction side as an open window-optimization problem with a certified rate `0.741582...`. `RE-212` moves that frontier qualitatively: **every exponent below one is already available inside a single classical one-parameter family**. The separated continuum problem for `H=log 8` now has

\[
0<c<0.0289079\ldots
\quad\text{constructed},
\qquad
c>0.2404491734\ldots
\quad\text{excluded within the separated KV architecture}.
\]

The next obstruction-side question is no longer to find a slightly better window, but to prove an upper bound for `Gamma(w)` and decide whether the unit rate is optimal. The dual constructive target remains source-aware control of the signed weighted prefix rather than absolute coefficient variation. A result on either side would now change the actual remaining gap rather than merely improve an ad hoc window constant.
