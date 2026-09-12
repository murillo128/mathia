# RE-061 — finite fan-switch packets obey an Egyptian-fraction residual-charge law

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + ADAPTIVE-FAN-SWITCH + FINITE-EVENT-PACKET + HIGHER-LAYER-CHARGE-COMPOSITION + EGYPTIAN-FRACTION-RESONANCE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-060` isolates a noncancelling source-bearing residual charge when one adjacent adaptive fan switch crosses one fixed higher-layer CA event. The first unresolved composition question is whether several such events can cancel when a fan breakpoint skips physical CA states. For every asymptotically fixed finite event packet, the answer has an exact leading form: **higher-layer charges add only through the reciprocal depths `1/j`, while all first-layer events disappear from the interior and only the two endpoint fringe bits remain.** Leading cancellation is possible only on an Egyptian-fraction resonance.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

and fix a compact interval

\[
J\Subset(1-\Theta,\tfrac12).
\tag{1}
\]

Consider an escaping sequence of sufficiently late common positive CA blocks from `RE-040`. On the `n`-th block let `b_n\in J` be a breakpoint of the rightmost adaptive-amplitude fan, and let

\[
C_{-,n}<C_{+,n}
\tag{2}
\]

be the two consecutive **exposed fan states** tied at that breakpoint. They need not be consecutive physical CA states. Write

\[
Y_{\pm,n}:=\log C_{\pm,n},
\qquad
Z_{\pm,n}:=Z_{b_n}(C_{\pm,n}),
\tag{3}
\]

for their adaptive tangent parameters, and put `Y_n:=Y_{-,n}` and `L_n:=\log Y_n`.

Assume that the complete CA event packet from `C_{-,n}` to `C_{+,n}`, counting simultaneous event occurrences with multiplicity, has cardinality bounded by one fixed constant `K`. After passing to a subsequence, assume that its higher-layer occurrences have one fixed nonempty depth multiset

\[
\{j_1,\ldots,j_m\},
\qquad j_i\ge2.
\tag{4}
\]

For the two selected endpoints let `\chi_{\pm,n}\in\{0,1\}` be the ordinary fringe bits of `RE-045`/`RE-059`; when `\chi_{\pm,n}=1`, let `r_{\pm,n}` be the corresponding unmatched ordinary prime. Let `\mathcal R_b(Z)` be the translated nonlinear residual of `RE-060`, normalized so that every genuine selected state satisfies `\mathcal R_b(Z)=o_J(1)`.

Then

\[
\boxed{
\frac{b_n\sqrt{Y_n}}{L_n}
\left(
\mathcal R_{b_n}(Z_{+,n})-
\mathcal R_{b_n}(Z_{-,n})
\right)
=
-\sum_{i=1}^m\frac1{j_i}
+\chi_{+,n}-\chi_{-,n}
+o_J(1).
}
\tag{5}
\]

Equivalently, if `\mathcal P_{\ge2,n}` is the multiset of intervening higher-layer events and

\[
H_{\ge2,n}
:=
\sum_{(p,j)\in\mathcal P_{\ge2,n}}\log p,
\tag{6}
\]

then before converting event bases into depths,

\[
\boxed{
\mathcal R_{b_n}(Z_{+,n})-
\mathcal R_{b_n}(Z_{-,n})
=
\frac{-H_{\ge2,n}
+\chi_{+,n}\log r_{+,n}
-\chi_{-,n}\log r_{-,n}}
{b_n\sqrt{Y_n}}
+o_J\!\left(\frac{L_n}{\sqrt{Y_n}}\right),
}
\tag{7}
\]

with absent fringe terms interpreted as zero.

Because the higher-layer reciprocal-depth sum is positive, the leading coefficient in (5) can vanish only if

\[
\boxed{
\chi_{-,n}=0,
\qquad
\chi_{+,n}=1,
\qquad
\sum_{i=1}^m\frac1{j_i}=1.
}
\tag{8}
\]

Thus every bounded higher-layer packet is asymptotically noncancelling except for a sharply delimited **Egyptian-fraction resonance**. The one-event law of `RE-060` is the case `m=1`: then `1/j_1<1`, so (8) is impossible. The first new resonant pattern is two second-layer events, `1/2+1/2=1`; other examples include `(2,3,6)` and `(3,3,3)`.

## 1. A bounded physical packet forces a logarithmically short tied selector jump

At a fan breakpoint the two exposed states have the same adaptive amplitude. Put

\[
c_n:=A_{b_n}(C_{-,n})=A_{b_n}(C_{+,n}).
\tag{9}
\]

Hence both endpoints lie on the same formal height curve

\[
h_n(Y)=\log(1+c_nY^{-b_n}),
\qquad
a_n(Y):=1-e^{-h_n(Y)}
=\frac{c_nY^{-b_n}}{1+c_nY^{-b_n}}.
\tag{10}
\]

The adaptive tangent is the unique solution of

\[
g(Z)=g(Y)-\frac{b_na_n(Y)}Y,
\qquad
g(x)=\frac1{x\log x}.
\tag{11}
\]

Every physical CA event from `C_-` to `C_+` multiplies the state by its generating prime `p`, so exactly

\[
Y_{+,n}-Y_{-,n}
=
\sum_{e\in\mathcal P_n}\log p_e.
\tag{12}
\]

All event primes belong to the prime support of `C_{+,n}`, whose first-layer frontier is asymptotic to `Y_{+,n}` on the late regular fan. Since `|\mathcal P_n|\le K`, (12) gives

\[
Y_{+,n}-Y_{-,n}=O_K(\log Y_{+,n}).
\tag{13}
\]

Consequently `Y_{+,n}/Y_{-,n}\to1` and we may use `Y_n` as one common physical scale.

The same-amplitude condition gives a stronger fact for the tangent parameters. Differentiate the right side of (11) with `b_n,c_n` fixed. Since

\[
a_n'(Y)=-\frac{b_na_n(Y)(1-a_n(Y))}{Y},
\tag{14}
\]

we obtain

\[
\frac d{dY}\left(g(Y)-\frac{b_na_n(Y)}Y\right)
=
g'(Y)+
\frac{b_na_n(Y)\bigl(1+b_n(1-a_n(Y))\bigr)}{Y^2}.
\tag{15}
\]

`RE-040` gives uniformly on the compact fan

\[
a_n(Y)\log Y\longrightarrow0,
\qquad
Z/Y\longrightarrow1.
\tag{16}
\]

Since

\[
g'(Y)=-\frac{\log Y+1}{Y^2(\log Y)^2},
\tag{17}
\]

the second term of (15) is `o_J(|g'(Y)|)`. Implicit differentiation of (11) therefore yields

\[
\frac{dZ}{dY}=1+o_J(1)
\tag{18}
\]

uniformly across the short interval between the tied endpoints. Combining (13) and (18),

\[
\boxed{
Z_{+,n}-Z_{-,n}
=(1+o_J(1))(Y_{+,n}-Y_{-,n})
=O_K(L_n).
}
\tag{19}
\]

Thus every event in the skipped physical packet lies in one `O_K(log Y)` selector window around a common scale `Y_n`.

## 2. The exact source-separated residual telescopes over the packet

`RE-045` gives, uniformly on the late compact fan, the source-separated form used again in `RE-060`:

\[
\mathcal R_b(Z)
=
-\sqrt2\,\frac{2b-1}{b}
+N(Z)T(C)
+N(Z)\delta_\ell(Z)
-A_b(Z)P(Z)
+A_b(Z)\delta_\vartheta(Z)
+O_J(Z^{-1/2}),
\tag{20}
\]

where

\[
N(Z)=\sqrt Z\log Z,
\qquad
P(Z)=\Phi_{\ge2}(Z),
\tag{21}
\]

and

\[
A_b(Z)
:=
\frac{\Psi'_{b,\log Z}(q_0(Z))}{\sqrt Z}
=
\frac{1-b}{b\sqrt Z}(1+o_J(1)).
\tag{22}
\]

The constant in (20) cancels because both endpoints use the same `b_n`. Across the physical packet,

\[
P(Z_+)-P(Z_-)
=
H_{\ge2,n}
\tag{23}
\]

exactly: first-layer events do not change `P`, while every depth-`j>=2` occurrence contributes `log p`.

The finite-exponent tail also telescopes event by event. A higher-layer event `(p,j)` changes it by

\[
\Delta T=-\lambda_j(p),
\qquad
\lambda_j(p)=g(\eta_j(p))\log p,
\tag{24}
\]

where `\eta_j(p)` is that event coordinate. A first-layer event changes `T` only by

\[
-\log(1-p^{-2})=O(p^{-2}).
\tag{25}
\]

By (19), every intervening event coordinate is `Y_n(1+o_J(1))`. First-layer event primes are therefore `Y_n(1+o_J(1))`, and the bounded number of contributions in (25) is negligible at the `L_n/\sqrt{Y_n}` scale. For the higher layers, (24) gives uniformly

\[
N(Z_- )\lambda_j(p)
=
\frac{\log p}{\sqrt{Y_n}}(1+o_J(1)).
\tag{26}
\]

Hence

\[
N(Z_-)(T_+-T_-)
=
-\frac{H_{\ge2,n}}{\sqrt{Y_n}}(1+o_J(1))
+o_J\!\left(\frac{L_n}{\sqrt{Y_n}}\right).
\tag{27}
\]

The motion of the normalization itself is smaller. From (19),

\[
N(Z_+)-N(Z_-)
=O_K\!\left(\frac{L_n^2}{\sqrt{Y_n}}\right),
\tag{28}
\]

while `RE-036` gives

\[
T(C)=O\!\left(\frac1{\sqrt{Y_n}L_n}\right).
\tag{29}
\]

Thus the extra product from replacing `N(Z_+)` by `N(Z_-)` is `O_K(L_n/Y_n)`, negligible compared with `L_n/\sqrt{Y_n}`.

For the `P` term, the explicit analytic formula for `\Psi'` in `RE-036`, together with the same-amplitude motion (18)--(19), gives

\[
A_{b_n}(Z_+)-A_{b_n}(Z_-)
=O_{J,K}\!\left(\frac{L_n}{Y_n^{3/2}}\right)
+o_J\!\left(\frac{L_n}{Y_n^{3/2}}\right).
\tag{30}
\]

Since `P(Z)=O(\sqrt Z)` by `RE-036`, equations (22), (23), and (30) yield

\[
-\bigl(A_+P_+-A_-P_-\bigr)
=
-\frac{1-b_n}{b_n}
\frac{H_{\ge2,n}}{\sqrt{Y_n}}
+o_J\!\left(\frac{L_n}{\sqrt{Y_n}}\right).
\tag{31}
\]

Combining (27) and (31), the whole interior higher-layer packet contributes

\[
\boxed{
-\frac{H_{\ge2,n}}{b_n\sqrt{Y_n}}
+o_J\!\left(\frac{L_n}{\sqrt{Y_n}}\right).
}
\tag{32}
\]

This is the multi-event version of the unit charge in `RE-060`. Importantly, **interior first-layer events contribute no term of size `log Y/sqrt(Y)`**: their ordinary source jump has already been matched at both selected endpoints, and their Euler-tail increment (25) is much smaller.

## 3. Only two ordinary fringe bits survive at the endpoints

At a selected endpoint `RE-045`/`RE-059` leave at most one unmatched ordinary first-layer prime. If the bit is one, then

\[
\delta_\vartheta(Z)=\log r,
\qquad
\delta_\ell(Z)=-\log(1-r^{-1}),
\tag{33}
\]

and `r\sim Z\sim Y_n`. Therefore

\[
N(Z)\delta_\ell(Z)
=
\frac{\log r}{\sqrt{Y_n}}(1+o_J(1)),
\tag{34}
\]

while (22) gives

\[
A_b(Z)\delta_\vartheta(Z)
=
\frac{1-b}{b}
\frac{\log r}{\sqrt{Y_n}}(1+o_J(1)).
\tag{35}
\]

Their sum is

\[
\boxed{
\frac{\log r}{b\sqrt{Y_n}}(1+o_J(1)).
}
\tag{36}
\]

Subtracting the lower endpoint correction from the upper endpoint correction and combining with (32) proves (7). The `O_J(Y^{-1/2})` remainder in (20) is also negligible because `L_n\to\infty`.

The structural content is now explicit. A skipped physical packet does **not** leave one independent first-layer fringe bit per crossed prime. Every interior ordinary prime is absorbed. No matter how the finite packet is arranged, its leading source-sensitive data are only

\[
H_{\ge2,n},
\qquad
\chi_{-,n},
\qquad
\chi_{+,n}.
\tag{37}
\]

## 4. Fixed layer depths turn total higher-layer mass into an Egyptian fraction

For one fixed depth `j>=2`, the event increment satisfies

\[
\lambda_j(p)
=
p^{-j}(1+O_j(p^{-1}))
\tag{38}
\]

as `p\to\infty`. Since its event coordinate is defined by

\[
g(\eta_j(p))=\frac{\lambda_j(p)}{\log p},
\tag{39}
\]

we have

\[
\eta_j(p)\log\eta_j(p)
=
\frac{\log p}{\lambda_j(p)}
=p^j\log p\,(1+o_j(1)).
\tag{40}
\]

Taking logarithms gives

\[
\frac{\log p}{\log\eta_j(p)}
\longrightarrow\frac1j.
\tag{41}
\]

Every event in the bounded packet has `\eta_j(p)=Y_n(1+o_J(1))` by (19). Therefore each fixed higher-layer occurrence in (4) satisfies

\[
\frac{\log p_i}{L_n}
\longrightarrow\frac1{j_i},
\tag{42}
\]

and hence

\[
\boxed{
\frac{H_{\ge2,n}}{L_n}
\longrightarrow
\sum_{i=1}^m\frac1{j_i}.
}
\tag{43}
\]

Similarly `r_{\pm,n}\sim Y_n` whenever the corresponding bit is one, so

\[
\frac{\log r_{\pm,n}}{L_n}\longrightarrow1.
\tag{44}
\]

Divide (7) by `L_n/(b_n\sqrt{Y_n})`; equations (43)--(44) prove (5).

Since `\chi_+-\chi_-\in\{-1,0,1\}` and the sum in (43) is strictly positive, equality of the leading coefficient to zero requires `\chi_+-\chi_-=1` and the reciprocal-depth sum to equal one. This proves (8).

The resonance is arithmetic but very specific: it depends only on the **layer depths** of the skipped higher-layer events, not on their prime bases. For example,

\[
\frac12+\frac12=1,
\qquad
\frac12+\frac13+\frac16=1,
\qquad
\frac13+\frac13+\frac13=1.
\tag{45}
\]

Such identities show why the one-event noncancellation of `RE-060` cannot simply be summed naively into a theorem saying that every multi-event fan switch is noncancelling.

## 5. What this settles and what remains open

Equation (5) answers the first finite-packet composition problem left by `RE-060`. **A bounded nonadjacent fan switch has only one leading higher-layer charge, equal to the sum of reciprocal event depths, and at most one unit of ordinary endpoint compensation.** Generic depth packets therefore retain a nonzero normalized charge; the complete leading cancellation locus is the Egyptian-fraction condition (8).

This still does not contradict the uniform selected residual law of `RE-040`. The physical increment in (7) is only `O(log Y/sqrt(Y))`, which tends to zero even when its normalized coefficient in (5) is nonzero. The theorem instead narrows what a global contradiction must use. There are now three distinct escapes: fan switches may cross unboundedly many physical events, bounded packets may repeatedly land on the resonant depth condition (8), or nonzero packet charges may alternate so that no stronger global statistic accumulates them.

The result also explains why first-layer complexity by itself is not the right counting variable. A bounded packet may contain several ordinary prime events, yet all of them are invisible at leading selected-residual scale once they are interior. What matters is the higher-layer depth multiset plus the two boundary fringe bits. A useful continuation is therefore to control the **depth spectrum of physical packets skipped by consecutive exposed fan states**, rather than merely the number of CA states or first-layer events between them.

One promising target is to show that, on a positive proportion of fan switches forced by `RE-051` in the strongly off-critical regime, the skipped packet is bounded and has reciprocal-depth mass separated from one. A different route is to prove that resonant packets such as `(2,2)` cannot repeatedly align with the unique endpoint fringe pattern `0 -> 1`. Either statement would convert the local source charge into a recurring obstruction. Without such an additional theorem, (5) is a structural composition law, not an RH proof.

## 6. Prior-art boundary

A targeted current search of colossally abundant transition packets, Robin counterexamples, higher prime-power layers, and Egyptian-fraction formulations found no external result matching (5) or (8). Mantovanelli's 2026 prime-layer workload is the closest prior art for exact CA event packets and packet-mass bookkeeping; Zimov's 2025 work is neighboring prior art for prime/semiprime consecutive CA quotients. Both are already anchored in `SOURCES.md`. Neither source studies the adaptive false-RH fan residual of `RE-036`--`RE-060` or the reciprocal-depth cancellation law above.

No novelty is claimed for the CA event decomposition, for the asymptotic event scale `eta_j(p)`, or for ordinary Egyptian-fraction identities. The line-specific delta is their combination with the selected nonlinear standard/reciprocal residual: equations (5)--(8) classify the leading cancellation of a finite physical packet between consecutive exposed adaptive fan states. No new external theorem is load-bearing, so `SOURCES.md` requires no change.