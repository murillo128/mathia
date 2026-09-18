# PL-343 — The recurrent sharp prime edge has exponentially small Haar/time density

**Evidence:** `EXACT-DERIVED + PNT + KRONECKER/HAAR MATCHED CONTROL + NEGATIVE/OBSTRUCTION`

**Status:** `RARE-RECURRENCE-SEPARATION + EDGE-WITNESS LARGE-DEVIATION + FIRST-HIT-GATE-REMAINS + NO-RH-CONSEQUENCE`

## Precise claim

`PL-341` identified PNT-adapted endpoint vectors that asymptotically attain the sharp outer prime-block edge `e^a`, and `PL-342` showed that high common modulations can recover the same Rayleigh value along a weakly-null Kronecker recurrence sequence. The recurrence is therefore enough to place the sharp edge in essential spectrum. It is, however, extremely sparse in modulation time.

Let

\[
c_a:=\frac{e^{-a}}{1-e^{-a}}
\]

and, for every outer prime power `p^k` satisfying

\[
e^a\le p^k<e^{2a},
\]

put

\[
b_{p,k}(a)
:=c_a\,\log p\,(2a-k\log p)>0.
\tag{PL343-1}
\]

For the finite set of prime coordinates underlying those outer prime powers, define the endpoint phase observable

\[
H_a(\theta)
:=\sum_p\sum_{k:\ e^a\le p^k<e^{2a}}
 b_{p,k}(a)\cos(k\theta_p),
\qquad \theta\in\mathbb T^{P_a}.
\tag{PL343-2}
\]

This is exactly the `PL-341` outer endpoint Rayleigh channel under independent prime phases. Along the actual physical modulation used by `PL-342`,

\[
\theta_p=\tau\log p\pmod{2\pi},
\]

one has

\[
H_a(\tau\log p)
=
\left\langle
M_{a\tau}u_a^+,
K_a^{\rm out}M_{a\tau}u_a^+
\right\rangle,
\tag{PL343-3}
\]

where `u_a^+=(f_a\oplus g_a)/sqrt(2)` is the normalized positive endpoint vector of `PL-342`. At zero phase,

\[
H_a(0)=e^a(1+o(1)).
\tag{PL343-4}
\]

If `mu_a` is Haar probability measure on this finite prime torus, then for every fixed `eta>0`,

\[
\boxed{
\mu_a\{|H_a|\ge \eta e^a\}
\le
2\exp\!\left[-\left(\frac{\eta^2}{8}+o(1)\right)
\frac{e^{2a}}{a}\right].
}
\tag{PL343-5}
\]

Equivalently, if

\[
d_a:=\#\{p:e^a\le p<e^{2a}\}
\sim \frac{e^{2a}}{2a},
\]

then

\[
\boxed{
\mu_a\{|H_a|\ge \eta e^a\}
\le
2\exp\!\left[-\left(\frac{\eta^2}{4}+o(1)\right)d_a\right].
}
\tag{PL343-6}
\]

Unique factorization makes the active prime logarithms rationally independent. Hence the Kronecker orbit `tau -> (tau log p)_p` is uniquely ergodic on the same torus. The level sets of the nonconstant trigonometric polynomial `H_a` have Haar measure zero, so the long-time density of edge-scale recurrence exists and equals the Haar probability. Therefore, for each sufficiently large fixed `a`,

\[
\boxed{
\lim_{T\to\infty}\frac1T
\operatorname{meas}\{0\le\tau\le T:
|H_a(\tau\log p)|\ge\eta e^a\}
\le
2\exp\!\left[-\left(\frac{\eta^2}{8}+o(1)\right)
\frac{e^{2a}}a\right].
}
\tag{PL343-7}
\]

Thus the `PL-342` mechanism has a precise two-sided interpretation: **qualitative Kronecker recurrence is strong enough to make the sharp PNT edge essential, but edge-sized recurrence in that same endpoint channel occupies exponentially small density in the number of outer prime coordinates.** This is a bulk-versus-extreme separation, not an RH mechanism.

