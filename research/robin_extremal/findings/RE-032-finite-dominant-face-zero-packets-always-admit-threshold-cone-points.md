# RE-032 — finite dominant-face zero packets always admit threshold-cone points

**Status:** `EXACT-DERIVED + FINITE-DOMINANT-FACE-SPECTRAL-CONTROL + NEGATIVE/OBSTRUCTION + MULTI-FREQUENCY-CONE-COMPATIBILITY + PRIOR-ART-ALIGNED`. `RE-029` forces a hypothetical threshold-tangent Robin sequence into a same-parameter cone where the standard Chebyshev error is negative at the threshold scale while the reciprocal logarithmic Mertens-product error is positive. `RE-030` shows that one off-critical conjugate zero pair can realize that cone near one of its Chebyshev zero crossings. The one-pair phenomenon is not special: **every nonzero finite packet of modes on one off-critical vertical line has infinitely many points realizing the same threshold-scale negative standard error while the reciprocal error remains positive at the packet's full power scale.**

Fix

\[
\frac12<\beta<1,
\qquad
\rho_j=\beta+i\gamma_j,
\qquad
\gamma_j>0,
\qquad
1\le j\le m,
\tag{1}
\]

with finitely many distinct ordinates, and positive integer multiplicities `nu_j`. Put

\[
a:=\beta-\frac12,
\qquad
c:=1-\beta>0.
\tag{2}
\]

After factoring out the common power `x^a`, define the standard and reciprocal packet profiles on logarithmic phase `u=log x` by

\[
S(u):=-2\Re\sum_{j=1}^m
\frac{\nu_j e^{i\gamma_j u}}{\rho_j},
\tag{3}
\]

\[
R(u):=-2\Re\sum_{j=1}^m
\frac{\nu_j e^{i\gamma_j u}}{\rho_j-1}.
\tag{4}
\]

These are exactly the finite-packet analogues of the two leading modes in `RE-030`. Assume only that the packet is nonzero, equivalently `S` is not identically zero. Then there exists a constant `eta>0` with the following property:

> For every `A>0` and every `delta>0`, there is an unbounded sequence `u_k` such that
> \[
> S(u_k)=-A u_k e^{-\delta u_k},
> \tag{5}
> \]
> while
> \[
> R(u_k)\ge\eta.
> \tag{6}
> \]

The constant `eta` depends on the packet but **not** on `A` or `delta`.

Consequently, if

\[
1-\beta<b<\frac12,
\qquad
\delta:=\beta+b-1>0,
\qquad
A:=b c_b,
\tag{7}
\]

where `c_b>0` is the quantitative Robin constant used in `RE-027`--`RE-029`, and `x_k=e^{u_k}`, then

\[
\boxed{
x_k^aS(\log x_k)
=-b c_b\,x_k^{1/2-b}\log x_k,
}
\tag{8}
\]

while

\[
\boxed{
x_k^aR(\log x_k)
\ge\eta x_k^{\beta-1/2}>0.
}
\tag{9}
\]

Since `delta=beta+b-1`,

\[
\boxed{
\frac{x_k^aR(\log x_k)}
{(1-b)c_b\,x_k^{1/2-b}\log x_k}
\longrightarrow+\infty.
}
\tag{10}
\]

Thus the finite same-real-part packet lies arbitrarily deep inside the reciprocal-positive side of the `RE-029` cone at infinitely many points where its standard component has **exactly** the threshold-required magnitude. Multi-frequency interference among finitely many dominant modes therefore cannot, by coefficient geometry or sign incompatibility alone, exclude the threshold race cone.

## 1. The reciprocal packet is an exact stable-filter transform of the standard packet

Define

\[
J(u):=\int_0^\infty e^{-cs}S(u+s)\,ds.
\tag{11}
\]

The integral is absolutely convergent because `S` is bounded and `c>0`. For one frequency,

\[
\int_0^\infty e^{-cs}e^{i\gamma_j(u+s)}\,ds
=
\frac{e^{i\gamma_j u}}{c-i\gamma_j}.
\tag{12}
\]

Since

\[
c-i\gamma_j=1-\rho_j,
\tag{13}
\]

one has the exact coefficient identity

\[
\frac1{\rho_j}
\left(1-\frac1{1-\rho_j}\right)
=
\frac1{\rho_j-1}.
\tag{14}
\]

Summing the finite packet gives

\[
\boxed{R(u)=S(u)-J(u).}
\tag{15}
\]

Differentiating (11), or directly differentiating its finite Fourier expansion, also gives

