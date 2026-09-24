# WI-439 — Wang endpoint localization already forces the short-interval support gap

Status: `PRIMARY-SOURCE-AUDIT + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + NON-RH + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parent: `WI-354`

Clue: `CLUE-wang-weighted-dephasing-support-localization`

## Claim

The proposed coefficient-weighted dephasing route does not, by itself, relax the fixed support gap `lambda<theta` in Biao Wang's current short-interval pair-correlation proof. The same support-scale loss is already generated **before the prime-polynomial mean-square step**, when the interval-localized zero expression is replaced by the full explicit-formula object.

Let

\[
I=[T,T+H],\qquad H=T^\theta,\qquad L=\log T,
\qquad 0<\lambda<\theta<1.
\tag{1}
\]

Wang's explicit-formula object is decomposed as

\[
A(x,t)=-D_x(t)+B_x(t)+E_x(t),
\tag{2}
\]

with

\[
D_x(t)=\sum_{n\ge2}a_n n^{-it},
\qquad
a_n=\frac{\Lambda(n)}{\sqrt n}\min\!\left(\frac nx,\frac xn\right),
\tag{3}
\]

and with the displayed elementary pieces `B_x(t)=log(t+2)/x` and `E_x(t)\ll1/x`. The arithmetic/dephasing proposal targets the mean-square treatment of `D_x`.

But Wang's Lemma 2.4 first compares the interval-zero object `A_I(x,t)` with `A(x,t)` and obtains, uniformly for `1<=x<=T^lambda`,

\[
2\pi F_I(x)
=\int_I |A(x,t)|^2\,dt+O(xL^3).
\tag{4}
\]

The proof itself gives on `I`

\[
|A(x,t)|+|A_I(x,t)|\ll \sqrt{x}\,L
\tag{5}
\]

and

\[
|A(x,t)-A_I(x,t)|
\ll \sqrt{x}\,L
\left(
\frac1{1+t-T}+\frac1{1+T+H-t}
\right).
\tag{6}
\]

Therefore, without invoking any mean-square estimate for `D_x`,

\[
\begin{aligned}
\int_I\bigl||A_I|^2-|A|^2\bigr|\,dt
&\le
\int_I (|A_I|+|A|)|A_I-A|\,dt\\
&\ll xL^2
\int_0^H
\left(\frac1{1+u}+\frac1{1+H-u}\right)du\\
&\ll xL^2\log(H+1)
=O(xL^3).
\end{aligned}
\tag{7}
\]

The exterior tail in the same localization comparison is only `O(xL^2)`, so (7) is already the dominant support-sensitive loss at this interface.

Now insert the Fourier-scale substitution `x=T^alpha` used in the pair-correlation argument. Integrating (7) over a fixed test-function support `0<=alpha<=lambda` gives

\[
\int_0^\lambda O(T^\alpha L^3)\,d\alpha
=O\!\left(L^3\frac{T^\lambda-1}{\log T}\right)
=O(T^\lambda L^2).
\tag{8}
\]

This reproduces the support-dependent term in Wang's Theorem 2.2 independently of the subsequent prime-polynomial estimate. Relative to the `HL` main scale,

\[
\frac{T^\lambda L^2}{HL}
=T^{\lambda-\theta}L.
\tag{9}
\]

Hence Wang's present proof architecture still needs a strict fixed `lambda<theta` even if the `D_x` mean square were evaluated perfectly.

## Consequence for the proposed route

The clue `CLUE-wang-weighted-dephasing-support-localization` asked whether preserving coefficient-weighted ratio geometry in the finite-height treatment of `D_x` could remove the `T^lambda L^2` loss that forces the support gap. Equation (7) answers the decisive test negatively: **prime-side dephasing is not the unique load-bearing source of that loss**.

Accordingly, any improvement confined to the signed prime polynomial `D_x` leaves (8) unchanged and cannot, by itself, enlarge the admissible fixed Fourier support beyond the current `lambda<theta` interface. This kills the clue in its proposed form.

The obstruction is narrower than a theorem-level support barrier. It does **not** show that short-interval pair correlation is intrinsically restricted to `lambda<theta`, nor that coefficient-weighted dephasing information is useless in a reorganized proof. It shows that a successful route must also change the zero-window localization step represented by Lemma 2.4. Plausible escape interfaces include a smoother height localization, cancellation in `A-A_I` rather than the absolute-value estimate (7), or a coupled localization/arithmetic argument performed before squaring. None of those is established here.

## Relation to WI-354

`WI-354` audited Wang's final displayed error

\[
O_g(H+T^\lambda L^2)
\tag{10}
\]

and identified the resulting support-localization barrier. It did not isolate whether the `T^lambda L^2` term was specifically an arithmetic/dephasing loss or was already forced elsewhere in the proof.

The present audit resolves that causal question. The endpoint-localization comparison alone has exactly the same `xL^3 -> T^lambda L^2` scaling. Thus the route suggested by the later coefficient-weighted finite-height analysis cannot move the support gate unless the Wang localization interface moves with it.

## Evidence and provenance

The literature-backed inputs are Wang's Theorem 2.2, the decomposition (2)--(3), and Lemma 2.4 together with the displayed bounds (5)--(6) in its proof. The derivations (7)--(9) are elementary consequences of those displayed estimates. No new zeta estimate is assumed.

Primary source: Biao Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918v1 (7 Sep 2026), already anchored in `research/weil_inertia/SOURCES.md`.

The local novelty audit checked `WI-354` and the current `weil_inertia` frontier. The aggregate support barrier was already known; the substantive new item recorded here is the proof-interface diagnosis that the same support-scale loss is independently generated at the zero-window endpoint-localization step before the `D_x` mean square. No claim of literature priority is made.

## Research disposition

This is a decisive negative for `CLUE-wang-weighted-dephasing-support-localization` as stated. Future work on Wang's short-interval support should not spend cycles improving only the finite-height dephasing estimate for `D_x`; it must first show a mechanism that simultaneously removes or beats the endpoint-localization loss in Lemma 2.4.