## 1. The observable is exactly the modulated PL-341 endpoint channel

For the normalized endpoint profiles `f_a,g_a` of `PL-341`, equation (PL341-16) gives for one outer source `n=p^k`

\[
\langle g_a,S_{\log n/a}f_a\rangle
=
\frac{(2a-\log n)e^{-(2a-\log n)/2}}
{1-e^{-a}}.
\]

Multiplying by the Weil weight

\[
\frac{\Lambda(n)}{\sqrt n}
=
\log p\,e^{-a}e^{(2a-\log n)/2}
\]

cancels the exponential profile and leaves exactly `b_(p,k)(a)` in (PL343-1).

For physical modulation

\[
(M_\xi v)(x)=e^{i\xi x}v(x),
\]

`PL-342` uses

\[
M_\xi^*S_hM_\xi=e^{-i\xi h}S_h.
\]

Taking `xi=a tau` and `h=log(p^k)/a` gives the phase

\[
e^{-i\tau k\log p}.
\]

Since the positive endpoint vector uses the symmetric off-diagonal pair, its Rayleigh quotient is the real part of the cross term and hence exactly (PL343-2). At `theta=0`, summing (PL343-1) recovers equation (PL341-17), so the PNT asymptotic (PL343-4) is already established by `PL-341`.

No zero information, analytic continuation, or probabilistic model has been inserted into the operator. Haar measure below is used only as the invariant distribution of the finite-dimensional Kronecker orbit and as a matched generic phase control.

## 2. Independent prime coordinates give a sharp concentration scale

Under Haar measure the coordinates `theta_p` are independent and uniform on `[0,2pi)`. Group the contribution by underlying prime,

\[
X_{p,a}(\theta_p)
:=
\sum_{k:\ e^a\le p^k<e^{2a}}
 b_{p,k}(a)\cos(k\theta_p),
\]

so that

\[
H_a=\sum_pX_{p,a}.
\]

Every `X_(p,a)` is centered because

\[
\int_0^{2\pi}\cos(k\theta)\,d\theta=0,
\qquad k\ge1,
\]

and the variables are independent across distinct primes. Put

\[
B_{p,a}:=\sum_{k:\ e^a\le p^k<e^{2a}}b_{p,k}(a).
\tag{PL343-8}
\]

Then

\[
|X_{p,a}|\le B_{p,a}.
\]

The concentration parameter is asymptotically only linear in `a`:

\[
\boxed{
\sum_pB_{p,a}^2=4a(1+o(1)).
}
\tag{PL343-9}
\]

To see the main term, primes in the outer shell `e^a<=p<e^(2a)` contribute only the fundamental exponent `k=1`, so the PNT gives

\[
\begin{aligned}
\sum_{e^a\le p<e^{2a}}B_{p,a}^2
&=c_a^2
\sum_{e^a\le p<e^{2a}}
(\log p)^2(2a-\log p)^2\\
&\sim e^{-2a}
\int_{e^a}^{e^{2a}}
(\log x)(2a-\log x)^2\,dx.
\end{aligned}
\]

With `u=2a-log x`, the last expression is

\[
\int_0^a(2a-u)u^2e^{-u}\,du
=4a-6+O(a^3e^{-a}),
\tag{PL343-10}
\]

which gives `4a+o(a)`.

Proper prime powers are negligible in this concentration norm. If `p<=e^a` contributes an outer power with `k>=2`, then there are at most `a/log p+1` admissible exponents, every deficit `2a-k log p` is at most `a`, and `log p<a`. Hence uniformly

\[
B_{p,a}\ll a^2e^{-a}.
\]

There are at most `e^a` such underlying primes, so

\[
\sum_{p\le e^a}B_{p,a}^2
\ll a^4e^{-a}=o(1).
\tag{PL343-11}
\]

Thus (PL343-9) follows without any short-interval prime theorem or zero-free estimate beyond the ordinary PNT used for the main shell.

Hoeffding's inequality for the independent centered variables `X_(p,a) in [-B_(p,a),B_(p,a)]` now gives