\[
\boxed{J'(u)=cJ(u)-S(u),}
\tag{16}
\]

or equivalently

\[
\bigl(e^{-cu}J(u)\bigr)'
=-e^{-cu}S(u).
\tag{17}
\]

Equation (15) is the packet-level version of the `rho -> rho-1` coefficient rotation derived in `RE-030`. It is useful here because it turns the sign question at a zero of the standard packet into a one-dimensional stable-filter question: when `S(u_0)=0`,

\[
R(u_0)=-J(u_0).
\tag{18}
\]

No linear independence of the ordinates is used.

## 2. Some standard downcrossing must have strictly positive reciprocal value

Because `S` is a nonzero finite real trigonometric sum with no zero-frequency term, its Cesaro mean is zero. It cannot be eventually of one sign: if, for example, it were eventually nonnegative, boundedness would give `S^2<=M S` on a half-line for some `M`, while the Cesaro mean of `S` is zero and the mean square of a nonzero finite trigonometric sum is strictly positive. The same argument applies to eventual nonpositivity. Hence `S` has infinitely many sign changes in both directions.

Call `u_0` a **downcrossing** when `S` is positive immediately to its left and negative immediately to its right. Tangential zeros that do not change sign are irrelevant. Since a nonzero finite exponential sum is real analytic, its zeros are isolated apart from the excluded identically-zero case.

Suppose, for contradiction, that

\[
J(u_0)\ge0
\tag{19}
\]

at every downcrossing. Start at one such `u_0`. On the following negative-sign interval of `S`, equation (17) says that `e^{-cu}J(u)` is nondecreasing, so `J` remains nonnegative until the next upcrossing. On the following positive-sign interval, `e^{-cu}J(u)` is nonincreasing. If it ever became negative there, it could not return to a nonnegative value at the next downcrossing, contradicting (19). Repeating across successive sign intervals yields

\[
J(u)\ge0
\qquad (u\ge u_0).
\tag{20}
\]

But `J` is itself a finite trigonometric sum with the same nonzero frequencies as `S`, and its Fourier multipliers `(c-i gamma_j)^(-1)` never vanish. Thus `J` is nonzero, has Cesaro mean zero, and has strictly positive mean square. If `M_J=sup|J|`, (20) gives on the half-line

\[
0\le J(u)^2\le M_JJ(u).
\tag{21}
\]

Taking Cesaro means forces the mean square of `J` to be zero, a contradiction. Therefore at least one downcrossing satisfies

\[
\boxed{J(u_*)<0.}
\tag{22}
\]

By (18),

\[
\boxed{R(u_*)>0.}
\tag{23}
\]

This is the multi-frequency replacement for the explicit branch calculation in `RE-030`. For one zero pair, every downcrossing of the appropriate parity has the required reciprocal sign. For a packet, individual crossings may have either sign, but **at least one reciprocal-positive downcrossing is forced by the stable-filter relation and zero-mean geometry.**

## 3. Finite-frequency recurrence produces infinitely many robust positive-reciprocal crossing windows

Choose a small interval

\[
I=[u_*-r,u_*+r]
\tag{24}
\]

and constants `m_0,eta_0>0` such that

\[
S(u_*-r)>m_0,
\qquad
S(u_*+r)<-m_0,
\tag{25}
\]

and, by continuity of `R`,

\[
R(u)>2\eta_0
\qquad (u\in I).
\tag{26}
\]

A finite trigonometric sum has arbitrarily large uniform approximate periods. Concretely, simultaneous Diophantine approximation gives a sequence `tau_k -> infinity` for which

\[
\max_{1\le j\le m}
|e^{i\gamma_j\tau_k}-1|\longrightarrow0.
\tag{27}
\]

Because `S` and `R` use the same finite frequency set, (27) implies uniformly in `u`

\[
S(u+\tau_k)-S(u)\to0,
\qquad
R(u+\tau_k)-R(u)\to0.
\tag{28}
\]

For all sufficiently large `k`, therefore,

\[
S(u_*-r+\tau_k)>\frac{m_0}{2},
\qquad
S(u_*+r+\tau_k)<-\frac{m_0}{2},
\tag{29}
\]

and

\[
R(u)>\eta_0
\qquad (u\in I+\tau_k).
\tag{30}
\]

This recurrence requires neither periodicity nor LI. Rational relations among the ordinates merely turn some approximate recurrences into exact ones.

## 4. Every exponentially shrinking negative target is hit inside those windows

Fix arbitrary `A>0` and `delta>0` and define

\[
q(u):=Aue^{-\delta u}.
\tag{31}
\]

Then `q(u)>0` for large positive `u` and `q(u)->0`. For sufficiently large recurrent windows `I+tau_k`, one has

\[
0<q(u)<\frac{m_0}{4}
\qquad (u\in I+\tau_k).
\tag{32}
\]

At the left endpoint of such a window,

\[
S(u)+q(u)>0,
\tag{33}
\]

whereas at the right endpoint

\[
S(u)+q(u)<0.
\tag{34}
\]

The intermediate value theorem therefore supplies `u_k in I+tau_k` with

\[
S(u_k)=-q(u_k)=-Au_ke^{-\delta u_k}.
\tag{35}
\]

At the same point, (30) gives

\[
R(u_k)\ge\eta_0.
\tag{36}
\]

Since the recurrent shifts are unbounded, so is `u_k`. Equations (35)--(36) prove (5)--(6), with `eta=eta_0`.

This step is stronger than locating zeros of the standard packet. It says that the packet repeatedly realizes **any prescribed exponentially shrinking negative level of the form relevant after factoring out an off-critical power**, while the reciprocal profile stays uniformly positive.

## 5. Matching the exact `RE-029` threshold scale

For the normalized standard Chebyshev packet and reciprocal logarithmic Mertens packet, restore the common off-critical amplitude by writing

\[
\Theta_\Gamma(x):=x^aS(\log x),
\qquad
L_\Gamma(x):=x^aR(\log x).
\tag{37}
\]

Choose `b` as in (7). Then

\[
d:=\frac12-b,
\qquad
\delta=a-d=\beta+b-1>0.
\tag{38}
\]

Putting `A=b c_b` into (35) and setting `x_k=e^{u_k}` gives

\[
\Theta_\Gamma(x_k)
=-b c_b\,x_k^{a-\delta}\log x_k
=-b c_b\,x_k^d\log x_k,
\tag{39}
\]

which is exactly the Chebyshev scale and sign forced by `RE-029`. Meanwhile

\[
L_\Gamma(x_k)\ge\eta x_k^a.
\tag{40}
\]

Because `a-d=delta>0`,

\[
\frac{L_\Gamma(x_k)}{x_k^d\log x_k}
\ge
\eta\frac{x_k^\delta}{\log x_k}
\longrightarrow+\infty.
\tag{41}
\]

Thus a finite packet not only meets the lower slope `(1-b)/b` of the `RE-029` cone; along the constructed points its reciprocal coordinate exceeds the required threshold scale by an unbounded factor.

This extends the negative lesson of `RE-030`: the reciprocal-positive side of the cone is not a fragile accident of one sinusoid. It survives arbitrary finite interference among modes sharing the same off-critical exponent `beta`, without LI, generic phases, or a simple-zero-crossing hypothesis.

## 6. Stress tests and exact boundary of the result

The result is a **spectral control**, not an admissible prime sequence and not a theorem about the actual zeta error functions along CA event parameters. The constructed `x_k` are points supplied by the finite packet; there is no claim that the threshold-tangent CA selector of `RE-027` hits them. This distinction remains the central unresolved arithmetic problem.

The common-real-part hypothesis is load-bearing. A finite packet on one vertical line has one common amplitude `x^a`, allowing the coefficient relation to become the stable filter (15) with a single decay rate `c=1-beta`. Modes on different real parts do not obey that one-kernel identity after a common normalization. A lower-real-part packet may be negligible at the full dominant scale while still being non-negligible at the much smaller threshold scale `x^d log x`; discarding it requires an explicit remainder estimate, not merely a spectral gap in words.

Likewise, the theorem does not cover an infinite dominant face, accumulation of real parts toward `Theta`, or the actual explicit-formula tail. Passing from a finite packet to an infinite zero sum requires convergence and remainder control at the threshold resolution. `RE-031` already shows that such remainder accuracy is precisely where local CA-spacing arguments become expensive.

Multiplicity causes no problem: repeated zeros simply give positive integer weights `nu_j`. Distinct equal ordinates can be combined before applying the argument. The excluded case `S identically 0` cannot occur for a genuine nonempty collection of distinct frequencies with their zeta coefficients, but it is stated explicitly so that the theorem is an elementary packet statement rather than an implicit appeal to zero simplicity.

No claim is made that every downcrossing has `R>0`; finite interference can change the reciprocal sign at individual crossings. The theorem is existential plus recurrent: one reciprocal-positive downcrossing must exist, and finite-frequency recurrence replicates a robust neighborhood often enough to hit the shrinking threshold levels.

## 7. Prior art and research consequence

The coefficient pair `1/rho` versus `1/(rho-1)` and the strong but imperfect correlation between standard and reciprocal weighted prime errors are already explicit in Bhattacharya--Martin--Simpson and are recorded in `SOURCES.md`. `RE-030` also derives the reciprocal coefficient directly from the exact line-local Mertens tail transform. No novelty is claimed for finite trigonometric sums, simultaneous recurrence, exponential convolution, or the coefficient rotation itself.

A targeted search of the joint weighted-prime-error literature and Robin/CA phase literature did not identify the specific finite-packet statement proved here: the stable-filter sign argument forcing a reciprocal-positive standard downcrossing, followed by recurrent realization of every exponentially shrinking negative threshold level. The Mathia delta is therefore deliberately narrow and source-conditioned: **finite multi-zero interference on a common off-critical face cannot supply a coefficient-level obstruction to the `RE-029` threshold cone.** No new load-bearing external theorem is introduced, so `SOURCES.md` does not require expansion.

This closes one continuation left open by `RE-030`--`RE-031`. Replacing one-zero dominance by an arbitrary finite same-`beta` dominant packet does not make the required opposite-sign cone spectrally impossible. Any successful contradiction must use information absent from this control: the arithmetic placement of the threshold-tangent CA selector relative to the recurrent packet windows, a threshold-scale remainder theorem strong enough to couple the full explicit formula to a finite dominant face, or genuinely infinite-spectrum structure that cannot be reduced to such a packet. Host sparsity and event depth may still matter, but only through that selector coupling; they do not become coercive merely by allowing finitely many dominant zero frequencies.