\[
\mu_a\{|H_a|\ge t\}
\le
2\exp\!\left(
-\frac{t^2}{2\sum_pB_{p,a}^2}
\right).
\tag{PL343-12}
\]

Taking `t=eta e^a` and using (PL343-9) proves (PL343-5). The prime number theorem also gives

\[
d_a\sim\frac{e^{2a}}{2a},
\]

which rewrites the exponent as (PL343-6).

There is an even simpler variance check. Orthogonality of the functions `cos(k theta_p)` gives

\[
\operatorname{Var}_{\mu_a}(H_a)
=
\frac12\sum_{p,k}b_{p,k}(a)^2
=2a(1+o(1)).
\tag{PL343-13}
\]

Thus an edge value of order `e^a` is already exponentially many standard deviations away from the Haar bulk. Hoeffding upgrades that scale separation to the exponential-in-dimension tail bound above.

## 3. Kronecker unique ergodicity turns Haar rarity into actual time-density rarity

For each fixed `a`, only finitely many underlying primes occur. If integers `m_p` satisfy

\[
\sum_{p\in P_a}m_p\log p=0,
\]

then

\[
\prod_{p\in P_a}p^{m_p}=1,
\]

and unique factorization forces every `m_p=0`. Hence the frequency vector `(log p)_(p in P_a)` has no nontrivial integer relation and the continuous Kronecker flow

\[
\tau\longmapsto
(\tau\log p\bmod2\pi)_{p\in P_a}
\]

is uniquely ergodic with Haar invariant measure.

For fixed nonzero threshold `t`, the boundary

\[
\{\theta:H_a(\theta)=t\}
\]

has Haar measure zero. Indeed `H_a-t` is a nonzero real-analytic trigonometric polynomial, and a nonzero real-analytic function has a null zero set. The indicator of `{H_a>=t}` is therefore Riemann-integrable on the torus, so unique ergodicity gives

\[
\lim_{T\to\infty}\frac1T
\int_0^T
\mathbf1_{\{H_a(\tau\log p)\ge t\}}\,d\tau
=
\mu_a\{H_a\ge t\}.
\tag{PL343-14}
\]

Applying the same statement to the negative tail and then (PL343-5) yields (PL343-7).

This sharpens the interpretation of `PL-342`. That finding uses only the existence of arbitrarily large times at which all relevant prime phases recur sufficiently close to zero. Essential numerical range needs only a weakly-null sequence, so the frequency of those times is irrelevant to the Calkin conclusion. For the full completed operator, however, the same modulations pay increasing logarithmic principal energy. The rarity calculation shows that **existence and prevalence are radically different questions in exactly the witness channel that creates the essential edge.**

## 4. What this does and does not say about the archimedean gate

Suzuki's principal form, already used throughout this line, has Fourier multiplier `log|xi|+C_0`. Thus sending the physical modulation frequency `xi=a tau` to infinity eventually incurs a logarithmic energy cost. `PL-342` correctly leaves open whether this cost suppresses the recurrent bounded-prime edge in the relevant low spectral states.

Equation (PL343-7) identifies the missing quantitative datum more sharply. A Haar-generic edge event has density at most

\[
\exp\!\left[-\Theta\!\left(\frac{e^{2a}}a\right)\right].
\]

The reciprocal of this density is astronomically larger than the scale suggested by the prime edge itself. But **density is not a first-return theorem**. A set with tiny asymptotic density may still be hit unusually early by one particular Kronecker orbit. Therefore it would be invalid to infer from (PL343-7) a lower bound of reciprocal-density size for the first dangerous modulation time, and no such inference is made here.

The surviving deterministic problem is consequently a quantitative simultaneous-Diophantine one on the *specific weighted edge observable*: how early can

\[
|H_a(\tau\log p)|\asymp e^a
\]

occur as `a` grows, and what logarithmic principal energy is paid at that first occurrence? A theorem proving that every edge-scale return satisfies a sufficiently large lower bound on `|tau|` could couple the prime recurrence to the archimedean penalty. Conversely, an unexpectedly early sequence of edge-scale returns would invalidate the generic-Haar heuristic and expose genuinely arithmetic structure in the rational prime logarithms.

That is more precise than demanding simultaneous near-zero phases for **all** active primes. The weighted observable itself is the correct target: a near-maximal Rayleigh quotient only asks for enough coherence in the PNT endpoint weights to make `H_a` large. Any future Diophantine estimate should therefore be tested against this weighted condition rather than against an unnecessarily stronger full-coordinate box recurrence.

## 5. Adversarial and matched-control audit

**No first-hit bound.** The result is an asymptotic time-density theorem at each fixed `a`; unique ergodicity supplies no useful rate uniform in the growing dimension. It does not prove that a dangerous return cannot occur before a specified finite frequency.

**No full-operator probability statement.** `H_a` is the concrete endpoint modulation channel used to prove the sharp essential edge. The theorem does not assign a probability distribution to arbitrary vectors of the completed Weil operator, nor does it claim that every near-edge state is a modulation of `u_a^+`.

**No replacement of the Calkin conclusion.** Exponentially small density does not remove a point from essential numerical range. `PL-342` remains exact: existence of a weakly-null recurrent sequence is enough for the essential edge.

**Proper powers do not create hidden concentration.** They share the same prime coordinate and are therefore grouped before applying Hoeffding. Their total squared group amplitude is `o(1)` by (PL343-11); the concentration scale is produced by the exponentially many fundamental primes in the outer shell.

**The result is PNT-universal.** The amplitude calculation uses the rational-prime PNT, while the time-density identification uses rational independence of the finite log frequencies. A matched positive atomic system with the same PNT shell law and rationally independent generators has the same concentration mechanism. Therefore the exponential rarity is a generic control, not RH rigidity.

**No zero information is hidden in Haar measure.** Haar appears because it is the invariant measure of the finite Kronecker flow. The tail estimate is a finite-dimensional trigonometric probability calculation. It neither invokes nor reconstructs the explicit zero formula.

**No claim of broad novelty.** Hoeffding concentration, Kronecker unique ergodicity, and PNT partial summation are classical. A targeted literature/repository audit around localized Weil/von-Mangoldt translation blocks, prime-log Kronecker recurrence, Haar large deviations, and endpoint spectral witnesses did not locate this exact line-specific estimate. Search absence is not evidence of mathematical priority. The durable contribution is the conjunction with `PL-341`--`PL-342`: the same endpoint channel that asymptotically saturates the sharp operator edge and makes it essential has exponentially small invariant time density at edge scale.

A decisive falsification would be an error in the exact coefficient reduction (PL343-1)--(PL343-3), a concentration norm larger than order `a`, failure of rational independence of the active prime logarithms, or a positive-measure threshold level set. The displayed calculations and unique factorization exclude those possibilities.

## Consequence for `prime_lattice`

The large-aperture source picture now separates three logically different facts. `PL-341` says the raw prime block has true spectral edges `+/-e^a`; `PL-342` says those edges survive modulo compacts because qualitative prime-log recurrence can recover them on weakly-null modulations; the present result says those very edge-scale recurrences are **exponentially sparse in invariant modulation time**, at scale `exp[-Theta(e^(2a)/a)]`.

This removes a potential overinterpretation of the essential-spectrum obstruction. The Calkin edge proves that no compact completion can erase the bounded source recurrence, but it does not show that recurrent edge states occur at frequencies cheap enough for the logarithmic principal operator. A viable RH-facing mechanism must now address the missing **first-hit/discrepancy problem at growing prime dimension** on the weighted endpoint observable, or find a different low/mesoscopic coupling that bypasses this rare high-frequency channel entirely.

No new external source entry is required: the localized Weil/Suzuki framework and PNT inputs are already registered in `research/prime_lattice/SOURCES.md`, while the added concentration and Kronecker-density steps are classical exact deductions from the existing `PL-341`/`PL-342` setup.
